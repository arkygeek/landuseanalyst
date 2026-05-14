import os
from typing import Optional, Type, Dict, Any, cast
import warnings
from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtProperty
from qgis.PyQt.QtXml import QDomDocument, QDomElement, QDomNodeList
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.lafoodsource import LaFoodSource
from la.lib.la import LaFoodSourceMap, Priority, AreaUnits, EnergyType
from la.resources_rc import *

class LaAnimalParameter(QObject, LaSerialisable, LaGuid):
    # Signal definitions
    _nameChanged = pyqtSignal(str)
    _descriptionChanged = pyqtSignal(str)
    _guidChanged = pyqtSignal(str)
    _animalGuidChanged = pyqtSignal(str)
    _percentTameMeatChanged = pyqtSignal(float)
    _useCommonGrazingLandChanged = pyqtSignal(bool)
    _useSpecificGrazingLandChanged = pyqtSignal(bool)
    _fodderUseChanged = pyqtSignal(bool)
    _foodSourceMapChanged = pyqtSignal(dict)
    _fallowUsageChanged = pyqtSignal(object)
    _rasterNameChanged = pyqtSignal(str)
    _areaUnitsChanged = pyqtSignal(object)  # Added signal for area units
    _energyTypeChanged = pyqtSignal(object)  # Added signal for energy type
    _specificLandEnergyTypeChanged = pyqtSignal(object) # Added signal for specific land energy type
    _valueCommonGrazingLandChanged = pyqtSignal(int)  # Added signal for common grazing land value
    _valueSpecificGrazingLandChanged = pyqtSignal(int)  # Added signal for specific grazing land value
    _fodderSourceMapChanged = pyqtSignal(dict)  # Added signal for fodder source map changes

    _instances = []

    def __init__(self, theAnimalParameter: Optional['LaAnimalParameter'] = None, parent=None):
        super().__init__(parent)
        self._init_properties(theAnimalParameter)
        self.__class__._instances.append(self)

    def _init_properties(self, theAnimalParameter: Optional['LaAnimalParameter'] = None):
        """Initialize all properties with proper type conversion."""
        if theAnimalParameter is None:
            self.mGuid = LaGuid.setGuid(self, None)
            self.mName = "No Name Set"
            self.mDescription = "Not Set"
            self.mAnimalGuid = ""
            self.mPercentTameMeat = 0.0
            self.mUseCommonGrazingLand = False
            self.mUseSpecificGrazingLand = False
            self.mFodderUse = False # Changed default to bool
            self.mFoodSourceMap: Dict[str, LaFoodSource] = {}
            self.mFallowUsage = Priority.Nope
            self.mRasterName = ""
            self.mAreaUnits = AreaUnits.Dunum
            self.mEnergyType = EnergyType.KCalories
            self.mSpecificLandEnergyType = EnergyType.KCalories # Added default
            # No default values for grazing land productivity, matching C++ implementation
            self.mValueCommonGrazingLand = 0
            self.mValueSpecificGrazingLand = 0
        else:
            # Copy properties with safe type conversion
            self.mGuid = str(getattr(theAnimalParameter, 'mGuid', LaGuid.setGuid(self, None))) # Use getter or default
            self.mName = str(getattr(theAnimalParameter, 'mName', "No Name Set"))
            self.mDescription = str(getattr(theAnimalParameter, 'mDescription', "Not Set"))
            self.mAnimalGuid = str(getattr(theAnimalParameter, 'mAnimalGuid', ""))
            self.mPercentTameMeat = float(getattr(theAnimalParameter, 'mPercentTameMeat', 0.0))
            self.mUseCommonGrazingLand = bool(getattr(theAnimalParameter, 'mUseCommonGrazingLand', False))
            self.mUseSpecificGrazingLand = bool(getattr(theAnimalParameter, 'mUseSpecificGrazingLand', False))
            self.mFodderUse = bool(getattr(theAnimalParameter, 'mFodderUse', False)) # Changed to bool
            self.mFoodSourceMap = dict(getattr(theAnimalParameter, 'mFoodSourceMap', {}))
            self.mFallowUsage = getattr(theAnimalParameter, 'mFallowUsage', Priority.Nope) # Use getter or default
            self.mRasterName = str(getattr(theAnimalParameter, 'mRasterName', "")) # Corrected attribute name
            self.mAreaUnits = getattr(theAnimalParameter, 'mAreaUnits', AreaUnits.Dunum) # Use getter or default
            self.mEnergyType = getattr(theAnimalParameter, 'mEnergyType', EnergyType.KCalories) # Use getter or default
            self.mSpecificLandEnergyType = getattr(theAnimalParameter, 'mSpecificLandEnergyType', EnergyType.KCalories) # Use getter or default
            self.mValueCommonGrazingLand = int(getattr(theAnimalParameter, 'mValueCommonGrazingLand', 0))
            self.mValueSpecificGrazingLand = int(getattr(theAnimalParameter, 'mValueSpecificGrazingLand', 0))

    def __eq__(self, other):
        if not isinstance(other, LaAnimalParameter):
            return False
        # Compare all relevant attributes
        myAttributes = [
            'mGuid', 'mName', 'mDescription', 'mAnimalGuid', 'mPercentTameMeat',
            'mUseCommonGrazingLand', 'mUseSpecificGrazingLand', 'mFodderUse',
            'mFoodSourceMap', 'mFallowUsage', 'mRasterName', 'mAreaUnits',
            'mEnergyType', 'mSpecificLandEnergyType', 'mValueCommonGrazingLand',
            'mValueSpecificGrazingLand'
        ]
        return all(getattr(self, attr) == getattr(other, attr) for attr in myAttributes)

    @classmethod
    def getInstances(cls):
        """Returns a list of all instances of LaAnimalParameter."""
        return cls._instances

    @classmethod
    def getInstanceByName(cls, name):
        for instance in cls._instances:
            if instance.mName == name:
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

    @pyqtProperty(str, notify=_nameChanged)
    def name(self) -> str: # type: ignore
        """Get the name of the animal parameter."""
        return str(self.mName)

    @name.setter
    def name(self, value: str) -> None:
        """Set the name of the animal parameter."""
        value = str(value)
        if self.mName != value:
            self.mName = value
            self._nameChanged.emit(value)

    @pyqtProperty(str, notify=_descriptionChanged)
    def description(self) -> str: # type: ignore
        """Get the description of the animal parameter."""
        return str(self.mDescription)

    @description.setter
    def description(self, value: str) -> None:
        """Set the description of the animal parameter."""
        value = str(value)
        if self.mDescription != value:
            self.mDescription = value
            self._descriptionChanged.emit(value)

    @pyqtProperty(str, notify=_guidChanged)
    def guid(self): # type: ignore
        return self.mGuid

    @guid.setter
    def guid(self, theGuid):
        if self.mGuid != theGuid:
            self.mGuid = theGuid
            self._guidChanged.emit(theGuid)

    @pyqtProperty(str, notify=_animalGuidChanged)
    def animalGuid(self) -> str: # type: ignore
        """Get the animal GUID."""
        return str(self.mAnimalGuid)

    @animalGuid.setter
    def animalGuid(self, value: str) -> None:
        """Set the animal GUID."""
        value = str(value)
        if self.mAnimalGuid != value:
            self.mAnimalGuid = value
            self._animalGuidChanged.emit(value)

    @pyqtProperty(float, notify=_percentTameMeatChanged)
    def percentTameMeat(self) -> float: # type: ignore
        """Get the percentage of tame meat."""
        return float(self.mPercentTameMeat)

    @percentTameMeat.setter
    def percentTameMeat(self, value: float) -> None:
        """Set the percentage of tame meat."""
        value = float(value)
        if self.mPercentTameMeat != value:
            self.mPercentTameMeat = value
            self._percentTameMeatChanged.emit(value)

    @pyqtProperty(bool, notify=_useCommonGrazingLandChanged)
    def useCommonGrazingLand(self) -> bool: # type: ignore
        """Get whether common grazing land is used."""
        return bool(self.mUseCommonGrazingLand)

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, value: bool) -> None:
        """Set whether common grazing land is used."""
        value = bool(value)
        if self.mUseCommonGrazingLand != value:
            self.mUseCommonGrazingLand = value
            self._useCommonGrazingLandChanged.emit(value)

    @pyqtProperty(bool, notify=_useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self) -> bool: # type: ignore
        """Get whether specific grazing land is used."""
        return bool(self.mUseSpecificGrazingLand)

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, value: bool) -> None:
        """Set whether specific grazing land is used."""
        value = bool(value)
        if self.mUseSpecificGrazingLand != value:
            self.mUseSpecificGrazingLand = value
            self._useSpecificGrazingLandChanged.emit(value)

    @pyqtProperty(bool, notify=_fodderUseChanged)
    def fodderUse(self) -> bool: # type: ignore
        """Get the fodder use value."""
        return bool(self.mFodderUse)

    @fodderUse.setter
    def fodderUse(self, value: bool) -> None:
        """Set the fodder use value."""
        value = bool(value)
        if self.mFodderUse != value:
            self.mFodderUse = value
            self._fodderUseChanged.emit(value)

    @pyqtProperty('QVariantMap', notify=_foodSourceMapChanged)
    def foodSourceMap(self) -> Dict[str, LaFoodSource]: # type: ignore
        """Get the food source map."""
        return dict(self.mFoodSourceMap)

    @pyqtProperty('QVariantMap', notify=_fodderSourceMapChanged)  # Changed type hint from object
    def fodderSourceMap(self) -> Dict[str, LaFoodSource]:
        """Get the fodder source map. This is an alias for foodSourceMap for compatibility with C++ code."""
        return dict(self.mFoodSourceMap)

    @foodSourceMap.setter
    def foodSourceMap(self, value: Dict[str, LaFoodSource]) -> None:
        """Set the food source map."""
        value = dict(value)
        if self.mFoodSourceMap != value:
            self.mFoodSourceMap = value
            self._foodSourceMapChanged.emit(value)

    @pyqtProperty(object, notify=_fallowUsageChanged)
    def fallowUsage(self) -> Priority: # type: ignore
        """Get the fallow usage priority."""
        return Priority(self.mFallowUsage)

    @fallowUsage.setter
    def fallowUsage(self, value: Priority) -> None:
        """Set the fallow usage priority."""
        if isinstance(value, Priority) and self.mFallowUsage != value:
            self.mFallowUsage = value
            self._fallowUsageChanged.emit(value)

    @pyqtProperty(str, notify=_rasterNameChanged)
    def rasterName(self): # type: ignore
        return self.mRasterName

    @rasterName.setter
    def rasterName(self, rasterName):
        if self.mRasterName != rasterName:
            self.mRasterName = rasterName
            self._rasterNameChanged.emit(rasterName)

    @pyqtProperty(AreaUnits, notify=_areaUnitsChanged)  # Changed type hint from object
    def areaUnits(self) -> AreaUnits: # type: ignore
        """Get the area units."""
        return AreaUnits(self.mAreaUnits)

    @areaUnits.setter
    def areaUnits(self, value: AreaUnits) -> None:
        """Set the area units."""
        if isinstance(value, AreaUnits) and self.mAreaUnits != value:
            self.mAreaUnits = value
            self._areaUnitsChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(EnergyType, notify=_energyTypeChanged)  # Changed type hint from object
    def energyType(self) -> EnergyType: # type: ignore
        """Get the energy type."""
        return EnergyType(self.mEnergyType)

    @energyType.setter
    def energyType(self, value: EnergyType) -> None:
        """Set the energy type."""
        if isinstance(value, EnergyType) and self.mEnergyType != value:
            self.mEnergyType = value
            self._energyTypeChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(EnergyType, notify=_specificLandEnergyTypeChanged) # Changed type hint from object
    def specificLandEnergyType(self) -> EnergyType: # type: ignore
        """Get the specific land energy type."""
        return EnergyType(self.mSpecificLandEnergyType)

    @specificLandEnergyType.setter
    def specificLandEnergyType(self, value: EnergyType) -> None:
        """Set the specific land energy type."""
        if isinstance(value, EnergyType) and self.mSpecificLandEnergyType != value:
            self.mSpecificLandEnergyType = value
            self._specificLandEnergyTypeChanged.emit(value)

    @pyqtProperty(int, notify=_valueCommonGrazingLandChanged)
    def valueCommonGrazingLand(self) -> int: # type: ignore
        """Get the value of common grazing land in calories per hectare."""
        return int(self.mValueCommonGrazingLand)

    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, value: int) -> None:
        """Set the value of common grazing land in calories per hectare."""
        value = int(value)
        if self.mValueCommonGrazingLand != value:
            self.mValueCommonGrazingLand = value
            self._valueCommonGrazingLandChanged.emit(value)

    @pyqtProperty(int, notify=_valueSpecificGrazingLandChanged)
    def valueSpecificGrazingLand(self) -> int: # type: ignore
        """Get the value of specific grazing land in calories per hectare."""
        return int(self.mValueSpecificGrazingLand)

    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, value: int) -> None:
        """Set the value of specific grazing land in calories per hectare."""
        value = int(value)
        if self.mValueSpecificGrazingLand != value:
            self.mValueSpecificGrazingLand = value
            self._valueSpecificGrazingLandChanged.emit(value)


    def fromXml(self, theXml):
        """
        Parse animal parameter data from XML string.
        Direct port from C++ version.
        """
        from la.lib.lautils import LaUtils
        from la.lib.lafoodsource import LaFoodSource
        from qgis.PyQt.QtXml import QDomDocument
        from la.lib.la import EnergyType, AreaUnits, Priority

        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("animalParameter")
        if myTopElement.isNull():
            LaUtils.debug.log("top element could not be found!")

        self.setGuid(myTopElement.attribute("guid"))
        self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        if self.mName == "":
            # Try alternative name tag (n) for backward compatibility
            self.mName = LaUtils.xmlDecode(myTopElement.firstChildElement("n").text())
        
        self.mDescription = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        self.mAnimalGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("animal").text())
        
        # Safe value extraction with defaults
        try:
            self.mPercentTameMeat = float(myTopElement.firstChildElement("percentTameMeat").text() or 0)
        except (ValueError, TypeError):
            self.mPercentTameMeat = 0.0
            
        try:
            self.mUseCommonGrazingLand = bool(int(myTopElement.firstChildElement("useCommonGrazingLand").text() or 0))
        except (ValueError, TypeError):
            self.mUseCommonGrazingLand = False
            
        try:
            self.mUseSpecificGrazingLand = bool(int(myTopElement.firstChildElement("useSpecificGrazingLand").text() or 0))
        except (ValueError, TypeError):
            self.mUseSpecificGrazingLand = False
            
        try:
            self.mValueCommonGrazingLand = int(myTopElement.firstChildElement("foodValueCommonGrazingLand").text() or 0)
        except (ValueError, TypeError):
            self.mValueCommonGrazingLand = 0
            
        try:
            self.mValueSpecificGrazingLand = int(myTopElement.firstChildElement("foodValueOfSpecificGrazingLand").text() or 0)
        except (ValueError, TypeError):
            self.mValueSpecificGrazingLand = 0

        # Parse area units
        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self.mAreaUnits = AreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self.mAreaUnits = AreaUnits.Hectare
        else:
            self.mAreaUnits = AreaUnits.Dunum  # Default

        # Parse energy type
        myEnergyType = myTopElement.firstChildElement("energyType").text()
        if myEnergyType == "KCalories":
            self.mEnergyType = EnergyType.KCalories
        elif myEnergyType == "TDN":
            self.mEnergyType = EnergyType.TDN
        else:
            self.mEnergyType = EnergyType.KCalories  # Default
            
        # Parse specific land energy type
        mySpecificLandEnergyType = myTopElement.firstChildElement("specificLandEnergyType").text()
        if mySpecificLandEnergyType == "KCalories":
            self.mSpecificLandEnergyType = EnergyType.KCalories
        elif mySpecificLandEnergyType == "TDN":
            self.mSpecificLandEnergyType = EnergyType.TDN
        else:
            self.mSpecificLandEnergyType = EnergyType.KCalories  # Default

        # Parse fodder use with safe conversion
        try:
            self.mFodderUse = bool(int(myTopElement.firstChildElement("fodderUse").text() or 0))
        except (ValueError, TypeError):
            self.mFodderUse = False

        # populate the fodder map
        self.mFoodSourceMap.clear()
        
        # Check for fodderCrops container element
        myFodderCropsElement = myTopElement.firstChildElement("fodderCrops")
        if not myFodderCropsElement.isNull():
            # Get all fodderCrop elements
            myFodderCropList = myFodderCropsElement.elementsByTagName("fodderCrop")
            
            for i in range(myFodderCropList.count()):
                myFoodSourceElement = myFodderCropList.at(i).toElement()
                if myFoodSourceElement.isNull():
                    continue
                    
                # Extract crop GUID
                myCropGuid = myFoodSourceElement.firstChildElement("fodderCropGuid").text()
                if not myCropGuid:
                    continue
                
                # Create food source with safe conversions
                myFoodSource = LaFoodSource()
                
                try:
                    myFoodSource.fodder = int(myFoodSourceElement.firstChildElement("fodderStrawChaff").text() or 0)
                except (ValueError, TypeError):
                    myFoodSource.fodder = 0
                    
                try:
                    myFoodSource.grain = int(myFoodSourceElement.firstChildElement("fodderGrain").text() or 0)
                except (ValueError, TypeError):
                    myFoodSource.grain = 0
                
                # In XML files, the fodder use element might exist at the individual food source level
                myUsedElement = myFoodSourceElement.firstChildElement("fodderUse")
                if not myUsedElement.isNull():
                    try:
                        myFoodSource.used = bool(int(myUsedElement.text() or 0))
                    except (ValueError, TypeError):
                        myFoodSource.used = False
                else:
                    # If not found at the individual level, use the global fodderUse setting
                    myFoodSource.used = bool(self.mFodderUse)
                
                try:
                    myFoodSource.days = int(myFoodSourceElement.firstChildElement("fodderDays").text() or 0)
                except (ValueError, TypeError):
                    myFoodSource.days = 0
                
                myFoodSource.cropGuid = myCropGuid
                
                # Add to map
                self.mFoodSourceMap[myCropGuid] = myFoodSource

        # Parse fallow usage
        myFallowUsage = myTopElement.firstChildElement("fallowUsage").text()
        if myFallowUsage == "High":
            self.mFallowUsage = Priority.High
        elif myFallowUsage == "Medium":
            self.mFallowUsage = Priority.Medium
        elif myFallowUsage == "Low":
            self.mFallowUsage = Priority.Low
        else:
            self.mFallowUsage = Priority.Nope

        self.mRasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
        return True

    def toXml(self) -> str:
        from la.lib.lautils import LaUtils
        myString = f"<animalParameter guid=\"{self.guid}\">\n"
        # Use both name tags for maximum compatibility
        myString += f"  <name>{LaUtils.xmlEncode(str(self.name))}</name>\n"  # Standard name tag
        myString += f"  <description>{LaUtils.xmlEncode(str(self.description))}</description>\n"
        myString += f"  <animal>{LaUtils.xmlEncode(str(self.animalGuid))}</animal>\n"
        myString += f"  <percentTameMeat>{self.percentTameMeat}</percentTameMeat>\n"
        myString += f"  <useCommonGrazingLand>{1 if self.useCommonGrazingLand else 0}</useCommonGrazingLand>\n"
        myString += f"  <useSpecificGrazingLand>{1 if self.useSpecificGrazingLand else 0}</useSpecificGrazingLand>\n"
        myString += f"  <fodderUse>{self.fodderUse}</fodderUse>\n"

        # Add food source map data
        if self.mFodderUse and self.mFoodSourceMap:
            myString += "  <fodderCrops>\n"
            for cropGuid, foodSource in dict(self.mFoodSourceMap).items():
                myString += "    <foodSource>\n"
                myString += f"      <fodderCropGuid>{cropGuid}</fodderCropGuid>\n"
                myString += f"      <fodderStrawChaff>{foodSource.fodder}</fodderStrawChaff>\n"
                myString += f"      <fodderGrain>{foodSource.grain}</fodderGrain>\n"
                myString += f"      <fodderUse>{1 if foodSource.used else 0}</fodderUse>\n"
                myString += f"      <fodderDays>{foodSource.days}</fodderDays>\n"
                myString += "    </foodSource>\n"
            myString += "  </fodderCrops>\n"

        # Handle fallowUsage based on Priority enum
        fallowUsageStr = "None"
        if self.mFallowUsage == Priority.High:
            fallowUsageStr = "High"
        elif self.mFallowUsage == Priority.Medium:
            fallowUsageStr = "Medium"
        elif self.mFallowUsage == Priority.Low:
            fallowUsageStr = "Low"

        myString += f"  <fallowUsage>{fallowUsageStr}</fallowUsage>\n"
        myString += f"  <rasterName>{LaUtils.xmlEncode(str(self.rasterName))}</rasterName>\n"
        myString += f"  <areaUnits>{self.mAreaUnits.name}</areaUnits>\n"
        myString += f"  <energyType>{self.mEnergyType.name}</energyType>\n"
        myString += f"  <specificLandEnergyType>{self.mSpecificLandEnergyType.name}</specificLandEnergyType>\n"
        myString += f"  <valueCommonGrazingLand>{self.valueCommonGrazingLand}</valueCommonGrazingLand>\n"
        myString += f"  <valueSpecificGrazingLand>{self.valueSpecificGrazingLand}</valueSpecificGrazingLand>\n"
        myString += "</animalParameter>\n"
        return myString

    def toHtml(self) -> str:
        """Generate HTML table representation of animal parameter data.

        Returns:
            HTML string containing formatted parameter attributes
        """
        from la.lib.lautils import LaUtils  # Import here to avoid circular imports
        myString = f'<h2>Details for {LaUtils.xmlEncode(str(self.mName))}</h2>'
        myString += '<table>'
        myString += f'<tr><td><b>Description:</b></td><td>{self.mDescription}</td></tr>'
        myString += f'<tr><td><b>Percentage of Tame Meat:</b></td><td>{self.mPercentTameMeat}</td></tr>'
        myString += f'<tr><td><b>Use Common Grazing Land:</b></td><td>{self.mUseCommonGrazingLand}</td></tr>'
        myString += f'<tr><td><b>Use Specific Grazing Land:</b></td><td>{self.mUseSpecificGrazingLand}</td></tr>'

        if self.mFodderUse:
            myString += '<tr><td><b>Uses Fodder:</b></td><td>Yes</td></tr>'
            if self.mFoodSourceMap:
                myString += '<tr><td colspan="2"><b>Food Sources:</b></td></tr>'
                counter = 0
                for cropGuid, foodSource in self.mFoodSourceMap.items():
                    counter += 1
                    myString += f'<tr><td colspan="2">Fodder Source #{counter}</td></tr>'
                    myString += f'<tr><td>Crop GUID:</td><td>{cropGuid}</td></tr>'
                    myString += f'<tr><td>Straw and Chaff:</td><td>{foodSource.fodder}</td></tr>'
                    myString += f'<tr><td>Grain:</td><td>{foodSource.grain}</td></tr>'
                    myString += f'<tr><td>Days:</td><td>{foodSource.days}</td></tr>'
                    myString += f'<tr><td>Used:</td><td>{"Yes" if foodSource.used else "No"}</td></tr>'
        else:
            myString += '<tr><td><b>Uses Fodder:</b></td><td>No</td></tr>'

        # Handle fallowUsage based on Priority enum
        fallowUsageStr = "None"
        if hasattr(self, "_fallowUsage"):
            if self.mFallowUsage == Priority.High:
                fallowUsageStr = "High"
            elif self.mFallowUsage == Priority.Medium:
                fallowUsageStr = "Medium"
            elif self.mFallowUsage == Priority.Low:
                fallowUsageStr = "Low"

        myString += f'<tr><td><b>Fallow Usage:</b></td><td>{fallowUsageStr}</td></tr>'

        if self.mRasterName:
            myString += f'<tr><td><b>Raster Mask:</b></td><td>{self.mRasterName}</td></tr>'

        myString += '</table>'
        return myString
