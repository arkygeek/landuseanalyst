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
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QFileDialog

from la.ui.lacropmanagerbase import LaCropManagerBase
from la.lib.lautils import LaUtils
from la.lib.lacrop import LaCrop


class LaCropManager(LaCropManagerBase):
    def __init__(self, theCropsMap=None, parent=None):
        """Constructor for the Crop Manager dialog.

        :param crops_map: Dictionary of crops with guid as key
        :type crops_map: dict
        :param parent: Parent widget
        :type parent: QWidget
        """
        super(LaCropManager, self).__init__(parent)

        # Initialize crops map (make a copy to avoid modifying the original)
        self._cropMap = {}
        if theCropsMap:
            for guid, value in theCropsMap.items():
                self._cropMap[guid] = value

        # Initialize other variables
        self._imageFile = ""
        self._crop = LaCrop()

        # Connect signals/slots
        self.connectSignalsSlots()

        # Populate the table with crops
        self.refreshCropTable()

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
        self._cropMap = LaUtils.getAvailableCrops()

        # Populate table
        myCurrentRow = 0
        mySelectedRow = 0

        for guid, crop in self._cropMap.items():
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
        self._crop = myCrop
        self._imageFile = ""
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
        self._crop = LaCrop()
        if not os.path.exists(myOriginalFileName):
            QMessageBox.warning(self, "Edit Crop", f"Could not find crop file: {myOriginalFileName}")
            return

        self._crop.fromXmlFile(myOriginalFileName)
        self._imageFile = self._crop.imageFile
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

        self._crop = LaCrop()
        self._crop.fromXmlFile(myOriginalFileName)

        # Change name to indicate it's a copy
        myNewName = str(self._crop.name)
        self._crop.name = f"{myNewName} (copy)"

        # Generate a new GUID
        self._crop.setGuid(None)

        # Keep the same image
        self._crop._imageFile = self._crop.imageFile

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
            # Save the image to the user data directory
            from la.lib.lautils import LaUtils
            savedPath = LaUtils.saveFilePath(fileName, 'image')

            # Copy the file if it's not already there
            if fileName != savedPath:
                shutil.copy(fileName, savedPath)

            pixmap = QPixmap(savedPath)
            if not pixmap.isNull():
                self.lblCropPix.setPixmap(pixmap)
                self._imageFile = savedPath
            else:
                QMessageBox.warning(self, "Image Error", "Could not load the selected image.")

    def on_tblCrops_itemSelectionChanged(self):
        """Handle selection change in the crops table."""
        if self.tblCrops.currentRow() < 0:
            return

        try:
            myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
            if not myGuid:
                return

            myOriginalFileName = LaUtils.userCropProfilesDirPath() + "/" + myGuid + ".xml"
            if not os.path.exists(myOriginalFileName):
                return

            self._crop = LaCrop()
            self._crop.fromXmlFile(myOriginalFileName)
            self._imageFile = self._crop.imageFile
            self.showCrop()
        except Exception as e:
            QMessageBox.warning(self, "Selection Change Error", f"Error loading crop: {str(e)}")

    def showCrop(self):
        """Show the current crop in the form."""
        try:
            self.leName.setText(str(self._crop.name))
            self.leDescription.setText(str(self._crop.description))
            self.sbCropYield.setValue(self._crop.cropYield)
            self.sbCropCalories.setValue(self._crop.cropCalories)
            self.sbCropFodderProduction.setValue(str(self._crop.cropFodderProduction))
            self.sbCropFodderValue.setValue(str(self._crop.cropFodderValue))

            # Handle comboboxes with bounds checking
            areaUnitsIndex = max(0, min(self.cbAreaUnits.count() - 1, str(self._crop.areaUnits)))
            self.cbAreaUnits.setCurrentIndex(areaUnitsIndex)

            energyTypeIndex = max(0, min(self.cbFodderEnergyType.count() - 1, str(self._crop.cropFodderEnergyType)))
            self.cbFodderEnergyType.setCurrentIndex(energyTypeIndex)

            # Show image if available
            if self._crop.imageFile and os.path.exists(str(self._crop.imageFile)):
                pixmap = QPixmap(self._crop.imageFile)
                self.lblCropPix.setPixmap(pixmap)
            else:
                self.lblCropPix.clear()
        except Exception as e:
            QMessageBox.warning(self, "Show Crop Error", f"Error displaying crop data: {str(e)}")

    def accept(self):
        """Handle OK button click to save changes."""
        try:
            # Validate form
            if not self.leName.text():
                QMessageBox.warning(self, "Validation Error", "Crop name cannot be empty.")
                self.leName.setFocus()
                return

            # Save crop data from form
            self._crop.name = self.leName.text()
            self._crop.description = self.leDescription.text()
            self._crop.cropYield = self.sbCropYield.value()
            self._crop.cropCalories = self.sbCropCalories.value()
            self._crop.cropFodderProduction = self.sbCropFodderProduction.value()
            self._crop.cropFodderValue = self.sbCropFodderValue.value()
            self._crop.areaUnits = self.cbAreaUnits.currentIndex()
            self._crop.cropFodderEnergyType = self.cbFodderEnergyType.currentIndex()
            self._crop.imageFile = self.imageFile()

            # Make sure we have a valid GUID
            if not self._crop.guid:
                self._crop.setGuid(None)

            # Ensure crops directory exists
            cropDirPath = LaUtils.userCropProfilesDirPath()
            if not os.path.exists(cropDirPath):
                os.makedirs(cropDirPath)

            # Save to file
            myFileName = cropDirPath + "/" + str(self._crop.guid) + ".xml"
            success = self._crop.toXmlFile(myFileName)

            if success:
                # Refresh the table, selecting the saved crop
                self.refreshCropTable(self._crop.guid)

                # Accept and close the dialog
                super(LaCropManager, self).accept()
            else:
                QMessageBox.critical(self, "Save Error", f"Failed to save crop to {myFileName}")

        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Error saving crop data: {str(e)}")

    def reject(self):
        """Handle Cancel button click."""
        # Simply call the parent's reject method
        super(LaCropManager, self).reject()

    def getCrops(self):
        """Return the crops map.

        :returns: Dictionary of crops
        :rtype: dict
        """
        return self._cropMap