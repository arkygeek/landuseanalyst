import os
from typing import Optional, Type
import warnings
from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.la import AreaUnits
# from la.lib.lautils import LaUtils


class LaAnimalParameter(QObject, LaSerialisable, LaGuid):
    # from la.lib.lautils import LaUtils
    from la.lib.la import AreaUnits

    _instances = []



    def __init__(self, theAnimalParameter: Optional[Type['LaAnimalParameter']] = None):
        super().__init__()
        from la.lib.la import AreaUnits


        if theAnimalParameter is None:
            self._guid = LaGuid()
            self._name = "No Name Set"
            self._description = "Not Set"
            self._animalGuid = ""
            self._percentTameMeat = 0.0
            self._useCommonGrazingLand = False
            self._useSpecificGrazingLand = False
            self._valueCommonGrazingLand = 0.0
            self._valueSpecificGrazingLand = 0.0
            self._areaUnits = AreaUnits.Dunum
            self._energyType = ""
            self._fodderUse = 0.0
            self._foodSourceMap = ""
            self._fallowUsage = 0.0
            self._rasterName = ""
        else:
            self._guid = theAnimalParameter.guid
            self._name = theAnimalParameter.name
            self._description = theAnimalParameter.description
            self._animalGuid = theAnimalParameter.animalGuid
            self._percentTameMeat = theAnimalParameter.percentTameMeat
            self._useCommonGrazingLand = theAnimalParameter.useCommonGrazingLand
            self._useSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand
            self._valueCommonGrazingLand = theAnimalParameter.valueCommonGrazingLand
            self._valueSpecificGrazingLand = theAnimalParameter.valueSpecificGrazingLand
            self._areaUnits = theAnimalParameter.areaUnits
            self._energyType = theAnimalParameter.energyType
            self._fodderUse = theAnimalParameter.fodderUse
            self._foodSourceMap = theAnimalParameter.foodSourceMap
            self._fallowUsage = theAnimalParameter.fallowUsage
            self._rasterName = theAnimalParameter.rasterName

        self.__class__._instances.append(self)



    def __eq__(self, other):
        if not isinstance(other, LaAnimalParameter):
            return False
        myAttributes = [
            '_guid',               '_name',              '_description',
            '_animalGuid',         '_percentTameMeat',   '_useCommonGrazingLand',
            '_useSpecificGrazingLand', '_valueCommonGrazingLand', '_valueSpecificGrazingLand',
            '_areaUnits',          '_energyType',        '_fodderUse',
            '_foodSourceMap',      '_fallowUsage',       '_rasterName'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    nameChanged: pyqtSignal = pyqtSignal(str)
    descriptionChanged: pyqtSignal = pyqtSignal(str)
    guidChanged: pyqtSignal = pyqtSignal(str)
    animalGuidChanged: pyqtSignal = pyqtSignal(str)
    percentTameMeatChanged: pyqtSignal = pyqtSignal(float)
    useCommonGrazingLandChanged: pyqtSignal = pyqtSignal(bool)
    useSpecificGrazingLandChanged: pyqtSignal = pyqtSignal(bool)
    valueCommonGrazingLandChanged: pyqtSignal = pyqtSignal(float)
    valueSpecificGrazingLandChanged: pyqtSignal = pyqtSignal(float)
    areaUnitsChanged: pyqtSignal = pyqtSignal(AreaUnits)
    energyTypeChanged: pyqtSignal = pyqtSignal(str)
    fodderUseChanged: pyqtSignal = pyqtSignal(float)
    foodSourceMapChanged: pyqtSignal = pyqtSignal(str)
    fallowUsageChanged: pyqtSignal = pyqtSignal(float)
    rasterNameChanged: pyqtSignal = pyqtSignal(str)



    @classmethod
    def getInstances(cls):
        """Returns a list of all instances of LaAnimalParameter."""
        return cls._instances

    @classmethod
    def getInstanceByName(cls, name):
        for instance in cls._instances:
            if instance._name == name:
                return instance
        return None

    def remove(self):
        """Removes the animal parameter instance."""
        self.__class__._instances.remove(self)

    def save(self) -> None:
        """Saves the animal parameter to an XML file.

        This method converts the animal parameter object to an XML string and writes it to a file
        in the user's animal parameter profiles directory. The file name is based on the GUID of the animal parameter.
        """
        from la.lib.lautils import LaUtils
        myXmlContent = self.toXml()
        myFilePath = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(), f"{self.guid}.xml")
        with open(myFilePath, 'w') as myFile:
            myFile.write(myXmlContent)

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, theName):
        if self._name != theName:
            self._name = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, guid):
        if self._guid != guid:
            self._guid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=animalGuidChanged)
    def animalGuid(self):
        return self._animalGuid

    @animalGuid.setter
    def animalGuid(self, animalGuid):
        if self._animalGuid != animalGuid:
            self._animalGuid = animalGuid
            self.animalGuidChanged.emit(animalGuid)

    @pyqtProperty(float, notify=percentTameMeatChanged)
    def percentTameMeat(self):
        return self._percentTameMeat

    @percentTameMeat.setter
    def percentTameMeat(self, percentTameMeat):
        if self._percentTameMeat != percentTameMeat:
            self._percentTameMeat = percentTameMeat
            self.percentTameMeatChanged.emit(percentTameMeat)

    @pyqtProperty(bool, notify=useCommonGrazingLandChanged)
    def useCommonGrazingLand(self):
        return self._useCommonGrazingLand

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, useCommonGrazingLand):
        if self._useCommonGrazingLand != useCommonGrazingLand:
            self._useCommonGrazingLand = useCommonGrazingLand
            self.useCommonGrazingLandChanged.emit(useCommonGrazingLand)

    @pyqtProperty(bool, notify=useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self):
        return self._useSpecificGrazingLand

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, useSpecificGrazingLand):
        if self._useSpecificGrazingLand != useSpecificGrazingLand:
            self._useSpecificGrazingLand = useSpecificGrazingLand
            self.useSpecificGrazingLandChanged.emit(useSpecificGrazingLand)

    @pyqtProperty(float, notify=valueCommonGrazingLandChanged)
    def valueCommonGrazingLand(self):
        return self._valueCommonGrazingLand

    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, valueCommonGrazingLand):
        if self._valueCommonGrazingLand != valueCommonGrazingLand:
            self._valueCommonGrazingLand = valueCommonGrazingLand
            self.valueCommonGrazingLandChanged.emit(valueCommonGrazingLand)

    @pyqtProperty(float, notify=valueSpecificGrazingLandChanged)
    def valueSpecificGrazingLand(self):
        return self._valueSpecificGrazingLand

    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, valueSpecificGrazingLand):
        if self._valueSpecificGrazingLand != valueSpecificGrazingLand:
            self._valueSpecificGrazingLand = valueSpecificGrazingLand
            self.valueSpecificGrazingLandChanged.emit(valueSpecificGrazingLand)

    @pyqtProperty(AreaUnits, notify=areaUnitsChanged)
    def areaUnits(self):
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, areaUnits):
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits)

    @pyqtProperty(str, notify=energyTypeChanged)
    def energyType(self):
        return self._energyType

    @energyType.setter
    def energyType(self, energyType):
        if self._energyType != energyType:
            self._energyType = energyType
            self.energyTypeChanged.emit(energyType)

    @pyqtProperty(float, notify=fodderUseChanged)
    def fodderUse(self):
        return self._fodderUse

    @fodderUse.setter
    def fodderUse(self, fodderUse):
        if self._fodderUse != fodderUse:
            self._fodderUse = fodderUse
            self.fodderUseChanged.emit(fodderUse)

    @pyqtProperty(str, notify=foodSourceMapChanged)
    def foodSourceMap(self):
        return self._foodSourceMap

    @foodSourceMap.setter
    def foodSourceMap(self, foodSourceMap):
        if self._foodSourceMap != foodSourceMap:
            self._foodSourceMap = foodSourceMap
            self.foodSourceMapChanged.emit(foodSourceMap)

    @pyqtProperty(float, notify=fallowUsageChanged)
    def fallowUsage(self):
        return self._fallowUsage

    @fallowUsage.setter
    def fallowUsage(self, fallowUsage):
        if self._fallowUsage != fallowUsage:
            self._fallowUsage = fallowUsage
            self.fallowUsageChanged.emit(fallowUsage)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self):
        return self._rasterName

    @rasterName.setter
    def rasterName(self, rasterName):
        if self._rasterName != rasterName:
            self._rasterName = rasterName
            self.rasterNameChanged.emit(rasterName)

    def fromXml(self, theXml: str) -> bool:
        from la.lib.lautils import LaUtils
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("animalParameter")
        # gracefully handle the case where the top element is null
        if myTopElement.isNull():
            warnings.warn("Failed to parse XML: myTopElement is null. The XML \
                element could not be found or parsed.")
            return False
        self.setGuid(myTopElement.attribute("guid"))
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        self.animalGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("animal").text())
        self.percentTameMeat = float(myTopElement.firstChildElement("percentTameMeat").text())
        self.useCommonGrazingLand = int(myTopElement.firstChildElement("useCommonGrazingLand").text())
        self.useSpecificGrazingLand = int(myTopElement.firstChildElement("useSpecificGrazingLand").text())

        valueCommonGrazingLand_text = myTopElement.firstChildElement("valueCommonGrazingLand").text()
        self.valueCommonGrazingLand = float(valueCommonGrazingLand_text) if valueCommonGrazingLand_text else 0.0

        valueSpecificGrazingLand_text = myTopElement.firstChildElement("valueSpecificGrazingLand").text()
        self.valueSpecificGrazingLand = float(valueSpecificGrazingLand_text) if valueSpecificGrazingLand_text else 0.0

        my_area_units = myTopElement.firstChildElement("areaUnits").text()
        # doing area units this way makes the xml files PROFOUNDLY easier to read
        if my_area_units == "Dunum":
            self.areaUnits = AreaUnits.Dunum
        elif my_area_units == "Hectare":
            self.areaUnits = AreaUnits.Hectare
        self.energyType = LaUtils.xmlDecode(myTopElement.firstChildElement("energyType").text())
        self.fodderUse = float(myTopElement.firstChildElement("fodderUse").text())
        self.foodSourceMap = LaUtils.xmlDecode(myTopElement.firstChildElement("foodSourceMap").text())

        fallowUsage_text = myTopElement.firstChildElement("fallowUsage").text()
        try:
            self.fallowUsage = float(fallowUsage_text)
        except ValueError:
            self.fallowUsage = 0.0  # or handle it appropriately

        self.rasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
        return True



    def toXml(self):
        """Converts the LaAnimalParameter object to an XML string."""

        myString = f'<animalParameter guid="{self.guid}">\n'
        myString += f'  <name>{LaUtils.xmlEncode(self.name)}</name>\n'
        myString += f'  <description>{LaUtils.xmlEncode(self.description)}</description>\n'
        myString += f'  <animal>{LaUtils.xmlEncode(self.animalGuid)}</animal>\n'
        myString += f'  <percentTameMeat>{self.percentTameMeat}</percentTameMeat>\n'
        myString += f'  <useCommonGrazingLand>{self.useCommonGrazingLand}</useCommonGrazingLand>\n'
        myString += f'  <useSpecificGrazingLand>{self.useSpecificGrazingLand}</useSpecificGrazingLand>\n'
        myString += f'  <valueCommonGrazingLand>{self.valueCommonGrazingLand}</valueCommonGrazingLand>\n'
        myString += f'  <valueSpecificGrazingLand>{self.valueSpecificGrazingLand}</valueSpecificGrazingLand>\n'
        myString += f'  <areaUnits>{self.areaUnits}</areaUnits>\n'
        myString += f'  <energyType>{LaUtils.xmlEncode(self.energyType)}</energyType>\n'
        myString += f'  <fodderUse>{self.fodderUse}</fodderUse>\n'
        myString += f'  <foodSourceMap>{LaUtils.xmlEncode(self.foodSourceMap)}</foodSourceMap>\n'
        myString += f'  <fallowUsage>{self.fallowUsage}</fallowUsage>\n'
        myString += f'  <rasterName>{LaUtils.xmlEncode(self.rasterName)}</rasterName>\n'
        myString += '</animalParameter>\n'
        return myString