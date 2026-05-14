# -*- coding: utf-8 -*-
"""
LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
of a settlement (with respect to required land needed for food production).

This file implements the controller that handles business logic for the main form.

@author:
    Dr. Jason S. Jorgenson <jjorgenson@gmail.com>

@date:
    2025-03-22

@license:
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.
"""

import os
from typing import Dict, Tuple
from qgis.PyQt.QtCore import QObject

from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacropparameter import LaCropParameter


class LaMainController(QObject):
    """
    Controller class that handles business logic for the main form.
    This class coordinates interactions between the UI and models.
    """

    def __init__(self, theLaModel: LaModel):
        """
        Initialize the controller with a model.

        Args:
            model: The model to use
        """
        super().__init__()
        self.model: LaModel = theLaModel

        # Initialize maps for tracking selected items
        # Dict[str, Tuple[bool, str]] - GUID -> (enabled, parameterGuid)
        self.animalsMap: Dict[str, Tuple[bool, str]] = {}
        self.cropsMap: Dict[str, Tuple[bool, str]] = {}

        # Cache for loaded data
        self._animals_cache = None
        self._crops_cache = None
        self._animal_params_cache = None
        self._crop_params_cache = None

    def getAvailableAnimals(self):
        """Get available animals from the model."""
        return LaUtils.getAvailableAnimals()

    def getAvailableCrops(self) -> Dict[str, LaCrop]:
        """
        Get available crops, using cached results if available.

        Returns:
            Dictionary of crops by GUID
        """
        if self._crops_cache is None:
            LaUtils.debug.log("Loading crops from storage", "Controller")
            self._crops_cache = LaUtils.getAvailableCrops()
        return self._crops_cache

    def getAvailableAnimalParameters(self) -> Dict[str, LaAnimalParameter]:
        """
        Get available animal parameters, using cached results if available.

        Returns:
            Dictionary of animal parameters by GUID
        """
        if self._animal_params_cache is None:
            LaUtils.debug.log("Loading animal parameters from storage", "Controller")
            self._animal_params_cache = LaUtils.getAvailableAnimalParameters()
        return self._animal_params_cache

    def getAvailableCropParameters(self) -> Dict[str, LaCropParameter]:
        """
        Get available crop parameters, using cached results if available.

        Returns:
            Dictionary of crop parameters by GUID
        """
        if self._crop_params_cache is None:
            LaUtils.debug.log("Loading crop parameters from storage", "Controller")
            self._crop_params_cache = LaUtils.getAvailableCropParameters()
        return self._crop_params_cache

    def refreshData(self):
        """
        Force refresh of all cached data.
        """
        LaUtils.debug.log("Refreshing all data caches", "Controller")
        self._animals_cache = None
        self._animal_params_cache = None
        self._crops_cache = None
        self._crop_params_cache = None

    def setAnimalEnabled(self, animalGuid: str, enabled: bool):
        """
        Enable or disable an animal for calculations.

        Args:
            animalGuid: GUID of the animal
            enabled: Whether the animal should be enabled
        """
        if animalGuid in self.animalsMap:
            value = self.animalsMap[animalGuid]
            if isinstance(value, tuple) and len(value) >= 2:
                parameterGuid = value[1]
                self.animalsMap[animalGuid] = (enabled, parameterGuid)
            else:
                self.animalsMap[animalGuid] = (enabled, "")
        else:
            self.animalsMap[animalGuid] = (enabled, "")

        LaUtils.debug.log(f"Animal {animalGuid} {'enabled' if enabled else 'disabled'}", "Controller")

    def setCropEnabled(self, cropGuid: str, enabled: bool):
        """
        Enable or disable a crop for calculations.

        Args:
            cropGuid: GUID of the crop
            enabled: Whether the crop should be enabled
        """
        if cropGuid in self.cropsMap:
            value = self.cropsMap[cropGuid]
            if isinstance(value, tuple) and len(value) >= 2:
                parameterGuid = value[1]
                self.cropsMap[cropGuid] = (enabled, parameterGuid)
            else:
                self.cropsMap[cropGuid] = (enabled, "")
        else:
            self.cropsMap[cropGuid] = (enabled, "")

        LaUtils.debug.log(f"Crop {cropGuid} {'enabled' if enabled else 'disabled'}", "Controller")

    def setAnimalParameter(self, animalGuid: str, parameterGuid: str):
        """
        Set the parameter to use for an animal.

        Args:
            animalGuid: GUID of the animal
            parameterGuid: GUID of the parameter to use
        """
        if animalGuid in self.animalsMap:
            value = self.animalsMap[animalGuid]
            if isinstance(value, tuple) and len(value) >= 1:
                enabled = value[0]
                self.animalsMap[animalGuid] = (enabled, parameterGuid)
            else:
                self.animalsMap[animalGuid] = (False, parameterGuid)
        else:
            self.animalsMap[animalGuid] = (False, parameterGuid)

        LaUtils.debug.log(f"Animal {animalGuid} parameter set to {parameterGuid}", "Controller")

    def setCropParameter(self, cropGuid: str, parameterGuid: str):
        """
        Set the parameter to use for a crop.

        Args:
            cropGuid: GUID of the crop
            parameterGuid: GUID of the parameter to use
        """
        if cropGuid in self.cropsMap:
            value = self.cropsMap[cropGuid]
            if isinstance(value, tuple) and len(value) >= 1:
                enabled = value[0]
                self.cropsMap[cropGuid] = (enabled, parameterGuid)
            else:
                self.cropsMap[cropGuid] = (False, parameterGuid)
        else:
            self.cropsMap[cropGuid] = (False, parameterGuid)

        LaUtils.debug.log(f"Crop {cropGuid} parameter set to {parameterGuid}", "Controller")

    def calculateTotalLandNeeded(self, population, diet_settings, enabled_animals, enabled_crops):
        """Calculate total land needed based on population and diet settings."""
        # Set diet ratio settings - convert to integers since model expects int
        self.model.dietPercent = diet_settings['plantAnimalRatio']
        self.model.percentOfDietThatIsFromCrops = diet_settings['wildTamePlantRatio']
        self.model.meatPercent = diet_settings['wildTameAnimalRatio']

        # Update population
        if hasattr(self.model, 'population'):
            self.model.population = population

        # Update enabled animals and crops
        if enabled_animals and hasattr(self.model, 'animals'):
            self.model.animals = enabled_animals
        if enabled_crops and hasattr(self.model, 'crops'):
            self.model.crops = enabled_crops

        # Calculate total land needed
        if hasattr(self.model, 'mDietLabels') and self.model.mDietLabels:
            return getattr(self.model.mDietLabels, 'totalLandNeeded', 0.0)
        return 0.0

    def calculateDietBreakdown(self, plantAnimalRatio, wildTameAnimalRatio, wildTamePlantRatio):
        """Calculate diet breakdown percentages."""
        # Business logic for calculating diet percentages
        animalPercent = plantAnimalRatio
        plantPercent = 100 - plantAnimalRatio

        wildAnimalPercent = wildTameAnimalRatio
        tameAnimalPercent = 100 - wildTameAnimalRatio
        wildPlantPercent = wildTamePlantRatio
        tamePlantPercent = 100 - wildTamePlantRatio

        # Calculate absolute percentages
        absoluteWildAnimalPercent = (animalPercent * wildAnimalPercent) / 100
        absoluteTameAnimalPercent = (animalPercent * tameAnimalPercent) / 100
        absoluteWildPlantPercent = (plantPercent * wildPlantPercent) / 100
        absoluteTamePlantPercent = (plantPercent * tamePlantPercent) / 100

        return {
            'animalPercent': animalPercent,
            'plantPercent': plantPercent,
            'wildAnimalPercent': wildAnimalPercent,
            'tameAnimalPercent': tameAnimalPercent,
            'wildPlantPercent': wildPlantPercent,
            'tamePlantPercent': tamePlantPercent,
            'absoluteWildAnimalPercent': absoluteWildAnimalPercent,
            'absoluteTameAnimalPercent': absoluteTameAnimalPercent,
            'absoluteWildPlantPercent': absoluteWildPlantPercent,
            'absoluteTamePlantPercent': absoluteTamePlantPercent
        }

    def calculateDietPercentages(self, plantAnimalRatio: int, wildTameAnimalRatio: int,
                                 wildTamePlantRatio: int) -> Dict[str, float]:
        """
        Calculate diet percentages based on slider values.

        Args:
            plantAnimalRatio: Value from plant/animal slider (0-100)
            wildTameAnimalRatio: Value from wild/tame animal slider (0-100)
            wildTamePlantRatio: Value from wild/tame plant slider (0-100)

        Returns:
            Dictionary with calculated percentages
        """
        try:
            # Calculate percentages
            animalPercent = plantAnimalRatio
            plantPercent = 100 - plantAnimalRatio

            wildAnimalPercent = animalPercent * wildTameAnimalRatio
            tameAnimalPercent = animalPercent * (100 - wildTameAnimalRatio)
            wildPlantPercent = plantPercent * wildTamePlantRatio
            tamePlantPercent = plantPercent * (100 - wildTamePlantRatio)

            return {
                'animalPercent': animalPercent,
                'plantPercent': plantPercent,
                'wildAnimalPercent': wildAnimalPercent,
                'tameAnimalPercent': tameAnimalPercent,
                'wildPlantPercent': wildPlantPercent,
                'tamePlantPercent': tamePlantPercent
            }

        except Exception as e:
            LaUtils.debug.log(f"Error calculating diet percentages: {str(e)}", "Error")
            return {
                'animalPercent': 0,
                'plantPercent': 0,
                'wildAnimalPercent': 0,
                'tameAnimalPercent': 0,
                'wildPlantPercent': 0,
                'tamePlantPercent': 0
            }

    def calculateAnimalParameterPercentages(self) -> float:
        """Calculate the total percentage of animal parameters."""
        total = 0.0

        try:
            animal_params = self.getAvailableAnimalParameters()

            for animal_guid, (is_enabled, param_guid) in self.animalsMap.items():
                if not is_enabled or not param_guid:
                    continue

                parameter = animal_params.get(param_guid)
                if parameter:
                    try:
                        # Get value from PyQt property
                        percent = parameter.property('percentTameMeat')
                        if percent is not None:
                            total += float(percent)
                    except (ValueError, TypeError):
                        LaUtils.debug.log(f"Invalid percentTameMeat for parameter {param_guid}", "Warning")

            LaUtils.debug.log(f"Total animal parameter percentage: {total:.1f}%", "Calculation")

        except Exception as e:
            LaUtils.debug.log(f"Error calculating animal percentages: {str(e)}", "Error")

        return total

    def calculateCropParameterPercentages(self) -> float:
        """Calculate the total percentage of crop parameters."""
        total = 0.0

        try:
            crop_params = self.getAvailableCropParameters()

            for crop_guid, (is_enabled, param_guid) in self.cropsMap.items():
                if not is_enabled or not param_guid:
                    continue

                parameter = crop_params.get(param_guid)
                if parameter:
                    try:
                        # Get value from PyQt property
                        percent = parameter.property('percentTameCrop')
                        if percent is not None:
                            total += float(percent)
                    except (ValueError, TypeError):
                        LaUtils.debug.log(f"Invalid percentTameCrop for parameter {param_guid}", "Warning")

            LaUtils.debug.log(f"Total crop parameter percentage: {total:.1f}%", "Calculation")

        except Exception as e:
            LaUtils.debug.log(f"Error calculating crop percentages: {str(e)}", "Error")

        return total

    def saveSettings(self):
        """Save controller settings to the model."""
        try:
            if self.model:
                if hasattr(self.model, 'animals'):
                    # Convert Dict[str, Tuple[bool, str]] to Dict[str, str]
                    # Only store the parameter GUID for enabled animals
                    myAnimalsMap: Dict[str, str] = {
                        guid: param_guid
                        for guid, (enabled, param_guid) in self.animalsMap.items()
                        if enabled and param_guid
                    }
                    self.model.animals = myAnimalsMap

                if hasattr(self.model, 'crops'):
                    # Convert Dict[str, Tuple[bool, str]] to Dict[str, str]
                    # Only store the parameter GUID for enabled crops
                    myCropsMap = {
                        guid: param_guid
                        for guid, (enabled, param_guid) in self.cropsMap.items()
                        if enabled and param_guid
                    }
                    self.model.crops = myCropsMap

                LaUtils.debug.log("Controller settings saved to model", "Controller")
        except Exception as e:
            LaUtils.debug.log(f"Error saving settings: {str(e)}", "Error")

    def loadSettings(self):
        """Load controller settings from the model."""
        try:
            if self.model:
                if hasattr(self.model, 'animals'):
                    # Convert Dict[str, str] to Dict[str, Tuple[bool, str]]
                    self.animalsMap = {
                        guid: (True, param_guid)
                        for guid, param_guid in self.model.animals.items()
                    }

                if hasattr(self.model, 'crops'):
                    # Convert Dict[str, str] to Dict[str, Tuple[bool, str]]
                    self.cropsMap = {
                        guid: (True, param_guid)
                        for guid, param_guid in self.model.crops.items()
                    }

                LaUtils.debug.log("Controller settings loaded from model", "Controller")
        except Exception as e:
            LaUtils.debug.log(f"Error loading settings: {str(e)}", "Error")