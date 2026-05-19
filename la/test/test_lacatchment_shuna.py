"""
test_lacatchment_shuna.py — end-to-end smoke test for the catchment
orchestrator (:class:`la.lib.lacatchment.LaCatchment`) running against
the real Shuna DEM.

What this exercises (that :mod:`test_lagis_shuna` doesn't)
----------------------------------------------------------
``test_lagis_shuna`` only drove the pure-Python r.walk replacement.
This script wires up the full orchestrator path:

* ``LaCatchment.prepareCostSurface`` → ``LaGrass.makeWalkCost``
  (pure-Python fallback because no QGIS Processing app is running
  under standalone ``python3``)
* ``LaCatchment._partitionItems`` → reads ``mAreaTargetsCropsMap`` +
  ``mCropsMap`` off the model, fetches per-item parameters via
  monkey-patched ``LaUtils.getCrop`` / ``LaUtils.getCropParameter``
* ``LaCatchment.analyseItem`` → the 17-iteration binary search,
  which on every iteration calls ``LaGrass.reclass`` +
  ``LaGrass.createMask`` + ``LaGrass.getArea`` — all three
  going through the pure-Python r.mapcalc fallbacks added in this
  session
* ``LaGrass.writeOutput`` → promotes the converged-iteration mask
  to a stable output path
* ``LaGrass.cleanup`` → drops intermediate temp rasters

Scenario
--------
A single dedicated crop ("WheatTest") with a target of 50 Ha and a
suitability raster covering the "low ground" inside the windowed Shuna
DEM (elevation between -100 m and 100 m — this matches real Jordan-Valley
floor terrain found in the windowed area). No animals, no commons.

The settlement and DEM window match ``test_lagis_shuna``: 6 km × 6 km at
30 m centred on (744800, 3611100) — UTM 36N, Shuna site.

Asserts
-------
1. Results contain exactly one ``AnalyseResult``.
2. Status is ``SearchStatus.Converged``.
3. ``|achievedHa - targetHa|`` is within ``precision% / 2`` of target.
4. ``outputPath`` exists on disk.

Run from QGIS Python Console::

    exec(open('/path/to/la/test/test_lacatchment_shuna.py').read())

Standalone (Linux dev env with PyQGIS via apt)::

    python3 la/test/test_lacatchment_shuna.py
"""

import os
import sys

import numpy as np
from osgeo import gdal


# ---------------------------------------------------------------------------
# Paths + canonical thesis coordinates
# ---------------------------------------------------------------------------
SETTLEMENT_X = 744800.0
SETTLEMENT_Y = 3611100.0

_TEST_DIR     = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_TEST_DIR, "..", ".."))
_SHUNA_DEM    = os.path.join(_TEST_DIR, "xmlData", "GrassData", "demShuna")
_SCRATCH_DIR  = os.path.join(_PROJECT_ROOT, "testData", "shunaCatchmentScratch")
_WIN_SIZE     = 200

# Scenario parameters
_TARGET_HA    = 50.0
_PRECISION    = 5     # percent, matches LaModel default


# ---------------------------------------------------------------------------
# Duck-typed stand-ins
# ---------------------------------------------------------------------------
class _Bbox:
    """Duck-types ``qgis.core.QgsRectangle`` for ``prepareCostSurface``."""
    def __init__(self, theXmin, theXmax, theYmin, theYmax):
        self._mXmin = theXmin
        self._mXmax = theXmax
        self._mYmin = theYmin
        self._mYmax = theYmax

    def xMinimum(self): return self._mXmin
    def xMaximum(self): return self._mXmax
    def yMinimum(self): return self._mYmin
    def yMaximum(self): return self._mYmax


class _DemLayer:
    """Minimum surface ``LaGrass.__init__`` reads off a DEM layer.

    Unlike :class:`la.test.test_lagis_shuna._StubDemLayer` (which leaves
    ``extent()`` as ``None``) this stub returns a real bounding-box-like
    object because the orchestrator's ``prepareCostSurface`` checks the
    settlement coords against it before kicking off the cost surface.

    :param theDemPath: Absolute path of the windowed DEM GeoTIFF.
    :type theDemPath: str
    """
    def __init__(self, theDemPath: str) -> None:
        myDataset = gdal.Open(theDemPath)
        myGeoTrans = myDataset.GetGeoTransform()
        myCols = myDataset.RasterXSize
        myRows = myDataset.RasterYSize
        self._mDemPath  = theDemPath
        self._mCellSize = abs(myGeoTrans[1])
        # gt = (originX, pixelW, 0, originY, 0, -pixelH) for north-up rasters.
        myXmax = myGeoTrans[0] + myCols * myGeoTrans[1]
        myYmin = myGeoTrans[3] + myRows * myGeoTrans[5]
        self._mExtent = _Bbox(myGeoTrans[0], myXmax, myYmin, myGeoTrans[3])

    def source(self) -> str:                return self._mDemPath
    def extent(self):                       return self._mExtent
    def rasterUnitsPerPixelX(self) -> float: return self._mCellSize


class _StubCrop:
    """Duck-types ``LaCrop`` — only ``.name`` is read by the orchestrator."""
    def __init__(self, theName: str) -> None:
        self.name = theName


class _StubParameter:
    """Duck-types ``LaCropParameter`` — ``.name``, ``.rasterName``, and
    ``.useCommonLand`` are the only attributes :meth:`_partitionItems`
    consults.
    """
    def __init__(
        self,
        theName:        str,
        theRasterName:  str,
        theUseCommon:   bool = False,
    ) -> None:
        self.name                  = theName
        self.rasterName            = theRasterName
        self.useCommonLand         = theUseCommon
        self.useCommonGrazingLand  = theUseCommon


class _StubModel:
    """Minimum LaModel-shaped object for :meth:`runCatchmentAnalysis`.

    The orchestrator only reads ``easting``, ``northing``, ``precision``,
    plus the four maps below. Diet calculations are bypassed entirely —
    we set the target hectares directly.
    """
    def __init__(
        self,
        theEasting:     float,
        theNorthing:    float,
        theCropsMap:    dict,
        theCropTargets: dict,
        thePrecision:   int = 5,
    ) -> None:
        self.easting              = theEasting
        self.northing             = theNorthing
        self.precision            = thePrecision
        self.mCropsMap            = theCropsMap
        self.mAreaTargetsCropsMap = theCropTargets
        self.mAnimalsMap            = {}
        self.mAreaTargetsAnimalsMap = {}


# ---------------------------------------------------------------------------
# Windowed DEM + suitability raster setup
# ---------------------------------------------------------------------------
def _windowDem(theSourcePath: str, theOutPath: str) -> str:
    """Window a 200x200 region around the settlement; write GeoTIFF.

    Reuses the math from :mod:`la.test.test_lagis_shuna._windowDemAroundSettlement`
    but keeps this script standalone — no inter-test imports — so it can
    be exec'd from the QGIS Python Console without path fiddling.
    """
    myDataset = gdal.Open(theSourcePath)
    myGeoTrans = myDataset.GetGeoTransform()
    myProjection = myDataset.GetProjection()
    myDem = myDataset.GetRasterBand(1).ReadAsArray()

    myCenterCol = int((SETTLEMENT_X - myGeoTrans[0]) / myGeoTrans[1])
    myCenterRow = int((SETTLEMENT_Y - myGeoTrans[3]) / myGeoTrans[5])
    myHalf = _WIN_SIZE // 2
    myColStart = myCenterCol - myHalf
    myRowStart = myCenterRow - myHalf
    myWindow = myDem[
        myRowStart:myRowStart + _WIN_SIZE,
        myColStart:myColStart + _WIN_SIZE,
    ]
    myNewGeoTrans = (
        myGeoTrans[0] + myColStart * myGeoTrans[1], myGeoTrans[1], 0.0,
        myGeoTrans[3] + myRowStart * myGeoTrans[5], 0.0, myGeoTrans[5],
    )

    myOutDs = gdal.GetDriverByName("GTiff").Create(
        theOutPath, _WIN_SIZE, _WIN_SIZE, 1, gdal.GDT_Float32,
        options=["COMPRESS=LZW", "TILED=YES"],
    )
    myOutDs.SetGeoTransform(myNewGeoTrans)
    myOutDs.SetProjection(myProjection)
    myBand = myOutDs.GetRasterBand(1)
    myBand.WriteArray(myWindow.astype(np.float32))
    myBand.FlushCache()
    myOutDs.FlushCache()
    return theOutPath


def _buildSuitabilityRaster(theWindowedDem: str, theOutPath: str) -> str:
    """Suitability = 1 wherever the windowed DEM is between -100 and 100 m.

    This matches "the low ground" in the real Jordan-Valley terrain
    captured by the windowed Shuna DEM (elevation range ~-265..223 m),
    giving us a recognisable spatial pattern with plenty of area for a
    50 Ha binary search to converge against.
    """
    myDataset = gdal.Open(theWindowedDem)
    myDem = myDataset.GetRasterBand(1).ReadAsArray()
    mySuit = ((myDem >= -100.0) & (myDem <= 100.0)).astype(np.uint8)
    myOutDs = gdal.GetDriverByName("GTiff").Create(
        theOutPath, mySuit.shape[1], mySuit.shape[0], 1, gdal.GDT_Byte,
        options=["COMPRESS=LZW", "TILED=YES"],
    )
    myOutDs.SetGeoTransform(myDataset.GetGeoTransform())
    myOutDs.SetProjection(myDataset.GetProjection())
    myBand = myOutDs.GetRasterBand(1)
    myBand.SetNoDataValue(0)
    myBand.WriteArray(mySuit)
    myBand.FlushCache()
    myOutDs.FlushCache()
    return theOutPath


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    if not os.path.isfile(_SHUNA_DEM):
        print(f"ERROR: missing test fixture {_SHUNA_DEM}", file=sys.stderr)
        return 1

    os.makedirs(_SCRATCH_DIR, exist_ok=True)
    print(f"Source DEM:       {os.path.relpath(_SHUNA_DEM, _PROJECT_ROOT)}")
    print(f"Scratch dir:      {os.path.relpath(_SCRATCH_DIR, _PROJECT_ROOT)}")
    print(f"Settlement:       ({SETTLEMENT_X}, {SETTLEMENT_Y})")
    print(f"Target crop area: {_TARGET_HA} Ha")
    print(f"Precision:        ±{_PRECISION / 2:.1f}% half-window")
    print()

    print("Step 1: window the DEM + build suitability raster")
    myWindowedDem = _windowDem(
        _SHUNA_DEM, os.path.join(_SCRATCH_DIR, "windowedDem.tif"),
    )
    mySuit = _buildSuitabilityRaster(
        myWindowedDem, os.path.join(_SCRATCH_DIR, "suitWheatTest.tif"),
    )
    print(f"  windowed DEM    → {os.path.relpath(myWindowedDem, _PROJECT_ROOT)}")
    print(f"  suitability     → {os.path.relpath(mySuit, _PROJECT_ROOT)}")

    # Deferred imports keep this module's top-level free of QGIS dependencies,
    # mirroring the test_lagis_shuna convention.
    from la.lib.lagrass     import LaGrass
    from la.lib.lacatchment import (
        LaCatchment, LaCatchmentInputs, DistanceMethod, SearchStatus,
    )
    from la.lib            import lautils

    print("\nStep 2: monkey-patch LaUtils to serve the stub crop + parameter")
    myCropGuid       = "test-crop-guid-1"
    myParameterGuid  = "test-param-guid-1"
    myCropsByGuid    = {myCropGuid: _StubCrop("WheatTest")}
    myParamsByGuid   = {myParameterGuid: _StubParameter("WheatTestParam", mySuit, False)}
    myOriginalGetCrop          = lautils.LaUtils.getCrop
    myOriginalGetCropParameter = lautils.LaUtils.getCropParameter

    try:
        lautils.LaUtils.getCrop          = staticmethod(
            lambda theGuid: myCropsByGuid.get(theGuid))
        lautils.LaUtils.getCropParameter = staticmethod(
            lambda theGuid: myParamsByGuid.get(theGuid))

        print("\nStep 3: construct model + LaGrass + LaCatchment")
        myModel = _StubModel(
            theEasting     = SETTLEMENT_X,
            theNorthing    = SETTLEMENT_Y,
            theCropsMap    = {myCropGuid: myParameterGuid},
            theCropTargets = {myCropGuid: _TARGET_HA},
            thePrecision   = _PRECISION,
        )
        myGrass     = LaGrass(_DemLayer(myWindowedDem), _SCRATCH_DIR)
        myCatchment = LaCatchment(myGrass, _PRECISION)
        myInputs    = LaCatchmentInputs(
            demLayerId           = "",      # _resolveLayerPath sees None ⇒ no QgsProject lookup
            commonCropLayerId    = None,
            commonGrazingLayerId = None,
            method               = DistanceMethod.WalkingTime,
        )
        print(f"  _mMapcalcId = {myGrass._mMapcalcId!r}  "
              f"(expect None ⇒ pure-Python mapcalc fallbacks engage)")

        print("\nStep 4: runCatchmentAnalysis")
        myResults = myCatchment.runCatchmentAnalysis(myModel, myInputs)
    finally:
        lautils.LaUtils.getCrop          = myOriginalGetCrop
        lautils.LaUtils.getCropParameter = myOriginalGetCropParameter

    print("\nStep 5: verify results")
    assert len(myResults.items) == 1, (
        f"Expected 1 result, got {len(myResults.items)}: {myResults.items}"
    )
    myItem = myResults.items[0]
    print(f"  item:         {myItem.itemName}")
    print(f"  status:       {myItem.status.name}")
    print(f"  threshold:    {myItem.threshold:.1f} s walking time")
    print(f"  achieved Ha:  {myItem.achievedHa:.3f}  (target {myItem.targetHa})")
    print(f"  output:       {os.path.relpath(myItem.outputPath, _PROJECT_ROOT) if myItem.outputPath else '(none)'}")

    assert myItem.status is SearchStatus.Converged, (
        f"Expected Converged, got {myItem.status.name}: {myItem.message}"
    )
    myHalfWindow = _TARGET_HA * (_PRECISION / 100.0) / 2.0
    assert abs(myItem.achievedHa - _TARGET_HA) <= myHalfWindow, (
        f"|{myItem.achievedHa} - {_TARGET_HA}| > {myHalfWindow} half-window"
    )
    assert myItem.outputPath and os.path.isfile(myItem.outputPath), (
        f"outputPath {myItem.outputPath} should exist on disk"
    )
    print("\nAll assertions passed.")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, _PROJECT_ROOT)
    raise SystemExit(main())
