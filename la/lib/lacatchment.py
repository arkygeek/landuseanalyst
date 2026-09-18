"""
lacatchment.py — pure-Python catchment-analysis orchestrator.

Owns the binary-search loop that finds, for each crop/animal, the smallest
cost-distance zone around the settlement whose suitable area matches the
target hectares (computed elsewhere by :mod:`la.lib.lacalculations`), and the
pipeline around it: a seed-centred working window sized from the targets
(re-run wider when a catchment reaches the window edge), a walking-time or
Euclidean cost surface, per-item slope bands intersected with (or standing in
for) the suitability rasters, a sown / fallow split of every crop, the
dedicated-vs-common land partition inherited from the C++ original, and
per-result diagnostics.

Deliberately has no QGIS imports — the raster back end is injected as an
:class:`la.lib.lagrass.LaGrass` instance, so the search is testable with a
duck-typed DEM layer and stub model.
"""

import os
import time
from dataclasses import dataclass, replace
from enum import Enum
from typing import Callable, List, Optional, Tuple

from qgis.PyQt.QtCore import QObject, pyqtSignal

from la.lib.lagrass import LaGrass, LaGrassError
from la.lib.lautils import LaUtils


# ---------------------------------------------------------------------------
# Public enums / dataclasses
# ---------------------------------------------------------------------------
class DistanceMethod(Enum):
    WalkingTime  = "WalkingTime"
    Euclidean    = "Euclidean"
    PathDistance = "PathDistance"   # not implemented; kept for XML compatibility


class SearchStatus(Enum):
    Converged = "Converged"
    Failed    = "Failed"
    Skipped   = "Skipped"


class LaGisInputError(ValueError):
    """Raised when a GIS input (DEM, coordinates) cannot be used."""


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
    :ivar kind:        ``"crop"`` or ``"animal"`` (common land takes the kind of its users).
    :ivar category:    ``""``, ``"sown"``, ``"fallow"`` or ``"total"`` for split cropland.
    :ivar iterations:  Binary-search iterations spent.
    :ivar elapsedSec:  Wall time for this item.
    :ivar elevationMin/Max: DEM range inside the mask (diagnostic).
    :ivar slopeEliminatedPct: Share of the base suitability removed by the slope band.
    :ivar slopeBand:   ``(minDeg, maxDeg)`` applied, or None.
    """
    itemName:   str
    threshold:  float
    achievedHa: float
    targetHa:   float
    outputPath: Optional[str]
    status:     SearchStatus
    message:    str = ""
    kind:       str = ""
    category:   str = ""
    iterations: int = 0
    elapsedSec: float = 0.0
    elevationMin: Optional[float] = None
    elevationMax: Optional[float] = None
    slopeEliminatedPct: Optional[float] = None
    slopeBand: Optional[Tuple[float, float]] = None


@dataclass(frozen=True)
class LaCatchmentInputs:
    """Runtime-only handles and options (not persisted in the LaModel)."""
    demLayerId:           str
    commonCropLayerId:    Optional[str]
    commonGrazingLayerId: Optional[str]
    method:               DistanceMethod
    windowPixels:         Optional[int] = None   # None → sized from the land targets
    applySlopeLimits:     bool = True             # honour each item's slope band
    useSlopeOnlySuitability: bool = False         # band alone when an item has no raster
    splitFallow:          bool = True             # sown + fallow masks per crop
    engine:               str = "pure"            # "pure" | "grass"
    barriersPath:         Optional[str] = None    # OGR-readable rivers/lakes/walls (exported by the UI)
    livePreview:          bool = False            # emit every iteration's mask for the map


@dataclass(frozen=True)
class LaCatchmentResults:
    """What :meth:`LaCatchment.runCatchmentAnalysis` returns."""
    items:          List[AnalyseResult]
    costRasterPath: Optional[str]
    windowPixels:   Optional[int] = None
    windowShape:    Optional[Tuple[int, int]] = None
    slopeRasterPath: Optional[str] = None
    retried:        bool = False
    barrierFeatures: Optional[int] = None   # features supplied (None = no barrier layer)
    barrierCells:    Optional[int] = None   # cells that actually received friction


# ---------------------------------------------------------------------------
# Constants matching the C++ implementation
# ---------------------------------------------------------------------------
_MAX_THRESHOLD     = 40000.0   # cost units, matches r.walk max_cost
_MAX_ITERATIONS    = 17        # matches the C++ binary-search ceiling
_BRACKET_LOW       = 0.0
_MAX_WINDOW_PIXELS = 1500      # ~630 MB peak for the sparse graph at 280 B/cell


@dataclass
class _Item:
    """One crop / animal to analyse, resolved from the model + catalogue."""
    guid: str
    name: str
    kind: str                 # "crop" | "animal"
    areaHa: float
    raster: str               # "" when none
    usesCommon: bool
    slopeBand: Optional[Tuple[float, float]]
    sownHa: float = 0.0
    fallowHa: float = 0.0


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
    # (itemName, maskPath, threshold, achievedHa, targetHa) — one per iteration when livePreview is on
    previewUpdated = pyqtSignal(str, str, float, float, float)

    def __init__(self, theGrass: LaGrass, thePrecisionPct: int) -> None:
        super().__init__()
        self.mGrass        = theGrass
        self.mPrecisionPct = max(int(thePrecisionPct), 1)
        self.mCostRaster: Optional[str] = None
        self.mSlopeRaster: Optional[str] = None
        self.mBarrierEffect = None   # la.lib.labarriers.BarrierEffect for the last pass
        self.mLivePreview = False
        self._mOverallDone = 0
        self._mOverallTotal = 0

    # ------------------------------------------------------------------
    # Cost surface
    # ------------------------------------------------------------------
    def prepareCostSurface(
        self, theEasting: float, theNorthing: float, theMethod: DistanceMethod, theFriction=None,
    ) -> str:
        """
        Build the cost surface around the settlement on the current window.

        :param theEasting:  Settlement easting in DEM CRS units.
        :param theNorthing: Settlement northing in DEM CRS units.
        :param theMethod:   :class:`DistanceMethod` enum value.
        :param theFriction: Optional friction grid (s/m, inf = impassable) on the window.
        :return: Absolute path of the cost-surface GeoTIFF (kept, not temp).
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
            myRaw = self.mGrass.makeWalkCost(theEasting, theNorthing, theFriction)
        elif theMethod is DistanceMethod.Euclidean:
            myRaw = self.mGrass.makeEuclideanCost(theEasting, theNorthing, theFriction)
        else:
            raise NotImplementedError(
                "Path Distance is not implemented yet; please select Walking Time or Euclidean."
            )
        # The builders register their output as an intermediate raster and
        # cleanup() would delete it before the task adds it to the map;
        # promote it to a kept output.
        self.mCostRaster = self.mGrass.writeOutput(myRaw, f"costSurface_{theMethod.name}")
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
        theKind:              str = "",
        theCategory:          str = "",
        theSlopeBand:         Optional[Tuple[float, float]] = None,
        theBaseSuitability:   Optional[str] = None,
    ) -> AnalyseResult:
        """
        Binary-search a cost threshold whose catchment matches a target Ha.

        :param theItemName:          Crop or animal name; used in output filename.
        :param theSuitabilityRaster: Effective suitability (already aligned, slope applied).
        :param theAreaTargetHa:      Target area in hectares.
        :param theIsCanceledFn:      Polled between iterations.
        :param theKind:              ``"crop"`` / ``"animal"`` for grouping.
        :param theCategory:          ``""`` / ``"sown"`` / ``"total"``.
        :param theSlopeBand:         Band applied, recorded for diagnostics.
        :param theBaseSuitability:   Suitability before the slope band (diagnostics).
        :return: :class:`AnalyseResult` — never raises on the convergence path.
        """
        myStart = time.time()
        myLabel = f"{theItemName} {theCategory}".strip()
        if self.mCostRaster is None:
            return AnalyseResult(theItemName, 0.0, 0.0, theAreaTargetHa, None, SearchStatus.Failed,
                                 "Cost surface not prepared. Call prepareCostSurface first.",
                                 kind=theKind, category=theCategory)
        if theAreaTargetHa <= 0.0:
            return AnalyseResult(theItemName, 0.0, 0.0, theAreaTargetHa, None, SearchStatus.Skipped,
                                 "Target area is zero.", kind=theKind, category=theCategory)

        # Half-window for acceptance: |achieved - target| <= target * pct% / 100 / 2
        myHalfWindow = theAreaTargetHa * (self.mPrecisionPct / 100.0) / 2.0
        myLow, myHigh = _BRACKET_LOW, _MAX_THRESHOLD
        myBestPath: Optional[str] = None
        myBestArea = 0.0
        myBestThresh = 0.0
        myBestDelta = float("inf")

        for myIteration in range(1, _MAX_ITERATIONS + 1):
            if theIsCanceledFn():
                return AnalyseResult(theItemName, myBestThresh, myBestArea, theAreaTargetHa, myBestPath,
                                     SearchStatus.Failed, "Cancelled by user.", kind=theKind,
                                     category=theCategory, iterations=myIteration - 1,
                                     elapsedSec=time.time() - myStart, slopeBand=theSlopeBand)
            myMid = (myLow + myHigh) / 2.0
            try:
                myReclassed = self.mGrass.reclass(self.mCostRaster, myMid)
                myMask      = self.mGrass.createMask(myReclassed, theSuitabilityRaster)
                myAchieved  = self.mGrass.getArea(myMask)
            except LaGrassError as e:
                return AnalyseResult(theItemName, myMid, myBestArea, theAreaTargetHa, myBestPath,
                                     SearchStatus.Failed, f"Raster step failed: {e}", kind=theKind,
                                     category=theCategory, iterations=myIteration,
                                     elapsedSec=time.time() - myStart, slopeBand=theSlopeBand)

            myDelta = abs(myAchieved - theAreaTargetHa)
            if myDelta < myBestDelta:
                myBestDelta, myBestArea, myBestThresh, myBestPath = myDelta, myAchieved, myMid, myMask

            self.progress.emit(self._mOverallDone, myIteration, _MAX_ITERATIONS)
            self.logged.emit(
                f"{myLabel}: iter {myIteration}/{_MAX_ITERATIONS} thresh={myMid:.0f} "
                f"achieved={myAchieved:.2f} Ha (target {theAreaTargetHa:.2f})"
            )
            if self.mLivePreview:
                self._emitPreview(myLabel, myMask, myMid, myAchieved, theAreaTargetHa)

            if myDelta <= myHalfWindow:
                myOutput = self.mGrass.writeOutput(
                    myMask, self._outputStem(theItemName, theCategory, myMid, myAchieved))
                myElevMin, myElevMax, mySlopePct = self._computeHeuristics(
                    myOutput, theSlopeBand, theBaseSuitability)
                return AnalyseResult(theItemName, myMid, myAchieved, theAreaTargetHa, myOutput,
                                     SearchStatus.Converged, "", kind=theKind, category=theCategory,
                                     iterations=myIteration, elapsedSec=time.time() - myStart,
                                     elevationMin=myElevMin, elevationMax=myElevMax,
                                     slopeEliminatedPct=mySlopePct, slopeBand=theSlopeBand)

            if myAchieved < theAreaTargetHa:
                myLow = myMid
            else:
                myHigh = myMid

        # No convergence in 17 iterations. Two different failure modes:
        # (a) the target is physically unreachable — the suitable area within
        #     the window at the maximum threshold is below the target;
        # (b) noisy convergence — the area function is too discontinuous in
        #     the threshold to land inside the precision window.
        myKept = self.mGrass.writeOutput(
            myBestPath, self._outputStem(theItemName, theCategory, myBestThresh, myBestArea) + "_partial",
        ) if myBestPath else None
        try:
            myCeilingMask = self.mGrass.createMask(
                self.mGrass.reclass(self.mCostRaster, _MAX_THRESHOLD), theSuitabilityRaster)
            myCeilingHa = self.mGrass.getArea(myCeilingMask)
        except LaGrassError:
            myCeilingHa = None
        if myCeilingHa is not None and myCeilingHa < theAreaTargetHa * 0.99:
            myMsg = (f"Target {theAreaTargetHa:.0f} Ha exceeds the maximum reachable suitable area "
                     f"({myCeilingHa:.0f} Ha) within the search window — widen the window, use a "
                     f"different suitability raster, or model a smaller settlement.")
        else:
            myMsg = (f"Did not converge within {_MAX_ITERATIONS} iterations: closest match "
                     f"{myBestArea:.2f} Ha vs target {theAreaTargetHa:.2f} Ha.")
        self.logged.emit(f"{myLabel}: {myMsg}")
        myElevMin, myElevMax, mySlopePct = self._computeHeuristics(myKept, theSlopeBand, theBaseSuitability)
        return AnalyseResult(theItemName, myBestThresh, myBestArea, theAreaTargetHa, myKept,
                             SearchStatus.Failed, myMsg, kind=theKind, category=theCategory,
                             iterations=_MAX_ITERATIONS, elapsedSec=time.time() - myStart,
                             elevationMin=myElevMin, elevationMax=myElevMax,
                             slopeEliminatedPct=mySlopePct, slopeBand=theSlopeBand)

    def _emitPreview(self, theLabel: str, theMaskPath: str, theThreshold: float, theAchieved: float, theTarget: float) -> None:
        """Copy the iteration's mask to a stable per-item path and announce it (the UI shows it on the map)."""
        import shutil
        mySafe = "".join(c if c.isalnum() else "_" for c in theLabel)
        myPreviewPath = os.path.join(self.mGrass.mScratchDir, f"_la_preview_{mySafe}.tif")
        try:
            shutil.copyfile(theMaskPath, myPreviewPath)
        except OSError as e:
            self.logged.emit(f"Live preview copy failed for {theLabel}: {e}")
            return
        if myPreviewPath not in self.mGrass._mTempRasters:
            self.mGrass._mTempRasters.append(myPreviewPath)
        self.previewUpdated.emit(theLabel, myPreviewPath, float(theThreshold), float(theAchieved), float(theTarget))
        time.sleep(0.12)   # let the canvas redraw between iterations

    @staticmethod
    def _outputStem(theItemName: str, theCategory: str, theThreshold: float, theArea: float) -> str:
        myCategory = f"_{theCategory}" if theCategory else ""
        return f"{theItemName}{myCategory}_t{int(theThreshold)}_a{int(theArea)}"

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

        The working window is sized from the land targets unless
        ``theInputs.windowPixels`` is given; when any converged catchment
        touches the window edge the whole run is repeated on a window twice as
        wide (up to ``_MAX_WINDOW_PIXELS`` or the DEM itself).

        :param theModel: ``LaModel`` with the diet calc already run.
        :param theInputs: Layer ids, distance method and options.
        :param theIsCanceledFn: Cancellation poll.
        :raises LaGisInputError: If the DEM can't be resolved or the seed is outside it.
        """
        myEasting  = float(_safeFloat(theModel, "easting", 0.0))
        myNorthing = float(_safeFloat(theModel, "northing", 0.0))
        self.mLivePreview = bool(getattr(theInputs, "livePreview", False))
        myAuto = not theInputs.windowPixels
        myPixels = int(theInputs.windowPixels) if not myAuto else self._suggestWindowPixels(theModel)
        myRetried = False
        try:
            while True:
                myShape = self.mGrass.windowAroundSeed(myEasting, myNorthing, myPixels)
                myResults = self._runOnce(theModel, theInputs, myEasting, myNorthing, theIsCanceledFn)
                myClipped = myAuto and myPixels < _MAX_WINDOW_PIXELS and max(myShape) >= myPixels and any(
                    self.mGrass.maskTouchesBorder(r.outputPath)
                    for r in myResults if r.status is SearchStatus.Converged and r.outputPath
                )
                if myClipped and not theIsCanceledFn():
                    myNext = min(myPixels * 2, _MAX_WINDOW_PIXELS)
                    self.logged.emit(
                        f"A catchment reached the edge of the {myPixels}-cell window; "
                        f"re-running on a {myNext}-cell window."
                    )
                    myPixels = myNext
                    myRetried = True
                    self.mGrass.cleanup()
                    continue
                myEffect = self.mBarrierEffect
                return LaCatchmentResults(
                    items=myResults, costRasterPath=self.mCostRaster, windowPixels=myPixels,
                    windowShape=myShape, slopeRasterPath=self.mSlopeRaster, retried=myRetried,
                    barrierFeatures=myEffect.features if myEffect else None,
                    barrierCells=myEffect.cells if myEffect else None,
                )
        except LaGrassError as e:
            raise LaGisInputError(str(e)) from e
        finally:
            self.mGrass.cleanup()

    def _barrierFriction(self, theBarriersPath: Optional[str]):
        """Rasterise the barrier layer onto the current window; records supplied vs reached counts."""
        self.mBarrierEffect = None
        if not theBarriersPath:
            return None
        from la.lib import labarriers
        try:
            myFriction, myEffect = labarriers.frictionFromVector(theBarriersPath, self.mGrass.mDemPath)
        except (FileNotFoundError, RuntimeError) as e:
            raise LaGisInputError(f"Could not use the barrier layer: {e}") from e
        self.mBarrierEffect = myEffect
        if myEffect.features and not myEffect.reachedRaster:
            self.logged.emit(
                f"[WARN] {myEffect.features} barrier feature(s) supplied but none fall inside the working "
                f"window — check the layer's CRS and extent. Water has NOT been modelled in this run."
            )
        elif myEffect.features:
            self.logged.emit(f"Barriers: {myEffect.features} feature(s) touching {myEffect.cells} cell(s).")
        return myFriction

    def _suggestWindowPixels(self, theModel) -> int:
        from la.lib import laraster
        myTotalHa = (sum((getattr(theModel, "mAreaTargetsCropsMap", {}) or {}).values())
                     + sum((getattr(theModel, "mAreaTargetsAnimalsMap", {}) or {}).values()))
        return int(laraster.windowSizeForTarget(float(myTotalHa), float(self.mGrass.mCellSize),
                                                theMaxPixels=_MAX_WINDOW_PIXELS))

    def _runOnce(self, theModel, theInputs: LaCatchmentInputs, theEasting: float, theNorthing: float,
                 theIsCanceledFn: Callable[[], bool]) -> List[AnalyseResult]:
        """One complete pass on the current window."""
        myCommonCropPath    = self._resolveLayerPath(theInputs.commonCropLayerId)
        myCommonGrazingPath = self._resolveLayerPath(theInputs.commonGrazingLayerId)

        myFriction = self._barrierFriction(theInputs.barriersPath)
        self.prepareCostSurface(theEasting, theNorthing, theInputs.method, myFriction)

        myCrops   = self._collectItems(theModel, "crop", theInputs)
        myAnimals = self._collectItems(theModel, "animal", theInputs)
        myNeedsSlope = theInputs.applySlopeLimits and any(
            i.slopeBand is not None for i in myCrops + myAnimals) or theInputs.useSlopeOnlySuitability
        self.mSlopeRaster = self.mGrass.slopeFromDem() if myNeedsSlope else None

        myDedicatedCrops   = [i for i in myCrops if not i.usesCommon and (i.raster or theInputs.useSlopeOnlySuitability)]
        myCommonCrops      = [i for i in myCrops if i.usesCommon]
        mySkippedCrops     = [i for i in myCrops if not i.usesCommon and not i.raster and not theInputs.useSlopeOnlySuitability]
        myDedicatedAnimals = [i for i in myAnimals if not i.usesCommon and (i.raster or theInputs.useSlopeOnlySuitability)]
        myCommonAnimals    = [i for i in myAnimals if i.usesCommon]
        mySkippedAnimals   = [i for i in myAnimals if not i.usesCommon and not i.raster and not theInputs.useSlopeOnlySuitability]

        myCommonCropAreaHa    = sum(i.areaHa for i in myCommonCrops)
        myCommonGrazingAreaHa = sum(i.areaHa for i in myCommonAnimals)
        self._mOverallTotal = (
            len(myDedicatedCrops) + (1 if myCommonCropAreaHa > 0 and myCommonCropPath else 0)
            + len(myDedicatedAnimals) + (1 if myCommonGrazingAreaHa > 0 and myCommonGrazingPath else 0)
        )
        self._mOverallDone = 0
        myResults: List[AnalyseResult] = []

        # 1. Dedicated crops (sown + fallow when the split is on)
        for myItem in myDedicatedCrops:
            if theIsCanceledFn():
                break
            mySuitability = self._effectiveSuitability(myItem.raster, myItem.slopeBand, theInputs)
            myResults.extend(self._analyseCrop(myItem.name, mySuitability, myItem, theInputs, theIsCanceledFn))
            self._mOverallDone += 1
        for myItem in mySkippedCrops:
            myResults.append(AnalyseResult(myItem.name, 0.0, 0.0, myItem.areaHa, None, SearchStatus.Skipped,
                                           "No suitability raster set and not flagged for common land.",
                                           kind="crop"))
            self.logged.emit(f"Skipped: {myItem.name} — no raster, not common.")

        # 2. Common-crop catchment + leftover for animals
        myLeftoverRaster: Optional[str] = None
        if myCommonCropAreaHa > 0 and myCommonCropPath:
            if theIsCanceledFn():
                return myResults
            myBand = self._mostRestrictiveBand(myCommonCrops) if theInputs.applySlopeLimits else None
            myCommonSuitability = self._effectiveSuitability(myCommonCropPath, myBand, theInputs)
            myCommonItem = _Item("commonCrop", "commonCrop", "crop", myCommonCropAreaHa, myCommonCropPath, True, myBand,
                                 sownHa=sum(i.sownHa for i in myCommonCrops),
                                 fallowHa=sum(i.fallowHa for i in myCommonCrops))
            myCommonResults = self._analyseCrop("commonCrop", myCommonSuitability, myCommonItem, theInputs, theIsCanceledFn)
            myResults.extend(myCommonResults)
            self._mOverallDone += 1
            myTotal = next((r for r in myCommonResults if r.category in ("", "total")), None)
            if myTotal is not None and myTotal.status is SearchStatus.Converged:
                try:
                    myLeftoverRaster = self.mGrass.createInverseMask(
                        self.mCostRaster, myTotal.threshold, myCommonSuitability)
                except LaGrassError as e:
                    self.logged.emit(f"createInverseMask failed: {e}")
        elif myCommonCropAreaHa > 0:
            self.logged.emit(f"Common-crop demand of {myCommonCropAreaHa:.2f} Ha but no common-crop raster picked; skipping.")

        # 3. Dedicated animals — merged with leftover if available
        for myItem in myDedicatedAnimals:
            if theIsCanceledFn():
                break
            mySuitability = self._effectiveSuitability(myItem.raster, myItem.slopeBand, theInputs)
            if myLeftoverRaster is not None:
                try:
                    mySuitability = self.mGrass.mergeMaps(myLeftoverRaster, mySuitability)
                except LaGrassError as e:
                    self.logged.emit(f"mergeMaps failed for {myItem.name}, using its own raster: {e}")
            myResults.append(self.analyseItem(myItem.name, mySuitability, myItem.areaHa, theIsCanceledFn,
                                              theKind="animal", theSlopeBand=myItem.slopeBand,
                                              theBaseSuitability=myItem.raster or None))
            self._mOverallDone += 1
        for myItem in mySkippedAnimals:
            myResults.append(AnalyseResult(myItem.name, 0.0, 0.0, myItem.areaHa, None, SearchStatus.Skipped,
                                           "No suitability raster set and not flagged for common grazing.",
                                           kind="animal"))
            self.logged.emit(f"Skipped: {myItem.name} — no raster, not common.")

        # 4. Common-grazing catchment
        if myCommonGrazingAreaHa > 0 and myCommonGrazingPath:
            if not theIsCanceledFn():
                myBand = self._mostRestrictiveBand(myCommonAnimals) if theInputs.applySlopeLimits else None
                mySuitability = self._effectiveSuitability(myCommonGrazingPath, myBand, theInputs)
                if myLeftoverRaster is not None:
                    try:
                        mySuitability = self.mGrass.mergeMaps(myLeftoverRaster, mySuitability)
                    except LaGrassError as e:
                        self.logged.emit(f"mergeMaps for common grazing failed: {e}")
                myResults.append(self.analyseItem("commonGrazing", mySuitability, myCommonGrazingAreaHa,
                                                  theIsCanceledFn, theKind="animal", theSlopeBand=myBand,
                                                  theBaseSuitability=myCommonGrazingPath))
                self._mOverallDone += 1
        elif myCommonGrazingAreaHa > 0:
            self.logged.emit(f"Common-grazing demand of {myCommonGrazingAreaHa:.2f} Ha but no common-grazing raster picked; skipping.")
        return myResults

    # ------------------------------------------------------------------
    # Crops: sown / fallow split
    # ------------------------------------------------------------------
    def _analyseCrop(self, theName: str, theSuitability: str, theItem: _Item, theInputs: LaCatchmentInputs,
                     theIsCanceledFn: Callable[[], bool]) -> List[AnalyseResult]:
        """
        Search a crop's land. With the split on and a rotation in force this
        yields a *sown* mask (the crop's cultivated target) and a *fallow* mask
        (total cropland minus sown); otherwise a single mask for the total.
        """
        myBase = theItem.raster or None
        if not (theInputs.splitFallow and theItem.fallowHa > 0 and theItem.sownHa > 0):
            return [self.analyseItem(theName, theSuitability, theItem.areaHa, theIsCanceledFn, theKind="crop",
                                     theSlopeBand=theItem.slopeBand, theBaseSuitability=myBase)]
        mySown = self.analyseItem(theName, theSuitability, theItem.sownHa, theIsCanceledFn, theKind="crop",
                                  theCategory="sown", theSlopeBand=theItem.slopeBand, theBaseSuitability=myBase)
        myTotal = self.analyseItem(theName, theSuitability, theItem.sownHa + theItem.fallowHa, theIsCanceledFn,
                                   theKind="crop", theCategory="total", theSlopeBand=theItem.slopeBand,
                                   theBaseSuitability=myBase)
        if mySown.outputPath and myTotal.outputPath:
            try:
                myFallowScratch = self.mGrass.subtractMasks(myTotal.outputPath, mySown.outputPath)
                myFallowHa = self.mGrass.getArea(myFallowScratch)
                myFallowPath = self.mGrass.writeOutput(
                    myFallowScratch, self._outputStem(theName, "fallow", myTotal.threshold, myFallowHa))
                myFallow = replace(myTotal, category="fallow", achievedHa=myFallowHa, targetHa=theItem.fallowHa,
                                   outputPath=myFallowPath, message="rested land within the total cropland catchment")
            except LaGrassError as e:
                myFallow = AnalyseResult(theName, myTotal.threshold, 0.0, theItem.fallowHa, None, SearchStatus.Failed,
                                         f"Could not derive the fallow mask: {e}", kind="crop", category="fallow")
        else:
            myFallow = AnalyseResult(theName, myTotal.threshold, 0.0, theItem.fallowHa, None, SearchStatus.Failed,
                                     "Could not derive the fallow mask (no total or sown mask).", kind="crop",
                                     category="fallow")
        return [mySown, myTotal, myFallow]

    # ------------------------------------------------------------------
    # Suitability helpers
    # ------------------------------------------------------------------
    def _effectiveSuitability(self, theRaster: str, theBand: Optional[Tuple[float, float]],
                              theInputs: LaCatchmentInputs) -> str:
        """
        Align the item's suitability raster to the window and intersect it with
        the slope band; with no raster the band alone defines suitable land.

        :raises LaGrassError: When neither a raster nor a band is available.
        """
        myBase = self.mGrass.alignRaster(theRaster) if theRaster else None
        myBandMask = None
        if theBand is not None and theInputs.applySlopeLimits and self.mSlopeRaster is not None:
            myBandMask = self.mGrass.slopeBandMask(theBand[0], theBand[1])
        if myBase is None and myBandMask is None:
            if theInputs.useSlopeOnlySuitability and self.mSlopeRaster is not None:
                myBandMask = self.mGrass.slopeBandMask(0.0, 90.0)
            else:
                raise LaGrassError("No suitability raster and no slope band for this item.")
        if myBase is None:
            return myBandMask
        if myBandMask is None:
            return myBase
        return self.mGrass.createMask(myBandMask, myBase)

    @staticmethod
    def _mostRestrictiveBand(theItems: List[_Item]) -> Optional[Tuple[float, float]]:
        myBands = [i.slopeBand for i in theItems if i.slopeBand is not None]
        if not myBands:
            return None
        return max(b[0] for b in myBands), min(b[1] for b in myBands)

    def _computeHeuristics(self, theMaskPath: Optional[str], theBand: Optional[Tuple[float, float]],
                           theBaseSuitability: Optional[str]) -> Tuple[Optional[float], Optional[float], Optional[float]]:
        """Elevation range inside the mask and the share of base suitability removed by the slope band."""
        if not theMaskPath:
            return None, None, None
        import numpy as np
        from la.lib import laraster
        myElevMin = myElevMax = mySlopePct = None
        try:
            myMask, _, _ = laraster._readBand(theMaskPath)
            myDem, _, _ = laraster._readBand(self.mGrass.mDemPath)
            if myMask.shape == myDem.shape:
                myCells = myDem[(myMask == 1) & np.isfinite(myDem)]
                if myCells.size:
                    myElevMin, myElevMax = float(np.nanmin(myCells)), float(np.nanmax(myCells))
        except Exception:
            pass
        if theBand is not None and self.mSlopeRaster and theBaseSuitability:
            try:
                mySlope, _, _ = laraster._readBand(self.mSlopeRaster)
                mySuit, _, _ = laraster._readBand(self.mGrass.alignRaster(theBaseSuitability))
                mySuitable = mySuit >= 1
                myTotal = int(mySuitable.sum())
                if myTotal > 0:
                    myOutside = mySuitable & (~np.isfinite(mySlope) | (mySlope < theBand[0]) | (mySlope > theBand[1]))
                    mySlopePct = 100.0 * int(myOutside.sum()) / myTotal
                else:
                    mySlopePct = 0.0
            except Exception:
                mySlopePct = None
        return myElevMin, myElevMax, mySlopePct

    # ------------------------------------------------------------------
    # Model → items
    # ------------------------------------------------------------------
    def _resolveLayerPath(self, theLayerId: Optional[str]) -> Optional[str]:
        """Return the .source() of a loaded QgsMapLayer by id, or None."""
        if not theLayerId:
            return None
        try:
            from qgis.core import QgsProject
        except ImportError:
            return None
        myLayer = QgsProject.instance().mapLayer(theLayerId)
        return myLayer.source() if myLayer is not None else None

    def _collectItems(self, theModel, theKind: str, theInputs: LaCatchmentInputs) -> List[_Item]:
        """Resolve the model's per-item area targets into :class:`_Item` records."""
        if theKind == "crop":
            myAreaMap  = getattr(theModel, "mAreaTargetsCropsMap", {}) or {}
            myParamMap = getattr(theModel, "mCropsMap", {}) or {}
            mySownMap  = getattr(theModel, "mAreaTargetsCropsSownMap", {}) or {}
            myFallowMap = getattr(theModel, "mAreaTargetsCropsFallowMap", {}) or {}
            myCommonFlag, myGetItem, myGetParam = "useCommonLand", LaUtils.getCrop, LaUtils.getCropParameter
        else:
            myAreaMap  = getattr(theModel, "mAreaTargetsAnimalsMap", {}) or {}
            myParamMap = getattr(theModel, "mAnimalsMap", {}) or {}
            mySownMap, myFallowMap = {}, {}
            myCommonFlag, myGetItem, myGetParam = "useCommonGrazingLand", LaUtils.getAnimal, LaUtils.getAnimalParameter

        myItems: List[_Item] = []
        for myGuid, myAreaHa in myAreaMap.items():
            if myGuid == "CommonTarget" or float(myAreaHa) <= 0:
                continue
            myCatalogueItem = myGetItem(myGuid)
            myName = getattr(myCatalogueItem, "name", "") or myGuid
            myParamGuid = myParamMap.get(myGuid, "")
            myParam = myGetParam(myParamGuid) if myParamGuid else None
            myRaster = (getattr(myParam, "rasterName", "") or "").strip() if myParam else ""
            myBand = None
            if theInputs.applySlopeLimits and myParam is not None and bool(getattr(myParam, "applySlopeLimit", False)):
                myBand = (float(getattr(myParam, "slopeMinDegrees", 0.0)), float(getattr(myParam, "slopeMaxDegrees", 90.0)))
            myItems.append(_Item(
                guid=myGuid, name=myName, kind=theKind, areaHa=float(myAreaHa), raster=myRaster,
                usesCommon=bool(getattr(myParam, myCommonFlag, False)) if myParam else False,
                slopeBand=myBand,
                sownHa=float(mySownMap.get(myGuid, 0.0) or 0.0),
                fallowHa=float(myFallowMap.get(myGuid, 0.0) or 0.0),
            ))
        return myItems


# ---------------------------------------------------------------------------
def _safeFloat(theObj, theAttr: str, theDefault: float = 0.0) -> float:
    try:
        return float(getattr(theObj, theAttr, theDefault))
    except (TypeError, ValueError):
        return theDefault
