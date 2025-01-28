# lacropparameter.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from .laserialisable import LaSerialisable
from .laguid import LaGuid

class LaCropParameter(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._value = ""

    def __del__(self):
        pass

    def __copy__(self):
        return LaCropParameter(self)

    def __deepcopy__(self, memo):
        return LaCropParameter(self)

    def name(self):
        return self._name

    def description(self):
        return self._description

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
