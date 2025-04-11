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
        self.mDietLabels = LaDietLabels(parent=self)

        # Basic UI setup
        self.setup()
        self.loadImages()
        self.refresh()
        self.readSettings()
        self.connect_additional_signals()

        # Connect diet label signals to UI update slots - do this once
        self._connectDietLabelSignals(self.mDietLabels)

        # Initialize diet labels with default values
        self.setDietLabels()  # This will calculate initial values based on default slider positions

        # Initialize debug dialog
        self.myDebugDialog = None
        myDebugMode = QSettings().value("landuse_analyst/debug", False, type=bool)
        LaUtils.debug.isEnabled(myDebugMode)

        if myDebugMode:
            from la.gui.ladebugdialog import LaDebugDialog
            self.myDebugDialog = LaDebugDialog(parent=self)
            if hasattr(self.myDebugDialog, 'addDebugMessage'):
                MESSAGE_BUS.debugMessaged.connect(self.myDebugDialog.addDebugMessage)
            if self.myDebugDialog is not None:
                self.myDebugDialog.show()

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

            # --- Retrieve the stored calculation report --- 
            myReportString = "No calculation results available for this animal."
            if hasattr(self.model, 'lastDietLabels') and self.model.mLastDietLabels:
                myReportMap = self.getPropertyValue(self.model.mLastDietLabels, 'animalCalcsReportMap')
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
                LaUtils.debug.log("lastDietLabels not found or empty on model", "Error")

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

            # --- Retrieve the stored calculation report --- 
            myReportString = "No calculation results available for this crop."
            if hasattr(self.model, 'lastDietLabels') and self.model.mLastDietLabels:
                myReportMap = self.getPropertyValue(self.model.mLastDietLabels, 'cropCalcsReportMap')
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
                LaUtils.debug.log("lastDietLabels not found or empty on model", "Error")

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
            message: The message to log
        """
        # Force console output for debugging ** only use in desperation as it consumes a lot of additional memory
        # print(f"LOG: {theMessage}")

        # Add the message to the logs tab
        if hasattr(self, 'tbLogs'):
            self.tbLogs.append(theMessage)
            self.tbLogs.ensureCursorVisible()
            # Force UI update immediately
            self.tbLogs.repaint()
            QtWidgets.QApplication.processEvents()

        # Add the message to the report tab
        if hasattr(self, 'tbReport'):
            self.tbReport.append(theMessage)
            # Force UI update
            self.tbReport.repaint()
            QtWidgets.QApplication.processEvents()

        # Log to debug dialog if exists and visible
        if hasattr(self, '_debug_dialog') and self.myDebugDialog is not None and self.myDebugDialog.isVisible():
            self.myDebugDialog.addDebugMessage(theMessage)

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
            # Call the parent class implementation which has the complete implementation
            super(LaMainForm, self).setDietLabels()
            
            # Store reference to the diet labels from the calculation for signal connections
            # This assumes the base class method updated the model with calculations
            if hasattr(self.model, 'lastDietLabels') and self.model.mLastDietLabels:
                self.mDietLabels = self.model.mLastDietLabels
                self._connectDietLabelSignals(self.mDietLabels)
            
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

    def ensure_debug_dialog_visible(self):
        """Ensure the debug dialog is created and visible."""
        if not self.myDebugDialog:
            from la.gui.ladebugdialog import LaDebugDialog
            self.myDebugDialog = LaDebugDialog(parent=self)
            MESSAGE_BUS.debugMessaged.connect(self.myDebugDialog.add_debug_message)
        self.myDebugDialog.show()

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
        self.myDebugDialog = None

    def override_on_cbDebug_clicked(self):
        """Override for debug checkbox click handler."""
        if self.cbDebug.isChecked():
            self.ensure_debug_dialog_visible()
        elif self.myDebugDialog:
            self.myDebugDialog.close()

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
                self.tbReport.setHtml("<h2>Error: Percentages Must Equal 100%</h2>")
                self.tbReport.append("<p>Check that Animals and Crops are both at 100%.</p>")
                self.tbReport.append("<p>I am NOT going to do anything until they are!</p>")
                return
            
            # Perform calculations based on diet settings
            diet_labels = None
            calculation_type = ""
            
            if self.cboxBaseOnPlants.isChecked():
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsPlantsFirstIncludeDairy()
                    calculation_type = "Plants First (Include Dairy)"
                else:
                    diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
                    calculation_type = "Plants First (Dairy Separate)"
            else:
                if self.cboxIncludeDairy.isChecked():
                    diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()
                    calculation_type = "Animals First (Include Dairy)"
                else:
                    diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()
                    calculation_type = "Animals First (Dairy Separate)"
            
            # Store the diet labels for future reference
            self.model.mLastDietLabels = diet_labels
            
            # Generate the report
            self.tbReport.clear()
            
            # Main HTML report
            self.tbReport.setHtml(f"<h1>LanduseAnalyst Calculation Results</h1>")
            self.tbReport.append(f"<h2>Calculation Method: {calculation_type}</h2>")
            
            # Add basic model information
            self.tbReport.append(self.model.toHtml())
            
            # Add specific reports
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlCalorieCropTargets())
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlCalorieAnimalTargets())
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlProductionCropTargets())
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlProductionAnimalTargets())
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlAreaCropTargets())
            self.tbReport.append("<hr>")
            self.tbReport.append(self.model.toHtmlAreaAnimalTargets())
            
            # Switch to the report tab
            if hasattr(self, 'tabWidgetMain'):
                reportTabIndex = self.findTabIndex('Report')
                if reportTabIndex >= 0:
                    self.tabWidgetMain.setCurrentIndex(reportTabIndex)
            
            # Update status
            if hasattr(self, 'statusBar'):
                self.statusBar().showMessage("Calculation complete", 3000)
            
            LaUtils.debug.log("Model calculations completed successfully", "Calculation")
            
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
