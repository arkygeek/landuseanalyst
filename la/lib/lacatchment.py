"""
lacatchment.py — pure-Python catchment-analysis orchestrator.

Owns the binary-search loop that finds, for each crop/animal, the smallest
cost-distance zone around the settlement whose suitable area matches the
target hectares (computed elsewhere by :mod:`la.lib.lacalculations`).

Deliberately has no QGIS imports — the GRASS-via-Processing back end is
injected as an :class:`la.lib.lagrass.LaGrass` instance. This makes the
binary search trivially mockable in unit tests.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional

from qgis.PyQt.QtCore import QObject, pyqtSignal

from la.lib.lagrass import LaGrass, LaGrassError
from la.lib.lautils import LaUtils


# ---------------------------------------------------------------------------
# Public enums / dataclasses
# ---------------------------------------------------------------------------
class DistanceMethod(Enum):
    """Cost-surface model: matches the three radio buttons in the main form."""
    WalkingTime  = "WalkingTime"
    Euclidean    = "Euclidean"
    PathDistance = "PathDistance"


class SearchStatus(Enum):
    """Outcome of a single per-item binary search."""
    Converged = "Converged"
    Failed    = "Failed"
    Skipped   = "Skipped"


class LaGisInputError(ValueError):
    """Raised when GIS inputs (DEM, coords, layer ids) are unusable."""


@dataclass(frozen=True)
class AnalyseResult:
    """
    Outcome of :meth:`LaCatchment.analyseItem` for one crop or animal.

    :ivar itemName:    Display name of the crop or animal.
    :ivar threshold:   Final cost-distance threshold that was chosen.
    :ivar achievedHa:  Suitable area inside the catchment, in hectares.
    :ivar targetHa:    Target area in hectares.
    :ivar outputPath:  Absolute path of the catchment mask GeoTIFF.
    :ivar status:      ``Converged`` / ``Failed`` / ``Skipped``.
    :ivar message:     Free-text explanation, primarily for ``Failed`` / ``Skipped``.
    """
    itemName:   str
    threshold:  float
    achievedHa: float
    targetHa:   float
    outputPath: Optional[str]
    status:     SearchStatus
    message:    str = ""


@dataclass(frozen=True)
class LaCatchmentInputs:
    """Runtime-only handles (not persisted in the LaModel)."""
    demLayerId:           str
    commonCropLayerId:    Optional[str]
    commonGrazingLayerId: Optional[str]
    method:               DistanceMethod


@dataclass(frozen=True)
class LaCatchmentResults:
    """What :meth:`LaCatchment.runCatchmentAnalysis` returns."""
    items:          List[AnalyseResult]
    costRasterPath: Optional[str]


# ---------------------------------------------------------------------------
# Constants matching the C++ implementation
# ---------------------------------------------------------------------------
_MAX_THRESHOLD     = 40000.0   # cost units, matches r.walk max_cost
_MAX_ITERATIONS    = 17        # matches the C++ binary-search ceiling
_BRACKET_LOW       = 0.0


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------
class LaCatchment(QObject):
    """
    Catchment-analysis orchestrator.

    Caller flow::

        myGrass     = LaGrass(theDemLayer, theScratchDir)
        myCatchment = LaCatchment(myGrass, thePrecisionPct=5)
        myCatchment.logged.connect(...)
        myCatchment.progress.connect(...)
        myResults = myCatchment.runCatchmentAnalysis(theModel, theInputs)

    :ivar mGrass:        The injected :class:`LaGrass` back end.
    :ivar mPrecisionPct: Convergence tolerance in percent, from ``LaModel.precision``.
    :ivar mCostRaster:   Path to the cost surface, set by :meth:`prepareCostSurface`.
    """

    progress = pyqtSignal(int, int, int)   # (overallDone, iter, maxIter)
    logged   = pyqtSignal(str)

    def __init__(self, theGrass: LaGrass, thePrecisionPct: int) -> None:
        super().__init__()
        self.mGrass        = theGrass
        self.mPrecisionPct = max(int(thePrecisionPct), 1)
        self.mCostRaster: Optional[str] = None
        self._mOverallDone = 0
        self._mOverallTotal = 0

    # ------------------------------------------------------------------
    # Cost surface
    # ------------------------------------------------------------------
    def prepareCostSurface(
        self, theEasting: float, theNorthing: float, theMethod: DistanceMethod,
    ) -> str:
        """
        Build the cost surface around the settlement.

        :param theEasting:  Settlement easting in DEM CRS units.
        :param theNorthing: Settlement northing in DEM CRS units.
        :param theMethod:   :class:`DistanceMethod` enum value.
        :return: Absolute path of the cost-surface GeoTIFF.
        :rtype: str
        :raises LaGisInputError: If the coords lie outside the DEM extent.
        :raises NotImplementedError: For :attr:`DistanceMethod.PathDistance`.
        """
        myExtent = self.mGrass.mRegionExtent
        if not (myExtent.xMinimum() <= theEasting  <= myExtent.xMaximum() and
                myExtent.yMinimum() <= theNorthing <= myExtent.yMaximum()):
            raise LaGisInputError(
                f"Settlement coordinates ({theEasting}, {theNorthing}) lie "
                f"outside the DEM extent ({myExtent.xMinimum()}..{myExtent.xMaximum()}, "
                f"{myExtent.yMinimum()}..{myExtent.yMaximum()})."
            )

        if theMethod is DistanceMethod.WalkingTime:
            self.mCostRaster = self.mGrass.makeWalkCost(theEasting, theNorthing)
        elif theMethod is DistanceMethod.Euclidean:
            self.mCostRaster = self.mGrass.makeEuclideanCost(theEasting, theNorthing)
        else:
            raise NotImplementedError(
                "Path Distance is not implemented yet; please select "
                "Walking Time or Euclidean."
            )
        self.logged.emit(f"Cost surface ready: {self.mCostRaster}")
        return self.mCostRaster

    # ------------------------------------------------------------------
    # Per-item binary search
    # ------------------------------------------------------------------
    def analyseItem(
        self,
        theItemName:          str,
        theSuitabilityRaster: str,
        theAreaTargetHa:      float,
        theIsCanceledFn:      Callable[[], bool] = lambda: False,
    ) -> AnalyseResult:
        """
        Binary-search a cost threshold whose catchment matches a target Ha.

        :param theItemName:          Crop or animal name; used in output filename.
        :param theSuitabilityRaster: Absolute path of the per-item suitability GeoTIFF.
        :param theAreaTargetHa:      Target area in hectares.
        :param theIsCanceledFn:      Polled between iterations.
        :return: :class:`AnalyseResult` — never raises on the convergence path;
            status reflects what happened.
        :rtype: AnalyseResult
        """
        if self.mCostRaster is None:
            return AnalyseResult(
                theItemName, 0.0, 0.0, theAreaTargetHa, None,
                SearchStatus.Failed,
                "Cost surface not prepared. Call prepareCostSurface first.",
            )
        if theAreaTargetHa <= 0.0:
            return AnalyseResult(
                theItemName, 0.0, 0.0, theAreaTargetHa, None,
                SearchStatus.Skipped,
                "Target area is zero.",
            )

        # Half-window for acceptance: |achieved - target| <= target * pct% / 100 / 2
        myHalfWindow = theAreaTargetHa * (self.mPrecisionPct / 100.0) / 2.0
        myLow         = _BRACKET_LOW
        myHigh        = _MAX_THRESHOLD
        myBestPath:    Optional[str]  = None
        myBestArea:    float          = 0.0
        myBestThresh:  float          = 0.0
        myBestDelta:   float          = float("inf")

        for myIteration in range(1, _MAX_ITERATIONS + 1):
            if theIsCanceledFn():
                return AnalyseResult(
                    theItemName, myBestThresh, myBestArea, theAreaTargetHa,
                    myBestPath, SearchStatus.Failed, "Cancelled by user.",
                )
            myMid = (myLow + myHigh) / 2.0
            try:
                myReclassed = self.mGrass.reclass(self.mCostRaster, myMid)
                myMask      = self.mGrass.createMask(myReclassed, theSuitabilityRaster)
                myAchieved  = self.mGrass.getArea(myMask)
            except LaGrassError as e:
                return AnalyseResult(
                    theItemName, myMid, myBestArea, theAreaTargetHa,
                    myBestPath, SearchStatus.Failed,
                    f"GRASS call failed: {e}",
                )

            myDelta = abs(myAchieved - theAreaTargetHa)
            if myDelta < myBestDelta:
                myBestDelta  = myDelta
                myBestArea   = myAchieved
                myBestThresh = myMid
                myBestPath   = myMask

            self.progress.emit(self._mOverallDone, myIteration, _MAX_ITERATIONS)
            self.logged.emit(
                f"{theItemName}: iter {myIteration}/{_MAX_ITERATIONS} "
                f"thresh={myMid:.0f} achieved={myAchieved:.2f} Ha "
                f"(target {theAreaTargetHa:.2f})"
            )

            if myDelta <= myHalfWindow:
                myOutput = self.mGrass.writeOutput(
                    myMask, f"{theItemName}_t{int(myMid)}_a{int(myAchieved)}"
                )
                return AnalyseResult(
                    theItemName, myMid, myAchieved, theAreaTargetHa,
                    myOutput, SearchStatus.Converged, "",
                )

            if myAchieved < theAreaTargetHa:
                myLow = myMid
            else:
                myHigh = myMid

        # No convergence in 17 iterations — promote the closest match anyway
        # so the run isn't empty and the user can see what they got.
        myKept = self.mGrass.writeOutput(
            myBestPath, f"{theItemName}_t{int(myBestThresh)}_a{int(myBestArea)}_partial",
        ) if myBestPath else None
        myMsg = (
            f"Did not converge within {_MAX_ITERATIONS} iterations: "
            f"closest match {myBestArea:.2f} Ha vs target {theAreaTargetHa:.2f} Ha."
        )
        self.logged.emit(f"{theItemName}: {myMsg}")
        return AnalyseResult(
            theItemName, myBestThresh, myBestArea, theAreaTargetHa,
            myKept, SearchStatus.Failed, myMsg,
        )

    # ------------------------------------------------------------------
    # Full pipeline
    # ------------------------------------------------------------------
    def runCatchmentAnalysis(
        self,
        theModel,
        theInputs:        LaCatchmentInputs,
        theIsCanceledFn:  Callable[[], bool] = lambda: False,
    ) -> LaCatchmentResults:
        """
        Run the full crops → common-crop → animals → common-grazing pipeline.

        :param theModel: ``LaModel`` instance with diet calc already run
            (:attr:`mAreaTargetsCropsMap` and :attr:`mAreaTargetsAnimalsMap`
            populated by ``doCalcs*`` in :mod:`la.lib.lacalculations`).
        :param theInputs: Layer ids + chosen distance method.
        :param theIsCanceledFn: Cancellation poll; checked between items and
            (via :meth:`analyseItem`) between iterations.
        :return: :class:`LaCatchmentResults` with one entry per analysed item.
        :rtype: LaCatchmentResults
        :raises LaGisInputError: If the DEM can't be resolved.
        """
        try:
            myCommonCropPath    = self._resolveLayerPath(theInputs.commonCropLayerId)
            myCommonGrazingPath = self._resolveLayerPath(theInputs.commonGrazingLayerId)

            # 1. Cost surface
            self.prepareCostSurface(
                float(_safeFloat(theModel, "easting", 0.0)),
                float(_safeFloat(theModel, "northing", 0.0)),
                theInputs.method,
            )

            # 2. Partition crops/animals
            myDedicatedCrops, myCommonCrops, mySkippedCrops = \
                self._partitionItems(theModel, "crops")
            myDedicatedAnimals, myCommonAnimals, mySkippedAnimals = \
                self._partitionItems(theModel, "animals")

            # The dedicated items run as themselves. The common items'
            # targets get summed and folded into one common-crop /
            # common-grazing allocation each.
            myCommonCropAreaHa    = sum(it["areaHa"] for it in myCommonCrops)
            myCommonGrazingAreaHa = sum(it["areaHa"] for it in myCommonAnimals)
            myDedicatedAnimalsAreaHa = sum(it["areaHa"] for it in myDedicatedAnimals)

            # Overall progress total = dedicated crops + 1 (common crop) +
            # dedicated animals + 1 (common grazing).
            self._mOverallTotal = (
                len(myDedicatedCrops)
                + (1 if (myCommonCropAreaHa > 0) else 0)
                + len(myDedicatedAnimals)
                + (1 if (myCommonGrazingAreaHa > 0) else 0)
            )
            self._mOverallDone = 0
            myResults: List[AnalyseResult] = []

            # 3. Dedicated crops
            for myItem in myDedicatedCrops:
                if theIsCanceledFn():
                    break
                try:
                    mySlopeMask = self.mGrass.createSlopeMask(
                        myItem["preferredSlopeMin"], myItem["preferredSlopeMax"]
                    )
                    if myItem["raster"]:
                        myEffectiveSuitability = self.mGrass.createMask(mySlopeMask, myItem["raster"])
                    else:
                        myEffectiveSuitability = mySlopeMask

                    myResults.append(self.analyseItem(
                        myItem["name"], myEffectiveSuitability, myItem["areaHa"], theIsCanceledFn,
                    ))
                except LaGrassError as e:
                    myResults.append(AnalyseResult(
                        myItem["name"], 0.0, 0.0, myItem["areaHa"], None,
                        SearchStatus.Failed,
                        f"Failed to create suitability/slope mask: {e}",
                    ))
                self._mOverallDone += 1

            # Skipped crops (no raster + not common-land) → recorded for transparency
            for myItem in mySkippedCrops:
                myResults.append(AnalyseResult(
                    myItem["name"], 0.0, 0.0, myItem["areaHa"], None,
                    SearchStatus.Skipped,
                    "No suitability raster set and not flagged for common land.",
                ))
                self.logged.emit(f"Skipped: {myItem['name']} — no raster, not common.")

            # 4. Common-crop catchment + leftover for animals
            myLeftoverRaster: Optional[str] = None
            myCommonCropThreshold: Optional[float] = None
            if myCommonCropAreaHa > 0:
                if theIsCanceledFn():
                    return self._packageResults(myResults)

                myCommonCropSlopeMin = min(it["preferredSlopeMin"] for it in myCommonCrops) if myCommonCrops else 0.0
                myCommonCropSlopeMax = max(it["preferredSlopeMax"] for it in myCommonCrops) if myCommonCrops else 9.0

                try:
                    myCommonCropSlopeMask = self.mGrass.createSlopeMask(
                        myCommonCropSlopeMin, myCommonCropSlopeMax
                    )
                    if myCommonCropPath:
                        myEffectiveCommonCrop = self.mGrass.createMask(myCommonCropSlopeMask, myCommonCropPath)
                    else:
                        myEffectiveCommonCrop = myCommonCropSlopeMask

                    myCommonResult = self.analyseItem(
                        "commonCrop", myEffectiveCommonCrop, myCommonCropAreaHa, theIsCanceledFn,
                    )
                    myResults.append(myCommonResult)
                    myCommonCropThreshold = myCommonResult.threshold

                    if myCommonResult.status is SearchStatus.Converged:
                        myLeftoverRaster = self.mGrass.createInverseMask(
                            self.mCostRaster, myCommonCropThreshold, myEffectiveCommonCrop,
                        )
                except LaGrassError as e:
                    myResults.append(AnalyseResult(
                        "commonCrop", 0.0, 0.0, myCommonCropAreaHa, None,
                        SearchStatus.Failed,
                        f"Common crop catchment failed: {e}",
                    ))
                self._mOverallDone += 1

            # 5. Dedicated animals — merged with leftover if available
            for myItem in myDedicatedAnimals:
                if theIsCanceledFn():
                    break
                try:
                    mySlopeMask = self.mGrass.createSlopeMask(
                        myItem["preferredSlopeMin"], myItem["preferredSlopeMax"]
                    )
                    if myItem["raster"]:
                        if myLeftoverRaster is not None:
                            myBaseSuit = self.mGrass.mergeMaps(myLeftoverRaster, myItem["raster"])
                        else:
                            myBaseSuit = myItem["raster"]
                        myEffectiveSuitability = self.mGrass.createMask(myBaseSuit, mySlopeMask)
                    else:
                        # Slope-only mode
                        if myLeftoverRaster is not None:
                            myEffectiveSuitability = self.mGrass.createMask(myLeftoverRaster, mySlopeMask)
                        else:
                            myEffectiveSuitability = mySlopeMask

                    myResults.append(self.analyseItem(
                        myItem["name"], myEffectiveSuitability, myItem["areaHa"], theIsCanceledFn,
                    ))
                except LaGrassError as e:
                    myResults.append(AnalyseResult(
                        myItem["name"], 0.0, 0.0, myItem["areaHa"], None,
                        SearchStatus.Failed,
                        f"Failed to create suitability/slope mask: {e}",
                    ))
                self._mOverallDone += 1

            for myItem in mySkippedAnimals:
                myResults.append(AnalyseResult(
                    myItem["name"], 0.0, 0.0, myItem["areaHa"], None,
                    SearchStatus.Skipped,
                    "No suitability raster set and not flagged for common grazing.",
                ))
                self.logged.emit(f"Skipped: {myItem['name']} — no raster, not common.")

            # 6. Common-grazing catchment
            if myCommonGrazingAreaHa > 0:
                if theIsCanceledFn():
                    return self._packageResults(myResults)

                myCommonGrazingSlopeMin = min(it["preferredSlopeMin"] for it in myCommonAnimals) if myCommonAnimals else 0.0
                myCommonGrazingSlopeMax = max(it["preferredSlopeMax"] for it in myCommonAnimals) if myCommonAnimals else 15.0

                try:
                    myCommonGrazingSlopeMask = self.mGrass.createSlopeMask(
                        myCommonGrazingSlopeMin, myCommonGrazingSlopeMax
                    )
                    if myCommonGrazingPath:
                        if myLeftoverRaster is not None:
                            myBaseSuit = self.mGrass.mergeMaps(myLeftoverRaster, myCommonGrazingPath)
                        else:
                            myBaseSuit = myCommonGrazingPath
                        myEffectiveCommonGrazing = self.mGrass.createMask(myBaseSuit, myCommonGrazingSlopeMask)
                    else:
                        # Slope-only mode
                        if myLeftoverRaster is not None:
                            myEffectiveCommonGrazing = self.mGrass.createMask(myLeftoverRaster, myCommonGrazingSlopeMask)
                        else:
                            myEffectiveCommonGrazing = myCommonGrazingSlopeMask

                    myResults.append(self.analyseItem(
                        "commonGrazing", myEffectiveCommonGrazing, myCommonGrazingAreaHa, theIsCanceledFn,
                    ))
                except LaGrassError as e:
                    myResults.append(AnalyseResult(
                        "commonGrazing", 0.0, 0.0, myCommonGrazingAreaHa, None,
                        SearchStatus.Failed,
                        f"Common grazing catchment failed: {e}",
                    ))
                self._mOverallDone += 1

            return self._packageResults(myResults)
        finally:
            self.mGrass.cleanup()

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _packageResults(self, theResults: List[AnalyseResult]) -> LaCatchmentResults:
        return LaCatchmentResults(items=list(theResults), costRasterPath=self.mCostRaster)

    def _resolveLayerPath(self, theLayerId: Optional[str]) -> Optional[str]:
        """Return the .source() of a loaded QgsMapLayer by id, or None."""
        if not theLayerId:
            return None
        try:
            from qgis.core import QgsProject
        except Exception:
            return None
        myLayer = QgsProject.instance().mapLayer(theLayerId)
        return myLayer.source() if myLayer is not None else None

    def _partitionItems(self, theModel, theKind: str):
        """
        Split a model's per-item area-target map into dedicated, common, skipped.

        :param theKind: ``"crops"`` or ``"animals"``.
        :return: 3-tuple of lists of dicts each shaped
            ``{"name": str, "areaHa": float, "raster": str, "guid": str}``.
            The 'common' bucket has empty ``raster`` (allocated together later).
        """
        if theKind == "crops":
            myAreaMap = getattr(theModel, "mAreaTargetsCropsMap", {}) or {}
            myParamMap = getattr(theModel, "mCropsMap", {}) or {}
            myCommonFlag = "useCommonLand"
            myGetItem = LaUtils.getCrop
            myGetParam = LaUtils.getCropParameter
        else:
            myAreaMap = getattr(theModel, "mAreaTargetsAnimalsMap", {}) or {}
            myParamMap = getattr(theModel, "mAnimalsMap", {}) or {}
            myCommonFlag = "useCommonGrazingLand"
            myGetItem = LaUtils.getAnimal
            myGetParam = LaUtils.getAnimalParameter

        myDedicated: List[Dict] = []
        myCommon:    List[Dict] = []
        mySkipped:   List[Dict] = []

        for myGuid, myAreaHa in myAreaMap.items():
            if myGuid == "CommonTarget" or float(myAreaHa) <= 0:
                continue
            myItem = myGetItem(myGuid)
            myName = myItem.name if (myItem is not None and getattr(myItem, "name", None)) else myGuid
            myParamGuid = myParamMap.get(myGuid, "")
            myParam = myGetParam(myParamGuid) if myParamGuid else None
            myRasterName = (getattr(myParam, "rasterName", "") or "").strip() if myParam else ""
            myUsesCommon = bool(getattr(myParam, myCommonFlag, False)) if myParam else False

            mySlopeMin = float(getattr(myParam, "preferredSlopeMin", 0.0)) if myParam else 0.0
            mySlopeMax = float(getattr(myParam, "preferredSlopeMax", 9.0 if theKind == "crops" else 15.0)) if myParam else (9.0 if theKind == "crops" else 15.0)

            myRecord = {
                "guid":   myGuid,
                "name":   myName,
                "areaHa": float(myAreaHa),
                "raster": myRasterName,
                "preferredSlopeMin": mySlopeMin,
                "preferredSlopeMax": mySlopeMax,
            }
            if myUsesCommon:
                myCommon.append(myRecord)
            elif myRasterName or myParam:
                myDedicated.append(myRecord)
            else:
                mySkipped.append(myRecord)
        return myDedicated, myCommon, mySkipped


# ---------------------------------------------------------------------------
# Small util that mirrors the one in lareports.py — kept local to avoid
# importing the report module just for a coercion helper.
# ---------------------------------------------------------------------------
def _safeFloat(theObj, theAttr: str, theDefault: float = 0.0) -> float:
    try:
        return float(str(getattr(theObj, theAttr, theDefault)))
    except (TypeError, ValueError):
        return theDefault
