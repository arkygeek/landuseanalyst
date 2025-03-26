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

        # Initialize diet labels
        self.diet_labels = LaDietLabels(parent=self)

        # Connect diet label signals to UI update slots
        self._connect_diet_label_signals(self.diet_labels)

        # Basic UI setup
        self.setup()
        self.loadImages()
        self.refresh()
        self.readSettings()
        self.connect_additional_signals()

        # Connect the diet label signals to UI update slots
        self._connect_diet_label_signals(self.diet_labels)  # Ensure this is called

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

    def logToAllChannels(self, message):
        """
        Unified logging method that sends messages to all log channels.

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
        else:
            print("Warning: tbLogs widget not found!")

        # Add the message to the report tab
        if hasattr(self, 'tbReport'):
            self.tbReport.append(message)
            # Force UI update
            self.tbReport.repaint()
            QtWidgets.QApplication.processEvents()
        else:
            print("Warning: tbReport widget not found!")

    def refresh(self):
        """Refresh all displays in the form."""
        # Call base class loadAnimals()
        super().loadAnimals()
        if hasattr(self, 'loadCrops'):
            self.loadCrops()

        # Update diet info
        if hasattr(self, 'updateDietLabels'):
            self.updateDietLabels()

        # Force UI update
        QtWidgets.QApplication.processEvents()

    def setup(self):
        """Perform additional setup beyond what's in the base class."""
        # Update the application title
        self.setWindowTitle("Land Use Analyst")

        # Initialize animals map if not already done
        if not hasattr(self, 'mAnimalsMap'):
            self.mAnimalsMap = {}

        # Load images or set additional properties not handled in the base class
        self.loadImages()
        # Set up any additional connections not in the base class
        self.connect_additional_signals()
        # Initialize the diet pie chart if it exists
        if hasattr(self, 'updateDietLabels'):
            self.updateDietLabels()
        # Set default values for the population fields
        self.sbPopulation.setValue(100)
        # Refresh all displays
        self.refresh()

        # Connect item changed signal for the animals table
        self.tblAnimals.itemChanged.connect(self.on_tblAnimals_itemChanged)

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

    def setDietLabels(self):
        """Update all diet-related labels based on current values"""
        try:
            diet_percent = self.sliderDiet.value()
            meat_percent = self.sliderMeat.value()
            daily_calories = self.sbDailyCalories.value()
            include_dairy = self.cboxIncludeDairy.isChecked()
            limit_dairy = self.cboxLimitDairy.isChecked()

            # Create diet labels object and populate with current values
            diet_labels = LaDietLabels()
            diet_labels.plantsPortionPct = 100 - diet_percent
            diet_labels.animalPortionPct = diet_percent
            diet_labels.tameMeatPortionPct = meat_percent
            diet_labels.wildAnimalPortionPct = 100 - meat_percent
            diet_labels.kiloCaloriesIndividualAnnual = daily_calories * 365

            if include_dairy:
                # Call appropriate calculation method based on dairy settings
                if limit_dairy:
                    diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()
                else:
                    diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()
            else:
                # Call non-dairy calculation methods
                if diet_percent >= 50:  # Plants first
                    diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
                else:  # Animals first
                    diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()

            # Connect signals and update labels
            self._connect_diet_label_signals(diet_labels)

            LaUtils.debug.log("Diet labels updated successfully", "Diet")
        except Exception as e:
            LaUtils.debug.log(f"Error updating diet labels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def updateCalculations(self):
        """Update all calculations based on current settings and selections."""
        try:
            # Get the current population
            population = self.sbPopulation.value() if hasattr(self, 'sbPopulation') else 100

            # Update text fields with calculated values
            LaUtils.debug.log(f"Updating calculations for population: {population}", "Calculation")

            # Call setDietLabels to update percentages
            self.setDietLabels()

            # Calculate and display total land needed
            self.calculateTotalLandNeeded()

        except Exception as e:
            LaUtils.debug.log(f"Error updating calculations: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

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

    def writeSettings(self):
        """Save application settings."""
        settings = QSettings()

        # Window geometry
        settings.setValue("landuse_analyst/geometry", self.saveGeometry())

        # Debug mode
        settings.setValue("landuse_analyst/debug", self.cbDebug.isChecked())

        # Save most recently used values
        if hasattr(self, 'sbPopulation'):
            settings.setValue("landuse_analyst/population", self.sbPopulation.value())

    def closeEvent(self, event):
        """Handle window close event - save settings before closing."""
        self.writeSettings()
        super(LaMainForm, self).closeEvent(event)

    def _override_on_cbDebug_clicked(self):
        """Override base class method to prevent double-handling"""
        pass  # Let our on_cbDebug_clicked handle it

    def _on_debug_dialog_closed(self):
        """Handle dialog closure cleanup"""
        if hasattr(self, '_debug_dialog') and self._debug_dialog is not None:
            try:
                # Check if connection exists before disconnecting
                try:
                    MESSAGE_BUS.debugMessaged.disconnect(self._debug_dialog.add_debug_message)
                except (TypeError, RuntimeError):
                    # Signal was not connected or other disconnect error
                    pass
                self._debug_dialog.deleteLater()
            except:
                pass
            finally:
                self._debug_dialog = None
        self.cbDebug.setChecked(False)

    def _ensure_debug_dialog_visible(self):
        """Helper method to ensure debug dialog remains visible after initial showing."""
        if hasattr(self, '_debug_dialog') and self._debug_dialog is not None and self.cbDebug.isChecked():
            try:
                if not self._debug_dialog.isVisible():
                    self._debug_dialog.show()
                self._debug_dialog.raise_()
                self._debug_dialog.activateWindow()
            except:
                pass  # Silently ignore any errors in this helper method

    def on_debug_message(self, message: str):
        """Handle debug messages from the message bus."""
        # Add the message to all logging channels
        self.logToAllChannels(message)
        # Force immediate UI update
        QtWidgets.QApplication.processEvents()

    def logMessage(self, message: str):
        """
        Add a message to the log.
        This method is maintained for backward compatibility.

        Args:
            message: The message to add
        """
        # Delegate to our unified logging method
        self.logToAllChannels(message)

    def connect_diet_label_signals(self):
        """Connect diet label signals to UI update slots"""
        try:
            # Check if we have a model
            if not hasattr(self, 'model'):
                LaUtils.debug.log("Cannot connect diet label signals - no model available", "Error")
                return

            # First attempt to get diet labels from the most recent calculation
            dietLabels = None
            if self.model.baseOnPlants:
                if self.model.includeDairy:
                    dietLabels = self.model.doCalcsPlantsFirstIncludeDairy()
                else:
                    dietLabels = self.model.doCalcsPlantsFirstDairySeparate()
            else:
                if self.model.includeDairy:
                    dietLabels = self.model.doCalcsAnimalsFirstIncludeDairy()
                else:
                    dietLabels = self.model.doCalcsAnimalsFirstDairySeparate()

            if not dietLabels:
                LaUtils.debug.log("No diet labels object available to connect signals", "Error")
                return

            # Connect all signals from diet labels to UI update slots
            # Calorie value signals
            dietLabels.dairyMCaloriesChanged.connect(self.update_dairy_calories)
            dietLabels.cropMCaloriesChanged.connect(self.update_crop_calories)
            dietLabels.animalMCaloriesChanged.connect(self.update_animal_calories)
            dietLabels.wildAnimalMCaloriesChanged.connect(self.update_wild_animal_calories)
            dietLabels.wildPlantsMCaloriesChanged.connect(self.update_wild_plants_calories)

            # Portion percentage signals
            dietLabels.dairyPortionPctChanged.connect(self.update_dairy_portion)
            dietLabels.tameMeatPortionPctChanged.connect(self.update_tame_meat_portion)
            dietLabels.cropsPortionPctChanged.connect(self.update_crops_portion)
            dietLabels.wildAnimalPortionPctChanged.connect(self.update_wild_animal_portion)
            dietLabels.wildPlantsPortionPctChanged.connect(self.update_wild_plants_portion)
            dietLabels.plantsPortionPctChanged.connect(self.update_plants_portion)
            dietLabels.animalPortionPctChanged.connect(self.update_animal_portion)

            # Other calorie values
            dietLabels.kiloCaloriesIndividualAnnualChanged.connect(self.update_calories_individual)
            dietLabels.megaCaloriesSettlementAnnualChanged.connect(self.update_calories_settlement)
            dietLabels.dairySurplusMCaloriesChanged.connect(self.update_dairy_surplus)

            LaUtils.debug.log("Diet label signals connected successfully", "Diet")
        except Exception as e:
            LaUtils.debug.log(f"Error connecting diet label signals: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    # Signal handler slots for diet label updates
    def update_dairy_calories(self, value):
        """Update dairy calories label"""
        if hasattr(self, 'labelCaloriesDairy'):
            self.labelCaloriesDairy.setText(f"{value:.1f}")

    def update_crop_calories(self, value):
        """Update crop calories label"""
        if hasattr(self, 'labelCaloriesCrops'):
            self.labelCaloriesCrops.setText(f"{value:.1f}")

    def update_animal_calories(self, value):
        """Update animal calories label"""
        if hasattr(self, 'labelCaloriesTameMeat'):
            self.labelCaloriesTameMeat.setText(f"{value:.1f}")

    def update_wild_animal_calories(self, value):
        """Update wild animal calories label"""
        if hasattr(self, 'labelCaloriesWildMeat'):
            self.labelCaloriesWildMeat.setText(f"{value:.1f}")

    def update_wild_plants_calories(self, value):
        """Update wild plants calories label"""
        if hasattr(self, 'labelCaloriesWildPlants'):
            self.labelCaloriesWildPlants.setText(f"{value:.1f}")

    def update_dairy_portion(self, value):
        """Update dairy portion labels"""
        if hasattr(self, 'labelPortionDairy'):
            self.labelPortionDairy.setText(f"{value:.1f}%")
        if hasattr(self, 'labelPortionAllDairy'):
            self.labelPortionAllDairy.setText(f"{value:.1f}%")

    def update_tame_meat_portion(self, value):
        """Update tame meat portion label"""
        if hasattr(self, 'labelPortionTameMeat'):
            self.labelPortionTameMeat.setText(f"{value:.1f}%")

    def update_crops_portion(self, value):
        """Update crops portion label"""
        if hasattr(self, 'labelPortionCrops'):
            self.labelPortionCrops.setText(f"{value:.1f}%")

    def update_wild_animal_portion(self, value):
        """Update wild animal portion label"""
        if hasattr(self, 'labelPortionWildMeat'):
            self.labelPortionWildMeat.setText(f"{value:.1f}%")

    def update_wild_plants_portion(self, value):
        """Update wild plants portion label"""
        if hasattr(self, 'labelPortionWildPlants'):
            self.labelPortionWildPlants.setText(f"{value:.1f}%")

    def update_plants_portion(self, value):
        """Update plants portion label"""
        if hasattr(self, 'labelPortionPlants'):
            self.labelPortionPlants.setText(f"{value:.1f}%")

    def update_animal_portion(self, value):
        """Update animal portion label"""
        if hasattr(self, 'labelPortionMeat'):
            self.labelPortionMeat.setText(f"{value:.1f}%")

    def update_calories_individual(self, value):
        """Update individual calories label"""
        if hasattr(self, 'labelCaloriesIndividual'):
            self.labelCaloriesIndividual.setText(f"{value:.1f}")

    def update_calories_settlement(self, value):
        """Update settlement calories label"""
        if hasattr(self, 'labelCaloriesSettlement'):
            self.labelCaloriesSettlement.setText(f"{value:.1f}")

    def update_dairy_surplus(self, value):
        """Update dairy surplus label"""
        if hasattr(self, 'labelDairySurplus'):
            self.labelDairySurplus.setText(f"{value:.1f}")

    def _connect_diet_label_signals(self, dietLabels):
        """
        Connect signals from diet labels to appropriate slots.
        This method is called from base class to update the UI when diet values change.
        """
        try:
            # Connect signals if they exist
            if hasattr(dietLabels, 'dairyMCaloriesChanged'):
                dietLabels.dairyMCaloriesChanged.connect(self.update_dairy_calories)
            if hasattr(dietLabels, 'cropMCaloriesChanged'):
                dietLabels.cropMCaloriesChanged.connect(self.update_crop_calories)
            if hasattr(dietLabels, 'animalMCaloriesChanged'):
                dietLabels.animalMCaloriesChanged.connect(self.update_animal_calories)
            if hasattr(dietLabels, 'wildAnimalMCaloriesChanged'):
                dietLabels.wildAnimalMCaloriesChanged.connect(self.update_wild_animal_calories)
            if hasattr(dietLabels, 'wildPlantsMCaloriesChanged'):
                dietLabels.wildPlantsMCaloriesChanged.connect(self.update_wild_plants_calories)

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

    def connectSignalsSlots(self):
        """Connect signals to slots for UI interaction."""
        # Diet slider connections
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sbDailyCalories.valueChanged.connect(self.on_sbDailyCalories_valueChanged)
        self.cboxIncludeDairy.clicked.connect(self.on_cboxIncludeDairy_clicked)
        self.cboxLimitDairy.clicked.connect(self.on_cboxLimitDairy_clicked)
        self.sbLimitDairyPercent.valueChanged.connect(self.on_sbLimitDairyPercent_valueChanged)
        self.cboxBaseOnPlants.clicked.connect(self.on_cboxBaseOnPlants_clicked)
        self.sbDairyUtilisation.valueChanged.connect(self.on_sbDairyUtilisation_valueChanged)

    @pyqtSlot(int)
    def on_sliderDiet_valueChanged(self, value):
        """Handle diet slider value changes."""
        self.labelMeatPercent.setText(str(value))
        self.labelCropPercent.setText(str(100 - value))
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sliderMeat_valueChanged(self, value):
        """Handle meat ratio slider value changes."""
        self.labelMeatWildPercent.setText(str(100 - value))
        self.labelMeatTamePercent.setText(str(value))
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sbDailyCalories_valueChanged(self, value):
        """Handle daily calories spinbox value changes."""
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
    def on_sbLimitDairyPercent_valueChanged(self, value):
        """Handle dairy limit percentage spinbox value changes."""
        self.setDietLabels()

    @pyqtSlot(bool)
    def on_cboxBaseOnPlants_clicked(self, checked):
        """Handle base on plants checkbox changes."""
        self.setDietLabels()

    @pyqtSlot(int)
    def on_sbDairyUtilisation_valueChanged(self, value):
        """Handle dairy utilisation spinbox value changes."""
        self.setDietLabels()

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

    def _configureModelFromUi(self):
        """Configure the model with current UI values using proper property setters."""
        if hasattr(self, 'model'):
            # Basic model settings
            self.model.name = self.lineEditSiteName.text() if hasattr(self, 'lineEditSiteName') else "Default Site"
            self.model.population = self.sbPopulation.value() if hasattr(self, 'sbPopulation') else 100
            self.model.period = self.lineEditPeriod.text() if hasattr(self, 'lineEditPeriod') else "Default Period"

            # Coordinates and spatial settings
            if hasattr(self, 'lineEditEasting'):
                self.model.easting = int(self.lineEditEasting.text()) if self.lineEditEasting.text() else 0
            if hasattr(self, 'lineEditNorthing'):
                self.model.northing = int(self.lineEditNorthing.text()) if self.lineEditNorthing.text() else 0

            # Analysis method settings
            if hasattr(self, 'radioButtonEuclidean'):
                self.model.euclideanDistance = self.radioButtonEuclidean.isChecked()
            if hasattr(self, 'radioButtonWalkingTime'):
                self.model.walkingTime = self.radioButtonWalkingTime.isChecked()
            if hasattr(self, 'radioButtonPathDistance'):
                self.model.pathDistance = self.radioButtonPathDistance.isChecked()

            # Diet settings
            if hasattr(self, 'sliderDiet'):
                self.model.dietPercent = self.sliderDiet.value()
            if hasattr(self, 'sliderMeat'):
                self.model.meatPercent = self.sliderMeat.value()
            if hasattr(self, 'sbDailyCalories'):
                self.model.caloriesPerPersonDaily = self.sbDailyCalories.value()

            # Dairy settings
            if hasattr(self, 'cboxBaseOnPlants'):
                self.model.baseOnPlants = self.cboxBaseOnPlants.isChecked()
            if hasattr(self, 'cboxIncludeDairy'):
                self.model.includeDairy = self.cboxIncludeDairy.isChecked()
            if hasattr(self, 'cboxLimitDairy'):
                self.model.limitDairy = self.cboxLimitDairy.isChecked()
            if hasattr(self, 'sbLimitDairyPercent'):
                self.model.limitDairyPercent = self.sbLimitDairyPercent.value()
            if hasattr(self, 'sbDairyUtilisation'):
                self.model.dairyUtilisation = self.sbDairyUtilisation.value()

            # Get animals and crops
            if hasattr(self, 'getSelectedAnimals'):
                self.model.animals = self.getSelectedAnimals()
            if hasattr(self, 'getSelectedCrops'):
                self.model.crops = self.getSelectedCrops()

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

    def _getPropertyValue(self, obj, prop_name):
        """Helper method to safely get PyQt property values"""
        if hasattr(obj, prop_name):
            prop = getattr(obj, prop_name)
            if hasattr(prop, '__get__'):  # If it's a property
                return prop.__get__(obj)
            return prop
        return None

    def updateDietLabels(self, dairy_portion_pct: float = 0.0, tame_meat_portion_pct: float = 0.0, crops_portion_pct: float = 0.0):
        """Update diet-related labels with new values"""
        try:
            if hasattr(self, 'labelPortionDairy'):
                self.labelPortionDairy.setText(f"{dairy_portion_pct:.1f}%")
            if hasattr(self, 'labelPortionTameMeat'):
                self.labelPortionTameMeat.setText(f"{tame_meat_portion_pct:.1f}%")
            if hasattr(self, 'labelPortionCrops'):
                self.labelPortionCrops.setText(f"{crops_portion_pct:.1f}%")

            # Calculate and update wild portions
            wild_meat_portion = 100.0 - tame_meat_portion_pct if tame_meat_portion_pct <= 100 else 0.0
            if hasattr(self, 'labelPortionWildMeat'):
                self.labelPortionWildMeat.setText(f"{wild_meat_portion:.1f}%")

            # Update totals
            total_animal = dairy_portion_pct + tame_meat_portion_pct + wild_meat_portion
            total_plant = crops_portion_pct + (100.0 - crops_portion_pct)  # Including wild plants

            if hasattr(self, 'labelTotalAnimal'):
                self.labelTotalAnimal.setText(f"{total_animal:.1f}%")
            if hasattr(self, 'labelTotalPlant'):
                self.labelTotalPlant.setText(f"{total_plant:.1f}%")

        except Exception as e:
            LaUtils.debug.log(f"Error updating diet labels: {str(e)}", "Error")
