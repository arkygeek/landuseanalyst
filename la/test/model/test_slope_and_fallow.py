"""Per-item slope limits on parameter profiles and the fallow-allocation toggle."""

import pytest


@pytest.mark.usefixtures("qtApp")
def test_crop_parameter_slope_defaults_and_round_trip():
    from la.lib.lacropparameter import LaCropParameter

    myParameter = LaCropParameter()
    assert myParameter.applySlopeLimit is True
    assert myParameter.slopeMinDegrees == 0.0
    assert myParameter.slopeMaxDegrees == 9.0

    myParameter.mName = "Olives params"
    myParameter.slopeMaxDegrees = 20.0
    myParameter.slopeMinDegrees = 2.0
    myXml = myParameter.toXml()
    assert "<preferredSlopeMax>20.0</preferredSlopeMax>" in myXml

    myCopy = LaCropParameter()
    myCopy.fromXml(myXml)
    assert myCopy.slopeMaxDegrees == 20.0 and myCopy.slopeMinDegrees == 2.0 and myCopy.applySlopeLimit
    myClone = LaCropParameter(myCopy)
    assert myClone.slopeMaxDegrees == 20.0


@pytest.mark.usefixtures("qtApp")
def test_legacy_profiles_without_slope_tags_get_thesis_defaults(sampleProfilesDir):
    from la.lib.lautils import LaUtils

    myCropParameters = LaUtils.getAvailableCropParameters()
    myAnimalParameters = LaUtils.getAvailableAnimalParameters()
    assert myCropParameters and myAnimalParameters
    assert all(p.slopeMaxDegrees == 9.0 and p.applySlopeLimit for p in myCropParameters.values())
    assert all(p.slopeMaxDegrees == 15.0 and p.applySlopeLimit for p in myAnimalParameters.values())


@pytest.mark.usefixtures("qtApp")
def test_animal_parameter_slope_round_trip():
    from la.lib.laanimalparameter import LaAnimalParameter

    myParameter = LaAnimalParameter()
    assert myParameter.slopeMaxDegrees == 15.0
    myParameter.mName = "Goat params"
    myParameter.applySlopeLimit = False
    myParameter.slopeMaxDegrees = 35.0
    myCopy = LaAnimalParameter()
    myCopy.fromXml(myParameter.toXml())
    assert myCopy.applySlopeLimit is False and myCopy.slopeMaxDegrees == 35.0


@pytest.fixture
def s01Controller(qtApp, sampleProfilesDir):
    from la.gui.lascenariocontroller import LaScenarioController

    myController = LaScenarioController()
    myController.setLivePreview(False)
    myController.selectAll()
    return myController


def test_fallow_ledger_is_populated(s01Controller):
    myModel = s01Controller.mModel
    s01Controller.runDietCalc()
    assert set(myModel.mAreaTargetsCropsSownMap) == set(myModel.mAreaTargetsCropsMap)
    for myGuid, myTotal in myModel.mAreaTargetsCropsMap.items():
        mySown = myModel.mAreaTargetsCropsSownMap[myGuid]
        myFallow = myModel.mAreaTargetsCropsFallowMap[myGuid]
        assert mySown + myFallow == pytest.approx(myTotal, rel=1e-9)
    assert myModel.mFallowMCalPool > 0
    assert 0 <= myModel.mFallowMCalAllocated <= myModel.mFallowMCalPool
    assert myModel.mFallowMCalAllocated + myModel.mFallowMCalResidual == pytest.approx(myModel.mFallowMCalPool)


def test_fallow_allocation_ignores_the_group_count(s01Controller, monkeypatch):
    """
    lamodel.cpp passed the HIGH group's count to the MEDIUM/LOW allocations.
    doTheFallowAllocation never reads that argument, so the 'bug' is inert;
    this pins that so nobody adds a toggle for it again.
    """
    from la.lib import lacalculations

    myModel = s01Controller.mModel
    s01Controller.runDietCalc()
    myBaseline = dict(myModel.mAreaTargetsAnimalsMap)
    assert sum(myBaseline.values()) == pytest.approx(82.36, abs=0.1)

    myOriginal = lacalculations.doTheFallowAllocation

    def _withBogusCount(theModel, thePriority, theAvailable, theNeeded, theCount):
        return myOriginal(theModel, thePriority, theAvailable, theNeeded, theCount * 1000 + 7)

    monkeypatch.setattr(lacalculations, "doTheFallowAllocation", _withBogusCount)
    s01Controller.runDietCalc()
    assert dict(myModel.mAreaTargetsAnimalsMap) == pytest.approx(myBaseline)
