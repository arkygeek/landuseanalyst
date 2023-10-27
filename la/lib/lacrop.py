# lacrop.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid

class LaCrop(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._cropType = ""
        self._plantingDate = ""
        self._harvestDate = ""
        self._yieldValue = 0

    def __del__(self):
        pass

    def __copy__(self):
        return LaCrop(self)

    def __deepcopy__(self, memo):
        return LaCrop(self)

    def name(self):
        return self._name

    def description(self):
        return self._description

    def cropType(self):
        return self._cropType

    def plantingDate(self):
        return self._plantingDate

    def harvestDate(self):
        return self._harvestDate

    def yieldValue(self):
        return self._yieldValue

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def setCropType(self, cropType):
        self._cropType = cropType

    def setPlantingDate(self, plantingDate):
        self._plantingDate = plantingDate

    def setHarvestDate(self, harvestDate):
        self._harvestDate = harvestDate

    def setYieldValue(self, yieldValue):
        self._yieldValue = yieldValue

    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    cropTypeChanged = pyqtSignal(str)
    plantingDateChanged = pyqtSignal(str)
    harvestDateChanged = pyqtSignal(str)
    yieldValueChanged = pyqtSignal(int)

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

    @pyqtProperty(str, notify=cropTypeChanged)
    def cropType(self):
        return self._cropType

    @cropType.setter
    def cropType(self, cropType):
        if self._cropType != cropType:
            self._cropType = cropType
            self.cropTypeChanged.emit(cropType)

    @pyqtProperty(str, notify=plantingDateChanged)
    def plantingDate(self):
        return self._plantingDate

    @plantingDate.setter
    def plantingDate(self, plantingDate):
        if self._plantingDate != plantingDate:
            self._plantingDate = plantingDate
            self.plantingDateChanged.emit(plantingDate)

    @pyqtProperty(str, notify=harvestDateChanged)
    def harvestDate(self):
        return self._harvestDate

    @harvestDate.setter
    def harvestDate(self, harvestDate):
        if self._harvestDate != harvestDate:
            self._harvestDate = harvestDate
            self.harvestDateChanged.emit(harvestDate)

    @pyqtProperty(int, notify=yieldValueChanged)
    def yieldValue(self):
        return self._yieldValue

    @yieldValue.setter
    def yieldValue(self, yieldValue):
        if self._yieldValue != yieldValue:
            self._yieldValue = yieldValue
            self.yieldValueChanged.emit(yieldValue)


# This code defines a LaCrop class in Python using PyQt5.
#
# The class inherits from LaSerialisable and LaGuid, assumed to be defined elsewhere.
#
# The class has several properties, including name, description, cropType, plantingDate,
# harvestDate, and yieldValue, which are defined using the @pyqtProperty decorator.
#
# The class also has several slots which are used to set values of the properties, including:
#   setName, setDescription, setCropType, setPlantingDate, setHarvestDate, and setYieldValue

# Finally, the class has several signals, including:
#   nameChanged, descriptionChanged, cropTypeChanged, plantingDateChanged, harvestDateChanged,
#   and yieldValueChanged, which are emitted whenever the corresponding property is changed.

# The lacrop.cpp file defines the implementation of the LaCrop class in C++.

# The Python version of the class does not require an implementation file, as the properties
# and slots are defined using decorators in the class definition.

# from this c++ code:

"""
# lacrop.cpp
#include "lacrop.h"

LaCrop::LaCrop()
{
    _name = "";
    _description = "";
    _cropType = "";
    _plantingDate = "";
    _harvestDate = "";
    _yieldValue = 0;
}

LaCrop::~LaCrop()
{
}

LaCrop::LaCrop(const LaCrop &other)
{
    _name = other._name;
    _description = other._description;
    _cropType = other._cropType;
    _plantingDate = other._plantingDate;
    _harvestDate = other._harvestDate;
    _yieldValue = other._yieldValue;
}

LaCrop &LaCrop::operator=(const LaCrop &other)
{
    if (this != &other) {
        _name = other._name;
        _description = other._description;
        _cropType = other._cropType;
        _plantingDate = other._plantingDate;
        _harvestDate = other._harvestDate;
        _yieldValue = other._yieldValue;
    }
    return *this;
}

QString LaCrop::name() const
{
    return _name;
}

QString LaCrop::description() const
{
    return _description;
}

QString LaCrop::cropType() const
{
    return _cropType;
}

QString LaCrop::plantingDate() const
{
    return _plantingDate;
}

QString LaCrop::harvestDate() const
{
    return _harvestDate;
}

int LaCrop::yieldValue() const
{
    return _yieldValue;
}

void LaCrop::setName(const QString &name)
{
    _name = name;
}

void LaCrop::setDescription(const QString &description)
{
    _description = description;
}

void LaCrop::setCropType(const QString &cropType)
{
    _cropType = cropType;
}

void LaCrop::setPlantingDate(const QString &plantingDate)
{
    _plantingDate = plantingDate;
}

void LaCrop::setHarvestDate(const QString &harvestDate)
{
    _harvestDate = harvestDate;
}

void LaCrop::setYieldValue(int yieldValue)
{
    _yieldValue = yieldValue;
}

"""