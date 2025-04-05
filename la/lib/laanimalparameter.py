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
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    guidChanged = pyqtSignal(str)
    animalGuidChanged = pyqtSignal(str)
    percentTameMeatChanged = pyqtSignal(float)
    useCommonGrazingLandChanged = pyqtSignal(bool)
    useSpecificGrazingLandChanged = pyqtSignal(bool)
    fodderUseChanged = pyqtSignal(bool)
    foodSourceMapChanged = pyqtSignal(dict)
    fallowUsageChanged = pyqtSignal(object)
    rasterNameChanged = pyqtSignal(str)
    areaUnitsChanged = pyqtSignal(object)  # Added signal for area units
    energyTypeChanged = pyqtSignal(object)  # Added signal for energy type
    specificLandEnergyTypeChanged = pyqtSignal(object) # Added signal for specific land energy type
    valueCommonGrazingLandChanged = pyqtSignal(int)  # Added signal for common grazing land value
    valueSpecificGrazingLandChanged = pyqtSignal(int)  # Added signal for specific grazing land value

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
            self.mFodderUse = 0.0
            self.mFoodSourceMap: Dict[str, LaFoodSource] = {}
            self.mFallowUsage = Priority.None_
            self.mRrasterName = ""
            self.mAreaUnits = AreaUnits.Dunum
            self.mEnergyType = EnergyType.KCalories
            self.mSpecificLandEnergyType = EnergyType.KCalories # Added default
            # No default values for grazing land productivity, matching C++ implementation
            self.mValueCommonGrazingLand = 0
            self.mValueSpecificGrazingLand = 0
        else:
            # Copy properties with safe type conversion
            self.mGuid = str(getattr(theAnimalParameter, '_mGuid', ''))
            self.mName = str(getattr(theAnimalParameter, '_mName', ''))
            self.mDescription = str(getattr(theAnimalParameter, '_mDescription', ''))
            self.mAnimalGuid = str(getattr(theAnimalParameter, '_mAnimalGuid', ''))
            self.mPercentTameMeat = float(getattr(theAnimalParameter, '_mPercentTameMeat', 0.0))
            self.mUseCommonGrazingLand = bool(getattr(theAnimalParameter, '_mUseCommonGrazingLand', False))
            self.mUseSpecificGrazingLand = bool(getattr(theAnimalParameter, '_mUseSpecificGrazingLand', False))
            self.mFodderUse = float(getattr(theAnimalParameter, '_mFodderUse', 0.0))
            self.mFoodSourceMap = dict(getattr(theAnimalParameter, '_mFoodSourceMap', {}))
            self.mFallowUsage = getattr(theAnimalParameter, '_fallowUsage', Priority)
            self.mRrasterName = str(getattr(theAnimalParameter, '_rasterName', ''))
            self.mAreaUnits = getattr(theAnimalParameter, '_areaUnits', AreaUnits)
            self.mEnergyType = getattr(theAnimalParameter, '_energyType', EnergyType)
            self.mSpecificLandEnergyType = getattr(theAnimalParameter, '_specificLandEnergyType', EnergyType.KCalories) # Added assignment
            self.mValueCommonGrazingLand = int(getattr(theAnimalParameter, '_mValueCommonGrazingLand', 0))
            self.mValueSpecificGrazingLand = int(getattr(theAnimalParameter, '_mValueSpecificGrazingLand', 0))

    def __eq__(self, other):
        if not isinstance(other, LaAnimalParameter):
            return False
        myAttributes = [
            'mGuid',               'mName',              'mDescription',
            'mAnimalGuid',         'mPercentTameMeat',   'mUseCommonGrazingLand',
            'mUseSpecificGrazingLand', 'mFodderUse',     'mFoodSourceMap',
            'mFallowUsage',        'mRrasterName',       'mAreaUnits',
            'mEnergyType',         'mSpecificLandEnergyType',
            'mValueCommonGrazingLand', 'mValueSpecificGrazingLand'
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
    def name(self) -> str: # type: ignore
        """Get the name of the animal parameter."""
        return str(self.mName)

    @name.setter
    def name(self, value: str) -> None:
        """Set the name of the animal parameter."""
        value = str(value)
        if self.mName != value:
            self.mName = value
            self.nameChanged.emit(value)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: # type: ignore
        """Get the description of the animal parameter."""
        return str(self.mDescription)

    @description.setter
    def description(self, value: str) -> None:
        """Set the description of the animal parameter."""
        value = str(value)
        if self.mDescription != value:
            self.mDescription = value
            self.descriptionChanged.emit(value)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self): # type: ignore
        return self.mGuid

    @guid.setter
    def guid(self, guid):
        if self.mGuid != guid:
            self.mGuid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=animalGuidChanged)
    def animalGuid(self) -> str: # type: ignore
        """Get the animal GUID."""
        return str(self.mAnimalGuid)

    @animalGuid.setter
    def animalGuid(self, value: str) -> None:
        """Set the animal GUID."""
        value = str(value)
        if self.mAnimalGuid != value:
            self.mAnimalGuid = value
            self.animalGuidChanged.emit(value)

    @pyqtProperty(float, notify=percentTameMeatChanged)
    def percentTameMeat(self) -> float: # type: ignore
        """Get the percentage of tame meat."""
        return float(self.mPercentTameMeat)

    @percentTameMeat.setter
    def percentTameMeat(self, value: float) -> None:
        """Set the percentage of tame meat."""
        value = float(value)
        if self.mPercentTameMeat != value:
            self.mPercentTameMeat = value
            self.percentTameMeatChanged.emit(value)

    @pyqtProperty(bool, notify=useCommonGrazingLandChanged)
    def useCommonGrazingLand(self) -> bool: # type: ignore
        """Get whether common grazing land is used."""
        return bool(self.mUseCommonGrazingLand)

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, value: bool) -> None:
        """Set whether common grazing land is used."""
        value = bool(value)
        if self.mUseCommonGrazingLand != value:
            self.mUseCommonGrazingLand = value
            self.useCommonGrazingLandChanged.emit(value)

    @pyqtProperty(bool, notify=useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self) -> bool: # type: ignore
        """Get whether specific grazing land is used."""
        return bool(self.mUseSpecificGrazingLand)

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, value: bool) -> None:
        """Set whether specific grazing land is used."""
        value = bool(value)
        if self.mUseSpecificGrazingLand != value:
            self.mUseSpecificGrazingLand = value
            self.useSpecificGrazingLandChanged.emit(value)

    @pyqtProperty(bool, notify=fodderUseChanged)
    def fodderUse(self) -> bool: # type: ignore
        """Get the fodder use value."""
        return bool(self.mFodderUse)

    @fodderUse.setter
    def fodderUse(self, value: bool) -> None:
        """Set the fodder use value."""
        value = bool(value)
        if self.mFodderUse != value:
            self.mFodderUse = value
            self.fodderUseChanged.emit(value)

    @pyqtProperty('QVariantMap', notify=foodSourceMapChanged)
    def foodSourceMap(self) -> Dict[str, LaFoodSource]: # type: ignore
        """Get the food source map."""
        return dict(self.mFoodSourceMap)

    def fodderSourceMap(self) -> Dict[str, LaFoodSource]:
        """Get the fodder source map. This is an alias for foodSourceMap for compatibility with C++ code."""
        return dict(self.mFoodSourceMap)

    @foodSourceMap.setter
    def foodSourceMap(self, value: Dict[str, LaFoodSource]) -> None:
        """Set the food source map."""
        value = dict(value)
        if self.mFoodSourceMap != value:
            self.mFoodSourceMap = value
            self.foodSourceMapChanged.emit(value)

    @pyqtProperty(object, notify=fallowUsageChanged)
    def fallowUsage(self) -> Priority: # type: ignore
        """Get the fallow usage priority."""
        return Priority(self.mFallowUsage)

    @fallowUsage.setter
    def fallowUsage(self, value: Priority) -> None:
        """Set the fallow usage priority."""
        if isinstance(value, Priority) and self.mFallowUsage != value:
            self.mFallowUsage = value
            self.fallowUsageChanged.emit(value)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self): # type: ignore
        return self.mRrasterName

    @rasterName.setter
    def rasterName(self, rasterName):
        if self.mRrasterName != rasterName:
            self.mRrasterName = rasterName
            self.rasterNameChanged.emit(rasterName)

    @pyqtProperty(AreaUnits, notify=areaUnitsChanged)  # Changed type hint from object
    def areaUnits(self) -> AreaUnits: # type: ignore
        """Get the area units."""
        return AreaUnits(self.mAreaUnits)

    @areaUnits.setter
    def areaUnits(self, value: AreaUnits) -> None:
        """Set the area units."""
        if isinstance(value, AreaUnits) and self.mAreaUnits != value:
            self.mAreaUnits = value
            self.areaUnitsChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(EnergyType, notify=energyTypeChanged)  # Changed type hint from object
    def energyType(self) -> EnergyType: # type: ignore
        """Get the energy type."""
        return EnergyType(self.mEnergyType)

    @energyType.setter
    def energyType(self, value: EnergyType) -> None:
        """Set the energy type."""
        if isinstance(value, EnergyType) and self.mEnergyType != value:
            self.mEnergyType = value
            self.energyTypeChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(EnergyType, notify=specificLandEnergyTypeChanged) # Changed type hint from object
    def specificLandEnergyType(self) -> EnergyType: # type: ignore
        """Get the specific land energy type."""
        return EnergyType(self.mSpecificLandEnergyType)

    @specificLandEnergyType.setter
    def specificLandEnergyType(self, value: EnergyType) -> None:
        """Set the specific land energy type."""
        if isinstance(value, EnergyType) and self.mSpecificLandEnergyType != value:
            self.mSpecificLandEnergyType = value
            self.specificLandEnergyTypeChanged.emit(value)

    @pyqtProperty(int, notify=valueCommonGrazingLandChanged)
    def valueCommonGrazingLand(self) -> int: # type: ignore
        """Get the value of common grazing land in calories per hectare."""
        return int(self.mValueCommonGrazingLand)

    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, value: int) -> None:
        """Set the value of common grazing land in calories per hectare."""
        value = int(value)
        if self.mValueCommonGrazingLand != value:
            self.mValueCommonGrazingLand = value
            self.valueCommonGrazingLandChanged.emit(value)

    @pyqtProperty(int, notify=valueSpecificGrazingLandChanged)
    def valueSpecificGrazingLand(self) -> int: # type: ignore
        """Get the value of specific grazing land in calories per hectare."""
        return int(self.mValueSpecificGrazingLand)

    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, value: int) -> None:
        """Set the value of specific grazing land in calories per hectare."""
        value = int(value)
        if self.mValueSpecificGrazingLand != value:
            self.mValueSpecificGrazingLand = value
            self.valueSpecificGrazingLandChanged.emit(value)


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
            self.mFallowUsage = Priority.None_

        self.mRrasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
        return True

    def toXml(self) -> str:
        from la.lib.lautils import LaUtils
        myString = f"<animalParameter guid=\"{self.guid}\">\n"
        # Use both name tags for maximum compatibility
        myString += f"  <name>{LaUtils.xmlEncode(str(self.name))}</name>\n"  # Standard name tag
        myString += f"  <description>{LaUtils.xmlEncode(str(self.description))}</description>\n"
        myString += f"  <animal>{LaUtils.xmlEncode(str(self.animalGuid))}</animal>\n"
        myString += f"  <percentTameMeat>{self.percentTameMeat}</percentTameMeat>\n"
        myString += f"  <useCommonGrazingLand>{self.useCommonGrazingLand}</useCommonGrazingLand>\n"
        myString += f"  <useSpecificGrazingLand>{1 if self.useSpecificGrazingLand else 0}</useSpecificGrazingLand>\n"
        myString += f"  <foodValueOfSpecificGrazingLand>{self.valueSpecificGrazingLand}</foodValueOfSpecificGrazingLand>\n"

        # we need to set mAreaUnits to the string value with match case
        match self.mAreaUnits:
            case AreaUnits.Dunum:
                myString += "  <areaUnits>Dunum</areaUnits>\n"
            case AreaUnits.Hectare:
                myString += "  <areaUnits>Hectare</areaUnits>\n"
            case _:
                myString += "  <areaUnits>Dunum</areaUnits>\n"
        # we need to set mEnergyType to the string value with match case
        match self.mEnergyType:
            case EnergyType.KCalories:
                myString += "  <energyType>KCalories</energyType>\n"
            case EnergyType.TDN:
                myString += "  <energyType>TDN</energyType>\n"
            case _:
                myString += "  <energyType>KCalories</energyType>\n"

        myString += f"  <fodderUse>{self.fodderUse}</fodderUse>\n"

        # Add food source map data
        if self.mFodderUse:
            myString += "   <fodderCrops>\n"
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

        if self.mRrasterName:
            myString += f'<tr><td><b>Raster Mask:</b></td><td>{self.mRrasterName}</td></tr>'

        myString += '</table>'
        return myString
