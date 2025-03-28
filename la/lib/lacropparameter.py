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
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    guidChanged = pyqtSignal(str)
    cropGuidChanged = pyqtSignal(str)
    percentTameCropChanged = pyqtSignal(float)
    spoilageChanged = pyqtSignal(float)
    reseedChanged = pyqtSignal(float)
    cropRotationChanged = pyqtSignal(bool)  # Changed to bool to match C++
    fallowRatioChanged = pyqtSignal(float)
    fallowEnergyTypeChanged = pyqtSignal(LaEnergyType)  # Changed to LaEnergyType to match C++
    fallowValueChanged = pyqtSignal(int)    # Added missing signal declaration
    areaUnitsChanged = pyqtSignal(object)   # Using object because LaAreaUnits is an enum
    useCommonLandChanged = pyqtSignal(bool)
    useSpecificLandChanged = pyqtSignal(bool)
    rasterNameChanged = pyqtSignal(str)

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
            self._mGuid = LaGuid.setGuid(self, None)  # Call with self as first parameter like in lacrop.py
            self._mName = "No Name Set"
            self._mDescription = "Not Set"
            self._mCropGuid = ""
            self._mPercentTameCrop = 0.0
            self._mSpoilage = 0
            self._mReseed = 0
            self._mCropRotation = False
            self._mFallowRatio = 0.0
            self._mFallowEnergyType = LaEnergyType.KCalories
            self._mFallowValue = 0
            self._mAreaUnits = LaAreaUnits.Dunum
            self._mUseCommonLand = False
            self._mUseSpecificLand = False
            self._mRasterName = ""
        else:  # If a crop parameter IS provided, copy the values from the existing parameter
            self._mGuid = theCropParameter.guid  # Use setter method from LaGuid
            self._mName = theCropParameter.name
            self._mDescription = theCropParameter.description
            self._mCropGuid = theCropParameter.cropGuid
            self._mPercentTameCrop = theCropParameter.percentTameCrop
            self._mSpoilage = theCropParameter.spoilage
            self._mReseed = theCropParameter.reseed
            self._mCropRotation = theCropParameter.cropRotation
            self._mFallowRatio = theCropParameter.fallowRatio
            self._mFallowValue = theCropParameter.fallowValue
            self._mAreaUnits = theCropParameter.areaUnits
            self._mUseCommonLand = theCropParameter.useCommonLand
            self._mUseSpecificLand = theCropParameter.useSpecificLand
            self._mRasterName = theCropParameter.rasterName

    # Remove the conflicting property accessor methods
    # @property
    # def guid(self):
    #    """Get the GUID (Globally Unique Identifier) of this crop."""
    #    return self._guid
    #
    # @guid.setter
    # def guid(self, theGuid):
    #    """Set the GUID (Globally Unique Identifier) for this crop parameter."""
    #    self.mGuid = theGuid

    # Use only the PyQt property that calls the LaGuid parent class method
    @pyqtProperty(str, notify=guidChanged)
    def guid(self) -> str:
        """Get the GUID of the crop parameter."""
        # Call the inherited method from LaGuid and ensure we always return a string
        result = super().guid()
        return result if result is not None else ""

    @pyqtProperty(str, notify=nameChanged)
    def name(self) -> str: #type: ignore
        """Get the name of the crop parameter."""
        return str(self._mName)

    @name.setter
    def name(self, theName: str) -> None:
        """Set the name of the crop parameter."""
        if self._mName != theName:
            self._mName = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: #type: ignore
        """Get the description of the crop parameter."""
        return str(self._mDescription)

    @description.setter
    def description(self, theDescription: str) -> None:
        """Set the description of the crop parameter."""
        if self._mDescription != theDescription:
            self._mDescription = theDescription
            self.descriptionChanged.emit(theDescription)

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self) -> str: #type: ignore
        """Get the crop GUID."""
        return str(self._mCropGuid)

    @cropGuid.setter
    def cropGuid(self, theCropGuid: str) -> None:
        """Set the crop GUID."""
        if self._mCropGuid != theCropGuid:
            self._mCropGuid = theCropGuid
            self.cropGuidChanged.emit(theCropGuid)

    @pyqtProperty(float, notify=percentTameCropChanged)
    def percentTameCrop(self) -> float: #type: ignore
        """Get the percentage of tame crop."""
        return float(str(self._mPercentTameCrop))

    @percentTameCrop.setter
    def percentTameCrop(self, theValue: float) -> None:
        """Set the percentage of tame crop."""
        try:
            myFloatValue = float(theValue)
            if self._mPercentTameCrop != myFloatValue:
                self._mPercentTameCrop = myFloatValue
                self.percentTameCropChanged.emit(myFloatValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert percentTameCrop value to float: {theValue}")
            self._mPercentTameCrop = 0.0
            self.percentTameCropChanged.emit(0.0)

    @pyqtProperty(int, notify=spoilageChanged)
    def spoilage(self) -> int: #type: ignore
        """Get the spoilage percentage."""
        try:
            if not self._mSpoilage and self._mSpoilage != 0:  # Check if empty or None
                return 0
            return int(str(self._mSpoilage))
        except (ValueError, TypeError):
            # Default to 0 if conversion fails
            return 0

    @spoilage.setter
    def spoilage(self, theValue: int) -> None:
        """Set the spoilage percentage."""
        try:
            myIntValue = int(theValue)
            if self._mSpoilage != myIntValue:
                self._mSpoilage = myIntValue
                self.spoilageChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert spoilage value to int: {theValue}")
            self._mSpoilage = 0
            self.spoilageChanged.emit(0)

    @pyqtProperty(int, notify=reseedChanged)
    def reseed(self) -> int: #type: ignore
        """Get the reseed percentage."""
        try:
            if not self._mReseed and self._mReseed != 0:  # Check if empty or None
                return 0
            return int(str(self._mReseed))
        except (ValueError, TypeError):
            # Default to 0 if conversion fails
            return 0

    @reseed.setter
    def reseed(self, theValue: int) -> None:
        """Set the reseed percentage."""
        try:
            myIntValue = int(theValue)
            if self._mReseed != myIntValue:
                self._mReseed = myIntValue
                self.reseedChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert reseed value to int: {theValue}")
            self._mReseed = 0
            self.reseedChanged.emit(0)

    @pyqtProperty(bool, notify=cropRotationChanged)
    def cropRotation(self) -> bool: #type: ignore
        """Get whether crop rotation is used."""
        return bool(self._mCropRotation)

    @cropRotation.setter
    def cropRotation(self, theValue: bool) -> None:
        """Set whether crop rotation is used."""
        bool_value = bool(theValue)
        if self._mCropRotation != bool_value:
            self._mCropRotation = bool_value
            self.cropRotationChanged.emit(bool_value)

    @pyqtProperty(float, notify=fallowRatioChanged)
    def fallowRatio(self) -> float: #type: ignore
        """Get the fallow ratio."""
        return float(str(self._mFallowRatio))

    @fallowRatio.setter
    def fallowRatio(self, theValue: float) -> None:
        """Set the fallow ratio."""
        try:
            myFloatValue = float(theValue)
            if self._mFallowRatio != myFloatValue:
                self._mFallowRatio = myFloatValue
                self.fallowRatioChanged.emit(myFloatValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowRatio value to float: {theValue}")
            self._mFallowRatio = 0.0
            self.fallowRatioChanged.emit(0.0)

    @pyqtProperty(LaEnergyType, notify=fallowEnergyTypeChanged)
    def fallowEnergyType(self) -> LaEnergyType: #type: ignore
        """Get the energy type for fallow."""
        return self._mFallowEnergyType

    @fallowEnergyType.setter
    def fallowEnergyType(self, theEnergyType: LaEnergyType) -> None:
        """Signal emitted when the fallow energy type changes."""
        if self._mFallowEnergyType != theEnergyType:
            self._mFallowEnergyType = theEnergyType
            self.fallowEnergyTypeChanged.emit(theEnergyType)

    @pyqtProperty(int, notify=fallowValueChanged)
    def fallowValue(self) -> int: #type: ignore
        """Get the fallow value."""
        return int(str(self._mFallowValue))

    @fallowValue.setter
    def fallowValue(self, theValue: int) -> None:
        """Set the fallow value."""
        try:
            myIntValue = int(theValue)
            if self._mFallowValue != myIntValue:
                self._mFallowValue = myIntValue
                self.fallowValueChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowValue to int: {theValue}")
            self._mFallowValue = 0
            self.fallowValueChanged.emit(0)

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self): #type: ignore
        """Get the area units used."""
        return self._mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnit: Optional[LaAreaUnits]) -> None:
        """Set the area units used."""
        # Provide a default if None is passed
        myCurrentAreaUnitValue = theAreaUnit if theAreaUnit is not None else LaAreaUnits.Dunum
        if self._mAreaUnits != myCurrentAreaUnitValue:
            self._mAreaUnits = myCurrentAreaUnitValue
            self.areaUnitsChanged.emit(myCurrentAreaUnitValue)

    @pyqtProperty(bool, notify=useCommonLandChanged)
    def useCommonLand(self) -> bool: #type: ignore
        """Get whether common land is used."""
        return bool(self._mUseCommonLand)

    @useCommonLand.setter
    def useCommonLand(self, theValue: bool) -> None:
        """Set whether common land is used."""
        bool_value = bool(theValue)
        if self._mUseCommonLand != bool_value:
            self._mUseCommonLand = bool_value
            self.useCommonLandChanged.emit(bool_value)

    @pyqtProperty(bool, notify=useSpecificLandChanged)
    def useSpecificLand(self) -> bool: #type: ignore
        """Get whether specific land is used."""
        return bool(self._mUseSpecificLand)

    @useSpecificLand.setter
    def useSpecificLand(self, theValue: bool) -> None:
        """Set whether specific land is used."""
        bool_value = bool(theValue)
        if self._mUseSpecificLand != bool_value:
            self._mUseSpecificLand = bool_value
            self.useSpecificLandChanged.emit(bool_value)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self) -> str: #type: ignore
        """Get the name of the raster."""
        return str(self._mRasterName)

    @rasterName.setter
    def rasterName(self, theValue: str) -> None:
        """Set the name of the raster."""
        if self._mRasterName != theValue:
            self._mRasterName = theValue
            self.rasterNameChanged.emit(theValue)

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
        myString = f"<cropParameter guid=\"{self.guid}\">\n"
        myString += f"  <name>{self.name}</name>\n"
        myString += f"  <description>{self.description}</description>\n"
        myString += f"  <crop>{self.cropGuid}</crop>\n"
        myString += f"  <percentTameCrop>{self.percentTameCrop}</percentTameCrop>\n"
        myString += f"  <spoilage>{self.spoilage}</spoilage>\n"
        myString += f"  <reseed>{self.reseed}</reseed>\n"
        myString += f"  <cropRotation>{1 if self.cropRotation else 0}</cropRotation>\n"
        myString += f"  <fallowRatio>{self.fallowRatio}</fallowRatio>\n"
        myString += f"  <fallowValue>{self.fallowValue}</fallowValue>\n"
        # Access the underlying enum value directly from the instance variable
        myString += f"  <fallowEnergyType>{self._mFallowEnergyType.name}</fallowEnergyType>\n"
        myUnits = "Dunum" if self._mAreaUnits == LaAreaUnits.Dunum else "Hectare"
        myString += f"  <areaUnits>{myUnits}</areaUnits>\n"
        myString += f"  <useCommonLand>{1 if self.useCommonLand else 0}</useCommonLand>\n"
        myString += f"  <useSpecificLand>{1 if self.useSpecificLand else 0}</useSpecificLand>\n"
        myString += f"  <rasterName>{self.rasterName}</rasterName>\n"
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
            self.setGuid(myTopElement.attribute("guid"))

            # Continue loading other parameters
            self._mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
            self._mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
            self._mCropGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("crop").text())

            # Parse numeric values with proper conversion
            try:
                self._mPercentTameCrop = float(myTopElement.firstChildElement("percentTameCrop").text())
            except (ValueError, TypeError):
                self._mPercentTameCrop = 0.0

            try:
                self._mSpoilage = myTopElement.firstChildElement("spoilage").text()
            except (ValueError, TypeError):
                self._mSpoilage = 0

            try:
                reseedText = myTopElement.firstChildElement("reseed").text()
                self._mReseed = int(reseedText) if reseedText else 0
            except (ValueError, TypeError):
                self._mReseed = 0

            # Parse boolean and other values similarly
            self._mCropRotation = myTopElement.firstChildElement("cropRotation").text()

            try:
                self._mFallowRatio = float(myTopElement.firstChildElement("fallowRatio").text())
            except (ValueError, TypeError):
                # Set default fallow ratio if parsing fails
                self._mFallowRatio = 0.0
                warnings.warn("Failed to parse fallowRatio from XML, using default value 0.0")

            try:
                self._mFallowValue = int(myTopElement.firstChildElement("fallowValue").text())
            except (ValueError, TypeError):
                self._mFallowValue = 0

            # Handle fallow energy type - look for the tag and parse the enum name
            try:
                energyTypeElement = myTopElement.firstChildElement("fallowEnergyType")
                if not energyTypeElement.isNull():
                    energyTypeText = energyTypeElement.text().strip()
                    # Match the enum name exactly
                    if energyTypeText == "TDN":
                        self._mFallowEnergyType = LaEnergyType.TDN
                    elif energyTypeText == "KCalories":
                        self._mFallowEnergyType = LaEnergyType.KCalories
                    else:
                        print(f"Warning: Unknown energy type '{energyTypeText}', defaulting to KCalories")
                        self._mFallowEnergyType = LaEnergyType.KCalories
                else:
                    print("Warning: No fallowEnergyType tag found, defaulting to KCalories")
                    self._mFallowEnergyType = LaEnergyType.KCalories
            except Exception as e:
                print(f"Warning: Error parsing fallowEnergyType: {e}, defaulting to KCalories")
                self._mFallowEnergyType = LaEnergyType.KCalories

            # Handle area units
            myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
            self._mAreaUnits = LaAreaUnits.Dunum if myAreaUnits == "Dunum" else LaAreaUnits.Hectare

            self._mUseCommonLand = myTopElement.firstChildElement("useCommonLand").text()
            self._mUseSpecificLand = myTopElement.firstChildElement("useSpecificLand").text()
            self._mRasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())

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

