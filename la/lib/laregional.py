"""
laregional.py — regional-scale Voronoi/Thiessen tessellation (no Qt, no GDAL).

Thiessen polygons (a.k.a. Voronoi tessellation) tile a region around a
set of input points so that every location belongs to the polygon of
its nearest input point. The thesis Ch 6 (§ 6.3, p. 333–336) uses
Thiessen polygons as the simplest territory-allocation method,
contrasting them with XTent (site-size-weighted, see
:mod:`la.lib.laxtent`) and Landuse Analyst catchments. The path-network
analysis of § 6.4 lives in :mod:`la.lib.lapathnetwork`.

This is the plugin-side port of the Landuse Analyst web app's
``backend/engine/regional.py``. Pure NumPy + SciPy — no Shapely, no
GDAL, no ``qgis`` import. ``scipy.spatial.Voronoi`` is imported lazily
inside :func:`computeThiessen` so the module itself loads with only
``numpy`` available.

The clipping uses the Sutherland-Hodgman algorithm against an
axis-aligned bbox, and the unbounded Voronoi cells are handled by
adding four far-away sentinel points to the input set so every real
point's region comes back from ``scipy.spatial.Voronoi`` bounded. This
trick is standard practice and avoids the ridge-to-infinity projection
that the bare ``Voronoi`` API leaves to the caller.
"""

from typing import Callable, Sequence

import numpy as np

# Sentinel points sit ``_SENTINEL_SCALE`` × bbox-span outside the
# bbox in each diagonal direction. Large enough that no real input
# point's Voronoi cell can touch them, so every real cell is bounded
# by ridges between the real points + the bbox edge (and never by a
# real-to-sentinel ridge that would distort the geometry).
_SENTINEL_SCALE = 100.0

Point = tuple[float, float]
Ring = list[Point]
Bbox = tuple[float, float, float, float]


def computeThiessen(
    thePoints: Sequence[Point],
    theBbox:   Bbox,
) -> list[Ring]:
    """Voronoi tessellation of ``thePoints``, clipped to ``theBbox``.

    :param thePoints: settlement coordinates ``[(x, y), ...]`` in a
        projected CRS. Must contain at least 3 non-collinear points
        for a valid Voronoi diagram.
    :param theBbox:   clipping bounds ``(minX, minY, maxX, maxY)`` in
        the same CRS as ``thePoints``.
    :return: one polygon per input point, same order as input. Each
        polygon is a closed ring (first point == last point) of
        ``(x, y)`` tuples in the input CRS.
    :rtype: list
    :raises ValueError: if fewer than 3 points, points are collinear,
        or the bbox is degenerate.
    :raises ImportError: if ``scipy`` is not installed.
    """
    from scipy.spatial import Voronoi

    if len(thePoints) < 3:
        raise ValueError(
            f"Thiessen requires ≥3 points; got {len(thePoints)}."
        )

    if _areCollinear(thePoints):
        raise ValueError(
            "Thiessen input points are collinear — territories are "
            "degenerate (infinite strips). Add at least one off-axis point."
        )

    myMinX, myMinY, myMaxX, myMaxY = theBbox
    if myMaxX <= myMinX or myMaxY <= myMinY:
        raise ValueError(
            f"Bbox is degenerate or inverted: {theBbox}."
        )

    mySpan = max(myMaxX - myMinX, myMaxY - myMinY)
    myCx = (myMinX + myMaxX) / 2.0
    myCy = (myMinY + myMaxY) / 2.0
    myFar = mySpan * _SENTINEL_SCALE
    mySentinels = [
        (myCx - myFar, myCy - myFar),
        (myCx + myFar, myCy - myFar),
        (myCx + myFar, myCy + myFar),
        (myCx - myFar, myCy + myFar),
    ]
    myAllPoints = np.array([tuple(p) for p in thePoints] + mySentinels, dtype=float)

    try:
        myVor = Voronoi(myAllPoints)
    except Exception as myExc:
        # scipy raises QhullError on collinear input. Re-raise as a
        # ValueError so callers get a stable exception type.
        raise ValueError(
            f"Voronoi failed (collinear or duplicate points?): {myExc}"
        ) from myExc

    myPolygons: list[Ring] = []
    for myIdx in range(len(thePoints)):
        myRegionIdx = myVor.point_region[myIdx]
        myVertIndices = myVor.regions[myRegionIdx]
        if -1 in myVertIndices or not myVertIndices:
            # Should not happen with sentinels; defensive fallback
            # produces an empty ring rather than crashing.
            myPolygons.append([])
            continue
        myRawRing: Ring = [
            (float(myVor.vertices[j, 0]), float(myVor.vertices[j, 1]))
            for j in myVertIndices
        ]
        myClipped = _clipPolygonToBbox(myRawRing, theBbox)
        if myClipped and myClipped[0] != myClipped[-1]:
            myClipped.append(myClipped[0])
        myPolygons.append(myClipped)
    return myPolygons


def _clipPolygonToBbox(
    thePolygon: Ring,
    theBbox:    Bbox,
) -> Ring:
    """Sutherland-Hodgman clip of ``thePolygon`` to an axis-aligned bbox.

    :param thePolygon: polygon vertices (not necessarily closed).
    :param theBbox:    ``(minX, minY, maxX, maxY)``.
    :return: vertices of the clipped polygon, not closed. May be empty
        if the polygon lies entirely outside the bbox.
    :rtype: list
    """
    myMinX, myMinY, myMaxX, myMaxY = theBbox
    myResult = list(thePolygon)
    myResult = _clipAgainstEdge(myResult, lambda p: p[0] >= myMinX,
                                lambda p1, p2: _intersectX(p1, p2, myMinX))
    myResult = _clipAgainstEdge(myResult, lambda p: p[0] <= myMaxX,
                                lambda p1, p2: _intersectX(p1, p2, myMaxX))
    myResult = _clipAgainstEdge(myResult, lambda p: p[1] >= myMinY,
                                lambda p1, p2: _intersectY(p1, p2, myMinY))
    myResult = _clipAgainstEdge(myResult, lambda p: p[1] <= myMaxY,
                                lambda p1, p2: _intersectY(p1, p2, myMaxY))
    return myResult


def _clipAgainstEdge(
    thePoly:    Ring,
    theInside:  Callable[[Point], bool],
    theCross:   Callable[[Point, Point], Point],
) -> Ring:
    """One pass of Sutherland-Hodgman against a single half-plane.

    :param thePoly:    input vertices.
    :param theInside:  predicate ``point -> bool`` — True if point
        is on the "kept" side of the edge.
    :param theCross:   intersector ``(p1, p2) -> point`` — returns the
        intersection of segment ``p1→p2`` with the clipping edge.
    :return: the clipped vertex list (not closed).
    :rtype: list
    """
    if not thePoly:
        return []
    myOut: Ring = []
    for myI in range(len(thePoly)):
        myCurr = thePoly[myI]
        myPrev = thePoly[myI - 1]
        myCurrIn = theInside(myCurr)
        myPrevIn = theInside(myPrev)
        if myCurrIn:
            if not myPrevIn:
                myOut.append(theCross(myPrev, myCurr))
            myOut.append(myCurr)
        elif myPrevIn:
            myOut.append(theCross(myPrev, myCurr))
    return myOut


def _intersectX(
    theP1: Point,
    theP2: Point,
    theX:  float,
) -> Point:
    """Intersect segment ``theP1→theP2`` with the vertical line ``X = theX``.

    :return: ``(theX, y)`` — the crossing point.
    :rtype: tuple
    """
    myX1, myY1 = theP1
    myX2, myY2 = theP2
    if myX2 == myX1:
        return (theX, myY1)
    myT = (theX - myX1) / (myX2 - myX1)
    return (theX, myY1 + myT * (myY2 - myY1))


def _intersectY(
    theP1: Point,
    theP2: Point,
    theY:  float,
) -> Point:
    """Intersect segment ``theP1→theP2`` with the horizontal line ``Y = theY``.

    :return: ``(x, theY)`` — the crossing point.
    :rtype: tuple
    """
    myX1, myY1 = theP1
    myX2, myY2 = theP2
    if myY2 == myY1:
        return (myX1, theY)
    myT = (theY - myY1) / (myY2 - myY1)
    return (myX1 + myT * (myX2 - myX1), theY)


def _areCollinear(thePoints: Sequence[Point], theEpsilon: float = 1e-9) -> bool:
    """``True`` iff all points lie on a single line (within ``theEpsilon``).

    Uses the cross-product of vectors from the first point to every
    other point against the vector from the first to the second.

    :param thePoints: ``[(x, y), ...]``.
    :param theEpsilon: cross-product magnitude below which two vectors
        count as parallel.
    :rtype: bool
    """
    if len(thePoints) < 3:
        return True
    myX0, myY0 = thePoints[0]
    myX1, myY1 = thePoints[1]
    myDx = myX1 - myX0
    myDy = myY1 - myY0
    for myPx, myPy in thePoints[2:]:
        myCross = (myPx - myX0) * myDy - (myPy - myY0) * myDx
        if abs(myCross) > theEpsilon:
            return False
    return True


def fitBbox(
    thePoints:    Sequence[Point],
    theBufferPct: float = 0.10,
) -> Bbox:
    """Compute a bbox around ``thePoints`` with a percentage buffer.

    :param thePoints:    settlement coordinates.
    :param theBufferPct: extra padding as a fraction of the extent on
        each side (0.10 = 10% on each side).
    :return: ``(minX, minY, maxX, maxY)``.
    :rtype: tuple
    :raises ValueError: if ``thePoints`` is empty.
    """
    if not thePoints:
        raise ValueError("fitBbox needs at least one point.")
    myXs = [p[0] for p in thePoints]
    myYs = [p[1] for p in thePoints]
    myMinX, myMaxX = min(myXs), max(myXs)
    myMinY, myMaxY = min(myYs), max(myYs)
    myWidth  = max(myMaxX - myMinX, 1.0)  # guard against single-point input
    myHeight = max(myMaxY - myMinY, 1.0)
    myDx = myWidth  * theBufferPct
    myDy = myHeight * theBufferPct
    return (myMinX - myDx, myMinY - myDy, myMaxX + myDx, myMaxY + myDy)
