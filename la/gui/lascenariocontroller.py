"""
lascenariocontroller.py — the one object that owns the scenario state.

The settings dock, results dock and map tool all talk to a
:class:`LaScenarioController`; none of them touch :class:`LaModel`
directly. The controller:

* holds the ``LaModel`` and the crop/animal selections,
* recomputes the diet (debounced) whenever an input changes and emits
  :attr:`dietChanged` so the donut and summary stay live,
* knows whether a run is possible (:meth:`readiness`) and why not,
* runs the full calculation, launches the catchment ``QgsTask`` and
  relays its progress,
* renders / exports the report.

This is the logic formerly spread over ``LaMainForm.on_pushButtonRun_clicked``,
``_configureGisInputsFromUi``, ``_launchCatchmentTask`` and the export slots.
"""

import json
import os
from typing import Dict, List, Optional, Tuple

from qgis.PyQt.QtCore import QObject, QTimer, pyqtSignal
from qgis.core import QgsSettings

from la.lib.la import AreaUnits, EnergyType
from la.lib.lacatalogue import LaCatalogue
from la.lib.lacatchment import DistanceMethod, LaCatchmentInputs, LaCatchmentResults, SearchStatus
from la.lib.ladietlabels import LaDietLabels
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils
from la.lib import lascenarioio

_PERCENT_TOLERANCE = 0.1
_LIVE_RECALC_DELAY_MS = 150


class LaScenarioController(QObject):
    """
    Owns the scenario (``LaModel`` + selections) and drives calculations.

    :signal settingsChanged: any input changed (used for the live summary line).
    :signal selectionChanged: crop/animal selection or parameter choice changed.
    :signal readinessChanged(bool, str): whether Calculate may run, and why not.
    :signal dietChanged(object): fresh ``LaDietLabels`` after a (live) diet calc, or None.
    :signal calculationFinished(str): full calculation done; argument is the method label.
    :signal calculationFailed(str): the diet calculation raised; argument is the message.
    :signal catchmentStarted(): a catchment task was submitted.
    :signal catchmentProgress(int, int, int): items done, iteration, max iterations.
    :signal catchmentMessage(str): log line from the catchment pipeline.
    :signal catchmentFinished(bool, str): task ended; success flag and summary text.
    :signal modelReplaced(): a new LaModel was installed (reset / load); panels must reload.
    """

    settingsChanged      = pyqtSignal()
    selectionChanged     = pyqtSignal()
    readinessChanged     = pyqtSignal(bool, str)
    dietChanged          = pyqtSignal(object)
    calculationFinished  = pyqtSignal(str)
    calculationFailed    = pyqtSignal(str)
    catchmentStarted     = pyqtSignal()
    catchmentProgress    = pyqtSignal(int, int, int)
    catchmentMessage     = pyqtSignal(str)
    catchmentFinished    = pyqtSignal(bool, str)
    modelReplaced        = pyqtSignal()
    recentScenariosChanged = pyqtSignal()

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.mModel = LaModel()
        self.mCatalogue = LaCatalogue(self)
        self.mSelectedCrops: Dict[str, str] = {}     # cropGuid -> cropParameterGuid
        self.mSelectedAnimals: Dict[str, str] = {}   # animalGuid -> animalParameterGuid
        self.mGisInputs: Optional[LaCatchmentInputs] = None
        self.mLivePreview = True
        self.mLastLabels: Optional[LaDietLabels] = None
        self.mLastCalculationType = ""
        self.mLastCatchmentResults: Optional[LaCatchmentResults] = None
        self._mCatchmentTask = None
        self.mScenarioPath: Optional[str] = None
        self.mPluginBlockProvider = None      # callable() -> dict, set by the settings dock
        self.mPendingPluginBlock: Dict = {}  # plugin block of the last loaded file, for the dock to apply
        self._mRecalcTimer = QTimer(self)
        self._mRecalcTimer.setSingleShot(True)
        self._mRecalcTimer.setInterval(_LIVE_RECALC_DELAY_MS)
        self._mRecalcTimer.timeout.connect(self._onRecalcTimer)
        self.mCatalogue.changed.connect(self._onCatalogueChanged)
        # Defaults matching the thesis validation scenario so a fresh dock
        # produces sensible numbers immediately.
        self.mModel.mDietPercent = 10
        self.mModel.mMeatPercent = 99
        self.mModel.mPercentOfDietThatIsFromCrops = 90
        self.mModel.mCaloriesPerPersonDaily = 2500
        self.mModel.mDairyUtilisation = 0
        self.mModel.mIncludeDairy = False
        self.mModel.mLimitDairy = False
        self.mModel.mLimitDairyPercentage = 10
        self.mModel.mBaseOnPlants = False
        self.mModel.mPopulation = 100

    def resetToDefaults(self) -> None:
        """Fresh model with the thesis-validation defaults and no selections."""
        self._mRecalcTimer.stop()
        self.mModel = LaModel()
        self.mModel.mDietPercent = 10
        self.mModel.mMeatPercent = 99
        self.mModel.mPercentOfDietThatIsFromCrops = 90
        self.mModel.mCaloriesPerPersonDaily = 2500
        self.mModel.mDairyUtilisation = 0
        self.mModel.mIncludeDairy = False
        self.mModel.mLimitDairy = False
        self.mModel.mLimitDairyPercentage = 10
        self.mModel.mBaseOnPlants = False
        self.mModel.mPopulation = 100
        self.mSelectedCrops.clear()
        self.mSelectedAnimals.clear()
        self.mLastLabels = None
        self.mLastCatchmentResults = None
        self.mScenarioPath = None
        self.mPendingPluginBlock = {}
        self.modelReplaced.emit()
        self.selectionChanged.emit()
        self._touched()
        self.dietChanged.emit(None)

    # ------------------------------------------------------------------
    # Scenario inputs (each schedules a live recalculation)
    # ------------------------------------------------------------------
    def _touched(self) -> None:
        self.settingsChanged.emit()
        self._emitReadiness()
        if self.mLivePreview:
            self._mRecalcTimer.start()

    def setScenarioName(self, theName: str) -> None:
        self.mModel.mName = str(theName)
        self.settingsChanged.emit()

    def setPeriod(self, thePeriod: str) -> None:
        self.mModel.mPeriod = str(thePeriod)
        self.settingsChanged.emit()

    def setPopulation(self, thePopulation: int) -> None:
        self.mModel.mPopulation = int(thePopulation)
        self._touched()

    def setCaloriesPerPersonDaily(self, theCalories: int) -> None:
        self.mModel.mCaloriesPerPersonDaily = int(theCalories)
        self._touched()

    def setAnimalShareOfDiet(self, thePercent: int) -> None:
        """Share of all calories that comes from animals (meat + dairy). ``mDietPercent``."""
        self.mModel.mDietPercent = int(thePercent)
        self._touched()

    def setTameMeatPercent(self, thePercent: int) -> None:
        """Share of the meat calories that comes from domestic animals. ``mMeatPercent``."""
        self.mModel.mMeatPercent = int(thePercent)
        self._touched()

    def setDomesticCropPercent(self, thePercent: int) -> None:
        """Share of the plant calories that comes from domestic crops."""
        self.mModel.mPercentOfDietThatIsFromCrops = int(thePercent)
        self._touched()

    def setDairyUtilisation(self, thePercent: int) -> None:
        self.mModel.mDairyUtilisation = int(thePercent)
        self._touched()

    def setIncludeDairy(self, theFlag: bool) -> None:
        self.mModel.mIncludeDairy = bool(theFlag)
        self._touched()

    def setLimitDairy(self, theFlag: bool) -> None:
        self.mModel.mLimitDairy = bool(theFlag)
        self._touched()

    def setLimitDairyPercent(self, thePercent: int) -> None:
        self.mModel.mLimitDairyPercentage = int(thePercent)
        self._touched()

    def setBaseOnPlants(self, theFlag: bool) -> None:
        self.mModel.mBaseOnPlants = bool(theFlag)
        self._touched()

    def setPrecision(self, thePercent: int) -> None:
        self.mModel.mPrecision = max(1, int(thePercent))
        self.settingsChanged.emit()

    def setSettlement(self, theEasting: float, theNorthing: float, theEpsg: int = 0) -> None:
        self.mModel.mEasting = int(round(theEasting))
        self.mModel.mNorthing = int(round(theNorthing))
        if theEpsg:
            self.mModel.mProjection = int(theEpsg)
        self.settingsChanged.emit()

    def setCommonLandValue(self, theValue: float, theAreaUnits: AreaUnits) -> None:
        self.mModel.setCommonLandValue(theValue, theAreaUnits)
        self._touched()

    def setSpecificLandEnergyType(self, theEnergyType: EnergyType) -> None:
        self.mModel.mSpecificLandEnergyType = theEnergyType
        self._touched()

    def setLivePreview(self, theFlag: bool) -> None:
        self.mLivePreview = bool(theFlag)
        if self.mLivePreview:
            self._mRecalcTimer.start()

    # ------------------------------------------------------------------
    # Selections
    # ------------------------------------------------------------------
    def setCropSelected(self, theCropGuid: str, theSelected: bool, theParameterGuid: str = "") -> None:
        """Select/deselect a crop; picks the first parameter set when none is given."""
        if theSelected:
            myParameterGuid = theParameterGuid or self.mSelectedCrops.get(theCropGuid, "")
            if not myParameterGuid:
                myParameters = self.mCatalogue.cropParametersFor(theCropGuid)
                myParameterGuid = next(iter(myParameters), "")
            self.mSelectedCrops[theCropGuid] = myParameterGuid
        else:
            self.mSelectedCrops.pop(theCropGuid, None)
        self.selectionChanged.emit()
        self._touched()

    def setCropParameter(self, theCropGuid: str, theParameterGuid: str) -> None:
        if theCropGuid in self.mSelectedCrops:
            self.mSelectedCrops[theCropGuid] = theParameterGuid
            self.selectionChanged.emit()
            self._touched()

    def setAnimalSelected(self, theAnimalGuid: str, theSelected: bool, theParameterGuid: str = "") -> None:
        if theSelected:
            myParameterGuid = theParameterGuid or self.mSelectedAnimals.get(theAnimalGuid, "")
            if not myParameterGuid:
                myParameters = self.mCatalogue.animalParametersFor(theAnimalGuid)
                myParameterGuid = next(iter(myParameters), "")
            self.mSelectedAnimals[theAnimalGuid] = myParameterGuid
        else:
            self.mSelectedAnimals.pop(theAnimalGuid, None)
        self.selectionChanged.emit()
        self._touched()

    def setAnimalParameter(self, theAnimalGuid: str, theParameterGuid: str) -> None:
        if theAnimalGuid in self.mSelectedAnimals:
            self.mSelectedAnimals[theAnimalGuid] = theParameterGuid
            self.selectionChanged.emit()
            self._touched()

    def selectAll(self) -> None:
        """Select every crop and animal that has at least one parameter set (thesis default)."""
        for myCropGuid in self.mCatalogue.crops():
            if self.mCatalogue.cropParametersFor(myCropGuid):
                self.mSelectedCrops.setdefault(
                    myCropGuid, next(iter(self.mCatalogue.cropParametersFor(myCropGuid)))
                )
        for myAnimalGuid in self.mCatalogue.animals():
            if self.mCatalogue.animalParametersFor(myAnimalGuid):
                self.mSelectedAnimals.setdefault(
                    myAnimalGuid, next(iter(self.mCatalogue.animalParametersFor(myAnimalGuid)))
                )
        self.selectionChanged.emit()
        self._touched()

    def percentTotals(self) -> Tuple[float, float]:
        """(sum of percentTameCrop over selected crops, sum of percentTameMeat over selected animals)."""
        myCropTotal = 0.0
        for myParameterGuid in self.mSelectedCrops.values():
            myParameter = self.mCatalogue.cropParameter(myParameterGuid) if myParameterGuid else None
            myCropTotal += float(getattr(myParameter, "percentTameCrop", 0.0) or 0.0)
        myAnimalTotal = 0.0
        for myParameterGuid in self.mSelectedAnimals.values():
            myParameter = self.mCatalogue.animalParameter(myParameterGuid) if myParameterGuid else None
            myAnimalTotal += float(getattr(myParameter, "percentTameMeat", 0.0) or 0.0)
        return myCropTotal, myAnimalTotal

    # ------------------------------------------------------------------
    # Readiness
    # ------------------------------------------------------------------
    def readiness(self) -> Tuple[bool, str]:
        """Whether a calculation can run, and a one-line reason when it cannot."""
        if self.mModel.mPopulation <= 0:
            return False, "Population must be at least 1."
        if self.mModel.mCaloriesPerPersonDaily <= 0:
            return False, "Daily calories per person must be positive."
        if not self.mSelectedCrops and not self.mSelectedAnimals:
            return False, "Select at least one crop or animal."
        if any(not g for g in self.mSelectedCrops.values()):
            return False, "A selected crop has no parameter set — create one in the crop parameter manager."
        if any(not g for g in self.mSelectedAnimals.values()):
            return False, "A selected animal has no parameter set — create one in the animal parameter manager."
        myCropTotal, myAnimalTotal = self.percentTotals()
        if self.mSelectedCrops and abs(myCropTotal - 100.0) > _PERCENT_TOLERANCE:
            return False, f"Crop shares sum to {myCropTotal:.1f} %, they must total 100 %."
        if self.mSelectedAnimals and abs(myAnimalTotal - 100.0) > _PERCENT_TOLERANCE:
            return False, f"Animal shares sum to {myAnimalTotal:.1f} %, they must total 100 %."
        return True, ""

    def _emitReadiness(self) -> None:
        myReady, myReason = self.readiness()
        self.readinessChanged.emit(myReady, myReason)

    # ------------------------------------------------------------------
    # Calculation
    # ------------------------------------------------------------------
    def calculationTypeLabel(self) -> str:
        myDairy = "Include Dairy" if self.mModel.mIncludeDairy else "Dairy Separate"
        if self.mModel.mBaseOnPlants:
            return f"Plants First ({myDairy}) — not implemented, Animals First used"
        return f"Animals First ({myDairy})"

    def _applySelectionsToModel(self) -> None:
        self.mModel.mCropsMap = dict(self.mSelectedCrops)
        self.mModel.mAnimalsMap = dict(self.mSelectedAnimals)

    def runDietCalc(self) -> Optional[LaDietLabels]:
        """
        Run the diet/herd calculation for the current inputs.

        Emits :attr:`dietChanged` with the labels (or None when the inputs are
        not ready). Returns the labels.
        """
        myReady, _ = self.readiness()
        self._emitReadiness()
        if not myReady:
            self.mLastLabels = None
            self.dietChanged.emit(None)
            return None
        self._applySelectionsToModel()
        try:
            if self.mModel.mIncludeDairy:
                myLabels = (self.mModel.doCalcsPlantsFirstIncludeDairy() if self.mModel.mBaseOnPlants
                            else self.mModel.doCalcsAnimalsFirstIncludeDairy())
            else:
                myLabels = (self.mModel.doCalcsPlantsFirstDairySeparate() if self.mModel.mBaseOnPlants
                            else self.mModel.doCalcsAnimalsFirstDairySeparate())
        except Exception as e:
            LaUtils.debug.log(f"Diet calculation failed: {e}", "Error")
            self.calculationFailed.emit(str(e))
            self.mLastLabels = None
            self.dietChanged.emit(None)
            return None
        self.mModel.mDietLabels = myLabels
        self.mLastLabels = myLabels
        self.mLastCalculationType = self.calculationTypeLabel()
        self.dietChanged.emit(myLabels)
        return myLabels

    def _onRecalcTimer(self) -> None:
        self.runDietCalc()

    def _onCatalogueChanged(self) -> None:
        # Drop selections whose parameter set vanished; keep the rest.
        myCropParameters = self.mCatalogue.cropParameters()
        myAnimalParameters = self.mCatalogue.animalParameters()
        for myGuid, myParameterGuid in list(self.mSelectedCrops.items()):
            if myParameterGuid and myParameterGuid not in myCropParameters:
                self.mSelectedCrops[myGuid] = next(iter(self.mCatalogue.cropParametersFor(myGuid)), "")
        for myGuid, myParameterGuid in list(self.mSelectedAnimals.items()):
            if myParameterGuid and myParameterGuid not in myAnimalParameters:
                self.mSelectedAnimals[myGuid] = next(iter(self.mCatalogue.animalParametersFor(myGuid)), "")
        self.selectionChanged.emit()
        self._touched()

    def runFullCalculation(self) -> bool:
        """
        Diet calculation followed (if GIS inputs are set) by the catchment task.

        :return: True when the diet calculation succeeded.
        """
        self._mRecalcTimer.stop()
        myLabels = self.runDietCalc()
        if myLabels is None:
            return False
        self.calculationFinished.emit(self.mLastCalculationType)
        if self.mGisInputs is not None:
            self.launchCatchment()
        return True

    # ------------------------------------------------------------------
    # Catchment
    # ------------------------------------------------------------------
    def setGisInputs(self, theInputs: Optional[LaCatchmentInputs]) -> None:
        self.mGisInputs = theInputs
        self.settingsChanged.emit()

    @staticmethod
    def catchmentAvailability(theInputs: LaCatchmentInputs) -> Optional[str]:
        """
        None when the requested method can run here, else a user-facing reason.

        Walking time has a pure-Python engine (needs scipy) with GRASS r.walk
        as the alternative; Euclidean still needs GRASS r.cost until the
        pure-Python port lands.
        """
        from la.lib.lagrassprocesslib import LaGrassProcessLib

        if theInputs.method is DistanceMethod.PathDistance:
            return "Path Distance is not implemented yet. Choose Walking Time or Euclidean."
        try:
            import scipy  # noqa: F401
            return None   # the pure-Python engine handles both methods (heap fallback ≤ 512² without scipy)
        except ImportError:
            pass
        myGrassId = (LaGrassProcessLib.walkAlgorithmId() if theInputs.method is DistanceMethod.WalkingTime
                     else LaGrassProcessLib.costAlgorithmId())
        if myGrassId is not None:
            return None
        return ("Catchment cost surfaces need scipy in the QGIS Python (python -m pip install scipy) "
                "for windows larger than 512×512 cells, or the GRASS Processing provider. Small "
                "windows still run without either; larger ones will stop with an install message.")

    def launchCatchment(self) -> bool:
        """Submit the catchment task to the QGIS task manager. Returns True when submitted."""
        from qgis.core import QgsApplication
        from la.gui.lacatchmenttask import LaCatchmentTask

        if self.mGisInputs is None:
            return False
        myProblem = self.catchmentAvailability(self.mGisInputs)
        if myProblem:
            self.catchmentFinished.emit(False, myProblem)
            return False
        if self._mCatchmentTask is not None:
            self.cancelCatchment()

        myTask = LaCatchmentTask(self.mModel, self.mGisInputs)
        myTask.grassMessage.connect(self.catchmentMessage)
        myTask.overallProgress.connect(lambda done, _total: self.catchmentProgress.emit(done, 0, 0))
        myTask.targetProgress.connect(lambda it, mx: self.catchmentProgress.emit(-1, it, mx))
        myTask.completed.connect(self._onCatchmentCompleted)
        myTask.failed.connect(self._onCatchmentTerminated)
        myTask.taskTerminated.connect(lambda: self._onCatchmentTerminated(""))
        self._mCatchmentTask = myTask
        QgsApplication.taskManager().addTask(myTask)
        self.catchmentStarted.emit()
        LaUtils.debug.log("Catchment task submitted to QGIS task manager.", "Setup")
        return True

    def cancelCatchment(self) -> None:
        if self._mCatchmentTask is not None:
            try:
                self._mCatchmentTask.cancel()
            except RuntimeError:  # task already deleted by the manager
                pass

    def _onCatchmentCompleted(self, theResults) -> None:
        self._mCatchmentTask = None
        self.mLastCatchmentResults = theResults
        myItems = getattr(theResults, "items", []) or []
        myConverged = sum(1 for i in myItems if getattr(i, "status", None) is SearchStatus.Converged)
        self.catchmentFinished.emit(
            True, f"Catchment analysis complete: {myConverged}/{len(myItems)} item(s) converged.")

    def _onCatchmentTerminated(self, theText: str = "") -> None:
        if self._mCatchmentTask is None:
            return  # already reported through completed/failed
        self._mCatchmentTask = None
        self.catchmentFinished.emit(False, theText or "Catchment analysis was cancelled or failed.")

    # ------------------------------------------------------------------
    # Scenario files (*.lascenario.json)
    # ------------------------------------------------------------------
    _RECENT_KEY = "landuseAnalyst/recentScenarios"
    _RECENT_MAX = 10

    def scenarioDocument(self, theIncludeResults: bool = True) -> Dict:
        """Current scenario as an interchange document (see :mod:`la.lib.lascenarioio`)."""
        myPluginBlock = {}
        if callable(self.mPluginBlockProvider):
            try:
                myPluginBlock = dict(self.mPluginBlockProvider() or {})
            except Exception as e:  # never let a UI hiccup block saving
                LaUtils.debug.log(f"Plugin block provider failed: {e}", "Warning")
        myResults = lascenarioio.resultsBlock(self.mModel, self.mLastCalculationType) if theIncludeResults else None
        return lascenarioio.toDict(self.mModel, self.mSelectedCrops, self.mSelectedAnimals, myPluginBlock, myResults)

    def saveScenario(self, thePath: str) -> str:
        """Write the scenario to ``thePath`` and remember it. Returns the path written."""
        myPath = lascenarioio.saveFile(thePath, self.scenarioDocument())
        self.mScenarioPath = myPath
        self._rememberRecent(myPath)
        self.settingsChanged.emit()
        return myPath

    def loadScenarioDocument(self, theDocument: Dict) -> None:
        """Replace the model and selections with ``theDocument`` and notify the panels."""
        self._mRecalcTimer.stop()
        myModel, myCrops, myAnimals, myPluginBlock = lascenarioio.fromDict(theDocument)
        self.mModel = myModel
        self.mSelectedCrops = dict(myCrops)
        self.mSelectedAnimals = dict(myAnimals)
        self.mLastLabels = None
        self.mLastCatchmentResults = None
        self.mPendingPluginBlock = dict(myPluginBlock)
        self.modelReplaced.emit()
        self.selectionChanged.emit()
        self._touched()
        if not self.mLivePreview:
            self.dietChanged.emit(None)

    def loadScenario(self, thePath: str) -> None:
        self.loadScenarioDocument(lascenarioio.loadFile(thePath))
        self.mScenarioPath = thePath
        self._rememberRecent(thePath)

    def recentScenarios(self) -> List[str]:
        myValue = QgsSettings().value(self._RECENT_KEY, [])
        if isinstance(myValue, str):
            myValue = [myValue] if myValue else []
        return [p for p in (myValue or []) if isinstance(p, str) and os.path.exists(p)]

    def _rememberRecent(self, thePath: str) -> None:
        myRecent = [p for p in self.recentScenarios() if p != thePath]
        myRecent.insert(0, thePath)
        QgsSettings().setValue(self._RECENT_KEY, myRecent[: self._RECENT_MAX])
        self.recentScenariosChanged.emit()

    # ------------------------------------------------------------------
    # Reports and exports
    # ------------------------------------------------------------------
    def hasResults(self) -> bool:
        return self.mLastLabels is not None

    def reportHtml(self, theIncludeCharts: bool = False) -> str:
        """Scenario header, diet summary, selections and the six target tables."""
        from la.lib import lareports

        if not self.hasResults():
            return "<p>No results yet. Set up the scenario and press Calculate.</p>"
        return (
            '<h1 style="color:#3B5A8C; margin-bottom:4px;">Landuse Analyst Calculation Results</h1>'
            f'<p style="color:#666; font-style:italic; margin-top:0;">'
            f'Calculation Method: {self.mLastCalculationType}</p>'
            + lareports.toHtml(self.mModel, theIncludeCharts=theIncludeCharts)
            + lareports.toHtmlCalorieCropTargets(self.mModel)
            + lareports.toHtmlCalorieAnimalTargets(self.mModel)
            + lareports.toHtmlProductionCropTargets(self.mModel)
            + lareports.toHtmlProductionAnimalTargets(self.mModel)
            + lareports.toHtmlAreaCropTargets(self.mModel)
            + lareports.toHtmlAreaAnimalTargets(self.mModel)
        )

    def chartsHtml(self) -> str:
        from la.lib import lareports

        if not self.hasResults():
            return "<p>No results yet.</p>"
        try:
            return (lareports._dietCompositionPanel(self.mModel)
                    + lareports.toHtmlHectaresLand(self.mModel)
                    + lareports.toHtmlHerdCharts(self.mModel))
        except Exception as e:  # matplotlib missing or a chart failing must not kill the dock
            LaUtils.debug.log(f"Chart rendering failed: {e}", "Error")
            return f"<p>Charts unavailable: {e}</p>"

    def tablesHtml(self) -> str:
        from la.lib import lareports

        if not self.hasResults():
            return "<p>No results yet.</p>"
        return (
            lareports.toHtmlMCalorieContributions(self.mModel)
            + lareports.toHtmlCalorieCropTargets(self.mModel)
            + lareports.toHtmlCalorieAnimalTargets(self.mModel)
            + lareports.toHtmlProductionCropTargets(self.mModel)
            + lareports.toHtmlProductionAnimalTargets(self.mModel)
            + lareports.toHtmlAreaCropTargets(self.mModel)
            + lareports.toHtmlAreaAnimalTargets(self.mModel)
        )

    def fullReportHtml(self) -> str:
        from la.lib import lareports
        return lareports.buildFullReportHtml(self.mModel, theCalculationType=self.mLastCalculationType)

    def reportDict(self) -> Dict:
        from la.lib import lareports
        return lareports.toDict(self.mModel)

    def reportJson(self) -> str:
        return json.dumps(self.reportDict(), indent=2, ensure_ascii=False)

    def defaultExportFilename(self, theExt: str) -> str:
        myName = self.mModel.mName or "landuse_analyst_report"
        mySafe = "".join(c if c.isalnum() or c in "-_." else "_" for c in str(myName))
        return os.path.join(os.path.expanduser("~"), f"{mySafe}.{theExt}")

    def exportJson(self, thePath: str) -> None:
        with open(thePath, "w", encoding="utf-8") as myFile:
            myFile.write(self.reportJson())
        LaUtils.debug.log(f"Exported report data JSON to {thePath}", "Setup")

    def exportPdf(self, thePath: str) -> None:
        from qgis.PyQt.QtGui import QTextDocument
        from qgis.PyQt.QtPrintSupport import QPrinter

        myDocument = QTextDocument()
        myDocument.setHtml(self.fullReportHtml())
        myPrinter = QPrinter(QPrinter.HighResolution)
        myPrinter.setOutputFormat(QPrinter.PdfFormat)
        myPrinter.setOutputFileName(thePath)
        myDocument.print_(myPrinter)
        LaUtils.debug.log(f"Exported report PDF to {thePath}", "Setup")
