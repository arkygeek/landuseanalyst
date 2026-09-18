"""Scenario JSON interchange: round trip through the controller and web-payload shape."""

import json

import pytest


@pytest.fixture
def controller(qtApp, sampleProfilesDir, monkeypatch, tmp_path):
    from qgis.core import QgsSettings
    from la.gui.lascenariocontroller import LaScenarioController

    # Keep the recent-files list out of the user's real QgsSettings.
    myStore = {}
    monkeypatch.setattr(QgsSettings, "value", lambda self, key, default=None, **kw: myStore.get(key, default))
    monkeypatch.setattr(QgsSettings, "setValue", lambda self, key, value: myStore.__setitem__(key, value))
    myController = LaScenarioController()
    myController.setLivePreview(False)
    return myController


def test_round_trip_preserves_inputs_selections_and_results(controller, tmp_path):
    controller.selectAll()
    controller.setScenarioName("Shuna S05")
    controller.setPeriod("Chalcolithic")
    controller.setPopulation(100)
    controller.setAnimalShareOfDiet(10)
    controller.setIncludeDairy(True)
    controller.setDairyUtilisation(100)
    controller.setSettlement(744800, 3611100, 32636)
    controller.runDietCalc()
    controller.mPluginBlockProvider = lambda: {"catchmentEnabled": True, "demSource": "/tmp/dem.tif",
                                               "commonCropSource": "", "commonGrazingSource": "",
                                               "distanceMethod": "WalkingTime"}

    myPath = controller.saveScenario(str(tmp_path / "s05"))
    assert myPath.endswith(".lascenario.json")
    myDocument = json.load(open(myPath, encoding="utf-8"))
    assert myDocument["schemaVersion"] == 1
    myScenario = myDocument["scenario"]
    assert myScenario["name"] == "Shuna S05"
    assert myScenario["dietPercentFromPlants"] == 10.0        # web's misnamed animal share, copied verbatim
    assert myScenario["calculationType"] == "animals_first_include_dairy"
    assert myScenario["crsEpsg"] == 32636 and myScenario["settlementX"] == 744800.0
    assert myScenario["cropSlopeMaxDegrees"] == 9.0 and myScenario["grazingSlopeMaxDegrees"] == 15.0
    assert len(myDocument["crops"]) == 8 and len(myDocument["animals"]) == 4
    assert sum(c["percent"] for c in myDocument["crops"]) == pytest.approx(100.0, abs=0.1)
    assert myDocument["plugin"]["demSource"] == "/tmp/dem.tif"
    assert myDocument["results"]["mcalSettlementAnnual"] == pytest.approx(91250.0, abs=0.1)
    assert any(i["itemType"] == "animal" and i["name"] == "Sheep" for i in myDocument["results"]["items"])
    assert controller.recentScenarios() == [myPath]

    controller.resetToDefaults()
    assert not controller.mSelectedCrops
    controller.loadScenario(myPath)
    assert controller.mModel.mName == "Shuna S05"
    assert controller.mModel.mDietPercent == 10 and controller.mModel.mIncludeDairy
    assert controller.mModel.mDairyUtilisation == 100 and controller.mModel.mProjection == 32636
    assert len(controller.mSelectedCrops) == 8 and len(controller.mSelectedAnimals) == 4
    assert controller.mPendingPluginBlock["catchmentEnabled"] is True
    myLabels = controller.runDietCalc()
    from la.lib.lautils import LaUtils
    myByName = {LaUtils.getAnimal(g).name: v for g, v in controller.mModel.mAreaTargetsAnimalsMap.items()}
    assert myByName["Sheep"] == pytest.approx(0.2162, abs=0.0005)
    assert myLabels is not None


def test_web_style_document_resolves_items_by_name(controller):
    from la.lib import lascenarioio

    myDocument = {
        "schemaVersion": 1,
        "scenario": {"name": "from web", "population": 600, "caloriesPerPersonDaily": 2500,
                     "dietPercentFromPlants": 20, "meatPercentTame": 99, "cropPercentTame": 90,
                     "dairyUtilisation": 50, "calculationType": "animals_first_dairy_separate",
                     "settlementX": 1.0, "settlementY": 2.0, "crsEpsg": 32636, "precisionPct": 5},
        "crops": [{"guid": "db-id-7", "name": "Emmer", "parameterName": "Emmer Params"}],
        "animals": [{"guid": "db-id-2", "name": "sheep"}],
    }
    controller.loadScenarioDocument(myDocument)
    assert controller.mModel.mPopulation == 600 and controller.mModel.mDietPercent == 20
    assert not controller.mModel.mIncludeDairy and not controller.mModel.mBaseOnPlants
    assert len(controller.mSelectedCrops) == 1 and len(controller.mSelectedAnimals) == 1
    myPayload = lascenarioio.toWebPayload(controller.scenarioDocument(theIncludeResults=False))
    assert set(myPayload) >= {"name", "population", "dietPercentFromPlants", "calculationType", "crsEpsg"}


def test_rejects_foreign_json(controller, tmp_path):
    myPath = tmp_path / "x.json"
    myPath.write_text('{"hello": 1}')
    with pytest.raises(ValueError):
        controller.loadScenario(str(myPath))
