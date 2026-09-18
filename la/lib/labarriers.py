"""
labarriers.py — turn a vector layer of rivers, lakes and walls into a friction grid.

Pure GDAL/OGR (no Qt), so it is testable with GeoJSON files. The QGIS side
exports the chosen ``QgsVectorLayer`` to a GeoPackage on the main thread and
hands the path to :class:`la.lib.lacatchment.LaCatchment`, which calls
:func:`frictionFromVector` on the current DEM window and feeds the grid to
:func:`la.lib.laraster.makeWalkCost` (``theFriction``: seconds per metre
added to every edge entering the cell; ``inf`` = impassable).

Per-feature rule, in precedence order (mirrors the web app):

1. a ``crossing_penalty`` attribute in minutes — negative means impassable;
2. a ``barrier_type`` attribute: ``impassable`` / ``ford``;
3. geometry: polygons (lakes, standing water) are impassable, lines and
   points (rivers, streams) cost :data:`DEFAULT_FORD_MINUTES` to cross.

Friction is never negative: scipy's Dijkstra silently returns wrong distances
on negative weights. A faster-than-walking corridor must be a small positive
penalty, not a negative one.
"""

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
from osgeo import gdal, ogr, osr

DEFAULT_FORD_MINUTES = 30.0
PENALTY_FIELD = "crossing_penalty"
TYPE_FIELD = "barrier_type"
IMPASSABLE = float("inf")


@dataclass(frozen=True)
class BarrierEffect:
    """How many features were supplied and how many cells they actually touched."""
    features: int
    cells: int

    @property
    def reachedRaster(self) -> bool:
        return self.cells > 0


def _penaltyMinutes(theFeature, theGeometryType: int) -> float:
    """Minutes to cross one cell of this feature; negative = impassable."""
    myDefinition = theFeature.GetDefnRef()
    myIndex = myDefinition.GetFieldIndex(PENALTY_FIELD)
    if myIndex >= 0 and theFeature.IsFieldSetAndNotNull(myIndex):
        try:
            return float(theFeature.GetField(myIndex))
        except (TypeError, ValueError):
            pass
    myTypeIndex = myDefinition.GetFieldIndex(TYPE_FIELD)
    if myTypeIndex >= 0 and theFeature.IsFieldSetAndNotNull(myTypeIndex):
        myType = str(theFeature.GetField(myTypeIndex) or "").strip().lower()
        if myType.startswith("impass"):
            return -1.0
        if myType.startswith("ford"):
            return DEFAULT_FORD_MINUTES
    myFlat = ogr.GT_Flatten(theGeometryType)
    if myFlat in (ogr.wkbPolygon, ogr.wkbMultiPolygon):
        return -1.0
    return DEFAULT_FORD_MINUTES


def frictionFromVector(theVectorPath: str, theDemPath: str,
                       theDefaultFordMinutes: float = DEFAULT_FORD_MINUTES) -> Tuple[Optional[np.ndarray], BarrierEffect]:
    """
    Rasterise every feature of ``theVectorPath`` onto ``theDemPath``'s grid.

    Features are reprojected into the DEM's CRS when both carry one. Cells are
    burnt with ``ALL_TOUCHED`` so a one-cell-wide river never leaks
    diagonally (the corner-cut sealing happens later in
    :func:`la.lib.laraster._cornerAwareFriction`).

    :return: ``(friction, effect)`` — ``friction`` is a float32 grid in seconds
        per metre (``inf`` impassable) or None when the layer has no features.
    :raises FileNotFoundError: If the DEM or the vector file cannot be opened.
    """
    myDem = gdal.Open(theDemPath)
    if myDem is None:
        raise FileNotFoundError(f"Could not open DEM {theDemPath}")
    myGeoTrans = myDem.GetGeoTransform()
    myCols, myRows = myDem.RasterXSize, myDem.RasterYSize
    myProjection = myDem.GetProjection()
    myCellSize = abs(myGeoTrans[1])
    myDem = None

    myVector = ogr.Open(theVectorPath)
    if myVector is None:
        raise FileNotFoundError(f"Could not open barrier layer {theVectorPath}")

    myTargetSrs = None
    if myProjection:
        myTargetSrs = osr.SpatialReference()
        myTargetSrs.ImportFromWkt(myProjection)
        myTargetSrs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)

    myFriction = np.zeros((myRows, myCols), dtype=np.float32)
    myFeatureCount = 0
    myMemDriver = ogr.GetDriverByName("Memory")
    myRasterDriver = gdal.GetDriverByName("MEM")

    for myLayerIndex in range(myVector.GetLayerCount()):
        myLayer = myVector.GetLayerByIndex(myLayerIndex)
        mySourceSrs = myLayer.GetSpatialRef()
        myTransform = None
        if myTargetSrs is not None and mySourceSrs is not None and not mySourceSrs.IsSame(myTargetSrs):
            mySourceSrs = mySourceSrs.Clone()
            mySourceSrs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
            myTransform = osr.CoordinateTransformation(mySourceSrs, myTargetSrs)
        myLayer.ResetReading()
        for myFeature in myLayer:
            myGeometry = myFeature.GetGeometryRef()
            if myGeometry is None or myGeometry.IsEmpty():
                continue
            myFeatureCount += 1
            myGeometry = myGeometry.Clone()
            if myTransform is not None:
                try:
                    myGeometry.Transform(myTransform)
                except RuntimeError:
                    continue
            myMinutes = _penaltyMinutes(myFeature, myGeometry.GetGeometryType())
            if myMinutes == DEFAULT_FORD_MINUTES and theDefaultFordMinutes != DEFAULT_FORD_MINUTES:
                myMinutes = theDefaultFordMinutes
            myValue = IMPASSABLE if myMinutes < 0 else float(myMinutes) * 60.0 / myCellSize

            myMemVector = myMemDriver.CreateDataSource("barrier")
            myMemLayer = myMemVector.CreateLayer("f", srs=myTargetSrs, geom_type=myGeometry.GetGeometryType())
            myMemFeature = ogr.Feature(myMemLayer.GetLayerDefn())
            myMemFeature.SetGeometry(myGeometry)
            myMemLayer.CreateFeature(myMemFeature)
            myMask = myRasterDriver.Create("", myCols, myRows, 1, gdal.GDT_Byte)
            myMask.SetGeoTransform(myGeoTrans)
            if myProjection:
                myMask.SetProjection(myProjection)
            gdal.RasterizeLayer(myMask, [1], myMemLayer, burn_values=[1], options=["ALL_TOUCHED=TRUE"])
            myBurnt = myMask.GetRasterBand(1).ReadAsArray() > 0
            myMask = None
            myMemVector = None
            if myBurnt.any():
                myFriction[myBurnt] = np.maximum(myFriction[myBurnt], myValue)

    myVector = None
    myCells = int((myFriction > 0).sum())
    if myFeatureCount == 0:
        return None, BarrierEffect(0, 0)
    return myFriction, BarrierEffect(myFeatureCount, myCells)
