# lacropparameter.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid

class LaCropParameter(LaSerialisable, LaGuid):
    def __init__(self, theCropParameter=None):
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

    def value(self):
        return self._value

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def setValue(self, value):
        self._value = value

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    valueChanged = pyqtSignal(str)

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

    @pyqtProperty(str, notify=valueChanged)
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value != value:
            self._value = value
            self.valueChanged.emit(value)

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
