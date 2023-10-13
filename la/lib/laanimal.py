"""
/***************************************************************************
 LaAnimal
                                 A QGIS plugin
 Archaeological modelling
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-22
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Dr. Jason S. Jorgenson
        email                : jjorgenson@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify   *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or      *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# laanimal.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid

class LaAnimal(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._meatFoodValue = 0
        self._usableMeat = 0
        self._slaughterWeight = 0

    def __del__(self):
        pass

    def __copy__(self):
        return LaAnimal(self)

    def __deepcopy__(self, memo):
        return LaAnimal(self)

    def name(self):
        return self._name

    def description(self):
        return self._description

    def meatFoodValue(self):
        return self._meatFoodValue

    def usableMeat(self):
        return self._usableMeat

    def slaughterWeight(self):
        return self._slaughterWeight

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def setMeatFoodValue(self, meatFoodValue):
        self._meatFoodValue = meatFoodValue

    def setUsableMeat(self, usableMeat):
        self._usableMeat = usableMeat

    def setSlaughterWeight(self, slaughterWeight):
        self._slaughterWeight = slaughterWeight

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    meatFoodValueChanged = pyqtSignal(int)
    usableMeatChanged = pyqtSignal(int)
    slaughterWeightChanged = pyqtSignal(int)

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

    @pyqtProperty(int, notify=usableMeatChanged)
    def usableMeat(self):
        return self._usableMeat

    @usableMeat.setter
    def usableMeat(self, usableMeat):
        if self._usableMeat != usableMeat:
            self._usableMeat = usableMeat
            self.usableMeatChanged.emit(usableMeat)

    @pyqtProperty(int, notify=slaughterWeightChanged)
    def slaughterWeight(self):
        return self._slaughterWeight

    @slaughterWeight.setter
    def slaughterWeight(self, slaughterWeight):
        if self._slaughterWeight != slaughterWeight:
            self._slaughterWeight = slaughterWeight
            self.slaughterWeightChanged.emit(slaughterWeight)

"""

This code defines a LaAnimal class in Python using PyQt5.

The class inherits from LaSerialisable and LaGuid, defined elsewhere.

The class has several properties, including name, description, meatFoodValue,
usableMeat, and slaughterWeight, defined using the @pyqtProperty decorator.

The class also has several slots, including setName, setDescription,
setMeatFoodValue, setUsableMeat, and setSlaughterWeight, which are used to set
the values of the properties.

The class has several signals, including nameChanged, descriptionChanged,
meatFoodValueChanged, usableMeatChanged, and slaughterWeightChanged, which are
emitted whenever the corresponding property is changed.

"""