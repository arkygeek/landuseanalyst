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
from qgis.PyQt.QtCore import QSettings
import os

from la.ui.lamainformbase import LaMainFormBase
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils, MESSAGE_BUS

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

        # Additional initialization specific to the main form
        self.setup()

        # Initialize settings and debug state first
        self.readSettings()

        # Connect item changed signal for the animals table
        self.tblAnimals.itemChanged.connect(self.on_tblAnimals_itemChanged)

        # Verify tbLogs exists
        if not hasattr(self, 'tbLogs'):
            import traceback
            print(f"ERROR: tbLogs widget not found in UI form!")
            for widget in self.findChildren(QtWidgets.QTextBrowser):
                print(f"Available QTextBrowser: {widget.objectName()}")
        else:
            # Ensure tbLogs is properly initialized
            self.tbLogs.clear()
            self.tbLogs.append("Debug log initialized")
            # Force UI update immediately
            self.tbLogs.repaint()
            QtWidgets.QApplication.processEvents()

        # Initialize debug logger before connecting message bus
        debugMode = self.cbDebug.isChecked()
        LaUtils.debug.initialize(
            enabled=debugMode,
            callback=self.logToAllChannels
        )

        # Now connect debug message bus after logger is initialized
        MESSAGE_BUS.debugMessaged.connect(self.on_debug_message)

        # Configure UI debug state
        if hasattr(self, 'tbLogs'):
            self.tbLogs.setVisible(debugMode)
        if hasattr(self, 'tbReport'):
            self.tbReport.setVisible(debugMode)

        # Test log message to verify the system is working
        LaUtils.debug.log("Application initialized", "MainForm")

        # Force a message to appear even if debug is off (for testing)
        self.logToAllChannels("Debug system test message - should always appear")
        # Force UI update again
        QtWidgets.QApplication.processEvents()

        # Add signal connection for table cell clicks
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)

        # Connect table selection change signal
        self.tblAnimals.itemSelectionChanged.connect(self.on_animal_selection_changed)

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
        # Load animals and crops
        self.loadAnimals()
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

        # Connect animal and crop table cell clicks
        if hasattr(self, 'tblAnimals'):
            self.tblAnimals.cellClicked.connect(self.animalCellClicked)
            # Connect parameter combo box changes
            self.tblAnimals.cellWidget = self.create_parameter_combo

        if hasattr(self, 'tblCrops'):
            self.tblCrops.cellClicked.connect(self.cropCellClicked)

        # Override the base class's on_cbDebug_clicked to use our version
        if hasattr(LaMainFormBase, 'on_cbDebug_clicked'):
            self.on_cbDebug_clicked = self._override_on_cbDebug_clicked

    def create_parameter_combo(self, row: int, col: int) -> QtWidgets.QComboBox:
        """Create a parameter combo box with change handler connected."""
        if col == 2:  # Parameters column
            combo = QtWidgets.QComboBox()
            combo.currentIndexChanged.connect(lambda idx, r=row: self.on_parameter_changed(r, idx))
            return combo
        return QtWidgets.QComboBox()  # Return empty combo box instead of None

    def on_parameter_changed(self, row: int, index: int):
        """Handle parameter combo box selection changes.

        Args:
            row: Table row number
            index: Selected index in combo box
        """
        try:
            # Get the combo box that changed
            combo = self.tblAnimals.cellWidget(row, 2)
            if not combo:
                return

            # Get the animal GUID from the name column
            nameItem = self.tblAnimals.item(row, 1)
            if not nameItem:
                return

            guid = nameItem.data(QtCore.Qt.UserRole)
            if not guid or guid not in self.mAnimalsMap:
                return

            # Get the newly selected parameter GUID
            parameter_guid = combo.itemData(index)
            if not parameter_guid:
                return

            # Update the parameter in mAnimalsMap while preserving enabled state
            oldValue = self.mAnimalsMap[guid]
            self.mAnimalsMap[guid] = (oldValue[0], parameter_guid)

            # Update the animal details display if this row is selected
            if self.tblAnimals.currentRow() == row:
                self.animalCellClicked(row, 1)

            # Refresh the table to update percentages
            self.loadAnimals()

        except Exception as e:
            LaUtils.debug.log(f"Error handling parameter change: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())

    def updateDietPieChart(self):
        """Update the diet information display.

        This method calculates the diet percentages based on slider values
        and updates relevant labels in the UI.
        """
        try:
            # Get current slider values
            plantAnimalRatio = self.sliderDiet.value()  # Plant % vs Animal %
            wildTameAnimalRatio = self.sliderMeat.value()  # Wild % vs Tame % for animal portion
            wildTamePlantRatio = self.sliderCrop.value()  # Wild % vs Tame % for plant portion

            # Calculate percentages
            animalPercent = plantAnimalRatio
            plantPercent = 100 - plantAnimalRatio

            wildAnimalPercent = (animalPercent * wildTameAnimalRatio) / 100
            tameAnimalPercent = (animalPercent * (100 - wildTameAnimalRatio)) / 100
            wildPlantPercent = (plantPercent * wildTamePlantRatio) / 100
            tamePlantPercent = (plantPercent * (100 - wildTamePlantRatio)) / 100

            # Update the labels with calculated values
            # This matches the C++ version behavior without adding a pie chart
            if hasattr(self, 'labelWildMeatPercentage'):
                self.labelWildMeatPercentage.setText(f"{wildAnimalPercent:.1f}%")
            if hasattr(self, 'labelTameMeatPercentage'):
                self.labelTameMeatPercentage.setText(f"{tameAnimalPercent:.1f}%")
            if hasattr(self, 'labelWildCropsPercentage'):
                self.labelWildCropsPercentage.setText(f"{wildPlantPercent:.1f}%")
            if hasattr(self, 'labelTameCropsPercentage'):
                self.labelTameCropsPercentage.setText(f"{tamePlantPercent:.1f}%")

            LaUtils.debug.log("Diet percentages updated", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error updating diet percentages: {str(e)}", "Error")
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
            # This would calculate the total land needed based on:
            # - Population
            # - Selected crops and animals
            # - Diet ratios
            # - Crop yields and animal parameters

            # Dummy calculation for demonstration
            population = self.sbPopulation.value() if hasattr(self, 'sbPopulation') else 100
            landNeeded = population * 0.5  # Simple example - would be much more complex in reality

            # Display the result
            if hasattr(self, 'lblTotalLandNeeded'):
                self.lblTotalLandNeeded.setText(f"{landNeeded:.2f}")

            LaUtils.debug.log(f"Total land needed calculated: {landNeeded:.2f} units", "Calculation")

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
            if tabIndex >= 0:
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

    def on_cbDebug_clicked(self):
        """Handle debug checkbox clicked - toggle debug mode."""
        isChecked = self.cbDebug.isChecked()

        # Update the debug logger first
        LaUtils.debug.set_enabled(isChecked)

        # Show/hide debug UI components and verify they exist
        if hasattr(self, 'tbLogs'):
            self.tbLogs.setVisible(isChecked)
            print(f"tbLogs visibility set to {isChecked}")
            if isChecked:
                # Add a test message when enabling debug mode
                self.tbLogs.append("Debug logging enabled - test message")
        else:
            print("ERROR: tbLogs widget not found!")

        if hasattr(self, 'tbReport'):
            self.tbReport.setVisible(isChecked)
        else:
            print("ERROR: tbReport widget not found!")

        # Show/hide the Logs tab
        if hasattr(self, 'MainTabs') and hasattr(self, 'log_tab'):
            tabIndex = self.MainTabs.indexOf(self.log_tab)
            if tabIndex >= 0:
                self.MainTabs.setTabEnabled(tabIndex, isChecked)
                self.log_tab.setVisible(isChecked)
        else:
            print("Note: MainTabs or log_tab not found")

        # Save setting
        QSettings().setValue("landuse_analyst/debug", isChecked)

        # Log the debug mode change last
        message = "Debug mode enabled" if isChecked else "Debug mode disabled"
        LaUtils.debug.log(message, "Debug")

        # Force a message to appear in tbLogs even if debug logger doesn't work
        if hasattr(self, 'tbLogs') and isChecked:
            self.tbLogs.append(f"Debug checkbox was clicked: {isChecked}")

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

    def animalCellClicked(self, row: int, column: int) -> None:
        """Handle clicks on the animals table.

        Updates the text browser with details about the selected animal
        and its parameters.

        Args:
            row: The clicked row index
            column: The clicked column index
        """
        # Clear the calculations list first
        self.listWidgetCalculationsAnimal.clear()

        try:
            # Get the animal GUID from the name column (column 1)
            item = self.tblAnimals.item(row, 1)
            if not item:
                LaUtils.debug.log("No item found in column 1")
                return

            animal_guid = item.data(QtCore.Qt.UserRole)
            if not animal_guid:
                LaUtils.debug.log("No animal GUID found in item data")
                return

            LaUtils.debug.log(f"Animal clicked - GUID: {animal_guid}")
                
            # Get the animal data
            animals_map = LaUtils.getAvailableAnimals()
            if animal_guid not in animals_map:
                LaUtils.debug.log(f"Animal with GUID {animal_guid} not found in available animals")
                return
            
            animal = animals_map[animal_guid]
            LaUtils.debug.log(f"Found animal: {animal.name}")
            
            # Get the animal parameter GUID from the combo box
            combo = self.tblAnimals.cellWidget(row, 2)
            if not combo:
                LaUtils.debug.log("No combo box found in column 2")
                return
            
            param_guid = combo.itemData(combo.currentIndex(), QtCore.Qt.UserRole)
            if not param_guid:
                LaUtils.debug.log("No parameter GUID found in combo box")
                return
            
            LaUtils.debug.log(f"Parameter GUID: {param_guid}")
            
            # Get the animal parameter data
            param_map = LaUtils.getAvailableAnimalParameters()
            if param_guid not in param_map:
                LaUtils.debug.log(f"Animal parameter with GUID {param_guid} not found")
                return
                
            parameter = param_map[param_guid]
            LaUtils.debug.log(f"Found parameter: {parameter.name}")
            
            # Display the animal and parameter details
            self.showAnimalDefinitionReport(animal, parameter)
            
            # Update the animal image
            if hasattr(animal, 'imageFile') and animal.imageFile:
                try:
                    # This follows the approach from the C++ version
                    image_path = LaUtils.resolvePath(str(animal.imageFile), 'image')
                    LaUtils.debug.log(f"Trying to load image from: {image_path}")
                    
                    if os.path.exists(image_path):
                        pixmap = QPixmap(image_path)
                        if not pixmap.isNull():
                            self.lblAnimalPix.setPixmap(pixmap)
                            self.lblAnimalPix.setScaledContents(True)
                            LaUtils.debug.log(f"Successfully loaded image: {image_path}")
                        else:
                            LaUtils.debug.log(f"Failed to create pixmap from {image_path}")
                            self.lblAnimalPix.clear()
                    else:
                        # Try the direct path as fallback
                        fallback_path = str(animal.imageFile)
                        LaUtils.debug.log(f"Trying fallback image path: {fallback_path}")
                        
                        if os.path.exists(fallback_path):
                            pixmap = QPixmap(fallback_path)
                            if not pixmap.isNull():
                                self.lblAnimalPix.setPixmap(pixmap)
                                self.lblAnimalPix.setScaledContents(True)
                                LaUtils.debug.log(f"Successfully loaded image from fallback path")
                            else:
                                LaUtils.debug.log(f"Failed to create pixmap from fallback path")
                                self.lblAnimalPix.clear()
                        else:
                            LaUtils.debug.log("Image not found at any path")
                            self.lblAnimalPix.clear()
                except Exception as e:
                    LaUtils.debug.log(f"Error loading animal image: {str(e)}")
                    import traceback
                    LaUtils.debug.log(traceback.format_exc())
                    self.lblAnimalPix.clear()
            else:
                LaUtils.debug.log("No image file specified for animal")
                self.lblAnimalPix.clear()

        except Exception as e:
            LaUtils.debug.log(f"Error in animalCellClicked: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())

    def showAnimalDefinitionReport(self, animal, animal_parameter):
        """Display the animal and parameter details in the text browser.
        
        Args:
            animal: The LaAnimal instance to display
            animal_parameter: The LaAnimalParameter instance to display
        """
        try:
            # Generate HTML representations of the animal and parameter
            animal_html = animal.toHtml()
            param_html = animal_parameter.toHtml()
            
            LaUtils.debug.log(f"Animal HTML generated, length: {len(animal_html)}")
            LaUtils.debug.log(f"Parameter HTML generated, length: {len(param_html)}")
            
            # Format the HTML in a table with two columns - just like cropDefinitionReport
            html = "<body>"
            html += "<table width=\"100%\">"
            html += "<tr>"
            html += "<td style=\"vertical-align:top; width:50%\">"
            html += animal_html
            html += "</td>"
            html += "<td style=\"vertical-align:top; width:50%\">"
            html += param_html
            html += "</td>"
            html += "</tr>"
            html += "</table>"
            html += "</body>"
            
            # Get the standard CSS
            css = LaUtils.getStandardCss()
            
            # Apply standard CSS and set the HTML content
            if hasattr(self, 'textBrowserAnimalDefinition'):
                self.textBrowserAnimalDefinition.document().setDefaultStyleSheet(css)
                self.textBrowserAnimalDefinition.setHtml(html)
                
                # Force update
                self.textBrowserAnimalDefinition.update()
                QtWidgets.QApplication.processEvents()
                
                LaUtils.debug.log("HTML content set to textBrowserAnimalDefinition")
            else:
                LaUtils.debug.log("ERROR: textBrowserAnimalDefinition widget not found")
                # Debug available QTextBrowser widgets
                for widget in self.findChildren(QtWidgets.QTextBrowser):
                    LaUtils.debug.log(f"Found QTextBrowser: {widget.objectName()}")
        
        except Exception as e:
            LaUtils.debug.log(f"Error in showAnimalDefinitionReport: {str(e)}")
            import traceback
            LaUtils.debug.log(traceback.format_exc())

    def loadAnimals(self):
        """Load and display animals in the main form table."""
        # Clear existing items
        self.listWidgetCalculationsAnimal.clear()

        # Clear and setup the animals table
        self.tblAnimals.clear()
        self.tblAnimals.setRowCount(0)
        self.tblAnimals.setColumnCount(4)

        # Initialize tracking variables
        myCurrentRow = 0
        myRunningPercentage = 0.0

        # Get available animals and parameters
        myAnimalsMap = LaUtils.getAvailableAnimals()
        myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()

        # Set up table headers
        headers = ["Used?", "Name", "Parameters", "Diet %"]
        self.tblAnimals.setHorizontalHeaderLabels(headers)

        # Iterate through available animals
        for myGuid, myAnimal in myAnimalsMap.items():
            myName = str(myAnimal.name)  # Convert property to string
            # Get or create animal data in mAnimalsMap
            myValue = self.mAnimalsMap.get(myGuid, (False, ""))
            if myGuid not in self.mAnimalsMap:
                self.mAnimalsMap[myGuid] = myValue

            # Add new row
            self.tblAnimals.insertRow(myCurrentRow)

            # Create Used? checkbox item
            mypUsedItem = QtWidgets.QTableWidgetItem()
            mypUsedItem.setText("Used?")
            mypUsedItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            mypUsedItem.setCheckState(QtCore.Qt.Checked if myValue[0] else QtCore.Qt.Unchecked)
            self.tblAnimals.setItem(myCurrentRow, 0, mypUsedItem)

            # Add name item with icon
            mypNameItem = QtWidgets.QTableWidgetItem()
            mypNameItem.setText(myName)
            mypNameItem.setData(QtCore.Qt.UserRole, myGuid)
            myIcon = QtGui.QIcon(":/localdata.png")
            mypNameItem.setIcon(myIcon)
            self.tblAnimals.setItem(myCurrentRow, 1, mypNameItem)

            # Create and populate parameters combo box
            mypCombo = QtWidgets.QComboBox()
            for paramGuid, param in myAnimalParametersMap.items():
                if myGuid == param.animalGuid:
                    myParameterName = f"{str(param.name)} ({str(param.description)})"
                    mypCombo.addItem(myIcon, myParameterName, paramGuid)

                    # If this is the selected parameter, add its percentage to running total
                    if myValue[0] and myValue[1] == paramGuid:
                        myRunningPercentage += float(str(param.percentTameMeat))

                        # Add percentage to table
                        mypPercentItem = QtWidgets.QTableWidgetItem()
                        mypPercentItem.setText(str(param.percentTameMeat))
                        self.tblAnimals.setItem(myCurrentRow, 3, mypPercentItem)

            # Set the default parameter in combo if one exists
            if myValue[1]:
                index = mypCombo.findData(myValue[1])
                if index >= 0:
                    mypCombo.setCurrentIndex(index)

            # Add combo to table
            self.tblAnimals.setCellWidget(myCurrentRow, 2, mypCombo)

            # Add to calculations list if enabled
            if myValue[0]:
                myItem = QtWidgets.QListWidgetItem()
                myItem.setText(myName)
                myItem.setData(QtCore.Qt.UserRole, myGuid)
                self.listWidgetCalculationsAnimal.addItem(myItem)

            myCurrentRow += 1

        # Show total percentage indicator
        myIcon = QtGui.QIcon(":/status_ok.png" if myRunningPercentage == 100 else ":/status_error.png")
        self.labelAnimalCheck.setText(f"{myRunningPercentage}%")

        # Resize columns to content
        self.tblAnimals.resizeColumnsToContents()
        self.tblAnimals.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def on_tblAnimals_itemChanged(self, item):
        """Handle changes to items in the animals table, particularly Used? checkbox."""
        if item.column() == 0:  # Used? column
            try:
                # Get the GUID from the name column
                nameItem = self.tblAnimals.item(item.row(), 1)
                if not nameItem:
                    return

                guid = nameItem.data(QtCore.Qt.UserRole)
                if not guid:
                    return

                # Update the enabled state in mAnimalsMap
                if guid in self.mAnimalsMap:
                    oldValue = self.mAnimalsMap[guid]
                    # Update tuple with new checked state but keep same parameter GUID
                    self.mAnimalsMap[guid] = (item.checkState() == QtCore.Qt.Checked, oldValue[1])

                # Refresh the table to update percentages
                self.loadAnimals()

            except Exception as e:
                LaUtils.debug.log(f"Error handling checkbox change: {str(e)}")
                import traceback
                LaUtils.debug.log(traceback.format_exc())

    def on_animal_selection_changed(self):
        current_row = self.tblAnimals.currentRow()
        if current_row >= 0:
            name_item = self.tblAnimals.item(current_row, 1)
            if name_item:
                guid = name_item.data(QtCore.Qt.UserRole)
                # Get the animal
                myAnimal = LaUtils.getAnimal(guid)
                # Get the parameter GUID from combo box
                param_combo = self.tblAnimals.cellWidget(current_row, 2)
                if param_combo:
                    param_guid = param_combo.currentData(QtCore.Qt.UserRole)
                    myParameter = LaUtils.getAnimalParameter(param_guid)
                    # Update the display
                    self.showAnimalDefinitionReport(myAnimal, myParameter)
                    # Fix: Create QPixmap from image file path
                    if myAnimal.imageFile:
                        self.lblAnimalPix.setPixmap(QPixmap(myAnimal.imageFile))
                        self.lblAnimalPix.setScaledContents(True)
