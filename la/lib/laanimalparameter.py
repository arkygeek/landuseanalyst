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
        return LaAnimalParameter(self)

    def __deepcopy__(self, memo):
        return LaAnimalParameter(self)

    def name(self):
        return self._name

    def description(self):
        return self._description

    def meatFoodValue(self):
        return self._meatFoodValue

    def slaughterWeight(self):
        return self._slaughterWeight

    def foodSources(self):
        return self._foodSources

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def setMeatFoodValue(self, meatFoodValue):
        self._meatFoodValue = meatFoodValue

    def setSlaughterWeight(self, slaughterWeight):
        self._slaughterWeight = slaughterWeight

    def setFoodSources(self, foodSources):
        self._foodSources = foodSources

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    meatFoodValueChanged = pyqtSignal(int)
    slaughterWeightChanged = pyqtSignal(int)
    foodSourcesChanged = pyqtSignal(list)

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

    @pyqtProperty(int, notify=meatFoodValueChanged)
    def meatFoodValue(self):
        return self._meatFoodValue

    @meatFoodValue.setter
    def meatFoodValue(self, meatFoodValue):
        if self._meatFoodValue != meatFoodValue:
            self._meatFoodValue = meatFoodValue
            self.meatFoodValueChanged.emit(meatFoodValue)

    @pyqtProperty(int, notify=slaughterWeightChanged)
    def slaughterWeight(self):
        return self._slaughterWeight

    @slaughterWeight.setter
    def slaughterWeight(self, slaughterWeight):
        if self._slaughterWeight != slaughterWeight:
            self._slaughterWeight = slaughterWeight
            self.slaughterWeightChanged.emit(slaughterWeight)

    @pyqtProperty(list, notify=foodSourcesChanged)
    def foodSources(self):
        return self._foodSources

    @foodSources.setter
    def foodSources(self, foodSources):
        if self._foodSources != foodSources:
            self._foodSources = foodSources
            self.foodSourcesChanged.emit(foodSources)

"""

This code defines a LaAnimalParameter class in Python using PyQt5. The class
    inherits from LaSerialisable and LaGuid, assumed to be defined elsewhere.

The class has several properties, including name, description, meatFoodValue,
    slaughterWeight, and foodSources, defined using the @pyqtProperty decorator.

The class also has several slots: setName, setDescription, setMeatFoodValue,
    setSlaughterWeight, and setFoodSources, which are used to set the values of
    the properties.

Finally the class has several signals including nameChanged, descriptionChanged,
    meatFoodValueChanged, slaughterWeightChanged, and foodSourcesChanged, which
    are emitted whenever the corresponding property is changed.

laanimalparameter.cpp defines implementation of LaAnimalParameter class in C++.

The Python version of the class does not require an implementation file, as the
    properties and slots are defined using decorators in the class definition.

"""