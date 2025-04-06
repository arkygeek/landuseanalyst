from qgis.PyQt.QtCore import pyqtSignal, pyqtProperty
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging # Keep standard logging
from typing import Dict, List, Tuple, Union

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType

MESSAGE_BUS: LaMessageBus = LaMessageBus()

class LaModel(QDialog, LaSerialisable, LaGuid):
    """
    LaModel class represents the main model for the Landuse Analyst plugin.

    Attributes:
        _animalsChanged (pyqtSignal): Signal emitted when the animals change.
        _areaUnitsChanged (pyqtSignal): Signal emitted when the area units change.
        _baseOnPlantsChanged (pyqtSignal): Signal emitted when the base on plants changes.
        _caloriesPerPersonDailyChanged (pyqtSignal): Signal emitted when the calories per person daily changes.
        _commonLandAreaUnitsChanged (pyqtSignal): Signal emitted when the common land area units changes.
        _commonLandValueChanged (pyqtSignal): Signal emitted when the common land value changes.
        _specificLandAreaUnitsChanged (pyqtSignal): Signal emitted when the specific land area units changes. # Added attribute doc
        _specificLandEnergyTypeChanged (pyqtSignal): Signal emitted when the specific land energy type changes. # Added attribute doc
        _cropsChanged (pyqtSignal): Signal emitted when the crops change.
        _dairyUtilisationChanged (pyqtSignal): Signal emitted when the dairy utilisation changes.
        _descriptionChanged (pyqtSignal): Signal emitted when the description changes.
        _dietLabelsChanged (pyqtSignal): Signal emitted when the diet labels change.
        _dietPercentChanged (pyqtSignal): Signal emitted when the diet percent changes.
        _dietsChanged (pyqtSignal): Signal emitted when the diets change.
        _eastingChanged (pyqtSignal): Signal emitted when the easting changes.
        _euclideanDistanceChanged (pyqtSignal): Signal emitted when the euclidean distance changes.
        _fallowRatioChanged (pyqtSignal): Signal emitted when the fallow ratio changes.
        _fallowStatusChanged (pyqtSignal): Signal emitted when the fallow status changes.
        _guidChanged (pyqtSignal): Signal emitted when the GUID changes.
        _herdSizeChanged (pyqtSignal): Signal emitted when the herd size changes.
        _iconChanged (pyqtSignal): Signal emitted when the icon changes.
        _includeDairyChanged (pyqtSignal): Signal emitted when the include dairy changes.
        _landBeingGrazedChanged (pyqtSignal): Signal emitted when the land being grazed changes.
        _landFoundChanged (pyqtSignal): Signal emitted when the land found changes.
        _limitDairyChanged (pyqtSignal): Signal emitted when the limit dairy changes.
        _limitDairyPercentChanged (pyqtSignal): Signal emitted when the limit dairy percent changes.
        _meatPercentChanged (pyqtSignal): Signal emitted when the meat percent changes.
        _nameChanged (pyqtSignal): Signal emitted when the name changes.
        _northingChanged (pyqtSignal): Signal emitted when the northing changes.
        _pathDistanceChanged (pyqtSignal): Signal emitted when the path distance changes.
        _percentOfDietThatIsFromCropsChanged (pyqtSignal): Signal emitted when the percent of diet from crops changes.
        _periodChanged (pyqtSignal): Signal emitted when the period changes.
        _populationChanged (pyqtSignal): Signal emitted when the population changes.
        _precisionChanged (pyqtSignal): Signal emitted when the precision changes.
        _priorityChanged (pyqtSignal): Signal emitted when the priority changes.
        _projectionChanged (pyqtSignal): Signal emitted when the projection changes.
        _statusChanged (pyqtSignal): Signal emitted when the status changes.
        _walkingTimeChanged (pyqtSignal): Signal emitted when the walking time changes.
    """

    # region Signals
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
    _dairyMCaloriesChanged = pyqtSignal()
    _cropMCaloriesChanged = pyqtSignal()
    _animalMCaloriesChanged = pyqtSignal()
    _wildAnimalMCaloriesChanged = pyqtSignal()
    _wildPlantsMCaloriesChanged = pyqtSignal()
    _dairyPortionPctChanged = pyqtSignal()
    _tameMeatPortionPctChanged = pyqtSignal()
    _cropsPortionPctChanged = pyqtSignal()
    _wildAnimalPortionPctChanged = pyqtSignal()
    _wildPlantsPortionPctChanged = pyqtSignal()
    _animalPortionPctChanged = pyqtSignal()
    _plantsPortionPctChanged = pyqtSignal()
    _kiloCaloriesIndividualAnnualChanged = pyqtSignal()
    _megaCaloriesSettlementAnnualChanged = pyqtSignal()
    _dairySurplusMCaloriesChanged = pyqtSignal()
    _cropCalcsReportMapChanged = pyqtSignal(dict)
    _animalCalcsReportMapChanged = pyqtSignal(dict)
    _logCalculationStep = pyqtSignal(str) # for logging calculation steps to the UI
    # endregion Signals

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
            self.setGuid(theModel.guid) # this sets the GUID
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
            self.mSpecificLandAreaUnits = theModel.specificLandAreaUnits
            self.mSpecificLandEnergyType = theModel.specificLandEnergyType
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
        # Ensure we return an integer, handling potential stored strings
        try:
            # Attempt to convert directly if it's already numeric or a clean string
            return int(self.mDairyUtilisation)
        except (ValueError, TypeError):
            # If conversion fails, try cleaning the string (remove '%', spaces)
            try:
                cleaned_value = str(self.mDairyUtilisation).replace('%', '').strip()
                return int(cleaned_value)
            except (ValueError, TypeError):
                # If cleaning also fails, return a default value (e.g., 0 or handle as error)
                self.logger.warning(f"Could not convert mDairyUtilisation '{self.mDairyUtilisation}' to int. Returning 0.")
                return 0
    @dairyUtilisation.setter
    def dairyUtilisation(self, thePercent: Union[int, float, str]): # Allow string input
        try:
            # Try to convert input to a numeric value
            numeric_value = 0
            if isinstance(thePercent, str):
                # Clean the string if it's passed
                cleaned_value = thePercent.replace('%', '').strip()
                numeric_value = int(float(cleaned_value)) # Use float first for potential decimals
            else:
                numeric_value = int(thePercent)

            # Store the numeric value and emit signal if changed
            if not hasattr(self, 'mDairyUtilisation') or self.mDairyUtilisation != numeric_value:
                self.mDairyUtilisation = numeric_value
                self._dairyUtilisationChanged.emit()
        except (ValueError, TypeError) as e:
            self.logger.error(f"Failed to set dairyUtilisation with value '{thePercent}': {e}")
            # Optionally set a default value or raise the error
            # self.mDairyUtilisation = 0 # Example default
            # self._dairyUtilisationChanged.emit()


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
        return self._mGuid # type: ignore
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
        self.logMessage("method ==> def requiredValue(self, theAnimalGuid: str) -> float:\n")
        self.logMessage("animal prodn target = calorie target of animal / food value\n")
        self.logMessage(f"Animal Production Target: {myAnimalProductionTarget}\n")
        self.logMessage(f"Slaughter animals required: {myAnimalsRequired}\n")
        self.logMessage(f"Birth events per year: {myBirthsPerYear}\n")
        self.logMessage(f"Offspring per mother yearly = {myOffspringPerMotherYearly}\n")
        self.logMessage(f"Mothers needed step one = {myMothersNeededStepOne}\n")
        self.logMessage(f"Males step one = {myMalesStepOne}\n")
        self.logMessage(f"Females step one = {myFemalesStepOne}\n")
        self.logMessage(f"Mother replacements per year = {myMotherReplacementsPerYear}\n")
        self.logMessage(f"Additional mothers = {myAdditionalMothers}\n")
        self.logMessage(f"Males step two = {myMalesStepTwo}\n")
        self.logMessage(f"Females step two = {myFemalesStepTwo}\n")
        self.logMessage(f"Total mothers = {myTotalMothers}\n")
        self.logMessage(f"Total males = {myTotalMales}\n")
        self.logMessage(f"Total females = {myTotalFemales}\n")
        self.logMessage(f"Total juveniles = {myTotalJuveniles}\n")
        self.logMessage(f"Total adult females value (Kg) = {myTotalMothersValueRequired}\n")
        self.logMessage(f"Total juveniles value (Kg) = {myTotalJuvenilesValueRequired}\n")
        self.logMessage(f"Total value (Kg) needed to feed animals = {myValueNeededToFeedAnimals}\n")
        self.logMessage("method ==> method ==> def requiredValue(self, theAnimalGuid: str) -> float:\n")
        self.logMessage(f"Animal: {myAnimal.name}\n")
        self.logMessage(f"Breeding stock: {myTotalMothers}\n")
        self.logMessage(f"Juveniles: {myTotalJuveniles}\n")
        self.logMessage(f"Kg value needed annually to feed the entire herd: {myReturnValue}\n")
        self.logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

        return myReturnValue


    def fromXml(self, theXmlData):
        """
        Initialize the LaModel instance from an XML string.

        Args:
            theXmlData (str): The XML string containing the model data.
        """
        root = ET.fromstring(theXmlData)

        self.setGuid(root.get('guid'))
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

    def setDairyMCalories(self, value: float):
        self.dairyMCalories = value
        if hasattr(self, 'dairyMCaloriesChanged'):
            self._dairyMCaloriesChanged.emit(value)

    def setCropMCalories(self, value: float):
        self.cropMCalories = value
        if hasattr(self, 'cropMCaloriesChanged'):
            self._cropMCaloriesChanged.emit(value)

    def setAnimalMCalories(self, value: float):
        self.animalMCalories = value
        if hasattr(self, 'animalMCaloriesChanged'):
            self._animalMCaloriesChanged.emit(value)

    def setWildAnimalMCalories(self, value: float):
        self.wildAnimalMCalories = value
        if hasattr(self, 'wildAnimalMCaloriesChanged'):
            self._wildAnimalMCaloriesChanged.emit(value)

    def setWildPlantsMCalories(self, value: float):
        self.wildPlantsMCalories = value
        if hasattr(self, 'wildPlantsMCaloriesChanged'):
            self._wildPlantsMCaloriesChanged.emit(value)

    def setDairyPortionPct(self, value: float):
        self.dairyPortionPct = value
        if hasattr(self, 'dairyPortionPctChanged'):
            self._dairyPortionPctChanged.emit(value)

    def setTameMeatPortionPct(self, value: float):
        self.tameMeatPortionPct = value
        if hasattr(self, 'tameMeatPortionPctChanged'):
            self._tameMeatPortionPctChanged.emit(value)

    def setCropsPortionPct(self, value: float):
        self.cropsPortionPct = value
        if hasattr(self, 'cropsPortionPctChanged'):
            self._cropsPortionPctChanged.emit(value)

    def setWildAnimalPortionPct(self, value: float):
        self.wildAnimalPortionPct = value
        if hasattr(self, 'wildAnimalPortionPctChanged'):
            self._wildAnimalPortionPctChanged.emit(value)

    def setWildPlantsPortionPct(self, value: float):
        self.wildPlantsPortionPct = value
        if hasattr(self, 'wildPlantsPortionPctChanged'):
            self._wildPlantsPortionPctChanged.emit(value)

    def setAnimalPortionPct(self, value: float):
        self.animalPortionPct = value
        if hasattr(self, 'animalPortionPctChanged'):
            self._animalPortionPctChanged.emit(value)

    def setPlantsPortionPct(self, value: float):
        self.plantsPortionPct = value
        if hasattr(self, 'plantsPortionPctChanged'):
            self._plantsPortionPctChanged.emit(value)

    def setKiloCaloriesIndividualAnnual(self, value: float):
        self.kiloCaloriesIndividualAnnual = value
        if hasattr(self, 'kiloCaloriesIndividualAnnualChanged'):
            self._kiloCaloriesIndividualAnnualChanged.emit(value)

    def setMegaCaloriesSettlementAnnual(self, value: float):
        self.megaCaloriesSettlementAnnual = value
        if hasattr(self, 'megaCaloriesSettlementAnnualChanged'):
            self._megaCaloriesSettlementAnnualChanged.emit(value)

    def setDairySurplusMCalories(self, value: float):
        self.dairySurplusMCalories = value
        if hasattr(self, 'dairySurplusMCaloriesChanged'):
            self._dairySurplusMCaloriesChanged.emit(value)

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
                theDietLabels._dairyMCaloriesChanged.emit(theOverallDairyMCals)
                theDietLabels._cropMCaloriesChanged.emit(theOverallCropsMCals)
                theDietLabels._animalMCaloriesChanged.emit(theOverallMeatMCals)
                theDietLabels._wildAnimalMCaloriesChanged.emit(theOverallWildMeatMCals)
                theDietLabels._wildPlantsMCaloriesChanged.emit(theOverallWildPlantsMCals)
                theDietLabels._dairyPortionPctChanged.emit(theOverallDairyPercent * 100.0)
                theDietLabels._tameMeatPortionPctChanged.emit(theDomesticMeatPercent * 100.0)
                theDietLabels._cropsPortionPctChanged.emit(theOverallCropPercent * 100.0)
                theDietLabels._wildAnimalPortionPctChanged.emit(theWildMeatPercent * 100.0)
                theDietLabels._wildPlantsPortionPctChanged.emit(theOverallWildPlantPercent * 100.0)
                theDietLabels._plantsPortionPctChanged.emit(theOverallPlantPercent * 100.0)
                theDietLabels._animalPortionPctChanged.emit(theOverallMeatPercent * 100.0)
                theDietLabels._kiloCaloriesIndividualAnnualChanged.emit(theMCalsIndividualAnnual)
                theDietLabels._megaCaloriesSettlementAnnualChanged.emit(theMCalsSettlementAnnual)
                theDietLabels._dairySurplusMCaloriesChanged.emit(theOverallDairySurplusMCals)
                theDietLabels._cropCalcsReportMapChanged.emit(theCropCalcsReportMap)
                theDietLabels._animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)
            except Exception as e:
                LaUtils.debug.log(f"Error emitting diet label signals: {str(e)}", "Error")

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error updating diet labels in model: {str(e)}", "Error")


    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        from la.lib.lautils import LaUtils
        myMCalsIndividualAnnual: float = self.caloriesPerPersonDaily * 365.0
        myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * self.population
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

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++ declaration but not used in this simplified version

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
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * (self._mDietPercent / 100.0) * (self._mMeatPercent / 100.0)  # tame meat
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * (self._mDietPercent / 100.0) * myWildMeatPortion  # wild meat

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
            self.setDietLabels(
                myDietLabels,
                myDairyMCalorieCounter,     # Overall dairy MCals
                myOverallCropsMCals,        # Overall crop MCals
                myTameMeatMCalorieCounter,  # Tame meat MCals
                myWildMeatMCalorieCounter,  # Wild meat MCals
                myOverallWildPlantsMCals,   # Wild plants MCals
                myOverallDairyPercent,      # Overall dairy percent
                myDomesticMeatPercent,      # Domestic meat percent
                myCropPercent,              # Overall crop percent
                myWildMeatPercent,          # Wild meat percent
                myWildPlantPercent,         # Overall wild plant percent
                myOverallMeatPercent,       # Overall meat percent
                myOverallPlantPercent,      # Overall plant percent
                myMCalsIndividualAnnual * 1000.0,  # Convert back to kCal
                myMCalsSettlementAnnual,    # MCals settlement annual
                myOVerallDairySurplusMCals, # Dairy surplus MCals
                myCropCalcsReportMap,       # Crop calcs report map
                myAnimalCalcsReportMap      # Animal calcs report map
            )

            # Log results
            LaUtils.debug.log(f"Results - Meat: {myOverallMeatPercent*100:.2f}%, Plant: {myOverallPlantPercent*100:.2f}%, Dairy: {myOverallDairyPercent*100:.2f}%", "Diet")
            LaUtils.debug.log("doCalcsPlantsFirstDairySeparate calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels

    def doCalcsAnimalsFirstIncludeDairy(self) -> LaDietLabels: # this was working in c++
        """
        Calculate diet values when animals are prioritized and dairy is included with meat.
        Ported directly from C++ version, using PyQt property getters.
        """
        # from la.lib.lautils import LaUtils
        # from la.lib.ladietlabels import LaDietLabels
        # from la.lib.laanimal import LaAnimal
        # from la.lib.laanimalparameter import LaAnimalParameter # Assuming this is needed for LaUtils.getAnimalParameter

        myDietLabels = LaDietLabels()
        # myAnimal instance is created inside the loop

        try:
            # Initialize base calculations using getter methods
            # Convert Python properties (0-100) to fractions (0.0-1.0) where C++ uses fractions
            myMCalsIndividualAnnual = float(self.caloriesPerPersonDaily) * 365.0 # Assume kCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * float(self.population) # Assume kCal
            myDairyMCalorieCounter = 0.0 # Assume kCal counter
            myTameMeatMCalorieCounter = 0.0 # Assume kCal counter
            myWildMeatMCalorieCounter = 0.0 # Assume kCal counter
            mySelectedAnimalsMap = self.animals() # Use getter

            # Calculate coefficients using getter methods and converting % to fractions
            # C++ mMeatPercent, mDietPercent etc. are likely fractions (0.0-1.0)
            # Python properties return int (0-100), so divide by 100.0
            c1 = 1.0 - (float(self.meatPercent) / 100.0)
            c8 = float(self.dairyUtilisation) / 100.0
            c10 = float(self.population)
            c11 = float(self.caloriesPerPersonDaily) # kCal/person/day
            c14 = c10 * c11 * 365.0 # Total annual kCal
            c15 = float(self.dietPercent) / 100.0
            c12 = float(self.percentOfDietThatIsFromCrops) / 100.0
            e15 = c14 * c15 # Total kCal from animal portion

            LaUtils.debug.log("Starting animal calculations (Animals First, Include Dairy - Strict Port)", "Diet")

            # Process each animal in the map
            for myAnimalGuid, myAnimalParameterGuid in mySelectedAnimalsMap.items():
                # Get animal and parameter objects
                myAnimal = LaUtils.getAnimal(myAnimalGuid)
                myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)

                if not myAnimal or not myAnimalParameter:
                    LaUtils.debug.log(f"Skipping animal {myAnimalGuid} due to missing data.", "Warning")
                    continue

                # Calculate animal-specific coefficients using getter methods
                # Perform calculations exactly as in C++
                c2 = float(myAnimal.getMilkGramsPerDay) * 0.001 # g -> kg
                c3 = float(myAnimal.milkFoodValue)
                c4 = float(myAnimal.lactationTime) # days
                c5 = float(myAnimal. weaningAge) # days
                c6 = float(myAnimal.killWeight) # kg
                c7 = float(myAnimal.usableMeat) * 0.01 # % -> fraction
                # Ensure non-negative lactation period for calculation
                e2 = c2 * c3 * max(0.0, (c4 - c5)) # kCal/animal/cycle
                e3 = e2 * c8 # Usable kCal/animal/cycle (uses fractional c8)
                c9 = float(myAnimal.meatFoodValue) # Assume kCal/kg
                e10 = e3 + (c9 * c7 * c6) # Total usable kCal (milk+meat) / animal cycle

                # Calculate number of animal cycles needed (e7)
                # Check for division by zero, matching C++ implicit handling
                e7 = (e15 * (1.0 - c1)) / e10 if e10 != 0.0 else 0.0 # Uses fractional c1

                # Calculate kCal contributions for this animal type
                c21 = e7 * e3 # Dairy kCal
                c23 = e7 * c6 * c7 * c9 # Tame Meat kCal
                c22 = e15 - c21 - c23 # Wild Meat kCal (remainder)

                # Update total counters
                myDairyMCalorieCounter += c21
                myWildMeatMCalorieCounter += c22
                myTameMeatMCalorieCounter += c23

                # Optional: Add detailed debug logging if needed, mirroring C++ qDebug comments
                # LaUtils.debug.log(f"  Animal {myAnimal.getName()}: c1={c1:.3f}, c2={c2:.3f}, c3={c3:.1f}, c4={c4}, c5={c5}, c6={c6}, c7={c7:.3f}", "DietDebug")
                # LaUtils.debug.log(f"  Animal {myAnimal.getName()}: e2={e2:.1f}, e3={e3:.1f}, c9={c9:.1f}, e10={e10:.1f}, e7={e7:.2f}", "DietDebug")
                # LaUtils.debug.log(f"  Animal {myAnimal.getName()}: c21(Dairy)={c21:.1f}, c23(Tame)={c23:.1f}, c22(Wild)={c22:.1f}", "DietDebug")

            # Calculate final coefficients (plant kCals and overall portions)

                c24 = (1.0 - c12) * (c14 - e15) # Wild plant kCal
                c25 = c12 * (c14 - e15)         # Crop kCal
                c30 = c24 / c14                 # Wild plant portion
                c31 = c25 / c14                 # Crop portion
                c28 = myWildMeatMCalorieCounter / c14 # Wild meat portion
                c29 = myTameMeatMCalorieCounter / c14 # Tame meat portion
                c27 = myDairyMCalorieCounter / c14    # Dairy portion

            # Set diet label values using setter methods
            # Use C++ conversion factors exactly (e.g., *.001*.001 for MCals)
            # Assuming counters are kCal and target is MCal/GCal as per C++ factors
            myMCalConversionFactor: float = 0.001 * 0.001 # Matches C++ *.001*.001

            myDietLabels.dairyMCalories = myDairyMCalorieCounter * 0.001 * 0.001
            myDietLabels.cropMCalories = c25 * myMCalConversionFactor
            myDietLabels.animalMCalories = myTameMeatMCalorieCounter * myMCalConversionFactor
            myDietLabels.wildAnimalMCalories = myWildMeatMCalorieCounter * myMCalConversionFactor
            myDietLabels.wildPlantsMCalories = c24 * myMCalConversionFactor

            # Set percentages (portions c27, c29 etc. are fractions, convert to %)
            myDietLabels.dairyPortionPct = c27 * 100.0
            myDietLabels.tameMeatPortionPct = c29 * 100.0
            myDietLabels.cropsPortionPct = c31 * 100.0
            myDietLabels.wildAnimalPortionPct = c28 * 100.0
            myDietLabels.wildPlantsPortionPct = c30 * 100.0

            # Set overall animal/plant portions based on input diet percent (0-100)
            # Matches C++ logic: mDietPercent*100. - c27*100. -> (mDietPercent_frac * 100.0) - (c27 * 100.0)
            # Python property self.dietPercent() is already 0-100
            myDietLabels.animalPortionPct = ((float(self.dietPercent) * 100.0) - (c27 * 100.0))
            myDietLabels.plantsPortionPct = (1.0 - (float(self.dietPercent))) * 100.0

            # Set annual calorie values
            myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual # Already in kCal
            # C++ uses *.001 for settlement MCals
            myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual * 0.001

            LaUtils.debug.log("Diet calculations completed successfully (Animals First, Include Dairy - Strict Port)", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error during strict port of doCalcsAnimalsFirstIncludeDairy: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(traceback.format_exc(), "Error")
            # Return empty labels on error to prevent downstream issues
            return LaDietLabels()

        return myDietLabels

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels: # this was working in c++
        """Calculate diet values when animals are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsAnimalsFirstDairySeparate calculation", "Diet")

        try:
            # Get base values from internal attributes
            myCaloriesDaily = float(self.mCaloriesPerPersonDaily)
            myPopulationCount = float(self.mPopulation)
            myMeatPercent = float(self.mMeatPercent) / 100.0  # Convert to decimal
            myDietPercent = float(self.mDietPercent) / 100.0  # Convert to decimal
            myDairyUtilisation = float(self.mDairyUtilisation) / 100.0 # Convert to decimal
            myLimitDairyPercent = float(self.mLimitDairyPercent) / 100.0 # Convert to decimal
            myLimitDairyBool = bool(self.mLimitDairy)
            myPlantPercent = 1.0 - myDietPercent # Overall plant portion
            myDomesticCropPortion = float(self.mPercentOfDietThatIsFromCrops) / 100.0 # Convert to decimal

            LaUtils.debug.log(f"Input parameters - calories_daily: {myCaloriesDaily}, population: {myPopulationCount}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {myMeatPercent*100}%, diet_percent: {myDietPercent*100}%", "Diet")
            LaUtils.debug.log(f"Dairy parameters - utilisation: {myDairyUtilisation*100}%, limit: {myLimitDairyBool}, limit_percent: {myLimitDairyPercent*100}%", "Diet")
            LaUtils.debug.log(f"Plant parameters - plant_percent: {myPlantPercent*100}%, domestic_crop_portion: {myDomesticCropPortion*100}%", "Diet")

            # Calculate basic values
            myMCalsIndividualAnnual = myCaloriesDaily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * myPopulationCount

            LaUtils.debug.log(f"myMCalsIndividualAnnual = {myMCalsIndividualAnnual}", "Diet")
            LaUtils.debug.log(f"myMCalsSettlementAnnual = {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters
            myDairyMCalorieCounter = 0.0
            myTameMeatMCalorieCounter = 0.0
            myWildMeatCounter = myMCalsSettlementAnnual * myDietPercent * (1.0 - myMeatPercent)  # Wild meat portion (initial estimate)
            myCropCounter = 0.0 # Will be calculated later
            myWildPlantCounter = 0.0 # Will be calculated later

            LaUtils.debug.log(f"Initial myDairyMCalorieCounter = {myDairyMCalorieCounter}", "Diet")
            LaUtils.debug.log(f"Initial myTameMeatMCalorieCounter = {myTameMeatMCalorieCounter}", "Diet")
            LaUtils.debug.log(f"Initial myWildMeatCounter = {myWildMeatCounter}", "Diet")

            # Create report maps for crops and animals
            myCropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}
            # Map to store animal requirements for fallow allocation
            myAnimalMCalRequirementMap = {}
            # Map to store fodder needs per crop
            myFodderNeedsPerCrop = {}

            # Populate animal report map with detailed calculations
            for myAnimalGuid, myParamGuid in self.mAnimals.items():
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                LaUtils.debug.log("--------==        Looping through the animals         ==-------", "Diet")
                LaUtils.debug.log("--------==--------------------------------------------==-------", "Diet")
                try:
                    animal = LaUtils.getAnimal(myAnimalGuid)
                    animalParameter = LaUtils.getAnimalParameter(myParamGuid)

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
                        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * myDietPercent * myMeatPercent # B3
                        myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * max(0, (myLactationTime - myWeaningAge)) # B4 - Ensure non-negative time
                        myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal # B5
                        myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilisation # B6

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
                            if myCropGuid not in myFodderNeedsPerCrop:
                                myFodderNeedsPerCrop[myCropGuid] = 0.0
                            myFodderNeedsPerCrop[myCropGuid] += myGrainToAddKg
                            LaUtils.debug.log(f"        myGrain = {myGrain}", "Diet")
                            LaUtils.debug.log(f"        myFodder = {myFodder}", "Diet")
                            LaUtils.debug.log(f"        myDays = {myDays}", "Diet")
                            LaUtils.debug.log(f"        Grain to add (kg) for {animal.name} from {myCrop.name}: {myGrainToAddKg}", "Diet")
                            LaUtils.debug.log(f"        Current total grain needed for {myCrop.name}: {myFodderNeedsPerCrop[myCropGuid]}", "Diet")

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
                        myAnimalMCalRequirementMap[myAnimalGuid] = myAnimalHerdMCalsRequired

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
            myDairyLimit = myLimitDairyPercent if myLimitDairyBool else 1.0 # B22
            myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B11
            myWildMeatPercent = (1.0 - myMeatPercent) * myDietPercent # B13 - Recalculate based on total diet percent
            myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0 # B21
            myNewLimit = (1.0 - myDomesticMeatPercent - myWildMeatPercent) if myLimitSatisfies else myDairyLimit # B20
            myPotentialDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0
            myPotentialDairyLessThanLimitBool = myPotentialDairyPercent < myDairyLimit # B19
            myNewDairyMCals = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual # B18
            myOverallDairyPercent = myNewDairyMCals / myMCalsSettlementAnnual if myMCalsSettlementAnnual > 0 else 0 # B12 & B8

            # --- Calculate final Plant/Crop percentages ---
            myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent # B7
            myOverallPlantPercent = max(0, 1.0 - myOverallMeatPercent - myOverallDairyPercent) # B6 - Ensure non-negative
            myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion # B14
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myDomesticCropPortion) # B15 - Adjusted logic

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
            for myCropGuid, myParamGuid in self.mCrops.items():
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                LaUtils.debug.log("**********         Looping through the crops          **********", "Diet")
                LaUtils.debug.log("        **--------------------------------------------**        ", "Diet")
                try:
                    myCrop = LaUtils.getCrop(myCropGuid)
                    cropParameter = LaUtils.getCropParameter(myParamGuid)

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
                        myAnimalKgAdd1 = myFodderNeedsPerCrop.get(myCropGuid, 0.0)

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
                        myCropCalcsReportMap[myCropGuid] = (cropReport, myTotalAreaNeeded)
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
                self._mValueMap = myAnimalMCalRequirementMap.copy() # Initialize _mValueMap with current requirements
                self.allocateFallowGrazingLand(myMCalsFromFallowCounter, self._mValueMap)
                # animalMCalRequirementMap now holds the *adjusted* requirements after fallow
                myAnimalMCalRequirementMap = self._mValueMap.copy() # Update the map with adjusted values

            # ----------- Final Animal Area Target Calculation -----------
            LaUtils.debug.log("--------==---------------------------------------------==-------", "Diet")
            LaUtils.debug.log("--------==        Looping to Update Animal Map         ==-------", "Diet")
            LaUtils.debug.log("--------==---------------------------------------------==-------", "Diet")
            myFinalAnimalAreaTargets = {} # Store final area targets separately
            for myAnimalGuid, myReportPair in myAnimalCalcsReportMap.items():
                try:
                    myReport, _ = myReportPair # Original report, second value is initial MCal req
                    myAdjustedMCalTarget = myAnimalMCalRequirementMap.get(myAnimalGuid, 0.0) # Get requirement *after* fallow
                    LaUtils.debug.log(f"        *** Processing animal {myAnimalGuid}", "Diet")
                    LaUtils.debug.log(f"        *** Adjusted MCal Target (after fallow): {myAdjustedMCalTarget}", "Diet")

                    # Get land productivity value
                    myParamGuid = self.mAnimals.get(myAnimalGuid, "")
                    animalParameter = LaUtils.getAnimalParameter(myParamGuid) if myParamGuid else None
                    myLandValue = 0.0
                    if animalParameter:
                        if getattr(animalParameter, 'useCommonGrazingLand', False):
                            myLandValue = self.mCommonLandValue
                        elif getattr(animalParameter, 'useSpecificGrazingLand', False):
                            myLandValue = float(str(getattr(animalParameter, 'valueSpecificGrazingLand', 0.0)))
                        # Handle energy type conversion if necessary (assuming values are MCal/ha for now)
                        # TODO: Implement TDN handling based on self.mSpecificLandEnergyType

                    if myLandValue <= 0:
                         # Fallback if specific value is zero or not set
                         myLandValue = self.mCommonLandValue
                         LaUtils.debug.log(f"        *** Using common land value: {myLandValue}", "Diet")

                    if int(myLandValue) <= 0:
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
            # Directly set diet label values instead of using _setDietLabels
            self.setDairyMCalories(myOverallDairyMCals)
            self.setCropMCalories(myOverallCropsMCals)
            self.setAnimalMCalories(myOverallDomesticMeatMCals)
            self.setWildAnimalMCalories(myOverallWildMeatMCals)
            self.setWildPlantsMCalories(myOverallWildPlantsMCals)
            self.setDairyPortionPct(myOverallDairyPercent * 100.0)
            self.setTameMeatPortionPct(myDomesticMeatPercent * 100.0)
            self.setCropsPortionPct(myOverallCropPercent * 100.0)
            self.setWildAnimalPortionPct(myWildMeatPercent * 100.0)
            self.setWildPlantsPortionPct(myOverallWildPlantPercent * 100.0)
            self.setAnimalPortionPct(myOverallMeatPercent * 100.0)
            self.setPlantsPortionPct(myOverallPlantPercent * 100.0)
            self.setKiloCaloriesIndividualAnnual(myMCalsIndividualAnnual * 1000.0)  # Convert back to kCal
            self.setMegaCaloriesSettlementAnnual(myMCalsSettlementAnnual)
            self.setDairySurplusMCalories(myOverallDairySurplusMCals)

            # Add the final area target maps to the diet labels object
            myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
            myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap
            myDietLabels.cropAreaTargetsMap = {guid: area for guid, (_, area) in myCropCalcsReportMap.items()}
            myDietLabels.animalAreaTargetsMap = myFinalAnimalAreaTargets

            LaUtils.debug.log("doCalcsAnimalsFirstDairySeparate calculation completed successfully", "Diet")

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