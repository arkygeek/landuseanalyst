"""
laraster.py — pure-NumPy catchment raster engine (no GRASS, no Qt).

This module is the plugin-side port of the Landuse Analyst web app's
``backend/engine/raster.py``. Every function takes raster paths in and
returns a raster path out; the caller owns the scratch directory and
its cleanup. It deliberately imports nothing from ``qgis`` so it can be
exercised under a plain ``python3`` with ``numpy`` + ``osgeo``; ``scipy``
is imported lazily inside the functions that need it and a pure-Python
heap Dijkstra takes over on small grids when it is missing.

I/O goes through ``osgeo.gdal`` (the web app uses ``rasterio``, which is
not bundled with QGIS). GDAL only finalises a GeoTIFF when the last
reference to the dataset is dropped, so every writer here ends with
``band = None; ds = None`` after ``FlushCache()``.

ACKNOWLEDGMENTS
---------------
The walking-cost algorithm replicates GRASS ``r.walk`` (originally by
Steno Fontanari, ITC-IRST 1992, and Pierre de Mouveaux; maintained by
Markus Neteler, Hamish Bowman, Roberto Flor and the GRASS development
team) using Waldo Tobler's hiking function:

    Tobler, W. (1993). "Three Presentations on Geographical Analysis and
    Modeling: Non-Isotropic Geographic Modeling; Speculations on the
    Geometry of Geography; and Global Spatial Analysis." NCGIA Technical
    Report 93-1.

The catchment workflow that consumes these surfaces is a Python port of
Jason Jorgenson's C++ Landuse Analyst — see ``cppArchive/`` and
``CREDITS.md`` in this repository.
"""

from __future__ import annotations

import heapq
import math
import os
import uuid
from collections import deque
from typing import Callable, Optional, Tuple

import numpy as np
from osgeo import gdal


# ---------------------------------------------------------------------------
# Travel direction
# ---------------------------------------------------------------------------
#: Which way the journey is costed. Only matters once edges are asymmetric —
#: which slope already makes them mildly, and which a current, a portage or a
#: one-way ferry makes strongly.
#:
#: - :data:`DIRECTION_OUTBOUND` — cost from the seed out to each cell. The
#:   historical behaviour and the default, so existing results are unchanged.
#: - :data:`DIRECTION_INBOUND` — cost from each cell back to the seed. The
#:   binding constraint when the load is carried home.
#: - :data:`DIRECTION_ROUND_TRIP` — both legs summed, so a threshold means the
#:   complete out-and-back journey fits within it.
DIRECTION_OUTBOUND:   str = "outbound"
DIRECTION_INBOUND:    str = "inbound"
DIRECTION_ROUND_TRIP: str = "round_trip"

# ---------------------------------------------------------------------------
# Tobler's hiking function parameters
# ---------------------------------------------------------------------------
_V_PEAK_KMH      = 6.0       # peak walking speed, km/h
_SLOPE_PENALTY   = 3.5       # exponential slope penalty
_DOWNHILL_BIAS   = 0.05      # peak speed occurs at a gentle downhill
_MAX_COST_SEC    = 40000.0   # ~11 h walking; matches the C++ original's max_cost
_MAX_COST_METRES = 40000.0   # 40 km cap for the Euclidean surface

# ---------------------------------------------------------------------------
# Tile-Dijkstra dispatch + geometry
# ---------------------------------------------------------------------------
# The single-pass csr_matrix + dijkstra build peaks at ~280 bytes per cell.
# Above _TILE_DISPATCH_PIXELS cells we route to a tiled implementation that
# bounds per-tile memory by working on _TILE_SIZE² blocks with _TILE_HALO-
# pixel halos and BFS-propagating from the seed tile outward. See
# _makeCostTiled for the algorithm and its cross-tile back-edge caveat.
_TILE_DISPATCH_PIXELS = 4_000_000
_TILE_SIZE            = 1024
_TILE_HALO            = 128

#: Largest grid the pure-Python heap Dijkstra will attempt when scipy is
#: missing (512²). Above this the fallback is too slow to be useful.
_HEAP_FALLBACK_MAX_CELLS = 262_144

_SCIPY_REQUIRED_MESSAGE = (
    "scipy is required for grids larger than 512×512 cells "
    "(python -m pip install scipy)"
)

#: Signature shared by the edge builders: ``(dem, cellX, cellY, cellDiag,
#: friction) -> (srcFlat, dstFlat, weight)``.
EdgeBuilder = Callable[..., Tuple[np.ndarray, np.ndarray, np.ndarray]]

_NUMPY_TO_GDAL_TYPE = {
    np.dtype(np.uint8):   gdal.GDT_Byte,
    np.dtype(np.int16):   gdal.GDT_Int16,
    np.dtype(np.uint16):  gdal.GDT_UInt16,
    np.dtype(np.int32):   gdal.GDT_Int32,
    np.dtype(np.uint32):  gdal.GDT_UInt32,
    np.dtype(np.float32): gdal.GDT_Float32,
    np.dtype(np.float64): gdal.GDT_Float64,
}


# ---------------------------------------------------------------------------
# GDAL I/O helpers
# ---------------------------------------------------------------------------
def _openDataset(thePath: str) -> gdal.Dataset:
    """Open a raster read-only, raising instead of returning ``None``.

    :param thePath: Path to any GDAL-readable raster.
    :return: The open dataset. The caller must drop the reference when done.
    :rtype: osgeo.gdal.Dataset
    :raises FileNotFoundError: If GDAL cannot open the raster.
    """
    try:
        myDataset = gdal.Open(str(thePath), gdal.GA_ReadOnly)
    except RuntimeError as myError:  # gdal.UseExceptions() may be on in the host
        raise FileNotFoundError(f"Could not open raster {thePath}: {myError}") from myError
    if myDataset is None:
        raise FileNotFoundError(f"Could not open raster {thePath}")
    return myDataset


def _readBand(thePath: str) -> Tuple[np.ndarray, tuple, str]:
    """Read band 1 of a raster plus its georeferencing.

    The dataset reference is held in a local for the duration of the read —
    chaining ``gdal.Open(p).GetRasterBand(1).ReadAsArray()`` on one line lets
    Python free the dataset mid-call and segfaults under the GDAL bindings.

    :param thePath: Path to a single-band GDAL-readable raster.
    :return: ``(array, geoTransform, projectionWkt)``.
    :rtype: tuple
    :raises FileNotFoundError: If GDAL cannot open the raster.
    """
    myDataset = _openDataset(thePath)
    myBand = myDataset.GetRasterBand(1)
    myArray = myBand.ReadAsArray()
    myGeoTransform = myDataset.GetGeoTransform()
    myProjection = myDataset.GetProjection()
    myBand = None
    myDataset = None
    return myArray, myGeoTransform, myProjection


def _readBandWithNoData(thePath: str) -> Tuple[np.ndarray, tuple, str, Optional[float]]:
    """Like :func:`_readBand` but also returns the band's nodata value.

    :param thePath: Path to a single-band GDAL-readable raster.
    :return: ``(array, geoTransform, projectionWkt, noData)``.
    :rtype: tuple
    """
    myDataset = _openDataset(thePath)
    myBand = myDataset.GetRasterBand(1)
    myArray = myBand.ReadAsArray()
    myGeoTransform = myDataset.GetGeoTransform()
    myProjection = myDataset.GetProjection()
    myNoData = myBand.GetNoDataValue()
    myBand = None
    myDataset = None
    return myArray, myGeoTransform, myProjection, myNoData


def _rasterShape(thePath: str) -> Tuple[int, int]:
    """Return ``(rows, cols)`` of a raster without reading its pixels.

    :param thePath: Path to a GDAL-readable raster.
    :return: ``(rows, cols)``.
    :rtype: tuple
    """
    myDataset = _openDataset(thePath)
    myShape = (myDataset.RasterYSize, myDataset.RasterXSize)
    myDataset = None
    return myShape


def _writeGeoTiff(
    thePath: str,
    theArray: np.ndarray,
    theGeoTransform: tuple,
    theProjection: str,
    theDtype,
    theNoData: Optional[float],
) -> str:
    """Write a single-band GeoTIFF (LZW, tiled) and finalise it on disk.

    :param thePath: Output path.
    :param theArray: 2-D array of pixel values; cast to ``theDtype``.
    :param theGeoTransform: Six-element GDAL geotransform.
    :param theProjection: Projection WKT (may be an empty string).
    :param theDtype: NumPy dtype (or anything ``np.dtype`` accepts) of the
        output band.
    :param theNoData: Nodata value to record on the band, or ``None`` for
        none. ``float("nan")`` is legal for float bands.
    :return: ``thePath``.
    :rtype: str
    """
    myDtype = np.dtype(theDtype)
    myGdalType = _NUMPY_TO_GDAL_TYPE[myDtype]
    myRows, myCols = theArray.shape
    myDriver = gdal.GetDriverByName("GTiff")
    myDataset = myDriver.Create(
        str(thePath), int(myCols), int(myRows), 1, myGdalType,
        options=["COMPRESS=LZW", "TILED=YES"],
    )
    myDataset.SetGeoTransform(tuple(theGeoTransform))
    if theProjection:
        myDataset.SetProjection(theProjection)
    myBand = myDataset.GetRasterBand(1)
    if theNoData is not None:
        myBand.SetNoDataValue(float(theNoData))
    myBand.WriteArray(np.ascontiguousarray(theArray.astype(myDtype, copy=False)))
    myBand.FlushCache()
    myDataset.FlushCache()
    # GDAL only finalises the GeoTIFF (header + directory) when the last
    # reference to the dataset is dropped. Without these the file stays
    # write-locked and the very next gdal.Open() on it fails with
    # "not recognized as a supported file format".
    myBand = None
    myDataset = None
    return str(thePath)


def _writeMaskCoregistered(
    theMask: np.ndarray,
    theReferenceRaster: str,
    theOutPath: str,
) -> None:
    """Write a ``uint8`` ``{0,1}`` mask co-registered with a reference raster.

    :param theMask: 2-D ``numpy.ndarray`` of ``uint8`` values (0 or 1).
    :param theReferenceRaster: Path to read geotransform + projection from.
        Cell grid must match ``theMask``.
    :param theOutPath: Output GeoTIFF path.
    :rtype: None
    """
    myReference = _openDataset(theReferenceRaster)
    myGeoTransform = myReference.GetGeoTransform()
    myProjection = myReference.GetProjection()
    myReference = None
    _writeGeoTiff(
        theOutPath, theMask.astype(np.uint8), myGeoTransform, myProjection,
        np.uint8, 0,
    )


def _writeCostGrid(
    theCostGrid: np.ndarray,
    theGeoTransform: tuple,
    theProjection: str,
    theOutPath: str,
) -> str:
    """Persist a Float32 cost grid as a NaN-nodata GeoTIFF.

    :param theCostGrid: 2-D float cost grid (NaN = unreachable / beyond cap).
    :param theGeoTransform: Geotransform of the source DEM.
    :param theProjection: Projection WKT of the source DEM.
    :param theOutPath: Output path.
    :return: ``theOutPath``.
    :rtype: str
    """
    return _writeGeoTiff(
        theOutPath, theCostGrid, theGeoTransform, theProjection,
        np.float32, float("nan"),
    )


def _scratchPath(theScratchDir: str, theStem: str) -> str:
    """Return a unique GeoTIFF path inside ``theScratchDir`` (created if needed).

    :param theScratchDir: Directory for scratch rasters.
    :param theStem: Human-readable stem for the file name.
    :return: ``<dir>/_la_<stem>_<8 hex>.tif``.
    :rtype: str
    """
    os.makedirs(theScratchDir, exist_ok=True)
    return os.path.join(str(theScratchDir), f"_la_{theStem}_{uuid.uuid4().hex[:8]}.tif")


def _seedCell(theGeoTransform: tuple, theX: float, theY: float) -> Tuple[int, int]:
    """Map a map coordinate to ``(row, col)`` on a north-up grid.

    Uses ``floor`` (like ``rasterio.transform.rowcol``) so a coordinate just
    outside the top-left corner lands at ``-1`` rather than being truncated
    onto cell 0.

    :param theGeoTransform: Six-element GDAL geotransform.
    :param theX: Easting in the raster's CRS units.
    :param theY: Northing in the raster's CRS units.
    :return: ``(row, col)``; may be out of range — the caller checks.
    :rtype: tuple
    """
    myCol = math.floor((theX - theGeoTransform[0]) / theGeoTransform[1])
    myRow = math.floor((theY - theGeoTransform[3]) / theGeoTransform[5])
    return int(myRow), int(myCol)


# ---------------------------------------------------------------------------
# Edge construction
# ---------------------------------------------------------------------------
def _directions(theCellX: float, theCellY: float, theCellDiag: float) -> list:
    """The fixed 8-neighbour ordering shared by every edge builder.

    The order is load-bearing: it fixes the order edges are laid out in the
    sparse graph and therefore the golden numbers of the Shuna test.

    :return: ``[(dRow, dCol, edgeLengthMetres), ...]`` N, NE, E, SE, S, SW, W, NW.
    :rtype: list
    """
    return [
        (-1,  0, theCellY),     # N
        (-1,  1, theCellDiag),  # NE
        ( 0,  1, theCellX),     # E
        ( 1,  1, theCellDiag),  # SE
        ( 1,  0, theCellY),     # S
        ( 1, -1, theCellDiag),  # SW
        ( 0, -1, theCellX),     # W
        (-1, -1, theCellDiag),  # NW
    ]


def _cornerAwareFriction(
    theFriction:  np.ndarray,
    theDr:        int,
    theDc:        int,
    theSrcWindow: Tuple[int, int, int, int],
    theDstWindow: Tuple[int, int, int, int],
) -> np.ndarray:
    """Destination friction for one direction, including diagonal corner-cuts.

    A barrier rasterised from a line is a **4-connected staircase**, but the
    walker moves on an **8-connected** graph. Where the staircase steps, two
    barrier cells meet at a corner while the two cells diagonally opposite are
    both clear — so a diagonal move can pass through that corner without ever
    entering a barrier cell. Charging only ``friction[destination]`` lets it
    through for nothing: a river running diagonally leaked (a 30-minute
    crossing cost 0.3 minutes, an impassable river was walked through in
    18 seconds) while an axis-aligned one sealed correctly.

    The fix charges a diagonal step for what it squeezes past. If both
    flanking cells — the two sharing the corner being cut — carry friction,
    the step cannot avoid the barrier and pays at least the cheaper of them.
    Taking the **minimum** of the flanks is the lenient reading (cross at the
    easier side); taking the **maximum** against the destination leaves a
    head-on crossing costing exactly what it always did.

    Straight steps are returned untouched.

    :param theFriction: Full ``(rows, cols)`` friction grid, seconds per metre.
    :param theDr: Row offset of this direction — ``-1``, ``0`` or ``1``.
    :param theDc: Column offset of this direction.
    :param theSrcWindow: ``(rowStart, rowStop, colStart, colStop)`` of the
        source-cell slice for this direction.
    :param theDstWindow: The same for the destination-cell slice.
    :return: Effective friction, shaped like the direction's window.
    :rtype: numpy.ndarray
    """
    mySrcRowStart, mySrcRowStop, mySrcColStart, mySrcColStop = theSrcWindow
    myDstRowStart, myDstRowStop, myDstColStart, myDstColStop = theDstWindow

    myDstFriction = theFriction[myDstRowStart:myDstRowStop, myDstColStart:myDstColStop]
    if theDr == 0 or theDc == 0:
        return myDstFriction

    # The two cells sharing the cut corner are (srcRow + dr, srcCol) and
    # (srcRow, srcCol + dc). Their slices reuse the windows already computed —
    # rows from one, columns from the other — so both match the window shape.
    myFlankA = theFriction[myDstRowStart:myDstRowStop, mySrcColStart:mySrcColStop]
    myFlankB = theFriction[mySrcRowStart:mySrcRowStop, myDstColStart:myDstColStop]

    return np.maximum(myDstFriction, np.minimum(myFlankA, myFlankB))


def _directionWindows(theRows: int, theCols: int, theDr: int, theDc: int):
    """Source + destination slice bounds for one neighbour direction.

    :return: ``((srcRow0, srcRow1, srcCol0, srcCol1), (dstRow0, dstRow1, dstCol0, dstCol1))``.
    :rtype: tuple
    """
    mySrc = (
        max(0, -theDr), min(theRows, theRows - theDr),
        max(0, -theDc), min(theCols, theCols - theDc),
    )
    myDst = (
        max(0,  theDr), min(theRows, theRows + theDr),
        max(0,  theDc), min(theCols, theCols + theDc),
    )
    return mySrc, myDst


def _flatIndices(theCols: int, theWindow: Tuple[int, int, int, int]) -> np.ndarray:
    """Row-major flat indices of every cell in a slice window.

    :param theCols: Grid width.
    :param theWindow: ``(rowStart, rowStop, colStart, colStop)``.
    :return: 1-D ``int32`` array, row-major order.
    :rtype: numpy.ndarray
    """
    myRowStart, myRowStop, myColStart, myColStop = theWindow
    myR = np.arange(myRowStart, myRowStop, dtype=np.int32)[:, None]
    myC = np.arange(myColStart, myColStop, dtype=np.int32)[None, :]
    return (myR * theCols + myC).ravel()


def _toblerEdges(
    theDem:      np.ndarray,
    theCellX:    float,
    theCellY:    float,
    theCellDiag: float,
    theFriction: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build directed 8-neighbour Tobler walk-cost edges over a DEM array.

    For each directed edge (cell A → cell B)::

        slope     = (z_B − z_A) / horizontal_distance          [signed]
        velocity  = 6.0 * exp(-3.5 * |slope + 0.05|)           [km/h]
        edge_cost = horizontal_distance / velocity_in_m_per_s  [seconds]

    Uphill and downhill across the same pair are different edges with
    different costs (anisotropic). Friction, when supplied, adds
    ``friction[destination] * edge_length`` seconds, with the diagonal
    corner-cut correction of :func:`_cornerAwareFriction`; ``np.inf``
    friction makes a cell impassable.

    :param theDem: 2-D float DEM array.
    :param theCellX: Pixel width in metres.
    :param theCellY: Pixel height in metres.
    :param theCellDiag: Diagonal pixel size in metres.
    :param theFriction: Optional 2-D float friction grid (seconds/metre).
    :return: Three flat arrays — source flat-index, destination flat-index,
        edge weight in seconds.
    :rtype: tuple
    """
    myRows, myCols = theDem.shape
    myDirections = _directions(theCellX, theCellY, theCellDiag)

    myTotalEdges = 0
    for myDr, myDc, _ in myDirections:
        myTotalEdges += (myRows - abs(myDr)) * (myCols - abs(myDc))

    myAllRows  = np.empty(myTotalEdges, dtype=np.int32)
    myAllCols  = np.empty(myTotalEdges, dtype=np.int32)
    myAllCosts = np.empty(myTotalEdges, dtype=np.float64)

    myWriteIdx = 0
    for myDr, myDc, myEdgeLen in myDirections:
        mySrcWindow, myDstWindow = _directionWindows(myRows, myCols, myDr, myDc)
        myChunkSize = (mySrcWindow[1] - mySrcWindow[0]) * (mySrcWindow[3] - mySrcWindow[2])

        mySrcZ = theDem[mySrcWindow[0]:mySrcWindow[1], mySrcWindow[2]:mySrcWindow[3]]
        myDstZ = theDem[myDstWindow[0]:myDstWindow[1], myDstWindow[2]:myDstWindow[3]]

        # Signed slope: positive = uphill from src to dst.
        mySlope  = (myDstZ - mySrcZ) / myEdgeLen
        myVelKmh = _V_PEAK_KMH * np.exp(-_SLOPE_PENALTY * np.abs(mySlope + _DOWNHILL_BIAS))
        myVelMs  = myVelKmh * (1000.0 / 3600.0)
        # Clamp to a tiny positive so absolute cliffs don't blow up.
        myEdgeCost = myEdgeLen / np.maximum(myVelMs, 1e-6)

        if theFriction is not None:
            myDstFriction = _cornerAwareFriction(
                theFriction, myDr, myDc, mySrcWindow, myDstWindow,
            )
            myEdgeCost = myEdgeCost + myDstFriction * myEdgeLen

        myAllRows[myWriteIdx:myWriteIdx + myChunkSize]  = _flatIndices(myCols, mySrcWindow)
        myAllCols[myWriteIdx:myWriteIdx + myChunkSize]  = _flatIndices(myCols, myDstWindow)
        myAllCosts[myWriteIdx:myWriteIdx + myChunkSize] = myEdgeCost.ravel()
        myWriteIdx += myChunkSize

    return myAllRows, myAllCols, myAllCosts


def _euclideanEdges(
    theDem:      np.ndarray,
    theCellX:    float,
    theCellY:    float,
    theCellDiag: float,
    theFriction: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build directed 8-neighbour uniform-friction edges over a DEM array.

    Edge weight is the pixel-to-pixel distance in metres; the DEM values are
    intentionally unused (a path-distance / uniform-cost surface, the
    equivalent of GRASS ``r.cost`` against a uniform-1 friction raster).

    :param theDem: 2-D DEM array (read only for its shape).
    :param theCellX: Pixel width in metres.
    :param theCellY: Pixel height in metres.
    :param theCellDiag: Diagonal pixel size in metres.
    :param theFriction: Optional 2-D float friction grid (seconds/metre).
        Converted to metres-per-metre at 5 km/h (1.388… m/s) so the same
        barrier grid serves both cost models.
    :return: Three flat arrays — source flat-index, destination flat-index,
        edge weight in metres.
    :rtype: tuple
    """
    myRows, myCols = theDem.shape
    myDirections = _directions(theCellX, theCellY, theCellDiag)

    myTotalEdges = 0
    for myDr, myDc, _ in myDirections:
        myTotalEdges += (myRows - abs(myDr)) * (myCols - abs(myDc))

    myAllRows  = np.empty(myTotalEdges, dtype=np.int32)
    myAllCols  = np.empty(myTotalEdges, dtype=np.int32)
    myAllCosts = np.empty(myTotalEdges, dtype=np.float64)

    myWriteIdx = 0
    for myDr, myDc, myEdgeLen in myDirections:
        mySrcWindow, myDstWindow = _directionWindows(myRows, myCols, myDr, myDc)
        myChunkSize = (mySrcWindow[1] - mySrcWindow[0]) * (mySrcWindow[3] - mySrcWindow[2])

        myEdgeCost = np.full(myChunkSize, myEdgeLen, dtype=np.float64)

        if theFriction is not None:
            myDstFriction = _cornerAwareFriction(
                theFriction, myDr, myDc, mySrcWindow, myDstWindow,
            )
            # Friction is seconds/metre; convert to metres/metre at 5 km/h.
            myEdgeCost = myEdgeCost + (myDstFriction.ravel() * 1.3888888888888888) * myEdgeLen

        myAllRows[myWriteIdx:myWriteIdx + myChunkSize]  = _flatIndices(myCols, mySrcWindow)
        myAllCols[myWriteIdx:myWriteIdx + myChunkSize]  = _flatIndices(myCols, myDstWindow)
        myAllCosts[myWriteIdx:myWriteIdx + myChunkSize] = myEdgeCost
        myWriteIdx += myChunkSize

    return myAllRows, myAllCols, myAllCosts


# ---------------------------------------------------------------------------
# Shortest-path solvers
# ---------------------------------------------------------------------------
def _dijkstraHeap(
    theRowIdx:    np.ndarray,
    theColIdx:    np.ndarray,
    theCost:      np.ndarray,
    theNodeCount: int,
    theSourceIdx: int,
) -> np.ndarray:
    """Single-source Dijkstra with a binary heap — the no-scipy fallback.

    Reproduces ``scipy.sparse.csgraph.dijkstra(csr_matrix((cost, (row, col))),
    indices=source)`` exactly: duplicate ``(row, col)`` pairs are summed the
    way ``csr_matrix`` sums them, explicit zero weights are kept as edges, and
    ``inf`` weights are unusable. Pure NumPy + :mod:`heapq`; fine up to
    :data:`_HEAP_FALLBACK_MAX_CELLS` nodes, painfully slow beyond.

    :param theRowIdx: Source node of every directed edge.
    :param theColIdx: Destination node of every directed edge.
    :param theCost: Non-negative weight of every directed edge.
    :param theNodeCount: Number of nodes in the graph.
    :param theSourceIdx: Node to start from.
    :return: Length-``theNodeCount`` float64 distances; ``inf`` = unreachable.
    :rtype: numpy.ndarray
    """
    myRow  = np.asarray(theRowIdx, dtype=np.int64)
    myCol  = np.asarray(theColIdx, dtype=np.int64)
    myCost = np.asarray(theCost,   dtype=np.float64)

    # Coalesce duplicate (row, col) pairs by summing, as coo -> csr does.
    myKey = myRow * theNodeCount + myCol
    myOrder = np.argsort(myKey, kind="stable")
    myKey, myCost = myKey[myOrder], myCost[myOrder]
    if myKey.size:
        myIsFirst = np.empty(myKey.size, dtype=bool)
        myIsFirst[0] = True
        np.not_equal(myKey[1:], myKey[:-1], out=myIsFirst[1:])
        myStarts = np.flatnonzero(myIsFirst)
        myCost = np.add.reduceat(myCost, myStarts)
        myKey = myKey[myStarts]
    myRow = myKey // theNodeCount
    myCol = myKey - myRow * theNodeCount

    # CSR layout: rows are already sorted so indptr is a cumulative count.
    myIndptr = np.zeros(theNodeCount + 1, dtype=np.int64)
    np.cumsum(np.bincount(myRow, minlength=theNodeCount), out=myIndptr[1:])
    myIndptrList = myIndptr.tolist()
    myColList = myCol.tolist()
    myCostList = myCost.tolist()

    myDist = np.full(theNodeCount, np.inf, dtype=np.float64)
    myDistList = myDist.tolist()
    myDistList[theSourceIdx] = 0.0
    myDone = bytearray(theNodeCount)
    myHeap = [(0.0, int(theSourceIdx))]
    myInf = math.inf

    while myHeap:
        myD, myU = heapq.heappop(myHeap)
        if myDone[myU]:
            continue
        myDone[myU] = 1
        for myE in range(myIndptrList[myU], myIndptrList[myU + 1]):
            myW = myCostList[myE]
            if myW == myInf:
                continue
            myV = myColList[myE]
            myNd = myD + myW
            if myNd < myDistList[myV]:
                myDistList[myV] = myNd
                heapq.heappush(myHeap, (myNd, myV))

    return np.asarray(myDistList, dtype=np.float64)


def _dijkstraScipy(
    theRowIdx:    np.ndarray,
    theColIdx:    np.ndarray,
    theCost:      np.ndarray,
    theNodeCount: int,
    theSourceIdx: int,
) -> np.ndarray:
    """Single-source Dijkstra via ``scipy.sparse.csgraph``.

    :raises ImportError: If scipy is not installed.
    :return: Length-``theNodeCount`` float64 distances; ``inf`` = unreachable.
    :rtype: numpy.ndarray
    """
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import dijkstra

    myGraph = csr_matrix(
        (theCost, (theRowIdx, theColIdx)),
        shape=(theNodeCount, theNodeCount),
    )
    return dijkstra(csgraph=myGraph, indices=theSourceIdx)


def _solveShortestPaths(
    theRowIdx:    np.ndarray,
    theColIdx:    np.ndarray,
    theCost:      np.ndarray,
    theNodeCount: int,
    theSourceIdx: int,
) -> np.ndarray:
    """Dispatch to scipy's Dijkstra, or the heap fallback when scipy is absent.

    :param theRowIdx: Source node of every directed edge.
    :param theColIdx: Destination node of every directed edge.
    :param theCost: Weight of every directed edge.
    :param theNodeCount: Number of nodes (including any super-source).
    :param theSourceIdx: Node to start from.
    :return: Length-``theNodeCount`` float64 distances.
    :rtype: numpy.ndarray
    :raises ImportError: If scipy is missing and the graph exceeds
        :data:`_HEAP_FALLBACK_MAX_CELLS` grid cells.
    """
    try:
        return _dijkstraScipy(theRowIdx, theColIdx, theCost, theNodeCount, theSourceIdx)
    except ImportError as myError:
        # theNodeCount includes the super-source; the grid itself is one less.
        if theNodeCount - 1 > _HEAP_FALLBACK_MAX_CELLS:
            raise ImportError(_SCIPY_REQUIRED_MESSAGE) from myError
        return _dijkstraHeap(theRowIdx, theColIdx, theCost, theNodeCount, theSourceIdx)


def _dijkstraFromSeeds(
    theDem:           np.ndarray,
    theCellX:         float,
    theCellY:         float,
    theSeedRows:      np.ndarray,
    theSeedCols:      np.ndarray,
    theSeedDistances: np.ndarray,
    theEdgeBuilder:   EdgeBuilder = _toblerEdges,
    theFriction:      Optional[np.ndarray] = None,
    theDirection:     str = DIRECTION_OUTBOUND,
) -> np.ndarray:
    """Multi-source Dijkstra over an edge-weighted graph on a DEM array.

    Each seed cell starts at its supplied initial distance — the helper
    wires a virtual super-source node above the grid and adds edges from it
    to each seed weighted by the initial distance. The super-source's own
    row is sliced off before reshape.

    Single-source case (``len(seeds) == 1``, distance ``0.0``) is exactly
    equivalent to ``dijkstra(graph, indices=seedFlat)``.

    :param theDem: 2-D float DEM array (rows × cols).
    :param theCellX: Pixel width in metres.
    :param theCellY: Pixel height in metres.
    :param theSeedRows: Source-cell rows (length-K int array).
    :param theSeedCols: Source-cell cols (length-K int array).
    :param theSeedDistances: Initial cost at each seed (length-K float).
    :param theEdgeBuilder: Strategy producing the directed 8-neighbour
        edges. Defaults to :func:`_toblerEdges`; pass :func:`_euclideanEdges`
        for path-distance / uniform-cost.
    :param theFriction: Optional 2-D float friction grid.
    :param theDirection: One of :data:`DIRECTION_OUTBOUND` (default),
        :data:`DIRECTION_INBOUND`, :data:`DIRECTION_ROUND_TRIP`.
    :return: 2-D cost grid (same shape as ``theDem``); ``inf`` where
        unreachable.
    :rtype: numpy.ndarray
    :raises ValueError: If ``theDirection`` is not a known direction.
    """
    myRows, myCols = theDem.shape
    myCellDiag     = math.sqrt(theCellX ** 2 + theCellY ** 2)
    myN            = myRows * myCols

    myEdgeRow, myEdgeCol, myEdgeCost = theEdgeBuilder(
        theDem, theCellX, theCellY, myCellDiag, theFriction,
    )

    # Super-source node at flat index myN. Outgoing edges only, so it
    # can't be used as a shortcut between distant seeds.
    mySuperRow  = np.full(np.shape(theSeedRows), myN, dtype=np.int64)
    mySuperCol  = (np.asarray(theSeedRows).astype(np.int64) * myCols
                   + np.asarray(theSeedCols).astype(np.int64))
    mySuperCost = np.asarray(theSeedDistances).astype(np.float64)

    def _solve(theFromIdx: np.ndarray, theToIdx: np.ndarray) -> np.ndarray:
        """Dijkstra over the grid edges in the given orientation.

        The super-source edges are appended *after* any transposition, so the
        virtual node keeps its outgoing-only wiring whichever way the grid
        edges point.
        """
        myAllRow  = np.concatenate([theFromIdx, mySuperRow])
        myAllCol  = np.concatenate([theToIdx,   mySuperCol])
        myAllCost = np.concatenate([myEdgeCost, mySuperCost])
        myDistFlat = _solveShortestPaths(myAllRow, myAllCol, myAllCost, myN + 1, myN)
        return myDistFlat[:myN].reshape(myRows, myCols)

    if theDirection == DIRECTION_OUTBOUND:
        return _solve(myEdgeRow, myEdgeCol)

    # Reversing every grid edge turns "cost from the seed to here" into "cost
    # from here to the seed" — the direction that matters when the load is
    # being carried home rather than out.
    if theDirection == DIRECTION_INBOUND:
        return _solve(myEdgeCol, myEdgeRow)

    if theDirection == DIRECTION_ROUND_TRIP:
        # Exact rather than approximated: solve each leg on its own and add.
        # Symmetrising the edge weights instead would force both legs onto one
        # path, which is wrong wherever the cheapest way back differs from the
        # cheapest way out.
        return _solve(myEdgeRow, myEdgeCol) + _solve(myEdgeCol, myEdgeRow)

    raise ValueError(
        f"Unknown travel direction {theDirection!r}; expected one of "
        f"{DIRECTION_OUTBOUND!r}, {DIRECTION_INBOUND!r}, {DIRECTION_ROUND_TRIP!r}."
    )


def _checkDirection(theDirection: str) -> None:
    """Raise early on an unknown direction, before any expensive work.

    :raises ValueError: If ``theDirection`` is not a known direction.
    """
    if theDirection not in (DIRECTION_OUTBOUND, DIRECTION_INBOUND, DIRECTION_ROUND_TRIP):
        raise ValueError(
            f"Unknown travel direction {theDirection!r}; expected one of "
            f"{DIRECTION_OUTBOUND!r}, {DIRECTION_INBOUND!r}, {DIRECTION_ROUND_TRIP!r}."
        )


# ---------------------------------------------------------------------------
# Cost-surface builders
# ---------------------------------------------------------------------------
def _loadDemForCost(theDemPath: str, theX: float, theY: float):
    """Read a DEM as float64 and locate the seed cell.

    :return: ``(dem, geoTransform, projection, cellX, cellY, seedRow, seedCol)``.
    :rtype: tuple
    :raises ValueError: If the seed falls outside the DEM.
    """
    myRaw, myGeoTransform, myProjection = _readBand(theDemPath)
    myDem = myRaw.astype(np.float64)
    myRows, myCols = myDem.shape
    myCellX = abs(myGeoTransform[1])
    myCellY = abs(myGeoTransform[5])
    mySeedRow, mySeedCol = _seedCell(myGeoTransform, theX, theY)
    if not (0 <= mySeedRow < myRows and 0 <= mySeedCol < myCols):
        raise ValueError(
            f"Seed ({theX}, {theY}) → cell ({mySeedRow}, {mySeedCol}) "
            f"is outside the DEM ({myRows} × {myCols})."
        )
    return myDem, myGeoTransform, myProjection, myCellX, myCellY, mySeedRow, mySeedCol


def _makeCostSinglePass(
    theDemPath:     str,
    theX:           float,
    theY:           float,
    theScratchDir:  str,
    theMaxCost:     float,
    theEdgeBuilder: EdgeBuilder,
    theScratchStem: str,
    theFriction:    Optional[np.ndarray] = None,
    theDirection:   str = DIRECTION_OUTBOUND,
) -> str:
    """Single-pass Dijkstra cost surface (the fast path for small DEMs).

    Parameterised on ``theEdgeBuilder`` so both Tobler walking-cost
    (seconds) and Euclidean path-distance (metres) share the same machinery.

    :param theDemPath: Input DEM path.
    :param theX: Seed easting in the DEM's CRS units.
    :param theY: Seed northing in the DEM's CRS units.
    :param theScratchDir: Directory for the output GeoTIFF.
    :param theMaxCost: Cells beyond this cost become NaN.
    :param theEdgeBuilder: :func:`_toblerEdges` or :func:`_euclideanEdges`.
    :param theScratchStem: Stem for the output file name.
    :param theFriction: Optional 2-D float friction grid.
    :param theDirection: Travel direction constant.
    :return: Path of the Float32 NaN-nodata cost GeoTIFF.
    :rtype: str
    :raises ValueError: If the seed falls outside the DEM.
    """
    _checkDirection(theDirection)
    (myDem, myGeoTransform, myProjection,
     myCellX, myCellY, mySeedRow, mySeedCol) = _loadDemForCost(theDemPath, theX, theY)

    myCostGrid = _dijkstraFromSeeds(
        myDem, myCellX, myCellY,
        np.array([mySeedRow], dtype=np.int64),
        np.array([mySeedCol], dtype=np.int64),
        np.array([0.0],       dtype=np.float64),
        theEdgeBuilder=theEdgeBuilder,
        theFriction=theFriction,
        theDirection=theDirection,
    )
    myCostGrid[~np.isfinite(myCostGrid)] = np.nan
    myCostGrid[myCostGrid > theMaxCost] = np.nan

    return _writeCostGrid(
        myCostGrid, myGeoTransform, myProjection,
        _scratchPath(theScratchDir, theScratchStem),
    )


def _tiledCostGrid(
    theDem:         np.ndarray,
    theCellX:       float,
    theCellY:       float,
    theSeedRow:     int,
    theSeedCol:     int,
    theMaxCost:     float,
    theEdgeBuilder: EdgeBuilder,
    theFriction:    Optional[np.ndarray],
    theDirection:   str,
) -> np.ndarray:
    """One-direction tile-Dijkstra over an in-memory DEM.

    See :func:`_makeCostTiled` for the algorithm. Reads :data:`_TILE_SIZE`
    and :data:`_TILE_HALO` at call time so tests can shrink them.

    :return: 2-D float64 cost grid; ``inf`` where unreached or beyond cap.
    :rtype: numpy.ndarray
    """
    myRows, myCols = theDem.shape
    myTileSize = _TILE_SIZE
    myHalo = _TILE_HALO

    myTilesY = (myRows + myTileSize - 1) // myTileSize
    myTilesX = (myCols + myTileSize - 1) // myTileSize

    # Globally-stitched cost grid. inf = not yet reached; np.minimum
    # stitches across overlapping tile halos as we go.
    myCostGrid = np.full((myRows, myCols), np.inf, dtype=np.float64)

    mySeedTy = theSeedRow // myTileSize
    mySeedTx = theSeedCol // myTileSize

    myQueue: deque = deque([(mySeedTy, mySeedTx)])
    myVisited: set = {(mySeedTy, mySeedTx)}

    while myQueue:
        myTy, myTx = myQueue.popleft()

        myIntRowStart = myTy * myTileSize
        myIntRowStop  = min((myTy + 1) * myTileSize, myRows)
        myIntColStart = myTx * myTileSize
        myIntColStop  = min((myTx + 1) * myTileSize, myCols)

        myExtRowStart = max(0,      myIntRowStart - myHalo)
        myExtRowStop  = min(myRows, myIntRowStop  + myHalo)
        myExtColStart = max(0,      myIntColStart - myHalo)
        myExtColStop  = min(myCols, myIntColStop  + myHalo)

        myTileDem = theDem[myExtRowStart:myExtRowStop, myExtColStart:myExtColStop]

        # Interior offset within the extended tile coords.
        myLocalIntR0 = myIntRowStart - myExtRowStart
        myLocalIntR1 = myIntRowStop  - myExtRowStart
        myLocalIntC0 = myIntColStart - myExtColStart
        myLocalIntC1 = myIntColStop  - myExtColStart

        mySeedRowsList = []
        mySeedColsList = []
        mySeedDistList = []

        # 1. Original seed, if this tile's extended region contains it.
        if (myExtRowStart <= theSeedRow < myExtRowStop and
                myExtColStart <= theSeedCol < myExtColStop):
            mySeedRowsList.append(np.array([theSeedRow - myExtRowStart], dtype=np.int64))
            mySeedColsList.append(np.array([theSeedCol - myExtColStart], dtype=np.int64))
            mySeedDistList.append(np.array([0.0], dtype=np.float64))

        # 2. Halo seeds: any extended-region cell *outside* this tile's
        #    interior that already has a finite global cost.
        myGlobalSlice = myCostGrid[myExtRowStart:myExtRowStop, myExtColStart:myExtColStop]
        myHaloMask = np.ones(myTileDem.shape, dtype=bool)
        myHaloMask[myLocalIntR0:myLocalIntR1, myLocalIntC0:myLocalIntC1] = False
        myHaloFiniteMask = myHaloMask & np.isfinite(myGlobalSlice)

        if np.any(myHaloFiniteMask):
            myHaloRows, myHaloCols = np.nonzero(myHaloFiniteMask)
            mySeedRowsList.append(myHaloRows.astype(np.int64))
            mySeedColsList.append(myHaloCols.astype(np.int64))
            mySeedDistList.append(myGlobalSlice[myHaloRows, myHaloCols].astype(np.float64))

        if not mySeedRowsList:
            # No seeds for this tile — nothing to compute. (Shouldn't
            # happen for the seed tile, but a far-disconnected tile
            # could queue then find no halo data.)
            continue

        mySeedRows = np.concatenate(mySeedRowsList)
        mySeedCols = np.concatenate(mySeedColsList)
        mySeedDist = np.concatenate(mySeedDistList)

        myTileFriction = (
            theFriction[myExtRowStart:myExtRowStop, myExtColStart:myExtColStop]
            if theFriction is not None
            else None
        )
        myTileCost = _dijkstraFromSeeds(
            myTileDem, theCellX, theCellY,
            mySeedRows, mySeedCols, mySeedDist,
            theEdgeBuilder=theEdgeBuilder,
            theFriction=myTileFriction,
            theDirection=theDirection,
        )
        # Clip beyond max-cost so they don't propagate as halo seeds to
        # neighbours and we don't waste a queue entry on them.
        myTileCost[myTileCost > theMaxCost] = np.inf

        # Stitch via element-wise minimum. Tiles that produced a better
        # cost for cells the neighbour also computed win.
        myExtSlice = myCostGrid[myExtRowStart:myExtRowStop, myExtColStart:myExtColStop]
        myCostGrid[myExtRowStart:myExtRowStop, myExtColStart:myExtColStop] = (
            np.minimum(myExtSlice, myTileCost)
        )

        # Queue 4-neighbour tiles if this tile reached anywhere in its
        # interior (otherwise no point — neighbours have nothing to inherit).
        myInteriorCost = myTileCost[myLocalIntR0:myLocalIntR1, myLocalIntC0:myLocalIntC1]
        if np.any(np.isfinite(myInteriorCost)):
            for myDy, myDx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                myNy, myNx = myTy + myDy, myTx + myDx
                if 0 <= myNy < myTilesY and 0 <= myNx < myTilesX:
                    myKey = (myNy, myNx)
                    if myKey not in myVisited:
                        myVisited.add(myKey)
                        myQueue.append(myKey)

    return myCostGrid


def _makeCostTiled(
    theDemPath:     str,
    theX:           float,
    theY:           float,
    theScratchDir:  str,
    theMaxCost:     float,
    theEdgeBuilder: EdgeBuilder,
    theScratchStem: str,
    theFriction:    Optional[np.ndarray] = None,
    theDirection:   str = DIRECTION_OUTBOUND,
) -> str:
    """Tile-based Dijkstra cost surface for large DEMs.

    Splits the DEM into :data:`_TILE_SIZE`-square interior tiles with
    :data:`_TILE_HALO`-wide halos. Processes tiles in BFS order from the
    seed-containing tile outward; each tile inherits boundary distances from
    already-computed neighbours via the multi-source
    :func:`_dijkstraFromSeeds` (the super-source trick lets per-seed initial
    costs come along for the ride).

    Approximation caveat: tiles are *not* re-processed when a later tile
    produces a better boundary distance than they used. Paths that re-enter
    a previously processed tile via a back-edge are under-represented — the
    affected cells' costs are over-estimated, never under.

    For archaeological catchments this is benign: a 1-2 km catchment at
    30 m resolution is 30-60 cells from the seed, well inside a single
    1024² tile.

    A round trip is solved as two independent tiled legs (outbound plus
    inbound) and summed, so halo seed distances are never double-counted.

    :param theDemPath: Input DEM path.
    :param theX: Seed easting in the DEM's CRS units.
    :param theY: Seed northing in the DEM's CRS units.
    :param theScratchDir: Directory for the output GeoTIFF.
    :param theMaxCost: Cells beyond this cost become NaN.
    :param theEdgeBuilder: :func:`_toblerEdges` or :func:`_euclideanEdges`.
    :param theScratchStem: Stem for the output file name.
    :param theFriction: Optional 2-D float friction grid.
    :param theDirection: Travel direction constant.
    :return: Path of the Float32 NaN-nodata cost GeoTIFF.
    :rtype: str
    :raises ValueError: If the seed falls outside the DEM.
    """
    _checkDirection(theDirection)
    (myDem, myGeoTransform, myProjection,
     myCellX, myCellY, mySeedRow, mySeedCol) = _loadDemForCost(theDemPath, theX, theY)

    if theDirection == DIRECTION_ROUND_TRIP:
        myLegs = (DIRECTION_OUTBOUND, DIRECTION_INBOUND)
    else:
        myLegs = (theDirection,)

    myCostGrid = None
    for myLeg in myLegs:
        myLegGrid = _tiledCostGrid(
            myDem, myCellX, myCellY, mySeedRow, mySeedCol, theMaxCost,
            theEdgeBuilder, theFriction, myLeg,
        )
        myCostGrid = myLegGrid if myCostGrid is None else myCostGrid + myLegGrid

    myCostGrid[~np.isfinite(myCostGrid)] = np.nan
    myCostGrid[myCostGrid > theMaxCost] = np.nan

    return _writeCostGrid(
        myCostGrid, myGeoTransform, myProjection,
        _scratchPath(theScratchDir, theScratchStem),
    )


def _dispatchCost(
    theDemPath:     str,
    theX:           float,
    theY:           float,
    theScratchDir:  str,
    theMaxCost:     float,
    theEdgeBuilder: EdgeBuilder,
    theScratchStem: str,
    theForceTiled:  bool,
    theFriction:    Optional[np.ndarray] = None,
    theDirection:   str = DIRECTION_OUTBOUND,
) -> str:
    """Dispatch helper shared by :func:`makeWalkCost` + :func:`makeEuclideanCost`.

    Routes to :func:`_makeCostTiled` when ``theForceTiled`` is set or the DEM
    exceeds :data:`_TILE_DISPATCH_PIXELS` cells, else :func:`_makeCostSinglePass`.

    :return: Path of the Float32 NaN-nodata cost GeoTIFF.
    :rtype: str
    """
    myRows, myCols = _rasterShape(theDemPath)
    myPixels = myRows * myCols
    myImpl = (
        _makeCostTiled
        if (theForceTiled or myPixels > _TILE_DISPATCH_PIXELS)
        else _makeCostSinglePass
    )
    return myImpl(
        theDemPath, theX, theY, theScratchDir,
        theMaxCost, theEdgeBuilder, theScratchStem,
        theFriction=theFriction,
        theDirection=theDirection,
    )


def makeWalkCost(
    theDemPath:    str,
    theX:          float,
    theY:          float,
    theScratchDir: str,
    theMaxCostSec: float = _MAX_COST_SEC,
    theForceTiled: bool = False,
    theFriction:   Optional[np.ndarray] = None,
    theDirection:  str = DIRECTION_OUTBOUND,
) -> str:
    """Build a Tobler walking-cost surface seeded at ``(theX, theY)``.

    Dispatches between a single-pass Dijkstra and a tile-Dijkstra
    implementation based on the DEM's pixel count. The single-pass path is
    exact; the tiled path is exact for any catchment that fits within one
    1024² tile and approximate (over-estimating) for catchments crossing
    tile boundaries — see :func:`_makeCostTiled`.

    :param theDemPath: Path of the input DEM (any GDAL-readable format with
        a north-up geotransform in metres).
    :param theX: Seed easting in the DEM's CRS units.
    :param theY: Seed northing in the DEM's CRS units.
    :param theScratchDir: Directory for the output GeoTIFF.
    :param theMaxCostSec: Cells beyond this many seconds of walking time
        from the seed become NaN in the output.
    :param theForceTiled: Force the tiled path even on small DEMs. For
        verification only.
    :param theFriction: Optional 2-D float friction grid, seconds per metre,
        same shape as the DEM; ``np.inf`` = impassable.
    :param theDirection: :data:`DIRECTION_OUTBOUND` (default),
        :data:`DIRECTION_INBOUND` or :data:`DIRECTION_ROUND_TRIP`.
    :return: Path of the cost-surface GeoTIFF (Float32, NaN nodata, seconds).
    :rtype: str
    :raises ValueError: If the seed falls outside the DEM extent.
    :raises FileNotFoundError: If the DEM cannot be opened.
    """
    return _dispatchCost(
        theDemPath, theX, theY, theScratchDir,
        theMaxCostSec, _toblerEdges, "walkCost", theForceTiled,
        theFriction=theFriction,
        theDirection=theDirection,
    )


def makeEuclideanCost(
    theDemPath:       str,
    theX:             float,
    theY:             float,
    theScratchDir:    str,
    theMaxCostMetres: float = _MAX_COST_METRES,
    theForceTiled:    bool  = False,
    theFriction:      Optional[np.ndarray] = None,
    theDirection:     str = DIRECTION_OUTBOUND,
) -> str:
    """Build a uniform-friction (path-distance) cost surface in metres.

    The pure-Python equivalent of GRASS ``r.cost`` against a uniform-1
    friction raster: Dijkstra over an 8-neighbour graph with edge cost equal
    to pixel-to-pixel distance, ignoring DEM elevation.

    :param theDemPath: Path of a DEM raster. Read only for its geotransform /
        projection / shape — values are intentionally ignored.
    :param theX: Seed easting in the DEM's CRS units.
    :param theY: Seed northing in the DEM's CRS units.
    :param theScratchDir: Directory for the output GeoTIFF.
    :param theMaxCostMetres: Cells beyond this many metres of path distance
        from the seed become NaN. Default 40 km matches ``r.cost max_cost``.
    :param theForceTiled: Force the tiled path on small DEMs (test only).
    :param theFriction: Optional 2-D float friction grid (seconds/metre).
    :param theDirection: Travel direction constant.
    :return: Path of the cost-surface GeoTIFF (Float32, NaN nodata, metres).
    :rtype: str
    :raises ValueError: If the seed falls outside the DEM extent.
    :raises FileNotFoundError: If the DEM cannot be opened.
    """
    return _dispatchCost(
        theDemPath, theX, theY, theScratchDir,
        theMaxCostMetres, _euclideanEdges, "euclideanCost", theForceTiled,
        theFriction=theFriction,
        theDirection=theDirection,
    )


# ---------------------------------------------------------------------------
# Per-iteration mapcalc ops (boolean expressions on co-registered rasters)
# ---------------------------------------------------------------------------
# These mirror the GRASS ``r.mapcalc.simple`` expressions of the original
# plugin. GRASS ``null()`` becomes 0 in a uint8 mask with nodata=0; a NaN
# cost compares False against any threshold, matching GRASS null-propagation.
def reclassCost(
    theCostRaster: str,
    theThreshold:  float,
    theScratchDir: str,
) -> str:
    """Binary mask of cells with ``cost < threshold`` (NaN ⇒ 0).

    :param theCostRaster: Path of a cost-surface raster.
    :param theThreshold: Cost threshold.
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path to a 1/0 uint8 mask GeoTIFF (nodata=0).
    :rtype: str
    """
    myCost, _, _ = _readBand(theCostRaster)
    myMask = (myCost < theThreshold).astype(np.uint8)
    myOut = _scratchPath(theScratchDir, f"reclass_{int(theThreshold)}")
    _writeMaskCoregistered(myMask, theCostRaster, myOut)
    return myOut


def createMask(
    theReclassed:         str,
    theSuitabilityRaster: str,
    theScratchDir:        str,
) -> str:
    """Binary intersection: ``A>=1 & B>=1``.

    :param theReclassed: Output of :func:`reclassCost`.
    :param theSuitabilityRaster: Co-registered suitability raster.
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path to a 1/0 uint8 mask GeoTIFF (nodata=0).
    :rtype: str
    """
    myA, _, _ = _readBand(theReclassed)
    myB, _, _ = _readBand(theSuitabilityRaster)
    myMask = ((myA >= 1) & (myB >= 1)).astype(np.uint8)
    myOut = _scratchPath(theScratchDir, "mask")
    _writeMaskCoregistered(myMask, theReclassed, myOut)
    return myOut


def createInverseMask(
    theCostRaster:      str,
    theThreshold:       float,
    theBaseSuitability: str,
    theScratchDir:      str,
) -> str:
    """Suitable cells outside the catchment: ``B>=1 & A>=threshold``.

    NaN cost cells evaluate ``A >= threshold`` as False — unreachable cells
    don't count as leftover.

    :param theCostRaster: The cost surface.
    :param theThreshold: Cost threshold used for the catchment.
    :param theBaseSuitability: The suitability raster the catchment was
        allocated from.
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path to a 1/0 uint8 leftover mask GeoTIFF (nodata=0).
    :rtype: str
    """
    myCost, _, _ = _readBand(theCostRaster)
    myBase, _, _ = _readBand(theBaseSuitability)
    myMask = ((myBase >= 1) & (myCost >= theThreshold)).astype(np.uint8)
    myOut = _scratchPath(theScratchDir, f"inverse_{int(theThreshold)}")
    _writeMaskCoregistered(myMask, theCostRaster, myOut)
    return myOut


def mergeMasks(
    theA:          str,
    theB:          str,
    theScratchDir: str,
) -> str:
    """Binary union: ``A>=1 | B>=1``.

    :param theA: First mask raster path (also the georeferencing reference).
    :param theB: Second mask raster path.
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path to a 1/0 uint8 union mask GeoTIFF (nodata=0).
    :rtype: str
    """
    myArrA, _, _ = _readBand(theA)
    myArrB, _, _ = _readBand(theB)
    myMask = ((myArrA >= 1) | (myArrB >= 1)).astype(np.uint8)
    myOut = _scratchPath(theScratchDir, "merge")
    _writeMaskCoregistered(myMask, theA, myOut)
    return myOut


def subtractMasks(
    theOuterMask:  str,
    theInnerMask:  str,
    theScratchDir: str,
    theStem:       str = "subtract",
) -> str:
    """Binary difference: ``outer>=1 & inner<1``.

    :param theOuterMask: Mask to subtract from (also the georeferencing
        reference).
    :param theInnerMask: Mask to subtract.
    :param theScratchDir: Directory for the output GeoTIFF.
    :param theStem: Stem for the output file name.
    :return: Path to a 1/0 uint8 difference mask GeoTIFF (nodata=0).
    :rtype: str
    """
    myOuter, _, _ = _readBand(theOuterMask)
    myInner, _, _ = _readBand(theInnerMask)
    myMask = ((myOuter >= 1) & (myInner < 1)).astype(np.uint8)
    myOut = _scratchPath(theScratchDir, theStem)
    _writeMaskCoregistered(myMask, theOuterMask, myOut)
    return myOut


# ---------------------------------------------------------------------------
# Windowing
# ---------------------------------------------------------------------------
def windowRastersAroundSeed(
    theDemPath:         str,
    theSuitabilityPath: str,
    theSeedX:           float,
    theSeedY:           float,
    theWindowPixels:    int,
    theScratchDir:      str,
) -> Tuple[str, str]:
    """Crop a ``theWindowPixels``-square window from both rasters, centred
    on the seed coordinates.

    The windowed crop bounds memory use for :func:`makeWalkCost` (peak is
    ~280 bytes per cell in the cropped raster, regardless of how big the
    source DEM is on disk).

    If the requested window extends beyond the source raster extent on any
    side the window is clamped — the crop will be smaller than
    ``theWindowPixels`` square. Callers shouldn't rely on the output being
    exactly that size (see :func:`maskTouchesBorder`).

    Both rasters must be co-registered (same geotransform + shape); the same
    pixel window is applied to each.

    :param theDemPath: Source DEM path.
    :param theSuitabilityPath: Source suitability raster path.
    :param theSeedX: Seed easting.
    :param theSeedY: Seed northing.
    :param theWindowPixels: Window edge length in pixels.
    :param theScratchDir: Directory for ``dem_window.tif`` and ``suit_window.tif``.
    :return: ``(croppedDemPath, croppedSuitabilityPath)``.
    :rtype: tuple
    """
    myHalf = theWindowPixels // 2
    myDataset = _openDataset(theDemPath)
    myGeoTransform = myDataset.GetGeoTransform()
    myRows, myCols = myDataset.RasterYSize, myDataset.RasterXSize
    myDataset = None

    myCenterRow, myCenterCol = _seedCell(myGeoTransform, theSeedX, theSeedY)
    myRowStart = max(0, myCenterRow - myHalf)
    myRowStop  = min(myRows, myCenterRow + myHalf)
    myColStart = max(0, myCenterCol - myHalf)
    myColStop  = min(myCols, myCenterCol + myHalf)
    mySrcWin = [myColStart, myRowStart, myColStop - myColStart, myRowStop - myRowStart]
    if mySrcWin[2] <= 0 or mySrcWin[3] <= 0:
        raise ValueError(
            f"Seed ({theSeedX}, {theSeedY}) → cell ({myCenterRow}, {myCenterCol}) "
            f"leaves an empty window on the DEM ({myRows} × {myCols})."
        )

    os.makedirs(theScratchDir, exist_ok=True)
    myDemOut  = os.path.join(str(theScratchDir), "dem_window.tif")
    mySuitOut = os.path.join(str(theScratchDir), "suit_window.tif")

    for mySrc, myDst in ((theDemPath, myDemOut), (theSuitabilityPath, mySuitOut)):
        myOut = gdal.Translate(
            myDst, str(mySrc), srcWin=mySrcWin, format="GTiff",
            creationOptions=["COMPRESS=LZW"],
        )
        if myOut is None:
            raise FileNotFoundError(f"gdal.Translate failed windowing {mySrc}")
        myOut.FlushCache()
        myOut = None
    return myDemOut, mySuitOut


def windowSizeForTarget(
    theTargetHa:    float,
    theCellSizeM:   float,
    theMinPixels:   int = 200,
    theMaxPixels:   int = 1500,
) -> int:
    """Size the search window from the land the scenario actually needs.

    Treats the target area as a disc centred on the settlement, takes its
    diameter in pixels, and multiplies by 3 to leave room for the catchment
    being nothing like a disc (suitability masks out cells, so the search
    reaches further; barriers force detours). The result is a starting
    point: :func:`maskTouchesBorder` catches a clipped result so the caller
    can re-run wider.

    :param theTargetHa: Sum of every category's target, in hectares.
    :param theCellSizeM: DEM pixel size in metres.
    :param theMinPixels: Never suggest fewer pixels per side than this.
    :param theMaxPixels: Never suggest more pixels per side than this.
    :return: Window size in pixels per side.
    :rtype: int
    """
    if theTargetHa <= 0.0 or theCellSizeM <= 0.0:
        return theMaxPixels

    myAreaSqM    = theTargetHa * 10_000.0
    myRadiusM    = math.sqrt(myAreaSqM / math.pi)
    myDiameterPx = (2.0 * myRadiusM) / theCellSizeM
    myWindow     = int(math.ceil(myDiameterPx * 3.0))

    return max(theMinPixels, min(myWindow, theMaxPixels))


def maskTouchesBorder(theMaskPath: Optional[str]) -> bool:
    """Did the catchment run into the edge of its window?

    If any set cell sits on the window border the catchment was clipped, and
    a wider window would give a different answer. Area alone cannot reveal
    this — a clipped run can still hit its target area exactly.

    A read failure returns ``True`` so an unreadable mask is treated as
    suspect and re-run wider, never quietly accepted.

    :param theMaskPath: Path to the mask GeoTIFF, or ``None`` (⇒ ``False``).
    :return: ``True`` if the mask has any non-zero cell on its outer ring.
    :rtype: bool
    """
    if not theMaskPath:
        return False
    try:
        myMask, _, _ = _readBand(theMaskPath)
    except Exception:
        return True
    if myMask is None or myMask.size == 0:
        return False
    return bool(
        myMask[0, :].any() or myMask[-1, :].any()
        or myMask[:, 0].any() or myMask[:, -1].any()
    )


# ---------------------------------------------------------------------------
# Slope
# ---------------------------------------------------------------------------
def slopeFromDem(
    theDemPath:    str,
    theScratchDir: str,
) -> str:
    """Compute per-pixel slope in degrees from a DEM.

    Uses :func:`numpy.gradient` for a central-difference dz/dy + dz/dx
    estimate (forward/backward difference at edges). Slope magnitude is
    ``atan(sqrt((dz/dy)**2 + (dz/dx)**2))`` converted to degrees.

    :param theDemPath: Path to a DEM (north-up geotransform, planar units
        consistent with the elevation units).
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path of the slope-degrees GeoTIFF (Float32, NaN nodata).
    :rtype: str
    """
    myRaw, myGeoTransform, myProjection = _readBand(theDemPath)
    myDem = myRaw.astype(np.float64)

    myCellX = abs(myGeoTransform[1])
    myCellY = abs(myGeoTransform[5])

    # np.gradient returns (dz/dy, dz/dx) for a 2-D array; the spacing args
    # are in the DEM's planar units so the result is dimensionless rise/run.
    myDzDy, myDzDx = np.gradient(myDem, myCellY, myCellX)
    myMagnitude = np.sqrt(myDzDy ** 2 + myDzDx ** 2)
    mySlopeDeg  = np.degrees(np.arctan(myMagnitude)).astype(np.float32)

    myOutPath = _scratchPath(theScratchDir, "slopeDeg")
    return _writeGeoTiff(
        myOutPath, mySlopeDeg, myGeoTransform, myProjection,
        np.float32, float("nan"),
    )


def slopeMask(
    theSlopePath:  str,
    theMaxDegrees: float,
    theScratchDir: str,
) -> str:
    """Binary mask of cells with ``slope <= theMaxDegrees``.

    Steep cells and NaN cells are excluded. Intended to be intersected with
    the suitability raster via :func:`createMask` before the catchment
    binary search runs.

    :param theSlopePath: Path to a slope-in-degrees GeoTIFF.
    :param theMaxDegrees: Inclusive upper bound on slope.
    :param theScratchDir: Directory for the output GeoTIFF.
    :return: Path to a 1/0 uint8 mask GeoTIFF (nodata=0).
    :rtype: str
    """
    mySlope, _, _ = _readBand(theSlopePath)
    myMask = (np.isfinite(mySlope) & (mySlope <= theMaxDegrees)).astype(np.uint8)
    myOut  = _scratchPath(theScratchDir, f"slopeMask_{int(theMaxDegrees)}")
    _writeMaskCoregistered(myMask, theSlopePath, myOut)
    return myOut


# ---------------------------------------------------------------------------
# Area
# ---------------------------------------------------------------------------
def getAreaHa(theMaskRaster: str) -> float:
    """Area of cells with value 1 in a binary mask, in hectares.

    :param theMaskRaster: Path to a 1/0 uint8 (or float) mask GeoTIFF with a
        projected CRS in metres.
    :return: Area in hectares.
    :rtype: float
    :raises FileNotFoundError: If the raster cannot be opened.
    """
    myArray, myGeoTransform, _, myNoData = _readBandWithNoData(theMaskRaster)
    myCellArea = abs(myGeoTransform[1] * myGeoTransform[5])  # m² for projected CRS

    if myNoData is not None:
        myCount = int(np.sum((myArray == 1) & (myArray != myNoData)))
    else:
        myCount = int(np.sum(myArray == 1))
    return myCount * myCellArea / 10000.0
