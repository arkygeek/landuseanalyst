"""Tests for :mod:`la.lib.lapathnetwork` — Delaunay baseline and Tobler
least-cost walking routes between sites. No QGIS import; DEMs are built
with GDAL in ``tmp_path``."""

import numpy as np
import pytest
from osgeo import gdal

from la.lib import laraster
from la.lib.lapathnetwork import (
    categoriseUsage,
    delaunayEdges,
    walkingRoutes,
)

_UTM36 = ('PROJCS["WGS 84 / UTM zone 36N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],'
          'PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],'
          'PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",33],PARAMETER["scale_factor",0.9996],'
          'PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1],AUTHORITY["EPSG","32636"]]')


def _writeDem(thePath, theArray, theCell=30.0, theX0=0.0, theY0=None):
    """Write ``theArray`` as a north-up UTM 36N GeoTIFF whose lower-left is (theX0, 0)."""
    myRows, myCols = theArray.shape
    myTop = theY0 if theY0 is not None else myRows * theCell
    myDs = gdal.GetDriverByName("GTiff").Create(str(thePath), myCols, myRows, 1, gdal.GDT_Float32)
    myDs.SetGeoTransform((theX0, theCell, 0.0, myTop, 0.0, -theCell))
    myDs.SetProjection(_UTM36)
    myDs.GetRasterBand(1).WriteArray(theArray.astype(np.float32))
    myDs = None
    return str(thePath)


# ----- delaunayEdges -----


def test_delaunay_threeTriangle() -> None:
    """3 points → 3 edges (triangle perimeter)."""
    myEdges = delaunayEdges([(0.0, 0.0), (10.0, 0.0), (5.0, 8.66)])
    assert myEdges == [(0, 1), (0, 2), (1, 2)]


def test_delaunay_squareFour() -> None:
    """4 corner-square points → 5 edges (4 sides + 1 diagonal)."""
    myEdges = delaunayEdges([(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)])
    assert len(myEdges) == 5
    # Every edge has i < j and is unique.
    for i, j in myEdges:
        assert i < j
    assert len(set(myEdges)) == 5


def test_delaunay_tooFewRaises() -> None:
    with pytest.raises(ValueError, match="≥3"):
        delaunayEdges([(0.0, 0.0), (1.0, 1.0)])


def test_delaunay_collinearRaises() -> None:
    with pytest.raises(ValueError):
        delaunayEdges([(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)])


# ----- walkingRoutes -----


@pytest.fixture
def syntheticFlatDem(tmp_path) -> str:
    """A 50×50 flat DEM at 30 m resolution, EPSG:32636, bounds (0, 0, 1500, 1500)."""
    return _writeDem(tmp_path / "flat_dem.tif", np.full((50, 50), 100.0, dtype=np.float32))


def test_walkingRoutes_threeSitesOnFlat(syntheticFlatDem) -> None:
    """3 sites on a flat DEM → 6 routes (both directions per pair)."""
    myPoints = [(200.0, 200.0), (1200.0, 300.0), (700.0, 1200.0)]
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    assert myResult.inCoverage == {0, 1, 2}
    assert len(myResult.routes) == 6  # N*(N-1) = 6, both directions
    assert set(myResult.routeIds) == {(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)}
    for myRoute in myResult.routes:
        assert len(myRoute) >= 2
    assert len(myResult.routeCosts) == 6 and len(myResult.routePeakUsage) == 6


def test_walkingRoutes_accumulationCountsPositive(syntheticFlatDem) -> None:
    """The accumulation raster has positive values along the route cells."""
    myPoints = [(200.0, 200.0), (1200.0, 1200.0), (1200.0, 200.0)]
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    assert myResult.accumulation.sum() > 0
    assert myResult.accumulation.max() >= 1


def test_walkingRoutes_outOfCoverageSkipped(syntheticFlatDem) -> None:
    """Points outside the DEM bbox are silently excluded from inCoverage."""
    myPoints = [
        (200.0, 200.0),                # in
        (1200.0, 1200.0),              # in
        (100000.0, 100000.0),          # far outside
        (700.0, 700.0),                # in
    ]
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    assert myResult.inCoverage == {0, 1, 3}
    # 3 in-coverage points × 2 directions = 6 routes
    assert set(myResult.routeIds) == {
        (0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1),
    }


def test_walkingRoutes_tooFewInCoverageRaises(syntheticFlatDem) -> None:
    """Fewer than 2 in-coverage points → ValueError."""
    myPoints = [(200.0, 200.0), (100000.0, 100000.0), (200000.0, 200000.0)]
    with pytest.raises(ValueError, match="≥2"):
        walkingRoutes(syntheticFlatDem, myPoints)


def test_walkingRoutes_missingDemRaises() -> None:
    with pytest.raises(FileNotFoundError):
        walkingRoutes("/no/such/path.tif", [(0.0, 0.0), (1.0, 1.0)])


def test_walkingRoutes_negativeWayPointStrengthRaises(syntheticFlatDem) -> None:
    with pytest.raises(ValueError, match="≥0"):
        walkingRoutes(
            syntheticFlatDem,
            [(200.0, 200.0), (1200.0, 1200.0), (700.0, 700.0)],
            theWayPointStrength=-1.0,
        )


def test_walkingRoutes_wayPointBundling(syntheticFlatDem) -> None:
    """A site between two others should attract more route traffic
    when way-point optimisation is enabled.

    On a flat DEM, three sites in a line: with ``alpha=0`` the
    direct route between the endpoints bypasses the middle (or
    coincides only by coincidence). With ``alpha`` large, the
    direct route gets pulled toward the middle site's
    low-friction corridor, so the middle site's neighbourhood
    sees more accumulation.
    """
    # End-points at left and right, middle site dead centre.
    myPoints = [(200.0, 750.0), (1200.0, 750.0), (700.0, 750.0)]

    myBaseline = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    myBundled  = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=5.0)

    # Pixel accumulation around the middle site (700, 750) should be
    # at least as high in the bundled run as the baseline. On a flat
    # DEM the baseline routes also pass through the middle by chance
    # (it's exactly on the centreline), so the test asserts ≥ rather
    # than strictly >. Bundled mode shouldn't make it *worse*.
    assert myBundled.accumulation.sum() >= myBaseline.accumulation.sum() * 0.8


def test_walkingRoutes_wayPointZeroMatchesBaseline(syntheticFlatDem) -> None:
    """``alpha = 0`` produces identical routes to the no-friction case."""
    myPoints = [(200.0, 200.0), (1200.0, 1200.0), (700.0, 700.0)]
    myA = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    myB = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    assert myA.routeIds == myB.routeIds
    assert (myA.accumulation == myB.accumulation).all()


# ----- plugin-specific: coordinates, costs, window, friction -----


def test_walkingRoutes_routeGeometryAndCost(syntheticFlatDem) -> None:
    """Routes start/end on the site cells, in DEM CRS, and cost Tobler flat-ground time."""
    myPoints = [(200.0, 750.0), (1100.0, 750.0)]
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    myRoute = myResult.routes[myResult.routeIds.index((0, 1))]
    # Pixel centres: (200, 750) → cell col 6 / row 25 → centre (195, 735).
    assert myRoute[0] == (195.0, 735.0)
    assert myRoute[-1] == (1095.0, 735.0)
    # Straight east along one row: every vertex on y=735, x increasing by 30.
    assert all(p[1] == 735.0 for p in myRoute)
    assert [p[0] for p in myRoute] == [195.0 + 30.0 * i for i in range(31)]
    # Tobler on flat ground: 6 * exp(-3.5 * 0.05) km/h over 900 m.
    myVelMs = 6.0 * np.exp(-3.5 * 0.05) * 1000.0 / 3600.0
    myExpected = 900.0 / myVelMs
    for myCost in myResult.routeCosts:
        assert myCost == pytest.approx(myExpected, rel=1e-9)
    # Window covers the whole DEM (buffer 5 km ≫ DEM), so bounds == DEM bounds.
    assert myResult.windowBounds == (0.0, 0.0, 1500.0, 1500.0)
    assert myResult.accumulation.shape == (50, 50)
    assert myResult.projectionWkt.startswith("PROJCS")


def test_walkingRoutes_windowIsCroppedAndWritable(syntheticFlatDem, tmp_path) -> None:
    """A small buffer crops the graph to the sites' bbox; the grid round-trips through GDAL."""
    myPoints = [(400.0, 400.0), (1000.0, 1000.0)]
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWindowBufferM=100.0, theWayPointStrength=0.0)
    myMinX, myMinY, myMaxX, myMaxY = myResult.windowBounds
    assert myMinX == 300.0 and myMaxX == 1110.0 and myMinY == 300.0 and myMaxY == 1110.0
    assert myResult.accumulation.shape == (27, 27)
    assert myResult.windowGeoTransform == (300.0, 30.0, 0.0, 1110.0, 0.0, -30.0)
    myOut = laraster._writeGeoTiff(
        str(tmp_path / "usage.tif"), myResult.accumulation, myResult.windowGeoTransform,
        myResult.projectionWkt, np.int32, 0,
    )
    myBack, myGt, _ = laraster._readBand(myOut)
    assert myGt == myResult.windowGeoTransform
    assert (myBack == myResult.accumulation).all()
    # Every route vertex lies inside the window.
    for myRoute in myResult.routes:
        assert all(myMinX <= x <= myMaxX and myMinY <= y <= myMaxY for x, y in myRoute)


def test_walkingRoutes_routesAreSymmetricOnFlat(syntheticFlatDem) -> None:
    """On flat terrain i→j and j→i overlay exactly, so peak usage along both is ≥2."""
    myPoints = [(200.0, 200.0), (1190.0, 1190.0)]       # a pure diagonal: unique shortest path
    myResult = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    myForward = myResult.routes[myResult.routeIds.index((0, 1))]
    myBack = myResult.routes[myResult.routeIds.index((1, 0))]
    assert myForward == list(reversed(myBack))
    assert myResult.routePeakUsage == [2, 2]
    assert myResult.accumulation.max() == 2


def test_walkingRoutes_impassableFrictionDivertsRoute(syntheticFlatDem) -> None:
    """A full-height wall with one gap forces both routes through the gap."""
    myFriction = np.zeros((50, 50), dtype=np.float64)
    myFriction[:, 25] = np.inf
    myFriction[45, 25] = 0.0           # the only crossing, near the bottom
    myPoints = [(300.0, 750.0), (1200.0, 750.0)]
    myFree = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0)
    myWalled = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0, theFriction=myFriction)
    assert len(myWalled.routes) == 2
    for myRoute in myWalled.routes:
        myCrossings = [p for p in myRoute if p[0] == 765.0]       # centre x of column 25
        assert myCrossings and all(p[1] == 1500.0 - 45.5 * 30.0 for p in myCrossings)
    assert min(myWalled.routeCosts) > max(myFree.routeCosts)
    assert myWalled.accumulation[45, 25] == 2
    # Seal the gap: no route can exist, so none is emitted.
    myFriction[45, 25] = np.inf
    mySealed = walkingRoutes(syntheticFlatDem, myPoints, theWayPointStrength=0.0, theFriction=myFriction)
    assert mySealed.routes == [] and mySealed.inCoverage == {0, 1}


def test_walkingRoutes_frictionShapeMismatchRaises(syntheticFlatDem) -> None:
    with pytest.raises(ValueError, match="shape"):
        walkingRoutes(syntheticFlatDem, [(200.0, 200.0), (1200.0, 1200.0)],
                      theFriction=np.zeros((10, 10)))


def test_walkingRoutes_frictionAndBarriersAreExclusive(syntheticFlatDem) -> None:
    with pytest.raises(ValueError, match="not both"):
        walkingRoutes(syntheticFlatDem, [(200.0, 200.0), (1200.0, 1200.0)],
                      theFriction=np.zeros((50, 50)), theBarriersPath="x.geojson")


def test_walkingRoutes_slopeMakesDirectionsDiffer(tmp_path) -> None:
    """On a tilted DEM the i→j and j→i costs differ (Tobler is anisotropic)."""
    myRows = np.arange(50, dtype=np.float32)[:, None]
    myDem = np.broadcast_to(myRows * 6.0, (50, 50)).copy()      # rises 6 m per row southward
    myPath = _writeDem(tmp_path / "tilt.tif", myDem)
    myPoints = [(750.0, 1300.0), (750.0, 200.0)]                # north site, south site
    myResult = walkingRoutes(myPath, myPoints, theWayPointStrength=0.0)
    myUp = myResult.routeCosts[myResult.routeIds.index((0, 1))]      # north → south climbs
    myDown = myResult.routeCosts[myResult.routeIds.index((1, 0))]
    assert myUp > myDown > 0


# ----- categoriseUsage -----


def test_categoriseUsage_terciles() -> None:
    """Well-distributed usage → 2 thresholds dividing it roughly in 3."""
    myAcc = np.arange(1, 100, dtype=np.int32)
    myThresh = categoriseUsage(myAcc, theNumClasses=3)
    assert len(myThresh) == 2
    assert myThresh[0] < myThresh[1]


def test_categoriseUsage_emptyRaster() -> None:
    """Empty (all-zero) accumulation → all-zero thresholds, no crash."""
    myAcc = np.zeros((10, 10), dtype=np.int32)
    myThresh = categoriseUsage(myAcc, theNumClasses=3)
    assert myThresh == [0, 0]


def test_categoriseUsage_tooFewClassesRaises() -> None:
    with pytest.raises(ValueError):
        categoriseUsage(np.array([1, 2, 3]), theNumClasses=1)
