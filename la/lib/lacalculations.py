# --- START OF FILE la/lib/lacalculations.py ---

from typing import Dict, Tuple, Optional
# import math # For potential math operations

# Assuming la.lib.lautils contains LaUtils
# Assuming la.lib.la contains Priority, Status, AreaUnits, etc.
# Assuming la.lib.ladietlabels contains LaDietLabels
# Assuming la.lib.laanimal contains LaAnimal
# Assuming la.lib.lacrop contains LaCrop
# Assuming la.lib.lafoodsource contains LaFoodSource
# Assuming la.lib.laanimalparameter contains LaAnimalParameter
# Assuming la.lib.lacropparameter contains LaCropParameter
# Assuming la.lib.lamodel contains LaModel type hint (use forward reference if needed)

from la.lib.lautils import LaUtils
from la.lib.la import Priority, Status, AreaUnits, EnergyType
from la.lib.ladietlabels import LaDietLabels
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lafoodsource import LaFoodSource
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacropparameter import LaCropParameter
# Forward reference for type hint if LaModel imports this module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   from la.lib.lamodel import LaModel

# Note: Replace all occurrences of 'self.' from the original LaModel methods
#       with 'model.' in the functions below.

def doCalcsPlantsFirstIncludeDairy(theModel: 'LaModel') -> LaDietLabels:
    # --- Paste the content of LaModel.doCalcsPlantsFirstIncludeDairy here ---
    # --- Remember to change all 'self.' references to 'model.' ---
    # Example change: self.caloriesPerPersonDaily -> model.caloriesPerPersonDaily
    # Example change: self.mAnimalsMap -> model.mAnimalsMap

    # --- Start of pasted and modified code ---
    myDietLabels = LaDietLabels()
    myMCalsIndividualAnnual: float = float(str(theModel.caloriesPerPersonDaily)) * 365.0
    myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * float(str(theModel.population))
    myAnimal = LaAnimal()  # Matches C++ declaration but not used in this simplified version
    myCrop = LaCrop()

    # Get property values from internal attributes (following C++ variable naming)
    try:
        # Base values - matching C++ variable names
        myMCalsIndividualAnnual = theModel.mCaloriesPerPersonDaily * 365.0 / 1000.0  # Convert to annual MCals
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * theModel.mPopulation
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0
        myWildMeatMCalorieCounter = 0.0
        mySelectedAnimalsMap = theModel.mAnimalsMap  # Similar to C++ QMap<QString,QString>

        # C++ style variable declarations (c1, c8, etc.)
        c1 = 1.0 - (theModel.mMeatPercent / 100.0)  # Decimal form of meat percent
        c8 = theModel.mDairyUtilisation / 100.0     # Decimal form of dairy utilization
        c10 = theModel.mPopulation
        c11 = theModel.mCaloriesPerPersonDaily
        c14 = c10 * c11 * 365.0 / 1000.0         # Settlement annual MCal
        c15 = theModel.mDietPercent / 100.0         # Decimal form of diet percent

        # Calculate MCals for different food sources
        # In this simplified version, we'll estimate values that would normally
        # come from detailed animal and crop calculations

        # Initialize counters (simplified calculation)
        myDairyMCalorieCounter = myMCalsSettlementAnnual * c15 * 0.05  # 5% of animal diet
        myTameMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * (theModel.mMeatPercent / 100.0)  # Tame meat percent
        myWildMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * c1  # Wild meat percent
        myCropMCalories = myMCalsSettlementAnnual * (1.0 - c15) * (theModel.mPercentOfDietThatIsFromCrops / 100.0)  # Crop percent
        myWildPlantsMCalories = myMCalsSettlementAnnual * (1.0 - c15) * (1.0 - theModel.mPercentOfDietThatIsFromCrops / 100.0)  # Wild plant percent

        # Calculate percentages (as in C++ implementation)
        totalMCalories = myMCalsSettlementAnnual
        tameMeatPercent = myTameMeatMCalorieCounter / totalMCalories
        wildMeatPercent = myWildMeatMCalorieCounter / totalMCalories
        cropPercent = myCropMCalories / totalMCalories
        wildPlantPercent = myWildPlantsMCalories / totalMCalories
        dairyPercent = myDairyMCalorieCounter / totalMCalories

        # Calculate overall percentages
        myOverallMeatPercent = tameMeatPercent + wildMeatPercent  # Combined meat percent
        myOverallPlantPercent = cropPercent + wildPlantPercent    # Combined plant percent

        # Report maps for crops and animals (empty in simplified version)
        myCropCalcsReportMap = {}
        myAnimalCalcsReportMap = {}
        myDairySurplus = 0.0 # No surplus dairy
        # Set all values in the diet labels object
        # model._setDietLabels(
        #     myDietLabels,
        #     myDairyMCalorieCounter,      # Overall dairy MCals
        #     myCropMCalories,              # Overall crop MCals
        #     myTameMeatMCalorieCounter,    # Tame meat MCals
        #     myWildMeatMCalorieCounter,    # Wild meat MCals
        #     myWildPlantsMCalories,        # Wild plants MCals
        #     dairyPercent,                # Overall dairy percent
        #     tameMeatPercent,             # Domestic meat percent
        #     cropPercent,                 # Overall crop percent
        #     wildMeatPercent,             # Wild meat percent
        #     wildPlantPercent,            # Overall wild plant percent
        #     myOverallMeatPercent,        # Overall meat percent
        #     myOverallPlantPercent,       # Overall plant percent
        #     myMCalsIndividualAnnual * 1000.0,  # Convert back to kCal
        #     myMCalsSettlementAnnual,     # MCals settlement annual
        #     0.0,                         # No dairy surplus in this simplified calculation
        #     myCropCalcsReportMap,        # Empty crop calcs report map
        #     myAnimalCalcsReportMap       # Empty animal calcs report map
        # )

        # Log results
        LaUtils.debug.log(f"doCalcsPlantsFirstIncludeDairy - Animal: {myOverallMeatPercent*100:.2f}%, Plant: {myOverallPlantPercent*100:.2f}%", "Diet")

    except Exception as e:
        LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
        import traceback
        LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    myDietLabels.mAnimalAreaTargetsMap = {}  # Empty in this simplified version
    myDietLabels.mCropAreaTargetsMap = {}  # Empty in this simplified version

    myDietLabels.dairyMCalories = myDairyMCalorieCounter * 0.001 * 0.001  # Set dairy MCals in diet labels
    myDietLabels.cropMCalories = myCropMCalories * 0.001 * 0.001  # Set crop MCals in diet labels
    myDietLabels.animalMCalories = myTameMeatMCalorieCounter * 0.001 * 0.001  # Set animal MCals in diet labels
    myDietLabels.wildAnimalMCalories = myWildMeatMCalorieCounter * 0.001 * 0.001  # Set wild animal MCals in diet labels
    myDietLabels.wildPlantsMCalories = myWildPlantsMCalories * 0.001 * 0.001  # Set wild plants MCals in diet labels
    myDietLabels.dairyPortionPct = dairyPercent * 100.0  # Set dairy percent in diet labels
    myDietLabels.tameMeatPortionPct = tameMeatPercent * 100.0  # Set tame meat percent in diet labels
    myDietLabels.cropsPortionPct = cropPercent * 100.0  # Set crop percent in diet labels
    myDietLabels.wildAnimalPortionPct = wildMeatPercent * 100.0  # Set wild animal percent in diet labels
    myDietLabels.wildPlantsPortionPct = wildPlantPercent * 100.0  # Set wild plants percent in diet labels
    myDietLabels.animalPortionPct = myOverallMeatPercent * 100.0  # Set overall animal percent in diet labels
    myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.0  # Set overall plant percent in diet labels
    myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0  # Set annual kCal in diet labels
    myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual  # Set settlement annual MCals in diet labels
    myDietLabels.dairySurplusMCalories = myDairySurplus * 0.001 * 0.001  # Set dairy surplus MCals in diet labels
    myDietLabels.mAnimalCalcsReportMap = myAnimalCalcsReportMap  # Set animal calcs report map in diet labels
    myDietLabels.mCropCalcsReportMap = myCropCalcsReportMap  # Set crop calcs report map in diet labels

    myDietLabels.animalPortionPct = myOverallMeatPercent * 100.0
    myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.0
    myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0
    myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
    myDietLabels.dairySurplusMCalories = myDairySurplus * 0.001 * 0.001
    myDietLabels.mAnimalCalcsReportMap = myAnimalCalcsReportMap
    myDietLabels.mCropCalcsReportMap = myCropCalcsReportMap

    LaUtils.debug.log(f"doCalcsPlantsFirstIncludeDairy completed", "Diet")
    return myDietLabels
    # --- End of pasted and modified code ---

def doCalcsPlantsFirstDairySeparate(theModel: 'LaModel') -> LaDietLabels:
    # --- Paste the content of LaModel.doCalcsPlantsFirstDairySeparate here ---
    # --- Remember to change all 'self.' references to 'model.' ---
    myDietLabels = LaDietLabels()
    LaAnimal = None  # Matches C++
    myMCalsIndividualAnnual = float(str(theModel.caloriesPerPersonDaily)) * 365.0 / 1000.0  # Convert to MCal
    myMCalsSettlementAnnual = myMCalsIndividualAnnual * int(str(theModel.population))
    myPlantPercent = 1.0 - (theModel.mDietPercent / 100.0)  # Plant portion as decimal
    myDomesticCropPortion = theModel.mPercentOfDietThatIsFromCrops / 100.0  # Crop portion of plants as decimal
    myWildMeatPortion = 1.0 - (theModel.mMeatPercent / 100.0)  # Wild meat portion as decimal
    # Log calculation start
    LaUtils.debug.log("Starting doCalcsPlantsFirstDairySeparate calculation", "Diet")

    try:
        # Base calculations similar to include dairy but with separate dairy tracking
        calories_daily = float(theModel.mCaloriesPerPersonDaily)
        population_count = float(theModel.mPopulation)
        meat_percent = float(theModel.mMeatPercent) / 100.0  # Convert to decimal
        diet_percent = float(theModel.mDietPercent) / 100.0  # Convert to decimal

        LaUtils.debug.log(f"Input parameters - calories_daily: {theModel.mCaloriesPerPersonDaily}, population: {theModel.mPopulation}", "Diet")
        LaUtils.debug.log(f"Diet parameters - meat_percent: {theModel.mMeatPercent}%, diet_percent: {theModel.mDietPercent}%", "Diet")
        LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

        # Initialize counters with simplified approach to match C++ variable names
        myDairyMCalorieCounter = myMCalsSettlementAnnual * 0.05  # Separate counter for dairy (5% of total)
        myTameMeatMCalorieCounter = myMCalsSettlementAnnual * (theModel.mDietPercent / 100.0) * (theModel.mMeatPercent / 100.0)  # tame meat
        myWildMeatMCalorieCounter = myMCalsSettlementAnnual * (float(str(theModel.mDietPercent)) / 100.0) * myWildMeatPortion  # wild meat

        # Following the same pattern from C++ for crop and plant calculations
        myOverallPlantPercent = myPlantPercent
        myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion
        myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myDomesticCropPortion)

        # Calculate MCals for different components
        myOverallDomesticMeatMCals = myTameMeatMCalorieCounter
        myOverallDairyMCals = myDairyMCalorieCounter
        myOverallWildMeatMCals = myWildMeatMCalorieCounter
        myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
        myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual

        # Calculate overall percentages - key values for UI display
        myOverallMeatPercent = (myTameMeatMCalorieCounter + myWildMeatMCalorieCounter) / myMCalsSettlementAnnual
        myOverallDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual

        # Check for dairy surplus (from C++)
        myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
        myOVerallDairySurplusMCals = myFirstDairySurplusBool if myFirstDairySurplusBool > 0 else 0.0

        # Calculate percentages of the total settlement MCals
        myDomesticMeatPercent = myOverallDomesticMeatMCals / myMCalsSettlementAnnual
        myWildMeatPercent = myOverallWildMeatMCals / myMCalsSettlementAnnual
        myCropPercent = myOverallCropsMCals / myMCalsSettlementAnnual
        myWildPlantPercent = myOverallWildPlantsMCals / myMCalsSettlementAnnual

        # Create report maps (empty in simplified version)
        myCropCalcsReportMap = {}
        myAnimalCalcsReportMap = {}

        # Set all values in the diet labels object
        # model.setDietLabels(
        #     myDietLabels,
        #     myDairyMCalorieCounter,     # Overall dairy MCals
        #     myOverallCropsMCals,        # Overall crop MCals
        #     myTameMeatMCalorieCounter,  # Tame meat MCals
        #     myWildMeatMCalorieCounter,  # Wild meat MCals
        #     myOverallWildPlantsMCals,   # Wild plants MCals
        #     myOverallDairyPercent,      # Overall dairy percent
        #     myDomesticMeatPercent,      # Domestic meat percent
        #     myCropPercent,              # Overall crop percent
        #     myWildMeatPercent,          # Wild meat percent
        #     myWildPlantPercent,         # Overall wild plant percent
        #     myOverallMeatPercent,       # Overall meat percent
        #     myOverallPlantPercent,      # Overall plant percent
        #     myMCalsIndividualAnnual * 1000.0,  # Convert back to kCal
        #     myMCalsSettlementAnnual,    # MCals settlement annual
        #     myOVerallDairySurplusMCals, # Dairy surplus MCals
        #     myCropCalcsReportMap,       # Crop calcs report map
        #     myAnimalCalcsReportMap      # Animal calcs report map
        # )

        # Log results
        LaUtils.debug.log(f"Results - Meat: {myOverallMeatPercent*100:.2f}%, Plant: {myOverallPlantPercent*100:.2f}%, Dairy: {myOverallDairyPercent*100:.2f}%", "Diet")
        LaUtils.debug.log("doCalcsPlantsFirstDairySeparate calculation completed successfully", "Diet")

    except Exception as e:
        LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
        import traceback
        LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
        # Return empty or default labels in case of error
        myDietLabels = LaDietLabels() # Reset to default
    LaUtils.debug.log(f"doCalcsPlantsFirstDairySeparate completed", "Diet")
    return myDietLabels

def doCalcsAnimalsFirstIncludeDairy(theModel: 'LaModel') -> LaDietLabels:
    # --- Paste the content of LaModel.doCalcsAnimalsFirstIncludeDairy here ---
    # --- Remember to change all 'self.' references to 'model.' ---
    myDietLabels = LaDietLabels()
    myAnimal = LaAnimal()

    # Initialize base calculations
    myMCalsIndividualAnnual: float = theModel.mCaloriesPerPersonDaily * 365.0
    myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * theModel.mPopulation
    myDairyMCalorieCounter: float = 0.0
    myTameMeatMCalorieCounter: float = 0.0
    myWildMeatMCalorieCounter: float = 0.0
    mySelectedAnimalsMap: Dict[str, str] = theModel.mAnimalsMap

    # Calculate coefficients
    c1: float = 1.0 - theModel.mMeatPercent
    c8: float = float(theModel.mDairyUtilisation) # convert to float
    c10: float = float(theModel.mPopulation) # convert to float
    c11: float = float( theModel.mCaloriesPerPersonDaily) # convert to float
    c14: float = c10 * c11 * 365.0
    c15: float = float(theModel.mDietPercent) # convert to float
    c12: float = float(theModel.mPercentOfDietThatIsFromCrops) # convert to float
    e15: float = c14 * c15

    LaUtils.debug.log("Starting animal calculations", "Diet")

    # Process each animal in the map
    for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
        try:
            myAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)

            # Calculate animal-specific coefficients
            c2 = float(str(myAnimal.milkGramsPerDay)) * 0.001
            c3 = myAnimal.milkFoodValue
            c4 = myAnimal.lactationTime
            c5 = myAnimal.weaningAge
            c6 = myAnimal.killWeight
            c7 = myAnimal.usableMeat * 0.01 # type: ignore
            e2 = c2 * c3 * (c4 - c5) # type: ignore
            e3 = e2 * c8
            c9 = myAnimal.meatFoodValue
            e10 = e3 + (c9 * c7 * c6)
            e7 = (e15 * (1.0 - c1)) / e10
            c21 = e7 * e3
            c23 = e7 * c6 * c7 * c9
            c22 = e15 - c21 - c23

            # Update counters
            myDairyMCalorieCounter += c21
            myWildMeatMCalorieCounter += c22
            myTameMeatMCalorieCounter += c23

            LaUtils.debug.log(f"Animal {myAnimal.name} processed - Dairy: {c21}, Wild: {c22}, Tame: {c23}", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error processing animal 916-lamodel {myAnimalGuid}: {str(e)}", "Error")

    # Calculate final coefficients
    c24 = (1.0 - c12) * (c14 - e15)
    c25 = c12 * (c14 - e15)
    c30 = c24 / c14
    c31 = c25 / c14

    c28 = myWildMeatMCalorieCounter / c14
    c29 = myTameMeatMCalorieCounter / c14
    c27 = myDairyMCalorieCounter / c14

    LaUtils.debug.log(f"Final coefficients - c27: {c27}, c28: {c28}, c29: {c29}", "Diet")

    # Set diet label values
    myDietLabels.dairyMCalories = myDairyMCalorieCounter * 0.001 * 0.001
    myDietLabels.cropMCalories = c25 * 0.001 * 0.001
    myDietLabels.animalMCalories = myTameMeatMCalorieCounter * 0.001 * 0.001
    myDietLabels.wildAnimalMCalories = myWildMeatMCalorieCounter * 0.001 * 0.001
    myDietLabels.wildPlantsMCalories = c24 * 0.001 * 0.001
    myDietLabels.dairyPortionPct = c27 * 100.0
    myDietLabels.tameMeatPortionPct = c29 * 100.0
    myDietLabels.cropsPortionPct = c31 * 100.0
    myDietLabels.wildAnimalPortionPct = c28 * 100.0
    myDietLabels.wildPlantsPortionPct = c30 * 100.0
    myDietLabels.animalPortionPct = theModel.mDietPercent * 100.0 - c27 * 100.0
    myDietLabels.plantsPortionPct = (1.0 - theModel.mDietPercent) * 100.0
    myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
    myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
    LaUtils.debug.log(f"doCalcsAnimalsFirstIncludeDairy completed", "Diet")
    return myDietLabels

def doCalcsAnimalsFirstDairySeparate(theModel: 'LaModel') -> LaDietLabels:
    # --- Paste the entire content of LaModel.doCalcsAnimalsFirstDairySeparate here ---
    # --- Including the loop through animals, fodder calculation, crop loop, ---
    # --- fallow allocation call, and final report update. ---
    # --- Remember to change ALL 'self.' references to 'model.' ---
    # --- Also change 'self.allocateFallowGrazingLand(...)' to 'allocateFallowGrazingLand(model, ...)' ---
    # --- And 'self.doTheFallowAllocation(...)' to 'doTheFallowAllocation(model, ...)' ---

    # --- Start of pasted and modified code ---
    """
        Calculate diet values when animals are prioritized and dairy is separate from meat.

        This method performs a detailed calculation of dietary requirements for a settlement,
        prioritizing animal-based food sources (meat and dairy) while treating dairy as a
        separate category from meat. It calculates the required caloric contributions from
        various food sources (animals, crops, wild plants) and determines the land area
        needed to meet these requirements. Matches the C++ implementation closely.

        Returns:
            LaDietLabels: An object containing the calculated dietary labels, including
                          percentages, caloric contributions, and area targets for crops
                          and animals.
    """
    # from la.lib.lautils import LaUtils
    # from la.lib.la import LaReportMap



    theModel.mCropCalcsReportMap = {} # Equivalent to C++ LaReportMap
    theModel.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap
    theModel.mValueMap = {} # Equivalent to C++ LaReportMap
    theModel.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap

    try:
        myAnimalCalcsReportMap: Dict[str, Tuple[str, float]] = {} # Equivalent to C++ LaReportMap
        myCropCalcsReportMap: Dict[str, Tuple[str, float]] = {} # Equivalent to C++ LaReportMap

        myAnimalsMap: Dict[str, float] = {} # for storing the calculations to send to fallow allocation

        myFodderNeedsPerCrop = {} # Equivalent to C++ myFoodSourceMapCounter (QMap<QString, float>)
        animalMCalRequirementMap = {} # Stores initial MCal requirements for fallow allocation

        myDietLabels = LaDietLabels()
        myAnimal = LaAnimal()

        myCrops: Dict[str, float] = theModel.mCropsMap  # for storing crop data


        # Assuming my_crops is a dictionary (equivalent to QMap<QString, QString>)
        # e.g., my_crops = {"crop_guid_1": "crop_name_1", "crop_guid_2": "crop_name_2"}

        myFoodSourceMapCounter: Dict[str, float] = {}  # for storing food source data Initialize an empty dictionary (equivalent to QMap<QString, int>)

        # Iterate through the keys of the my_crops dictionary
        for myCropGuid in myCrops:
            # Insert the key into myFoodSourceMapCounter with a value of 0
            myFoodSourceMapCounter[myCropGuid] = 0
            # myFoodSourceMapCounter will now be like: {"cropGuid1": 0, "cropGuid2": 0, ...}

        myMCalsIndividualAnnual: float = theModel.mCaloriesPerPersonDaily * 365.0 * 0.001  # MCal/person/year
        myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * theModel.mPopulation # MCal/settlement/year
        myDairyMCalorieCounter: float = 0.0  # Accumulates potential dairy MCals from all animals
        myTameMeatMCalorieCounter: float = 0.0  # Accumulates potential tame meat MCals from all animals

        myWildMeatPortion: float = (1.0 - theModel.mMeatPercent)  # C++: myWildMeatPortion
        myDairyUtilization: float = (theModel.mDairyUtilisation)
        myDairyLimitPercent: float = theModel.mLimitDairyPercentage
        myLimitDairyBool: bool = bool(theModel.mLimitDairy)  # C++: myDairyUtilisation

        myPlantPercent: float = 1.0 - theModel.mDietPercent
        myDomesticCropPortion: float = theModel.mPercentOfDietThatIsFromCrops

        mySelectedAnimalsMap: Dict[str, float] = theModel.mAnimalsMap # type: ignore

        for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
            # print("--------==--------------------------------------------==-------") # Using print instead of LaUtils.debug for literalness
            # print("--------==        Looping through the animals         ==-------")
            # print("--------==--------------------------------------------==-------")

            myAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid) # type: ignore
            myAdditionalMCalCounter = 0.
            myAdditionalMCalCounter1 = 0.

            myMilkKgPerDay = myAnimal.milkGramsPerDay * .001 # type: ignore
            myMilkFoodValue = myAnimal.milkFoodValue * .001 # type: ignore
            myLactationTime = myAnimal.lactationTime
            myWeaningAge = myAnimal.weaningAge
            myGestatingTime = myAnimal.gestationTime
            myEstrousCycle = myAnimal.estrousCycle
            myBabiesPerBirth = myAnimal.youngPerBirth

            myDeathRate = myAnimal.deathRate * .01 # type: ignore
            myBreedingRatio = myAnimal.femalesPerMale
            myKillWeight = myAnimal.killWeight
            myUsablePortionOfAnimal = myAnimal.usableMeat * .01 # type: ignore
            myAdultWeight = myAnimal.adultWeight
            myFemalesToMales = myAnimal.femalesPerMale
            myConceptionEfficiency = myAnimal.conceptionEfficiency * .01 # type: ignore
            myMeatValueMCal = myAnimal.meatFoodValue * .001 # type: ignore
            mySexualMaturity = myAnimal.sexualMaturity # in months
            myBreedingYears = myAnimal.breedingExpectancy # in years
            myAnimalContributionToMeatPortion = myAnimalParameter.percentTameMeat * .01 # type: ignore # B2
            myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * theModel.dietPercent * theModel.meatPercent # B3
            myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge) # type: ignore # B4
            myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal # B5
            myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization # B6

            myBirthingEventsPerYear1 = 365. / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime) # type: ignore # B21
            myBirthingEventsPerYear = 1. if myBirthingEventsPerYear1 < 1. else myBirthingEventsPerYear1
            myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal * (1. / ((mySexualMaturity / 12.) + myBreedingYears))) # type: ignore
            myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear) # type: ignore # B7
            myCulledAdultMalesValue = myCulledMothersValue / myFemalesToMales # B8
            myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue # B9
            myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue # B1
            myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue # B12
            myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear  # B14

            myTameMeatMCalorieCounter += myMCalsFromTheMeat
            myDairyMCalorieCounter += myMCalsUtilizedFromDairy

            myFoodSourceMap: Dict[str, LaFoodSource] = myAnimalParameter.fodderSourceMap # type: ignore

            myMeatPercent: float = myMCalsFromTheMeat / myMCalsSettlementAnnual  # B15
            myDairyPercent: float = myMCalsUtilizedFromDairy / myMCalsSettlementAnnual  # B16

            #
            # Now to get the herd size so we can calculate MCal requirements
            #
            #   !!! remember that this needs adjustment later for fodder fallow and grain
            #

            myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1. - myDeathRate) * myConceptionEfficiency # type: ignore B22
            myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear # B23
            myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5 # B24
            myFemalesStepOne = myMalesStepOne # B25
            myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity / 12.)) / myBreedingYears # type: ignore # B26
            myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio # B27
            myAdditionalMothers = ((myReplacementMothersPerYear / myOffspringPerMotherPerYear) * 2.) + (myBreedingMalesRequired * 2.) # B28
            myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5 # B29
            myFemalesStepTwo = myMalesStepTwo # B30
            myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear # B32
            myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo # B33
            myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo # B34
            myTotalOffspring = myTotalMaleOffspring * 2. #+ myTotalFemaleOffspring; # B35

            myFeedForGestating = myAnimal.gestating * .001 # type: ignore
            myFeedForLactating = myAnimal.lactating * .001 # type: ignore
            myFeedForMaintenance = myAnimal.maintenance * .001 # type: ignore
            myFeedForOffspringPerKg = myAnimal.juvenile * .001 # type: ignore

            myGestatingMCals = myTotalOffspring * myGestatingTime * myFeedForGestating

            myLactatingMCals = myTotalOffspring * myLactationTime * myFeedForLactating
            myDaysForMaintenance = 0 if (365 - (myGestatingTime + myLactationTime) < 0) else (365 - (myGestatingTime + myLactationTime)) # type: ignore


            myDryMothers = 0 if myTotalMothers - myTotalOffspring < 0 else myTotalMothers - myTotalOffspring
            myDryMothersMCals = myDryMothers * 365. * myFeedForMaintenance
            myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance
            myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals

            myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.
            myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365. - myWeaningAge) # type: ignore

            myAnimalReport = "myMilkKgPerDay = " + str(myMilkKgPerDay) + "\n"
            myAnimalReport += "myMilkFoodValue = " + str(myMilkFoodValue) + "\n"
            myAnimalReport += "myLactationTime = " + str(myLactationTime) + "\n"
            myAnimalReport += "myWeaningAge = " + str(myWeaningAge) + "\n"
            myAnimalReport += "myKillWeight = " + str(myKillWeight) + "\n"
            myAnimalReport += "myUsablePortionOfAnimal = " + str(myUsablePortionOfAnimal) + "\n"
            myAnimalReport += "myAdultWeight = " + str(myAdultWeight) + "\n"
            myAnimalReport += "myFemalesToMales = " + str(myFemalesToMales) + "\n"
            myAnimalReport += "myMeatValueMCal = " + str(myMeatValueMCal) + "\n"
            myAnimalReport += "mySexualMaturity = " + str(mySexualMaturity) + "\n"
            myAnimalReport += "myBreedingYears = " + str(myBreedingYears) + "\n"
            myAnimalReport += "myAnimalContributionToMeatPortion = " + str(myAnimalContributionToMeatPortion) + "\n"
            myAnimalReport += "myAnimalMCalTarget = " + str(myAnimalMCalTarget) + "\n"
            myAnimalReport += "myPotentialDairyPerOffspring = " + str(myPotentialDairyPerOffspring) + "\n"
            myAnimalReport += "myValuePerOffspring = " + str(myValuePerOffspring) + "\n"
            myAnimalReport += "myActualDairyValueOfOffspring = " + str(myActualDairyValueOfOffspring) + "\n"
            myAnimalReport += "myCulledMothersValue = " + str(myCulledMothersValue) + "\n"
            myAnimalReport += "myCulledAdultMalesValue = " + str(myCulledAdultMalesValue) + "\n"
            myAnimalReport += "myFinalOffspringValue = " + str(myFinalOffspringValue) + "\n"
            myAnimalReport += "myOffspringNeededPerYear = " + str(myOffspringNeededPerYear) + "\n"
            myAnimalReport += "myMCalsFromTheMeat = " + str(myMCalsFromTheMeat) + "\n"
            myAnimalReport += "myMCalsUtilizedFromDairy = " + str(myMCalsUtilizedFromDairy) + "\n"
            myAnimalReport += "myTameMeatMCalorieCounter = " + str(myTameMeatMCalorieCounter) + "\n"
            myAnimalReport += "myDairyMCalorieCounter = " + str(myDairyMCalorieCounter) + "\n"
            myAnimalReport += "\n"
            myAnimalReport += "myBirthingEventsPerYear = " + str(myBirthingEventsPerYear) + "\n"
            myAnimalReport += "myOffspringPerMotherPerYear = " + str(myOffspringPerMotherPerYear) + "\n"
            myAnimalReport += "myMothersNeededStepOne = " + str(myMothersNeededStepOne) + "\n"
            myAnimalReport += "myMalesStepOne = " + str(myMalesStepOne) + "\n"
            myAnimalReport += "myFemalesStepOne = " + str(myFemalesStepOne) + "\n"
            myAnimalReport += "myReplacementMothersPerYear = " + str(myReplacementMothersPerYear) + "\n"
            myAnimalReport += "myBreedingMalesRequired = " + str(myBreedingMalesRequired) + "\n"
            myAnimalReport += "myAdditionalMothers = " + str(myAdditionalMothers) + "\n"
            myAnimalReport += "myMalesStepTwo = " + str(myMalesStepTwo) + "\n"
            myAnimalReport += "myFemalesStepTwo = " + str(myFemalesStepTwo) + "\n"
            myAnimalReport += "\n"
            myAnimalReport += "myTotalMothers = " + str(myTotalMothers) + "\n"
            myAnimalReport += "myTotalMaleOffspring = " + str(myTotalMaleOffspring) + "\n"
            myAnimalReport += "myTotalFemaleOffspring = " + str(myTotalFemaleOffspring) + "\n"
            myAnimalReport += "myTotalOffspring = " + str(myTotalOffspring) + "\n"
            myAnimalReport += "myFeedForGestating = " + str(myFeedForGestating) + "\n"
            myAnimalReport += "myFeedForLactating = " + str(myFeedForLactating) + "\n"
            myAnimalReport += "myFeedForMaintenance = " + str(myFeedForMaintenance) + "\n"
            myAnimalReport += "myFeedForOffspringPerKg = " + str(myFeedForOffspringPerKg) + "\n"

            # C++ Debug comments ported directly
            print(myAnimal.name)
            print("myMilkKgPerDay = " + str(myMilkKgPerDay))
            print("myMilkFoodValue = " + str(myMilkFoodValue))
            print("myLactationTime = " + str(myLactationTime))
            print("myWeaningAge = " + str(myWeaningAge))
            print("myKillWeight = " + str(myKillWeight))
            print("myUsablePortionOfAnimal = " + str(myUsablePortionOfAnimal))
            print("myAdultWeight = " + str(myAdultWeight))
            print("myFemalesToMales = " + str(myFemalesToMales))
            print("myMeatValueMCal = " + str(myMeatValueMCal))
            print("mySexualMaturity = " + str(mySexualMaturity))
            print("myBreedingYears = " + str(myBreedingYears))
            print("myAnimalContributionToMeatPortion = " + str(myAnimalContributionToMeatPortion))
            # Debug line continues
            print("myAnimalMCalTarget = " + str(myAnimalMCalTarget))
            print("myPotentialDairyPerOffspring = " + str(myPotentialDairyPerOffspring))
            print("myValuePerOffspring = " + str(myValuePerOffspring))
            print("myActualDairyValueOfOffspring = " + str(myActualDairyValueOfOffspring))
            print("myCulledMothersValue = " + str(myCulledMothersValue))
            print("myCulledAdultMalesValue = " + str(myCulledAdultMalesValue))
            print("myFinalOffspringValue = " + str(myFinalOffspringValue))
            print("myOffspringNeededPerYear = " + str(myOffspringNeededPerYear))
            print("myMCalsFromTheMeat = " + str(myMCalsFromTheMeat))
            print("myMCalsUtilizedFromDairy = " + str(myMCalsUtilizedFromDairy))
            print("myTameMeatMCalorieCounter = " + str(myTameMeatMCalorieCounter))
            print("myDairyMCalorieCounter = " + str(myDairyMCalorieCounter))

            print("myBirthingEventsPerYear = " + str(myBirthingEventsPerYear))
            print("myOffspringPerMotherPerYear = " + str(myOffspringPerMotherPerYear))
            print("myMothersNeededStepOne = " + str(myMothersNeededStepOne))
            print("myMalesStepOne = " + str(myMalesStepOne))
            print("myFemalesStepOne = " + str(myFemalesStepOne))
            print("myReplacementMothersPerYear = " + str(myReplacementMothersPerYear))
            print("myBreedingMalesRequired = " + str(myBreedingMalesRequired))
            print("myAdditionalMothers = " + str(myAdditionalMothers))
            print("myMalesStepTwo = " + str(myMalesStepTwo))
            print("myFemalesStepTwo = " + str(myFemalesStepTwo))
            print("         ++         ++         ")
            print("+++++++++++++++++++++++++++++++")
            print("           ++  +  ++           ")
            print("+++++++++++++++++++++++++++++++")
            print("         ++         ++         ")

            print("myTotalMothers = " + str(myTotalMothers))
            print("myTotalMaleOffspring = " + str(myTotalMaleOffspring))
            print("myTotalFemaleOffspring = " + str(myTotalFemaleOffspring))
            print("myTotalOffspring = " + str(myTotalOffspring))

            print("myFeedForGestating = " + str(myFeedForGestating))
            print("myFeedForLactating = " + str(myFeedForLactating))
            print("myFeedForMaintenance = " + str(myFeedForMaintenance))
            print("myFeedForOffspringPerKg = " + str(myFeedForOffspringPerKg))

            print("myGestatingMCals = " + str(myGestatingMCals))
            print("myLactatingMCals = " + str(myLactatingMCals))
            print("myDaysForMaintenance = " + str(myDaysForMaintenance))
            print("________------~~~~ Number of days gestating: " + str(myGestatingTime))
            print("________------~~~~ Number of days lactating: " + str(myLactationTime))
            print("myDryMothers = " + str(myDryMothers))
            print("myDryMothersMCals = " + str(myDryMothersMCals))
            print("myOtherMaintenanceMCals = " + str(myOtherMaintenanceMCals))
            print("myMaintenanceMCals = " + str(myMaintenanceMCals))
            print("myAdultMalesMCals = " + str(myAdultMalesMCals))
            print("myOffspringMCals = " + str(myOffspringMCals))

            # still looping through the animals here....

            # Iterate through fodder map (assuming it's a dict)
            for myCropGuid, myFoodSource in myFoodSourceMap: # Use items() for key-value pairs
                # print("    ----==--------------------------------------------==----")
                # print("    ----==          Adding to the fodder Map          ==----")
                # print("    ----==--------------------------------------------==----")
                # Note: C++ code used myFoodSourceMap.value(myCropGuid) which is redundant with iterator
                myFoodSource: LaFoodSource = myFoodSourceMap[myCropGuid] # type: ignore
                myGrain = myFoodSource.grain * .001
                myFodder = myFoodSource.fodder * .001
                myDays = myFoodSource.days
                myGrainToAdd = myGrain * myDays * myTotalOffspring
                myGrainTotal = myFoodSourceMapCounter.get(myCropGuid, 0.0) + myGrainToAdd # Use get for safety
                # print("        myGrain = " + str(myGrain))
                # print("        myFodder = " + str(myFodder))
                # print("        myDays = " + str(myDays))
                # print("  previous value of the fodder counter: " + str(myFoodSourceMapCounter.get(myCropGuid, 0.0)))

                myFoodSourceMapCounter[myCropGuid] = myGrainTotal
                # print("  -------> next value of the fodder counter: " + str(myFoodSourceMapCounter.get(myCropGuid, 0.0)))
                # print("Additional MCal counter original Value: " + str(myAdditionalMCalCounter))

                myCrop = LaUtils.getCrop(myCropGuid)
                myFoodValueOfCrop = myCrop.cropCalories * .001
                myFoodValueofFodder = myCrop.fodderValue * .001
                # print("Food Value of the Crop: " + str(myFoodValueOfCrop))
                # print("Food Value of the Fodder: " + str(myFoodValueofFodder))

                myGrainMCal = myGrainToAdd * myFoodValueOfCrop
                myFodderMCal = myFodder * myDays * myFoodValueofFodder * myTotalOffspring
                myAdditionalMCalCounter1 += myFodderMCal
                myAdditionalMCalCounter += myGrainMCal + myFodderMCal
                # print(" myGrainMCal = " + str(myGrainMCal))
                # print(" myFodderMCal = " + str(myFodderMCal))
                # print(" Crop Name: " + str(myCrop.name))
                # print(" value to add grain: " + str(myGrainToAdd))
                # print(" Value now of the fodder counter: " + str(myFoodSourceMapCounter.get(myCropGuid, 0.0)))
                # print(" myFoodSourceMapCounter = " + str(myFoodSourceMapCounter)) # Might print dict representation
                # print("Total MCals counted so far for grain feeding this animal: " + str(myAdditionalMCalCounter))

            # .^.^.^.^.^.^.^.^.^     Insert data into myAnimalCalcsMap    .^.^.^.^.^.^.^.^.^

            myAnimalHerdMCalsRequired1 = myGestatingMCals + myLactatingMCals + myMaintenanceMCals + myAdultMalesMCals + myOffspringMCals
            # print("  ---- AnimalHerd MCals Required before accounting for grain feeding: " + str(myAnimalHerdMCalsRequired1))
            # the next line adjusts for the grain contribution
            myAnimalHerdMCalsRequired = myAnimalHerdMCalsRequired1 - myAdditionalMCalCounter
            # print("  ---- AnimalHerd MCals Required *AFTER* accounting for grain feeding: " + str(myAnimalHerdMCalsRequired))
            myAnimalReport += "myAnimalHerdMCalsRequired1 = " + str(myAnimalHerdMCalsRequired1) + "\n"
            myAnimalReport += "myAnimalHerdMCalsRequired = " + str(myAnimalHerdMCalsRequired) + "\n"
            myAnimalReport += ".........................\n"
            myAnimalReport += ".        Summary        .\n"
            myAnimalReport += ".........................\n"

            myAnimalReport += "MCal Target = " + str(myMCalsFromTheMeat) + "\n"
            myAnimalReport += "Dairy Contribution = " + str(myMCalsUtilizedFromDairy) + "\n"
            myAnimalReport += "Meat Percent = " + str(myMeatPercent * 100.) + "% \n" # Added space before % like C++
            myAnimalReport += "Dairy Percent = " + str(myDairyPercent * 100.) + "% \n" # Added space before % like C++
            myAnimalReport += "Number of Offspring = " + str(myTotalMaleOffspring * 2.) + "\n"
            myAnimalReport += "Number of Mothers = " + str(myTotalMothers) + "\n"
            myAnimalReport += "Number of Breeding Males = " + str(myBreedingMalesRequired) + "\n"

            # myLandValue = myAnimalParameter.ValueCommonGrazingLand(); # Assuming this method/property exists
            # print("the common land grazing value I have is: " + str(myLandValue))
            # print("the Herd MCals are .originally. :" + str(myAnimalHerdMCalsRequired))
            # print("and they are being temporarily stored in the report map slot for area target for further adjustment")
            # myAnimalAreaTarget = myAnimalHerdMCalsRequired / myLandValue # Potential DivisionByZeroError
            # print("but at this point we would need " + str(myAnimalAreaTarget) + " Ha of Land")

            # Create tuple directly
            myReportAndAreaTarget = (myAnimalReport, myAnimalHerdMCalsRequired)
            myAnimalCalcsReportMap[myAnimalGuid] = myReportAndAreaTarget
            myAnimalsMap[myAnimalGuid] = myAnimalHerdMCalsRequired # Direct port of C++: inserting into local myAnimalsMap
            theModel.mValueMap[myAnimalGuid] = myAnimalHerdMCalsRequired # Direct port of C++: inserting into member mValueMap

            # Store MCal requirement for fallow calculation (use local map)
            myAnimalsMapForFallow = {} # Equivalent to C++ myAnimalsMapForFallow
            myAnimalsMapForFallow[myAnimalGuid] = myAnimalHerdMCalsRequired # Store final req

            # Store report and MCal requirement (for display/later use)
            myAnimalCalcsReportMap[myAnimalGuid] = (myAnimalReport, myAnimalHerdMCalsRequired) # Store report and req

            # Update the model's value map directly - needed for fallow allocation logic
            # This assumes the fallow allocation functions below will read from model.mValueMap
            theModel.mValueMap[myAnimalGuid] = myAnimalHerdMCalsRequired
        # done looping through the animals here

        # ----------- Dairy Portion to be calculated ------------
        # ------ the check should be: SUM(B11..B15) == 1.0 ------

        # limit the dairy.  if no limit the limit is 100 percent
        myDairyLimit: float = myDairyLimitPercent if myLimitDairyBool else 1.0
        myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
        myWildMeatPortion = (1.0 - theModel.meatPercent / 100.0)
        myWildMeatPercent = myWildMeatPortion * (theModel.dietPercent / 100.0)
        myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0
        myNewLimit = max(0.0, 1.0 - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit # This was `min` before, double check C++ logic for B17/B18
        myPotentialDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0
        myPotentialDairyLessThanLimitBool = myPotentialDairyPercent < myDairyLimit
        myNewDairy = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual
        myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0




        myDairyLimit: float = myDairyLimitPercent if myLimitDairyBool else 1.0
        myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
        myWildMeatPercent = myWildMeatPortion * theModel.mDietPercent
        myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0
        myNewLimit = max(0.0, 1.0 - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit
        myPotentialDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0
        myPotentialDairyLessThanLimitBool = myPotentialDairyPercent < myDairyLimit
        # B18: Calculate final dairy MCals. Use potential if below initial limit, else use adjusted limit.
        myNewDairy = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual
        myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0

        # --- To get the final Crops and Wild Plants percent, we need to get the overall Meat and Dairy First ---
        myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent
        myOverallPlantPercent = 1.0 - myOverallMeatPercent - myOverallDairyPercent
        myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion
        myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myDomesticCropPortion)

        # Calculate MCals for different components
        myOverallDomesticMeatMCals = myTameMeatMCalorieCounter
        myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual
        myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual
        myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
        myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual
        myOverallMeatMCals = myOverallWildMeatMCals + myOverallDomesticMeatMCals
        myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
        myOverallDairySurplusMCals = max(0.0, myFirstDairySurplusBool)
        myMCalsFromFallowCounter = 0.0

        # myCropReport = f"myOverallPlantPercent = {myOverallPlantPercent}\n"
        # myCropReport += f"myDomesticCropPortion = {myDomesticCropPortion}\n"
        # myCropReport += f"myOverallCropPercent = {myOverallCropPercent}\n"
        # myCropReport += f"myOverallMeatPercent = {myOverallMeatPercent}\n"
        # myCropReport += f"myOverallDairyPercent = {myOverallDairyPercent}\n"
        # myCropReport += "----- = \n" # + str(HOLDER) + "\n"


        # now that we have dairy contributions calculated we can calculate targets for crops
        mySelectedCropsMap: Dict[str, str] = theModel.mCropsMap # Assuming mCropsMap holds CropGuid -> CropParameterGuid

        # Iterate through the selected crops
        for myCropGuid, myCropParameterGuid in mySelectedCropsMap.items():
            # print("        **--------------------------------------------**        ")
            # print("**********         Looping through the crops          **********")
            # print("        **--------------------------------------------**        ")

            myCrop = LaUtils.getCrop(myCropGuid)
            myCropParameter = LaUtils.getCropParameter(myCropParameterGuid)

            # Ensure crop and parameter objects were found
            if not myCrop or not myCropParameter:
                print(f"Warning: Could not find Crop or CropParameter for GUID {myCropGuid}")
                continue

            myCropPortion = myCropParameter.percentTameCrop * .01
            # print(f"          myCropPortion = {myCropPortion}")
            myCropFoodValue = myCrop.cropCalories * .001
            # print(f"          myCropFoodValue = {myCropFoodValue}")
            # Note: C++ code comments out multiplication by myOverallPlantPercent
            myCropPercent = myCropPortion * myOverallCropPercent
            # print(f"          myOverallCropPercent = {myOverallCropPercent}")
            # print(f"          myCropPercent = {myCropPercent}")
            myMCalsFromTheCrop = myCropPercent * myMCalsSettlementAnnual

            myKgForPeople1 = myMCalsFromTheCrop / myCropFoodValue # Potential DivisionByZeroError
            myAnimalKgAdd1 = myFoodSourceMapCounter.get(myCropGuid, 0.0) # Use .get for safety

            # adjust for spoilage and reseeding here
            mySpoilagePercent = myCropParameter.spoilage * .01
            myReseedPercent = myCropParameter.reseed * .01

            myKgForPeopleReseed = (myKgForPeople1 * myReseedPercent)
            myKgForPeopleSpoilage = (myKgForPeople1 * mySpoilagePercent)
            myKgForPeople = myKgForPeopleReseed + myKgForPeopleSpoilage + myKgForPeople1

            myAnimalKgAddReseed = (myAnimalKgAdd1 * myReseedPercent)
            myAnimalKgAddSpoilage = (myAnimalKgAdd1 * mySpoilagePercent)
            myAnimalKgAdd = myAnimalKgAddReseed + myAnimalKgAddSpoilage + myAnimalKgAdd1

            myAdjustedTarget = myKgForPeople + myAnimalKgAdd

            # Check AreaUnits enum - assuming it's defined in la.lib.la
            from la.lib.la import AreaUnits # Make sure AreaUnits is imported
            myCropYield = myCrop.cropYield * 10. if myCrop.areaUnits == AreaUnits.Dunum else myCrop.cropYield
            myCropAreaTargetPeople = myKgForPeople / myCropYield # Potential DivisionByZeroError
            myCropAreaTargetAnimals = myAnimalKgAdd / myCropYield # Potential DivisionByZeroError

            myRatio = myCropParameter.fallowRatio
            myFallowValue = myCropParameter.fallowValue
            myCropAreaTarget1 = myAdjustedTarget / myCropYield # Potential DivisionByZeroError
            myCropAreaTarget = myCropAreaTarget1 * (myRatio + 1.)

            myFallowArea = myRatio * myCropAreaTarget1
            myFallowMCals = myFallowArea * myFallowValue

            myMCalsFromFallowCounter += myFallowMCals

            myCropReport = f"MCals People = {myMCalsFromTheCrop}\n"
            myCropReport += f"myCropPortion = {myCropPortion}\n"
            myCropReport += f"myCropFoodValue = {myCropFoodValue}\n"
            myCropReport += f"myOverallCropPercent = {myOverallCropPercent}\n"
            myCropReport += f"myCropPercent = {myCropPercent}\n"
            myCropReport += f"myMCalsFromTheCrop = {myMCalsFromTheCrop}\n"

            myCropReport += f"myAnimalKgAdd = {myAnimalKgAdd}\n"
            myCropReport += f"myAdjustedTarget = {myAdjustedTarget}\n"
            myCropReport += f"myCrop.cropYield() = {myCrop.cropYield}\n" # Access attribute directly
            myCropReport += f"myCropYield = {myCropYield}\n"

            myCropReport += f"Crop Production People before adjusting= {myKgForPeople1}\n"
            myCropReport += f"Extra Kg to account for spoilage= {myKgForPeopleSpoilage}\n"
            myCropReport += f"Extra Kg to account for reseeding= {myKgForPeopleReseed}\n"
            myCropReport += f"Crop Production People after adjusting= {myKgForPeople}\n"
            myCropReport += f"Crop Production Animal before adjusting= {myAnimalKgAdd1}\n"
            myCropReport += f"Extra Kg to account for spoilage= {myAnimalKgAddSpoilage}\n"
            myCropReport += f"Extra Kg to account for reseeding= {myAnimalKgAddReseed}\n"
            myCropReport += f"Crop Production Animal after adjusting= {myAnimalKgAdd}\n"

            myCropReport += f"myCropAreaTarget People = {myCropAreaTargetPeople}\n"
            myCropReport += f"myCropAreaTarget Animals= {myCropAreaTargetAnimals}\n"

            myCropReport += f"myCropAreaTarget = {myCropAreaTarget}\n"
            myCropReport += "\n"

            myCropReport += f"Kg for People = {myKgForPeople}\n"
            myCropReport += f"KG for Animals = {myAnimalKgAdd}\n"
            myCropReport += f"Percent of Diet = {myCropPercent * 100.}% \n" # Added space before % like C++
            myCropReport += f"Area Target People: {myCropAreaTargetPeople}\n"
            myCropReport += f"Area Target Animal: {myCropAreaTargetAnimals}\n"
            myCropReport += f"Area Target is {myCropAreaTarget}\n"
            myCropReport += f"myFallowValue =  {myFallowValue}\n"

            myCropReport += f"MCals from Fallow: {myFallowMCals}\n"

            # print(f"______ myCropPortion= {myCropPortion}")
            # print(f"______ myCropFoodValue= {myCropFoodValue}")
            # print(f"______ myCropPercent= {myCropPercent}")
            # print(f"______ myMCalsFromTheCrop= {myMCalsFromTheCrop}")
            # print(f"______ myKgForPeople= {myKgForPeople}")
            # print(f"______ myAnimalsKgAdd= {myAnimalKgAdd}") # C++ variable name was myAnimalKgAdd
            # print(f"______ my Area Target: {myCropAreaTarget}")
            # print(f"______ MCals from Fallow = {myFallowMCals}")
            # print(f"______ MCals total from Fallow Counter= {myMCalsFromFallowCounter}")

            # Create tuple directly
            myReportAndAreaTarget = (myCropReport, myCropAreaTarget)

            myCropCalcsReportMap[myCropGuid] = myReportAndAreaTarget
            # Accumulate fallow MCals
            myMCalsFromFallowCounter += myFallowMCals
            # Store crop report and area target
            myCropCalcsReportMap[myCropGuid] = (myCropReport, myCropAreaTarget)

        # --- Fallow Allocation ---
        # --- Fallow Allocation ---
        allocateFallowGrazingLand(theModel, myMCalsFromFallowCounter, myAnimalsMapForFallow)

        # --- Final Animal Report Update ---
        # finally, we have the mcal target for the animal herd, stored in mValueMap !!!!!!!
        # So at this stage all we have to do is polish up the data contained in myAnimalCalcsMap
        #    so that it contains the final area target along with the rest of the calculations to
        #    be sent in the QString portion of the QPair
        # To do this, I will iterate through the report, and transfer the targets from mValueMap
        #    as well as add on to the report

        # Direct port of the C++ iteration and update logic
        # QMapIterator <QString,QPair<QString,float> > myReportIterator(myAnimalCalcsReportMap);
        # while (myReportIterator.hasNext())
        # --- Final Animal Report Update Loop ---
        # Update the animal report map with final area targets based on fallow allocation results stored in model.mValueMap
        # for myAnimalGuid, myPair in myAnimalCalcsReportMap.items():
        for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
            try:
                myReport = str(myAnimalCalcsReportMap[myAnimalGuid][0])
                myFinalMCalTarget: float = theModel.mValueMap.get(myAnimalGuid, 0.0) # Get updated req from model map

                # Calculate Area Target
                # Access common grazing value (already in hectares) from the model
                myLandValueHectares = theModel.commonGrazingValue # This should be the converted value
                if myLandValueHectares <= 0:
                    LaUtils.debug.log(f"Warning: Common Grazing Value ({myLandValueHectares}) is zero or negative for final area calculation for animal {myAnimalGuid}. Setting area target to infinity.", "Warning")
                    myAreaTarget = float('inf')
                else:
                    myAreaTarget = myFinalMCalTarget / myLandValueHectares
            except Exception as e_area:
                LaUtils.debug.log(f"Error calculating final area target for {myAnimalGuid}: {e_area}", "Error")
                myAreaTarget = 0.0 # Default on error

        # Update report string
        myReport += f"Final MCal Target (Post-Fallow) = {myFinalMCalTarget}\n"
        myReport += f"Final Area Target (Hectares) = {myAreaTarget:.2f}\n" # Use float for area

        # Update the map with the modified report and final area target
        myAnimalCalcsReportMap[myAnimalGuid] = (myReport, myAreaTarget)

        # print(f"myFinal Calculations for animals map: \n{myAnimalCalcsReportMap}") # Python dict representation

        # print(f"myDairyLimit = {myDairyLimit}")
        # print(f"myDomesticMeatPercent = {myDomesticMeatPercent}")
        # print(f"myWildMeatPercent = {myWildMeatPercent}")
        # print(f"myLimitSatisfies = {myLimitSatisfies}")
        # print(f"myNewLimit = {myNewLimit}")
        # print(f"myPotentialDairyLessThanLimitBool = {myPotentialDairyLessThanLimitBool}")
        # print(f"myNewDairy = {myNewDairy}")
        # print(f"myOverallDairyPercent = {myOverallDairyPercent}")
        # print(f"myOverallMeatPercent = {myOverallMeatPercent}")
        # print(f"myOverallPlantPercent = {myOverallPlantPercent}")
        # print(f"myOverallCropPercent = {myOverallCropPercent}")
        # print(f"myOverallWildPlantPercent = {myOverallWildPlantPercent}")
        # print(f"myOverallDomesticMeatMCals = {myOverallDomesticMeatMCals}")
        # print(f"myOverallDairyMCals = {myOverallDairyMCals}")
        # print(f"myOverallWildMeatMCals = {myOverallWildMeatMCals}")
        # print(f"myOverallCropsMCals = {myOverallCropsMCals}")
        # print(f"myOverallWildPlantsMCals = {myOverallWildPlantsMCals}")
        # print(f"myOverallMeatMCals = {myOverallMeatMCals}")
        # print(f"myFirstDairySurplusBool = {myFirstDairySurplusBool}")
        # print(f"myOverallDairySurplusMCals = {myOverallDairySurplusMCals}")
        # print("***********************************************************************")
        # print("**                                                                   **")
        # print("**                        Calculating Again                          **")
        # print("**                                                                   **")
        # print("***********************************************************************")

        # ----------- Set the Diet Labels in preparation for return -------------
        myDietLabels.dairyMCalories = myOverallDairyMCals
        myDietLabels.cropMCalories = myOverallCropsMCals
        myDietLabels.animalMCalories = myOverallDomesticMeatMCals # C++ uses myOverallMeatMCals here, but context suggests tame meat
        myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
        myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals
        myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.
        myDietLabels.tameMeatPortionPct = myDomesticMeatPercent * 100.
        myDietLabels.cropsPortionPct = myOverallCropPercent * 100.
        myDietLabels.wildAnimalPortionPct = myWildMeatPercent * 100.
        myDietLabels.wildPlantsPortionPct = myOverallWildPlantPercent * 100.
        myDietLabels.animalPortionPct = myOverallMeatPercent * 100. # Total meat
        myDietLabels.plantsPortionPct = myOverallPlantPercent * 100. # Total plant
        myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0 # Convert back to kCal
        myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
        myDietLabels.dairySurplusMCalories = myOverallDairySurplusMCals

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # -=-=-=-=-=- Setting the report info with area targets -=-=-=-=-=-
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # print("££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("      ££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("££££££££££££££££££££££££££££££££££££")
        # print("£££")
        # print(f" £££    mValueMap = {model.mValueMap}") # Python dict representation
        # print("£££")
        # print("££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("      ££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("££££££££££££££££££££££££££££££££££££")

        # print(f"myFinal Calculations for animals map: \n{myAnimalCalcsReportMap}") # Python dict representation

        # print(f"myDairyLimit = {myDairyLimit}")
        # print(f"myDomesticMeatPercent = {myDomesticMeatPercent}")
        # print(f"myWildMeatPercent = {myWildMeatPercent}")
        # print(f"myLimitSatisfies = {myLimitSatisfies}")
        # print(f"myNewLimit = {myNewLimit}")
        # print(f"myPotentialDairyLessThanLimitBool = {myPotentialDairyLessThanLimitBool}")
        # print(f"myNewDairy = {myNewDairy}")
        # print(f"myOverallDairyPercent = {myOverallDairyPercent}")
        # print(f"myOverallMeatPercent = {myOverallMeatPercent}")
        # print(f"myOverallPlantPercent = {myOverallPlantPercent}")
        # print(f"myOverallCropPercent = {myOverallCropPercent}")
        # print(f"myOverallWildPlantPercent = {myOverallWildPlantPercent}")
        # print(f"myOverallDomesticMeatMCals = {myOverallDomesticMeatMCals}")
        # print(f"myOverallDairyMCals = {myOverallDairyMCals}")
        # print(f"myOverallWildMeatMCals = {myOverallWildMeatMCals}")
        # print(f"myOverallCropsMCals = {myOverallCropsMCals}")
        # print(f"myOverallWildPlantsMCals = {myOverallWildPlantsMCals}")
        # print(f"myOverallMeatMCals = {myOverallMeatMCals}")
        # print(f"myFirstDairySurplusBool = {myFirstDairySurplusBool}")
        # print(f"myOverallDairySurplusMCals = {myOverallDairySurplusMCals}")
        # print("***********************************************************************")
        # print("**                                                                   **")
        # print("**                        Calculating Again                          **")
        # print("**                                                                   **")
        # print("***********************************************************************")

        # ----------- Set the Diet Labels in preparation for return -------------
        myDietLabels.dairyMCalories = myOverallDairyMCals
        myDietLabels.cropMCalories = myOverallCropsMCals
        myDietLabels.animalMCalories = myOverallDomesticMeatMCals # C++ uses myOverallMeatMCals here, but context suggests tame meat
        myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
        myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals
        myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.
        myDietLabels.tameMeatPortionPct = myDomesticMeatPercent * 100.
        myDietLabels.cropsPortionPct = myOverallCropPercent * 100.
        myDietLabels.wildAnimalPortionPct = myWildMeatPercent * 100.
        myDietLabels.wildPlantsPortionPct = myOverallWildPlantPercent * 100.
        myDietLabels.animalPortionPct = myOverallMeatPercent * 100. # Total meat
        myDietLabels.plantsPortionPct = myOverallPlantPercent * 100. # Total plant
        myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0 # Convert back to kCal
        myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
        myDietLabels.dairySurplusMCalories = myOverallDairySurplusMCals

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # -=-=-=-=-=- Setting the report info with area targets -=-=-=-=-=-
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # print("££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("      ££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££££££££££££££££££££")
        # print("££££££££££££££££££££££££££££££££££££")
        # print("£££")
        # print(f" £££    mValueMap = {model.mValueMap}") # Python dict representation
        # print("£££")
        # print("££££££££££££££££££££££££££££££££££££")
        # print("   ££££££££££££££££££
        myLowPriorityCount: float = 0.0
        myHighPriorityValue: float = 0.0
        myMediumPriorityValue: float = 0.0
        myLowPriorityValue: float = 0.0
        # put starting caloric requirements of all used animals floato a map
        # for reduction due to grazing of fallow crop land
        # initialiseValueMap(); # Assumed model.mValueMap is already initialized correctly before this call

        myTotalFallowValue: float = myFallowMCals

        # Count the Animals in each Priority Level and sum their calorie requirements
        # Note: C++ iterates mAnimalsMap (animalGuid -> paramGuid)
        #       High priority uses mValueMap for value summing.
        #       Medium/Low use theAnimalMCalRequirementMap for value summing.
        for myAnimalGuid, myAnimalParameterGuid in theModel.mAnimalsMap.items():
            # myAnimalIterator.next(); # Implicit in Python loop
            # QString myAnimalGuid = myAnimalIterator.key();
            # QString myAnimalParameterGuid = myAnimalIterator.value();
            myAnimal: LaAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)

            # Use match case for the switch statement
            match myAnimalParameter.fallowUsage: # Assuming fallowUsage is an attribute returning Priority enum
                case Priority.High:
                    myHighPriorityCount += 1
                    LaUtils.debug.log(f"Animal: {myAnimal.name}", "Diet")
                    # Use model.mValueMap, mirroring C++ for High priority
                    animal_value = theModel.mValueMap.get(myAnimalGuid, 0.0)
                    LaUtils.debug.log(f"      : {animal_value}", "Diet")
                    myHighPriorityValue += animal_value
                case Priority.Medium:
                    myMediumPriorityCount += 1
                    # Use theAnimalMCalRequirementMap, mirroring C++ for Medium priority
                    animal_value = theAnimalMCalRequirementMap.get(myAnimalGuid, 0.0)
                    myMediumPriorityValue += animal_value
                case Priority.Low:
                    myLowPriorityCount += 1
                    # Use theAnimalMCalRequirementMap, mirroring C++ for Low priority
                    animal_value = theAnimalMCalRequirementMap.get(myAnimalGuid, 0.0)
                    myLowPriorityValue += animal_value
                case Priority.Nope:
                    pass # break; equivalent
                case _: # default: equivalent
                    pass # break; equivalent

        LaUtils.debug.log(f"High Priority Animals: {myHighPriorityCount}", "Diet")
        LaUtils.debug.log(f"Medium Priority Animals: {myMediumPriorityCount}", "Diet")
        LaUtils.debug.log(f"Low Priority Animals: {myLowPriorityCount}", "Diet")

        LaUtils.debug.log(f"High Priority Animal Calorie requirements: {myHighPriorityValue}", "Diet")
        LaUtils.debug.log(f"Medium Priority Animal Calorie requirements: {myMediumPriorityValue}", "Diet")
        LaUtils.debug.log(f"Low Priority Animal Calorie requirements: {myLowPriorityValue}", "Diet")

        LaUtils.debug.log(f"Total Available Fallow Calories before adjustments: {myTotalFallowValue}", "Diet")

        # The following three if statements process all of the animals which
        # utilize fallow cropland as grazing land. It first checks that there
        # is fallow land available, and next allocates the the fallow based on
        # the animals fallow access priority

        # HIGH priority animals get allocated fallow cropland
        if myTotalFallowValue > 0:
            myPriority = Priority.High
            # Call the C++ style doTheFallowAllocation
            myLeftoverCalories = theModel.doTheFallowAllocation(myPriority, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount)
            LaUtils.debug.log(f"Remaining Fallow Calories after HIGH adjustments: {myLeftoverCalories}", "Diet")
            myTotalFallowValue = myLeftoverCalories

        # MEDIUM priority animals get allocated fallow cropland
        if myTotalFallowValue > 0:
            myPriority = Priority.Medium
            # Call the C++ style doTheFallowAllocation
            # C++ BUG?: Passes myHighPriorityCount instead of myMediumPriorityCount. Replicating bug.
            myLeftoverCalories = theModel.doTheFallowAllocation(myPriority, myTotalFallowValue, myMediumPriorityValue, myHighPriorityCount)
            LaUtils.debug.log(f"Remaining Fallow Calories after MED adjustments: {myLeftoverCalories}", "Diet")
            myTotalFallowValue = myLeftoverCalories

        # LOW priority animals get allocated fallow cropland
        if myTotalFallowValue > 0:
            myPriority = Priority.Low
            # Call the C++ style doTheFallowAllocation
            # C++ BUG?: Passes myHighPriorityCount instead of myLowPriorityCount. Replicating bug.
            myLeftoverCalories = theModel.doTheFallowAllocation(myPriority, myTotalFallowValue, myLowPriorityValue, myHighPriorityCount)
            LaUtils.debug.log(f"Remaining Fallow Calories after LOW adjustments: {myLeftoverCalories}", "Diet")
            myTotalFallowValue = myLeftoverCalories

        # float myReturnValue = static_cast<float>(myTotalFallowValue);
        # return myReturnValue; # Python function returns None (void equivalent)
    except Exception as e:
        LaUtils.debug.log(f"Error in doCalcsAnimalsFirstDairySeparate: {str(e)}", "Error")
        import traceback
        LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
        return LaDietLabels()  # Return an empty diet labels object in case of error

    return myDietLabels

























































    # --- Dairy Limit Calculation ---
    # ... (logic as before, using calculated counters and model properties like model.mDietPercent) ...
    myDairyLimit: float = myDairyLimitPercent if myLimitDairyBool else 1.0
    myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0
    myWildMeatPortion = (1.0 - theModel.meatPercent / 100.0) # Assumes model.meatPercent is 0-100
    myWildMeatPercent = myWildMeatPortion * (theModel.dietPercent / 100.0) # Assumes model.dietPercent is 0-100
    myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0
    myNewLimit = max(0.0, 1.0 - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit # This was `min` before, double check C++ logic for B17/B18
    myPotentialDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0
    myPotentialDairyLessThanLimitBool = myPotentialDairyPercent < myDairyLimit
    myNewDairy = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual
    myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0.0

    # --- Final Overall Percentages ---
    myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent
    myOverallPlantPercent = max(0.0, 1.0 - myOverallMeatPercent - myOverallDairyPercent) # Ensure non-negative
    myDomesticCropPortion = theModel.percentOfDietThatIsFromCrops / 100.0 # Assumes model.percent... is 0-100
    myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion
    myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myDomesticCropPortion)

    # --- Crop Loop ---
    mySelectedCropsMap = theModel.mCropsMap
    for myCropGuid, myCropParameterGuid in mySelectedCropsMap.items():
         # ... (entire crop loop logic, ensure 'self.' is changed to 'model.') ...
         # Accumulate fallow MCals
         myMCalsFromFallowCounter += myFallowMCals
         # Store crop report and area target
         myCropCalcsReportMap[myCropGuid] = (myCropReport, myCropAreaTarget)

    # --- Fallow Allocation ---
    # Call the function within this module, passing the model instance
    allocateFallowGrazingLand(theModel, myMCalsFromFallowCounter, myAnimalsMapForFallow)

    # --- Final Animal Report Update Loop ---
    # Update the animal report map with final area targets based on fallow allocation results stored in model.mValueMap
    # for myAnimalGuid, myPair in myAnimalCalcsReportMap.items():
    for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
        myReport: str = myAnimalCalcsReportMap[myAnimalGuid][0]
        myFinalMCalTarget: float = theModel.mValueMap.get(myAnimalGuid, 0.0) # Get updated req from model map

        # Calculate Area Target
        try:
             # Access common grazing value (already in hectares) from the model
             myLandValueHectares = theModel.commonGrazingValue # This should be the converted value
             if myLandValueHectares <= 0:
                  LaUtils.debug.log(f"Warning: Common Grazing Value ({myLandValueHectares}) is zero or negative for final area calculation for animal {myAnimalGuid}. Setting area target to infinity.", "Warning")
                  myAreaTarget = float('inf')
             else:
                  myAreaTarget = myFinalMCalTarget / myLandValueHectares
        except Exception as e_area:
             LaUtils.debug.log(f"Error calculating final area target for {myAnimalGuid}: {e_area}", "Error")
             myAreaTarget = 0.0 # Default on error

        # Update report string
        myReport += f"Final MCal Target (Post-Fallow) = {int(myFinalMCalTarget)}\n"
        myReport += f"Final Area Target (Hectares) = {myAreaTarget:.2f}\n" # Use float for area

        # Update the map with the modified report and final area target
        myAnimalCalcsReportMap[myAnimalGuid] = (myReport, myAreaTarget)

    # --- Set final values on the LaDietLabels object ---
    # ... (set all attributes like myDietLabels.dairyMCalories, etc.) ...
    # Use the calculated overall MCal values and percentages
    myOverallDomesticMeatMCals = myTameMeatMCalorieCounter # Reaffirm this value
    myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual
    myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual
    myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
    myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual
    myOverallDairySurplusMCals = max(0.0, myDairyMCalorieCounter - myOverallDairyMCals)

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

    # Store the final report maps and area target maps
    myDietLabels.mAnimalCalcsReportMap = myAnimalCalcsReportMap
    myDietLabels.mCropCalcsReportMap = myCropCalcsReportMap
    # Extract just the area targets for the specific area target maps
    myDietLabels.mAnimalAreaTargetsMap = {guid: area for guid, (_, area) in myAnimalCalcsReportMap.items()}
    myDietLabels.mCropAreaTargetsMap = {guid: area for guid, (_, area) in myCropCalcsReportMap.items()}


    LaUtils.debug.log(f"doCalcsAnimalsFirstDairySeparate completed", "Diet")
    return myDietLabels
    # --- End of pasted and modified code ---


# --- Fallow Allocation Functions ---

def allocateFallowGrazingLand(model: 'LaModel', theFallowMCalsAvailable: float, theAnimalMCalRequirementMap: Dict[str, float]) -> None:
    # --- Paste the content of LaModel.allocateFallowGrazingLand here ---
    # --- Remember to change 'self.' to 'model.' ---
    # --- And 'self.doTheFallowAllocation(...)' to 'doTheFallowAllocation(model, ...)' ---
    LaUtils.debug.log(f"method ==> allocateFallowGrazingLand(MCals: {theFallowMCalsAvailable})", "Diet")
    myHighPriorityCount: float = 0.0
    myMediumPriorityCount: float = 0.0
    # ... rest of the method logic ...
    if myTotalFallowValue > 0:
        myPriority = Priority.High
        # Call the function in THIS module, passing the model
        myLeftoverCalories = doTheFallowAllocation(model, myPriority, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount)
        LaUtils.debug.log(f"Remaining Fallow Calories after HIGH adjustments: {myLeftoverCalories}", "Diet")
        myTotalFallowValue = myLeftoverCalories
    # ... medium and low priority calls ...

def doTheFallowAllocation(model: 'LaModel', thePriority: Priority, theAvailableFallowValue: float,
                           theTotalNeededByGroup: float, theCountInGroup: float) -> float:
    # --- Paste the content of LaModel.doTheFallowAllocation here ---
    # --- Remember to change 'self.' to 'model.' ---
    # --- Especially 'self.mAnimalsMap' to 'model.mAnimalsMap' ---
    # --- And 'self.mValueMap' to 'model.mValueMap' ---

    from la.lib.lautils import LaUtils
    from la.lib.la import Status, Priority # Ensure Status enum is imported
    from la.lib.laanimal import LaAnimal
    from la.lib.laanimalparameter import LaAnimalParameter

    LaUtils.debug.log(f"method ==> float LaModel::doTheFallowAllocation(Priority {thePriority.name})", "Diet")
    """Allocate fallow land to animals of a specific priority.
        Strict port of C++ version's logic, using the C++ style signature.

    Args:
        thePriority: Priority level being processed
        theAvailableFallowValue: MCals available from fallow land for this group
        theTotalNeededByGroup: Total MCals needed by all animals in this priority group
        theCountInGroup: Number of animals in this priority group (Note: C++ version might pass incorrect count)

    Returns:
        float: Remaining MCals after allocation for this group
    """
    from la.lib.lautils import LaUtils
    from la.lib.la import Status, Priority # Ensure Status enum is imported
    from la.lib.laanimal import LaAnimal
    from la.lib.laanimalparameter import LaAnimalParameter

    LaUtils.debug.log(f"method ==> float LaModel::doTheFallowAllocation(Priority {thePriority.name})", "Diet")
    LaUtils.debug.log(f"Available Fallow: {theAvailableFallowValue}, Total Needed by Group: {theTotalNeededByGroup}", "Diet")

    myFallowDifference: float = theAvailableFallowValue - theTotalNeededByGroup
    myFallowStatus: Status

    if myFallowDifference > 0:
        myFallowStatus = Status.MoreThanEnoughToCompletelySatisfy
    else:
        myFallowStatus = Status.NotEnoughToCompletelySatisfy

    myFallowStatusString = "More than Enough" if myFallowStatus == Status.MoreThanEnoughToCompletelySatisfy else "Not Enough"
    LaUtils.debug.log(f"Fallow Status: {myFallowStatusString}", "Diet")

    myRemainingFallow: float = 0.0

    # Use match case based on the calculated status
    match myFallowStatus:
        case Status.MoreThanEnoughToCompletelySatisfy:
            LaUtils.debug.log("CASE: MoreThanEnoughToCompletelySatisfy", "Diet")
            # Each animal in this group gets its full requirement met by fallow.
            # Reduce their remaining requirement in the main value map (mValueMap).
            # Need to iterate through animals again to find those matching thePriority.
            for myAnimalGuid, myAnimalParameterGuid in model.mAnimalsMap.items():
                myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
                if myAnimalParameter.fallowUsage == thePriority:
                    # Get the animal's individual requirement from mValueMap
                    myIndividualRequirement = model.mValueMap.get(myAnimalGuid, 0.0)
                    if myAnimalGuid in model.mValueMap:
                        # Reduce the value in mValueMap by the full individual requirement
                        # C++ doesn't explicitly check min, but let's prevent negative values
                        myReduction = myIndividualRequirement
                        model.mValueMap[myAnimalGuid] -= myReduction
                        model.mValueMap[myAnimalGuid] = max(0.0, model.mValueMap[myAnimalGuid]) # Ensure non-negative
                        LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement fully met by fallow. Reduced by {myReduction:.2f}. Remaining need: {model.mValueMap[myAnimalGuid]:.2f}", "Diet")
                    else:
                        LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in mValueMap during fallow allocation (MoreThanEnough).", "Warning")

            # Calculate and return the leftover fallow value
            myRemainingFallow = myFallowDifference
            LaUtils.debug.log(f"Remaining Fallow Value after allocation: {myRemainingFallow:.2f}", "Diet")

        case Status.NotEnoughToCompletelySatisfy:
            LaUtils.debug.log("CASE: NotEnoughToCompletelySatisfy", "Diet")
            # Distribute the available fallow proportionally among animals in this group.
            # Need to iterate through animals again.
            for myAnimalGuid, myAnimalParameterGuid in model.mAnimalsMap.items():
                    myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
                    if myAnimalParameter.fallowUsage == thePriority:
                        if myAnimalGuid in model.mValueMap:
                            # Get the animal's individual requirement from mValueMap
                            myIndividualRequirement = model.mValueMap.get(myAnimalGuid, 0.0)

                            # Calculate the proportion of available fallow this animal gets
                            # C++ does not guard division by zero here
                            myProportion = myIndividualRequirement / theTotalNeededByGroup
                            myAllocatedMCals = theAvailableFallowValue * myProportion
                            LaUtils.debug.log(f"  Animal {myAnimalGuid}: Needs {myIndividualRequirement:.2f}, Proportion {myProportion:.4f}, Allocated {myAllocatedMCals:.2f}", "Diet")

                            # Reduce the animal's requirement in the main value map
                            # C++ doesn't explicitly check min, but let's prevent negative values
                            myReduction = myAllocatedMCals
                            model.mValueMap[myAnimalGuid] -= myReduction
                            model.mValueMap[myAnimalGuid] = max(0.0, model.mValueMap[myAnimalGuid]) # Ensure non-negative
                            LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement reduced by {myReduction:.2f}. Remaining need: {model.mValueMap[myAnimalGuid]:.2f}", "Diet")
                        else:
                            LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in mValueMap during fallow allocation (NotEnough).", "Warning")
            # All available fallow has been used
            myRemainingFallow = 0.0
            LaUtils.debug.log(f"All available fallow allocated. Remaining Fallow Value: {myRemainingFallow:.2f}", "Diet")
        case _: # Default case, should not happen with Status enum
            LaUtils.debug.log(f"Unexpected fallow status: {myFallowStatus}", "Error")
            myRemainingFallow = theAvailableFallowValue # Return original value if status is unknown

    return myRemainingFallow

# --- Other Calculation Helpers (if any, e.g., requiredValue could move here too) ---

def requiredValue(model: 'LaModel', theAnimalGuid: str) -> float:
    # --- Paste the content of LaModel.requiredValue here ---
    # --- Remember to change 'self.' to 'model.' ---
    # --- And 'self.logMessage(...)' to 'LaUtils.debug.log(...)' or pass logger ---
    myAnimal = LaUtils.getAnimal(theAnimalGuid)
    # ... rest of calculation ...
    LaUtils.debug.log("method ==> def requiredValue(...)", "CalcDetail")
    # ... rest of logging ...
    return myReturnValue


















def allocateFallowGrazingLand(theModel: 'LaModel', theFallowMCalsAvailable: float, theAnimalMCalRequirementMap: Dict[str, float]) -> None:
    """
    Allocate fallow land for grazing to animals based on their priority and requirements.

    This method distributes available fallow land MCals to animals based on their priorities:
        1. High priority animals get first access to fallow grazing
        2. Medium priority animals get second access
        3. Low priority animals get third access

    Args:
        theFallowMCalsAvailable (float): Total MCals available from fallow land
        theAnimalMCalRequirementMap (Dict[str, float]): Dictionary mapping animal GUIDs to their MCal requirements
    """
    from la.lib.lautils import LaUtils
    from la.lib.la import Priority, Status
    from la.lib.laanimal import LaAnimal
    from la.lib.laanimalparameter import LaAnimalParameter

    LaUtils.debug.log(f"method ==> allocateFallowGrazingLand(MCals: {theFallowMCalsAvailable})", "Diet")
    myHighPriorityCount: float = 0.0
    myMediumPriorityCount: float = 0.0
    myLowPriorityCount: float = 0.0
    myHighPriorityValue: float = 0.0
    myMediumPriorityValue: float = 0.0
    myLowPriorityValue: float = 0.0

    myTotalFallowValue: float = theFallowMCalsAvailable

    # Count the Animals in each Priority Level and sum their calorie requirements
    for myAnimalGuid, myMCalRequirement in theAnimalMCalRequirementMap.items():
        myAnimal: LaAnimal = LaUtils.getAnimal(myAnimalGuid)

        # Get the animal parameter GUID from the animals map
        myAnimalParameterGuid = theModel.mAnimalsMap.get(myAnimalGuid, "")
        if not myAnimalParameterGuid:
            LaUtils.debug.log(f"No parameter found for animal {myAnimalGuid}", "Warning")
            continue

        myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)

        # Match the animal's fallow usage priority
        match myAnimalParameter.fallowUsage:
            case Priority.High:
                myHighPriorityCount += 1
                myHighPriorityValue += myMCalRequirement
            case Priority.Medium:
                myMediumPriorityCount += 1
                myMediumPriorityValue += myMCalRequirement
            case Priority.Low:
                myLowPriorityCount += 1
                myLowPriorityValue += myMCalRequirement
            case _:
                pass  # Ignore other cases

    LaUtils.debug.log(f"High Priority Animals: {myHighPriorityCount}", "Diet")
    LaUtils.debug.log(f"Medium Priority Animals: {myMediumPriorityCount}", "Diet")
    LaUtils.debug.log(f"Low Priority Animals: {myLowPriorityCount}", "Diet")

    LaUtils.debug.log(f"High Priority Animal Calorie requirements: {myHighPriorityValue}", "Diet")
    LaUtils.debug.log(f"Medium Priority Animal Calorie requirements: {myMediumPriorityValue}", "Diet")
    LaUtils.debug.log(f"Low Priority Animal Calorie requirements: {myLowPriorityValue}", "Diet")

    LaUtils.debug.log(f"Total Available Fallow Calories before adjustments: {myTotalFallowValue}", "Diet")

    # Process animals in priority order (High -> Medium -> Low)

    # HIGH priority animals get allocated fallow cropland
    if myTotalFallowValue > 0:
        myPriority = Priority.High
        # Call the function in THIS module, passing the model
        myLeftoverCalories = doTheFallowAllocation(theModel, myPriority, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount)
        LaUtils.debug.log(f"Remaining Fallow Calories after HIGH adjustments: {myLeftoverCalories}", "Diet")
        myTotalFallowValue = myLeftoverCalories

    # MEDIUM priority animals get allocated fallow cropland
    if myTotalFallowValue > 0:
        myPriority = Priority.Medium
        myLeftoverCalories = doTheFallowAllocation(theModel, myPriority, myTotalFallowValue, myMediumPriorityValue, myMediumPriorityCount)
        LaUtils.debug.log(f"Remaining Fallow Calories after MEDIUM adjustments: {myLeftoverCalories}", "Diet")
        myTotalFallowValue = myLeftoverCalories

    # LOW priority animals get allocated fallow cropland
    if myTotalFallowValue > 0:
        myPriority = Priority.Low
        myLeftoverCalories = doTheFallowAllocation(theModel, myPriority, myTotalFallowValue, myLowPriorityValue, myLowPriorityCount)
        LaUtils.debug.log(f"Remaining Fallow Calories after LOW adjustments: {myLeftoverCalories}", "Diet")
        myTotalFallowValue = myLeftoverCalories

    LaUtils.debug.log(f"Final Remaining Fallow Calories: {myTotalFallowValue}", "Diet")

    # The doTheFallowAllocation method is responsible for updating the mValueMap with
    # the reduced MCal requirements after allocation



