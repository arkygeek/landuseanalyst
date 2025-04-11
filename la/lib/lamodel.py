from qgis.PyQt.QtCore import pyqtSignal, pyqtProperty, QObject # Ensure QObject is imported if not already
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging # Keep standard logging
from typing import Dict, List, Tuple, Union

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType # Added EnergyType
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
        self.mPopulation = "100"
        self.mTotalLandNeeded = "0"

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
        self._mValueMap = {}

        # Diet calculation properties
        self.mAnimals = {}
        self.mCrops = {}
        self.mBaseOnPlants = False
        self.mIncludeDairy = True
        self.mLimitDairy = True
        self.mLimitDairyPercent = 10
        self.mCaloriesPerPersonDaily = 2500
        self.mDairyUtilisation = 100

        # Store calculation results
        self.mLastDietLabels = LaDietLabels()

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
        return self.mLimitDairyPercent
    @limitDairyPercent.setter
    def limitDairyPercent(self, thePercent: int):
        # Ensure the value is within a reasonable range if needed
        # thePercent = max(0, min(100, thePercent))
        if self.mLimitDairyPercent != thePercent:
            self.mLimitDairyPercent = thePercent
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
        return self.mAnimals
    @animals.setter
    def animals(self, theAnimals: Dict[str, str]):
        if self.mAnimals != theAnimals:
            self.mAnimals = theAnimals
            self._animalsChanged.emit()


    @pyqtProperty(str, notify=_cropsChanged) # TODO: check this to see if it is correct
    def crops(self) -> Dict[str, str]: # type: ignore
        return self.mCrops
    @crops.setter
    def crops(self, theCrops: Dict[str, str]):
        if self.mCrops != theCrops:
            self.mCrops = theCrops
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
        self.mLimitDairyPercent = int(root.findtext('limitDairyPercent', default="10"))
        self.mDairyUtilisation = int(root.findtext('dairyUtilisation', default="100"))
        self.mFallowStatus = Status[root.findtext('fallowStatus', default="FALLOW")]
        self.mFallowRatio = int(root.findtext('fallowRatio', default="1"))
        self.mCommonLandValue = float(root.findtext('commonLandValue', default="0.0"))
        self.mCommonLandAreaUnits = AreaUnits[root.findtext('commonLandAreaUnits', default="Hectare")] # Changed default to match enum
        # Added parsing for specific land units and energy type
        self.mSpecificLandAreaUnits = AreaUnits[root.findtext('specificLandAreaUnits', default="Hectare")]
        self.mSpecificLandEnergyType = EnergyType[root.findtext('specificLandEnergyType', default="KCalories")] # Corrected default
        self.mHerdSize = int(root.findtext('herdSize', default="0"))
        self.mAnimals = {}  # Assuming animals are stored in a more complex structure
        self.mCrops = {}  # Assuming crops are stored in a more complex structure
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
        myString += f'  <limitDairyPercent>{self.mLimitDairyPercent}</limitDairyPercent>\\n'
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
            mySelectedAnimalsMap = self.mAnimals  # Similar to C++ QMap<QString,QString>

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
        mySelectedAnimalsMap = self.mAnimals

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
        myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual * 0.001

        LaUtils.debug.log("Diet calculations completed successfully", "Diet")

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


    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """
        Calculate diet values when animals are prioritized and dairy is separate from meat.

        This method performs a detailed calculation of dietary requirements for a settlement,
        prioritizing animal-based food sources (meat and dairy) while treating dairy as a
        separate category from meat. It calculates the required caloric contributions from
        various food sources (animals, crops, wild plants) and determines the land area
        needed to meet these requirements.

        Returns:
            LaDietLabels: An object containing the calculated dietary labels, including
                          percentages, caloric contributions, and area targets for crops
                          and animals.

        Key Steps:
            1. Input Parameter Extraction:
               - Extracts and logs input parameters such as daily caloric needs, population,
                 diet percentages, and utilization rates.

            2. Initial Caloric Calculations:
               - Calculates the total annual caloric needs for the settlement and initializes
                 counters for dairy, meat, crops, and wild plants.

            3. Animal-Based Food Calculations:
               - Iterates through the list of animals to calculate their contributions to
                 meat and dairy portions of the diet.
               - Determines herd sizes, feed requirements, and caloric contributions from
                 meat and dairy.
               - Accounts for fodder and grain needs for animals and adjusts caloric
                 requirements accordingly.

            4. Dairy Portion Adjustment:
               - Adjusts the dairy portion based on utilization limits and recalculates
                 percentages for meat, dairy, and plant-based food sources.

            5. Crop-Based Food Calculations:
               - Iterates through the list of crops to calculate their contributions to the
                 diet.
               - Determines the area needed for crop production, accounting for spoilage,
                 reseeding, and fallow land requirements.

            6. Fallow Land Allocation:
               - Allocates fallow land for grazing and adjusts animal caloric requirements
                 based on the contribution of fallow land.

            7. Final Area Target Calculation:
               - Calculates the final land area targets for animals and crops, considering
                 adjusted caloric requirements and land productivity values.

            8. Final Diet Labels:
               - Sets the final dietary labels, including caloric contributions, percentages,
                 and area targets for crops and animals.

        Exceptions:
            - Logs and handles any exceptions that occur during the calculation process,
              providing detailed error messages and stack traces.

        Notes:
            - This method relies on several external utility functions and data structures
              (e.g., LaUtils, LaDietLabels) for calculations and logging.
            - The calculations are based on a detailed model that includes parameters such
              as breeding cycles, feed requirements, spoilage rates, and land productivity.

        """

        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsAnimalsFirstDairySeparate calculation", "Diet")

        try:
            # Get base values from internal attributes
            calories_daily = float(self.mCaloriesPerPersonDaily)
            population_count = float(self.mPopulation)
            meat_percent = float(self.mMeatPercent) / 100.0  # Convert to decimal
            diet_percent = float(self.mDietPercent) / 100.0  # Convert to decimal
            dairy_utilisation = float(self.mDairyUtilisation) / 100.0 # Convert to decimal
            limit_dairy_percent = float(self.mLimitDairyPercent) / 100.0 # Convert to decimal
            limit_dairy_bool = bool(self.mLimitDairy)
            plant_percent = 1.0 - diet_percent # Overall plant portion
            domestic_crop_portion = float(self.mPercentOfDietThatIsFromCrops) / 100.0 # Convert to decimal

            LaUtils.debug.log(f"Input parameters - calories_daily: {calories_daily}, population: {population_count}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {meat_percent*100}%, diet_percent: {diet_percent*100}%", "Diet")
            LaUtils.debug.log(f"Dairy parameters - utilisation: {dairy_utilisation*100}%, limit: {limit_dairy_bool}, limit_percent: {limit_dairy_percent*100}%", "Diet")
            LaUtils.debug.log(f"Plant parameters - plant_percent: {plant_percent*100}%, domestic_crop_portion: {domestic_crop_portion*100}%", "Diet")

            # Calculate basic values
            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

            LaUtils.debug.log(f"myMCalsIndividualAnnual = {myMCalsIndividualAnnual}", "Diet")
            LaUtils.debug.log(f"myMCalsSettlementAnnual = {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters
            myDairyMCalorieCounter = 0.0
            myTameMeatMCalorieCounter = 0.0
            myWildMeatCounter = myMCalsSettlementAnnual * diet_percent * (1.0 - meat_percent)  # Wild meat portion (initial estimate)
            myCropCounter = 0.0 # Will be calculated later
            myWildPlantCounter = 0.0 # Will be calculated later

            LaUtils.debug.log(f"Initial myDairyMCalorieCounter = {myDairyMCalorieCounter}", "Diet")
            LaUtils.debug.log(f"Initial myTameMeatMCalorieCounter = {myTameMeatMCalorieCounter}", "Diet")
            LaUtils.debug.log(f"Initial myWildMeatCounter = {myWildMeatCounter}", "Diet")

            # Create report maps for crops and animals
            cropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}
            # Map to store animal requirements for fallow allocation
            animalMCalRequirementMap = {}
            # Map to store fodder needs per crop
            fodderNeedsPerCrop = {}

            # Populate animal report map with detailed calculations
            for myAnimalGuid, paramGuid in self.mAnimals.items():
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                LaUtils.debug.log("--------==        Looping through the animals         ==-------", "Diet")
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                try:
                    animal = LaUtils.getAnimal(myAnimalGuid)
                    animalParameter = LaUtils.getAnimalParameter(paramGuid)

                    # Initialize variables at the start
                    myAnimalReport = ""
                    myAnimalHerdMCalsRequired = 0.0

                    if animal and animalParameter:
                        LaUtils.debug.log(f"Processing animal: {animal.name} (GUID: {myAnimalGuid})", "Diet")

                        # Get animal values safely
                        myMilkKgPerDay = float(str(animal.milkGramsPerDay)) * 0.001  # Convert g to kg
                        myMilkFoodValue = float(str(animal.milkFoodValue)) * 0.001   # Convert to MCal/kg
                        myLactationTime = float(str(animal.lactationTime))
                        myWeaningAge = float(str(animal.weaningAge))
                        myGestatingTime = float(str(animal.gestationTime))
                        myEstrousCycle = float(str(animal.estrousCycle))
                        myBabiesPerBirth = float(str(animal.youngPerBirth))
                        myDeathRate = float(str(animal.deathRate)) * 0.01  # Convert from percent
                        myBreedingRatio = float(str(animal.femalesPerMale)) # Same as myFemalesToMales

                        # Check for zero breeding ratio to avoid division by zero
                        if myBreedingRatio <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has a breeding ratio of {myBreedingRatio}, using default of 1.0", "Warning")
                            myBreedingRatio = 1.0  # Default to 1 if zero or negative

                        myKillWeight = float(str(animal.killWeight))
                        myUsablePortionOfAnimal = float(str(animal.usableMeat)) * 0.01  # Convert from percent
                        myAdultWeight = float(str(animal.adultWeight))
                        myFemalesToMales = myBreedingRatio # Use the validated value
                        myConceptionEfficiency = float(str(animal.conceptionEfficiency)) * 0.01  # Convert from percent
                        myMeatValueMCal = float(str(animal.meatFoodValue)) * 0.001  # Convert to MCal/kg
                        mySexualMaturity = float(str(animal.sexualMaturity)) # in months
                        myBreedingYears = float(str(animal.breedingExpectancy)) # in years

                        # Get parameter values
                        myAnimalContributionToMeatPortion = 0.0 # B2
                        try:
                            myAnimalContributionToMeatPortion = float(str(animalParameter.percentTameMeat)) * 0.01
                        except:
                            myAnimalContributionToMeatPortion = 1.0 / len(self.mAnimals) if len(self.mAnimals) > 0 else 0.0

                        # Calculate animal targets using the C++ approach
                        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * diet_percent * meat_percent # B3
                        myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * max(0, (myLactationTime - myWeaningAge)) # B4 - Ensure non-negative time
                        myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal # B5
                        myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * dairy_utilisation # B6

                        # Calculate birthing events per year, handling edge case for too many days
                        cycle_length = myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime
                        myBirthingEventsPerYear1 = 365.0 / cycle_length if cycle_length > 0 else 0 # B21
                        myBirthingEventsPerYear = max(1.0, myBirthingEventsPerYear1) # Ensure at least 1 event if cycle is very short or zero

                        # Calculate culled mothers value
                        breeding_life_years = (mySexualMaturity / 12.0) + myBreedingYears
                        myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal *
                                                (1.0 / breeding_life_years)) if breeding_life_years > 0 else 0
                        myCulledMothersValue = (myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear)) if (myBabiesPerBirth * myBirthingEventsPerYear) > 0 else 0 # B7

                        # Calculate culled adult males value
                        myCulledAdultMalesValue = myCulledMothersValue / myFemalesToMales if myFemalesToMales > 0 else 0 # B8

                        # Calculate final offspring value
                        myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue # B9

                        # Calculate number of offspring needed per year
                        myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue if myFinalOffspringValue > 0 else 0 # B11

                        # Calculate MCals from meat and utilized from dairy
                        myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue # B12
                        myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear # B14

                        # Add to the diet counters
                        myTameMeatMCalorieCounter += myMCalsFromTheMeat
                        myDairyMCalorieCounter += myMCalsUtilizedFromDairy

                        # Calculate meat and dairy percentages for this animal (relative to total settlement needs)
                        myMeatPercent = myMCalsFromTheMeat / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B15
                        myDairyPercent = myMCalsUtilizedFromDairy / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B16

                        # Calculate herd size based on birthing cycles
                        myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1.0 - myDeathRate) * myConceptionEfficiency # B22

                        # Check for zero offspring per mother per year to avoid division by zero
                        if myOffspringPerMotherPerYear <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has zero or negative offspring per mother per year calculation ({myOffspringPerMotherPerYear}). Using default value of 1.0", "Warning")
                            myOffspringPerMotherPerYear = 1.0  # Default to 1 if zero or negative

                        myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear # B23
                        myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5 # B24
                        myFemalesStepOne = myMalesStepOne # B25
                        myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity / 12.0)) / myBreedingYears if myBreedingYears > 0 else 0 # B26
                        # Match original C++ implementation exactly for breeding males
                        myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio if myBreedingRatio > 0 else 0 # B27
                        myAdditionalMothers = ((myReplacementMothersPerYear / myOffspringPerMotherPerYear) * 2.0) + (myBreedingMalesRequired * 2.0) if myOffspringPerMotherPerYear > 0 else (myBreedingMalesRequired * 2.0) # B28

                        myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5 # B29
                        myFemalesStepTwo = myMalesStepTwo # B30
                        myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear # B32
                        myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo # B33
                        myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo # B34 - Note: C++ has '-' here, seems correct for replacements
                        myTotalOffspring = myTotalMaleOffspring * 2.0 # B35 - C++ comment says '+ myTotalFemaleOffspring' but code uses '* 2.0'

                        # Calculate feed requirements
                        myFeedForGestating = float(str(animal.gestating)) * 0.001 # MCal/day
                        myFeedForLactating = float(str(animal.lactating)) * 0.001 # MCal/day
                        myFeedForMaintenance = float(str(animal.maintenance)) * 0.001 # MCal/day
                        myFeedForOffspringPerKg = float(str(animal.juvenile)) * 0.001 # MCal/day/kg

                        myGestatingMCals = myTotalMothers * myGestatingTime * myFeedForGestating # C++ uses myTotalOffspring here, seems incorrect. Using myTotalMothers.
                        myLactatingMCals = myTotalMothers * myLactationTime * myFeedForLactating # C++ uses myTotalOffspring here, seems incorrect. Using myTotalMothers.
                        myDaysForMaintenance = max(0, 365.0 - (myGestatingTime + myLactationTime))

                        myDryMothers = max(0, myTotalMothers - myTotalOffspring) # C++ logic
                        myDryMothersMCals = myDryMothers * 365.0 * myFeedForMaintenance
                        myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance # C++ logic
                        myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals

                        myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.0
                        myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * max(0, (365.0 - myWeaningAge))

                        # Set the total herd requirements in MCal per year (before fodder/fallow)
                        myAnimalHerdMCalsRequired1 = (myGestatingMCals + myLactatingMCals +
                                                   myMaintenanceMCals + myAdultMalesMCals +
                                                   myOffspringMCals)

                        # Calculate fodder needs and adjust crop requirements
                        myAdditionalMCalCounter = 0.0 # MCal provided by fodder/grain
                        myFoodSourceMap = animalParameter.fodderSourceMap()
                        LaUtils.debug.log(f"    ----==--------------------------------------------==----", "Diet")
                        LaUtils.debug.log(f"    ----==          Adding to the fodder Map          ==----", "Diet")
                        LaUtils.debug.log(f"    ----==--------------------------------------------==----", "Diet")
                        for myCropGuid, myFoodSource in myFoodSourceMap.items():
                            LaUtils.debug.log(f"Processing fodder source: Crop GUID {myCropGuid}", "Diet")
                            myCrop = LaUtils.getCrop(myCropGuid)
                            if not myCrop:
                                LaUtils.debug.log(f"        Crop {myCropGuid} not found for fodder source.", "Warning")
                                continue

                            myGrain = float(str(myFoodSource.grain)) * 0.001 # kg/day
                            myFodder = float(str(myFoodSource.fodder)) * 0.001 # kg/day
                            myDays = float(str(myFoodSource.days))
                            myFoodValueOfCrop = float(str(myCrop.cropCalories)) * 0.001 # MCal/kg
                            myFoodValueofFodder = float(str(myCrop.cropFodderValue)) * 0.001 # MCal/kg

                            # Calculate total kg of grain needed from this crop for the entire herd
                            # Note: C++ calculates grain *per offspring*, which seems wrong. Calculating per animal in herd.
                            total_herd_size_for_fodder = myTotalMothers + myBreedingMalesRequired + myTotalOffspring
                            myGrainToAddKg = myGrain * myDays * total_herd_size_for_fodder
                            myFodderToAddKg = myFodder * myDays * total_herd_size_for_fodder

                            # Add grain requirement to the crop's fodder map
                            if myCropGuid not in fodderNeedsPerCrop:
                                fodderNeedsPerCrop[myCropGuid] = 0.0
                            fodderNeedsPerCrop[myCropGuid] += myGrainToAddKg
                            LaUtils.debug.log(f"        myGrain = {myGrain}", "Diet")
                            LaUtils.debug.log(f"        myFodder = {myFodder}", "Diet")
                            LaUtils.debug.log(f"        myDays = {myDays}", "Diet")
                            LaUtils.debug.log(f"        Grain to add (kg) for {animal.name} from {myCrop.name}: {myGrainToAddKg}", "Diet")
                            LaUtils.debug.log(f"        Current total grain needed for {myCrop.name}: {fodderNeedsPerCrop[myCropGuid]}", "Diet")

                            # Calculate MCal provided by this fodder/grain source
                            myGrainMCal = myGrainToAddKg * myFoodValueOfCrop
                            myFodderMCal = myFodderToAddKg * myFoodValueofFodder
                            myAdditionalMCalCounter += myGrainMCal + myFodderMCal
                            LaUtils.debug.log(f"        Food Value of the Crop: {myFoodValueOfCrop}", "Diet")
                            LaUtils.debug.log(f"        Food Value of the Fodder: {myFoodValueofFodder}", "Diet")
                            LaUtils.debug.log(f"        myGrainMCal = {myGrainMCal}", "Diet")
                            LaUtils.debug.log(f"        myFodderMCal = {myFodderMCal}", "Diet")
                            LaUtils.debug.log(f"        Crop Name: {myCrop.name}", "Diet")
                            LaUtils.debug.log(f"        Total MCals counted so far for grain/fodder feeding this animal: {myAdditionalMCalCounter}", "Diet")

                        # Adjust herd MCal requirement based on fodder/grain contribution
                        myAnimalHerdMCalsRequired = myAnimalHerdMCalsRequired1 - myAdditionalMCalCounter
                        LaUtils.debug.log(f"  ---- AnimalHerd MCals Required before accounting for grain/fodder feeding: {myAnimalHerdMCalsRequired1}", "Diet")
                        LaUtils.debug.log(f"  ---- AnimalHerd MCals Required *AFTER* accounting for grain/fodder feeding: {myAnimalHerdMCalsRequired}", "Diet")

                        # Store the initial requirement for fallow allocation
                        animalMCalRequirementMap[myAnimalGuid] = myAnimalHerdMCalsRequired

                        # Build the detailed report string
                        myAnimalReport = f"myMilkKgPerDay = {myMilkKgPerDay}\n"
                        myAnimalReport += f"myMilkFoodValue = {myMilkFoodValue}\n"
                        myAnimalReport += f"myLactationTime = {myLactationTime}\n"
                        myAnimalReport += f"myWeaningAge = {myWeaningAge}\n"
                        myAnimalReport += f"myKillWeight = {myKillWeight}\n"
                        myAnimalReport += f"myUsablePortionOfAnimal = {myUsablePortionOfAnimal}\n"
                        myAnimalReport += f"myAdultWeight = {myAdultWeight}\n"
                        myAnimalReport += f"myFemalesToMales = {myFemalesToMales}\n"
                        myAnimalReport += f"myMeatValueMCal = {myMeatValueMCal}\n"
                        myAnimalReport += f"mySexualMaturity = {mySexualMaturity}\n"
                        myAnimalReport += f"myBreedingYears = {myBreedingYears}\n"
                        myAnimalReport += f"myAnimalContributionToMeatPortion = {myAnimalContributionToMeatPortion}\n"
                        myAnimalReport += f"myAnimalMCalTarget = {myAnimalMCalTarget}\n"
                        myAnimalReport += f"myPotentialDairyPerOffspring = {myPotentialDairyPerOffspring}\n"
                        myAnimalReport += f"myValuePerOffspring = {myValuePerOffspring}\n"
                        myAnimalReport += f"myActualDairyValueOfOffspring = {myActualDairyValueOfOffspring}\n"
                        myAnimalReport += f"myCulledMothersValue = {myCulledMothersValue}\n"
                        myAnimalReport += f"myCulledAdultMalesValue = {myCulledAdultMalesValue}\n"
                        myAnimalReport += f"myFinalOffspringValue = {myFinalOffspringValue}\n"
                        myAnimalReport += f"myOffspringNeededPerYear = {myOffspringNeededPerYear}\n"
                        myAnimalReport += f"myMCalsFromTheMeat = {myMCalsFromTheMeat}\n"
                        myAnimalReport += f"myMCalsUtilizedFromDairy = {myMCalsUtilizedFromDairy}\n"
                        myAnimalReport += f"myTameMeatMCalorieCounter (cumulative) = {myTameMeatMCalorieCounter}\n"
                        myAnimalReport += f"myDairyMCalorieCounter (cumulative) = {myDairyMCalorieCounter}\n"
                        myAnimalReport += "\n"
                        myAnimalReport += f"myBirthingEventsPerYear = {myBirthingEventsPerYear}\n"
                        myAnimalReport += f"myOffspringPerMotherPerYear = {myOffspringPerMotherPerYear}\n"
                        myAnimalReport += f"myMothersNeededStepOne = {myMothersNeededStepOne}\n"
                        myAnimalReport += f"myMalesStepOne = {myMalesStepOne}\n"
                        myAnimalReport += f"myFemalesStepOne = {myFemalesStepOne}\n"
                        myAnimalReport += f"myReplacementMothersPerYear = {myReplacementMothersPerYear}\n"
                        myAnimalReport += f"myBreedingMalesRequired = {myBreedingMalesRequired}\n"
                        myAnimalReport += f"myAdditionalMothers = {myAdditionalMothers}\n"
                        myAnimalReport += f"myMalesStepTwo = {myMalesStepTwo}\n"
                        myAnimalReport += f"myFemalesStepTwo = {myFemalesStepTwo}\n"
                        myAnimalReport += "\n"
                        myAnimalReport += f"myTotalMothers = {myTotalMothers}\n"
                        myAnimalReport += f"myTotalMaleOffspring = {myTotalMaleOffspring}\n"
                        myAnimalReport += f"myTotalFemaleOffspring = {myTotalFemaleOffspring}\n"
                        myAnimalReport += f"myTotalOffspring = {myTotalOffspring}\n"
                        myAnimalReport += f"myFeedForGestating = {myFeedForGestating}\n"
                        myAnimalReport += f"myFeedForLactating = {myFeedForLactating}\n"
                        myAnimalReport += f"myFeedForMaintenance = {myFeedForMaintenance}\n"
                        myAnimalReport += f"myFeedForOffspringPerKg = {myFeedForOffspringPerKg}\n"
                        myAnimalReport += f"myGestatingMCals = {myGestatingMCals}\n"
                        myAnimalReport += f"myLactatingMCals = {myLactatingMCals}\n"
                        myAnimalReport += f"myDaysForMaintenance = {myDaysForMaintenance}\n"
                        myAnimalReport += f"myGestatingTime = {myGestatingTime}\n"
                        myAnimalReport += f"myLactationTime = {myLactationTime}\n"
                        myAnimalReport += f"myDryMothers = {myDryMothers}\n"
                        myAnimalReport += f"myDryMothersMCals = {myDryMothersMCals}\n"
                        myAnimalReport += f"myOtherMaintenanceMCals = {myOtherMaintenanceMCals}\n"
                        myAnimalReport += f"myMaintenanceMCals = {myMaintenanceMCals}\n"
                        myAnimalReport += f"myAdultMalesMCals = {myAdultMalesMCals}\n"
                        myAnimalReport += f"myOffspringMCals = {myOffspringMCals}\n"
                        myAnimalReport += f"myAnimalHerdMCalsRequired1 (Before Fodder) = {myAnimalHerdMCalsRequired1}\n"
                        myAnimalReport += f"myAnimalHerdMCalsRequired (After Fodder) = {myAnimalHerdMCalsRequired}\n"
                        myAnimalReport += ".........................\n"
                        myAnimalReport += ".        Summary        .\n"
                        myAnimalReport += ".........................\n"
                        myAnimalReport += f"MCal Target (Meat) = {myMCalsFromTheMeat}\n"
                        myAnimalReport += f"Dairy Contribution = {myMCalsUtilizedFromDairy}\n"
                        myAnimalReport += f"Meat Percent (of total) = {myMeatPercent*100.:.2f}%\n"
                        myAnimalReport += f"Dairy Percent (of total) = {myDairyPercent*100.:.2f}%\n"
                        myAnimalReport += f"Number of Offspring = {myTotalOffspring}\n"
                        myAnimalReport += f"Number of Mothers = {myTotalMothers}\n"
                        myAnimalReport += f"Number of Breeding Males = {myBreedingMalesRequired}\n"

                        # Store the report and the *initial* MCal requirement (before fallow)
                        # The second value will be updated later with the final area target
                        myAnimalCalcsReportMap[myAnimalGuid] = (myAnimalReport, myAnimalHerdMCalsRequired)
                        LaUtils.debug.log(f"Added detailed animal calculation for {animal.name}", "Diet")
                    else:
                        LaUtils.debug.log(f"Missing animal or animal parameter for GUID {myAnimalGuid}", "Warning")

                except Exception as e:
                    LaUtils.debug.log(f"Error in animal calculation for GUID {myAnimalGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # ----------- Dairy Portion Calculation (Post Animal Loop) ------------
            LaUtils.debug.log("Calculating final diet portions...", "Diet")
            myDairyLimit = limit_dairy_percent if limit_dairy_bool else 1.0 # B22
            myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B11
            myWildMeatPercent = (1.0 - meat_percent) * diet_percent # B13 - Recalculate based on total diet percent
            myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0 # B21
            myNewLimit = (1.0 - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit # B20
            myPotentialDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0
            myPotentialDairyLessThanLimitBool = myPotentialDairyPercent < myDairyLimit # B19
            myNewDairyMCals = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual # B18
            myOverallDairyPercent = myNewDairyMCals / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B12 & B8

            # --- Calculate final Plant/Crop percentages ---
            myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent # B7
            myOverallPlantPercent = max(0, 1.0 - myOverallMeatPercent - myOverallDairyPercent) # B6 - Ensure non-negative
            myOverallCropPercent = myOverallPlantPercent * domestic_crop_portion # B14
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - domestic_crop_portion) # B15 - Adjusted logic

            # --- Calculate final MCals for each category ---
            myOverallDomesticMeatMCals = myTameMeatMCalorieCounter # B25
            myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual # B26
            myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual # B27
            myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual # B28
            myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual # B29
            myOverallMeatMCals = myOverallWildMeatMCals + myOverallDomesticMeatMCals # For reporting

            # --- Calculate Dairy Surplus ---
            myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
            myOverallDairySurplusMCals = max(0, myFirstDairySurplusBool)

            LaUtils.debug.log(f"myDairyLimit = {myDairyLimit}", "Diet")
            LaUtils.debug.log(f"myDomesticMeatPercent = {myDomesticMeatPercent}", "Diet")
            LaUtils.debug.log(f"myWildMeatPercent = {myWildMeatPercent}", "Diet")
            LaUtils.debug.log(f"myLimitSatisfies = {myLimitSatisfies}", "Diet")
            LaUtils.debug.log(f"myNewLimit = {myNewLimit}", "Diet")
            LaUtils.debug.log(f"myPotentialDairyLessThanLimitBool = {myPotentialDairyLessThanLimitBool}", "Diet")
            LaUtils.debug.log(f"myNewDairyMCals = {myNewDairyMCals}", "Diet")
            LaUtils.debug.log(f"myOverallDairyPercent = {myOverallDairyPercent}", "Diet")
            LaUtils.debug.log(f"myOverallMeatPercent = {myOverallMeatPercent}", "Diet")
            LaUtils.debug.log(f"myOverallPlantPercent = {myOverallPlantPercent}", "Diet")
            LaUtils.debug.log(f"myOverallCropPercent = {myOverallCropPercent}", "Diet")
            LaUtils.debug.log(f"myOverallWildPlantPercent = {myOverallWildPlantPercent}", "Diet")
            LaUtils.debug.log(f"myOverallDomesticMeatMCals = {myOverallDomesticMeatMCals}", "Diet")
            LaUtils.debug.log(f"myOverallDairyMCals = {myOverallDairyMCals}", "Diet")
            LaUtils.debug.log(f"myOverallWildMeatMCals = {myOverallWildMeatMCals}", "Diet")
            LaUtils.debug.log(f"myOverallCropsMCals = {myOverallCropsMCals}", "Diet")
            LaUtils.debug.log(f"myOverallWildPlantsMCals = {myOverallWildPlantsMCals}", "Diet")
            LaUtils.debug.log(f"myOverallMeatMCals = {myOverallMeatMCals}", "Diet")
            LaUtils.debug.log(f"myFirstDairySurplusBool = {myFirstDairySurplusBool}", "Diet")
            LaUtils.debug.log(f"myOverallDairySurplusMCals = {myOverallDairySurplusMCals}", "Diet")

            # ----------- Crop Calculation Loop -----------
            myMCalsFromFallowCounter = 0.0
            for myCropGuid, paramGuid in self.mCrops.items():
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                LaUtils.debug.log("**********         Looping through the crops          **********", "Diet")
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                try:
                    myCrop = LaUtils.getCrop(myCropGuid)
                    cropParameter = LaUtils.getCropParameter(paramGuid)

                    if myCrop and cropParameter:
                        myCropPortion = float(str(cropParameter.percentTameCrop)) * 0.01
                        LaUtils.debug.log(f"          myCropPortion = {myCropPortion}", "Diet")
                        myCropFoodValue = float(str(myCrop.cropCalories)) * 0.001  # MCal/kg
                        LaUtils.debug.log(f"          myCropFoodValue = {myCropFoodValue}", "Diet")
                        # Calculate this crop's MCal target based on its portion of the overall crop MCal target
                        myMCalsFromTheCrop = myCropPortion * myOverallCropsMCals
                        LaUtils.debug.log(f"          myOverallCropPercent = {myOverallCropPercent}", "Diet")
                        LaUtils.debug.log(f"          myMCalsFromTheCrop = {myMCalsFromTheCrop}", "Diet")

                        # Calculate kg needed for people (initial calculation before adjustments)
                        myKgForPeople1 = myMCalsFromTheCrop / myCropFoodValue if myCropFoodValue > 0 else 0

                        # Get spoilage and reseeding percentages
                        mySpoilagePercent = float(str(cropParameter.spoilage)) * 0.01
                        myReseedPercent = float(str(cropParameter.reseed)) * 0.01

                        # Calculate additional kg needed for spoilage and reseeding for people
                        myKgForPeopleSpoilage = myKgForPeople1 * mySpoilagePercent
                        myKgForPeopleReseed = myKgForPeople1 * myReseedPercent
                        myKgForPeople = myKgForPeople1 + myKgForPeopleSpoilage + myKgForPeopleReseed

                        # Get additional kg needed for animal fodder/grain from the map populated earlier
                        myAnimalKgAdd1 = fodderNeedsPerCrop.get(myCropGuid, 0.0)

                        # Adjust animal fodder/grain needs for spoilage and reseeding
                        myAnimalKgAddSpoilage = myAnimalKgAdd1 * mySpoilagePercent
                        myAnimalKgAddReseed = myAnimalKgAdd1 * myReseedPercent
                        myAnimalKgAdd = myAnimalKgAdd1 + myAnimalKgAddSpoilage + myAnimalKgAddReseed

                        # Total production target (kg) for this crop
                        myAdjustedTarget = myKgForPeople + myAnimalKgAdd
                        LaUtils.debug.log(f"          myKgForPeople1 = {myKgForPeople1}", "Diet")
                        LaUtils.debug.log(f"          myAnimalKgAdd1 = {myAnimalKgAdd1}", "Diet")
                        LaUtils.debug.log(f"          mySpoilagePercent = {mySpoilagePercent}", "Diet")
                        LaUtils.debug.log(f"          myReseedPercent = {myReseedPercent}", "Diet")
                        LaUtils.debug.log(f"          myKgForPeople = {myKgForPeople}", "Diet")
                        LaUtils.debug.log(f"          myAnimalKgAdd = {myAnimalKgAdd}", "Diet")
                        LaUtils.debug.log(f"          myAdjustedTarget = {myAdjustedTarget}", "Diet")

                        # Calculate area needed based on yield
                        myCropYield = float(str(myCrop.cropYield)) # kg/area_unit
                        # Adjust yield to kg/hectare if necessary
                        if hasattr(myCrop, 'areaUnits') and str(myCrop.areaUnits) == "Dunum":
                            myCropYield = myCropYield * 10.0  # Convert from Dunum to hectare
                        LaUtils.debug.log(f"          myCrop.cropYield() = {myCrop.cropYield}", "Diet")
                        LaUtils.debug.log(f"          myCropYield (kg/ha) = {myCropYield}", "Diet")

                        # Calculate initial crop area target (before fallow)
                        myCropAreaTarget1 = myAdjustedTarget / myCropYield if myCropYield > 0 else 0

                        # Calculate fallow land area and MCals if applicable
                        myFallowArea = 0.0
                        myFallowMCals = 0.0
                        myTotalAreaNeeded = myCropAreaTarget1 # Start with crop area

                        if hasattr(cropParameter, 'fallowRatio') and float(str(cropParameter.fallowRatio)) > 0:
                            myRatio = float(str(cropParameter.fallowRatio))
                            myFallowValue = float(str(cropParameter.fallowValue)) # MCal/ha (assuming fallow value is per hectare)

                            # C++ calculates fallow area based on *total* area, which requires solving:
                            # TotalArea = CropArea + FallowArea = CropArea + CropArea * Ratio
                            # CropArea = TotalArea / (1 + Ratio)
                            # FallowArea = TotalArea * Ratio / (1 + Ratio)
                            # We have CropArea (myCropAreaTarget1), so:
                            # TotalArea = myCropAreaTarget1 * (1 + myRatio)
                            # FallowArea = myCropAreaTarget1 * myRatio
                            myFallowArea = myCropAreaTarget1 * myRatio
                            myTotalAreaNeeded = myCropAreaTarget1 + myFallowArea
                            myFallowMCals = myFallowArea * myFallowValue
                            myMCalsFromFallowCounter += myFallowMCals
                            LaUtils.debug.log(f"          Fallow Ratio = {myRatio}", "Diet")
                            LaUtils.debug.log(f"          Fallow Value = {myFallowValue}", "Diet")
                            LaUtils.debug.log(f"          Crop Area (before fallow) = {myCropAreaTarget1}", "Diet")
                            LaUtils.debug.log(f"          Fallow Area = {myFallowArea}", "Diet")
                            LaUtils.debug.log(f"          Total Area Needed = {myTotalAreaNeeded}", "Diet")
                            LaUtils.debug.log(f"          Fallow MCals = {myFallowMCals}", "Diet")
                        else:
                            LaUtils.debug.log(f"          No fallow for this crop.", "Diet")

                        # Create detailed report for this crop
                        cropReport = f"MCals People = {myMCalsFromTheCrop:.2f}\n"
                        cropReport += f"myCropPortion = {myCropPortion:.4f}\n"
                        cropReport += f"myCropFoodValue = {myCropFoodValue:.4f}\n"
                        cropReport += f"myOverallCropPercent = {myOverallCropPercent:.4f}\n"
                        # cropReport += f"myCropPercent = {myCropPercent:.4f}\n" # This was calculated differently in C++
                        cropReport += f"myMCalsFromTheCrop = {myMCalsFromTheCrop:.2f}\n"
                        cropReport += f"myAnimalKgAdd = {myAnimalKgAdd:.2f}\n"
                        cropReport += f"myAdjustedTarget = {myAdjustedTarget:.2f}\n"
                        cropReport += f"myCrop.cropYield() = {myCrop.cropYield}\n"
                        cropReport += f"myCropYield (kg/ha) = {myCropYield:.2f}\n"
                        cropReport += f"Crop Production People before adjusting= {myKgForPeople1:.2f}\n"
                        cropReport += f"Extra Kg to account for spoilage= {myKgForPeopleSpoilage:.2f}\n"
                        cropReport += f"Extra Kg to account for reseeding= {myKgForPeopleReseed:.2f}\n"
                        cropReport += f"Crop Production People after adjusting= {myKgForPeople:.2f}\n"
                        cropReport += f"Crop Production Animal before adjusting= {myAnimalKgAdd1:.2f}\n"
                        cropReport += f"Extra Kg to account for spoilage= {myAnimalKgAddSpoilage:.2f}\n"
                        cropReport += f"Extra Kg to account for reseeding= {myAnimalKgAddReseed:.2f}\n"
                        cropReport += f"Crop Production Animal after adjusting= {myAnimalKgAdd:.2f}\n"
                        # cropReport += f"myCropAreaTarget People = {myCropAreaTargetPeople:.2f}\n" # Not calculated in C++ report
                        # cropReport += f"myCropAreaTarget Animals= {myCropAreaTargetAnimals:.2f}\n" # Not calculated in C++ report
                        cropReport += f"myCropAreaTarget (Total Area) = {myTotalAreaNeeded:.2f}\n"
                        cropReport += "\n"
                        cropReport += f"Kg for People = {myKgForPeople:.2f}\n"
                        cropReport += f"KG for Animals = {myAnimalKgAdd:.2f}\n"
                        # cropReport += f"Percent of Diet = {myCropPercent * 100.:.2f}%\n" # Calculated differently
                        # cropReport += f"Area Target People: {myCropAreaTargetPeople:.2f}\n" # Not calculated
                        # cropReport += f"Area Target Animal: {myCropAreaTargetAnimals:.2f}\n" # Not calculated
                        cropReport += f"Area Target is {myTotalAreaNeeded:.2f}\n"
                        cropReport += f"myFallowValue = {myFallowValue:.2f}\n"
                        cropReport += f"MCals from Fallow: {myFallowMCals:.2f}\n"

                        # Store the report and the final area target
                        cropCalcsReportMap[myCropGuid] = (cropReport, myTotalAreaNeeded)
                        LaUtils.debug.log(f"Added crop calculation for {myCrop.name}", "Diet")
                    else:
                        LaUtils.debug.log(f"Missing crop or crop parameter for GUID {myCropGuid}", "Warning")

                except Exception as e:
                    LaUtils.debug.log(f"Error creating crop report for GUID {myCropGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # ----------- Fallow Allocation -----------
            LaUtils.debug.log(f"Total MCals from fallow: {myMCalsFromFallowCounter}", "Diet")
            if myMCalsFromFallowCounter > 0:
                # Use the _mValueMap for allocation as it holds the requirements
                self._mValueMap = animalMCalRequirementMap.copy() # Initialize _mValueMap with current requirements
                self.allocateFallowGrazingLand(myMCalsFromFallowCounter, self._mValueMap)
                # animalMCalRequirementMap now holds the *adjusted* requirements after fallow
                animalMCalRequirementMap = self._mValueMap.copy() # Update the map with adjusted values

            # ----------- Final Animal Area Target Calculation -----------
            LaUtils.debug.log("--------==---------------------------------------------==-------", "Diet")
            LaUtils.debug.log("--------==        Looping to Update Animal Map         ==-------", "Diet")
            LaUtils.debug.log("--------==---------------------------------------------==-------", "Diet")
            myFinalAnimalAreaTargets = {} # Store final area targets separately
            for myAnimalGuid, myReportPair in myAnimalCalcsReportMap.items():
                try:
                    myReport, _ = myReportPair # Original report, second value is initial MCal req
                    myAdjustedMCalTarget = animalMCalRequirementMap.get(myAnimalGuid, 0.0) # Get requirement *after* fallow
                    LaUtils.debug.log(f"        *** Processing animal {myAnimalGuid}", "Diet")
                    LaUtils.debug.log(f"        *** Adjusted MCal Target (after fallow): {myAdjustedMCalTarget}", "Diet")

                    # Get land productivity value
                    paramGuid = self.mAnimals.get(myAnimalGuid, "")
                    animalParameter = LaUtils.getAnimalParameter(paramGuid) if paramGuid else None
                    myLandValue = 0.0
                    if animalParameter:
                        if getattr(animalParameter, 'useCommonGrazingLand', False):
                            myLandValue = self.mCommonLandValue
                        elif getattr(animalParameter, 'useSpecificGrazingLand', False):
                            myLandValue = float(str(getattr(animalParameter, 'valueSpecificGrazingLand', 0.0)))
                        # Handle energy type conversion if necessary (assuming values are MCal/ha for now)
                        # TODO: Implement TDN handling based on self.mSpecificLandEnergyType

                    try:
                        # Convert myLandValue to float if it's not already
                        myLandValue = float(myLandValue) if myLandValue else 0.0
                    except (ValueError, TypeError):
                        # If conversion fails, it's probably a string like "Dunum"
                        LaUtils.debug.log(f"Warning: Land value '{myLandValue}' is not a number. Falling back to common land value.", "Warning")
                        try:
                            # Try to use the common land value as a fallback
                            myLandValue = float(self.mCommonLandValue) if self.mCommonLandValue else 0.0
                            LaUtils.debug.log(f"        *** Using common land value: {myLandValue}", "Diet")
                        except (ValueError, TypeError):
                            # If that also fails, default to 0
                            LaUtils.debug.log(f"Warning: Common land value '{self.mCommonLandValue}' is also not a number.", "Warning")
                            myLandValue = 0.0

                    if myLandValue <= 0:
                        LaUtils.debug.log(f"        *** Warning: Land value is zero for animal {myAnimalGuid}. Area target will be zero.", "Warning")
                        myAreaTarget = 0.0
                    else:
                        myAreaTarget = myAdjustedMCalTarget / myLandValue
                        LaUtils.debug.log(f"        *** Land Value = {myLandValue}", "Diet")
                        LaUtils.debug.log(f"        *** Calculated Area Target = {myAreaTarget}", "Diet")

                    # Update the report string
                    myReport += f"Final MCal Target (after fallow) = {myAdjustedMCalTarget:.2f}\n"
                    myReport += f"Final Area Target = {myAreaTarget:.2f}\n"

                    # Update the report map with the final area target
                    myAnimalCalcsReportMap[myAnimalGuid] = (myReport, myAreaTarget)
                    myFinalAnimalAreaTargets[myAnimalGuid] = myAreaTarget # Store for LaDietLabels

                except Exception as e:
                    LaUtils.debug.log(f"Error calculating final area target for animal {myAnimalGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # Log the final calculations for the animals map
            LaUtils.debug.log("myFinal Calculations for animals map:", "Diet")
            for animal_guid, (report, area_target) in myAnimalCalcsReportMap.items():
                LaUtils.debug.log(f"Animal GUID: {animal_guid}", "Diet")
                LaUtils.debug.log("Report:", "Diet")
                for line in report.split("\n"):
                    LaUtils.debug.log(line, "Diet")
                LaUtils.debug.log(f"Area Target: {area_target}", "Diet")
                LaUtils.debug.log("--------------------------------------------", "Diet")

            # ----------- Set Final Diet Labels -----------
            # self._setDietLabels(
            #     myDietLabels,
            #     myOverallDairyMCals,
            #     myOverallCropsMCals,
            #     myOverallDomesticMeatMCals, # Use domestic meat MCals here
            #     myOverallWildMeatMCals,
            #     myOverallWildPlantsMCals,
            #     myOverallDairyPercent,
            #     myDomesticMeatPercent,
            #     myOverallCropPercent,
            #     myWildMeatPercent,
            #     myOverallWildPlantPercent,
            #     myOverallMeatPercent, # Use combined meat percent
            #     myOverallPlantPercent,
            #     myMCalsIndividualAnnual,
            #     myMCalsSettlementAnnual,
            #     myOverallDairySurplusMCals,
            #     cropCalcsReportMap,
            #     myAnimalCalcsReportMap # Pass the map with updated reports and area targets
            # )

            # Add the final area target maps to the diet labels object
            myDietLabels.cropAreaTargetsMap = {guid: area for guid, (_, area) in cropCalcsReportMap.items()}
            myDietLabels.animalAreaTargetsMap = myFinalAnimalAreaTargets

            LaUtils.debug.log("doCalcsAnimalsFirstDairySeparate calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsAnimalsFirstDairySeparate: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels


    def toHtmlCalorieCropTargets(self) -> str:
        """Generate HTML report for crop calorie targets."""
        html = "<h3>Crop Calorie Targets</h3>"

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

        # Get crop calorie targets from lastDietLabels if available
        total_calories = 0
        crop_calories = {}

        if hasattr(self.lastDietLabels, 'cropCalorieTargets'):
            crop_calories = self.lastDietLabels.cropCalorieTargets
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

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Calories (kcal)</th><th>Percentage</th></tr>"

        # Get animal calorie targets from lastDietLabels if available
        total_calories = 0
        animal_calories = {}

        if hasattr(self.lastDietLabels, 'animalCalorieTargets'):
            animal_calories = self.lastDietLabels.animalCalorieTargets
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

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Production (kg)</th><th>Percentage</th></tr>"

        # Get crop production targets from lastDietLabels if available
        total_production = 0
        crop_production = {}

        if hasattr(self.lastDietLabels, 'cropProductionTargets'):
            crop_production = self.lastDietLabels.cropProductionTargets
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

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Production (kg)</th><th>Percentage</th></tr>"

        # Get animal production targets from lastDietLabels if available
        total_production = 0
        animal_production = {}

        if hasattr(self.lastDietLabels, 'animalProductionTargets'):
            animal_production = self.lastDietLabels.animalProductionTargets
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

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Crop</th><th>Area (ha)</th><th>Percentage</th></tr>"

        # Get crop area targets from lastDietLabels if available
        total_area = 0
        crop_areas = {}

        if hasattr(self.lastDietLabels, 'cropAreaTargets'):
            crop_areas = self.lastDietLabels.cropAreaTargets
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

        if not self.lastDietLabels:
            return html + "<p>No calculation results available</p>"

        html += "<table border='1' cellpadding='4'>"
        html += "<tr><th>Animal</th><th>Area (ha)</th><th>Percentage</th></tr>"

        # Get animal area targets from lastDietLabels if available
        total_area = 0
        animal_areas = {}

        if hasattr(self.lastDietLabels, 'animalAreaTargets'):
            animal_areas = self.lastDietLabels.animalAreaTargets
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