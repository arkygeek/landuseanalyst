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

    def __init__(self, theDemLayer, theScratchDir: str) -> None:
        """
        :param theDemLayer: ``QgsRasterLayer`` for the DEM. Drives region.
        :type theDemLayer: qgis.core.QgsRasterLayer
        :param theScratchDir: Directory for temp + output rasters. Created
            if it doesn't exist.
        :type theScratchDir: str
        """
        super().__init__()
        os.makedirs(theScratchDir, exist_ok=True)
        self.mScratchDir = theScratchDir
        self.mDemPath = theDemLayer.source()
        self.mRegionExtent = theDemLayer.extent()
        self.mCellSize = float(theDemLayer.rasterUnitsPerPixelX())
        self._mTempRasters: List[str] = []
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
        if self._mWalkId is None:
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
        if self._mCostId is None:
            raise LaGrassError(
                "grass:r.cost is not available. Enable the GRASS Processing "
                "provider in QGIS, then restart the plugin."
            )
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

        Uses GDAL + NumPy directly (both ship with QGIS) — faster and more
        robust than parsing the text output of ``r.stats``.

        :param theMaskRaster: Path of a 1/null binary mask GeoTIFF.
        :return: Area in hectares.
        :rtype: float
        """
        from osgeo import gdal
        import numpy as np

        myDataset = gdal.Open(theMaskRaster)
        if myDataset is None:
            raise LaGrassError(f"Could not open mask raster {theMaskRaster}")
        myBand = myDataset.GetRasterBand(1)
        myArray = myBand.ReadAsArray()
        myGeoTransform = myDataset.GetGeoTransform()
        myCellAreaM2 = abs(myGeoTransform[1] * myGeoTransform[5])
        # Treat NaN and band-null as non-counting; "==1" captures the mask.
        myNoData = myBand.GetNoDataValue()
        if myNoData is not None:
            myCount = int(np.sum((myArray == 1) & (myArray != myNoData)))
        else:
            myCount = int(np.sum(myArray == 1))
        return myCount * myCellAreaM2 / 10000.0

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

        Why this exists
        ---------------
        The reference path is GRASS ``r.walk`` (called via ``grass:r.walk``
        in QGIS Processing). For a portable QGIS plugin we need a fallback:
        even when GRASS itself is installed, the QGIS Processing GRASS
        provider intermittently excludes ``r.walk`` from its registered
        algorithm list across QGIS bundles (the macOS standalone bundle
        and several Linux distributions don't expose it). End users would
        otherwise see "grass:r.walk is not available" errors despite
        having GRASS on their machine; this method gives every user the
        Walking Time analysis without any GRASS or extra-install
        dependency.

        Math
        ----
        Edge cost is computed per-pair-of-adjacent-cells using **Tobler's
        hiking function** (Tobler, 1993):

            v(slope) = V_PEAK * exp(-K * |slope + BIAS|)        [km/h]

        with the canonical parameters

            V_PEAK = 6.0    (km/h, peak walking speed)
            K      = 3.5    (slope penalty)
            BIAS   = 0.05   (peak occurs at gentle downhill)

        For each directed edge (cell A → cell B):

            slope     = (z_B − z_A) / horizontal_distance        [signed]
            velocity  = Tobler(slope)                            [km/h]
            edge_cost = horizontal_distance / velocity_in_m_per_s [seconds]

        The full grid is then represented as a directed sparse graph
        (8-connected, anisotropic — uphill and downhill from the same
        edge have different costs) and Dijkstra propagates accumulated
        cost from the settlement seed. Cells beyond ``MAX_COST`` seconds
        of walking are masked to null in the output.

        Output is a Float32 GeoTIFF co-registered with the DEM, with
        nodata = NaN, units = seconds of walking time. This matches the
        units the binary-search threshold sweep in
        :class:`la.lib.lacatchment.LaCatchment` expects (the bracket
        ``[0, 40000]`` corresponds to up to ~11 hours of walking, in
        line with the C++ original's max_cost setting).

        ACKNOWLEDGMENTS
        ---------------
        The reference algorithm — GRASS ``r.walk`` — was originally
        written by Steno Fontanari (ITC-IRST, 1992) and Pierre de
        Mouveaux, and is maintained by the GRASS GIS development team:
        Markus Neteler, Hamish Bowman, Roberto Flor and many others.
        Source: https://github.com/OSGeo/grass/tree/main/raster/r.walk

        The walking-velocity model is Waldo Tobler's hiking function:
        Tobler, W. (1993). "Three Presentations on Geographical Analysis
        and Modeling: Non-Isotropic Geographic Modeling; Speculations on
        the Geometry of Geography; and Global Spatial Analysis."
        National Center for Geographic Information and Analysis,
        Technical Report 93-1.

        The Landuse Analyst plugin's binary-search catchment workflow
        (which consumes the cost surface this method produces) is a
        Python port of Jason Jorgenson's C++ Landuse Analyst — see
        ``cppArchive/`` in this codebase.

        :param theX: Settlement easting in DEM CRS units.
        :param theY: Settlement northing in DEM CRS units.
        :return: Absolute path of a Float32 cost-surface GeoTIFF.
        :rtype: str
        :raises LaGrassError: On unreadable DEM or seed outside DEM extent.
        """
        import math
        import numpy as np
        from osgeo import gdal
        from scipy.sparse import csr_matrix
        from scipy.sparse.csgraph import dijkstra

        # Tobler's hiking function parameters — see method docstring.
        _V_PEAK_KMH    = 6.0
        _SLOPE_PENALTY = 3.5
        _DOWNHILL_BIAS = 0.05
        _MAX_COST_SEC  = 40000.0     # ~11 h walking — matches C++ max_cost

        # --- 1. Read DEM into a NumPy array, capture georeferencing ---
        myDataset = gdal.Open(self.mDemPath)
        if myDataset is None:
            raise LaGrassError(f"Could not open DEM {self.mDemPath}")
        myDem        = myDataset.GetRasterBand(1).ReadAsArray().astype(np.float64)
        myGeoTrans   = myDataset.GetGeoTransform()
        myProjection = myDataset.GetProjection()
        myCellX      = abs(myGeoTrans[1])
        myCellY      = abs(myGeoTrans[5])
        myCellDiag   = math.sqrt(myCellX ** 2 + myCellY ** 2)
        myRows, myCols = myDem.shape

        # --- 2. Locate the seed cell from settlement coordinates ---
        # GeoTransform: (originX, pixelW, 0, originY, 0, -pixelH) for
        # north-up rasters. Inverse is straightforward.
        mySeedCol = int((theX - myGeoTrans[0]) / myGeoTrans[1])
        mySeedRow = int((theY - myGeoTrans[3]) / myGeoTrans[5])
        if not (0 <= mySeedRow < myRows and 0 <= mySeedCol < myCols):
            raise LaGrassError(
                f"Settlement ({theX}, {theY}) maps to cell "
                f"({mySeedRow}, {mySeedCol}) outside DEM "
                f"({myRows} × {myCols})."
            )

        # --- 3. Build a directed sparse cost graph (8-neighbor) ---
        # For each of the 8 directions we vectorise across the whole DEM:
        #   * compute slope from "src" cells to "dst" cells (signed)
        #   * compute Tobler velocity (km/h) per edge
        #   * convert to edge-cost in seconds
        # Then accumulate into COO arrays for a single csr_matrix at the end.
        myDirections = [
            (-1,  0, myCellY),     # N
            (-1,  1, myCellDiag),  # NE
            ( 0,  1, myCellX),     # E
            ( 1,  1, myCellDiag),  # SE
            ( 1,  0, myCellY),     # S
            ( 1, -1, myCellDiag),  # SW
            ( 0, -1, myCellX),     # W
            (-1, -1, myCellDiag),  # NW
        ]

        myRowIdxList:  List[np.ndarray] = []
        myColIdxList:  List[np.ndarray] = []
        myDataList:    List[np.ndarray] = []

        for myDr, myDc, myEdgeLen in myDirections:
            # In-bounds windows for src (where dst exists) and dst.
            mySrcRowStart, mySrcRowStop = max(0, -myDr), min(myRows, myRows - myDr)
            mySrcColStart, mySrcColStop = max(0, -myDc), min(myCols, myCols - myDc)
            myDstRowStart, myDstRowStop = max(0,  myDr), min(myRows, myRows + myDr)
            myDstColStart, myDstColStop = max(0,  myDc), min(myCols, myCols + myDc)

            mySrcZ = myDem[mySrcRowStart:mySrcRowStop, mySrcColStart:mySrcColStop]
            myDstZ = myDem[myDstRowStart:myDstRowStop, myDstColStart:myDstColStop]

            # Signed slope: positive = uphill from src to dst.
            mySlope = (myDstZ - mySrcZ) / myEdgeLen

            # Tobler velocity (km/h); convert to m/s for cost-in-seconds.
            myVelKmh = _V_PEAK_KMH * np.exp(
                -_SLOPE_PENALTY * np.abs(mySlope + _DOWNHILL_BIAS)
            )
            myVelMs = myVelKmh * (1000.0 / 3600.0)
            # Clamp to a tiny positive so absolute cliffs don't blow up.
            myEdgeCost = myEdgeLen / np.maximum(myVelMs, 1e-6)

            # Flatten (row, col) → flat index for src and dst.
            mySrcRowGrid, mySrcColGrid = np.meshgrid(
                np.arange(mySrcRowStart, mySrcRowStop),
                np.arange(mySrcColStart, mySrcColStop),
                indexing="ij",
            )
            myDstRowGrid, myDstColGrid = np.meshgrid(
                np.arange(myDstRowStart, myDstRowStop),
                np.arange(myDstColStart, myDstColStop),
                indexing="ij",
            )
            myRowIdxList.append((mySrcRowGrid * myCols + mySrcColGrid).ravel())
            myColIdxList.append((myDstRowGrid * myCols + myDstColGrid).ravel())
            myDataList.append(myEdgeCost.ravel())

        myRowIdx = np.concatenate(myRowIdxList)
        myColIdx = np.concatenate(myColIdxList)
        myCosts  = np.concatenate(myDataList)
        myN      = myRows * myCols
        myGraph  = csr_matrix((myCosts, (myRowIdx, myColIdx)), shape=(myN, myN))

        # --- 4. Dijkstra from the seed ---
        mySeedFlat = mySeedRow * myCols + mySeedCol
        myDistFlat = dijkstra(csgraph=myGraph, indices=mySeedFlat)
        myCostGrid = myDistFlat.reshape(myRows, myCols)

        # Mask cells beyond max_cost or unreachable (∞).
        myCostGrid[~np.isfinite(myCostGrid)] = np.nan
        myCostGrid[myCostGrid > _MAX_COST_SEC] = np.nan

        # --- 5. Write the output GeoTIFF ---
        myOutPath = self._tempPath("walkCost_pure")
        myDriver = gdal.GetDriverByName("GTiff")
        myOutDs  = myDriver.Create(
            myOutPath, myCols, myRows, 1, gdal.GDT_Float32,
            options=["COMPRESS=LZW", "TILED=YES"],
        )
        myOutDs.SetGeoTransform(myGeoTrans)
        myOutDs.SetProjection(myProjection)
        myOutBand = myOutDs.GetRasterBand(1)
        myOutBand.SetNoDataValue(float("nan"))
        myOutBand.WriteArray(myCostGrid.astype(np.float32))
        myOutBand.FlushCache()
        myOutDs.FlushCache()
        self._mTempRasters.append(myOutPath)
        self.message.emit(
            f"Built walk-cost surface (pure-Python Tobler) from "
            f"({theX:.1f}, {theY:.1f})."
        )
        return myOutPath

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
