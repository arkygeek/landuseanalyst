"""Tests for :mod:`la.lib.laregional` — Thiessen polygon computation for
the regional-analysis layer (§ 6.3 of the thesis). No QGIS import."""

import pytest

from la.lib.laregional import (
    _clipPolygonToBbox,
    _intersectX,
    _intersectY,
    computeThiessen,
    fitBbox,
)


# ----- _intersectX / _intersectY -----


def test_intersectX_midpoint() -> None:
    """A horizontal segment crossing X=0 yields the midpoint Y."""
    assert _intersectX((-1.0, 5.0), (1.0, 5.0), 0.0) == (0.0, 5.0)


def test_intersectX_slanted() -> None:
    """Slanted segment from (0,0) to (2,4) crossing X=1 yields (1, 2)."""
    x, y = _intersectX((0.0, 0.0), (2.0, 4.0), 1.0)
    assert x == 1.0
    assert y == pytest.approx(2.0)


def test_intersectY_midpoint() -> None:
    """A vertical segment crossing Y=0 yields the midpoint X."""
    assert _intersectY((3.0, -1.0), (3.0, 1.0), 0.0) == (3.0, 0.0)


# ----- _clipPolygonToBbox -----


def test_clipPolygon_fullyInside() -> None:
    """A polygon entirely inside the bbox is returned unchanged."""
    myPoly = [(1.0, 1.0), (2.0, 1.0), (2.0, 2.0), (1.0, 2.0)]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    myResult = _clipPolygonToBbox(myPoly, myBbox)
    assert set(myResult) == set(myPoly)


def test_clipPolygon_partiallyOutside() -> None:
    """A polygon overlapping one bbox edge gets clipped to the edge."""
    myPoly = [(-5.0, 1.0), (5.0, 1.0), (5.0, 2.0), (-5.0, 2.0)]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    myResult = _clipPolygonToBbox(myPoly, myBbox)
    # All result vertices should have X >= 0
    assert all(p[0] >= 0.0 for p in myResult)
    # X=0 must appear at the new clipped edge
    assert any(p[0] == 0.0 for p in myResult)


def test_clipPolygon_fullyOutside() -> None:
    """A polygon entirely outside the bbox returns empty."""
    myPoly = [(20.0, 20.0), (30.0, 20.0), (30.0, 30.0), (20.0, 30.0)]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    assert _clipPolygonToBbox(myPoly, myBbox) == []


# ----- fitBbox -----


def test_fitBbox_addsBuffer() -> None:
    """fitBbox expands the point-set extent by the buffer percent."""
    myPoints = [(0.0, 0.0), (10.0, 10.0)]
    myMinX, myMinY, myMaxX, myMaxY = fitBbox(myPoints, theBufferPct=0.10)
    assert myMinX == pytest.approx(-1.0)
    assert myMinY == pytest.approx(-1.0)
    assert myMaxX == pytest.approx(11.0)
    assert myMaxY == pytest.approx(11.0)


def test_fitBbox_emptyRaises() -> None:
    with pytest.raises(ValueError):
        fitBbox([])


# ----- computeThiessen -----


def test_thiessen_tooFewPointsRaises() -> None:
    """Voronoi needs ≥3 points; computeThiessen rejects fewer."""
    with pytest.raises(ValueError, match="≥3"):
        computeThiessen([(0.0, 0.0), (1.0, 1.0)], (0.0, 0.0, 10.0, 10.0))


def test_thiessen_degenerateBboxRaises() -> None:
    with pytest.raises(ValueError, match="degenerate|inverted"):
        computeThiessen(
            [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)],
            (5.0, 5.0, 5.0, 5.0),
        )


def test_thiessen_collinearRaises() -> None:
    """Collinear input has no valid Voronoi diagram."""
    with pytest.raises(ValueError):
        computeThiessen(
            [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)],
            (-1.0, -1.0, 3.0, 1.0),
        )


def test_thiessen_squareFourPoints() -> None:
    """Four points at unit-square corners produce four equal quadrant cells.

    For points at (0,0), (10,0), (10,10), (0,10) clipped to the same
    bbox, each Voronoi cell is the corresponding quadrant of the bbox
    centered on the centroid (5, 5).
    """
    myPoints = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
    myBbox   = (0.0, 0.0, 10.0, 10.0)
    myPolys  = computeThiessen(myPoints, myBbox)
    assert len(myPolys) == 4
    # Each polygon should be 25 (=10*10/4) sq units
    for myRing in myPolys:
        assert myRing[0] == myRing[-1], "ring not closed"
        assert _polygonArea(myRing) == pytest.approx(25.0, abs=1e-6)


def test_thiessen_areasSumToBbox() -> None:
    """Areas of all polygons sum to the bbox area (no gaps, no overlaps).

    This is the global invariant for a Voronoi-clipped tessellation
    — if the clipping is correct the polygons tile the bbox exactly.
    """
    myPoints = [
        (2.0, 2.0), (8.0, 2.0), (5.0, 5.0), (2.0, 8.0), (8.0, 8.0),
    ]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    myPolys = computeThiessen(myPoints, myBbox)
    myTotal = sum(_polygonArea(p) for p in myPolys)
    myBboxArea = (myBbox[2] - myBbox[0]) * (myBbox[3] - myBbox[1])
    assert myTotal == pytest.approx(myBboxArea, abs=1e-6)


def test_thiessen_outputOrderMatchesInput() -> None:
    """Polygon i should contain input point i (nearest-point property)."""
    myPoints = [(2.0, 2.0), (8.0, 2.0), (5.0, 7.0)]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    myPolys = computeThiessen(myPoints, myBbox)
    assert len(myPolys) == 3
    for myI, myPoint in enumerate(myPoints):
        assert _pointInRing(myPoint, myPolys[myI]), (
            f"polygon {myI} should contain its seed point {myPoint}"
        )


def test_thiessen_ringsAreClosed() -> None:
    """Every returned polygon's first vertex equals its last."""
    myPoints = [(1.0, 1.0), (9.0, 1.0), (5.0, 9.0)]
    myBbox = (0.0, 0.0, 10.0, 10.0)
    for myRing in computeThiessen(myPoints, myBbox):
        assert myRing, "empty ring for a bounded cell — bug"
        assert myRing[0] == myRing[-1], "ring not closed"


def test_thiessen_projectedUtmCoordinates() -> None:
    """Metre-scale UTM 36N coordinates (the Shuna study area) tile the bbox."""
    myPoints = [(744800.0, 3611100.0), (748300.0, 3609200.0), (742100.0, 3606900.0), (746900.0, 3604500.0)]
    myBbox = fitBbox(myPoints, theBufferPct=0.25)
    myPolys = computeThiessen(myPoints, myBbox)
    myTotal = sum(_polygonArea(p) for p in myPolys)
    assert myTotal == pytest.approx((myBbox[2] - myBbox[0]) * (myBbox[3] - myBbox[1]), rel=1e-9)
    for myI, myPoint in enumerate(myPoints):
        assert _pointInRing(myPoint, myPolys[myI])


# ----- helpers -----


def _polygonArea(theRing: list[tuple[float, float]]) -> float:
    """Shoelace formula. Assumes ``theRing`` is closed."""
    if len(theRing) < 4:  # min closed-ring is triangle: 4 vertices
        return 0.0
    myAcc = 0.0
    for myI in range(len(theRing) - 1):
        x1, y1 = theRing[myI]
        x2, y2 = theRing[myI + 1]
        myAcc += x1 * y2 - x2 * y1
    return abs(myAcc) / 2.0


def _pointInRing(thePoint: tuple[float, float], theRing: list[tuple[float, float]]) -> bool:
    """Ray-casting point-in-polygon test."""
    if not theRing:
        return False
    x, y = thePoint
    myInside = False
    for myI in range(len(theRing) - 1):
        x1, y1 = theRing[myI]
        x2, y2 = theRing[myI + 1]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            myInside = not myInside
    return myInside
