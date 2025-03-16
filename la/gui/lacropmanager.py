# -*- coding: utf-8 -*-
"""
LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
of a settlement (with respect to required land needed for food production).
Land area targets for each food source supplied to the model are calculated based
on a multitude of demographic and dietary inputs.

This file implements the Crop Manager functionality.

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

import os
import shutil
from qgis.PyQt import QtCore, QtWidgets
from qgis.PyQt.QtCore import QSettings
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QFileDialog

from la.ui.lacropmanagerbase import LaCropManagerBase
from la.lib.lautils import LaUtils
from la.lib.lacrop import LaCrop
from la.lib.la import AreaUnits, EnergyType


class LaCropManager(LaCropManagerBase):
    def __init__(self, theCropsMap, parent=None):
        """Constructor for the Crop Manager dialog.

        :param theCropsMap: Dictionary of crops with guid as key
        :type theCropsMap: dict
        :param parent: Parent widget
        :type parent: QWidget
        """
        super(LaCropManager, self).__init__(parent)
        # Store a working copy of the crops map
        self.mCropsMap = theCropsMap.copy() if theCropsMap else {}
        # Initialize crops map (make a copy to avoid modifying the original)
        if theCropsMap:
            for guid, value in theCropsMap.items():
                self.mCropsMap[guid] = value

        # Initialize other variables
        self.imageFile = ""
        self.crop = LaCrop()

        # Connect signals/slots
        self.connectSignalsSlots()
        self.setupComboBoxes()  # Add this line to initialize combo boxes

        # Populate the table with crops
        self.refreshCropTable()

        # Read window settings
        self.readSettings()


    def connectSignalsSlots(self):
        """Connect signals to slots for UI interaction."""
        # Connect buttons
        self.toolNew.clicked.connect(self.on_toolNew_clicked)
        # self.toolEdit.clicked.connect(self.on_toolEdit_clicked)  # Commented out
        self.toolDelete.clicked.connect(self.on_toolDelete_clicked)
        self.toolCopy.clicked.connect(self.on_toolCopy_clicked)
        self.pbnCropPic.clicked.connect(self.on_pbnCropPic_clicked)

        # Connect the table selection change
        self.tblCrops.itemSelectionChanged.connect(self.on_tblCrops_itemSelectionChanged)

        # Connect the dialog buttons
        # self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

    def refreshCropTable(self, theGuid=None):
        """Refresh the crops table with current data.

        :param theGuid: GUID of crop to select after refresh
        :type theGuid: str
        """
        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(2)

        # Get available crops
        self.mCropMap = LaUtils.getAvailableCrops()

        # Populate table
        myCurrentRow = 0
        mySelectedRow = 0

        for guid, crop in self.mCropMap.items():
            self.tblCrops.insertRow(myCurrentRow)

            # GUID column (hidden)
            guidItem = QTableWidgetItem(guid)
            self.tblCrops.setItem(myCurrentRow, 0, guidItem)

            # Name column
            nameItem = QTableWidgetItem(str(crop.name))
            nameItem.setIcon(QIcon(":/localdata.png"))
            self.tblCrops.setItem(myCurrentRow, 1, nameItem)

            # Store selection row if this is the requested GUID
            if theGuid and guid == theGuid:
                mySelectedRow = myCurrentRow

            myCurrentRow += 1

        # Hide the GUID column
        self.tblCrops.setColumnWidth(0, 0)
        self.tblCrops.setColumnWidth(1, self.tblCrops.width())
        self.tblCrops.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Select the requested row if we have items in the table
        if self.tblCrops.rowCount() > 0:
            self.tblCrops.selectRow(mySelectedRow)
            self.on_tblCrops_itemSelectionChanged()

    def on_toolNew_clicked(self):
        """Create a new crop."""
        myCrop = LaCrop()
        myCrop.setGuid(None)  # Generate a new GUID
        self.crop = myCrop
        self.imageFile = ""
        self.showCrop()

        # Clear form fields for new crop
        self.leName.clear()
        self.leDescription.clear()
        self.sbCropYield.setValue(0)
        self.sbCropCalories.setValue(0)
        self.sbCropFodderProduction.setValue(0)
        self.sbCropFodderValue.setValue(0)
        self.cbAreaUnits.setCurrentIndex(0)
        self.cbFodderEnergyType.setCurrentIndex(0)
        self.lblCropPix.clear()

        # Set focus to name field
        self.leName.setFocus()

    def on_toolEdit_clicked(self):
        """Edit the selected crop."""
        if self.tblCrops.currentRow() < 0:
            QMessageBox.information(self, "Edit Crop", "Please select a crop to edit.")
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if not myGuid:
            QMessageBox.warning(self, "Edit Crop", "Could not determine crop GUID.")
            return

        myOriginalFileName = LaUtils.userCropProfilesDirPath() + "/" + myGuid + ".xml"
        self.crop = LaCrop()
        if not os.path.exists(myOriginalFileName):
            QMessageBox.warning(self, "Edit Crop", f"Could not find crop file: {myOriginalFileName}")
            return

        self.crop.fromXmlFile(myOriginalFileName)
        self.imageFile = self.crop.imageFile
        self.showCrop()

    def on_toolDelete_clicked(self):
        """Delete the selected crop."""
        if self.tblCrops.currentRow() < 0:
            QMessageBox.information(self, "Delete Crop", "Please select a crop to delete.")
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if not myGuid:
            QMessageBox.warning(self, "Delete Crop", "Could not determine crop GUID.")
            return

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Delete Crop",
            "Are you sure you want to delete this crop?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Delete the file
            myFileName = LaUtils.userCropProfilesDirPath() + "/" + myGuid + ".xml"
            if os.path.exists(myFileName):
                os.remove(myFileName)
                # Refresh the table
                self.refreshCropTable()
            else:
                QMessageBox.warning(self, "Delete Crop", f"Could not find crop file: {myFileName}")

    def on_toolCopy_clicked(self):
        """Copy the selected crop."""
        if self.tblCrops.currentRow() < 0:
            QMessageBox.information(self, "Copy Crop", "Please select a crop to copy.")
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if not myGuid:
            QMessageBox.warning(self, "Copy Crop", "Could not determine crop GUID.")
            return

        myOriginalFileName = LaUtils.userCropProfilesDirPath() + "/" + myGuid + ".xml"
        if not os.path.exists(myOriginalFileName):
            QMessageBox.warning(self, "Copy Crop", f"Could not find crop file: {myOriginalFileName}")
            return

        self.crop = LaCrop()
        self.crop.fromXmlFile(myOriginalFileName)

        # Change name to indicate it's a copy
        myNewName = self.crop.name
        self.crop.name = f"{myNewName} (copy)"

        # Generate a new GUID
        self.crop.setGuid(None)

        # Keep the same image
        self.crop.imageFile = self.crop.imageFile

        self.showCrop()

    def on_pbnCropPic_clicked(self):
        """Open image file dialog for crop picture."""
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Select Crop Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)",
            options=options
        )

        if fileName:
            try:
                # Get just the filename without path
                baseFileName = os.path.basename(fileName)

                # Save the image to the user data directory
                imagesDir = LaUtils.userImagesDirPath()
                savedPath = os.path.join(imagesDir, baseFileName)

                print(f"DEBUG: Saving image from {fileName} to {savedPath}")

                # Copy the file if it's not already there
                if fileName != savedPath and not os.path.exists(savedPath):
                    shutil.copy(fileName, savedPath)

                # Update the image display
                pixmap = QPixmap(savedPath)
                if not pixmap.isNull():
                    self.lblCropPix.setPixmap(pixmap)
                    # Store just the filename, not the full path
                    self.imageFile = baseFileName
                    print(f"DEBUG: Image set to: {self.imageFile}")
                else:
                    QMessageBox.warning(self, "Image Error", "Could not load the selected image.")
                    print(f"DEBUG: Failed to load image from {savedPath}")
            except Exception as e:
                QMessageBox.warning(self, "Image Error", f"Error processing image: {str(e)}")
                import traceback
                print(f"DEBUG: Exception in on_pbnCropPic_clicked: {traceback.format_exc()}")

    def on_tblCrops_itemSelectionChanged(self):
        """Handle selection change in the crops table."""
        if self.tblCrops.currentRow() < 0:
            return

        try:
            myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
            if not myGuid:
                return

            myOriginalFileName = LaUtils.userCropProfilesDirPath() + "/" + myGuid + ".xml"
            print(f"DEBUG: Looking for crop XML file: {myOriginalFileName}")

            if not os.path.exists(myOriginalFileName):
                print(f"DEBUG: XML file doesn't exist: {myOriginalFileName}")
                return

            self.crop = LaCrop()
            print(f"DEBUG: Loading crop from XML file: {myOriginalFileName}")
            success = self.crop.fromXmlFile(myOriginalFileName)
            print(f"DEBUG: fromXmlFile result: {success}")

            if success:
                print(f"DEBUG: After loading - cropYield: {self.crop.cropYield}, type: {type(self.crop.cropYield)}")
                print(f"DEBUG: After loading - cropFodderProduction: {self.crop.cropFodderProduction}, type: {type(self.crop.cropFodderProduction)}")
                print(f"DEBUG: Image path from crop: {self.crop.imageFile}")

                self.showCrop()
            else:
                QMessageBox.warning(self, "Load Error", f"Failed to load crop from {myOriginalFileName}")
        except Exception as e:
            QMessageBox.warning(self, "Selection Change Error", f"Error loading crop: {str(e)}")
            import traceback
            print(f"DEBUG: Exception in itemSelectionChanged: {traceback.format_exc()}")

    def showCrop(self):
        """Show the current crop in the form."""
        try:
            print(f"DEBUG: Showing crop: {self.crop.name}")
            print(f"DEBUG: cropYield value: {self.crop.cropYield}, type: {type(self.crop.cropYield)}")
            print(f"DEBUG: cropFodderProduction value: {self.crop.cropFodderProduction}, type: {type(self.crop.cropFodderProduction)}")

            self.leName.setText(str(self.crop.name))
            self.leDescription.setText(str(self.crop.description))

            # Handle cropYield - ensure it's an integer
            try:
                self.sbCropYield.setValue(int(self.crop.cropYield))
            except (ValueError, TypeError) as e:
                print(f"DEBUG: Error converting cropYield: {e}")
                self.sbCropYield.setValue(0)

            # Handle cropCalories
            try:
                self.sbCropCalories.setValue(int(self.crop.cropCalories))
            except (ValueError, TypeError) as e:
                print(f"DEBUG: Error converting cropCalories: {e}")
                self.sbCropCalories.setValue(0)

            # Handle cropFodderProduction
            try:
                self.sbCropFodderProduction.setValue(int(self.crop.cropFodderProduction))
            except (ValueError, TypeError) as e:
                print(f"DEBUG: Error converting cropFodderProduction: {e}")
                self.sbCropFodderProduction.setValue(0)

            # Handle cropFodderValue
            try:
                self.sbCropFodderValue.setValue(int(self.crop.cropFodderValue))
            except (ValueError, TypeError) as e:
                print(f"DEBUG: Error converting cropFodderValue: {e}")
                self.sbCropFodderValue.setValue(0)

            # For area units, find the enum value index directly
            if isinstance(self.crop.areaUnits, AreaUnits):
                # If it's already an enum, use its value directly
                areaUnitsValue = self.crop.areaUnits.value
            else:
                # Try to convert to int or look up in the enum
                try:
                    areaUnitsValue = int(self.crop.areaUnits)
                except (ValueError, TypeError):
                    # Convert string representation to enum value if possible
                    areaUnitsStr = str(self.crop.areaUnits)
                    for unit in AreaUnits:
                        if unit.name in areaUnitsStr:
                            areaUnitsValue = unit.value
                            break
                    else:
                        areaUnitsValue = 0  # Default to first item

            # Use min/max to ensure the index is within valid range
            areaUnitsIndex = max(0, min(self.cbAreaUnits.count() - 1, areaUnitsValue))
            self.cbAreaUnits.setCurrentIndex(areaUnitsIndex)

            # Similarly for energy type
            if isinstance(self.crop.cropFodderEnergyType, EnergyType):
                energyTypeValue = self.crop.cropFodderEnergyType.value
            else:
                try:
                    energyTypeValue = int(self.crop.cropFodderEnergyType)
                except (ValueError, TypeError):
                    energyTypeStr = str(self.crop.cropFodderEnergyType)
                    for etype in EnergyType:
                        if etype.name in energyTypeStr:
                            energyTypeValue = etype.value
                            break
                    else:
                        energyTypeValue = 0  # Default to first item

            energyTypeIndex = max(0, min(self.cbFodderEnergyType.count() - 1, energyTypeValue))
            self.cbFodderEnergyType.setCurrentIndex(energyTypeIndex)

            # Show image if available
            if self.crop.imageFile:
                # Resolve image path using LaUtils
                imagePath = LaUtils.resolvePath(self.crop.imageFile, 'image')
                print(f"DEBUG: Resolved image path: {imagePath}")

                # Update self.imageFile so it gets saved correctly
                self.imageFile = self.crop.imageFile

                # Try to load the image
                if os.path.exists(imagePath):
                    pixmap = QPixmap(imagePath)
                    if not pixmap.isNull():
                        self.lblCropPix.setPixmap(pixmap)
                        print(f"DEBUG: Successfully loaded image from: {imagePath}")
                    else:
                        print(f"DEBUG: Failed to load image - pixmap is null: {imagePath}")
                        self.lblCropPix.clear()
                else:
                    print(f"DEBUG: Image file doesn't exist: {imagePath}")

                    # Try from images directory
                    imagesDir = LaUtils.userImagesDirPath()
                    imageFileName = os.path.basename(self.crop.imageFile)
                    alternativePath = os.path.join(imagesDir, imageFileName)

                    if os.path.exists(alternativePath):
                        pixmap = QPixmap(alternativePath)
                        if not pixmap.isNull():
                            self.lblCropPix.setPixmap(pixmap)
                            print(f"DEBUG: Successfully loaded image from alternative path: {alternativePath}")
                        else:
                            print(f"DEBUG: Failed to load image from alternative path: {alternativePath}")
                            self.lblCropPix.clear()
                    else:
                        print(f"DEBUG: Alternative image path doesn't exist: {alternativePath}")
                        self.lblCropPix.clear()
            else:
                print("DEBUG: No image file specified")
                self.lblCropPix.clear()

        except Exception as e:
            QMessageBox.warning(self, "Show Crop Error", f"Error displaying crop data: {str(e)}")
            import traceback
            print(f"DEBUG: Exception in showCrop: {traceback.format_exc()}")

    def accept(self):
        """Handle OK button click to save changes."""
        try:
            # Validate form
            if not self.leName.text():
                QMessageBox.warning(self, "Validation Error", "Crop name cannot be empty.")
                self.leName.setFocus()
                return

            # Save crop data from form
            self.crop.name = self.leName.text()
            self.crop.description = self.leDescription.text()
            self.crop.cropYield = int(self.sbCropYield.value())  # Ensure cropYield is saved as an integer
            self.crop.cropCalories = self.sbCropCalories.value()
            self.crop.cropFodderProduction = self.sbCropFodderProduction.value()
            self.crop.cropFodderValue = self.sbCropFodderValue.value()
            self.crop.areaUnits = AreaUnits(self.cbAreaUnits.currentIndex())
            self.crop.cropFodderEnergyType = EnergyType(self.cbFodderEnergyType.currentIndex())

            # Store just the filename, not the full path for the image
            if self.imageFile:
                self.crop.imageFile = os.path.basename(self.imageFile)

            print(f"DEBUG: Saving crop with image: {self.crop.imageFile}")

            # Make sure we have a valid GUID
            if not self.crop.guid:
                self.crop.setGuid(None)

            # Ensure crops directory exists
            cropDirPath = LaUtils.userCropProfilesDirPath()
            if not os.path.exists(cropDirPath):
                os.makedirs(cropDirPath)

            # Save to file
            myFileName = cropDirPath + "/" + str(self.crop.guid) + ".xml"
            success = self.crop.toXmlFile(myFileName)

            if success:
                print(f"DEBUG: Successfully saved crop to {myFileName}")
                # Refresh the table, selecting the saved crop
                self.refreshCropTable(self.crop.guid)

                # Accept and close the dialog
                super(LaCropManager, self).accept()
            else:
                QMessageBox.critical(self, "Save Error", f"Failed to save crop to {myFileName}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Error saving crop data: {str(e)}")
            import traceback
            print(f"DEBUG: Exception in accept: {traceback.format_exc()}")

    def reject(self):
        """Handle Cancel button click."""
        # Simply call the parent's reject method
        super(LaCropManager, self).reject()

    def getCrops(self):
        """Return the crops map.

        :returns: Dictionary of crops
        :rtype: dict
        """
        return self.mCropMap

    def readSettings(self):
        """Reads the settings of the window's position and size from QSettings."""
        settings = QSettings()
        pos = settings.value("mainwindow/pos", QtCore.QPoint(200, 200))
        size = settings.value("mainwindow/size", QtCore.QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        """Saves the window's position and size to QSettings."""
        settings = QSettings()
        settings.setValue("mainwindow/pos", self.pos())
        settings.setValue("mainwindow/size", self.size())

    def populateEnumComboBox(self, comboBox, enumClass):
        """
        Populate a combo box with items from an enum class.

        :param comboBox: The combo box to populate
        :type comboBox: QComboBox
        :param enumClass: The enum class to use
        :type enumClass: Enum class
        """
        comboBox.clear()
        for member in enumClass:
            # Extract the name, replacing underscores with spaces if needed
            display_name = member.name.replace('_', ' ')
            # Use the enum value as the data item
            comboBox.addItem(display_name, member.value)

    def setupComboBoxes(self):
        """Initialize combo boxes with values from enums."""
        # Populate area units combo box
        self.populateEnumComboBox(self.cbAreaUnits, AreaUnits)
        # Populate energy type combo box
        self.populateEnumComboBox(self.cbFodderEnergyType, EnergyType)