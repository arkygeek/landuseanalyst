from qgis.PyQt.QtCore import pyqtSignal, pyqtProperty
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging # Keep standard logging
from typing import Dict, List, Tuple, Union

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType, LaReportMap
from la.lib.laanimal import LaAnimal

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
    def commonLandValue(self) -> float:
        """Get the common land value in calories per hectare."""
        return float(self.mCommonLandValue) if isinstance(self.mCommonLandValue, (int, float)) else 0.0

    @commonLandValue.setter
    def commonLandValue(self, theValue: Union[float, str]) -> None:
        """Set the common land value in calories per hectare.
        Converts the value to hectares if needed based on current area units.
        """
        try:
            if isinstance(theValue, str):
                # Handle non-numeric values like 'Dunum'
                if theValue.lower() == 'dunum':
                    value = 10.0  # Example conversion factor for 'Dunum' to hectares
                else:
                    raise ValueError(f"Invalid string value for commonLandValue: {theValue}")
            else:
                value = float(theValue)

            if self.mCommonLandAreaUnits == AreaUnits.Dunum:
                # Convert from Dunum to Hectare if needed
                value = LaUtils.convertAreaToHectares('Dunum', value)

            self.mCommonLandValue = value
            self._commonLandValueChanged.emit()
        except (ValueError, TypeError) as e:
            LaUtils.debug.log(f"Error setting commonLandValue: {e}", "Error")


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


    def fromXml(self, theXml: str) -> bool:
        """
        Load model data from an XML string.

        Args:
            theXml: XML string containing model data

        Returns:
            True if loaded successfully, False otherwise
        """
        from qgis.PyQt.QtXml import QDomDocument
        from la.lib.lautils import LaUtils

        try:
            myDocument = QDomDocument("mydocument")
            if not myDocument.setContent(theXml):
                LaUtils.debug.log("Invalid XML content", "Error")
                return False

            myTopElement = myDocument.firstChildElement("model")
            if myTopElement.isNull():
                LaUtils.debug.log("Missing top-level 'model' element", "Error")
                return False

            # Set GUID
            self.setGuid(myTopElement.attribute("guid"))

            # Parse elements with safe conversions
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
            self.mPopulation = int(myTopElement.firstChildElement("population").text() or 0)
            self.mPeriod = LaUtils.xmlDecode(myTopElement.firstChildElement("period").text())
            self.mProjection = int(myTopElement.firstChildElement("projection").text() or 0)
            self.mEasting = int(myTopElement.firstChildElement("easting").text() or 0)
            self.mNorthing = int(myTopElement.firstChildElement("northing").text() or 0)

            # Parse boolean values
            self.mEuclideanDistance = myTopElement.firstChildElement("euclideanDistance").text() == "1"
            self.mWalkingTime = myTopElement.firstChildElement("walkingTime").text() == "1"
            self.mPathDistance = myTopElement.firstChildElement("pathDistance").text() == "1"

            # Parse float values
            self.mPrecision = float(myTopElement.firstChildElement("precision").text() or 0.0)
            self.mDietPercent = float(myTopElement.firstChildElement("dietPercent").text() or 0.0)
            self.mPercentOfDietThatIsFromCrops = float(myTopElement.firstChildElement("plantPercent").text() or 0.0)
            self.mMeatPercent = float(myTopElement.firstChildElement("meatPercent").text() or 0.0)
            self.mCaloriesPerPersonDaily = float(myTopElement.firstChildElement("caloriesPerPersonDaily").text() or 0.0)

            # Parse additional boolean values
            self.mBaseOnPlants = myTopElement.firstChildElement("baseOnPlants").text() == "1"
            self.mIncludeDairy = myTopElement.firstChildElement("includeDairy").text() == "1"
            self.mLimitDairy = myTopElement.firstChildElement("limitDairy").text() == "1"

            # Parse float values for dairy
            self.mLimitDairyPercentage = float(myTopElement.firstChildElement("limitDairyPercent").text() or 0.0)
            self.mDairyUtilisation = float(myTopElement.firstChildElement("dairyUtilisation").text() or 0.0)

            return True

        except Exception as e:
            LaUtils.debug.log(f"Error parsing XML: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(traceback.format_exc(), "Error")
            return False


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

    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels: # NOT working
        from la.lib.lautils import LaUtils
        myMCalsIndividualAnnual: float = int(str(self.caloriesPerPersonDaily)) * 365.0
        myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * int(str(self.population))
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++ declaration but not used in this simplified version

        # Get property values from internal attributes (following C++ variable naming)
        try:
            # Base values - matching C++ variable names
            myMCalsIndividualAnnual = float(self.mCaloriesPerPersonDaily) * 365.0 * 0.001  # Convert to annual MCals
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * self.mPopulation
            myDairyMCalorieCounter = 0.0
            myTameMeatMCalorieCounter = 0.0
            myWildMeatMCalorieCounter = 0.0
            mySelectedAnimalsMap: Dict[str, str] = self.mAnimals  # Similar to C++ QMap<QString,QString>

            # C++ style variable declarations (c1, c8, etc.)
            myWildMeatFraction: float = 1.0 - (self.mMeatPercent / 100.0)  # Decimal form of meat percent was c1
            myDairyUtilizationFraction: float = self.mDairyUtilisation / 100.0     # Decimal form of dairy utilization
            mySettlementPopulation = self.mPopulation
            myCaloriesPerPersonDaily = self.mCaloriesPerPersonDaily
            mySettlementAnnualMCalReqmt = float(str(mySettlementPopulation)) * float(str(myCaloriesPerPersonDaily)) * 365.0 * 0.001         # Settlement annual MCal
            myAnimalDietFraction: float = self.mDietPercent / 100.0         # Decimal form of diet percentdoCalcsPlantsFirstIncludeDairy

            # Calculate MCals for different food sources
            # In this simplified version, we'll estimate values that would normally
            # come from detailed animal and crop calculations

            # Initialize counters (simplified calculation)
            myDairyMCalorieCounter = myMCalsSettlementAnnual * myAnimalDietFraction * 0.05  # 5% of animal diet
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * myAnimalDietFraction * (self.mMeatPercent / 100.0)  # Tame meat percent
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * myAnimalDietFraction * myWildMeatFraction  # Wild meat percent
            myCropMCalories = myMCalsSettlementAnnual * (1.0 - myAnimalDietFraction) * (self.mPercentOfDietThatIsFromCrops / 100.0)  # Crop percent
            myWildPlantsMCalories = myMCalsSettlementAnnual * (1.0 - myAnimalDietFraction) * (1.0 - self.mPercentOfDietThatIsFromCrops / 100.0)  # Wild plant percent
            myOverallDairySurplusMCals = 0.0
            # Calculate percentages (as in C++ implementation)
            myTotalMCalories = myMCalsSettlementAnnual
            myTameMeatPercent = myTameMeatMCalorieCounter / myTotalMCalories
            myWildMeatPercent = myWildMeatMCalorieCounter / myTotalMCalories
            myCropPercent = myCropMCalories / myTotalMCalories
            myWildPlantPercent = myWildPlantsMCalories / myTotalMCalories
            myDairyPercent = myDairyMCalorieCounter / myTotalMCalories

            # Calculate overall percentages
            myOverallMeatPercent = myTameMeatPercent + myWildMeatPercent  # Combined meat percent
            myOverallPlantPercent = myCropPercent + myWildPlantPercent    # Combined plant percent

            # Report maps for crops and animals (empty in simplified version)
            myCropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}
            myDairySurplus = 0.0 # No surplus dairy
            # ----------- Set Final Diet Labels -----------
            self.setDairyMCalories(myDairyMCalorieCounter)
            self.setCropMCalories(myCropMCalories)
            self.setAnimalMCalories(myTameMeatMCalorieCounter)
            self.setWildAnimalMCalories(myWildMeatMCalorieCounter)
            self.setWildPlantsMCalories(myWildPlantsMCalories)
            self.setDairyPortionPct(myDairyPercent * 100.0)
            self.setTameMeatPortionPct(myTameMeatPercent * 100.0)
            self.setCropsPortionPct(myCropPercent * 100.0)
            self.setWildAnimalPortionPct(myWildMeatPercent * 100.0)
            self.setWildPlantsPortionPct(myWildPlantPercent * 100.0)
            self.setAnimalPortionPct(myOverallMeatPercent * 100.0)
            self.setPlantsPortionPct(myOverallPlantPercent * 100.0)
            self.setKiloCaloriesIndividualAnnual(myMCalsIndividualAnnual * 1000.0)  # Convert back to kCal
            self.setMegaCaloriesSettlementAnnual(myMCalsSettlementAnnual)
            self.setDairySurplusMCalories(myOverallDairySurplusMCals)

            # Log results
            LaUtils.debug.log(f"doCalcsPlantsFirstIncludeDairy - Animal: {myOverallMeatPercent*100:.2f}%, Plant: {myOverallPlantPercent*100:.2f}%", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels: # NOT working
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++ declaration but not used in this simplified version
        myMCalsSettlementAnnual = 0.0
        myMCalsIndividualAnnual = 0.0
        myDairyMCalorieCounter = 0.0
        myDomesticMeatPercent = 0.0
        myDomesticCropPortion = 0.0
        myPlantPercent = 0.0
        myWildMeatPortion = 0.0
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
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * (float(str(self.dietPercent)) / 100.0) * (float(str(self.meatPercent)) / 100.0)  # tame meat
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * (float(str(self.dietPercent)) / 100.0) * myWildMeatPortion  # wild meat

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
            myOverallDairySurplusMCals = myFirstDairySurplusBool if myFirstDairySurplusBool > 0 else 0.0

            # Calculate percentages of the total settlement MCals
            myDomesticMeatPercent = myOverallDomesticMeatMCals / myMCalsSettlementAnnual
            myWildMeatPercent = myOverallWildMeatMCals / myMCalsSettlementAnnual
            myCropPercent = myOverallCropsMCals / myMCalsSettlementAnnual
            myWildPlantPercent = myOverallWildPlantsMCals / myMCalsSettlementAnnual

            # Create report maps (empty in simplified version)
            myCropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}
            myFinalAnimalAreaTargets = {}
            # # Set all values in the diet labels object
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

            # create myDietLabels object and populate it with calculated values
            myDietLabels = LaDietLabels()  # Assuming this is a class that holds the diet labels
            myDietLabels.dairyMCalories = myOverallDairyMCals
            myDietLabels.cropMCalories = myOverallCropsMCals
            myDietLabels.animalMCalories = myOverallDomesticMeatMCals
            myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
            myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals
            myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.0
            myDietLabels.tameMeatPortionPct = myDomesticMeatPercent * 100.0
            myDietLabels.cropsPortionPct = myCropPercent * 100.0
            myDietLabels.wildAnimalPortionPct = myWildMeatPercent * 100.0
            myDietLabels.wildPlantsPortionPct = myWildPlantPercent * 100.0
            myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.0
            myDietLabels.animalPortionPct = myOverallMeatPercent * 100.0
            myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0  # Convert back to kCal
            myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
            myDietLabels.dairySurplusMCalories = myOverallDairySurplusMCals
            myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
            myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap

            # Emit signals for changes (if applicable)

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
            myMCalsIndividualAnnual = self.caloriesPerPersonDaily * 365.0 # Assume kCal
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
            myDietLabels.animalPortionPct = ((float(str(self.dietPercent)) * 100.0) - (c27 * 100.0))
            myDietLabels.plantsPortionPct = (1.0 - (float(str(self.dietPercent)))) * 100.0

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

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is separate."""
        from la.lib.lautils import LaUtils
        from la.lib.ladietlabels import LaDietLabels
        from la.lib.laanimal import LaAnimal
        from la.lib.laanimalparameter import LaAnimalParameter

        # Initialize maps if they don't exist
        if not hasattr(self, '_mCalcsCropsMap'):
            self._mCalcsCropsMap = {}
        if not hasattr(self, '_mCalcsAnimalsMap'):
            self._mCalcsAnimalsMap = {}
        if not hasattr(self, '_mValueMap'):
            self._mValueMap = {}
        if not hasattr(self, '_mAnimalCalcReport'):
            self._mAnimalCalcReport = {}

        # Clear maps
        self._mCalcsCropsMap.clear()
        self._mCalcsAnimalsMap.clear()
        self._mValueMap.clear()
        self._mAnimalCalcReport.clear()

        myCropCalcsReportMap = LaReportMap
        myAnimalCalcsReportMap = LaReportMap

        myDietLabels = LaDietLabels()
        myMCalsIndividualAnnual = float(str(self.mCaloriesPerPersonDaily)) * 365.0 * 0.001  # Convert to MCal
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * float(str(self.mPopulation))
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0

        # Base calculations using string conversion for PyQt properties
        myWildMeatPortion = 1.0 - float(str(self.mMeatPercent)) / 100.0
        myDomesticMeatPortion = float(str(self.mMeatPercent)) / 100.0
        myDairyUtilization = float(str(self.mDairyUtilisation)) / 100.0
        myDairyLimitPercent = float(str(self.mLimitDairyPercent)) / 100.0
        myLimitDairyBool = bool(self.mLimitDairy)

        try:
            # Process each animal
            for myAnimalGuid, myAnimalParameterGuid in self.mAnimals.items():
                myAnimal = LaUtils.getAnimal(myAnimalGuid)
                myAnimalParameter = LaUtils.getAnimalParameter(myAnimalParameterGuid)

                if not myAnimal or not myAnimalParameter:
                    continue

                # Calculate base animal values using string conversion for PyQt properties
                myMilkKgPerDay = float(str(myAnimal.milkGramsPerDay)) * 0.001  # g -> kg
                myMilkFoodValue = float(str(myAnimal.milkFoodValue)) * 0.001
                myLactationTime = float(str(myAnimal.lactationTime))
                myWeaningAge = float(str(myAnimal.weaningAge))
                myKillWeight = float(str(myAnimal.killWeight))
                myUsablePortionOfAnimal = float(str(myAnimal.usableMeat)) * 0.01
                myMeatValueMCal = float(str(myAnimal.meatFoodValue)) * 0.001

                # Calculate animal contribution
                myAnimalContributionToMeatPortion = float(str(myAnimalParameter.percentTameMeat)) * 0.01
                myAnimalMCalTarget = (myAnimalContributionToMeatPortion * myMCalsSettlementAnnual *
                                    float(str(self.mDietPercent)) / 100.0 * float(str(self.mMeatPercent)) / 100.0)

                # Calculate dairy and meat values
                myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge)
                myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal
                myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization

                # Calculate meat MCals
                myFinalOffspringValue = myValuePerOffspring
                myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue if myFinalOffspringValue > 0 else 0
                myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue
                myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear

                # Update counters
                myTameMeatMCalorieCounter += myMCalsFromTheMeat
                myDairyMCalorieCounter += myMCalsUtilizedFromDairy

                # Record in value map
                self._mValueMap[myAnimalGuid] = myAnimalMCalTarget

                # Add detailed report for this animal
                myAnimalReport = f"Animal: {myAnimal.name}, Meat MCals: {myMCalsFromTheMeat:.2f}, Dairy MCals: {myMCalsUtilizedFromDairy:.2f}"
                myAnimalCalcsReportMap[myAnimalGuid] = (myAnimal.name, myMCalsFromTheMeat + myMCalsUtilizedFromDairy)
                LaUtils.debug.log(myAnimalReport, "AnimalReport")

            # Assign the populated report map to the diet labels
            myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap

            # Calculate final percentages
            myDairyLimit = myDairyLimitPercent if myLimitDairyBool else 1.0
            myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
            myWildMeatPercent = myWildMeatPortion * float(str(self.mDietPercent)) / 100.0

            myLimitSatisfies = (myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1.0
            myNewLimit = min(1.0 - myDomesticMeatPercent - myWildMeatPercent, myDairyLimit) if myLimitSatisfies else myDairyLimit

            myPotentialDairyLessThanLimitBool = (myDairyMCalorieCounter / myMCalsSettlementAnnual) < myDairyLimit
            myNewDairy = myDairyMCalorieCounter if myPotentialDairyLessThanLimitBool else myNewLimit * myMCalsSettlementAnnual
            myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual

            # Calculate overall percentages
            myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent
            myOverallPlantPercent = 1.0 - myOverallMeatPercent - myOverallDairyPercent
            myOverallCropPercent = myOverallPlantPercent * float(str(self.mPercentOfDietThatIsFromCrops)) / 100.0
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - float(str(self.mPercentOfDietThatIsFromCrops)) / 100.0)

            # Calculate MCal values
            myOverallDomesticMeatMCals = myTameMeatMCalorieCounter
            myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual
            myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual
            myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
            myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual

            # Set diet label values
            myDietLabels.dairyMCalories = myOverallDairyMCals
            myDietLabels.cropMCalories = myOverallCropsMCals
            myDietLabels.animalMCalories = myOverallDomesticMeatMCals
            myDietLabels.wildAnimalMCalories = myOverallWildMeatMCals
            myDietLabels.wildPlantsMCalories = myOverallWildPlantsMCals
            myDietLabels.dairyPortionPct = myOverallDairyPercent * 100.0
            myDietLabels.tameMeatPortionPct = myDomesticMeatPercent * 100.0
            myDietLabels.cropsPortionPct = myOverallCropPercent * 100.0
            myDietLabels.wildAnimalPortionPct = myWildMeatPercent * 100.0
            myDietLabels.wildPlantsPortionPct = myOverallWildPlantPercent * 100.0
            myDietLabels.animalPortionPct = myOverallMeatPercent * 100.0
            myDietLabels.plantsPortionPct = myOverallPlantPercent * 100.0
            myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual * 1000.0
            myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

            # Handle dairy surplus
            myDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
            myDietLabels.dairySurplusMCalories = max(0.0, myDairySurplusBool)

            return myDietLabels

        except Exception as e:
            LaUtils.debug.log(f"Error in calculations: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            return LaDietLabels()

    @pyqtProperty(float, notify=_commonLandValueChanged)
    def getCommonLandValue(self) -> float:
        """Get the common land value in calories per hectare."""
        return float(str(self.mCommonLandValue)) if isinstance(self.mCommonLandValue, (int, float, str)) else 0.0

    # Fix animal and crop attribute access
    def _GetAnimalValue(self, animal: LaAnimal, prop_name: str) -> float:
        """Helper method to safely get float values from animal properties."""
        if prop_name == "milkGramsPerDay":
            return float(str(animal.mMilkGramsPerDay))
        elif prop_name == "milkFoodValue":
            return float(str(animal.mMilkFoodValue))
        elif prop_name == "lactationTime":
            return float(str(animal.mLactationTime))
        elif prop_name == "weaningAge":
            return float(str(animal.mWeaningAge))
        elif prop_name == "killWeight":
            return float(str(animal.mKillWeight))
        elif prop_name == "usableMeat":
            return float(str(animal.mUsableMeat))
        elif prop_name == "meatFoodValue":
            return float(str(animal.mMeatFoodValue))
        return 0.0

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