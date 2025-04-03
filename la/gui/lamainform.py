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

        # Initialize the model first
        self.model = LaModel(self)
        # Connect the new signal for calculation logging
        self.model.logCalculationStep.connect(self.logToAllChannels) # Add this line

        # Initialize diet labels
        self.diet_labels = LaDietLabels(parent=self)

        # Basic UI setup
        self.setup()
        self.loadImages()
        self.refresh()
        self.readSettings()
        self.connect_additional_signals()

        # Connect diet label signals to UI update slots - do this once
        self._connect_diet_label_signals(self.diet_labels)

        # Initialize diet labels with default values
        self.setDietLabels()  # This will calculate initial values based on default slider positions

        # Initialize debug dialog
        self._debug_dialog = None
        debugMode = QSettings().value("landuse_analyst/debug", False, type=bool)
        LaUtils.debug.initialize(enabled=debugMode)

        if debugMode:
            from la.gui.ladebugdialog import LaDebugDialog
            self._debug_dialog = LaDebugDialog(parent=self)
            if hasattr(self._debug_dialog, 'add_debug_message'):
                MESSAGE_BUS.debugMessaged.connect(self._debug_dialog.add_debug_message)
            if self._debug_dialog is not None:
                self._debug_dialog.show()

        # Connect debug message bus to main form
        MESSAGE_BUS.debugMessaged.connect(self.on_debug_message)
        LaUtils.debug.log("Application initialized", "MainForm")

    # --- alphabetically ordered methods ---

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
            animal_guid = current_item.data(Qt.UserRole)
            if hasattr(animal_guid, 'guid') and callable(animal_guid.guid):
                animal_guid = animal_guid.guid()  # Call the method to get the GUID string

            # Make sure we have a string GUID
            animal_guid = str(animal_guid)

            LaUtils.debug.log(f"Using animal GUID: {animal_guid}", "Calculation")

            # Get the animal object
            animal = LaUtils.getAnimal(animal_guid)
            if not animal:
                LaUtils.debug.log(f"Could not find animal with GUID: {animal_guid}", "Error")
                return

            # Perform calculations based on diet settings
            diet_labels = None
            if self.cboxBaseOnPlants.isChecked():
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsPlantsFirstIncludeDairy()
                else:
                    diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
            else:
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()
                else:
                    diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()

            # Get the calculation report for this animal
            if hasattr(diet_labels, 'animalCalcsReportMap'):
                report_map = self._getPropertyValue(diet_labels, 'animalCalcsReportMap')
                if isinstance(report_map, dict):
                    if animal_guid in report_map:
                        report_pair = report_map[animal_guid]
                        if isinstance(report_pair, tuple) and len(report_pair) > 0:
                            report_string = report_pair[0]
                            if hasattr(self, 'textBrowserResultsAnimals'):
                                self.textBrowserResultsAnimals.setText(report_string)
                                LaUtils.debug.log(f"Animal {animal.name} calculation report displayed", "Calculation")

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
                enabled_animals=self.getEnabledAnimals(),
                enabled_crops=self.getEnabledCrops() if hasattr(self, 'getEnabledCrops') else []
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
            self.on_cbDebug_clicked = self._override_on_cbDebug_clicked

        # Connect the calculation list item clicks to the handler methods
        if hasattr(self, 'listWidgetCalculationsAnimal'):
            self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)

        if hasattr(self, 'listWidgetCalculationsCrop'):
            self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)

        LaUtils.debug.log("Additional signals connected", "Setup")

    def connect_diet_label_signals(self):
        """This method is deprecated - use _connect_diet_label_signals() instead"""
        # Delegate to the main connection method for compatibility with any existing calls
        dietLabels = self.diet_labels if hasattr(self, 'diet_labels') else None
        if dietLabels:
            self._connect_diet_label_signals(dietLabels)
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

            # Check that both animal and crop percentages are at 100%
            if self.labelAnimalCheck.text() != "100%" or self.labelCropCheck.text() != "100%":
                self.tbReport.setText("Check that Animals and Crops are both at 100%\n")
                self.tbReport.append("I am NOT going to do anything until they are!")
                return

            # Get the GUID of the selected crop
            crop_guid = current_item.data(Qt.UserRole)
            if hasattr(crop_guid, 'guid') and callable(crop_guid.guid):
                crop_guid = crop_guid.guid()  # Call the method to get the GUID string

            # Make sure we have a string GUID
            crop_guid = str(crop_guid)

            LaUtils.debug.log(f"Using crop GUID: {crop_guid}", "Calculation")

            # Get the GUID of the selected crop
            crop_guid = current_item.data(Qt.UserRole)
            if not crop_guid:
                LaUtils.debug.log("No GUID found for selected crop", "Error")
                return

            # Get the crop object
            crop = LaUtils.getCrop(crop_guid)
            if not crop:
                LaUtils.debug.log(f"Could not find crop with GUID: {crop_guid}", "Error")
                return

            # Set up model with current UI values
            self._configureModelFromUi()

            # Display the crop image if available
            if hasattr(self, 'lblCropPicCalcs') and hasattr(crop, 'imageFile'):
                image_path = crop.imageFile
                if image_path and os.path.exists(image_path):
                    self.lblCropPicCalcs.setPixmap(QtGui.QPixmap(image_path))
                else:
                    self.lblCropPicCalcs.clear()

            # Perform calculations based on diet settings
            diet_labels = None
            if self.cboxBaseOnPlants.isChecked():
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsPlantsFirstIncludeDairy()
                    LaUtils.debug.log("Using plants-first with dairy included calculation", "Diet")
                else:
                    diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
                    LaUtils.debug.log("Using plants-first with dairy separate calculation", "Diet")
            else:
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()  # Fixed typo
                    LaUtils.debug.log("Using animals-first with dairy included calculation", "Diet")
                else:
                    diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()
                    LaUtils.debug.log("Using animals-first with dairy separate calculation", "Diet")

            # Get the calculation report for this crop
            if hasattr(diet_labels, 'cropCalcsReportMap'):
                report_map = self._getPropertyValue(diet_labels, 'cropCalcsReportMap')
                if isinstance(report_map, dict):
                    actual_guid = str(crop_guid)
                    if actual_guid in report_map:
                        report_pair = report_map[actual_guid]
                        if isinstance(report_pair, tuple) and len(report_pair) > 0:
                            report_string = report_pair[0]
                            if hasattr(self, 'textBrowserResultsCrop'):
                                self.textBrowserResultsCrop.setText(report_string)
                                LaUtils.debug.log(f"Crop {crop.name} calculation report displayed", "Calculation")

            # Also display model HTML in the report tab for debugging
            self.tbReport.setHtml(self.model.toHtml())

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

    def logToAllChannels(self, message):
        """
        Unified logging method that sends messages to all log channels.
        This is the central logging method that all other logging methods should use.

        Args:
            message: The message to log
        """
        # Force console output for debugging
        print(f"LOG: {message}")

        # Add the message to the logs tab
        if hasattr(self, 'tbLogs'):
            self.tbLogs.append(message)
            self.tbLogs.ensureCursorVisible()
            # Force UI update immediately
            self.tbLogs.repaint()
            QtWidgets.QApplication.processEvents()

        # Add the message to the report tab
        if hasattr(self, 'tbReport'):
            self.tbReport.append(message)
            # Force UI update
            self.tbReport.repaint()
            QtWidgets.QApplication.processEvents()

        # Log to debug dialog if exists and visible
        if hasattr(self, '_debug_dialog') and self._debug_dialog is not None and self._debug_dialog.isVisible():
            self._debug_dialog.add_debug_message(message)

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
        self.tbReport.setVisible(debugMode)

        # Also set up the Logs tab based on debug mode
        if hasattr(self, 'MainTabs') and hasattr(self, 'log_tab'):
            tabIndex = self.MainTabs.indexOf(self.log_tab)
            if (tabIndex >= 0):
                self.MainTabs.setTabEnabled(tabIndex, debugMode)
            self.log_tab.setVisible(debugMode)

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
            if not hasattr(self, 'model'):
                return

            # Configure model from current UI state
            self._configureModelFromUi()

            # Disconnect previous model's signal if necessary (optional, depends on how model is managed)
            # try:
            #     self.model.logCalculationStep.disconnect(self.logToAllChannels)
            # except TypeError: # Signal not connected or already disconnected
            #     pass

            # Calculate diet labels based on settings
            # NOTE: The doCalcs methods themselves now emit the signals
            if self.cboxBaseOnPlants.isChecked():
                if self.cboxIncludeDairy.isChecked():
                    self.diet_labels = self.model.doCalcsPlantsFirstIncludeDairy()
                else:
                    self.diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
            else:
                if self.cboxIncludeDairy.isChecked():
                    self.diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()
                else:
                    self.diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()

            # Reconnect the signal from the current model instance (important if model instance changes)
            # If self.model instance *doesn't* change, this reconnect isn't strictly needed here
            # but doesn't hurt. If the doCalcs methods *returned* a new model, it would be crucial.
            # Since they seem to modify the existing self.model, the initial connection in __init__ is likely sufficient.
            # self.model.logCalculationStep.connect(self.logToAllChannels) # Reconnect (likely optional here)

            # Connect signals from the new diet labels object (if it emits signals)
            self._connect_diet_label_signals(self.diet_labels)

            # Update calculations (this might trigger more logging)
            self.updateCalculations()

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

    def _connect_diet_label_signals(self, dietLabels):
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

    def _configureModelFromUi(self):
        """Configure the model with current UI values."""
        if hasattr(self, 'model'):
            # Configure basic settings
            self.model.baseOnPlants = self.cboxBaseOnPlants.isChecked()
            self.model.includeDairy = self.cboxIncludeDairy.isChecked()
            self.model.limitDairy = self.cboxLimitDairy.isChecked()
            self.model.limitDairyPercent = self.sbLimitDairyPercent.value()
            self.model.caloriesPerPersonDaily = self.sbDailyCalories.value()

            # Configure model with selected animals and crops
            self.model.mAnimals = self.getSelectedAnimals()
            self.model.mCrops = self.getSelectedCrops()

            # Configure dairy utilisation if available
            if hasattr(self, 'sbDairyUtilisation'):
                self.model.dairyUtilisation = self.sbDairyUtilisation.value()

    def _ensure_debug_dialog_visible(self):
        """Ensure the debug dialog is created and visible."""
        if not self._debug_dialog:
            from la.gui.ladebugdialog import LaDebugDialog
            self._debug_dialog = LaDebugDialog(parent=self)
            MESSAGE_BUS.debugMessaged.connect(self._debug_dialog.add_debug_message)
        self._debug_dialog.show()

    def _getPropertyValue(self, obj, prop_name: str):
        """Helper method to safely get PyQt property values"""
        if hasattr(obj, prop_name):
            prop = getattr(obj, prop_name)
            if hasattr(prop, '__get__'):  # If it's a property
                return prop.__get__(obj)
            return prop
        return None

    def _on_debug_dialog_closed(self):
        """Handle debug dialog close event."""
        self._debug_dialog = None

    def _override_on_cbDebug_clicked(self):
        """Override for debug checkbox click handler."""
        if self.cbDebug.isChecked():
            self._ensure_debug_dialog_visible()
        elif self._debug_dialog:
            self._debug_dialog.close()
