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
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    meatFoodValueChanged = pyqtSignal(int)
    usableMeatChanged = pyqtSignal(int)
    killWeightChanged = pyqtSignal(int)
    growTimeChanged = pyqtSignal(int)
    deathRateChanged = pyqtSignal(int)
    feedEnergyTypeChanged = pyqtSignal(LaEnergyType)
    gestatingChanged = pyqtSignal(int)
    lactatingChanged = pyqtSignal(int)
    maintenanceChanged = pyqtSignal(int)
    juvenileChanged = pyqtSignal(int)
    sexualMaturityChanged = pyqtSignal(int)
    breedingExpectancyChanged = pyqtSignal(int)
    conceptionEfficiencyChanged = pyqtSignal(int)
    femalesToMalesChanged = pyqtSignal(int)
    adultWeightChanged = pyqtSignal(str)
    youngPerBirthChanged = pyqtSignal(int)
    weaningAgeChanged = pyqtSignal(int)
    weaningWeightChanged = pyqtSignal(int)
    gestationTimeChanged = pyqtSignal(int)
    estrousCycleChanged = pyqtSignal(int)
    lactationTimeChanged = pyqtSignal(int)
    milkChanged = pyqtSignal(bool)  # Changed from int to bool to match property type
    milkGramsPerDayChanged = pyqtSignal(int)
    milkFoodValueChanged = pyqtSignal(int)
    fleeceChanged = pyqtSignal(bool)  # Changed from int to bool to match property type
    fleeceWeightKgChanged = pyqtSignal(float)  # Changed to float for more precise measurements
    imageFileChanged = pyqtSignal(str)
    femalesPerMaleChanged = pyqtSignal(int)  # Changed from femalesToMalesChanged

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
        self._guid = LaGuid.setGuid(self, None)
        # Basic info
        self._name = "No Name Set"
        self._description = "Not Set"
        self._imageFile = ""

        # Meat production
        self._meatFoodValue = 3000  # Calories per kg
        self._usableMeat = 50  # Percent
        self._killWeight = 100  # kg
        self._adultWeight = 0  # kg
        self._growTime = 10  # weeks
        self._deathRate = 10  # percent

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
        self._guid = theAnimal.guid
        self._name = theAnimal.name
        self._description = theAnimal.description
        self._meatFoodValue = theAnimal.meatFoodValue
        self._usableMeat = theAnimal.usableMeat
        self._killWeight = theAnimal.killWeight
        self._growTime = theAnimal.growTime
        self._deathRate = theAnimal.deathRate
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
        self._adultWeight = theAnimal.adultWeight
        self._gestationTime = theAnimal.gestationTime
        self._estrousCycle = theAnimal.estrousCycle
        self._lactationTime = theAnimal.lactationTime
        self._milk = theAnimal.milk
        self._milkGramsPerDay = theAnimal.milkGramsPerDay
        self._milkFoodValue = theAnimal.milkFoodValue
        self._fleece = theAnimal.fleece
        self._fleeceWeightKg = theAnimal.fleeceWeightKg
        self._imageFile = theAnimal.imageFile

    def validate(self) -> Dict[str, str]:
        """Validate the animal's attributes.

        Performs comprehensive validation of all animal attributes to ensure they are within
        acceptable ranges and logically consistent.

        Returns:
            Dict[str, str]: Dictionary of field names and error messages for invalid fields
        """
        errors = {}

        # Basic info validation
        if not cast(str, self._name):
            errors['name'] = "Name is required"
        if not cast(str, self._description):
            errors['description'] = "Description is required"

        # Meat production validation
        if cast(int, self._meatFoodValue) <= 0:
            errors['meatFoodValue'] = "Meat food value must be positive"
        if cast(int, self._usableMeat) < 0 or cast(int, self._usableMeat) > 100:
            errors['usableMeat'] = "Usable meat must be between 0-100%"
        if cast(int, self._killWeight) <= 0:
            errors['killWeight'] = "Kill weight must be positive"
        if cast(int, self._growTime) <= 0:
            errors['growTime'] = "Grow time must be positive"
        if cast(int, self._deathRate) < 0 or cast(int, self._deathRate) > 100:
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
        if cast(int, self._killWeight) <= cast(int, self._weaningWeight):
            errors['killWeight'] = "Kill weight must be greater than weaning weight"
        if cast(int, self._adultWeight) <= cast(int, self._weaningWeight):
            errors['adultWeight'] = "Adult weight must be greater than weaning weight"
        if cast(int, self._weaningAge) >= cast(int, self._growTime):
            errors['weaningAge'] = "Weaning age must be less than grow time"

        return errors

    # Properties with type hints and docstrings
    @pyqtProperty(str, notify=nameChanged)
    def name(self) -> str: # type: ignore
        """Get the animal's common name."""
        return cast(str, self._name)

    @name.setter
    def name(self, value: str) -> None:
        """Set the animal's common name.

        Args:
            value: The name to set
        """
        if self._name != value:
            self._name = value
            self.nameChanged.emit(value)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: # type: ignore
        """Get the animal's description."""
        return cast(str, self._description)

    @description.setter
    def description(self, value: str) -> None:
        """Set the animal's description.

        Args:
            value: The description to set
        """
        if self._description != value:
            self._description = value
            self.descriptionChanged.emit(value)

    @pyqtProperty(int, notify=meatFoodValueChanged)
    def meatFoodValue(self) -> int: # type: ignore
        """Get the animal's meat food value."""
        return cast(int, self._meatFoodValue)

    @meatFoodValue.setter
    def meatFoodValue(self, value: int) -> None:
        """Set the animal's meat food value.

        Args:
            value: The meat food value to set
        """
        if self._meatFoodValue != value:
            self._meatFoodValue = value
            self.meatFoodValueChanged.emit(value)

    @pyqtProperty(int, notify=usableMeatChanged)
    def usableMeat(self) -> int: # type: ignore
        """Get the animal's usable meat percentage."""
        return cast(int, self._usableMeat)

    @usableMeat.setter
    def usableMeat(self, value: int) -> None:
        """Set the animal's usable meat percentage.

        Args:
            value: The usable meat percentage to set
        """
        if self._usableMeat != value:
            self._usableMeat = value
            self.usableMeatChanged.emit(value)

    @pyqtProperty(int, notify=killWeightChanged)
    def killWeight(self) -> int: # type: ignore
        """Get the animal's kill weight."""
        return cast(int, self._killWeight)

    @killWeight.setter
    def killWeight(self, value: int) -> None:
        """Set the animal's kill weight.

        Args:
            value: The kill weight to set
        """
        if self._killWeight != value:
            self._killWeight = value
            self.killWeightChanged.emit(value)

    @pyqtProperty(int, notify=growTimeChanged)
    def growTime(self) -> int: # type: ignore
        """Get the animal's grow time."""
        return cast(int, self._growTime)

    @growTime.setter
    def growTime(self, value: int) -> None:
        """Set the animal's grow time.

        Args:
            value: The grow time to set
        """
        if self._growTime != value:
            self._growTime = value
            self.growTimeChanged.emit(value)

    @pyqtProperty(int, notify=deathRateChanged)
    def deathRate(self) -> int: # type: ignore
        """Get the animal's death rate."""
        return cast(int, self._deathRate)

    @deathRate.setter
    def deathRate(self, value: int) -> None:
        """Set the animal's death rate.

        Args:
            value: The death rate to set
        """
        if self._deathRate != value:
            self._deathRate = value
            self.deathRateChanged.emit(value)

    @pyqtProperty(LaEnergyType, notify=feedEnergyTypeChanged)
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
            self.feedEnergyTypeChanged.emit(theFeedEnergyType)

    @pyqtProperty(int, notify=gestatingChanged)
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
            self.gestatingChanged.emit(value)

    @pyqtProperty(int, notify=lactatingChanged)
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
            self.lactatingChanged.emit(value)

    @pyqtProperty(int, notify=maintenanceChanged)
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
            self.maintenanceChanged.emit(value)

    @pyqtProperty(int, notify=juvenileChanged)
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
            self.juvenileChanged.emit(value)

    @pyqtProperty(int, notify=sexualMaturityChanged)
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
            self.sexualMaturityChanged.emit(value)

    @pyqtProperty(int, notify=breedingExpectancyChanged)
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
            self.breedingExpectancyChanged.emit(value)

    @pyqtProperty(int, notify=conceptionEfficiencyChanged)
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
            self.conceptionEfficiencyChanged.emit(value)

    @pyqtProperty(int, notify=femalesPerMaleChanged)
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
            self.femalesPerMaleChanged.emit(value)

    @pyqtProperty(str, notify=adultWeightChanged)
    def adultWeight(self) -> str: # type: ignore
        """Get the animal's adult weight."""
        return cast(str, self._adultWeight)

    @adultWeight.setter
    def adultWeight(self, value: str) -> None:
        """Set the animal's adult weight.

        Args:
            value: The adult weight to set
        """
        if self._adultWeight != value:
            self._adultWeight = value
            self.adultWeightChanged.emit(value)

    @pyqtProperty(int, notify=youngPerBirthChanged)
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
            self.youngPerBirthChanged.emit(value)

    @pyqtProperty(int, notify=weaningAgeChanged)
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
            self.weaningAgeChanged.emit(value)

    @pyqtProperty(int, notify=weaningWeightChanged)
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
            self.weaningWeightChanged.emit(value)

    @pyqtProperty(int, notify=gestationTimeChanged)
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
            self.gestationTimeChanged.emit(value)

    @pyqtProperty(int, notify=estrousCycleChanged)
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
            self.estrousCycleChanged.emit(value)

    @pyqtProperty(int, notify=lactationTimeChanged)
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
            self.lactationTimeChanged.emit(value)

    @pyqtProperty(bool, notify=milkChanged)
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
            self.milkChanged.emit(value)

    @pyqtProperty(int, notify=milkGramsPerDayChanged)
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
            self.milkGramsPerDayChanged.emit(value)

    @pyqtProperty(int, notify=milkFoodValueChanged)
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
            self.milkFoodValueChanged.emit(value)

    @pyqtProperty(bool, notify=fleeceChanged)
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
            self.fleeceChanged.emit(value)

    @pyqtProperty(float, notify=fleeceWeightKgChanged)
    def fleeceWeightKg(self) -> float: # type: ignore
        """Get the animal's fleece weight value."""
        return cast(float, self._fleeceWeightKg)

    @fleeceWeightKg.setter
    def fleeceWeightKg(self, value: float) -> None:
        """Set the animal's fleece weight value.

        Args:
            value: The fleece weight value to set
        """
        if self._fleeceWeightKg != value:
            self._fleeceWeightKg = value
            self.fleeceWeightKgChanged.emit(value)

    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self) -> str: # type: ignore
        """Get the animal's image file path."""
        return cast(str, self._imageFile)

    @imageFile.setter
    def imageFile(self, value: str) -> None:
        """Set the animal's image file path.

        Args:
            value: The image file path to set
        """
        if self._imageFile != value:
            self._imageFile = value
            self.imageFileChanged.emit(value)

    def fromXml(self, theXml: str) -> bool:
        """Load animal data from XML string.

        Args:
            theXml: XML string containing animal data

        Returns:
            True if loaded successfully, False otherwise

        Raises:
            ValueError: If required elements are missing or invalid
        """
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues

        try:
            LaUtils.debug.log(f"Loading animal XML: first 100 chars: {theXml[:100]}")

            myDocument = QDomDocument()
            if not myDocument.setContent(theXml):
                LaUtils.debug.log("Invalid XML content")
                raise ValueError("Invalid XML content")

            myTopElement = myDocument.firstChildElement("animal")
            if myTopElement.isNull():
                LaUtils.debug.log("Missing animal element")
                raise ValueError("Missing animal element")

            # Set GUID from attribute
            self.setGuid(myTopElement.attribute("guid"))
            LaUtils.debug.log(f"Loading animal with GUID: {self.guid}")

            # Helper function to safely get integer values
            def getIntValue(elementName: str, default: int = 0) -> int:
                element = myTopElement.firstChildElement(elementName)
                if element.isNull():
                    return default
                text = element.text()
                try:
                    return int(text)
                except (ValueError, TypeError):
                    return default

            # Helper function to get text from an element with a fallback element name
            def getElementText(primaryName: str, fallbackName: str = "", defaultValue: str = "") -> str:
                element = myTopElement.firstChildElement(primaryName)
                if element.isNull() and fallbackName:
                    element = myTopElement.firstChildElement(fallbackName)
                if element.isNull():
                    return defaultValue
                return element.text()

            # Basic info - try both 'name' and 'n' tags for compatibility
            self._name = LaUtils.xmlDecode(getElementText("name", "n", "No Name Set"))
            self._description = LaUtils.xmlDecode(getElementText("description", "", "No Description Set"))
            LaUtils.debug.log(f"Loaded animal name: {self._name}")

            # Meat production
            self._meatFoodValue = getIntValue("meatFoodValue", 3000)
            self._usableMeat = getIntValue("usableMeat", 50)
            self._killWeight = getIntValue("killWeight", 100)
            self._adultWeight = getIntValue("adultWeight", 0)
            self._growTime = getIntValue("growTime", 10)
            self._deathRate = getIntValue("deathRate", 10)

            # Reproduction
            self._conceptionEfficiency = getIntValue("conceptionEfficiency", 0)
            self._femalesToMales = getIntValue("femalesToMales", 0)
            self._sexualMaturity = getIntValue("sexualMaturity", 18)
            self._breedingExpectancy = getIntValue("breedingExpectancy", 5)
            self._youngPerBirth = getIntValue("youngPerBirth", 1)
            self._gestationTime = getIntValue("gestationTime", 120)
            self._estrousCycle = getIntValue("estrousCycle", 21)

            # Early life
            self._weaningAge = getIntValue("weaningAge", 12)
            self._weaningWeight = getIntValue("weaningWeight", 30)

            # Energy requirements type
            myFeedEnergyType = myTopElement.firstChildElement("feedEnergyType").text()
            self._feedEnergyType = LaEnergyType.TDN if myFeedEnergyType == "TDN" else LaEnergyType.KCalories

            # Energy requirements
            self._gestating = getIntValue("gestating", 0)
            self._lactating = getIntValue("lactating", 0)
            self._maintenance = getIntValue("maintenance", 0)
            self._juvenile = getIntValue("juvenile", 0)

            # Dairy
            self._milk = bool(getIntValue("milk", 0))
            self._milkGramsPerDay = getIntValue("milkGramsPerDay", 0)
            self._milkFoodValue = getIntValue("milkFoodValue", 0)
            self._lactationTime = getIntValue("lactationTime", 0)

            # Fiber
            self._fleece = bool(getIntValue("fleece", 0))
            self._fleeceWeightKg = getIntValue("fleeceWeightKg", 0)

            # Image
            imageElement = myTopElement.firstChildElement("imageFile")
            if not imageElement.isNull():
                self._imageFile = LaUtils.xmlDecode(imageElement.text())
            else:
                # Set default image file based on animal name
                defaultImage = str(self._name).lower() + ".png"
                self._imageFile = defaultImage
                LaUtils.debug.log(f"No image file specified, using default: {defaultImage}", "UI")

            LaUtils.debug.log(f"Successfully loaded animal: {self._name}")
            return True

        except Exception as e:
            LaUtils.debug.log(f"Error loading animal from XML: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())
            return False

    def toXml(self) -> str:
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues

        """Generate XML representation of animal data."""
        myString = f'<animal guid="{self.guid}">\n'
        myString += f'  <name>{LaUtils.xmlEncode(str(cast(str, self._name)))}</name>\n'
        myString += f'  <description>{LaUtils.xmlEncode(str(cast(str, self._description)))}</description>\n'
        myString += f'  <meatFoodValue>{self._meatFoodValue}</meatFoodValue>\n'
        myString += f'  <usableMeat>{self._usableMeat}</usableMeat>\n'
        myString += f'  <killWeight>{self._killWeight}</killWeight>\n'
        myString += f'  <adultWeight>{self._adultWeight}</adultWeight>\n'
        myString += f'  <breedingExpectancy>{self._breedingExpectancy}</breedingExpectancy>\n'
        myString += f'  <conceptionEfficiency>{self._conceptionEfficiency}</conceptionEfficiency>\n'
        myString += f'  <femalesToMales>{self._femalesToMales}</femalesToMales>\n'
        myString += f'  <growTime>{self._growTime}</growTime>\n'
        if self._feedEnergyType == LaEnergyType.KCalories:
            myString += '  <feedEnergyType>KCalories</feedEnergyType>\n'
        elif self._feedEnergyType == LaEnergyType.TDN:
            myString += '  <feedEnergyType>TDN</feedEnergyType>\n'
        myString += f'  <gestating>{self._gestating}</gestating>\n'
        myString += f'  <lactating>{self._lactating}</lactating>\n'
        myString += f'  <maintenance>{self._maintenance}</maintenance>\n'
        myString += f'  <juvenile>{self._juvenile}</juvenile>\n'
        myString += f'  <sexualMaturity>{self._sexualMaturity}</sexualMaturity>\n'
        myString += f'  <breedingExpectancy>{self._breedingExpectancy}</breedingExpectancy>\n'
        myString += f'  <youngPerBirth>{self._youngPerBirth}</youngPerBirth>\n'
        myString += f'  <weaningAge>{self._weaningAge}</weaningAge>\n'
        myString += f'  <weaningWeight>{self._weaningWeight}</weaningWeight>\n'
        myString += f'  <gestationTime>{self._gestationTime}</gestationTime>\n'
        myString += f'  <estrousCycle>{self._estrousCycle}</estrousCycle>\n'
        myString += f'  <lactationTime>{self._lactationTime}</lactationTime>\n'
        myString += f'  <milk>{bool(self._milk)}</milk>\n'
        myString += f'  <milkGramsPerDay>{self._milkGramsPerDay}</milkGramsPerDay>\n'
        myString += f'  <milkFoodValue>{self._milkFoodValue}</milkFoodValue>\n'
        myString += f'  <fleece>{bool(self._fleece)}</fleece>\n'
        myString += f'  <fleeceWeightKg>{self._fleeceWeightKg}</fleeceWeightKg>\n'
        myString += f'  <imageFile>{LaUtils.xmlEncode(str(self._imageFile))}</imageFile>\n'
        myString += '</animal>\n'
        return myString

    def toText(self) -> str:
        """Generate plain text representation of animal data.

        Returns:
            Text string with animal attributes in key=>value format
        """
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues
        myString: str = f'guid=>{self.guid()}\n'
        myString += f'name=>{LaUtils.xmlEncode(str(cast(str, self._name)))}\n'
        myString += f'description=>{LaUtils.xmlEncode(str(cast(str, self._description)))}\n'
        myString += f'meatFoodValue=>{self._meatFoodValue}\n'
        myString += f'usableMeat=>{self._usableMeat}\n'
        myString += f'killWeight=>{self._killWeight}\n'
        myString += f'adultWeight=>{self._adultWeight}\n'
        myString += f'conceptionEfficiency=>{self._conceptionEfficiency}\n'
        myString += f'femalesToMales=>{self._femalesToMales}\n'
        myString += f'growTime=>{self._growTime}\n'
        myString += f'deathRate=>{self._deathRate}\n'
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
        myString += f'milk=>{self._milk}\n'
        myString += f'milkGramsPerDay=>{self._milkGramsPerDay}\n'
        myString += f'milkFoodValue=>{self._milkFoodValue}\n'
        myString += f'fleece=>{self._fleece}\n'
        myString += f'fleeceWeightKg=>{self._fleeceWeightKg}\n'
        return myString

    def toHtml(self) -> str:
        """Generate HTML table representation of animal data.

        Returns:
            HTML string containing formatted animal attributes
        """
        from la.lib.lautils import LaUtils # we do this to avoid circular import issues
        myString = f'<h2>Details for {LaUtils.xmlEncode(str(cast(str, self._name)))}</h2>'
        myString += '<table>'
        myString += f'<tr><td><b>Description:</b></td><td>{self._description}</td></tr>'
        myString += f'<tr><td><b>Meat Food Value:</b></td><td>{self._meatFoodValue}</td></tr>'
        myString += f'<tr><td><b>Usable Meat (%):</b></td><td>{self._usableMeat}</td></tr>'
        myString += f'<tr><td><b>Sexual Maturity:</b></td><td>{self._sexualMaturity}</td></tr>'
        myString += f'<tr><td><b>Years Breedable:</b></td><td>{self._breedingExpectancy}</td></tr>'
        myString += f'<tr><td><b>Young Per Birth:</b></td><td>{self._youngPerBirth}</td></tr>'
        myString += f'<tr><td><b>Weaning Age:</b></td><td>{self._weaningAge}</td></tr>'
        myString += f'<tr><td><b>Weaning Weight:</b></td><td>{self._weaningWeight}</td></tr>'
        myString += f'<tr><td><b>Kill Weight (Kg):</b></td><td>{self._killWeight}</td></tr>'
        myString += f'<tr><td><b>Adult Weight (Kg):</b></td><td>{self._adultWeight}</td></tr>'
        myString += f'<tr><td><b>Conception Efficiency(Percent):</b></td><td>{self._conceptionEfficiency}</td></tr>'
        myString += f'<tr><td><b>Females to Males (Breeding):</b></td><td>{self._femalesToMales}</td></tr>'
        myString += f'<tr><td><b>Grow Time:</b></td><td>{self._growTime}</td></tr>'
        myString += f'<tr><td><b>Death Rate (%):</b></td><td>{self._deathRate}</td></tr>'
        myString += f'<tr><td><b>Gestation Time:</b></td><td>{self._gestationTime}</td></tr>'
        myString += f'<tr><td><b>Estrous Cycle:</b></td><td>{self._estrousCycle}</td></tr>'
        myString += f'<tr><td><b>lactationTime:</b></td><td>{self._lactationTime}</td></tr>'
        myString += f'<tr><td><b>milk:</b></td><td>{self._milk}</td></tr>'
        myString += f'<tr><td><b>milkGramsPerDay:</b></td><td>{self._milkGramsPerDay}</td></tr>'
        myString += f'<tr><td><b>milkFoodValue:</b></td><td>{self._milkFoodValue}</td></tr>'
        myString += f'<tr><td><b>fleece:</b></td><td>{self._fleece}</td></tr>'
        myString += f'<tr><td><b>fleeceWeightKg:</b></td><td>{self._fleeceWeightKg}</td></tr>'
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
