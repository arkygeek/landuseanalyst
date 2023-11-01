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

# laanimal.py
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt, QMetaProperty
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.lautils import xmlEncode, xmlDecode # moved to method to avoid circular import
from la.lib.la import EnergyType
from qgis.PyQt.QtCore import pyqtProperty

class LaAnimal(LaSerialisable, LaGuid):
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
     # assign the signals
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    meatFoodValueChanged = pyqtSignal(int)
    usableMeatChanged = pyqtSignal(int)
    killWeightChanged = pyqtSignal(int)
    growTimeChanged = pyqtSignal(int)
    deathRateChanged = pyqtSignal(int)
    feedEnergyTypeChanged = pyqtSignal(EnergyType)  
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

    def __init__(self):
        super().__init__()
        self.name="No Name Set"
        self.description="Not Set"
        self.meatFoodValue=3000
        self.usableMeat=50
        self.killWeight=100
        self.growTime=10
        self.deathRate=10
            # self.Gestating=5000;//
            # self.Lactating=5000;
            # self.Juvenile=3500;
        self.sexualMaturity=18
        self.breedingExpectancy=5
        self.youngPerBirth=1
        self.weaningAge=12
        self.weaningWeight=30
        self.gestationTime=120
        self.estrousCycle=21

    def __del__(self):
        pass

    def __copy__(self):
        return LaAnimal(self)

    def __deepcopy__(self, memo):
        return LaAnimal(self)

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        return self._description

    @pyqtProperty(int, notify=meatFoodValueChanged)
    def meatFoodValue(self):
        return self._meatFoodValue

    @pyqtProperty(int, notify=usableMeatChanged)
    def usableMeat(self):
        return self._usableMeat

    @pyqtProperty(int, notify=killWeightChanged)
    def killWeight(self):
        return self._killWeight
    
    @pyqtProperty(int, notify=growTimeChanged)
    def growTime(self):
        return self._growTime
    
    @pyqtProperty(int, notify=deathRateChanged)
    def deathRate(self):
        return self._deathRate
    
    @pyqtProperty(EnergyType, notify=feedEnergyTypeChanged)
    def feedEnergyType(self):
        return self._feedEnergyType
    
    @pyqtProperty(int, notify=gestatingChanged)
    def gestating(self):
        return self._gestating
    
    @pyqtProperty(int, notify=lactatingChanged)
    def lactating(self):
        return self._lactating
    
    @pyqtProperty(int, notify=maintenanceChanged)
    def maintenance(self):
        return self._maintenance
    
    @pyqtProperty(int, notify=juvenileChanged)
    def juvenile(self):
        return self._juvenile
    
    @pyqtProperty(int, notify=sexualMaturityChanged)
    def sexualMaturity(self):
        return self._sexualMaturity
    
    @pyqtProperty(int, notify=breedingExpectancyChanged)
    def breedingExpectancy(self):
        return self._breedingExpectancy
    
    @pyqtProperty(int, notify=conceptionEfficiencyChanged)
    def conceptionEfficiency(self):
        return self._conceptionEfficiency
    
    @pyqtProperty(int, notify=femalesToMalesChanged)
    def femalesToMales(self):
        return self._femalesToMales
    
    @pyqtProperty(int, notify=adultWeightChanged)
    def adultWeight(self):
        return self._adultWeight
    
    @pyqtProperty(int, notify=youngPerBirthChanged)
    def youngPerBirth(self):
        return self._youngPerBirth
    
    @pyqtProperty(int, notify=weaningAgeChanged)
    def weaningAge(self):
        return self._weaningAge
    
    @pyqtProperty(int, notify=weaningWeightChanged)
    def weaningWeight(self):
        return self._weaningWeight
    
    @pyqtProperty(int, notify=gestationTimeChanged)
    def gestationTime(self):
        return self._gestationTime
    
    @pyqtProperty(int, notify=estrousCycleChanged)
    def estrousCycle(self):
        return self._estrousCycle
    
    @pyqtProperty(int, notify=lactationTimeChanged)
    def lactationTime(self):
        return self._lactationTime
    
    @pyqtProperty(int, notify=milkChanged)
    def milk(self):
        return self._milk
    
    @pyqtProperty(int, notify=milkGramsPerDayChanged)
    def milkGramsPerDay(self):
        return self._milkGramsPerDay
    
    @pyqtProperty(int, notify=milkFoodValueChanged)
    def milkFoodValue(self):    
        return self._milkFoodValue
    
    @pyqtProperty(int, notify=fleeceChanged)
    def fleece(self):
        return self._fleece
    
    @pyqtProperty(int, notify=fleeceWeightKgChanged)
    def fleeceWeightKg(self):
        return self._fleeceWeightKg
    
    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self):
        return self._imageFile

    def fromXml(self, theXml):
        # the following import is here to avoid a circular import
        from la.lib.lautils import xmlEncode, xmlDecode
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("animal")
        if myTopElement.isNull():
            # TODO - just make this a warning
            pass

        self.setGuid(myTopElement.attribute("guid"))
        self.name = xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = xmlDecode(myTopElement.firstChildElement("description").text())
        self.meatFoodValue = int(myTopElement.firstChildElement("meatFoodValue").text())
        self.usableMeat = int(myTopElement.firstChildElement("usableMeat").text())
        self.killWeight = int(myTopElement.firstChildElement("killWeight").text())
        self.adultWeight = int(myTopElement.firstChildElement("adultWeight").text())
        self.conceptionEfficiency = int(myTopElement.firstChildElement("conceptionEfficiency").text())
        self.femalesToMales = int(myTopElement.firstChildElement("femalesToMales").text())
        self.growTime = int(myTopElement.firstChildElement("growTime").text())
        self.deathRate = int(myTopElement.firstChildElement("deathRate").text())
        self.gestating = int(myTopElement.firstChildElement("gestating").text())
        self.lactating = int(myTopElement.firstChildElement("lactating").text())
        self.maintenance = int(myTopElement.firstChildElement("maintenance").text())
        self.juvenile = int(myTopElement.firstChildElement("juvenile").text())
        self.sexualMaturity = int(myTopElement.firstChildElement("sexualMaturity").text())
        self.breedingExpectancy = int(myTopElement.firstChildElement("breedingExpectancy").text())
        self.youngPerBirth = int(myTopElement.firstChildElement("youngPerBirth").text())
        self.weaningAge = int(myTopElement.firstChildElement("weaningAge").text())
        self.weaningWeight = int(myTopElement.firstChildElement("weaningWeight").text())
        self.gestationTime = int(myTopElement.firstChildElement("gestationTime").text())
        self.estrousCycle = int(myTopElement.firstChildElement("estrousCycle").text())
        self.lactationTime = int(myTopElement.firstChildElement("lactationTime").text())
        self.milk = int(myTopElement.firstChildElement("milk").text())
        self.milkGramsPerDay = int(myTopElement.firstChildElement("milkGramsPerDay").text())
        self.milkFoodValue = int(myTopElement.firstChildElement("milkFoodValue").text())
        self.fleece = int(myTopElement.firstChildElement("fleece").text())
        self.fleeceWeightKg = int(myTopElement.firstChildElement("fleeceWeightKg").text())
        self.imageFile = xmlDecode(myTopElement.firstChildElement("imageFile").text())
        # the following is a hack to get around the fact that the feedEnergyType
        # property is an enum, and the enum values are not being saved to the
        # XML file
        myFeedEnergyType: str = myTopElement.firstChildElement("feedEnergyType").text()
        if myFeedEnergyType == "KCalories":
            self.mFeedEnergyType = "KCalories"
        elif myFeedEnergyType == "TDN":
            self.mFeedEnergyType = "TDN"

        return True

    @name.setter
    def setName(self, name):
        self._name = name
        self.nameChanged.emit(name)

    # def setName(self, name):
    #     self._name = name

    def setGuid(self, guid):
        # Implement this method to set the guid
        pass

    def setDescription(self, description):
        self._description = description

    def setMeatFoodValue(self, meatFoodValue):
        self._meatFoodValue = meatFoodValue

    def setUsableMeat(self, usableMeat):
        self._usableMeat = usableMeat

    def setKillWeight(self, killWeight):
        self._killWeight = killWeight

    def setGrowTime(self, growTime):
        self._growTime = growTime

    
   


    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name != name:
            self._name = name
            self.nameChanged.emit(name)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(int, notify=meatFoodValueChanged)
    def meatFoodValue(self):
        return self._meatFoodValue

    @meatFoodValue.setter
    def meatFoodValue(self, meatFoodValue):
        if self._meatFoodValue != meatFoodValue:
            self._meatFoodValue = meatFoodValue
            self.meatFoodValueChanged.emit(meatFoodValue)

    @pyqtProperty(int, notify=usableMeatChanged)
    def usableMeat(self):
        return self._usableMeat

    @usableMeat.setter
    def usableMeat(self, usableMeat):
        if self._usableMeat != usableMeat:
            self._usableMeat = usableMeat
            self.usableMeatChanged.emit(usableMeat)

    @pyqtProperty(int, notify=killWeightChanged)
    def killWeight(self):
        return self._killWeight

    @killWeight.setter
    def killWeight(self, killWeight):
        if self._killWeight != killWeight:
            self._killWeight = killWeight
            self.killWeightChanged.emit(killWeight)

    @growTime.setter
    def growTime(self, growTime):
        if self._growTime != growTime:
            self._growTime = growTime
            self.growTimeChanged.emit(growTime)

    @deathRate.setter
    def deathRate(self, deathRate):
        if self._deathRate != deathRate:
            self._deathRate = deathRate
            self.deathRateChanged.emit(deathRate)

    @feedEnergyType.setter
    def feedEnergyType(self, feedEnergyType):
        if self._feedEnergyType != feedEnergyType:
            self._feedEnergyType = feedEnergyType
            self.feedEnergyTypeChanged.emit(feedEnergyType)

    @gestating.setter
    def gestating(self, gestating):
        if self._gestating != gestating:
            self._gestating = gestating
            self.gestatingChanged.emit(gestating)

    