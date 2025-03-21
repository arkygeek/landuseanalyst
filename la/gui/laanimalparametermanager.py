"""
laanimalparametermanager.py - A PyQt5 implementation of the LaAnimalParameterManager class.

This file contains the LaAnimalParameterManager class, which is a PyQt5 implementation of the
LaAnimalParameterManager class from the original C++ code. The class is responsible for managing
animal parameters, including adding, removing, and editing animal parameters.

Author: [Jason Jorgenson]
Date created: [12-OCT-2023]
"""

from qgis.PyQt.QtCore import Qt, QSettings
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QSpinBox

from la.ui.laanimalparametermanagerbase import LaAnimalParameterManagerBase
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lautils import LaUtils
from la.lib.la import AreaUnits, EnergyType as LaEnergyType, Priority
from la.lib.lagrass import LaGrass
import os

class LaAnimalParameterManager(LaAnimalParameterManagerBase):
    """Manager for animal parameters.

    This class provides the functionality for managing animal parameters, including
    creating, editing, copying, and deleting animal parameters.
    """

    def __init__(self, thePair=None, parent=None, flags=Qt.WindowFlags()):
        """Initialize the Animal Parameter Manager.

        Args:
            thePair: A tuple containing selected crops map and common grazed land value
            parent: Parent widget
            flags: Window flags
        """
        super(LaAnimalParameterManager, self).__init__(parent, flags)
        self.readSettings()

        # Initialize member variables
        self.mAnimalParameterMap = {}
        self.mAnimalParameter = LaAnimalParameter()
        self.mSelectedCropsMap = {}
        self.mCommonGrazedLandValue = 0
        self.mCommonGrazingLandAreaUnits = AreaUnits.Dunum

        # Connect signals
        self.tblAnimalParameterProfiles.cellClicked.connect(self.cellClicked)
        self.cboAnimal.currentIndexChanged.connect(self.on_cboAnimal_changed)

        # Set up the raster combo box with available maps
        myList = []
        myGrass = LaGrass()
        myMapsetList = []  # myGrass.getMapsetList() @TODO get Grass stuff working
        self.cboRaster.addItems(myList)

        # Hide import/export buttons for now
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)

        # Set up combo boxes
        self.setupAnimalsCombo()
        self.setupAreaUnitsCombo()
        self.setupEnergyTypeCombo()
        self.setupFallowComboBox()

        # Initialize the parameters table
        self.refreshAnimalParameterTable()
        self.populateFodder()

    def setupAnimalsCombo(self):
        """Set up the animals combo box with available animals."""
        myAnimalsMap = LaUtils.getAvailableAnimals()

        for animalGuid, myAnimal in myAnimalsMap.items():
            myName = myAnimal.name
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            self.cboAnimal.addItem(myName, animalGuid)

    def setupAreaUnitsCombo(self):
        """Set up the area units combo box."""
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")

    def setupEnergyTypeCombo(self):
        """Set up the energy type combo box."""
        self.cbSpecificLandEnergyType.addItem("KCalories")
        self.cbSpecificLandEnergyType.addItem("TDN")

    def setupFallowComboBox(self):
        """Set up the fallow usage combo box."""
        self.cbFallowUsage.addItem("Do Not Graze Fallow", "None")
        self.cbFallowUsage.addItem("HIGH Fallow Priority", "High")
        self.cbFallowUsage.addItem("MED Fallow Priority", "Medium")
        self.cbFallowUsage.addItem("LOW Fallow Priority", "Low")

    def readSettings(self):
        """Read window settings."""
        settings = QSettings()
        if settings.contains("/LanduseAnalyst/AnimalParameterManager/geometry"):
            self.restoreGeometry(settings.value("/LanduseAnalyst/AnimalParameterManager/geometry"))

    def writeSettings(self):
        """Save window settings."""
        settings = QSettings()
        settings.setValue("/LanduseAnalyst/AnimalParameterManager/geometry", self.saveGeometry())

    def cellClicked(self, theRow: int, theColumn: int):
        """Handle cell click event in the animal parameters table."""
        item = self.tblAnimalParameterProfiles.item(theRow, 0)
        if item:
            self.selectAnimalParameter(item.text())

    def selectAnimalParameter(self, theFileName: str):
        """Load and display the selected animal parameter."""
        myAnimalParameterDir = LaUtils.userAnimalParameterProfilesDirPath()
        self.mAnimalParameter = LaAnimalParameter()
        self.mAnimalParameter.fromXmlFile(os.path.join(myAnimalParameterDir, theFileName))
        self.showAnimalParameter()

    def showAnimalParameter(self):
        """Display the current animal parameter in the UI."""
        self.leName.setText(self.mAnimalParameter.name)
        self.leDescription.setText(self.mAnimalParameter.description)
        self.setComboToDefault(self.cboAnimal, self.mAnimalParameter.animalGuid)
        self.sbPercentTameMeat.setValue(self.mAnimalParameter.percentTameMeat)
        self.checkBoxCommonRaster.setChecked(self.mAnimalParameter.useCommonGrazingLand)
        self.checkBoxSpecificRaster.setChecked(self.mAnimalParameter.useSpecificGrazingLand)
        self.refreshFodderTable()

        # Set fallow usage combo box
        fallowUsage = self.mAnimalParameter.fallowUsage
        if fallowUsage == Priority.High:
            self.setComboToDefault(self.cbFallowUsage, "High")
        elif fallowUsage == Priority.Medium:
            self.setComboToDefault(self.cbFallowUsage, "Medium")
        elif fallowUsage == Priority.Low:
            self.setComboToDefault(self.cbFallowUsage, "Low")
        else:
            self.setComboToDefault(self.cbFallowUsage, "None")

    def on_toolNew_clicked(self):
        """Handle new button click."""
        self.mAnimalParameter = LaAnimalParameter()
        self.showAnimalParameter()

    def on_toolCopy_clicked(self):
        """Handle copy button click."""
        currentRow = self.tblAnimalParameterProfiles.currentRow()
        if currentRow < 0:
            QMessageBox.information(self, "Copy Animal Parameter", "Please select an Animal Parameter to copy.")
            return

        myGuid = self.tblAnimalParameterProfiles.item(currentRow, 0).text()
        if not myGuid:
            return

        myOriginalFileName = LaUtils.userAnimalParameterProfilesDirPath() + f"{myGuid}.xml"
        myAnimalParameter = LaAnimalParameter()
        myAnimalParameter.fromXmlFile(myOriginalFileName)
        myAnimalParameter.setGuid(None)
        myAnimalParameter.name = "Copy of " + myAnimalParameter.name

        myNewFileName = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(), 
                                   f"{myAnimalParameter.guid}.xml")
        myAnimalParameter.toXmlFile(myNewFileName)
        self.refreshAnimalParameterTable(str(myAnimalParameter.guid))
        self.refreshFodderTable()

    def on_toolDelete_clicked(self):
        """Handle delete button click."""
        currentRow = self.tblAnimalParameterProfiles.currentRow()
        if currentRow < 0:
            return

        myGuid = self.tblAnimalParameterProfiles.item(currentRow, 0).text()
        if not myGuid:
            return

        fileName = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(), f"{myGuid}.xml")
        if os.path.exists(fileName):
            os.remove(fileName)
        self.refreshAnimalParameterTable()

    def on_pbnApply_clicked(self):
        """Handle apply button click."""
        self.mAnimalParameter.name = self.leName.text()
        self.mAnimalParameter.description = self.leDescription.text()
        self.mAnimalParameter.animalGuid = self.cboAnimal.currentData()
        self.mAnimalParameter.percentTameMeat = self.sbPercentTameMeat.value()
        self.mAnimalParameter.useCommonGrazingLand = self.checkBoxCommonRaster.isChecked()
        self.mAnimalParameter.useSpecificGrazingLand = self.checkBoxSpecificRaster.isChecked()

        # Set energy type and area units
        energyType = LaEnergyType.KCalories if self.cbSpecificLandEnergyType.currentText() == "KCalories" else LaEnergyType.TDN
        areaUnits = AreaUnits.Dunum if self.cbAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare

        # Set fallow usage
        fallowText = self.cbFallowUsage.currentText()
        if fallowText == "HIGH Fallow Priority":
            self.mAnimalParameter.fallowUsage = Priority.High
        elif fallowText == "MED Fallow Priority":
            self.mAnimalParameter.fallowUsage = Priority.Medium
        elif fallowText == "LOW Fallow Priority":
            self.mAnimalParameter.fallowUsage = Priority.Low
        else:
            self.mAnimalParameter.fallowUsage = Priority.None_

        # Save to file
        filepath = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(),
                              f"{self.mAnimalParameter.guid}.xml")
        self.mAnimalParameter.toXmlFile(filepath)
        self.refreshAnimalParameterTable(str(self.mAnimalParameter.guid))
        self.refreshFodderTable()

    def refreshAnimalParameterTable(self, theGuid: str = ""):
        """Refresh the animal parameters table."""
        self.mAnimalParameterMap.clear()
        self.tblAnimalParameterProfiles.clear()
        self.tblAnimalParameterProfiles.setRowCount(0)
        self.tblAnimalParameterProfiles.setColumnCount(2)

        self.mAnimalParameterMap = LaUtils.getAvailableAnimalParameters()
        mySelectedRow = 0
        myCurrentRow = 0

        for guid, parameter in self.mAnimalParameterMap.items():
            self.tblAnimalParameterProfiles.insertRow(myCurrentRow)
            myFileItem = QTableWidgetItem(guid)
            myNameItem = QTableWidgetItem(parameter.name)
            
            self.tblAnimalParameterProfiles.setItem(myCurrentRow, 0, myFileItem)
            self.tblAnimalParameterProfiles.setItem(myCurrentRow, 1, myNameItem)

            if theGuid and guid == theGuid:
                mySelectedRow = myCurrentRow
                self.mAnimalParameter = parameter
            myCurrentRow += 1

        if not theGuid:
            self.on_toolNew_clicked()

        # Set headers
        self.tblAnimalParameterProfiles.setHorizontalHeaderLabels(["File Name", "Name"])
        self.tblAnimalParameterProfiles.setColumnWidth(0, 0)
        self.tblAnimalParameterProfiles.setColumnWidth(1, self.tblAnimalParameterProfiles.width())
        self.tblAnimalParameterProfiles.horizontalHeader().hide()
        self.tblAnimalParameterProfiles.verticalHeader().hide()
        self.tblAnimalParameterProfiles.sortItems(1, Qt.AscendingOrder)

    def refreshFodderTable(self):
        """Refresh the fodder table."""
        # Implementation for fodder table refresh
        pass

    def populateFodder(self):
        """Populate the fodder table."""
        # Implementation for populating fodder table
        pass

    def setComboToDefault(self, combo, default):
        """Set a combo box to a default value."""
        index = combo.findData(default)
        if index >= 0:
            combo.setCurrentIndex(index)
            return True
        return False

    def closeEvent(self, event):
        """Handle window close event."""
        self.writeSettings()
        super().closeEvent(event)
    
    def on_cboAnimal_changed(self, index):
        """Handle animal combo box change event."""
        # Implementation for animal combo change
        pass