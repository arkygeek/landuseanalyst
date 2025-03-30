from qgis.PyQt.QtCore import pyqtProperty, pyqtSignal, QUuid
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging
from typing import Dict, List, Tuple

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType # Added EnergyType
from la.lib.laanimal import LaAnimal
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

    def __init__(self, parent=None, theModel=None):
        """
        Initialize the LaModel instance.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
            theModel (LaModel, optional): An existing LaModel instance to copy attributes from. Defaults to None.
        """
        super().__init__(parent)
        if theModel is not None:
            self.mName = theModel.name
            self.mPopulation = theModel.population
            self.setGuid(str(theModel.guid))
            self.mPeriod = theModel.period
            self.mProjection = theModel.projection
            self.mEasting = theModel.easting
            self.mNorthing = theModel.northing
            self.mEuclideanDistance = theModel.euclideanDistance
            self.mWalkingTime = theModel.walkingTime
            self.mPathDistance = theModel.pathDistance
            self.mPrecision = theModel.precision
            self.mDietPercent = theModel.dietPercent
            self.mPercentOfDietThatIsFromCrops = theModel.percentOfDietThatIsFromCrops
            self.mMeatPercent = theModel.meatPercent
            self.mCaloriesPerPersonDaily = theModel.caloriesPerPersonDaily
            self.mDairyUtilisation = theModel.dairyUtilisation
            self.mBaseOnPlants = theModel.baseOnPlants
            self.mIncludeDairy = theModel.includeDairy
            self.mLimitDairy = theModel.limitDairy
            self.mLimitDairyPercent = theModel.limitDairyPercent
            self.mFallowStatus = theModel.fallowStatus
            self.mFallowRatio = theModel.fallowRatio
            self.mLandBeingGrazed = theModel.landBeingGrazed
            self.mLandFound = theModel.landFound

            self.mCommonLandValue = theModel.commonLandValue
            self.mCommonLandAreaUnits = theModel.commonLandAreaUnits
            self.mSpecificLandAreaUnits = theModel.specificLandAreaUnits # Added assignment
            self.mSpecificLandEnergyType = theModel.specificLandEnergyType # Added assignment
            self.mHerdSize = theModel.herdSize
            self.mAnimals = {}
            self.mCrops = {}
            self.mDiets = {}
            self.mDietLabels = []
            self.mPriority = theModel.priority
            self.mDescription  = theModel.description
            self.mAreaUnits = theModel.areaUnits
            self.mStatus = theModel.status
            self.mIcon = None
        else:
            self.setGuid(None)
            self.mName = "Default Site"
            self.mPopulation = 1000
            self.mPeriod = "No Period Set"
            self.mProjection = 100
            self.mPrecision = 5
            self.mDietPercent = 25
            self.mPercentOfDietThatIsFromCrops = 10
            self.mMeatPercent = 10
            self.mCaloriesPerPersonDaily = 2500
            self.mDairyUtilisation = 100
            self.mBaseOnPlants = True
            self.mIncludeDairy = True
            self.mLimitDairy = False
            self.mLimitDairyPercent = 10
            self.mFallowStatus = Status.MoreThanEnoughToCompletelySatisfy
            self.mFallowRatio = 1
            self.mEasting = 0
            self.mNorthing = 0
            self.mEuclideanDistance = True
            self.mWalkingTime = False
            self.mPathDistance = False
            self.mLandBeingGrazed = LandBeingGrazed.Common
            self.mLandFound = LandFound.NotEnough

            self.mCommonLandValue = 0.0
            self.mCommonLandAreaUnits = AreaUnits.Hectare
            self.mSpecificLandAreaUnits = AreaUnits.Hectare # Added default
            self.mSpecificLandEnergyType = EnergyType.KCalories # Corrected default
            self.mHerdSize = 0
            self.mAnimals = {}
            self.mCrops = {}
            self.mDiets = {}
            self.mDietLabels = []
            self.mPriority = Priority.None_
            self.mDescription = "No Description Set"
            self.mAreaUnits = AreaUnits.Hectare
            self.mStatus = Status.MoreThanEnoughToCompletelySatisfy
            self.mIcon = None

        # Initialize value map for fallow allocation
        self._mValueMap = {}
        self.logger = logging.getLogger(__name__)


    def logMessage(self, theMessage: str):
        """
        Logs a message using the logger.

        Args:
            message (str): The message to log.
        """
        self.logger.info(theMessage)


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
        return int(str(self.mPopulation))
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
        return int(self.mCaloriesPerPersonDaily)
    @caloriesPerPersonDaily.setter
    def caloriesPerPersonDaily(self, theCaloriesPerPersonDaily: int):
        if self.mCaloriesPerPersonDaily != theCaloriesPerPersonDaily:
            self.mCaloriesPerPersonDaily = theCaloriesPerPersonDaily
            self._caloriesPerPersonDailyChanged.emit()


    @pyqtProperty(int, notify=_dairyUtilisationChanged)
    def dairyUtilisation(self) -> int: # type: ignore
        return int(self.mDairyUtilisation)
    @dairyUtilisation.setter
    def dairyUtilisation(self, thePercent: int):
        if self.mDairyUtilisation != thePercent:
            self.mDairyUtilisation = thePercent
            self._dairyUtilisationChanged.emit()


    @pyqtProperty(bool, notify=_baseOnPlantsChanged)
    def baseOnPlants(self) -> bool: # type: ignore
        return bool(self.mBaseOnPlants)
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
        return bool(self.mIncludeDairy)
    @includeDairy.setter
    def includeDairy(self, theBool: bool):
        if self.mIncludeDairy != theBool:
            self.mIncludeDairy = theBool
            self._includeDairyChanged.emit()


    @pyqtProperty(bool, notify=_limitDairyChanged)
    def limitDairy(self) -> bool: # type: ignore
        return bool(self.mLimitDairy)
    @limitDairy.setter
    def limitDairy(self, theBool: bool):
        if self.mLimitDairy != theBool:
            self.mLimitDairy = theBool
            self._limitDairyChanged.emit()


    @pyqtProperty(int, notify=_limitDairyPercentChanged)
    def limitDairyPercent(self) -> int: # type: ignore
        return int(str(self.mLimitDairyPercent))
    @limitDairyPercent.setter
    def limitDairyPercent(self, thePercent: int):
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
        return self._mGuid
    @guid.setter
    def guid(self, theGuid: str):
        if self._mGuid != theGuid:
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

        self._mGuid = root.attrib.get('guid', QUuid.createUuid().toString(QUuid.StringFormat.Id128))
        self.mName = root.findtext('name', default="No Name Set")
        self.mPopulation = int(root.findtext('population', default="1000"))
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


    def _GetAnimalValue(self, animal, prop_name: str) -> float:
        """Helper method to safely get float values from animal properties."""
        prop = getattr(animal, prop_name, None)
        if prop is None:
            return 0.0
        if isinstance(prop, property):
            return float(prop.__get__(animal, type(animal)))
        return float(prop)


    def _GetAnimalParamValue(self, theParam, thePropName: str) -> float:
        """Helper method to safely get float values from animal parameter properties."""
        myProp = getattr(theParam, thePropName, None)
        if myProp is None:
            return 0.0
        if isinstance(myProp, property):
            return float(myProp.__get__(theParam, type(theParam)))
        return float(myProp)


    def _setDietLabels(self, theDietLabels: LaDietLabels,
                        theOverallDairyMCals: float,
                        theOverallCropsMCals: float,
                        theOverallMeatMCals: float,
                        theOverallWildMeatMCals: float,
                        theOverallWildPlantsMCals: float,
                        theOverallDairyPercent: float,
                        theDomesticMeatPercent: float,
                        theOverallCropPercent: float,
                        theWildMeatPercent: float,
                        theOverallWildPlantPercent: float,
                        theOverallMeatPercent: float,
                        theOverallPlantPercent: float,
                        theMCalsIndividualAnnual: float,
                        theMCalsSettlementAnnual: float,
                        theOverallDairySurplusMCals: float,
                        theCropCalcsReportMap: Dict[str, Tuple[str, float]],
                        theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """Helper method to safely set all diet label private attributes."""
        try:
            # Log the ID of the object we're updating to help with debugging
            from la.lib.lautils import LaUtils
            # Log new values before emitting signals
            LaUtils.debug.log(f"New values set - Dairy: {theOverallDairyMCals:.2f},\
                                Crops: {theOverallCropsMCals:.2f}", "Diet")
            # Set values directly to attributes first - using naming from C++ version
            theDietLabels.dairyMCalories = theOverallDairyMCals # type: ignore
            theDietLabels.cropMCalories = theOverallCropsMCals  # type: ignore
            theDietLabels.animalMCalories = theOverallMeatMCals # type: ignore
            theDietLabels.wildAnimalMCalories = theOverallWildMeatMCals # type: ignore
            theDietLabels.wildPlantsMCalories = theOverallWildPlantsMCals # type: ignore
            theDietLabels.dairyPortionPct = theOverallDairyPercent * 100.0 # type: ignore
            theDietLabels.tameMeatPortionPct = theDomesticMeatPercent * 100.0 # type: ignore
            theDietLabels.cropsPortionPct = theOverallCropPercent * 100.0 # type: ignore
            theDietLabels.wildAnimalPortionPct = theWildMeatPercent * 100.0 # type: ignore
            theDietLabels.wildPlantsPortionPct = theOverallWildPlantPercent * 100.0 # type: ignore
            theDietLabels.plantsPortionPct = theOverallPlantPercent * 100.0 # type: ignore
            theDietLabels.animalPortionPct = theOverallMeatPercent * 100.0 # type: ignore
            theDietLabels.kiloCaloriesIndividualAnnual = theMCalsIndividualAnnual # type: ignore
            theDietLabels.megaCaloriesSettlementAnnual = theMCalsSettlementAnnual # type: ignore
            theDietLabels.dairySurplusMCalories = theOverallDairySurplusMCals # type: ignore
            theDietLabels.cropCalcsReportMap = theCropCalcsReportMap # type: ignore
            theDietLabels.animalCalcsReportMap = theAnimalCalcsReportMap # type: ignore

            try:
                theDietLabels.dairyMCaloriesChanged.emit(theOverallDairyMCals)
                theDietLabels.cropMCaloriesChanged.emit(theOverallCropsMCals)
                theDietLabels.animalMCaloriesChanged.emit(theOverallMeatMCals)
                theDietLabels.wildAnimalMCaloriesChanged.emit(theOverallWildMeatMCals)
                theDietLabels.wildPlantsMCaloriesChanged.emit(theOverallWildPlantsMCals)
                theDietLabels.dairyPortionPctChanged.emit(theOverallDairyPercent * 100.0)
                theDietLabels.tameMeatPortionPctChanged.emit(theDomesticMeatPercent * 100.0)
                theDietLabels.cropsPortionPctChanged.emit(theOverallCropPercent * 100.0)
                theDietLabels.wildAnimalPortionPctChanged.emit(theWildMeatPercent * 100.0)
                theDietLabels.wildPlantsPortionPctChanged.emit(theOverallWildPlantPercent * 100.0)
                theDietLabels.plantsPortionPctChanged.emit(theOverallPlantPercent * 100.0)
                theDietLabels.animalPortionPctChanged.emit(theOverallMeatPercent * 100.0)
                theDietLabels.kiloCaloriesIndividualAnnualChanged.emit(theMCalsIndividualAnnual)
                theDietLabels.megaCaloriesSettlementAnnualChanged.emit(theMCalsSettlementAnnual)
                theDietLabels.dairySurplusMCaloriesChanged.emit(theOverallDairySurplusMCals)
                theDietLabels.cropCalcsReportMapChanged.emit(theCropCalcsReportMap)
                theDietLabels.animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)
            except Exception as e:
                LaUtils.debug.log(f"Error emitting diet label signals: {str(e)}", "Error")

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error updating diet labels in model: {str(e)}", "Error")


    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is included with meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++ declaration but not used in this simplified version

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
            self._setDietLabels(
                myDietLabels,
                myDairyMCalorieCounter,      # Overall dairy MCals
                myCropMCalories,              # Overall crop MCals
                myTameMeatMCalorieCounter,    # Tame meat MCals
                myWildMeatMCalorieCounter,    # Wild meat MCals
                myWildPlantsMCalories,        # Wild plants MCals
                dairyPercent,                # Overall dairy percent
                tameMeatPercent,             # Domestic meat percent
                cropPercent,                 # Overall crop percent
                wildMeatPercent,             # Wild meat percent
                wildPlantPercent,            # Overall wild plant percent
                myOverallMeatPercent,        # Overall meat percent
                myOverallPlantPercent,       # Overall plant percent
                myMCalsIndividualAnnual * 1000.0,  # Convert back to kCal
                myMCalsSettlementAnnual,     # MCals settlement annual
                0.0,                         # No dairy surplus in this simplified calculation
                myCropCalcsReportMap,        # Empty crop calcs report map
                myAnimalCalcsReportMap       # Empty animal calcs report map
            )

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
        myDietLabels: LaDietLabels = LaDietLabels()
        myAnimal: LaAnimal = LaAnimal()
        # Log start of calculation
        LaUtils.debug.log("Starting doCalcsAnimalsFirstIncludeDairy calculation", "Diet")

        try:
            # Get base values from internal attributes
            calories_daily = self.mCaloriesPerPersonDaily
            population_count = self.mPopulation
            meat_percent = self.mMeatPercent / 100.0  # Convert to decimal
            diet_percent = self.mDietPercent / 100.0  # Convert to decimal

            # Log input values
            LaUtils.debug.log(f"Calories per person daily: {calories_daily}", "Diet")
            LaUtils.debug.log(f"Population count: {population_count}", "Diet")
            LaUtils.debug.log(f"Meat percent: {meat_percent*100:.1f}%, Diet percent: {diet_percent*100:.1f}%", "Diet")

            # Calculate basic values that are required for all calculations
            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

            # Log calculated values
            LaUtils.debug.log(f"Annual individual calories (MCal): {myMCalsIndividualAnnual}", "Diet")
            LaUtils.debug.log(f"Annual settlement calories (MCal): {myMCalsSettlementAnnual}", "Diet")

            # Initialize MCal counters for simplified calculation
            myDairyMCalorieCounter = myMCalsSettlementAnnual * diet_percent * 0.05  # 5% of animal diet
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * diet_percent * 0.05  # 5% of animal diet
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * diet_percent * 0.9  # 90% of animal diet
            myCropMCalories = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.1  # 10% of plant diet
            myWildPlantsMCalories = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.9  # 90% of plant diet

            # Calculate percentages
            totalMCalories = myMCalsSettlementAnnual

            dairyPercent = myDairyMCalorieCounter / totalMCalories
            tameMeatPercent = myTameMeatMCalorieCounter / totalMCalories
            wildMeatPercent = myWildMeatMCalorieCounter / totalMCalories
            cropPercent = myCropMCalories / totalMCalories
            wildPlantPercent = myWildPlantsMCalories / totalMCalories

            animalPercent = diet_percent
            plantPercent = 1.0 - diet_percent

            # Set calculated values on diet labels
            myDietLabels._dairyMCalories = myDairyMCalorieCounter
            myDietLabels._animalMCalories = myTameMeatMCalorieCounter
            myDietLabels._wildAnimalMCalories = myWildMeatMCalorieCounter
            myDietLabels._cropMCalories = myCropMCalories
            myDietLabels._wildPlantsMCalories = myWildPlantsMCalories

            myDietLabels._dairyPortionPct = dairyPercent * 100.0
            myDietLabels._tameMeatPortionPct = tameMeatPercent * 100.0
            myDietLabels._wildAnimalPortionPct = wildMeatPercent * 100.0
            myDietLabels._cropsPortionPct = cropPercent * 100.0
            myDietLabels._wildPlantsPortionPct = wildPlantPercent * 100.0

            myDietLabels._animalPortionPct = animalPercent * 100.0
            myDietLabels._plantsPortionPct = plantPercent * 100.0

            myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0  # Convert back to kCal
            myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

            # No dairy surplus in this simple calculation
            myDietLabels._dairySurplusMCalories = 0.0

            LaUtils.debug.log(f"Final percentages - Animal: {animalPercent*100:.1f}%, Plant: {plantPercent*100:.1f}%", "Diet")
            LaUtils.debug.log("doCalcsAnimalsFirstIncludeDairy calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels


    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsPlantsFirstDairySeparate calculation", "Diet")

        try:
            # Base calculations similar to include dairy but with separate dairy tracking
            calories_daily = float(self.mCaloriesPerPersonDaily)
            population_count = float(self.mPopulation)
            meat_percent = float(self.mMeatPercent) / 100.0  # Convert to decimal
            diet_percent = float(self.mDietPercent) / 100.0  # Convert to decimal

            LaUtils.debug.log(f"Input parameters - calories_daily: {calories_daily}, population: {population_count}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {meat_percent*100}%, diet_percent: {diet_percent*100}%", "Diet")

            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

            LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters with simplified approach for testing
            myDairyCounter = myMCalsSettlementAnnual * 0.05  # Separate counter for dairy (5% of total)
            myTameMeatCounter = myMCalsSettlementAnnual * diet_percent * 0.05  # 5% of animal diet
            myWildMeatCounter = myMCalsSettlementAnnual * diet_percent * 0.9  # 90% of animal diet
            myCropCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.1  # 10% of plant diet
            myWildPlantCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.9  # 90% of plant diet

            # Calculate percentages (adjusted for separate dairy)
            totalMCaloriesWithoutDairy = myMCalsSettlementAnnual - myDairyCounter

            dairyPercent = myDairyCounter / myMCalsSettlementAnnual
            tameMeatPercent = myTameMeatCounter / myMCalsSettlementAnnual
            wildMeatPercent = myWildMeatCounter / myMCalsSettlementAnnual
            cropPercent = myCropCounter / myMCalsSettlementAnnual
            wildPlantPercent = myWildPlantCounter / myMCalsSettlementAnnual

            animalPercent = (myTameMeatCounter + myWildMeatCounter) / myMCalsSettlementAnnual
            plantPercent = (myCropCounter + myWildPlantCounter) / myMCalsSettlementAnnual

            # Set calculated values using private attributes
            myDietLabels._dairyMCalories = myDairyCounter
            myDietLabels._animalMCalories = myTameMeatCounter
            myDietLabels._wildAnimalMCalories = myWildMeatCounter
            myDietLabels._cropMCalories = myCropCounter
            myDietLabels._wildPlantsMCalories = myWildPlantCounter

            myDietLabels._dairyPortionPct = dairyPercent * 100.0
            myDietLabels._tameMeatPortionPct = tameMeatPercent * 100.0
            myDietLabels._wildAnimalPortionPct = wildMeatPercent * 100.0
            myDietLabels._cropsPortionPct = cropPercent * 100.0
            myDietLabels._wildPlantsPortionPct = wildPlantPercent * 100.0

            myDietLabels._animalPortionPct = animalPercent * 100.0
            myDietLabels._plantsPortionPct = plantPercent * 100.0

            myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0
            myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

            # Log results
            LaUtils.debug.log(f"Calculation results - Animal: {animalPercent*100:.2f}%, Plant: {plantPercent*100:.2f}%, Dairy: {dairyPercent*100:.2f}%", "Diet")
            LaUtils.debug.log("doCalcsPlantsFirstDairySeparate calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels


    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is separate from meat."""
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

            LaUtils.debug.log(f"Input parameters - calories_daily: {calories_daily}, population: {population_count}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {meat_percent*100}%, diet_percent: {diet_percent*100}%", "Diet")

            # Calculate basic values
            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

            LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters with a simplified calculation approach
            myDairyCounter = myMCalsSettlementAnnual * 0.05  # Separate dairy calculation (5% of total)
            myTameMeatCounter = myMCalsSettlementAnnual * diet_percent * meat_percent  # Tame meat portion
            myWildMeatCounter = myMCalsSettlementAnnual * diet_percent * (1.0 - meat_percent)  # Wild meat portion
            myCropCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.8  # Crops portion (80% of plant calories)
            myWildPlantCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.2  # Wild plants (20% of plant calories)

            # Calculate percentages
            totalMCalories = myMCalsSettlementAnnual

            dairyPercent = myDairyCounter / totalMCalories
            tameMeatPercent = myTameMeatCounter / totalMCalories
            wildMeatPercent = myWildMeatCounter / totalMCalories
            cropPercent = myCropCounter / totalMCalories
            wildPlantPercent = myWildPlantCounter / totalMCalories

            animalPercent = (myTameMeatCounter + myWildMeatCounter) / totalMCalories
            plantPercent = (myCropCounter + myWildPlantCounter) / totalMCalories

            # Create report maps for crops and animals
            cropCalcsReportMap = {}
            animalCalcsReportMap = {}

            # Populate crop report map with some sample data for each crop
            for cropGuid, paramGuid in self.mCrops.items():
                try:
                    crop = LaUtils.getCrop(cropGuid)
                    cropParameter = LaUtils.getCropParameter(paramGuid)

                    if crop and cropParameter:
                        # Calculate this crop's share of the total crop calories using crop parameter percentages
                        cropContributionPercent = 1.0
                        try:
                            # Use the crop parameter's percent tame crop value if available
                            cropContributionPercent = float(str(cropParameter.percentTameCrop)) * 0.01
                        except:
                            # Fall back to equal distribution if parameter not available
                            cropContributionPercent = 1.0 / len(self.mCrops) if self.mCrops else 0.0

                        # Calculate crop calories following the C++ approach
                        cropPercent = cropContributionPercent * cropPercent
                        myCropFoodValue = float(str(crop.cropCalories)) * 0.001  # Convert to MCal/kg
                        myMCalsFromTheCrop = cropPercent * myMCalsSettlementAnnual

                        # Calculate kg needed for people (initial calculation before adjustments)
                        myKgForPeople1 = myMCalsFromTheCrop / myCropFoodValue

                        # Get spoilage and reseeding percentages from crop parameters
                        mySpoilagePercent = 0.1  # Default 10% if not available
                        myReseedPercent = 0.1    # Default 10% if not available

                        try:
                            mySpoilagePercent = float(str(cropParameter.spoilage)) * 0.01
                            myReseedPercent = float(str(cropParameter.reseed)) * 0.01
                        except Exception as e:
                            LaUtils.debug.log(f"Error getting spoilage/reseed parameters for {crop.name}: {e}", "Warning")

                        # Calculate additional kg needed for spoilage and reseeding
                        myKgForPeopleSpoilage = myKgForPeople1 * mySpoilagePercent
                        myKgForPeopleReseed = myKgForPeople1 * myReseedPercent

                        # Total kg needed for people after accounting for spoilage and reseeding
                        myKgForPeople = myKgForPeople1 + myKgForPeopleSpoilage + myKgForPeopleReseed

                        # Calculate area needed based on yield
                        myCropYield = crop.cropYield

                        # Determine area units and convert values if needed
                        areaUnitName = "hectares"
                        if hasattr(self, '_mAreaUnits') and self.mAreaUnits == AreaUnits.Dunum:
                            areaUnitName = "dunums"
                            # If crop yield is in hectares but we want dunums, adjust the yield
                            if hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Hectare":
                                myCropYield = myCropYield / 10.0  # Convert hectares to dunums
                        elif hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Dunum":
                            # If crop yield is in dunums but we want hectares, adjust the yield
                            myCropYield = myCropYield * 10.0  # Convert dunums to hectares

                        # Calculate area needed in the appropriate units
                        myCropAreaTarget = myKgForPeople / myCropYield

                        # Calculate fallow land area if applicable
                        myFallowArea = 0.0
                        myFallowMCals = 0.0
                        myTotalAreaNeeded = myCropAreaTarget

                        if hasattr(cropParameter, 'fallowRatio') and cropParameter.fallowRatio > 0:
                            myRatio = float(str(cropParameter.fallowRatio))
                            myFallowValue = 0.0
                            if hasattr(cropParameter, 'fallowValue'):
                                myFallowValue = float(str(cropParameter.fallowValue))

                            myFallowArea = myCropAreaTarget * (myRatio / (1.0 + myRatio))
                            myFallowMCals = myFallowArea * myFallowValue
                            myTotalAreaNeeded = myCropAreaTarget + myFallowArea

                        # Create detailed report for this crop including all calculation steps
                        cropReport = f"Calculation Report for {crop.name}\n"
                        cropReport += f"===========================\n"
                        cropReport += f"Crop calories: {myMCalsFromTheCrop:.2f} MCal\n"
                        cropReport += f"Population: {population_count} people\n"
                        cropReport += f"Individual needs: {myMCalsIndividualAnnual:.2f} MCal/year\n"
                        cropReport += f"Settlement needs: {myMCalsSettlementAnnual:.2f} MCal/year\n"
                        cropReport += f"Plant portion: {plantPercent*100:.2f}% of diet\n"
                        cropReport += f"Crop portion: {cropPercent*100:.2f}% of diet\n"
                        cropReport += f"Crop food value: {myCropFoodValue:.2f} MCal/kg\n"

                        cropReport += f"\nProduction Calculations:\n"
                        cropReport += f"Base production needed: {myKgForPeople1:.2f} kg\n"
                        cropReport += f"Spoilage adjustment ({mySpoilagePercent*100:.1f}%): {myKgForPeopleSpoilage:.2f} kg\n"
                        cropReport += f"Reseed adjustment ({myReseedPercent*100:.1f}%): {myKgForPeopleReseed:.2f} kg\n"
                        cropReport += f"Total production needed: {myKgForPeople:.2f} kg\n"

                        cropReport += f"\nArea Calculations:\n"
                        cropReport += f"Crop yield: {myCropYield:.2f} kg/{areaUnitName}\n"
                        cropReport += f"Required crop area: {myCropAreaTarget:.2f} {areaUnitName}\n"

                        if myFallowArea > 0:
                            cropReport += f"Fallow land area: {myFallowArea:.2f} {areaUnitName}\n"
                            cropReport += f"Fallow land value: {myFallowValue:.2f} MCal/{areaUnitName}\n"
                            cropReport += f"Fallow land calories: {myFallowMCals:.2f} MCal\n"
                            cropReport += f"Total area needed (crop + fallow): {myTotalAreaNeeded:.2f} {areaUnitName}\n"

                        # Store the report in the map with the required production as the second value
                        cropCalcsReportMap[cropGuid] = (cropReport, myKgForPeople)
                        LaUtils.debug.log(f"Added detailed crop calculation for {crop.name}", "Diet")
                    else:
                        LaUtils.debug.log(f"Missing crop or crop parameter for GUID {cropGuid}", "Warning")

                except Exception as e:
                    LaUtils.debug.log(f"Error creating crop report for GUID {cropGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # Populate animal report map with some sample data for each animal
            for animalGuid, paramGuid in self.mAnimals.items():
                try:
                    animal = LaUtils.getAnimal(animalGuid)
                    animalParameter = LaUtils.getAnimalParameter(paramGuid)

                    # Initialize variables at the start
                    myAnimalReport = ""
                    myAnimalHerdMCalsRequired = 0.0

                    if animal:
                        LaUtils.debug.log(f"Processing animal: {animal.name} (GUID: {animalGuid})", "Diet")

                        # Get animal values safely
                        myMilkKgPerDay = float(str(animal.milkGramsPerDay)) * 0.001  # Convert g to kg
                        myMilkFoodValue = float(str(animal.milkFoodValue)) * 0.001   # Convert to MCal
                        myLactationTime = float(str(animal.lactationTime))
                        myWeaningAge = float(str(animal.weaningAge))
                        myGestatingTime = float(str(animal.gestationTime))
                        myEstrousCycle = float(str(animal.estrousCycle))
                        myBabiesPerBirth = float(str(animal.youngPerBirth))
                        myDeathRate = float(str(animal.deathRate)) * 0.01  # Convert from percent
                        myBreedingRatio = float(str(animal.femalesPerMale))

                        # Check for zero breeding ratio to avoid division by zero
                        if myBreedingRatio <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has a breeding ratio of {myBreedingRatio}, using default of 1.0", "Warning")
                            myBreedingRatio = 1.0  # Default to 1 if zero or negative

                        myKillWeight = float(str(animal.killWeight))
                        myUsablePortionOfAnimal = float(str(animal.usableMeat)) * 0.01  # Convert from percent
                        myAdultWeight = float(str(animal.adultWeight))
                        myConceptionEfficiency = float(str(animal.conceptionEfficiency)) * 0.01  # Convert from percent
                        myMeatValueMCal = float(str(animal.meatFoodValue)) * 0.001  # Convert to MCal
                        mySexualMaturity = float(str(animal.sexualMaturity))
                        myBreedingYears = float(str(animal.breedingExpectancy))

                        # Get parameter values
                        myAnimalContributionToMeatPortion = 0
                        if animalParameter:
                            try:
                                myAnimalContributionToMeatPortion = float(str(animalParameter.percentTameMeat)) * 0.01
                            except:
                                myAnimalContributionToMeatPortion = 1.0 / len(self.mAnimals) if len(self.mAnimals) > 0 else 0

                        # Calculate animal targets using the C++ approach
                        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * diet_percent * meat_percent
                        myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge)
                        myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal

                        # Get dairy utilization as a decimal (0-1)
                        myDairyUtilization = float(self.mDairyUtilisation) / 100.0
                        myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization

                        # Calculate birthing events per year, handling edge case for too many days
                        myBirthingEventsPerYear1 = 365.0 / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime)
                        myBirthingEventsPerYear = 1.0 if myBirthingEventsPerYear1 < 1.0 else myBirthingEventsPerYear1

                        # Calculate culled mothers value
                        myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal *
                                                (1.0 / ((mySexualMaturity / 12.0) + myBreedingYears)))
                        myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear)

                        # Calculate culled adult males value
                        myCulledAdultMalesValue = myCulledMothersValue / myBreedingRatio

                        # Calculate final offspring value
                        myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue

                        # Calculate number of offspring needed per year
                        myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue

                        # Calculate MCals from meat and utilized from dairy
                        myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue
                        myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear

                        # Add to the diet counters
                        myTameMeatCounter += myMCalsFromTheMeat
                        myDairyCounter += myMCalsUtilizedFromDairy

                        # Calculate meat and dairy percentages
                        myMeatPercent = myMCalsFromTheMeat / myMCalsSettlementAnnual
                        myDairyPercent = myMCalsUtilizedFromDairy / myMCalsSettlementAnnual

                        # Calculate herd size based on birthing cycles
                        myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1.0 - myDeathRate) * myConceptionEfficiency

                        # Check for zero offspring per mother per year to avoid division by zero
                        if myOffspringPerMotherPerYear <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has zero or negative offspring per mother per year calculation. Using default value of 1.0", "Warning")
                            myOffspringPerMotherPerYear = 1.0  # Default to 1 if zero or negative

                        myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear
                        myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5
                        myFemalesStepOne = myMalesStepOne
                        myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity / 12.0)) / myBreedingYears
                        # Match original C++ implementation exactly
                        myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio
                        myAdditionalMothers = ((myReplacementMothersPerYear / myOffspringPerMotherPerYear) * 2.0) + (myBreedingMalesRequired * 2.0)

                        myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5
                        myFemalesStepTwo = myMalesStepTwo
                        myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear
                        myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo
                        myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo
                        myTotalOffspring = myTotalMaleOffspring * 2.0  # Total offspring

                        # Calculate feed requirements
                        try:
                            # Get animal feed values from animal parameters
                            myFeedForMaintenance = float(str(animal.maintenance))  # kg feed per day
                            myFeedForGestating = float(str(animal.gestating))      # kg feed per day
                            myFeedForLactating = float(str(animal.lactating))      # kg feed per day
                            myFeedForOffspringPerKg = float(str(animal.juvenile))  # kg feed per kg weight of offspring

                            # Get values needed for grazing land calculations from animal parameter
                            myUseCommonGrazingLand = True
                            myUseSpecificGrazingLand = False

                            # Get grazing land productivity from parameters - critical for correct area calculation
                            # In the original C++ code, this is ValueCommonGrazingLand or ValueSpecificGrazingLand
                            # representing calories per hectare/dunum
                            myGrazingLandCalories: float = 0.0

                            if animalParameter:
                                if hasattr(animalParameter, 'useCommonGrazingLand'):
                                    myUseCommonGrazingLand = bool(animalParameter.useCommonGrazingLand)
                                if hasattr(animalParameter, 'useSpecificGrazingLand'):
                                    myUseSpecificGrazingLand = bool(animalParameter.useSpecificGrazingLand)

                                # Get the correct grazing land caloric value
                                if myUseCommonGrazingLand and hasattr(animalParameter, 'ValueCommonGrazingLand'):
                                    myGrazingLandCalories = float(str(animalParameter.valueCommonGrazingLand))
                                elif myUseSpecificGrazingLand and hasattr(animalParameter, 'ValueSpecificGrazingLand'):
                                    myGrazingLandCalories = float(str(animalParameter.valueSpecificGrazingLand))

                            # If we couldn't get a value from parameters, use the model's common grazing value
                            if myGrazingLandCalories <= 0.0 and hasattr(self, '_mCommonLandValue'):
                                myGrazingLandCalories = float(str(self.mCommonLandValue))

                            # Default fallback if no values available
                            if myGrazingLandCalories <= 0.0:
                                myGrazingLandCalories = 7500.0  # Default calories per hectare (reasonable value)
                                LaUtils.debug.log(f"Using default grazing land value of {myGrazingLandCalories} calories/hectare", "Warning")

                        except Exception as e:
                            # Default values if there's an error getting feed requirements
                            LaUtils.debug.log(f"Error getting feed requirements for {animal.name}: {e}", "Error")
                            myFeedForMaintenance = 3.3  # Default values
                            myFeedForGestating = 3.3
                            myFeedForLactating = 3.3
                            myFeedForOffspringPerKg = 3.3
                            myUseCommonGrazingLand = True
                            myUseSpecificGrazingLand = False
                            myGrazingLandCalories = 3333.3  # Default calories per hectare

                        # Calculate MCals needed for each phase
                        myGestatingMCals = myTotalMothers * myGestatingTime * myFeedForGestating
                        myLactatingMCals = myTotalMothers * myLactationTime * myFeedForLactating
                        myDaysForMaintenance = max(0, 365 - (myGestatingTime + myLactationTime))

                        myDryMothers = max(0, myTotalMothers - myTotalOffspring)
                        myDryMothersMCals = myDryMothers * 365.0 * myFeedForMaintenance
                        myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance
                        myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals
                        myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.0
                        myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365.0 - myWeaningAge)

                        # Set the total herd requirements in kg feed per year
                        myAnimalHerdMCalsRequired = (myGestatingMCals + myLactatingMCals +
                                                   myMaintenanceMCals + myAdultMalesMCals +
                                                   myOffspringMCals)

                        # Calculate total feed required in kg - this is what was missing
                        myTotalFeedRequiredKg = myAnimalHerdMCalsRequired

                        # Calculate grazing land area needed
                        # Convert feed requirements to calories using an approximation
                        # Average feed is about 2000 calories per kg (rough estimate)
                        feedToCaloriesFactor = 2000.0  # calories per kg of feed
                        totalCaloriesRequired = myAnimalHerdMCalsRequired * feedToCaloriesFactor

                        # Calculate area needed - divide total calories needed by calories per hectare provided by land
                        myGrazingAreaNeeded = totalCaloriesRequired / myGrazingLandCalories if myGrazingLandCalories > 0 else 0

                        # Convert to appropriate area units for display
                        areaUnitName = "hectares"
                        if hasattr(self, '_mAreaUnits') and self.mAreaUnits == AreaUnits.Dunum:
                            myGrazingAreaNeeded = myGrazingAreaNeeded * 10.0  # Convert hectares to dunum
                            areaUnitName = "dunums"

                        # Format the herd information for the report
                        totalHerd = myTotalMothers + myBreedingMalesRequired + myTotalOffspring

                        # Create the animal report
                        myAnimalReport = f"Calculation Report for {animal.name}\n"
                        myAnimalReport += f"===========================\n"
                        myAnimalReport += f"Animal meat calories: {myMCalsFromTheMeat:.2f} MCal\n"
                        myAnimalReport += f"Animal dairy calories: {myMCalsUtilizedFromDairy:.2f} MCal\n"
                        myAnimalReport += f"Population: {population_count} people\n"
                        myAnimalReport += f"Individual needs: {myMCalsIndividualAnnual:.2f} MCal/year\n"
                        myAnimalReport += f"Settlement needs: {myMCalsSettlementAnnual:.2f} MCal/year\n\n"

                        myAnimalReport += f"Herd Composition:\n"
                        myAnimalReport += f"- Adult females (breeding): {myTotalMothers:.1f}\n"
                        myAnimalReport += f"- Adult males (breeding): {myBreedingMalesRequired:.1f}\n"
                        myAnimalReport += f"- Offspring: {myTotalOffspring:.1f}\n"
                        myAnimalReport += f"- Total herd size: {totalHerd:.1f}\n\n"

                        myAnimalReport += f"Feed Requirements:\n"
                        myAnimalReport += f"- Gestating females: {myGestatingMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Lactating females: {myLactatingMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Adult maintenance: {myMaintenanceMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Adult males: {myAdultMalesMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Offspring growth: {myOffspringMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Total feed required: {myTotalFeedRequiredKg:.1f} kg/year\n\n"

                        myAnimalReport += f"Land Requirements:\n"
                        myAnimalReport += f"- Grazing land productivity: {myGrazingLandCalories:.1f} calories/{areaUnitName}\n"
                        myAnimalReport += f"- Grazing area needed: {myGrazingAreaNeeded:.2f} {areaUnitName}\n"

                        if myUseCommonGrazingLand:
                            myAnimalReport += f"- Using common grazing land: Yes\\n"
                        if myUseSpecificGrazingLand:
                            myAnimalReport += f"- Using specific grazing land: Yes\\n"

                    # Now we can safely store both the report and requirements
                    animalCalcsReportMap[animalGuid] = (myAnimalReport, myAnimalHerdMCalsRequired)
                    LaUtils.debug.log(f"Added detailed animal calculation for {animal.name if animal else animalGuid}", "Diet")

                except Exception as e:
                    LaUtils.debug.log(f"Error in animal calculation for GUID {animalGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # Set all values in the diet labels object
            self._setDietLabels(
                myDietLabels,
                myDairyCounter,           # Overall dairy MCals
                myCropCounter,            # Overall crop MCals
                myTameMeatCounter,        # Overall meat MCals
                myWildMeatCounter,        # Overall wild meat MCals
                myWildPlantCounter,       # Overall wild plants MCals
                dairyPercent,             # Overall dairy percent
                tameMeatPercent,          # Domestic meat percent
                cropPercent,              # Overall crop percent
                wildMeatPercent,          # Wild meat percent
                wildPlantPercent,         # Overall wild plant percent
                animalPercent,            # Overall meat percent
                plantPercent,             # Overall plant percent
                myMCalsIndividualAnnual,  # MCals individual annual
                myMCalsSettlementAnnual,  # MCals settlement annual
                0.0,                      # Overall dairy surplus MCals
                cropCalcsReportMap,       # Crop calcs report map
                animalCalcsReportMap      # Animal calcs report map
            )

            LaUtils.debug.log(f"Created report maps with {len(cropCalcsReportMap)} crops and {len(animalCalcsReportMap)} animals", "Diet")
            LaUtils.debug.log("doCalcsAnimalsFirstDairySeparate calculation completed successfully", "Diet")

            # Calculate fallow MCals from crops for animal grazing
            myMCalsFromFallowCounter = 0.0
            for cropGuid, reportPair in cropCalcsReportMap.items():
                cropParameter = LaUtils.getCropParameter(self.mCrops.get(cropGuid, ""))
                if cropParameter and hasattr(cropParameter, 'fallowRatio') and hasattr(cropParameter, 'fallowValue'):
                    try:
                        fallowRatio = float(str(cropParameter.fallowRatio))
                        fallowValue = float(str(cropParameter.fallowValue))

                        # Get the area from the report pair's second value
                        productionTarget = reportPair[1]

                        # Get the crop to calculate yield
                        crop = LaUtils.getCrop(cropGuid)
                        if crop:
                            myCropYield = float(str(crop.cropYield))
                            if hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Dunum":
                                myCropYield = myCropYield * 10.0  # Convert from Dunum to hectare

                            # Calculate area and fallow MCals
                            cropArea = productionTarget / myCropYield
                            fallowArea = cropArea * (fallowRatio / (1.0 + fallowRatio))
                            fallowMCals = fallowArea * fallowValue

                            myMCalsFromFallowCounter += fallowMCals
                            LaUtils.debug.log(f"Fallow from crop {crop.name}: {fallowArea:.2f} ha producing {fallowMCals:.2f} MCal", "Diet")
                    except Exception as e:
                        LaUtils.debug.log(f"Error calculating fallow for crop {cropGuid}: {str(e)}", "Error")

            # Now allocate the fallow grazing calories to reduce animal requirements
            if myMCalsFromFallowCounter > 0:
                LaUtils.debug.log(f"Allocating {myMCalsFromFallowCounter:.2f} MCal from fallow land to animals", "Diet")

                # Create a map of animal requirements for allocation
                animalMCalRequirementMap = {}
                for animalGuid in self._mValueMap:
                    if animalGuid in self.mAnimals:  # Only include animals in the current diet
                        animalMCalRequirementMap[animalGuid] = self._mValueMap[animalGuid]

                # Allocate the fallow land to animals
                self.allocateFallowGrazingLand(myMCalsFromFallowCounter, animalMCalRequirementMap)

                # Update the animal calculation reports with the new values after fallow allocation
                for animalGuid, requirements in self._mValueMap.items():
                    if animalGuid in animalCalcsReportMap:
                        myAnimalReport, oldRequirements = animalCalcsReportMap[animalGuid]
                        myAnimalReport = myAnimalReport or ""  # Initialize as an empty string if None or unbound
                        if oldRequirements > requirements:
                            reductionAmount = oldRequirements - requirements
                            myAnimalReport += f"\\nFallow Land Grazing:\\n"
                            myAnimalReport += f"Feed requirement reduced by {reductionAmount:.2f} MCal from fallow grazing\\n"
                            myAnimalReport += f"Final feed requirement: {requirements:.2f} MCal\\n"

                            # Update the report with new value
                            animalCalcsReportMap[animalGuid] = (myAnimalReport, requirements)
                            LaUtils.debug.log(f"Updated animal {animalGuid} with fallow grazing allocation", "Diet")

                # Recalculate overall values with the reduced requirements
                LaUtils.debug.log("Recalculating targets after fallow allocation", "Diet")

                # Update crop area targets to account for animal feed requirements
                for cropGuid, reportPair in cropCalcsReportMap.items():
                    cropReport, productionTarget = reportPair

                    # Check if any animals need grain from this crop
                    totalGrainNeeded = 0.0
                    for animalGuid, (myAnimalReport, requirements) in animalCalcsReportMap.items():
                        myAnimalReport = myAnimalReport or ""  # Initialize as an empty string if None or unbound

                        animalParameter = LaUtils.getAnimalParameter(self.mAnimals.get(animalGuid, ""))
                        if animalParameter and hasattr(animalParameter, 'fodderSourceMap'):
                            try:
                                fodderSources = animalParameter.fodderSourceMap()
                                if cropGuid in fodderSources:
                                    # Calculate requirement (simplified example)
                                    foodSource = fodderSources[cropGuid]
                                    totalGrainNeeded += requirements * 0.1  # Simplified calculation
                            except Exception as e:
                                LaUtils.debug.log(f"Error accessing fodderSourceMap for animal {animalGuid}: {e}", "Diet")

                    cropReport = cropReport or ""  # Initialize as an empty string if None or unbound

                    if totalGrainNeeded > 0:
                        newProductionTarget = productionTarget + totalGrainNeeded
                        cropReport += f"\\nGrain for Animal Feed:\\n"
                        cropReport += f"Additional production for animal feed: {totalGrainNeeded:.2f} kg\\n"
                        cropReport += f"Total production target: {newProductionTarget:.2f} kg\\n"

                        # Update the report
                        cropCalcsReportMap[cropGuid] = (cropReport, newProductionTarget)
                        LaUtils.debug.log(f"Updated crop {cropGuid} with animal feed requirements", "Diet")

            # Final diet percentages may need adjustment after all calculations
            LaUtils.debug.log("Finalizing diet calculations", "Diet")

            # Update the diet labels with final values including all reports
            myDietLabels._cropCalcsReportMap = cropCalcsReportMap
            myDietLabels._animalCalcsReportMap = animalCalcsReportMap

        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsAnimalsFirstDairySeparate: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels


    def toHtml(self) -> str:
        """Generate an HTML representation of the model."""
        html = f"<h1>Model Report</h1>\\n"
        html += f"<p><strong>Name:</strong> {self.name}</p>\\n"
        html += f"<p><strong>Population:</strong> {self.population}</p>\\n"
        html += f"<p><strong>Period:</strong> {self.period}</p>\\n"
        html += f"<p><strong>Projection:</strong> {self.projection}</p>\\n"
        html += f"<p><strong>Easting:</strong> {self.easting}</p>\\n"
        html += f"<p><strong>Northing:</strong> {self.northing}</p>\\n"
        html += f"<p><strong>Diet Percent:</strong> {self.dietPercent}%</p>\\n"
        html += f"<p><strong>Meat Percent:</strong> {self.meatPercent}%</p>\\n"
        html += f"<p><strong>Calories Per Person Daily:</strong> {self.caloriesPerPersonDaily}</p>\\n"
        html += f"<p><strong>Dairy Utilisation:</strong> {self.dairyUtilisation}%</p>\\n"
        html += f"<p><strong>Base on Plants:</strong> {self.baseOnPlants}</p>\\n"
        html += f"<p><strong>Include Dairy:</strong> {self.includeDairy}</p>\\n"
        html += f"<p><strong>Limit Dairy:</strong> {self.limitDairy}</p>\\n"
        html += f"<p><strong>Limit Dairy Percent:</strong> {self.limitDairyPercent}%</p>\\n"
        html += f"<p><strong>Common Land Value:</strong> {self.commonLandValue}</p>\\n"
        html += f"<p><strong>Common Land Area Units:</strong> {self.commonLandAreaUnits}</p>\\n"
        return html


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
        """Allocate fallow land to animals of a specific priority.

        Args:
            thePriority: Priority level being processed
            theAvailableFallowValue: MCals available from fallow land
            theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements

        Returns:
            float: Remaining MCals after allocation
        """
        from la.lib.lautils import LaUtils

        if theAvailableFallowValue <= 0 or not theAnimalMCalRequirementMap:
            return theAvailableFallowValue

        # Calculate total MCals needed by this priority group
        totalNeeded = sum(theAnimalMCalRequirementMap.values())

        # If we have more than enough fallow land
        if theAvailableFallowValue >= totalNeeded:
            # Each animal gets 100% of what it needs
            LaUtils.debug.log(f"Enough fallow land for all {thePriority} priority animals", "Diet")
            for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
                # Adjust the animal's MCal requirement in the value map
                if animalGuid in self._mValueMap:
                    self._mValueMap[animalGuid] = max(0, self._mValueMap[animalGuid] - mCalRequirement)
                    LaUtils.debug.log(f"Animal {animalGuid} requirement reduced by {mCalRequirement:.2f} MCal", "Diet")

            # Return remaining MCals
            return theAvailableFallowValue - totalNeeded

        # Otherwise, distribute proportionally
        else:
            LaUtils.debug.log(f"Not enough fallow land for all {thePriority} priority animals. Distributing {theAvailableFallowValue:.2f} MCal proportionally.", "Diet")
            for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
                # Calculate proportion
                proportion = mCalRequirement / totalNeeded
                allocatedMCals = theAvailableFallowValue * proportion

                # Adjust the animal's MCal requirement
                if animalGuid in self._mValueMap:
                    self._mValueMap[animalGuid] = max(0, self._mValueMap[animalGuid] - allocatedMCals)
                    LaUtils.debug.log(f"Animal {animalGuid} requirement reduced by {allocatedMCals:.2f} MCal", "Diet")

            # All MCals have been allocated
            return 0.0
