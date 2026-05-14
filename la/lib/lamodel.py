from qgis.PyQt.QtCore import pyqtSignal, pyqtProperty, QObject
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtXml import QDomDocument

from typing import Dict, List, Tuple, Union, Mapping

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound, EnergyType
from la.lib.la import LaFoodSourceMap, LaReportMap, LaTripleMap, LaFoodSource, LandFound, LandBeingGrazed
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
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
        self.mProjection: int
        self.mEasting = 0
        self.mNorthing = 0
        self.mEuclideanDistance = False
        self.mWalkingTime = False
        self.mPathDistance = False
        self.mPrecision = 5
        self.mDietPercent = 25
        self.mPercentOfDietThatIsFromCrops = 10
        self.mMeatPercent = 10
        self.mCommonLandAreaUnits = AreaUnits.Hectare # Will be properly set from AreaUnits enum
        self.mCommonLandValue = 0.0
        self.mCommonGrazingValue = 0.0
        self.mSpecificLandAreaUnits = AreaUnits.Hectare
        self.mSpecificLandEnergyType = EnergyType.KCalories
        self.mHerdSize = 0
        self.mFallowStatus: Status = Status.NotEnoughToCompletelySatisfy
        self.mFallowRatio = 1
        self.mDescription = ""
        self.mAreaUnits = 0
        self.mStatus = 0
        self.mLandBeingGrazed = 0
        self.mLandFound = 0
        self.mPriority = 0

        # Internal maps used by the calculation engine
        self.mCalcsCropsMap: Dict[str, str] = {}
        self.mCalcsAnimalsMap: Dict[str, str] = {}
        self.mValueMap: Dict[str, float] = {}
        self.mAnimalCalcReport: Dict[str, Tuple[str, float]] = {}
        self.mAreaTargetsCropsMap: Dict[str, float] = {}
        self.mAreaTargetsAnimalsMap: Dict[str, float] = {}

        # Diet calculation properties
        self.mAnimalsMap: dict[str, str] = {} # Corresponds to mAnimalsMap in C++
        self.mCropsMap: dict = {} # Corresponds to mCropsMap in C++
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
        self.mDietLabels: LaDietLabels = LaDietLabels()

        # Use MESSAGE_BUS for logging instead of QgsMessageLog
        self.mLogger: LaMessageBus = MESSAGE_BUS


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


    def setCommonLandValue(self, theValue: float, theAreaUnits: AreaUnits):
        """Set the common land value by converting to hectares first.

        This is a direct port of C++ version:
        void LaModel::setCommonLandValue(float theValue, AreaUnits theAreaUnits)
        { mCommonGrazingValue = LaUtils::convertAreaToHectares(theAreaUnits,theValue); }

        Args:
            theValue (float): The value in the specified area units
            theAreaUnits (AreaUnits): The units of the provided value (Dunum or Hectare)
        """
        # Store the raw value for future reference
        self.mCommonLandValue = float(theValue)

        # Convert to int as the C++ version expects an int
        myIntValue = int(theValue)

        # Convert to hectares and store in mCommonGrazingValue - this is the value used in calculations
        self.mCommonGrazingValue = LaUtils.convertAreaToHectares(theAreaUnits, myIntValue)

        LaUtils.debug.log(f"Set mCommonGrazingValue to {self.mCommonGrazingValue} hectares (converted from {theValue} {theAreaUnits.name})", "Debug")

        # Emit signal for UI updates
        self._commonLandValueChanged.emit()


    @pyqtProperty(float, notify=_commonGrazingValueChanged)
    def commonGrazingValue(self) -> float: # type: ignore
        # Ensure it returns a float, handle potential initial non-float values if necessary
        try:
            return float(self.mCommonGrazingValue)
        except (ValueError, TypeError):
            return 0.0 # Default value if conversion fails
    @commonGrazingValue.setter
    def commonGrazingValue(self, theValue: float):
         # Ensure the input is treated as float
        try:
            float_value = float(theValue)
            if self.mCommonGrazingValue != float_value:
                self.mCommonGrazingValue = float_value
                self._commonGrazingValueChanged.emit()
        except (ValueError, TypeError):
            LaUtils.debug.log(f"Invalid value passed to commonGrazingValue setter: {theValue}", "Error")

    @pyqtProperty(float, notify=_commonLandValueChanged)
    def commonLandValue(self) -> float: # type: ignore
        """Get the common land value (raw value before unit conversion).

        This is the 'raw' value in the current area units, not the converted value in hectares.
        For calculations, use commonGrazingValue which is always in hectares.

        Returns:
            float: The common land value in the current area units.
        """
        return float(self.mCommonLandValue)

    @commonLandValue.setter
    def commonLandValue(self, theValue: float) -> None:
        """Set the common land value.

        This setter delegates to setCommonLandValue to ensure proper conversion to hectares.
        The value is stored both as the raw value (mCommonLandValue) and the hectare-converted
        value (mCommonGrazingValue) which is used in actual calculations.

        Args:
            theValue (float): The value in the current area units
        """
        # Store the raw value for display purposes
        self.mCommonLandValue = float(theValue)
        # Use the proper method to calculate the hectare equivalent
        self.setCommonLandValue(theValue, self.mCommonLandAreaUnits)
        # Note: setCommonLandValue already emits _commonLandValueChanged


    @pyqtProperty(AreaUnits, notify=_commonLandAreaUnitsChanged)
    def commonLandAreaUnits(self) -> AreaUnits: # type: ignore
        # Return the enum member directly
        return self.mCommonLandAreaUnits
    @commonLandAreaUnits.setter
    def commonLandAreaUnits(self, theAreaUnits: AreaUnits):
        # Ensure it's an AreaUnits enum member
        if isinstance(theAreaUnits, AreaUnits):
            if self.mCommonLandAreaUnits != theAreaUnits:
                self.mCommonLandAreaUnits = theAreaUnits
                self._commonLandAreaUnitsChanged.emit()
        else:
            # Attempt conversion if a string name is passed (e.g., from UI)
            try:
                myUnitEnum = AreaUnits[str(theAreaUnits)]
                if self.mCommonLandAreaUnits != myUnitEnum:
                    self.mCommonLandAreaUnits = myUnitEnum
                    self._commonLandAreaUnitsChanged.emit()
            except (KeyError, TypeError):
                 LaUtils.debug.log(f"Invalid AreaUnits value passed to setter: {theAreaUnits}", "Error")


    @pyqtProperty(AreaUnits, notify=_specificLandAreaUnitsChanged) # Added property
    def specificLandAreaUnits(self) -> AreaUnits: # type: ignore
        return self.mSpecificLandAreaUnits
    @specificLandAreaUnits.setter
    def specificLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self.mSpecificLandAreaUnits != theAreaUnits:
            myUnitEnum = AreaUnits[str(theAreaUnits)]
            if self.mSpecificLandAreaUnits != myUnitEnum:
                self.mSpecificLandAreaUnits = myUnitEnum
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


    @pyqtProperty(QObject, notify=_dietLabelsChanged)
    def dietLabels(self) -> LaDietLabels: # type: ignore
        return self.mDietLabels
    @dietLabels.setter
    def dietLabels(self, theDietLabels: LaDietLabels):
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


    def fromXml(self, theXml: str) -> bool:
        """
        Initialize the LaModel instance from an XML string.

        Args:
            theXml (str): The XML string containing the model data.

        Returns:
            bool: True if successful, False otherwise
        """
        self.logMessage("method ==> bool LaModel::fromXml(QString theXml)")
        myFlag = ""
        self.logMessage("Loading model from xml")
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("model")
        if myTopElement.isNull():
            # TODO - just make this a warning
            self.logMessage("top element could not be found!")

        self.logMessage("Model::fromXml - guid found : " + myTopElement.attribute("guid"))
        self.setGuid(myTopElement.attribute("guid"))
        self.logMessage("Model::fromXml - guid set to : " + self.guid)

        self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.mPopulation = int(myTopElement.firstChildElement("population").text())
        self.mPeriod = LaUtils.xmlDecode(myTopElement.firstChildElement("period").text())
        self.mProjection = int(myTopElement.firstChildElement("projection").text())
        self.mEasting = int(myTopElement.firstChildElement("easting").text())
        self.mNorthing = int(myTopElement.firstChildElement("northing").text())

        myFlag = myTopElement.firstChildElement("euclideanDistance").text()
        if myFlag == "1":
            self.mEuclideanDistance = True
        else:
            self.mEuclideanDistance = False

        myFlag = myTopElement.firstChildElement("walkingTime").text()
        if myFlag == "1":
            self.mWalkingTime = True
        else:
            self.mWalkingTime = False

        myFlag = myTopElement.firstChildElement("pathDistance").text()
        if myFlag == "1":
            self.mPathDistance = True
        else:
            self.mPathDistance = False

        self.mPrecision = int(myTopElement.firstChildElement("precision").text())
        self.mDietPercent = int(myTopElement.firstChildElement("dietPercent").text())
        self.mPercentOfDietThatIsFromCrops = int(myTopElement.firstChildElement("plantPercent").text())
        self.mMeatPercent = int(myTopElement.firstChildElement("meatPercent").text())
        self.mCaloriesPerPersonDaily = int(myTopElement.firstChildElement("caloriesPerPersonDaily").text())

        self.mBaseOnPlants = int(myTopElement.firstChildElement("baseOnPlants").text())
        self.mIncludeDairy = int(myTopElement.firstChildElement("includeDairy").text())
        self.mLimitDairy = int(myTopElement.firstChildElement("limitDairy").text())
        self.mLimitDairyPercentage = int(myTopElement.firstChildElement("limitDairyPercent").text())

        self.mDairyUtilisation = int(myTopElement.firstChildElement("dairyUtilisation").text())
        return True

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

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """
        Proxy method that calls the function in lacalculations.py to calculate diet values
        when animals are prioritized and dairy is separate from meat.

        Returns:
            LaDietLabels: Object containing the calculated diet values and requirements
        """
        self.logMessage("Running doCalcsAnimalsFirstDairySeparate")

        # Import the lacalculations module
        from la.lib import lacalculations

        # Call the function and pass self as the model parameter
        return lacalculations.doCalcsAnimalsFirstDairySeparate(self)

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """
        Proxy method that calls the function in lacalculations.py to calculate diet values
        when plants are prioritized and dairy is separate from meat.

        Returns:
            LaDietLabels: Object containing the calculated diet values and requirements
        """
        try:
            from la.lib import lacalculations
            self.logMessage("Running doCalcsPlantsFirstDairySeparate")
            return lacalculations.doCalcsPlantsFirstDairySeparate(self)
        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsPlantsFirstDairySeparate: {str(e)}", "Error")
            return LaDietLabels()

    def doCalcsAnimalsFirstIncludeDairy(self) -> LaDietLabels:
        """
        Proxy method that calls the function in lacalculations.py to calculate diet values
        when animals are prioritized and dairy is included with meat.

        Returns:
            LaDietLabels: Object containing the calculated diet values and requirements
        """
        try:
            from la.lib import lacalculations
            self.logMessage("Running doCalcsAnimalsFirstIncludeDairy")
            return lacalculations.doCalcsAnimalsFirstIncludeDairy(self)
        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsAnimalsFirstIncludeDairy: {str(e)}", "Error")
            return LaDietLabels()

    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        """
        Proxy method that calls the function in lacalculations.py to calculate diet values
        when plants are prioritized and dairy is included with meat.

        Returns:
            LaDietLabels: Object containing the calculated diet values and requirements
        """
        try:
            from la.lib import lacalculations
            self.logMessage("Running doCalcsPlantsFirstIncludeDairy")
            return lacalculations.doCalcsPlantsFirstIncludeDairy(self)
        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsPlantsFirstIncludeDairy: {str(e)}", "Error")
            return LaDietLabels()

