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
from qgis.PyQt.QtWidgets import QApplication, QMessageBox
import os
from typing import Dict, List, Optional, Union
from la.lib.laanimal import LaAnimal

from la.ui.lamainformbase import LaMainFormBase
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils, MESSAGE_BUS
from la.lib.lamaincontroller import LaMainController

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
        
        # Basic UI setup
        self.setup()
        self.loadImages()
        self.refresh()
        self.readSettings()
        self.connect_additional_signals()
        
        # Connect the diet label signals to UI update slots
        self.connect_diet_label_signals()
        
        # Initialize diet labels with default values
        self.setDietLabels()  # This will calculate initial values based on default slider positions
        
        # Initialize debug logger before anything else
        debugMode = QSettings().value("landuse_analyst/debug", False, type=bool)
        LaUtils.debug.initialize(enabled=debugMode)
        
        # Create debug dialog if debug mode is enabled
        self._debug_dialog = None
        if (debugMode):
            from la.gui.ladebugdialog import LaDebugDialog
            self._debug_dialog = LaDebugDialog.get_instance(parent=self)
            
        # Connect debug message bus after dialog creation
        MESSAGE_BUS.debugMessaged.connect(self._debug_dialog.add_debug_message)
        
        # Load existing messages
        if hasattr(LaUtils.debug, 'get_history'):
            self._debug_dialog.add_messages_from_history(LaUtils.debug.get_history())
        
        # Show dialog
        self._debug_dialog.show()
        
        # Additional initialization specific to the main form
        self.setup()
        
        # Initialize settings and debug state
        self.readSettings()
        
        # Connect debug message bus to main form
        MESSAGE_BUS.debugMessaged.connect(self.on_debug_message)
        
        # Test log message to verify the system is working
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
        if hasattr(self, 'updateDietPieChart'):
            self.updateDietPieChart()

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
        if hasattr(self, 'updateDietPieChart'):
            self.updateDietPieChart()
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

    def setDietLabels(self):
        """Calculate and update diet labels with current values."""
        # Get the current population value from the spin box
        population = self.sbPopulation.value()

        # Update the model with the new population value
        self.model.population(population)

        # Calculate the land area required for food production based on the model's calculations
        land_area_required = self.model.calculate_land_area_required()

        # Update the diet labels with the calculated values
        self.dietLabels.update_labels(land_area_required)
        """Update the diet information display including visual indicators."""
        try:
            # Calculate basic percentages from slider values
            myAnimalPercent = self.sliderDiet.value()
            myPlantPercent = 100 - myAnimalPercent
            
            myWildAnimalPercent = self.sliderMeat.value()
            myTameAnimalPercent = 100 - myWildAnimalPercent
            
            myWildPlantPercent = self.sliderCrop.value()
            myTamePlantPercent = 100 - myWildPlantPercent
    
            # Calculate absolute percentages
            myAbsoluteWildAnimalPercent = (myAnimalPercent * myWildAnimalPercent) / 100.0
            myAbsoluteTameAnimalPercent = (myAnimalPercent * myTameAnimalPercent) / 100.0
            myAbsoluteWildPlantPercent = (myPlantPercent * myWildPlantPercent) / 100.0
            myAbsoluteTamePlantPercent = (myPlantPercent * myTamePlantPercent) / 100.0
    
            # Update basic percentage labels
            self.labelMeatPercent.setText(f"{myAnimalPercent}%")
            self.labelCropPercent.setText(f"{myPlantPercent}%")
            self.labelMeatWildPercent.setText(f"{myWildAnimalPercent}%")
            self.labelMeatTamePercent.setText(f"{myTameAnimalPercent}%")
            self.labelCropWildPercent.setText(f"{myWildPlantPercent}%")
            self.labelCropTamePercent.setText(f"{myTamePlantPercent}%")
    
            self.labelAnimalCheck.setText("100%" if myAnimalPercent + myPlantPercent == 100 else f"{myAnimalPercent + myPlantPercent}%")
            self.labelCropCheck.setText("100%" if myWildPlantPercent + myTamePlantPercent == 100 else f"{myWildPlantPercent + myTamePlantPercent}%")
    
            # Update the model's diet percentages
            if hasattr(self, 'model'):
                # Store these changes to model
                LaUtils.debug.log(f"Setting model diet percentages - Animal: {myAnimalPercent}%, Wild animal: {myWildAnimalPercent}%, Wild plant: {myWildPlantPercent}%", "Diet")
                self.model.dietPercent = myAnimalPercent
                self.model.meatPercent = myWildAnimalPercent
                self.model.percentOfDietThatIsFromCrops = myWildPlantPercent
    
                # Store reference to any previously calculated diet labels
                self._previous_diet_labels = getattr(self, '_current_diet_labels', None)
    
                # Force recalculation of diet values based on slider positions
                LaUtils.debug.log("Recalculating diet values...", "Diet")
                if self.model.baseOnPlants:
                    if self.model.includeDairy:
                        self._current_diet_labels = self.model.doCalcsPlantsFirstIncludeDairy()
                        LaUtils.debug.log("Used doCalcsPlantsFirstIncludeDairy calculation method", "Diet")
                    else:
                        self._current_diet_labels = self.model.doCalcsPlantsFirstDairySeparate()
                        LaUtils.debug.log("Used doCalcsPlantsFirstDairySeperate calculation method", "Diet")
                else:
                    if self.model.includeDairy:
                        self._current_diet_labels = self.model.doCalcsAnimalsFirstIncludeDairy()
                        LaUtils.debug.log("Used doCalcsAnimalsFirstIncludeDiary calculation method", "Diet")
                    else:
                        self._current_diet_labels = self.model.doCalcsAnimalsFirstDairySeparate()
                        LaUtils.debug.log("Used doCalcsAnimalsFirstDairySeparate calculation method", "Diet")
                
                # Store reference to the new diet labels and connect its signals
                dietLabels = self._current_diet_labels
                
                if dietLabels is None:
                    LaUtils.debug.log("Error: Diet labels calculation returned None", "Error")
                    return
                
                LaUtils.debug.log(f"New diet labels object created with ID: {id(dietLabels)}", "Diet")
                LaUtils.debug.log(f"Diet values - Dairy: {dietLabels.dairyMCalories:.2f}, Crops: {dietLabels.cropMCalories:.2f}", "Diet")
                LaUtils.debug.log(f"Diet percentages - Animal: {dietLabels.animalPortionPct:.2f}%, Plants: {dietLabels.plantsPortionPct:.2f}%", "Diet")
                
                # Connect signals from the newly calculated diet labels object
                self._connect_diet_label_signals(dietLabels)
                
                # Directly update all UI elements with the new values for immediate feedback
                # Update portion labels
                if hasattr(self, 'labelPortionMeat'):
                    self.labelPortionMeat.setText(f"{dietLabels.animalPortionPct:.1f}%")
                if hasattr(self, 'labelPortionCrops'):
                    self.labelPortionCrops.setText(f"{dietLabels.plantsPortionPct:.1f}%")
                if hasattr(self, 'labelPortionAllDairy'):
                    self.labelPortionAllDairy.setText(f"{dietLabels.dairyPortionPct:.1f}%")
                if hasattr(self, 'labelPortionDairy'):
                    self.labelPortionDairy.setText(f"{dietLabels.dairyPortionPct:.1f}%")
                if hasattr(self, 'labelPortionTameMeat'):
                    self.labelPortionTameMeat.setText(f"{dietLabels.tameMeatPortionPct:.1f}%")
                if hasattr(self, 'labelPortionWildMeat'):
                    self.labelPortionWildMeat.setText(f"{dietLabels.wildAnimalPortionPct:.1f}%")
                if hasattr(self, 'labelPortionWildPlants'):
                    self.labelPortionWildPlants.setText(f"{dietLabels.wildPlantsPortionPct:.1f}%")
                
                # Update calorie labels
                if hasattr(self, 'labelCaloriesCrops'):
                    self.labelCaloriesCrops.setText(f"{dietLabels.cropMCalories:.1f}")
                if hasattr(self, 'labelCaloriesTameMeat'):
                    self.labelCaloriesTameMeat.setText(f"{dietLabels.animalMCalories:.1f}")
                if hasattr(self, 'labelCaloriesDairy'):
                    self.labelCaloriesDairy.setText(f"{dietLabels.dairyMCalories:.1f}")
                if hasattr(self, 'labelCaloriesWildMeat'):
                    self.labelCaloriesWildMeat.setText(f"{dietLabels.wildAnimalMCalories:.1f}")
                if hasattr(self, 'labelCaloriesWildPlants'):
                    self.labelCaloriesWildPlants.setText(f"{dietLabels.wildPlantsMCalories:.1f}")
                
                # Update settlement and individual calorie labels
                if hasattr(self, 'labelCaloriesIndividual'):
                    self.labelCaloriesIndividual.setText(f"{dietLabels.kiloCaloriesIndividualAnnual:.1f}")
                if hasattr(self, 'labelCaloriesSettlement'):
                    self.labelCaloriesSettlement.setText(f"{dietLabels.megaCaloriesSettlementAnnual:.1f}")
                
                # Update dairy surplus if available
                if hasattr(self, 'labelDairySurplus'):
                    self.labelDairySurplus.setText(f"{dietLabels.dairySurplusMCalories:.1f}")
                
                # Log successful update
                LaUtils.debug.log("Diet labels UI updated directly from calculation results", "Diet")
    
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
        """Connect signals from a specific diet labels object to UI update slots.
        
        Args:
            dietLabels: The LaDietLabels object whose signals should be connected
        """
        try:
            if not dietLabels:
                LaUtils.debug.log("No diet labels object provided to connect signals", "Error")
                return

            # Add debug logging to trace the object we're connecting to
            LaUtils.debug.log(f"Connecting diet label signals from object: {dietLabels}", "Diet")
            LaUtils.debug.log(f"Diet labels object ID: {id(dietLabels)}", "Diet")
            LaUtils.debug.log(f"Diet values - Dairy: {dietLabels.dairyMCalories}, Crops: {dietLabels.cropMCalories}", "Diet")

            # Disconnect signals from previous diet labels object if it exists
            if hasattr(self, '_previous_diet_labels') and self._previous_diet_labels:
                try:
                    # Debug which object we're disconnecting from
                    LaUtils.debug.log(f"Disconnecting from previous object ID: {id(self._previous_diet_labels)}", "Diet")
                    
                    self._previous_diet_labels.dairyMCaloriesChanged.disconnect(self.update_dairy_calories)
                    self._previous_diet_labels.cropMCaloriesChanged.disconnect(self.update_crop_calories)
                    self._previous_diet_labels.animalMCaloriesChanged.disconnect(self.update_animal_calories)
                    self._previous_diet_labels.wildAnimalMCaloriesChanged.disconnect(self.update_wild_animal_calories)
                    self._previous_diet_labels.wildPlantsMCaloriesChanged.disconnect(self.update_wild_plants_calories)
                    
                    self._previous_diet_labels.dairyPortionPctChanged.disconnect(self.update_dairy_portion)
                    self._previous_diet_labels.tameMeatPortionPctChanged.disconnect(self.update_tame_meat_portion)
                    self._previous_diet_labels.cropsPortionPctChanged.disconnect(self.update_crops_portion)
                    self._previous_diet_labels.wildAnimalPortionPctChanged.disconnect(self.update_wild_animal_portion)
                    self._previous_diet_labels.wildPlantsPortionPctChanged.disconnect(self.update_wild_plants_portion)
                    self._previous_diet_labels.plantsPortionPctChanged.disconnect(self.update_plants_portion)
                    self._previous_diet_labels.animalPortionPctChanged.disconnect(self.update_animal_portion)
                    
                    self._previous_diet_labels.kiloCaloriesIndividualAnnualChanged.disconnect(self.update_calories_individual)
                    self._previous_diet_labels.megaCaloriesSettlementAnnualChanged.disconnect(self.update_calories_settlement)
                    self._previous_diet_labels.dairySurplusMCaloriesChanged.disconnect(self.update_dairy_surplus)
                    
                    LaUtils.debug.log("Successfully disconnected previous signals", "Diet")
                except Exception as e:
                    # Log specific disconnect errors but continue execution
                    LaUtils.debug.log(f"Error disconnecting signals: {str(e)}", "Diet")
                    pass

            # Connect calorie value signals from the new diet labels object
            LaUtils.debug.log("Connecting signals for calorie values", "Diet")
            dietLabels.dairyMCaloriesChanged.connect(self.update_dairy_calories)
            dietLabels.cropMCaloriesChanged.connect(self.update_crop_calories)
            dietLabels.animalMCaloriesChanged.connect(self.update_animal_calories)
            dietLabels.wildAnimalMCaloriesChanged.connect(self.update_wild_animal_calories)
            dietLabels.wildPlantsMCaloriesChanged.connect(self.update_wild_plants_calories)
            
            # Connect portion percentage signals
            LaUtils.debug.log("Connecting signals for portion percentages", "Diet")
            dietLabels.dairyPortionPctChanged.connect(self.update_dairy_portion)
            dietLabels.tameMeatPortionPctChanged.connect(self.update_tame_meat_portion)
            dietLabels.cropsPortionPctChanged.connect(self.update_crops_portion)
            dietLabels.wildAnimalPortionPctChanged.connect(self.update_wild_animal_portion)
            dietLabels.wildPlantsPortionPctChanged.connect(self.update_wild_plants_portion)
            dietLabels.plantsPortionPctChanged.connect(self.update_plants_portion)
            dietLabels.animalPortionPctChanged.connect(self.update_animal_portion)
            
            # Connect other calorie values
            LaUtils.debug.log("Connecting signals for settlement calories", "Diet")
            dietLabels.kiloCaloriesIndividualAnnualChanged.connect(self.update_calories_individual)
            dietLabels.megaCaloriesSettlementAnnualChanged.connect(self.update_calories_settlement)
            dietLabels.dairySurplusMCaloriesChanged.connect(self.update_dairy_surplus)
            
            # Force a manual update of all UI labels to ensure they match the diet labels object
            LaUtils.debug.log("Manually updating UI labels from diet labels object", "Diet")
            self.update_dairy_calories(dietLabels.dairyMCalories)
            self.update_crop_calories(dietLabels.cropMCalories)
            self.update_animal_calories(dietLabels.animalMCalories)
            self.update_wild_animal_calories(dietLabels.wildAnimalMCalories)
            self.update_wild_plants_calories(dietLabels.wildPlantsMCalories)
            
            self.update_dairy_portion(dietLabels.dairyPortionPct)
            self.update_tame_meat_portion(dietLabels.tameMeatPortionPct)
            self.update_crops_portion(dietLabels.cropsPortionPct)
            self.update_wild_animal_portion(dietLabels.wildAnimalPortionPct)
            self.update_wild_plants_portion(dietLabels.wildPlantsPortionPct)
            self.update_plants_portion(dietLabels.plantsPortionPct)
            self.update_animal_portion(dietLabels.animalPortionPct)
            
            self.update_calories_individual(dietLabels.kiloCaloriesIndividualAnnual)
            self.update_calories_settlement(dietLabels.megaCaloriesSettlementAnnual)
            self.update_dairy_surplus(dietLabels.dairySurplusMCalories)
            
            LaUtils.debug.log("Diet label signals connected and UI updated for specific instance", "Diet")
        except Exception as e:
            LaUtils.debug.log(f"Error connecting specific diet label signals: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
