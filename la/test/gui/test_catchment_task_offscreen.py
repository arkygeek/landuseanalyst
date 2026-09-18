"""
Full catchment pipeline through the controller and the QGIS task manager.

Windows the real Shuna DEM (200 × 200 cells around the thesis settlement),
builds the low-ground suitability raster, runs one dedicated crop with a 50 Ha target
and checks both the golden numbers and the layer tree the task builds.
"""

import os

import numpy as np
import pytest
from osgeo import gdal

SETTLEMENT_X = 744800.0
SETTLEMENT_Y = 3611100.0
WINDOW = 200
TARGET_HA = 50.0


def _windowDem(theSource: str, theOut: str) -> None:
    myDataset = gdal.Open(theSource)
    myGeoTrans = myDataset.GetGeoTransform()
    myCol = int((SETTLEMENT_X - myGeoTrans[0]) / myGeoTrans[1]) - WINDOW // 2
    myRow = int((SETTLEMENT_Y - myGeoTrans[3]) / myGeoTrans[5]) - WINDOW // 2
    gdal.Translate(theOut, myDataset, srcWin=[myCol, myRow, WINDOW, WINDOW], format="GTiff",
                   outputType=gdal.GDT_Float32, creationOptions=["COMPRESS=LZW"])
    myDataset = None


def _writeSuitability(theDem: str, theOut: str) -> None:
    """'Low ground' suitability (-100 m .. 100 m), the definition behind the golden numbers."""
    myDem = gdal.Open(theDem)
    myElevation = myDem.GetRasterBand(1).ReadAsArray()
    mySuitable = ((myElevation >= -100.0) & (myElevation <= 100.0)).astype(np.uint8)
    myOut = gdal.GetDriverByName("GTiff").Create(theOut, WINDOW, WINDOW, 1, gdal.GDT_Byte)
    myOut.SetGeoTransform(myDem.GetGeoTransform())
    myOut.SetProjection(myDem.GetProjection())
    myOut.GetRasterBand(1).WriteArray(mySuitable)
    myOut.FlushCache()
    myOut = None
    myDem = None


class _StubCrop:
    def __init__(self, theName):
        self.name = theName


class _StubParameter:
    def __init__(self, theRaster):
        self.name = "WheatTest params"
        self.rasterName = theRaster
        self.useCommonLand = False
        self.useCommonGrazingLand = False


class _StubModel:
    """Only what LaCatchment / LaCatchmentTask read off an LaModel."""

    def __init__(self):
        self.name = "Shuna smoke"
        self.period = "Chalcolithic"
        self.easting = SETTLEMENT_X
        self.northing = SETTLEMENT_Y
        self.precision = 5
        self.mCropsMap = {"wheat-guid": "wheat-param-guid"}
        self.mAreaTargetsCropsMap = {"wheat-guid": TARGET_HA}
        self.mAnimalsMap = {}
        self.mAreaTargetsAnimalsMap = {}


@pytest.mark.usefixtures("qtApp")
def test_controller_runs_catchment_task_and_builds_layer_tree(tmp_path, shunaDemPath, monkeypatch):
    pytest.importorskip("scipy")
    from qgis.PyQt.QtTest import QTest
    from qgis.core import QgsProject, QgsRasterLayer, QgsTask
    from la.gui.lascenariocontroller import LaScenarioController
    from la.lib.lacatchment import DistanceMethod, LaCatchmentInputs, SearchStatus
    from la.lib.lautils import LaUtils

    myDemPath = str(tmp_path / "dem.tif")
    mySuitPath = str(tmp_path / "suit.tif")
    _windowDem(shunaDemPath, myDemPath)
    _writeSuitability(myDemPath, mySuitPath)

    myProject = QgsProject.instance()
    myProject.clear()
    myDem = QgsRasterLayer(myDemPath, "Shuna DEM")
    try:
        _runScenario(myProject, myDem, mySuitPath, monkeypatch)
    finally:
        myProject.clear()


def _runScenario(myProject, myDem, mySuitPath, monkeypatch):
    from qgis.PyQt.QtTest import QTest
    from la.gui.lascenariocontroller import LaScenarioController
    from la.lib.lacatchment import DistanceMethod, LaCatchmentInputs, SearchStatus
    from la.lib.lautils import LaUtils

    assert myDem.isValid()
    myProject.addMapLayer(myDem)

    monkeypatch.setattr(LaUtils, "getCrop", staticmethod(lambda g: _StubCrop("WheatTest")))
    monkeypatch.setattr(LaUtils, "getCropParameter", staticmethod(lambda g: _StubParameter(mySuitPath)))

    myController = LaScenarioController()
    myController.mModel = _StubModel()
    myController.setGisInputs(LaCatchmentInputs(myDem.id(), None, None, DistanceMethod.WalkingTime))
    myFinished = []
    myController.catchmentFinished.connect(lambda ok, text: myFinished.append((ok, text)))
    assert myController.launchCatchment()

    for _ in range(600):           # up to 60 s
        QTest.qWait(100)
        if myFinished:
            break
    assert myFinished, "catchment task did not finish"
    myOk, myText = myFinished[0]
    assert myOk, myText

    myResults = myController.mLastCatchmentResults
    assert myResults is not None and len(myResults.items) == 1
    myItem = myResults.items[0]
    assert myItem.status is SearchStatus.Converged
    assert myItem.achievedHa == pytest.approx(49.14, abs=0.05)
    assert myItem.threshold == pytest.approx(1328.125, abs=0.01)
    assert os.path.exists(myItem.outputPath)

    myRoot = myProject.layerTreeRoot()
    myGroup = myRoot.findGroup("Catchment Analysis")
    assert myGroup is not None
    myRunGroups = [c for c in myGroup.children() if c.nodeType() == c.NodeGroup]
    assert len(myRunGroups) == 1
    myRun = myRunGroups[0]
    myNames = [c.name() for c in myRun.children()]
    assert myNames[0] == "Settlement"
    assert "Crops" in myNames
    assert myNames[-1].startswith("Cost surface")
    assert "Animals" not in myNames            # empty sub-groups are removed
    myCrops = myRun.findGroup("Crops")
    assert len(myCrops.children()) == 1
    assert myCrops.children()[0].name().startswith("WheatTest (49.1 Ha")
    myCostLayer = myRun.children()[-1].layer()
    assert myCostLayer.renderer().type() == "singlebandpseudocolor"
    assert myCostLayer.opacity() == pytest.approx(0.45)
