# lafoodsource.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from .laserialisable import LaSerialisable
from .laguid import LaGuid

class LaFoodSource(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._foodValue = 0

    def __del__(self):
        pass

    def __copy__(self):
        return LaFoodSource(self)

    def __deepcopy__(self, memo):
        return LaFoodSource(self)



    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    foodValueChanged = pyqtSignal(int)

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

    @pyqtProperty(int, notify=foodValueChanged)
    def foodValue(self):
        return self._foodValue

    @foodValue.setter
    def foodValue(self, foodValue):
        if self._foodValue != foodValue:
            self._foodValue = foodValue
            self.foodValueChanged.emit(foodValue)

"""

This code defines a LaFoodSource class in Python using PyQt5.

The class inherits from LaSerialisable and LaGuid, defined elsewhere.

The class has several properties, including name, description, and foodValue,
    which are defined using the @pyqtProperty decorator.

The class several slots, including setName, setDescription, and setFoodValue,
    which are used to set the values of the properties.

The class also has several signals, including nameChanged, descriptionChanged,
    and foodValueChanged. These signals are emitted whenever the corresponding
    property is changed.

lafoodsource.cpp file defines the implementation of LaFoodSource class in C++.

The Python version of the class does not require an implementation file, as the
properties and slots are defined using decorators in the class definition.

"""