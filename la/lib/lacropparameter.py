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
    fallowValueChanged = pyqtSignal(int)    # Changed to int to match C++
    areaUnitsChanged = pyqtSignal(object)   # Using object because LaAreaUnits is an enum
    useCommonLandChanged = pyqtSignal(bool)
    useSpecificLandChanged = pyqtSignal(bool)
    rasterNameChanged = pyqtSignal(str)

    def __init__(self, theCropParameter: Optional['LaCropParameter'] = None):
        """
        Initialize a new crop parameter object.

        :param theCropParameter: Optional crop parameter to copy from
        :type theCropParameter: Optional[LaCropParameter]
        """
        super().__init__()
        self.mGuid = LaGuid()
        self.mName = "No Name Set"
        self.mDescription = "Not Set"
        self.mCropGuid = ""
        self.mPercentTameCrop = 0.0
        self.mSpoilage = 0.0
        self.mReseed = 0.0
        self.mCropRotation = False
        self.mFallowRatio = 0.0
        self.mFallowValue = 0
        self.mAreaUnits = LaAreaUnits.Dunum
        self.mUseCommonLand = False
        self.mUseSpecificLand = False
        self.mRasterName = ""

        if theCropParameter is not None:
            # Copy from existing parameter
            self.name(theCropParameter.name)
            self.name = theCropParameter.name
            self.description = theCropParameter.description
            self.guid = theCropParameter.guid
            self.cropGuid = theCropParameter.cropGuid
            self.percentTameCrop = theCropParameter.percentTameCrop
            self.spoilage = theCropParameter.spoilage
            self.reseed = theCropParameter.reseed
            self.cropRotation = theCropParameter.cropRotation
            self.fallowRatio = theCropParameter.fallowRatio
            self.fallowValue = theCropParameter.fallowValue
            self.areaUnits = theCropParameter.areaUnits
            self.useCommonLand = theCropParameter.useCommonLand
            self.useSpecificLand = theCropParameter.useSpecificLand
            self.rasterName = theCropParameter.rasterName

    @pyqtProperty(str, notify=nameChanged)
    def name(self) -> str: #type: ignore
        """Get the name of the crop parameter."""
        return str(self.mName)

    @name.setter
    def name(self, theName: str) -> None:
        """Set the name of the crop parameter."""
        if self.mName != theName:
            self.mName = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: #type: ignore
        """Get the description of the crop parameter."""
        return str(self.mDescription)

    @description.setter
    def description(self, theDescription: str) -> None:
        """Set the description of the crop parameter."""
        if self.mDescription != theDescription:
            self.mDescription = theDescription
            self.descriptionChanged.emit(theDescription)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self) -> str: #type: ignore
        """Get the GUID of the crop parameter."""
        return str(self.mGuid)

    @guid.setter
    def guid(self, theGuid: str) -> None:
        """Set the GUID of the crop parameter."""
        if self.mGuid != theGuid:
            self.mGuid = theGuid
            self.guidChanged.emit(theGuid)

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self) -> str: #type: ignore
        """Get the crop GUID."""
        return str(self.mCropGuid)

    @cropGuid.setter
    def cropGuid(self, theCropGuid: str) -> None:
        """Set the crop GUID."""
        if self.mCropGuid != theCropGuid:
            self.mCropGuid = theCropGuid
            self.cropGuidChanged.emit(theCropGuid)

    @pyqtProperty(float, notify=percentTameCropChanged)
    def percentTameCrop(self) -> float: #type: ignore
        """Get the percentage of tame crop."""
        return float(self.mPercentTameCrop)

    @percentTameCrop.setter
    def percentTameCrop(self, theValue: float) -> None:
        """Set the percentage of tame crop."""
        try:
            myFloatValue = float(theValue)
            if self.mPercentTameCrop != myFloatValue:
                self.mPercentTameCrop = myFloatValue
                self.percentTameCropChanged.emit(myFloatValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert percentTameCrop value to float: {theValue}")
            self.mPercentTameCrop = 0.0
            self.percentTameCropChanged.emit(0.0)

    @pyqtProperty(int, notify=spoilageChanged)
    def spoilage(self) -> int: #type: ignore
        """Get the spoilage percentage."""
        return int(self.mSpoilage)

    @spoilage.setter
    def spoilage(self, theValue: int) -> None:
        """Set the spoilage percentage."""
        try:
            myIntValue = int(theValue)
            if self.mSpoilage != myIntValue:
                self.mSpoilage = myIntValue
                self.spoilageChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert spoilage value to int: {theValue}")
            self.mSpoilage = 0
            self.spoilageChanged.emit(0)

    @pyqtProperty(int, notify=reseedChanged)
    def reseed(self) -> int: #type: ignore
        """Get the reseed percentage."""
        return int(self.mReseed)

    @reseed.setter
    def reseed(self, theValue: int) -> None:
        """Set the reseed percentage."""
        try:
            myIntValue = int(theValue)
            if self.mReseed != myIntValue:
                self.mReseed = myIntValue
                self.reseedChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert reseed value to int: {theValue}")
            self.mReseed = 0
            self.reseedChanged.emit(0)

    @pyqtProperty(bool, notify=cropRotationChanged)
    def cropRotation(self) -> bool: #type: ignore
        """Get whether crop rotation is used."""
        return bool(self.mCropRotation)

    @cropRotation.setter
    def cropRotation(self, theValue: bool) -> None:
        """Set whether crop rotation is used."""
        bool_value = bool(theValue)
        if self.mCropRotation != bool_value:
            self.mCropRotation = bool_value
            self.cropRotationChanged.emit(bool_value)

    @pyqtProperty(float, notify=fallowRatioChanged)
    def fallowRatio(self) -> float: #type: ignore
        """Get the fallow ratio."""
        return float(self.mFallowRatio)

    @fallowRatio.setter
    def fallowRatio(self, theValue: float) -> None:
        """Set the fallow ratio."""
        try:
            myFloatValue = float(theValue)
            if self.mFallowRatio != myFloatValue:
                self.mFallowRatio = myFloatValue
                self.fallowRatioChanged.emit(myFloatValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowRatio value to float: {theValue}")
            self.mFallowRatio = 0.0
            self.fallowRatioChanged.emit(0.0)

    @pyqtProperty(int, notify=fallowValueChanged)
    def fallowValue(self) -> int: #type: ignore
        """Get the fallow value."""
        return int(self.mFallowValue)

    @fallowValue.setter
    def fallowValue(self, theValue: int) -> None:
        """Set the fallow value."""
        try:
            myIntValue = int(theValue)
            if self.mFallowValue != myIntValue:
                self.mFallowValue = myIntValue
                self.fallowValueChanged.emit(myIntValue)
        except (ValueError, TypeError):
            print(f"Warning: Failed to convert fallowValue to int: {theValue}")
            self.mFallowValue = 0
            self.fallowValueChanged.emit(0)

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self) -> LaAreaUnits: #type: ignore
        """Get the area units used."""
        return self.mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theValue: LaAreaUnits) -> None:
        """Set the area units used."""
        if self.mAreaUnits != theValue:
            self.mAreaUnits = theValue
            self.areaUnitsChanged.emit(theValue)

    @pyqtProperty(bool, notify=useCommonLandChanged)
    def useCommonLand(self) -> bool: #type: ignore
        """Get whether common land is used."""
        return bool(self.mUseCommonLand)

    @useCommonLand.setter
    def useCommonLand(self, theValue: bool) -> None:
        """Set whether common land is used."""
        bool_value = bool(theValue)
        if self.mUseCommonLand != bool_value:
            self.mUseCommonLand = bool_value
            self.useCommonLandChanged.emit(bool_value)

    @pyqtProperty(bool, notify=useSpecificLandChanged)
    def useSpecificLand(self) -> bool: #type: ignore
        """Get whether specific land is used."""
        return bool(self.mUseSpecificLand)

    @useSpecificLand.setter
    def useSpecificLand(self, theValue: bool) -> None:
        """Set whether specific land is used."""
        bool_value = bool(theValue)
        if self.mUseSpecificLand != bool_value:
            self.mUseSpecificLand = bool_value
            self.useSpecificLandChanged.emit(bool_value)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self) -> str: #type: ignore
        """Get the name of the raster."""
        return str(self.mRasterName)

    @rasterName.setter
    def rasterName(self, theValue: str) -> None:
        """Set the name of the raster."""
        if self.mRasterName != theValue:
            self.mRasterName = theValue
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
        myUnits = "Dunum" if self.mAreaUnits == LaAreaUnits.Dunum else "Hectare"
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

            # Use property assignment instead of calling them as functions
            self.setGuid(myTopElement.attribute("guid"))
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
            self.mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
            self.mCropGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("crop").text())
            self.mPercentTameCrop = myTopElement.firstChildElement("percentTameCrop").text()
            self.mSpoilage = myTopElement.firstChildElement("spoilage").text()
            self.mReseed = myTopElement.firstChildElement("reseed").text()
            self.mCropRotation = myTopElement.firstChildElement("cropRotation").text()
            self.mFallowRatio = myTopElement.firstChildElement("fallowRatio").text()
            self.mFallowValue = myTopElement.firstChildElement("fallowValue").text()

            # Handle area units
            myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
            self.mAreaUnits = LaAreaUnits.Dunum if myAreaUnits == "Dunum" else LaAreaUnits.Hectare
            # Convert AreaUnits enum to integer index
            # self.cbAreaUnits.setCurrentIndex(self.mAreaUnits.value)

            self.mUseCommonLand = bool(int(myTopElement.firstChildElement("useCommonLand").text()))
            self.mUseSpecificLand = bool(int(myTopElement.firstChildElement("useSpecificLand").text()))
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
