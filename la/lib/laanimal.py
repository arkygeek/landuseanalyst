# laanimal.py

from typing import Optional, Type
import warnings

from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.lautils import  LaUtils, xmlEncode, xmlDecode # moved to method to avoid circular import
from la.lib.la import EnergyType

class LaAnimal(QObject, LaSerialisable, LaGuid):
    """ This class defines an LaAnimal object (an animal)

    Properties:
        name: the name of the animal
        description: the description of the animal
        meatFoodValue: the meat food value of the animal
        usableMeat: the usable meat of the animal
        killWeight: the kill weight of the animal
        growTime: the grow time of the animal
        deathRate: the death rate of the animal
        sexualMaturity: the sexual maturity of the animal
        breedingExpectancy: the breeding expectancy of the animal
        youngPerBirth: the young per birth of the animal
        weaningAge: the weaning age of the animal
        weaningWeight: the weaning weight of the animal
        gestationTime: the gestation time of the animal
        estrousCycle: the estrous cycle of the animal

    Methods:
        setName: sets the name of the animal
        setDescription: sets the description of the animal
        setMeatFoodValue: sets the meat food value of the animal
        setUsableMeat: sets the usable meat of the animal
        setSlaughterWeight: sets the kill weight of the animal

    Decorators:
        @pyqtProperty: defines a property
        @pyqtSignal: defines a signal
        @pyqtSlot: defines a slot
    """

     # Correct signal definitions
    nameChanged: pyqtSignal = pyqtSignal(str)
    descriptionChanged: pyqtSignal = pyqtSignal(str)
    meatFoodValueChanged: pyqtSignal = pyqtSignal(int)
    usableMeatChanged: pyqtSignal = pyqtSignal(int)
    killWeightChanged: pyqtSignal = pyqtSignal(int)
    growTimeChanged: pyqtSignal = pyqtSignal(int)
    deathRateChanged: pyqtSignal = pyqtSignal(int)
    feedEnergyTypeChanged: pyqtSignal = pyqtSignal(str)
    gestatingChanged: pyqtSignal = pyqtSignal(int)
    lactatingChanged: pyqtSignal = pyqtSignal(int)
    maintenanceChanged: pyqtSignal = pyqtSignal(int)
    juvenileChanged: pyqtSignal = pyqtSignal(int)
    sexualMaturityChanged: pyqtSignal = pyqtSignal(int)
    breedingExpectancyChanged: pyqtSignal = pyqtSignal(int)
    conceptionEfficiencyChanged: pyqtSignal = pyqtSignal(int)
    femalesToMalesChanged: pyqtSignal = pyqtSignal(int)
    adultWeightChanged: pyqtSignal = pyqtSignal(int)
    youngPerBirthChanged: pyqtSignal = pyqtSignal(int)
    weaningAgeChanged: pyqtSignal = pyqtSignal(int)
    weaningWeightChanged: pyqtSignal = pyqtSignal(int)
    gestationTimeChanged: pyqtSignal = pyqtSignal(int)
    estrousCycleChanged: pyqtSignal = pyqtSignal(int)
    lactationTimeChanged: pyqtSignal = pyqtSignal(int)
    milkChanged: pyqtSignal = pyqtSignal(int)
    milkGramsPerDayChanged: pyqtSignal = pyqtSignal(int)
    milkFoodValueChanged: pyqtSignal = pyqtSignal(int)
    fleeceChanged: pyqtSignal = pyqtSignal(int)
    fleeceWeightKgChanged: pyqtSignal = pyqtSignal(int)
    imageFileChanged: pyqtSignal = pyqtSignal(str)

    def __init__(self, theAnimal: Optional[Type['LaAnimal']] = None, parent=None):
        super().__init__(parent)
        if theAnimal is None:
            self._guid = LaGuid.setGuid(self, None)
            self._name = "No Name Set"
            self._description = "Not Set"
            self._meatFoodValue = 3000
            self._usableMeat = 50
            self._killWeight = 100
            self._growTime = 10
            self._deathRate = 10
            self._sexualMaturity = 18
            self._breedingExpectancy = 5
            self._adultWeight = ""
            self._youngPerBirth = 1
            self._weaningAge = 12
            self._weaningWeight = 30
            self._gestationTime = 120
            self._estrousCycle = 21
            self._feedEnergyType = ""
            self._gestating = ""
            self._lactating = ""
            self._maintenance = ""
            self._juvenile = ""
            self._conceptionEfficiency = ""
            self._femalesToMales = ""
            self._lactationTime = ""
            self._milk = ""
            self._milkGramsPerDay = ""
            self._milkFoodValue = ""
            self._fleece = ""
            self._fleeceWeightKg = ""
            self._imageFile = ""
        else:
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
            self._femalesToMales = theAnimal.femalesToMales
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

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        """ Gets or sets the name of the animal

        :return: The name of the animal as a string
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, theAnimalName):
        """ Sets the name of the animal and emits a signal when done

        :param theAnimalName: The new name for the animal
        :type theAnimalName: str
        """
        if self._name != theAnimalName:
            self._name = theAnimalName
            self.nameChanged.emit(theAnimalName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        """ Gets or sets the description of the animal

        :return: The description of the animal as a string
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """ Sets the description of the animal and emits a signal when done

        :param description: The new description for the animal
        :type description: str
        """
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(int, notify=meatFoodValueChanged)
    def meatFoodValue(self):
        """ Gets or sets the meat food value of the animal

        :return: The meat food value as an integer
        :rtype: int
        """
        return self._meatFoodValue

    @meatFoodValue.setter
    def meatFoodValue(self, meatFoodValue):
        """ Sets the meat food value of the animal and emits a signal when done

        :param meatFoodValue: The new meat food value for the animal
        :type meatFoodValue: int
        """
        if self._meatFoodValue != meatFoodValue:
            self._meatFoodValue = meatFoodValue
            self.meatFoodValueChanged.emit(meatFoodValue)

    @pyqtProperty(int, notify=usableMeatChanged)
    def usableMeat(self):
        """ Gets or sets the usable meat of the animal

        :return: The usable meat as an integer (in percent)
        :rtype: int
        """
        return self._usableMeat

    @usableMeat.setter
    def usableMeat(self, usableMeat):
        """ Sets the usable meat of the animal and emits a signal when done

        :param usableMeat: The new usable meat value for the animal (in percent)
        :type usableMeat: int
        """
        if self._usableMeat != usableMeat:
            self._usableMeat = usableMeat
            self.usableMeatChanged.emit(usableMeat)

    @pyqtProperty(int, notify=killWeightChanged)
    def killWeight(self):
        """ Gets or sets the kill weight of the animal

        :return: The kill weight as an integer (in kg)
        :rtype: int
        """
        return self._killWeight

    @killWeight.setter
    def killWeight(self, killWeight):
        """ Sets the kill weight of the animal and emits a signal when done

        :param killWeight: The new kill weight value for the animal (in kg)
        :type killWeight: int
        """
        if self._killWeight != killWeight:
            self._killWeight = killWeight
            self.killWeightChanged.emit(killWeight)

    @pyqtProperty(int, notify=growTimeChanged)
    def growTime(self):
        """ Gets or sets the grow time of the animal

        :return: The grow time as an integer (in years)
        :rtype: int
        """
        return self._growTime

    @growTime.setter
    def growTime(self, growTime):
        """ Sets the grow time of the animal and emits a signal when done

        :param growTime: The new grow time value for the animal (in years)
        :type growTime: int
        """
        if self._growTime != growTime:
            self._growTime = growTime
            self.growTimeChanged.emit(growTime)

    @pyqtProperty(int, notify=deathRateChanged)
    def deathRate(self):
        """ Gets or sets the death rate of the animal

        :return: The death rate as an integer (in percent)
        :rtype: int
        """
        return self._deathRate

    @deathRate.setter
    def deathRate(self, deathRate):
        """ Sets the death rate of the animal and emits a signal when done

        :param deathRate: The new death rate value for the animal (in percent)
        :type deathRate: int
        """
        if self._deathRate != deathRate:
            self._deathRate = deathRate
            self.deathRateChanged.emit(deathRate)

    @pyqtProperty(str, notify=feedEnergyTypeChanged)
    def feedEnergyType(self):
        """ Gets or sets the energy type for animal feed

        :return: The energy type as a string (KCalories or TDN)
        :rtype: str
        """
        return self._feedEnergyType

    @feedEnergyType.setter
    def feedEnergyType(self, feedEnergyType):
        """ Sets the energy type for animal feed and emits a signal when done

        :param feedEnergyType: The new energy type value for animal feed (KCalories or TDN)
        :type feedEnergyType: str
        """
        if self._feedEnergyType != feedEnergyType:
            self._feedEnergyType = feedEnergyType
            self.feedEnergyTypeChanged.emit(feedEnergyType)

    @pyqtProperty(int, notify=gestatingChanged)
    def gestating(self):
        """ Gets or sets the number of gestating females

        :return: The number of gestating females as an integer
        :rtype: int
        """
        return self._gestating

    @gestating.setter
    def gestating(self, gestating):
        """ Sets the number of gestating females and emits a signal when done

        :param gestating: The new number of gestating females for the animal
        :type gestating: int
        """
        if self._gestating != gestating:
            self._gestating = gestating
            self.gestatingChanged.emit(gestating)

    @pyqtProperty(int, notify=lactatingChanged)
    def lactating(self):
        """ Gets or sets the number of lactating females

        :return: The number of lactating females as an integer
        :rtype: int
        """
        return self._lactating

    @lactating.setter
    def lactating(self, lactating):
        """ Sets the number of lactating females and emits a signal when done

        :param lactating: The new number of lactating females for the animal
        :type lactating: int
        """
        if self._lactating != lactating:
            self._lactating = lactating
            self.lactatingChanged.emit(lactating)

    @pyqtProperty(int, notify=maintenanceChanged)
    def maintenance(self):
        """ Gets or sets the adult maintenance value

        :return: The adult maintenance value as an integer (in kg/day)
        :rtype: int
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """ Sets the adult maintenance value and emits a signal when done

        :param maintenance: The new adult maintenance value for the animal (in kg/day)
        :type maintenance: int
        """
        if self._maintenance != maintenance:
            self._maintenance = maintenance
            self.maintenanceChanged.emit(maintenance)

    @pyqtProperty(int, notify=juvenileChanged)
    def juvenile(self):
        """ Gets or sets the number of juveniles

        :return: The number of juveniles as an integer
        :rtype: int
        """
        return self._juvenile

    @juvenile.setter
    def juvenile(self, juvenile):
        """ Sets the number of juveniles and emits a signal when done

        :param juvenile: The new number of juveniles for the animal
        :type juvenile: int
        """
        if self._juvenile != juvenile:
            self._juvenile = juvenile
            self.juvenileChanged.emit(juvenile)

    @pyqtProperty(int, notify=sexualMaturityChanged)
    def sexualMaturity(self):
        """ Gets or sets the sexual maturity value

        :return: The sexual maturity value as an integer (in years)
        :rtype: int
        """
        return self._sexualMaturity

    @sexualMaturity.setter
    def sexualMaturity(self, sexualMaturity):
        """ Sets the sexual maturity value and emits a signal when done

        :param sexualMaturity: The new sexual maturity value for the animal (in years)
        :type sexualMaturity: int
        """
        if self._sexualMaturity != sexualMaturity:
            self._sexualMaturity = sexualMaturity
            self.sexualMaturityChanged.emit(sexualMaturity)

    @pyqtProperty(int, notify=breedingExpectancyChanged)
    def breedingExpectancy(self):
        """ Gets or sets the breeding expectancy value

        :return: The breeding expectancy value as an integer (in years)
        :rtype: int
        """
        return self._breedingExpectancy

    @breedingExpectancy.setter
    def breedingExpectancy(self, breedingExpectancy):
        """ Sets the breeding expectancy value and emits a signal when done

        :param breedingExpectancy: The new breeding expectancy value for the animal (in years)
        :type breedingExpectancy: int
        """
        if self._breedingExpectancy != breedingExpectancy:
            self._breedingExpectancy = breedingExpectancy
            self.breedingExpectancyChanged.emit(breedingExpectancy)

    @pyqtProperty(int, notify=conceptionEfficiencyChanged)
    def conceptionEfficiency(self):
        """ Gets or sets the conception efficiency value

        :return: The conception efficiency value as an integer (in percent)
        :rtype: int
        """
        return self._conceptionEfficiency

    @conceptionEfficiency.setter
    def conceptionEfficiency(self, conceptionEfficiency):
        """ Sets the conception efficiency value and emits a signal when done

        :param conceptionEfficiency: The new conception efficiency value for the animal (in percent)
        :type conceptionEfficiency: int
        """
        if self._conceptionEfficiency != conceptionEfficiency:
            self._conceptionEfficiency = conceptionEfficiency
            self.conceptionEfficiencyChanged.emit(conceptionEfficiency)

    @pyqtProperty(int, notify=femalesToMalesChanged)
    def femalesPerMale(self):
        """ Gets or sets the number of females to males for breeding

        :return: The number of females to males as an integer
        :rtype: int
        """
        return self._femalesToMales

    @femalesPerMale.setter
    def femalesPerMale(self, femalesPerMale):
        """ Sets the number of females to males for breeding and emits a signal when done

        :param femalesPerMale: The new number of females to males for the animal (for breeding)
        :type femalesPerMale: int
        """
        if self._femalesToMales != femalesPerMale:
            self._femalesToMales = femalesPerMale
            self.femalesPerMaleChanged.emit(femalesPerMale)

    @pyqtProperty(str, notify=adultWeightChanged)
    def adultWeight(self):
        """ Gets or sets the adult weight value

        :return: The adult weight as a string (in kg)
        :rtype: str
        """
        return self._adultWeight

    @adultWeight.setter
    def adultWeight(self, adultWeight):
        """ Sets the adult weight value and emits a signal when done

        :param adultWeight: The new adult weight value for the animal (in kg)
        :type adultWeight: str
        """
        if self._adultWeight != adultWeight:
            self._adultWeight = adultWeight
            self.adultWeightChanged.emit(adultWeight)

    @pyqtProperty(int, notify=youngPerBirthChanged)
    def youngPerBirth(self):
        """ Gets or sets the number of young per birth

        :return: The number of young per birth as an integer
        :rtype: int
        """
        return self._youngPerBirth

    @youngPerBirth.setter
    def youngPerBirth(self, youngPerBirth):
        """ Sets the number of young per birth and emits a signal when done

        :param youngPerBirth: The new number of young per birth for the animal
        :type youngPerBirth: int
        """
        if self._youngPerBirth != youngPerBirth:
            self._youngPerBirth = youngPerBirth
            self.youngPerBirthChanged.emit(youngPerBirth)

    @pyqtProperty(int, notify=weaningAgeChanged)
    def weaningAge(self):
        """ Gets or sets the weaning age value

        :return: The weaning age as an integer (in months)
        :rtype: int
        """
        return self._weaningAge

    @weaningAge.setter
    def weaningAge(self, weaningAge):
        """ Sets the weaning age value and emits a signal when done

        :param weaningAge: The new weaning age value for the animal (in months)
        :type weaningAge: int
        """
        if self._weaningAge != weaningAge:
            self._weaningAge = weaningAge
            self.weaningAgeChanged.emit(weaningAge)

    @pyqtProperty(int, notify=weaningWeightChanged)
    def weaningWeight(self):
        """ Gets or sets the weaning weight value

        :return: The weaning weight as an integer (in kg)
        :rtype: int
        """
        return self._weaningWeight

    @weaningWeight.setter
    def weaningWeight(self, weaningWeight):
        """ Sets the weaning weight value and emits a signal when done

        :param weaningWeight: The new weaning weight value for the animal (in kg)
        :type weaningWeight: int
        """
        if self._weaningWeight != weaningWeight:
            self._weaningWeight = weaningWeight
            self.weaningWeightChanged.emit(weaningWeight)

    @pyqtProperty(int, notify=gestationTimeChanged)
    def gestationTime(self):
        """ Gets or sets the gestation time value

        :return: The gestation time as an integer (in days)
        :rtype: int
        """
        return self._gestationTime

    @gestationTime.setter
    def gestationTime(self, gestationTime):
        """ Sets the gestation time value and emits a signal when done

        :param gestationTime: The new gestation time value for the animal (in days)
        :type gestationTime: int
        """
        if self._gestationTime != gestationTime:
            self._gestationTime = gestationTime
            self.gestationTimeChanged.emit(gestationTime)

    @pyqtProperty(int, notify=estrousCycleChanged)
    def estrousCycle(self):
        """ Gets or sets the estrous cycle value

        :return: The estrous cycle as an integer (in days)
        :rtype: int
        """
        return self._estrousCycle

    @estrousCycle.setter
    def estrousCycle(self, estrousCycle):
        """ Sets the estrous cycle value and emits a signal when done

        :param estrousCycle: The new estrous cycle value for the animal (in days)
        :type estrousCycle: int
        """
        if self._estrousCycle != estrousCycle:
            self._estrousCycle = estrousCycle
            self.estrousCycleChanged.emit(estrousCycle)

    @pyqtProperty(int, notify=lactationTimeChanged)
    def lactationTime(self):
        """ Gets or sets the lactation time value

        :return: The lactation time as an integer (in days)
        :rtype: int
        """
        return self._lactationTime

    @lactationTime.setter
    def lactationTime(self, lactationTime):
        """ Sets the lactation time value and emits a signal when done

        :param lactationTime: The new lactation time value for the animal (in days)
        :type lactationTime: int
        """
        if self._lactationTime != lactationTime:
            self._lactationTime = lactationTime
            self.lactationTimeChanged.emit(lactationTime)

    @pyqtProperty(int, notify=milkChanged)
    def milk(self):
        """ Gets or sets the milk value

        :return: The milk as an integer (in kg/day)
        :rtype: int
        """
        return self._milk

    @milk.setter
    def milk(self, milk):
        """ Sets the milk value and emits a signal when done

        :param milk: The new milk value for the animal (in kg/day)
        :type milk: int
        """
        if self._milk != milk:
            self._milk = milk
            self.milkChanged.emit(milk)

    @pyqtProperty(int, notify=milkGramsPerDayChanged)
    def milkGramsPerDay(self):
        """ Gets or sets the milk grams per day value

        :return: The milk grams per day as an integer (in g/day)
        :rtype: int
        """
        return self._milkGramsPerDay

    @milkGramsPerDay.setter
    def milkGramsPerDay(self, milkGramsPerDay):
        """ Sets the milk grams per day value and emits a signal when done

        :param milkGramsPerDay: The new milk grams per day value for the animal (in g/day)
        :type milkGramsPerDay: int
        """
        if self._milkGramsPerDay != milkGramsPerDay:
            self._milkGramsPerDay = milkGramsPerDay
            self.milkGramsPerDayChanged.emit(milkGramsPerDay)

    @pyqtProperty(int, notify=milkFoodValueChanged)
    def milkFoodValue(self):
        """ Gets or sets the milk food value

        :return: The milk food value as an integer (in kg/day)
        :rtype: int
        """
        return self._milkFoodValue

    @milkFoodValue.setter
    def milkFoodValue(self, milkFoodValue):
        """ Sets the milk food value and emits a signal when done

        :param milkFoodValue: The new milk food value for the animal (in kg/day)
        :type milkFoodValue: int
        """
        if self._milkFoodValue != milkFoodValue:
            self._milkFoodValue = milkFoodValue
            self.milkFoodValueChanged.emit(milkFoodValue)

    @pyqtProperty(int, notify=fleeceChanged)
    def fleece(self):
        """ Gets or sets the fleece value

        :return: The fleece as an integer (in kg/year)
        :rtype: int
        """
        return self._fleece

    @fleece.setter
    def fleece(self, fleece):
        """ Sets the fleece value and emits a signal when done

        :param fleece: The new fleece value for the animal (in kg/year)
        :type fleece: int
        """
        if self._fleece != fleece:
            self._fleece = fleece
            self.fleeceChanged.emit(fleece)

    @pyqtProperty(int, notify=fleeceWeightKgChanged)
    def fleeceWeightKg(self):
        """ Gets or sets the fleece weight value

        :return: The fleece weight as an integer (in kg/year)
        :rtype: int
        """
        return self._fleeceWeightKg

    @fleeceWeightKg.setter
    def fleeceWeightKg(self, fleeceWeightKg):
        """ Sets the fleece weight value and emits a signal when done

        :param fleeceWeightKg: The new fleece weight value for the animal (in kg/year)
        :type fleeceWeightKg: int
        """
        if self._fleeceWeightKg != fleeceWeightKg:
            self._fleeceWeightKg = fleeceWeightKg
            self.fleeceWeightKgChanged.emit(fleeceWeightKg)

    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self):
        """ Gets or sets the image file value

        :return: The image file as a string (e.g., 'animal.jpg')
        :rtype: str
        """
        return self._imageFile

    @imageFile.setter
    def imageFile(self, imageFile):
        """ Sets the image file value and emits a signal when done

        :param imageFile: The new image file for the animal (e.g., 'animal.jpg')
        :type imageFile: str
        """
        if self._imageFile != imageFile:
            self._imageFile = imageFile
            self.imageFileChanged.emit(imageFile)

    def fromXml(self, theXml: str) -> bool:
        """
        Parses an XML string and sets the properties of the animal object accordingly.

        :param theXml: The XML string to parse.
        :type theXml: str
        :return: True if the parsing was successful, False otherwise.
        :rtype: bool
        """
        # the following import is here to avoid a circular import
        from la.lib.lautils import LaUtils  # , xmlEncode, xmlDecode
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("animal")

        # gracefully handle the case where the top element is null
        if myTopElement.isNull():
            warnings.warn("Failed to parse XML: myTopElement is null. The XML \
                element could not be found or parsed.")
            return False

        self.setGuid(myTopElement.attribute("guid"))
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())

        def getIntValue(theElementName: str) -> int:
            myElementText: int = myTopElement.firstChildElement(theElementName).text()
            return int(myElementText) if myElementText else 0

        self.meatFoodValue = getIntValue("meatFoodValue")
        self.usableMeat = getIntValue("usableMeat")
        self.killWeight = getIntValue("killWeight")
        self.adultWeight = getIntValue("adultWeight")
        self.conceptionEfficiency = getIntValue("conceptionEfficiency")
        self.femalesToMales = getIntValue("femalesToMales")
        self.growTime = getIntValue("growTime")
        self.deathRate = getIntValue("deathRate")
        self.gestating = getIntValue("gestating")
        self.lactating = getIntValue("lactating")
        self.maintenance = getIntValue("maintenance")
        self.juvenile = getIntValue("juvenile")
        self.sexualMaturity = getIntValue("sexualMaturity")
        self.breedingExpectancy = getIntValue("breedingExpectancy")
        self.youngPerBirth = getIntValue("youngPerBirth")
        self.weaningAge = getIntValue("weaningAge")
        self.weaningWeight = getIntValue("weaningWeight")
        self.gestationTime = getIntValue("gestationTime")
        self.estrousCycle = getIntValue("estrousCycle")
        self.lactationTime = getIntValue("lactationTime")
        self.milk = getIntValue("milk")
        self.milkGramsPerDay = getIntValue("milkGramsPerDay")
        self.milkFoodValue = getIntValue("milkFoodValue")
        self.fleece = getIntValue("fleece")
        self.fleeceWeightKg = getIntValue("fleeceWeightKg")
        self.imageFile = LaUtils.xmlDecode(myTopElement.firstChildElement("imageFile").text())

        # the following is a hack to get around the fact that the feedEnergyType
        # property is an enum, and the enum values are not being saved to the
        # XML file
        myFeedEnergyType: str = myTopElement.firstChildElement("feedEnergyType").text()
        if myFeedEnergyType == "KCalories":
            self.mFeedEnergyType = "KCalories"
        elif myFeedEnergyType == "TDN":
            self.mFeedEnergyType = "TDN"

        return True


    def toXml(self) -> str:
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import
        myString = f'<animal guid="{self.guid}">\n'
        """ NOTE:
            The LaUtils.xmlEncode function is likely used here to escape special
             characters that have specific meanings in XML. This is done to ensure
             that the _name value can be safely included in an XML document without
             causing parsing errors.
             For example, chars like <, >, and & are used in XML tags and entities.
             If these characters appear in the _name value, they could cause the XML to be malformed.

             The xmlEncode function would replace these characters with their corresponding
            XML entities (&lt;, &gt;, and &amp; respectively).
        """
        myString += f'  <name>{LaUtils.xmlEncode(self._name)}</name>\n'
        myString += f'  <description>{LaUtils.xmlEncode(self._description)}</description>\n'
        myString += f'  <meatFoodValue>{self._meatFoodValue}</meatFoodValue>\n'
        myString += f'  <usableMeat>{self._usableMeat}</usableMeat>\n'
        myString += f'  <killWeight>{self._killWeight}</killWeight>\n'
        myString += f'  <adultWeight>{self._adultWeight}</adultWeight>\n'
        myString += f'  <conceptionEfficiency>{self._conceptionEfficiency}</conceptionEfficiency>\n'
        myString += f'  <femalesToMales>{self._femalesToMales}</femalesToMales>\n'
        myString += f'  <growTime>{self._growTime}</growTime>\n'
        myString += f'  <deathRate>{self._deathRate}</deathRate>\n'
        if self._feedEnergyType == EnergyType.KCalories:
            myString += '  <feedEnergyType>KCalories</feedEnergyType>\n'
        elif self._feedEnergyType == EnergyType.TDN:
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
        myString += f'  <milk>{self._milk}</milk>\n'
        myString += f'  <milkGramsPerDay>{self._milkGramsPerDay}</milkGramsPerDay>\n'
        myString += f'  <milkFoodValue>{self._milkFoodValue}</milkFoodValue>\n'
        myString += f'  <fleece>{self._fleece}</fleece>\n'
        myString += f'  <fleeceWeightKg>{self._fleeceWeightKg}</fleeceWeightKg>\n'
        myString += f'  <imageFile>{LaUtils.xmlEncode(self._imageFile)}</imageFile>\n'
        myString += '</animal>\n'
        return myString


    def toText(self) -> str:
        """
        Returns a string representation of the animal object.
        The string contains the following fields:
        - guid
        - name
        - description
        - meatFoodValue
        - usableMeat
        - killWeight
        - adultWeight
        - conceptionEfficiency
        - femalesToMales
        - growTime
        - deathRate
        - feedEnergyType
        - gestating
        - lactating
        - maintenance
        - juvenile
        - sexualMaturity
        - breedingExpectancy
        - youngPerBirth
        - weaningAge
        - weaningWeight
        - gestationTime
        - estrousCycle
        - lactationTime
        - milk
        - milkGramsPerDay
        - milkFoodValue
        - fleece
        - fleeceWeightKg
        """
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import
        myString: str = f'guid=>{self.guid()}\n'
        """ NOTE:
            The LaUtils.xmlEncode function is likely used here to escape special
             characters that have specific meanings in XML. This is done to ensure
             that the _name value can be safely included in an XML document without
             causing parsing errors.
             For example, chars like <, >, and & are used in XML tags/entities
             These characters could cause the XML to be malformed.

             The xmlEncode function replaces these characters with their corresponding
            XML entities (&lt;, &gt;, and &amp; respectively).
        """
        myString += f'name=>{LaUtils.xmlEncode(self._name)}\n'
        myString += f'description=>{LaUtils.xmlEncode(self._description)}\n'
        myString += f'meatFoodValue=>{self._meatFoodValue}\n'
        myString += f'usableMeat=>{self._usableMeat}\n'
        myString += f'killWeight=>{self._killWeight}\n'
        myString += f'adultWeight=>{self._adultWeight}\n'
        myString += f'conceptionEfficiency=>{self._conceptionEfficiency}\n'
        myString += f'femalesToMales=>{self._femalesToMales}\n'
        myString += f'growTime=>{self._growTime}\n'
        myString += f'deathRate=>{self._deathRate}\n'
        if self._feedEnergyType == EnergyType.KCalories:
            myString += 'feedEnergyType=>KCalories\n'
        elif self._feedEnergyType == EnergyType.TDN:
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
        """
        Returns an HTML string containing details of the animal object.

        The string contains the following fields:
        -
        """
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import
        myString = f'<h2>Details for {LaUtils.xmlEncode(self._name)}</h2>'
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
        if self._feedEnergyType == EnergyType.KCalories:
            myString += '<tr><td><b>EnergyType:</b></td><td>KCalories</td></tr>'
        elif self._feedEnergyType == EnergyType.TDN:
            myString += '<tr><td><b>EnergyType:</b></td><td>TDN</td></tr>'
        myString += f'<tr><td><b>Gestating Female:</b></td><td>{self._gestating}</td></tr>'
        myString += f'<tr><td><b>Lactating Female:</b></td><td>{self._lactating}</td></tr>'
        myString += f'<tr><td><b>Adult Maintenance:</b></td><td>{self._maintenance}</td></tr>'
        myString += f'<tr><td><b>Juveniles:</b></td><td>{self._juvenile}</td></tr>'
        myString += '</table>'
        return myString
