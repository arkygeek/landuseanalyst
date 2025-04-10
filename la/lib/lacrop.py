# lacrop.py
# pyqtProperty is a decorator that is used to define Qt properties in Python.
# It is defined in a stub file that provides type hints
# for PyQt5 classes and methods. The actual implementation of the pyqtProperty
# decorator is in the PyQt5.QtCore module. The pyqtProperty decorator is used
# to define the properties of the LaCrop class, including name, description,
# cropType, plantingDate, harvestDate, and yieldValue.
import warnings
from typing import Optional, Type

from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument
from la.lib.lautils import LaMessageBus, LaUtils
from la.resources_rc import *

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType

MESSAGE_BUS: LaMessageBus = LaMessageBus()

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
    cropFodderEnergyTypeChanged = pyqtSignal(LaEnergyType)
    areaUnitsChanged = pyqtSignal(LaAreaUnits)
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
            self._mGuid = LaGuid.setGuid(self, None)
            self._mName = "No Name Set"
            self._mDescription = "Not Set"
            self._mCropYield = 60
            self._mCalories = 3000
            self._mFodderProduction = 50
            self._mFodderValue = 1000
            self._mImageFile = ""
            self._mFodderEnergyType = ""
            self._mAreaUnits = ""
        else: # If a crop IS provided, copy the values from the existing crop.
            self._mGuid = theCrop.guid
            self._mName = theCrop.name
            self._mDescription = theCrop.description
            self._mCropYield = theCrop.cropYield
            self._mCalories = theCrop.cropCalories
            self._mFodderProduction = theCrop.cropFodderProduction
            self._mFodderValue = theCrop.cropFodderValue
            self._mFodderEnergyType = theCrop.cropFodderEnergyType
            self._mAreaUnits = theCrop.areaUnits
            self._mImageFile = theCrop.imageFile

    def __eq__(self, other):
        """
        Compare this crop with another for equality.

        :param other: Another object to compare with
        :type other: object
        :returns: True if both crops have identical properties, False otherwise
        :rtype: bool
        """
        if not isinstance(other, LaCrop):
            return False
        myAttributes = [
            '_mName',              '_mDescription',     '_mGuid',
            '_mCropYield',         '_mCalories',        '_mFodderProduction',
            '_mFodderValue',       '_mFodderEnergyType', '_mAreaUnits',
            '_mImageFile'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed.
        Performs necessary cleanup operations.
        """
        # Perform any necessary cleanup here
        pass

    def __copy__(self) -> "LaCrop":
        """
        Create a deep copy of this crop.

        :returns: A new LaCrop instance with the same properties as this one
        :rtype: LaCrop
        """
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
        """
        Get the GUID (Globally Unique Identifier) of this crop.

        :returns: The crop's GUID
        :rtype: str
        """
        return self._mGuid

    @guid.setter
    def guid(self, theGuid):
        """
        Set the GUID (Globally Unique Identifier) for this crop.

        :param value: The new GUID value
        :type value: str
        """
        self._mGuid = theGuid

    @pyqtProperty(str, notify=nameChanged)
    def name(self): #type: ignore
        """
        Get the name of this crop.

        :returns: The crop's name
        :rtype: str
        """
        return self._mName

    @name.setter
    def name(self, name):
        """
        Set the name of this crop.

        :param name: The new crop name
        :type name: str
        """
        if self._mName != name:
            self._mName = name
            self.nameChanged.emit(name)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self): #type: ignore
        """
        Get the description of this crop.

        :returns: The crop's description
        :rtype: str
        """
        return self._mDescription

    @description.setter
    def description(self, description):
        """
        Set the description of this crop.

        :param description: The new crop description
        :type description: str
        """
        if self._mDescription != description:
            self._mDescription = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(int, notify=yieldChanged)
    def cropYield(self): #type: ignore
        """
        Get the yield value for this crop (kg/ha or kg/dunum).

        :returns: The crop's yield value
        :rtype: int
        """
        myCropYield = self._mCropYield
        return self._mCropYield

    @cropYield.setter
    def cropYield(self, theYield):
        """
        Set the yield value for this crop.

        :param theYield: The new yield value
        :type theYield: int
        """
        if self._mCropYield != theYield:
            self._mCropYield = theYield
            self.yieldChanged.emit(theYield)

    @pyqtProperty(int, notify=cropCaloriesChanged)
    def cropCalories(self): #type: ignore
        """
        Get the caloric value per kg of this crop.

        :returns: The calories per kilogram
        :rtype: int
        """
        return self._mCalories

    @cropCalories.setter
    def cropCalories(self, cropCalories):
        """
        Set the caloric value per kg of this crop.

        :param cropCalories: The new caloric value
        :type cropCalories: int
        """
        if self._mCalories != cropCalories:
            self._mCalories = cropCalories
            self.cropCaloriesChanged.emit(cropCalories)

    @pyqtProperty(int, notify=cropFodderProductionChanged)
    def cropFodderProduction(self): #type: ignore
        """
        Get the fodder production amount for this crop.

        :returns: The amount of fodder produced per area unit
        :rtype: int
        """
        return self._mFodderProduction

    @cropFodderProduction.setter
    def cropFodderProduction(self, theCropFodderProduction):
        """
        Set the fodder production amount for this crop.

        :param theCropFodderProduction: The new fodder production value
        :type theCropFodderProduction: int
        """
        if self._mFodderProduction != theCropFodderProduction:
            self._mFodderProduction = theCropFodderProduction
            self.cropFodderProductionChanged.emit(theCropFodderProduction)

    @pyqtProperty(int, notify=cropFodderValueChanged)
    def cropFodderValue(self): #type: ignore
        """
        Get the nutritional value of fodder produced by this crop.

        :returns: The fodder's nutritional value
        :rtype: int
        """
        return self._mFodderValue

    @cropFodderValue.setter
    def cropFodderValue(self, cropFodderValue):
        """
        Set the nutritional value of fodder produced by this crop.

        :param cropFodderValue: The new fodder nutritional value
        :type cropFodderValue: int
        """
        if self._mFodderValue != cropFodderValue:
            self._mFodderValue = cropFodderValue
            self.cropFodderValueChanged.emit(cropFodderValue)

    @pyqtProperty(LaEnergyType, notify=cropFodderEnergyTypeChanged)
    def cropFodderEnergyType(self): #type: ignore
        """
        Get the energy type for measuring fodder value (KCalories or TDN).

        :returns: The fodder energy measurement type
        :rtype: LaEnergyType
        """
        return self._mFodderEnergyType

    @cropFodderEnergyType.setter
    def cropFodderEnergyType(self, theCropFodderEnergyType):
        """
        Set the energy type for measuring fodder value.

        :param cropFodderEnergyType: The new fodder energy measurement type
        :type cropFodderEnergyType: LaEnergyType
        """
        if self._mFodderEnergyType != theCropFodderEnergyType:
            self._mFodderEnergyType = theCropFodderEnergyType
            self.cropFodderEnergyTypeChanged.emit(theCropFodderEnergyType)

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self): #type: ignore
        """
        Get the area units used for this crop (Hectare or Dunum).

        :returns: The area units used for yield calculations
        :rtype: LaAreaUnits
        """
        return self._mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnits):
        """
        Set the area units used for this crop.

        :param theAreaUnits: The new area units
        :type theAreaUnits: LaAreaUnits
        """
        if self._mAreaUnits != theAreaUnits:
            self._mAreaUnits = theAreaUnits
            self.areaUnitsChanged.emit(theAreaUnits)

    @pyqtProperty(str, notify=imageFileChanged)
    def imageFile(self): #type: ignore
        """
        Get the path to the image file representing this crop.

        :returns: The image file path
        :rtype: str
        """
        return self._mImageFile

    @imageFile.setter
    def imageFile(self, imageFile) -> None:
        """
        Set the path to the image file representing this crop.

        :param imageFile: The new image file path
        :type imageFile: str
        """
        if self._mImageFile != imageFile:
            self._mImageFile = imageFile
            self.imageFileChanged.emit(imageFile)

    def fromXml(self, theXml):
        """
        Parses an XML string and sets the properties of the crop object accordingly.
        Direct port from C++ version.

        Args:
            theXml (str): The XML string to parse.
        Returns:
            bool: True if successful.
        """
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("crop")
        if myTopElement.isNull():
            # C++ version just continues
            LaUtils.debug.log("Failed to parse XML: top element could not be found!", "Warning")
            return False

        # Directly set attributes, mirroring C++ but with safe conversions
        self.guid = myTopElement.attribute("guid")
        
        # Parse name - check for both name and n tags for backward compatibility
        self._mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        if not self._mName:
            self._mName = LaUtils.xmlDecode(myTopElement.firstChildElement("n").text())
        
        self._mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        
        # Safe integer conversions with default values
        try:
            crop_yield_text = myTopElement.firstChildElement("cropYield").text()
            self._mCropYield = int(crop_yield_text) if crop_yield_text else 60
        except (ValueError, TypeError):
            self._mCropYield = 60
            
        try:
            calories_text = myTopElement.firstChildElement("cropCalories").text()
            self._mCalories = int(calories_text) if calories_text else 3000
        except (ValueError, TypeError):
            self._mCalories = 3000
            
        try:
            fodder_production_text = myTopElement.firstChildElement("fodderProduction").text()
            self._mFodderProduction = int(fodder_production_text) if fodder_production_text else 50
        except (ValueError, TypeError):
            self._mFodderProduction = 50
            
        try:
            fodder_calories_text = myTopElement.firstChildElement("fodderCalories").text()
            self._mFodderValue = int(fodder_calories_text) if fodder_calories_text else 1000
        except (ValueError, TypeError):
            self._mFodderValue = 1000

        # Parse cropFodderEnergyType using match-case with safe default
        myCropFodderEnergyType = myTopElement.firstChildElement("cropFodderEnergyType").text()
        if myCropFodderEnergyType == "KCalories":
            self._mFodderEnergyType = LaEnergyType.KCalories
        elif myCropFodderEnergyType == "TDN":
            self._mFodderEnergyType = LaEnergyType.TDN
        else:
            self._mFodderEnergyType = LaEnergyType.KCalories  # Default
        
        # Parse areaUnits using match-case with safe default
        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self._mAreaUnits = LaAreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self._mAreaUnits = LaAreaUnits.Hectare
        else:
            self._mAreaUnits = LaAreaUnits.Dunum  # Default
        
        self._mImageFile = myTopElement.firstChildElement("imageFile").text()
        
        # Log successful parsing
        LaUtils.debug.log(f"After fromXml - cropYield: {self._mCropYield}, cropFodderProduction: {self._mFodderProduction}")
        
        return True

    def fromXmlFile(self, filePath):
        """
        Load crop data from an XML file.

        :param filePath: Path to the XML file
        :type filePath: str
        :returns: True if successful, False otherwise
        :rtype: bool
        """
        try:
            # Open the file
            with open(filePath, 'r') as f:
                xmlContent = f.read()

            # Debug output for XML content
            LaUtils.debug.log(f"Loading crop from file: {filePath}")
            LaUtils.debug.log(f"XML content (first 200 chars): {xmlContent[:200]}...")

            # Parse the XML
            result = self.fromXml(xmlContent)

            # Debug output after parsing
            LaUtils.debug.log(f"After fromXml - cropYield: {self.cropYield}, cropFodderProduction: {self.cropFodderProduction}")

            return result
        except Exception as e:
            LaUtils.debug.log(f"Error in fromXmlFile for {filePath}: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())
            return False

    def toXml(self):
        """
        Convert this crop to an XML representation.

        :returns: XML string representing the crop's data
        :rtype: str
        """
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        # Build XML directly matching the existing structure
        xml = f'<crop guid="{self.guid}">\n'
        xml += f'  <name>{LaUtils.xmlEncode(self.name)}</name>\n' # type: ignore
        xml += f'  <description>{LaUtils.xmlEncode(self.description)}</description>\n' # type: ignore
        xml += f'  <cropYield>{self.cropYield}</cropYield>\n'
        xml += f'  <cropCalories>{self.cropCalories}</cropCalories>\n'
        xml += f'  <fodderProduction>{self.cropFodderProduction}</fodderProduction>\n'
        xml += f'  <fodderCalories>{self.cropFodderValue}</fodderCalories>\n'
        # Convert energy type enum to string using match-case
        match self._mFodderEnergyType:
            case LaEnergyType.KCalories: myCropFodderEnergyTypeString = "KCalories"
            case LaEnergyType.TDN: myCropFodderEnergyTypeString = "TDN"
        # Convert area units enum to string using match-case
        match self._mAreaUnits:
            case LaAreaUnits.Dunum: myAreaUnitsString = "Dunum"
            case LaAreaUnits.Hectare: myAreaUnitsString = "Hectare"
        xml += f'  <cropFodderEnergyType>{myCropFodderEnergyTypeString}</cropFodderEnergyType>\n'
        xml += f'  <areaUnits>{myAreaUnitsString}</areaUnits>\n'
        xml += f'  <imageFile>{LaUtils.xmlEncode(str(self.imageFile))}</imageFile>\n'
        xml += '</crop>\n'
        
        return xml

    def toText(self):
        """
        Convert this crop to a plain text representation.

        :returns: Text string representing the crop's data in key-value format
        :rtype: str
        """
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
        myString += "imageFile=>" + str(myImageFile) + "\n"
        return myString

    def toHtml(self):
        """
        Convert this crop to an HTML representation for display.

        :returns: HTML string representing the crop's data in a formatted table
        :rtype: str
        """
        from la.lib.lautils import LaUtils  # we import this here to avoid a circular import

        myCropFodderEnergyType = "KCalories" if self.cropFodderEnergyType == LaEnergyType.KCalories else "TDN"
        myUnits = "Dunum" if self.areaUnits == LaAreaUnits.Dunum else "Hectare"

        myString = "<h3>Details for " + LaUtils.xmlEncode(str(self.name)) + "</h3>"
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