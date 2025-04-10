# ladietlabels.py
import copy
from typing import Dict, Tuple
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.lautils import LaUtils


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
        Initialize a new LaDietLabels instance using values from the ui.

        """
        super().__init__(parent)
        LaSerialisable.__init__(self)
        LaGuid.__init__(self)

        self.mDairyMCalories: float = 0.0
        self.mCropMCalories: float = 0.0
        self.mAnimalMCalories: float = 0.0
        self.mWildAnimalMCalories: float = 0.0
        self.mWildPlantsMCalories: float = 0.0
        self.mDairyPortionPct: float = 0.0
        self.mTameMeatPortionPct: float = 0.0
        self.mCropsPortionPct: float = 0.0
        self.mWildAnimalPortionPct: float = 0.0
        self.mWildPlantsPortionPct: float = 0.0
        self.mPlantsPortionPct: float = 0.0
        self.mAnimalPortionPct: float = 0.0
        self.mKiloCaloriesIndividualAnnual: float = 0.0
        self.mMegaCaloriesSettlementAnnual: float = 0.0
        self.mDairySurplusMCalories: float = 0.0
        self.mCropAreaTargetsMap = {}  # Map of crop GUID to area target
        self.mAnimalAreaTargetsMap = {}  # Map of animal GUID to area target
        self.mCropCalcsReportMap: Dict[str, Tuple[str, float]] = {}
        self.mAnimalCalcsReportMap: Dict[str, Tuple[str, float]] = {}
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
        return float(str(self.mDairyMCalories))

    @dairyMCalories.setter
    def dairyMCalories(self, theDairyMCalories: float) -> None:
        """
        Set the dairy mega-calories value and emit a signal if changed.

        :param theDairyMCalories: The new dairy mega-calories value
        :type theDairyMCalories: float
        """
        if self.mDairyMCalories != theDairyMCalories:
            self.mDairyMCalories = theDairyMCalories
            self._dairyMCaloriesChanged.emit(theDairyMCalories)

    @pyqtProperty(float, notify=_cropMCaloriesChanged)
    def cropMCalories(self) -> float: # type: ignore
        """
        Get the crop mega-calories value.

        :return: The crop mega-calories value
        :rtype: float
        """
        return self.mCropMCalories

    @cropMCalories.setter
    def cropMCalories(self, theCropMCalories: float) -> None:
        """
        Set the crop mega-calories value and emit a signal if changed.

        :param theCropMCalories: The new crop mega-calories value
        :type theCropMCalories: float
        """
        if self.mCropMCalories != theCropMCalories:
            self.mCropMCalories = theCropMCalories
            self._cropMCaloriesChanged.emit(theCropMCalories)

    @pyqtProperty(float, notify=_animalMCaloriesChanged)
    def animalMCalories(self) -> float: # type: ignore
        """
        Get the animal mega-calories value.

        :return: The animal mega-calories value
        :rtype: float
        """
        return self.mAnimalMCalories

    @animalMCalories.setter
    def animalMCalories(self, theAnimalMCalories: float) -> None:
        """
        Set the animal mega-calories value and emit a signal if changed.

        :param theAnimalMCalories: The new animal mega-calories value
        :type theAnimalMCalories: float
        """
        if self.mAnimalMCalories != theAnimalMCalories:
            self.mAnimalMCalories = theAnimalMCalories
            self._animalMCaloriesChanged.emit(theAnimalMCalories)

    @pyqtProperty(float, notify=_wildAnimalMCaloriesChanged)
    def wildAnimalMCalories(self) -> float: # type: ignore
        """
        Get the wild animal mega-calories value.

        :return: The wild animal mega-calories value
        :rtype: float
        """
        return self.mWildAnimalMCalories

    @wildAnimalMCalories.setter
    def wildAnimalMCalories(self, theWildAnimalMCalories: float) -> None:
        """
        Set the wild animal mega-calories value and emit a signal if changed.

        :param theWildAnimalMCalories: The new wild animal mega-calories value
        :type theWildAnimalMCalories: float
        """
        if self.mWildAnimalMCalories != theWildAnimalMCalories:
            self.mWildAnimalMCalories = theWildAnimalMCalories
            self._wildAnimalMCaloriesChanged.emit(theWildAnimalMCalories)

    @pyqtProperty(float, notify=_wildPlantsMCaloriesChanged)
    def wildPlantsMCalories(self) -> float: # type: ignore
        """
        Get the wild plants mega-calories value.

        :return: The wild plants mega-calories value
        :rtype: float
        """
        return self.mWildPlantsMCalories

    @wildPlantsMCalories.setter
    def wildPlantsMCalories(self, theWildPlantsMCalories: float) -> None:
        """
        Set the wild plants mega-calories value and emit a signal if changed.

        :param theWildPlantsMCalories: The new wild plants mega-calories value
        :type theWildPlantsMCalories: float
        """
        if self.mWildPlantsMCalories != theWildPlantsMCalories:
            self.mWildPlantsMCalories = theWildPlantsMCalories
            self._wildPlantsMCaloriesChanged.emit(theWildPlantsMCalories)

    @pyqtProperty(float, notify=_dairyPortionPctChanged)
    def dairyPortionPct(self) -> float: # type: ignore
        """
        Get the dairy portion percentage value.

        :return: The dairy portion percentage value
        :rtype: float
        """
        return self.mDairyPortionPct

    @dairyPortionPct.setter
    def dairyPortionPct(self, theDairyPortionPct: float) -> None:
        """
        Set the dairy portion percentage value and emit a signal if changed.

        :param theDairyPortionPct: The new dairy portion percentage value
        :type theDairyPortionPct: float
        """
        if self.mDairyPortionPct != theDairyPortionPct:
            self.mDairyPortionPct = theDairyPortionPct
            self._dairyPortionPctChanged.emit(theDairyPortionPct)

    @pyqtProperty(float, notify=_tameMeatPortionPctChanged)
    def tameMeatPortionPct(self) -> float: # type: ignore
        """
        Get the domesticated meat portion percentage value.

        :return: The domesticated meat portion percentage value
        :rtype: float
        """
        return self.mTameMeatPortionPct

    @tameMeatPortionPct.setter
    def tameMeatPortionPct(self, theTameMeatPortionPct: float) -> None:
        """
        Set the domesticated meat portion percentage value and emit a signal if changed.

        :param theTameMeatPortionPct: The new domesticated meat portion percentage value
        :type theTameMeatPortionPct: float
        """
        if self.mTameMeatPortionPct != theTameMeatPortionPct:
            self.mTameMeatPortionPct = theTameMeatPortionPct
            self._tameMeatPortionPctChanged.emit(theTameMeatPortionPct)

    @pyqtProperty(float, notify=_cropsPortionPctChanged)
    def cropsPortionPct(self) -> float: # type: ignore
        """
        Get the crops portion percentage value.

        :return: The crops portion percentage value
        :rtype: float
        """
        return self.mCropsPortionPct

    @cropsPortionPct.setter
    def cropsPortionPct(self, theCropsPortionPct: float) -> None:
        """
        Set the crops portion percentage value and emit a signal if changed.

        :param theCropsPortionPct: The new crops portion percentage value
        :type theCropsPortionPct: float
        """
        if self.mCropsPortionPct != theCropsPortionPct:
            self.mCropsPortionPct = theCropsPortionPct
            self._cropsPortionPctChanged.emit(theCropsPortionPct)

    @pyqtProperty(float, notify=_wildAnimalPortionPctChanged)
    def wildAnimalPortionPct(self) -> float: # type: ignore
        """
        Get the wild animal portion percentage value.

        :return: The wild animal portion percentage value
        :rtype: float
        """
        return self.mWildAnimalPortionPct

    @wildAnimalPortionPct.setter
    def wildAnimalPortionPct(self, theWildAnimalPortionPct: float) -> None:
        """
        Set the wild animal portion percentage value and emit a signal if changed.

        :param theWildAnimalPortionPct: The new wild animal portion percentage value
        :type theWildAnimalPortionPct: float
        """
        if self.mWildAnimalPortionPct != theWildAnimalPortionPct:
            self.mWildAnimalPortionPct = theWildAnimalPortionPct
            self._wildAnimalPortionPctChanged.emit(theWildAnimalPortionPct)

    @pyqtProperty(float, notify=_wildPlantsPortionPctChanged)
    def wildPlantsPortionPct(self) -> float: # type: ignore
        """
        Get the wild plants portion percentage value.

        :return: The wild plants portion percentage value
        :rtype: float
        """
        return self.mWildPlantsPortionPct

    @wildPlantsPortionPct.setter
    def wildPlantsPortionPct(self, theWildPlantsPortionPct: float) -> None:
        """
        Set the wild plants portion percentage value and emit a signal if changed.

        :param theWildPlantsPortionPct: The new wild plants portion percentage value
        :type theWildPlantsPortionPct: float
        """
        if self.mWildPlantsPortionPct != theWildPlantsPortionPct:
            self.mWildPlantsPortionPct = theWildPlantsPortionPct
            self._wildPlantsPortionPctChanged.emit(theWildPlantsPortionPct)

    @pyqtProperty(float, notify=_plantsPortionPctChanged)
    def plantsPortionPct(self) -> float: # type: ignore
        """
        Get the plants portion percentage value (both wild and cultivated).

        :return: The plants portion percentage value
        :rtype: float
        """
        return self.mPlantsPortionPct

    @plantsPortionPct.setter
    def plantsPortionPct(self, thePlantsPortionPct: float) -> None:
        """
        Set the plants portion percentage value and emit a signal if changed.

        :param thePlantsPortionPct: The new plants portion percentage value
        :type thePlantsPortionPct: float
        """
        if self.mPlantsPortionPct != thePlantsPortionPct:
            self.mPlantsPortionPct = thePlantsPortionPct
            self._plantsPortionPctChanged.emit(thePlantsPortionPct)

    @pyqtProperty(float, notify=_animalPortionPctChanged)
    def animalPortionPct(self) -> float: # type: ignore
        """
        Get the animal portion percentage value (both wild and domestic).

        :return: The animal portion percentage value
        :rtype: float
        """
        return self.mAnimalPortionPct

    @animalPortionPct.setter
    def animalPortionPct(self, theAnimalPortionPct: float) -> None:
        """
        Set the animal portion percentage value and emit a signal if changed.

        :param theAnimalPortionPct: The new animal portion percentage value
        :type theAnimalPortionPct: float
        """
        if self.mAnimalPortionPct != theAnimalPortionPct:
            self.mAnimalPortionPct = theAnimalPortionPct
            self._animalPortionPctChanged.emit(theAnimalPortionPct)

    @pyqtProperty(float, notify=_kiloCalsIndividualAnnualChanged)
    def kiloCaloriesIndividualAnnual(self) -> float: # type: ignore
        """
        Get the individual annual kilocalories requirement.

        :return: The individual annual kilocalories requirement
        :rtype: float
        """
        return self.mKiloCaloriesIndividualAnnual

    @kiloCaloriesIndividualAnnual.setter
    def kiloCaloriesIndividualAnnual(self, theKiloCaloriesIndividualAnnual) -> None:
        """
        Set the individual annual kilocalories requirement and emit a signal if changed.

        :param theKiloCaloriesIndividualAnnual: The new individual annual kilocalories requirement
        :type theKiloCaloriesIndividualAnnual: float
        """
        if self.mKiloCaloriesIndividualAnnual != theKiloCaloriesIndividualAnnual:
            self.mKiloCaloriesIndividualAnnual = theKiloCaloriesIndividualAnnual
            self._kiloCalsIndividualAnnualChanged.emit(theKiloCaloriesIndividualAnnual)


    @pyqtProperty(float, notify=_megaCalSettlementAnnualChanged)
    def megaCaloriesSettlementAnnual(self) -> float: # type: ignore
        """
        Get the settlement annual megacalories requirement.

        :return: The settlement annual megacalories requirement
        :rtype: float
        """
        return self.mMegaCaloriesSettlementAnnual
    @megaCaloriesSettlementAnnual.setter
    def megaCaloriesSettlementAnnual(self, theMegaCaloriesSettlementAnnual: float) -> None:
        """
        Set the settlement annual megacalories requirement and emit a signal if changed.

        :param theMegaCaloriesSettlementAnnual: The new settlement annual megacalories requirement
        :type theMegaCaloriesSettlementAnnual: float
        """
        if self.mMegaCaloriesSettlementAnnual != theMegaCaloriesSettlementAnnual:
            self.mMegaCaloriesSettlementAnnual = theMegaCaloriesSettlementAnnual
            self._megaCalSettlementAnnualChanged.emit(theMegaCaloriesSettlementAnnual)


    @pyqtProperty(float, notify=_dairySurplusMCaloriesChanged)
    def dairySurplusMCalories(self) -> float: # type: ignore
        """
        Get the dairy surplus megacalories value.

        :return: The dairy surplus megacalories value
        :rtype: float
        """
        return self.mDairySurplusMCalories
    @dairySurplusMCalories.setter
    def dairySurplusMCalories(self, theDairySurplusMCalories: float) -> None:
        """
        Set the dairy surplus megacalories value and emit a signal if changed.

        :param theDairySurplusMCalories: The new dairy surplus megacalories value
        :type theDairySurplusMCalories: float
        """
        if self.mDairySurplusMCalories != theDairySurplusMCalories:
            self.mDairySurplusMCalories = theDairySurplusMCalories
            self._dairySurplusMCaloriesChanged.emit(theDairySurplusMCalories)


    @pyqtProperty(dict, notify=_cropAreaTargetsMapChanged)
    def cropAreaTargetsMap(self) -> Dict[str, float]: # type: ignore
        """
        Get the crop area targets map.
        :return: A dictionary mapping crop GUIDs to area targets
        :rtype: Dict[str, float]
        """
        return self.mCropAreaTargetsMap
    @cropAreaTargetsMap.setter
    def cropAreaTargetsMap(self, theCropAreaTargetsMap: Dict[str, float]) -> None:
        """
        Set the crop area targets map and emit a signal if changed.

        :param theCropAreaTargetsMap: The new crop area targets map
        :type theCropAreaTargetsMap: Dict[str, float]
        """
        if self.mCropAreaTargetsMap != theCropAreaTargetsMap:
            self.mCropAreaTargetsMap = theCropAreaTargetsMap
            self._cropAreaTargetsMapChanged.emit(theCropAreaTargetsMap)
    @pyqtProperty(dict, notify=_animalAreaTargetsMapChanged)


    def animalAreaTargetsMap(self) -> Dict[str, float]: # type: ignore
        """
        Get the animal area targets map.
        :return: A dictionary mapping animal GUIDs to area targets
        :rtype: Dict[str, float]
        """
        return self.mAnimalAreaTargetsMap
    @animalAreaTargetsMap.setter
    def animalAreaTargetsMap(self, theAnimalAreaTargetsMap: Dict[str, float]) -> None:
        """
        Set the animal area targets map and emit a signal if changed.

        :param theAnimalAreaTargetsMap: The new animal area targets map
        :type theAnimalAreaTargetsMap: Dict[str, float]
        """
        if self.mAnimalAreaTargetsMap != theAnimalAreaTargetsMap:
            self.mAnimalAreaTargetsMap = theAnimalAreaTargetsMap
            self._animalAreaTargetsMapChanged.emit(theAnimalAreaTargetsMap)


    @pyqtProperty(dict, notify=_cropCalcsReportMapChanged)
    def cropCalcsReportMap(self) -> Dict[str, Tuple[str, float]]: # type: ignore
        """
        Get the crop calculations report map.

        :return: A dictionary mapping strings to tuples of (string, float)
        :rtype: Dict[str, Tuple[str, float]]
        """
        return self.mCropCalcsReportMap
    @cropCalcsReportMap.setter
    def cropCalcsReportMap(self, theCropCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """
        Set the crop calculations report map and emit a signal if changed.

        :param theCropCalcsReportMap: The new crop calculations report map
        :type theCropCalcsReportMap: Dict[str, Tuple[str, float]]
        """
        if self.mCropCalcsReportMap != theCropCalcsReportMap:
            self.mCropCalcsReportMap = theCropCalcsReportMap
            self._cropCalcsReportMapChanged.emit(theCropCalcsReportMap)


    @pyqtProperty(dict, notify=_animalCalcsReportMapChanged)
    def animalCalcsReportMap(self) -> Dict[str, Tuple[str, float]]: # type: ignore
        """
        Get the animal calculations report map.

        :return: A dictionary mapping strings to tuples of (string, float)
        :rtype: Dict[str, Tuple[str, float]]
        """
        return self.mAnimalCalcsReportMap
    @animalCalcsReportMap.setter
    def animalCalcsReportMap(self, theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """
        Set the animal calculations report map and emit a signal if changed.

        :param theAnimalCalcsReportMap: The new animal calculations report map
        :type theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]
        """
        if self.mAnimalCalcsReportMap != theAnimalCalcsReportMap:
            self.mAnimalCalcsReportMap = theAnimalCalcsReportMap
            self._animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)


    # Required implementations for LaSerialisable
    def toXml(self) -> str:
        """
        Convert the LaDietLabels object to XML representation.

        Required implementation of the abstract method from LaSerialisable.

        :return: String containing XML representation of the object
        :rtype: str
        """
        myXml = '<dietLabels>\n'
        myXml += f'  <guid>{self.guid}</guid>\n'
        myXml += f'  <dairyMCalories>{self.mDairyMCalories}</dairyMCalories>\n'
        myXml += f'  <cropMCalories>{self.mCropMCalories}</cropMCalories>\n'
        myXml += f'  <animalMCalories>{self.mAnimalMCalories}</animalMCalories>\n'
        myXml += f'  <wildAnimalMCalories>{self.mWildAnimalMCalories}</wildAnimalMCalories>\n'
        myXml += f'  <wildPlantsMCalories>{self.mWildPlantsMCalories}</wildPlantsMCalories>\n'
        myXml += f'  <dairyPortionPct>{self.mDairyPortionPct}</dairyPortionPct>\n'
        myXml += f'  <tameMeatPortionPct>{self.mTameMeatPortionPct}</tameMeatPortionPct>\n'
        myXml += f'  <cropsPortionPct>{self.mCropsPortionPct}</cropsPortionPct>\n'
        myXml += f'  <wildAnimalPortionPct>{self.mWildAnimalPortionPct}</wildAnimalPortionPct>\n'
        myXml += f'  <wildPlantsPortionPct>{self.mWildPlantsPortionPct}</wildPlantsPortionPct>\n'
        myXml += f'  <plantsPortionPct>{self.mPlantsPortionPct}</plantsPortionPct>\n'
        myXml += f'  <animalPortionPct>{self.mAnimalPortionPct}</animalPortionPct>\n'
        myXml += f'  <kiloCaloriesIndividualAnnual>{self.mKiloCaloriesIndividualAnnual}</kiloCaloriesIndividualAnnual>\n'
        myXml += f'  <megaCaloriesSettlementAnnual>{self.mMegaCaloriesSettlementAnnual}</megaCaloriesSettlementAnnual>\n'
        myXml += f'  <dairySurplusMCalories>{self.mDairySurplusMCalories}</dairySurplusMCalories>\n'
        myXml += '</dietLabels>\n'
        return myXml


    def fromXml(self, xml_string: str) -> bool:
        """
        Initialize the LaDietLabels object from XML representation.

        Required implementation of the abstract method from LaSerialisable.

        :param xml_string: XML string to parse
        :type xml_string: str
        :return: True if successful, False otherwise
        :rtype: bool
        """
        import xml.etree.ElementTree as ET

        try:
            # Parse the XML string
            root = ET.fromstring(xml_string)

            # Extract values from XML
            if root.find('guid') is not None:
                self.setGuid(root.find('guid'))

            # Helper function to safely get float values
            def getFloat(theElementName):
                myElement = root.find(theElementName)
                if myElement is not None and myElement.text:
                    try:
                        return float(myElement.text)
                    except (ValueError, TypeError):
                        return 0.0
                return 0.0

            # Set properties from XML
            self.dairyMCalories = getFloat('dairyMCalories') # type: ignore
            self.cropMCalories = getFloat('cropMCalories') # type: ignore
            self.animalMCalories = getFloat('animalMCalories') # type: ignore
            self.wildAnimalMCalories = getFloat('wildAnimalMCalories') # type: ignore
            self.wildPlantsMCalories = getFloat('wildPlantsMCalories') # type: ignore
            self.dairyPortionPct = getFloat('dairyPortionPct') # type: ignore
            self.tameMeatPortionPct = getFloat('tameMeatPortionPct') # type: ignore
            self.cropsPortionPct = getFloat('cropsPortionPct') # type: ignore
            self.wildAnimalPortionPct = getFloat('wildAnimalPortionPct') # type: ignore
            self.wildPlantsPortionPct = getFloat('wildPlantsPortionPct') # type: ignore
            self.plantsPortionPct = getFloat('plantsPortionPct') # type: ignore
            self.animalPortionPct = getFloat('animalPortionPct') # type: ignore
            self.kiloCaloriesIndividualAnnual = getFloat('kiloCaloriesIndividualAnnual') # type: ignore
            self.megaCaloriesSettlementAnnual = getFloat('megaCaloriesSettlementAnnual') # type: ignore
            self.dairySurplusMCalories = getFloat('dairySurplusMCalories') # type: ignore

            return True
        except Exception as e:
            LaUtils.debug.log(f"Error parsing XML: {str(e)}", "Error")
            return False
