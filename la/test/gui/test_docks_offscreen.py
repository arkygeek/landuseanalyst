"""Construct the dock workspace offscreen and drive it end to end (no catchment)."""

import pytest


@pytest.fixture
def workspace(qtApp, sampleProfilesDir):
    from la.gui.lascenariocontroller import LaScenarioController
    from la.gui.lasettingsdock import LaSettingsDock
    from la.gui.laresultsdock import LaResultsDock

    from qgis.core import QgsProject

    QgsProject.instance().clear()
    myController = LaScenarioController()
    mySettings = LaSettingsDock(myController, None)
    myResults = LaResultsDock(myController)
    yield myController, mySettings, myResults
    mySettings.close()
    myResults.close()


def test_settings_dock_widgets_have_manual_object_names(workspace):
    _, mySettings, _ = workspace
    for myName in ("grpScenario", "grpPopulationDiet", "grpAgriculture", "grpCatchment", "grpAdvanced",
                   "sbPopulation", "sbDailyCalories", "sliderAnimalShare", "pbnCalculate", "pbnPickSeed",
                   "cboDem", "donutDiet"):
        assert mySettings.findChild(object, myName) is not None, myName


def test_calculate_disabled_until_ready_then_runs(workspace):
    from qgis.PyQt.QtTest import QTest

    myController, mySettings, myResults = workspace
    assert not mySettings.footer.pbnCalculate.isEnabled()
    mySettings.agriculturePanel.pbnSelectAll.click()
    QTest.qWait(300)   # live preview debounce
    assert mySettings.footer.pbnCalculate.isEnabled()
    assert mySettings.dietPanel.donut.plantsPercent() > 80

    mySettings.footer.pbnCalculate.click()
    assert myController.hasResults()
    assert "Emmer" in myResults.tablesView.toPlainText() or "Emmer" in myResults.tablesView.toHtml()
    assert myResults.tilesLayout.count() >= 8
    assert myResults.pbnCopyJson.isEnabled()


def test_sliders_drive_the_model(workspace):
    myController, mySettings, _ = workspace
    mySettings.dietPanel.sliderAnimalShare.setValue(30)
    mySettings.dietPanel.sbPopulation.setValue(600)
    assert myController.mModel.mDietPercent == 30
    assert myController.mModel.mPopulation == 600
    assert "600 people" in mySettings.footer.lblSummary.text()


def test_catchment_section_off_means_no_gis_inputs(workspace):
    _, mySettings, _ = workspace
    assert not mySettings.catchmentPanel.isChecked()
    assert mySettings.catchmentPanel.gisInputs() is None
    mySettings.catchmentPanel.setChecked(True)
    assert mySettings.catchmentPanel.gisInputs() is None          # no DEM in the project
    assert mySettings.catchmentPanel.validate() is not None       # and the panel says so


def test_help_tab_lists_embedded_topics(workspace):
    _, _, myResults = workspace
    assert myResults.treeHelp.topLevelItemCount() > 0
    myFirstGroup = myResults.treeHelp.topLevelItem(0)
    assert myFirstGroup.childCount() > 0
    myResults.treeHelp.setCurrentItem(myFirstGroup.child(0))
    assert len(myResults.textHelp.toPlainText()) > 20


def test_barrier_layer_can_be_created_and_exported(workspace, tmp_path, monkeypatch):
    import os
    from qgis.core import QgsProject

    _, mySettings, _ = workspace
    monkeypatch.setattr(os.path, "expanduser", lambda p: str(tmp_path) if p == "~" else p)
    myPanel = mySettings.catchmentPanel
    myLayer = myPanel.createBarrierLayer()
    assert myLayer.isValid() and myLayer.isEditable()
    assert {f.name() for f in myLayer.fields()} >= {"name", "barrier_type", "crossing_penalty"}
    assert myPanel.barrierLayer() is myLayer
    myLayer.commitChanges()
    myPath = myPanel.exportBarriers()
    assert myPath and myPath.endswith(".gpkg") and os.path.exists(myPath)
    assert "barriersSource" in mySettings.pluginBlock()
    QgsProject.instance().removeMapLayer(myLayer.id())
