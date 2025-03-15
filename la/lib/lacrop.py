# lacrop.py
# pyqtProperty is a decorator that is used to define Qt properties in Python.
# It is defined in a stub file that provides type hints
# for PyQt5 classes and methods. The actual implementation of the pyqtProperty
# decorator is in the PyQt5.QtCore module. The pyqtProperty decorator is used
# to define the properties of the LaCrop class, including name, description,
# cropType, plantingDate, harvestDate, and yieldValue.
import warnings
from typing import Literal, Optional, Type
from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot, Qt
from qgis.PyQt.QtXml import QDomDocument

from la.resources_rc import *

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType

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
        yield (int): The yield of the crop in kg/ha.
        cropCalories (int): The number of calories produced by the crop.
        fodderProduction (int): The amount of fodder produced by the crop.
        fodderValue (int): The value of the fodder produced by the crop.
        cropFodderEnergyType (str): The type of energy produced by the crop.
        areaUnits (str): The units used to measure the area of the crop.
        imageFile (str): The image file used to represent the crop.
    """
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    yieldChanged = pyqtSignal(int)
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
            self._name = "No Name Set"
            self._description = "Not Set"
            self._cropYield = 60
            self._calories = 3000
            self._fodderProduction = 50
            self._fodderValue = 1000
            self._imageFile = ""
            self._fodderEnergyType = ""
            self._areaUnits = ""
        else: # If a crop IS provided, copy the values from the existing crop.
            self._name = theCrop.name
            self._description = theCrop.description
            self._guid = theCrop.guid
            self._cropYield = theCrop.cropYield
            self._calories = theCrop.cropCalories
            self._fodderProduction = theCrop.cropFodderProduction
            self._fodderValue = theCrop.cropFodderValue
            self._fodderEnergyType = theCrop.cropFodderEnergyType
            self._areaUnits = theCrop.areaUnits
            self._imageFile = theCrop.imageFile

    def __eq__(self, other):
        if not isinstance(other, LaCrop):
            return False
        myAttributes = [
            '_name',              '_description',     '_guid',
            '_cropYield',             '_calories',    '_fodderProduction',
            '_fodderValue',       '_fodderEnergyType', '_areaUnits',
            '_imageFile'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    def __del__(self):
        # Perform any necessary cleanup here
        pass

    def __copy__(self):
        myNewCrop = LaCrop()
        myNewCrop.guid = self.guid
        myNewCrop.name = self.name
        myNewCrop.description = self.description
        myNewCrop.cropYield = self.cropYield
        myNewCrop.cropCalories = self.cropCalories
        myNewCrop.cropFodderProduction = self.cropFodderProduction
        myNewCrop.cropFodderValue = self.cropFodderValue
        myNewCrop.cropFodderEnergyType = self.cropFodderEnergyType
        myNewCrop.areaUnits = self.areaUnits
        myNewCrop.imageFile = self.imageFile
        return myNewCrop

    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value

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

    @pyqtProperty(int, notify=yieldChanged)
    def cropYield(self):
        return self._cropYield

    @cropYield.setter
    def cropYield(self, value):
        if self._cropYield != value:
            self._cropYield = value
            self.yieldChanged.emit(value)

    @pyqtProperty(int, notify=cropCaloriesChanged)
    def cropCalories(self):
        return self._calories

    @cropCalories.setter
    def cropCalories(self, cropCalories):
        if self._calories != cropCalories:
            self._calories = cropCalories
            self.cropCaloriesChanged.emit(cropCalories)

    @pyqtProperty(int, notify=cropFodderProductionChanged)
    def cropFodderProduction(self):
        return self._fodderProduction

    @cropFodderProduction.setter
    def cropFodderProduction(self, cropFodderProduction):
        if self._fodderProduction != cropFodderProduction:
            self._fodderProduction = cropFodderProduction
            self.cropFodderProductionChanged.emit(cropFodderProduction)

    @pyqtProperty(int, notify=cropFodderValueChanged)
    def cropFodderValue(self):
        return self._fodderValue

    @cropFodderValue.setter
    def cropFodderValue(self, cropFodderValue):
        if self._fodderValue != cropFodderValue:
            self._fodderValue = cropFodderValue
            self.cropFodderValueChanged.emit(cropFodderValue)

    @pyqtProperty(LaEnergyType, notify=cropFodderEnergyTypeChanged)
    def cropFodderEnergyType(self):
        return self._fodderEnergyType

    @cropFodderEnergyType.setter
    def cropFodderEnergyType(self, cropFodderEnergyType):
        if self._fodderEnergyType != cropFodderEnergyType:
            self._fodderEnergyType = cropFodderEnergyType
            self.cropFodderEnergyTypeChanged.emit(cropFodderEnergyType)

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self):
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, areaUnits):
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits)

    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self):
        return self._imageFile

    @imageFile.setter
    def imageFile(self, imageFile) -> None:
        if self._imageFile != imageFile:
            self._imageFile = imageFile
            self.imageFileChanged.emit(imageFile)

    def fromXml(self, theXml):
        """
        Parses an XML string and sets the properties of the crop object accordingly.
        Args:
        theXml (str): The XML string to parse.
        Returns:
        bool: True if the parsing was successful, False otherwise.
        """

        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("crop")

        # gracefully handle the case where the top element is null
        if myTopElement.isNull():
            warnings.warn("Failed to parse XML: myTopElement is null. The XML \
                element could not be found or parsed.")
            return False

        self.setGuid(myTopElement.attribute("guid"))
        self._name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self._description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())

        def GetIntValue(theElementName):
            myElementText = myTopElement.firstChildElement(theElementName).text()
            return int(myElementText) if myElementText else 0

        self._cropYield = GetIntValue("yield")  # XML tag can still be "yield"
        self._calories = GetIntValue("cropCalories")
        self._fodderProduction = GetIntValue("fodderProduction")
        self._fodderValue = GetIntValue("fodderCalories")

        myCropFodderEnergyType = myTopElement.firstChildElement("cropFodderEnergyType").text()
        if myCropFodderEnergyType == "KCalories":
            self._fodderEnergyType = LaEnergyType.KCalories
        elif myCropFodderEnergyType == "TDN":
            self._fodderEnergyType = LaEnergyType.TDN

        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self._areaUnits = LaAreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self._areaUnits = LaAreaUnits.Hectare
        # self.imageFile = myTopElement.firstChildElement("imageFile").text()
        # Handle image path with cross-platform resolution
        imagePath = myTopElement.firstChildElement("imageFile").text()
        from la.lib.lautils import LaUtils
        self._imageFile = LaUtils.resolvePath(imagePath, 'image')

        return True

    def toXml(self):
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        # Prepare values for XML
        myName = self.name
        myDescription = str(self.description)
        myCropYield = str(self.cropYield)
        myCropCalories = str(self.cropCalories)
        myCropFodderProduction = str(self.cropFodderProduction)
        myCropFodderValue = str(self.cropFodderValue)

        # Determine area units
        myAreaUnitsType = "Hectare"
        if self.areaUnits == LaAreaUnits.Dunum:
            myAreaUnitsType = "Dunum"

        # Determine energy type
        myCropFodderEnergyType = ""
        if self.cropFodderEnergyType == LaEnergyType.KCalories:
            myCropFodderEnergyType = "KCalories"
        elif self.cropFodderEnergyType == LaEnergyType.TDN:
            myCropFodderEnergyType = "TDN"

        myImageFile = str(self._imageFile)

        # Build XML using f-strings for each line
        xml = f'<crop guid="{self.guid}">\n'
        xml += f'  <name>{myName}</name>\n'
        xml += f'  <description>{myDescription}</description>\n'
        xml += f'  <yield>{myCropYield}</yield>\n'
        xml += f'  <cropCalories>{myCropCalories}</cropCalories>\n'
        xml += f'  <fodderProduction>{myCropFodderProduction}</fodderProduction>\n'
        xml += f'  <fodderCalories>{myCropFodderValue}</fodderCalories\n'
        xml += f'  <cropFodderEnergyType>{myCropFodderEnergyType}</cropFodderEnergyType>\n'
        xml += f'  <areaUnits>{myAreaUnitsType}</areaUnits>\n'
        xml += f'  <imageFile>{myImageFile}</imageFile>\n'
        xml += '</crop>\n'

        return xml

    def toText(self):
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        myName = str(self.name)
        myGuid = str(self.guid)
        myDescription = str(self.description)
        myCropYield = str(self.cropYield)
        myCropCalories = str(self.cropCalories)
        myCropFodderProduction = str(self.cropFodderProduction)
        myCropFodderValue = str(self.cropFodderValue)

        if self.cropFodderEnergyType == LaEnergyType.KCalories:
            myCropFodderEnergyType = "KCalories"
        elif self.cropFodderEnergyType == LaEnergyType.TDN:
            myCropFodderEnergyType = "TDN"

        myAreaUnitsType= ""
        if self.areaUnits == LaAreaUnits.Dunum:
            myAreaUnitsType = "Dunum"
        elif self.areaUnits == LaAreaUnits.Hectare:
            myAreaUnitsType = "Hectare"
        myImageFile = self.imageFile

        myString = "guid=>" + str(self.guid) + "\n"
        myString += "name=>" + myName + "\n"
        myString += "description=>" + myDescription + "\n"
        myString += "yield=>" + myCropYield + "\n"
        myString += "cropCalories=>" + myCropCalories + "\n"
        myString += "fodderProduction=>" + myCropFodderProduction + "\n"
        myString += "fodderCalories=>" + myCropFodderValue + "\n"
        myString += "cropFodderEnergyType=>" + myCropFodderEnergyType + "\n"
        myString += "yieldUnits=>" + myAreaUnitsType + "\n"
        return myString

    def toHtml(self):
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        myCropFodderEnergyType = "KCalories" if self.cropFodderEnergyType == LaEnergyType.KCalories else "TDN"
        myUnits = "Dunum" if self.areaUnits == LaAreaUnits.Dunum else "Hectare"

        myString = "<h3>Details for " + str(LaUtils.xmlEncode(self.name)) + "</h3>"
        myString += "<table>"
        myString += "<tr><td><b>Description: </b></td><td>" + str(self.description) + "</td></tr>"
        myString += "<tr><td><b>Avg Yield: </b></td><td>" + str(self.cropYield) + "</td></tr>"
        myString += "<tr><td><b>Cals/Kg: </b></td><td>" + str(self.cropCalories) + "</td></tr>"
        myString += "<tr><td><b>Fodder (kg/" + myUnits + "): </b></td><td>" + str(self.cropFodderProduction) + "</td></tr>"
        myString += "<tr><td><b>Fodder Value/Kg: </b></td><td>" + str(self.cropFodderValue) + "</td></tr>"
        myString += "<tr><td><b>FodderEnergyType: </b></td><td>" + myCropFodderEnergyType + "</td></tr>"
        myString += "<tr><td><b>AreaUnits: </b></td><td>" + myUnits + "</td></tr>"
        myString += "</table>"
        return myString