"""
/***************************************************************************
 LaAnimal
                                 A QGIS plugin
 Archaeological modelling
                             -------------------
        begin                : 2022-03-22
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Dr. Jason S. Jorgenson
        email                : jjorgenson@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify   *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or      *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/


This code defines a LaAnimal class in Python using PyQt5.

The class inherits from LaSerialisable and LaGuid, defined elsewhere.

The class has several properties, including name, description, meatFoodValue,
usableMeat, and killWeight, defined using the @pyqtProperty decorator.

The class also has several slots, including setName, setDescription,
setMeatFoodValue, setUsableMeat, and setSlaughterWeight, which are used to set
the values of the properties.

The class defines several PyQt signals, including:
    nameChanged, descriptionChanged, meatFoodValueChanged, usableMeatChanged,
    and killWeightChanged, which are emitted when the corresponding property changes.

The class has several methods, including
    __init__, __del__, __copy__, and __deepcopy__
"""

from typing import Optional, Type
import warnings
# laanimal.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.lautils import  LaUtils, xmlEncode, xmlDecode # moved to method to avoid circular import
from la.lib.la import EnergyType
# from qgis.PyQt.QtCore import pyqtProperty

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
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    meatFoodValueChanged = pyqtSignal(int)
    usableMeatChanged = pyqtSignal(int)
    killWeightChanged = pyqtSignal(int)
    growTimeChanged = pyqtSignal(int)
    deathRateChanged = pyqtSignal(int)
    feedEnergyTypeChanged = pyqtSignal(str)
    gestatingChanged = pyqtSignal(int)
    lactatingChanged = pyqtSignal(int)
    maintenanceChanged = pyqtSignal(int)
    juvenileChanged = pyqtSignal(int)
    sexualMaturityChanged = pyqtSignal(int)
    breedingExpectancyChanged = pyqtSignal(int)
    conceptionEfficiencyChanged = pyqtSignal(int)
    femalesToMalesChanged = pyqtSignal(int)
    adultWeightChanged = pyqtSignal(int)
    youngPerBirthChanged = pyqtSignal(int)
    weaningAgeChanged = pyqtSignal(int)
    weaningWeightChanged = pyqtSignal(int)
    gestationTimeChanged = pyqtSignal(int)
    estrousCycleChanged = pyqtSignal(int)
    lactationTimeChanged = pyqtSignal(int)
    milkChanged = pyqtSignal(int)
    milkGramsPerDayChanged = pyqtSignal(int)
    milkFoodValueChanged = pyqtSignal(int)
    fleeceChanged = pyqtSignal(int)
    fleeceWeightKgChanged = pyqtSignal(int)
    imageFileChanged = pyqtSignal(str)

    def __init__(self, theAnimal: Optional[Type['LaAnimal']] = None, parent=None):
        super().__init__(parent)
        if theAnimal is None:
            self._guid = LaGuid.setGuid(self, None)
            self._animalName = "No Name Set"
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
            self._animalName = theAnimal.name
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

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

    def __eq__(self, other):
        if not isinstance(other, LaAnimal):
            return False
        myAttributes = [
            '_animalName',            '_description',     '_guid',
            '_meatFoodValue',         '_usableMeat',      '_killWeight',
            '_growTime',              '_deathRate',       '_feedEnergyType',
            '_gestating',             '_lactating',       '_maintenance',
            '_juvenile',              '_sexualMaturity',  '_breedingExpectancy',
            '_youngPerBirth',         '_weaningAge',      '_weaningWeight',
            '_conceptionEfficiency',  '_femalesToMales',  '_adultWeight',
            '_gestationTime',         '_estrousCycle',    '_lactationTime',
            '_milk',                  '_milkGramsPerDay', '_milkFoodValue',
            '_fleece',                '_fleeceWeightKg',  '_imageFile'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    def __del__(self):
        pass

    def __copy__(self):
        myNewAnimal: LaAnimal = LaAnimal()
        myNewAnimal._animalName = self._animalName
        myNewAnimal._description = self._description
        myNewAnimal._guid = LaGuid.setGuid() # this gets a new guid
        myNewAnimal._meatFoodValue = self._meatFoodValue
        myNewAnimal._usableMeat = self._usableMeat
        myNewAnimal._killWeight = self._killWeight
        myNewAnimal._growTime = self._growTime
        myNewAnimal._deathRate = self._deathRate
        myNewAnimal._feedEnergyType = self._feedEnergyType
        myNewAnimal._gestating = self._gestating
        myNewAnimal._lactating = self._lactating
        myNewAnimal._maintenance = self._maintenance
        myNewAnimal._juvenile = self._juvenile
        myNewAnimal._sexualMaturity = self._sexualMaturity
        myNewAnimal._breedingExpectancy = self._breedingExpectancy
        myNewAnimal._conceptionEfficiency = self._conceptionEfficiency
        myNewAnimal._femalesToMales = self._femalesToMales
        myNewAnimal._adultWeight = self._adultWeight
        myNewAnimal._youngPerBirth = self._youngPerBirth
        myNewAnimal._weaningAge = self._weaningAge
        myNewAnimal._weaningWeight = self._weaningWeight
        myNewAnimal._gestationTime = self._gestationTime
        myNewAnimal._estrousCycle = self._estrousCycle
        myNewAnimal._lactationTime = self._lactationTime
        myNewAnimal._milk = self._milk
        myNewAnimal._milkGramsPerDay = self._milkGramsPerDay
        myNewAnimal._milkFoodValue = self._milkFoodValue
        myNewAnimal._fleece = self._fleece
        myNewAnimal._fleeceWeightKg = self._fleeceWeightKg
        myNewAnimal._imageFile = self._imageFile
        return myNewAnimal

    @pyqtProperty(str, notify=nameChanged)
    def animalName(self):
        return self._animalName

    @animalName.setter
    def animalName(self, theAnimalName):
        if self._animalName != theAnimalName:
            self._animalName = theAnimalName
            self.nameChanged.emit(theAnimalName)



    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @property
    def meatFoodValue(self):
        return self._meatFoodValue

    @meatFoodValue.setter
    def meatFoodValue(self, meatFoodValue):
        if self._meatFoodValue != meatFoodValue:
            self._meatFoodValue = meatFoodValue
            self.meatFoodValueChanged.emit(meatFoodValue)

    @property
    def usableMeat(self):
        return self._usableMeat

    @usableMeat.setter
    def usableMeat(self, usableMeat):
        if self._usableMeat != usableMeat:
            self._usableMeat = usableMeat
            self.usableMeatChanged.emit(usableMeat)

    @property
    def killWeight(self):
        return self._killWeight

    @killWeight.setter
    def killWeight(self, killWeight):
        if self._killWeight != killWeight:
            self._killWeight = killWeight
            self.killWeightChanged.emit(killWeight)

    @property
    def growTime(self):
        return self._growTime

    @growTime.setter
    def growTime(self, growTime):
        if self._growTime != growTime:
            self._growTime = growTime
            self.growTimeChanged.emit(growTime)

    @property
    def deathRate(self):
        return self._deathRate

    @deathRate.setter
    def deathRate(self, deathRate):
        if self._deathRate != deathRate:
            self._deathRate = deathRate
            self.deathRateChanged.emit(deathRate)

    @property
    def feedEnergyType(self):
        return self._feedEnergyType

    @feedEnergyType.setter
    def feedEnergyType(self, feedEnergyType):
        if self._feedEnergyType != feedEnergyType:
            self._feedEnergyType = feedEnergyType
            self.feedEnergyTypeChanged.emit(feedEnergyType)

    @property
    def gestating(self):
        return self._gestating

    @gestating.setter
    def gestating(self, gestating):
        if self._gestating != gestating:
            self._gestating = gestating
            self.gestatingChanged.emit(gestating)

    @property
    def lactating(self):
        return self._lactating

    @lactating.setter
    def lactating(self, lactating):
        if self._lactating != lactating:
            self._lactating = lactating
            self.lactatingChanged.emit(lactating)

    @property
    def maintenance(self):
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        if self._maintenance != maintenance:
            self._maintenance = maintenance
            self.maintenanceChanged.emit(maintenance)

    @property
    def juvenile(self):
        return self._juvenile

    @juvenile.setter
    def juvenile(self, juvenile):
        if self._juvenile != juvenile:
            self._juvenile = juvenile
            self.juvenileChanged.emit(juvenile)

    @property
    def sexualMaturity(self):
        return self._sexualMaturity

    @sexualMaturity.setter
    def sexualMaturity(self, sexualMaturity):
        if self._sexualMaturity != sexualMaturity:
            self._sexualMaturity = sexualMaturity
            self.sexualMaturityChanged.emit(sexualMaturity)

    @property
    def breedingExpectancy(self):
        return self._breedingExpectancy

    @breedingExpectancy.setter
    def breedingExpectancy(self, breedingExpectancy):
        if self._breedingExpectancy != breedingExpectancy:
            self._breedingExpectancy = breedingExpectancy
            self.breedingExpectancyChanged.emit(breedingExpectancy)

    @property
    def conceptionEfficiency(self):
        return self._conceptionEfficiency

    @conceptionEfficiency.setter
    def conceptionEfficiency(self, conceptionEfficiency):
        if self._conceptionEfficiency != conceptionEfficiency:
            self._conceptionEfficiency = conceptionEfficiency
            self.conceptionEfficiencyChanged.emit(conceptionEfficiency)

    @property
    def femalesPerMale(self):
        return self._femalesPerMale

    @femalesPerMale.setter
    def femalesPerMale(self, femalesPerMale):
        if self._femalesPerMale != femalesPerMale:
            self._femalesPerMale = femalesPerMale
            self.femalesPerMaleChanged.emit(femalesPerMale)

    @property
    def adultWeight(self):
        return self._adultWeight

    @adultWeight.setter
    def adultWeight(self, adultWeight):
        if self._adultWeight != adultWeight:
            self._adultWeight = adultWeight
            self.adultWeightChanged.emit(adultWeight)

    @property
    def youngPerBirth(self):
        return self._youngPerBirth

    @youngPerBirth.setter
    def youngPerBirth(self, youngPerBirth):
        if self._youngPerBirth != youngPerBirth:
            self._youngPerBirth = youngPerBirth
            self.youngPerBirthChanged.emit(youngPerBirth)

    @property
    def weaningAge(self):
        return self._weaningAge

    @weaningAge.setter
    def weaningAge(self, weaningAge):
        if self._weaningAge != weaningAge:
            self._weaningAge = weaningAge
            self.weaningAgeChanged.emit(weaningAge)

    @property
    def weaningWeight(self):
        return self._weaningWeight

    @weaningWeight.setter
    def weaningWeight(self, weaningWeight):
        if self._weaningWeight != weaningWeight:
            self._weaningWeight = weaningWeight
            self.weaningWeightChanged.emit(weaningWeight)

    @property
    def gestationTime(self):
        return self._gestationTime

    @gestationTime.setter
    def gestationTime(self, gestationTime):
        if self._gestationTime != gestationTime:
            self._gestationTime = gestationTime
            self.gestationTimeChanged.emit(gestationTime)

    @property
    def estrousCycle(self):
        return self._estrousCycle

    @estrousCycle.setter
    def estrousCycle(self, estrousCycle):
        if self._estrousCycle != estrousCycle:
            self._estrousCycle = estrousCycle
            self.estrousCycleChanged.emit(estrousCycle)

    @property
    def lactationTime(self):
        return self._lactationTime

    @lactationTime.setter
    def lactationTime(self, lactationTime):
        if self._lactationTime != lactationTime:
            self._lactationTime = lactationTime
            self.lactationTimeChanged.emit(lactationTime)

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, milk):
        if self._milk != milk:
            self._milk = milk
            self.milkChanged.emit(milk)

    @property
    def milkGramsPerDay(self):
        return self._milkGramsPerDay

    @milkGramsPerDay.setter
    def milkGramsPerDay(self, milkGramsPerDay):
        if self._milkGramsPerDay != milkGramsPerDay:
            self._milkGramsPerDay = milkGramsPerDay
            self.milkGramsPerDayChanged.emit(milkGramsPerDay)

    @property
    def milkFoodValue(self):
        return self._milkFoodValue

    @milkFoodValue.setter
    def milkFoodValue(self, milkFoodValue):
        if self._milkFoodValue != milkFoodValue:
            self._milkFoodValue = milkFoodValue
            self.milkFoodValueChanged.emit(milkFoodValue)

    @property
    def fleece(self):
        return self._fleece

    @fleece.setter
    def fleece(self, fleece):
        if self._fleece != fleece:
            self._fleece = fleece
            self.fleeceChanged.emit(fleece)

    @property
    def fleeceWeightKg(self):
        return self._fleeceWeightKg

    @fleeceWeightKg.setter
    def fleeceWeightKg(self, fleeceWeightKg):
        if self._fleeceWeightKg != fleeceWeightKg:
            self._fleeceWeightKg = fleeceWeightKg
            self.fleeceWeightKgChanged.emit(fleeceWeightKg)

    @property
    def imageFile(self):
        return self._imageFile

    @imageFile.setter
    def imageFile(self, imageFile):
        if self._imageFile != imageFile:
            self._imageFile = imageFile
            self.imageFileChanged.emit(imageFile)

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._animalName

    @name.setter
    def name(self, theAnimalName):
        if self._animalName != theAnimalName:
            self._animalName = theAnimalName
            self.nameChanged.emit(theAnimalName)


    def fromXml(self, theXml: str) -> bool:
        """
        Parses an XML string and sets the properties of the animal object accordingly.

        :param theXml: The XML string to parse.
        :type theXml: str
        :return: True if the parsing was successful, False otherwise.
        :rtype: bool
        """
        # the following import is here to avoid a circular import
        from la.lib.lautils import LaUtils #, xmlEncode, xmlDecode
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
        from la.lib.lautils import LaUtils # we import this here to avoid a circular import
        myString = f'<animal guid="{self.guid}">\n'
        """ NOTE:
            The LaUtils.xmlEncode function is likely used here to escape special characters that
            have specific meanings in XML. This is done to ensure that the _name value can be safely
            included in an XML document without causing parsing errors.

            For example, characters like <, >, and & are used in XML tags and entities.
            If these characters appear in the _name value, they could cause the XML to be malformed.

            The xmlEncode function would replace these characters with their corresponding
            XML entities (&lt;, &gt;, and &amp; respectively).
        """
        myString += f'  <name>{LaUtils.xmlEncode(self._animalName)}</name>\n'
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
        from la.lib.lautils import LaUtils # we import this here to avoid a circular import
        myString: str = f'guid=>{self.guid()}\n'
        """
        NOTE: The LaUtils.xmlEncode function is likely used here to escape special
             characters that have specific meanings in XML. This is done to ensure
             that the _name value can be safely included in an XML document without
             causing parsing errors.
             For example, chars like <, >, and & are used in XML tags/entities
             These characters in could cause the XML to be malformed.

             The xmlEncode function replaces these characters with their corresponding
            XML entities (&lt;, &gt;, and &amp; respectively).
        """
        myString += f'name=>{LaUtils.xmlEncode(self._animalName)}\n'
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
        from la.lib.lautils import LaUtils # we import this here to avoid a circular import
        myString = f'<h2>Details for {LaUtils.xmlEncode(self._animalName)}</h2>'
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
