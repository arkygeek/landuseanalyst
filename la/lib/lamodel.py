# lamodel.py
from qgis.PyQt.QtCore import (
    QObject, pyqtSignal, pyqtSlot, Qt, QSettings, QProcess, QFile, QTextStream)
from qgis.PyQt.QtWidgets import (
    QDialog, QTreeWidget, QTreeWidgetItem, QTableWidgetItem, QListWidget, QComboBox, QHeaderView)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtXml import QDomDocument, QDomElement
from qgis.PyQt.QtCore import qDebug
from qgis.core import QgsProperty
from typing import Tuple
from builtins import dict as Dict
from builtins import list as List

from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from qgis.PyQt.QtWidgets import QDialog
from typing import Dict, List, Tuple
from lib.la import La
from lib.laserialisable import LaSerialisable
from lib.laguid import LaGuid
from lib.ladietlabels import LaDietLabels
from lib.lautils import LaMessageBus

""" The messaged signal in LaMessageBus is used for inter-object communication in the application.

    In PyQt, signals and slots are used for communication between objects. A signal is emitted when
    a particular event occurs, and slots can be connected to a signal. When the signal is emitted, 
    the connected slots are automatically executed.

    In the context of the LaMessageBus class, the messaged signal would be emitted when there's a
    new message to be broadcasted across the system. 
    
    Other parts of the application can connect slots to this signal to react to new messages. 
    For example, a logging system might connect a slot to the messaged signal to log all messages, 
    or a GUI might connect a slot to update a message display whenever a new message is sent.

    This allows for a decoupled architecture where the LaMessageBus doesn't need to know what 
    parts of the system are interested in messages, it just emits the messaged signal whenever it
    has a new message. Any part of the system interested in these messages can simply connect a slot
    to the messaged signal to handle them. """
message_bus: LaMessageBus = LaMessageBus()


class LaModel(QDialog, LaSerialisable, LaGuid):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self._name: str = "No Name Set"
        self._population: int = 1000
        self._period: str = "No Period Set"
        self._projection: int = 100
        self._precision: int = 5
        self._diet_percent: int = 25
        self._percent_of_diet_that_is_from_crops: int = 10
        self._meat_percent: int = 10
        self._calories_per_person_daily: int = 2500

    def __del__(self):
        pass

    def __copy__(self):
        return LaModel(self)

    def __deepcopy__(self, memo):
        return LaModel(self)

    def name(self):
        return self._name

    def description(self):
        return self._description

    def diets(self):
        return self._diets

    def dietLabels(self):
        return self._dietLabels

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def setDiets(self, diets):
        self._diets = diets

    def setDietLabels(self, dietLabels):
        self._dietLabels = dietLabels

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    dietsChanged = pyqtSignal(dict)
    dietLabelsChanged = pyqtSignal(list)

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

    @pyqtProperty(dict, notify=dietsChanged)
    def diets(self):
        return self._diets

    @diets.setter
    def diets(self, diets):
        if self._diets != diets:
            self._diets = diets
            self.dietsChanged.emit(diets)

    @pyqtProperty(list, notify=dietLabelsChanged)
    def dietLabels(self):
        return self._dietLabels

    @dietLabels.setter
    def dietLabels(self, dietLabels):
        if self._dietLabels != dietLabels:
            self._dietLabels = dietLabels
            self.dietLabelsChanged.emit(dietLabels)

    def addDiet(self, diet: La):
        self._diets[diet.guid()] = diet

    def removeDiet(self, guid: str):
        if guid in self._diets:
            del self._diets[guid]

    def getDiet(self, guid: str) -> La:
        if guid in self._diets:
            return self._diets[guid]
        else:
            return None

    def addDietLabel(self, label: LaDietLabels):
        self._dietLabels.append(label)

    def removeDietLabel(self, label: LaDietLabels):
        if label in self._dietLabels:
            self._dietLabels.remove(label)

    def getDietLabels(self) -> List[LaDietLabels]:
        return self._dietLabels

    def getDietLabel(self, name: str) -> LaDietLabels:
        for label in self._dietLabels:
            if label.name() == name:
                return label
        return None

"""

This code defines a LaModel class in Python using PyQt5.

The class inherits from QDialog, LaSerialisable, and LaGuid.

It has several properties, including name, description, diets, and dietLabels,
    which are defined using the @pyqtProperty decorator.

It defines slots, including setName, setDescription, setDiets, and setDietLabels
    which are used to set the values of the properties.

The class has several signals including nameChanged, descriptionChanged,
    dietsChanged, and dietLabelsChanged, which are emitted whenever the
    corresponding property is changed.

The lamodel.cpp file defines the implementation of the LaModel class in C++.

The Python version of the class does not require an implementation file, as the
    properties and slots are defined using decorators in the class definition.

"""