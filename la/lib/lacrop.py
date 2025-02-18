# lacrop.py
# pyqtProperty is a decorator that is used to define Qt properties in Python.
# It is defined in a stub file that provides type hints
# for PyQt5 classes and methods. The actual implementation of the pyqtProperty
# decorator is in the PyQt5.QtCore module. The pyqtProperty decorator is used
# to define the properties of the LaCrop class, including name, description,
# cropType, plantingDate, harvestDate, and yieldValue.
import warnings
from typing import Optional, Type
from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot, Qt
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits
from la.lib.la import EnergyType

class LaCrop(QObject, LaSerialisable, LaGuid):
    """ The LaCrop class represents a crop that can be grown in a simulation.

    This class contains information about the crop's name, description, yield,
    and other properties. Note that the class name is used as a string in the
    type hint for the `the_crop` parameter. This is necessary because the class
    definition hasn't been fully parsed yet when the type hint is evaluated.
    The `Type` type hint is used to refer to the class itself.

    Attributes:
        name (str): The name of the crop.
        description (str): A description of the crop.
        cropYield (int): The yield of the crop in kg/ha.
        cropCalories (int): The number of calories produced by the crop.
        fodderProduction (int): The amount of fodder produced by the crop.
        fodderValue (int): The value of the fodder produced by the crop.
        cropFodderEnergyType (str): The type of energy produced by the crop.
        areaUnits (str): The units used to measure the area of the crop.
        imageFile (str): The image file used to represent the crop.
    """
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    cropYieldChanged = pyqtSignal(int)
    cropCaloriesChanged = pyqtSignal(int)
    cropFodderProductionChanged = pyqtSignal(int)
    cropFodderValueChanged = pyqtSignal(int)
    cropFodderEnergyTypeChanged = pyqtSignal(str)
    areaUnitsChanged = pyqtSignal(str)
    imageFileChanged = pyqtSignal(str)

    def __init__(self, theCrop: Optional[Type['LaCrop']] = None, parent=None):
        """Initializes a new instance of the LaCrop class.

        Args:
            the_crop (Optional[Type['LaCrop']]): An existing LaCrop object to copy.
                If provided, the new instance will be a copy of the existing object.
                If not provided, the new instance will be initialized with default values.
        """
        super().__init__(parent)
        if theCrop is None: # If NO crop is provided, initialize with default values.
            self._guid = LaGuid.setGuid(self, None)
            self._cropName = "No Name Set"
            self._description = "Not Set"
            self._cropYield = 60
            self._cropCalories = 3000
            self._cropFodderProduction = 50
            self._cropFodderValue = 1000
            self._imageFile = ""
            self._cropFodderEnergyType = ""
            self._areaUnits = ""
        else: # If a crop IS provided, copy the values from the existing crop.
            self._cropName = theCrop.name
            self._description = theCrop.description
            self._guid = theCrop.guid
            self._cropYield = theCrop.cropYield
            self._cropCalories = theCrop.cropCalories
            self._cropFodderProduction = theCrop.cropFodderProduction
            self._cropFodderValue = theCrop.cropFodderValue
            self._cropFodderEnergyType = theCrop.cropFodderEnergyType
            self._areaUnits = theCrop.areaUnits
            self._imageFile = theCrop.imageFile

    def __eq__(self, other):
        if not isinstance(other, LaCrop):
            return False
        myAttributes = [
            '_cropName',              '_description',     '_guid',
            '_cropYield',             '_cropCalories',    '_cropFodderProduction',
            '_cropFodderValue',       '_cropFodderEnergyType', '_areaUnits',
            '_imageFile'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    def __del__(self):
        # Perform any necessary cleanup here
        pass

    def __copy__(self):
        new_crop = LaCrop()
        new_crop._guid = self._guid
        new_crop._cropName = self._cropName
        new_crop._description = self._description
        new_crop._cropYield = self._cropYield
        new_crop._cropCalories = self._cropCalories
        new_crop._cropFodderProduction = self._cropFodderProduction
        new_crop._cropFodderValue = self._cropFodderValue
        new_crop._cropFodderEnergyType = self._cropFodderEnergyType
        new_crop._areaUnits = self._areaUnits
        new_crop._imageFile = self._imageFile
        return new_crop

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

    @pyqtProperty(str, notify=nameChanged)
    def name(self): # type: ignore
        return self._cropName

    @name.setter
    def name(self, name):
        if self._cropName != name:
            self._cropName = name
            self.nameChanged.emit(name)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self): # type: ignore
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(int, notify=cropYieldChanged)
    def cropYield(self): # type: ignore
        return self._cropYield

    @cropYield.setter
    def cropYield(self, cropYield):
        if self._cropYield != cropYield:
            self._cropYield = cropYield
            self.cropYieldChanged.emit(cropYield)

    @pyqtProperty(int, notify=cropCaloriesChanged)
    def cropCalories(self): # type: ignore
        return self._cropCalories

    @cropCalories.setter
    def cropCalories(self, cropCalories):
        if self._cropCalories != cropCalories:
            self._cropCalories = cropCalories
            self.cropCaloriesChanged.emit(cropCalories)

    @pyqtProperty(int, notify=cropFodderProductionChanged)
    def cropFodderProduction(self): # type: ignore
        return self._cropFodderProduction

    @cropFodderProduction.setter
    def cropFodderProduction(self, cropFodderProduction):
        if self._cropFodderProduction != cropFodderProduction:
            self._cropFodderProduction = cropFodderProduction
            self.cropFodderProductionChanged.emit(cropFodderProduction)

    @pyqtProperty(int, notify=cropFodderValueChanged)
    def cropFodderValue(self): # type: ignore
        return self._cropFodderValue

    @cropFodderValue.setter
    def cropFodderValue(self, cropFodderValue):
        if self._cropFodderValue != cropFodderValue:
            self._cropFodderValue = cropFodderValue
            self.cropFodderValueChanged.emit(cropFodderValue)

    @pyqtProperty(str, notify=cropFodderEnergyTypeChanged)
    def cropFodderEnergyType(self): # type: ignore
        return self._cropFodderEnergyType

    @cropFodderEnergyType.setter
    def cropFodderEnergyType(self, cropFodderEnergyType):
        if self._cropFodderEnergyType != cropFodderEnergyType:
            self._cropFodderEnergyType = cropFodderEnergyType
            self.cropFodderEnergyTypeChanged.emit(cropFodderEnergyType)

    @pyqtProperty(str, notify=areaUnitsChanged)
    def areaUnits(self): # type: ignore
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, areaUnits):
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits)

    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self): # type: ignore
        return self._imageFile

    @imageFile.setter
    def imageFile(self, imageFile):
        if self._imageFile != imageFile:
            self._imageFile = imageFile
            self.imageFileChanged.emit(imageFile)

    def fromXml(self, theXml: str) -> bool:
        """
        Parses an XML string and sets the properties of the crop object accordingly.

        Args:
        theXml (str): The XML string to parse.

        Returns:
        bool: True if the parsing was successful, False otherwise.
        """
        from la.lib.lautils import LaUtils
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("crop")

        # gracefully handle the case where the top element is null
        if myTopElement.isNull():
            warnings.warn("Failed to parse XML: myTopElement is null. The XML \
                element could not be found or parsed.")
            return False

        self.setGuid(myTopElement.attribute("guid"))
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())

        def GetIntValue(theElementName):
            myElementText = myTopElement.firstChildElement(theElementName).text()
            return int(myElementText) if myElementText else 0

        self.cropYield = GetIntValue("cropYield")
        self.cropCalories = GetIntValue("cropCalories")
        self.cropFodderProduction = GetIntValue("fodderProduction")
        self.cropFodderValue = GetIntValue("fodderCalories")

        myCropFodderEnergyType = myTopElement.firstChildElement("cropFodderEnergyType").text()
        if myCropFodderEnergyType == "KCalories":
            self.cropFodderEnergyType = EnergyType.KCalories
        elif myCropFodderEnergyType == "TDN":
            self.cropFodderEnergyType = EnergyType.TDN

        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self.areaUnits = AreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self.areaUnits = AreaUnits.Hectare
        self.imageFile = myTopElement.firstChildElement("imageFile").text()

        return True

    def toXml(self):
        myName: str = self.name
        myDescription: str = self.description
        myCropYield: int = self.cropYield
        myCropCalories: int = self.cropCalories
        myCropFodderProduction: int = self.cropFodderProduction
        myCropFodderValue: int = self.cropFodderValue

        myCropFodderEnergyType: str = ""
        if self.cropFodderEnergyType == EnergyType.KCalories:
            myCropFodderEnergyType = "KCalories"
        elif self.cropFodderEnergyType == EnergyType.TDN:
            myCropFodderEnergyType = "TDN"

        myAreaUnitsType: str = ""
        if self.areaUnits == AreaUnits.Dunum:
            myAreaUnitsType = "Dunum"
        elif self.areaUnits == AreaUnits.Hectare:
            myAreaUnitsType = "Hectare"
        myImageFile: str = self.imageFile

        myString = "<crop guid=\"" + self.guid() + "\">\n"
        myString += "  <name>" + myName + "</name>\n"
        myString += "  <description>" + myDescription + "</description>\n"
        myString += "  <cropYield>" + str(myCropYield) + "</cropYield>\n"
        myString += "  <cropCalories>" + str(myCropCalories) + "</cropCalories>\n"
        myString += "  <fodderProduction>" + str(myCropFodderProduction) + "</fodderProduction>\n"
        myString += "  <fodderCalories>" + str(myCropFodderValue) + "</fodderCalories>\n"
        myString += "  <cropFodderEnergyType>" + myCropFodderEnergyType + "</cropFodderEnergyType>\n"
        myString += "  <areaUnits>" + myAreaUnitsType + "</areaUnits>\n"
        myString += "  <imageFile>" + myImageFile + "</imageFile>\n"
        myString += "</crop>\n"
        return myString

    def toText(self):
        myName: str = self.name
        myDescription: str = self.description
        myCropYield: str = str(self.cropYield)
        myCropCalories: str = str(self.cropCalories)
        myCropFodderProduction: str = str(self.cropFodderProduction)
        myCropFodderValue: str = str(self.cropFodderValue)

        myCropFodderEnergyType: str = ""
        if self.cropFodderEnergyType == EnergyType.KCalories:
            myCropFodderEnergyType = "KCalories"
        elif self.cropFodderEnergyType == EnergyType.TDN:
            myCropFodderEnergyType = "TDN"

        myAreaUnitsType: str = ""
        if self.areaUnits == AreaUnits.Dunum:
            myAreaUnitsType = "Dunum"
        elif self.areaUnits == AreaUnits.Hectare:
            myAreaUnitsType = "Hectare"
        myImageFile: str = self.imageFile

        myString = "guid=>" + self.guid() + "\n"
        myString += "name=>" + myName + "\n"
        myString += "description=>" + myDescription + "\n"
        myString += "cropYield=>" + myCropYield + "\n"
        myString += "cropCalories=>" + myCropCalories + "\n"
        myString += "fodderProduction=>" + myCropFodderProduction + "\n"
        myString += "fodderCalories=>" + myCropFodderValue + "\n"
        myString += "cropFodderEnergyType=>" + myCropFodderEnergyType + "\n"
        myUnits = "Dunum" if self.areaUnits == AreaUnits.Dunum else "Hectare"
        myString += "yieldUnits=>" + myUnits + "\n"
        return myString

    def toHtml(self):
        myString = "<h3>Details for " + LaUtils.xmlEncode(self.name) + "</h3>"
        myString += "<table>"
        myString += "<tr><td><b>Description: </b></td><td>" + self.description + "</td></tr>"
        myString += "<tr><td><b>Avg Yield: </b></td><td>" + str(self.cropYield) + "</td></tr>"
        myString += "<tr><td><b>Cals/Kg: </b></td><td>" + str(self.cropCalories) + "</td></tr>"
        myCropFodderEnergyType = "KCalories" if self.cropFodderEnergyType == EnergyType.KCalories else "TDN"
        myUnits = "Dunum" if self.areaUnits == AreaUnits.Dunum else "Hectare"
        myString += "<tr><td><b>Fodder (kg/" + myUnits + "): </b></td><td>" + str(self.cropFodderProduction) + "</td></tr>"
        myString += "<tr><td><b>Fodder Value/Kg: </b></td><td>" + str(self.cropFodderValue) + "</td></tr>"
        myString += "<tr><td><b>FodderEnergyType: </b></td><td>" + myCropFodderEnergyType + "</td></tr>"
        myString += "<tr><td><b>AreaUnits: </b></td><td>" + myUnits + "</td></tr>"
        myString += "</table>"
        return myString