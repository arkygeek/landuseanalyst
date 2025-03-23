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
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QSpinBox, QTableWidget

from la.ui.laanimalparametermanagerbase import LaAnimalParameterManagerBase
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lautils import LaUtils
from la.lib.la import AreaUnits, EnergyType, Priority
from la.lib.lagrass import LaGrass
import os

class LaAnimalParameterManager(LaAnimalParameterManagerBase):
    """Manager for animal parameters."""

    def __init__(self, thePair=None, parent=None, flags=Qt.WindowFlags()):
        """Initialize the Animal Parameter Manager."""
        super().__init__(parent, flags)
        self.readSettings()
        
        # Debug log to check UI initialization
        LaUtils.debug.log("Animal Parameter Manager: Initializing UI")
        
        # Verify key widgets exist
        for widget_name in ["leName", "leDescription", "cboAnimal", "sbPercentTameMeat", 
                            "checkBoxCommonRaster", "checkBoxSpecificRaster", "lblAnimalPic"]:
            if hasattr(self, widget_name):
                LaUtils.debug.log(f"Widget {widget_name} found")
            else:
                LaUtils.debug.log(f"WARNING: Widget {widget_name} not found!")
        
        # Make sure the animal parameters table is visible and has correct properties
        if hasattr(self, "tblAnimalParameterProfiles"):
            self.tblAnimalParameterProfiles.setVisible(True)
            self.tblAnimalParameterProfiles.horizontalHeader().setStretchLastSection(True)
            self.tblAnimalParameterProfiles.setAlternatingRowColors(True)
            self.tblAnimalParameterProfiles.setSelectionMode(QTableWidget.SingleSelection)
            self.tblAnimalParameterProfiles.setSelectionBehavior(QTableWidget.SelectRows)
        
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
        myList = []  # Will be populated by grass module later
        myMapsetList = []  # Will be populated by grass module later
        self.cboRaster.addItems(myList)

        # Hide experimental features
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)

        # Set up combo boxes and initial values
        self.setupAnimalsCombo()
        self.setupAreaUnitsCombo()
        self.setupEnergyTypeCombo()
        self.setupFallowComboBox()
        
        # Make the common raster value read-only
        if hasattr(self, 'sbCommonRasterValue'):
            self.sbCommonRasterValue.setReadOnly(True)
            self.sbCommonRasterValue.setValue(self.mCommonGrazedLandValue)

        # Initialize table and fodder
        self.refreshAnimalParameterTable()
        self.populateFodder()

    def setupAnimalsCombo(self):
        """Set up the animals combo box."""
        myAnimalsMap = LaUtils.getAvailableAnimals()
        for guid, animal in myAnimalsMap.items():
            myName = animal.name
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            self.cboAnimal.addItem(myIcon, myName, guid)

    def setupAreaUnitsCombo(self):
        """Set up the area units combo box."""
        self.cbAreaUnits.clear()
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")

    def setupEnergyTypeCombo(self):
        """Set up the energy type combo box."""
        self.cbSpecificLandEnergyType.clear()
        self.cbSpecificLandEnergyType.addItem("KCalories")
        self.cbSpecificLandEnergyType.addItem("TDN")

    def setupFallowComboBox(self):
        """Set up the fallow usage combo box with proper priority values."""
        self.cbFallowUsage.clear()
        self.cbFallowUsage.addItem("HIGH Fallow Priority", Priority.High)
        self.cbFallowUsage.addItem("MED Fallow Priority", Priority.Medium)
        self.cbFallowUsage.addItem("LOW Fallow Priority", Priority.Low)
        self.cbFallowUsage.addItem("No Fallow Priority", Priority.None_)

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
        LaUtils.debug.log(f"Selecting animal parameter with guid: {theFileName}")
        
        # Make sure we have the .xml suffix
        if not theFileName.endswith(".xml"):
            theFileName = f"{theFileName}.xml"
        
        myAnimalParameterDir = LaUtils.userAnimalParameterProfilesDirPath()
        filePath = os.path.join(myAnimalParameterDir, theFileName)
        
        LaUtils.debug.log(f"Loading animal parameter from file: {filePath}")
        
        if os.path.exists(filePath):
            self.mAnimalParameter = LaAnimalParameter()
            result = self.mAnimalParameter.fromXmlFile(filePath)
            LaUtils.debug.log(f"File loaded successfully: {result}")
            if result:
                self.showAnimalParameter()
            else:
                LaUtils.debug.log("ERROR: Failed to load animal parameter from XML file")
        else:
            LaUtils.debug.log(f"ERROR: Animal parameter file does not exist: {filePath}")

    def showAnimalParameter(self):
        """Display the current animal parameter in the UI."""
        # Debug log to see what we're trying to display
        LaUtils.debug.log(f"showAnimalParameter: Displaying animal parameter: {self.mAnimalParameter._mName}")
        LaUtils.debug.log(f"showAnimalParameter: Properties: animalGuid={self.mAnimalParameter.animalGuid}, percentTameMeat={self.mAnimalParameter.percentTameMeat}")
        
        # Set text fields and checkboxes
        self.leName.setText(str(self.mAnimalParameter.name))
        LaUtils.debug.log(f"showAnimalParameter: Set name text to: {self.mAnimalParameter.name}")
        
        self.leDescription.setText(str(self.mAnimalParameter.description))
        LaUtils.debug.log(f"showAnimalParameter: Set description text to: {self.mAnimalParameter.description}")
        
        # Check if animals combo exists and has items
        LaUtils.debug.log(f"showAnimalParameter: cboAnimal item count: {self.cboAnimal.count()}")
        
        result = self.setComboToDefault(self.cboAnimal, str(self.mAnimalParameter.animalGuid))
        LaUtils.debug.log(f"showAnimalParameter: setComboToDefault for animal guid returned: {result}")
        
        self.sbPercentTameMeat.setValue(float(self.mAnimalParameter.percentTameMeat))
        LaUtils.debug.log(f"showAnimalParameter: Set percent tame meat to: {float(self.mAnimalParameter.percentTameMeat)}")
        
        # Continue with other widgets...
        
        self.checkBoxCommonRaster.setChecked(bool(getattr(self.mAnimalParameter, '_mUseCommonGrazingLand', False)))
        self.checkBoxSpecificRaster.setChecked(bool(getattr(self.mAnimalParameter, '_mUseSpecificGrazingLand', False)))
        
        # Set area units and energy type
        areaUnits = getattr(self.mAnimalParameter, '_areaUnits', AreaUnits.Dunum)
        self.cbAreaUnits.setCurrentText("Dunum" if areaUnits == AreaUnits.Dunum else "Hectare")
        
        energyType = getattr(self.mAnimalParameter, '_energyType', EnergyType.KCalories)
        self.cbSpecificLandEnergyType.setCurrentText("KCalories" if energyType == EnergyType.KCalories else "TDN")

        # Update animal picture if available
        animalGuid = str(getattr(self.mAnimalParameter, '_mAnimalGuid', ""))
        if animalGuid:
            animals_map = LaUtils.getAvailableAnimals()
            if animalGuid in animals_map:
                animal = animals_map[animalGuid]
                if hasattr(animal, 'imageFile') and animal.imageFile:
                    image_path = LaUtils.resolvePath(str(animal.imageFile), 'image')
                    if os.path.exists(image_path):
                        pixmap = QPixmap(image_path)
                        if not pixmap.isNull():
                            self.lblAnimalPic.setPixmap(pixmap.scaled(
                                self.lblAnimalPic.width(),
                                self.lblAnimalPic.height(),
                                Qt.KeepAspectRatio,
                                Qt.SmoothTransformation
                            ))
                            return
            self.lblAnimalPic.clear()

        # Set fallow usage combo box based on Priority enum
        fallowUsage = getattr(self.mAnimalParameter, '_fallowUsage', Priority.None_)
        index = -1
        if fallowUsage == Priority.High:
            index = self.cbFallowUsage.findText("HIGH Fallow Priority")
        elif fallowUsage == Priority.Medium:
            index = self.cbFallowUsage.findText("MED Fallow Priority")
        elif fallowUsage == Priority.Low:
            index = self.cbFallowUsage.findText("LOW Fallow Priority")
        else:
            index = self.cbFallowUsage.findText("No Fallow Priority")
        
        if index >= 0:
            self.cbFallowUsage.setCurrentIndex(index)

        self.refreshFodderTable()

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

        myOriginalFileNameWithAddedPath = LaUtils.userAnimalParameterProfilesDirPath() + f"{myGuid}.xml"
        myAnimalParameter = LaAnimalParameter() # Load the original animal parameter
        myAnimalParameter.fromXmlFile(myOriginalFileNameWithAddedPath)
        myAnimalParameter.setGuid(None) # Clear the old GUID so the new copy will be unique
        myTempName = f"Copy of {myAnimalParameter.name}"
        myAnimalParameter._mName = myTempName
        myTempDescription = f"Copy of {myAnimalParameter.description}"
        myAnimalParameter._mDescription = myTempDescription

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
        # Basic parameters
        self.mAnimalParameter._mName = self.leName.text()
        self.mAnimalParameter._mDescription = self.leDescription.text()
        self.mAnimalParameter._mAnimalGuid = self.cboAnimal.currentData()
        self.mAnimalParameter._mPercentTameMeat = self.sbPercentTameMeat.value()
        self.mAnimalParameter._mUseCommonGrazingLand = self.checkBoxCommonRaster.isChecked()
        self.mAnimalParameter._mUseSpecificGrazingLand = self.checkBoxSpecificRaster.isChecked()

        # Set energy type and area units
        self.mAnimalParameter._energyType = EnergyType.KCalories if self.cbSpecificLandEnergyType.currentText() == "KCalories" else EnergyType.TDN
        self.mAnimalParameter._areaUnits = AreaUnits.Dunum if self.cbAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare

        # Set fallow usage based on combo box data
        index = self.cbFallowUsage.currentIndex()
        if index >= 0:
            self.mAnimalParameter._fallowUsage = self.cbFallowUsage.itemData(index)

        # Save parameter to file
        filepath = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(),
                              f"{self.mAnimalParameter.guid}.xml")
        self.mAnimalParameter.toXmlFile(filepath)
        
        # Refresh displays
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
            myFileItem = QTableWidgetItem(str(guid))
            myNameItem = QTableWidgetItem(str(getattr(parameter, '_mName', "")))

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
        self.tblAnimalParameterProfiles.setColumnWidth(0, 0)  # Hide GUID column
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