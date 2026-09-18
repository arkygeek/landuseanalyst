"""
laxtent.py — Renfrew & Level (1979) site-size-weighted territorial allocation.

Thesis Ch 6, § 6.3, p. 333–336 compares Thiessen polygons (equal weight
per site, :mod:`la.lib.laregional`) with XTent (site size as weighting
factor). Ben Ducke's ``r.xtent`` GRASS module was the historical
reference implementation used by the thesis; this is a clean-room
implementation of the same formula, ported from the Landuse Analyst web
app's ``backend/engine/xtent.py``.

**XTent formula** — for each site ``i`` with size ``C_i`` and a point
``p`` at distance ``d`` from the site::

    influence_i(p) = C_i ** a  -  k * d

where ``a`` is the size-exponent (Renfrew & Level used ``a = 1.5`` with
population; Ducke's defaults for ``r.xtent`` are ``a = 0.5, k = 1``).
A point ``p`` is "controlled by" site ``i`` when:

1. ``influence_i(p) > 0`` — the size win still beats the distance penalty.
2. ``influence_i(p) >= influence_j(p)`` for every other site ``j``.

Points where no site has positive influence are unassigned (empty
space between territories — distinctive of XTent vs Thiessen). Sites
whose territory is entirely dominated by larger neighbours produce
**no** polygon at all.

**Unit assumption** — the default ``k`` is chosen for ``sizeHa`` in
hectares and distances in metres (the southern-Levant case-study CRS
is EPSG:32636, UTM 36N — metres). Running on a CRS with degrees
(EPSG:4326) requires a different ``k`` calibration.

**Implementation** — the web app polygonises the winner grid with
``rasterio.features.shapes``. Here the grid is written to a GDAL ``MEM``
raster (nodata = -1 for unassigned cells) and traced with
``gdal.Polygonize`` into an OGR in-memory layer; the OGR geometries are
then returned as plain GeoJSON-like dicts (:func:`polygoniseLabels`,
:func:`computeXtentFeatures`) or reduced to the web's list-of-rings shape
(:func:`computeXtent`). Both tracers use 4-connectivity, so the
polygons match cell for cell; only the vertex start point / winding of a
ring may differ. No ``qgis`` import; pure ``numpy`` + ``osgeo``.
"""

import json
from typing import Optional, Sequence

import numpy as np
from osgeo import gdal, ogr

Point = tuple[float, float]
Ring = list[Point]
Bbox = tuple[float, float, float, float]

#: Label value of cells no site controls.
UNASSIGNED = -1

_DEFAULT_SIZE_EXPONENT  = 0.5
_DEFAULT_DISTANCE_DECAY = 0.001
_DEFAULT_GRID_RESOLUTION = 250


def computeXtent(
    thePoints:          Sequence[tuple[float, float, float]],
    theBbox:            Bbox,
    theSizeExponent:    float = _DEFAULT_SIZE_EXPONENT,
    theDistanceDecay:   float = _DEFAULT_DISTANCE_DECAY,
    theGridResolution:  int   = _DEFAULT_GRID_RESOLUTION,
) -> list[list[Ring]]:
    """Compute XTent territorial polygons for ``thePoints``.

    :param thePoints: ``[(x, y, sizeHa), ...]`` — settlement
        coordinates in a projected CRS plus site size in hectares.
        Must contain at least 1 point.
    :param theBbox: ``(minX, minY, maxX, maxY)`` in the same CRS as
        ``thePoints`` — the polygonisation domain.
    :param theSizeExponent: ``a`` in the XTent formula. ``0.5`` is
        Ducke's ``r.xtent`` default; raise to favour large sites.
    :param theDistanceDecay: ``k`` in the XTent formula. ``0.001``
        is chosen for size in ha + distance in metres.
    :param theGridResolution: cells per side for the raster grid.
        Clamped silently by the caller, not here. ``250`` is a good
        balance between polygon detail and compute cost (~600K
        floats for 10 sites).
    :return: one list of polygons per input point, same order. A
        site dominated by neighbours returns ``[]``. Each polygon is
        a closed outer ring (``[(x, y), ...]``) of vertices in the
        input CRS; interior rings (holes) are dropped, as in the web
        app. Most sites yield exactly one polygon; some pathological
        configurations yield two disjoint regions.
    :rtype: list
    :raises ValueError: on empty input, a degenerate bbox, a
        non-positive site size or ``theGridResolution < 2``.
    """
    myLabels, myGeoTransform = xtentLabels(
        thePoints, theBbox, theSizeExponent, theDistanceDecay, theGridResolution,
    )
    myBySite = polygoniseLabels(myLabels, myGeoTransform)

    myOutput: list[list[Ring]] = []
    for myIdx in range(len(thePoints)):
        myRings: list[Ring] = []
        for myGeom in myBySite.get(myIdx, []):
            myCoords = myGeom.get("coordinates") or []
            if myGeom.get("type") != "Polygon" or not myCoords:
                continue
            # Take only the outer ring; ignore holes (a site's XTent
            # territory shouldn't have holes anyway — those would mean
            # another site is strictly inside, which by XTent definition
            # means the outer ring belongs to that other site).
            myOuter: Ring = [(float(x), float(y)) for x, y in myCoords[0]]
            if myOuter and myOuter[0] != myOuter[-1]:
                myOuter.append(myOuter[0])
            myRings.append(myOuter)
        myOutput.append(myRings)
    return myOutput


def computeXtentFeatures(
    thePoints:          Sequence[tuple[float, float, float]],
    theBbox:            Bbox,
    theSizeExponent:    float = _DEFAULT_SIZE_EXPONENT,
    theDistanceDecay:   float = _DEFAULT_DISTANCE_DECAY,
    theGridResolution:  int   = _DEFAULT_GRID_RESOLUTION,
) -> dict:
    """XTent territories as a GeoJSON-like ``FeatureCollection`` dict.

    Same maths as :func:`computeXtent`, but the polygons are returned
    with their holes intact and tagged with the site they belong to, so
    the QGIS side can hand the dict straight to
    ``QgsJsonUtils.stringToFeatureList`` (or write it with OGR).

    :return: ``{"type": "FeatureCollection", "features": [...]}`` — one
        feature per connected territory, ``properties`` =
        ``{"site": <input index>, "sizeHa": <size>}`` and a GeoJSON
        ``Polygon`` geometry (outer ring first, then any holes). Sites
        that control no cell have no feature. Order: by site index, then
        by OGR feature order.
    :rtype: dict
    """
    myLabels, myGeoTransform = xtentLabels(
        thePoints, theBbox, theSizeExponent, theDistanceDecay, theGridResolution,
    )
    myBySite = polygoniseLabels(myLabels, myGeoTransform)
    myFeatures = []
    for myIdx in range(len(thePoints)):
        for myGeom in myBySite.get(myIdx, []):
            myFeatures.append({
                "type": "Feature",
                "properties": {"site": myIdx, "sizeHa": float(thePoints[myIdx][2])},
                "geometry": myGeom,
            })
    return {"type": "FeatureCollection", "features": myFeatures}


def xtentLabels(
    thePoints:          Sequence[tuple[float, float, float]],
    theBbox:            Bbox,
    theSizeExponent:    float = _DEFAULT_SIZE_EXPONENT,
    theDistanceDecay:   float = _DEFAULT_DISTANCE_DECAY,
    theGridResolution:  int   = _DEFAULT_GRID_RESOLUTION,
) -> tuple[np.ndarray, tuple]:
    """Winner-index grid of the XTent model over ``theBbox``.

    The grid is ``theGridResolution`` cells square, north-up, with cell
    ``(0, 0)`` at the top-left ``(minX, maxY)`` corner. Influence is
    evaluated at pixel centres.

    :return: ``(labels, geoTransform)`` — ``labels`` is an ``int32``
        ``(H, W)`` array holding the controlling site's input index or
        :data:`UNASSIGNED`; ``geoTransform`` is the six-element GDAL
        geotransform of that grid (suitable for
        :func:`la.lib.laraster._writeGeoTiff` with nodata ``-1``).
    :rtype: tuple
    :raises ValueError: on empty input, a degenerate bbox, a
        non-positive site size or ``theGridResolution < 2``.
    """
    if len(thePoints) < 1:
        raise ValueError("XTent needs at least 1 input point.")
    if theGridResolution < 2:
        raise ValueError(f"gridResolution must be ≥2; got {theGridResolution}.")

    myMinX, myMinY, myMaxX, myMaxY = theBbox
    if myMaxX <= myMinX or myMaxY <= myMinY:
        raise ValueError(f"Bbox is degenerate or inverted: {theBbox}.")

    myXs    = np.array([p[0] for p in thePoints], dtype=float)
    myYs    = np.array([p[1] for p in thePoints], dtype=float)
    mySizes = np.array([p[2] for p in thePoints], dtype=float)

    if np.any(mySizes <= 0):
        raise ValueError("All site sizes must be strictly positive.")

    myH = int(theGridResolution)
    myW = int(theGridResolution)
    myCellX = (myMaxX - myMinX) / myW
    myCellY = (myMaxY - myMinY) / myH
    myGeoTransform = (myMinX, myCellX, 0.0, myMaxY, 0.0, -myCellY)

    # Pixel-centre sample positions, y descending (row 0 = top).
    myPxX = myMinX + (np.arange(myW) + 0.5) * myCellX
    myPxY = myMaxY - (np.arange(myH) + 0.5) * myCellY
    myMeshX, myMeshY = np.meshgrid(myPxX, myPxY)

    # Influence cube: shape (N, H, W). For each site compute its
    # influence at every pixel. Broadcasts cleanly.
    myDx = myMeshX[None, :, :] - myXs[:, None, None]
    myDy = myMeshY[None, :, :] - myYs[:, None, None]
    myDist = np.sqrt(myDx * myDx + myDy * myDy)
    mySizePow = mySizes ** theSizeExponent     # shape (N,)
    myInfluence = mySizePow[:, None, None] - theDistanceDecay * myDist

    # Per-pixel: who wins, and is the win positive?
    myWinner = np.argmax(myInfluence, axis=0)               # (H, W) int
    myMaxInfluence = np.max(myInfluence, axis=0)            # (H, W) float
    myAssigned = myMaxInfluence > 0                          # (H, W) bool

    myLabels = np.where(myAssigned, myWinner, UNASSIGNED).astype(np.int32)
    return myLabels, myGeoTransform


def polygoniseLabels(
    theLabels:       np.ndarray,
    theGeoTransform: tuple,
    theNoData:       int = UNASSIGNED,
    theProjection:   Optional[str] = None,
) -> dict[int, list[dict]]:
    """Trace every connected run of equal label into a GeoJSON-like Polygon.

    Replaces ``rasterio.features.shapes``: the grid goes into a GDAL
    ``MEM`` raster whose nodata mask hides ``theNoData`` cells, and
    ``gdal.Polygonize`` (4-connected) writes one OGR feature per
    connected region into an in-memory layer.

    :param theLabels: 2-D integer array of region labels.
    :param theGeoTransform: six-element GDAL geotransform of the grid.
    :param theNoData: label value to leave untraced.
    :param theProjection: optional WKT to stamp on the scratch raster
        (informational only — coordinates come from the geotransform).
    :return: ``{label: [geometry, ...]}`` where each geometry is
        ``{"type": "Polygon", "coordinates": [outerRing, hole, ...]}``
        with ``(x, y)`` float tuples and every ring closed.
    :rtype: dict
    :raises RuntimeError: if GDAL cannot polygonise the grid.
    """
    myLabels = np.ascontiguousarray(np.asarray(theLabels, dtype=np.int32))
    myRows, myCols = myLabels.shape

    myRaster = gdal.GetDriverByName("MEM").Create("", int(myCols), int(myRows), 1, gdal.GDT_Int32)
    myRaster.SetGeoTransform(tuple(float(v) for v in theGeoTransform))
    if theProjection:
        myRaster.SetProjection(theProjection)
    myBand = myRaster.GetRasterBand(1)
    myBand.SetNoDataValue(float(theNoData))
    myBand.WriteArray(myLabels)
    myBand.FlushCache()

    myDriver = ogr.GetDriverByName("Memory") or ogr.GetDriverByName("MEM")
    myVector = myDriver.CreateDataSource("xtent")
    myLayer = myVector.CreateLayer("territories", None, ogr.wkbPolygon)
    myLayer.CreateField(ogr.FieldDefn("label", ogr.OFTInteger))

    myStatus = gdal.Polygonize(myBand, myBand.GetMaskBand(), myLayer, 0, [])
    if myStatus != 0:
        raise RuntimeError(f"gdal.Polygonize failed with status {myStatus}.")

    myBySite: dict[int, list[dict]] = {}
    myLayer.ResetReading()
    for myFeature in myLayer:
        myLabel = int(myFeature.GetField(0))
        myGeomRef = myFeature.GetGeometryRef()
        if myGeomRef is None:
            continue
        myGeom = json.loads(myGeomRef.ExportToJson())
        if myGeom.get("type") != "Polygon":
            continue
        myGeom["coordinates"] = [
            _closeRing([(float(c[0]), float(c[1])) for c in myRing])
            for myRing in myGeom["coordinates"]
        ]
        myBySite.setdefault(myLabel, []).append(myGeom)

    myLayer = None
    myVector = None
    myBand = None
    myRaster = None
    return myBySite


def _closeRing(theRing: Ring) -> Ring:
    """Return ``theRing`` with its first vertex repeated at the end if needed.

    :rtype: list
    """
    if theRing and theRing[0] != theRing[-1]:
        return theRing + [theRing[0]]
    return theRing
