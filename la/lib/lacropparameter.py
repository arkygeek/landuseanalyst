# lacropparameter.py
import warnings
from typing import Optional, Type, Dict
import os

from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument

from la.resources_rc import *

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType

class LaCropParameter(QObject, LaSerialisable, LaGuid):
    """
    A class representing the parameters for a crop.

    This class stores parameters related to a crop, such as its name, description,
    yield, calories, etc. It also provides methods to convert to and from XML.

    :ivar mName: The name of the crop parameter
    :type mName: str
    :ivar mDescription: The description of the crop parameter
    :type mDescription: str
    :ivar mCropGuid: The GUID of the crop this parameter is associated with
    :type mCropGuid: str
    :ivar mPercentTameCrop: The percentage of tame crop
    :type mPercentTameCrop: float
    :ivar mSpoilage: The spoilage percentage
    :type mSpoilage: float
    :ivar mReseed: The reseed percentage
    :type mReseed: float
    :ivar mCropRotation: Whether crop rotation is used
    :type mCropRotation: bool
    :ivar mFallowRatio: The fallow ratio
    :type mFallowRatio: float
    :ivar mFallowValue: The fallow value
    :type mFallowValue: int
    :ivar mAreaUnits: The area units used
    :type mAreaUnits: LaAreaUnits
    :ivar mUseCommonLand: Whether common land is used
    :type mUseCommonLand: bool
    :ivar mUseSpecificLand: Whether specific land is used
    :type mUseSpecificLand: bool
    :ivar mRasterName: The name of the raster
    :type mRasterName: str
    """
    # Signal declarations - ensure they match property types
    _nameChanged = pyqtSignal(str)
    _descriptionChanged = pyqtSignal(str)
    _guidChanged = pyqtSignal(str)
    _cropGuidChanged = pyqtSignal(str)
    _percentTameCropChanged = pyqtSignal(float)
    _spoilageChanged = pyqtSignal(float)
    _reseedChanged = pyqtSignal(float)
    _cropRotationChanged = pyqtSignal(bool)  # Changed to bool to match C++
    _fallowRatioChanged = pyqtSignal(float)
    _fallowEnergyTypeChanged = pyqtSignal(LaEnergyType)  # Changed to LaEnergyType to match C++
    _fallowValueChanged = pyqtSignal(int)    # Added missing signal declaration
    _areaUnitsChanged = pyqtSignal(object)   # Using object because LaAreaUnits is an enum
    _useCommonLandChanged = pyqtSignal(bool)
    _useSpecificLandChanged = pyqtSignal(bool)
    _rasterNameChanged = pyqtSignal(str)

    def __init__(self, theCropParameter: Optional['LaCropParameter'] = None, parent=None):
        """
        Initialize a new crop parameter object.

        :param theCropParameter: Optional crop parameter to copy from
        :type theCropParameter: Optional[LaCropParameter]
        :param parent: Parent QObject
        :type parent: QObject
        """
        super().__init__(parent)
        if theCropParameter is None:  # If NO crop parameter is provided, initialize with default values
            self.setGuid()
            self.mName = "No Name Set"
            self.mDescription = "Not Set"
            self.mCropGuid = ""
            self.mPercentTameCrop = 0.0
            self.mSpoilage = 10
            self.mReseed = 10
            self.mCropRotation = 0
            self.mFallowRatio = 0.0
            self.mFallowEnergyType = LaEnergyType.KCalories
            self.mFallowValue = 0
            self.mAreaUnits = LaAreaUnits.Dunum
            self.mUseCommonLand = 0
            self.mUseSpecificLand = 0
            self.mRasterName = ""
        else:  # If a crop parameter IS provided, copy the values from the existing parameter
            self.setGuid(theCropParameter.guid)  # Use setter method from LaGuid
            self.mName = theCropParameter.name
            self.mDescription = theCropParameter.description
            self.mCropGuid = theCropParameter.cropGuid
            self.mPercentTameCrop = theCropParameter.percentTameCrop
            self.mSpoilage = theCropParameter.spoilage
            self.mReseed = theCropParameter.reseed
            self.mCropRotation = theCropParameter.cropRotation
            self.mFallowRatio = theCropParameter.fallowRatio
            self.mFallowValue = theCropParameter.fallowValue
            self.mAreaUnits = theCropParameter.areaUnits
            self.mUseCommonLand = theCropParameter.useCommonLand
            self.mUseSpecificLand = theCropParameter.useSpecificLand
            self.mRasterName = theCropParameter.rasterName

    # Remove the conflicting property accessor methods
    # Define pyqtProperty using the property from the parent class
    @pyqtProperty(str, notify=_guidChanged)
    def guid(self) -> str:
        """Get the GUID of the crop parameter."""
        return super().guid

    # No setter needed since we'll use the setter from the parent class

    @pyqtProperty(str, notify=_nameChanged)
    def name(self) -> str: #type: ignore
        """Get the name of the crop parameter."""
        return str(self.mName)

    @name.setter
    def name(self, theName: str) -> None:
        """Set the name of the crop parameter."""
        if self.mName != theName:
            self.mName = theName
            self._nameChanged.emit(theName)

    @pyqtProperty(str, notify=_descriptionChanged)
    def description(self) -> str: #type: ignore
        """Get the description of the crop parameter."""
        return str(self.mDescription)

    @description.setter
    def description(self, theDescription: str) -> None:
        """Set the description of the crop parameter."""
        if self.mDescription != theDescription:
            self.mDescription = theDescription
            self._descriptionChanged.emit(theDescription)

    @pyqtProperty(str, notify=_cropGuidChanged)
    def cropGuid(self) -> str: #type: ignore
        """Get the crop GUID."""
        return str(self.mCropGuid)

    @cropGuid.setter
    def cropGuid(self, theCropGuid: str) -> None:
        """Set the crop GUID."""
        if self.mCropGuid != theCropGuid:
            self.mCropGuid = theCropGuid
            self._cropGuidChanged.emit(theCropGuid)

    @pyqtProperty(float, notify=_percentTameCropChanged)
    def percentTameCrop(self) -> float: #type: ignore
        """Get the percentage of tame crop."""
        return float(str(self.mPercentTameCrop))

    @percentTameCrop.setter
    def percentTameCrop(self, theValue: float) -> None:
        """Set the percentage of tame crop."""
        myFloatValue = float(theValue)
        if self.mPercentTameCrop != myFloatValue:
            self.mPercentTameCrop = myFloatValue
            self._percentTameCropChanged.emit(myFloatValue)

    @pyqtProperty(int, notify=_spoilageChanged)
    def spoilage(self) -> int: #type: ignore
        """Get the spoilage percentage."""
        try:
            if not self.mSpoilage and self.mSpoilage != 0:  # Check if empty or None
                return 0
            return int(str(self.mSpoilage))
        except (ValueError, TypeError):
            # Default to 0 if conversion fails
            return 0

    @spoilage.setter
    def spoilage(self, theValue: int) -> None:
        """Set the spoilage percentage."""
        myIntValue = int(theValue)
        if self.mSpoilage != myIntValue:
            self.mSpoilage = myIntValue
            self._spoilageChanged.emit(myIntValue)

    @pyqtProperty(int, notify=_reseedChanged)
    def reseed(self) -> int: #type: ignore
        """Get the reseed percentage."""
        try:
            if not self.mReseed and self.mReseed != 0:  # Check if empty or None
                return 0
            return int(str(self.mReseed))
        except (ValueError, TypeError):
            # Default to 0 if conversion fails
            return 0

    @reseed.setter
    def reseed(self, theValue: int) -> None:
        """Set the reseed percentage."""
        myIntValue = int(theValue)
        if self.mReseed != myIntValue:
            self.mReseed = myIntValue
            self._reseedChanged.emit(myIntValue)

    @pyqtProperty(bool, notify=_cropRotationChanged)
    def cropRotation(self) -> bool: #type: ignore
        """Get whether crop rotation is used."""
        return bool(self.mCropRotation)

    @cropRotation.setter
    def cropRotation(self, theValue: bool) -> None:
        """Set whether crop rotation is used."""
        bool_value = bool(theValue)
        if self.mCropRotation != bool_value:
            self.mCropRotation = bool_value
            self._cropRotationChanged.emit(bool_value)

    @pyqtProperty(float, notify=_fallowRatioChanged)
    def fallowRatio(self) -> float: #type: ignore
        """Get the fallow ratio."""
        return float(str(self.mFallowRatio))

    @fallowRatio.setter
    def fallowRatio(self, theValue: float) -> None:
        """Set the fallow ratio."""
        myFloatValue = float(theValue)
        if self.mFallowRatio != myFloatValue:
            self.mFallowRatio = myFloatValue
            self._fallowRatioChanged.emit(myFloatValue)

    @pyqtProperty(LaEnergyType, notify=_fallowEnergyTypeChanged)
    def fallowEnergyType(self) -> LaEnergyType: #type: ignore
        """Get the energy type for fallow."""
        return self.mFallowEnergyType

    @fallowEnergyType.setter
    def fallowEnergyType(self, theEnergyType: LaEnergyType) -> None:
        """Signal emitted when the fallow energy type changes."""
        if self.mFallowEnergyType != theEnergyType:
            self.mFallowEnergyType = theEnergyType
            self._fallowEnergyTypeChanged.emit(theEnergyType)

    @pyqtProperty(int, notify=_fallowValueChanged)
    def fallowValue(self) -> int: #type: ignore
        """Get the fallow value."""
        return int(str(self.mFallowValue))

    @fallowValue.setter
    def fallowValue(self, theValue: int) -> None:
        """Set the fallow value."""
        myIntValue = int(theValue)
        if self.mFallowValue != myIntValue:
            self.mFallowValue = myIntValue
            self._fallowValueChanged.emit(myIntValue)

    @pyqtProperty(LaAreaUnits, notify=_areaUnitsChanged)
    def areaUnits(self): #type: ignore
        """Get the area units used."""
        return self.mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnit: Optional[LaAreaUnits]) -> None:
        """Set the area units used."""
        # Provide a default if None is passed
        myCurrentAreaUnitValue = theAreaUnit if theAreaUnit is not None else LaAreaUnits.Dunum
        if self.mAreaUnits != myCurrentAreaUnitValue:
            self.mAreaUnits = myCurrentAreaUnitValue
            self._areaUnitsChanged.emit(myCurrentAreaUnitValue)

    @pyqtProperty(bool, notify=_useCommonLandChanged)
    def useCommonLand(self) -> bool: #type: ignore
        """Get whether common land is used."""
        return bool(self.mUseCommonLand)

    @useCommonLand.setter
    def useCommonLand(self, theValue: bool) -> None:
        """Set whether common land is used."""
        bool_value = bool(theValue)
        if self.mUseCommonLand != bool_value:
            self.mUseCommonLand = bool_value
            self._useCommonLandChanged.emit(bool_value)

    @pyqtProperty(bool, notify=_useSpecificLandChanged)
    def useSpecificLand(self) -> bool: #type: ignore
        """Get whether specific land is used."""
        return bool(self.mUseSpecificLand)

    @useSpecificLand.setter
    def useSpecificLand(self, theValue: bool) -> None:
        """Set whether specific land is used."""
        bool_value = bool(theValue)
        if self.mUseSpecificLand != bool_value:
            self.mUseSpecificLand = bool_value
            self._useSpecificLandChanged.emit(bool_value)

    @pyqtProperty(str, notify=_rasterNameChanged)
    def rasterName(self) -> str: #type: ignore
        """Get the name of the raster."""
        return str(self.mRasterName)

    @rasterName.setter
    def rasterName(self, theValue: str) -> None:
        """Set the name of the raster."""
        if self.mRasterName != theValue:
            self.mRasterName = theValue
            self._rasterNameChanged.emit(theValue)

    # File I/O methods

    def fromXmlFile(self, theFilePath: str) -> bool:
        """
        Load this crop parameter from an XML file.

        :param theFilePath: The path to the XML file
        :type theFilePath: str
        :return: True if loading was successful, False otherwise
        :rtype: bool
        """
        try:
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
        """
        Save this crop parameter to an XML file.

        :param theFilePath: The path to the XML file
        :type theFilePath: str
        :return: True if saving was successful, False otherwise
        :rtype: bool
        """
        try:
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
        """
        Convert this crop parameter to XML.

        :return: The XML representation of this crop parameter
        :rtype: str
        """
        from la.lib.lautils import LaUtils

        # Get the actual guid string using the property
        guid_str = str(self.guid)

        myString = f"<cropParameter guid=\"{guid_str}\">\n"
        myString += f"  <name>{LaUtils.xmlEncode(self.name)}</name>\n"  # Fix name tag, was using <n>
        myString += f"  <description>{LaUtils.xmlEncode(self.description)}</description>\n"
        myString += f"  <crop>{self.cropGuid}</crop>\n"
        myString += f"  <percentTameCrop>{self.percentTameCrop}</percentTameCrop>\n"
        myString += f"  <spoilage>{self.spoilage}</spoilage>\n"
        myString += f"  <reseed>{self.reseed}</reseed>\n"
        myString += f"  <cropRotation>{1 if self.cropRotation else 0}</cropRotation>\n"
        myString += f"  <fallowRatio>{self.fallowRatio}</fallowRatio>\n"
        myString += f"  <fallowValue>{self.fallowValue}</fallowValue>\n"
        # Access the underlying enum value directly from the instance variable
        myString += f"  <fallowEnergyType>{self.mFallowEnergyType.name}</fallowEnergyType>\n"
        myUnits = "Dunum" if self.mAreaUnits == LaAreaUnits.Dunum else "Hectare"
        myString += f"  <areaUnits>{myUnits}</areaUnits>\n"
        myString += f"  <useCommonLand>{1 if self.useCommonLand else 0}</useCommonLand>\n"
        myString += f"  <useSpecificLand>{1 if self.useSpecificLand else 0}</useSpecificLand>\n"
        myString += f"  <rasterName>{LaUtils.xmlEncode(self.rasterName)}</rasterName>\n"
        myString += "</cropParameter>\n"
        return myString

    def fromXml(self, theXml):
        """
        Parse XML and set this crop parameter's properties.

        :param theXml: The XML to parse
        :type theXml: str
        :return: True if parsing was successful, False otherwise
        :rtype: bool
        """
        from la.lib.lautils import LaUtils

        try:
            myDocument = QDomDocument("mydocument")
            myDocument.setContent(theXml)
            myTopElement = myDocument.firstChildElement("cropParameter")

            if myTopElement.isNull():
                warnings.warn("Failed to parse XML: myTopElement is null. The XML element could not be found or parsed.")
                return False

            # Use setGuid method from LaGuid instead of trying to assign to the property directly
            self._mGuid = myTopElement.attribute("guid")

            # Continue loading other parameters
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
            self.mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
            self.mCropGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("crop").text())
            # Parse numeric values without try-except blocks
            self.mPercentTameCrop = float(myTopElement.firstChildElement("percentTameCrop").text())
            self.mSpoilage = myTopElement.firstChildElement("spoilage").text()
            reseedText = myTopElement.firstChildElement("reseed").text()
            self.mReseed = int(reseedText) if reseedText else 0

            # Parse boolean and other values
            self.mCropRotation = myTopElement.firstChildElement("cropRotation").text()
            self.mFallowRatio = float(myTopElement.firstChildElement("fallowRatio").text())
            self.mFallowValue = int(myTopElement.firstChildElement("fallowValue").text())

            # Handle fallow energy type
            energyTypeElement = myTopElement.firstChildElement("fallowEnergyType")
            energyTypeText = energyTypeElement.text().strip()
            # Match the enum name exactly
            if energyTypeText == "TDN":
                self.mFallowEnergyType = LaEnergyType.TDN
            elif energyTypeText == "KCalories":
                self.mFallowEnergyType = LaEnergyType.KCalories
            else:
                print(f"Warning: Unknown energy type '{energyTypeText}', defaulting to KCalories")
                self.mFallowEnergyType = LaEnergyType.KCalories

            # Handle area units
            myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
            self.mAreaUnits = LaAreaUnits.Dunum if myAreaUnits == "Dunum" else LaAreaUnits.Hectare

            self.mUseCommonLand = myTopElement.firstChildElement("useCommonLand").text()
            self.mUseSpecificLand = myTopElement.firstChildElement("useSpecificLand").text()
            self.mRasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())

            return True
        except Exception as e:
            print(f"DEBUG: Error in fromXml: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return False

    def debug_info(self) -> str:
        """
        Get debug information about this crop parameter.

        :return: Debug information about this crop parameter
        :rtype: str
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

def on_toolNew_clicked(self):
    """Create a new crop parameter"""
    myCropParameter = LaCropParameter()
    myCropParameter.setGuid(None)  # Use setGuid instead of guid property setter.
    self.mCropParameter = myCropParameter
    self.showCropParameter()

