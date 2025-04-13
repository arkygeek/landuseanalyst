from qgis.PyQt.QtCore import pyqtSignal, pyqtProperty, QObject # Ensure QObject is imported if not already
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging # Keep standard logging
from typing import Dict, List, Tuple, Union

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType
from la.lib.la import LaFoodSourceMap, LaReportMap, LaFoodSource, LandFound, LandBeingGrazed, LaTripleMap
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lafoodsource import LaFoodSource

MESSAGE_BUS: LaMessageBus = LaMessageBus()

class LaModel(QDialog, LaSerialisable, LaGuid):
    """
    LaModel class represents the main model for the Landuse Analyst plugin.

    Attributes:
        animalsChanged (pyqtSignal): Signal emitted when the animals change.
        areaUnitsChanged (pyqtSignal): Signal emitted when the area units change.
        baseOnPlantsChanged (pyqtSignal): Signal emitted when the base on plants changes.
        caloriesPerPersonDailyChanged (pyqtSignal): Signal emitted when the calories per person daily changes.
        commonLandAreaUnitsChanged (pyqtSignal): Signal emitted when the common land area units changes.
        commonLandValueChanged (pyqtSignal): Signal emitted when the common land value changes.
        specificLandAreaUnitsChanged (pyqtSignal): Signal emitted when the specific land area units changes. # Added attribute doc
        specificLandEnergyTypeChanged (pyqtSignal): Signal emitted when the specific land energy type changes. # Added attribute doc
        cropsChanged (pyqtSignal): Signal emitted when the crops change.
        dairyUtilisationChanged (pyqtSignal): Signal emitted when the dairy utilisation changes.
        descriptionChanged (pyqtSignal): Signal emitted when the description changes.
        dietLabelsChanged (pyqtSignal): Signal emitted when the diet labels change.
        dietPercentChanged (pyqtSignal): Signal emitted when the diet percent changes.
        dietsChanged (pyqtSignal): Signal emitted when the diets change.
        eastingChanged (pyqtSignal): Signal emitted when the easting changes.
        euclideanDistanceChanged (pyqtSignal): Signal emitted when the euclidean distance changes.
        fallowRatioChanged (pyqtSignal): Signal emitted when the fallow ratio changes.
        fallowStatusChanged (pyqtSignal): Signal emitted when the fallow status changes.
        guidChanged (pyqtSignal): Signal emitted when the GUID changes.
        herdSizeChanged (pyqtSignal): Signal emitted when the herd size changes.
        iconChanged (pyqtSignal): Signal emitted when the icon changes.
        includeDairyChanged (pyqtSignal): Signal emitted when the include dairy changes.
        landBeingGrazedChanged (pyqtSignal): Signal emitted when the land being grazed changes.
        landFoundChanged (pyqtSignal): Signal emitted when the land found changes.
        limitDairyChanged (pyqtSignal): Signal emitted when the limit dairy changes.
        limitDairyPercentChanged (pyqtSignal): Signal emitted when the limit dairy percent changes.
        meatPercentChanged (pyqtSignal): Signal emitted when the meat percent changes.
        nameChanged (pyqtSignal): Signal emitted when the name changes.
        northingChanged (pyqtSignal): Signal emitted when the northing changes.
        pathDistanceChanged (pyqtSignal): Signal emitted when the path distance changes.
        percentOfDietThatIsFromCropsChanged (pyqtSignal): Signal emitted when the percent of diet from crops changes.
        periodChanged (pyqtSignal): Signal emitted when the period changes.
        populationChanged (pyqtSignal): Signal emitted when the population changes.
        precisionChanged (pyqtSignal): Signal emitted when the precision changes.
        priorityChanged (pyqtSignal): Signal emitted when the priority changes.
        projectionChanged (pyqtSignal): Signal emitted when the projection changes.
        statusChanged (pyqtSignal): Signal emitted when the status changes.
        walkingTimeChanged (pyqtSignal): Signal emitted when the walking time changes.
    """
    _animalsChanged = pyqtSignal()
    _areaUnitsChanged = pyqtSignal()
    _baseOnPlantsChanged = pyqtSignal()
    _caloriesPerPersonDailyChanged = pyqtSignal()
    _commonLandAreaUnitsChanged = pyqtSignal()
    _commonLandValueChanged = pyqtSignal()
    _specificLandAreaUnitsChanged = pyqtSignal() # Added signal
    _specificLandEnergyTypeChanged = pyqtSignal() # Added signal
    _cropsChanged = pyqtSignal()
    _dairyUtilisationChanged = pyqtSignal()
    _descriptionChanged = pyqtSignal()
    _dietLabelsChanged = pyqtSignal()
    _dietPercentChanged = pyqtSignal()
    _dietsChanged = pyqtSignal()
    _eastingChanged = pyqtSignal()
    _euclideanDistanceChanged = pyqtSignal()
    _fallowRatioChanged = pyqtSignal()
    _fallowStatusChanged = pyqtSignal()
    _guidChanged = pyqtSignal()
    _herdSizeChanged = pyqtSignal()
    _iconChanged = pyqtSignal()
    _includeDairyChanged = pyqtSignal()
    _landBeingGrazedChanged = pyqtSignal()
    _commonLandValueChanged = pyqtSignal()
    _commonGrazingValueChanged = pyqtSignal()
    _landFoundChanged = pyqtSignal()
    _limitDairyChanged = pyqtSignal()
    _limitDairyPercentChanged = pyqtSignal()
    _meatPercentChanged = pyqtSignal()
    _nameChanged = pyqtSignal()
    _northingChanged = pyqtSignal()
    _pathDistanceChanged = pyqtSignal()
    _percentOfDietThatIsFromCropsChanged = pyqtSignal()
    _periodChanged = pyqtSignal()
    _populationChanged = pyqtSignal()
    _precisionChanged = pyqtSignal()
    _priorityChanged = pyqtSignal()
    _projectionChanged = pyqtSignal()
    _statusChanged = pyqtSignal()
    _walkingTimeChanged = pyqtSignal()

    # Add a new signal for logging calculation steps to the UI
    logCalculationStep = pyqtSignal(str)

    def __init__(self, parent=None):
        # Call constructors of all base classes
        QDialog.__init__(self, parent)
        LaSerialisable.__init__(self) # Assuming LaSerialisable might have its own init logic
        LaGuid.__init__(self) # Explicitly call LaGuid constructor to initialize _mGuid

        self.mTotalLandNeeded = 0

        # Initialize LaSerialisable (maintains backward compatibility)
        # Check the underlying _mGuid attribute directly to avoid property/method confusion
        if not self._mGuid:
            self.setGuid() # Generate a new GUID if one wasn't set


        # Model properties
        self.mName = ""
        self.mPopulation = 100

        # Added missing fields that are used in property getters/setters
        self.mPeriod = "No Period Set"
        self.mProjection = 0
        self.mEasting = 0
        self.mNorthing = 0
        self.mEuclideanDistance = False
        self.mWalkingTime = False
        self.mPathDistance = False
        self.mPrecision = 5
        self.mDietPercent = 25
        self.mPercentOfDietThatIsFromCrops = 10
        self.mMeatPercent = 10
        self.mCommonLandValue = 0.0
        self.mCommonGrazingValue = 0.0
        self.mCommonLandAreaUnits: AreaUnits = AreaUnits.Hectare
        self.mSpecificLandAreaUnits = 0
        self.mSpecificLandEnergyType = 0
        self.mHerdSize = 0
        self.mFallowStatus: Status = Status.NotEnoughToCompletelySatisfy
        self.mFallowRatio = 1
        self.mDescription = ""
        self.mAreaUnits = 0
        self.mStatus = 0
        self.mLandBeingGrazed = 0
        self.mLandFound = 0
        self.mPriority = 0

        # Value map for fallow land calculations
        self.mValueMap = {} # Corresponds to mValueMap in C++

        # Diet calculation properties
        self.mAnimalsMap: dict[str, str] = {} # Corresponds to mAnimalsMap in C++
        self.mCropsMap: dict[str, float] = {} # Corresponds to mCropsMap in C++
        self.mBaseOnPlants = False
        self.mIncludeDairy = True
        self.mLimitDairy = True
        self.mLimitDairyPercentage = 10 # Corresponds to mLimitDairyPercentage in C++
        self.mCaloriesPerPersonDaily = 2500
        self.mDairyUtilisation = 100

        # Initialize maps corresponding to C++ private members
        self.mCaloriesProvidedByMeatMap = {}
        self.mCaloriesProvidedByMilkMap = {}
        self.mCaloriesProvidedByCropsMap = {}
        self.mProductionRequiredAnimalsMap = {}
        self.mProductionRequiredCropsMap = {}
        self.mAreaTargetsAnimalsMap = {}
        self.mAreaTargetsCropsMap = {}
        self.mFodderMap: dict[str, Dict[str, LaFoodSource]] = {}
        self.mCalcsAnimalsMap: dict[str, str] = {} # Corresponds to mAnimalCalcReport? Or mCalcsAnimalsMap? Assuming the latter.
        self.mCalcsCropsMap: dict[str, str] = {}

        # Store calculation results
        self.mDietLabels = LaDietLabels()

        # Use MESSAGE_BUS for logging instead of QgsMessageLog
        self.mLogger = MESSAGE_BUS


    def logMessage(self, theMessage: str):
        """
        Logs a message using the MESSAGE_BUS.

        Args:
            message (str): The message to log.
        """
        # Emit the message through MESSAGE_BUS with "Model" as the component type
        self.mLogger.debugMessaged.emit(f"Model: {theMessage}")


    def __del__(self):
        pass


    def __copy__(self):
        myModel: LaModel = LaModel()
        myModel.name = self.name

        return LaModel(self)


    def __deepcopy__(self, memo):
        return LaModel(self)


    @pyqtProperty(str, notify=_nameChanged)
    def name(self) -> str: # type: ignore
        return self.mName
    @name.setter
    def name(self, theName: str):
        if self.mName != theName:
            self.mName = theName
            self._nameChanged.emit()


    @pyqtProperty(int, notify=_populationChanged)
    def population(self) -> int: # type: ignore
        return int(self.mPopulation)
    @population.setter
    def population(self, thePopulation: int):
        if self.mPopulation != thePopulation:
            self.mPopulation = thePopulation
            self._populationChanged.emit()


    @pyqtProperty(str, notify=_periodChanged)
    def period(self) -> str: # type: ignore
        return str(self.mPeriod)
    @period.setter
    def period(self, thePeriod: str):
        if self.mPeriod != thePeriod:
            self.mPeriod = thePeriod
            self._periodChanged.emit()


    @pyqtProperty(int, notify=_projectionChanged)
    def projection(self) -> int: # type: ignore
        return int(str(self.mProjection))
    @projection.setter
    def projection(self, theProjection: int):
        if self.mProjection != theProjection:
            self.mProjection = theProjection
            self._projectionChanged.emit()


    @pyqtProperty(int, notify=_precisionChanged)
    def precision(self) -> int: # type: ignore
        return int(str(self.mPrecision))
    @precision.setter
    def precision(self, thePrecision: int):
        if self.mPrecision != thePrecision:
            self.mPrecision = thePrecision
            self._precisionChanged.emit()


    @pyqtProperty(int, notify=_dietPercentChanged)
    def dietPercent(self) -> int: # type: ignore
        return int(self.mDietPercent)
    @dietPercent.setter
    def dietPercent(self, theDietPercent: int):
        if self.mDietPercent != theDietPercent:
            self.mDietPercent = theDietPercent
            self._dietPercentChanged.emit()


    @pyqtProperty(int, notify=_percentOfDietThatIsFromCropsChanged)
    def percentOfDietThatIsFromCrops(self) -> int: # type: ignore
        return int(self.mPercentOfDietThatIsFromCrops)
    @percentOfDietThatIsFromCrops.setter
    def percentOfDietThatIsFromCrops(self, thePercent: int):
        if self.mPercentOfDietThatIsFromCrops != thePercent:
            self.mPercentOfDietThatIsFromCrops = thePercent
            self._percentOfDietThatIsFromCropsChanged.emit()


    @pyqtProperty(int, notify=_meatPercentChanged)
    def meatPercent(self) -> int: # type: ignore
        return int(self.mMeatPercent)
    @meatPercent.setter
    def meatPercent(self, theMeatPercent: int):
        if self.mMeatPercent != theMeatPercent:
            self.mMeatPercent = theMeatPercent
            self._meatPercentChanged.emit()


    @pyqtProperty(int, notify=_caloriesPerPersonDailyChanged)
    def caloriesPerPersonDaily(self) -> int: # type: ignore
        return self.mCaloriesPerPersonDaily
    @caloriesPerPersonDaily.setter
    def caloriesPerPersonDaily(self, theCaloriesPerPersonDaily: int):
        if self.mCaloriesPerPersonDaily != theCaloriesPerPersonDaily:
            self.mCaloriesPerPersonDaily = theCaloriesPerPersonDaily
            self._caloriesPerPersonDailyChanged.emit()


    @pyqtProperty(int, notify=_dairyUtilisationChanged)
    def dairyUtilisation(self) -> int: # type: ignore
        return self.mDairyUtilisation
    @dairyUtilisation.setter
    def dairyUtilisation(self, thePercent: Union[int, float, str]): # Allow string input
        try:
            numeric_value = 0
            if isinstance(thePercent, str):
                cleaned_value = thePercent.replace('%', '').strip()
                numeric_value = int(float(cleaned_value))
            else:
                numeric_value = int(thePercent)

            # Ensure the value is within a reasonable range if needed
            # numeric_value = max(0, min(100, numeric_value))

            if self.mDairyUtilisation != numeric_value:
                self.mDairyUtilisation = numeric_value
                self._dairyUtilisationChanged.emit()
        except (ValueError, TypeError) as e:
            # self.logCalculationStep(f"Failed to set dairyUtilisation with value '{thePercent}': {e}")
            LaUtils.debug.log(f"Error details: Failed to set dairyUtilisation with value '{thePercent}': {e}", "Error")

    @pyqtProperty(bool, notify=_baseOnPlantsChanged)
    def baseOnPlants(self) -> bool: # type: ignore
        return self.mBaseOnPlants
        """ Hint on usage to read and set the checkbox state
            # When reading from checkbox
            self._baseOnPlants = self.cboxBaseOnPlants.isChecked()
            # When setting checkbox state
            self.cboxBaseOnPlants.setChecked(self._baseOnPlants) """
    @baseOnPlants.setter
    def baseOnPlants(self, theBool: bool):
        if self.mBaseOnPlants != theBool:
            self.mBaseOnPlants = theBool
            self._baseOnPlantsChanged.emit()


    @pyqtProperty(bool, notify=_includeDairyChanged)
    def includeDairy(self) -> bool: # type: ignore
        return self.mIncludeDairy
    @includeDairy.setter
    def includeDairy(self, theBool: bool):
        if self.mIncludeDairy != theBool:
            self.mIncludeDairy = theBool
            self._includeDairyChanged.emit()


    @pyqtProperty(bool, notify=_limitDairyChanged)
    def limitDairy(self) -> bool: # type: ignore
        return self.mLimitDairy
    @limitDairy.setter
    def limitDairy(self, theBool: bool):
        if self.mLimitDairy != theBool:
            self.mLimitDairy = theBool
            self._limitDairyChanged.emit()


    @pyqtProperty(int, notify=_limitDairyPercentChanged)
    def limitDairyPercent(self) -> int: # type: ignore
        return self.mLimitDairyPercentage
    @limitDairyPercent.setter
    def limitDairyPercent(self, thePercent: int):
        # Ensure the value is within a reasonable range if needed
        # thePercent = max(0, min(100, thePercent))
        if self.mLimitDairyPercentage != thePercent:
            self.mLimitDairyPercentage = thePercent
            self._limitDairyPercentChanged.emit()


    @pyqtProperty(Status, notify=_fallowStatusChanged) # TODO: set this to the correct return type
    def fallowStatus(self) -> Status: # type: ignore
        return (self.mFallowStatus)
    @fallowStatus.setter
    def fallowStatus(self, theStatus: Status):
        if self.mFallowStatus != theStatus:
            self.mFallowStatus = theStatus
            self._fallowStatusChanged.emit()



    @pyqtProperty(int, notify=_fallowRatioChanged)
    def fallowRatio(self) -> int: # type: ignore
        return int(str(self.mFallowRatio))
    @fallowRatio.setter
    def fallowRatio(self, theRatio: int):
        if self.mFallowRatio != theRatio:
            self.mFallowRatio = theRatio
            self._fallowRatioChanged.emit()


    @pyqtProperty(int, notify=_eastingChanged)
    def easting(self) -> int: # type: ignore
        return int(str(self.mEasting))
    @easting.setter
    def easting(self, theEasting: int):
        if self.mEasting != theEasting:
            self.mEasting = theEasting
            self._eastingChanged.emit()


    @pyqtProperty(int, notify=_northingChanged)
    def northing(self) -> int: # type: ignore
        return int(str(self.mNorthing))
    @northing.setter
    def northing(self, theNorthing: int):
        if self.mNorthing != theNorthing:
            self.mNorthing = theNorthing
            self._northingChanged.emit()


    @pyqtProperty(bool, notify=_euclideanDistanceChanged)
    def euclideanDistance(self) -> bool: # type: ignore
        return bool(self.mEuclideanDistance)
    @euclideanDistance.setter
    def euclideanDistance(self, theBool: bool):
        if self.mEuclideanDistance != theBool:
            self.mEuclideanDistance = theBool
            self._euclideanDistanceChanged.emit()


    @pyqtProperty(bool, notify=_walkingTimeChanged)
    def walkingTime(self) -> bool: # type: ignore
        return bool(self.mWalkingTime)
    @walkingTime.setter
    def walkingTime(self, theBool: bool):
        if self.mWalkingTime != theBool:
            self.mWalkingTime = theBool
            self._walkingTimeChanged.emit()


    @pyqtProperty(bool, notify=_pathDistanceChanged)
    def pathDistance(self) -> bool: # type: ignore
        return bool(self.mPathDistance)
    @pathDistance.setter
    def pathDistance(self, theBool: bool):
        if self.mPathDistance != theBool:
            self.mPathDistance = theBool
            self._pathDistanceChanged.emit()


    @pyqtProperty(float, notify=_commonLandValueChanged)
    def commonLandValue(self) -> float: # type: ignore
        return float(str(self.mCommonLandValue))
    @commonLandValue.setter
    def commonLandValue(self, theValue: float):
        if self.mCommonLandValue != theValue:
            self.mCommonLandValue = theValue
            self._commonLandValueChanged.emit()

    @pyqtProperty(float, notify=_commonGrazingValueChanged)
    def commonGrazingValue(self) -> float: # type: ignore
        return float(str(self.mCommonGrazingValue))
    @commonGrazingValue.setter
    def commonGrazingValue(self, theValue: float):
        if self.mCommonGrazingValue != theValue:
            self.mCommonGrazingValue = theValue
            self._commonGrazingValueChanged.emit()


    @pyqtProperty(AreaUnits, notify=_commonLandAreaUnitsChanged)
    def commonLandAreaUnits(self) -> AreaUnits: # type: ignore
        return self.mCommonLandAreaUnits # TODO: figure out how to do this
    @commonLandAreaUnits.setter
    def commonLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self.mCommonLandAreaUnits != theAreaUnits:
            self.mCommonLandAreaUnits: AreaUnits = theAreaUnits
            self._commonLandAreaUnitsChanged.emit()


    @pyqtProperty(AreaUnits, notify=_specificLandAreaUnitsChanged) # Added property
    def specificLandAreaUnits(self) -> AreaUnits: # type: ignore
        return self.mSpecificLandAreaUnits
    @specificLandAreaUnits.setter
    def specificLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self.mSpecificLandAreaUnits != theAreaUnits:
            self.mSpecificLandAreaUnits = theAreaUnits
            self._specificLandAreaUnitsChanged.emit()


    @pyqtProperty(EnergyType, notify=_specificLandEnergyTypeChanged) # Added property
    def specificLandEnergyType(self) -> EnergyType: # type: ignore
        return self.mSpecificLandEnergyType
    @specificLandEnergyType.setter
    def specificLandEnergyType(self, theEnergyType: EnergyType):
        if self.mSpecificLandEnergyType != theEnergyType:
            self.mSpecificLandEnergyType = theEnergyType
            self._specificLandEnergyTypeChanged.emit()


    @pyqtProperty(int, notify=_herdSizeChanged)
    def herdSize(self) -> int: # type: ignore
        return int(str(self.mHerdSize))
    @herdSize.setter
    def herdSize(self, theAnimalGuid: str):
        if self.mHerdSize != theAnimalGuid:
            self.mHerdSize = theAnimalGuid
            self._herdSizeChanged.emit()


    @pyqtProperty(str, notify=_animalsChanged) # TODO: check this I think Dict type might be wrong
    def animals(self) -> Dict[str, str]: # type: ignore
        return self.mAnimalsMap
    @animals.setter
    def animals(self, theAnimals: Dict[str, str]):
        if self.mAnimalsMap != theAnimals:
            self.mAnimalsMap = theAnimals
            self._animalsChanged.emit()


    @pyqtProperty(str, notify=_cropsChanged) # TODO: check this to see if it is correct
    def crops(self) -> Dict[str, str]: # type: ignore
        return self.mCropsMap
    @crops.setter
    def crops(self, theCrops: Dict[str, str]):
        if self.mCropsMap != theCrops:
            self.mCropsMap = theCrops
            self._cropsChanged.emit()


    @pyqtProperty(str, notify=_dietsChanged) # TODO: check this to see if it is correct
    def diets(self) -> Dict[str, LaDietLabels]: # type: ignore
        return self.mDiets
    @diets.setter
    def diets(self, theDiets: Dict[str, LaDietLabels]):
        if self.mDiets != theDiets:
            self.mDiets = theDiets
            self._dietsChanged.emit()


    @pyqtProperty(str, notify=_dietLabelsChanged) # TODO: check this to see if it is correct
    def dietLabels(self) -> List[LaDietLabels]: # type: ignore
        return self.mDietLabels
    @dietLabels.setter
    def dietLabels(self, theDietLabels: List[LaDietLabels]):
        if self.mDietLabels != theDietLabels:
            self.mDietLabels = theDietLabels
            self._dietLabelsChanged.emit()


    @pyqtProperty(str, notify=_landBeingGrazedChanged) # TODO: check this to see if it is correct
    def landBeingGrazed(self) -> LandBeingGrazed: # type: ignore
        return self.mLandBeingGrazed
    @landBeingGrazed.setter
    def landBeingGrazed(self, theLandBeingGrazed: LandBeingGrazed):
        if self.mLandBeingGrazed != theLandBeingGrazed:
            self.mLandBeingGrazed = theLandBeingGrazed
            self._landBeingGrazedChanged.emit()


    @pyqtProperty(str, notify=_landFoundChanged)
    def landFound(self) -> LandFound: # type: ignore
        return self.mLandFound
    @landFound.setter
    def landFound(self, theLandFound: LandFound):
        if self.mLandFound != theLandFound:
            self.mLandFound = theLandFound
            self._landFoundChanged.emit()


    @pyqtProperty(str, notify=_priorityChanged)
    def priority(self) -> Priority: # type: ignore
        return self.mPriority
    @priority.setter
    def priority(self, thePriority: Priority):
        if self.mPriority != thePriority:
            self.mPriority = thePriority
            self._priorityChanged.emit()


    @pyqtProperty(str, notify=_descriptionChanged)
    def description(self) -> str: # type: ignore
        return self.mDescription
    @description.setter
    def description(self, theDescription: str):
        if self.mDescription != theDescription:
            self.mDescription = theDescription
            self._descriptionChanged.emit()


    @pyqtProperty(str, notify=_areaUnitsChanged)
    def areaUnits(self) -> AreaUnits: # type: ignore
        return self.mAreaUnits
    @areaUnits.setter
    def areaUnits(self, theAreaUnits: AreaUnits):
        if self.mAreaUnits != theAreaUnits:
            self.mAreaUnits = theAreaUnits
            self._areaUnitsChanged.emit()


    @pyqtProperty(str, notify=_statusChanged)
    def status(self) -> Status: # type: ignore
        return self.mStatus
    @status.setter
    def status(self, theStatus: Status):
        if self.mStatus != theStatus:
            self.mStatus = theStatus
            self._statusChanged.emit()


    @property
    def guid(self) -> str:
        return self.mGuid
    @guid.setter
    def guid(self, theGuid: str):
        if self.mGuid != theGuid:
            self.setGuid(theGuid)
            self._guidChanged.emit()


    def requiredValue(self, theAnimalGuid: str) -> float:
        """Calculate required value for an animal.

        Args:
            theAnimalGuid (str): GUID of the animal to calculate for

        Returns:
            float: The required value
        """
        myAnimal = LaUtils.getAnimal(theAnimalGuid)
        myAnimalProductionTarget = 1
        myAnimalsRequired = (myAnimalProductionTarget / float(str(myAnimal.killWeight))) / (float(str(myAnimal.usableMeat)) * 0.01)
        myBirthsPerYear = 365.0 / (float(str(myAnimal.gestationTime)) + float(str(myAnimal.estrousCycle)) + float(str(myAnimal.weaningAge)))
        myOffspringPerMotherYearly = myBirthsPerYear * float(str(myAnimal.youngPerBirth)) * (1.0 - (0.01 * float(str(myAnimal.deathRate))))
        myMothersNeededStepOne = myAnimalsRequired / myOffspringPerMotherYearly
        myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly) / 2.0
        myFemalesStepOne = myMalesStepOne
        myMotherReplacementsPerYear = myMothersNeededStepOne / float(str(myAnimal.breedingExpectancy))
        myAdditionalMothers = (myMotherReplacementsPerYear / myOffspringPerMotherYearly) * 2.0
        myMalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myFemalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myTotalMothers = myMothersNeededStepOne + myAdditionalMothers
        myTotalMales = myMalesStepOne + myMalesStepTwo
        myTotalFemales = myFemalesStepOne - myFemalesStepTwo
        myTotalJuveniles = myTotalMales + myTotalFemales
        myTotalMothersValueRequired = myTotalMothers * myAnimal.gestating # type: ignore
        myTotalJuvenilesValueRequired = myTotalJuveniles * myAnimal.juvenile
        myValueNeededToFeedAnimals = myTotalMothersValueRequired + myTotalJuvenilesValueRequired
        myReturnValue = float(myValueNeededToFeedAnimals)

        # Log report
        self.logMessage("method ==> def requiredValue(self, theAnimalGuid: str) -> float:")
        self.logMessage("animal prodn target = calorie target of animal / food value")
        self.logMessage(f"Animal Production Target: {myAnimalProductionTarget}")
        self.logMessage(f"Slaughter animals required: {myAnimalsRequired}")
        self.logMessage(f"Birth events per year: {myBirthsPerYear}")
        self.logMessage(f"Offspring per mother yearly = {myOffspringPerMotherYearly}")
        self.logMessage(f"Mothers needed step one = {myMothersNeededStepOne}")
        self.logMessage(f"Males step one = {myMalesStepOne}")
        self.logMessage(f"Females step one = {myFemalesStepOne}")
        self.logMessage(f"Mother replacements per year = {myMotherReplacementsPerYear}")
        self.logMessage(f"Additional mothers = {myAdditionalMothers}")
        self.logMessage(f"Males step two = {myMalesStepTwo}")
        self.logMessage(f"Females step two = {myFemalesStepTwo}")
        self.logMessage(f"Total mothers = {myTotalMothers}")
        self.logMessage(f"Total males = {myTotalMales}")
        self.logMessage(f"Total females = {myTotalFemales}")
        self.logMessage(f"Total juveniles = {myTotalJuveniles}")
        self.logMessage(f"Total adult females value (Kg) = {myTotalMothersValueRequired}")
        self.logMessage(f"Total juveniles value (Kg) = {myTotalJuvenilesValueRequired}")
        self.logMessage(f"Total value (Kg) needed to feed animals = {myValueNeededToFeedAnimals}")
        self.logMessage("method ==> def requiredValue(self, theAnimalGuid: str) -> float:")
        self.logMessage(f"Animal: {myAnimal.name}")
        self.logMessage(f"Breeding stock: {myTotalMothers}")
        self.logMessage(f"Juveniles: {myTotalJuveniles}")
        self.logMessage(f"Kg value needed annually to feed the entire herd: {myReturnValue}")
        self.logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        return myReturnValue


    def fromXml(self, theXmlData):
        """
        Initialize the LaModel instance from an XML string.

        Args:
            theXmlData (str): The XML string containing the model data.
        """
        root = ET.fromstring(theXmlData)

        self.mGuid = self.setGuid(root.attrib.get('guid'))
        self.mName = root.findtext('name', default="No Name Set")
        self.mPopulation: int = int(root.findtext('population', default="1000"))
        self.mPeriod = root.findtext('period', default="No Period Set")
        self.mProjection = int(root.findtext('projection', default="100"))
        self.mEasting = int(root.findtext('easting', default="0"))
        self.mNorthing = int(root.findtext('northing', default="0"))
        self.mEuclideanDistance = root.findtext('euclideanDistance', default="True") == "True"
        self.mWalkingTime = root.findtext('walkingTime', default="False") == "False"
        self.mPathDistance = root.findtext('pathDistance', default="False") == "False"
        self.mPrecision = int(root.findtext('precision', default="5"))
        self.mDietPercent = int(root.findtext('dietPercent', default="25"))
        self.mPercentOfDietThatIsFromCrops = int(root.findtext('plantPercent', default="10"))
        self.mMeatPercent = int(root.findtext('meatPercent', default="10"))
        self.mCaloriesPerPersonDaily = int(root.findtext('caloriesPerPersonDaily', default="2500"))
        self.mBaseOnPlants = root.findtext('baseOnPlants', default="True") == "True"
        self.mIncludeDairy = root.findtext('includeDairy', default="True") == "True"
        self.mLimitDairy = root.findtext('limitDairy', default="False") == "False"
        self.mLimitDairyPercentage = int(root.findtext('limitDairyPercent', default="10"))
        self.mDairyUtilisation = int(root.findtext('dairyUtilisation', default="100"))
        self.mFallowStatus = Status[root.findtext('fallowStatus', default="FALLOW")]
        self.mFallowRatio = int(root.findtext('fallowRatio', default="1"))
        self.mCommonLandValue = float(root.findtext('commonLandValue', default="0.0"))
        self.mCommonLandAreaUnits = AreaUnits[root.findtext('commonLandAreaUnits', default="Hectare")] # Changed default to match enum
        # Added parsing for specific land units and energy type
        self.mSpecificLandAreaUnits = AreaUnits[root.findtext('specificLandAreaUnits', default="Hectare")]
        self.mSpecificLandEnergyType = EnergyType[root.findtext('specificLandEnergyType', default="KCalories")] # Corrected default
        self.mHerdSize = int(root.findtext('herdSize', default="0"))
        self.mAnimalsMap = {}  # Assuming animals are stored in a more complex structure
        self.mCropsMap = {}  # Assuming crops are stored in a more complex structure
        self.mDiets = {}  # Assuming diets are stored in a more complex structure
        self.mDietLabels = []  # Assuming diet labels are stored in a more complex structure
        self.mLandBeingGrazed = LandBeingGrazed[root.findtext('landBeingGrazed', default="Common")] # Changed default to match enum
        self.mLandFound = LandFound[root.findtext('landFound', default="NotEnough")] # Changed default to match enum
        self.mPriority = Priority[root.findtext('priority', default="Nope")] # Changed default to match enum
        self.mDescription = root.findtext('description', default="No Description Set")
        self.mAreaUnits = AreaUnits[root.findtext('areaUnits', default="Hectare")] # Changed default to match enum
        self.mStatus = Status[root.findtext('status', default="MoreThanEnoughToCompletelySatisfy")] # Changed default to match enum
        self.mIcon = None  # Assuming icon is handled separately

    def toXml(self) -> str:
        myString = f'<model guid="{self.guid}">\\n'
        myString += f'  <name>{LaUtils.xmlEncode(self.mName)}</name>\\n'
        myString += f'  <population>{self.mPopulation}</population>\\n'
        myString += f'  <period>{LaUtils.xmlEncode(self.mPeriod)}</period>\\n'
        myString += f'  <projection>{self.mProjection}</projection>\\n'
        myString += f'  <easting>{self.mEasting}</easting>\\n'
        myString += f'  <northing>{self.mNorthing}</northing>\\n'
        myString += f'  <euclideanDistance>{self.mEuclideanDistance}</euclideanDistance>\\n'
        myString += f'  <walkingTime>{self.mWalkingTime}</walkingTime>\\n'
        myString += f'  <pathDistance>{self.mPathDistance}</pathDistance>\\n'
        myString += f'  <precision>{self.mPrecision}</precision>\\n'
        myString += f'  <dietPercent>{self.mDietPercent}</dietPercent>\\n'
        myString += f'  <plantPercent>{self.mPercentOfDietThatIsFromCrops}</plantPercent>\\n'
        myString += f'  <meatPercent>{self.mMeatPercent}</meatPercent>\\n'
        myString += f'  <caloriesPerPersonDaily>{self.mCaloriesPerPersonDaily}</caloriesPerPersonDaily>\\n'
        myString += f'  <baseOnPlants>{self.mBaseOnPlants}</baseOnPlants>\\n'
        myString += f'  <includeDairy>{self.mIncludeDairy}</includeDairy>\\n'
        myString += f'  <limitDairy>{self.mLimitDairy}</limitDairy>\\n'
        myString += f'  <limitDairyPercent>{self.mLimitDairyPercentage}</limitDairyPercent>\\n'
        myString += f'  <dairyUtilisation>{self.mDairyUtilisation}</dairyUtilisation>\\n'
        # Added writing for specific land units and energy type
        myString += f'  <commonLandValue>{self.mCommonLandValue}</commonLandValue>\\n'
        myString += f'  <commonLandAreaUnits>{self.mCommonLandAreaUnits.name}</commonLandAreaUnits>\\n'
        myString += f'  <specificLandAreaUnits>{self.mSpecificLandAreaUnits.name}</specificLandAreaUnits>\\n'
        myString += f'  <specificLandEnergyType>{self.mSpecificLandEnergyType.name}</specificLandEnergyType>\\n'
        myString += f'  <herdSize>{self.mHerdSize}</herdSize>\\n'
        myString += f'  <dairyUtilisation>{self.mDairyUtilisation}</dairyUtilisation>\\n'
        myString += '</model>\\n'
        return myString




    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        from la.lib.lautils import LaUtils

        myDietLabels = LaDietLabels()
        myMCalsIndividualAnnual: float = float(str(self.caloriesPerPersonDaily)) * 365.0
        myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * float(str(self.population))
        myAnimal = LaAnimal()  # Matches C++ declaration but not used in this simplified version
        myCrop = LaCrop()

        # Get property values from internal attributes (following C++ variable naming)
        try:
            # Base values - matching C++ variable names
            myMCalsIndividualAnnual = self.mCaloriesPerPersonDaily * 365.0 / 1000.0  # Convert to annual MCals
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * self.mPopulation
            myDairyMCalorieCounter = 0.0
            myTameMeatMCalorieCounter = 0.0
            myWildMeatMCalorieCounter = 0.0
            mySelectedAnimalsMap = self.mAnimalsMap  # Similar to C++ QMap<QString,QString>

            # C++ style variable declarations (c1, c8, etc.)
            c1 = 1.0 - (self.mMeatPercent / 100.0)  # Decimal form of meat percent
            c8 = self.mDairyUtilisation / 100.0     # Decimal form of dairy utilization
            c10 = self.mPopulation
            c11 = self.mCaloriesPerPersonDaily
            c14 = c10 * c11 * 365.0 / 1000.0         # Settlement annual MCal
            c15 = self.mDietPercent / 100.0         # Decimal form of diet percent

            # Calculate MCals for different food sources
            # In this simplified version, we'll estimate values that would normally
            # come from detailed animal and crop calculations

            # Initialize counters (simplified calculation)
            myDairyMCalorieCounter = myMCalsSettlementAnnual * c15 * 0.05  # 5% of animal diet
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * (self.mMeatPercent / 100.0)  # Tame meat percent
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * c1  # Wild meat percent
            myCropMCalories = myMCalsSettlementAnnual * (1.0 - c15) * (self.mPercentOfDietThatIsFromCrops / 100.0)  # Crop percent
            myWildPlantsMCalories = myMCalsSettlementAnnual * (1.0 - c15) * (1.0 - self.mPercentOfDietThatIsFromCrops / 100.0)  # Wild plant percent

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
            # self._setDietLabels(
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

        return myDietLabels

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++
        myMCalsIndividualAnnual = float(str(self.caloriesPerPersonDaily)) * 365.0 / 1000.0  # Convert to MCal
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * int(str(self.population))
        myPlantPercent = 1.0 - (self.mDietPercent / 100.0)  # Plant portion as decimal
        myDomesticCropPortion = self.mPercentOfDietThatIsFromCrops / 100.0  # Crop portion of plants as decimal
        myWildMeatPortion = 1.0 - (self.mMeatPercent / 100.0)  # Wild meat portion as decimal
        # Log calculation start
        LaUtils.debug.log("Starting doCalcsPlantsFirstDairySeparate calculation", "Diet")

        try:
            # Base calculations similar to include dairy but with separate dairy tracking
            calories_daily = float(self.mCaloriesPerPersonDaily)
            population_count = float(self.mPopulation)
            meat_percent = float(self.mMeatPercent) / 100.0  # Convert to decimal
            diet_percent = float(self.mDietPercent) / 100.0  # Convert to decimal

            LaUtils.debug.log(f"Input parameters - calories_daily: {self.mCaloriesPerPersonDaily}, population: {self.mPopulation}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {self.mMeatPercent}%, diet_percent: {self.mDietPercent}%", "Diet")
            LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters with simplified approach to match C++ variable names
            myDairyMCalorieCounter = myMCalsSettlementAnnual * 0.05  # Separate counter for dairy (5% of total)
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * (self.mDietPercent / 100.0) * (self.mMeatPercent / 100.0)  # tame meat
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * (float(str(self.mDietPercent)) / 100.0) * myWildMeatPortion  # wild meat

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
            # self.setDietLabels(
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

        return myDietLabels








    def doCalcsAnimalsFirstIncludeDairy(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is included with meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        myAnimal = LaAnimal()

        # Initialize base calculations
        myMCalsIndividualAnnual = self.mCaloriesPerPersonDaily * 365.0
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * self.mPopulation
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0
        myWildMeatMCalorieCounter = 0.0
        mySelectedAnimalsMap = self.mAnimalsMap

        # Calculate coefficients
        c1 = 1.0 - self.mMeatPercent
        c8 = self.mDairyUtilisation
        c10 = self.mPopulation
        c11 = self.mCaloriesPerPersonDaily
        c14 = c10 * c11 * 365.0
        c15 = self.mDietPercent
        c12 = self.mPercentOfDietThatIsFromCrops
        e15 = c14 * c15

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
                c7 = myAnimal.usableMeat * 0.01
                e2 = c2 * c3 * (c4 - c5)
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
        myDietLabels.animalPortionPct = self.mDietPercent * 100.0 - c27 * 100.0
        myDietLabels.plantsPortionPct = (1.0 - self.mDietPercent) * 100.0
        myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

        LaUtils.debug.log("Diet calculations completed successfully", "Diet")

        return myDietLabels


    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
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
        from la.lib.lautils import LaUtils
        from la.lib.la import LaReportMap



        self.mCropCalcsReportMap = {} # Equivalent to C++ LaReportMap
        self.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap
        self.mValueMap = {} # Equivalent to C++ LaReportMap
        self.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap

        try:
            myAnimalCalcsReportMap: Dict[str, Tuple[str, float]] = {} # Equivalent to C++ LaReportMap
            myCropCalcsReportMap: Dict[str, Tuple[str, float]] = {} # Equivalent to C++ LaReportMap

            myAnimalsMap: Dict[str, float] = {} # for storing the calculations to send to fallow allocation

            myFodderNeedsPerCrop = {} # Equivalent to C++ myFoodSourceMapCounter (QMap<QString, float>)
            animalMCalRequirementMap = {} # Stores initial MCal requirements for fallow allocation

            myDietLabels = LaDietLabels()
            myAnimal = LaAnimal()

            myCrops: Dict[str, float] = self.mCropsMap  # for storing crop data


            # Assuming my_crops is a dictionary (equivalent to QMap<QString, QString>)
            # e.g., my_crops = {"crop_guid_1": "crop_name_1", "crop_guid_2": "crop_name_2"}

            myFoodSourceMapCounter: Dict[str, float] = {}  # for storing food source data Initialize an empty dictionary (equivalent to QMap<QString, int>)

            # Iterate through the keys of the my_crops dictionary
            for myCropGuid in myCrops:
                # Insert the key into myFoodSourceMapCounter with a value of 0
                myFoodSourceMapCounter[myCropGuid] = 0
                # myFoodSourceMapCounter will now be like: {"cropGuid1": 0, "cropGuid2": 0, ...}

            myMCalsIndividualAnnual: float = self.mCaloriesPerPersonDaily * 365.0 * 0.001  # MCal/person/year
            myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * self.mPopulation # MCal/settlement/year
            myDairyMCalorieCounter: float = 0.0  # Accumulates potential dairy MCals from all animals
            myTameMeatMCalorieCounter: float = 0.0  # Accumulates potential tame meat MCals from all animals

            myWildMeatPortion: float = (1.0 - self.mMeatPercent)  # C++: myWildMeatPortion
            myDairyUtilization: float = (self.mDairyUtilisation)
            myDairyLimitPercent: float = self.mLimitDairyPercentage
            myLimitDairyBool: bool = bool(self.mLimitDairy)  # C++: myDairyUtilisation

            myPlantPercent: float = 1.0 - self.mDietPercent
            myDomesticCropPortion: float = self.mPercentOfDietThatIsFromCrops

            mySelectedAnimalsMap: Dict[str, float] = self.mAnimalsMap # type: ignore

            for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
                # print("--------==--------------------------------------------==-------") # Using print instead of LaUtils.debug for literalness
                # print("--------==        Looping through the animals         ==-------")
                # print("--------==--------------------------------------------==-------")

                myAnimal = LaUtils.getAnimal(myAnimalGuid)
                myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid) # type: ignore
                myAdditionalMCalCounter = 0.
                myAdditionalMCalCounter1 = 0.

                myMilkKgPerDay = myAnimal.milkGramsPerDay * .001 # type: ignore # entered as Grams so need to convert to kg
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
                myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * self.dietPercent * self.meatPercent # B3
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
                myAnimalReport += "myGestatingMCals = " + str(myGestatingMCals) + "\n"
                myAnimalReport += "myLactatingMCals = " + str(myLactatingMCals) + "\n"
                myAnimalReport += "myDaysForMaintenance = " + str(myDaysForMaintenance) + "\n"
                myAnimalReport += "myGestatingTime = " + str(myGestatingTime) + "\n"
                myAnimalReport += "myLactationTime = " + str(myLactationTime) + "\n"
                myAnimalReport += "myDryMothers = " + str(myDryMothers) + "\n"
                myAnimalReport += "myDryMothersMCals = " + str(myDryMothersMCals) + "\n"
                myAnimalReport += "myOtherMaintenanceMCals = " + str(myOtherMaintenanceMCals) + "\n"
                myAnimalReport += "myMaintenanceMCals = " + str(myMaintenanceMCals) + "\n"
                myAnimalReport += "myAdultMalesMCals = " + str(myAdultMalesMCals) + "\n"
                myAnimalReport += "myOffspringMCals = " + str(myOffspringMCals) + "\n"

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
                print("myOffspringMCals = "   + str(myOffspringMCals))

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
                # .^.^.^.^.^.^.^.^.^      GUID , (theReportString , Area)     .^.^.^.^.^.^.^.^.^

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
                self.mValueMap[myAnimalGuid] = myAnimalHerdMCalsRequired # Direct port of C++: inserting into member mValueMap
            # done looping through the animals here

            # ----------- Dairy Portion to be calculated ------------
            # ------ the check should be: SUM(B11..B15) == 1.0 ------

            # limit the dairy.  if no limit the limit is 100 percent
            myDairyLimit: float = myDairyLimitPercent if myLimitDairyBool else 1.0
            myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
            myWildMeatPercent = myWildMeatPortion * self.mDietPercent
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
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myPlantPercent)
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
            mySelectedCropsMap: Dict[str, str] = self.mCropsMap # Assuming mCropsMap holds CropGuid -> CropParameterGuid

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
                myCropReport += f"Percent of Diet = {myCropPercent * 100.}% \n" # Added space before %
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

            # --- Fallow Allocation ---
            # --- Fallow Allocation ---
            self.allocateFallowGrazingLand(myMCalsFromFallowCounter, myAnimalsMap)

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
            for myAnimalGuid, myPair in myAnimalCalcsReportMap.items():
                # myReportIterator.next(); # Implicit in Python loop
                # QString myAnimalGuid = myReportIterator.key();
                # LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid); # Not used in C++ snippet

                # QPair <QString,float> myPair; # myPair is the loop variable (value)
                # myPair = myReportIterator.value();

                myReport: str = myPair[0] # QString myReport = myPair.first;
                # float myMCalTarget = mValueMap.value(myAnimalGuid);
                myMCalTarget: float = float(self.mValueMap[myAnimalGuid]) # Direct access, may raise KeyError if key not found

                # float myLandValue = mCommonGrazingValue;
                # Assuming mCommonLandValue is the Python equivalent
                myLandValue: float = self.mCommonGrazingValue # Assuming this is a class attribute
                # float myAreaTarget = myMCalTarget / myLandValue; # No division guard as requested
                myAreaTarget: float = myMCalTarget / myLandValue

                # myPair.second = myAreaTarget; # Tuples are immutable, create new one later

                # myReport += QString("Final MCal Target = " + QString::number(static_cast <int>(myMCalTarget)) + "\n");
                myReport += f"Final MCal Target = {int(myMCalTarget)}\n"
                # myReport += QString("Final Area Target = " + QString::number(static_cast <int>(myAreaTarget)) + "\n");
                myReport += f"Final Area Target = {int(myAreaTarget)}\n"

                # myPair.first = myReport; # Tuples are immutable, create new one

                # Create the updated tuple
                updatedPair: Tuple[str, float] = (myReport, myAreaTarget)

                # myAnimalCalcsReportMap[myAnimalGuid] = myPair;
                myAnimalCalcsReportMap[myAnimalGuid] = updatedPair
                # mAnimalCalcReport.insert(myAnimalGuid,myPair);
                # Assuming self.mAnimalCalcReport is the intended member dictionary
                if not hasattr(self, 'mAnimalCalcReport'):
                    self.mAnimalCalcReport = {} # Initialize if it doesn't exist
                self.mAnimalCalcReport[myAnimalGuid] = updatedPair


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
            # print(f" £££    mValueMap = {self.mValueMap}") # Python dict representation
            # print("£££")
            # print("££££££££££££££££££££££££££££££££££££")
            # print("   ££££££££££££££££££££££££££££££££££££")
            # print("      ££££££££££££££££££££££££££££££££££££")
            # print("   ££££££££££££££££££££££££££££££££££££")
            # print("££££££££££££££££££££££££££££££££££££")
            myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
            myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap # Use the updated map

            return myDietLabels

        



            

            LaUtils.debug.log("doCalcsAnimalsFirstDairySeparate calculation completed successfully", "Diet")
            self.mDietLabels = myDietLabels # Store result

        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsAnimalsFirstDairySeparate: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            # Return empty or default labels in case of error
            myDietLabels = LaDietLabels() # Reset to default

        return myDietLabels









    def allocateFallowGrazingLand(self, theFallowMCalsAvailable: float, theAnimalMCalRequirementMap: Dict[str, float]) -> None:
            """Allocate fallow grazing land to animals based on their priority.
            Strict port of C++ version.

            Args:
                theFallowMCalsAvailable: MCals available from fallow land
                theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements (Used differently than previous Python version)
            """
            from la.lib.lautils import LaUtils
            from la.lib.la import Priority
            from la.lib.laanimal import LaAnimal
            from la.lib.laanimalparameter import LaAnimalParameter

            LaUtils.debug.log("method ==> void LaModel::allocateFallowGrazingLand()", "Diet")
            # We need to divide the available fallow land amongst the animals
            # that graze fallow. We split the animal breeds by fallow land
            # access priority (high / medium and low priority).
            # e.g. We have 10 animal breeds, 6 of which graze fallow,
            # caw and horse are high priority, shee and pig medium,
            # chicken and gooxe low.

            myHighPriorityCount: float = 0.0
            myMediumPriorityCount: float = 0.0
            myLowPriorityCount: float = 0.0
            myHighPriorityValue: float = 0.0
            myMediumPriorityValue: float = 0.0
            myLowPriorityValue: float = 0.0
            # put starting caloric requirements of all used animals floato a map
            # for reduction due to grazing of fallow crop land
            # initialiseValueMap(); # Assumed self.mValueMap is already initialized correctly before this call

            myTotalFallowValue: float = theFallowMCalsAvailable

            # Count the Animals in each Priority Level and sum their calorie requirements
            # Note: C++ iterates mAnimalsMap (animalGuid -> paramGuid)
            #       High priority uses mValueMap for value summing.
            #       Medium/Low use theAnimalMCalRequirementMap for value summing.
            for myAnimalGuid, myAnimalParameterGuid in self.mAnimalsMap.items():
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
                        # Use self.mValueMap, mirroring C++ for High priority
                        animal_value = self.mValueMap.get(myAnimalGuid, 0.0)
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
                myLeftoverCalories = self.doTheFallowAllocation(myPriority, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount)
                LaUtils.debug.log(f"Remaining Fallow Calories after HIGH adjustments: {myLeftoverCalories}", "Diet")
                myTotalFallowValue = myLeftoverCalories

            # MEDIUM priority animals get allocated fallow cropland
            if myTotalFallowValue > 0:
                myPriority = Priority.Medium
                # Call the C++ style doTheFallowAllocation
                # C++ BUG?: Passes myHighPriorityCount instead of myMediumPriorityCount. Replicating bug.
                myLeftoverCalories = self.doTheFallowAllocation(myPriority, myTotalFallowValue, myMediumPriorityValue, myHighPriorityCount)
                LaUtils.debug.log(f"Remaining Fallow Calories after MED adjustments: {myLeftoverCalories}", "Diet")
                myTotalFallowValue = myLeftoverCalories

            # LOW priority animals get allocated fallow cropland
            if myTotalFallowValue > 0:
                myPriority = Priority.Low
                # Call the C++ style doTheFallowAllocation
                # C++ BUG?: Passes myHighPriorityCount instead of myLowPriorityCount. Replicating bug.
                myLeftoverCalories = self.doTheFallowAllocation(myPriority, myTotalFallowValue, myLowPriorityValue, myHighPriorityCount)
                LaUtils.debug.log(f"Remaining Fallow Calories after LOW adjustments: {myLeftoverCalories}", "Diet")
                myTotalFallowValue = myLeftoverCalories

            # float myReturnValue = static_cast<float>(myTotalFallowValue);
            # return myReturnValue; # Python function returns None (void equivalent)

    def doTheFallowAllocation(self, thePriority: Priority, theAvailableFallowValue: float,
                                theTotalNeededByGroup: float, theCountInGroup: float) -> float:
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
                for myAnimalGuid, myAnimalParameterGuid in self.mAnimalsMap.items():
                    myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
                    if myAnimalParameter.fallowUsage == thePriority:
                        # Get the animal's individual requirement from mValueMap
                        myIndividualRequirement = self.mValueMap.get(myAnimalGuid, 0.0)
                        if myAnimalGuid in self.mValueMap:
                            # Reduce the value in mValueMap by the full individual requirement
                            # C++ doesn't explicitly check min, but let's prevent negative values
                            myReduction = myIndividualRequirement
                            self.mValueMap[myAnimalGuid] -= myReduction
                            self.mValueMap[myAnimalGuid] = max(0.0, self.mValueMap[myAnimalGuid]) # Ensure non-negative
                            LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement fully met by fallow. Reduced by {myReduction:.2f}. Remaining need: {self.mValueMap[myAnimalGuid]:.2f}", "Diet")
                        else:
                            LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in mValueMap during fallow allocation (MoreThanEnough).", "Warning")

                # Calculate and return the leftover fallow value
                myRemainingFallow = myFallowDifference
                LaUtils.debug.log(f"Remaining Fallow Value after allocation: {myRemainingFallow:.2f}", "Diet")

            case Status.NotEnoughToCompletelySatisfy:
                LaUtils.debug.log("CASE: NotEnoughToCompletelySatisfy", "Diet")
                # Distribute the available fallow proportionally among animals in this group.
                # Need to iterate through animals again.
                for myAnimalGuid, myAnimalParameterGuid in self.mAnimalsMap.items():
                        myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)
                        if myAnimalParameter.fallowUsage == thePriority:
                            if myAnimalGuid in self.mValueMap:
                                # Get the animal's individual requirement from mValueMap
                                myIndividualRequirement = self.mValueMap.get(myAnimalGuid, 0.0)

                                # Calculate the proportion of available fallow this animal gets
                                # C++ does not guard division by zero here
                                myProportion = myIndividualRequirement / theTotalNeededByGroup
                                myAllocatedMCals = theAvailableFallowValue * myProportion
                                LaUtils.debug.log(f"  Animal {myAnimalGuid}: Needs {myIndividualRequirement:.2f}, Proportion {myProportion:.4f}, Allocated {myAllocatedMCals:.2f}", "Diet")

                                # Reduce the animal's requirement in the main value map
                                # C++ doesn't explicitly check min, but let's prevent negative values
                                myReduction = myAllocatedMCals
                                self.mValueMap[myAnimalGuid] -= myReduction
                                self.mValueMap[myAnimalGuid] = max(0.0, self.mValueMap[myAnimalGuid]) # Ensure non-negative
                                LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement reduced by {myReduction:.2f}. Remaining need: {self.mValueMap[myAnimalGuid]:.2f}", "Diet")
                            else:
                                LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in mValueMap during fallow allocation (NotEnough).", "Warning")
                # All available fallow has been used
                myRemainingFallow = 0.0
                LaUtils.debug.log(f"All available fallow allocated. Remaining Fallow Value: {myRemainingFallow:.2f}", "Diet")
            case _: # Default case, should not happen with Status enum
                LaUtils.debug.log(f"Unexpected fallow status: {myFallowStatus}", "Error")
                myRemainingFallow = theAvailableFallowValue # Return original value if status is unknown

        return myRemainingFallow










    def toHtmlCalorieCropTargets(self) -> str:
        """Generate HTML report for crop calorie targets."""
        html = "<h3>Crop Calorie Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

        # Get crop calorie targets from mDietLabels if available
        total_calories = 0
        crop_calories = {}

        if hasattr(self.mDietLabels, 'cropCalorieTargets'):
            crop_calories = self.mDietLabels.cropCalorieTargets
            total_calories = sum(crop_calories.values()) if crop_calories else 0

        # Generate rows for each crop
        if crop_calories:
            for crop_guid, calories in crop_calories.items():
                crop = LaUtils.getCrop(crop_guid)
                crop_name = crop.name if crop and crop.name else "Unknown"
                percentage = (calories / total_calories * 100) if total_calories > 0 else 0
                html += f"<tr><td>{crop_name}</td><td>{calories:,.0f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No crop calorie targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtmlCalorieAnimalTargets(self) -> str:
        """Generate HTML report for animal calorie targets."""
        html = "<h3>Animal Calorie Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

        # Get animal calorie targets from mDietLabels if available
        total_calories = 0
        animal_calories = {}

        if hasattr(self.mDietLabels, 'animalCalorieTargets'):
            animal_calories = self.mDietLabels.animalCalorieTargets
            total_calories = sum(animal_calories.values()) if animal_calories else 0

        # Generate rows for each animal
        if animal_calories:
            for animal_guid, calories in animal_calories.items():
                animal = LaUtils.getAnimal(animal_guid)
                animal_name = animal.name if animal and animal.name else "Unknown"
                percentage = (calories / total_calories * 100) if total_calories > 0 else 0
                html += f"<tr><td>{animal_name}</td><td>{calories:,.0f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No animal calorie targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtmlProductionCropTargets(self) -> str:
        """Generate HTML report for crop production targets."""
        html = "<h3>Crop Production Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Production (kg)</th><th>Percentage</th></tr>"

        # Get crop production targets from mDietLabels if available
        total_production = 0
        crop_production = {}

        if hasattr(self.mDietLabels, 'cropProductionTargets'):
            crop_production = self.mDietLabels.cropProductionTargets
            total_production = sum(crop_production.values()) if crop_production else 0

        # Generate rows for each crop
        if crop_production:
            for crop_guid, production in crop_production.items():
                crop = LaUtils.getCrop(crop_guid)
                crop_name = crop.name if crop and crop.name else "Unknown"
                percentage = (production / total_production * 100) if total_production > 0 else 0
                html += f"<tr><td>{crop_name}</td><td>{production:,.1f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No crop production targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtmlProductionAnimalTargets(self) -> str:
        """Generate HTML report for animal production targets."""
        html = "<h3>Animal Production Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Production (kg)</th><th>Percentage</th></tr>"

        # Get animal production targets from mDietLabels if available
        total_production = 0
        animal_production = {}

        if hasattr(self.mDietLabels, 'animalProductionTargets'):
            animal_production = self.mDietLabels.animalProductionTargets
            total_production = sum(animal_production.values()) if animal_production else 0

        # Generate rows for each animal
        if animal_production:
            for animal_guid, production in animal_production.items():
                animal = LaUtils.getAnimal(animal_guid)
                animal_name = animal.name if animal and animal.name else "Unknown"
                percentage = (production / total_production * 100) if total_production > 0 else 0
                html += f"<tr><td>{animal_name}</td><td>{production:,.1f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No animal production targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtmlAreaCropTargets(self) -> str:
        """Generate HTML report for crop area targets."""
        html = "<h3>Crop Area Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Area (ha)</th><th>Percentage</th></tr>"

        # Get crop area targets from mDietLabels if available
        total_area = 0
        crop_areas = {}

        if hasattr(self.mDietLabels, 'cropAreaTargets'):
            crop_areas = self.mDietLabels.cropAreaTargets
            total_area = sum(crop_areas.values()) if crop_areas else 0

        # Generate rows for each crop
        if crop_areas:
            for crop_guid, area in crop_areas.items():
                crop = LaUtils.getCrop(crop_guid)
                crop_name = crop.name if crop and crop.name else "Unknown"
                percentage = (area / total_area * 100) if total_area > 0 else 0
                html += f"<tr><td>{crop_name}</td><td>{area:,.2f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No crop area targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtmlAreaAnimalTargets(self) -> str:
        """Generate HTML report for animal area targets."""
        html = "<h3>Animal Area Targets</h3>"

        if not self.mDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Area (ha)</th><th>Percentage</th></tr>"

        # Get animal area targets from mDietLabels if available
        total_area = 0
        animal_areas = {}

        if hasattr(self.mDietLabels, 'animalAreaTargets'):
            animal_areas = self.mDietLabels.animalAreaTargets
            total_area = sum(animal_areas.values()) if animal_areas else 0

        # Generate rows for each animal
        if animal_areas:
            for animal_guid, area in animal_areas.items():
                animal = LaUtils.getAnimal(animal_guid)
                animal_name = animal.name if animal and animal.name else "Unknown"
                percentage = (area / total_area * 100) if total_area > 0 else 0
                html += f"<tr><td>{animal_name}</td><td>{area:,.2f}</td><td>{percentage:.1f}%</td></tr>"
        else:
            html += "<tr><td colspan='3'>No animal area targets calculated</td></tr>"

        html += "</table>"
        return html

    def toHtml(self) -> str:
        """Generate HTML report for the model."""
        html = f"<h3>Model Settings</h3>"
        html += "<table border='1' cellpadding='4'>"
        html += f"<tr><td><b>Population:</b></td><td>{self.population}</td></tr>"
        html += f"<tr><td><b>Calories per person per day:</b></td><td>{self.caloriesPerPersonDaily}</td></tr>"

        method = "Plants First" if self.baseOnPlants else "Animals First"
        dairy = "Included in Calculation" if self.includeDairy else "Calculated Separately"
        dairy_limit = f"Limited to {self.limitDairyPercent}%" if self.limitDairy else "Not Limited"

        html += f"<tr><td><b>Calculation Method:</b></td><td>{method}</td></tr>"
        html += f"<tr><td><b>Dairy:</b></td><td>{dairy}</td></tr>"
        html += f"<tr><td><b>Dairy Limit:</b></td><td>{dairy_limit}</td></tr>"
        html += "</table>"

        return html
