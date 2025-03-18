# lacropparameter.py
import warnings
from typing import Optional, Type, Dict
import os

from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument

from la.resources_rc import *

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import LaTripleMap, LaRasterInfo, LaFoodSourceMap, HerdSize, LaReportMap
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType

class LaCropParameter(QObject, LaSerialisable, LaGuid):
    """A class representing the parameters for a crop.

    This class stores parameters related to a crop, such as its name, description,
    yield, calories, etc. It also provides methods to convert to and from XML.

    Attributes:
        name (str): The name of the crop parameter.
        description (str): The description of the crop parameter.
        cropGuid (str): The GUID of the crop this parameter is associated with.
        percentTameCrop (float): The percentage of tame crop.
        spoilage (float): The spoilage percentage.
        reseed (float): The reseed percentage.
        cropRotation (bool): Whether crop rotation is used.
        fallowRatio (float): The fallow ratio.
        fallowValue (int): The fallow value.
        areaUnits (AreaUnits): The area units used.
        useCommonLand (bool): Whether common land is used.
        useSpecificLand (bool): Whether specific land is used.
        rasterName (str): The name of the raster.
    """
    # Signal declarations - ensure they match property types
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    guidChanged = pyqtSignal(str)
    cropGuidChanged = pyqtSignal(str)
    percentTameCropChanged = pyqtSignal(float)
    spoilageChanged = pyqtSignal(float)
    reseedChanged = pyqtSignal(float)
    cropRotationChanged = pyqtSignal(bool)  # Changed to bool to match C++
    fallowRatioChanged = pyqtSignal(float)
    fallowValueChanged = pyqtSignal(int)    # Changed to int to match C++
    areaUnitsChanged = pyqtSignal(object)   # Using object because LaAreaUnits is an enum
    useCommonLandChanged = pyqtSignal(bool)
    useSpecificLandChanged = pyqtSignal(bool)
    rasterNameChanged = pyqtSignal(str)

    def __init__(self, theCropParameter: Optional['LaCropParameter'] = None):
        """
        Initialize a new crop parameter object.

        Args:
            theCropParameter: Optional crop parameter to copy from.
        """
        super().__init__()
        if theCropParameter is None:
            self._guid = LaGuid()
            self._name = "No Name Set"
            self._description = "Not Set"
            self._cropGuid = ""
            self._percentTameCrop = 0.0
            self._spoilage = 0.0
            self._reseed = 0.0
            self._cropRotation = False  # Changed to False (bool) to match C++
            self._fallowRatio = 0.0
            self._fallowValue = 0
            self._areaUnits = LaAreaUnits.Dunum
            self._useCommonLand = False
            self._useSpecificLand = False
            self._rasterName = ""
        else:
            self._name = theCropParameter.name
            self._description = theCropParameter.description
            self._guid = theCropParameter.guid
            self._cropGuid = theCropParameter.cropGuid
            self._percentTameCrop = theCropParameter.percentTameCrop
            self._spoilage = theCropParameter.spoilage
            self._reseed = theCropParameter.reseed
            self._cropRotation = theCropParameter.cropRotation
            self._fallowRatio = theCropParameter.fallowRatio
            self._fallowValue = theCropParameter.fallowValue
            self._areaUnits = theCropParameter.areaUnits
            self._useCommonLand = theCropParameter.useCommonLand
            self._useSpecificLand = theCropParameter.useSpecificLand
            self._rasterName = theCropParameter.rasterName

    # Standard properties with correct types

    @pyqtProperty(str, notify=nameChanged)
    def name(self):  # type: ignore
        return self._name

    @name.setter
    def name(self, theName):
        if self._name != theName:
            self._name = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self): # type: ignore
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self): # type: ignore
        return self._guid

    @guid.setter
    def guid(self, guid):
        if self._guid != guid:
            self._guid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self): # type: ignore
        return self._cropGuid

    @cropGuid.setter
    def cropGuid(self, cropGuid):
        if self._cropGuid != cropGuid:
            self._cropGuid = cropGuid
            self.cropGuidChanged.emit(cropGuid)

    @pyqtProperty(float, notify=percentTameCropChanged)
    def percentTameCrop(self): # type: ignore
        """Get the percentage of tame crop.

        Returns:
            float: The percentage of tame crop.
        """
        # Ensure we return a float, matching C++ behavior
        try:
            return float(self._percentTameCrop)
        except (ValueError, TypeError):
            # Log and return default if conversion fails
            print(f"Warning: Invalid percentTameCrop value: {self._percentTameCrop}, using 0.0")
            return 0.0

    @percentTameCrop.setter
    def percentTameCrop(self, value):
        """Set the percentage of tame crop.

        Args:
            value: The new percentage of tame crop.
        """
        try:
            float_value = float(value)
            if self._percentTameCrop != float_value:
                self._percentTameCrop = float_value
                self.percentTameCropChanged.emit(float_value)
        except (ValueError, TypeError):
            # Log error but don't crash
            print(f"Warning: Failed to convert percentTameCrop value to float: {value}")
            self._percentTameCrop = 0.0
            self.percentTameCropChanged.emit(0.0)

    @pyqtProperty(float, notify=spoilageChanged)
    def spoilage(self):
        """Get the spoilage percentage.

        Returns:
            float: The spoilage percentage.
        """
        try:
            return float(self._spoilage)
        except (ValueError, TypeError):
            return 0.0

    @spoilage.setter
    def spoilage(self, value):
        """Set the spoilage percentage.

        Args:
            value: The new spoilage percentage.
        """
        try:
            float_value = float(value)
            if self._spoilage != float_value:
                self._spoilage = float_value
                self.spoilageChanged.emit(float_value)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert spoilage value to float: {value}")
            self._spoilage = 0.0
            self.spoilageChanged.emit(0.0)

    @pyqtProperty(float, notify=reseedChanged)
    def reseed(self):
        """Get the reseed percentage.

        Returns:
            float: The reseed percentage.
        """
        try:
            return float(self._reseed)
        except (ValueError, TypeError):
            return 0.0

    @reseed.setter
    def reseed(self, value):
        """Set the reseed percentage.

        Args:
            value: The new reseed percentage.
        """
        try:
            float_value = float(value)
            if self._reseed != float_value:
                self._reseed = float_value
                self.reseedChanged.emit(float_value)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert reseed value to float: {value}")
            self._reseed = 0.0
            self.reseedChanged.emit(0.0)

    @pyqtProperty(bool, notify=cropRotationChanged)
    def cropRotation(self):
        """Get whether crop rotation is used.

        Returns:
            bool: Whether crop rotation is used.
        """
        # In C++, this is a bool
        return bool(self._cropRotation)

    @cropRotation.setter
    def cropRotation(self, value):
        """Set whether crop rotation is used.

        Args:
            value: The new value for whether crop rotation is used.
        """
        bool_value = bool(value)
        if self._cropRotation != bool_value:
            self._cropRotation = bool_value
            self.cropRotationChanged.emit(bool_value)

    @pyqtProperty(float, notify=fallowRatioChanged)
    def fallowRatio(self):
        """Get the fallow ratio.

        Returns:
            float: The fallow ratio.
        """
        try:
            return float(self._fallowRatio)
        except (ValueError, TypeError):
            return 0.0

    @fallowRatio.setter
    def fallowRatio(self, value):
        """Set the fallow ratio.

        Args:
            value: The new fallow ratio.
        """
        try:
            float_value = float(value)
            if self._fallowRatio != float_value:
                self._fallowRatio = float_value
                self.fallowRatioChanged.emit(float_value)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowRatio value to float: {value}")
            self._fallowRatio = 0.0
            self.fallowRatioChanged.emit(0.0)

    @pyqtProperty(int, notify=fallowValueChanged)
    def fallowValue(self):
        """Get the fallow value.

        Returns:
            int: The fallow value.
        """
        # In C++, this is an int
        try:
            return int(self._fallowValue)
        except (ValueError, TypeError):
            return 0

    @fallowValue.setter
    def fallowValue(self, value):
        """Set the fallow value.

        Args:
            value: The new fallow value.
        """
        try:
            int_value = int(value)
            if self._fallowValue != int_value:
                self._fallowValue = int_value
                self.fallowValueChanged.emit(int_value)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowValue to int: {value}")
            self._fallowValue = 0
            self.fallowValueChanged.emit(0)

    @pyqtProperty(object, notify=areaUnitsChanged)
    def areaUnits(self):
        """Get the area units.

        Returns:
            LaAreaUnits: The area units.
        """
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, value):
        """Set the area units.

        Args:
            value: The new area units.
        """
        if self._areaUnits != value:
            self._areaUnits = value
            self.areaUnitsChanged.emit(value)

    @pyqtProperty(bool, notify=useCommonLandChanged)
    def useCommonLand(self):
        """Get whether common land is used.

        Returns:
            bool: Whether common land is used.
        """
        return bool(self._useCommonLand)

    @useCommonLand.setter
    def useCommonLand(self, value):
        """Set whether common land is used.

        Args:
            value: The new value for whether common land is used.
        """
        bool_value = bool(value)
        if self._useCommonLand != bool_value:
            self._useCommonLand = bool_value
            self.useCommonLandChanged.emit(bool_value)

    @pyqtProperty(bool, notify=useSpecificLandChanged)
    def useSpecificLand(self):
        """Get whether specific land is used.

        Returns:
            bool: Whether specific land is used.
        """
        return bool(self._useSpecificLand)

    @useSpecificLand.setter
    def useSpecificLand(self, value):
        """Set whether specific land is used.

        Args:
            value: The new value for whether specific land is used.
        """
        bool_value = bool(value)
        if self._useSpecificLand != bool_value:
            self._useSpecificLand = bool_value
            self.useSpecificLandChanged.emit(bool_value)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self):
        """Get the name of the raster.

        Returns:
            str: The name of the raster.
        """
        return self._rasterName

    @rasterName.setter
    def rasterName(self, value):
        """Set the name of the raster.

        Args:
            value: The new name of the raster.
        """
        if self._rasterName != value:
            self._rasterName = value
            self.rasterNameChanged.emit(value)

    # File I/O methods

    def fromXmlFile(self, theFilePath: str) -> bool:
        """Load this crop parameter from an XML file.

        Args:
            theFilePath: The path to the XML file.

        Returns:
            bool: True if loading was successful, False otherwise.
        """
        try:
            # Check if file exists before attempting to read
            if not os.path.exists(theFilePath):
                print(f"Error: File does not exist: {theFilePath}")
                return False

            with open(theFilePath, 'r') as myFile:
                myXmlContent = myFile.read()
                return self.fromXml(myXmlContent)
        except Exception as e:
            print(f"Error loading crop parameter from XML file: {e}")
            return False

    def toXmlFile(self, theFilePath: str) -> bool:
        """Save this crop parameter to an XML file.

        Args:
            theFilePath: The path to the XML file.

        Returns:
            bool: True if saving was successful, False otherwise.
        """
        try:
            # Ensure directory exists
            directory = os.path.dirname(theFilePath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            myXmlContent = self.toXml()
            with open(theFilePath, 'w') as myFile:
                myFile.write(myXmlContent)
            return True
        except Exception as e:
            print(f"Error saving crop parameter to XML file: {e}")
            return False

    def toXml(self) -> str:
        """Convert this crop parameter to XML.

        Returns:
            str: The XML representation of this crop parameter.
        """
        from la.lib.lautils import LaUtils

        # Using the exact same format as the C++ version
        myString = f"<cropParameter guid=\"{self.guid}\">\n"
        myString += f"  <name>{LaUtils.xmlEncode(self.name)}</name>\n"
        myString += f"  <description>{LaUtils.xmlEncode(self.description)}</description>\n"
        myString += f"  <crop>{LaUtils.xmlEncode(self.cropGuid)}</crop>\n"

        # Format numeric values carefully
        myString += f"  <percentTameCrop>{self.percentTameCrop}</percentTameCrop>\n"
        myString += f"  <spoilage>{self.spoilage}</spoilage>\n"
        myString += f"  <reseed>{self.reseed}</reseed>\n"

        # Store boolean as 1/0 like in the C++ version
        myString += f"  <cropRotation>{1 if self.cropRotation else 0}</cropRotation>\n"
        myString += f"  <fallowRatio>{self.fallowRatio}</fallowRatio>\n"
        myString += f"  <fallowValue>{self.fallowValue}</fallowValue>\n"

        # Format enum values as strings
        myUnits = "Dunum" if self._areaUnits == LaAreaUnits.Dunum else "Hectare"
        myString += f"  <areaUnits>{myUnits}</areaUnits>\n"

        # Store booleans as 1/0
        myString += f"  <useCommonLand>{1 if self._useCommonLand else 0}</useCommonLand>\n"
        myString += f"  <useSpecificLand>{1 if self._useSpecificLand else 0}</useSpecificLand>\n"

        myString += f"  <rasterName>{LaUtils.xmlEncode(self._rasterName)}</rasterName>\n"
        myString += "</cropParameter>\n"
        return myString

    def fromXml(self, theXml: str) -> bool:
        """Parse XML and set this crop parameter's properties.

        Args:
            theXml: The XML to parse.

        Returns:
            bool: True if parsing was successful, False otherwise.
        """
        from la.lib.lautils import LaUtils

        # Log entry point for debugging
        print(f"Parsing XML into crop parameter: length={len(theXml)}")

        # Set up XML document
        myDocument = QDomDocument("mydocument")
        if not myDocument.setContent(theXml):
            warnings.warn(f"Failed to parse XML content")
            return False

        myTopElement = myDocument.firstChildElement("cropParameter")
        if myTopElement.isNull():
            warnings.warn("Failed to parse XML: myTopElement is null")
            return False

        # Set guid attribute
        self.setGuid(myTopElement.attribute("guid"))

        # Parse all the child elements
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        self.cropGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("crop").text())

        # Parse percentTameCrop with proper error handling
        percentTameCropText = myTopElement.firstChildElement("percentTameCrop").text()
        try:
            self.percentTameCrop = float(percentTameCropText) if percentTameCropText else 0.0
        except ValueError:
            print(f"Warning: Could not convert percentTameCrop value '{percentTameCropText}' to float, using 0.0")
            self.percentTameCrop = 0.0

        # Parse spoilage with proper error handling
        spoilageText = myTopElement.firstChildElement("spoilage").text()
        try:
            self.spoilage = float(spoilageText) if spoilageText else 0.0
        except ValueError:
            print(f"Warning: Could not convert spoilage value '{spoilageText}' to float, using 0.0")
            self.spoilage = 0.0

        # Parse reseed with proper error handling
        reseedText = myTopElement.firstChildElement("reseed").text()
        try:
            self.reseed = float(reseedText) if reseedText else 0.0
        except ValueError:
            print(f"Warning: Could not convert reseed value '{reseedText}' to float, using 0.0")
            self.reseed = 0.0

        # Parse cropRotation as a boolean (stored as 0/1 in XML)
        cropRotationText = myTopElement.firstChildElement("cropRotation").text()
        try:
            self.cropRotation = bool(int(cropRotationText)) if cropRotationText else False
        except ValueError:
            print(f"Warning: Could not convert cropRotation value '{cropRotationText}' to bool, using False")
            self.cropRotation = False

        # Parse fallowRatio with proper error handling
        fallowRatioText = myTopElement.firstChildElement("fallowRatio").text()
        try:
            self.fallowRatio = float(fallowRatioText) if fallowRatioText else 0.0
        except ValueError:
            print(f"Warning: Could not convert fallowRatio value '{fallowRatioText}' to float, using 0.0")
            self.fallowRatio = 0.0

        # Parse fallowValue as integer
        fallowValueText = myTopElement.firstChildElement("fallowValue").text()
        try:
            self.fallowValue = int(fallowValueText) if fallowValueText else 0
        except ValueError:
            print(f"Warning: Could not convert fallowValue value '{fallowValueText}' to int, using 0")
            self.fallowValue = 0

        # Parse areaUnits as enum
        areaUnitsText = myTopElement.firstChildElement("areaUnits").text()
        if areaUnitsText == "Dunum":
            self.areaUnits = LaAreaUnits.Dunum
        elif areaUnitsText == "Hectare":
            self.areaUnits = LaAreaUnits.Hectare
        else:
            # Default to Dunum if unrecognized
            print(f"Warning: Unrecognized areaUnits value '{areaUnitsText}', using Dunum")
            self.areaUnits = LaAreaUnits.Dunum

        # Parse useCommonLand as boolean (stored as 0/1 in XML)
        useCommonLandText = myTopElement.firstChildElement("useCommonLand").text()
        try:
            self.useCommonLand = bool(int(useCommonLandText)) if useCommonLandText else False
        except ValueError:
            print(f"Warning: Could not convert useCommonLand value '{useCommonLandText}' to bool, using False")
            self.useCommonLand = False

        # Parse useSpecificLand as boolean (stored as 0/1 in XML)
        useSpecificLandText = myTopElement.firstChildElement("useSpecificLand").text()
        try:
            self.useSpecificLand = bool(int(useSpecificLandText)) if useSpecificLandText else False
        except ValueError:
            print(f"Warning: Could not convert useSpecificLand value '{useSpecificLandText}' to bool, using False")
            self.useSpecificLand = False

        # Parse rasterName
        self.rasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())

        print(f"Successfully parsed crop parameter: {self.name}")
        return True

    def debug_info(self) -> str:
        """Get debug information about this crop parameter.

        Returns:
            str: Debug information about this crop parameter.
        """
        info = f"LaCropParameter '{self.name}' (guid={self.guid})\n"
        info += f"  description: {self.description}\n"
        info += f"  cropGuid: {self.cropGuid}\n"
        info += f"  percentTameCrop: {self.percentTameCrop} (type: {type(self.percentTameCrop)})\n"
        info += f"  spoilage: {self.spoilage} (type: {type(self.spoilage)})\n"
        info += f"  reseed: {self.reseed} (type: {type(self.reseed)})\n"
        info += f"  cropRotation: {self.cropRotation} (type: {type(self.cropRotation)})\n"
        info += f"  fallowRatio: {self.fallowRatio} (type: {type(self.fallowRatio)})\n"
        info += f"  fallowValue: {self.fallowValue} (type: {type(self.fallowValue)})\n"
        info += f"  areaUnits: {self.areaUnits} (type: {type(self.areaUnits)})\n"
        info += f"  useCommonLand: {self.useCommonLand} (type: {type(self.useCommonLand)})\n"
        info += f"  useSpecificLand: {self.useSpecificLand} (type: {type(self.useSpecificLand)})\n"
        info += f"  rasterName: {self.rasterName} (type: {type(self.rasterName)})\n"
        return info
