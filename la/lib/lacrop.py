# lacrop.py
from typing import Optional, Type

# pyqtProperty is a decorator that is used to define Qt properties in Python.   
# It is defined in a stub file that provides type hints
# for PyQt5 classes and methods. The actual implementation of the pyqtProperty
# decorator is in the PyQt5.QtCore module. The pyqtProperty decorator is used   
# to define the properties of the LaCrop class, including name, description,
# cropType, plantingDate, harvestDate, and yieldValue.

from qgis.PyQt.QtCore import (
        QObject, 
        pyqtSignal,
        pyqtProperty, 
        pyqtSlot, 
        Qt
    )
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid

class LaCrop(LaSerialisable, LaGuid):
    """ The LaCrop class represents a crop that can be grown in a simulation. 
    
    This class contains information about the crop's name, description, yield,
    and other properties. Note that the class name is used as a string in the 
    type hint for the `the_crop` parameter. This is necessary because the class 
    definition hasn't been fully parsed yet when the type hint is evaluated. 
    The `Type` type hint is used to refer to the class itself.

    Attributes:
        name (str): The name of the crop.
        description (str): A description of the crop.
        cropYield (int): The yield of the crop in kg/ha.
        cropCalories (int): The number of calories produced by the crop.
        fodderProduction (int): The amount of fodder produced by the crop.
        fodderValue (int): The value of the fodder produced by the crop.
        cropFodderEnergyType (str): The type of energy produced by the crop.
        areaUnits (str): The units used to measure the area of the crop.
        imageFile (str): The image file used to represent the crop.

    """
    def __init__(self, theCrop: Optional[Type['LaCrop']] = None):
        """Initializes a new instance of the LaCrop class.

        Args:
            the_crop (Optional[Type['LaCrop']]): An existing LaCrop object to copy.
                If provided, the new instance will be a copy of the existing object. 
                If not provided, the new instance will be initialized with default values.
        """
        super().__init__()
        if theCrop is None: # If NO crop is provided, initialize with default values.
            self._guid = LaGuid() # @TODO: check that this works.
            self._name = "No Name Set"
            self._description = "Not Set"
            self._cropYield = 60
            self._cropCalories = 3000
            self._cropFodderProduction = 50
            self._cropFodderValue = 1000
        else: # If a crop IS provided, copy the values from the existing crop.
            self._name = theCrop.name
            self._description = theCrop.description
            self.setGuid(theCrop.guid)
            self._cropYield = theCrop.cropYield
            self._cropCalories = theCrop.cropCalories
            self._cropFodderProduction = theCrop.fodderProduction
            self._cropFodderValue = theCrop.fodderValue
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
        return self._name == theCrop.name and \
                self._description == theCrop.description and \
                self.guid == theCrop.guid and \
                self._cropYield == theCrop.cropYield and \
                self._cropCalories == theCrop.cropCalories and \
                self._cropFodderProduction == theCrop.fodderProduction and \
                self._cropFodderValue == theCrop.fodderValue and \
                self.mCropFodderEnergyType == theCrop.cropFodderEnergyType and \
                self.mAreaUnits == theCrop.areaUnits and \
                self.mImageFile == theCrop.imageFile
        
    def __copy__(self) -> 'LaCrop':
        myNewCrop: LaCrop = LaCrop()
        myNewCrop._name = self._name
        myNewCrop._description = self._description
        myNewCrop.setGuid(self.guid)
        myNewCrop._cropYield = self._cropYield
        myNewCrop._cropCalories = self._cropCalories
        myNewCrop._cropFodderProduction = self._cropFodderProduction
        myNewCrop._cropFodderValue = self._cropFodderValue
        myNewCrop.mCropFodderEnergyType = self.mCropFodderEnergyType
        myNewCrop.mAreaUnits = self.mAreaUnits
        myNewCrop.mImageFile = self.mImageFile
        return myNewCrop

    def __deepcopy__(self, memo):
            """
            Create a deep copy of the LaCrop object.

            Args:
                memo: A dictionary that is used to track already copied objects.

            Returns:
                A new instance of LaCrop with the same attribute values as the original.
            """
            return LaCrop(self)

    nameChanged: pyqtSignal = pyqtSignal(str)
    descriptionChanged: pyqtSignal = pyqtSignal(str)
    cropTypeChanged: pyqtSignal = pyqtSignal(str)
    plantingDateChanged: pyqtSignal = pyqtSignal(str)
    harvestDateChanged: pyqtSignal = pyqtSignal(str)
    yieldValueChanged: pyqtSignal = pyqtSignal(int)
    foddervalueChanged: pyqtSignal = pyqtSignal(int)
    areaUnitsChanged: pyqtSignal = pyqtSignal(str)
    imageFileChanged: pyqtSignal = pyqtSignal(str)

    @pyqtProperty(str, notify=nameChanged)
    def name(self): # type: ignore
        return self._name

    @name.setter
    def name(self, name):
        if self._name != name:
            self._name = name
            self.nameChanged.emit(name)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self): # type: ignore
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(str, notify=cropTypeChanged)
    def cropType(self): # type: ignore
        return self._cropType

    @cropType.setter
    def cropType(self, cropType):
        if self._cropType != cropType:
            self._cropType = cropType
            self.cropTypeChanged.emit(cropType)

    @pyqtProperty(str, notify=plantingDateChanged)
    def plantingDate(self): # type: ignore
        return self._plantingDate

    @plantingDate.setter
    def plantingDate(self, plantingDate):
        if self._plantingDate != plantingDate:
            self._plantingDate = plantingDate
            self.plantingDateChanged.emit(plantingDate)

    @pyqtProperty(str, notify=harvestDateChanged)
    def harvestDate(self): # type: ignore
        return self._harvestDate

    @harvestDate.setter
    def harvestDate(self, harvestDate):
        if self._harvestDate != harvestDate:
            self._harvestDate = harvestDate
            self.harvestDateChanged.emit(harvestDate)

    @pyqtProperty(int, notify=yieldValueChanged)
    def yieldValue(self): # type: ignore
        return self._yieldValue

    @yieldValue.setter
    def yieldValue(self, yieldValue):
        if self._yieldValue != yieldValue:
            self._yieldValue = yieldValue
            self.yieldValueChanged.emit(yieldValue)

    @pyqtProperty(str, notify=foddervalueChanged)
    def fodderValue(self): # type: ignore
        return self._fodderValue
    
    @fodderValue.setter
    def fodderValue(self, fodderValue):
        if self._fodderValue != fodderValue:
            self._fodderValue = fodderValue
            self.foddervalueChanged.emit(fodderValue)



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

