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
        new_obj = LaAnimalParameter()
        new_obj._name = self.name()
        new_obj._description = self.description()
        new_obj._guid = self.guid()
        new_obj._animalGuid = self.animalGuid()
        new_obj._percentTameMeat = self.percentTameMeat()
        new_obj._valueSpecificGrazingLand = self.valueSpecificGrazingLand()
        new_obj._valueCommonGrazingLand = self.valueCommonGrazingLand()
        new_obj._areaUnits = self.areaUnits()
        new_obj._energyType = self.energyType()
        new_obj._fodderUse = self.fodderUse()
        new_obj._foodSourceMap = self.fodderSourceMap().copy()  # Assuming this is a dictionary

        # Copy fodder stuff here

        new_obj._useSpecificGrazingLand = self.useSpecificGrazingLand()
        new_obj._useCommonGrazingLand = self.useCommonGrazingLand()
        new_obj._fallowUsage = self.fallowUsage()
        new_obj._rasterName = self.rasterName()
        return new_obj

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

            