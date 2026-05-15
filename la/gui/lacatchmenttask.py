"""
lacatchmenttask.py — QgsTask wrapper for the catchment-analysis pipeline.

Runs :class:`la.lib.lacatchment.LaCatchment.runCatchmentAnalysis` off the
UI thread so the QGIS main window stays responsive during the 17-iter
binary search × N items workload. On completion (main thread) it adds
each output raster to the QGIS canvas inside a "Catchment Analysis"
layer group, with a sensible default style applied.

Signal flow::

    LaGrass        -- message  -->  LaCatchment.logged
    LaCatchment    -- logged   -->  LaCatchmentTask.grassMessage
    LaCatchment    -- progress -->  LaCatchmentTask.overallProgress + targetProgress
    LaCatchmentTask.{overall,target}Progress + grassMessage -->  LaMainForm progress + log widgets
"""

import os
import time
from typing import Optional

from qgis.PyQt.QtCore import pyqtSignal
from qgis.core import (
    QgsTask,
    QgsProject,
    QgsRasterLayer,
    QgsLayerTreeGroup,
    QgsApplication,
)

from la.lib.lautils import LaUtils
from la.lib.lagrass import LaGrass, LaGrassError
from la.lib.lacatchment import (
    LaCatchment,
    LaCatchmentInputs,
    LaCatchmentResults,
    AnalyseResult,
    SearchStatus,
    LaGisInputError,
)


_GROUP_NAME = "Catchment Analysis"
_QML_STYLE  = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),  # la/
    "resources", "styles", "catchment_mask.qml",
)


class LaCatchmentTask(QgsTask):
    """
    Background runner for :meth:`LaCatchment.runCatchmentAnalysis`.

    :ivar mModel:      The ``LaModel`` instance the diet calc was run on.
    :ivar mInputs:     :class:`LaCatchmentInputs` with layer ids + method.
    :ivar mResults:    Populated in :meth:`run` on success; consumed by
                       :meth:`finished` on the main thread.
    :ivar mErrorText:  Populated on exception, surfaced to the user.
    """

    overallProgress = pyqtSignal(int, int)
    targetProgress  = pyqtSignal(int, int)
    grassMessage    = pyqtSignal(str)

    def __init__(self, theModel, theInputs: LaCatchmentInputs) -> None:
        """
        :param theModel: The ``LaModel`` with diet calc already populated.
        :type theModel: la.lib.lamodel.LaModel
        :param theInputs: GIS-only runtime handles (layer ids + method).
        :type theInputs: la.lib.lacatchment.LaCatchmentInputs
        """
        super().__init__("Landuse Analyst — Catchment Analysis", QgsTask.CanCancel)
        self.mModel:    "LaModel" = theModel
        self.mInputs:   LaCatchmentInputs = theInputs
        self.mResults:  Optional[LaCatchmentResults] = None
        self.mErrorText: Optional[str] = None
        self._mScratchDir: str = self._buildScratchDir()
        # Held off-main-thread so we can cleanup on cancel
        self._mGrass:   Optional[LaGrass]      = None
        self._mCatchment: Optional[LaCatchment] = None

    # ------------------------------------------------------------------
    # Worker thread
    # ------------------------------------------------------------------
    def run(self) -> bool:
        """
        Worker-thread entry point.

        Resolves the DEM layer, instantiates :class:`LaGrass` and
        :class:`LaCatchment`, hooks their signals into ours, and calls
        :meth:`LaCatchment.runCatchmentAnalysis`.

        :return: True on success (including non-converged items, which are
            still useful output); False on hard failure (DEM missing,
            algorithm unavailable, etc.).
        """
        try:
            myDem = self._resolveLayer(self.mInputs.demLayerId, "DEM")
            if myDem is None:
                self.mErrorText = (
                    f"DEM layer ({self.mInputs.demLayerId}) is not loaded in "
                    "the current project."
                )
                return False
            self._mGrass = LaGrass(myDem, self._mScratchDir)
            self._mCatchment = LaCatchment(
                self._mGrass, thePrecisionPct=self._modelPrecision()
            )
            self._mCatchment.logged.connect(self._onLogged)
            self._mCatchment.progress.connect(self._onProgress)

            self.mResults = self._mCatchment.runCatchmentAnalysis(
                self.mModel, self.mInputs, theIsCanceledFn=self.isCanceled,
            )
            return True
        except LaGisInputError as e:
            self.mErrorText = str(e)
            return False
        except LaGrassError as e:
            self.mErrorText = f"GRASS call failed: {e}"
            return False
        except Exception as e:
            import traceback
            self.mErrorText = f"Unexpected error: {e}\n\n{traceback.format_exc()}"
            return False

    # ------------------------------------------------------------------
    # Main thread (after worker returns)
    # ------------------------------------------------------------------
    def finished(self, theResult: bool) -> None:
        """
        Called on the main thread after :meth:`run`.

        On success: add each output raster to a "Catchment Analysis" layer
        group inside the project's layer tree, with a default mask style.

        On failure: log the error; the main form's ``grassMessage``
        connection will already have surfaced log messages to the user.
        """
        if not theResult:
            myMsg = self.mErrorText or "Catchment analysis did not complete."
            LaUtils.debug.log(f"Catchment task failed: {myMsg}", "Error")
            self.grassMessage.emit(f"[FAILED] {myMsg}")
            return
        if self.mResults is None:
            return

        myProject = QgsProject.instance()
        myRoot = myProject.layerTreeRoot()
        myGroup = myRoot.findGroup(_GROUP_NAME)
        if myGroup is None:
            myGroup = myRoot.insertGroup(0, _GROUP_NAME)
        myRunGroup = myGroup.addGroup(self._runGroupName())

        # Cost surface first — semi-transparent gradient via default renderer
        if self.mResults.costRasterPath:
            myCostLayer = QgsRasterLayer(
                self.mResults.costRasterPath, "Cost surface"
            )
            if myCostLayer.isValid():
                myProject.addMapLayer(myCostLayer, False)
                myRunGroup.addLayer(myCostLayer)
                myCostLayer.setOpacity(0.55)

        # Then the per-item masks, with the catchment-mask style if it exists
        for myItem in self.mResults.items:
            if myItem.outputPath is None or myItem.status is SearchStatus.Skipped:
                continue
            myLayer = QgsRasterLayer(myItem.outputPath, self._layerName(myItem))
            if not myLayer.isValid():
                self.grassMessage.emit(
                    f"[WARN] Could not load output for {myItem.itemName}: "
                    f"{myItem.outputPath}"
                )
                continue
            myProject.addMapLayer(myLayer, False)
            myRunGroup.addLayer(myLayer)
            self._applyMaskStyle(myLayer)

        self.grassMessage.emit(
            f"[DONE] Added {len(self.mResults.items)} item(s) to layer group "
            f"'{_GROUP_NAME}'."
        )
        LaUtils.debug.log("Catchment task complete", "Calculation")

    def cancel(self) -> None:
        """Cooperative cancel — :class:`LaCatchment` polls :meth:`isCanceled`."""
        self.grassMessage.emit("[CANCEL] Cancelling catchment analysis...")
        super().cancel()

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _onLogged(self, theMessage: str) -> None:
        self.grassMessage.emit(theMessage)

    def _onProgress(self, theOverallDone: int, theIter: int, theMaxIter: int) -> None:
        """
        Map the orchestrator's per-item per-iter signal into QGIS's
        single-percentage task progress.

        The orchestrator knows the count of items done across the whole run
        and the current iteration index inside the current item. We don't
        know the total item count here, so we just feed iteration percentage
        into ``setProgress`` — gives users a moving bar that resets per item.
        """
        if theMaxIter > 0:
            self.setProgress(100.0 * theIter / theMaxIter)
        self.overallProgress.emit(theOverallDone, 0)
        self.targetProgress.emit(theIter, theMaxIter)

    def _modelPrecision(self) -> int:
        myPrecision = getattr(self.mModel, "precision", 5)
        try:
            return max(int(myPrecision), 1)
        except (TypeError, ValueError):
            return 5

    @staticmethod
    def _resolveLayer(theLayerId: Optional[str], theLabel: str) -> Optional[QgsRasterLayer]:
        if not theLayerId:
            return None
        myLayer = QgsProject.instance().mapLayer(theLayerId)
        if not isinstance(myLayer, QgsRasterLayer):
            return None
        return myLayer

    def _buildScratchDir(self) -> str:
        try:
            from qgis.core import QgsProcessingUtils
            myBase = QgsProcessingUtils.tempFolder()
        except Exception:
            import tempfile
            myBase = tempfile.gettempdir()
        myDir = os.path.join(
            myBase, "landuseanalyst", f"run_{int(time.time())}"
        )
        os.makedirs(myDir, exist_ok=True)
        return myDir

    def _runGroupName(self) -> str:
        myScenario = getattr(self.mModel, "name", "") or "scenario"
        myPeriod   = getattr(self.mModel, "period", "") or ""
        myStamp    = time.strftime("%Y-%m-%d %H:%M:%S")
        myParts = [str(myScenario)]
        if myPeriod:
            myParts.append(str(myPeriod))
        myParts.append(myStamp)
        return " — ".join(myParts)

    @staticmethod
    def _layerName(theItem: AnalyseResult) -> str:
        myStatusBadge = ""
        if theItem.status is SearchStatus.Failed:
            myStatusBadge = "  ⚠"
        return (
            f"{theItem.itemName} ({theItem.achievedHa:.1f} Ha"
            f" / target {theItem.targetHa:.1f}){myStatusBadge}"
        )

    @staticmethod
    def _applyMaskStyle(theLayer: QgsRasterLayer) -> None:
        if os.path.exists(_QML_STYLE):
            theLayer.loadNamedStyle(_QML_STYLE)
            theLayer.triggerRepaint()
