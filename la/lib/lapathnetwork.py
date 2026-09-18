"""
lapathnetwork.py — path-network analysis between settlements (thesis § 6.4).

Two methods, both producing a network of edges between settlements:

* **Delaunay triangulation** — pure geometry, no DEM. Mentioned in
  thesis § 6.4 (p. 341) as the comparison case that the walking-time
  network is more sophisticated than. Useful when no terrain data is
  available, or as a baseline to compare against.

* **Walking-time least-cost routes** — Dijkstra on a Tobler walk-cost
  edge graph over a DEM. For every ordered pair of in-coverage points,
  recover the path via the predecessor chain. Accumulate route usage
  per pixel so the most-trafficked corridors can be styled "heavily
  used" (thesis § 6.4 p. 341: "the values of Lightly Used, Well Used,
  and Heavily Used were chosen").

This is the plugin-side port of the Landuse Analyst web app's
``backend/engine/path_network.py``. The raster side is delegated to
:mod:`la.lib.laraster`: the DEM is read with ``_readBand``, the
anisotropic Tobler edges come from ``_toblerEdges`` (so barrier friction
and the diagonal corner-cut rule are identical to the catchment engine),
and the multi-origin way-point surface reuses ``_dijkstraFromSeeds``.
Only the per-origin predecessor Dijkstra is local, because
:mod:`la.lib.laraster` never needs predecessors.

Way-point optimisation (§ 6.4): a multi-origin "cost to the nearest
site" surface, normalised to ``[0, 1]``, multiplies every edge entering
pixel ``b`` by ``1 + alpha * M_norm[b]``. Per-origin routes then bundle
through the low-friction corridors around other settlements. Routes are
emitted in **both directions** per pair because Tobler costs are
anisotropic — the ``j → i`` route can differ from ``i → j`` on slopes.

No ``qgis`` import; ``numpy`` + ``osgeo`` at import time, ``scipy``
lazily inside the functions that need it.
"""

import math
import os
from dataclasses import dataclass
from typing import Optional

import numpy as np

from la.lib import laraster

Point = tuple[float, float]

#: ``scipy.sparse.csgraph.dijkstra`` marks "no predecessor" with this value.
_NO_PREDECESSOR = -9999

_SCIPY_REQUIRED_MESSAGE = (
    "scipy is required for path-network analysis (python -m pip install scipy)"
)


@dataclass(frozen=True)
class WalkingRoutesResult:
    """All-pairs walking-route output.

    ``routes[i]`` runs from site ``routeIds[i][0]`` to site
    ``routeIds[i][1]`` as pixel-centre ``(x, y)`` coordinates in the DEM
    CRS; ``routeCosts[i]`` is its Tobler walking time in seconds (the
    way-point multiplier is **not** included — it steers the route, the
    reported cost is the real walking time along it).

    ``routePeakUsage[i]`` is the maximum per-cell accumulation count
    encountered along ``routes[i]`` after every route in the network
    has been accumulated. A high value means the route shares a
    heavily-trafficked corridor with other routes — the "heavily used
    paths" of thesis § 6.4.

    Routes are emitted in **both directions**: one (i → j) and one
    (j → i) per pair. The two can differ on sloped terrain because the
    Tobler hiking function is anisotropic; on flat terrain they overlay
    perfectly. The accumulation raster counts each direction separately,
    so corridors carrying traffic both ways correctly rank "heavy".

    ``accumulation`` is an ``int32`` grid on the DEM window described by
    ``windowGeoTransform`` / ``projectionWkt`` — write it with
    ``laraster._writeGeoTiff(path, accumulation, windowGeoTransform,
    projectionWkt, numpy.int32, 0)``.
    """
    routes:              list[list[Point]]
    routeIds:            list[tuple[int, int]]
    routeCosts:          list[float]
    routePeakUsage:      list[int]
    accumulation:        np.ndarray
    windowBounds:        tuple[float, float, float, float]
    windowGeoTransform:  tuple
    projectionWkt:       str
    inCoverage:          set[int]


def delaunayEdges(
    thePoints: list[Point],
) -> list[tuple[int, int]]:
    """Return the unique Delaunay triangulation edges as index pairs.

    :param thePoints: ``[(x, y), ...]`` site coordinates (CRS-agnostic).
    :return: list of ``(i, j)`` with ``i < j`` — one entry per edge in
        the triangulation, never duplicated, sorted.
    :rtype: list
    :raises ValueError: if fewer than 3 points, or points are
        degenerate (collinear, coincident).
    :raises ImportError: if ``scipy`` is not installed.
    """
    try:
        from scipy.spatial import Delaunay
    except ImportError as myError:
        raise ImportError(_SCIPY_REQUIRED_MESSAGE) from myError

    if len(thePoints) < 3:
        raise ValueError(f"Delaunay requires ≥3 points; got {len(thePoints)}.")
    try:
        myTri = Delaunay(np.array(thePoints, dtype=float))
    except Exception as myExc:
        raise ValueError(
            f"Delaunay failed (collinear or duplicate points?): {myExc}"
        ) from myExc

    myEdges: set[tuple[int, int]] = set()
    for mySimplex in myTri.simplices:
        # Each triangle has 3 edges (3 unordered pairs from its 3 vertices).
        for myA, myB in ((mySimplex[0], mySimplex[1]),
                         (mySimplex[1], mySimplex[2]),
                         (mySimplex[0], mySimplex[2])):
            if myA == myB:
                continue
            myEdges.add((int(min(myA, myB)), int(max(myA, myB))))
    return sorted(myEdges)


def walkingRoutes(
    theDemPath:          str,
    thePoints:           list[Point],
    theWindowBufferM:    float = 5000.0,
    theWayPointStrength: float = 2.0,
    theFriction:         Optional[np.ndarray] = None,
    theBarriersPath:     Optional[str] = None,
) -> WalkingRoutesResult:
    """All-pairs least-cost walking routes over the DEM at ``theDemPath``.

    :param theDemPath: GDAL-readable DEM with elevation in metres and a
        north-up geotransform in metres. Its CRS must match the
        coordinate units of ``thePoints``.
    :param thePoints: ``[(x, y), ...]`` in the DEM's CRS. Points
        outside the DEM bounds are silently excluded from routing
        (their index appears in :attr:`WalkingRoutesResult.inCoverage`
        only if they fall inside).
    :param theWindowBufferM: buffer in metres added to the bbox of
        in-coverage points before cropping the DEM. The Dijkstra graph
        is built on the cropped window only.
    :param theWayPointStrength: way-point-optimisation coefficient
        ``alpha`` per thesis § 6.4. ``0.0`` = no waypoint preference
        (raw least-cost Tobler routes). ``2.0`` (default) = strong
        preference for routes through corridors near other settlements.
    :param theFriction: optional friction grid in seconds per metre on
        the **full** DEM grid (``inf`` = impassable), e.g. the output of
        :func:`la.lib.labarriers.frictionFromVector`. Windowed together
        with the DEM.
    :param theBarriersPath: optional path of a vector layer of barriers
        (rivers, lakes, walls) — rasterised onto the DEM with
        :func:`la.lib.labarriers.frictionFromVector`. Mutually exclusive
        with ``theFriction``.
    :return: :class:`WalkingRoutesResult` with routes in **both
        directions** per pair (i→j and j→i).
    :rtype: WalkingRoutesResult
    :raises ValueError: if fewer than 2 input points fall within DEM
        coverage (no routes possible), ``theWayPointStrength < 0``,
        ``theFriction`` does not match the DEM shape, or both friction
        arguments are given.
    :raises FileNotFoundError: if the DEM path doesn't exist.
    :raises ImportError: if ``scipy`` is not installed.
    """
    if theWayPointStrength < 0:
        raise ValueError(
            f"theWayPointStrength must be ≥0; got {theWayPointStrength}."
        )
    if theFriction is not None and theBarriersPath is not None:
        raise ValueError("Pass either theFriction or theBarriersPath, not both.")
    if not os.path.isfile(str(theDemPath)):
        raise FileNotFoundError(f"DEM not found at {theDemPath}.")

    myRaw, myGeoTransform, myProjection = laraster._readBand(str(theDemPath))
    myFullDem = myRaw.astype(np.float64)
    myFullRows, myFullCols = myFullDem.shape
    myCellX = abs(myGeoTransform[1])
    myCellY = abs(myGeoTransform[5])
    myLeft   = myGeoTransform[0]
    myTop    = myGeoTransform[3]
    myRight  = myLeft + myFullCols * myGeoTransform[1]
    myBottom = myTop  + myFullRows * myGeoTransform[5]

    myInCoverage = {
        i for i, (x, y) in enumerate(thePoints)
        if myLeft <= x <= myRight and myBottom <= y <= myTop
    }
    if len(myInCoverage) < 2:
        raise ValueError(
            f"Need ≥2 points within DEM coverage; got {len(myInCoverage)}."
        )

    myFullFriction = theFriction
    if theBarriersPath is not None:
        from la.lib import labarriers
        myFullFriction, _ = labarriers.frictionFromVector(str(theBarriersPath), str(theDemPath))
    if myFullFriction is not None and np.shape(myFullFriction) != myFullDem.shape:
        raise ValueError(
            f"theFriction shape {np.shape(myFullFriction)} does not match the DEM "
            f"{myFullDem.shape}."
        )

    # Window the DEM to the bbox of in-coverage points + buffer, snapped
    # outward to whole cells and clamped to the grid.
    myXs = [thePoints[i][0] for i in myInCoverage]
    myYs = [thePoints[i][1] for i in myInCoverage]
    myColStart = _clamp(math.floor((min(myXs) - theWindowBufferM - myLeft) / myCellX), 0, myFullCols - 1)
    myColStop  = _clamp(math.ceil((max(myXs) + theWindowBufferM - myLeft) / myCellX), myColStart + 1, myFullCols)
    myRowStart = _clamp(math.floor((myTop - (max(myYs) + theWindowBufferM)) / myCellY), 0, myFullRows - 1)
    myRowStop  = _clamp(math.ceil((myTop - (min(myYs) - theWindowBufferM)) / myCellY), myRowStart + 1, myFullRows)

    myDem = np.ascontiguousarray(myFullDem[myRowStart:myRowStop, myColStart:myColStop])
    myFriction = (
        np.ascontiguousarray(np.asarray(myFullFriction, dtype=np.float64)[myRowStart:myRowStop, myColStart:myColStop])
        if myFullFriction is not None else None
    )
    myWindowGeoTransform = (
        myLeft + myColStart * myGeoTransform[1], myGeoTransform[1], 0.0,
        myTop  + myRowStart * myGeoTransform[5], 0.0, myGeoTransform[5],
    )
    myRows, myCols = myDem.shape
    myWindowBounds = (
        myWindowGeoTransform[0],
        myWindowGeoTransform[3] + myRows * myGeoTransform[5],
        myWindowGeoTransform[0] + myCols * myGeoTransform[1],
        myWindowGeoTransform[3],
    )

    # Convert each in-coverage point to (row, col) in the windowed DEM.
    myRowCol: dict[int, tuple[int, int]] = {}
    for myIdx in myInCoverage:
        myX, myY = thePoints[myIdx]
        myR, myC = laraster._seedCell(myWindowGeoTransform, myX, myY)
        if 0 <= myR < myRows and 0 <= myC < myCols:
            myRowCol[myIdx] = (myR, myC)

    if len(myRowCol) < 2:
        raise ValueError(
            "After windowing, fewer than 2 points landed on valid DEM cells."
        )

    # Build the Tobler edge graph once. It is used twice — unmodified for
    # the multi-origin way-point surface and for the reported route
    # costs, and friction-multiplied for the per-origin routing.
    myCellDiag = math.sqrt(myCellX ** 2 + myCellY ** 2)
    myRowsEdges, myColsEdges, myCostsEdges = laraster._toblerEdges(
        myDem, myCellX, myCellY, myCellDiag, theFriction=myFriction,
    )
    myN = myRows * myCols

    myAdjustedCosts = myCostsEdges
    if theWayPointStrength > 0:
        mySeedRows = np.array([r for (r, _) in myRowCol.values()], dtype=np.int64)
        mySeedCols = np.array([c for (_, c) in myRowCol.values()], dtype=np.int64)
        myMultiOrigin = _multiOriginCostSurface(
            myDem, myCellX, myCellY, myRowsEdges, myColsEdges, myCostsEdges,
            mySeedRows, mySeedCols,
        )
        myFinite = myMultiOrigin[np.isfinite(myMultiOrigin)]
        myMaxCost = float(myFinite.max()) if myFinite.size else 0.0
        if myMaxCost > 0:
            myNorm = np.where(
                np.isfinite(myMultiOrigin),
                myMultiOrigin / myMaxCost,
                1.0,  # unreachable cells: treat as maximally remote
            )
            myFlatNorm = myNorm.ravel()
            myAdjustedCosts = myCostsEdges * (1.0 + theWayPointStrength * myFlatNorm[myColsEdges])

    # Per-edge lookup of the unmodified Tobler cost, for the route cost.
    myEdgeCostByPair = _edgeCostLookup(myRowsEdges, myColsEdges, myCostsEdges, myN)

    # For each origin, run dijkstra with predecessors. Inner loop is
    # SYMMETRIC: every (origin, destination) pair where they differ.
    # This produces N*(N-1) routes — both i→j and j→i are kept,
    # because Tobler costs are anisotropic and the routes can diverge
    # on slopes.
    myOrderedIds = sorted(myRowCol.keys())
    myAccumulation = np.zeros(myDem.shape, dtype=np.int32)
    myRoutes:     list[list[Point]] = []
    myRouteIds:   list[tuple[int, int]] = []
    myRouteCosts: list[float] = []
    myRoutePaths: list[list[int]] = []  # flat-index chains for the peak-usage pass

    for myOriginId in myOrderedIds:
        myOriginRow, myOriginCol = myRowCol[myOriginId]
        myOriginFlat = myOriginRow * myCols + myOriginCol
        _, myPred = _dijkstraWithPredecessors(
            myRowsEdges, myColsEdges, myAdjustedCosts, myN, myOriginFlat,
        )
        for myDestId in myOrderedIds:
            if myDestId == myOriginId:
                continue
            myDestRow, myDestCol = myRowCol[myDestId]
            myDestFlat = myDestRow * myCols + myDestCol
            myPath = _walkPredecessorChain(myPred, myOriginFlat, myDestFlat)
            if not myPath:
                continue
            myRing: list[Point] = []
            for myFlat in myPath:
                myR, myC = divmod(myFlat, myCols)
                myAccumulation[myR, myC] += 1
                myRing.append((
                    float(myWindowGeoTransform[0] + (myC + 0.5) * myWindowGeoTransform[1]),
                    float(myWindowGeoTransform[3] + (myR + 0.5) * myWindowGeoTransform[5]),
                ))
            myRoutes.append(myRing)
            myRouteIds.append((myOriginId, myDestId))
            myRouteCosts.append(_pathCost(myPath, myEdgeCostByPair, myN))
            myRoutePaths.append(myPath)

    # Second pass: per-route peak usage = max accumulation along its
    # cells. Has to happen after accumulating all routes (otherwise
    # the first route always reads peak=1).
    myRoutePeakUsage: list[int] = []
    for myPath in myRoutePaths:
        myRowsIdx, myColsIdx = np.divmod(np.asarray(myPath, dtype=np.int64), myCols)
        myRoutePeakUsage.append(int(myAccumulation[myRowsIdx, myColsIdx].max()))

    return WalkingRoutesResult(
        routes             = myRoutes,
        routeIds           = myRouteIds,
        routeCosts         = myRouteCosts,
        routePeakUsage     = myRoutePeakUsage,
        accumulation       = myAccumulation,
        windowBounds       = myWindowBounds,
        windowGeoTransform = myWindowGeoTransform,
        projectionWkt      = myProjection or "",
        inCoverage         = set(myRowCol.keys()),
    )


def _clamp(theValue: int, theLow: int, theHigh: int) -> int:
    """Clamp ``theValue`` into ``[theLow, theHigh]``.

    :rtype: int
    """
    return int(max(theLow, min(theHigh, theValue)))


def _multiOriginCostSurface(
    theDem:        np.ndarray,
    theCellX:      float,
    theCellY:      float,
    theRowsEdges:  np.ndarray,
    theColsEdges:  np.ndarray,
    theCostsEdges: np.ndarray,
    theSeedRows:   np.ndarray,
    theSeedCols:   np.ndarray,
) -> np.ndarray:
    """Cost-to-nearest-seed surface over an already-built edge graph.

    Delegates to :func:`la.lib.laraster._dijkstraFromSeeds` (super-source
    trick, scipy or heap fallback) with an edge builder that simply hands
    back the prebuilt Tobler edges, so the graph is not rebuilt.

    :return: 2-D float64 cost grid shaped like ``theDem``; ``inf`` where
        no seed can reach.
    :rtype: numpy.ndarray
    """
    def _prebuiltEdges(theDemArg, theCellXArg, theCellYArg, theCellDiagArg, theFrictionArg=None):
        return theRowsEdges, theColsEdges, theCostsEdges

    return laraster._dijkstraFromSeeds(
        theDem, theCellX, theCellY,
        np.asarray(theSeedRows, dtype=np.int64),
        np.asarray(theSeedCols, dtype=np.int64),
        np.zeros(len(theSeedRows), dtype=np.float64),
        theEdgeBuilder=_prebuiltEdges,
    )


def _dijkstraWithPredecessors(
    theRowIdx:    np.ndarray,
    theColIdx:    np.ndarray,
    theCost:      np.ndarray,
    theNodeCount: int,
    theSourceIdx: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Single-source Dijkstra returning distances **and** predecessors.

    :mod:`la.lib.laraster` only ever needs distances, so this is the one
    solver the path network keeps for itself. ``scipy`` is required.

    :return: ``(distances, predecessors)`` — both length
        ``theNodeCount``; ``predecessors`` uses :data:`_NO_PREDECESSOR`
        for the source and for unreachable nodes.
    :rtype: tuple
    :raises ImportError: if ``scipy`` is not installed.
    """
    try:
        from scipy.sparse import csr_matrix
        from scipy.sparse.csgraph import dijkstra
    except ImportError as myError:
        raise ImportError(_SCIPY_REQUIRED_MESSAGE) from myError

    myGraph = csr_matrix(
        (theCost, (theRowIdx, theColIdx)),
        shape=(theNodeCount, theNodeCount),
    )
    myDist, myPred = dijkstra(
        csgraph=myGraph,
        indices=int(theSourceIdx),
        return_predecessors=True,
        directed=True,
    )
    return myDist, myPred


def _walkPredecessorChain(
    thePred:     np.ndarray,
    theSource:   int,
    theTarget:   int,
) -> list[int]:
    """Walk ``thePred`` from ``theTarget`` back to ``theSource``.

    :return: flat indices of the path in source→target order, or
        ``[]`` if the target is unreachable.
    :rtype: list
    """
    if thePred[theTarget] == _NO_PREDECESSOR and theTarget != theSource:
        return []
    myPath: list[int] = []
    myNode = int(theTarget)
    # Hard cap on path length so a broken predecessor array can't loop
    # forever. The DEM diagonal is the longest plausible path.
    for _ in range(thePred.shape[0] + 1):
        myPath.append(int(myNode))
        if myNode == theSource:
            myPath.reverse()
            return myPath
        myPrev = int(thePred[myNode])
        if myPrev == _NO_PREDECESSOR:
            return []
        myNode = myPrev
    return []


def _edgeCostLookup(
    theRowIdx:    np.ndarray,
    theColIdx:    np.ndarray,
    theCost:      np.ndarray,
    theNodeCount: int,
) -> dict:
    """Sorted ``(key, cost)`` arrays keyed by ``src * n + dst`` for fast lookup.

    :return: ``{"keys": int64 array (sorted), "costs": float64 array}``.
    :rtype: dict
    """
    myKeys = np.asarray(theRowIdx, dtype=np.int64) * int(theNodeCount) + np.asarray(theColIdx, dtype=np.int64)
    myOrder = np.argsort(myKeys, kind="stable")
    return {"keys": myKeys[myOrder], "costs": np.asarray(theCost, dtype=np.float64)[myOrder]}


def _pathCost(thePath: list[int], theLookup: dict, theNodeCount: int) -> float:
    """Sum the unmodified edge costs along a flat-index path.

    :param thePath: flat indices in travel order (length ≥ 1).
    :param theLookup: output of :func:`_edgeCostLookup`.
    :param theNodeCount: number of grid cells (the key stride).
    :return: total cost in the edge builder's units (seconds for Tobler).
    :rtype: float
    """
    if len(thePath) < 2:
        return 0.0
    myNodes = np.asarray(thePath, dtype=np.int64)
    myWanted = myNodes[:-1] * int(theNodeCount) + myNodes[1:]
    myPos = np.searchsorted(theLookup["keys"], myWanted)
    myPos = np.minimum(myPos, len(theLookup["keys"]) - 1)
    myFound = theLookup["keys"][myPos] == myWanted
    myCosts = np.where(myFound, theLookup["costs"][myPos], 0.0)
    return float(myCosts.sum())


def categoriseUsage(
    theAccumulation: np.ndarray,
    theNumClasses:   int = 3,
) -> list[int]:
    """Equal-quantile usage thresholds from a route-accumulation raster.

    :param theAccumulation: per-cell route-count raster, 0+ ints.
    :param theNumClasses: how many usage classes (default 3:
        light/medium/heavy).
    :return: ``[t_1, t_2, ..., t_{numClasses-1}]`` — usage count
        thresholds. A cell with count <= ``t_1`` is class 0
        ("light"); ``t_1 < count <= t_2`` is class 1; etc.
    :rtype: list
    :raises ValueError: if ``theNumClasses < 2``.
    """
    if theNumClasses < 2:
        raise ValueError(f"theNumClasses must be ≥2; got {theNumClasses}.")
    myNonzero = theAccumulation[theAccumulation > 0]
    if myNonzero.size == 0:
        return [0] * (theNumClasses - 1)
    myQuantiles = np.linspace(0.0, 1.0, theNumClasses + 1)[1:-1]
    return [int(np.quantile(myNonzero, q)) for q in myQuantiles]
