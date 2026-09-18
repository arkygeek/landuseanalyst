"""
Golden-number regression tests for the diet/herd engine.

The expected values come from two independent sources:

* Jorgenson thesis, Shuna Chalcolithic scenarios (min population 100),
  as reproduced by the web port's ``tests/test_thesis_golden_numbers.py``.
* The 2026-06-06 parity session, which established the S05
  Animals-First-Include-Dairy animal area targets after the 1000× kcal→MCal
  bug was fixed (Sheep 0.2162 Ha, Cow 2.8794 Ha).

Any change to these numbers is an engine regression unless the thesis
appendices say otherwise.
"""

import pytest

from la.lib.lautils import LaUtils


def _buildModel(thePopulation: int, theMeatPercent: int, theDairyUtilisation: int):
    """Build an ``LaModel`` with the thesis validation inputs and all catalogue items selected."""
    from la.lib.lamodel import LaModel

    myModel = LaModel()
    myModel.mPopulation = thePopulation
    myModel.mDietPercent = theMeatPercent                # "ALL meat %" (animal share)
    myModel.mMeatPercent = 99                            # domestic animal contribution
    myModel.mPercentOfDietThatIsFromCrops = 90           # domestic crop contribution
    myModel.mCaloriesPerPersonDaily = 2500
    myModel.mDairyUtilisation = theDairyUtilisation
    myModel.mIncludeDairy = True
    myModel.mLimitDairy = False
    myModel.mLimitDairyPercentage = 0
    myModel.mBaseOnPlants = False

    myAnimalParameters = LaUtils.getAvailableAnimalParameters()
    myCropParameters = LaUtils.getAvailableCropParameters()
    myModel.mAnimalsMap = {p.animalGuid: g for g, p in myAnimalParameters.items()}
    myModel.mCropsMap = {p.cropGuid: g for g, p in myCropParameters.items()}
    assert len(myModel.mAnimalsMap) == 4
    assert len(myModel.mCropsMap) == 8
    return myModel


def _byName(theModel, theTargets, theGetter):
    return {theGetter(g).name: v for g, v in theTargets.items()}


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_s01_animals_first_dairy_separate_matches_thesis():
    """Chalcolithic S01: pop 100, meat 10 %, dairy 0 %, with 90-day feed."""
    myModel = _buildModel(100, 10, 0)
    myLabels = myModel.doCalcsAnimalsFirstDairySeparate()

    assert myLabels.megaCaloriesSettlementAnnual == pytest.approx(91250.0, abs=0.1)
    assert myLabels.cropMCalories == pytest.approx(73912.5, abs=0.1)
    assert myLabels.animalMCalories == pytest.approx(9033.75, abs=0.1)
    assert myLabels.wildAnimalMCalories == pytest.approx(91.25, abs=0.1)
    assert myLabels.dairyMCalories == pytest.approx(0.0, abs=0.1)
    assert myLabels.wildPlantsMCalories == pytest.approx(8212.5, abs=0.1)

    myCropLandHa = sum(myModel.mAreaTargetsCropsMap.values())
    myGrazingLandHa = sum(myModel.mAreaTargetsAnimalsMap.values())
    assert myCropLandHa == pytest.approx(191.91, abs=0.1)
    assert myGrazingLandHa == pytest.approx(82.36, abs=0.1)

    myCrops = _byName(myModel, myModel.mAreaTargetsCropsMap, LaUtils.getCrop)
    assert myCrops["Emmer"] == pytest.approx(77.64, abs=0.05)
    assert myCrops["Barley"] == pytest.approx(82.31, abs=0.05)


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_s05_animals_first_include_dairy_animal_targets():
    """
    Chalcolithic S05: pop 100, meat 10 %, dairy 100 %, Include-Dairy mode.

    Guards the kcal→MCal constant (1e-3): with the old 1e-6 every target
    here was 1000× smaller than a single 10 m pixel.
    """
    myModel = _buildModel(100, 10, 100)
    myLabels = myModel.doCalcsAnimalsFirstIncludeDairy()

    myAnimals = _byName(myModel, myModel.mAreaTargetsAnimalsMap, LaUtils.getAnimal)
    assert myAnimals["Sheep"] == pytest.approx(0.2162, abs=0.0005)
    assert myAnimals["Cow"] == pytest.approx(2.8794, abs=0.0005)
    assert myAnimals["Goat"] == pytest.approx(0.7197, abs=0.0005)
    assert myAnimals["Pig"] == pytest.approx(2.2072, abs=0.0005)

    # MCal labels must be in true MCal (settlement total = 91,250 MCal/yr).
    assert myLabels.megaCaloriesSettlementAnnual == pytest.approx(91250.0, abs=0.1)
    assert myLabels.cropMCalories == pytest.approx(73912.5, abs=0.1)
    assert myLabels.dairyMCalories == pytest.approx(3670.39, abs=0.01)
    assert myLabels.animalMCalories == pytest.approx(5363.36, abs=0.01)
    assert sum(myModel.mAreaTargetsCropsMap.values()) == pytest.approx(79.37, abs=0.01)
