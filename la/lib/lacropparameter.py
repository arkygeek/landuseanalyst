# lacropparameter.py
from typing import Optional, Type

from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits #, LaTripleMap, LaRasterInfo, LaFoodSourceMap, HerdSize, LaReportMap

class LaCropParameter(LaSerialisable, LaGuid):
    def __init__(self, theCropParameter: Optional[Type['LaCropParameter']] = None):
        """
        Initializes a new instance of the LaCropParameter class.
        
        Args:
            theCropParameter (LaCropParameter, optional): An existing LaCropParameter object to copy. Defaults to None.
        """
        super().__init__()
        if theCropParameter is None:
            self.setGuid()
            self._name = "No Name Set"
            self._description = "Not Set"
        else:
            self._name = theCropParameter.name
            self._description = theCropParameter.description
            self._guid = theCropParameter.guid
            self._cropGuid = theCropParameter.cropGuid
            self._percentTameCrop = theCropParameter.percentTameCrop
            self._spoilage = theCropParameter.spoilage
            self._reseed = theCropParameter.reseed
            self._cropRotation = theCropParameter.cropRotation
            self._fallowRatio = theCropParameter.fallowRatio
            self._fallowValue = theCropParameter.fallowValue
            self._areaUnits = theCropParameter.areaUnits
            self._useCommonLand = theCropParameter.useCommonLand
            self._useSpecificLand = theCropParameter.useSpecificLand
            self._rasterName = theCropParameter.rasterName


    def __del__(self):
        pass

    def __copy__(self) -> 'LaCropParameter':
        myNewCropParameter: LaCropParameter = LaCropParameter()
        myNewCropParameter._name = self._name
        myNewCropParameter._description = self._description
        myNewCropParameter._cropGuid = self._cropGuid
        myNewCropParameter._percentTameCrop = self._percentTameCrop
        myNewCropParameter._spoilage = self._spoilage
        myNewCropParameter._reseed = self._reseed
        myNewCropParameter._cropRotation = self._cropRotation
        myNewCropParameter._fallowRatio = self._fallowRatio
        myNewCropParameter._fallowValue = self._fallowValue
        myNewCropParameter._areaUnits = self._areaUnits
        myNewCropParameter._useCommonLand = self._useCommonLand
        myNewCropParameter._useSpecificLand = self._useSpecificLand
        myNewCropParameter._rasterName = self._rasterName
        return myNewCropParameter
    

    def __deepcopy__(self, memo):
        return LaCropParameter(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, theName: str) -> None:
        self._name = theName
    
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, theDescription):
        self._description = theDescription  
    
    @property
    def cropGuid(self) -> str:
        return self._cropGuid
    
    @cropGuid.setter
    def cropGuid(self, theCropGuid: str) -> None:
        self._cropGuid = theCropGuid

    @property
    def percentTameCrop(self) -> float:
        return self._percentTameCrop
    
    @percentTameCrop.setter
    def percentTameCrop(self, thePercentTameCrop: float) -> None:
        self._percentTameCrop = thePercentTameCrop

    @property
    def spoilage(self) -> float:
        return self._spoilage
    
    @spoilage.setter
    def spoilage(self, theSpoilage: float) -> None:
        self._spoilage = theSpoilage
    
    @property
    def reseed(self) -> float:
        return self._reseed
    
    @reseed.setter
    def reseed(self, theReseed: float) -> None:
        self._reseed = theReseed
    
    @property
    def cropRotation(self) -> float:
        return self._cropRotation
    
    @cropRotation.setter
    def cropRotation(self, theCropRotation: float) -> None:
        self._cropRotation = theCropRotation

    @property
    def fallowRatio(self) -> float:
        return self._fallowRatio
    
    @fallowRatio.setter
    def fallowRatio(self, theFallowRatio: float) -> None:
        self._fallowRatio = theFallowRatio
    
    @property
    def fallowValue(self) -> float:
        return self._fallowValue
    
    @fallowValue.setter
    def fallowValue(self, theFallowValue: float) -> None:
        self._fallowValue = theFallowValue

    @property
    def areaUnits(self) -> LaAreaUnits:
        return self._areaUnits
    
    @areaUnits.setter
    def areaUnits(self, theAreaUnits: LaAreaUnits) -> None:
        self._areaUnits = theAreaUnits

    @property
    def useCommonLand(self) -> bool:
        return self._useCommonLand
    
    @useCommonLand.setter
    def useCommonLand(self, theUseCommonLand: bool) -> None:
        self._useCommonLand = theUseCommonLand

    @property
    def useSpecificLand(self) -> bool:
        return self._useSpecificLand
    
    @useSpecificLand.setter
    def useSpecificLand(self, theUseSpecificLand: bool) -> None:
        self._useSpecificLand = theUseSpecificLand

    @property
    def rasterName(self) -> str:
        return self._rasterName
    
    @rasterName.setter
    def rasterName(self, theRasterName: str) -> None:
        self._rasterName = theRasterName

    
    

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    cropGuidChanged = pyqtSignal(str)
    percentTameCropChanged = pyqtSignal(float)
    spoilageChanged = pyqtSignal(float)
    reseedChanged = pyqtSignal(float)
    cropRotationChanged = pyqtSignal(float)
    fallowRatioChanged = pyqtSignal(float)
    fallowValueChanged = pyqtSignal(float)
    areaUnitsChanged = pyqtSignal(LaAreaUnits)
    useCommonLandChanged = pyqtSignal(bool)
    useSpecificLandChanged = pyqtSignal(bool)
    rasterNameChanged = pyqtSignal(str)




    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name != name:
            self._name = name
            self.nameChanged.emit(name)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self):
        return self._cropGuid
    
    @cropGuid.setter
    def cropGuid(self, cropGuid):
        if self._cropGuid != cropGuid:
            self._cropGuid = cropGuid
            self.cropGuidChanged.emit(cropGuid)
    
    @pyqtProperty(float, notify=percentTameCropChanged)
    def percentTameCrop(self):
        return self._percentTameCrop
    
    @percentTameCrop.setter
    def percentTameCrop(self, percentTameCrop):
        if self._percentTameCrop != percentTameCrop:
            self._percentTameCrop = percentTameCrop
            self.percentTameCropChanged.emit(percentTameCrop)
    
    @pyqtProperty(float, notify=spoilageChanged)
    def spoilage(self):
        return self._spoilage
    
    @spoilage.setter
    def spoilage(self, spoilage):
        if self._spoilage != spoilage:
            self._spoilage = spoilage
            self.spoilageChanged.emit(spoilage)

    @pyqtProperty(float, notify=reseedChanged)
    def reseed(self):
        return self._reseed
    
    @reseed.setter
    def reseed(self, reseed):
        if self._reseed != reseed:
            self._reseed = reseed
            self.reseedChanged.emit(reseed)

    @pyqtProperty(float, notify=cropRotationChanged)
    def cropRotation(self):
        return self._cropRotation
    
    @cropRotation.setter
    def cropRotation(self, cropRotation):
        if self._cropRotation != cropRotation:
            self._cropRotation = cropRotation
            self.cropRotationChanged.emit(cropRotation)

    @pyqtProperty(float, notify=fallowRatioChanged)
    def fallowRatio(self):
        return self._fallowRatio
    
    @fallowRatio.setter
    def fallowRatio(self, fallowRatio):
        if self._fallowRatio != fallowRatio:
            self._fallowRatio = fallowRatio
            self.fallowRatioChanged.emit(fallowRatio)

    @pyqtProperty(float, notify=fallowValueChanged)
    def fallowValue(self):
        return self._fallowValue
    
    @fallowValue.setter
    def fallowValue(self, fallowValue):
        if self._fallowValue != fallowValue:
            self._fallowValue = fallowValue
            self.fallowValueChanged.emit(fallowValue)

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self):
        return self._areaUnits
    
    @areaUnits.setter
    def areaUnits(self, areaUnits):
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits)

    @pyqtProperty(bool, notify=useCommonLandChanged)
    def useCommonLand(self):
        return self._useCommonLand
    
    @useCommonLand.setter
    def useCommonLand(self, useCommonLand):
        if self._useCommonLand != useCommonLand:
            self._useCommonLand = useCommonLand
            self.useCommonLandChanged.emit(useCommonLand)
    
    @pyqtProperty(bool, notify=useSpecificLandChanged)
    def useSpecificLand(self):
        return self._useSpecificLand
    
    @useSpecificLand.setter
    def useSpecificLand(self, useSpecificLand):
        if self._useSpecificLand != useSpecificLand:
            self._useSpecificLand = useSpecificLand
            self.useSpecificLandChanged.emit(useSpecificLand)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self):
        return self._rasterName
    
    @rasterName.setter
    def rasterName(self, rasterName):
        if self._rasterName != rasterName:
            self._rasterName = rasterName
            self.rasterNameChanged.emit(rasterName)






"""
This code defines a LaCropParameter class in Python using PyQt5.

The class inherits from LaSerialisable and LaGuid, defined elsewhere.

The class has several properties, including name, description, and value, which
    are defined using the @pyqtProperty decorator.

The class has several slots including setName, setDescription, and setValue,
    which are used to set the values of the properties.

It has several signals including nameChanged, descriptionChanged, & valueChanged
    which are emitted whenever the corresponding property is changed.

lacropparameter.cpp defines the implementation of LaCropParameter class in C++.

The Python version of the class does not require an implementation file, as the
properties and slots are defined using decorators in the class definition.
"""
