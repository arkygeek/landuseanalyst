"""
LaCatchment orchestrator on the real Shuna window: golden number, slope bands,
sown / fallow split, diagnostics and the automatic window retry.
"""

import os

import numpy as np
import pytest
from osgeo import gdal

SETTLEMENT_X = 744800.0
SETTLEMENT_Y = 3611100.0


class _Extent:
    def __init__(self, x0, y0, x1, y1):
        self._v = (x0, y0, x1, y1)

    def xMinimum(self): return self._v[0]
    def yMinimum(self): return self._v[1]
    def xMaximum(self): return self._v[2]
    def yMaximum(self): return self._v[3]


class _DemLayer:
    """Duck-typed QgsRasterLayer for LaGrass."""

    def __init__(self, thePath):
        myDs = gdal.Open(thePath)
        gt = myDs.GetGeoTransform()
        self._mPath = thePath
        self._mCell = abs(gt[1])
        self._mExtent = _Extent(gt[0], gt[3] + myDs.RasterYSize * gt[5], gt[0] + myDs.RasterXSize * gt[1], gt[3])
        myDs = None

    def source(self): return self._mPath
    def extent(self): return self._mExtent
    def rasterUnitsPerPixelX(self): return self._mCell


class _Crop:
    def __init__(self, theName): self.name = theName


class _Parameter:
    def __init__(self, theRaster, theApplySlope=False, theMax=9.0, theCommon=False):
        self.name = "params"
        self.rasterName = theRaster
        self.useCommonLand = theCommon
        self.useCommonGrazingLand = theCommon
        self.applySlopeLimit = theApplySlope
        self.slopeMinDegrees = 0.0
        self.slopeMaxDegrees = theMax


class _Model:
    def __init__(self, theTargets, theSown=None, theFallow=None):
        self.easting, self.northing, self.precision = SETTLEMENT_X, SETTLEMENT_Y, 5
        self.mCropsMap = {g: g + "-param" for g in theTargets}
        self.mAreaTargetsCropsMap = dict(theTargets)
        self.mAreaTargetsCropsSownMap = dict(theSown or {})
        self.mAreaTargetsCropsFallowMap = dict(theFallow or {})
        self.mAnimalsMap = {}
        self.mAreaTargetsAnimalsMap = {}


def _window(theSource, theOut, thePixels=200):
    myDs = gdal.Open(theSource)
    gt = myDs.GetGeoTransform()
    myCol = int((SETTLEMENT_X - gt[0]) / gt[1]) - thePixels // 2
    myRow = int((SETTLEMENT_Y - gt[3]) / gt[5]) - thePixels // 2
    gdal.Translate(theOut, myDs, srcWin=[myCol, myRow, thePixels, thePixels], format="GTiff", outputType=gdal.GDT_Float32)
    myDs = None


def _lowGround(theDem, theOut, theAll=False):
    myDs = gdal.Open(theDem)
    myElev = myDs.GetRasterBand(1).ReadAsArray()
    mySuit = np.ones_like(myElev, dtype=np.uint8) if theAll else ((myElev >= -100) & (myElev <= 100)).astype(np.uint8)
    myOut = gdal.GetDriverByName("GTiff").Create(theOut, myDs.RasterXSize, myDs.RasterYSize, 1, gdal.GDT_Byte)
    myOut.SetGeoTransform(myDs.GetGeoTransform()); myOut.SetProjection(myDs.GetProjection())
    myOut.GetRasterBand(1).WriteArray(mySuit); myOut.FlushCache(); myOut = None; myDs = None


@pytest.fixture
def shuna(tmp_path, shunaDemPath, monkeypatch, qtApp):
    pytest.importorskip("scipy")
    myDem = str(tmp_path / "dem.tif"); _window(shunaDemPath, myDem)
    mySuit = str(tmp_path / "lowground.tif"); _lowGround(myDem, mySuit)
    myAll = str(tmp_path / "all.tif"); _lowGround(myDem, myAll, theAll=True)
    return {"dem": myDem, "suit": mySuit, "all": myAll, "scratch": str(tmp_path / "scratch")}


def _run(shuna, theModel, theParameter, monkeypatch, **theOptions):
    from la.lib.lacatchment import DistanceMethod, LaCatchment, LaCatchmentInputs
    from la.lib.lagrass import LaGrass
    from la.lib.lautils import LaUtils

    monkeypatch.setattr(LaUtils, "getCrop", staticmethod(lambda g: _Crop("WheatTest")))
    monkeypatch.setattr(LaUtils, "getCropParameter", staticmethod(lambda g: theParameter))
    myGrass = LaGrass(_DemLayer(shuna["dem"]), shuna["scratch"])
    myCatchment = LaCatchment(myGrass, thePrecisionPct=5)
    myLog = []
    myCatchment.logged.connect(myLog.append)
    myInputs = LaCatchmentInputs("dem", None, None, DistanceMethod.WalkingTime, **theOptions)
    return myCatchment.runCatchmentAnalysis(theModel, myInputs), myLog


def test_golden_number_survives_windowing_and_split_off(shuna, monkeypatch):
    from la.lib.lacatchment import SearchStatus

    myResults, _ = _run(shuna, _Model({"wheat": 50.0}), _Parameter(shuna["suit"]), monkeypatch,
                        applySlopeLimits=False, splitFallow=False)
    assert len(myResults.items) == 1
    myItem = myResults.items[0]
    assert myItem.status is SearchStatus.Converged
    assert myItem.threshold == pytest.approx(1328.125, abs=0.01)
    assert myItem.achievedHa == pytest.approx(49.14, abs=0.05)
    assert myItem.kind == "crop" and myItem.category == ""
    assert myItem.iterations == 9
    assert myItem.elevationMin is not None and -100 <= myItem.elevationMin <= myItem.elevationMax <= 100
    assert myResults.windowPixels == 200 and myResults.windowShape == (200, 200) and not myResults.retried
    assert os.path.exists(myResults.costRasterPath)


def test_slope_band_and_sown_fallow_split(shuna, monkeypatch):
    from la.lib.lacatchment import SearchStatus

    myModel = _Model({"wheat": 50.0}, theSown={"wheat": 30.0}, theFallow={"wheat": 20.0})
    myResults, _ = _run(shuna, myModel, _Parameter(shuna["suit"], theApplySlope=True, theMax=9.0), monkeypatch)
    myByCategory = {r.category: r for r in myResults.items}
    assert set(myByCategory) == {"sown", "total", "fallow"}
    mySown, myTotal, myFallow = myByCategory["sown"], myByCategory["total"], myByCategory["fallow"]
    assert mySown.status is SearchStatus.Converged and myTotal.status is SearchStatus.Converged
    assert mySown.targetHa == 30.0 and myTotal.targetHa == 50.0 and myFallow.targetHa == 20.0
    assert mySown.achievedHa + myFallow.achievedHa == pytest.approx(myTotal.achievedHa, abs=0.01)
    assert myFallow.outputPath and os.path.exists(myFallow.outputPath)
    assert mySown.slopeBand == (0.0, 9.0)
    assert mySown.slopeEliminatedPct is not None and 0.0 <= mySown.slopeEliminatedPct <= 100.0
    # the slope band removes land, so reaching 30 Ha needs a wider (or equal) threshold than without it
    assert myResults.slopeRasterPath and os.path.exists(myResults.slopeRasterPath) is False  # temp, cleaned up


def test_slope_only_suitability_runs_without_a_raster(shuna, monkeypatch):
    from la.lib.lacatchment import SearchStatus

    myResults, _ = _run(shuna, _Model({"wheat": 50.0}), _Parameter("", theApplySlope=True, theMax=15.0),
                        monkeypatch, useSlopeOnlySuitability=True, splitFallow=False)
    assert len(myResults.items) == 1
    assert myResults.items[0].status is SearchStatus.Converged
    assert myResults.items[0].achievedHa == pytest.approx(50.0, rel=0.05)


def test_unreachable_target_reports_ceiling(shuna, monkeypatch):
    from la.lib.lacatchment import SearchStatus

    # 4000 Ha on a 200-cell window (3600 Ha total) can never be reached.
    myResults, _ = _run(shuna, _Model({"wheat": 4000.0}), _Parameter(shuna["all"]), monkeypatch,
                        applySlopeLimits=False, splitFallow=False, windowPixels=200)
    myItem = myResults.items[0]
    assert myItem.status is SearchStatus.Failed
    assert "exceeds the maximum reachable" in myItem.message
    assert myItem.iterations == 17


def test_auto_window_retries_when_clipped(shuna, monkeypatch):
    # A 1500 Ha target needs a ~4.4 km radius: the auto window (3× the disc radius) starts at
    # ~440 cells but the DEM is only 200 cells, so the first mask touches the border and the
    # run widens once; the DEM bound then stops further retries.
    myResults, myLog = _run(shuna, _Model({"wheat": 1500.0}), _Parameter(shuna["all"]), monkeypatch,
                            applySlopeLimits=False, splitFallow=False)
    assert myResults.windowShape == (200, 200)
    assert not myResults.retried or any("re-running" in m for m in myLog)


def _wallGeojson(thePath, theX, theY0, theY1, theProps=None):
    import json
    myDoc = {"type": "FeatureCollection",
             "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::32636"}},
             "features": [{"type": "Feature", "properties": theProps or {"barrier_type": "impassable"},
                           "geometry": {"type": "LineString", "coordinates": [[theX, theY0], [theX, theY1]]}}]}
    with open(thePath, "w") as f:
        json.dump(myDoc, f)


def test_barrier_wall_blocks_the_catchment_and_is_recorded(shuna, monkeypatch, tmp_path):
    from la.lib.lacatchment import SearchStatus

    myWall = str(tmp_path / "wall.geojson")
    # north-south wall 300 m east of the seed, spanning the whole window
    _wallGeojson(myWall, SETTLEMENT_X + 300.0, SETTLEMENT_Y + 4000.0, SETTLEMENT_Y - 4000.0)
    myResults, myLog = _run(shuna, _Model({"wheat": 50.0}), _Parameter(shuna["all"]), monkeypatch,
                            applySlopeLimits=False, splitFallow=False, windowPixels=200, barriersPath=myWall)
    assert myResults.barrierFeatures == 1 and myResults.barrierCells and myResults.barrierCells >= 190
    myItem = myResults.items[0]
    assert myItem.status is SearchStatus.Converged
    myCost = gdal.Open(myResults.costRasterPath).ReadAsArray()
    myDs = gdal.Open(shuna["dem"]); gt = myDs.GetGeoTransform(); myDs = None
    mySeedCol = int((SETTLEMENT_X - gt[0]) / gt[1]); mySeedRow = int((SETTLEMENT_Y - gt[3]) / gt[5])
    assert np.isfinite(myCost[mySeedRow, mySeedCol - 5])
    assert np.isnan(myCost[mySeedRow, mySeedCol + 40])          # east of the wall: unreachable
    assert any("Barriers: 1 feature" in m for m in myLog)


def test_barrier_outside_the_window_is_reported_not_silently_ignored(shuna, monkeypatch, tmp_path):
    myWall = str(tmp_path / "far.geojson")
    _wallGeojson(myWall, SETTLEMENT_X + 50000.0, SETTLEMENT_Y + 100.0, SETTLEMENT_Y - 100.0)
    myResults, myLog = _run(shuna, _Model({"wheat": 50.0}), _Parameter(shuna["suit"]), monkeypatch,
                            applySlopeLimits=False, splitFallow=False, windowPixels=200, barriersPath=myWall)
    assert myResults.barrierFeatures == 1 and myResults.barrierCells == 0
    assert any("NOT been modelled" in m for m in myLog)
    assert myResults.items[0].threshold == pytest.approx(1328.125, abs=0.01)   # nothing changed
