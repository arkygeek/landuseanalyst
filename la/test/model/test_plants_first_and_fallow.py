# coding=utf-8
"""
Unit tests for Plants-First calculation modes, fodderUse gating, and multi-tier
fallow grazing priority cascading.
"""

import pytest

from la.lib.la import Priority, Status
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacalculations import (
    allocateFallowGrazingLand,
    doCalcsAnimalsFirstDairySeparate,
    doCalcsPlantsFirstDairySeparate,
    doCalcsPlantsFirstIncludeDairy,
    doTheFallowAllocation,
)
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils


def _buildThesisModel(
    thePopulation: int = 100,
    theMeatPercent: int = 10,
    theDairyUtilisation: int = 50,
    theBaseOnPlants: bool = False,
    theIncludeDairy: bool = False,
) -> LaModel:
    """Build an LaModel with the thesis validation inputs and all catalogue items selected."""
    myModel = LaModel()
    myModel.mPopulation = thePopulation
    myModel.mDietPercent = theMeatPercent
    myModel.mMeatPercent = 99
    myModel.mPercentOfDietThatIsFromCrops = 90
    myModel.mCaloriesPerPersonDaily = 2500
    myModel.mDairyUtilisation = theDairyUtilisation
    myModel.mIncludeDairy = theIncludeDairy
    myModel.mLimitDairy = False
    myModel.mLimitDairyPercentage = 0
    myModel.mBaseOnPlants = theBaseOnPlants

    myAnimalParameters = LaUtils.getAvailableAnimalParameters()
    myCropParameters = LaUtils.getAvailableCropParameters()
    myModel.mAnimalsMap = {p.animalGuid: g for g, p in myAnimalParameters.items()}
    myModel.mCropsMap = {p.cropGuid: g for g, p in myCropParameters.items()}
    return myModel


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_plants_first_include_dairy_anchors_plants_with_and_without_dairy_limit():
    """PlantsFirstIncludeDairy keeps Plants at (100% - mDietPercent) even under limitDairy."""
    myModel = _buildThesisModel(100, 10, 100, theBaseOnPlants=True, theIncludeDairy=True)
    myLabels = doCalcsPlantsFirstIncludeDairy(myModel)

    assert myLabels.plantsPortionPct == pytest.approx(90.0, abs=1e-4)
    assert myLabels.cropsPortionPct == pytest.approx(81.0, abs=1e-4)
    assert myLabels.wildPlantsPortionPct == pytest.approx(9.0, abs=1e-4)
    assert (
        myLabels.tameMeatPortionPct
        + myLabels.dairyPortionPct
        + myLabels.wildAnimalPortionPct
    ) == pytest.approx(10.0, abs=1e-4)
    assert len(myModel.mAnimalHerdMap) == 4
    assert myModel.mFallowMCalPool > 0.0

    # Impose a 2% dairy limit (below unconstrained dairy share)
    myModel.mLimitDairy = True
    myModel.mLimitDairyPercentage = 2
    myLimited = doCalcsPlantsFirstIncludeDairy(myModel)

    assert myLimited.plantsPortionPct == pytest.approx(90.0, abs=1e-4)
    assert myLimited.cropsPortionPct == pytest.approx(81.0, abs=1e-4)
    assert myLimited.dairyPortionPct == pytest.approx(2.0, abs=1e-4)
    assert myLimited.tameMeatPortionPct == pytest.approx(7.9, abs=1e-4)
    assert myLimited.dairySurplusMCalories > 0.0


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_plants_first_dairy_separate_anchors_plants_and_displaces_tame_meat():
    """PlantsFirstDairySeparate keeps Plants at (100% - mDietPercent) and displaces tame meat."""
    myModel = _buildThesisModel(100, 10, 50, theBaseOnPlants=True, theIncludeDairy=False)
    myLabels = doCalcsPlantsFirstDairySeparate(myModel)

    assert myLabels.plantsPortionPct == pytest.approx(90.0, abs=1e-4)
    assert myLabels.cropsPortionPct == pytest.approx(81.0, abs=1e-4)
    assert myLabels.wildPlantsPortionPct == pytest.approx(9.0, abs=1e-4)
    assert (
        myLabels.wildAnimalPortionPct
        + myLabels.tameMeatPortionPct
        + myLabels.dairyPortionPct
    ) == pytest.approx(10.0, abs=1e-4)
    assert len(myModel.mAnimalHerdMap) == 4

    # With limitDairy=True at 2%, Dairy is capped at 2%, Tame Meat is 7.9%, Plants stay 90%
    myModel.mLimitDairy = True
    myModel.mLimitDairyPercentage = 2
    myLimited = doCalcsPlantsFirstDairySeparate(myModel)
    assert myLimited.plantsPortionPct == pytest.approx(90.0, abs=1e-4)
    assert myLimited.dairyPortionPct == pytest.approx(2.0, abs=1e-4)
    assert myLimited.tameMeatPortionPct == pytest.approx(7.9, abs=1e-4)
    assert myLimited.dairySurplusMCalories > 0.0


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_fodder_use_false_disables_barley_feed_in_memory():
    """Toggling fodderUse=False in memory disables Barley grain/straw fodder even if mFoodSourceMap is non-empty."""
    myModel = _buildThesisModel(100, 10, 50, theBaseOnPlants=False, theIncludeDairy=False)
    for myParamGuid in myModel.mAnimalsMap.values():
        myParam = LaUtils.getAnimalParameter(myParamGuid)
        myParam.fodderUse = False
        LaUtils.registerAnimalParameter(myParam)

    myLabels = doCalcsAnimalsFirstDairySeparate(myModel)
    myCropAreaByName = {
        LaUtils.getCrop(myGuid).name: myArea
        for myGuid, myArea in myModel.mAreaTargetsCropsMap.items()
    }
    assert myCropAreaByName["Barley"] == pytest.approx(45.9674, abs=0.01)
    assert sum(myModel.mAreaTargetsAnimalsMap.values()) == pytest.approx(107.9063, abs=0.01)
    assert myLabels.totalLandNeeded == pytest.approx(257.6831, abs=0.01)
    LaUtils.clearRegistries()


@pytest.mark.usefixtures("qtApp")
def test_allocate_fallow_grazing_land_priority_cascading():
    """Verify High -> Medium -> Low -> Nope priority cascading and mFallowStatus updates."""
    LaUtils.clearRegistries()
    myModel = LaModel()
    myPriorities = {
        "animal-high": ("param-high", Priority.High),
        "animal-med": ("param-med", Priority.Medium),
        "animal-low": ("param-low", Priority.Low),
        "animal-none": ("param-none", Priority.Nope),
    }
    myModel.mAnimalsMap = {}
    for myAnimalGuid, (myParamGuid, myPriority) in myPriorities.items():
        myParam = LaAnimalParameter()
        myParam.setGuid(myParamGuid)
        myParam.animalGuid = myAnimalGuid
        myParam.fallowUsage = myPriority
        LaUtils.registerAnimalParameter(myParam)
        myModel.mAnimalsMap[myAnimalGuid] = myParamGuid

    myInitialReqs = {
        "animal-high": 1000.0,
        "animal-med": 800.0,
        "animal-low": 500.0,
        "animal-none": 400.0,
    }
    myModel.mValueMap = dict(myInitialReqs)
    myResidual = allocateFallowGrazingLand(myModel, 1500.0, dict(myInitialReqs))
    assert myResidual == pytest.approx(0.0)
    assert myModel.mValueMap["animal-high"] == pytest.approx(0.0)
    assert myModel.mValueMap["animal-med"] == pytest.approx(300.0)
    assert myModel.mValueMap["animal-low"] == pytest.approx(500.0)
    assert myModel.mValueMap["animal-none"] == pytest.approx(400.0)
    assert myModel.mFallowStatus == Status.NotEnoughToCompletelySatisfy

    myModel.mValueMap = dict(myInitialReqs)
    myResidualSurplus = allocateFallowGrazingLand(myModel, 3000.0, dict(myInitialReqs))
    assert myResidualSurplus == pytest.approx(700.0)
    assert myModel.mValueMap["animal-high"] == pytest.approx(0.0)
    assert myModel.mValueMap["animal-med"] == pytest.approx(0.0)
    assert myModel.mValueMap["animal-low"] == pytest.approx(0.0)
    assert myModel.mValueMap["animal-none"] == pytest.approx(400.0)
    assert myModel.mFallowStatus == Status.MoreThanEnoughToCompletelySatisfy

    myLeftover = doTheFallowAllocation(myModel, Priority.High, 400.0, 0.0, 1.0)
    assert myLeftover == pytest.approx(400.0)
    LaUtils.clearRegistries()
