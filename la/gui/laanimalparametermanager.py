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
        self.cboAnimal.clear()  # Clear existing items
        
        for guid, animal in myAnimalsMap.items():
            # Store the GUID as a string, not as an object with a guid method
            guid_str = str(guid)
            myName = animal.name
            
            LaUtils.debug.log(f"setupAnimalsCombo: Adding animal {myName} with GUID {guid_str}")
            
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            self.cboAnimal.addItem(myIcon, myName, guid_str)

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
        LaUtils.debug.log(f"showAnimalParameter: Displaying animal parameter: {self.mAnimalParameter._mName}")
        LaUtils.debug.log(f"showAnimalParameter: Properties: animalGuid={self.mAnimalParameter._mAnimalGuid}, percentTameMeat={self.mAnimalParameter._mPercentTameMeat}")
    
        # Set UI elements with parameter values
        self.leName.setText(str(self.mAnimalParameter._mName))
        LaUtils.debug.log(f"showAnimalParameter: Set name text to: {self.mAnimalParameter._mName}")
        
        self.leDescription.setText(str(self.mAnimalParameter._mDescription))
        LaUtils.debug.log(f"showAnimalParameter: Set description text to: {self.mAnimalParameter._mDescription}")
        
        # Handle matching the correct animal in the combo box
        LaUtils.debug.log(f"showAnimalParameter: cboAnimal item count: {self.cboAnimal.count()}")
        
        found_match = False
        if self.mAnimalParameter._mAnimalGuid:
            # Try to find a direct string match first
            for i in range(self.cboAnimal.count()):
                animal = self.cboAnimal.itemData(i)
                animal_guid = ""
                
                # Get the guid as a string
                if hasattr(animal, 'guid'):
                    if callable(animal.guid):
                        try:
                            animal_guid = animal.guid()
                        except:
                            animal_guid = str(animal.guid)
                    else:
                        animal_guid = animal.guid
                else:
                    animal_guid = str(animal)
                    
                # Compare the last part of the guid string
                target_guid = str(self.mAnimalParameter._mAnimalGuid)
                if target_guid in animal_guid or animal_guid in target_guid:
                    self.cboAnimal.setCurrentIndex(i)
                    LaUtils.debug.log(f"showAnimalParameter: Found matching animal at index {i}")
                    found_match = True
                    break
        
        if not found_match:
            # Fall back to setComboToDefault
            result = self.setComboToDefault(self.cboAnimal, self.mAnimalParameter._mAnimalGuid)
            LaUtils.debug.log(f"showAnimalParameter: setComboToDefault for animal guid returned: {result}")
        
        # Set other parameters
        self.sbPercentTameMeat.setValue(float(self.mAnimalParameter._mPercentTameMeat))
        LaUtils.debug.log(f"showAnimalParameter: Set percent tame meat to: {self.mAnimalParameter._mPercentTameMeat}")
        
        # Update the animal picture
        LaUtils.debug.log(f"showAnimalParameter: Updating animal picture for animal GUID: {self.mAnimalParameter._mAnimalGuid}")
        self.update_animal_picture()

    def update_animal_picture(self):
        """Update the animal picture based on the selected animal in the parameter."""
        animalGuid = str(self.mAnimalParameter._mAnimalGuid)
        if not animalGuid:
            self.lblAnimalPic.clear()
            return
            
        animals_map = LaUtils.getAvailableAnimals()
        LaUtils.debug.log(f"update_animal_picture: Found {len(animals_map)} animals")
        
        for guid, animal in animals_map.items():
            # Convert guid to string
            guid_str = str(guid)
            if callable(getattr(animal, 'guid', None)):
                try:
                    guid_str = animal.guid()
                except:
                    guid_str = str(guid)
            
            LaUtils.debug.log(f"update_animal_picture: Available animal - GUID: {guid_str}, Name: {animal.name}")
            
            # Compare to find match
            if guid_str == animalGuid or animalGuid in guid_str:
                # Get image file
                if hasattr(animal, 'imageFile'):
                    image_file = animal.imageFile
                    if callable(image_file):
                        image_file = image_file()
                        
                    if image_file:
                        # Try to resolve path 
                        image_path = LaUtils.resolveImagePath(image_file)
                        if os.path.exists(image_path):
                            pixmap = QPixmap(image_path)
                            if not pixmap.isNull():
                                self.lblAnimalPic.setPixmap(pixmap)
                                self.lblAnimalPic.setScaledContents(True)
                                return
        
        # If we get here, no image was found
        LaUtils.debug.log("update_animal_picture: No valid image found, clearing picture label")
        self.lblAnimalPic.clear()
        
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
        LaUtils.debug.log(f"setComboToDefault: Looking for {default} in combo with {combo.count()} items")

        # We need to extract the raw GUID string value from potential method
        default_guid_str = str(default)

        for i in range(combo.count()):
            item = combo.itemData(i)

            # Extract the GUID string from the combo box item
            item_guid_str = ""
            if hasattr(item, 'guid'):
                if callable(item.guid):
                    try:
                        # Call the guid method to get actual GUID string
                        item_guid_str = item.guid()
                    except:
                        item_guid_str = str(item.guid)
                else:
                    item_guid_str = str(item.guid)
            else:
                item_guid_str = str(item)

            LaUtils.debug.log(f"setComboToDefault: Item {i}: '{combo.itemText(i)}' has GUID '{item_guid_str}'")

            # Now compare actual string values
            if default_guid_str == item_guid_str or default_guid_str in item_guid_str:
                LaUtils.debug.log(f"setComboToDefault: Found match at index {i}")
                combo.setCurrentIndex(i)
                return True

        LaUtils.debug.log(f"setComboToDefault: No match found for '{default_guid_str}'")
        return False

    def closeEvent(self, event):
        """Handle window close event."""
        self.writeSettings()
        super().closeEvent(event)

    def on_cboAnimal_changed(self, index):
        """Handle animal combo box change event."""
        if index < 0:
            return
        
        # Get the selected animal GUID as a string
        selected_guid = str(self.cboAnimal.currentData())
        LaUtils.debug.log(f"on_cboAnimal_changed: Selected animal GUID: {selected_guid}")
        
        # Update the animal parameter with this GUID
        if hasattr(self, 'mAnimalParameter'):
            self.mAnimalParameter._mAnimalGuid = selected_guid
        
        # Find the animal object matching this GUID
        animals_map = LaUtils.getAvailableAnimals()
        for guid, animal in animals_map.items():
            guid_str = str(guid)
            
            # Compare string GUIDs
            if guid_str == selected_guid:
                LaUtils.debug.log(f"on_cboAnimal_changed: Found matching animal: {animal.name}")
                
                # Get image file from animal object
                if hasattr(animal, 'imageFile') and animal.imageFile:
                    image_file = str(animal.imageFile)
                    LaUtils.debug.log(f"on_cboAnimal_changed: Animal has image file: {image_file}")
                    
                    # First try to use LaUtils.resolveImagePath
                    image_path = LaUtils.resolveImagePath(image_file)
                    
                    # If not found, try direct path to images directory 
                    if not image_path or not os.path.exists(image_path):
                        image_path = os.path.join(os.path.expanduser("~"), ".landuseAnalyst", "images", image_file)
                        LaUtils.debug.log(f"on_cboAnimal_changed: Trying direct path: {image_path}")
                    
                    # Check if file exists
                    if os.path.exists(image_path):
                        LaUtils.debug.log(f"on_cboAnimal_changed: Found image at: {image_path}")
                        
                        pixmap = QPixmap(image_path)
                        if not pixmap.isNull():
                            LaUtils.debug.log(f"on_cboAnimal_changed: Successfully loaded pixmap")
                            # Make label visible and set properties
                            self.lblAnimalPic.setVisible(True)
                            self.lblAnimalPic.setMinimumSize(100, 100)
                            self.lblAnimalPic.setScaledContents(True)
                            self.lblAnimalPic.setPixmap(pixmap)
                            return
                        else:
                            LaUtils.debug.log(f"on_cboAnimal_changed: Failed to load pixmap from {image_path}")
                    else:
                        LaUtils.debug.log(f"on_cboAnimal_changed: Image file not found: {image_path}")
                else:
                    LaUtils.debug.log(f"on_cboAnimal_changed: Animal has no image file")
        
        # If we get here, no image was found
        LaUtils.debug.log("on_cboAnimal_changed: No valid image found, clearing picture label")
        self.lblAnimalPic.clear()