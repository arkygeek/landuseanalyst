"""
test_lagis_shuna.py — exercise the pure-Python r.walk fallback against
the real thesis-era Shuna DEM.

Source data
-----------
``la/test/xmlData/GrassData/demShuna`` is a 2362 × 2464, 30 m GRASS-ASCII
DEM covering ~74 km × 71 km around the Chalcolithic settlement of Shuna
(southern Levant, UTM 36N). It was generated for the original C++
Landuse Analyst thesis runs.

Why a window, not the full raster
---------------------------------
The full DEM is ~5.8 M cells. An 8-connected, anisotropic Dijkstra at
that scale would take minutes and ~1 GB of RAM — fine for a one-off
research run, far too heavy for a smoke test. This script windows out a
200 × 200 region (6 km × 6 km) centred on the canonical thesis
settlement coordinates (744800 E, 3611100 N — the same point baked into
``test_lagrass_synth.py`` and the .ui defaults).

What this test asserts
----------------------
After driving ``LaGrass._makeWalkCostPure`` against the windowed DEM:

1. The output GeoTIFF exists, is readable, and matches the window shape.
2. The settlement cell has cost ~ 0 (Dijkstra source).
3. Walking-cost rises with radius (sample-based monotonicity check —
   eight points at 600 m all exceed eight points at 150 m).
4. Every cell in the window is finite (max-cost = 11 h walking; nothing
   in a 6 km radius should be unreachable at Tobler peak speed).

Run from the QGIS Python Console::

    exec(open('/path/to/la/test/test_lagis_shuna.py').read())

Standalone use (Linux dev env where the system ``python3`` resolves
``qgis.PyQt`` — i.e. PyQGIS installed via apt)::

    python3 la/test/test_lagis_shuna.py

Output rasters are written to ``testData/shunaCatchmentScratch/`` so you
can drop them on a QGIS map and look at them. That directory is
gitignored.
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

# 200 × 200 cells × 30 m = 6 km × 6 km — covers the Min-Pop scenario's
# ~268 ha demand comfortably, runs Dijkstra in a few seconds.
_WIN_SIZE = 200


# ---------------------------------------------------------------------------
# Step 1 — window the full DEM around the settlement
# ---------------------------------------------------------------------------
def _windowDemAroundSettlement(theSourcePath: str, theOutPath: str) -> str:
    """
    Read ``theSourcePath`` via GDAL, extract a ``_WIN_SIZE`` × ``_WIN_SIZE``
    window centred on the thesis settlement, and write a GeoTIFF with a
    geotransform that preserves the original georeferencing.

    :param theSourcePath: Absolute path of the source GRASS-ASCII DEM.
    :param theOutPath: Absolute path of the GeoTIFF to write.
    :return: ``theOutPath`` (for chaining).
    :rtype: str
    """
    myDataset = gdal.Open(theSourcePath)
    if myDataset is None:
        raise RuntimeError(f"Could not open {theSourcePath}")

    myGeoTrans   = myDataset.GetGeoTransform()
    myProjection = myDataset.GetProjection()
    myFullDem    = myDataset.GetRasterBand(1).ReadAsArray()
    myFullRows, myFullCols = myFullDem.shape

    # Inverse geotransform — assumes north-up: gt = (ox, pw, 0, oy, 0, -ph).
    myCenterCol = int((SETTLEMENT_X - myGeoTrans[0]) / myGeoTrans[1])
    myCenterRow = int((SETTLEMENT_Y - myGeoTrans[3]) / myGeoTrans[5])

    myHalf = _WIN_SIZE // 2
    myColStart = myCenterCol - myHalf
    myRowStart = myCenterRow - myHalf
    myColEnd   = myColStart + _WIN_SIZE
    myRowEnd   = myRowStart + _WIN_SIZE

    if not (0 <= myColStart and myColEnd <= myFullCols
            and 0 <= myRowStart and myRowEnd <= myFullRows):
        raise RuntimeError(
            f"Settlement window [{myRowStart}:{myRowEnd}, "
            f"{myColStart}:{myColEnd}] falls outside DEM "
            f"({myFullRows} × {myFullCols})."
        )

    myWindow = myFullDem[myRowStart:myRowEnd, myColStart:myColEnd]
    myNewOriginX = myGeoTrans[0] + myColStart * myGeoTrans[1]
    myNewOriginY = myGeoTrans[3] + myRowStart * myGeoTrans[5]
    myNewGeoTrans = (
        myNewOriginX, myGeoTrans[1], 0.0,
        myNewOriginY, 0.0, myGeoTrans[5],
    )

    myDriver = gdal.GetDriverByName("GTiff")
    myOutDs  = myDriver.Create(
        theOutPath, _WIN_SIZE, _WIN_SIZE, 1, gdal.GDT_Float32,
        options=["COMPRESS=LZW", "TILED=YES"],
    )
    myOutDs.SetGeoTransform(myNewGeoTrans)
    myOutDs.SetProjection(myProjection)
    myOutBand = myOutDs.GetRasterBand(1)
    myOutBand.WriteArray(myWindow.astype(np.float32))
    myOutBand.FlushCache()
    myOutDs.FlushCache()

    print(f"  Windowed DEM    → {os.path.relpath(theOutPath, _PROJECT_ROOT)}")
    print(f"    centre cell   = (row {myCenterRow}, col {myCenterCol})")
    print(f"    elev range    = [{float(myWindow.min()):.1f}, "
          f"{float(myWindow.max()):.1f}] m")
    return theOutPath


# ---------------------------------------------------------------------------
# Step 2 — duck-typed DEM-layer stub for LaGrass.__init__
# ---------------------------------------------------------------------------
class _StubDemLayer:
    """
    Minimum surface that :class:`la.lib.lagrass.LaGrass` reads off a DEM
    layer at construction time. The pure-Python ``_makeWalkCostPure``
    path doesn't touch ``extent()`` or ``rasterUnitsPerPixelX()`` — both
    are only consumed by the GRASS Processing path's ``_regionString``.
    They're here purely so ``LaGrass.__init__`` doesn't raise.

    :param theDemPath: Absolute path of the windowed DEM GeoTIFF.
    :type theDemPath: str
    """
    def __init__(self, theDemPath: str) -> None:
        self._mDemPath = theDemPath
        myDataset = gdal.Open(theDemPath)
        myGeoTrans = myDataset.GetGeoTransform()
        self._mCellSize = abs(myGeoTrans[1])

    def source(self) -> str:
        return self._mDemPath

    def extent(self):
        return None

    def rasterUnitsPerPixelX(self) -> float:
        return self._mCellSize


# ---------------------------------------------------------------------------
# Step 3 — assertions on the cost surface
# ---------------------------------------------------------------------------
def _assertWalkCostSurface(theCostPath: str) -> None:
    """
    Verify ``_makeWalkCostPure``'s output against a real-terrain DEM.

    Properties checked:

    * Output is readable, single-band, ``_WIN_SIZE`` × ``_WIN_SIZE``.
    * The seed cell (window centre) has cost ~ 0.
    * Sample mean cost at radius 600 m exceeds sample mean at 150 m.
    * Every cell in the window is finite (capped at 40 000 s).

    :param theCostPath: Absolute path of the walk-cost GeoTIFF.
    :raises AssertionError: On any failed property.
    """
    myDataset = gdal.Open(theCostPath)
    assert myDataset is not None, f"Could not open {theCostPath}"
    myCost = myDataset.GetRasterBand(1).ReadAsArray()
    assert myCost.shape == (_WIN_SIZE, _WIN_SIZE), \
        f"Cost shape {myCost.shape} != ({_WIN_SIZE}, {_WIN_SIZE})"

    myCenter = _WIN_SIZE // 2
    mySeedCost = float(myCost[myCenter, myCenter])
    assert mySeedCost < 1e-6, f"Seed cell cost {mySeedCost} should be ~0"

    # Eight cardinal+diagonal samples at each radius, averaged.
    # Radii in cells: 5 cells = 150 m, 20 cells = 600 m.
    def _sampleRing(theRadius: int) -> float:
        myOffsets = [
            ( theRadius,  0), (-theRadius,  0),
            ( 0,  theRadius), ( 0, -theRadius),
            ( theRadius,  theRadius), (-theRadius, -theRadius),
            ( theRadius, -theRadius), (-theRadius,  theRadius),
        ]
        myValues = [float(myCost[myCenter + dr, myCenter + dc])
                    for dr, dc in myOffsets]
        return sum(myValues) / len(myValues)

    myShortMean = _sampleRing(5)
    myLongMean  = _sampleRing(20)
    assert myLongMean > myShortMean, (
        f"Mean cost at 600 m ({myLongMean:.1f} s) should exceed mean at "
        f"150 m ({myShortMean:.1f} s) — walk-cost is not increasing "
        f"with radius."
    )

    myFiniteFrac = float(np.isfinite(myCost).sum()) / myCost.size
    assert myFiniteFrac == 1.0, (
        f"Expected every cell in the 6 km window to be reachable within "
        f"the 40000 s cap; only {myFiniteFrac:.4f} are finite."
    )

    print(f"  Seed cost       = {mySeedCost:.3f} s")
    print(f"  Mean cost @150m = {myShortMean:.1f} s")
    print(f"  Mean cost @600m = {myLongMean:.1f} s")
    print(f"  Finite fraction = {myFiniteFrac:.4f}")
    print(f"  Cost range      = [{float(np.nanmin(myCost)):.1f}, "
          f"{float(np.nanmax(myCost)):.1f}] s")


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
    print(f"Window:           {_WIN_SIZE} x {_WIN_SIZE} cells")
    print()

    print("Step 1: window the Shuna DEM around the settlement")
    myWindowedDem = _windowDemAroundSettlement(
        _SHUNA_DEM, os.path.join(_SCRATCH_DIR, "windowedDem.tif"),
    )

    print("\nStep 2: build LaGrass + run _makeWalkCostPure")
    # Import is deferred so the standalone helper functions above can be
    # imported without pulling in qgis.PyQt at module-load time (handy
    # if someone wants to reuse _windowDemAroundSettlement elsewhere).
    from la.lib.lagrass import LaGrass

    myStub  = _StubDemLayer(myWindowedDem)
    myGrass = LaGrass(myStub, _SCRATCH_DIR)
    myCostPath = myGrass._makeWalkCostPure(SETTLEMENT_X, SETTLEMENT_Y)
    print(f"  Walk-cost       → {os.path.relpath(myCostPath, _PROJECT_ROOT)}")

    print("\nStep 3: verify cost-surface properties")
    _assertWalkCostSurface(myCostPath)

    print("\nAll assertions passed.")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, _PROJECT_ROOT)
    raise SystemExit(main())
