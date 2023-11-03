# lacrop.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid

class LaCrop(LaSerialisable, LaGuid):
    """
    A class representing a crop.

    Attributes:
        mName (str): The name of the crop.
        mDescription (str): The description of the crop.
        mCropYield (int): The yield of the crop.
        mCropCalories (int): The calories of the crop.
        mCropFodderProduction (int): The fodder production of the crop.
        mCropFodderValue (int): The fodder value of the crop.
        mCropFodderEnergyType (str): The energy type of the crop fodder.
        mAreaUnits (str): The area units of the crop.
        mImageFile (str): The image file of the crop.
    """

    class LACrop:
        def __init__(self, theCrop=None):
            """
            Initializes a new instance of the LACrop class.

            Args:
                theCrop (LACrop, optional): An existing LACrop object to copy. Defaults to None.
            """
            super().__init__()
            if theCrop is None:
                self.setGuid()
                self.mName = "No Name Set"
                self.mDescription = "Not Set"
                self.mCropYield = 60
                self.mCropCalories = 3000
                self.mCropFodderProduction = 50
                self.mCropFodderValue = 1000
            else:
                self.mName = theCrop.name
                self.mDescription = theCrop.description
                self.setGuid(theCrop.guid)
                self.mCropYield = theCrop.cropYield
                self.mCropCalories = theCrop.cropCalories
                self.mCropFodderProduction = theCrop.fodderProduction
                self.mCropFodderValue = theCrop.fodderValue
                self.mCropFodderEnergyType = theCrop.cropFodderEnergyType
                self.mAreaUnits = theCrop.areaUnits
                self.mImageFile = theCrop.imageFile

    def __del__(self):
        pass

    def __eq__(self, theCrop: 'LaCrop') -> bool:
        """Compare two LaCrop objects for equality.
        Args:
            theCrop (LaCrop): The LaCrop object to compare against.
        Returns:
            bool: True if the two objects are equal, False otherwise.
        :param theCrop: the crop to compare against
        :paramtype theCrop: LaCrop
        :return: True if the two objects are equal, False otherwise
        :rtype: bool
        """
        return self.mName == theCrop.name and \
                self.mDescription == theCrop.description and \
                self.guid == theCrop.guid and \
                self.mCropYield == theCrop.cropYield and \
                self.mCropCalories == theCrop.cropCalories and \
                self.mCropFodderProduction == theCrop.fodderProduction and \
                self.mCropFodderValue == theCrop.fodderValue and \
                self.mCropFodderEnergyType == theCrop.cropFodderEnergyType and \
                self.mAreaUnits == theCrop.areaUnits and \
                self.mImageFile == theCrop.imageFile
        
    def __copy__(self) -> 'LaCrop':
        myNewCrop: LaCrop = LaCrop()
        myNewCrop.mName = self.mName
        myNewCrop.mDescription = self.mDescription
        myNewCrop.setGuid(self.guid)
        myNewCrop.mCropYield = self.mCropYield
        myNewCrop.mCropCalories = self.mCropCalories
        myNewCrop.mCropFodderProduction = self.mCropFodderProduction
        myNewCrop.mCropFodderValue = self.mCropFodderValue
        myNewCrop.mCropFodderEnergyType = self.mCropFodderEnergyType
        myNewCrop.mAreaUnits = self.mAreaUnits
        myNewCrop.mImageFile = self.mImageFile
        return myNewCrop

    def __deepcopy__(self, memo):
        return LaCrop(self)

    @property
    def name(self) -> str:
        """
        Returns the name of the crop.
        """
        return self.mName

    @property
    def description(self) -> str:
        """
        Returns the description of the crop.
        """
        return self.mDescription

    @property
    def cropYield(self) -> int:
        """
        Returns the crop yield of the current crop object.

        :return: float
        """
        return self.mCropYield

    @property
    def cropCalories(self) -> int:
        """
        Returns the number of calories in 1 Kg of that part of the crop which is eaten (ie. the grain or fruit)
        """
        return self.mCropCalories

    @property
    def fodderProduction(self) -> int:
        """
        When harvesting crops, the chaff and straw (fodder) can be saved and
        used as feed for animals. Landuse Analyst needs to know the food value
        of this fodder. This is expressed as number of calories per Kg.
        """
        return self.mCropFodderProduction

    @property
    def fodderValue(self):
        return self.mCropFodderValue

    @property
    def cropFodderEnergyType(self):
        return self.mCropFodderEnergyType

    @property
    def areaUnits(self):
        return self.mAreaUnits

    @property
    def imageFile(self):
        return self.mImageFile

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