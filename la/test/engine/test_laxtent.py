"""Tests for :mod:`la.lib.laxtent` — Renfrew & Level (1979) XTent
territorial allocation, polygonised through GDAL. No QGIS import."""

import numpy as np
import pytest

from la.lib.laxtent import (
    UNASSIGNED,
    computeXtent,
    computeXtentFeatures,
    polygoniseLabels,
    xtentLabels,
)


# ----- input validation -----


def test_xtent_emptyInputRaises() -> None:
    with pytest.raises(ValueError):
        computeXtent([], (0.0, 0.0, 10.0, 10.0))


def test_xtent_degenerateBboxRaises() -> None:
    with pytest.raises(ValueError, match="degenerate|inverted"):
        computeXtent(
            [(5.0, 5.0, 10.0)],
            (5.0, 5.0, 5.0, 5.0),
        )


def test_xtent_zeroSizeRaises() -> None:
    """A non-positive site size has no well-defined XTent influence."""
    with pytest.raises(ValueError, match="strictly positive"):
        computeXtent(
            [(1.0, 1.0, 0.0), (9.0, 9.0, 10.0)],
            (0.0, 0.0, 10.0, 10.0),
        )


def test_xtent_gridTooSmallRaises() -> None:
    with pytest.raises(ValueError, match="≥2"):
        computeXtent([(5.0, 5.0, 10.0)], (0.0, 0.0, 10.0, 10.0), theGridResolution=1)


# ----- single-site sanity -----


def test_xtent_singleSiteFillsBboxWithLowDecay() -> None:
    """One site with k=0 → its territory is the entire bbox."""
    myPolys = computeXtent(
        [(50.0, 50.0, 100.0)],
        (0.0, 0.0, 100.0, 100.0),
        theDistanceDecay=0.0,
        theGridResolution=50,
    )
    assert len(myPolys) == 1
    assert len(myPolys[0]) >= 1, "single site should produce at least one polygon"
    # ...and that polygon is the bbox itself.
    assert _totalPolygonArea(myPolys) == pytest.approx(100.0 * 100.0)


# ----- multi-site: dominance + parameter sensitivity -----


def test_xtent_twoEqualSitesProduceTwoTerritories() -> None:
    """Two equal sites on the X axis → both get a polygon."""
    myPolys = computeXtent(
        [(25.0, 50.0, 50.0), (75.0, 50.0, 50.0)],
        (0.0, 0.0, 100.0, 100.0),
        theSizeExponent=0.5,
        theDistanceDecay=0.001,
        theGridResolution=80,
    )
    assert len(myPolys) == 2
    assert len(myPolys[0]) >= 1, "left site should have territory"
    assert len(myPolys[1]) >= 1, "right site should have territory"


def test_xtent_smallSiteDominatedByLarge() -> None:
    """A tiny site next to a huge one should yield empty territory.

    Use the explicit XTent dominance condition: at the small site's
    own location, the large neighbour's influence already beats the
    small site's, so the small site can't claim any pixel.
    """
    # Large site at (50, 50) with size 10000; tiny site at (60, 50)
    # with size 1. At (60, 50): big's influence = 10000^0.5 - 0.5*10 =
    # 95; small's influence = 1^0.5 - 0 = 1. Big dominates.
    myPolys = computeXtent(
        [(50.0, 50.0, 10000.0), (60.0, 50.0, 1.0)],
        (0.0, 0.0, 100.0, 100.0),
        theSizeExponent=0.5,
        theDistanceDecay=0.5,
        theGridResolution=80,
    )
    assert len(myPolys[1]) == 0, "small site should be dominated"
    assert len(myPolys[0]) >= 1, "large site should still have territory"


def test_xtent_higherDistanceDecayShrinksTerritory() -> None:
    """Raising k makes all territories shrink (less ambitious influence).

    Total polygon area for the same input set should decrease as k
    increases (for fixed a + grid).
    """
    myPoints = [(25.0, 25.0, 50.0), (75.0, 75.0, 50.0)]
    myBbox = (0.0, 0.0, 100.0, 100.0)

    # Site size = 50 → size**0.5 ≈ 7.07. With k=0.5 and distances of
    # ~50 the influence drops to ~ -18 at the corners → corners become
    # unassigned → total area drops below the low-k baseline.
    myLowK  = _totalPolygonArea(computeXtent(myPoints, myBbox, theDistanceDecay=0.0001, theGridResolution=80))
    myHighK = _totalPolygonArea(computeXtent(myPoints, myBbox, theDistanceDecay=0.5,    theGridResolution=80))

    assert myHighK < myLowK, "higher distance decay should shrink the total territory"


def test_xtent_polygonsClosed() -> None:
    """Every returned ring is closed (first == last)."""
    myPolys = computeXtent(
        [(2.0, 2.0, 5.0), (8.0, 2.0, 5.0), (5.0, 8.0, 5.0)],
        (0.0, 0.0, 10.0, 10.0),
        theDistanceDecay=0.0,
        theGridResolution=60,
    )
    for myRings in myPolys:
        for myRing in myRings:
            assert myRing[0] == myRing[-1], "ring not closed"


# ----- GDAL-specific: label grid + polygonisation -----


def test_xtentLabels_gridAndGeotransform() -> None:
    """The winner grid is square, north-up, and each site owns its own cell."""
    myLabels, myGt = xtentLabels(
        [(25.0, 50.0, 50.0), (75.0, 50.0, 50.0)],
        (0.0, 0.0, 100.0, 100.0), theGridResolution=100,
    )
    assert myLabels.shape == (100, 100) and myLabels.dtype == np.int32
    assert myGt == (0.0, 1.0, 0.0, 100.0, 0.0, -1.0)
    assert myLabels[49, 25] == 0 and myLabels[49, 75] == 1
    # Symmetric sites → an even split of the grid, nothing unassigned.
    assert (myLabels == UNASSIGNED).sum() == 0
    assert (myLabels == 0).sum() == (myLabels == 1).sum()


def test_polygoniseLabels_twoBlocksWithHole() -> None:
    """A label grid with a nodata gap and a hole yields correct GeoJSON polygons."""
    myLabels = np.full((10, 10), UNASSIGNED, dtype=np.int32)
    myLabels[:, :4] = 0                 # left block, 4 cells wide
    myLabels[2:8, 5:10] = 1             # right block ...
    myLabels[4:6, 7:9] = 3              # ... with a 2x2 island of another label inside
    myGt = (0.0, 10.0, 0.0, 100.0, 0.0, -10.0)
    myBySite = polygoniseLabels(myLabels, myGt)
    assert set(myBySite) == {0, 1, 3}
    assert len(myBySite[0]) == 1 and len(myBySite[1]) == 1 and len(myBySite[3]) == 1
    myLeft = myBySite[0][0]
    assert myLeft["type"] == "Polygon"
    assert _shoelaceArea(myLeft["coordinates"][0]) == pytest.approx(40.0 * 100.0)
    myRight = myBySite[1][0]
    assert len(myRight["coordinates"]) == 2, "island should appear as a hole"
    assert _shoelaceArea(myRight["coordinates"][0]) == pytest.approx(50.0 * 60.0)
    assert _shoelaceArea(myRight["coordinates"][1]) == pytest.approx(20.0 * 20.0)
    for myGeom in (myLeft, myRight, myBySite[3][0]):
        for myRing in myGeom["coordinates"]:
            assert myRing[0] == myRing[-1]
            assert all(isinstance(c, tuple) and len(c) == 2 for c in myRing)


def test_computeXtentFeatures_isFeatureCollection() -> None:
    myDoc = computeXtentFeatures(
        [(25.0, 50.0, 50.0), (75.0, 50.0, 50.0), (50.0, 50.0, 0.01)],
        (0.0, 0.0, 100.0, 100.0), theGridResolution=40,
    )
    assert myDoc["type"] == "FeatureCollection"
    mySites = [f["properties"]["site"] for f in myDoc["features"]]
    assert mySites == [0, 1], "the dominated middle site must not appear"
    for myFeature in myDoc["features"]:
        assert myFeature["type"] == "Feature"
        assert myFeature["geometry"]["type"] == "Polygon"
        assert myFeature["properties"]["sizeHa"] == 50.0
    assert sum(_shoelaceArea(f["geometry"]["coordinates"][0]) for f in myDoc["features"]) == pytest.approx(10000.0)


def test_xtent_areaMatchesLabelGrid() -> None:
    """Polygon area equals assigned-cell count × cell area (lossless tracing)."""
    myPoints = [(20.0, 20.0, 40.0), (80.0, 70.0, 90.0)]
    myBbox = (0.0, 0.0, 100.0, 100.0)
    myLabels, _ = xtentLabels(myPoints, myBbox, theDistanceDecay=0.2, theGridResolution=50)
    myCellArea = (100.0 / 50) ** 2
    myPolys = computeXtent(myPoints, myBbox, theDistanceDecay=0.2, theGridResolution=50)
    for myIdx in range(2):
        assert _totalPolygonArea([myPolys[myIdx]]) == pytest.approx((myLabels == myIdx).sum() * myCellArea)
    assert (myLabels == UNASSIGNED).any(), "k=0.2 should leave the far corners unassigned"


# ----- helpers -----


def _totalPolygonArea(theNestedPolys: list[list[list[tuple[float, float]]]]) -> float:
    """Sum of shoelace areas across every ring in every site's polygons."""
    myTotal = 0.0
    for myRings in theNestedPolys:
        for myRing in myRings:
            myTotal += _shoelaceArea(myRing)
    return myTotal


def _shoelaceArea(theRing: list[tuple[float, float]]) -> float:
    if len(theRing) < 4:
        return 0.0
    myAcc = 0.0
    for myI in range(len(theRing) - 1):
        x1, y1 = theRing[myI]
        x2, y2 = theRing[myI + 1]
        myAcc += x1 * y2 - x2 * y1
    return abs(myAcc) / 2.0
