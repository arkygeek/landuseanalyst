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
        """Constructor for LaMainForm"""
        super(LaMainForm, self).__init__(parent)

        # Initialize the model
        self.model = LaModel()

        # Initialize the controller
        self.controller = LaMainController(self.model)

        # Initialize debug logger before anything else
        debugMode = QSettings().value("landuse_analyst/debug", False, type=bool)
        LaUtils.debug.initialize(enabled=debugMode)

        # Create debug dialog if debug mode is enabled
        self._debug_dialog = None
        if (debugMode):
            from la.gui.ladebugdialog import LaDebugDialog
            self._debug_dialog = LaDebugDialog.get_instance()
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

        # Connect item changed signal for the animals table
        self.tblAnimals.itemChanged.connect(self.on_tblAnimals_itemChanged)

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
        """Update the diet information display."""
        try:
            # Get current slider values
            plantAnimalRatio = self.sliderDiet.value()
            wildTameAnimalRatio = self.sliderMeat.value()
            wildTamePlantRatio = self.sliderCrop.value()

            # Delegate calculation to controller
            diet_breakdown = self.controller.calculateDietBreakdown(
                plantAnimalRatio,
                wildTameAnimalRatio,
                wildTamePlantRatio
            )

            # Update UI with calculated values (UI code stays in form)
            self.labelMeatPercent.setText(str(diet_breakdown['animalPercent']))
            self.labelCropPercent.setText(str(diet_breakdown['plantPercent']))
            self.labelMeatWildPercent.setText(str(diet_breakdown['wildAnimalPercent']))
            self.labelMeatTamePercent.setText(str(diet_breakdown['tameAnimalPercent']))
            self.labelCropWildPercent.setText(str(diet_breakdown['wildPlantPercent']))
            self.labelCropTamePercent.setText(str(diet_breakdown['tamePlantPercent']))

            # Update additional labels if they exist
            labels_map = {
                'labelWildMeatPercentage': f"{diet_breakdown['absoluteWildAnimalPercent']:.1f}%",
                'labelTameMeatPercentage': f"{diet_breakdown['absoluteTameAnimalPercent']:.1f}%",
                'labelWildCropsPercentage': f"{diet_breakdown['absoluteWildPlantPercent']:.1f}%",
                'labelTameCropsPercentage': f"{diet_breakdown['absoluteTamePlantPercent']:.1f}%"
            }

            for label_name, value in labels_map.items():
                if hasattr(self, label_name):
                    getattr(self, label_name).setText(value)

            # Update any visualization dependent on these values
            if hasattr(self, 'updateDietPieChart'):
                self.updateDietPieChart()

            LaUtils.debug.log("Diet labels updated", "Diet")

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

    def animalCellClicked(self, row, column):
        """Handle animal table cell click event.

        This method is called when a user clicks on a cell in the animals table.
        It handles the selection and display of animal details.

        Args:
            row: The row index of the clicked cell
            column: The column index of the clicked cell
        """
        if column == 0:  # Checkbox column
            item = self.tblAnimals.item(row, column)
            guid = self.tblAnimals.item(row, 1).data(QtCore.Qt.UserRole)

            # Get the current check state
            isChecked = item.checkState() == QtCore.Qt.Checked

            # Update the animals map
            if guid in self.mAnimalsMap:
                currentValue = self.mAnimalsMap[guid]
                self.mAnimalsMap[guid] = (isChecked, currentValue[1])

                # Update the animal calculations list
                if isChecked:
                    # Add to calculations list if not already there
                    self.addAnimalToCalculationsList(guid)
                else:
                    # Remove from calculations list
                    self.removeAnimalFromCalculationsList(guid)
                self.updateTotalPercentages()

        # Always show selected animal details when any cell in the row is clicked
        self.showSelectedAnimalDetails(row)

        # Debugging
        LaUtils.debug.log(f"Animal cell clicked - row: {row}, column: {column}", "UI")

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

    def on_tblAnimals_itemChanged(self, item):
        """Handle item change in the animals table."""
        try:
            if item is None:
                return

            row = item.row()
            col = item.column()

            # Check if we have a reference to this animal
            if not hasattr(self, 'mAnimalsMap') or self.mAnimalsMap is None or row not in self.mAnimalsMap:
                LaUtils.debug.log(f"Cannot update animal parameters: no animal at row {row}", "Error")
                return

            animal = self.mAnimalsMap[row]
            if animal is None:
                return

            # Column 1 is the enable/disable checkbox
            if col == 1:
                animal.enabled = (item.checkState() == QtCore.Qt.Checked)
                LaUtils.debug.log(f"Animal '{animal.name}' {'enabled' if animal.enabled else 'disabled'}", "Animals")
                # Update calculations when animal is enabled/disabled
                self.updateCalculations()

            # Handle other columns/parameters as needed
            # ...

        except Exception as e:
            LaUtils.debug.log(f"Error updating animal parameter: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
    
    def getEnabledAnimals(self):
        """Get list of enabled animals to pass to controller."""
        enabled_animals = []
        if hasattr(self, 'mAnimalsMap'):
            for guid, animal in self.mAnimalsMap.items():
                if hasattr(animal, 'enabled') and animal.enabled:
                    enabled_animals.append(guid)
        return enabled_animals

    # Add a method to save animal parameters if not already present
    def saveAnimalParameters(self):
        """Save the current animal parameters to the model."""
        try:
            if not hasattr(self, 'model') or self.model is None:
                return

            if not hasattr(self, 'mAnimalsMap') or self.mAnimalsMap is None:
                return

            # Update model with values from UI
            for row, animal in self.mAnimalsMap.items():
                if animal is None:
                    continue

                # Get enable state from checkbox
                enableItem = self.tblAnimals.item(row, 1)
                if enableItem is not None:
                    animal.enabled = (enableItem.checkState() == QtCore.Qt.Checked)

                # Get other parameters from table if applicable
                # ...

            LaUtils.debug.log("Animal parameters saved", "Animals")

        except Exception as e:
            LaUtils.debug.log(f"Error saving animal parameters: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
