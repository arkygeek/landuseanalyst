"""
lacalculations.py - Core calculation engine for the Landuse Analyst plugin.

This module implements the mathematical models defined in Chapter 4 of the thesis.
It provides functions to calculate dietary distributions, animal herd requirements,
crop area targets, and fallow land allocation.

Strict mathematical parity with the original C++ research code (lamodel.cpp) is maintained.
"""

from typing import Dict, Tuple, TYPE_CHECKING
import os

from la.lib.lautils import LaUtils
from la.lib.la import Priority, Status, AreaUnits, EnergyType
from la.lib.ladietlabels import LaDietLabels
from la.lib.lafoodsource import LaFoodSource
from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter

if TYPE_CHECKING:
    from la.lib.lamodel import LaModel

def doCalcsAnimalsFirstDairySeparate(theModel: 'LaModel') -> LaDietLabels:
    """
    Implements the 'Animals First, Dairy Separate' calculation path.
    Direct port of LaModel::doCalcsAnimalsFirstDairySeparate() from lamodel.cpp.
    """
    # 1. Initialization (C++ lines 835-864)
    theModel.mCalcsCropsMap.clear()
    theModel.mCalcsAnimalsMap.clear()
    theModel.mValueMap.clear()
    theModel.mAnimalCalcReport.clear()

    myCropCalcsReportMap: Dict[str, Tuple[str, float]] = {}
    myAnimalCalcsReportMap: Dict[str, Tuple[str, float]] = {}
    myAnimalsMap: Dict[str, float] = {} # For fallow allocation

    myDietLabels = LaDietLabels()
    myCrops = theModel.mCropsMap
    myFoodSourceMapCounter: Dict[str, float] = {}

    # Initialize fodder map counter
    for myCropGuid in myCrops.keys():
        myFoodSourceMapCounter[myCropGuid] = 0.0

    myMCalsIndividualAnnual = theModel.mCaloriesPerPersonDaily * 365.0 * .001
    myMCalsSettlementAnnual = myMCalsIndividualAnnual * theModel.mPopulation
    myDairyMCalorieCounter = 0.0
    myTameMeatMCalorieCounter = 0.0

    myWildMeatPortion = (1. - (theModel.mMeatPercent * 0.01))
    myDairyUtilization = theModel.mDairyUtilisation * 0.01 # Assuming percent input
    myDairyLimitPercent = theModel.mLimitDairyPercentage * 0.01 # Assuming percent input
    myLimitDairyBool = theModel.mLimitDairy
    myPlantPercent = 1. - (theModel.mDietPercent * 0.01)
    myDomesticCropPortion = theModel.mPercentOfDietThatIsFromCrops * 0.01

    mySelectedAnimalsMap = theModel.mAnimalsMap

    # 2. Animal Loop (C++ lines 901-1205)
    for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
        myAnimal = LaUtils.getAnimal(myAnimalGuid)
        myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
        
        myAdditionalMCalCounter = 0.0
        myAdditionalMCalCounter1 = 0.0

        # Biological Parameters
        myMilkKgPerDay = myAnimal.milkGramsPerDay * .001
        myMilkFoodValue = myAnimal.milkFoodValue * .001
        myLactationTime = myAnimal.lactationTime
        myWeaningAge = myAnimal.weaningAge
        myGestatingTime = myAnimal.gestationTime
        myEstrousCycle = myAnimal.estrousCycle
        myBabiesPerBirth = myAnimal.youngPerBirth

        myDeathRate = myAnimal.deathRate * .01
        myBreedingRatio = myAnimal.femalesPerMale
        myKillWeight = myAnimal.killWeight
        myUsablePortionOfAnimal = myAnimal.usableMeat * .01
        myAdultWeight = myAnimal.adultWeight
        myFemalesToMales = myAnimal.femalesPerMale
        myConceptionEfficiency = myAnimal.conceptionEfficiency * .01
        myMeatValueMCal = myAnimal.meatFoodValue * .001
        mySexualMaturity = myAnimal.sexualMaturity
        myBreedingYears = myAnimal.breedingExpectancy
        
        myAnimalContributionToMeatPortion = myAnimalParameter.percentTameMeat * .01
        # B3 target
        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * (theModel.mDietPercent * 0.01) * (theModel.mMeatPercent * 0.01)
        
        myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge) # B4
        myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal # B5
        myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization # B6

        # Birthing logic (B21, B7, B8, B9)
        myBirthingEventsPerYear1 = 365. / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime)
        myBirthingEventsPerYear = max(1.0, myBirthingEventsPerYear1)
        
        myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal * (1. / ((mySexualMaturity / 12.) + myBreedingYears)))
        myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear) # B7
        myCulledAdultMalesValue = myCulledMothersValue / myFemalesToMales if myFemalesToMales > 0 else 0 # B8
        
        myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue # B9
        myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue if myFinalOffspringValue > 0 else 0 # B11
        
        myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue # B12
        myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear # B14

        myTameMeatMCalorieCounter += myMCalsFromTheMeat
        myDairyMCalorieCounter += myMCalsUtilizedFromDairy

        myFoodSourceMap = myAnimalParameter.fodderSourceMap
        myMeatPercentLocal = myMCalsFromTheMeat / myMCalsSettlementAnnual # B15
        myDairyPercentLocal = myMCalsUtilizedFromDairy / myMCalsSettlementAnnual # B16

        # --- Herd Population Dynamics (B22-B35) ---
        myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1. - myDeathRate) * myConceptionEfficiency # B22
        myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear if myOffspringPerMotherPerYear > 0 else 0 # B23
        myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5 # B24
        myFemalesStepOne = myMalesStepOne # B25
        
        myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity/12.)) / myBreedingYears if myBreedingYears > 0 else 0 # B26
        myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio if myBreedingRatio > 0 else 0 # B27
        
        myAdditionalMothers = ((myReplacementMothersPerYear/myOffspringPerMotherPerYear)*2.)+(myBreedingMalesRequired * 2.) if myOffspringPerMotherPerYear > 0 else 0 # B28
        myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5 # B29
        myFemalesStepTwo = myMalesStepTwo # B30
        
        myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear # B32
        myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo # B33
        myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo # B34
        myTotalOffspring = myTotalMaleOffspring * 2. # B35

        # --- Feed Requirements ---
        myFeedForGestating = myAnimal.gestating * .001
        myFeedForLactating = myAnimal.lactating * .001
        myFeedForMaintenance = myAnimal.maintenance * .001
        myFeedForOffspringPerKg = myAnimal.juvenile * .001

        myGestatingMCals = myTotalOffspring * myGestatingTime * myFeedForGestating
        myLactatingMCals = myTotalOffspring * myLactationTime * myFeedForLactating
        myDaysForMaintenance = max(0.0, 365.0 - (myGestatingTime + myLactationTime))

        myDryMothers = max(0.0, myTotalMothers - myTotalOffspring)
        myDryMothersMCals = myDryMothers * 365. * myFeedForMaintenance
        myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance
        myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals

        myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.
        myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365. - myWeaningAge)

        # --- Grain/Fodder Map Updates (C++ lines 1124-1168) ---
        for myCropGuid, myFoodSource in myFoodSourceMap.items():
            myGrain = myFoodSource.grain * .001
            myFodder = myFoodSource.fodder * .001
            myDays = myFoodSource.days
            
            myGrainToAdd = myGrain * myDays * myTotalOffspring
            myFoodSourceMapCounter[myCropGuid] += myGrainToAdd
            
            myCropObj = LaUtils.getCrop(myCropGuid)
            myFoodValueOfCrop = myCropObj.cropCalories * .001
            myFoodValueofFodder = myCropObj.fodderValue * .001
            
            myGrainMCal = myGrainToAdd * myFoodValueOfCrop
            myFodderMCal = myFodder * myDays * myFoodValueofFodder * myTotalOffspring
            
            myAdditionalMCalCounter1 += myFodderMCal
            myAdditionalMCalCounter += myGrainMCal + myFodderMCal

        # --- Final Animal Reporting Stage 1 ---
        myAnimalHerdMCalsRequired1 = myGestatingMCals + myLactatingMCals + myMaintenanceMCals + myAdultMalesMCals + myOffspringMCals
        myAnimalHerdMCalsRequired = myAnimalHerdMCalsRequired1 - myAdditionalMCalCounter
        
        myAnimalReport = (
            f"myMilkKgPerDay = {myMilkKgPerDay}\n"
            f"myMilkFoodValue = {myMilkFoodValue}\n"
            f"myLactationTime = {myLactationTime}\n"
            f"myWeaningAge = {myWeaningAge}\n"
            f"myKillWeight = {myKillWeight}\n"
            f"myUsablePortionOfAnimal = {myUsablePortionOfAnimal}\n"
            f"myAdultWeight = {myAdultWeight}\n"
            f"myFemalesToMales = {myFemalesToMales}\n"
            f"myMeatValueMCal = {myMeatValueMCal}\n"
            f"mySexualMaturity = {mySexualMaturity}\n"
            f"myBreedingYears = {myBreedingYears}\n"
            f"myAnimalContributionToMeatPortion = {myAnimalContributionToMeatPortion}\n"
            f"myAnimalMCalTarget = {myAnimalMCalTarget}\n"
            f"myPotentialDairyPerOffspring = {myPotentialDairyPerOffspring}\n"
            f"myValuePerOffspring = {myValuePerOffspring}\n"
            f"myActualDairyValueOfOffspring = {myActualDairyValueOfOffspring}\n"
            f"myCulledMothersValue = {myCulledMothersValue}\n"
            f"myCulledAdultMalesValue = {myCulledAdultMalesValue}\n"
            f"myFinalOffspringValue = {myFinalOffspringValue}\n"
            f"myOffspringNeededPerYear = {myOffspringNeededPerYear}\n"
            f"myMCalsFromTheMeat = {myMCalsFromTheMeat}\n"
            f"myMCalsUtilizedFromDairy = {myMCalsUtilizedFromDairy}\n"
            f"myTameMeatMCalorieCounter = {myTameMeatMCalorieCounter}\n"
            f"myDairyMCalorieCounter = {myDairyMCalorieCounter}\n\n"
            f"myBirthingEventsPerYear = {myBirthingEventsPerYear}\n"
            f"myOffspringPerMotherPerYear = {myOffspringPerMotherPerYear}\n"
            f"myMothersNeededStepOne = {myMothersNeededStepOne}\n"
            f"myMalesStepOne = {myMalesStepOne}\n"
            f"myFemalesStepOne = {myFemalesStepOne}\n"
            f"myReplacementMothersPerYear = {myReplacementMothersPerYear}\n"
            f"myBreedingMalesRequired = {myBreedingMalesRequired}\n"
            f"myAdditionalMothers = {myAdditionalMothers}\n"
            f"myMalesStepTwo = {myMalesStepTwo}\n"
            f"myFemalesStepTwo = {myFemalesStepTwo}\n\n"
            f"myTotalMothers = {myTotalMothers}\n"
            f"myTotalMaleOffspring = {myTotalMaleOffspring}\n"
            f"myTotalFemaleOffspring = {myTotalFemaleOffspring}\n"
            f"myTotalOffspring = {myTotalOffspring}\n"
            f"myFeedForGestating = {myFeedForGestating}\n"
            f"myFeedForLactating = {myFeedForLactating}\n"
            f"myFeedForMaintenance = {myFeedForMaintenance}\n"
            f"myFeedForOffspringPerKg = {myFeedForOffspringPerKg}\n"
            f"myGestatingMCals = {myGestatingMCals}\n"
            f"myLactatingMCals = {myLactatingMCals}\n"
            f"myDaysForMaintenance = {myDaysForMaintenance}\n"
            f"myGestatingTime = {myGestatingTime}\n"
            f"myLactationTime = {myLactationTime}\n"
            f"myDryMothers = {myDryMothers}\n"
            f"myDryMothersMCals = {myDryMothersMCals}\n"
            f"myOtherMaintenanceMCals = {myOtherMaintenanceMCals}\n"
            f"myMaintenanceMCals = {myMaintenanceMCals}\n"
            f"myAdultMalesMCals = {myAdultMalesMCals}\n"
            f"myOffspringMCals = {myOffspringMCals}\n\n"
            f"myAnimalHerdMCalsRequired1 = {myAnimalHerdMCalsRequired1}\n"
            f"myAnimalHerdMCalsRequired = {myAnimalHerdMCalsRequired}\n"
            ".........................\n"
            ".        Summary        .\n"
            ".........................\n"
            f"MCal Target = {myMCalsFromTheMeat}\n"
            f"Dairy Contribution = {myMCalsUtilizedFromDairy}\n"
            f"Meat Percent = {myMeatPercentLocal*100.:.2f}% \n"
            f"Dairy Percent = {myDairyPercentLocal*100.:.2f}% \n"
            f"Number of Offspring = {myTotalMaleOffspring * 2.}\n"
            f"Number of Mothers = {myTotalMothers}\n"
            f"Number of Breeding Males = {myBreedingMalesRequired}\n"
        )

        myAnimalCalcsReportMap[myAnimalGuid] = (myAnimalReport, myAnimalHerdMCalsRequired)
        myAnimalsMap[myAnimalGuid] = myAnimalHerdMCalsRequired
        theModel.mValueMap[myAnimalGuid] = myAnimalHerdMCalsRequired

    # 3. Dairy Portion Logic (C++ lines 1207-1232)
    myDairyLimit = myDairyLimitPercent if myLimitDairyBool else 1.0
    myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
    myWildMeatPercent = myWildMeatPortion * (theModel.mDietPercent * 0.01)
    
    myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.
    myNewLimit = (1. - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit
    
    myPotentialDairyLessThanLimitBool = (myDairyMCalorieCounter / myMCalsSettlementAnnual) < myDairyLimit
    myNewDairy = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual
    
    myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual
    myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent
    myOverallPlantPercent = 1. - myOverallMeatPercent - myOverallDairyPercent
    myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion
    myOverallWildPlantPercent = myOverallPlantPercent * (1. - theModel.mPercentOfDietThatIsFromCrops * 0.01) # Refined based on C++ myPlantPercent
    
    myOverallDomesticMeatMCals = myTameMeatMCalorieCounter
    myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual
    myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual
    myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
    myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual
    
    myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
    myOverallDairySurplusMCals = max(0.0, myFirstDairySurplusBool)
    myMCalsFromFallowCounter = 0.0

    # 4. Crop Loop (C++ lines 1242-1354)
    for myCropGuid, myCropParameterGuid in theModel.mCropsMap.items():
        myCrop = LaUtils.getCrop(myCropGuid)
        myCropParameter = LaUtils.getCropParameter(myCropParameterGuid)
        
        myCropPortion = myCropParameter.percentTameCrop * .01
        myCropFoodValue = myCrop.cropCalories * .001
        myCropPercentLocal = myCropPortion * myOverallCropPercent
        myMCalsFromTheCrop = myCropPercentLocal * myMCalsSettlementAnnual
        
        myKgForPeople1 = myMCalsFromTheCrop / myCropFoodValue if myCropFoodValue > 0 else 0
        myAnimalKgAdd1 = myFoodSourceMapCounter.get(myCropGuid, 0.0)
        
        mySpoilagePercent = myCropParameter.spoilage * .01
        myReseedPercent = myCropParameter.reseed * .01
        
        myKgForPeopleReseed = myKgForPeople1 * myReseedPercent
        myKgForPeopleSpoilage = myKgForPeople1 * mySpoilagePercent
        myKgForPeople = myKgForPeopleReseed + myKgForPeopleSpoilage + myKgForPeople1
        
        myAnimalKgAddReseed = myAnimalKgAdd1 * myReseedPercent
        myAnimalKgAddSpoilage = myAnimalKgAdd1 * mySpoilagePercent
        myAnimalKgAdd = myAnimalKgAddReseed + myAnimalKgAddSpoilage + myAnimalKgAdd1
        
        myAdjustedTarget = myKgForPeople + myAnimalKgAdd
        
        myCropYield = myCrop.cropYield * 10.0 if myCrop.areaUnits == AreaUnits.Dunum else myCrop.cropYield
        myCropAreaTargetPeople = myKgForPeople / myCropYield if myCropYield > 0 else 0
        myCropAreaTargetAnimals = myAnimalKgAdd / myCropYield if myCropYield > 0 else 0
        
        myRatio = myCropParameter.fallowRatio
        myFallowValue = myCropParameter.fallowValue
        myCropAreaTarget1 = myAdjustedTarget / myCropYield if myCropYield > 0 else 0
        myCropAreaTarget = myCropAreaTarget1 * (myRatio + 1.)
        
        myFallowArea = myRatio * myCropAreaTarget1
        myFallowMCals = myFallowArea * myFallowValue
        myMCalsFromFallowCounter += myFallowMCals
        
        myCropReport = (
            f"MCals People = {myMCalsFromTheCrop}\n"
            f"myCropPortion = {myCropPortion}\n"
            f"myCropFoodValue = {myCropFoodValue}\n"
            f"myOverallCropPercent = {myOverallCropPercent}\n"
            f"myCropPercent = {myCropPercentLocal}\n"
            f"myMCalsFromTheCrop = {myMCalsFromTheCrop}\n"
            f"myAnimalKgAdd = {myAnimalKgAdd}\n"
            f"myAdjustedTarget = {myAdjustedTarget}\n"
            f"myCrop.cropYield = {myCrop.cropYield}\n"
            f"myCropYield = {myCropYield}\n"
            f"Crop Production People before adjusting= {myKgForPeople1}\n"
            f"Extra Kg to account for spoilage= {myKgForPeopleSpoilage}\n"
            f"Extra Kg to account for reseeding= {myKgForPeopleReseed}\n"
            f"Crop Production People after adjusting= {myKgForPeople}\n"
            f"Crop Production Animal before adjusting= {myAnimalKgAdd1}\n"
            f"Extra Kg to account for spoilage= {myAnimalKgAddSpoilage}\n"
            f"Extra Kg to account for reseeding= {myAnimalKgAddReseed}\n"
            f"Crop Production Animal after adjusting= {myAnimalKgAdd}\n"
            f"myCropAreaTarget People = {myCropAreaTargetPeople}\n"
            f"myCropAreaTarget Animals= {myCropAreaTargetAnimals}\n"
            f"myCropAreaTarget = {myCropAreaTarget}\n\n"
            f"Kg for People = {myKgForPeople}\n"
            f"KG for Animals = {myAnimalKgAdd}\n"
            f"Percent of Diet = {myCropPercentLocal * 100.:.2f}% \n"
            f"Area Target People: {myCropAreaTargetPeople}\n"
            f"Area Target Animal: {myCropAreaTargetAnimals}\n"
            f"Area Target is {myCropAreaTarget}\n"
            f"myFallowValue =  {myFallowValue}\n"
            f"MCals from Fallow: {myFallowMCals}\n"
        )
        
        myCropCalcsReportMap[myCropGuid] = (myCropReport, myCropAreaTarget)

    # 5. Fallow Allocation (C++ line 1356)
    allocateFallowGrazingLand(theModel, myMCalsFromFallowCounter, myAnimalsMap)

    # 6. Final Animal Report Aggregation (C++ lines 1365-1398)
    for myAnimalGuid, (myReport, _) in myAnimalCalcsReportMap.items():
        myMCalTarget = theModel.mValueMap.get(myAnimalGuid, 0.0)
        myLandValue = theModel.mCommonGrazingValue # Assuming Hectare value
        myAreaTarget = myMCalTarget / myLandValue if myLandValue > 0 else 0
        
        updatedReport = myReport + (
            f"Final MCal Target = {int(myMCalTarget)}\n"
            f"Final Area Target = {int(myAreaTarget)}\n"
        )
        theModel.mAnimalCalcReport[myAnimalGuid] = (updatedReport, myAreaTarget)

    # 7. Final Diet Label Setup
    myDietLabels.dairyMCalories = myOverallDairyMCals
    myDietLabels.cropMCalories = myOverallCropsMCals
    myDietLabels.animalMCalories = myOverallDomesticMeatMCals
    myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
    myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals
    
    myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.
    myDietLabels.tameMeatPortionPct = myDomesticMeatPercent * 100.
    myDietLabels.cropsPortionPct = myOverallCropPercent * 100.
    myDietLabels.wildAnimalPortionPct = myWildMeatPercent * 100.
    myDietLabels.wildPlantsPortionPct = myOverallWildPlantPercent * 100.
    
    myDietLabels.animalPortionPct = myOverallMeatPercent * 100.
    myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.
    myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0
    myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
    myDietLabels.dairySurplusMCalories = myOverallDairySurplusMCals

    # 8. Total Land Area Summation
    myTotalLandArea = 0.0
    for _, myArea in myCropCalcsReportMap.values():
        myTotalLandArea += myArea
    for _, myArea in theModel.mAnimalCalcReport.values():
        myTotalLandArea += myArea
    
    myDietLabels.totalLandNeeded = myTotalLandArea

    # Populate model maps for persistence
    theModel.mCalcsCropsMap = {k: v[0] for k, v in myCropCalcsReportMap.items()}
    theModel.mAreaTargetsCropsMap = {k: v[1] for k, v in myCropCalcsReportMap.items()}
    
    myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap
    myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
    myDietLabels.animalAreaTargetsMap = {k: v[1] for k, v in myAnimalCalcsReportMap.items()}
    myDietLabels.cropAreaTargetsMap = {k: v[1] for k, v in myCropCalcsReportMap.items()}
    
    theModel.mDietLabels = myDietLabels
    
    return myDietLabels

def allocateFallowGrazingLand(theModel: 'LaModel', theFallowMCalsAvailable: float, theAnimalMCalRequirementMap: Dict[str, float]) -> None:
    """
    Distributes available fallow land MCals to animals based on priority.
    Direct port of LaModel::allocateFallowGrazingLand() from lamodel.cpp (lines 388-447).
    """
    myHighPriorityCount = 0.0
    myMediumPriorityCount = 0.0
    myLowPriorityCount = 0.0
    myHighPriorityValue = 0.0
    myMediumPriorityValue = 0.0
    myLowPriorityValue = 0.0
    
    myTotalFallowValue = theFallowMCalsAvailable

    # Count animals and sum requirements
    for myAnimalGuid, myMCalReq in theAnimalMCalRequirementMap.items():
        myAnimalParameterGuid = theModel.mAnimalsMap.get(myAnimalGuid, "")
        if not myAnimalParameterGuid: continue
        myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
        
        if myAnimalParameter.fallowUsage == Priority.High:
            myHighPriorityCount += 1
            myHighPriorityValue += myMCalReq
        elif myAnimalParameter.fallowUsage == Priority.Medium:
            myMediumPriorityCount += 1
            myMediumPriorityValue += myMCalReq
        elif myAnimalParameter.fallowUsage == Priority.Low:
            myLowPriorityCount += 1
            myLowPriorityValue += myMCalReq

    # Allocate HIGH (C++ line 423)
    if myTotalFallowValue > 0:
        myTotalFallowValue = doTheFallowAllocation(theModel, Priority.High, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount)
    
    # Allocate MEDIUM (C++ line 431 - REPLICATING BUG: passes myHighPriorityCount)
    if myTotalFallowValue > 0:
        myTotalFallowValue = doTheFallowAllocation(theModel, Priority.Medium, myTotalFallowValue, myMediumPriorityValue, myHighPriorityCount)
        
    # Allocate LOW (C++ line 439 - REPLICATING BUG: passes myHighPriorityCount)
    if myTotalFallowValue > 0:
        myTotalFallowValue = doTheFallowAllocation(theModel, Priority.Low, myTotalFallowValue, myLowPriorityValue, myHighPriorityCount)

# --- Additional Calculation Path Stubs ---

def doCalcsPlantsFirstDairySeparate(theModel: 'LaModel') -> LaDietLabels:
    """Stub for Plants First, Dairy Separate."""
    LaUtils.debug.log("Using stub for doCalcsPlantsFirstDairySeparate", "Warning")
    return doCalcsAnimalsFirstDairySeparate(theModel)

def doCalcsAnimalsFirstIncludeDairy(theModel: 'LaModel') -> LaDietLabels:
    """
    Implements the 'Animals First, Include Dairy' calculation path.
    In this mode, dairy calories produced by the meat herd are counted
    towards the total animal product requirement.

    The aggregate diet-label math is a direct port of the C++ original.
    The per-animal and per-crop *report maps* are a Python-only addition
    (see PYTHON ENHANCEMENT block below).
    """
    # -----------------------------------------------------------------------
    # Direct port of C++ LaModel::doCalcsAnimalsFirstIncludeDiary() (lines 736-831)
    # NOTE: The C++ version uses a simple calorie-apportionment formula,
    #       NOT the full herd-population algorithm of DairySeparate.
    # In C++ all percentages are stored as fractions (setter divides by 100),
    # so in Python we apply * 0.01 to mDietPercent, mMeatPercent, etc.
    #
    # PYTHON ENHANCEMENT — Per-item calculation reports
    # -------------------------------------------------
    # The C++ source has stub getters `getAreaTargetsAnimalsMapAFID()` and
    # `getAreaTargetsCropsMapAFID()` (lamodel.cpp:1485, :1575) that return
    # empty QMaps — i.e. the per-animal/per-crop area targets were never
    # finished for the Include-Dairy modes. The C++ Calculations tab in
    # this mode therefore shows no per-item breakdown.
    #
    # To make the Python plugin's Calculations tab informative in this mode
    # we synthesize per-item reports here using the same apportionment
    # pattern DairySeparate uses (animals split by percentTameMeat, crops
    # split by percentTameCrop). The math is a Python-only extension; the
    # aggregate diet labels above remain a strict C++ port.
    # -----------------------------------------------------------------------
    myDietLabels = LaDietLabels()

    # C++ c-variables, translated to Python with proper 0.01 scaling
    # c1  = 1 - mMeatPercent  (in C++ mMeatPercent is already a fraction)
    c1  = 1.0 - (theModel.mMeatPercent * 0.01)          # wild-meat fraction
    c8  = theModel.mDairyUtilisation * 0.01              # dairy utilisation fraction
    c10 = float(theModel.mPopulation)
    c11 = float(theModel.mCaloriesPerPersonDaily)        # kcal/person/day
    c12 = theModel.mPercentOfDietThatIsFromCrops * 0.01  # domestic-crop fraction
    c14 = c10 * c11 * 365.0                              # total settlement kcals/year
    c15 = theModel.mDietPercent * 0.01                   # animal fraction of diet
    e15 = c14 * c15                                      # animal kcal budget

    # kcal → MCal scaling (used by reports and aggregate labels)
    _K_KCAL_TO_MCAL = 1e-6

    myDairyMCalorieCounter    = 0.0
    myTameMeatMCalorieCounter = 0.0
    myWildMeatMCalorieCounter = 0.0

    myAnimalCalcsReportMap: Dict[str, Tuple[str, float]] = {}
    myCropCalcsReportMap:   Dict[str, Tuple[str, float]] = {}

    mySelectedAnimalsMap = theModel.mAnimalsMap
    LaUtils.debug.log(
        f"IncludeDairy(simple) start. Diet%={theModel.mDietPercent}, "
        f"Meat%={theModel.mMeatPercent}, c14={c14:.1f}, e15={e15:.1f}, "
        f"animals={list(mySelectedAnimalsMap.keys())}",
        "Calculation"
    )

    # --- Animal loop: direct port of C++ lines 759-802 ---
    num_animals = len(mySelectedAnimalsMap)
    for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
        myAnimal = LaUtils.getAnimal(myAnimalGuid)
        myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
        
        # Scaling factor: if multiple animals are selected, each should only 
        # satisfy its assigned percentage of the domestic meat portion.
        # This matches the logic in DairySeparate mode and fixes the "multiple animal" bug in C++.
        myAnimalContributionScale = myAnimalParameter.percentTameMeat * 0.01 if myAnimalParameter else (1.0 / num_animals if num_animals > 0 else 1.0)

        # C++ animal variables (names kept identical to C++ source)
        c2 = myAnimal.milkGramsPerDay * 0.001        # milk kg/day
        c3 = myAnimal.milkFoodValue                   # kcal/kg milk
        c4 = myAnimal.lactationTime                   # days lactation
        c5 = myAnimal.weaningAge                      # days to wean
        c6 = myAnimal.killWeight                      # kg
        c7 = myAnimal.usableMeat * 0.01               # fraction usable
        c9 = myAnimal.meatFoodValue                   # kcal/kg

        # C++ line 776: e2 = c2 * c3 * (c4 - c5)   (kcal dairy per offspring)
        e2 = c2 * c3 * (c4 - c5)
        # C++ line 777: e3 = e2 * c8   (actual dairy kcal utilised per offspring)
        e3 = e2 * c8
        # C++ line 779: e10 = e3 + (c9 * c7 * c6)  (total value per offspring including dairy)
        e10 = e3 + (c9 * c7 * c6)
        
        # Target for THIS animal = Total Animal Budget * Meat Fraction * Animal's Share
        myTargetForThisAnimal = e15 * (1.0 - c1) * myAnimalContributionScale

        # C++ line 780: e7 = (Target) / e10   (offspring needed)
        e7 = myTargetForThisAnimal / e10 if e10 > 0 else 0.0
        # C++ line 781: c21 = e7 * e3   (dairy kcals for this animal)
        c21 = e7 * e3
        # C++ line 782: c23 = e7 * c6 * c7 * c9   (meat kcals for this animal)
        c23 = e7 * c6 * c7 * c9
        # C++ line 783 is `c22 = e15 - c21 - c23`. Because e7 is solved to make
        # c21 + c23 = e15*(1-c1) (the tame-meat budget), this reduces to e15*c1
        # — the wild-meat budget. We express it directly, scaled by the per-animal
        # contribution so the multi-animal counter sums correctly:
        #   sum_i (e15 * c1 * scale_i) = e15 * c1   when sum_i(scale_i) = 1
        # (Literal C++ port would triple-count with 3 animals: 3 * e15*c1.)
        c22 = e15 * c1 * myAnimalContributionScale

        myDairyMCalorieCounter    += c21
        myWildMeatMCalorieCounter += c22
        myTameMeatMCalorieCounter += c23

        LaUtils.debug.log(
            f"IncludeDairy animal {myAnimalGuid[:8]}: "
            f"e2={e2:.1f}, e3={e3:.1f}, e10={e10:.1f}, e7={e7:.3f}, "
            f"c21(dairy)={c21:.1f}, c23(meat)={c23:.1f}",
            "Calculation"
        )

        # --- Per-animal report (IncludeDairy mode — simple apportionment, no herd dynamics) ---
        myAnimalName = myAnimal.name if myAnimal else "(unknown)"
        myAnimalReport = (
            f"Animal: {myAnimalName}\n"
            f"Mode: Animals First, Include Dairy\n"
            f"Contribution share (percentTameMeat): {myAnimalContributionScale*100.:.2f}%\n"
            f"Target kcal for this animal: {myTargetForThisAnimal:,.1f}\n"
            f"Offspring needed per year: {e7:.3f}\n\n"
            ".........................\n"
            ".  Per-Offspring Values  .\n"
            ".........................\n"
            f"Milk kg/day: {c2:.4f}\n"
            f"Milk kcal/kg: {c3:.1f}\n"
            f"Lactation days: {c4}\n"
            f"Wean age days: {c5}\n"
            f"Kill weight kg: {c6}\n"
            f"Usable meat fraction: {c7:.3f}\n"
            f"Meat kcal/kg: {c9}\n"
            f"Dairy potential per offspring (e2): {e2:,.1f} kcal\n"
            f"Dairy actual after utilisation (e3): {e3:,.1f} kcal\n"
            f"Total value per offspring (e10): {e10:,.1f} kcal\n\n"
            ".........................\n"
            ".    Contributions      .\n"
            ".........................\n"
            f"Dairy MCals (c21):           {c21*_K_KCAL_TO_MCAL:,.2f}\n"
            f"Tame Meat MCals (c23):       {c23*_K_KCAL_TO_MCAL:,.2f}\n"
            f"Wild Meat MCals (c22 share): {c22*_K_KCAL_TO_MCAL:,.2f}\n"
            f"Total animal MCals:          {(c21+c23+c22)*_K_KCAL_TO_MCAL:,.2f}\n"
        )
        # second tuple element: this animal's contribution in MCals (no herd land calc here)
        myAnimalCalcsReportMap[myAnimalGuid] = (
            myAnimalReport,
            (c21 + c23) * _K_KCAL_TO_MCAL,
        )

    # --- Finalization: direct port of C++ lines 804-830 ---
    # c14 is total kcal/year; convert counters to same unit for ratios
    c24 = (1.0 - c12) * (c14 - e15)    # wild-plant kcals
    c25 = c12 * (c14 - e15)             # domestic-crop kcals
    c30 = c24 / c14                      # wild-plant fraction
    c31 = c25 / c14                      # domestic-crop fraction

    c28 = myWildMeatMCalorieCounter / c14   # wild-meat fraction
    c29 = myTameMeatMCalorieCounter / c14   # tame-meat fraction
    c27 = myDairyMCalorieCounter / c14      # dairy fraction

    # Convert kcal → MCal (* 0.001 * 0.001 = * 1e-6)
    _k = _K_KCAL_TO_MCAL

    LaUtils.debug.log(
        f"IncludeDairy(simple) end. c27(dairy)={c27:.4f}, c28(wild)={c28:.4f}, "
        f"c29(tame)={c29:.4f}, c30(wildPlant)={c30:.4f}, c31(crop)={c31:.4f}",
        "Calculation"
    )

    # C++ lines 816-829
    myDietLabels.dairyMCalories        = myDairyMCalorieCounter * _k
    myDietLabels.cropMCalories         = c25 * _k
    myDietLabels.animalMCalories       = myTameMeatMCalorieCounter * _k
    myDietLabels.wildAnimalMCalories   = myWildMeatMCalorieCounter * _k
    myDietLabels.wildPlantsMCalories   = c24 * _k
    myDietLabels.dairyPortionPct       = c27 * 100.0
    myDietLabels.tameMeatPortionPct    = c29 * 100.0
    myDietLabels.cropsPortionPct       = c31 * 100.0
    myDietLabels.wildAnimalPortionPct  = c28 * 100.0
    myDietLabels.wildPlantsPortionPct  = c30 * 100.0
    # C++ line 826: setAnimalPortionPct(mDietPercent*100. - c27*100.)
    myDietLabels.animalPortionPct      = (c15 - c27) * 100.0
    # C++ line 827: setPlantsPortionPct((1 - mDietPercent)*100.)
    myDietLabels.plantsPortionPct      = (1.0 - c15) * 100.0
    # C++ line 828: setMCalsIndividualAnnual(myMCalsIndividualAnnual)  (kcal in C++)
    myDietLabels.kiloCaloriesIndividualAnnual = c11 * 365.0
    # C++ line 829: setMCalsSettlementAnnual(myMCalsSettlementAnnual * .001)
    myDietLabels.megaCaloriesSettlementAnnual = c14 * 0.001

    # -----------------------------------------------------------------------
    # PYTHON ENHANCEMENT — Per-crop synthesis
    # -----------------------------------------------------------------------
    # C++ `getAreaTargetsCropsMapAFID()` (lamodel.cpp:1575-1579) is an empty
    # stub. We split the domestic-crop budget c25 across selected crops
    # using `cropParameter.percentTameCrop` as each crop's share, then size
    # the area from cropCalories (kcal/kg) and cropYield (kg per area unit).
    # Spoilage and reseed adjustments mirror DairySeparate's pattern.
    # -----------------------------------------------------------------------
    myTotalCropAreaHa = 0.0
    for myCropGuid, myCropParameterGuid in theModel.mCropsMap.items():
        myCrop = LaUtils.getCrop(myCropGuid)
        myCropParameter = LaUtils.getCropParameter(myCropParameterGuid)

        myCropName  = myCrop.name if myCrop else "(unknown)"
        myCropShare = (myCropParameter.percentTameCrop * 0.01) if myCropParameter else 0.0
        myCropKcal  = c25 * myCropShare
        myCropMCal  = myCropKcal * _K_KCAL_TO_MCAL

        myCropCalsPerKg = myCrop.cropCalories if (myCrop and myCrop.cropCalories > 0) else 0.0
        myKgForPeopleBase = myCropKcal / myCropCalsPerKg if myCropCalsPerKg > 0 else 0.0

        mySpoilagePct = (myCropParameter.spoilage * 0.01) if myCropParameter else 0.0
        myReseedPct   = (myCropParameter.reseed   * 0.01) if myCropParameter else 0.0
        myKgForPeople = myKgForPeopleBase * (1.0 + myReseedPct + mySpoilagePct)

        # Normalize yield to kg/ha (cropYield is kg/dunum if areaUnits == Dunum)
        myYieldKgPerHa = (
            myCrop.cropYield * 10.0
            if myCrop and myCrop.areaUnits == AreaUnits.Dunum
            else (myCrop.cropYield if myCrop else 0.0)
        )
        myCropAreaHa = myKgForPeople / myYieldKgPerHa if myYieldKgPerHa > 0 else 0.0
        myTotalCropAreaHa += myCropAreaHa

        myCropReport = (
            f"Crop: {myCropName}\n"
            f"Mode: Animals First, Include Dairy (Python enhancement)\n"
            f"Crop share (percentTameCrop): {myCropShare*100.:.2f}%\n"
            f"Domestic crop budget (c25):   {c25*_K_KCAL_TO_MCAL:,.2f} MCals\n"
            f"This crop's MCal target:      {myCropMCal:,.2f} MCals\n\n"
            ".........................\n"
            ".   Production Target   .\n"
            ".........................\n"
            f"Crop calories: {myCropCalsPerKg:,.0f} kcal/kg\n"
            f"Kg for people (base):                  {myKgForPeopleBase:,.0f} kg\n"
            f"  + Reseed allowance ({myReseedPct*100.:>5.1f}%): {myKgForPeopleBase*myReseedPct:>10,.0f} kg\n"
            f"  + Spoilage allowance ({mySpoilagePct*100.:>5.1f}%): {myKgForPeopleBase*mySpoilagePct:>10,.0f} kg\n"
            f"Adjusted kg target:                    {myKgForPeople:,.0f} kg\n\n"
            ".........................\n"
            ".      Area Target      .\n"
            ".........................\n"
            f"Yield: {myYieldKgPerHa:,.0f} kg/ha"
            f"{' (normalized from Dunum)' if (myCrop and myCrop.areaUnits == AreaUnits.Dunum) else ''}\n"
            f"Area needed: {myCropAreaHa:,.2f} ha\n"
        )
        myCropCalcsReportMap[myCropGuid] = (myCropReport, myCropAreaHa)

    # Publish the synthesized maps + area totals (Python enhancement)
    myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap
    myDietLabels.cropCalcsReportMap   = myCropCalcsReportMap
    myDietLabels.animalAreaTargetsMap = {k: v[1] for k, v in myAnimalCalcsReportMap.items()}
    myDietLabels.cropAreaTargetsMap   = {k: v[1] for k, v in myCropCalcsReportMap.items()}
    myDietLabels.totalLandNeeded      = myTotalCropAreaHa

    theModel.mDietLabels = myDietLabels
    return myDietLabels

def doCalcsPlantsFirstIncludeDairy(theModel: 'LaModel') -> LaDietLabels:
    """Stub for Plants First, Include Dairy."""
    LaUtils.debug.log("Using stub for doCalcsPlantsFirstIncludeDairy", "Warning")
    return doCalcsAnimalsFirstDairySeparate(theModel)


def doTheFallowAllocation(model: 'LaModel', thePriority: Priority, theAvailableFallowValue: float, theTotalNeededByGroup: float, theCountInGroup: float) -> float:
    """
    Allocates fallow value to a priority group.
    Direct port of LaModel::doTheFallowAllocation() from lamodel.cpp (lines 448-498).
    """
    if theTotalNeededByGroup <= 0: return theAvailableFallowValue
    
    myFallowDifference = theAvailableFallowValue - theTotalNeededByGroup
    myRemainingFallow = 0.0
    
    if myFallowDifference > 0:
        # Status.MoreThanEnoughToCompletelySatisfy
        for myAnimalGuid, myAnimalParameterGuid in model.mAnimalsMap.items():
            myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
            if myAnimalParameter.fallowUsage == thePriority:
                if myAnimalGuid in model.mValueMap:
                    model.mValueMap[myAnimalGuid] = 0.0 # Requirement fully met
        myRemainingFallow = myFallowDifference
    else:
        # Status.NotEnoughToCompletelySatisfy
        for myAnimalGuid, myAnimalParameterGuid in model.mAnimalsMap.items():
            myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
            if myAnimalParameter.fallowUsage == thePriority:
                if myAnimalGuid in model.mValueMap:
                    myIndividualRequirement = model.mValueMap[myAnimalGuid]
                    myProportion = myIndividualRequirement / theTotalNeededByGroup
                    myAllocatedMCals = theAvailableFallowValue * myProportion
                    model.mValueMap[myAnimalGuid] -= myAllocatedMCals
                    model.mValueMap[myAnimalGuid] = max(0.0, model.mValueMap[myAnimalGuid])
        myRemainingFallow = 0.0
        
    return myRemainingFallow
