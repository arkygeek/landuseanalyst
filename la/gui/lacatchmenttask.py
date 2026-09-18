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
from typing import Optional, TYPE_CHECKING

from qgis.PyQt.QtCore import pyqtSignal
from qgis.core import (
    QgsTask,
    QgsProject,
    QgsRasterLayer,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
)

from la.lib.lautils import LaUtils
from la.gui.lalayerstyles import LaLayerStyles
from la.lib.lagrass import LaGrass, LaGrassError
from la.lib.lacatchment import (
    LaCatchment,
    LaCatchmentInputs,
    LaCatchmentResults,
    AnalyseResult,
    SearchStatus,
    LaGisInputError,
)

if TYPE_CHECKING:  # pragma: no cover
    from la.lib.lamodel import LaModel


_GROUP_NAME = "Catchment Analysis"


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
    # Emitted from finished() on the main thread, *before* QgsTaskManager
    # deletes the task, so listeners never touch a dead wrapper.
    completed       = pyqtSignal(object)   # LaCatchmentResults
    failed          = pyqtSignal(str)

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
        if not theResult or self.mResults is None:
            myMsg = self.mErrorText or "Catchment analysis did not complete."
            LaUtils.debug.log(f"Catchment task failed: {myMsg}", "Error")
            self.grassMessage.emit(f"[FAILED] {myMsg}")
            self.failed.emit(myMsg)
            return

        myProject = QgsProject.instance()
        myRoot = myProject.layerTreeRoot()
        myGroup = myRoot.findGroup(_GROUP_NAME)
        if myGroup is None:
            myGroup = myRoot.insertGroup(0, _GROUP_NAME)
        myGroup.setExpanded(True)
        myRunGroup = myGroup.addGroup(self._runGroupName())
        myRunGroup.setExpanded(True)

        myDemLayer = self._resolveLayer(self.mInputs.demLayerId, "DEM")
        myCrs = myDemLayer.crs() if myDemLayer is not None else None

        # 1. Settlement marker on top so the seed is always visible.
        mySettlementLayer = self._buildSettlementLayer(myCrs)
        if mySettlementLayer is not None:
            myProject.addMapLayer(mySettlementLayer, False)
            myRunGroup.addLayer(mySettlementLayer)

        # 2. Per-item masks, split into Crops / Animals sub-groups. Both are
        #    expanded so the results are visible without any clicking.
        myCropsGroup   = myRunGroup.addGroup("Crops")
        myAnimalsGroup = myRunGroup.addGroup("Animals")
        myCropsGroup.setExpanded(True)
        myAnimalsGroup.setExpanded(True)
        myCropNames = self._selectedCropNames()
        myAdded = 0
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
            myIsCrop = myItem.itemName == "commonCrop" or myItem.itemName in myCropNames
            (myCropsGroup if myIsCrop else myAnimalsGroup).addLayer(myLayer)
            LaLayerStyles.applyCatchmentMaskStyle(myLayer, theIsCrop=myIsCrop)
            myAdded += 1
        for mySubGroup in (myCropsGroup, myAnimalsGroup):
            if not mySubGroup.children():
                myRunGroup.removeChildNode(mySubGroup)

        # 3. Cost surface last (bottom of the group), semi-transparent so the
        #    terrain underneath stays readable.
        if self.mResults.costRasterPath:
            myCostLayer = QgsRasterLayer(self.mResults.costRasterPath, "Cost surface (s walking)")
            if myCostLayer.isValid():
                myProject.addMapLayer(myCostLayer, False)
                myRunGroup.addLayer(myCostLayer)
                LaLayerStyles.applyCostSurfaceStyle(myCostLayer)

        self.grassMessage.emit(
            f"[DONE] Added {myAdded} item layer(s) to group '{_GROUP_NAME}'."
        )
        LaUtils.debug.log("Catchment task complete", "Calculation")
        self.completed.emit(self.mResults)

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

    def _selectedCropNames(self) -> set:
        """Names of the crops selected on the model, for Crops/Animals grouping."""
        myNames = set()
        for myCropGuid in getattr(self.mModel, "mCropsMap", {}).keys():
            try:
                myCrop = LaUtils.getCrop(myCropGuid)
                if myCrop is not None and myCrop.name:
                    myNames.add(myCrop.name)
            except Exception:  # pragma: no cover - defensive, catalogue lookups
                continue
        return myNames

    def _buildSettlementLayer(self, theCrs) -> Optional[QgsVectorLayer]:
        """
        Memory point layer holding the settlement seed, styled as a red circle.

        :param theCrs: CRS of the DEM (``QgsCoordinateReferenceSystem``) or None.
        :rtype: QgsVectorLayer | None
        """
        try:
            myEasting  = float(getattr(self.mModel, "easting", 0.0))
            myNorthing = float(getattr(self.mModel, "northing", 0.0))
        except (TypeError, ValueError):
            return None
        myUri = "Point"
        if theCrs is not None and theCrs.isValid():
            myUri += f"?crs={theCrs.authid()}"
        myLayer = QgsVectorLayer(myUri, "Settlement", "memory")
        if not myLayer.isValid():
            return None
        myFeature = QgsFeature()
        myFeature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(myEasting, myNorthing)))
        myLayer.dataProvider().addFeatures([myFeature])
        myLayer.updateExtents()
        LaLayerStyles.applySettlementStyle(myLayer)
        return myLayer
