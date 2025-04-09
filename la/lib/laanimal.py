import os
from typing import Optional, Type, Union, Dict, Any, cast
from dataclasses import dataclass
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal
from PyQt5.QtXml import QDomDocument, QDomElement
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import EnergyType as LaEnergyType, AreaUnits as LaAreaUnits
from la.resources_rc import *

class LaAnimal(QObject, LaSerialisable, LaGuid):
    """Represents an animal species and its characteristics for land use analysis.

    This class defines all the biological, nutritional and production parameters
    needed to model animal husbandry in archaeozoological contexts.

    Properties:
        Basic Info:
            name (str): Common name of the animal species
            description (str): Detailed description
            imageFile (str): Path to image file representing the animal

        Meat Production:
            meatFoodValue (int): Caloric value per kg of meat
            usableMeat (int): Percentage of carcass weight usable for meat
            killWeight (int): Weight at which animals are slaughtered in kg
            adultWeight (int): Weight of mature adult in kg
            growTime (int): Weeks from birth to slaughter weight
            deathRate (int): Percentage mortality before reaching usable age

        Reproduction:
            conceptionEfficiency (int): Percentage success rate of breeding
            femalesToMales (int): Ratio of breeding females to males
            youngPerBirth (int): Average number of offspring per birth
            gestationTime (int): Days of pregnancy
            estrousCycle (int): Days between breeding cycles
            sexualMaturity (int): Age in months when breeding can begin
            breedingExpectancy (int): Years of productive breeding life

        Early Life:
            weaningAge (int): Weeks until offspring stop nursing
            weaningWeight (int): Weight in kg at weaning

        Dairy:
            milk (bool): Whether species produces harvestable milk
            milkGramsPerDay (int): Daily milk production in grams
            milkFoodValue (int): Calories per kg of milk
            lactationTime (int): Days milk production continues

        Fibers:
            fleece (bool): Whether species produces harvestable fiber
            fleeceWeightKg (int): Annual fiber harvest per animal in kg

        Energy Requirements:
            feedEnergyType (EnergyType): Unit for feed requirements
            gestating (int): Daily calories needed when pregnant
            lactating (int): Daily calories needed when producing milk
            maintenance (int): Daily calories for basic survival
            juvenile (int): Daily calories needed by growing young
    """

    # Signal definitions
    _nameChanged = pyqtSignal(str)
    _descriptionChanged = pyqtSignal(str)
    _meatFoodValueChanged = pyqtSignal(int)
    _usableMeatChanged = pyqtSignal(int)
    _killWeightChanged = pyqtSignal(int)
    _growTimeChanged = pyqtSignal(int)
    _deathRateChanged = pyqtSignal(int)
    _feedEnergyTypeChanged = pyqtSignal(LaEnergyType)
    _gestatingChanged = pyqtSignal(int)
    _lactatingChanged = pyqtSignal(int)
    _maintenanceChanged = pyqtSignal(int)
    _juvenileChanged = pyqtSignal(int)
    _sexualMaturityChanged = pyqtSignal(int)
    _breedingExpectancyChanged = pyqtSignal(int)
    _conceptionEfficiencyChanged = pyqtSignal(int)
    _femalesToMalesChanged = pyqtSignal(int)
    _adultWeightChanged = pyqtSignal(int)
    _youngPerBirthChanged = pyqtSignal(int)
    _weaningAgeChanged = pyqtSignal(int)
    _weaningWeightChanged = pyqtSignal(int)
    _gestationTimeChanged = pyqtSignal(int)
    _estrousCycleChanged = pyqtSignal(int)
    _lactationTimeChanged = pyqtSignal(int)
    _milkChanged = pyqtSignal(bool)  # Changed from int to bool to match property type
    _milkGramsPerDayChanged = pyqtSignal(int)
    _milkFoodValueChanged = pyqtSignal(int)
    _fleeceChanged = pyqtSignal(bool)  # Changed from int to bool to match property type
    _fleeceWeightKgChanged = pyqtSignal(float)  # Changed to float for more precise measurements
    _imageFileChanged = pyqtSignal(str)
    _femalesPerMaleChanged = pyqtSignal(int)  # Changed from femalesToMalesChanged

    def __init__(self, theAnimal: Optional['LaAnimal'] = None, parent: Optional[QObject] = None):
        """Initialize an animal with default values or copy from existing.

        Args:
            theAnimal: Optional existing animal to copy from
            parent: Optional Qt parent object
        """
        super().__init__(parent)
        self._initializeDefaults()

        if isinstance(theAnimal, LaAnimal):
            self._copyFromAnimal(theAnimal)

    def _initializeDefaults(self) -> None:
        """Set default values for all properties."""
        self.mGuid: str = LaGuid.setGuid(self, None)
        # Basic info
        self.mName = "No Name Set"
        self.mDescription = "Not Set"
        self.mImageFile = ""

        # Meat production
        self.mMeatFoodValue = 3000  # Calories per kg
        self.mUsableMeat = 50  # Percent
        self.mKillWeight = 100  # kg
        self.mAdultWeight = 0  # kg
        self.mGrowTime = 10  # weeks
        self.mDeathRate = 10  # percent

        # Reproduction
        self._sexualMaturity = 18  # months
        self._breedingExpectancy = 5  # years
        self._youngPerBirth = 1
        self._gestationTime = 120  # days
        self._estrousCycle = 21  # days
        self._conceptionEfficiency = 0  # percent
        self._femalesToMales = 0  # ratio

        # Early life
        self._weaningAge = 12  # weeks
        self._weaningWeight = 30  # kg

        # Dairy
        self._milk = False
        self._milkGramsPerDay = 0
        self._milkFoodValue = 0
        self._lactationTime = 0  # days

        # Fiber
        self._fleece = False
        self._fleeceWeightKg = 0

        # Energy
        self._feedEnergyType = LaEnergyType.KCalories
        self._gestating = 0  # calories/day
        self._lactating = 0  # calories/day
        self._maintenance = 0  # calories/day
        self._juvenile = 0  # calories/day

    def _copyFromAnimal(self, theAnimal: 'LaAnimal') -> None:
        """Copy all attributes from another animal instance.

        Args:
            theAnimal: Source animal to copy from
        """
        self.mGuid = theAnimal.guid
        self.mName = theAnimal.name
        self.mDescription = theAnimal.description
        self.mMeatFoodValue = theAnimal.meatFoodValue
        self.mUsableMeat = theAnimal.usableMeat
        self.mKillWeight = theAnimal.killWeight
        self.mGrowTime = theAnimal.growTime
        self.mDeathRate = theAnimal.deathRate
        self._feedEnergyType = theAnimal.feedEnergyType
        self._gestating = theAnimal.gestating
        self._lactating = theAnimal.lactating
        self._maintenance = theAnimal.maintenance
        self._juvenile = theAnimal.juvenile
        self._sexualMaturity = theAnimal.sexualMaturity
        self._breedingExpectancy = theAnimal.breedingExpectancy
        self._youngPerBirth = theAnimal.youngPerBirth
        self._weaningAge = theAnimal.weaningAge
        self._weaningWeight = theAnimal.weaningWeight
        self._conceptionEfficiency = theAnimal.conceptionEfficiency
        self._femalesToMales = theAnimal.femalesPerMale
        self.mAdultWeight = theAnimal.adultWeight
        self._gestationTime = theAnimal.gestationTime
        self._estrousCycle = theAnimal.estrousCycle
        self._lactationTime = theAnimal.lactationTime
        self._milk = theAnimal.milk
        self._milkGramsPerDay = theAnimal.milkGramsPerDay
        self._milkFoodValue = theAnimal.milkFoodValue
        self._fleece = theAnimal.fleece
        self._fleeceWeightKg = theAnimal.fleeceWeightKg
        self.mImageFile = theAnimal.imageFile

    def validate(self) -> Dict[str, str]:
        """Validate the animal's attributes.

        Performs comprehensive validation of all animal attributes to ensure they are within
        acceptable ranges and logically consistent.

        Returns:
            Dict[str, str]: Dictionary of field names and error messages for invalid fields
        """
        errors = {}

        # Basic info validation
        if not cast(str, self.mName):
            errors['name'] = "Name is required"
        if not cast(str, self.mDescription):
            errors['description'] = "Description is required"

        # Meat production validation
        if cast(int, self.mMeatFoodValue) <= 0:
            errors['meatFoodValue'] = "Meat food value must be positive"
        if cast(int, self.mUsableMeat) < 0 or cast(int, self.mUsableMeat) > 100:
            errors['usableMeat'] = "Usable meat must be between 0-100%"
        if cast(int, self.mKillWeight) <= 0:
            errors['killWeight'] = "Kill weight must be positive"
        if cast(int, self.mGrowTime) <= 0:
            errors['growTime'] = "Grow time must be positive"
        if cast(int, self.mDeathRate) < 0 or cast(int, self.mDeathRate) > 100:
            errors['deathRate'] = "Death rate must be between 0-100%"

        # Reproduction validation
        if cast(int, self._sexualMaturity) <= 0:
            errors['sexualMaturity'] = "Sexual maturity must be positive"
        if cast(int, self._breedingExpectancy) <= 0:
            errors['breedingExpectancy'] = "Breeding expectancy must be positive"
        if cast(int, self._youngPerBirth) <= 0:
            errors['youngPerBirth'] = "Young per birth must be positive"
        if cast(int, self._gestationTime) <= 0:
            errors['gestationTime'] = "Gestation time must be positive"
        if cast(int, self._estrousCycle) <= 0:
            errors['estrousCycle'] = "Estrous cycle must be positive"
        if cast(int, self._conceptionEfficiency) < 0 or cast(int, self._conceptionEfficiency) > 100:
            errors['conceptionEfficiency'] = "Conception efficiency must be between 0-100%"
        if cast(int, self._femalesToMales) <= 0:
            errors['femalesToMales'] = "Females to males ratio must be positive"

        # Early life validation
        if cast(int, self._weaningAge) <= 0:
            errors['weaningAge'] = "Weaning age must be positive"
        if cast(int, self._weaningWeight) <= 0:
            errors['weaningWeight'] = "Weaning weight must be positive"

        # Dairy validation
        if self._milk:
            if cast(int, self._milkGramsPerDay) <= 0:
                errors['milkGramsPerDay'] = "Milk grams per day must be positive when milk is enabled"
            if cast(int, self._milkFoodValue) <= 0:
                errors['milkFoodValue'] = "Milk food value must be positive when milk is enabled"
            if cast(int, self._lactationTime) <= 0:
                errors['lactationTime'] = "Lactation time must be positive when milk is enabled"

        # Fiber validation
        if self._fleece and cast(float, self._fleeceWeightKg) <= 0:
            errors['fleeceWeightKg'] = "Fleece weight must be positive when fleece is enabled"

        # Energy requirements validation
        if cast(int, self._gestating) < 0:
            errors['gestating'] = "Gestating energy requirement cannot be negative"
        if cast(int, self._lactating) < 0:
            errors['lactating'] = "Lactating energy requirement cannot be negative"
        if cast(int, self._maintenance) < 0:
            errors['maintenance'] = "Maintenance energy requirement cannot be negative"
        if cast(int, self._juvenile) < 0:
            errors['juvenile'] = "Juvenile energy requirement cannot be negative"

        # Logical consistency checks
        if cast(int, self.mKillWeight) <= cast(int, self._weaningWeight):
            errors['killWeight'] = "Kill weight must be greater than weaning weight"
        if cast(int, self.mAdultWeight) <= cast(int, self._weaningWeight):
            errors['adultWeight'] = "Adult weight must be greater than weaning weight"
        if cast(int, self._weaningAge) >= cast(int, self.mGrowTime):
            errors['weaningAge'] = "Weaning age must be less than grow time"

        return errors

    # Properties with type hints and docstrings
    @pyqtProperty(str, notify=_nameChanged)
    def name(self) -> str: # type: ignore
        """Get the animal's common name."""
        return cast(str, self.mName)

    @name.setter
    def name(self, value: str) -> None:
        """Set the animal's common name.

        Args:
            value: The name to set
        """
        if self.mName != value:
            self.mName = value
            self._nameChanged.emit(value)

    @pyqtProperty(str, notify=_descriptionChanged)
    def description(self) -> str: # type: ignore
        """Get the animal's description."""
        return cast(str, self.mDescription)

    @description.setter
    def description(self, value: str) -> None:
        """Set the animal's description.

        Args:
            value: The description to set
        """
        if self.mDescription != value:
            self.mDescription = value
            self._descriptionChanged.emit(value)

    @pyqtProperty(int, notify=_meatFoodValueChanged)
    def meatFoodValue(self) -> int: # type: ignore
        """Get the animal's meat food value."""
        return cast(int, self.mMeatFoodValue)

    @meatFoodValue.setter
    def meatFoodValue(self, value: int) -> None:
        """Set the animal's meat food value.

        Args:
            value: The meat food value to set
        """
        if self.mMeatFoodValue != value:
            self.mMeatFoodValue = value
            self._meatFoodValueChanged.emit(value)

    @pyqtProperty(int, notify=_usableMeatChanged)
    def usableMeat(self) -> int: # type: ignore
        """Get the animal's usable meat percentage."""
        return cast (int, int(str(self.mUsableMeat)))

    @usableMeat.setter
    def usableMeat(self, value):
        """Set the animal's usable meat percentage.

        Args:
            value: The usable meat percentage to set
        """
        if self.mUsableMeat != value:
            self.mUsableMeat = value
            self._usableMeatChanged.emit(value)

    @pyqtProperty(int, notify=_killWeightChanged)
    def killWeight(self) -> int: # type: ignore
        """Get the animal's kill weight."""
        return cast(int, self.mKillWeight)

    @killWeight.setter
    def killWeight(self, value: int) -> None:
        """Set the animal's kill weight.

        Args:
            value: The kill weight to set
        """
        if self.mKillWeight != value:
            self.mKillWeight = value
            self._killWeightChanged.emit(value)

    @pyqtProperty(int, notify=_growTimeChanged)
    def growTime(self) -> int: # type: ignore
        """Get the animal's grow time."""
        return cast(int, self.mGrowTime)

    @growTime.setter
    def growTime(self, value: int) -> None:
        """Set the animal's grow time.

        Args:
            value: The grow time to set
        """
        if self.mGrowTime != value:
            self.mGrowTime = value
            self._growTimeChanged.emit(value)

    @pyqtProperty(int, notify=_deathRateChanged)
    def deathRate(self) -> int: # type: ignore
        """Get the animal's death rate."""
        return cast(int, self.mDeathRate)

    @deathRate.setter
    def deathRate(self, value: int) -> None:
        """Set the animal's death rate.

        Args:
            value: The death rate to set
        """
        if self.mDeathRate != value:
            self.mDeathRate = value
            self._deathRateChanged.emit(value)

    @pyqtProperty(LaEnergyType, notify=_feedEnergyTypeChanged)
    def feedEnergyType(self): # type: ignore
        """Get the animal's feed energy type."""
        return self._feedEnergyType

    @feedEnergyType.setter
    def feedEnergyType(self, theFeedEnergyType):
        """Set the animal's feed energy type.

        Args:
            value: The feed energy type to set
        """
        if self._feedEnergyType != theFeedEnergyType:
            self._feedEnergyType = theFeedEnergyType
            self._feedEnergyTypeChanged.emit(theFeedEnergyType)

    @pyqtProperty(int, notify=_gestatingChanged)
    def gestating(self) -> int: # type: ignore
        """Get the animal's gestating value."""
        return cast(int, self._gestating)

    @gestating.setter
    def gestating(self, value: int) -> None:
        """Set the animal's gestating value.

        Args:
            value: The gestating value to set
        """
        if self._gestating != value:
            self._gestating = value
            self._gestatingChanged.emit(value)

    @pyqtProperty(int, notify=_lactatingChanged)
    def lactating(self) -> int: # type: ignore
        """Get the animal's lactating value."""
        return cast(int, self._lactating)

    @lactating.setter
    def lactating(self, value: int) -> None:
        """Set the animal's lactating value.

        Args:
            value: The lactating value to set
        """
        if self._lactating != value:
            self._lactating = value
            self._lactatingChanged.emit(value)

    @pyqtProperty(int, notify=_maintenanceChanged)
    def maintenance(self) -> int: # type: ignore
        """Get the animal's maintenance value."""
        return cast(int, self._maintenance)

    @maintenance.setter
    def maintenance(self, value: int) -> None:
        """Set the animal's maintenance value.

        Args:
            value: The maintenance value to set
        """
        if self._maintenance != value:
            self._maintenance = value
            self._maintenanceChanged.emit(value)

    @pyqtProperty(int, notify=_juvenileChanged)
    def juvenile(self) -> int: # type: ignore
        """Get the animal's juvenile value."""
        return cast(int, self._juvenile)

    @juvenile.setter
    def juvenile(self, value: int) -> None:
        """Set the animal's juvenile value.

        Args:
            value: The juvenile value to set
        """
        if self._juvenile != value:
            self._juvenile = value
            self._juvenileChanged.emit(value)

    @pyqtProperty(int, notify=_sexualMaturityChanged)
    def sexualMaturity(self) -> int: # type: ignore
        """Get the animal's sexual maturity value."""
        return cast(int, self._sexualMaturity)

    @sexualMaturity.setter
    def sexualMaturity(self, value: int) -> None:
        """Set the animal's sexual maturity value.

        Args:
            value: The sexual maturity value to set
        """
        if self._sexualMaturity != value:
            self._sexualMaturity = value
            self._sexualMaturityChanged.emit(value)

    @pyqtProperty(int, notify=_breedingExpectancyChanged)
    def breedingExpectancy(self) -> int: # type: ignore
        """Get the animal's breeding expectancy value."""
        return cast(int, self._breedingExpectancy)

    @breedingExpectancy.setter
    def breedingExpectancy(self, value: int) -> None:
        """Set the animal's breeding expectancy value.

        Args:
            value: The breeding expectancy value to set
        """
        if self._breedingExpectancy != value:
            self._breedingExpectancy = value
            self._breedingExpectancyChanged.emit(value)

    @pyqtProperty(int, notify=_conceptionEfficiencyChanged)
    def conceptionEfficiency(self) -> int: # type: ignore
        """Get the animal's conception efficiency value."""
        return cast(int, self._conceptionEfficiency)

    @conceptionEfficiency.setter
    def conceptionEfficiency(self, value: int) -> None:
        """Set the animal's conception efficiency value.

        Args:
            value: The conception efficiency value to set
        """
        if self._conceptionEfficiency != value:
            self._conceptionEfficiency = value
            self._conceptionEfficiencyChanged.emit(value)

    @pyqtProperty(int, notify=_femalesPerMaleChanged)
    def femalesPerMale(self) -> int: # type: ignore
        """Get the animal's females to males ratio."""
        return cast(int, self._femalesToMales)

    @femalesPerMale.setter
    def femalesPerMale(self, value: int) -> None:
        """Set the animal's females to males ratio.

        Args:
            value: The females to males ratio to set
        """
        if self._femalesToMales != value:
            self._femalesToMales = value
            self._femalesPerMaleChanged.emit(value)

    @pyqtProperty(int, notify=_adultWeightChanged)
    def adultWeight(self) -> int: # type: ignore
        """Get the animal's adult weight."""
        return cast(int, self.mAdultWeight)

    @adultWeight.setter
    def adultWeight(self, value: int) -> None:
        """Set the animal's adult weight.

        Args:
            value: The adult weight to set
        """
        if self.mAdultWeight != value:
            self.mAdultWeight = value
            self._adultWeightChanged.emit(value)

    @pyqtProperty(int, notify=_youngPerBirthChanged)
    def youngPerBirth(self) -> int: # type: ignore
        """Get the animal's young per birth value."""
        return cast(int, self._youngPerBirth)

    @youngPerBirth.setter
    def youngPerBirth(self, value: int) -> None:
        """Set the animal's young per birth value.

        Args:
            value: The young per birth value to set
        """
        if self._youngPerBirth != value:
            self._youngPerBirth = value
            self._youngPerBirthChanged.emit(value)

    @pyqtProperty(int, notify=_weaningAgeChanged)
    def weaningAge(self) -> int: # type: ignore
        """Get the animal's weaning age."""
        return cast(int, self._weaningAge)

    @weaningAge.setter
    def weaningAge(self, value: int) -> None:
        """Set the animal's weaning age.

        Args:
            value: The weaning age to set
        """
        if self._weaningAge != value:
            self._weaningAge = value
            self._weaningAgeChanged.emit(value)

    @pyqtProperty(int, notify=_weaningWeightChanged)
    def weaningWeight(self) -> int: # type: ignore
        """Get the animal's weaning weight."""
        return cast(int, self._weaningWeight)

    @weaningWeight.setter
    def weaningWeight(self, value: int) -> None:
        """Set the animal's weaning weight.

        Args:
            value: The weaning weight to set
        """
        if self._weaningWeight != value:
            self._weaningWeight = value
            self._weaningWeightChanged.emit(value)

    @pyqtProperty(int, notify=_gestationTimeChanged)
    def gestationTime(self) -> int: # type: ignore
        """Get the animal's gestation time."""
        return cast(int, self._gestationTime)

    @gestationTime.setter
    def gestationTime(self, value: int) -> None:
        """Set the animal's gestation time.

        Args:
            value: The gestation time to set
        """
        if self._gestationTime != value:
            self._gestationTime = value
            self._gestationTimeChanged.emit(value)

    @pyqtProperty(int, notify=_estrousCycleChanged)
    def estrousCycle(self) -> int: # type: ignore
        """Get the animal's estrous cycle."""
        return cast(int, self._estrousCycle)

    @estrousCycle.setter
    def estrousCycle(self, value: int) -> None:
        """Set the animal's estrous cycle.

        Args:
            value: The estrous cycle to set
        """
        if self._estrousCycle != value:
            self._estrousCycle = value
            self._estrousCycleChanged.emit(value)

    @pyqtProperty(int, notify=_lactationTimeChanged)
    def lactationTime(self) -> int: # type: ignore
        """Get the animal's lactation time."""
        return cast(int, self._lactationTime)

    @lactationTime.setter
    def lactationTime(self, value: int) -> None:
        """Set the animal's lactation time.

        Args:
            value: The lactation time to set
        """
        if self._lactationTime != value:
            self._lactationTime = value
            self._lactationTimeChanged.emit(value)

    @pyqtProperty(bool, notify=_milkChanged)
    def milk(self) -> bool: # type: ignore
        """Get the animal's milk value."""
        return cast(bool, self._milk)

    @milk.setter
    def milk(self, value: bool) -> None:
        """Set the animal's milk value.

        Args:
            value: The milk value to set
        """
        if self._milk != value:
            self._milk = value
            self._milkChanged.emit(value)

    @pyqtProperty(int, notify=_milkGramsPerDayChanged)
    def milkGramsPerDay(self) -> int: # type: ignore
        """Get the animal's milk grams per day value."""
        return cast(int, self._milkGramsPerDay)

    @milkGramsPerDay.setter
    def milkGramsPerDay(self, value: int) -> None:
        """Set the animal's milk grams per day value.

        Args:
            value: The milk grams per day value to set
        """
        if self._milkGramsPerDay != value:
            self._milkGramsPerDay = value
            self._milkGramsPerDayChanged.emit(value)

    @pyqtProperty(int, notify=_milkFoodValueChanged)
    def milkFoodValue(self) -> int: # type: ignore
        """Get the animal's milk food value."""
        return cast(int, self._milkFoodValue)

    @milkFoodValue.setter
    def milkFoodValue(self, value: int) -> None:
        """Set the animal's milk food value.

        Args:
            value: The milk food value to set
        """
        if self._milkFoodValue != value:
            self._milkFoodValue = value
            self._milkFoodValueChanged.emit(value)

    @pyqtProperty(bool, notify=_fleeceChanged)
    def fleece(self) -> bool: # type: ignore
        """Get the animal's fleece value."""
        return cast(bool, self._fleece)

    @fleece.setter
    def fleece(self, value: bool) -> None:
        """Set the animal's fleece value.

        Args:
            value: The fleece value to set
        """
        if self._fleece != value:
            self._fleece = value
            self._fleeceChanged.emit(value)

    @pyqtProperty(int, notify=_fleeceWeightKgChanged)
    def fleeceWeightKg(self) -> int: # type: ignore
        """Get the animal's fleece weight value."""
        return cast(int, self._fleeceWeightKg)

    @fleeceWeightKg.setter
    def fleeceWeightKg(self, value: int) -> None:
        """Set the animal's fleece weight value.

        Args:
            value: The fleece weight value to set
        """
        if self._fleeceWeightKg != value:
            self._fleeceWeightKg = value
            self._fleeceWeightKgChanged.emit(value)

    @pyqtProperty(str, notify=_imageFileChanged)
    def imageFile(self) -> str: # type: ignore
        """Get the animal's image file path."""
        return cast(str, self.mImageFile)

    @imageFile.setter
    def imageFile(self, value: str) -> None:
        """Set the animal's image file path.

        Args:
            value: The image file path to set
        """
        if self.mImageFile != value:
            self.mImageFile = value
            self._imageFileChanged.emit(value)

    def fromXml(self, theXml: str) -> bool:
        """Load animal data from XML string.
        Args:
            theXml: XML string containing animal data
        Returns:
            True if loaded successfully, False otherwise
        """
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues

        try:
            LaUtils.debug.log(f"Loading animal XML: first 100 chars: {theXml[:100]}")

            myDocument = QDomDocument()
            if not myDocument.setContent(theXml):
                LaUtils.debug.log("Invalid XML content")
                # Mimic C++ behavior: continue processing even if content is invalid,
                # relying on subsequent checks for null elements.

            myTopElement = myDocument.firstChildElement("animal")
            if myTopElement.isNull():
                LaUtils.debug.log("Warning: Missing top-level 'animal' element")
                # Mimic C++ behavior: don't raise an error immediately

            # Set GUID from attribute
            self.guid = myTopElement.attribute("guid") # guid setter handles None
            LaUtils.debug.log(f"Loading animal with GUID in laanimal.py: {self.guid}")


            # Basic info - try both 'name' and 'n' tags for compatibility
            # Mimic C++: get text (empty if null), then decode
            name_element = myTopElement.firstChildElement("name")
            if name_element.isNull():
                name_element = myTopElement.firstChildElement("n") # Fallback
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text()) # Handles null element returning empty text
            self.mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
            LaUtils.debug.log(f"Loaded animal name: {self.mName}")

            # Meat production
            self.mMeatFoodValue = int(myTopElement.firstChildElement("meatFoodValue").text())
            self.mUsableMeat = int(myTopElement.firstChildElement("usableMeat").text())
            self.mKillWeight = int(myTopElement.firstChildElement("killWeight").text())
            self.mAdultWeight = int(myTopElement.firstChildElement("adultWeight").text())
            self.mGrowTime = int(myTopElement.firstChildElement("growTime").text())
            self.mDeathRate = int(myTopElement.firstChildElement("deathRate").text())

            # Reproduction
            self._conceptionEfficiency = int(myTopElement.firstChildElement("conceptionEfficiency").text())
            self._femalesToMales = int(myTopElement.firstChildElement("femalesToMales").text())
            self._sexualMaturity = int(myTopElement.firstChildElement("sexualMaturity").text())
            self._breedingExpectancy = int(myTopElement.firstChildElement("breedingExpectancy").text())
            self._youngPerBirth = int(myTopElement.firstChildElement("youngPerBirth").text())
            self._gestationTime = int(myTopElement.firstChildElement("gestationTime").text())
            self._estrousCycle = int(myTopElement.firstChildElement("estrousCycle").text())

            # Early life
            self._weaningAge = int(myTopElement.firstChildElement("weaningAge").text())
            self._weaningWeight = int(myTopElement.firstChildElement("weaningWeight").text())

            # Energy requirements type
            myFeedEnergyType = myTopElement.firstChildElement("feedEnergyType").text()
            # Default to KCalories if not TDN or element missing/empty
            self._feedEnergyType = LaEnergyType.TDN if myFeedEnergyType == "TDN" else LaEnergyType.KCalories

            # Energy requirements
            self._gestating = int(myTopElement.firstChildElement("gestating").text())
            self._lactating = int(myTopElement.firstChildElement("lactating").text())
            self._maintenance = int(myTopElement.firstChildElement("maintenance").text())
            self._juvenile = int(myTopElement.firstChildElement("juvenile").text())

            # Dairy
            milk_text = myTopElement.firstChildElement("milk").text().lower()
            self._milk = milk_text == "true"
            self._milkGramsPerDay = int(myTopElement.firstChildElement("milkGramsPerDay").text())
            self._milkFoodValue = int(myTopElement.firstChildElement("milkFoodValue").text())
            self._lactationTime = int(myTopElement.firstChildElement("lactationTime").text())

            # Fiber
            fleece_text = myTopElement.firstChildElement("fleece").text().lower()
            self._fleece = fleece_text == "true"
            self._fleeceWeightKg = float(myTopElement.firstChildElement("fleeceWeightKg").text())

            # Image - Store the full image path correctly
            image_file_text = LaUtils.xmlDecode(myTopElement.firstChildElement("imageFile").text())
            # Check if the path exists directly
            if image_file_text and os.path.exists(image_file_text):
                self.mImageFile = image_file_text
            else:
                # Try to find the file in the images directory
                images_dir = LaUtils.userImagesDirPath()
                basename = os.path.basename(image_file_text) if image_file_text else ""
                possible_path = os.path.join(images_dir, basename) if basename else ""
                if basename and os.path.exists(possible_path):
                    self.mImageFile = possible_path
                else:
                    # Just store the filename, resolution will be handled on display
                    self.mImageFile = basename
            
            LaUtils.debug.log(f"Set animal image file to: {self.mImageFile}")


            LaUtils.debug.log(f"Successfully processed XML for animal: {self.mName}")
            return True # Mimic C++ return true even if some elements were missing/invalid

        except Exception as e:
            LaUtils.debug.log(f"Critical error loading animal from XML: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())
            return False # Return False on major exceptions

    def toXml(self) -> str:
        """Generate XML representation consistent with C++ version."""
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues

        myString = f'<animal guid="{self.guid}">\n'
        # Use 'name' tag for consistency with C++ output and fromXml reading
        myString += f'  <name>{LaUtils.xmlEncode(str(self.mName))}</name>\n'
        myString += f'  <description>{LaUtils.xmlEncode(str(self.mDescription))}</description>\n'
        myString += f'  <meatFoodValue>{self.mMeatFoodValue}</meatFoodValue>\n'
        myString += f'  <usableMeat>{self.mUsableMeat}</usableMeat>\n'
        myString += f'  <killWeight>{self.mKillWeight}</killWeight>\n'
        myString += f'  <adultWeight>{self.mAdultWeight}</adultWeight>\n'
        myString += f'  <conceptionEfficiency>{self._conceptionEfficiency}</conceptionEfficiency>\n'
        myString += f'  <femalesToMales>{self._femalesToMales}</femalesToMales>\n'
        myString += f'  <growTime>{self.mGrowTime}</growTime>\n'
        myString += f'  <deathRate>{self.mDeathRate}</deathRate>\n' # Ensure deathRate is present
        if self._feedEnergyType == LaEnergyType.KCalories:
            myString += '  <feedEnergyType>KCalories</feedEnergyType>\n'
        elif self._feedEnergyType == LaEnergyType.TDN:
            myString += '  <feedEnergyType>TDN</feedEnergyType>\n'
        myString += f'  <gestating>{self._gestating}</gestating>\n'
        myString += f'  <lactating>{self._lactating}</lactating>\n'
        myString += f'  <maintenance>{self._maintenance}</maintenance>\n'
        myString += f'  <juvenile>{self._juvenile}</juvenile>\n'
        myString += f'  <sexualMaturity>{self._sexualMaturity}</sexualMaturity>\n'
        myString += f'  <breedingExpectancy>{self._breedingExpectancy}</breedingExpectancy>\n' # Ensure not duplicated
        myString += f'  <youngPerBirth>{self._youngPerBirth}</youngPerBirth>\n'
        myString += f'  <weaningAge>{self._weaningAge}</weaningAge>\n'
        myString += f'  <weaningWeight>{self._weaningWeight}</weaningWeight>\n'
        myString += f'  <gestationTime>{self._gestationTime}</gestationTime>\n'
        myString += f'  <estrousCycle>{self._estrousCycle}</estrousCycle>\n'
        myString += f'  <lactationTime>{self._lactationTime}</lactationTime>\n'
        # Output booleans as 0/1 like C++ QString::number(bool)
        myString += f'  <milk>{"True" if self._milk else "False"}</milk>\n'
        myString += f'  <milkGramsPerDay>{self._milkGramsPerDay}</milkGramsPerDay>\n'
        myString += f'  <milkFoodValue>{self._milkFoodValue}</milkFoodValue>\n'
        myString += f'  <fleece>{"True" if self._fleece else "False"}</fleece>\n'
        # Outputting float for fleeceWeightKg as defined in Python property, read by fromXml
        # C++ version stores int, but Python uses float.
        myString += f'  <fleeceWeightKg>{self._fleeceWeightKg}</fleeceWeightKg>\n'
        myString += f'  <imageFile>{LaUtils.xmlEncode(str(self.mImageFile))}</imageFile>\n'
        myString += '</animal>\n'
        return myString

    def toText(self) -> str:
        """Generate plain text representation consistent with C++ version."""
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues
        # Use self.guid which is the property access
        myString: str = f'guid=>{self.guid}\n'
        myString += f'name=>{LaUtils.xmlEncode(str(cast(str, self.mName)))}\n'
        myString += f'description=>{LaUtils.xmlEncode(str(cast(str, self.mDescription)))}\n'
        myString += f'meatFoodValue=>{self.mMeatFoodValue}\n'
        myString += f'usableMeat=>{self.mUsableMeat}\n'
        myString += f'killWeight=>{self.mKillWeight}\n'
        myString += f'adultWeight=>{self.mAdultWeight}\n'
        myString += f'conceptionEfficiency=>{self._conceptionEfficiency}\n'
        myString += f'femalesToMales=>{self._femalesToMales}\n'
        myString += f'growTime=>{self.mGrowTime}\n'
        myString += f'deathRate=>{self.mDeathRate}\n'
        if self._feedEnergyType == LaEnergyType.KCalories:
            myString += 'feedEnergyType=>KCalories\n'
        elif self._feedEnergyType == LaEnergyType.TDN:
            myString += 'feedEnergyType=>TDN\n'
        myString += f'gestating=>{self._gestating}\n'
        myString += f'lactating=>{self._lactating}\n'
        myString += f'maintenance=>{self._maintenance}\n'
        myString += f'juvenile=>{self._juvenile}\n'
        myString += f'sexualMaturity=>{self._sexualMaturity}\n'
        myString += f'breedingExpectancy=>{self._breedingExpectancy}\n'
        myString += f'youngPerBirth=>{self._youngPerBirth}\n'
        myString += f'weaningAge=>{self._weaningAge}\n'
        myString += f'weaningWeight=>{self._weaningWeight}\n'
        myString += f'gestationTime=>{self._gestationTime}\n'
        myString += f'estrousCycle=>{self._estrousCycle}\n'
        myString += f'lactationTime=>{self._lactationTime}\n'
        # Output booleans as 0/1 like C++ QString::number(bool)
        myString += f'milk=>{1 if self._milk else 0}\n'
        myString += f'milkGramsPerDay=>{self._milkGramsPerDay}\n'
        myString += f'milkFoodValue=>{self._milkFoodValue}\n'
        myString += f'fleece=>{1 if self._fleece else 0}\n'
        myString += f'fleeceWeightKg=>{self._fleeceWeightKg}\n'
        # imageFile is not included in C++ toText, omitting here too for consistency
        return myString

    def toHtml(self) -> str:
        """Generate HTML table representation consistent with C++ version."""
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues
        myString = f'<h2>Details for {LaUtils.xmlEncode(str(cast(str, self.mName)))}</h2>'
        myString += '<table>'
        myString += f'<tr><td><b>Description:</b></td><td>{self.mDescription}</td></tr>'
        myString += f'<tr><td><b>Meat Food Value:</b></td><td>{self.mMeatFoodValue}</td></tr>'
        myString += f'<tr><td><b>Usable Meat (%):</b></td><td>{self.mUsableMeat}</td></tr>'
        myString += f'<tr><td><b>Sexual Maturity:</b></td><td>{self._sexualMaturity}</td></tr>'
        myString += f'<tr><td><b>Years Breedable:</b></td><td>{self._breedingExpectancy}</td></tr>'
        myString += f'<tr><td><b>Young Per Birth:</b></td><td>{self._youngPerBirth}</td></tr>'
        myString += f'<tr><td><b>Weaning Age:</b></td><td>{self._weaningAge}</td></tr>'
        myString += f'<tr><td><b>Weaning Weight:</b></td><td>{self._weaningWeight}</td></tr>'
        myString += f'<tr><td><b>Kill Weight (Kg):</b></td><td>{self.mKillWeight}</td></tr>'
        myString += f'<tr><td><b>Adult Weight (Kg):</b></td><td>{self.mAdultWeight}</td></tr>'
        myString += f'<tr><td><b>Conception Efficiency(Percent):</b></td><td>{self._conceptionEfficiency}</td></tr>'
        myString += f'<tr><td><b>Females to Males (Breeding):</b></td><td>{self._femalesToMales}</td></tr>'
        myString += f'<tr><td><b>Grow Time:</b></td><td>{self.mGrowTime}</td></tr>'
        myString += f'<tr><td><b>Death Rate (%):</b></td><td>{self.mDeathRate}</td></tr>'
        myString += f'<tr><td><b>Gestation Time:</b></td><td>{self._gestationTime}</td></tr>'
        myString += f'<tr><td><b>Estrous Cycle:</b></td><td>{self._estrousCycle}</td></tr>'
        myString += f'<tr><td><b>lactationTime:</b></td><td>{self._lactationTime}</td></tr>'
        # Output booleans as 0/1 like C++ QString::number(bool)
        myString += f'<tr><td><b>milk:</b></td><td>{1 if self._milk else 0}</td></tr>'
        myString += f'<tr><td><b>milkGramsPerDay:</b></td><td>{self._milkGramsPerDay}</td></tr>'
        myString += f'<tr><td><b>milkFoodValue:</b></td><td>{self._milkFoodValue}</td></tr>'
        myString += f'<tr><td><b>fleece:</b></td><td>{1 if self._fleece else 0}</td></tr>'
        myString += f'<tr><td><b>fleeceWeightKg:</b></td><td>{self._fleeceWeightKg}</td></tr>'
        # imageFile is not included in C++ toHtml, omitting here too for consistency
        # The C++ version has an empty <tr><td></td><td>, keeping it for now
        myString += '<tr><td></td><td>'
        myString += '<tr><td><FONT COLOR="#0063F7">Feed Requirements (pa)</FONT></td><td>'
        if self._feedEnergyType == LaEnergyType.KCalories:
            myString += '<tr><td><b>EnergyType:</b></td><td>KCalories</td></tr>'
        elif self._feedEnergyType == LaEnergyType.TDN:
            myString += '<tr><td><b>EnergyType:</b></td><td>TDN</td></tr>'
        myString += f'<tr><td><b>Gestating Female:</b></td><td>{self._gestating}</td></tr>'
        myString += f'<tr><td><b>Lactating Female:</b></td><td>{self._lactating}</td></tr>'
        myString += f'<tr><td><b>Adult Maintenance:</b></td><td>{self._maintenance}</td></tr>'
        myString += f'<tr><td><b>Juveniles:</b></td><td>{self._juvenile}</td></tr>'
        myString += '</table>'
        return myString
