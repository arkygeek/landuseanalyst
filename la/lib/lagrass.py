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
        Run ``grass:r.walk`` against the stored DEM, seeded at the settlement.

        Parameter values match the C++ original: Tobler's walking function
        coefficients (0.72, 6.0, 1.9998, -1.9998), lambda 0.75,
        slope_factor -0.2125, max_cost 40000, Knight's-move on.

        :param theX: Settlement easting in DEM CRS units.
        :param theY: Settlement northing in DEM CRS units.
        :return: Absolute path of the output cost-surface GeoTIFF.
        :rtype: str
        :raises LaGrassError: If ``grass:r.walk`` isn't available or fails.
        """
        if self._mWalkId is None:
            raise LaGrassError(
                "grass:r.walk is not available. Enable the GRASS Processing "
                "provider in QGIS, then restart the plugin."
            )
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
