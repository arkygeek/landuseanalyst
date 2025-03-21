import os
from typing import Optional, Type
import warnings
from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.resources_rc import *

# from la.lib.la import AreaUnits
# from la.lib.lautils import LaUtils


class LaAnimalParameter(QObject, LaSerialisable, LaGuid):
    # from la.lib.lautils import LaUtils
    from la.lib.la import AreaUnits, Priority  # Added Priority import

    _instances = []

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    guidChanged = pyqtSignal(str)
    animalGuidChanged = pyqtSignal(str)
    percentTameMeatChanged = pyqtSignal(float)
    useCommonGrazingLandChanged = pyqtSignal(bool)
    useSpecificGrazingLandChanged = pyqtSignal(bool)
    fodderUseChanged = pyqtSignal(float)
    foodSourceMapChanged = pyqtSignal(str)
    fallowUsageChanged = pyqtSignal(object)  # Changed to object for enum
    rasterNameChanged = pyqtSignal(str)

    def __init__(self, theAnimalParameter: Optional['LaAnimalParameter'] = None, parent=None):
        super().__init__(parent)
        if theAnimalParameter is None:
            self._mGuid = LaGuid.setGuid(self, None)
            self._mName = "No Name Set"
            self._mDescription = "Not Set"
            self._mAnimalGuid = ""
            self._mPercentTameMeat = 0.0
            self._mUseCommonGrazingLand = False
            self._mUseSpecificGrazingLand = False
            self._mFodderUse = 0.0
            self._mFoodSourceMap = ""
            self._fallowUsage = 0.0  # Initialize fallow usage
            self._rasterName = ""    # Initialize raster name
        else:
            self._mGuid = theAnimalParameter.guid
            self._mName = theAnimalParameter.name
            self._mDescription = theAnimalParameter.description
            self._mAnimalGuid = theAnimalParameter.animalGuid
            self._mPercentTameMeat = theAnimalParameter.percentTameMeat
            self._mUseCommonGrazingLand = theAnimalParameter.useCommonGrazingLand
            self._mUseSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand
            self._mFodderUse = theAnimalParameter.fodderUse
            self._mFoodSourceMap = theAnimalParameter.foodSourceMap
            self._fallowUsage = theAnimalParameter.fallowUsage  # Copy fallow usage
            self._rasterName = theAnimalParameter.rasterName    # Copy raster name

        self.__class__._instances.append(self)

    def __eq__(self, other):
        if not isinstance(other, LaAnimalParameter):
            return False
        myAttributes = [
            '_mGuid',               '_mName',              '_mDescription',
            '_mAnimalGuid',         '_mPercentTameMeat',   '_mUseCommonGrazingLand',
            '_mUseSpecificGrazingLand', '_mFodderUse', '_mFoodSourceMap'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    @classmethod
    def getInstances(cls):
        """Returns a list of all instances of LaAnimalParameter."""
        return cls._instances

    @classmethod
    def getInstanceByName(cls, name):
        for instance in cls._instances:
            if instance._mName == name:
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
    def name(self): # type: ignore
        return self._mName

    @name.setter
    def name(self, theName: str) -> None:
        if self._mName != theName:
            self._mName = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str:
        return self._mDescription

    @description.setter
    def description(self, theDescription: str) -> None:
        if self._mDescription != theDescription:
            self._mDescription = theDescription
            self.descriptionChanged.emit(theDescription)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self):
        return self._mGuid

    @guid.setter
    def guid(self, guid):
        if self._mGuid != guid:
            self._mGuid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=animalGuidChanged)
    def animalGuid(self) -> str:
        return self._mAnimalGuid

    @animalGuid.setter
    def animalGuid(self, theAnimalGuid: str) -> None:
        if self._mAnimalGuid != theAnimalGuid:
            self._mAnimalGuid = theAnimalGuid
            self.animalGuidChanged.emit(theAnimalGuid)

    @pyqtProperty(float, notify=percentTameMeatChanged)
    def percentTameMeat(self) -> float:
        return self._mPercentTameMeat

    @percentTameMeat.setter
    def percentTameMeat(self, thePercentTameMeat: float) -> None:
        if self._mPercentTameMeat != thePercentTameMeat:
            self._mPercentTameMeat = thePercentTameMeat
            self.percentTameMeatChanged.emit(thePercentTameMeat)

    @pyqtProperty(bool, notify=useCommonGrazingLandChanged)
    def useCommonGrazingLand(self) -> bool:
        return self._mUseCommonGrazingLand

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, theUseCommonGrazingLand: bool) -> None:
        if self._mUseCommonGrazingLand != theUseCommonGrazingLand:
            self._mUseCommonGrazingLand = theUseCommonGrazingLand
            self.useCommonGrazingLandChanged.emit(theUseCommonGrazingLand)

    @pyqtProperty(bool, notify=useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self) -> bool:
        return self._mUseSpecificGrazingLand

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, theUseSpecificGrazingLand: bool) -> None:
        if self._mUseSpecificGrazingLand != theUseSpecificGrazingLand:
            self._mUseSpecificGrazingLand = theUseSpecificGrazingLand
            self.useSpecificGrazingLandChanged.emit(theUseSpecificGrazingLand)

    @pyqtProperty(float, notify=fodderUseChanged)
    def fodderUse(self) -> float:
        return self._mFodderUse

    @fodderUse.setter
    def fodderUse(self, theFodderUse: float) -> None:
        if self._mFodderUse != theFodderUse:
            self._mFodderUse = theFodderUse
            self.fodderUseChanged.emit(theFodderUse)

    @pyqtProperty(str, notify=foodSourceMapChanged)
    def foodSourceMap(self) -> str:
        return self._mFoodSourceMap

    @foodSourceMap.setter
    def foodSourceMap(self, theFoodSourceMap: str) -> None:
        if self._mFoodSourceMap != theFoodSourceMap:
            self._mFoodSourceMap = theFoodSourceMap
            self.foodSourceMapChanged.emit(theFoodSourceMap)

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
        from la.lib.la import Priority
        try:
            myDocument = QDomDocument("mydocument")
            myDocument.setContent(theXml)
            myTopElement = myDocument.firstChildElement("animalParameter")
            if myTopElement.isNull():
                warnings.warn("Failed to parse XML: myTopElement is null. The XML element could not be found or parsed.")
                return False
            self.setGuid(myTopElement.attribute("guid"))
            self._mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
            self._mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
            self._mAnimalGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("animal").text())
            self._mPercentTameMeat = float(myTopElement.firstChildElement("percentTameMeat").text())
            self._mUseCommonGrazingLand = bool(myTopElement.firstChildElement("useCommonGrazingLand").text())
            self._mUseSpecificGrazingLand = bool(myTopElement.firstChildElement("useSpecificGrazingLand").text())
            self._mFodderUse = float(myTopElement.firstChildElement("fodderUse").text())
            self._mFoodSourceMap = LaUtils.xmlDecode(myTopElement.firstChildElement("foodSourceMap").text())
            
            # Handle fallowUsage as a Priority enum
            fallowUsageElement = myTopElement.firstChildElement("fallowUsage")
            if not fallowUsageElement.isNull():
                fallowUsageText = fallowUsageElement.text()
                if fallowUsageText == "High":
                    self._fallowUsage = Priority.High
                elif fallowUsageText == "Medium":
                    self._fallowUsage = Priority.Medium
                elif fallowUsageText == "Low":
                    self._fallowUsage = Priority.Low
                else:
                    self._fallowUsage = Priority.None_  # Default to None if value doesn't match
            else:
                self._fallowUsage = Priority.None_  # Default if element is missing
            
            self._rasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
            return True
        except Exception as e:
            print(f"DEBUG: Error in fromXml: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return False

    def toXml(self) -> str:
        from la.lib.lautils import LaUtils
        myString = f"<animalParameter guid=\"{self.guid}\">\n"
        myString += f"  <name>{self.name}</name>\n"
        myString += f"  <description>{self.description}</description>\n"
        myString += f"  <animal>{self.animalGuid}</animal>\n"
        myString += f"  <percentTameMeat>{self.percentTameMeat}</percentTameMeat>\n"
        myString += f"  <useCommonGrazingLand>{1 if self.useCommonGrazingLand else 0}</useCommonGrazingLand>\n"
        myString += f"  <useSpecificGrazingLand>{1 if self.useSpecificGrazingLand else 0}</useSpecificGrazingLand>\n"
        myString += f"  <fodderUse>{self.fodderUse}</fodderUse>\n"
        myString += f"  <foodSourceMap>{self.foodSourceMap}</foodSourceMap>\n"
        myString += f"  <fallowUsage>{self.fallowUsage}</fallowUsage>\n"
        myString += f"  <rasterName>{self.rasterName}</rasterName>\n"
        myString += "</animalParameter>\n"
        return myString