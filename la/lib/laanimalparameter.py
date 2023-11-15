# laanimalparameter.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import La
from la.lib.lafoodsource import LaFoodSource

class LaAnimalParameter(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._meatFoodValue = 0
        self._slaughterWeight = 0
        self._foodSources = []

    def __del__(self):
        pass

    def __copy__(self):
        myAnimalParameter = LaAnimalParameter()
        myAnimalParameter._name = self.name()
        myAnimalParameter._description = self.description()
        myAnimalParameter._guid = self.guid()
        myAnimalParameter._animalGuid = self.animalGuid()
        myAnimalParameter._percentTameMeat = self.percentTameMeat()
        myAnimalParameter._valueSpecificGrazingLand = self.valueSpecificGrazingLand()
        myAnimalParameter._valueCommonGrazingLand = self.valueCommonGrazingLand()
        myAnimalParameter._areaUnits = self.areaUnits()
        myAnimalParameter._energyType = self.energyType()
        myAnimalParameter._fodderUse = self.fodderUse()
        myAnimalParameter._foodSourceMap = self.fodderSourceMap().copy()  # Assuming this is a dictionary

        # Copy fodder stuff here

        myAnimalParameter._useSpecificGrazingLand = self.useSpecificGrazingLand()
        myAnimalParameter._useCommonGrazingLand = self.useCommonGrazingLand()
        myAnimalParameter._fallowUsage = self.fallowUsage()
        myAnimalParameter._rasterName = self.rasterName()
        return myAnimalParameter

    def __deepcopy__(self, memo):
        return LaAnimalParameter(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self._name != name:
            self._name = name
            self.nameChanged.emit(name)

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @property
    def guid(self) -> str:
        return super().guid()
    
    @guid.setter
    def guid(self, guid: str):
        super().guid(guid)

    @property
    def animalGuid(self) -> str:
        return super().guid()
    
    @animalGuid.setter
    def animalGuid(self, guid: str):
        super().guid(guid)

    @property
    def percentTameMeat(self) -> float:
        return self._meatFoodValue
    
    @percentTameMeat.setter
    def percentTameMeat(self, value: float):
        if self._meatFoodValue != value:
            self._meatFoodValue = value
            self.percentTameMeatChanged.emit(value)

    @property
    def valueSpecificGrazingLand(self) -> float:
        return self._slaughterWeight
    
    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, value: float):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.valueSpecificGrazingLandChanged.emit(value)

    @property
    def valueCommonGrazingLand(self) -> float:
        return self._slaughterWeight
    
    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, value: float):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.valueCommonGrazingLandChanged.emit(value)

    @property
    def areaUnits(self) -> str:
        return self._slaughterWeight
    
    @areaUnits.setter
    def areaUnits(self, value: str):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.areaUnitsChanged.emit(value)

    @property
    def energyType(self) -> str:
        return self._slaughterWeight
    
    @energyType.setter
    def energyType(self, value: str):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.energyTypeChanged.emit(value)

    @property
    def fodderUse(self) -> str:
        return self._slaughterWeight
    
    @fodderUse.setter
    def fodderUse(self, value: str):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.fodderUseChanged.emit(value)

    @property
    def fodderSourceMap(self) -> dict:
        return self._slaughterWeight
    
    @fodderSourceMap.setter
    def fodderSourceMap(self, value: dict):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.fodderSourceMapChanged.emit(value)

    @property
    def useSpecificGrazingLand(self) -> bool:
        return self._slaughterWeight
    
    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, value: bool):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.useSpecificGrazingLandChanged.emit(value)

    @property
    def useCommonGrazingLand(self) -> bool:
        return self._slaughterWeight
    
    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, value: bool):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.useCommonGrazingLandChanged.emit(value)

    @property
    def fallowUsage(self) -> float:
        return self._slaughterWeight
    
    @fallowUsage.setter
    def fallowUsage(self, value: float):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.fallowUsageChanged.emit(value)

    @property
    def rasterName(self) -> str:
        return self._slaughterWeight
    
    @rasterName.setter
    def rasterName(self, value: str):
        if self._slaughterWeight != value:
            self._slaughterWeight = value
            self.rasterNameChanged.emit(value)

    