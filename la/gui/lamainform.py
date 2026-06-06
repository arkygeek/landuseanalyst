# -*- coding: utf-8 -*-
"""
LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
of a settlement (with respect to required land needed for food production).
Land area targets for each food source supplied to the model are calculated based
on a multitude of demographic and dietary inputs.

This file implements the main form functionality.

@author:
    Dr. Jason S. Jorgenson <jjorgenson@gmail.com>

@date:
    2022-03-22

@version:
    git sha: $Format:%H$

@license:
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.
"""

from qgis.PyQt import QtGui, QtCore, QtWidgets
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtCore import QSettings, Qt, pyqtSlot
from qgis.PyQt.QtWidgets import QApplication, QMessageBox, QDialog
import os
from typing import Dict, List, Optional, Union
from la.lib.laanimal import LaAnimal

from la.ui.lamainformbase import LaMainFormBase
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils, MESSAGE_BUS
from la.lib.lamaincontroller import LaMainController
from la.lib.ladietlabels import LaDietLabels

class LaMainForm(LaMainFormBase):
    """
    Main form for LanduseAnalyst.
    This class extends LaMainFormBase with additional functionality.
    """

    def __init__(self, parent=None):
        """
        Constructor for LaMainForm.

        Initializes the model first and then sets up the UI. It also connects the diet label signals to UI update slots.
        Additionally, it initializes the debug logger before anything else and creates a debug dialog if debug mode is enabled.
        Finally, it loads existing messages from the history and shows the dialog.
        """
        super(LaMainForm, self).__init__(parent)

        # Use the same LaModel instance the base class (LaMainFormBase) created
        # at self.model. Aliasing self.mModel → self.model means click handlers
        # see the same calculation results that setDietLabels populated, instead
        # of operating on a second disconnected model.
        self.mModel = self.model
        # Connect the new signal for calculation logging
        self.mModel.logCalculationStep.connect(self.logToAllChannels) # Add this line

        # Initialize diet labels
        self.mDietLabels = LaDietLabels(parent=self)

        # Basic UI setup
        self.setup()
        self._addFullReportButton()
        self._upgradeGisCombos()
        self.loadImages()
        self.refresh()
        self.readSettings()
        self.connect_additional_signals()

        # Connect diet label signals to UI update slots - do this once
        self._connectDietLabelSignals(self.mDietLabels)

        # TEMP for thesis verification: preload the Min Pop / Chalcolithic
        # scenario so we don't have to re-set inputs every plugin reload.
        # Remove or guard with a setting later. See scratch/thesis_scenarios/
        # min_pop_chalcolithic/ for the canonical scenario values.
        self._applyMinPopValidationDefaults()

        # Initialize diet labels with default values
        self.setDietLabels()  # This will calculate initial values based on default slider positions

        # Initialize debug dialog
        self.mDebugDialog = None
        myDebugMode = QSettings().value("landuse_analyst/debug", False, type=bool)
        LaUtils.debug.setEnabled(myDebugMode)

        if myDebugMode:
            self.ensure_debug_dialog_visible()

        # Connect debug message bus to main form
        MESSAGE_BUS.debugMessaged.connect(self.on_debug_message)

        LaUtils.debug.log("Application initialized", "MainForm")

    # --- alphabetically ordered methods ---

    def _applyMinPopValidationDefaults(self):
        """Preload the 'Min Pop / Chalcolithic / Shuna' thesis verification scenario.

        See scratch/thesis_scenarios/min_pop_chalcolithic/ for the canonical
        spreadsheet values. Sets sliders / spinboxes / checkboxes and selects
        all animals + all crops that have parameter profiles, so the user
        can immediately click a crop or animal in the Calculations tab (or
        press Run) and get thesis-canonical numbers without re-configuring
        the UI on every plugin reload.

        Temporary scaffold. Remove or make conditional (e.g. dev-mode flag,
        explicit menu item) once we have a proper 'Load scenario' UI.
        """
        try:
            from qgis.PyQt.QtCore import Qt as _Qt

            # --- Slider / spinbox / checkbox values ---
            # Values from scratch/thesis_scenarios/min_pop_chalcolithic/
            # 01_settlement_input.csv + 03_animal_selection.csv + 09_crop_selection.csv
            if hasattr(self, 'sbPopulation'):
                self.sbPopulation.setValue(100)
            if hasattr(self, 'sbDailyCalories'):
                self.sbDailyCalories.setValue(2500)
            if hasattr(self, 'sliderDiet'):
                self.sliderDiet.setValue(10)     # ALL Meat % (animal portion of diet)
            if hasattr(self, 'sliderMeat'):
                self.sliderMeat.setValue(99)     # Domestic Animal Contribution (tame meat %)
            if hasattr(self, 'sliderCrop'):
                self.sliderCrop.setValue(90)     # Crop Contribution (domestic crop %)
            if hasattr(self, 'sbDairyUtilisation'):
                self.sbDairyUtilisation.setValue(50)
            if hasattr(self, 'cboxIncludeDairy'):
                self.cboxIncludeDairy.setChecked(False)  # use DairySeparate algorithm
            if hasattr(self, 'cboxBaseOnPlants'):
                self.cboxBaseOnPlants.setChecked(False)  # Animals First
            if hasattr(self, 'cboxLimitDairy'):
                self.cboxLimitDairy.setChecked(False)

            # --- Select all animals that have parameter profiles ---
            if hasattr(self, 'mAnimalsMap'):
                for myGuid in list(self.mAnimalsMap.keys()):
                    myIsSelected, myParamGuid = self.mAnimalsMap[myGuid]
                    if myParamGuid:
                        self.mAnimalsMap[myGuid] = (True, myParamGuid)
                        try:
                            self.addAnimalToCalculationsList(myGuid)
                        except Exception:
                            pass

            # --- Select all crops that have parameter profiles ---
            if hasattr(self, 'mCropsMap'):
                for myGuid in list(self.mCropsMap.keys()):
                    myIsSelected, myParamGuid = self.mCropsMap[myGuid]
                    if myParamGuid:
                        self.mCropsMap[myGuid] = (True, myParamGuid)
                        try:
                            self.addCropToCalculationsList(myGuid)
                        except Exception:
                            pass

            # --- Sync table widget checkboxes to match the map state ---
            if hasattr(self, 'tblAnimals'):
                for myRow in range(self.tblAnimals.rowCount()):
                    myItem = self.tblAnimals.item(myRow, 0)
                    if myItem is not None:
                        myItem.setCheckState(_Qt.Checked)
            if hasattr(self, 'tblCrops'):
                for myRow in range(self.tblCrops.rowCount()):
                    myItem = self.tblCrops.item(myRow, 0)
                    if myItem is not None:
                        myItem.setCheckState(_Qt.Checked)

            LaUtils.debug.log(
                "Applied Min Pop / Chalcolithic scenario defaults "
                f"({sum(1 for _, p in self.mAnimalsMap.values() if p)} animals, "
                f"{sum(1 for _, p in self.mCropsMap.values() if p)} crops selected)",
                "Setup",
            )

        except Exception as e:
            import traceback
            LaUtils.debug.log(
                f"Error applying Min Pop validation defaults: {e}\n{traceback.format_exc()}",
                "Warning",
            )

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def animalCalcClicked(self, current_item, previous_item):
        """
        Display calculation details when an animal is clicked in the calculations list.
        """
        try:
            # If no item is selected, do nothing
            if current_item is None:
                return

            # Get the GUID of the selected animal
            myAnimalGuid = current_item.data(Qt.UserRole)
            if not myAnimalGuid:
                LaUtils.debug.log("No GUID found for selected animal", "Error")
                return
            myAnimalGuid = str(myAnimalGuid) # Ensure string

            # Get the animal object for display purposes
            myAnimal = LaUtils.getAnimal(myAnimalGuid)
            if not myAnimal:
                LaUtils.debug.log(f"Could not find animal with GUID: {myAnimalGuid}", "Error")
                return

            # Display the animal image if available
            if hasattr(self, 'lblAnimalPicCalcs') and hasattr(myAnimal, 'imageFile'):
                myImagePath = LaUtils.resolvePath(str(myAnimal.imageFile), 'image')
                if myImagePath and os.path.exists(myImagePath):
                    self.lblAnimalPicCalcs.setPixmap(QtGui.QPixmap(myImagePath))
                else:
                    self.lblAnimalPicCalcs.clear()

            # Mirror C++ behaviour (lamainform.cpp::animalCalcClicked at line 1540):
            # run the calculation fresh on every click so the user doesn't have
            # to press Run first. setDietLabels pushes current UI state into the
            # model, dispatches the right doCalcs*, and populates report maps.
            self.setDietLabels()

            # --- Retrieve the freshly-populated calculation report ---
            myReportString = "No calculation results available for this animal."
            if hasattr(self.mModel, 'mDietLabels') and self.mModel.mDietLabels:
                myReportMap = self.getPropertyValue(self.mModel.mDietLabels, 'animalCalcsReportMap')
                if isinstance(myReportMap, dict) and myAnimalGuid in myReportMap:
                    myReportPair = myReportMap[myAnimalGuid]
                    if isinstance(myReportPair, tuple) and len(myReportPair) > 0:
                        myReportString = myReportPair[0] # Get the report text
                        LaUtils.debug.log(f"Retrieved report for animal {myAnimal.name}", "Calculation")
                    else:
                        LaUtils.debug.log(f"Report data format error for animal {myAnimalGuid}", "Error")
                else:
                    LaUtils.debug.log(f"No report found in map for animal {myAnimalGuid}", "Calculation")
            else:
                LaUtils.debug.log("mDietLabels not found or empty on model", "Error")

            # Update the text browser
            if hasattr(self, 'textBrowserResultsAnimals'):
                self.textBrowserResultsAnimals.setText(myReportString)

        except Exception as e:
            LaUtils.debug.log(f"Error displaying animal calculations: {str(e)}", "Error")

    def calculateTotalLandNeeded(self):
        """Calculate and display the total land needed."""
        try:
            # Get inputs for calculation
            population = self.sbPopulation.value() if hasattr(self, 'sbPopulation') else 100

            # Package diet settings
            diet_settings = {
                'plantAnimalRatio': self.sliderDiet.value(),
                'wildTameAnimalRatio': self.sliderMeat.value(),
                'wildTamePlantRatio': self.sliderCrop.value()
            }

            # Delegate calculation to controller
            land_needed = self.controller.calculateTotalLandNeeded(
                population=population,
                diet_settings=diet_settings,
                enabled_animals=self.getSelectedAnimals(),
                enabled_crops=self.getSelectedCrops()
            )

            # Display the result (UI code stays in form)
            if hasattr(self, 'lblTotalLandNeeded'):
                self.lblTotalLandNeeded.setText(f"{land_needed:.2f}")

            LaUtils.debug.log(f"Total land needed calculated: {land_needed:.2f} units", "Calculation")

        except Exception as e:
            LaUtils.debug.log(f"Error calculating land needed: {str(e)}", "Error")

    def closeEvent(self, event):
        """Handle window close event - save settings before closing."""
        self.writeSettings()
        super(LaMainForm, self).closeEvent(event)

    def connect_additional_signals(self):
        """Connect additional signals not handled in the base class."""
        # Connect the population spin box to update calculations
        if hasattr(self, 'sbPopulation'):
            self.sbPopulation.valueChanged.connect(self.updateCalculations)

        # Connect the area units combo box to update calculations
        if hasattr(self, 'cbAreaUnits'):
            self.cbAreaUnits.currentIndexChanged.connect(self.updateCalculations)

        # Connect the debug checkbox to enable/disable debug logging
        if hasattr(self, 'cbDebug'):
            self.cbDebug.clicked.connect(self.on_cbDebug_clicked)

        # Override the base class's on_cbDebug_clicked to use our version
        if hasattr(LaMainFormBase, 'on_cbDebug_clicked'):
            self.on_cbDebug_clicked = self.override_on_cbDebug_clicked

        # Connect the calculation list item clicks to the handler methods
        if hasattr(self, 'listWidgetCalculationsAnimal'):
            self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)

        if hasattr(self, 'listWidgetCalculationsCrop'):
            self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)

        LaUtils.debug.log("Additional signals connected", "Setup")

    def connect_diet_label_signals(self):
        """This method is deprecated - use _connect_diet_label_signals() instead"""
        # Delegate to the main connection method for compatibility with any existing calls
        dietLabels = self.mDietLabels if hasattr(self, 'diet_labels') else None
        if dietLabels:
            self._connectDietLabelSignals(dietLabels)
        else:
            LaUtils.debug.log("Warning: deprecated connect_diet_label_signals called with no diet_labels available", "Warning")

    @pyqtSlot(QtWidgets.QListWidgetItem, QtWidgets.QListWidgetItem)
    def cropCalcClicked(self, current_item, previous_item):
        """
        Display calculation details when a crop is clicked in the calculations list.
        """
        try:
            # If no item is selected, do nothing
            if current_item is None:
                return

            # Get the GUID of the selected crop
            myCropGuid = current_item.data(Qt.UserRole)
            if not myCropGuid:
                LaUtils.debug.log("No GUID found for selected crop", "Error")
                return
            myCropGuid = str(myCropGuid) # Ensure string

            # Get the crop object for display purposes
            myCrop = LaUtils.getCrop(myCropGuid)
            if not myCrop:
                LaUtils.debug.log(f"Could not find crop with GUID: {myCropGuid}", "Error")
                return

            # Display the crop image if available
            if hasattr(self, 'lblCropPicCalcs') and hasattr(myCrop, 'imageFile'):
                myImagePath = LaUtils.resolvePath(str(myCrop.imageFile), 'image')
                if myImagePath and os.path.exists(myImagePath):
                    self.lblCropPicCalcs.setPixmap(QtGui.QPixmap(myImagePath))
                else:
                    self.lblCropPicCalcs.clear()

            # Mirror C++ behaviour (lamainform.cpp::cropCalcClicked at line 1341):
            # run the calculation fresh on every click so the user doesn't have
            # to press Run first. setDietLabels pushes current UI state into the
            # model, dispatches the right doCalcs*, and populates report maps.
            # The 100% gating check inside setDietLabels prevents calc until
            # animal + crop percentages both sum to 100%.
            self.setDietLabels()

            # --- Retrieve the freshly-populated calculation report ---
            myReportString = "No calculation results available for this crop."
            if hasattr(self.mModel, 'mDietLabels') and self.mModel.mDietLabels:
                myReportMap = self.getPropertyValue(self.mModel.mDietLabels, 'cropCalcsReportMap')
                if isinstance(myReportMap, dict) and myCropGuid in myReportMap:
                    myReportPair = myReportMap[myCropGuid]
                    if isinstance(myReportPair, tuple) and len(myReportPair) > 0:
                        myReportString = myReportPair[0] # Get the report text
                        LaUtils.debug.log(f"Retrieved report for crop {myCrop.name}", "Calculation")
                    else:
                        LaUtils.debug.log(f"Report data format error for crop {myCropGuid}", "Error")
                else:
                    LaUtils.debug.log(f"No report found in map for crop {myCropGuid}", "Calculation")
            else:
                LaUtils.debug.log("mDietLabels not found or empty on model", "Error")

            # Update the text browser
            if hasattr(self, 'textBrowserResultsCrop'):
                self.textBrowserResultsCrop.setText(myReportString)

        except Exception as e:
            LaUtils.debug.log(f"Error displaying crop calculations: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            if hasattr(self, 'textBrowserResultsCrop'):
                self.textBrowserResultsCrop.setText(f"Error calculating: {str(e)}")

    def getSelectedAnimals(self) -> Dict[str, str]:
        """
        Get the dictionary of selected animals (animal_guid: parameter_guid).
        This is used by the calculation methods.

        Returns:
            Dict mapping animal GUIDs to their parameter GUIDs
        """
        selected_animals = {}

        if not hasattr(self, 'mAnimalsMap'):
            LaUtils.debug.log("No animals map found", "Warning")
            return selected_animals

        # Iterate through animals map and get selected animals
        for animal_guid, value_pair in self.mAnimalsMap.items():
            is_selected, param_guid = value_pair
            if is_selected:
                selected_animals[animal_guid] = param_guid

        return selected_animals

    def getSelectedCrops(self) -> Dict[str, str]:
        """
        Get the dictionary of selected crops (crop_guid: parameter_guid).
        This is used by the calculation methods.

        Returns:
            Dict mapping crop GUIDs to their parameter GUIDs
        """
        selected_crops = {}

        if not hasattr(self, 'mCropsMap'):
            LaUtils.debug.log("No crops map found", "Warning")
            return selected_crops

        # Iterate through crops map and get selected crops
        for crop_guid, value_pair in self.mCropsMap.items():
            is_selected, param_guid = value_pair
            if is_selected:
                selected_crops[crop_guid] = param_guid

        return selected_crops

    def loadImages(self):
        """Load images for the application."""
        try:
            # Load application logo or other static images
            logoPath = ":/la_icon.png"
            if os.path.exists(logoPath):
                self.lblLogo.setPixmap(QPixmap(logoPath))
                self.lblLogo.setScaledContents(True)
        except Exception as e:
            LaUtils.debug.log(f"Error loading images: {str(e)}", "Error")

    def logMessage(self, message: str):
        """
        Add a message to the log.
        This method is maintained for backward compatibility.

        Args:
            message: The message to add
        """
        # Delegate to our unified logging method
        self.logToAllChannels(message)

    def logToAllChannels(self, theMessage):
        """
        Unified logging method that sends messages to all log channels.
        This is the central logging method that all other logging methods should use.

        Args:
            theMessage: The message to log
        """
        # Log to debug dialog if it exists
        if hasattr(self, 'mDebugDialog') and self.mDebugDialog is not None:
            try:
                self.mDebugDialog.addDebugMessage(theMessage)
            except Exception:
                pass

        # Also print to console for development visibility
        # print(f"DEBUG: {theMessage}")

    def on_debug_message(self, message: str):
        """Handle debug messages from the message bus."""
        # Simply delegate to our unified logging method
        self.logToAllChannels(message)

    @pyqtSlot(bool)
    def on_cboxBaseOnPlants_clicked(self, checked):
        """Handle base on plants checkbox changes."""
        self.setDietLabels()

    @pyqtSlot(bool)
    def on_cboxIncludeDairy_clicked(self, checked):
        """Handle include dairy checkbox changes."""
        self.setDietLabels()

    @pyqtSlot(bool)
    def on_cboxLimitDairy_clicked(self, checked):
        """Handle limit dairy checkbox changes."""
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sbDailyCalories_valueChanged(self, value):
        """Handle daily calories spinbox value changes."""
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sbDairyUtilisation_valueChanged(self, value):
        """Handle dairy utilisation spinbox value changes."""
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sbLimitDairyPercent_valueChanged(self, value):
        """Handle dairy limit percentage spinbox value changes."""
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sliderDiet_valueChanged(self, value):
        """Handle diet slider value changes."""
        self.labelMeatPercent.setText(str(value))
        self.labelCropPercent.setText(str(100 - value))
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sliderMeat_valueChanged(self, theValue):
        """Handle meat ratio slider value changes."""
        myMinString = 100 - theValue
        myMaxString = theValue
        self.labelMeatWildPercent.setText(str(myMinString))
        self.labelMeatTamePercent.setText(str(myMaxString))
        self.setDietLabels()

    def readSettings(self):
        """Read application settings."""
        settings = QSettings()

        # Window geometry
        if settings.contains("landuse_analyst/geometry"):
            self.restoreGeometry(settings.value("landuse_analyst/geometry"))

        # Debug mode
        debugMode = settings.value("landuse_analyst/debug", False, type=bool)
        self.cbDebug.setChecked(debugMode)
        
        # We still show/hide the log tab if it exists
        if hasattr(self, 'MainTabs') and hasattr(self, 'log_tab'):
            tabIndex = self.MainTabs.indexOf(self.log_tab)
            if tabIndex >= 0:
                self.MainTabs.setTabVisible(tabIndex, debugMode)

        # Load most recently used values
        if hasattr(self, 'sbPopulation'):
            self.sbPopulation.setValue(settings.value("landuse_analyst/population", 100, type=int))

    def refresh(self):
        """Refresh all displays in the form."""
        # Update all UI elements
        self.loadAnimals()
        self.loadCrops()
        self.updateCalculations()
        self.setDietLabels()

    def setDietLabels(self):
        """Update all diet-related labels based on current values"""
        try:
            # Call the parent class implementation which has the complete implementation
            super(LaMainForm, self).setDietLabels()
            
            myModel = getattr(self, 'mModel', getattr(self, 'model', None))
            if myModel and hasattr(myModel, 'mDietLabels') and myModel.mDietLabels:
                self.mDietLabels = myModel.mDietLabels
                self._connectDietLabelSignals(self.mDietLabels)

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error updating diet labels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def setup(self):
        """Perform additional setup beyond what's in the base class."""
        try:
            # Initialize the main controller
            self.controller = LaMainController(self)

            # Set up initial UI state
            if hasattr(self, 'cbDebug'):
                self.cbDebug.setChecked(False)

            # Initialize model properties
            self.mAnimalsMap = {}
            self.mCropsMap = {}

            # Initial GUI setup
            self.loadImages()
            self.refresh()
            self.readSettings()

            # Setup Jorgenson Thesis UI
            self.initThesisUi()

        except Exception as e:
            LaUtils.debug.log(f"Error in setup: {str(e)}", "Error")

    def updateCalculations(self):
        """Update all calculations based on current settings and selections."""
        # Recalculate total land needed
        self.calculateTotalLandNeeded()

        # Update animal and crop calculations if items are selected
        if hasattr(self, 'listWidgetCalculationsAnimal') and self.listWidgetCalculationsAnimal.currentItem():
            self.animalCalcClicked(self.listWidgetCalculationsAnimal.currentItem(), None)

        if hasattr(self, 'listWidgetCalculationsCrop') and self.listWidgetCalculationsCrop.currentItem():
            self.cropCalcClicked(self.listWidgetCalculationsCrop.currentItem(), None)

    def writeSettings(self):
        """Save application settings."""
        settings = QSettings()

        # Save window geometry
        settings.setValue("landuse_analyst/geometry", self.saveGeometry())

        # Save debug mode state
        settings.setValue("landuse_analyst/debug", self.cbDebug.isChecked())

        # Save most recently used values
        if hasattr(self, 'sbPopulation'):
            settings.setValue("landuse_analyst/population", self.sbPopulation.value())

    # --- private methods ---

    def _applyMinPopValidationDefaults(self):
        """TEMP: preload thesis Min Pop / Chalcolithic scenario inputs.

        Saves the user from re-setting all the inputs on every plugin reload
        while we're verifying the calculation engine against the thesis
        spreadsheet. Inputs match scratch/thesis_scenarios/min_pop_chalcolithic/
        (Population 100, ALL Meat 10%, Domestic Animal 99%, Domestic Crop 90%,
        Dairy Utilisation 50%, Animals First + DairySeparate mode). All four
        animals and all crops with a configured parameter profile are selected.
        Remove this call from __init__ once the validation phase is done.
        """
        try:
            # Numeric inputs
            if hasattr(self, 'sbPopulation'):       self.sbPopulation.setValue(100)
            if hasattr(self, 'sbDailyCalories'):    self.sbDailyCalories.setValue(2500)
            if hasattr(self, 'sbDairyUtilisation'): self.sbDairyUtilisation.setValue(50)

            # Diet sliders (slider position = percentage on that side of the bar)
            if hasattr(self, 'sliderDiet'): self.sliderDiet.setValue(10)  # MEAT side = 10% animal
            if hasattr(self, 'sliderMeat'): self.sliderMeat.setValue(99)  # Domestic side = 99% tame meat
            if hasattr(self, 'sliderCrop'): self.sliderCrop.setValue(90)  # Domestic side = 90% crops

            # Mode selection — Animals First, Dairy Separate (matches spreadsheet algorithm)
            if hasattr(self, 'cboxBaseOnPlants'): self.cboxBaseOnPlants.setChecked(False)
            if hasattr(self, 'cboxIncludeDairy'): self.cboxIncludeDairy.setChecked(False)
            if hasattr(self, 'cboxLimitDairy'):   self.cboxLimitDairy.setChecked(False)

            # Select all animals (the 4 with parameter profiles, sum to 100%)
            if hasattr(self, 'mAnimalsMap'):
                for guid, (_, param_guid) in list(self.mAnimalsMap.items()):
                    if param_guid:
                        self.mAnimalsMap[guid] = (True, param_guid)

            # Select all crops that have a parameter profile (8 of the 11 — those
            # with non-empty param_guid; Grapes/Grass Peas/FreeHull Barley have none)
            if hasattr(self, 'mCropsMap'):
                for guid, (_, param_guid) in list(self.mCropsMap.items()):
                    if param_guid:
                        self.mCropsMap[guid] = (True, param_guid)

            # Re-render the animal + crop tables so the checkboxes reflect the new state
            if hasattr(self, 'loadAnimals'): self.loadAnimals()
            if hasattr(self, 'loadCrops'):   self.loadCrops()

            LaUtils.debug.log("Applied Min Pop / Chalcolithic validation defaults", "Setup")
        except Exception as e:
            LaUtils.debug.log(f"Error applying validation defaults: {e}", "Error")

    def _addFullReportButton(self):
        """Wrap tbReport in a container that adds a Results-tab toolbar with
        [Full Report] [Export PDF] [Export JSON] buttons above the report.

        The tab itself shows the simple styled-tables version (fast to render).
        The Full Report button opens a modal with the rich version (tables +
        matplotlib chart PNGs). Exports work directly from the toolbar without
        needing the modal open — they generate the full report HTML on demand
        and route it through QTextDocument (for PDF) or lareports.toDict
        (for JSON).
        """
        from qgis.PyQt.QtWidgets import (
            QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSplitter, QSizePolicy
        )

        myOldWidget = getattr(self, "tbReport", None)
        if myOldWidget is None:
            return
        myParent = myOldWidget.parentWidget()
        if myParent is None:
            return

        # tbReport's parent in the .ui is a QSplitter. Wrap tbReport in a
        # container that adds a toolbar above it, then put the container back
        # where tbReport was.
        #
        # Force Expanding/Expanding on both the container AND the existing
        # report widget. The .ui file pins tbReport to Fixed/Fixed which makes
        # QSplitter shrink it to a tiny default — override here so the report
        # fills the available space in the Results tab.
        myContainer = QWidget(myParent)
        myContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        myOldWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        myOldWidget.setMinimumSize(0, 0)
        myVBox = QVBoxLayout(myContainer)
        myVBox.setContentsMargins(0, 0, 0, 0)
        myVBox.setSpacing(4)

        myButtonRow = QHBoxLayout()
        self.pbnFullReport = QPushButton("Full Report", myContainer)
        self.pbnExportPdf  = QPushButton("Export PDF",  myContainer)
        self.pbnExportJson = QPushButton("Export JSON", myContainer)
        self.pbnFullReport.setToolTip("Open the full report (tables + charts) in a new window")
        self.pbnExportPdf.setToolTip("Save the full report (tables + charts) as a PDF")
        self.pbnExportJson.setToolTip("Save the report data as JSON (for downstream tooling)")
        self.pbnFullReport.clicked.connect(self._onFullReport)
        self.pbnExportPdf.clicked.connect(self._onExportPdf)
        self.pbnExportJson.clicked.connect(self._onExportJson)
        myButtonRow.addWidget(self.pbnFullReport)
        myButtonRow.addWidget(self.pbnExportPdf)
        myButtonRow.addWidget(self.pbnExportJson)
        myButtonRow.addStretch()
        myVBox.addLayout(myButtonRow)

        # Swap tbReport into the container, handling QSplitter parents
        if isinstance(myParent, QSplitter):
            mySplitIndex = myParent.indexOf(myOldWidget)
            myOldWidget.setParent(None)
            myParent.insertWidget(mySplitIndex, myContainer)
        else:
            myLayout = myParent.layout()
            if myLayout is not None:
                myLayout.replaceWidget(myOldWidget, myContainer)

        myOldWidget.setParent(myContainer)
        myVBox.addWidget(myOldWidget, stretch=1)
        # self.tbReport stays the same QTextBrowser — Run handler still works.

    def _upgradeGisCombos(self):
        """
        Promote the .ui's plain ``cboDEM`` ``QComboBox`` to a
        ``QgsMapLayerComboBox`` and add sibling combos for common-crop and
        common-grazing suitability rasters.

        Done programmatically so the .ui file stays a simple Designer-compatible
        artefact (no customwidget declarations needed). Same pattern used by
        :meth:`_addFullReportButton`.
        """
        from qgis.PyQt.QtWidgets import QLabel
        from qgis.gui import QgsMapLayerComboBox
        from qgis.core import QgsMapLayerProxyModel

        myDemCombo = getattr(self, "cboDEM", None)
        if myDemCombo is None:
            LaUtils.debug.log("cboDEM not found; skipping GIS combo upgrade.", "Warning")
            return
        myParent = myDemCombo.parentWidget()
        myLayout = myParent.layout() if myParent else None
        if myLayout is None:
            LaUtils.debug.log(
                "cboDEM has no parent layout; skipping GIS combo upgrade.", "Warning"
            )
            return

        # Find cboDEM's grid position
        myIndex = myLayout.indexOf(myDemCombo)
        try:
            myRow, myCol, _, _ = myLayout.getItemPosition(myIndex)
        except Exception:
            LaUtils.debug.log(
                "cboDEM not in a QGridLayout; skipping GIS combo upgrade.", "Warning"
            )
            return

        # Replace cboDEM with a QgsMapLayerComboBox in-place
        myNewDem = QgsMapLayerComboBox(myParent)
        myNewDem.setObjectName("cboDEM")
        myNewDem.setFilters(QgsMapLayerProxyModel.RasterLayer)
        myNewDem.setAllowEmptyLayer(True, "(no DEM — skip GIS analysis)")
        myLayout.replaceWidget(myDemCombo, myNewDem)
        myDemCombo.deleteLater()
        self.cboDEM = myNewDem

        # Add common-crop and common-grazing combos right below the DEM row
        self.cboCommonCrop = QgsMapLayerComboBox(myParent)
        self.cboCommonCrop.setObjectName("cboCommonCrop")
        self.cboCommonCrop.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.cboCommonCrop.setAllowEmptyLayer(True, "(no common-crop raster)")

        self.cboCommonGrazing = QgsMapLayerComboBox(myParent)
        self.cboCommonGrazing.setObjectName("cboCommonGrazing")
        self.cboCommonGrazing.setFilters(QgsMapLayerProxyModel.RasterLayer)
        self.cboCommonGrazing.setAllowEmptyLayer(True, "(no common-grazing raster)")

        # Mirror the "DEM:" label column at myCol-2 (label) + myCol (combo).
        myLabelCol = max(0, myCol - 2)
        myLblCC = QLabel("Common Crop Raster:", myParent)
        myLblCC.setAlignment(myLblCC.alignment() | 0x0002)  # right-align numeric flag — harmless on label
        myLayout.addWidget(myLblCC,                 myRow + 1, myLabelCol)
        myLayout.addWidget(self.cboCommonCrop,      myRow + 1, myCol)

        myLblCG = QLabel("Common Grazing Raster:", myParent)
        myLayout.addWidget(myLblCG,                 myRow + 2, myLabelCol)
        myLayout.addWidget(self.cboCommonGrazing,   myRow + 2, myCol)

        LaUtils.debug.log("Upgraded GIS combos (DEM + common-crop + common-grazing).", "Setup")

    def _configureGisInputsFromUi(self):
        """
        Read DEM / common-crop / common-grazing layer ids and the chosen
        distance method from the form. Returns ``None`` if no DEM is picked
        (caller treats that as "run diet report only").

        :rtype: la.lib.lacatchment.LaCatchmentInputs | None
        """
        from la.lib.lacatchment import LaCatchmentInputs, DistanceMethod

        myDemLayer = self.cboDEM.currentLayer() if hasattr(self, "cboDEM") else None
        if myDemLayer is None:
            return None

        myCcLayer = self.cboCommonCrop.currentLayer()    if hasattr(self, "cboCommonCrop")    else None
        myCgLayer = self.cboCommonGrazing.currentLayer() if hasattr(self, "cboCommonGrazing") else None

        # Match the radio buttons we already wire in configureModelFromUi
        myMethod = DistanceMethod.WalkingTime
        if hasattr(self, "radioButtonEuclidean") and self.radioButtonEuclidean.isChecked():
            myMethod = DistanceMethod.Euclidean
        elif hasattr(self, "radioButtonPathDistance") and self.radioButtonPathDistance.isChecked():
            myMethod = DistanceMethod.PathDistance

        return LaCatchmentInputs(
            demLayerId=myDemLayer.id(),
            commonCropLayerId=myCcLayer.id() if myCcLayer is not None else None,
            commonGrazingLayerId=myCgLayer.id() if myCgLayer is not None else None,
            method=myMethod,
        )

    def _launchCatchmentTask(self, theInputs) -> None:
        """
        Verify GRASS Processing availability + chosen method, then submit a
        :class:`la.gui.lacatchmenttask.LaCatchmentTask` to the QGIS task
        manager.

        :param theInputs: :class:`la.lib.lacatchment.LaCatchmentInputs`.
        """
        from qgis.PyQt.QtWidgets import QMessageBox
        from qgis.core import QgsApplication
        from la.lib.lacatchment import DistanceMethod
        from la.lib.lagrassprocesslib import LaGrassProcessLib
        from la.gui.lacatchmenttask import LaCatchmentTask

        if theInputs.method is DistanceMethod.PathDistance:
            QMessageBox.warning(
                self,
                "Path Distance not implemented",
                "Path Distance is not implemented yet. Please choose Walking "
                "Time or Euclidean. The diet report has been generated; "
                "skipping the GIS run.",
            )
            return

        # Method-specific availability check.
        #
        # Walking Time has a pure-Python fallback (LaGrass._makeWalkCostPure
        # using Tobler's hiking function + scipy Dijkstra), so it doesn't
        # require grass:r.walk to be registered — only the per-iteration
        # rasterwork via grass:r.mapcalc.simple.
        #
        # Euclidean uses grass:r.cost with a uniform-1 friction; that
        # algorithm IS required (no pure-Python fallback for Euclidean yet —
        # could be added later, but r.cost is much more reliably registered
        # in QGIS Processing GRASS providers than r.walk).
        myMapcalcAlg = LaGrassProcessLib.mapcalcAlgorithmId()
        myMissing = []
        if myMapcalcAlg is None:
            myMissing.append("grass:r.mapcalc.simple")
        if theInputs.method is DistanceMethod.Euclidean:
            if LaGrassProcessLib.costAlgorithmId() is None:
                myMissing.append("grass:r.cost")

        if myMissing:
            myMissingLines = "\n".join(f"  • {m}" for m in myMissing)
            QMessageBox.warning(
                self,
                "GRASS algorithm(s) unavailable",
                "The catchment-analysis step needs the following GRASS "
                "algorithm(s) which aren't registered in this QGIS:\n\n"
                f"{myMissingLines}\n\n"
                "Likely causes:\n"
                "• The GRASS Processing provider is disabled — enable it via "
                "Settings → Options → Processing → Providers → GRASS.\n"
                "• GRASS itself isn't installed alongside QGIS — install it "
                "(macOS: `brew install grass`; Linux: package manager; "
                "Windows: OSGeo4W) and restart QGIS.\n\n"
                "The diet report has been generated; the GIS step is skipped.",
            )
            return

        myTask = LaCatchmentTask(self.mModel, theInputs, theLivePreview=True)
        myTask.grassMessage.connect(self._onCatchmentMessage)
        myTask.previewUpdated.connect(self._onCatchmentPreviewUpdated)
        QgsApplication.taskManager().addTask(myTask)
        # Keep a reference so Python doesn't garbage-collect it
        self._mCatchmentTask = myTask
        LaUtils.debug.log("Catchment task submitted to QGIS task manager.", "Setup")
        if hasattr(self, "statusBar"):
            self.statusBar().showMessage(
                "Catchment analysis running — see QGIS task manager for progress.",
                8000,
            )

    def _onCatchmentMessage(self, theMessage: str) -> None:
        """Mirror catchment-task log messages into the plugin's debug log."""
        LaUtils.debug.log(theMessage, "Calculation")

    def _onCatchmentPreviewUpdated(
        self,
        theItemName:  str,
        theRasterPath: str,
        theThreshold: float,
        theAchieved:  float,
        theTarget:    float,
    ) -> None:
        """
        Slot called when the background catchment task updates its search preview.
        Loads/updates a temporary raster layer in the "Live Search" group.
        """
        try:
            from qgis.core import QgsProject, QgsRasterLayer, QgsLayerTreeNode
            from qgis.utils import iface
            from la.gui.lacatchmenttask import _GROUP_NAME, _QML_STYLE

            myProject = QgsProject.instance()
            myRoot = myProject.layerTreeRoot()

            # Ensure "Catchment Analysis" group exists
            myGroup = myRoot.findGroup(_GROUP_NAME)
            if myGroup is None:
                myGroup = myRoot.insertGroup(0, _GROUP_NAME)

            # Ensure "Live Search" subgroup exists
            myLiveGroup = myGroup.findGroup("Live Search")
            if myLiveGroup is None:
                myLiveGroup = myGroup.insertGroup(0, "Live Search")

            # Find if layer already exists in the Live Search group
            myExistingLayer = None
            for myNode in myLiveGroup.children():
                if myNode.nodeType() == QgsLayerTreeNode.NodeLayer:
                    myLyr = myNode.layer()
                    if myLyr is not None and myLyr.name().startswith(f"Preview: {theItemName}"):
                        myExistingLayer = myLyr
                        break

            myNewName = f"Preview: {theItemName} (iter threshold: {theThreshold:.1f}, area: {theAchieved:.1f} Ha / target {theTarget:.1f})"

            if myExistingLayer is not None:
                # Reload data provider to refresh canvas cache
                myExistingLayer.dataProvider().reloadData()
                myExistingLayer.setName(myNewName)
                myExistingLayer.triggerRepaint()
            else:
                # Create a new layer
                myLayer = QgsRasterLayer(theRasterPath, myNewName)
                if myLayer.isValid():
                    # Apply style
                    if os.path.exists(_QML_STYLE):
                        myLayer.loadNamedStyle(_QML_STYLE)
                    myProject.addMapLayer(myLayer, False)
                    # Add to the top of the Live Search group
                    myLiveGroup.insertLayer(0, myLayer)
                    myLayer.triggerRepaint()

            # Force map canvas refresh to display the changes immediately
            if iface is not None and iface.mapCanvas() is not None:
                iface.mapCanvas().refresh()

        except Exception as e:
            import traceback
            LaUtils.debug.log(f"Error updating catchment preview: {e}\n{traceback.format_exc()}", "Warning")

    def _onFullReport(self):
        """Run the calc, then open the modal report viewer."""
        if not self._ensureFreshCalc():
            return
        from la.gui.lareportdialog import LaReportDialog
        self._reportDialog = LaReportDialog(
            self.mModel, theCalculationType=self._calculationTypeLabel(), parent=self
        )
        self._reportDialog.show()

    def _onExportPdf(self):
        """Export the full report (tables + charts) to a PDF via QTextDocument."""
        from qgis.PyQt.QtWidgets import QFileDialog
        from qgis.PyQt.QtPrintSupport import QPrinter
        from qgis.PyQt.QtGui import QTextDocument
        from la.lib import lareports

        if not self._ensureFreshCalc():
            return

        myDefault = self._defaultExportFilename("pdf")
        myPath, _ = QFileDialog.getSaveFileName(
            self, "Export Report as PDF", myDefault, "PDF Files (*.pdf)"
        )
        if not myPath:
            return

        try:
            myDoc = QTextDocument()
            myDoc.setHtml(lareports.buildFullReportHtml(
                self.mModel, theCalculationType=self._calculationTypeLabel()
            ))
            myPrinter = QPrinter(QPrinter.HighResolution)
            myPrinter.setOutputFormat(QPrinter.PdfFormat)
            myPrinter.setOutputFileName(myPath)
            myDoc.print_(myPrinter)
            LaUtils.debug.log(f"Exported report PDF to {myPath}", "Setup")
            if hasattr(self, "statusBar"):
                self.statusBar().showMessage(f"PDF exported to {myPath}", 5000)
        except Exception as e:
            LaUtils.debug.log(f"PDF export failed: {e}", "Error")

    def _onExportJson(self):
        """Export the report's underlying data as JSON."""
        import json
        from qgis.PyQt.QtWidgets import QFileDialog
        from la.lib import lareports

        if not self._ensureFreshCalc():
            return

        myDefault = self._defaultExportFilename("json")
        myPath, _ = QFileDialog.getSaveFileName(
            self, "Export Report Data as JSON", myDefault, "JSON Files (*.json)"
        )
        if not myPath:
            return

        try:
            myData = lareports.toDict(self.mModel)
            with open(myPath, "w", encoding="utf-8") as myFile:
                json.dump(myData, myFile, indent=2, ensure_ascii=False)
            LaUtils.debug.log(f"Exported report data JSON to {myPath}", "Setup")
            if hasattr(self, "statusBar"):
                self.statusBar().showMessage(f"JSON exported to {myPath}", 5000)
        except Exception as e:
            LaUtils.debug.log(f"JSON export failed: {e}", "Error")

    def _ensureFreshCalc(self) -> bool:
        """Run the model calc with current UI values. Returns True on success."""
        if hasattr(self, "on_pushButtonRun_clicked"):
            try:
                self.on_pushButtonRun_clicked()
            except Exception as e:
                LaUtils.debug.log(f"Run failed: {e}", "Error")
                return False
        return bool(getattr(self.mModel, "mDietLabels", None))

    def _calculationTypeLabel(self) -> str:
        if self.cboxBaseOnPlants.isChecked():
            return "Plants First (" + (
                "Include Dairy" if self.cboxIncludeDairy.isChecked() else "Dairy Separate"
            ) + ")"
        return "Animals First (" + (
            "Include Dairy" if self.cboxIncludeDairy.isChecked() else "Dairy Separate"
        ) + ")"

    def _defaultExportFilename(self, theExt: str) -> str:
        import os
        myName = getattr(self.mModel, "name", "") or "landuse_analyst_report"
        mySafe = "".join(c if c.isalnum() or c in "-_." else "_" for c in str(myName))
        return os.path.join(os.path.expanduser("~"), f"{mySafe}.{theExt}")

    def _connectDietLabelSignals(self, dietLabels):
        """Connect diet label signals to UI update slots."""
        try:
            if not dietLabels:
                LaUtils.debug.log("No diet labels to connect signals to", "Warning")
                return

            # Portion percentage signals
            if hasattr(dietLabels, 'dairyPortionPctChanged'):
                dietLabels.dairyPortionPctChanged.connect(self.update_dairy_portion)
            if hasattr(dietLabels, 'tameMeatPortionPctChanged'):
                dietLabels.tameMeatPortionPctChanged.connect(self.update_tame_meat_portion)
            if hasattr(dietLabels, 'cropsPortionPctChanged'):
                dietLabels.cropsPortionPctChanged.connect(self.update_crops_portion)
            if hasattr(dietLabels, 'wildAnimalPortionPctChanged'):
                dietLabels.wildAnimalPortionPctChanged.connect(self.update_wild_animal_portion)
            if hasattr(dietLabels, 'wildPlantsPortionPctChanged'):
                dietLabels.wildPlantsPortionPctChanged.connect(self.update_wild_plants_portion)

            # Total portion signals
            if hasattr(dietLabels, 'plantsPortionPctChanged'):
                dietLabels.plantsPortionPctChanged.connect(self.update_plants_portion)
            if hasattr(dietLabels, 'animalPortionPctChanged'):
                dietLabels.animalPortionPctChanged.connect(self.update_animal_portion)

            # Other calorie values
            if hasattr(dietLabels, 'kiloCaloriesIndividualAnnualChanged'):
                dietLabels.kiloCaloriesIndividualAnnualChanged.connect(self.update_calories_individual)
            if hasattr(dietLabels, 'megaCaloriesSettlementAnnualChanged'):
                dietLabels.megaCaloriesSettlementAnnualChanged.connect(self.update_calories_settlement)
            if hasattr(dietLabels, 'dairySurplusMCaloriesChanged'):
                dietLabels.dairySurplusMCaloriesChanged.connect(self.update_dairy_surplus)

            LaUtils.debug.log("Diet label signals connected successfully", "Diet")
        except Exception as e:
            LaUtils.debug.log(f"Error connecting diet label signals: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def configureModelFromUi(self):
        """Configure the model with current UI values."""
        if hasattr(self, 'model'):
            # Configure basic settings
            self.mModel.baseOnPlants = self.cboxBaseOnPlants.isChecked()
            self.mModel.includeDairy = self.cboxIncludeDairy.isChecked()
            self.mModel.limitDairy = self.cboxLimitDairy.isChecked()
            self.mModel.limitDairyPercent = self.sbLimitDairyPercent.value()
            self.mModel.caloriesPerPersonDaily = self.sbDailyCalories.value()

            # Configure model with selected animals and crops
            self.mModel.mAnimalsMap = self.getSelectedAnimals()
            self.mModel.mCropsMap = self.getSelectedCrops()

            # Configure dairy utilisation if available
            if hasattr(self, 'sbDairyUtilisation'):
                self.mModel.dairyUtilisation = self.sbDairyUtilisation.value()

    def ensure_debug_dialog_visible(self):
        """Ensure the debug dialog is created and visible."""
        if not self.mDebugDialog:
            from la.gui.ladebugdialog import LaDebugDialog
            self.mDebugDialog = LaDebugDialog.get_instance(parent=self)
            # Signal connection is now handled in __init__ and dialog constructor
        self.mDebugDialog.show()
        self.mDebugDialog.raise_()
        self.mDebugDialog.activateWindow()

    def getPropertyValue(self, obj, prop_name: str):
        """Helper method to safely get PyQt property values"""
        if hasattr(obj, prop_name):
            prop = getattr(obj, prop_name)
            if hasattr(prop, '__get__'):  # If it's a property
                return prop.__get__(obj)
            return prop
        return None

    def on_debug_dialog_closed(self):
        """Handle debug dialog close event."""
        self.mDebugDialog = None

    def override_on_cbDebug_clicked(self):
        """Override for debug checkbox click handler."""
        if self.cbDebug.isChecked():
            self.ensure_debug_dialog_visible()
        elif self.mDebugDialog:
            self.mDebugDialog.close()

    def on_pushButtonRun_clicked(self):
        """
        Handle the Run button click event.
        
        This method configures the model with the current UI values,
        performs the calculations, and displays the results in the report tab.
        """
        try:
            # Update progress
            if hasattr(self, 'statusBar'):
                self.statusBar().showMessage("Running model calculations...")
            
            # Configure model from UI
            self.configureModelFromUi()
            
            # Check that animal and crop percentages add up to 100%
            animalPercentTotal = float(self.labelAnimalCheck.text().replace('%', ''))
            cropPercentTotal = float(self.labelCropCheck.text().replace('%', ''))
            
            if abs(animalPercentTotal - 100.0) > 0.1 or abs(cropPercentTotal - 100.0) > 0.1:
                self.tbReport.setHtml(
                    "<h2>Error: Percentages Must Equal 100%</h2>"
                    "<p>Check that Animals and Crops are both at 100%.</p>"
                    "<p>I am NOT going to do anything until they are!</p>"
                )
                return
            
            # Perform calculations based on diet settings
            myDietLabels: LaDietLabels = LaDietLabels()
            myCalculationType = ""
            
            if self.cboxBaseOnPlants.isChecked():
                if self.cboxIncludeDairy.isChecked():
                    myDietLabels = self.mModel.doCalcsPlantsFirstIncludeDairy()
                    myCalculationType = "Plants First (Include Dairy)"
                else:
                    myDietLabels = self.mModel.doCalcsPlantsFirstDairySeparate()
                    myCalculationType = "Plants First (Dairy Separate)"
            else:
                if self.cboxIncludeDairy.isChecked():
                    myDietLabels = self.mModel.doCalcsAnimalsFirstIncludeDairy()
                    myCalculationType = "Animals First (Include Dairy)"
                else:
                    myDietLabels = self.mModel.doCalcsAnimalsFirstDairySeparate()
                    myCalculationType = "Animals First (Dairy Separate)"
            
            # Store the diet labels for future reference
            self.mModel.mDietLabels = myDietLabels
            
            # Generate the report. Building the full document as one HTML string
            # and assigning via setHtml() keeps Qt's rich-text engine from
            # wrapping each fragment in its own paragraph block, which would
            # break the consistent table styling.
            # The tab gets the simple, fast-rendering version: scenario header,
            # diet summary, selections + settings, diet composition (as tables),
            # plus the six per-item target tables. Charts and exports live in
            # the "Full Report" modal — see _onFullReport.
            from la.lib import lareports
            myReportHtml = (
                '<h1 style="color:#3B5A8C; margin-bottom:4px;">'
                'LanduseAnalyst Calculation Results</h1>'
                f'<p style="color:#666; font-style:italic; margin-top:0;">'
                f'Calculation Method: {myCalculationType}</p>'
                + lareports.toHtml(self.mModel, theIncludeCharts=False)
                + lareports.toHtmlCalorieCropTargets(self.mModel)
                + lareports.toHtmlCalorieAnimalTargets(self.mModel)
                + lareports.toHtmlProductionCropTargets(self.mModel)
                + lareports.toHtmlProductionAnimalTargets(self.mModel)
                + lareports.toHtmlAreaCropTargets(self.mModel)
                + lareports.toHtmlAreaAnimalTargets(self.mModel)
            )
            self.tbReport.setHtml(myReportHtml)
            
            # Switch to the report tab
            if hasattr(self, 'tabWidgetMain'):
                reportTabIndex = self.findTabIndex('Report')
                if reportTabIndex >= 0:
                    self.tabWidgetMain.setCurrentIndex(reportTabIndex)
            
            # Update status
            if hasattr(self, 'statusBar'):
                self.statusBar().showMessage("Calculation complete", 3000)

            LaUtils.debug.log("Model calculations completed successfully", "Calculation")

            # Tail step: if the user has picked a DEM, run the catchment
            # analysis in the background. The diet report has already
            # rendered; this just adds GIS output to the canvas when ready.
            myGisInputs = self._configureGisInputsFromUi()
            if myGisInputs is not None:
                self._launchCatchmentTask(myGisInputs)
            else:
                LaUtils.debug.log(
                    "No DEM selected — skipping catchment analysis.", "Setup"
                )

        except Exception as e:
            LaUtils.debug.log(f"Error running model: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            self.tbReport.setHtml(f"<h2>Error Running Model</h2><p>{str(e)}</p>")
            
    def findTabIndex(self, tabName):
        """Find the index of a tab by name."""
        if not hasattr(self, 'tabWidgetMain'):
            return -1
            
        for i in range(self.tabWidgetMain.count()):
            if self.tabWidgetMain.tabText(i) == tabName:
                return i
        return -1

    @pyqtSlot()
    def on_pushButtonSave_clicked(self):
        """Handle save scenario button click."""
        myFileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save Scenario Profile",
            "",
            "XML Files (*.xml)"
        )
        if myFileName:
            self.configureModelFromUi()
            try:
                myXml = self.mModel.exportScenario()
                with open(myFileName, 'w', encoding='utf-8') as myFile:
                    myFile.write(myXml)
                QtWidgets.QMessageBox.information(
                    self,
                    "Scenario Saved",
                    f"Successfully saved scenario profile to:\n{myFileName}"
                )
            except Exception as myEx:
                QtWidgets.QMessageBox.critical(
                    self,
                    "Save Error",
                    f"Failed to save scenario profile:\n{str(myEx)}"
                )

    @pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        """Handle load scenario button click."""
        myFileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Load Scenario Profile",
            "",
            "XML Files (*.xml)"
        )
        if myFileName:
            try:
                with open(myFileName, 'r', encoding='utf-8') as myFile:
                    myXml = myFile.read()
                
                if not self.mModel.importScenario(myXml):
                    raise ValueError("Failed to parse scenario XML file.")
                
                # Update MainForm selections from Model's selections
                self.mCropsMap.clear()
                myAvailableCrops = LaUtils.getAvailableCrops()
                for myGuid in myAvailableCrops.keys():
                    if myGuid in self.mModel.mCropsMap:
                        self.mCropsMap[myGuid] = (True, self.mModel.mCropsMap[myGuid])
                    else:
                        self.mCropsMap[myGuid] = (False, "")
                        
                self.mAnimalsMap.clear()
                myAvailableAnimals = LaUtils.getAvailableAnimals()
                for myGuid in myAvailableAnimals.keys():
                    if myGuid in self.mModel.mAnimalsMap:
                        self.mAnimalsMap[myGuid] = (True, self.mModel.mAnimalsMap[myGuid])
                    else:
                        self.mAnimalsMap[myGuid] = (False, "")
                
                # Populate UI controls from Model properties
                self.populateUiFromModel()
                
                # Refresh tables to show imported selections
                self.loadCrops()
                self.loadAnimals()
                
                # Update diet labels and run calculations
                self.setDietLabels()
                self.updateCalculations()
                
                QtWidgets.QMessageBox.information(
                    self,
                    "Scenario Loaded",
                    f"Successfully loaded scenario profile from:\n{myFileName}"
                )
            except Exception as myEx:
                QtWidgets.QMessageBox.critical(
                    self,
                    "Load Error",
                    f"Failed to load scenario profile:\n{str(myEx)}"
                )

    def populateUiFromModel(self):
        """Populate UI widgets with values from self.mModel."""
        if not hasattr(self, 'mModel'):
            return

        widgets = [
            'lineEditSiteName', 'lineEditPeriod', 'sbPopulation', 'lineEditEasting', 'lineEditNorthing',
            'sbDailyCalories', 'cboxBaseOnPlants', 'cboxIncludeDairy', 'cboxLimitDairy', 'sbLimitDairyPercent',
            'sbDairyUtilisation', 'sbModelPrecision', 'radioButtonEuclidean', 'radioButtonWalkingTime',
            'radioButtonPathDistance', 'cbAreaUnits', 'cbCommonLandEnergyType', 'sbCommonRasterValue',
            'sliderDiet', 'sliderMeat', 'sliderCrop'
        ]
        
        # Block signals to prevent GUI feedback loops
        blocked_states = {}
        for name in widgets:
            widget = getattr(self, name, None)
            if widget is not None:
                blocked_states[widget] = widget.blockSignals(True)

        try:
            if hasattr(self, 'lineEditSiteName'):
                self.lineEditSiteName.setText(self.mModel.name)
            if hasattr(self, 'lineEditPeriod'):
                self.lineEditPeriod.setText(self.mModel.period)
            if hasattr(self, 'sbPopulation'):
                self.sbPopulation.setValue(self.mModel.population)
            if hasattr(self, 'lineEditEasting'):
                self.lineEditEasting.setText(str(self.mModel.easting))
            if hasattr(self, 'lineEditNorthing'):
                self.lineEditNorthing.setText(str(self.mModel.northing))
            if hasattr(self, 'sbDailyCalories'):
                self.sbDailyCalories.setValue(self.mModel.caloriesPerPersonDaily)
            if hasattr(self, 'cboxBaseOnPlants'):
                self.cboxBaseOnPlants.setChecked(self.mModel.baseOnPlants)
            if hasattr(self, 'cboxIncludeDairy'):
                self.cboxIncludeDairy.setChecked(self.mModel.includeDairy)
            if hasattr(self, 'cboxLimitDairy'):
                self.cboxLimitDairy.setChecked(self.mModel.limitDairy)
            if hasattr(self, 'sbLimitDairyPercent'):
                self.sbLimitDairyPercent.setValue(self.mModel.limitDairyPercent)
            if hasattr(self, 'sbDairyUtilisation'):
                self.sbDairyUtilisation.setValue(self.mModel.dairyUtilisation)
            if hasattr(self, 'sbModelPrecision'):
                self.sbModelPrecision.setValue(self.mModel.precision)

            if hasattr(self, 'radioButtonEuclidean'):
                self.radioButtonEuclidean.setChecked(self.mModel.euclideanDistance)
            if hasattr(self, 'radioButtonWalkingTime'):
                self.radioButtonWalkingTime.setChecked(self.mModel.walkingTime)
            if hasattr(self, 'radioButtonPathDistance'):
                self.radioButtonPathDistance.setChecked(self.mModel.pathDistance)

            if hasattr(self, 'cbAreaUnits'):
                myText = self.mModel.commonLandAreaUnits.name
                myIndex = self.cbAreaUnits.findText(myText)
                if myIndex >= 0:
                    self.cbAreaUnits.setCurrentIndex(myIndex)

            if hasattr(self, 'cbCommonLandEnergyType'):
                myText = self.mModel.specificLandEnergyType.name
                myIndex = self.cbCommonLandEnergyType.findText(myText)
                if myIndex >= 0:
                    self.cbCommonLandEnergyType.setCurrentIndex(myIndex)

            if hasattr(self, 'sbCommonRasterValue'):
                self.sbCommonRasterValue.setValue(int(self.mModel.commonLandValue or 0))

            if hasattr(self, 'sliderDiet'):
                self.sliderDiet.setValue(self.mModel.dietPercent)
            if hasattr(self, 'sliderMeat'):
                self.sliderMeat.setValue(self.mModel.meatPercent)
            if hasattr(self, 'sliderCrop'):
                self.sliderCrop.setValue(self.mModel.percentOfDietThatIsFromCrops)
        finally:
            # Restore signals
            for widget, state in blocked_states.items():
                widget.blockSignals(state)

    def initThesisUi(self):
        """Set up the Jorgenson Thesis Scenarios and Shuna Demo Data UI components."""
        from qgis.PyQt.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QPushButton
        from qgis.PyQt.QtCore import Qt
        
        # 1. Create the GroupBox
        self.grpThesis = QGroupBox("Jorgenson PhD Thesis Scenarios & Shuna Demo Data", self.main_tab)
        
        # 2. Grid Layout inside the GroupBox
        myThesisLayout = QGridLayout(self.grpThesis)
        
        # Label
        self.lblThesis = QLabel("Select Thesis Scenario:", self.grpThesis)
        myThesisLayout.addWidget(self.lblThesis, 0, 0)
        
        # Combobox
        self.cboThesisScenarios = QComboBox(self.grpThesis)
        self.cboThesisScenarios.setMinimumWidth(300)
        myThesisLayout.addWidget(self.cboThesisScenarios, 0, 1)
        
        # Button: Load Scenario
        self.btnLoadThesisScenario = QPushButton("Load Scenario", self.grpThesis)
        self.btnLoadThesisScenario.clicked.connect(self.on_btnLoadThesisScenario_clicked)
        myThesisLayout.addWidget(self.btnLoadThesisScenario, 0, 2)
        
        # Button: Load Shuna Layers
        self.btnLoadShunaLayers = QPushButton("Load Shuna Map Layers", self.grpThesis)
        self.btnLoadShunaLayers.clicked.connect(self.on_btnLoadShunaLayers_clicked)
        myThesisLayout.addWidget(self.btnLoadShunaLayers, 0, 3)
        
        # 3. Add the GroupBox to the main tab layout
        # In main_tab, the grid layout has row 2 which previously had a spacer in column 1.
        # Let's add grpThesis at Row 2, Column 1, spanning 1 row and 2 columns.
        if self.main_tab.layout():
            self.main_tab.layout().addWidget(self.grpThesis, 2, 1, 1, 2)
            
        # 4. Populate the combobox with scenarios
        self.populateThesisScenariosCombo()

    def populateThesisScenariosCombo(self):
        """Search the plugin's thesis_scenarios folder and populate the combobox."""
        import xml.etree.ElementTree as ET
        
        plugin_dir = os.path.dirname(os.path.dirname(__file__))
        thesis_scenarios_dir = os.path.join(plugin_dir, "thesis_scenarios")
        
        if not os.path.exists(thesis_scenarios_dir):
            LaUtils.debug.log(f"Thesis scenarios directory not found: {thesis_scenarios_dir}", "Warning")
            return
            
        # List xml files
        xml_files = sorted([f for f in os.listdir(thesis_scenarios_dir) if f.endswith(".xml")])
        for filename in xml_files:
            file_path = os.path.join(thesis_scenarios_dir, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                model_el = root.find("model")
                if model_el is not None:
                    name_el = model_el.find("name")
                    if name_el is not None and name_el.text:
                        scenario_name = name_el.text
                        self.cboThesisScenarios.addItem(scenario_name, file_path)
            except Exception as e:
                LaUtils.debug.log(f"Error parsing scenario {filename}: {e}", "Warning")

    def on_btnLoadThesisScenario_clicked(self):
        """Load the selected thesis scenario."""
        index = self.cboThesisScenarios.currentIndex()
        if index < 0:
            return
        file_path = self.cboThesisScenarios.itemData(index)
        if not file_path or not os.path.exists(file_path):
            QtWidgets.QMessageBox.warning(self, "File Not Found", "The scenario file could not be found.")
            return
            
        try:
            with open(file_path, 'r', encoding='utf-8') as myFile:
                myXml = myFile.read()
            
            # Clear registries before importing scenario to avoid mixing up parameter data
            LaUtils.clearRegistries()
            
            if not self.mModel.importScenario(myXml):
                raise ValueError("Failed to parse scenario XML file.")
            
            # Update MainForm selections from Model's selections
            self.mCropsMap.clear()
            myAvailableCrops = LaUtils.getAvailableCrops()
            for myGuid in myAvailableCrops.keys():
                if myGuid in self.mModel.mCropsMap:
                    self.mCropsMap[myGuid] = (True, self.mModel.mCropsMap[myGuid])
                else:
                    self.mCropsMap[myGuid] = (False, "")
                    
            self.mAnimalsMap.clear()
            myAvailableAnimals = LaUtils.getAvailableAnimals()
            for myGuid in myAvailableAnimals.keys():
                if myGuid in self.mModel.mAnimalsMap:
                    self.mAnimalsMap[myGuid] = (True, self.mModel.mAnimalsMap[myGuid])
                else:
                    self.mAnimalsMap[myGuid] = (False, "")
            
            # Populate UI controls from Model properties
            self.populateUiFromModel()
            
            # Refresh tables to show imported selections
            self.loadCrops()
            self.loadAnimals()
            
            # Update diet labels and run calculations
            self.setDietLabels()
            self.updateCalculations()
            
            # Auto-select the loaded rasters if they are loaded in QGIS
            self._selectLoadedLayersInCombos()
            
            QtWidgets.QMessageBox.information(
                self,
                "Scenario Loaded",
                f"Successfully loaded thesis scenario:\n{self.cboThesisScenarios.itemText(index)}"
            )
        except Exception as myEx:
            import traceback
            LaUtils.debug.log(f"Load thesis scenario error: {str(myEx)}\n{traceback.format_exc()}", "Error")
            QtWidgets.QMessageBox.critical(
                self,
                "Load Error",
                f"Failed to load scenario profile:\n{str(myEx)}"
            )

    def on_btnLoadShunaLayers_clicked(self):
        """Load Shuna DEM and suitability rasters into QGIS canvas."""
        dem_name = "dem_full.tif"
        suit_name = "suitability_full.tif"
        
        user_dir = LaUtils.userSettingsDirPath()
        shuna_dir = os.path.join(user_dir, "shuna")
        os.makedirs(shuna_dir, exist_ok=True)
        
        target_dem = os.path.join(shuna_dir, dem_name)
        target_suit = os.path.join(shuna_dir, suit_name)
        
        # Source paths to search:
        search_dirs = [
            "/home/arkygeek/Dev/LA/landuseanalyst-web/data/shuna",
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "landuseanalyst-web", "data", "shuna")),
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data")),
        ]
        
        found_dem = os.path.exists(target_dem)
        found_suit = os.path.exists(target_suit)
        
        import shutil
        for name, target_path, found in [
            (dem_name, target_dem, found_dem),
            (suit_name, target_suit, found_suit)
        ]:
            if not found:
                # Try to find it
                for s_dir in search_dirs:
                    src_path = os.path.join(s_dir, name)
                    if os.path.exists(src_path):
                        try:
                            shutil.copy(src_path, target_path)
                            if name == dem_name:
                                found_dem = True
                            else:
                                found_suit = True
                            break
                        except Exception as e:
                            LaUtils.debug.log(f"Failed to copy {name} from {src_path}: {e}", "Error")
                            
        if not found_dem or not found_suit:
            QtWidgets.QMessageBox.warning(
                self,
                "Data Not Found",
                "Could not locate Shuna demo raster files. Please ensure the landuseanalyst-web repository is located next to the plugin."
            )
            return
            
        # Register in QGIS Project
        from qgis.core import QgsRasterLayer, QgsProject
        
        # Check if already loaded
        dem_layer = None
        suit_layer = None
        
        for layer in QgsProject.instance().mapLayers().values():
            if isinstance(layer, QgsRasterLayer):
                source = layer.source()
                if source == target_dem or layer.name() == "Shuna DEM":
                    dem_layer = layer
                elif source == target_suit or layer.name() == "Shuna Suitability":
                    suit_layer = layer
                    
        # Load them if not present
        loaded_new = False
        if dem_layer is None:
            dem_layer = QgsRasterLayer(target_dem, "Shuna DEM")
            if dem_layer.isValid():
                QgsProject.instance().addMapLayer(dem_layer)
                loaded_new = True
            else:
                QtWidgets.QMessageBox.critical(self, "Invalid Raster", f"Failed to load DEM: {target_dem}")
                
        if suit_layer is None:
            suit_layer = QgsRasterLayer(target_suit, "Shuna Suitability")
            if suit_layer.isValid():
                QgsProject.instance().addMapLayer(suit_layer)
                loaded_new = True
            else:
                QtWidgets.QMessageBox.critical(self, "Invalid Raster", f"Failed to load Suitability: {target_suit}")
                
        # Select them in the combos
        if dem_layer and hasattr(self, "cboDEM"):
            self.cboDEM.setLayer(dem_layer)
        if suit_layer and hasattr(self, "cboCommonCrop"):
            self.cboCommonCrop.setLayer(suit_layer)
            
        if loaded_new:
            QtWidgets.QMessageBox.information(
                self,
                "Layers Loaded",
                "Successfully loaded Shuna DEM and Suitability layers into QGIS project."
            )
        else:
            QtWidgets.QMessageBox.information(
                self,
                "Layers Active",
                "Shuna DEM and Suitability layers are already active in the project."
            )

    def _selectLoadedLayersInCombos(self):
        """Auto-select matching loaded map layers in DEM and Common Crop combo boxes."""
        from qgis.core import QgsProject, QgsRasterLayer
        
        user_dir = LaUtils.userSettingsDirPath()
        shuna_dir = os.path.join(user_dir, "shuna")
        target_dem = os.path.join(shuna_dir, "dem_full.tif")
        target_suit = os.path.join(shuna_dir, "suitability_full.tif")
        
        dem_layer = None
        suit_layer = None
        
        for layer in QgsProject.instance().mapLayers().values():
            if isinstance(layer, QgsRasterLayer):
                source = layer.source()
                if source == target_dem or layer.name() == "Shuna DEM":
                    dem_layer = layer
                elif source == target_suit or layer.name() == "Shuna Suitability":
                    suit_layer = layer
                    
        if dem_layer and hasattr(self, "cboDEM"):
            self.cboDEM.setLayer(dem_layer)
        if suit_layer and hasattr(self, "cboCommonCrop"):
            self.cboCommonCrop.setLayer(suit_layer)

