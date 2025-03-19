import json
from typing import Dict, Tuple
# ladietlabels.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.la import La

class LaDietLabels(LaSerialisable, LaGuid):
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
    dairyMCaloriesChanged = pyqtSignal(float)
    cropMCaloriesChanged = pyqtSignal(float)
    animalMCaloriesChanged = pyqtSignal(float)
    wildAnimalMCaloriesChanged = pyqtSignal(float)
    wildPlantsMCaloriesChanged = pyqtSignal(float)
    dairyPortionPctChanged = pyqtSignal(float)
    tameMeatPortionPctChanged = pyqtSignal(float)
    cropsPortionPctChanged = pyqtSignal(float)
    wildAnimalPortionPctChanged = pyqtSignal(float)
    wildPlantsPortionPctChanged = pyqtSignal(float)
    plantsPortionPctChanged = pyqtSignal(float)
    animalPortionPctChanged = pyqtSignal(float)
    kiloCaloriesIndividualAnnualChanged = pyqtSignal(float)
    megaCaloriesSettlementAnnualChanged = pyqtSignal(float)
    dairySurplusMCaloriesChanged = pyqtSignal(float)
    cropCalcsReportMapChanged = pyqtSignal(dict)
    animalCalcsReportMapChanged = pyqtSignal(dict)

    def __init__(self):
        """
        Initialize a new LaDietLabels instance with default values.

        All numeric values are initialized to 0.0 and dictionaries are empty.
        """
        super().__init__()
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
        self._cropCalcsReportMap: Dict[str, Tuple[str, float]] = {}
        self._animalCalcsReportMap: Dict[str, Tuple[str, float]] = {}

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
        return LaDietLabels(self)

    def __deepcopy__(self, memo):
        """
        Create a deep copy of this LaDietLabels instance.

        :param memo: Dictionary of id to object references
        :type memo: dict
        :return: A new LaDietLabels instance with copies of all values
        :rtype: LaDietLabels
        """
        return LaDietLabels(self)

    @pyqtProperty(float, notify=dairyMCaloriesChanged)
    def dairyMCalories(self) -> float:
        """
        Get the dairy mega-calories value.

        :return: The dairy mega-calories value
        :rtype: float
        """
        return self._dairyMCalories

    @dairyMCalories.setter
    def dairyMCalories(self, theDairyMCalories: float) -> None:
        """
        Set the dairy mega-calories value and emit a signal if changed.

        :param theDairyMCalories: The new dairy mega-calories value
        :type theDairyMCalories: float
        """
        if self._dairyMCalories != theDairyMCalories:
            self._dairyMCalories = theDairyMCalories
            self.dairyMCaloriesChanged.emit(theDairyMCalories)

    @pyqtProperty(float, notify=cropMCaloriesChanged)
    def cropMCalories(self) -> float:
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
            self.cropMCaloriesChanged.emit(theCropMCalories)

    @pyqtProperty(float, notify=animalMCaloriesChanged)
    def animalMCalories(self) -> float:
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
            self.animalMCaloriesChanged.emit(theAnimalMCalories)

    @pyqtProperty(float, notify=wildAnimalMCaloriesChanged)
    def wildAnimalMCalories(self) -> float:
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
            self.wildAnimalMCaloriesChanged.emit(theWildAnimalMCalories)

    @pyqtProperty(float, notify=wildPlantsMCaloriesChanged)
    def wildPlantsMCalories(self) -> float:
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
            self.wildPlantsMCaloriesChanged.emit(theWildPlantsMCalories)

    @pyqtProperty(float, notify=dairyPortionPctChanged)
    def dairyPortionPct(self) -> float:
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
            self.dairyPortionPctChanged.emit(theDairyPortionPct)

    @pyqtProperty(float, notify=tameMeatPortionPctChanged)
    def tameMeatPortionPct(self) -> float:
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
            self.tameMeatPortionPctChanged.emit(theTameMeatPortionPct)

    @pyqtProperty(float, notify=cropsPortionPctChanged)
    def cropsPortionPct(self) -> float:
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
            self.cropsPortionPctChanged.emit(theCropsPortionPct)

    @pyqtProperty(float, notify=wildAnimalPortionPctChanged)
    def wildAnimalPortionPct(self) -> float:
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
            self.wildAnimalPortionPctChanged.emit(theWildAnimalPortionPct)

    @pyqtProperty(float, notify=wildPlantsPortionPctChanged)
    def wildPlantsPortionPct(self) -> float:
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
            self.wildPlantsPortionPctChanged.emit(theWildPlantsPortionPct)

    @pyqtProperty(float, notify=plantsPortionPctChanged)
    def plantsPortionPct(self) -> float:
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
            self.plantsPortionPctChanged.emit(thePlantsPortionPct)

    @pyqtProperty(float, notify=animalPortionPctChanged)
    def animalPortionPct(self) -> float:
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
            self.animalPortionPctChanged.emit(theAnimalPortionPct)

    @pyqtProperty(float, notify=kiloCaloriesIndividualAnnualChanged)
    def kiloCaloriesIndividualAnnual(self) -> float:
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
            self.kiloCaloriesIndividualAnnualChanged.emit(theKiloCaloriesIndividualAnnual)

    @pyqtProperty(float, notify=megaCaloriesSettlementAnnualChanged)
    def megaCaloriesSettlementAnnual(self) -> float:
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
            self.megaCaloriesSettlementAnnualChanged.emit(theMegaCaloriesSettlementAnnual)

    @pyqtProperty(float, notify=dairySurplusMCaloriesChanged)
    def dairySurplusMCalories(self) -> float:
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
            self.dairySurplusMCaloriesChanged.emit(theDairySurplusMCalories)

    @pyqtProperty(dict, notify=cropCalcsReportMapChanged)
    def cropCalcsReportMap(self) -> Dict[str, Tuple[str, float]]:
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
            self.cropCalcsReportMapChanged.emit(theCropCalcsReportMap)

    @pyqtProperty(dict, notify=animalCalcsReportMapChanged)
    def animalCalcsReportMap(self) -> Dict[str, Tuple[str, float]]:
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
            self.animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)
