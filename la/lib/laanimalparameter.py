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
    fodderUseChanged = pyqtSignal(float)
    foodSourceMapChanged = pyqtSignal(dict)
    fallowUsageChanged = pyqtSignal(object)
    rasterNameChanged = pyqtSignal(str)
    areaUnitsChanged = pyqtSignal(object)  # Added signal for area units
    energyTypeChanged = pyqtSignal(object)  # Added signal for energy type
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
            self._mGuid = LaGuid.setGuid(self, None)
            self._mName = "No Name Set"
            self._mDescription = "Not Set"
            self._mAnimalGuid = ""
            self._mPercentTameMeat = 0.0
            self._mUseCommonGrazingLand = False
            self._mUseSpecificGrazingLand = False
            self._mFodderUse = 0.0
            self._mFoodSourceMap: Dict[str, LaFoodSource] = {}
            self._fallowUsage = Priority.None_
            self._rasterName = ""
            self._areaUnits = AreaUnits.Dunum
            self._energyType = EnergyType.KCalories
            # No default values for grazing land productivity, matching C++ implementation
            self._mValueCommonGrazingLand = 0
            self._mValueSpecificGrazingLand = 0
        else:
            # Copy properties with safe type conversion
            self._mGuid = str(getattr(theAnimalParameter, '_mGuid', ''))
            self._mName = str(getattr(theAnimalParameter, '_mName', ''))
            self._mDescription = str(getattr(theAnimalParameter, '_mDescription', ''))
            self._mAnimalGuid = str(getattr(theAnimalParameter, '_mAnimalGuid', ''))
            self._mPercentTameMeat = float(getattr(theAnimalParameter, '_mPercentTameMeat', 0.0))
            self._mUseCommonGrazingLand = bool(getattr(theAnimalParameter, '_mUseCommonGrazingLand', False))
            self._mUseSpecificGrazingLand = bool(getattr(theAnimalParameter, '_mUseSpecificGrazingLand', False))
            self._mFodderUse = float(getattr(theAnimalParameter, '_mFodderUse', 0.0))
            self._mFoodSourceMap = dict(getattr(theAnimalParameter, '_mFoodSourceMap', {}))
            self._fallowUsage = getattr(theAnimalParameter, '_fallowUsage', Priority)
            self._rasterName = str(getattr(theAnimalParameter, '_rasterName', ''))
            self._areaUnits = getattr(theAnimalParameter, '_areaUnits', AreaUnits)
            self._energyType = getattr(theAnimalParameter, '_energyType', EnergyType)
            self._mValueCommonGrazingLand = int(getattr(theAnimalParameter, '_mValueCommonGrazingLand', 0))
            self._mValueSpecificGrazingLand = int(getattr(theAnimalParameter, '_mValueSpecificGrazingLand', 0))

    def __eq__(self, other):
        if not isinstance(other, LaAnimalParameter):
            return False
        myAttributes = [
            '_mGuid',               '_mName',              '_mDescription',
            '_mAnimalGuid',         '_mPercentTameMeat',   '_mUseCommonGrazingLand',
            '_mUseSpecificGrazingLand', '_mFodderUse', '_mFoodSourceMap'
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
        return str(self._mName)

    @name.setter
    def name(self, value: str) -> None:
        """Set the name of the animal parameter."""
        value = str(value)
        if self._mName != value:
            self._mName = value
            self.nameChanged.emit(value)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: # type: ignore
        """Get the description of the animal parameter."""
        return str(self._mDescription)

    @description.setter
    def description(self, value: str) -> None:
        """Set the description of the animal parameter."""
        value = str(value)
        if self._mDescription != value:
            self._mDescription = value
            self.descriptionChanged.emit(value)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self): # type: ignore
        return self._mGuid

    @guid.setter
    def guid(self, guid):
        if self._mGuid != guid:
            self._mGuid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=animalGuidChanged)
    def animalGuid(self) -> str: # type: ignore
        """Get the animal GUID."""
        return str(self._mAnimalGuid)

    @animalGuid.setter
    def animalGuid(self, value: str) -> None:
        """Set the animal GUID."""
        value = str(value)
        if self._mAnimalGuid != value:
            self._mAnimalGuid = value
            self.animalGuidChanged.emit(value)

    @pyqtProperty(float, notify=percentTameMeatChanged)
    def percentTameMeat(self) -> float: # type: ignore
        """Get the percentage of tame meat."""
        return float(self._mPercentTameMeat)

    @percentTameMeat.setter
    def percentTameMeat(self, value: float) -> None:
        """Set the percentage of tame meat."""
        value = float(value)
        if self._mPercentTameMeat != value:
            self._mPercentTameMeat = value
            self.percentTameMeatChanged.emit(value)

    @pyqtProperty(bool, notify=useCommonGrazingLandChanged)
    def useCommonGrazingLand(self) -> bool: # type: ignore
        """Get whether common grazing land is used."""
        return bool(self._mUseCommonGrazingLand)

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, value: bool) -> None:
        """Set whether common grazing land is used."""
        value = bool(value)
        if self._mUseCommonGrazingLand != value:
            self._mUseCommonGrazingLand = value
            self.useCommonGrazingLandChanged.emit(value)

    @pyqtProperty(bool, notify=useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self) -> bool: # type: ignore
        """Get whether specific grazing land is used."""
        return bool(self._mUseSpecificGrazingLand)

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, value: bool) -> None:
        """Set whether specific grazing land is used."""
        value = bool(value)
        if self._mUseSpecificGrazingLand != value:
            self._mUseSpecificGrazingLand = value
            self.useSpecificGrazingLandChanged.emit(value)

    @pyqtProperty(float, notify=fodderUseChanged)
    def fodderUse(self) -> float: # type: ignore
        """Get the fodder use value."""
        return float(self._mFodderUse)

    @fodderUse.setter
    def fodderUse(self, value: float) -> None:
        """Set the fodder use value."""
        value = float(value)
        if self._mFodderUse != value:
            self._mFodderUse = value
            self.fodderUseChanged.emit(value)

    @pyqtProperty('QVariantMap', notify=foodSourceMapChanged)
    def foodSourceMap(self) -> Dict[str, LaFoodSource]: # type: ignore
        """Get the food source map."""
        return dict(self._mFoodSourceMap)

    def fodderSourceMap(self) -> Dict[str, LaFoodSource]:
        """Get the fodder source map. This is an alias for foodSourceMap for compatibility with C++ code."""
        return dict(self._mFoodSourceMap)

    @foodSourceMap.setter
    def foodSourceMap(self, value: Dict[str, LaFoodSource]) -> None:
        """Set the food source map."""
        value = dict(value)
        if self._mFoodSourceMap != value:
            self._mFoodSourceMap = value
            self.foodSourceMapChanged.emit(value)

    @pyqtProperty(object, notify=fallowUsageChanged)
    def fallowUsage(self) -> Priority: # type: ignore
        """Get the fallow usage priority."""
        return Priority(self._fallowUsage)

    @fallowUsage.setter
    def fallowUsage(self, value: Priority) -> None:
        """Set the fallow usage priority."""
        if isinstance(value, Priority) and self._fallowUsage != value:
            self._fallowUsage = value
            self.fallowUsageChanged.emit(value)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self): # type: ignore
        return self._rasterName

    @rasterName.setter
    def rasterName(self, rasterName):
        if self._rasterName != rasterName:
            self._rasterName = rasterName
            self.rasterNameChanged.emit(rasterName)

    @pyqtProperty(object, notify=areaUnitsChanged)  # Updated to use signal
    def areaUnits(self) -> AreaUnits: # type: ignore
        """Get the area units."""
        return AreaUnits(self._areaUnits)

    @areaUnits.setter
    def areaUnits(self, value: AreaUnits) -> None:
        """Set the area units."""
        if isinstance(value, AreaUnits) and self._areaUnits != value:
            self._areaUnits = value
            self.areaUnitsChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(object, notify=energyTypeChanged)  # Updated to use signal
    def energyType(self) -> EnergyType: # type: ignore
        """Get the energy type."""
        return EnergyType(self._energyType)

    @energyType.setter
    def energyType(self, value: EnergyType) -> None:
        """Set the energy type."""
        if isinstance(value, EnergyType) and self._energyType != value:
            self._energyType = value
            self.energyTypeChanged.emit(value)  # Emit signal when value changes

    @pyqtProperty(int, notify=valueCommonGrazingLandChanged)
    def valueCommonGrazingLand(self) -> int: # type: ignore
        """Get the value of common grazing land in calories per hectare."""
        return int(self._mValueCommonGrazingLand)

    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, value: int) -> None:
        """Set the value of common grazing land in calories per hectare."""
        value = int(value)
        if self._mValueCommonGrazingLand != value:
            self._mValueCommonGrazingLand = value
            self.valueCommonGrazingLandChanged.emit(value)

    @pyqtProperty(int, notify=valueSpecificGrazingLandChanged)
    def valueSpecificGrazingLand(self) -> int: # type: ignore
        """Get the value of specific grazing land in calories per hectare."""
        return int(self._mValueSpecificGrazingLand)

    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, value: int) -> None:
        """Set the value of specific grazing land in calories per hectare."""
        value = int(value)
        if self._mValueSpecificGrazingLand != value:
            self._mValueSpecificGrazingLand = value
            self.valueSpecificGrazingLandChanged.emit(value)


    def fromXml(self, theXml: str) -> bool:
        from la.lib.lautils import LaUtils
        try:
            LaUtils.debug.log(f"Loading animal parameter XML, first 100 chars: {theXml[:100]}")
            myDocument = QDomDocument("mydocument")
            myDocument.setContent(theXml)
            myTopElement = myDocument.firstChildElement("animalParameter")
            if myTopElement.isNull():
                warnings.warn("Failed to parse XML: myTopElement is null. The XML element could not be found or parsed.")
                return False

            # Get GUID directly from the XML attribute
            guid_value = myTopElement.attribute("guid")
            if guid_value:
                self._mGuid = str(guid_value)  # Ensure it's a string
                LaUtils.debug.log(f"Loading animal parameter with GUID: {self._mGuid}")
            else:
                LaUtils.debug.log("No GUID found in XML, generating a new one")
                import uuid
                self._mGuid = str(uuid.uuid4())
                LaUtils.debug.log(f"Generated new GUID: {self._mGuid}")

            # Check for both name tag styles (<name> and <n>)
            nameElement = myTopElement.firstChildElement("name")
            if nameElement.isNull():
                nameElement = myTopElement.firstChildElement("n")

            self._mName = LaUtils.xmlDecode(nameElement.text())
            LaUtils.debug.log(f"Loaded animal parameter name: {self._mName}")

            # Continue with the rest of the XML parsing
            descriptionElement = myTopElement.firstChildElement("description")
            self._mDescription = LaUtils.xmlDecode(descriptionElement.text()) if not descriptionElement.isNull() else ""

            animalElement = myTopElement.firstChildElement("animal")
            self._mAnimalGuid = LaUtils.xmlDecode(animalElement.text()) if not animalElement.isNull() else ""

            # Parse numeric values safely
            try:
                percentElement = myTopElement.firstChildElement("percentTameMeat")
                self._mPercentTameMeat = float(percentElement.text()) if not percentElement.isNull() else 0.0
            except (ValueError, TypeError):
                self._mPercentTameMeat = 0.0
                LaUtils.debug.log("Failed to parse percentTameMeat, using 0.0")

            # Parse boolean values safely
            useCommonElement = myTopElement.firstChildElement("useCommonGrazingLand")
            self._mUseCommonGrazingLand = bool(int(useCommonElement.text())) if not useCommonElement.isNull() else False

            useSpecificElement = myTopElement.firstChildElement("useSpecificGrazingLand")
            self._mUseSpecificGrazingLand = bool(int(useSpecificElement.text())) if not useSpecificElement.isNull() else False

            fodderUseElement = myTopElement.firstChildElement("fodderUse")
            self._mFodderUse = float(fodderUseElement.text()) if not fodderUseElement.isNull() else 0.0

            # Parse food source map from XML
            self._mFoodSourceMap = {}  # Initialize as empty LaFoodSourceMap
            if self._mFodderUse:
                # Check both "fodderCrops" (Python version) and older "fodderCrop" (C++ version) tags
                fodderCropsElement = myTopElement.firstChildElement("fodderCrops")
                if fodderCropsElement.isNull():
                    # Try alternate tag
                    fodderCropsElement = myTopElement.firstChildElement("fodderCrop")

                if not fodderCropsElement.isNull():
                    # Try different possible element names for individual food sources
                    foodSourceNode = fodderCropsElement.firstChildElement("foodSource")
                    if foodSourceNode.isNull():
                        foodSourceNode = fodderCropsElement.firstChildElement("fodderCrop")

                    while not foodSourceNode.isNull():
                        myFoodSource = LaFoodSource()

                        # First check for "fodderCropGuid" then fall back to "cropGuid"
                        guidElement = foodSourceNode.firstChildElement("fodderCropGuid")
                        if guidElement.isNull():
                            guidElement = foodSourceNode.firstChildElement("cropGuid")

                        cropGuid = guidElement.text()
                        myFoodSource.cropGuid = cropGuid

                        # Handle different tag names between C++ and Python versions
                        fodderElement = foodSourceNode.firstChildElement("fodderStrawChaff")
                        myFoodSource.fodder = int(fodderElement.text()) if not fodderElement.isNull() else 0

                        grainElement = foodSourceNode.firstChildElement("fodderGrain")
                        myFoodSource.grain = int(grainElement.text()) if not grainElement.isNull() else 0

                        daysElement = foodSourceNode.firstChildElement("fodderDays")
                        myFoodSource.days = int(daysElement.text()) if not daysElement.isNull() else 0

                        usedElement = foodSourceNode.firstChildElement("fodderUse")
                        if usedElement.isNull():
                            usedElement = foodSourceNode.firstChildElement("used")
                        myFoodSource.used = bool(int(usedElement.text())) if not usedElement.isNull() else False

                        # Insert data into LaFoodSourceMap
                        self._mFoodSourceMap[cropGuid] = myFoodSource
                        LaUtils.debug.log(f"Added food source with guid {cropGuid} to parameter {self._mName}")

                        # Move to next food source
                        prevNode = foodSourceNode
                        foodSourceNode = foodSourceNode.nextSiblingElement("foodSource")
                        if foodSourceNode.isNull():
                            foodSourceNode = prevNode.nextSiblingElement("fodderCrop")

            # Handle fallowUsage as a Priority enum - carefully handle various formats
            fallowUsageElement = myTopElement.firstChildElement("fallowUsage")
            if not fallowUsageElement.isNull():
                fallowUsageText = fallowUsageElement.text()
                if fallowUsageText.upper() == "HIGH":
                    self._fallowUsage = Priority.High
                elif fallowUsageText.upper() == "MEDIUM":
                    self._fallowUsage = Priority.Medium
                elif fallowUsageText.upper() == "LOW":
                    self._fallowUsage = Priority.Low
                else:
                    self._fallowUsage = Priority.None_
            else:
                self._fallowUsage = Priority.None_

            # Get raster name with proper fallback
            rasterNameElement = myTopElement.firstChildElement("rasterName")
            if rasterNameElement.isNull():
                rasterNameElement = myTopElement.firstChildElement("RasterName")
            self._rasterName = LaUtils.xmlDecode(rasterNameElement.text()) if not rasterNameElement.isNull() else ""

            LaUtils.debug.log(f"Successfully loaded animal parameter: {self._mName}")
            return True
        except Exception as e:
            LaUtils.debug.log(f"Error loading animal parameter from XML: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())
            return False

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
        if self._mFodderUse and self._mFoodSourceMap:
            myString += "  <fodderCrops>\n"
            for cropGuid, foodSource in dict(self._mFoodSourceMap).items():
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
        if self._fallowUsage == Priority.High:
            fallowUsageStr = "High"
        elif self._fallowUsage == Priority.Medium:
            fallowUsageStr = "Medium"
        elif self._fallowUsage == Priority.Low:
            fallowUsageStr = "Low"

        myString += f"  <fallowUsage>{fallowUsageStr}</fallowUsage>\n"
        myString += f"  <rasterName>{LaUtils.xmlEncode(str(self.rasterName))}</rasterName>\n"
        myString += "</animalParameter>\n"
        return myString

    def toHtml(self) -> str:
        """Generate HTML table representation of animal parameter data.

        Returns:
            HTML string containing formatted parameter attributes
        """
        from la.lib.lautils import LaUtils  # Import here to avoid circular imports
        myString = f'<h2>Details for {LaUtils.xmlEncode(str(self._mName))}</h2>'
        myString += '<table>'
        myString += f'<tr><td><b>Description:</b></td><td>{self._mDescription}</td></tr>'
        myString += f'<tr><td><b>Percentage of Tame Meat:</b></td><td>{self._mPercentTameMeat}</td></tr>'
        myString += f'<tr><td><b>Use Common Grazing Land:</b></td><td>{self._mUseCommonGrazingLand}</td></tr>'
        myString += f'<tr><td><b>Use Specific Grazing Land:</b></td><td>{self._mUseSpecificGrazingLand}</td></tr>'

        if self._mFodderUse:
            myString += '<tr><td><b>Uses Fodder:</b></td><td>Yes</td></tr>'
            if self._mFoodSourceMap:
                myString += '<tr><td colspan="2"><b>Food Sources:</b></td></tr>'
                counter = 0
                for cropGuid, foodSource in self._mFoodSourceMap.items():
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
            if self._fallowUsage == Priority.High:
                fallowUsageStr = "High"
            elif self._fallowUsage == Priority.Medium:
                fallowUsageStr = "Medium"
            elif self._fallowUsage == Priority.Low:
                fallowUsageStr = "Low"

        myString += f'<tr><td><b>Fallow Usage:</b></td><td>{fallowUsageStr}</td></tr>'

        if self._rasterName:
            myString += f'<tr><td><b>Raster Mask:</b></td><td>{self._rasterName}</td></tr>'

        myString += '</table>'
        return myString