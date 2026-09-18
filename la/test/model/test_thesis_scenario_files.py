"""The bundled thesis scenario files load through the controller and reproduce the golden numbers."""

import glob
import os
import shutil

import pytest


def _thesisDir(repoRoot):
    return os.path.join(repoRoot, "la", "scenarios", "thesis")


def test_all_108_files_are_present_and_well_formed(repoRoot):
    import json

    myFiles = sorted(glob.glob(os.path.join(_thesisDir(repoRoot), "*.lascenario.json")))
    assert len(myFiles) == 108
    for myPath in myFiles:
        myDocument = json.load(open(myPath, encoding="utf-8"))
        assert myDocument["schemaVersion"] == 1
        assert len(myDocument["crops"]) == 8 and len(myDocument["animals"]) == 4
        assert sum(c["percent"] for c in myDocument["crops"]) == pytest.approx(100.0, abs=0.2)
        assert sum(a["percent"] for a in myDocument["animals"]) == pytest.approx(100.0, abs=0.2)


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_chalcolithic_s01_file_reproduces_thesis_numbers(repoRoot):
    from la.gui.lascenariocontroller import LaScenarioController

    myController = LaScenarioController()
    myController.setLivePreview(False)
    myController.loadScenario(os.path.join(_thesisDir(repoRoot), "shuna_chalcolithic_s01.lascenario.json"))
    assert myController.mModel.mPopulation == 100 and myController.mModel.mDietPercent == 10
    assert len(myController.mSelectedCrops) == 8 and len(myController.mSelectedAnimals) == 4
    myLabels = myController.runDietCalc()
    assert myLabels.megaCaloriesSettlementAnnual == pytest.approx(91250.0, abs=0.1)
    assert sum(myController.mModel.mAreaTargetsCropsMap.values()) == pytest.approx(191.91, abs=0.1)
    assert sum(myController.mModel.mAreaTargetsAnimalsMap.values()) == pytest.approx(82.36, abs=0.1)


@pytest.fixture
def installedProfilesDir(repoRoot, tmp_path, monkeypatch):
    """testData + the derived thesis profiles, as install_sample_data.sh would lay them out."""
    from la.lib.lautils import LaUtils

    myRoot = tmp_path / "landuseAnalyst"
    shutil.copytree(os.path.join(repoRoot, "testData"), myRoot)
    for mySub in ("cropParameterProfiles", "animalParameterProfiles"):
        mySource = os.path.join(_thesisDir(repoRoot), "profiles", mySub)
        for myName in os.listdir(mySource):
            shutil.copy(os.path.join(mySource, myName), myRoot / mySub / myName)
    monkeypatch.setattr(LaUtils, "userDataPath", staticmethod(lambda: str(myRoot)))
    monkeypatch.setattr(LaUtils, "userSettingsDirPath", staticmethod(lambda: str(myRoot)))
    LaUtils.invalidateProfileCache()
    return str(myRoot)


@pytest.mark.usefixtures("qtApp", "installedProfilesDir")
def test_eeb1_file_resolves_derived_profiles_and_runs(repoRoot):
    from la.gui.lascenariocontroller import LaScenarioController
    from la.lib.lautils import LaUtils

    myController = LaScenarioController()
    myController.setLivePreview(False)
    myController.loadScenario(os.path.join(_thesisDir(repoRoot), "shuna_eeb1_s02.lascenario.json"))
    assert myController.mModel.mPopulation == 1000
    myCropTotal, myAnimalTotal = myController.percentTotals()
    assert myCropTotal == pytest.approx(100.0, abs=0.2) and myAnimalTotal == pytest.approx(100.0, abs=0.2)
    mySheepParameter = LaUtils.getAnimalParameter(
        myController.mSelectedAnimals[next(g for g in myController.mSelectedAnimals
                                           if LaUtils.getAnimal(g).name == "Sheep")])
    assert mySheepParameter.name == "Sheep · Early EB I · no feed"
    assert mySheepParameter.percentTameMeat == pytest.approx(12.26)
    assert mySheepParameter.fodderUse is False
    assert myController.readiness() == (True, "")
    myLabels = myController.runDietCalc()
    assert myLabels is not None
    assert myLabels.megaCaloriesSettlementAnnual == pytest.approx(912500.0, abs=0.1)   # 1000 people


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_june_xml_scenario_opens_and_matches_s05(repoRoot):
    """The June 2026 <landuseAnalystScenario> files (la/thesis_scenarios/) open through the same controller."""
    from la.gui.lascenariocontroller import LaScenarioController
    from la.lib.lautils import LaUtils

    myPath = os.path.join(repoRoot, "la", "thesis_scenarios", "shuna_chalcolithic_s05.xml")
    myController = LaScenarioController()
    myController.setLivePreview(False)
    myController.loadScenario(myPath)
    myModel = myController.mModel
    assert myModel.mPopulation == 100 and myModel.mDietPercent == 10 and myModel.mDairyUtilisation == 100
    assert myModel.mIncludeDairy is True and myModel.mWalkingTime is True and myModel.mEuclideanDistance is False
    assert myModel.mEasting == 744800 and myModel.mProjection == 32636
    assert len(myController.mSelectedCrops) == 8 and len(myController.mSelectedAnimals) == 4
    assert myController.readiness() == (True, "")
    myController.runDietCalc()
    myByName = {LaUtils.getAnimal(g).name: v for g, v in myModel.mAreaTargetsAnimalsMap.items()}
    assert myByName["Sheep"] == pytest.approx(0.2162, abs=0.0005)
    LaUtils.clearRegistries()
