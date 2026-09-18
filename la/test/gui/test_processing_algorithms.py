"""Run the Landuse Analyst Processing algorithms directly (no Processing framework init)."""

import os

import numpy as np
import pytest
from osgeo import gdal

SETTLEMENT_X, SETTLEMENT_Y = 744800.0, 3611100.0


def _pointsLayer(thePoints, theSizes=None):
    from qgis.core import QgsFeature, QgsGeometry, QgsPointXY, QgsVectorLayer

    myLayer = QgsVectorLayer("Point?crs=EPSG:32636&field=size_ha:double", "sites", "memory")
    myFeatures = []
    for myIndex, (x, y) in enumerate(thePoints):
        myFeature = QgsFeature(myLayer.fields())
        myFeature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
        myFeature.setAttributes([float(theSizes[myIndex]) if theSizes else 1.0])
        myFeatures.append(myFeature)
    myLayer.dataProvider().addFeatures(myFeatures)
    return myLayer


def _run(theAlgorithm, theParameters):
    from qgis.core import QgsProcessingContext, QgsProcessingFeedback, QgsProject

    theAlgorithm.initAlgorithm({})
    myContext = QgsProcessingContext()
    myContext.setProject(QgsProject.instance())
    myFeedback = QgsProcessingFeedback()
    myResults, myOk = theAlgorithm.run(theParameters, myContext, myFeedback)
    assert myOk, myFeedback.textLog()
    return myResults, myContext


@pytest.mark.usefixtures("qtApp")
def test_provider_lists_three_algorithms():
    from la.processing.algorithms import allAlgorithms

    myNames = sorted(a.name() for a in allAlgorithms())
    assert myNames == ["thiessen", "walkingroutes", "xtent"]


@pytest.mark.usefixtures("qtApp")
def test_thiessen_territories_cover_the_extent():
    from qgis.core import QgsProject
    from la.processing.lathiessenalgorithm import LaThiessenAlgorithm

    myPoints = [(0.0, 0.0), (1000.0, 0.0), (0.0, 1000.0), (1000.0, 1000.0), (500.0, 500.0)]
    myLayer = _pointsLayer(myPoints)
    QgsProject.instance().addMapLayer(myLayer)
    try:
        myResults, myContext = _run(LaThiessenAlgorithm(), {
            "SITES": myLayer.id(), "EXTENT": "-500,1500,-500,1500 [EPSG:32636]", "OUTPUT": "memory:"})
        myOutput = myContext.getMapLayer(myResults["OUTPUT"])
        assert myOutput.featureCount() == 5
        assert sum(f["area_ha"] for f in myOutput.getFeatures()) == pytest.approx(400.0, rel=1e-3)   # 2000 m square
        assert {f["site_fid"] for f in myOutput.getFeatures()} == {f.id() for f in myLayer.getFeatures()}
    finally:
        QgsProject.instance().removeMapLayer(myLayer.id())


@pytest.mark.usefixtures("qtApp")
def test_xtent_large_site_absorbs_small_neighbour(tmp_path):
    from qgis.core import QgsProject
    from la.processing.laxtentalgorithm import LaXtentAlgorithm

    myLayer = _pointsLayer([(0.0, 0.0), (600.0, 0.0)], theSizes=[100.0, 1.0])
    QgsProject.instance().addMapLayer(myLayer)
    try:
        myLabels = str(tmp_path / "labels.tif")
        myResults, myContext = _run(LaXtentAlgorithm(), {
            "SITES": myLayer.id(), "SIZE_FIELD": "size_ha", "EXTENT": "-2000,2600,-2000,2000 [EPSG:32636]",
            "SIZE_EXPONENT": 0.5, "DISTANCE_DECAY": 0.001, "RESOLUTION": 100,
            "OUTPUT": "memory:", "LABELS": myLabels})
        myOutput = myContext.getMapLayer(myResults["OUTPUT"])
        mySites = {f["site_fid"] for f in myOutput.getFeatures()}
        myBig = next(f.id() for f in myLayer.getFeatures() if f["size_ha"] == 100.0)
        assert mySites == {myBig}                       # the 1 Ha site is dominated
        assert os.path.exists(myLabels)
        myGrid = gdal.Open(myLabels).ReadAsArray()
        assert set(np.unique(myGrid)) <= {-1, 0}
    finally:
        QgsProject.instance().removeMapLayer(myLayer.id())


@pytest.mark.usefixtures("qtApp")
def test_walking_routes_on_the_shuna_window(tmp_path, shunaDemPath):
    pytest.importorskip("scipy")
    from qgis.core import QgsProject, QgsRasterLayer
    from la.processing.lawalkingroutesalgorithm import LaWalkingRoutesAlgorithm

    myDemPath = str(tmp_path / "dem.tif")
    myDs = gdal.Open(shunaDemPath); gt = myDs.GetGeoTransform()
    myCol = int((SETTLEMENT_X - gt[0]) / gt[1]) - 100; myRow = int((SETTLEMENT_Y - gt[3]) / gt[5]) - 100
    gdal.Translate(myDemPath, myDs, srcWin=[myCol, myRow, 200, 200], format="GTiff", outputType=gdal.GDT_Float32)
    myDs = None
    myDem = QgsRasterLayer(myDemPath, "dem")
    mySites = _pointsLayer([(SETTLEMENT_X, SETTLEMENT_Y), (SETTLEMENT_X + 1500, SETTLEMENT_Y + 300),
                            (SETTLEMENT_X - 900, SETTLEMENT_Y - 1200), (SETTLEMENT_X + 400, SETTLEMENT_Y - 1600)])
    QgsProject.instance().addMapLayer(myDem); QgsProject.instance().addMapLayer(mySites)
    try:
        myAccumulation = str(tmp_path / "usage.tif")
        myResults, myContext = _run(LaWalkingRoutesAlgorithm(), {
            "DEM": myDem.id(), "SITES": mySites.id(), "BUFFER_M": 500.0, "WAYPOINT": 2.0,
            "ROUTES": "memory:", "ACCUMULATION": myAccumulation})
        myRoutes = myContext.getMapLayer(myResults["ROUTES"])
        assert myRoutes.featureCount() >= 6                     # 3+ Delaunay edges, both directions
        for myFeature in myRoutes.getFeatures():
            assert myFeature["cost_s"] > 0 and myFeature["cost_h"] == pytest.approx(myFeature["cost_s"] / 3600.0)
            assert myFeature.geometry().length() > 500
        assert os.path.exists(myAccumulation)
        assert gdal.Open(myAccumulation).ReadAsArray().max() >= 2
    finally:
        QgsProject.instance().removeMapLayer(myDem.id()); QgsProject.instance().removeMapLayer(mySites.id())
