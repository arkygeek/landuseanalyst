# ladietlabels.py
import copy
from typing import Dict, Tuple
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.lautils import LaUtils
from la.lib.la import AreaUnits, EnergyType, Status

class LaDietLabels(QObject, LaSerialisable, LaGuid):
    """
    LaDietLabels class for managing dietary information in the Land Use Analyst.

    This class handles the calculation and storage of dietary information including
    caloric values from different food sources, portion percentages, and annual
    caloric requirements. It provides properties for accessing and modifying these
    values, with signal emission when values change.

    Inherits from:
        LaSerialisable: Provides serialization capabilities
        LaGuid: Provides unique identifier functionality
    """
    _dairyMCaloriesChanged = pyqtSignal(float)
    _cropMCaloriesChanged = pyqtSignal(float)
    _animalMCaloriesChanged = pyqtSignal(float)
    _wildAnimalMCaloriesChanged = pyqtSignal(float)
    _wildPlantsMCaloriesChanged = pyqtSignal(float)
    _dairyPortionPctChanged = pyqtSignal(float)
    _tameMeatPortionPctChanged = pyqtSignal(float)
    _cropsPortionPctChanged = pyqtSignal(float)
    _wildAnimalPortionPctChanged = pyqtSignal(float)
    _wildPlantsPortionPctChanged = pyqtSignal(float)
    _plantsPortionPctChanged = pyqtSignal(float)
    _animalPortionPctChanged = pyqtSignal(float)
    _kiloCalsIndividualAnnualChanged = pyqtSignal(float)
    _megaCalSettlementAnnualChanged = pyqtSignal(float)
    _dairySurplusMCaloriesChanged = pyqtSignal(float)
    _cropAreaTargetsMapChanged = pyqtSignal(dict)
    _animalAreaTargetsMapChanged = pyqtSignal(dict)
    _cropCalcsReportMapChanged = pyqtSignal(dict)
    _animalCalcsReportMapChanged = pyqtSignal(dict)

    def __init__(self, parent=None):
        """
        Initialize a new LaDietLabels instance with default values.

        All numeric values are initialized to 0.0 and dictionaries are empty.
        """
        super().__init__(parent)
        LaSerialisable.__init__(self)
        LaGuid.__init__(self)

        self._dairyMCalories: float = 0.0
        self._cropMCalories: float = 0.0
        self._animalMCalories: float = 0.0
        self._wildAnimalMCalories: float = 0.0
        self._wildPlantsMCalories: float = 0.0
        self._dairyPortionPct: float = 0.0
        self._tameMeatPortionPct: float = 0.0
        self._cropsPortionPct: float = 0.0
        self._wildAnimalPortionPct: float = 0.0
        self._wildPlantsPortionPct: float = 0.0
        self._plantsPortionPct: float = 0.0
        self._animalPortionPct: float = 0.0
        self._kiloCaloriesIndividualAnnual: float = 0.0
        self._megaCaloriesSettlementAnnual: float = 0.0
        self._dairySurplusMCalories: float = 0.0
        self._cropAreaTargetsMap = {}  # Map of crop GUID to area target
        self._animalAreaTargetsMap = {}  # Map of animal GUID to area target
        self._cropCalcsReportMap: Dict[str, Tuple[str, float]] = {}
        self._animalCalcsReportMap: Dict[str, Tuple[str, float]] = {}
        LaUtils.debug.log("LaDietLabels initialized with default values", "Diet")

    def __del__(self):
        """
        Destructor method for the LaDietLabels class.
        """
        pass

    def __copy__(self):
        """
        Create a shallow copy of this LaDietLabels instance.

        :return: A new LaDietLabels instance with the same values
        :rtype: LaDietLabels
        """
        other = LaDietLabels()
        other.__dict__.update(self.__dict__)
        return other

    def __deepcopy__(self, memo):
        """
        Create a deep copy of this LaDietLabels instance.

        :param memo: Dictionary of id to object references
        :type memo: dict
        :return: A new LaDietLabels instance with copies of all values
        :rtype: LaDietLabels
        """
        other = LaDietLabels()
        memo[id(self)] = other
        for k, v in self.__dict__.items():
            setattr(other, k, copy.deepcopy(v, memo))
        return other

    @pyqtProperty(float, notify=_dairyMCaloriesChanged)
    def dairyMCalories(self) -> float: # type: ignore
        """
        Get the dairy mega-calories value.

        :return: The dairy mega-calories value
        :rtype: float
        """
        return float(str(self._dairyMCalories))

    @dairyMCalories.setter
    def dairyMCalories(self, theDairyMCalories: float) -> None:
        """
        Set the dairy mega-calories value and emit a signal if changed.

        :param theDairyMCalories: The new dairy mega-calories value
        :type theDairyMCalories: float
        """
        if self._dairyMCalories != theDairyMCalories:
            self._dairyMCalories = theDairyMCalories
            self._dairyMCaloriesChanged.emit(theDairyMCalories)

    @pyqtProperty(float, notify=_cropMCaloriesChanged)
    def cropMCalories(self) -> float: # type: ignore
        """
        Get the crop mega-calories value.

        :return: The crop mega-calories value
        :rtype: float
        """
        return self._cropMCalories

    @cropMCalories.setter
    def cropMCalories(self, theCropMCalories: float) -> None:
        """
        Set the crop mega-calories value and emit a signal if changed.

        :param theCropMCalories: The new crop mega-calories value
        :type theCropMCalories: float
        """
        if self._cropMCalories != theCropMCalories:
            self._cropMCalories = theCropMCalories
            self._cropMCaloriesChanged.emit(theCropMCalories)

    @pyqtProperty(float, notify=_animalMCaloriesChanged)
    def animalMCalories(self) -> float: # type: ignore
        """
        Get the animal mega-calories value.

        :return: The animal mega-calories value
        :rtype: float
        """
        return self._animalMCalories

    @animalMCalories.setter
    def animalMCalories(self, theAnimalMCalories: float) -> None:
        """
        Set the animal mega-calories value and emit a signal if changed.

        :param theAnimalMCalories: The new animal mega-calories value
        :type theAnimalMCalories: float
        """
        if self._animalMCalories != theAnimalMCalories:
            self._animalMCalories = theAnimalMCalories
            self._animalMCaloriesChanged.emit(theAnimalMCalories)

    @pyqtProperty(float, notify=_wildAnimalMCaloriesChanged)
    def wildAnimalMCalories(self) -> float: # type: ignore
        """
        Get the wild animal mega-calories value.

        :return: The wild animal mega-calories value
        :rtype: float
        """
        return self._wildAnimalMCalories

    @wildAnimalMCalories.setter
    def wildAnimalMCalories(self, theWildAnimalMCalories: float) -> None:
        """
        Set the wild animal mega-calories value and emit a signal if changed.

        :param theWildAnimalMCalories: The new wild animal mega-calories value
        :type theWildAnimalMCalories: float
        """
        if self._wildAnimalMCalories != theWildAnimalMCalories:
            self._wildAnimalMCalories = theWildAnimalMCalories
            self._wildAnimalMCaloriesChanged.emit(theWildAnimalMCalories)

    @pyqtProperty(float, notify=_wildPlantsMCaloriesChanged)
    def wildPlantsMCalories(self) -> float: # type: ignore
        """
        Get the wild plants mega-calories value.

        :return: The wild plants mega-calories value
        :rtype: float
        """
        return self._wildPlantsMCalories

    @wildPlantsMCalories.setter
    def wildPlantsMCalories(self, theWildPlantsMCalories: float) -> None:
        """
        Set the wild plants mega-calories value and emit a signal if changed.

        :param theWildPlantsMCalories: The new wild plants mega-calories value
        :type theWildPlantsMCalories: float
        """
        if self._wildPlantsMCalories != theWildPlantsMCalories:
            self._wildPlantsMCalories = theWildPlantsMCalories
            self._wildPlantsMCaloriesChanged.emit(theWildPlantsMCalories)

    @pyqtProperty(float, notify=_dairyPortionPctChanged)
    def dairyPortionPct(self) -> float: # type: ignore
        """
        Get the dairy portion percentage value.

        :return: The dairy portion percentage value
        :rtype: float
        """
        return self._dairyPortionPct

    @dairyPortionPct.setter
    def dairyPortionPct(self, theDairyPortionPct: float) -> None:
        """
        Set the dairy portion percentage value and emit a signal if changed.

        :param theDairyPortionPct: The new dairy portion percentage value
        :type theDairyPortionPct: float
        """
        if self._dairyPortionPct != theDairyPortionPct:
            self._dairyPortionPct = theDairyPortionPct
            self._dairyPortionPctChanged.emit(theDairyPortionPct)

    @pyqtProperty(float, notify=_tameMeatPortionPctChanged)
    def tameMeatPortionPct(self) -> float: # type: ignore
        """
        Get the domesticated meat portion percentage value.

        :return: The domesticated meat portion percentage value
        :rtype: float
        """
        return self._tameMeatPortionPct

    @tameMeatPortionPct.setter
    def tameMeatPortionPct(self, theTameMeatPortionPct: float) -> None:
        """
        Set the domesticated meat portion percentage value and emit a signal if changed.

        :param theTameMeatPortionPct: The new domesticated meat portion percentage value
        :type theTameMeatPortionPct: float
        """
        if self._tameMeatPortionPct != theTameMeatPortionPct:
            self._tameMeatPortionPct = theTameMeatPortionPct
            self._tameMeatPortionPctChanged.emit(theTameMeatPortionPct)

    @pyqtProperty(float, notify=_cropsPortionPctChanged)
    def cropsPortionPct(self) -> float: # type: ignore
        """
        Get the crops portion percentage value.

        :return: The crops portion percentage value
        :rtype: float
        """
        return self._cropsPortionPct

    @cropsPortionPct.setter
    def cropsPortionPct(self, theCropsPortionPct: float) -> None:
        """
        Set the crops portion percentage value and emit a signal if changed.

        :param theCropsPortionPct: The new crops portion percentage value
        :type theCropsPortionPct: float
        """
        if self._cropsPortionPct != theCropsPortionPct:
            self._cropsPortionPct = theCropsPortionPct
            self._cropsPortionPctChanged.emit(theCropsPortionPct)

    @pyqtProperty(float, notify=_wildAnimalPortionPctChanged)
    def wildAnimalPortionPct(self) -> float: # type: ignore
        """
        Get the wild animal portion percentage value.

        :return: The wild animal portion percentage value
        :rtype: float
        """
        return self._wildAnimalPortionPct

    @wildAnimalPortionPct.setter
    def wildAnimalPortionPct(self, theWildAnimalPortionPct: float) -> None:
        """
        Set the wild animal portion percentage value and emit a signal if changed.

        :param theWildAnimalPortionPct: The new wild animal portion percentage value
        :type theWildAnimalPortionPct: float
        """
        if self._wildAnimalPortionPct != theWildAnimalPortionPct:
            self._wildAnimalPortionPct = theWildAnimalPortionPct
            self._wildAnimalPortionPctChanged.emit(theWildAnimalPortionPct)

    @pyqtProperty(float, notify=_wildPlantsPortionPctChanged)
    def wildPlantsPortionPct(self) -> float: # type: ignore
        """
        Get the wild plants portion percentage value.

        :return: The wild plants portion percentage value
        :rtype: float
        """
        return self._wildPlantsPortionPct

    @wildPlantsPortionPct.setter
    def wildPlantsPortionPct(self, theWildPlantsPortionPct: float) -> None:
        """
        Set the wild plants portion percentage value and emit a signal if changed.

        :param theWildPlantsPortionPct: The new wild plants portion percentage value
        :type theWildPlantsPortionPct: float
        """
        if self._wildPlantsPortionPct != theWildPlantsPortionPct:
            self._wildPlantsPortionPct = theWildPlantsPortionPct
            self._wildPlantsPortionPctChanged.emit(theWildPlantsPortionPct)

    @pyqtProperty(float, notify=_plantsPortionPctChanged)
    def plantsPortionPct(self) -> float: # type: ignore
        """
        Get the plants portion percentage value (both wild and cultivated).

        :return: The plants portion percentage value
        :rtype: float
        """
        return self._plantsPortionPct

    @plantsPortionPct.setter
    def plantsPortionPct(self, thePlantsPortionPct: float) -> None:
        """
        Set the plants portion percentage value and emit a signal if changed.

        :param thePlantsPortionPct: The new plants portion percentage value
        :type thePlantsPortionPct: float
        """
        if self._plantsPortionPct != thePlantsPortionPct:
            self._plantsPortionPct = thePlantsPortionPct
            self._plantsPortionPctChanged.emit(thePlantsPortionPct)

    @pyqtProperty(float, notify=_animalPortionPctChanged)
    def animalPortionPct(self) -> float: # type: ignore
        """
        Get the animal portion percentage value (both wild and domestic).

        :return: The animal portion percentage value
        :rtype: float
        """
        return self._animalPortionPct

    @animalPortionPct.setter
    def animalPortionPct(self, theAnimalPortionPct: float) -> None:
        """
        Set the animal portion percentage value and emit a signal if changed.

        :param theAnimalPortionPct: The new animal portion percentage value
        :type theAnimalPortionPct: float
        """
        if self._animalPortionPct != theAnimalPortionPct:
            self._animalPortionPct = theAnimalPortionPct
            self._animalPortionPctChanged.emit(theAnimalPortionPct)

    @pyqtProperty(float, notify=_kiloCalsIndividualAnnualChanged)
    def kiloCaloriesIndividualAnnual(self) -> float: # type: ignore
        """
        Get the individual annual kilocalories requirement.

        :return: The individual annual kilocalories requirement
        :rtype: float
        """
        return self._kiloCaloriesIndividualAnnual

    @kiloCaloriesIndividualAnnual.setter
    def kiloCaloriesIndividualAnnual(self, theKiloCaloriesIndividualAnnual: float) -> None:
        """
        Set the individual annual kilocalories requirement and emit a signal if changed.

        :param theKiloCaloriesIndividualAnnual: The new individual annual kilocalories requirement
        :type theKiloCaloriesIndividualAnnual: float
        """
        if self._kiloCaloriesIndividualAnnual != theKiloCaloriesIndividualAnnual:
            self._kiloCaloriesIndividualAnnual = theKiloCaloriesIndividualAnnual
            self._kiloCalsIndividualAnnualChanged.emit(theKiloCaloriesIndividualAnnual)

    @pyqtProperty(float, notify=_megaCalSettlementAnnualChanged)
    def megaCaloriesSettlementAnnual(self) -> float: # type: ignore
        """
        Get the settlement annual megacalories requirement.

        :return: The settlement annual megacalories requirement
        :rtype: float
        """
        return self._megaCaloriesSettlementAnnual

    @megaCaloriesSettlementAnnual.setter
    def megaCaloriesSettlementAnnual(self, theMegaCaloriesSettlementAnnual: float) -> None:
        """
        Set the settlement annual megacalories requirement and emit a signal if changed.

        :param theMegaCaloriesSettlementAnnual: The new settlement annual megacalories requirement
        :type theMegaCaloriesSettlementAnnual: float
        """
        if self._megaCaloriesSettlementAnnual != theMegaCaloriesSettlementAnnual:
            self._megaCaloriesSettlementAnnual = theMegaCaloriesSettlementAnnual
            self._megaCalSettlementAnnualChanged.emit(theMegaCaloriesSettlementAnnual)

    @pyqtProperty(float, notify=_dairySurplusMCaloriesChanged)
    def dairySurplusMCalories(self) -> float: # type: ignore
        """
        Get the dairy surplus megacalories value.

        :return: The dairy surplus megacalories value
        :rtype: float
        """
        return self._dairySurplusMCalories

    @dairySurplusMCalories.setter
    def dairySurplusMCalories(self, theDairySurplusMCalories: float) -> None:
        """
        Set the dairy surplus megacalories value and emit a signal if changed.

        :param theDairySurplusMCalories: The new dairy surplus megacalories value
        :type theDairySurplusMCalories: float
        """
        if self._dairySurplusMCalories != theDairySurplusMCalories:
            self._dairySurplusMCalories = theDairySurplusMCalories
            self._dairySurplusMCaloriesChanged.emit(theDairySurplusMCalories)

    @pyqtProperty(dict, notify=_cropAreaTargetsMapChanged)
    def cropAreaTargetsMap(self) -> Dict[str, float]: # type: ignore
        """
        Get the crop area targets map.
        :return: A dictionary mapping crop GUIDs to area targets
        :rtype: Dict[str, float]
        """
        return self._cropAreaTargetsMap
    @cropAreaTargetsMap.setter
    def cropAreaTargetsMap(self, theCropAreaTargetsMap: Dict[str, float]) -> None:
        """
        Set the crop area targets map and emit a signal if changed.

        :param theCropAreaTargetsMap: The new crop area targets map
        :type theCropAreaTargetsMap: Dict[str, float]
        """
        if self._cropAreaTargetsMap != theCropAreaTargetsMap:
            self._cropAreaTargetsMap = theCropAreaTargetsMap
            self._cropAreaTargetsMapChanged.emit(theCropAreaTargetsMap)
    @pyqtProperty(dict, notify=_animalAreaTargetsMapChanged)
    def animalAreaTargetsMap(self) -> Dict[str, float]: # type: ignore
        """
        Get the animal area targets map.
        :return: A dictionary mapping animal GUIDs to area targets
        :rtype: Dict[str, float]
        """
        return self._animalAreaTargetsMap
    @animalAreaTargetsMap.setter
    def animalAreaTargetsMap(self, theAnimalAreaTargetsMap: Dict[str, float]) -> None:
        """
        Set the animal area targets map and emit a signal if changed.

        :param theAnimalAreaTargetsMap: The new animal area targets map
        :type theAnimalAreaTargetsMap: Dict[str, float]
        """
        if self._animalAreaTargetsMap != theAnimalAreaTargetsMap:
            self._animalAreaTargetsMap = theAnimalAreaTargetsMap
            self._animalAreaTargetsMapChanged.emit(theAnimalAreaTargetsMap)

    @pyqtProperty(dict, notify=_cropCalcsReportMapChanged)
    def cropCalcsReportMap(self) -> Dict[str, Tuple[str, float]]: # type: ignore
        """
        Get the crop calculations report map.

        :return: A dictionary mapping strings to tuples of (string, float)
        :rtype: Dict[str, Tuple[str, float]]
        """
        return self._cropCalcsReportMap

    @cropCalcsReportMap.setter
    def cropCalcsReportMap(self, theCropCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """
        Set the crop calculations report map and emit a signal if changed.

        :param theCropCalcsReportMap: The new crop calculations report map
        :type theCropCalcsReportMap: Dict[str, Tuple[str, float]]
        """
        if self._cropCalcsReportMap != theCropCalcsReportMap:
            self._cropCalcsReportMap = theCropCalcsReportMap
            self._cropCalcsReportMapChanged.emit(theCropCalcsReportMap)

    @pyqtProperty(dict, notify=_animalCalcsReportMapChanged)
    def animalCalcsReportMap(self) -> Dict[str, Tuple[str, float]]: # type: ignore
        """
        Get the animal calculations report map.

        :return: A dictionary mapping strings to tuples of (string, float)
        :rtype: Dict[str, Tuple[str, float]]
        """
        return self._animalCalcsReportMap

    @animalCalcsReportMap.setter
    def animalCalcsReportMap(self, theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """
        Set the animal calculations report map and emit a signal if changed.

        :param theAnimalCalcsReportMap: The new animal calculations report map
        :type theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]
        """
        if self._animalCalcsReportMap != theAnimalCalcsReportMap:
            self._animalCalcsReportMap = theAnimalCalcsReportMap
            self._animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)

    def calculateFodderNeeds(self, animalGuid, animalParameter, herdSize):
        """Calculate fodder needs for an animal's herd.
        
        Args:
            animalGuid: The GUID of the animal
            animalParameter: The animal parameter containing fodder settings
            herdSize: Dictionary of herd size components (mothers, offspring, etc.)
        
        Returns:
            Dictionary mapping crop GUIDs to additional kg needed for fodder
        """
        fodderNeeds = {}
        
        # Skip if animal doesn't use fodder
        if not animalParameter.fodderUse:
            return fodderNeeds
            
        # Get the fodder source map
        fodderSourceMap = animalParameter.fodderSourceMap
        
        # For each fodder source
        for cropGuid, foodSource in fodderSourceMap.items():
            # Get crop info
            crop = LaUtils.getCrop(cropGuid)
            if crop is None:
                continue
                
            # Calculate daily fodder/grain needs
            dailyFodderKcal = foodSource.fodder * foodSource.fodderValue
            dailyGrainKcal = foodSource.grain * foodSource.grainValue
            
            # Calculate total requirements based on herd composition
            # This should account for different animals in the herd having
            # different requirements (mothers, males, offspring)
            totalDays = foodSource.days
            totalAnimals = (herdSize['mothers'] + herdSize['males'] + 
                            herdSize['offspring'] + herdSize['motherReplacements'] +
                            herdSize['maleReplacements'])
            
            # Total KCal needed as fodder/grain from this crop
            totalKcalNeeded = (dailyFodderKcal + dailyGrainKcal) * totalDays * totalAnimals
            
            # Convert to kg based on crop calories/fodder value
            if crop.cropCalories > 0:
                kgNeeded = totalKcalNeeded / crop.cropCalories
                
                # Add to the fodder needs map
                if cropGuid in fodderNeeds:
                    fodderNeeds[cropGuid] += kgNeeded
                else:
                    fodderNeeds[cropGuid] = kgNeeded
                    
        return fodderNeeds

    def calculateAnimalAreaTarget(self, theAnimalGuid, theAnimalParameter, theAdjustedFeedRequirement):
        """Calculate grazing area needed for an animal.
        
        Args:
            animalGuid: The GUID of the animal
            animalParameter: The animal parameter
            adjustedFeedRequirement: The feed requirement adjusted for fallow/fodder
        
        Returns:
            The calculated area target in area units
        """
        # Determine land productivity value based on parameter settings
        myLandValue = 0.0
        
        if theAnimalParameter.useCommonGrazingLand:
            # Use common grazing land value
            if self.landSpecificEnergyType == EnergyType.KCalories:
                myLandValue = self.commonLandValue  # KCal/area unit
            else:
                # Handle TDN case appropriately
                myLandValue = self.commonLandValue  # TDN/area unit
        elif theAnimalParameter.useSpecificGrazingLand:
            # Use specific grazing land value
            if self.specificLandEnergyType == EnergyType.KCalories:
                myLandValue = theAnimalParameter.valueSpecificGrazingLand  # KCal/area unit
            else:
                # Handle TDN case appropriately
                myLandValue = theAnimalParameter.valueSpecificGrazingLand  # TDN/area unit
        
        if myLandValue <= 0:
            return 0.0  # Cannot calculate area if land value is zero or negative
        
        # Calculate grazing area by dividing adjusted requirement by land value
        # NOTE: No arbitrary conversion factor needed - use the requirement directly
        grazingAreaNeeded = theAdjustedFeedRequirement / myLandValue
        
        return grazingAreaNeeded

    def toXml(self) -> str:
        """Convert the diet labels to XML format.

        Returns:
            str: XML representation of the diet labels
        """
        xml = f'<dietLabels guid="{self.guid}">\n'
        xml += f'  <dairyMCalories>{self._dairyMCalories}</dairyMCalories>\n'
        xml += f'  <cropMCalories>{self._cropMCalories}</cropMCalories>\n'
        xml += f'  <animalMCalories>{self._animalMCalories}</animalMCalories>\n'
        xml += f'  <wildAnimalMCalories>{self._wildAnimalMCalories}</wildAnimalMCalories>\n'
        xml += f'  <wildPlantsMCalories>{self._wildPlantsMCalories}</wildPlantsMCalories>\n'
        xml += f'  <dairyPortionPct>{self._dairyPortionPct}</dairyPortionPct>\n'
        xml += f'  <tameMeatPortionPct>{self._tameMeatPortionPct}</tameMeatPortionPct>\n'
        xml += f'  <cropsPortionPct>{self._cropsPortionPct}</cropsPortionPct>\n'
        xml += f'  <wildAnimalPortionPct>{self._wildAnimalPortionPct}</wildAnimalPortionPct>\n'
        xml += f'  <wildPlantsPortionPct>{self._wildPlantsPortionPct}</wildPlantsPortionPct>\n'
        xml += f'  <plantsPortionPct>{self._plantsPortionPct}</plantsPortionPct>\n'
        xml += f'  <animalPortionPct>{self._animalPortionPct}</animalPortionPct>\n'
        xml += f'  <kiloCaloriesIndividualAnnual>{self._kiloCaloriesIndividualAnnual}</kiloCaloriesIndividualAnnual>\n'
        xml += f'  <megaCaloriesSettlementAnnual>{self._megaCaloriesSettlementAnnual}</megaCaloriesSettlementAnnual>\n'
        xml += f'  <dairySurplusMCalories>{self._dairySurplusMCalories}</dairySurplusMCalories>\n'
        xml += '</dietLabels>\n'
        return xml

    def fromXml(self, xmlStr: str) -> None:
        """Initialize this object from XML data.

        Args:
            xmlStr (str): XML string containing diet label data
        """
        import xml.etree.ElementTree as ET
        root = ET.fromstring(xmlStr)

        self.setGuid(root.attrib.get('guid', ''))
        self._dairyMCalories = float(root.findtext('dairyMCalories', '0'))
        self._cropMCalories = float(root.findtext('cropMCalories', '0'))
        self._animalMCalories = float(root.findtext('animalMCalories', '0'))
        self._wildAnimalMCalories = float(root.findtext('wildAnimalMCalories', '0'))
        self._wildPlantsMCalories = float(root.findtext('wildPlantsMCalories', '0'))
        self._dairyPortionPct = float(root.findtext('dairyPortionPct', '0'))
        self._tameMeatPortionPct = float(root.findtext('tameMeatPortionPct', '0'))
        self._cropsPortionPct = float(root.findtext('cropsPortionPct', '0'))
        self._wildAnimalPortionPct = float(root.findtext('wildAnimalPortionPct', '0'))
        self._wildPlantsPortionPct = float(root.findtext('wildPlantsPortionPct', '0'))
        self._plantsPortionPct = float(root.findtext('plantsPortionPct', '0'))
        self._animalPortionPct = float(root.findtext('animalPortionPct', '0'))
        self._kiloCaloriesIndividualAnnual = float(root.findtext('kiloCaloriesIndividualAnnual', '0'))
        self._megaCaloriesSettlementAnnual = float(root.findtext('megaCaloriesSettlementAnnual', '0'))
        self._dairySurplusMCalories = float(root.findtext('dairySurplusMCalories', '0'))

        # Emit signals for all changed values
        self._dairyMCaloriesChanged.emit(self._dairyMCalories)
        self._cropMCaloriesChanged.emit(self._cropMCalories)
        self._animalMCaloriesChanged.emit(self._animalMCalories)
        self._wildAnimalMCaloriesChanged.emit(self._wildAnimalMCalories)
        self._wildPlantsMCaloriesChanged.emit(self._wildPlantsMCalories)
        self._dairyPortionPctChanged.emit(self._dairyPortionPct)
        self._tameMeatPortionPctChanged.emit(self._tameMeatPortionPct)
        self._cropsPortionPctChanged.emit(self._cropsPortionPct)
        self._wildAnimalPortionPctChanged.emit(self._wildAnimalPortionPct)
        self._wildPlantsPortionPctChanged.emit(self._wildPlantsPortionPct)
        self._plantsPortionPctChanged.emit(self._plantsPortionPct)
        self._animalPortionPctChanged.emit(self._animalPortionPct)
        self._kiloCalsIndividualAnnualChanged.emit(self._kiloCaloriesIndividualAnnual)
        self._megaCalSettlementAnnualChanged.emit(self._megaCaloriesSettlementAnnual)
        self._dairySurplusMCaloriesChanged.emit(self._dairySurplusMCalories)
