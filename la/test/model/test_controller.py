"""LaScenarioController: readiness rules, live recalculation and golden numbers."""

import pytest


@pytest.fixture
def controller(qtApp, sampleProfilesDir):
    from la.gui.lascenariocontroller import LaScenarioController

    myController = LaScenarioController()
    myController.setLivePreview(False)   # tests call runDietCalc explicitly
    return myController


def test_not_ready_without_selection(controller):
    myReady, myReason = controller.readiness()
    assert not myReady
    assert "at least one" in myReason


def test_select_all_reaches_100_percent_and_runs_s01(controller):
    controller.selectAll()
    assert len(controller.mSelectedCrops) == 8
    assert len(controller.mSelectedAnimals) == 4
    myCropTotal, myAnimalTotal = controller.percentTotals()
    assert myCropTotal == pytest.approx(100.0, abs=0.1)
    assert myAnimalTotal == pytest.approx(100.0, abs=0.1)
    assert controller.readiness() == (True, "")

    myLabels = controller.runDietCalc()
    assert myLabels is not None
    assert myLabels.megaCaloriesSettlementAnnual == pytest.approx(91250.0, abs=0.1)
    assert sum(controller.mModel.mAreaTargetsCropsMap.values()) == pytest.approx(191.91, abs=0.1)
    assert sum(controller.mModel.mAreaTargetsAnimalsMap.values()) == pytest.approx(82.36, abs=0.1)
    assert controller.calculationTypeLabel() == "Animals First (Dairy Separate)"
    assert controller.hasResults()
    assert "Emmer" in controller.tablesHtml()
    assert '"totalLandHa"' in controller.reportJson()


def test_deselecting_breaks_the_percent_rule(controller):
    controller.selectAll()
    myGuid = next(iter(controller.mSelectedCrops))
    controller.setCropSelected(myGuid, False)
    myReady, myReason = controller.readiness()
    assert not myReady
    assert "Crop shares sum" in myReason
    assert controller.runDietCalc() is None


def test_include_dairy_switches_method_and_matches_s05(controller):
    controller.selectAll()
    controller.setIncludeDairy(True)
    controller.setDairyUtilisation(100)
    assert controller.calculationTypeLabel() == "Animals First (Include Dairy)"
    controller.runDietCalc()
    from la.lib.lautils import LaUtils
    myByName = {LaUtils.getAnimal(g).name: v for g, v in controller.mModel.mAreaTargetsAnimalsMap.items()}
    assert myByName["Sheep"] == pytest.approx(0.2162, abs=0.0005)


def test_diet_changed_signal_fires_with_live_preview(controller, qtApp):
    from qgis.PyQt.QtTest import QTest

    myReceived = []
    controller.dietChanged.connect(myReceived.append)
    controller.setLivePreview(True)
    controller.selectAll()
    QTest.qWait(400)
    assert myReceived and myReceived[-1] is not None


def test_reset_clears_everything(controller):
    controller.selectAll()
    controller.runDietCalc()
    controller.resetToDefaults()
    assert not controller.mSelectedCrops and not controller.mSelectedAnimals
    assert not controller.hasResults()
    assert controller.mModel.mPopulation == 100
