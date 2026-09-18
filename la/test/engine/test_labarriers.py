"""Barrier rasterisation and its effect on the walking-cost surface (no QGIS)."""

import json
import math

import numpy as np
import pytest
from osgeo import gdal

from la.lib import labarriers, laraster

_UTM36 = ('PROJCS["WGS 84 / UTM zone 36N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],'
          'PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],'
          'PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",33],PARAMETER["scale_factor",0.9996],'
          'PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1],AUTHORITY["EPSG","32636"]]')


def _flatDem(thePath, theSize=60, theCell=30.0, theX0=744000.0, theY0=3612000.0):
    myDs = gdal.GetDriverByName("GTiff").Create(thePath, theSize, theSize, 1, gdal.GDT_Float32)
    myDs.SetGeoTransform((theX0, theCell, 0.0, theY0, 0.0, -theCell))
    myDs.SetProjection(_UTM36)
    myDs.GetRasterBand(1).WriteArray(np.full((theSize, theSize), 100.0, dtype=np.float32))
    myDs = None
    return theX0, theY0, theCell, theSize


def _geojson(thePath, theFeatures, theCrs=None):
    myDoc = {"type": "FeatureCollection", "features": theFeatures}
    if theCrs:
        myDoc["crs"] = {"type": "name", "properties": {"name": theCrs}}
    with open(thePath, "w") as f:
        json.dump(myDoc, f)


def test_polygon_is_impassable_and_line_is_a_ford(tmp_path):
    myDem = str(tmp_path / "dem.tif")
    x0, y0, cell, n = _flatDem(myDem)
    myVector = str(tmp_path / "b.geojson")
    _geojson(myVector, [
        {"type": "Feature", "properties": {}, "geometry": {"type": "Polygon", "coordinates": [[
            [x0 + 5 * cell, y0 - 5 * cell], [x0 + 10 * cell, y0 - 5 * cell], [x0 + 10 * cell, y0 - 10 * cell],
            [x0 + 5 * cell, y0 - 10 * cell], [x0 + 5 * cell, y0 - 5 * cell]]]}},
        {"type": "Feature", "properties": {}, "geometry": {"type": "LineString", "coordinates": [
            [x0 + 30 * cell + 1, y0 - 1], [x0 + 30 * cell + 1, y0 - n * cell + 1]]}},
        {"type": "Feature", "properties": {"crossing_penalty": 5}, "geometry": {"type": "LineString", "coordinates": [
            [x0 + 1, y0 - 50 * cell - 1], [x0 + n * cell - 1, y0 - 50 * cell - 1]]}},
    ], theCrs="urn:ogc:def:crs:EPSG::32636")
    myFriction, myEffect = labarriers.frictionFromVector(myVector, myDem)
    assert myEffect.features == 3 and myEffect.reachedRaster
    assert np.isinf(myFriction[7, 7])                                   # inside the lake
    assert myFriction[20, 30] == pytest.approx(30 * 60 / cell)          # river column: 30-minute ford
    assert myFriction[50, 20] == pytest.approx(5 * 60 / cell)           # explicit 5-minute crossing
    assert myFriction[2, 2] == 0.0
    assert not (myFriction < 0).any()


def test_wgs84_barriers_are_reprojected_onto_the_dem(tmp_path):
    from osgeo import osr

    myDem = str(tmp_path / "dem.tif")
    x0, y0, cell, n = _flatDem(myDem)
    mySrs = osr.SpatialReference(); mySrs.ImportFromWkt(_UTM36); mySrs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    myWgs = osr.SpatialReference(); myWgs.ImportFromEPSG(4326); myWgs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    myToWgs = osr.CoordinateTransformation(mySrs, myWgs)
    myPoints = [myToWgs.TransformPoint(x0 + 30 * cell + 1, y0 - 1), myToWgs.TransformPoint(x0 + 30 * cell + 1, y0 - n * cell + 1)]
    myVector = str(tmp_path / "wgs.geojson")
    _geojson(myVector, [{"type": "Feature", "properties": {"barrier_type": "impassable"},
                         "geometry": {"type": "LineString", "coordinates": [[p[0], p[1]] for p in myPoints]}}],
             theCrs="urn:ogc:def:crs:OGC:1.3:CRS84")
    myFriction, myEffect = labarriers.frictionFromVector(myVector, myDem)
    assert myEffect.reachedRaster
    assert np.isinf(myFriction[:, 30]).sum() >= n - 2


def test_impassable_wall_splits_the_walk_cost_surface(tmp_path):
    myDem = str(tmp_path / "dem.tif")
    x0, y0, cell, n = _flatDem(myDem)
    myVector = str(tmp_path / "wall.geojson")
    _geojson(myVector, [{"type": "Feature", "properties": {"barrier_type": "impassable"},
                         "geometry": {"type": "LineString", "coordinates": [
                             [x0 + 30 * cell + 1, y0 + 100], [x0 + 30 * cell + 1, y0 - n * cell - 100]]}}],
             theCrs="urn:ogc:def:crs:EPSG::32636")
    myFriction, _ = labarriers.frictionFromVector(myVector, myDem)
    mySeedX, mySeedY = x0 + 10 * cell + cell / 2, y0 - 30 * cell - cell / 2
    myCost = laraster.makeWalkCost(myDem, mySeedX, mySeedY, str(tmp_path / "s"), theFriction=myFriction)
    myGrid = gdal.Open(myCost).ReadAsArray()
    assert np.isfinite(myGrid[30, 10])
    assert np.isnan(myGrid[30, 50])                       # the far side is unreachable
    assert np.isfinite(myGrid[30, 29])                    # right up to the wall is fine
    # a 30-minute ford instead: reachable, and about 1800 s dearer than the mirror cell
    _geojson(myVector, [{"type": "Feature", "properties": {},
                         "geometry": {"type": "LineString", "coordinates": [
                             [x0 + 30 * cell + 1, y0 + 100], [x0 + 30 * cell + 1, y0 - n * cell - 100]]}}],
             theCrs="urn:ogc:def:crs:EPSG::32636")
    myFord, _ = labarriers.frictionFromVector(myVector, myDem)
    myCost2 = laraster.makeWalkCost(myDem, mySeedX, mySeedY, str(tmp_path / "s2"), theFriction=myFord)
    myGrid2 = gdal.Open(myCost2).ReadAsArray()
    myBase = laraster.makeWalkCost(myDem, mySeedX, mySeedY, str(tmp_path / "s3"))
    myBaseGrid = gdal.Open(myBase).ReadAsArray()
    assert math.isfinite(myGrid2[30, 50])
    assert myGrid2[30, 50] - myBaseGrid[30, 50] == pytest.approx(1800.0, abs=15.0)


def test_empty_layer_gives_no_friction(tmp_path):
    myDem = str(tmp_path / "dem.tif")
    _flatDem(myDem)
    myVector = str(tmp_path / "empty.geojson")
    _geojson(myVector, [], theCrs="urn:ogc:def:crs:EPSG::32636")
    myFriction, myEffect = labarriers.frictionFromVector(myVector, myDem)
    assert myFriction is None and myEffect.features == 0 and not myEffect.reachedRaster
