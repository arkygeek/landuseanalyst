"""XML deserialisation must tolerate the legacy grazing-value tag names."""

import pytest


_ANIMAL_PARAMETER_LEGACY = """<?xml version='1.0' encoding='utf-8'?>
<animalParameter guid="11111111-2222-3333-4444-555555555555">
  <name>Legacy Sheep</name>
  <description>written by an older toXml</description>
  <animal>f1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6</animal>
  <percentTameMeat>3.59</percentTameMeat>
  <useCommonGrazingLand>0</useCommonGrazingLand>
  <useSpecificGrazingLand>1</useSpecificGrazingLand>
  <fodderUse>0</fodderUse>
  <fallowUsage>High</fallowUsage>
  <areaUnits>Dunum</areaUnits>
  <energyType>KCalories</energyType>
  <specificLandEnergyType>KCalories</specificLandEnergyType>
  <valueCommonGrazingLand>1500</valueCommonGrazingLand>
  <valueSpecificGrazingLand>10</valueSpecificGrazingLand>
</animalParameter>"""


@pytest.mark.usefixtures("qtApp")
def test_animal_parameter_reads_legacy_grazing_tags():
    from la.lib.laanimalparameter import LaAnimalParameter

    myParameter = LaAnimalParameter()
    myParameter.fromXml(_ANIMAL_PARAMETER_LEGACY)
    assert myParameter.name == "Legacy Sheep"
    assert myParameter.valueCommonGrazingLand == 1500
    assert myParameter.valueSpecificGrazingLand == 10


@pytest.mark.usefixtures("qtApp")
def test_animal_parameter_round_trips_grazing_values():
    """toXml must write the tag names fromXml reads (this was the 108-scenario zeroing bug)."""
    from la.lib.laanimalparameter import LaAnimalParameter

    mySource = LaAnimalParameter()
    mySource.fromXml(_ANIMAL_PARAMETER_LEGACY)
    myXml = mySource.toXml()
    assert "<foodValueCommonGrazingLand>1500</foodValueCommonGrazingLand>" in myXml

    myCopy = LaAnimalParameter()
    myCopy.fromXml(myXml)
    assert myCopy.valueCommonGrazingLand == 1500
    assert myCopy.valueSpecificGrazingLand == 10


@pytest.mark.usefixtures("qtApp")
def test_model_xml_round_trip_writes_real_newlines_and_land_fields():
    from la.lib.la import AreaUnits
    from la.lib.lamodel import LaModel

    myModel = LaModel()
    myModel.mName = "Round trip"
    myModel.mPopulation = 250
    myModel.mDietPercent = 20
    myModel.setCommonLandValue(3000, AreaUnits.Dunum)
    myModel.mHerdSize = 7
    myModel.mWalkingTime = True
    myModel.mIncludeDairy = True
    myModel.mLimitDairy = False
    myXml = myModel.toXml()
    assert "\\n" not in myXml           # no literal backslash-n
    assert myXml.count("<dairyUtilisation>") == 1

    myCopy = LaModel()
    assert myCopy.fromXml(myXml)
    assert myCopy.mName == "Round trip"
    assert myCopy.mPopulation == 250
    assert myCopy.mDietPercent == 20
    assert myCopy.mHerdSize == 7
    assert myCopy.mWalkingTime is True and myCopy.mEuclideanDistance is False
    assert myCopy.mIncludeDairy and not myCopy.mLimitDairy
    assert myCopy.mCommonLandAreaUnits == AreaUnits.Dunum
    assert myCopy.mCommonGrazingValue == pytest.approx(myModel.mCommonGrazingValue)
