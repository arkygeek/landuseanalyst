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

        # Initialize LaSerialisable (maintains backward compatibility)
        # Check the underlying _mGuid attribute directly to avoid property/method confusion
        if not self._mGuid:
            self.setGuid() # Generate a new GUID if one wasn't set

        # Model properties
        self.mName = ""
        self.mPopulation = 100
        self.mTotalLandNeeded = 0

        # Added missing fields that are used in property getters/setters
        self.mPeriod = ""
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
        self.mCommonLandAreaUnits = 0  # Will be properly set from AreaUnits enum
        self.mSpecificLandAreaUnits = 0
        self.mSpecificLandEnergyType = 0
        self.mHerdSize = 0
        self.mFallowStatus = 0
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
        self.mCropsMap: dict[str, str] = {} # Corresponds to mCropsMap in C++
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
            self.mLogger.error(f"Failed to set dairyUtilisation with value '{thePercent}': {e}")


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


    @pyqtProperty(str, notify=_fallowStatusChanged) # TODO: set this to the correct return type
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


    @pyqtProperty(AreaUnits, notify=_commonLandAreaUnitsChanged)
    def commonLandAreaUnits(self) -> AreaUnits: # type: ignore
        return self.mCommonLandAreaUnits # TODO: figure out how to do this
    @commonLandAreaUnits.setter
    def commonLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self.mCommonLandAreaUnits != theAreaUnits:
            self.mCommonLandAreaUnits = theAreaUnits
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
        myTotalMothersValueRequired = myTotalMothers * float(str(myAnimal.gestating))
        myTotalJuvenilesValueRequired = myTotalJuveniles * float(str(myAnimal.juvenile))
        myValueNeededToFeedAnimals = myTotalMothersValueRequired + myTotalJuvenilesValueRequired
        myReturnValue = float(myValueNeededToFeedAnimals)

        # Log report
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
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
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
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
        self.mPriority = Priority[root.findtext('priority', default="None_")] # Changed default to match enum
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
        
        myDietLabels = LaDietLabels()
        myAnimal = LaAnimal()



        self.mCropCalcsReportMap = {} # Equivalent to C++ LaReportMap
        self.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap
        self.mValueMap = {} # Equivalent to C++ LaReportMap
        self.mAnimalCalcsReportMap = {} # Equivalent to C++ LaReportMap
        
        
        
        
        fodderNeedsPerCrop = {} # Equivalent to C++ myFoodSourceMapCounter (QMap<QString, float>)
        animalMCalRequirementMap = {} # Stores initial MCal requirements for fallow allocation

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsAnimalsFirstDairySeparate calculation (Python Port)", "Diet")

        try:
            # --- 1. Input Parameter Extraction & Initial Calculations ---
            calories_daily = float(self.mCaloriesPerPersonDaily)
            population_count = float(self.mPopulation)
            # Convert percentages to decimals right away
            meat_percent_of_animal_diet = float(self.mMeatPercent) / 100.0
            animal_diet_percent_of_total = float(self.mDietPercent) / 100.0
            dairy_utilisation = float(self.mDairyUtilisation) / 100.0
            limit_dairy_percent = float(self.mLimitDairyPercentage) / 100.0
            limit_dairy_bool = bool(self.mLimitDairy)
            plant_percent_of_total = 1.0 - animal_diet_percent_of_total
            domestic_crop_portion_of_plant = float(self.mPercentOfDietThatIsFromCrops) / 100.0
            wild_meat_portion_of_animal_diet = 1.0 - meat_percent_of_animal_diet # C++: myWildMeatPortion

            LaUtils.debug.log(f"Input parameters - calories_daily: {calories_daily}, population: {population_count}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent_of_animal_diet: {meat_percent_of_animal_diet*100}%, animal_diet_percent_of_total: {animal_diet_percent_of_total*100}%", "Diet")
            LaUtils.debug.log(f"Dairy parameters - utilisation: {dairy_utilisation*100}%, limit: {limit_dairy_bool}, limit_percent: {limit_dairy_percent*100}%", "Diet")
            LaUtils.debug.log(f"Plant parameters - plant_percent_of_total: {plant_percent_of_total*100}%, domestic_crop_portion_of_plant: {domestic_crop_portion_of_plant*100}%", "Diet")

            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # MCal/person/year
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count # MCal/settlement/year

            LaUtils.debug.log(f"myMCalsIndividualAnnual = {myMCalsIndividualAnnual}", "Diet")
            LaUtils.debug.log(f"myMCalsSettlementAnnual = {myMCalsSettlementAnnual}", "Diet")

            # Initialize overall counters
            myDairyMCalorieCounter = 0.0 # Accumulates potential dairy MCals from all animals
            myTameMeatMCalorieCounter = 0.0 # Accumulates potential tame meat MCals from all animals

            # Initialize fodder map (needs to be populated before crop loop)
            for crop_guid in self.mCropsMap.keys():
                 fodderNeedsPerCrop[crop_guid] = 0.0
            LaUtils.debug.log(f"Initialized fodderNeedsPerCrop: {fodderNeedsPerCrop}", "Diet")


            # --- 2. Animal Calculation Loop ---
            for myAnimalGuid, paramGuid in self.mAnimalsMap.items():
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                LaUtils.debug.log(f"--------==        Looping through animal: {myAnimalGuid}         ==-------", "Diet")
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                try:
                    animal = LaUtils.getAnimal(myAnimalGuid)
                    animalParameter = LaUtils.getAnimalParameter(paramGuid)

                    if not animal or not animalParameter:
                        LaUtils.debug.log(f"Missing animal or animal parameter for GUID {myAnimalGuid}", "Warning")
                        continue

                    LaUtils.debug.log(f"Processing animal: {animal.name} (GUID: {myAnimalGuid})", "Diet")

                    # --- 2a. Get Animal & Parameter Data (with type conversions and defaults) ---
                    myMilkKgPerDay = float(animal.milkGramsPerDay) * 0.001
                    myMilkFoodValue = float(animal.milkFoodValue) * 0.001 # MCal/kg
                    myLactationTime = float(animal.lactationTime)
                    myWeaningAge = float(animal.weaningAge)
                    myGestatingTime = float(animal.gestationTime)
                    myEstrousCycle = float(animal.estrousCycle)
                    myBabiesPerBirth = float(animal.youngPerBirth or 1) # Default 1
                    myDeathRate = float(animal.deathRate) * 0.01
                    myBreedingRatio = float(animal.femalesPerMale or 1) # females per male, default 1
                    if myBreedingRatio <= 0: myBreedingRatio = 1.0 # Avoid division by zero
                    myKillWeight = float(animal.killWeight)
                    myUsablePortionOfAnimal = float(animal.usableMeat) * 0.01
                    myAdultWeight = float(animal.adultWeight)
                    myFemalesToMales = myBreedingRatio # C++ uses same variable
                    myConceptionEfficiency = float(animal.conceptionEfficiency or 100) * 0.01 # Default 100%
                    myMeatValueMCal = float(animal.meatFoodValue) * 0.001 # MCal/kg
                    mySexualMaturity = float(animal.sexualMaturity or 12) # months, default 12
                    myBreedingYears = float(animal.breedingExpectancy or 1) # years, default 1
                    if myBreedingYears <= 0: myBreedingYears = 1.0 # Avoid division by zero

                    # Animal's contribution to the *tame meat* portion of the *animal* diet
                    # Default: Equal share among selected animals if parameter not set
                    try:
                        myAnimalContributionToMeatPortion = float(animalParameter.percentTameMeat or (100.0 / len(self.mAnimalsMap))) * 0.01 # B2
                    except ZeroDivisionError:
                         myAnimalContributionToMeatPortion = 0.0

                    # --- 2b. Calculate MCal Targets & Values per Offspring ---
                    # Target MCals this animal needs to provide (from tame meat portion)
                    myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * animal_diet_percent_of_total * meat_percent_of_animal_diet # B3
                    # Potential dairy MCals per offspring (if milked after weaning)
                    myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * max(0, myLactationTime - myWeaningAge) # B4
                    # Meat value (MCals) per offspring at kill weight
                    myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal # B5
                    # Actual utilized dairy MCals per offspring
                    myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * dairy_utilisation # B6

                    # --- 2c. Calculate Value from Culled Adults ---
                    # Birthing events per year (handle division by zero)
                    cycle_length_days = myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime
                    myBirthingEventsPerYear1 = (365.0 / cycle_length_days) if cycle_length_days > 0 else 0 # B21
                    # C++ logic: Ensure at least 1 event/year if cycle is very short? Seems odd, but matching it.
                    myBirthingEventsPerYear = max(1.0, myBirthingEventsPerYear1)

                    # Value (MCals) from culled mothers, distributed per offspring produced over lifetime
                    breeding_life_years = (mySexualMaturity / 12.0) + myBreedingYears
                    culled_mother_mcal_total = myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal
                    mcal_per_mother_per_year = (culled_mother_mcal_total / breeding_life_years) if breeding_life_years > 0 else 0
                    offspring_per_mother_per_year_for_cull_calc = myBabiesPerBirth * myBirthingEventsPerYear # Simplified for this calc
                    myCulledMothersValue = (mcal_per_mother_per_year / offspring_per_mother_per_year_for_cull_calc) if offspring_per_mother_per_year_for_cull_calc > 0 else 0 # B7

                    # Value (MCals) from culled adult males, distributed per offspring
                    myCulledAdultMalesValue = (myCulledMothersValue / myFemalesToMales) if myFemalesToMales > 0 else 0 # B8

                    # Final combined MCal value per offspring (meat + culled adults)
                    myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue # B9

                    # --- 2d. Calculate Offspring Needed & MCal Contributions ---
                    # Number of offspring needed per year to meet this animal's MCal target
                    myOffspringNeededPerYear = (myAnimalMCalTarget / myFinalOffspringValue) if myFinalOffspringValue > 0 else 0 # B11

                    # Total MCals provided by this animal (meat and dairy)
                    myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue # B12
                    myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear # B14

                    # Add to overall counters
                    myTameMeatMCalorieCounter += myMCalsFromTheMeat
                    myDairyMCalorieCounter += myMCalsUtilizedFromDairy

                    # --- 2e. Calculate Herd Size ---
                    # Effective offspring per mother per year considering survival and conception
                    myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1.0 - myDeathRate) * myConceptionEfficiency # B22
                    if myOffspringPerMotherPerYear <= 0: # Avoid division by zero
                        LaUtils.debug.log(f"Warning: Animal {animal.name} has zero effective offspring per mother per year ({myOffspringPerMotherPerYear}). Herd size calculation may be inaccurate.", "Warning")
                        # Cannot proceed with herd size calculation if this is zero.
                        # Store minimal report and skip feed calculation for this animal.
                        myAnimalReport = f"Cannot calculate herd size: Effective offspring per mother per year is {myOffspringPerMotherPerYear}\\n"
                        myAnimalCalcsReportMap[myAnimalGuid] = (myAnimalReport, 0.0) # Store 0 MCal requirement
                        animalMCalRequirementMap[myAnimalGuid] = 0.0
                        continue # Skip to next animal

                    # Mothers needed just for the target offspring
                    myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear # B23
                    # Offspring produced by these mothers (split male/female)
                    myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5 # B24
                    myFemalesStepOne = myMalesStepOne # B25

                    # Replacement mothers needed per year
                    # C++ adds (mySexualMaturity/12.) to myMothersNeededStepOne - this seems biologically questionable
                    # but matching C++ logic:
                    myReplacementMothersPerYear = ((myMothersNeededStepOne + (mySexualMaturity / 12.0)) / myBreedingYears) if myBreedingYears > 0 else 0 # B26

                    # Breeding males required for all mothers (needed + replacements)
                    # C++ B27: ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio
                    # Implementing the C++ formula directly as requested, without division check
                    myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio # B27 (Direct C++ formula)

                    # Additional mothers needed to produce replacements and breeding males
                    # C++ B28: ((myReplacementMothersPerYear/myOffspringPerMotherPerYear)*2.)+(myBreedingMalesRequired * 2.)
                    # Implementing the C++ formula directly as requested, without division check
                    mothers_for_replacements_term = (myReplacementMothersPerYear / myOffspringPerMotherPerYear) * 2.0
                    breeding_males_term = myBreedingMalesRequired * 2.0
                    myAdditionalMothers = mothers_for_replacements_term + breeding_males_term # B28 (Direct C++ formula)

                    # Offspring produced by these additional mothers
                    myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5 # B29
                    myFemalesStepTwo = myMalesStepTwo # B30

                    # Final herd composition
                    myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear # B32 (C++ uses this)
                    myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo # B33
                    # C++ B34: myFemalesStepOne - myFemalesStepTwo
                    myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo # B34 (Matching C++ logic)
                    # C++ B35: myTotalOffspring = myTotalMaleOffspring * 2.; // + myTotalFemaleOffspring;
                    myTotalOffspring = myTotalMaleOffspring * 2.0 # B35 (Matching C++ logic)

                    # --- 2f. Calculate Feed Requirements (MCals/year) ---
                    myFeedForGestating = float(animal.gestating) * 0.001 # MCal/day/mother
                    myFeedForLactating = float(animal.lactating) * 0.001 # MCal/day/mother
                    myFeedForMaintenance = float(animal.maintenance) * 0.001 # MCal/day/adult
                    myFeedForOffspringPerKg = float(animal.juvenile) * 0.001 # MCal/day/kg_offspring

                    # MCals for mothers during gestation/lactation/maintenance
                    # C++ uses myTotalOffspring for gestating/lactating counts
                    myGestatingMCals = myTotalOffspring * myGestatingTime * myFeedForGestating # Using myTotalOffspring per C++ comment
                    myLactatingMCals = myTotalOffspring * myLactationTime * myFeedForLactating # Using myTotalOffspring per C++ comment
                    # C++ logic for dry mothers maintenance days calculation (no max(0,...) guard)
                    myDaysForMaintenance = 365.0 - (myGestatingTime + myLactationTime)
                    # Using myTotalMothers for maintenance as C++ comment only mentioned gestating/lactating
                    myMotherMaintenanceMCals = myTotalMothers * myDaysForMaintenance * myFeedForMaintenance

                    # MCals for adult males (maintenance)
                    myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.0

                    # MCals for offspring (growth) - from weaning to kill weight (approximated)
                    # C++: myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365. - myWeaningAge)
                    # Using killWeight per C++ comment, instead of average weight.
                    # C++ logic for growth days (no max(0,...) guard)
                    days_growing = 365.0 - myWeaningAge
                    myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * days_growing # Using myKillWeight per C++ comment

                    # Total herd MCal requirement BEFORE fodder/grain contribution
                    myAnimalHerdMCalsRequired1 = (myGestatingMCals + myLactatingMCals + myMotherMaintenanceMCals +
                                                   myAdultMalesMCals + myOffspringMCals)

                    # --- 2g. Calculate Fodder/Grain Contribution ---
                    myAdditionalMCalCounter = 0.0 # MCals provided by grain/fodder
                    myFoodSourceMap = animalParameter.fodderSourceMap() # Dict[cropGuid, LaFoodSource]
                    LaUtils.debug.log(f"    ----== Calculating Fodder/Grain Needs ==----", "Diet")
                    for myCropGuid, myFoodSource in myFoodSourceMap.items():
                        LaUtils.debug.log(f"        Processing fodder source: Crop GUID {myCropGuid}", "Diet")
                        myCrop = LaUtils.getCrop(myCropGuid)
                        if not myCrop:
                            LaUtils.debug.log(f"            Crop {myCropGuid} not found for fodder source.", "Warning")
                            continue

                        # Get food source details (kg/day/animal)
                        myGrainKgPerDay = float(myFoodSource.grain) * 0.001
                        myFodderKgPerDay = float(myFoodSource.fodder) * 0.001
                        myDaysFed = float(myFoodSource.days)

                        # Get crop energy values (MCal/kg)
                        myFoodValueOfCrop = float(myCrop.cropCalories) * 0.001
                        myFoodValueofFodder = float(myCrop.cropFodderValue) * 0.001

                        # Calculate total kg needed for the *entire herd* over the specified days
                        # C++ calculates per offspring? Seems wrong. Applying to relevant herd members.
                        # Who eats grain/fodder? Assume all except maybe young offspring before weaning?
                        # Let's assume total mothers + breeding males + total offspring (post-weaning equiv).
                        herd_size_for_feed = myTotalMothers + myBreedingMalesRequired + myTotalOffspring # Approximation

                        myGrainToAddKgTotal = myGrainKgPerDay * myDaysFed * herd_size_for_feed
                        myFodderToAddKgTotal = myFodderKgPerDay * myDaysFed * herd_size_for_feed

                        # Add grain requirement (kg) to the crop's total needed (for crop loop later)
                        if myCropGuid in fodderNeedsPerCrop:
                             fodderNeedsPerCrop[myCropGuid] += myGrainToAddKgTotal
                        else:
                             # This case shouldn't happen if initialized correctly, but handle it
                             fodderNeedsPerCrop[myCropGuid] = myGrainToAddKgTotal
                             LaUtils.debug.log(f"            Warning: Crop {myCropGuid} not pre-initialized in fodderNeedsPerCrop.", "Warning")

                        # Log details for debugging
                        LaUtils.debug.log(f"            myGrainKgPerDay = {myGrainKgPerDay}", "Diet")
                        LaUtils.debug.log(f"            myFodderKgPerDay = {myFodderKgPerDay}", "Diet")
                        LaUtils.debug.log(f"            myDaysFed = {myDaysFed}", "Diet")
                        LaUtils.debug.log(f"            herd_size_for_feed = {herd_size_for_feed}", "Diet")
                        LaUtils.debug.log(f"            Grain to add (kg) for {animal.name} from {myCrop.name}: {myGrainToAddKgTotal:.2f}", "Diet")
                        LaUtils.debug.log(f"            Current total grain needed for {myCrop.name}: {fodderNeedsPerCrop[myCropGuid]:.2f}", "Diet")

                        # Calculate MCal provided by this grain/fodder source
                        myGrainMCal = myGrainToAddKgTotal * myFoodValueOfCrop
                        myFodderMCal = myFodderToAddKgTotal * myFoodValueofFodder
                        myAdditionalMCalCounter += myGrainMCal + myFodderMCal

                        LaUtils.debug.log(f"            Food Value of Crop Grain: {myFoodValueOfCrop}", "Diet")
                        LaUtils.debug.log(f"            Food Value of Crop Fodder: {myFoodValueofFodder}", "Diet")
                        LaUtils.debug.log(f"            myGrainMCal = {myGrainMCal:.2f}", "Diet")
                        LaUtils.debug.log(f"            myFodderMCal = {myFodderMCal:.2f}", "Diet")
                        LaUtils.debug.log(f"            Cumulative MCals from grain/fodder for {animal.name}: {myAdditionalMCalCounter:.2f}", "Diet")

                    # --- 2h. Adjust Herd MCal Requirement & Store Results ---
                    # Final MCal requirement for this herd (needs to come from grazing/fallow)
                    myAnimalHerdMCalsRequired = max(0, myAnimalHerdMCalsRequired1 - myAdditionalMCalCounter) # Ensure non-negative

                    LaUtils.debug.log(f"  ---- AnimalHerd MCals Required BEFORE grain/fodder: {myAnimalHerdMCalsRequired1:.2f}", "Diet")
                    LaUtils.debug.log(f"  ---- AnimalHerd MCals Required AFTER grain/fodder: {myAnimalHerdMCalsRequired:.2f}", "Diet")

                    # Store the requirement for fallow allocation later
                    animalMCalRequirementMap[myAnimalGuid] = myAnimalHerdMCalsRequired

                    # Build the detailed report string (similar to C++)
                    myAnimalReport = f"--- Calculation Report for Animal: {animal.name} ({myAnimalGuid}) ---\\n"
                    myAnimalReport += f"Inputs & Intermediate Values:\\n"
                    myAnimalReport += f"  MilkKgPerDay: {myMilkKgPerDay:.3f}, MilkFoodValue: {myMilkFoodValue:.3f} MCal/kg\\n"
                    myAnimalReport += f"  LactationTime: {myLactationTime} days, WeaningAge: {myWeaningAge} days\\n"
                    myAnimalReport += f"  GestationTime: {myGestatingTime} days, EstrousCycle: {myEstrousCycle} days\\n"
                    myAnimalReport += f"  BabiesPerBirth: {myBabiesPerBirth}, DeathRate: {myDeathRate*100:.1f}%, ConceptionEff: {myConceptionEfficiency*100:.1f}%\\n"
                    myAnimalReport += f"  KillWeight: {myKillWeight} kg, UsableMeat: {myUsablePortionOfAnimal*100:.1f}%, MeatValue: {myMeatValueMCal:.3f} MCal/kg\\n"
                    myAnimalReport += f"  AdultWeight: {myAdultWeight} kg, FemalesPerMale: {myFemalesToMales}\\n"
                    myAnimalReport += f"  SexualMaturity: {mySexualMaturity} months, BreedingYears: {myBreedingYears} years\\n"
                    myAnimalReport += f"  ContributionToMeatPortion: {myAnimalContributionToMeatPortion*100:.2f}%\\n"
                    myAnimalReport += f"MCal Targets & Values:\\n"
                    myAnimalReport += f"  AnimalMCalTarget (Meat): {myAnimalMCalTarget:.2f} MCal\\n"
                    myAnimalReport += f"  PotentialDairyPerOffspring: {myPotentialDairyPerOffspring:.2f} MCal\\n"
                    myAnimalReport += f"  ValuePerOffspring (Meat): {myValuePerOffspring:.2f} MCal\\n"
                    myAnimalReport += f"  ActualDairyValueOfOffspring: {myActualDairyValueOfOffspring:.2f} MCal\\n"
                    myAnimalReport += f"  CulledMothersValue (per offspring): {myCulledMothersValue:.2f} MCal\\n"
                    myAnimalReport += f"  CulledAdultMalesValue (per offspring): {myCulledAdultMalesValue:.2f} MCal\\n"
                    myAnimalReport += f"  FinalOffspringValue (Meat+Cull): {myFinalOffspringValue:.2f} MCal\\n"
                    myAnimalReport += f"Offspring & MCal Contribution:\\n"
                    myAnimalReport += f"  OffspringNeededPerYear: {myOffspringNeededPerYear:.2f}\\n"
                    myAnimalReport += f"  MCalsFromTheMeat: {myMCalsFromTheMeat:.2f} MCal\\n"
                    myAnimalReport += f"  MCalsUtilizedFromDairy: {myMCalsUtilizedFromDairy:.2f} MCal\\n"
                    myAnimalReport += f"Herd Size Calculation:\\n"
                    myAnimalReport += f"  BirthingEventsPerYear: {myBirthingEventsPerYear:.2f}\\n"
                    myAnimalReport += f"  OffspringPerMotherPerYear (Effective): {myOffspringPerMotherPerYear:.2f}\\n"
                    myAnimalReport += f"  MothersNeededStepOne: {myMothersNeededStepOne:.2f}\\n"
                    myAnimalReport += f"  MalesStepOne: {myMalesStepOne:.2f}, FemalesStepOne: {myFemalesStepOne:.2f}\\n"
                    myAnimalReport += f"  ReplacementMothersPerYear: {myReplacementMothersPerYear:.2f}\\n"
                    myAnimalReport += f"  BreedingMalesRequired: {myBreedingMalesRequired:.2f}\\n"
                    myAnimalReport += f"  AdditionalMothers: {myAdditionalMothers:.2f}\\n"
                    myAnimalReport += f"  MalesStepTwo: {myMalesStepTwo:.2f}, FemalesStepTwo: {myFemalesStepTwo:.2f}\\n"
                    myAnimalReport += f"Final Herd Composition:\\n"
                    myAnimalReport += f"  TotalMothers: {myTotalMothers:.2f}\\n"
                    myAnimalReport += f"  TotalMaleOffspring: {myTotalMaleOffspring:.2f}\\n"
                    myAnimalReport += f"  TotalFemaleOffspring: {myTotalFemaleOffspring:.2f}\\n"
                    myAnimalReport += f"  TotalOffspring (B35): {myTotalOffspring:.2f}\\n"
                    myAnimalReport += f"Feed Requirements (MCal/year):\\n"
                    myAnimalReport += f"  FeedForGestating: {myFeedForGestating:.3f} MCal/day/mother\\n"
                    myAnimalReport += f"  FeedForLactating: {myFeedForLactating:.3f} MCal/day/mother\\n"
                    myAnimalReport += f"  FeedForMaintenance: {myFeedForMaintenance:.3f} MCal/day/adult\\n"
                    myAnimalReport += f"  FeedForOffspringPerKg: {myFeedForOffspringPerKg:.3f} MCal/day/kg\\n"
                    myAnimalReport += f"  GestatingMCals: {myGestatingMCals:.2f}\\n"
                    myAnimalReport += f"  LactatingMCals: {myLactatingMCals:.2f}\\n"
                    myAnimalReport += f"  MotherMaintenanceMCals: {myMotherMaintenanceMCals:.2f} (Days: {myDaysForMaintenance})\\n"
                    myAnimalReport += f"  AdultMalesMCals: {myAdultMalesMCals:.2f}\\n"
                    myAnimalReport += f"  OffspringMCals: {myOffspringMCals:.2f}\\n"
                    myAnimalReport += f"Total & Adjusted Feed Needs:\\n"
                    myAnimalReport += f"  Total Herd MCals (Before Fodder): {myAnimalHerdMCalsRequired1:.2f} MCal\\n"
                    myAnimalReport += f"  MCals from Fodder/Grain: {myAdditionalMCalCounter:.2f} MCal\\n"
                    myAnimalReport += f"  Final Herd MCals Required (Grazing/Fallow): {myAnimalHerdMCalsRequired:.2f} MCal\\n"
                    myAnimalReport += f"--- End Report for {animal.name} ---\\n"

                    # Store report and initial MCal requirement (Area Target is calculated later)
                    myAnimalCalcsReportMap[myAnimalGuid] = (myAnimalReport, 0.0) # Placeholder for area target
                    LaUtils.debug.log(f"Stored report for {animal.name}. Initial MCal Requirement: {myAnimalHerdMCalsRequired:.2f}", "Diet")

                except Exception as e:
                    LaUtils.debug.log(f"Error in animal calculation loop for GUID {myAnimalGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
                    # Store error message in report
                    myAnimalCalcsReportMap[myAnimalGuid] = (f"Error processing animal {myAnimalGuid}: {e}", 0.0)
                    animalMCalRequirementMap[myAnimalGuid] = 0.0 # Ensure it exists even if error occurred

            # --- 3. Dairy Portion Adjustment (Post Animal Loop) ---
            LaUtils.debug.log("Adjusting final diet portions based on dairy limit...", "Diet")
            LaUtils.debug.log(f"Total Potential Dairy (Sum from animals): {myDairyMCalorieCounter:.2f} MCal", "Diet")
            LaUtils.debug.log(f"Total Potential Tame Meat (Sum from animals): {myTameMeatMCalorieCounter:.2f} MCal", "Diet")

            # Calculate potential percentages based on total settlement needs
            potential_domestic_meat_percent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B11 in C++
            potential_dairy_percent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0

            # Wild meat percent of *total* diet
            wild_meat_percent_of_total = animal_diet_percent_of_total * wild_meat_portion_of_animal_diet # B13 in C++

            # Determine the actual dairy limit percentage to apply
            effective_dairy_limit_percent = limit_dairy_percent if limit_dairy_bool else 1.0 # B22 in C++ (1.0 means no limit)

            # Check if the potential meat + limited dairy exceeds the total diet allowed
            # C++ B21: myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0
            # This seems wrong. Should check against animal_diet_percent_of_total?
            # Let's re-evaluate: Check if potential meat + potential dairy (capped by limit) exceeds the animal portion
            max_allowed_dairy_percent = effective_dairy_limit_percent
            potential_total_animal_percent = potential_domestic_meat_percent + wild_meat_percent_of_total + min(potential_dairy_percent, max_allowed_dairy_percent)

            # If the potential animal sources exceed the target animal diet percentage, scale them down?
            # C++ logic seems different. It recalculates the dairy limit based on 1.0 (total diet).
            # Let's stick to C++ B20/B18 logic for now:
            # If (potential domestic meat + wild meat + dairy limit) > 100% of total diet, reduce the dairy limit
            limit_plus_meat_check = potential_domestic_meat_percent + wild_meat_percent_of_total + effective_dairy_limit_percent
            myLimitSatisfies = limit_plus_meat_check > 1.0 # B21
            # New dairy limit if the sum exceeds 100%
            myNewLimit = max(0, 1.0 - potential_domestic_meat_percent - wild_meat_percent_of_total) if myLimitSatisfies else effective_dairy_limit_percent # B20

            # Is potential dairy less than the (potentially adjusted) limit?
            myPotentialDairyLessThanLimitBool = potential_dairy_percent < myNewLimit # B19

            # Final MCal for dairy
            myNewDairyMCals = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual # B18

            # --- 4. Calculate Final Diet Percentages & MCals ---
            # Final percentages of TOTAL settlement diet
            myOverallDairyPercent = myNewDairyMCals / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B12 & B8
            myOverallDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B11 (using the potential value)
            myOverallWildMeatPercent = wild_meat_percent_of_total # B13 (as calculated earlier)

            myOverallMeatPercent = myOverallDomesticMeatPercent + myOverallWildMeatPercent # B7
            # Plant percent is whatever is left over
            myOverallPlantPercent = max(0, 1.0 - myOverallMeatPercent - myOverallDairyPercent) # B6

            # Split plant percent into crops and wild plants
            myOverallCropPercent = myOverallPlantPercent * domestic_crop_portion_of_plant # B14
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - domestic_crop_portion_of_plant) # B15

            # Final MCals for each category
            myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual # B26
            myOverallDomesticMeatMCals = myOverallDomesticMeatPercent * myMCalsSettlementAnnual # B25
            myOverallWildMeatMCals = myOverallWildMeatPercent * myMCalsSettlementAnnual # B27
            myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual # B28
            myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual # B29
            myOverallMeatMCals = myOverallDomesticMeatMCals + myOverallWildMeatMCals # For reporting

            # Dairy Surplus
            myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals # Difference between potential and actual used
            myOverallDairySurplusMCals = max(0, myFirstDairySurplusBool)

            LaUtils.debug.log(f"Final Diet Calculation Results:", "Diet")
            LaUtils.debug.log(f"  Overall Dairy: {myOverallDairyPercent*100:.2f}% ({myOverallDairyMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Overall Domestic Meat: {myOverallDomesticMeatPercent*100:.2f}% ({myOverallDomesticMeatMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Overall Wild Meat: {myOverallWildMeatPercent*100:.2f}% ({myOverallWildMeatMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Overall Meat (Total): {myOverallMeatPercent*100:.2f}% ({myOverallMeatMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Overall Plant (Total): {myOverallPlantPercent*100:.2f}%", "Diet")
            LaUtils.debug.log(f"  Overall Crops: {myOverallCropPercent*100:.2f}% ({myOverallCropsMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Overall Wild Plants: {myOverallWildPlantPercent*100:.2f}% ({myOverallWildPlantsMCals:.2f} MCal)", "Diet")
            LaUtils.debug.log(f"  Dairy Surplus: {myOverallDairySurplusMCals:.2f} MCal", "Diet")
            LaUtils.debug.log(f"  Sum Check: {(myOverallDairyPercent + myOverallMeatPercent + myOverallPlantPercent)*100:.2f}%", "Diet")


            # --- 5. Crop Calculation Loop ---
            myMCalsFromFallowCounter = 0.0 # Accumulates MCals provided by fallow land associated with crops
            total_crop_area_before_fallow = 0.0 # Sum of myCropAreaTarget1 for all crops

            for myCropGuid, paramGuid in self.mCrops.items():
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                LaUtils.debug.log(f"**********         Looping through crop: {myCropGuid}          **********", "Diet")
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                try:
                    myCrop = LaUtils.getCrop(myCropGuid)
                    cropParameter = LaUtils.getCropParameter(paramGuid)

                    if not myCrop or not cropParameter:
                        LaUtils.debug.log(f"          Missing crop or crop parameter for GUID {myCropGuid}", "Warning")
                        continue

                    LaUtils.debug.log(f"          Processing crop: {myCrop.name}", "Diet")

                    # --- 5a. Calculate Crop MCal Target & Production Needs (kg) ---
                    # This crop's portion of the *total* crop MCal target
                    try:
                        myCropPortion = float(cropParameter.percentTameCrop or (100.0 / len(self.mCrops))) * 0.01
                    except ZeroDivisionError:
                        myCropPortion = 0.0

                    myMCalsFromTheCrop = myCropPortion * myOverallCropsMCals # Target MCals from this crop for people
                    myCropFoodValue = float(myCrop.cropCalories) * 0.001 # MCal/kg

                    LaUtils.debug.log(f"          myCropPortion = {myCropPortion*100:.2f}%", "Diet")
                    LaUtils.debug.log(f"          myMCalsFromTheCrop (for people) = {myMCalsFromTheCrop:.2f} MCal", "Diet")
                    LaUtils.debug.log(f"          myCropFoodValue = {myCropFoodValue:.3f} MCal/kg", "Diet")

                    # Kg needed for people (before spoilage/reseed)
                    myKgForPeople1 = (myMCalsFromTheCrop / myCropFoodValue) if myCropFoodValue > 0 else 0

                    # Get spoilage and reseeding percentages
                    mySpoilagePercent = float(cropParameter.spoilage) * 0.01
                    myReseedPercent = float(cropParameter.reseed) * 0.01

                    # Calculate additional kg needed for spoilage and reseeding (applied to people's portion)
                    myKgForPeopleSpoilage = myKgForPeople1 * mySpoilagePercent
                    myKgForPeopleReseed = myKgForPeople1 * myReseedPercent
                    myKgForPeopleTotal = myKgForPeople1 + myKgForPeopleSpoilage + myKgForPeopleReseed

                    # Get additional kg needed for animal grain (from map populated in animal loop)
                    myAnimalKgAdd1 = fodderNeedsPerCrop.get(myCropGuid, 0.0)

                    # Adjust animal grain needs for spoilage and reseeding
                    myAnimalKgAddSpoilage = myAnimalKgAdd1 * mySpoilagePercent
                    myAnimalKgAddReseed = myAnimalKgAdd1 * myReseedPercent
                    myAnimalKgAddTotal = myAnimalKgAdd1 + myAnimalKgAddSpoilage + myAnimalKgAddReseed

                    # Total production target (kg) for this crop
                    myAdjustedTargetKg = myKgForPeopleTotal + myAnimalKgAddTotal

                    LaUtils.debug.log(f"          myKgForPeople1 (raw) = {myKgForPeople1:.2f} kg", "Diet")
                    LaUtils.debug.log(f"          mySpoilagePercent = {mySpoilagePercent*100:.1f}%, myReseedPercent = {myReseedPercent*100:.1f}%", "Diet")
                    LaUtils.debug.log(f"          myKgForPeopleTotal (incl. spoil/reseed) = {myKgForPeopleTotal:.2f} kg", "Diet")
                    LaUtils.debug.log(f"          myAnimalKgAdd1 (raw grain) = {myAnimalKgAdd1:.2f} kg", "Diet")
                    LaUtils.debug.log(f"          myAnimalKgAddTotal (incl. spoil/reseed) = {myAnimalKgAddTotal:.2f} kg", "Diet")
                    LaUtils.debug.log(f"          myAdjustedTargetKg (Total Production) = {myAdjustedTargetKg:.2f} kg", "Diet")

                    # --- 5b. Calculate Area Needed (Before Fallow) ---
                    myCropYieldKgPerHa = float(myCrop.cropYield) # Assume yield is in kg/ha unless specified otherwise
                    # C++ adjusts for Dunum, add similar logic if needed based on LaCrop definition
                    if hasattr(myCrop, 'areaUnits') and str(myCrop.areaUnits) == "Dunum":
                        myCropYieldKgPerHa = myCropYieldKgPerHa * 10.0

                    LaUtils.debug.log(f"          myCropYield = {myCropYieldKgPerHa:.2f} kg/ha", "Diet")

                    # Initial crop area target (hectares) before considering fallow
                    myCropAreaTarget1 = (myAdjustedTargetKg / myCropYieldKgPerHa) if myCropYieldKgPerHa > 0 else 0
                    total_crop_area_before_fallow += myCropAreaTarget1 # Accumulate for fallow calculation

                    LaUtils.debug.log(f"          myCropAreaTarget1 (Before Fallow) = {myCropAreaTarget1:.4f} ha", "Diet")

                    # --- 5c. Calculate Fallow Contribution (if applicable) ---
                    myFallowArea = 0.0
                    myFallowMCals = 0.0
                    myCropAreaTarget = myCropAreaTarget1 # Final area starts as initial area

                    # Check if fallow is used for this crop parameter
                    fallow_ratio = float(cropParameter.fallowRatio)
                    if fallow_ratio > 0:
                        # Fallow value (MCal/ha/year from fallow land associated with this crop)
                        myFallowValueMcalPerHa = float(cropParameter.fallowValue)

                        # C++ solves: TotalArea = CropArea + FallowArea = CropArea + CropArea * Ratio
                        # TotalArea = CropArea * (1 + Ratio)
                        # CropArea = TotalArea / (1 + Ratio)
                        # We know CropArea = myCropAreaTarget1 (area needed *just* for the crop yield)
                        # So, TotalArea = myCropAreaTarget1 * (1.0 + fallow_ratio)
                        myTotalAreaNeeded = myCropAreaTarget1 * (1.0 + fallow_ratio)
                        myFallowArea = myTotalAreaNeeded - myCropAreaTarget1 # Area dedicated to fallow
                        myCropAreaTarget = myCropAreaTarget1 # The area actively cropped remains the same

                        # MCals generated by this fallow land
                        myFallowMCals = myFallowArea * myFallowValueMcalPerHa
                        myMCalsFromFallowCounter += myFallowMCals # Accumulate total fallow MCals

                        LaUtils.debug.log(f"          Fallow Calculation:", "Diet")
                        LaUtils.debug.log(f"            Fallow Ratio = {fallow_ratio}", "Diet")
                        LaUtils.debug.log(f"            Fallow Value = {myFallowValueMcalPerHa:.2f} MCal/ha", "Diet")
                        LaUtils.debug.log(f"            Total Area (Crop + Fallow) = {myTotalAreaNeeded:.4f} ha", "Diet")
                        LaUtils.debug.log(f"            Fallow Area = {myFallowArea:.4f} ha", "Diet")
                        LaUtils.debug.log(f"            MCals from this Fallow = {myFallowMCals:.2f} MCal", "Diet")
                    else:
                         myTotalAreaNeeded = myCropAreaTarget1 # No fallow, total area = crop area
                         LaUtils.debug.log(f"          No Fallow for this crop.", "Diet")


                    # --- 5d. Store Crop Results ---
                    # Build report string
                    myCropReport = f"--- Calculation Report for Crop: {myCrop.name} ({myCropGuid}) ---\\n"
                    myCropReport += f"Target MCals (People): {myMCalsFromTheCrop:.2f} MCal\\n"
                    myCropReport += f"Production Needs (kg):\\n"
                    myCropReport += f"  People (Raw): {myKgForPeople1:.2f} kg\\n"
                    myCropReport += f"  People (Total incl. Spoil/Reseed): {myKgForPeopleTotal:.2f} kg\\n"
                    myCropReport += f"  Animal Grain (Raw): {myAnimalKgAdd1:.2f} kg\\n"
                    myCropReport += f"  Animal Grain (Total incl. Spoil/Reseed): {myAnimalKgAddTotal:.2f} kg\\n"
                    myCropReport += f"  Total Production Target: {myAdjustedTargetKg:.2f} kg\\n"
                    myCropReport += f"Area Calculation (ha):\\n"
                    myCropReport += f"  Yield: {myCropYieldKgPerHa:.2f} kg/ha\\n"
                    myCropReport += f"  Crop Area Needed (Active): {myCropAreaTarget:.4f} ha\\n"
                    if fallow_ratio > 0:
                        myCropReport += f"  Fallow Ratio: {fallow_ratio}\\n"
                        myCropReport += f"  Fallow Area: {myFallowArea:.4f} ha\\n"
                        myCropReport += f"  Total Area (Crop + Fallow): {myTotalAreaNeeded:.4f} ha\\n"
                        myCropReport += f"  MCals from Fallow: {myFallowMCals:.2f} MCal\\n"
                    else:
                        myCropReport += f"  Total Area: {myTotalAreaNeeded:.4f} ha\\n"
                    myCropReport += f"--- End Report for {myCrop.name} ---\\n"

                    # Store report and the *total* area (crop + fallow) for this crop system
                    myCropCalcsReportMap[myCropGuid] = (myCropReport, myTotalAreaNeeded)
                    LaUtils.debug.log(f"          Stored report for {myCrop.name}. Total Area: {myTotalAreaNeeded:.4f} ha", "Diet")

                except Exception as e:
                    LaUtils.debug.log(f"          Error in crop calculation loop for GUID {myCropGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"          Error details: {traceback.format_exc()}", "Error")
                    myCropCalcsReportMap[myCropGuid] = (f"Error processing crop {myCropGuid}: {e}", 0.0)


            # --- 6. Fallow Land Allocation to Animals ---
            LaUtils.debug.log("Allocating Fallow MCals to Animals...", "Diet")
            LaUtils.debug.log(f"Total MCals available from Fallow: {myMCalsFromFallowCounter:.2f} MCal", "Diet")

            # Calculate total animal MCal requirement (sum from map)
            total_animal_mcal_requirement = sum(animalMCalRequirementMap.values())
            LaUtils.debug.log(f"Total Animal MCal Requirement (Grazing): {total_animal_mcal_requirement:.2f} MCal", "Diet")

            if total_animal_mcal_requirement > 0 and myMCalsFromFallowCounter > 0:
                # Distribute fallow MCals proportionally based on initial requirements
                for animalGuid, initial_requirement in animalMCalRequirementMap.items():
                    proportion = initial_requirement / total_animal_mcal_requirement
                    mcal_from_fallow_for_animal = myMCalsFromFallowCounter * proportion
                    # Reduce the animal's requirement by the fallow contribution
                    adjusted_requirement = max(0, initial_requirement - mcal_from_fallow_for_animal)
                    animalMCalRequirementMap[animalGuid] = adjusted_requirement # Update map with adjusted value

                    LaUtils.debug.log(f"  Animal {animalGuid}:", "Diet")
                    LaUtils.debug.log(f"    Initial Requirement: {initial_requirement:.2f} MCal", "Diet")
                    LaUtils.debug.log(f"    Proportion: {proportion:.4f}", "Diet")
                    LaUtils.debug.log(f"    MCals from Fallow: {mcal_from_fallow_for_animal:.2f} MCal", "Diet")
                    LaUtils.debug.log(f"    Adjusted Requirement (Grazing): {adjusted_requirement:.2f} MCal", "Diet")
            else:
                LaUtils.debug.log("  No fallow MCals to distribute or no animal requirement.", "Diet")


            # --- 7. Final Area Target Calculation for Animals ---
            LaUtils.debug.log("Calculating Final Animal Area Targets...", "Diet")
            # Get common land grazing value (MCal/ha/year) - Assuming Ha is the unit
            # C++ uses mCommonLandValue, mCommonLandAreaUnits
            common_land_value_mcal_per_ha = float(self.mCommonLandValue)
            # TODO: Add conversion if mCommonLandAreaUnits is not Hectare

            LaUtils.debug.log(f"Common Land Grazing Value: {common_land_value_mcal_per_ha:.2f} MCal/ha", "Diet")

            if common_land_value_mcal_per_ha > 0:
                for animalGuid, adjusted_requirement in animalMCalRequirementMap.items():
                    animal_area_target_ha = adjusted_requirement / common_land_value_mcal_per_ha

                    # Update the animal report map with the final area target
                    if animalGuid in myAnimalCalcsReportMap:
                        report_string, _ = myAnimalCalcsReportMap[animalGuid]
                        # Append final area target to report
                        report_string += f"\\nFinal Grazing/Fallow Needs:\\n"
                        report_string += f"  Adjusted MCal Requirement: {adjusted_requirement:.2f} MCal\\n"
                        report_string += f"  Common Land Value: {common_land_value_mcal_per_ha:.2f} MCal/ha\\n"
                        report_string += f"  Final Area Target (Common Land): {animal_area_target_ha:.4f} ha\\n"
                        myAnimalCalcsReportMap[animalGuid] = (report_string, animal_area_target_ha)
                        LaUtils.debug.log(f"  Animal {animalGuid}: Final Area Target = {animal_area_target_ha:.4f} ha", "Diet")
                    else:
                         LaUtils.debug.log(f"  Warning: Animal {animalGuid} not found in report map to update area target.", "Warning")
            else:
                LaUtils.debug.log("  Common Land Value is zero. Cannot calculate animal area targets.", "Warning")
                # Set area targets to 0 or infinity? Let's set to 0 and keep the MCal requirement in the report.
                for animalGuid, adjusted_requirement in animalMCalRequirementMap.items():
                     if animalGuid in myAnimalCalcsReportMap:
                        report_string, _ = myAnimalCalcsReportMap[animalGuid]
                        report_string += f"\\nFinal Grazing/Fallow Needs:\\n"
                        report_string += f"  Adjusted MCal Requirement: {adjusted_requirement:.2f} MCal\\n"
                        report_string += f"  Common Land Value: {common_land_value_mcal_per_ha:.2f} MCal/ha\\n"
                        report_string += f"  Final Area Target (Common Land): N/A (Land value is zero)\\n"
                        myAnimalCalcsReportMap[animalGuid] = (report_string, 0.0)


            # --- 8. Set Final Diet Labels ---
            LaUtils.debug.log("Setting final diet labels...", "Diet")
            myDietLabels.dairyMCalories = myOverallDairyMCals
            myDietLabels.cropMCalories = myOverallCropsMCals
            myDietLabels.animalMCalories = myOverallDomesticMeatMCals # Tame meat
            myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
            myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals

            myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.0
            myDietLabels.tameMeatPortionPct = myOverallDomesticMeatPercent * 100.0
            myDietLabels.cropsPortionPct = myOverallCropPercent * 100.0
            myDietLabels.wildAnimalPortionPct = myOverallWildMeatPercent * 100.0
            myDietLabels.wildPlantsPortionPct = myOverallWildPlantPercent * 100.0

            myDietLabels.animalPortionPct = myOverallMeatPercent * 100.0 # Total meat (tame + wild)
            myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.0 # Total plant (crop + wild)

            myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0 # Convert back to kCal
            myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

            myDietLabels.dairySurplus = myOverallDairySurplusMCals

            # Store the report maps
            myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
            myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap

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

        Args:
            theFallowMCalsAvailable: MCals available from fallow land
            theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements
        """
        from la.lib.lautils import LaUtils
        from la.lib.la import Priority

        LaUtils.debug.log(f"Starting fallow grazing land allocation with {theFallowMCalsAvailable:.2f} MCal available", "Diet")

        if theFallowMCalsAvailable <= 0 or not theAnimalMCalRequirementMap:
            LaUtils.debug.log("No fallow land or no animals to allocate to", "Diet")
            return

        # Create maps to hold animals by priority
        highPriorityMap = {}
        mediumPriorityMap = {}
        lowPriorityMap = {}

        # Group animals by fallow access priority
        for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
            if mCalRequirement <= 0:
                continue

            # Get animal parameter
            paramGuid = self.mAnimals.get(animalGuid, "")
            if not paramGuid:
                continue

            animalParameter = LaUtils.getAnimalParameter(paramGuid)
            if not animalParameter:
                continue

            # Get fallow usage priority
            try:
                fallowUsage = getattr(animalParameter, 'fallowUsage', Priority.None_)
                if fallowUsage == Priority.High:
                    highPriorityMap[animalGuid] = mCalRequirement
                elif fallowUsage == Priority.Medium:
                    mediumPriorityMap[animalGuid] = mCalRequirement
                elif fallowUsage == Priority.Low:
                    lowPriorityMap[animalGuid] = mCalRequirement
            except Exception as e:
                LaUtils.debug.log(f"Error getting fallow usage for animal {animalGuid}: {str(e)}", "Error")

        # Track remaining MCals to distribute
        remainingMCals = theFallowMCalsAvailable

        # Allocate to high priority animals first
        if highPriorityMap:
            LaUtils.debug.log(f"Allocating to {len(highPriorityMap)} high priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.High, remainingMCals, highPriorityMap)

        # Then to medium priority animals
        if mediumPriorityMap and remainingMCals > 0:
            LaUtils.debug.log(f"Allocating to {len(mediumPriorityMap)} medium priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.Medium, remainingMCals, mediumPriorityMap)

        # Finally to low priority animals
        if lowPriorityMap and remainingMCals > 0:
            LaUtils.debug.log(f"Allocating to {len(lowPriorityMap)} low priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.Low, remainingMCals, lowPriorityMap)

        LaUtils.debug.log(f"Fallow allocation complete. {remainingMCals:.2f} MCal remains unallocated.", "Diet")

    def doTheFallowAllocation(self, thePriority: Priority, theAvailableFallowValue: float,
                            theAnimalMCalRequirementMap: Dict[str, float]) -> float:
        """Allocate fallow land to animals of a specific priority using match case.

        Args:
            thePriority: Priority level being processed
            theAvailableFallowValue: MCals available from fallow land
            theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements
                                         for the current priority group.

        Returns:
            float: Remaining MCals after allocation
        """
        from la.lib.lautils import LaUtils
        from la.lib.la import Status # Ensure Status enum is imported

        if theAvailableFallowValue <= 0 or not theAnimalMCalRequirementMap:
            LaUtils.debug.log(f"No fallow allocation needed for priority {thePriority.name}. Available: {theAvailableFallowValue}, Animals: {len(theAnimalMCalRequirementMap)}", "Diet")
            return theAvailableFallowValue

        # Calculate total MCals needed by this priority group
        myTotalNeeded = sum(theAnimalMCalRequirementMap.values())
        LaUtils.debug.log(f"Priority {thePriority.name}: Total Needed = {myTotalNeeded:.2f} MCal, Available Fallow = {theAvailableFallowValue:.2f} MCal", "Diet")

        # Determine the fallow status based on C++ logic
        myFallowDifference = theAvailableFallowValue - myTotalNeeded
        myFallowStatus = Status.MoreThanEnoughToCompletelySatisfy if myFallowDifference > 0 else Status.NotEnoughToCompletelySatisfy

        myFallowStatusString = "More than Enough" if myFallowStatus == Status.MoreThanEnoughToCompletelySatisfy else "Not Enough"
        LaUtils.debug.log(f"Fallow Status: {myFallowStatusString}", "Diet")

        myRemainingFallow = 0.0

        # Use match case based on the calculated status
        match myFallowStatus:
            case Status.MoreThanEnoughToCompletelySatisfy:
                LaUtils.debug.log("CASE: MoreThanEnoughToCompletelySatisfy", "Diet")
                # Each animal in this group gets its full requirement met by fallow.
                # Reduce their remaining requirement in the main value map (_mValueMap) to zero.
                for myAnimalGuid, myMCalRequirement in theAnimalMCalRequirementMap.items():
                    if myAnimalGuid in self._mValueMap:
                        # Check if the current requirement is less than or equal to the value in the map
                        # This prevents accidentally reducing requirement below zero if it was already partially met
                        myReduction = min(myMCalRequirement, self._mValueMap[myAnimalGuid])
                        self._mValueMap[myAnimalGuid] -= myReduction
                        # Ensure it doesn't go below zero due to floating point issues
                        self._mValueMap[myAnimalGuid] = max(0, self._mValueMap[myAnimalGuid])
                        LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement fully met by fallow. Reduced by {myReduction:.2f}. Remaining need: {self._mValueMap[myAnimalGuid]:.2f}", "Diet")
                    else:
                        LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in _mValueMap during fallow allocation.", "Warning")

                # Calculate and return the leftover fallow value
                myRemainingFallow = myFallowDifference # or theAvailableFallowValue - totalNeeded
                LaUtils.debug.log(f"Remaining Fallow Value after allocation: {myRemainingFallow:.2f}", "Diet")

            case Status.NotEnoughToCompletelySatisfy:
                LaUtils.debug.log("CASE: NotEnoughToCompletelySatisfy", "Diet")
                # Distribute the available fallow proportionally among animals in this group.
                if myTotalNeeded > 0: # Avoid division by zero
                    for myAnimalGuid, myMCalRequirement in theAnimalMCalRequirementMap.items():
                        if myAnimalGuid in self._mValueMap:
                            # Calculate the proportion of available fallow this animal gets
                            myProportion = myMCalRequirement / myTotalNeeded
                            myAllocatedMCals = theAvailableFallowValue * myProportion
                            LaUtils.debug.log(f"  Animal {myAnimalGuid}: Needs {myMCalRequirement:.2f}, Proportion {myProportion:.4f}, Allocated {myAllocatedMCals:.2f}", "Diet")

                            # Reduce the animal's requirement in the main value map
                            # Check if the current requirement is less than or equal to the value in the map
                            myReduction = min(myAllocatedMCals, self._mValueMap[myAnimalGuid])
                            self._mValueMap[myAnimalGuid] -= myReduction
                            # Ensure it doesn't go below zero
                            self._mValueMap[myAnimalGuid] = max(0, self._mValueMap[myAnimalGuid])
                            LaUtils.debug.log(f"  Animal {myAnimalGuid}: Requirement reduced by {myReduction:.2f}. Remaining need: {self._mValueMap[myAnimalGuid]:.2f}", "Diet")
                        else:
                            LaUtils.debug.log(f"  Animal {myAnimalGuid} not found in _mValueMap during fallow allocation.", "Warning")
                else:
                    LaUtils.debug.log("  Total needed is zero, skipping proportional allocation.", "Diet")

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
