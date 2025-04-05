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
        self.cboAnimal.clear()

        for guid, animal in myAnimalsMap.items():
            # Call the guid method to get the actual GUID string
            if callable(getattr(animal, 'guid', None)):
                guid_str = animal.guid()
            else:
                guid_str = str(guid)

            myName = animal.name
            LaUtils.debug.log(f"setupAnimalsCombo: Adding animal {myName} with actual GUID {guid_str}")

            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            # Store the actual GUID string as the item data
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

        # Store both display text and actual Priority enum value
        self.cbFallowUsage.addItem("HIGH Fallow Priority", Priority.High)
        self.cbFallowUsage.addItem("MED Fallow Priority", Priority.Medium)
        self.cbFallowUsage.addItem("LOW Fallow Priority", Priority.Low)
        self.cbFallowUsage.addItem("Do Not Graze Fallow", Priority.None_)

        LaUtils.debug.log("setupFallowComboBox: Initialized fallow priority combo box")

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
        LaUtils.debug.log(f"showAnimalParameter: Displaying animal parameter: {self.mAnimalParameter.mName}")
        
        # Set basic parameters
        self.leName.setText(str(self.mAnimalParameter.mName))
        self.leDescription.setText(str(self.mAnimalParameter.mDescription))
        self.sbPercentTameMeat.setValue(float(self.mAnimalParameter.mPercentTameMeat))
        self.checkBoxCommonRaster.setChecked(bool(self.mAnimalParameter.mUseCommonGrazingLand))
        self.checkBoxSpecificRaster.setChecked(bool(self.mAnimalParameter.mUseSpecificGrazingLand))
        
        # Set fodder use group box checked state
        self.grpFodderUse.setChecked(bool(self.mAnimalParameter.mFodderUse))
        LaUtils.debug.log(f"showAnimalParameter: Set fodder use to: {self.mAnimalParameter.mFodderUse}")
        
        # Match animal in combo box
        found_match = False
        if self.mAnimalParameter.mAnimalGuid:
            for i in range(self.cboAnimal.count()):
                item_data = str(self.cboAnimal.itemData(i))
                if self.mAnimalParameter.mAnimalGuid in item_data:
                    self.cboAnimal.setCurrentIndex(i)
                    found_match = True
                    break
                    
        if not found_match:
            self.setComboToDefault(self.cboAnimal, self.mAnimalParameter.mAnimalGuid)
            
        # Set energy type
        current_energy_type = self.mAnimalParameter.mSpecificLandEnergyType
        for i in range(self.cbSpecificLandEnergyType.count()):
            if self.cbSpecificLandEnergyType.itemText(i) == current_energy_type.name:
                self.cbSpecificLandEnergyType.setCurrentIndex(i)
                break
                
        # Set fallow usage
        current_fallow = self.mAnimalParameter.mFallowUsage
        for i in range(self.cbFallowUsage.count()):
            combo_priority = self.cbFallowUsage.itemData(i)
            if combo_priority == current_fallow:
                self.cbFallowUsage.setCurrentIndex(i)
                break
                
        # Update the fodder table AFTER setting fodder use state
        self.refreshFodderTable()
        
        # Update animal picture
        self.update_animal_picture()

    def update_animal_picture(self):
        """Update the animal picture based on the selected animal in the parameter."""
        animalGuid = str(self.mAnimalParameter.mAnimalGuid)
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
            # Ensure animalGuid is a string for comparison
            target_guid_str = str(animalGuid) if animalGuid is not None else None
            if target_guid_str and (guid_str == target_guid_str or target_guid_str in guid_str):
                # Get image file
                if hasattr(animal, 'imageFile'):
                    image_file = animal.imageFile
                    # No need to call image_file() again here, it's handled if callable below
                    # if callable(image_file):
                    #     image_file = image_file()

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
        myAnimalParameter.mName = myTempName
        myTempDescription = f"Copy of {myAnimalParameter.description}"
        myAnimalParameter.mDescription = myTempDescription

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
        self.mAnimalParameter.mName = self.leName.text()
        self.mAnimalParameter.mDescription = self.leDescription.text()
        self.mAnimalParameter.mAnimalGuid = self.cboAnimal.currentData()
        self.mAnimalParameter.mPercentTameMeat = self.sbPercentTameMeat.value()
        self.mAnimalParameter.mUseCommonGrazingLand = self.checkBoxCommonRaster.isChecked()
        self.mAnimalParameter.mUseSpecificGrazingLand = self.checkBoxSpecificRaster.isChecked()
        self.mAnimalParameter.mValueSpecificGrazingLand = self.sbSpecificRasterValue.value()

        # Set fodder use from group box checked state
        self.mAnimalParameter.mFodderUse = bool(self.grpFodderUse.isChecked())

        # Save fodder data from the table
        if self.grpFodderUse.isChecked():
            from la.lib.lafoodsource import LaFoodSource
            myFoodSourceMap = {}

            # Loop through all rows in the fodder table
            for myCurrentRow in range(self.tblFodder.rowCount()):
                mypNameWidget = self.tblFodder.item(myCurrentRow, 0)
                if not mypNameWidget or mypNameWidget.checkState() != Qt.Checked:
                    continue

                # Get the crop GUID
                myGuid = mypNameWidget.data(Qt.UserRole)
                if not myGuid:
                    continue

                # Get the spin box values
                mypFodderSpinBox = self.tblFodder.cellWidget(myCurrentRow, 1)
                mypGrainSpinBox = self.tblFodder.cellWidget(myCurrentRow, 2)
                mypDaysSpinBox = self.tblFodder.cellWidget(myCurrentRow, 3)

                # Create a new food source
                myFoodSource = LaFoodSource()
                myFoodSource.used = True
                myFoodSource.fodder = mypFodderSpinBox.value()
                myFoodSource.grain = mypGrainSpinBox.value()
                myFoodSource.days = mypDaysSpinBox.value()

                # Add to the map
                myFoodSourceMap[myGuid] = myFoodSource

            # Save the food source map to the animal parameter
            self.mAnimalParameter.mFoodSourceMap = myFoodSourceMap
            LaUtils.debug.log(f"on_pbnApply_clicked: Saved {len(myFoodSourceMap)} fodder crops")

        # Set energy type and area units by assigning to private attributes
        self.mAnimalParameter.mAreaUnits = AreaUnits.Dunum if self.cbAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare

        # Set specific land energy type by assigning to private attribute
        mySelectedEnergyTypeText = self.cbSpecificLandEnergyType.currentText() # Renamed variable
        try:
            self.mAnimalParameter.mSpecificLandEnergyType = EnergyType[mySelectedEnergyTypeText]
            LaUtils.debug.log(f"on_pbnApply_clicked: Set _specificLandEnergyType to {mySelectedEnergyTypeText}")
        except KeyError:
            LaUtils.debug.log(f"on_pbnApply_clicked: Invalid energy type selected: {mySelectedEnergyTypeText}, defaulting to KCalories")
            self.mAnimalParameter.mSpecificLandEnergyType = EnergyType.KCalories

        # Save raster name by assigning to private attribute
        self.mAnimalParameter.mRrasterName = self.cboRaster.currentText()
        
        # Set fallow usage based on combo box data by assigning to private attribute
        index = self.cbFallowUsage.currentIndex()
        if index >= 0:
            self.mAnimalParameter.mFallowUsage = self.cbFallowUsage.itemData(index)

        # Save parameter to file
        filepath = os.path.join(LaUtils.userAnimalParameterProfilesDirPath(),
                              f"{self.mAnimalParameter.guid}.xml")
        self.mAnimalParameter.toXmlFile(filepath)
        LaUtils.debug.log(f"on_pbnApply_clicked: Saved animal parameter to {filepath}")

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
        """Refresh the fodder table with values from the selected animal parameter."""
        LaUtils.debug.log("refreshFodderTable: Updating fodder table for animal parameter")

        # Get the food source map from the current animal parameter
        myFoodSourceMap = self.mAnimalParameter.fodderSourceMap()

        # Update each row in the fodder table
        for myCurrentRow in range(self.tblFodder.rowCount()):
            # Get item and guid
            mypItem = self.tblFodder.item(myCurrentRow, 0)
            if not mypItem:
                continue

            myGuid = mypItem.data(Qt.UserRole)
            LaUtils.debug.log(f"refreshFodderTable: Processing crop with GUID: {myGuid}")

            # Get the spin box widgets
            mypFodderSpinBox = self.tblFodder.cellWidget(myCurrentRow, 1)
            mypGrainSpinBox = self.tblFodder.cellWidget(myCurrentRow, 2)
            mypDaysSpinBox = self.tblFodder.cellWidget(myCurrentRow, 3)

            # If this crop is in the food source map, set the values
            if myGuid in myFoodSourceMap:
                myFoodSource = myFoodSourceMap[myGuid]
                LaUtils.debug.log(f"refreshFodderTable: Found in food sources: fodder={myFoodSource.fodder}, grain={myFoodSource.grain}, days={myFoodSource.days}")

                mypFodderSpinBox.setValue(myFoodSource.fodder)
                mypGrainSpinBox.setValue(myFoodSource.grain)
                mypDaysSpinBox.setValue(myFoodSource.days)

                # Mark as checked
                mypItem.setCheckState(Qt.Checked)
            else:
                # Reset values to 0
                mypFodderSpinBox.setValue(0)
                mypGrainSpinBox.setValue(0)
                mypDaysSpinBox.setValue(0)

                # Mark as unchecked
                mypItem.setCheckState(Qt.Unchecked)

    def populateFodder(self):
        """Populate the fodder table with available crops."""
        from la.lib.lacrop import LaCrop

        LaUtils.debug.log("populateFodder: Setting up fodder table")

        # Clear the table
        self.tblFodder.clear()
        self.tblFodder.setRowCount(0)
        self.tblFodder.setColumnCount(4)

        # Set column headers
        self.tblFodder.setHorizontalHeaderLabels(["Crop", "Straw/Chaff", "Grain", "Days"])

        myCurrentRow = 0
        myCropsMap = LaUtils.getAvailableCrops()
        LaUtils.debug.log(f"populateFodder: Found {len(myCropsMap)} available crops")
        myCrop: LaCrop = LaCrop()
        for myGuid, myCrop in myCropsMap.items():
            # Insert a new row
            self.tblFodder.insertRow(myCurrentRow)

            # Create item for crop name with checkbox
            mypNameItem = QTableWidgetItem(myCrop.name)
            mypNameItem.setData(Qt.UserRole, myGuid)  # Store guid for reference

            # Set appropriate icon based on selection status
            if hasattr(self, 'mSelectedCropsMap') and myGuid in self.mSelectedCropsMap:
                pair = self.mSelectedCropsMap.get(myGuid)
                if pair and pair[0]:
                    mypNameItem.setIcon(QIcon(":/status_ok.png"))
                else:
                    mypNameItem.setIcon(QIcon(":/status_error.png"))
            else:
                mypNameItem.setIcon(QIcon(":/status_error.png"))

            mypNameItem.setCheckState(Qt.Unchecked)
            self.tblFodder.setItem(myCurrentRow, 0, mypNameItem)

            # Create spin boxes for fodder, grain, and days values
            mypSpinFodder = QSpinBox(self)
            mypSpinGrain = QSpinBox(self)
            mypSpinDays = QSpinBox(self)

            # Set maximum values
            mypSpinFodder.setMaximum(10000)
            mypSpinGrain.setMaximum(10000)
            mypSpinDays.setMaximum(365)

            # Set default values
            mypSpinFodder.setValue(0)
            mypSpinGrain.setValue(0)
            mypSpinDays.setValue(0)

            # Add spin boxes to table
            self.tblFodder.setCellWidget(myCurrentRow, 1, mypSpinFodder)
            self.tblFodder.setCellWidget(myCurrentRow, 2, mypSpinGrain)
            self.tblFodder.setCellWidget(myCurrentRow, 3, mypSpinDays)

            # Increment row counter
            myCurrentRow += 1

        LaUtils.debug.log(f"populateFodder: Populated {myCurrentRow} crops in fodder table")

    def setComboToDefault(self, combo, default_guid):
        """Set a combo box to a default value based on GUID."""
        if not default_guid:
            return False

        LaUtils.debug.log(f"setComboToDefault: Looking for GUID {default_guid} in combo with {combo.count()} items")

        # Convert default_guid to string if it isn't already
        default_guid_str = str(default_guid)

        for i in range(combo.count()):
            # Get the stored GUID string from the combo box item data
            item_guid = combo.itemData(i)
            LaUtils.debug.log(f"setComboToDefault: Comparing '{default_guid_str}' with combo item {i} GUID: '{item_guid}'")

            if item_guid == default_guid_str:
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
            self.mAnimalParameter.mAnimalGuid = selected_guid

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

    def on_pbnMore_clicked(self):
        """Handle the 'More' button click to launch the Assemblage Conversion Utility dialog."""
        from la.gui.laassemblageconversion import LaAssemblageConversion

        # Create and show the Assemblage Conversion Utility dialog
        assemblage_conversion_dialog = LaAssemblageConversion(self)
        assemblage_conversion_dialog.exec_()