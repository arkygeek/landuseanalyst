"""
Tests for :mod:`la.lib.laraster` — the pure-NumPy catchment raster engine.

No ``qgis`` import anywhere: these run under any Python with ``numpy`` and
``osgeo``. ``scipy`` is optional (the heap fallback is exercised by blocking
it in :data:`sys.modules`).
"""

import math
import sys

import numpy as np
import pytest
from osgeo import gdal

from la.lib import laraster


_CELL = 30.0
_ORIGIN_X = 744000.0
_ORIGIN_Y = 3612000.0
_UTM36N = (
    'PROJCS["WGS 84 / UTM zone 36N",GEOGCS["WGS 84",DATUM["WGS_1984",'
    'SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],'
    'UNIT["degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],'
    'PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",33],'
    'PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],'
    'PARAMETER["false_northing",0],UNIT["metre",1]]'
)

#: Flat-ground Tobler speed: 6.0 * exp(-3.5 * |0 + 0.05|) km/h, in m/s.
_FLAT_V_MS = 6.0 * math.exp(-3.5 * 0.05) * 1000.0 / 3600.0
_STRAIGHT_SEC = _CELL / _FLAT_V_MS


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _geoTransform(theCell: float = _CELL) -> tuple:
    return (_ORIGIN_X, theCell, 0.0, _ORIGIN_Y, 0.0, -theCell)


def _writeRaster(thePath, theArray, theDtype=np.float32, theNoData=None, theCell=_CELL) -> str:
    return laraster._writeGeoTiff(
        str(thePath), np.asarray(theArray), _geoTransform(theCell), _UTM36N, theDtype, theNoData,
    )


def _cellCentre(theRow: int, theCol: int, theCell: float = _CELL) -> tuple:
    """Map coordinates of a cell centre for the shared geotransform."""
    return (_ORIGIN_X + (theCol + 0.5) * theCell, _ORIGIN_Y - (theRow + 0.5) * theCell)


def _read(thePath) -> np.ndarray:
    return laraster._readBand(thePath)[0]


def _octagonalDistance(theRows: int, theCols: int, theSeedRow: int, theSeedCol: int,
                       theCell: float = _CELL) -> np.ndarray:
    """8-neighbour shortest path length on a flat grid, in metres."""
    myDr = np.abs(np.arange(theRows)[:, None] - theSeedRow)
    myDc = np.abs(np.arange(theCols)[None, :] - theSeedCol)
    myDiag = np.minimum(myDr, myDc)
    myStraight = np.maximum(myDr, myDc) - myDiag
    return myStraight * theCell + myDiag * theCell * math.sqrt(2.0)


def _blockScipy(theMonkeypatch) -> None:
    """Make every ``import scipy...`` raise ImportError for this test."""
    for myName in ("scipy", "scipy.sparse", "scipy.sparse.csgraph"):
        theMonkeypatch.setitem(sys.modules, myName, None)


# ---------------------------------------------------------------------------
# (a) flat walk cost == octagonal distance / flat Tobler speed
# ---------------------------------------------------------------------------
def test_flat_walk_cost_matches_octagonal_distance(tmp_path):
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((100, 100)))
    myX, myY = _cellCentre(50, 50)

    myOut = laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "scratch"))
    myCost = _read(myOut).astype(np.float64)

    myExpected = _octagonalDistance(100, 100, 50, 50) / _FLAT_V_MS
    assert np.isfinite(myCost).all()
    assert myCost[50, 50] == 0.0
    np.testing.assert_allclose(myCost, myExpected, rtol=1e-6, atol=1e-6)


def test_walk_cost_output_is_finalised_float32_nan_nodata(tmp_path):
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((20, 20)))
    myOut = laraster.makeWalkCost(myDem, *_cellCentre(10, 10), str(tmp_path))

    myDs = gdal.Open(myOut)
    assert myDs is not None
    myBand = myDs.GetRasterBand(1)
    assert myBand.DataType == gdal.GDT_Float32
    assert math.isnan(myBand.GetNoDataValue())
    assert myDs.GetGeoTransform() == pytest.approx(_geoTransform())
    myBand = None
    myDs = None


def test_seed_outside_dem_raises(tmp_path):
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((20, 20)))
    with pytest.raises(ValueError):
        laraster.makeWalkCost(myDem, _ORIGIN_X - 100.0, _ORIGIN_Y, str(tmp_path))


def test_max_cost_masks_far_cells_to_nan(tmp_path):
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((60, 60)))
    myOut = laraster.makeWalkCost(
        myDem, *_cellCentre(0, 0), str(tmp_path), theMaxCostSec=10.0 * _STRAIGHT_SEC,
    )
    myCost = _read(myOut)
    assert np.isnan(myCost[59, 59])
    assert np.isfinite(myCost[5, 5])
    assert np.nanmax(myCost) <= 10.0 * _STRAIGHT_SEC * (1 + 1e-6)


# ---------------------------------------------------------------------------
# (b) Euclidean cost == octagonal metric distance
# ---------------------------------------------------------------------------
def test_euclidean_cost_is_octagonal_metric_distance(tmp_path):
    # Non-flat DEM on purpose: the Euclidean surface must ignore elevation.
    myRng = np.random.default_rng(1)
    myDem = _writeRaster(tmp_path / "bumpy.tif", myRng.random((100, 100)) * 50.0)

    myOut = laraster.makeEuclideanCost(myDem, *_cellCentre(50, 50), str(tmp_path))
    myCost = _read(myOut).astype(np.float64)

    np.testing.assert_allclose(myCost, _octagonalDistance(100, 100, 50, 50), rtol=1e-6)


# ---------------------------------------------------------------------------
# (c) heap fallback == scipy
# ---------------------------------------------------------------------------
def test_heap_dijkstra_matches_scipy_on_random_dem():
    pytest.importorskip("scipy")
    myRng = np.random.default_rng(7)
    myDem = myRng.random((40, 40)) * 20.0
    myRows, myCols, myCost = laraster._toblerEdges(myDem, _CELL, _CELL, _CELL * math.sqrt(2.0))
    myN = myDem.size
    mySeed = 20 * 40 + 20

    myHeap  = laraster._dijkstraHeap(myRows, myCols, myCost, myN, mySeed)
    myScipy = laraster._dijkstraScipy(myRows, myCols, myCost, myN, mySeed)

    assert np.isfinite(myHeap).all()
    np.testing.assert_allclose(myHeap, myScipy, rtol=0, atol=1e-9)


def test_heap_dijkstra_sums_duplicate_edges_like_csr():
    pytest.importorskip("scipy")
    # Two parallel 0->1 edges (weights 1 and 2) must coalesce to a single
    # weight-3 edge, exactly as csr_matrix((data, (i, j))) does.
    myRow  = np.array([0, 0, 1], dtype=np.int64)
    myCol  = np.array([1, 1, 2], dtype=np.int64)
    myCost = np.array([1.0, 2.0, 5.0])
    myHeap  = laraster._dijkstraHeap(myRow, myCol, myCost, 3, 0)
    myScipy = laraster._dijkstraScipy(myRow, myCol, myCost, 3, 0)
    np.testing.assert_array_equal(myHeap, [0.0, 3.0, 8.0])
    np.testing.assert_array_equal(myHeap, myScipy)


def test_walk_cost_without_scipy_uses_heap_and_matches(tmp_path, monkeypatch):
    pytest.importorskip("scipy")
    myRng = np.random.default_rng(3)
    myDem = _writeRaster(tmp_path / "rand.tif", myRng.random((40, 40)) * 20.0)
    myX, myY = _cellCentre(20, 20)

    myWithScipy = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "a")))

    _blockScipy(monkeypatch)
    myWithHeap = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "b")))

    np.testing.assert_array_equal(myWithHeap, myWithScipy)


def test_without_scipy_large_grid_raises_import_error(monkeypatch):
    _blockScipy(monkeypatch)
    myDem = np.zeros((520, 520))
    with pytest.raises(ImportError, match=r"scipy is required for grids larger than 512×512"):
        laraster._dijkstraFromSeeds(
            myDem, _CELL, _CELL,
            np.array([260]), np.array([260]), np.array([0.0]),
        )


def test_heap_fallback_limit_is_inclusive_at_512_squared(monkeypatch):
    _blockScipy(monkeypatch)
    # Exactly 512² cells must still be attempted (not raise). Use a graph with
    # no edges so the heap run is instant.
    myN = 512 * 512
    myDist = laraster._solveShortestPaths(
        np.zeros(0, dtype=np.int64), np.zeros(0, dtype=np.int64), np.zeros(0), myN + 1, myN,
    )
    assert myDist[myN] == 0.0 and np.isinf(myDist[:myN]).all()


# ---------------------------------------------------------------------------
# (d) tiled path >= single pass, equal almost everywhere
# ---------------------------------------------------------------------------
def test_tiled_path_over_estimates_and_mostly_matches_single_pass(tmp_path, monkeypatch):
    myRng = np.random.default_rng(11)
    myDem = _writeRaster(tmp_path / "rand300.tif", myRng.random((300, 300)) * 3.0)
    myX, myY = _cellCentre(150, 150)

    mySingle = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "s"))).astype(np.float64)

    # Shrink the tiles so a 300×300 grid really is split (3×3 tiles, 20-px halo).
    monkeypatch.setattr(laraster, "_TILE_SIZE", 100)
    monkeypatch.setattr(laraster, "_TILE_HALO", 20)
    myTiled = _read(
        laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "t"), theForceTiled=True)
    ).astype(np.float64)

    assert np.isfinite(mySingle).all() and np.isfinite(myTiled).all()
    # Every tiled distance is a real path, so it can never beat the exact answer.
    assert np.all(myTiled >= mySingle - 1e-6)
    myEqual = np.isclose(myTiled, mySingle, rtol=1e-9, atol=1e-6)
    assert myEqual.mean() > 0.99, f"only {myEqual.mean():.4%} of cells agree"


def test_force_tiled_on_single_tile_grid_is_exact(tmp_path):
    myRng = np.random.default_rng(5)
    myDem = _writeRaster(tmp_path / "rand.tif", myRng.random((80, 80)) * 10.0)
    myX, myY = _cellCentre(40, 40)
    mySingle = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "s")))
    myTiled = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "t"), theForceTiled=True))
    np.testing.assert_array_equal(myTiled, mySingle)


# ---------------------------------------------------------------------------
# (e) slope
# ---------------------------------------------------------------------------
def test_slope_from_planar_10_degree_dem(tmp_path):
    myCols = np.arange(60, dtype=np.float64)[None, :]
    myDem = np.repeat(np.tan(math.radians(10.0)) * myCols * _CELL, 50, axis=0)
    myDemPath = _writeRaster(tmp_path / "plane.tif", myDem, theDtype=np.float64)

    mySlopePath = laraster.slopeFromDem(myDemPath, str(tmp_path))
    mySlope = _read(mySlopePath)
    assert mySlope.dtype == np.float32
    assert np.abs(mySlope[1:-1, 1:-1] - 10.0).max() < 0.05

    myMaskPath = laraster.slopeMask(mySlopePath, 9.0, str(tmp_path))
    myMask = _read(myMaskPath)
    assert myMask.dtype == np.uint8
    assert not myMask.any()

    myLenientPath = laraster.slopeMask(mySlopePath, 11.0, str(tmp_path))
    assert _read(myLenientPath).all()


def test_slope_mask_excludes_nan(tmp_path):
    mySlope = np.full((5, 5), 3.0, dtype=np.float32)
    mySlope[2, 2] = np.nan
    myPath = _writeRaster(tmp_path / "slope.tif", mySlope, theNoData=float("nan"))
    myMask = _read(laraster.slopeMask(myPath, 5.0, str(tmp_path)))
    assert myMask.sum() == 24 and myMask[2, 2] == 0


# ---------------------------------------------------------------------------
# (f) mask algebra + area on tiny arrays
# ---------------------------------------------------------------------------
def test_mask_algebra_and_area(tmp_path):
    myA = np.array([[1, 1, 0],
                    [1, 0, 0],
                    [0, 0, 0]], dtype=np.uint8)
    myB = np.array([[0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0]], dtype=np.uint8)
    myAPath = _writeRaster(tmp_path / "a.tif", myA, theDtype=np.uint8, theNoData=0)
    myBPath = _writeRaster(tmp_path / "b.tif", myB, theDtype=np.uint8, theNoData=0)

    myMerge = _read(laraster.mergeMasks(myAPath, myBPath, str(tmp_path)))
    np.testing.assert_array_equal(myMerge, (myA | myB))

    mySub = _read(laraster.subtractMasks(myAPath, myBPath, str(tmp_path)))
    np.testing.assert_array_equal(mySub, [[1, 0, 0], [1, 0, 0], [0, 0, 0]])

    myAnd = _read(laraster.createMask(myAPath, myBPath, str(tmp_path)))
    np.testing.assert_array_equal(myAnd, (myA & myB))

    # 30 m cells: one cell = 0.09 ha.
    assert laraster.getAreaHa(myAPath) == pytest.approx(3 * 0.09)
    assert laraster.getAreaHa(myBPath) == pytest.approx(3 * 0.09)
    myMergePath = laraster.mergeMasks(myAPath, myBPath, str(tmp_path))
    assert laraster.getAreaHa(myMergePath) == pytest.approx(5 * 0.09)

    # Output masks are uint8, nodata 0, co-registered with the first input.
    myDs = gdal.Open(myMergePath)
    assert myDs.GetRasterBand(1).DataType == gdal.GDT_Byte
    assert myDs.GetRasterBand(1).GetNoDataValue() == 0
    assert myDs.GetGeoTransform() == pytest.approx(_geoTransform())
    myDs = None


def test_reclass_and_inverse_mask_treat_nan_as_false(tmp_path):
    myCost = np.array([[0.0, 10.0, np.nan],
                       [20.0, 30.0, 40.0]], dtype=np.float32)
    mySuit = np.array([[1, 1, 1],
                       [1, 0, 1]], dtype=np.uint8)
    myCostPath = _writeRaster(tmp_path / "cost.tif", myCost, theNoData=float("nan"))
    mySuitPath = _writeRaster(tmp_path / "suit.tif", mySuit, theDtype=np.uint8, theNoData=0)

    myReclass = _read(laraster.reclassCost(myCostPath, 25.0, str(tmp_path)))
    np.testing.assert_array_equal(myReclass, [[1, 1, 0], [1, 0, 0]])

    myInverse = _read(laraster.createInverseMask(myCostPath, 25.0, mySuitPath, str(tmp_path)))
    # suit>=1 & cost>=25: (1,2) yes, (1,1) unsuitable, (0,2) NaN never counts.
    np.testing.assert_array_equal(myInverse, [[0, 0, 0], [0, 0, 1]])


def test_get_area_without_nodata_counts_ones_only(tmp_path):
    myArr = np.array([[1, 2], [1, 0]], dtype=np.float32)
    myPath = _writeRaster(tmp_path / "f.tif", myArr)
    assert laraster.getAreaHa(myPath) == pytest.approx(2 * 0.09)


def test_get_area_unreadable_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        laraster.getAreaHa(str(tmp_path / "nope.tif"))


# ---------------------------------------------------------------------------
# (g) corner-aware friction
# ---------------------------------------------------------------------------
def test_corner_aware_friction_unit_behaviour():
    # A 4-connected staircase step: barrier at (1,1) and (2,2)... use the
    # smallest case — barrier cells (1,0) and (0,1), clear at (0,0) and (1,1).
    myFriction = np.array([[0.0, 5.0],
                           [7.0, 0.0]])
    mySrc, myDst = laraster._directionWindows(2, 2, 1, 1)   # SE move (0,0) -> (1,1)
    myDiag = laraster._cornerAwareFriction(myFriction, 1, 1, mySrc, myDst)
    assert myDiag.shape == (1, 1)
    assert myDiag[0, 0] == 5.0            # max(dst=0, min(flanks 7, 5)) = 5

    mySrcE, myDstE = laraster._directionWindows(2, 2, 0, 1)  # straight E
    myStraight = laraster._cornerAwareFriction(myFriction, 0, 1, mySrcE, myDstE)
    np.testing.assert_array_equal(myStraight, myFriction[:, 1:2])

    # An impassable flank pair seals the corner even though the destination is clear.
    myWall = np.array([[0.0, np.inf],
                       [np.inf, 0.0]])
    assert np.isinf(laraster._cornerAwareFriction(myWall, 1, 1, mySrc, myDst)[0, 0])
    # Only one flank blocked: the walker can squeeze past the other side.
    myHalf = np.array([[0.0, np.inf],
                       [0.0, 0.0]])
    assert laraster._cornerAwareFriction(myHalf, 1, 1, mySrc, myDst)[0, 0] == 0.0


def _antiDiagonalBarrier(theSize: int, theValue: float) -> np.ndarray:
    """1-cell-wide line of cells with ``row + col == theSize - 1``."""
    myFriction = np.zeros((theSize, theSize), dtype=np.float64)
    myIdx = np.arange(theSize)
    myFriction[myIdx, theSize - 1 - myIdx] = theValue
    return myFriction


def test_impassable_diagonal_line_splits_flat_dem(tmp_path):
    mySize = 41
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((mySize, mySize)))
    myFriction = _antiDiagonalBarrier(mySize, np.inf)
    myX, myY = _cellCentre(5, 5)                       # near side: row + col < 40

    myCost = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path), theFriction=myFriction))

    myRowPlusCol = np.add.outer(np.arange(mySize), np.arange(mySize))
    assert np.isfinite(myCost[myRowPlusCol < mySize - 1]).all()
    assert np.isnan(myCost[myRowPlusCol >= mySize - 1]).all()


def test_impassable_diagonal_line_in_euclidean_cost_too(tmp_path):
    mySize = 41
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((mySize, mySize)))
    myFriction = _antiDiagonalBarrier(mySize, np.inf)
    myCost = _read(laraster.makeEuclideanCost(
        myDem, *_cellCentre(5, 5), str(tmp_path), theFriction=myFriction,
    ))
    myRowPlusCol = np.add.outer(np.arange(mySize), np.arange(mySize))
    assert np.isfinite(myCost[myRowPlusCol < mySize - 1]).all()
    assert np.isnan(myCost[myRowPlusCol > mySize - 1]).all()


def test_thirty_minute_diagonal_line_adds_about_1800s_from_any_approach(tmp_path):
    mySize = 41
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((mySize, mySize)))
    myPenaltySec = 1800.0
    myFriction = _antiDiagonalBarrier(mySize, myPenaltySec / _CELL)   # seconds per metre
    myRowPlusCol = np.add.outer(np.arange(mySize), np.arange(mySize))
    myFar = myRowPlusCol > mySize - 1

    # Several seeds so the far side is approached head-on, obliquely and along
    # the barrier's own diagonal.
    for mySeed in ((5, 5), (20, 2), (2, 20), (30, 3)):
        myX, myY = _cellCentre(*mySeed)
        myFree = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "free"))).astype(np.float64)
        myWith = _read(laraster.makeWalkCost(
            myDem, myX, myY, str(tmp_path / "with"), theFriction=myFriction,
        )).astype(np.float64)

        myExtra = (myWith - myFree)[myFar]
        assert np.isfinite(myExtra).all(), mySeed
        # Every crossing pays at least the full ford; the corner-cut never leaks.
        # (1e-3 s slack: the surface is stored as Float32, ~1e-4 s at 2500 s.)
        assert myExtra.min() >= myPenaltySec - 1e-3, (mySeed, myExtra.min())
        # ...and never much more: at worst one diagonal step is traded for two
        # straight ones to line up a head-on crossing (~12.6 s on flat ground).
        assert myExtra.max() <= myPenaltySec + 2.0 * _STRAIGHT_SEC, (mySeed, myExtra.max())
        # The near side is untouched.
        np.testing.assert_allclose(myWith[myRowPlusCol < mySize - 1], myFree[myRowPlusCol < mySize - 1])


def test_thirty_minute_horizontal_line_adds_exactly_1800s(tmp_path):
    mySize = 41
    myDem = _writeRaster(tmp_path / "flat.tif", np.zeros((mySize, mySize)))
    myPenaltySec = 1800.0
    myFriction = np.zeros((mySize, mySize))
    myFriction[30, :] = myPenaltySec / _CELL
    myX, myY = _cellCentre(10, 20)

    myFree = _read(laraster.makeWalkCost(myDem, myX, myY, str(tmp_path / "free"))).astype(np.float64)
    myWith = _read(laraster.makeWalkCost(
        myDem, myX, myY, str(tmp_path / "with"), theFriction=myFriction,
    )).astype(np.float64)

    np.testing.assert_allclose(myWith[31:] - myFree[31:], myPenaltySec, rtol=1e-6)
    np.testing.assert_allclose(myWith[:30], myFree[:30])


def test_friction_edges_add_destination_friction_times_length():
    myDem = np.zeros((3, 3))
    myFriction = np.zeros((3, 3))
    myFriction[1, 1] = 2.0                             # 2 s/m at the centre
    myRow, myCol, myCost = laraster._toblerEdges(myDem, _CELL, _CELL, _CELL * math.sqrt(2.0), myFriction)
    myCentre = 4
    myInto = myCost[myCol == myCentre]
    myOutOf = myCost[myRow == myCentre]
    # Straight into the centre: base + 2*30; diagonal: base*sqrt2 + 2*30*sqrt2.
    assert set(np.round(myInto, 6)) == {
        round(_STRAIGHT_SEC + 60.0, 6), round((_STRAIGHT_SEC + 60.0) * math.sqrt(2.0), 6),
    }
    # Leaving the centre costs nothing extra.
    assert set(np.round(myOutOf, 6)) == {
        round(_STRAIGHT_SEC, 6), round(_STRAIGHT_SEC * math.sqrt(2.0), 6),
    }


# ---------------------------------------------------------------------------
# (h) window sizing
# ---------------------------------------------------------------------------
def test_window_size_for_target_clamps():
    assert laraster.windowSizeForTarget(50, 30) == 200
    assert laraster.windowSizeForTarget(1e9, 30) == 1500
    assert laraster.windowSizeForTarget(0, 30) == 1500
    assert laraster.windowSizeForTarget(50, 0) == 1500
    assert laraster.windowSizeForTarget(50, 30, theMinPixels=400, theMaxPixels=900) == 400
    assert laraster.windowSizeForTarget(1e9, 30, theMaxPixels=900) == 900


def test_window_size_for_target_between_clamps():
    # 1986 ha -> r = 2514 m -> diameter 167.6 px at 30 m -> x3 = 502.8 -> 503
    myRadius = math.sqrt(1986.0 * 10_000.0 / math.pi)
    myExpected = int(math.ceil(3.0 * 2.0 * myRadius / 30.0))
    assert laraster.windowSizeForTarget(1986.0, 30.0) == myExpected == 503


# ---------------------------------------------------------------------------
# (i) border touch
# ---------------------------------------------------------------------------
def test_mask_touches_border(tmp_path):
    myInner = np.zeros((10, 10), dtype=np.uint8)
    myInner[3:6, 3:6] = 1
    myInnerPath = _writeRaster(tmp_path / "inner.tif", myInner, theDtype=np.uint8, theNoData=0)
    assert laraster.maskTouchesBorder(myInnerPath) is False

    for myRow, myCol in ((0, 4), (9, 4), (4, 0), (4, 9)):
        myEdge = myInner.copy()
        myEdge[myRow, myCol] = 1
        myEdgePath = _writeRaster(tmp_path / f"edge_{myRow}_{myCol}.tif", myEdge,
                                  theDtype=np.uint8, theNoData=0)
        assert laraster.maskTouchesBorder(myEdgePath) is True

    assert laraster.maskTouchesBorder(None) is False
    assert laraster.maskTouchesBorder("") is False
    # Unreadable is treated as suspect.
    assert laraster.maskTouchesBorder(str(tmp_path / "missing.tif")) is True
    myGarbage = tmp_path / "garbage.tif"
    myGarbage.write_bytes(b"not a tiff")
    assert laraster.maskTouchesBorder(str(myGarbage)) is True


# ---------------------------------------------------------------------------
# (j) travel direction
# ---------------------------------------------------------------------------
def _slopedDem(theRows: int = 40, theCols: int = 40) -> np.ndarray:
    """z rises 0.1 m per metre eastward — a 10 % planar slope."""
    return np.repeat(0.1 * np.arange(theCols, dtype=np.float64)[None, :] * _CELL, theRows, axis=0)


def test_round_trip_is_outbound_plus_inbound_not_twice_outbound(tmp_path):
    myDemPath = _writeRaster(tmp_path / "slope.tif", _slopedDem(), theDtype=np.float64)
    myX, myY = _cellCentre(20, 20)
    myScratch = str(tmp_path)

    myOut  = _read(laraster.makeWalkCost(myDemPath, myX, myY, myScratch,
                                         theDirection=laraster.DIRECTION_OUTBOUND)).astype(np.float64)
    myIn   = _read(laraster.makeWalkCost(myDemPath, myX, myY, myScratch,
                                         theDirection=laraster.DIRECTION_INBOUND)).astype(np.float64)
    myBoth = _read(laraster.makeWalkCost(myDemPath, myX, myY, myScratch,
                                         theDirection=laraster.DIRECTION_ROUND_TRIP)).astype(np.float64)

    np.testing.assert_allclose(myBoth, myOut + myIn, rtol=1e-6)
    # Tobler is asymmetric: going uphill east is slower than coming back down.
    assert myOut[20, 39] > myIn[20, 39]
    assert not np.allclose(myBoth, 2.0 * myOut, rtol=1e-3)
    # Directly downhill the ordering flips, so both legs really are solved.
    assert myOut[20, 0] < myIn[20, 0]


def test_direction_variants_agree_between_array_and_file_paths(tmp_path):
    myDem = _slopedDem()
    myGrid = laraster._dijkstraFromSeeds(
        myDem, _CELL, _CELL, np.array([20]), np.array([20]), np.array([0.0]),
        theDirection=laraster.DIRECTION_ROUND_TRIP,
    )
    myDemPath = _writeRaster(tmp_path / "slope.tif", myDem, theDtype=np.float64)
    myFile = _read(laraster.makeWalkCost(
        myDemPath, *_cellCentre(20, 20), str(tmp_path), theDirection=laraster.DIRECTION_ROUND_TRIP,
    ))
    np.testing.assert_allclose(myFile, myGrid.astype(np.float32), rtol=1e-6)


def test_round_trip_tiled_matches_single_pass_on_one_tile(tmp_path):
    myDemPath = _writeRaster(tmp_path / "slope.tif", _slopedDem(), theDtype=np.float64)
    myX, myY = _cellCentre(20, 20)
    mySingle = _read(laraster.makeWalkCost(myDemPath, myX, myY, str(tmp_path / "s"),
                                           theDirection=laraster.DIRECTION_ROUND_TRIP))
    myTiled = _read(laraster.makeWalkCost(myDemPath, myX, myY, str(tmp_path / "t"),
                                          theDirection=laraster.DIRECTION_ROUND_TRIP,
                                          theForceTiled=True))
    np.testing.assert_array_equal(myTiled, mySingle)


def test_unknown_direction_raises():
    myDem = np.zeros((5, 5))
    with pytest.raises(ValueError, match="Unknown travel direction"):
        laraster._dijkstraFromSeeds(
            myDem, _CELL, _CELL, np.array([2]), np.array([2]), np.array([0.0]),
            theDirection="sideways",
        )


# ---------------------------------------------------------------------------
# Windowing
# ---------------------------------------------------------------------------
def test_window_rasters_around_seed_crops_both_and_shifts_origin(tmp_path):
    myDem = np.arange(100 * 100, dtype=np.float32).reshape(100, 100)
    mySuit = (myDem % 2 == 0).astype(np.uint8)
    myDemPath = _writeRaster(tmp_path / "dem.tif", myDem, theNoData=-9999.0)
    mySuitPath = _writeRaster(tmp_path / "suit.tif", mySuit, theDtype=np.uint8, theNoData=0)

    myDemOut, mySuitOut = laraster.windowRastersAroundSeed(
        myDemPath, mySuitPath, *_cellCentre(50, 50), 40, str(tmp_path / "win"),
    )
    myDemWin, myGeoTransform, myProjection = laraster._readBand(myDemOut)
    mySuitWin = _read(mySuitOut)

    assert myDemWin.shape == (40, 40) and mySuitWin.shape == (40, 40)
    np.testing.assert_array_equal(myDemWin, myDem[30:70, 30:70])
    np.testing.assert_array_equal(mySuitWin, mySuit[30:70, 30:70])
    assert myGeoTransform[0] == pytest.approx(_ORIGIN_X + 30 * _CELL)
    assert myGeoTransform[3] == pytest.approx(_ORIGIN_Y - 30 * _CELL)
    assert "UTM zone 36N" in myProjection

    myDs = gdal.Open(myDemOut)
    assert myDs.GetRasterBand(1).GetNoDataValue() == -9999.0
    myDs = None


def test_window_rasters_around_seed_clamps_at_corner(tmp_path):
    myDem = np.zeros((50, 50), dtype=np.float32)
    myDemPath = _writeRaster(tmp_path / "dem.tif", myDem)
    mySuitPath = _writeRaster(tmp_path / "suit.tif", myDem.astype(np.uint8), theDtype=np.uint8)
    myDemOut, _ = laraster.windowRastersAroundSeed(
        myDemPath, mySuitPath, *_cellCentre(2, 3), 20, str(tmp_path / "win"),
    )
    assert _read(myDemOut).shape == (12, 13)
    assert laraster._readBand(myDemOut)[1][0] == pytest.approx(_ORIGIN_X)


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------
def test_write_geotiff_is_immediately_readable_with_lzw_tiling(tmp_path):
    myPath = laraster._writeGeoTiff(
        str(tmp_path / "w.tif"), np.ones((10, 20), dtype=np.uint8), _geoTransform(), _UTM36N,
        np.uint8, 0,
    )
    myDs = gdal.Open(myPath)
    assert myDs is not None
    assert myDs.RasterXSize == 20 and myDs.RasterYSize == 10
    myMeta = myDs.GetMetadata("IMAGE_STRUCTURE")
    assert myMeta.get("COMPRESSION") == "LZW"
    assert myDs.GetRasterBand(1).GetBlockSize() != [20, 1]     # tiled, not stripped
    myDs = None


def test_read_band_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        laraster._readBand(str(tmp_path / "missing.tif"))


def test_module_imports_without_scipy(monkeypatch):
    import importlib

    _blockScipy(monkeypatch)
    monkeypatch.delitem(sys.modules, "la.lib.laraster", raising=False)
    myModule = importlib.import_module("la.lib.laraster")
    assert myModule.DIRECTION_ROUND_TRIP == "round_trip"
    assert myModule._TILE_SIZE == 1024 and myModule._TILE_HALO == 128
    assert myModule._TILE_DISPATCH_PIXELS == 4_000_000
    # Restore the original module object for the remaining tests.
    monkeypatch.setitem(sys.modules, "la.lib.laraster", laraster)
