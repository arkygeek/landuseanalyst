# lacrop.py
# pyqtProperty is a decorator that is used to define Qt properties in Python.
# It is defined in a stub file that provides type hints
# for PyQt5 classes and methods. The actual implementation of the pyqtProperty
# decorator is in the PyQt5.QtCore module. The pyqtProperty decorator is used
# to define the properties of the LaCrop class, including name, description,
# cropType, plantingDate, harvestDate, and yieldValue.
import os
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
        mName (str): The name of the crop.
        mDescription (str): A description of the crop.
        mYield (int): The yield of the crop in kg/ha.
        mCropCalories (int): The number of calories produced by the crop.
        mFodderProduction (int): The amount of fodder produced by the crop.
        mFodderValue (int): The value of the fodder produced by the crop.
        mCropFodderEnergyType (str): The type of energy produced by the crop.
        mAreaUnits (str): The units used to measure the area of the crop.
        mImageFile (str): The image file used to represent the crop.
    """
    _nameChanged = pyqtSignal(str)
    _descriptionChanged = pyqtSignal(str)
    _yieldChanged = pyqtSignal(int)
    _cropCaloriesChanged = pyqtSignal(int)
    _cropFodderProductionChanged = pyqtSignal(int)
    _cropFodderValueChanged = pyqtSignal(int)
    _cropFodderEnergyTypeChanged = pyqtSignal(LaEnergyType)
    _areaUnitsChanged = pyqtSignal(LaAreaUnits)
    _imageFileChanged = pyqtSignal(str)

    def __init__(self, theCrop: Optional[Type['LaCrop']] = None, parent=None):
        """Initializes a new instance of the LaCrop class.

        Args:
            theCrop (Optional[Type['LaCrop']]): An existing LaCrop object to copy.
                If provided, the new instance will be a copy of the existing object.
                If not provided, the new instance will be initialized with default values.
        """
        super().__init__(parent)
        if theCrop is None: # If NO crop is provided, initialize with default values.
            LaGuid.setGuid(self, None)  # writes self._mGuid
            self.mName = "No Name Set"
            self.mDescription = "Not Set"
            self.mCropYield = 60
            self.mCalories = 3000
            self.mFodderProduction = 50
            self.mFodderValue = 1000
            self.mImageFile = ""
            self.mFodderEnergyType = ""
            self.mAreaUnits = ""
        else: # If a crop IS provided, copy the values from the existing crop.
            LaGuid.setGuid(self, theCrop.guid)  # writes self._mGuid
            self.mName = theCrop.name
            self.mDescription = theCrop.description
            self.mCropYield = theCrop.cropYield
            self.mCalories = theCrop.cropCalories
            self.mFodderProduction = theCrop.cropFodderProduction
            self.mFodderValue = theCrop.cropFodderValue
            self.mFodderEnergyType = theCrop.cropFodderEnergyType
            self.mAreaUnits = theCrop.areaUnits
            self.mImageFile = theCrop.imageFile

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
            'mName',              'mDescription',     '_mGuid',
            'mCropYield',         'mCalories',        'mFodderProduction',
            'mFodderValue',       'mFodderEnergyType', 'mAreaUnits',
            'mImageFile'
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

    @pyqtProperty(str, notify=_nameChanged)
    def name(self): #type: ignore
        """
        Get the name of this crop.

        :returns: The crop's name
        :rtype: str
        """
        return self.mName

    @name.setter
    def name(self, name):
        """
        Set the name of this crop.

        :param name: The new crop name
        :type name: str
        """
        if self.mName != name:
            self.mName = name
            self._nameChanged.emit(name)

    @pyqtProperty(str, notify=_descriptionChanged)
    def description(self): #type: ignore
        """
        Get the description of this crop.

        :returns: The crop's description
        :rtype: str
        """
        return self.mDescription

    @description.setter
    def description(self, description):
        """
        Set the description of this crop.

        :param description: The new crop description
        :type description: str
        """
        if self.mDescription != description:
            self.mDescription = description
            self._descriptionChanged.emit(description)

    @pyqtProperty(int, notify=_yieldChanged)
    def cropYield(self): #type: ignore
        """
        Get the yield value for this crop (kg/ha or kg/dunum).

        :returns: The crop's yield value
        :rtype: int
        """
        myCropYield = self.mCropYield
        return self.mCropYield

    @cropYield.setter
    def cropYield(self, theYield):
        """
        Set the yield value for this crop.

        :param theYield: The new yield value
        :type theYield: int
        """
        if self.mCropYield != theYield:
            self.mCropYield = theYield
            self._yieldChanged.emit(theYield)

    @pyqtProperty(int, notify=_cropCaloriesChanged)
    def cropCalories(self): #type: ignore
        """
        Get the caloric value per kg of this crop.

        :returns: The calories per kilogram
        :rtype: int
        """
        return self.mCalories

    @cropCalories.setter
    def cropCalories(self, cropCalories):
        """
        Set the caloric value per kg of this crop.

        :param cropCalories: The new caloric value
        :type cropCalories: int
        """
        if self.mCalories != cropCalories:
            self.mCalories = cropCalories
            self._cropCaloriesChanged.emit(cropCalories)

    @pyqtProperty(int, notify=_cropFodderProductionChanged)
    def cropFodderProduction(self): #type: ignore
        """
        Get the fodder production amount for this crop.

        :returns: The amount of fodder produced per area unit
        :rtype: int
        """
        return self.mFodderProduction

    @cropFodderProduction.setter
    def cropFodderProduction(self, theCropFodderProduction):
        """
        Set the fodder production amount for this crop.

        :param theCropFodderProduction: The new fodder production value
        :type theCropFodderProduction: int
        """
        if self.mFodderProduction != theCropFodderProduction:
            self.mFodderProduction = theCropFodderProduction
            self._cropFodderProductionChanged.emit(theCropFodderProduction)

    @pyqtProperty(int, notify=_cropFodderValueChanged)
    def cropFodderValue(self): #type: ignore
        """
        Get the nutritional value of fodder produced by this crop.

        :returns: The fodder's nutritional value
        :rtype: int
        """
        return self.mFodderValue

    @cropFodderValue.setter
    def cropFodderValue(self, cropFodderValue):
        """
        Set the nutritional value of fodder produced by this crop.

        :param cropFodderValue: The new fodder nutritional value
        :type cropFodderValue: int
        """
        if self.mFodderValue != cropFodderValue:
            self.mFodderValue = cropFodderValue
            self._cropFodderValueChanged.emit(cropFodderValue)

    @pyqtProperty(LaEnergyType, notify=_cropFodderEnergyTypeChanged)
    def cropFodderEnergyType(self): #type: ignore
        """
        Get the energy type for measuring fodder value (KCalories or TDN).

        :returns: The fodder energy measurement type
        :rtype: LaEnergyType
        """
        return self.mFodderEnergyType

    @cropFodderEnergyType.setter
    def cropFodderEnergyType(self, theCropFodderEnergyType):
        """
        Set the energy type for measuring fodder value.

        :param cropFodderEnergyType: The new fodder energy measurement type
        :type cropFodderEnergyType: LaEnergyType
        """
        if self.mFodderEnergyType != theCropFodderEnergyType:
            self.mFodderEnergyType = theCropFodderEnergyType
            self._cropFodderEnergyTypeChanged.emit(theCropFodderEnergyType)

    @pyqtProperty(LaAreaUnits, notify=_areaUnitsChanged)
    def areaUnits(self): #type: ignore
        """
        Get the area units used for this crop (Hectare or Dunum).

        :returns: The area units used for yield calculations
        :rtype: LaAreaUnits
        """
        return self.mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnits):
        """
        Set the area units used for this crop.

        :param theAreaUnits: The new area units
        :type theAreaUnits: LaAreaUnits
        """
        if self.mAreaUnits != theAreaUnits:
            self.mAreaUnits = theAreaUnits
            self._areaUnitsChanged.emit(theAreaUnits)

    @pyqtProperty(str, notify=_imageFileChanged)
    def imageFile(self): #type: ignore
        """
        Get the path to the image file representing this crop.

        :returns: The image file path
        :rtype: str
        """
        return self.mImageFile

    @imageFile.setter
    def imageFile(self, imageFile) -> None:
        """
        Set the path to the image file representing this crop.

        :param imageFile: The new image file path
        :type imageFile: str
        """
        if self.mImageFile != imageFile:
            self.mImageFile = imageFile
            self._imageFileChanged.emit(imageFile)

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
        self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        if not self.mName:
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("n").text())
        
        self.mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        
        # Safe integer conversions with default values
        try:
            crop_yield_text = myTopElement.firstChildElement("cropYield").text()
            self.mCropYield = int(crop_yield_text) if crop_yield_text else 60
        except (ValueError, TypeError):
            self.mCropYield = 60
            
        try:
            calories_text = myTopElement.firstChildElement("cropCalories").text()
            self.mCalories = int(calories_text) if calories_text else 3000
        except (ValueError, TypeError):
            self.mCalories = 3000
            
        try:
            fodder_production_text = myTopElement.firstChildElement("fodderProduction").text()
            self.mFodderProduction = int(fodder_production_text) if fodder_production_text else 50
        except (ValueError, TypeError):
            self.mFodderProduction = 50
            
        try:
            fodder_calories_text = myTopElement.firstChildElement("fodderCalories").text()
            self.mFodderValue = int(fodder_calories_text) if fodder_calories_text else 1000
        except (ValueError, TypeError):
            self.mFodderValue = 1000

        # Parse cropFodderEnergyType using match-case with safe default
        myCropFodderEnergyType = myTopElement.firstChildElement("cropFodderEnergyType").text()
        if myCropFodderEnergyType == "KCalories":
            self.mFodderEnergyType = LaEnergyType.KCalories
        elif myCropFodderEnergyType == "TDN":
            self.mFodderEnergyType = LaEnergyType.TDN
        else:
            self.mFodderEnergyType = LaEnergyType.KCalories  # Default
        
        # Parse areaUnits using match-case with safe default
        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self.mAreaUnits = LaAreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self.mAreaUnits = LaAreaUnits.Hectare
        else:
            self.mAreaUnits = LaAreaUnits.Dunum  # Default
        
        # Image - Store the full image path correctly with dynamic resolution
        image_file_text = LaUtils.xmlDecode(myTopElement.firstChildElement("imageFile").text())
        if image_file_text and os.path.exists(image_file_text):
            self.mImageFile = image_file_text
        else:
            images_dir = LaUtils.userImagesDirPath()
            basename = os.path.basename(image_file_text) if image_file_text else ""
            possible_path = os.path.join(images_dir, basename) if basename else ""
            if basename and os.path.exists(possible_path):
                self.mImageFile = possible_path
            else:
                self.mImageFile = basename
        
        # Log successful parsing
        LaUtils.debug.log(f"After fromXml - cropYield: {self.mCropYield}, cropFodderProduction: {self.mFodderProduction}")
        
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
        myCropFodderEnergyTypeString = "KCalories"
        match self.mFodderEnergyType:
            case LaEnergyType.KCalories: myCropFodderEnergyTypeString = "KCalories"
            case LaEnergyType.TDN: myCropFodderEnergyTypeString = "TDN"
            case "KCalories" | "TDN" as val: myCropFodderEnergyTypeString = val
        # Convert area units enum to string using match-case
        myAreaUnitsString = "Hectare"
        match self.mAreaUnits:
            case LaAreaUnits.Dunum: myAreaUnitsString = "Dunum"
            case LaAreaUnits.Hectare: myAreaUnitsString = "Hectare"
            case "Dunum" | "Hectare" as val: myAreaUnitsString = val
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