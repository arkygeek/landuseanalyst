"""
lagrass.py — QGIS Processing wrapper for the catchment-analysis GRASS calls.

This is the ONLY module that talks to ``processing.run("grass:...")``. Every
other module talks to it in Landuse-Analyst-domain verbs (``makeWalkCost``,
``reclass``, ``getArea``) so the orchestrator can be unit-tested against a
mock and so future moves between GRASS, QGIS-native, or pure-Python
back-ends only touch one file.

End users need zero extra Python packages — the QGIS install bundles the
GRASS provider plus matplotlib, numpy, and GDAL.
"""

import os
from typing import List, Optional

from qgis.PyQt.QtCore import QObject, pyqtSignal


ENGINE_PURE = "pure"
ENGINE_GRASS = "grass"


class _Extent:
    """Duck-typed ``QgsRectangle`` (xMinimum() …) for windows built without QGIS."""

    def __init__(self, theXmin: float, theYmin: float, theXmax: float, theYmax: float) -> None:
        self._mXmin, self._mYmin, self._mXmax, self._mYmax = theXmin, theYmin, theXmax, theYmax

    def xMinimum(self) -> float: return self._mXmin
    def xMaximum(self) -> float: return self._mXmax
    def yMinimum(self) -> float: return self._mYmin
    def yMaximum(self) -> float: return self._mYmax


class LaGrassError(RuntimeError):
    """Raised when a GRASS-via-QGIS-Processing call fails or returns no output."""


class LaGrass(QObject):
    """
    Thin wrapper around the GRASS algorithms the catchment analysis needs.

    The wrapper snapshots a processing region (extent + cell size) from the
    supplied DEM at construction time, so every algorithm produces a
    co-registered raster. Intermediate GeoTIFFs are tracked in
    ``_mTempRasters`` and removed by :meth:`cleanup` unless promoted via
    :meth:`writeOutput`.

    :ivar mRegionExtent: ``QgsRectangle`` snapshot of the DEM extent.
    :ivar mCellSize: Cell size in CRS units (from the DEM x-pixel width).
    :ivar mDemPath: Filesystem path of the DEM raster.
    :ivar mScratchDir: Directory for intermediate + output GeoTIFFs.
    """

    message = pyqtSignal(str)

    def __init__(self, theDemLayer, theScratchDir: str, theEngine: str = ENGINE_PURE) -> None:
        """
        :param theDemLayer: ``QgsRasterLayer`` for the DEM. Drives region.
        :type theDemLayer: qgis.core.QgsRasterLayer
        :param theScratchDir: Directory for temp + output rasters. Created
            if it doesn't exist.
        :type theScratchDir: str
        :param theEngine: ``"pure"`` (default) runs the numpy/scipy engine in
            :mod:`la.lib.laraster` even when GRASS is registered; ``"grass"``
            prefers the GRASS Processing algorithms and falls back to pure.
        """
        super().__init__()
        os.makedirs(theScratchDir, exist_ok=True)
        self.mScratchDir = theScratchDir
        self.mEngine = theEngine if theEngine in (ENGINE_PURE, ENGINE_GRASS) else ENGINE_PURE
        self.mDemPath = theDemLayer.source()
        self.mSourceDemPath = self.mDemPath
        self.mRegionExtent = theDemLayer.extent()
        self.mCellSize = float(theDemLayer.rasterUnitsPerPixelX())
        self._mTempRasters: List[str] = []
        self._mSlopeRaster: Optional[str] = None
        self._mSlopeRasterFor: Optional[str] = None
        self._mWindowShape: Optional[tuple] = None
        # Algorithm-id probe: QGIS 3.x usually exposes "grass7:..." but
        # may also expose "grass:..." in some bundles. Cache whichever works.
        self._mWalkId: Optional[str]    = self._probeAlg(("grass7:r.walk",       "grass:r.walk"))
        self._mCostId: Optional[str]    = self._probeAlg(("grass7:r.cost",       "grass:r.cost"))
        self._mMapcalcId: Optional[str] = self._probeAlg(("grass7:r.mapcalc.simple", "grass:r.mapcalc.simple"))

    # ------------------------------------------------------------------
    # Cost-surface builders
    # ------------------------------------------------------------------
    def makeWalkCost(self, theX: float, theY: float) -> str:
        """
        Build an anisotropic walking-cost surface around the settlement.

        Tries ``grass:r.walk`` first (the fastest path for users who have a
        full GRASS install with the algorithm registered). Falls back to a
        pure-Python Tobler-based implementation
        (:meth:`_makeWalkCostPure`) when ``r.walk`` isn't available in the
        QGIS Processing GRASS provider — a common case, because the
        provider intermittently excludes ``r.walk`` across QGIS versions
        even when GRASS itself is installed.

        :param theX: Settlement easting in DEM CRS units.
        :param theY: Settlement northing in DEM CRS units.
        :return: Absolute path of the output cost-surface GeoTIFF.
        :rtype: str
        """
        if self._usePure(self._mWalkId):
            self.message.emit(
                "grass:r.walk not registered; using pure-Python Tobler "
                "walking-cost fallback."
            )
            return self._makeWalkCostPure(theX, theY)
        myFriction = self._uniformFrictionFromDem()
        myOutPath = self._tempPath("walkCost")
        myParams = {
            "elevation":         self.mDemPath,
            "friction":          myFriction,
            "start_coordinates": f"{theX},{theY}",
            "max_cost":          40000,
            "walk_coefficient":  "0.72,6.0,1.9998,-1.9998",
            "lambda":            0.75,
            "slope_factor":      -0.2125,
            "-k":                True,
            "output":            myOutPath,
            "GRASS_REGION_PARAMETER":          self._regionString(),
            "GRASS_REGION_CELLSIZE_PARAMETER": self.mCellSize,
            "GRASS_RASTER_FORMAT_OPT":         "",
            "GRASS_RASTER_FORMAT_META":        "",
        }
        self._runAlg(self._mWalkId, myParams)
        self._mTempRasters.append(myOutPath)
        self.message.emit(f"Built walk-cost surface from ({theX:.1f}, {theY:.1f}).")
        return myOutPath

    def makeEuclideanCost(self, theX: float, theY: float) -> str:
        """
        Run ``grass:r.cost`` with a uniform-1 friction raster, seeded at
        the settlement. Cost units come out in metres directly.

        :param theX: Settlement easting in DEM CRS units.
        :param theY: Settlement northing in DEM CRS units.
        :return: Absolute path of the output cost raster.
        :rtype: str
        :raises LaGrassError: If ``grass:r.cost`` isn't available or fails.
        """
        if self._usePure(self._mCostId):
            return self._makeEuclideanCostPure(theX, theY)
        myFriction = self._uniformFrictionFromDem()
        myOutPath = self._tempPath("euclideanCost")
        myParams = {
            "input":             myFriction,
            "start_coordinates": f"{theX},{theY}",
            "max_cost":          40000,
            "output":            myOutPath,
            "GRASS_REGION_PARAMETER":          self._regionString(),
            "GRASS_REGION_CELLSIZE_PARAMETER": self.mCellSize,
        }
        self._runAlg(self._mCostId, myParams)
        self._mTempRasters.append(myOutPath)
        self.message.emit(f"Built Euclidean-cost surface from ({theX:.1f}, {theY:.1f}).")
        return myOutPath

    # ------------------------------------------------------------------
    # Per-iteration ops
    # ------------------------------------------------------------------
    def reclass(self, theCostRaster: str, theThreshold: float) -> str:
        """
        Binary mask of cells with ``cost < threshold``. Cells at or above
        the threshold become null.

        :param theCostRaster: Absolute path of a cost-surface raster.
        :param theThreshold: Cost-distance threshold.
        :return: Absolute path of a 1/null binary mask GeoTIFF.
        :rtype: str
        """
        if self._usePure(self._mMapcalcId):
            return self._reclassPure(theCostRaster, theThreshold)
        myOutPath = self._tempPath(f"reclass_{int(theThreshold)}")
        myParams = self._mapcalcParams(
            theExpression=f"if(A < {theThreshold}, 1, null())",
            theA=theCostRaster,
            theOutput=myOutPath,
        )
        self._runAlg(self._mMapcalcId, myParams)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def createMask(self, theReclassed: str, theSuitabilityRaster: str) -> str:
        """
        Intersect the cost-bounded reclass with a suitability raster.

        Result cells are 1 only where the reclass is 1 AND the suitability
        raster is ≥ 1; null elsewhere.

        :param theReclassed: Output of :meth:`reclass`.
        :param theSuitabilityRaster: Per-crop / per-animal suitability raster.
        :return: Absolute path of a 1/null mask GeoTIFF.
        :rtype: str
        """
        if self._usePure(self._mMapcalcId):
            return self._createMaskPure(theReclassed, theSuitabilityRaster)
        myOutPath = self._tempPath("mask")
        myParams = self._mapcalcParams(
            theExpression="if(A >= 1 && B >= 1, 1, null())",
            theA=theReclassed,
            theB=theSuitabilityRaster,
            theOutput=myOutPath,
        )
        self._runAlg(self._mMapcalcId, myParams)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def createInverseMask(
        self,
        theCostRaster: str,
        theThreshold: float,
        theBaseSuitability: str,
    ) -> str:
        """
        Suitable cells that fell OUTSIDE the catchment.

        Used by the orchestrator to compute the "leftover" common-crop
        suitable area that becomes available to animals as common grazing.

        :param theCostRaster: The cost surface from :meth:`makeWalkCost`
            or :meth:`makeEuclideanCost`.
        :param theThreshold: Cost threshold used for the catchment.
        :param theBaseSuitability: The suitability raster the catchment was
            allocated from.
        :return: Absolute path of a 1/null leftover mask GeoTIFF.
        :rtype: str
        """
        if self._usePure(self._mMapcalcId):
            return self._createInverseMaskPure(
                theCostRaster, theThreshold, theBaseSuitability,
            )
        myOutPath = self._tempPath(f"inverse_{int(theThreshold)}")
        myParams = self._mapcalcParams(
            theExpression=f"if(B >= 1 && A >= {theThreshold}, 1, null())",
            theA=theCostRaster,
            theB=theBaseSuitability,
            theOutput=myOutPath,
        )
        self._runAlg(self._mMapcalcId, myParams)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def mergeMaps(self, theA: str, theB: str) -> str:
        """
        Union of two 1/null binary masks.

        :param theA: First mask raster path.
        :param theB: Second mask raster path.
        :return: Absolute path of a merged 1/null mask GeoTIFF.
        :rtype: str
        """
        if self._usePure(self._mMapcalcId):
            return self._mergeMapsPure(theA, theB)
        myOutPath = self._tempPath("merge")
        myParams = self._mapcalcParams(
            theExpression="if(A >= 1 || B >= 1, 1, null())",
            theA=theA,
            theB=theB,
            theOutput=myOutPath,
        )
        self._runAlg(self._mMapcalcId, myParams)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def getArea(self, theMaskRaster: str) -> float:
        """
        Area of cells with value 1 in a binary mask, in hectares.

        Delegates to :func:`la.lib.laraster.getAreaHa` (GDAL + NumPy, both
        ship with QGIS) — faster and more robust than parsing the text
        output of ``r.stats``.

        :param theMaskRaster: Path of a 1/null binary mask GeoTIFF.
        :return: Area in hectares.
        :rtype: float
        :raises LaGrassError: If the mask raster cannot be opened.
        """
        from la.lib import laraster

        try:
            return laraster.getAreaHa(theMaskRaster)
        except FileNotFoundError as myError:
            raise LaGrassError(f"Could not open mask raster {theMaskRaster}") from myError

    # ------------------------------------------------------------------
    # Lifecycle / IO
    # ------------------------------------------------------------------
    def writeOutput(self, theMaskRaster: str, theOutputName: str) -> str:
        """
        Promote a temp raster to a stable output path; drop it from cleanup.

        :param theMaskRaster: Path returned by :meth:`createMask` etc.
        :param theOutputName: Filename (no path, no extension) for the kept file.
        :return: Absolute path of the promoted GeoTIFF.
        :rtype: str
        """
        import shutil
        mySafe = "".join(c if c.isalnum() or c in "._-" else "_" for c in theOutputName)
        myDest = os.path.join(self.mScratchDir, f"{mySafe}.tif")
        shutil.copyfile(theMaskRaster, myDest)
        if theMaskRaster in self._mTempRasters:
            self._mTempRasters.remove(theMaskRaster)
        return myDest

    def cleanup(self) -> None:
        """Remove every intermediate raster not promoted via :meth:`writeOutput`."""
        for myPath in list(self._mTempRasters):
            try:
                if os.path.exists(myPath):
                    os.remove(myPath)
            except OSError:
                pass
        self._mTempRasters.clear()

    # ------------------------------------------------------------------
    # Pure-Python r.walk replacement
    # ------------------------------------------------------------------
    def _makeWalkCostPure(self, theX: float, theY: float) -> str:
        """
        Pure-Python anisotropic walking-cost surface using Tobler's hiking
        function on the DEM grid, with Dijkstra propagation from the
        settlement.

        The algorithm lives in :func:`la.lib.laraster.makeWalkCost` (shared
        with the Landuse Analyst web app); this method only adapts it to the
        wrapper's scratch-directory + temp-raster bookkeeping. It exists
        because the QGIS Processing GRASS provider intermittently excludes
        ``r.walk`` from its registered algorithms across QGIS bundles, so
        every user gets the Walking Time analysis without GRASS.

        Output is a Float32 GeoTIFF co-registered with the DEM, nodata =
        NaN, units = seconds of walking time, cells beyond 40 000 s masked
        to null — the units the binary-search threshold sweep in
        :class:`la.lib.lacatchment.LaCatchment` expects.

        :param theX: Settlement easting in DEM CRS units.
        :param theY: Settlement northing in DEM CRS units.
        :return: Absolute path of a Float32 cost-surface GeoTIFF.
        :rtype: str
        :raises LaGrassError: On unreadable DEM or seed outside DEM extent.
        """
        from la.lib import laraster

        try:
            myOutPath = laraster.makeWalkCost(
                self.mDemPath, theX, theY, self.mScratchDir,
            )
        except (FileNotFoundError, ValueError) as myError:
            raise LaGrassError(str(myError)) from myError
        self._mTempRasters.append(myOutPath)
        self.message.emit(
            f"Built walk-cost surface (pure-Python Tobler) from "
            f"({theX:.1f}, {theY:.1f})."
        )
        return myOutPath

    # ------------------------------------------------------------------
    # Pure-Python r.mapcalc.simple replacements
    # ------------------------------------------------------------------
    # The four ops below mirror the GRASS ``r.mapcalc.simple`` expressions
    # used in :meth:`reclass`, :meth:`createMask`, :meth:`createInverseMask`,
    # and :meth:`mergeMaps`. The public methods route to these when
    # ``self._mMapcalcId is None`` — same gate that protects the r.walk
    # fallback. The maths lives in :mod:`la.lib.laraster`; these wrappers
    # only add temp-raster registration and LaGrassError translation.
    #
    # Semantic-match notes
    # --------------------
    # - GRASS ``null()`` becomes 0 in a ``uint8`` mask with ``nodata=0`` —
    #   downstream consumers (:meth:`getArea`, the orchestrator) test for
    #   ``== 1`` so 0 and null are equivalent.
    # - ``cost < threshold`` against a NaN cell evaluates ``False`` in
    #   NumPy, matching GRASS's null-propagation in the same comparison.
    # - Co-registration: every output GeoTIFF re-uses the reference
    #   raster's geotransform + projection so the cost surface, masks,
    #   suitability rasters, and outputs all line up cell-for-cell.

    def _usePure(self, theAlgId: Optional[str]) -> bool:
        """True when the pure-Python engine should handle a step (default, or GRASS alg missing)."""
        return self.mEngine != ENGINE_GRASS or theAlgId is None

    def _makeEuclideanCostPure(self, theX: float, theY: float) -> str:
        """Pure-Python Euclidean (octagonal metric) cost surface, in metres."""
        from la.lib import laraster
        try:
            myOutPath = laraster.makeEuclideanCost(self.mDemPath, theX, theY, self.mScratchDir)
        except (FileNotFoundError, ValueError) as myError:
            raise LaGrassError(str(myError)) from myError
        self._mTempRasters.append(myOutPath)
        self.message.emit(f"Built Euclidean-cost surface (pure-Python) from ({theX:.1f}, {theY:.1f}).")
        return myOutPath

    # ------------------------------------------------------------------
    # Windowing, alignment, slope (pure-Python only)
    # ------------------------------------------------------------------
    def windowAroundSeed(self, theX: float, theY: float, thePixels: int) -> tuple:
        """
        Restrict the working region to a ``thePixels``-square window of the
        source DEM centred on the seed (clipped to the DEM). Every later cost,
        slope and mask raster is built on that window.

        :return: ``(columns, rows)`` of the window actually cut.
        :raises LaGrassError: If the DEM cannot be read or the seed is outside it.
        """
        from osgeo import gdal
        myDataset = gdal.Open(self.mSourceDemPath)
        if myDataset is None:
            raise LaGrassError(f"Could not open DEM {self.mSourceDemPath}")
        myGeoTrans = myDataset.GetGeoTransform()
        myCols, myRows = myDataset.RasterXSize, myDataset.RasterYSize
        myCol = int((theX - myGeoTrans[0]) / myGeoTrans[1])
        myRow = int((theY - myGeoTrans[3]) / myGeoTrans[5])
        if not (0 <= myCol < myCols and 0 <= myRow < myRows):
            raise LaGrassError(f"Seed ({theX}, {theY}) lies outside the DEM.")
        myHalf = max(1, int(thePixels)) // 2
        myCol0 = max(0, myCol - myHalf)
        myRow0 = max(0, myRow - myHalf)
        myCol1 = min(myCols, myCol - myHalf + int(thePixels))
        myRow1 = min(myRows, myRow - myHalf + int(thePixels))
        myWidth, myHeight = myCol1 - myCol0, myRow1 - myRow0
        if myWidth >= myCols and myHeight >= myRows:
            myOutPath = self.mSourceDemPath  # window covers the whole DEM: nothing to cut
        else:
            myOutPath = self._tempPath(f"demWindow_{int(thePixels)}")
            gdal.Translate(myOutPath, myDataset, srcWin=[myCol0, myRow0, myWidth, myHeight],
                           format="GTiff", creationOptions=["COMPRESS=LZW", "TILED=YES"])
            self._mTempRasters.append(myOutPath)
        myDataset = None
        self.mDemPath = myOutPath
        myXmin = myGeoTrans[0] + myCol0 * myGeoTrans[1]
        myYmax = myGeoTrans[3] + myRow0 * myGeoTrans[5]
        self.mRegionExtent = _Extent(myXmin, myYmax + myHeight * myGeoTrans[5], myXmin + myWidth * myGeoTrans[1], myYmax)
        self.mCellSize = abs(myGeoTrans[1])
        self._mWindowShape = (myWidth, myHeight)
        self._mSlopeRaster = None
        self.message.emit(f"Working window: {myWidth} × {myHeight} cells around the seed.")
        return myWidth, myHeight

    def resetWindow(self) -> None:
        """Go back to the full source DEM."""
        self.mDemPath = self.mSourceDemPath
        self._mSlopeRaster = None
        self._mWindowShape = None

    def alignRaster(self, thePath: str) -> str:
        """
        Warp a suitability raster onto the current DEM grid (nearest neighbour, uint8).

        Handles suitability layers with a different extent, resolution or CRS
        than the DEM — the web app's "auto-align suitability to DEM".
        """
        from osgeo import gdal
        myDem = gdal.Open(self.mDemPath)
        if myDem is None:
            raise LaGrassError(f"Could not open DEM {self.mDemPath}")
        myGeoTrans = myDem.GetGeoTransform()
        myCols, myRows = myDem.RasterXSize, myDem.RasterYSize
        myProjection = myDem.GetProjection()
        myDem = None
        mySource = gdal.Open(thePath)
        if mySource is None:
            raise LaGrassError(f"Could not open suitability raster {thePath}")
        mySourceProjection = mySource.GetProjection()
        mySource = None
        myXmin = myGeoTrans[0]
        myYmax = myGeoTrans[3]
        myBounds = (myXmin, myYmax + myRows * myGeoTrans[5], myXmin + myCols * myGeoTrans[1], myYmax)
        myOutPath = self._tempPath("aligned")
        myOptions = dict(format="GTiff", outputBounds=myBounds, width=myCols, height=myRows,
                         resampleAlg="near", outputType=gdal.GDT_Byte, dstNodata=0,
                         creationOptions=["COMPRESS=LZW", "TILED=YES"])
        if myProjection and mySourceProjection and myProjection != mySourceProjection:
            myOptions["dstSRS"] = myProjection
        myResult = gdal.Warp(myOutPath, thePath, **myOptions)
        if myResult is None:
            raise LaGrassError(f"Could not align {thePath} to the DEM grid.")
        myResult = None
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def slopeFromDem(self) -> str:
        """Slope raster (degrees) of the current DEM window, computed once per window."""
        from la.lib import laraster
        if self._mSlopeRaster is None or self._mSlopeRasterFor != self.mDemPath:
            self._mSlopeRaster = self._registerTemp(laraster.slopeFromDem, self.mDemPath)
            self._mSlopeRasterFor = self.mDemPath
        return self._mSlopeRaster

    def slopeBandMask(self, theMinDegrees: float, theMaxDegrees: float) -> str:
        """uint8 mask of cells whose slope lies within ``[min, max]`` degrees."""
        import numpy as np
        from la.lib import laraster
        mySlope, myGeoTrans, myProjection = laraster._readBand(self.slopeFromDem())
        myMask = (np.isfinite(mySlope) & (mySlope >= float(theMinDegrees)) & (mySlope <= float(theMaxDegrees)))
        myOutPath = self._tempPath(f"slopeBand_{int(theMinDegrees)}_{int(theMaxDegrees)}")
        laraster._writeGeoTiff(myOutPath, myMask.astype(np.uint8), myGeoTrans, myProjection, np.uint8, 0)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def subtractMasks(self, theOuterMask: str, theInnerMask: str) -> str:
        """Cells set in ``theOuterMask`` but not in ``theInnerMask`` (fallow = total − sown)."""
        from la.lib import laraster
        return self._registerTemp(laraster.subtractMasks, theOuterMask, theInnerMask)

    @staticmethod
    def maskTouchesBorder(theMaskPath: Optional[str]) -> bool:
        from la.lib import laraster
        return laraster.maskTouchesBorder(theMaskPath)

    def _registerTemp(self, theCall, *theArgs) -> str:
        """Run a :mod:`laraster` op and register its output as a temp raster.

        :param theCall: A ``laraster`` function returning an output path.
        :param theArgs: Positional arguments for ``theCall`` (the scratch
            directory is appended automatically).
        :return: The output path.
        :rtype: str
        :raises LaGrassError: If an input raster cannot be opened.
        """
        try:
            myOutPath = theCall(*theArgs, self.mScratchDir)
        except FileNotFoundError as myError:
            raise LaGrassError(str(myError)) from myError
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def _reclassPure(self, theCostRaster: str, theThreshold: float) -> str:
        """Pure-Python equivalent of ``if(cost < threshold, 1, null())``.

        :param theCostRaster: Absolute path of a cost-surface raster.
        :param theThreshold: Cost-distance threshold.
        :return: Absolute path of a 1/0 uint8 mask GeoTIFF (nodata=0).
        :rtype: str
        """
        from la.lib import laraster

        return self._registerTemp(laraster.reclassCost, theCostRaster, theThreshold)

    def _createMaskPure(
        self, theReclassed: str, theSuitabilityRaster: str,
    ) -> str:
        """Pure-Python equivalent of ``if(A >= 1 && B >= 1, 1, null())``.

        :param theReclassed: Output of :meth:`_reclassPure`.
        :param theSuitabilityRaster: Per-item suitability raster.
        :return: Absolute path of a 1/0 uint8 mask GeoTIFF (nodata=0).
        :rtype: str
        """
        from la.lib import laraster

        return self._registerTemp(laraster.createMask, theReclassed, theSuitabilityRaster)

    def _createInverseMaskPure(
        self,
        theCostRaster:      str,
        theThreshold:       float,
        theBaseSuitability: str,
    ) -> str:
        """Pure-Python equivalent of ``if(B >= 1 && A >= threshold, 1, null())``.

        :param theCostRaster: The cost surface.
        :param theThreshold: Cost threshold used for the catchment.
        :param theBaseSuitability: The suitability raster the catchment was
            allocated from.
        :return: Absolute path of a 1/0 uint8 leftover mask GeoTIFF.
        :rtype: str
        """
        from la.lib import laraster

        return self._registerTemp(
            laraster.createInverseMask, theCostRaster, theThreshold, theBaseSuitability,
        )

    def _mergeMapsPure(self, theA: str, theB: str) -> str:
        """Pure-Python equivalent of ``if(A >= 1 || B >= 1, 1, null())``.

        :param theA: First mask raster path.
        :param theB: Second mask raster path.
        :return: Absolute path of a 1/0 uint8 union mask GeoTIFF.
        :rtype: str
        """
        from la.lib import laraster

        return self._registerTemp(laraster.mergeMasks, theA, theB)

    def _readBand(self, thePath: str):
        """Read band 1 of a raster into a NumPy array.

        Thin wrapper over :func:`la.lib.laraster._readBand`, which keeps the
        Dataset reference alive for the duration of the read (chaining
        ``gdal.Open(...).GetRasterBand(1).ReadAsArray()`` on one line lets
        Python free the Dataset mid-call and segfaults).

        :param thePath: Absolute path of a single-band GDAL-readable raster.
        :return: 2-D NumPy array of the band's values.
        :raises LaGrassError: If the raster cannot be opened.
        """
        from la.lib import laraster

        try:
            myArray, _, _ = laraster._readBand(thePath)
        except FileNotFoundError as myError:
            raise LaGrassError(f"Could not open {thePath}") from myError
        return myArray

    def _writeMaskCoregistered(
        self, theMask, theReferenceRaster: str, theOutPath: str,
    ) -> None:
        """Write a uint8 ``{0,1}`` mask co-registered with a reference raster.

        Thin wrapper over :func:`la.lib.laraster._writeMaskCoregistered`
        (LZW, tiled, nodata 0, handles released so GDAL finalises the file).

        :param theMask: 2-D ``numpy.ndarray`` of ``uint8`` values (0 or 1).
        :param theReferenceRaster: Path to read geotransform + projection
            from. Cell grid must match ``theMask``.
        :param theOutPath: Absolute output path.
        :rtype: None
        """
        from la.lib import laraster

        laraster._writeMaskCoregistered(theMask, theReferenceRaster, theOutPath)

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _runAlg(self, theAlgId: Optional[str], theParams: dict) -> dict:
        """Wrap ``processing.run`` with a uniform error path."""
        if theAlgId is None:
            raise LaGrassError("Required GRASS algorithm is not available.")
        from qgis import processing  # imported lazily so non-QGIS test contexts can still import this module
        try:
            return processing.run(theAlgId, theParams)
        except Exception as e:
            raise LaGrassError(f"{theAlgId} failed: {e}") from e

    def _probeAlg(self, theIds) -> Optional[str]:
        """Return the first algorithm id that the processing registry knows about."""
        try:
            from qgis.core import QgsApplication
            myReg = QgsApplication.processingRegistry()
        except Exception:
            return None
        for myId in theIds:
            if myReg.algorithmById(myId) is not None:
                return myId
        return None

    def _regionString(self) -> str:
        """``"xmin,xmax,ymin,ymax"`` for the snapshotted DEM extent."""
        myExtent = self.mRegionExtent
        return (
            f"{myExtent.xMinimum()},{myExtent.xMaximum()},"
            f"{myExtent.yMinimum()},{myExtent.yMaximum()}"
        )

    def _tempPath(self, theStem: str) -> str:
        """Build a unique temp GeoTIFF path under the scratch dir."""
        myCounter = len(self._mTempRasters)
        return os.path.join(self.mScratchDir, f"_la_{theStem}_{myCounter:04d}.tif")

    def _uniformFrictionFromDem(self) -> str:
        """
        Synthesise a uniform-1 friction raster covering the DEM.

        The C++ code reused the DEM as friction (a bug); we follow what the
        algorithm actually wants — a uniform-cost raster with valid pixels
        wherever the DEM is defined.
        """
        myOutPath = self._tempPath("friction")
        myParams = self._mapcalcParams(
            theExpression="if(isnull(A), null(), 1)",
            theA=self.mDemPath,
            theOutput=myOutPath,
        )
        self._runAlg(self._mMapcalcId, myParams)
        self._mTempRasters.append(myOutPath)
        return myOutPath

    def _mapcalcParams(
        self,
        theExpression: str,
        theA: Optional[str] = None,
        theB: Optional[str] = None,
        theC: Optional[str] = None,
        theOutput: Optional[str] = None,
    ) -> dict:
        """Common parameter dict for ``grass:r.mapcalc.simple``."""
        myParams: dict = {
            "expression": theExpression,
            "output":     theOutput,
            "GRASS_REGION_PARAMETER":          self._regionString(),
            "GRASS_REGION_CELLSIZE_PARAMETER": self.mCellSize,
        }
        if theA is not None: myParams["a"] = theA
        if theB is not None: myParams["b"] = theB
        if theC is not None: myParams["c"] = theC
        return myParams
