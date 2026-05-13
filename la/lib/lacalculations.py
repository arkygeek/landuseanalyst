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
from la.lib.la import Priority, Status, AreaUnits, EnergyType, LaDietLabels
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

    myWildMeatPortion = (1. - theModel.mMeatPercent)
    myDairyUtilization = theModel.mDairyUtilisation * 0.01 # Assuming percent input
    myDairyLimitPercent = theModel.mLimitDairyPercentage * 0.01 # Assuming percent input
    myLimitDairyBool = theModel.mLimitDairy
    myPlantPercent = 1. - theModel.mDietPercent
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
        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * theModel.mDietPercent * theModel.mMeatPercent
        
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

        myFoodSourceMap = myAnimalParameter.fodderSourceMap()
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
            myGrain = myFoodSource.grain() * .001
            myFodder = myFoodSource.fodder() * .001
            myDays = myFoodSource.days()
            
            myGrainToAdd = myGrain * myDays * myTotalOffspring
            myFoodSourceMapCounter[myCropGuid] += myGrainToAdd
            
            myCropObj = LaUtils.getCrop(myCropGuid)
            myFoodValueOfCrop = myCropObj.cropCalories() * .001
            myFoodValueofFodder = myCropObj.fodderValue() * .001
            
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
    myWildMeatPercent = myWildMeatPortion * theModel.mDietPercent
    
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
        myCropFoodValue = myCrop.cropCalories() * .001
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
        
        myCropYield = myCrop.cropYield() * 10.0 if myCrop.areaUnits() == AreaUnits.Dunum else myCrop.cropYield()
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
            f"myCrop.cropYield() = {myCrop.cropYield()}\n"
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

    # Populate model maps for persistence
    theModel.mCalcsCropsMap = {k: v[0] for k, v in myCropCalcsReportMap.items()}
    theModel.mAreaTargetsCropsMap = {k: v[1] for k, v in myCropCalcsReportMap.items()}
    
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
