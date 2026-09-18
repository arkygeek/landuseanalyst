"""The parameter editors open offscreen and expose the per-item slope band."""

import pytest


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_crop_parameter_manager_has_preferred_land_group():
    from la.gui.lacropparametermanager import LaCropParameterManager

    myDialog = LaCropParameterManager(None)
    try:
        myGroup = myDialog.findChild(object, "grpPreferredLand")
        assert myGroup is not None
        assert myDialog.mCropParameter is not None
        myDialog.showCropParameter()
        assert myGroup.sbSlopeMaxDegrees.value() == pytest.approx(9.0)
        myGroup.sbSlopeMaxDegrees.setValue(20.0)
        myGroup.applyTo(myDialog.mCropParameter)
        assert myDialog.mCropParameter.slopeMaxDegrees == 20.0
    finally:
        myDialog.close()


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_animal_parameter_manager_has_preferred_land_group():
    from la.gui.laanimalparametermanager import LaAnimalParameterManager

    myDialog = LaAnimalParameterManager()
    try:
        myGroup = myDialog.findChild(object, "grpPreferredLand")
        assert myGroup is not None
        if myDialog.mAnimalParameter is not None:
            myDialog.showAnimalParameter()
            assert myGroup.sbSlopeMaxDegrees.value() == pytest.approx(15.0)
    finally:
        myDialog.close()


@pytest.mark.usefixtures("qtApp")
def test_preferred_land_widget_round_trip_swaps_inverted_band():
    from la.gui.widgets.lapreferredlandwidget import LaPreferredLandWidget
    from la.lib.lacropparameter import LaCropParameter

    myWidget = LaPreferredLandWidget()
    myParameter = LaCropParameter()
    myWidget.loadFrom(myParameter)
    myWidget.sbSlopeMinDegrees.setValue(12.0)
    myWidget.sbSlopeMaxDegrees.setValue(4.0)
    myWidget.applyTo(myParameter)
    assert (myParameter.slopeMinDegrees, myParameter.slopeMaxDegrees) == (4.0, 12.0)
    myWidget.cbApplySlopeLimit.setChecked(False)
    assert not myWidget.sbSlopeMaxDegrees.isEnabled()
