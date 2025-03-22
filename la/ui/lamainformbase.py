# -*- coding: utf-8 -*-
"""
LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
of a settlement (with respect to required land needed for food production).
Land area targets for each food source supplied to the model are calculated based
on a multitude of demographic and dietary inputs.

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

# region imports
from qgis.PyQt.QtWidgets import QListWidgetItem, QTableWidgetItem, QComboBox
from qgis.PyQt import uic
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFile, QSettings
from qgis.PyQt.QtCore import QTextStream
from qgis.PyQt.QtGui import QIcon

import os

from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils

from la.ui.lacropmanagerbase import LaCropManagerBase
from la.ui.lacropparametermanagerbase import LaCropParameterManagerBase
from la.ui.laanimalmanagerbase import LaAnimalManagerBase
from la.ui.laanimalparameterbase import LaAnimalParameterBase

# Add imports for implementation classes
from la.gui.lacropmanager import LaCropManager
from la.gui.lacropparametermanager import LaCropParameterManager
from la.gui.laanimalmanager import LaAnimalManager
from la.gui.laanimalparametermanager import LaAnimalParameterManager

# Make sure we have the proper imports at the top
from qgis.PyQt import QtWidgets, QtCore, QtGui
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFile, QTextStream
from qgis.PyQt.QtGui import QIcon, QPixmap

# endregion

# This loads your .ui file so that PyQt can
# populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(
                    os.path.join(
                        os.path.dirname(__file__),
                        'lamainformbase.ui'))


class LaMainFormBase(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor for LaMainFormBase (.ui file)"""
        super(LaMainFormBase, self).__init__(parent)
        self.setupUi(self)

        # Initialize maps
        self.mAnimalsMap = {}
        self.mCropsMap = {}
        self.mCropParametersMap = {}
        self.mAnimalParametersMap = {}

        # make the form's buttons work
        self.connectSignalsSlots()

        # set labels that for pix to scaled so images display properly
        # region INIT_PIXMAP_SCALING
        self.lblCropPix.setScaledContents(True)
        self.lblAnimalPix.setScaledContents(True)
        self.lblCropPicCalcs.setScaledContents(True)
        self.lblAnimalPicCalcs.setScaledContents(True)
        #endregion

        # region PREPARE FORM DISPLAY PANELS
        self.tblAnimals.horizontalHeader().hide()
        self.tblAnimals.verticalHeader().hide()
        self.tblAnimals.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tblCrops.horizontalHeader().hide()
        self.tblCrops.verticalHeader().hide()
        self.tblCrops.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.listWidgetCalculationsAnimal.clear()
        # endregion

        # region LOAD CROPS AND ANIMALS
        self.loadAnimals()
        self.loadCrops()
        # endregion

        # region COMBO BOX ITEMS LOADED
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.cbCommonLandEnergyType.addItem("KCalories")
        self.cbCommonLandEnergyType.addItem("TDN")
        # endregion

        # region DIET SLIDERS CONNECTED
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)
        # endregion

        # connect the change in tree to it's def
        self.treeHelp.currentItemChanged.connect(self.current_item_changed)

        # Connect signals to slots
        self.treeHelp.currentItemChanged.connect(self.helpItemClicked)
        self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)
        self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)
        self.pushButtonExit.clicked.connect(QtWidgets.qApp.quit)
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)
        self.tblAnimals.cellChanged.connect(self.animalCalcSelectionChanged)
        self.tblCrops.cellClicked.connect(self.cropCellClicked)
        self.tblCrops.cellChanged.connect(self.cropCalcSelectionChanged)
        self.cbDebug.clicked.connect(self.on_cbDebug_clicked)

    # read/load/display help file corresponding to selected item in helpTree
    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, QtWidgets.QTreeWidgetItem)
    def current_item_changed(self, theCurrentItem, thePreviousItem):
        LaUtils.debug.log(f"Item clicked in help browser: {theCurrentItem.text(0)}", "Help")
        myQFile = QFile(":/" + theCurrentItem.text(0) + ".html")
        myQFile.open(QFile.ReadOnly | QFile.Text)
        istream = QTextStream(myQFile)
        self.textHelp.setHtml(istream.readAll())
        myQFile.close()

    def on_clicked_pbnNewCrop(self):
        LaUtils.debug.log("Manage Crops button clicked", "UI")
        myCropsMap = self.mCropsMap  # Pass the crops map
        myCropManager = LaCropManager(myCropsMap, self)  # Pass parent if needed
        myCropManager.exec_()  # Use exec_ to show the dialog modally

    def on_clicked_pbnNewCropParameter(self):
        LaUtils.debug.log("Manage Crop Parameters button clicked", "UI")
        myCropParametersMap = self.mCropParametersMap  # Pass the crops map
        myCropParameterManager = LaCropParameterManager(self)  # Pass parent if needed
        myCropParameterManager.exec_()  # Use exec_ to show the dialog modally

    def on_clicked_pbnNewAnimal(self):
        LaUtils.debug.log("Manage Animals button clicked", "UI")
        myAnimalManager = LaAnimalManager(parent=self)  # Remove the empty dict and just pass parent
        myAnimalManager.exec_()  # Use exec_ to show the dialog modally

    def on_clicked_pbnNewAnimalParameter(self):
        LaUtils.debug.log("Manage Animal Parameters button clicked", "UI")
        myAnimalParameterManager = LaAnimalParameterManager(self)  # Pass parent if needed
        myAnimalParameterManager.exec_()  # Use exec_ to show the dialog modally

    def on_sliderDiet_valueChanged(self, theValue):
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelMeatPercent.setText(myMinString)
        self.labelCropPercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def on_sliderMeat_valueChanged(self, theValue):
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelMeatWildPercent.setText(myMinString)
        self.labelMeatTamePercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def on_sliderCrop_valueChanged(self, theValue):
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelCropWildPercent.setText(myMinString)
        self.labelCropTamePercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def setDietLabels(self):
        """Update the diet labels based on slider values.
        This recalculates percentages for the diet breakdown display.
        """
        try:
            # Get current slider values
            plantAnimalRatio = self.sliderDiet.value()  # Plant % vs Animal %
            wildTameAnimalRatio = self.sliderMeat.value()  # Wild % vs Tame % for animal portion
            wildTamePlantRatio = self.sliderCrop.value()  # Wild % vs Tame % for plant portion

            # Calculate percentages
            animalPercent = plantAnimalRatio
            plantPercent = 100 - plantAnimalRatio

            # Animal breakdown
            wildAnimalPercent = wildTameAnimalRatio
            tameAnimalPercent = 100 - wildTameAnimalRatio
            
            # Plant breakdown
            wildPlantPercent = wildTamePlantRatio
            tamePlantPercent = 100 - wildTamePlantRatio
            
            # Calculate absolute percentages (of total diet)
            absoluteWildAnimalPercent = (animalPercent * wildAnimalPercent) / 100
            absoluteTameAnimalPercent = (animalPercent * tameAnimalPercent) / 100
            absoluteWildPlantPercent = (plantPercent * wildPlantPercent) / 100
            absoluteTamePlantPercent = (plantPercent * tamePlantPercent) / 100
            
            # Update the main percentage labels which we know exist
            self.labelMeatPercent.setText(str(animalPercent))
            self.labelCropPercent.setText(str(plantPercent))
            self.labelMeatWildPercent.setText(str(wildAnimalPercent))
            self.labelMeatTamePercent.setText(str(tameAnimalPercent))
            self.labelCropWildPercent.setText(str(wildPlantPercent))
            self.labelCropTamePercent.setText(str(tamePlantPercent))
            
            # Try to update additional percentage breakdown labels if they exist
            # Use hasattr to safely check if the attribute exists before trying to access it
            label_map = {
                'labelWildMeatPercentage': f"{absoluteWildAnimalPercent:.1f}%",
                'labelTameMeatPercentage': f"{absoluteTameAnimalPercent:.1f}%",
                'labelWildCropsPercentage': f"{absoluteWildPlantPercent:.1f}%",
                'labelTameCropsPercentage': f"{absoluteTamePlantPercent:.1f}%"
            }
            
            for label_name, value in label_map.items():
                if hasattr(self, label_name):
                    getattr(self, label_name).setText(value)
                else:
                    # Optional: Create a debug message
                    LaUtils.debug.log(f"Note: Label '{label_name}' not found in the UI", "UI")
            
            # Update the model if needed
            if hasattr(self, 'model'):
                self.model.setPlantAnimalRatio(plantAnimalRatio)
                self.model.setWildTameAnimalRatio(wildTameAnimalRatio)
                self.model.setWildTamePlantRatio(wildTamePlantRatio)
            
            # Also update any visualization or graph that depends on these values
            if hasattr(self, 'updateDietPieChart'):
                self.updateDietPieChart()
                
            LaUtils.debug.log("Diet labels updated", "Diet")
            # Show the calculated percentages in the report for debugging
            LaUtils.debug.log(f"Animal: {animalPercent}%, Plant: {plantPercent}%", "Diet")
            LaUtils.debug.log(f"Wild Animal: {absoluteWildAnimalPercent:.1f}%, Tame Animal: {absoluteTameAnimalPercent:.1f}%", "Diet")
            LaUtils.debug.log(f"Wild Plant: {absoluteWildPlantPercent:.1f}%, Tame Plant: {absoluteTamePlantPercent:.1f}%", "Diet")
            
        except Exception as e:
            LaUtils.debug.log(f"Error updating diet labels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def setModel(self, *args):
        from la.lib.la import AreaUnits
        self.mSelectedCropsMap.clear()
        self.mSelectedAnimalsMap.clear()
        mySelectedAreaUnit = AreaUnits(self.cbAreaUnits.currentText())
        myCommonRasterValue = int(self.sbCommonRasterValue.value())
        myAreaUnits = 'Dunum' if mySelectedAreaUnit else 'Hectare'
        print(mySelectedAreaUnit, myAreaUnits, myCommonRasterValue)

    def loadAnimals(self):
        self.listWidgetCalculationsAnimal.clear()
        myModel = LaModel()
        self.tblAnimals.clear()
        self.tblAnimals.setRowCount(0)
        self.tblAnimals.setColumnCount(4)
        
        myCurrentRow = 0
        myRunningPercentage = 0.0
        
        # Get available animals and parameters
        myAnimalsMap = LaUtils.getAvailableAnimals()
        myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()
        
        for myGuid, myAnimal in myAnimalsMap.items():
            # Get the actual GUID string
            if hasattr(myGuid, '__call__'):
                myGuid = myGuid()
            
            myName = myAnimal.name
            myValue = self.mAnimalsMap.get(myGuid, (False, ""))
            
            if myGuid not in self.mAnimalsMap:
                self.mAnimalsMap[myGuid] = myValue
                
            myIcon = QIcon(":/localdata.png")
            self.tblAnimals.insertRow(myCurrentRow)
            
            # Add used checkbox
            mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
            if myValue[0]:
                mypUsedItem.setCheckState(QtCore.Qt.Checked)
                myItem = QListWidgetItem(str(myAnimal.name))
                # Store the actual GUID string
                myItem.setData(QtCore.Qt.UserRole, str(myGuid))
                self.listWidgetCalculationsAnimal.addItem(myItem)
            else:
                mypUsedItem.setCheckState(QtCore.Qt.Unchecked)
                myItem = QListWidgetItem(str(myAnimal.name))
                myItem.setData(QtCore.Qt.UserRole, str(myGuid))
                self.listWidgetCalculationsAnimal.takeItem(self.listWidgetCalculationsAnimal.row(myItem))
                
            self.tblAnimals.setItem(myCurrentRow, 0, mypUsedItem)
            
            # Add name with GUID
            mypNameItem = QTableWidgetItem(str(myAnimal.name))
            # Store the actual GUID string
            mypNameItem.setData(QtCore.Qt.UserRole, str(myGuid))
            self.tblAnimals.setItem(myCurrentRow, 1, mypNameItem)
            mypNameItem.setIcon(myIcon)
            
            # Add parameters combo
            mypCombo = QComboBox(self)
            for myParameterGuid, myAnimalParameter in myAnimalParametersMap.items():
                if hasattr(myAnimalParameter.animalGuid, '__call__'):
                    paramAnimalGuid = myAnimalParameter.animalGuid()
                else:
                    paramAnimalGuid = myAnimalParameter.animalGuid
                    
                if str(myGuid) != str(paramAnimalGuid):
                    continue
                    
                myParameterName = f"{myAnimalParameter.name}  ({myAnimalParameter.description})"
                
                if not myValue[1]:
                    myValue = (myValue[0], str(myParameterGuid))
                    
                if str(myValue[1]) == str(myAnimalParameter.guid):
                    if myValue[0]:
                        myRunningPercentage += float(str(myAnimalParameter.percentTameMeat))
                    mypPercentItem = QtWidgets.QTableWidgetItem(str(myAnimalParameter.percentTameMeat))
                    self.tblAnimals.setItem(myCurrentRow, 3, mypPercentItem)
                    
                # Store the actual GUID string    
                mypCombo.addItem(myIcon, myParameterName, str(myParameterGuid))
                
            self.setComboToDefault(mypCombo, myValue[1])
            self.mAnimalsMap[str(myGuid)] = myValue
            self.tblAnimals.setCellWidget(myCurrentRow, 2, mypCombo)
            myCurrentRow += 1
            
        # Set status icon based on total percentage
        myIcon = QIcon(":/status_ok.png") if myRunningPercentage == 100 else QIcon(":/status_error.png")
        myPercentItem = str(myRunningPercentage)
        self.labelAnimalCheck.setText(f"{myPercentItem}%")

    def loadCrops(self):
        """Load crops into the table widget."""
        try:
            # Clear the lists first
            if hasattr(self, 'listWidgetCalculationsCrop'):
                self.listWidgetCalculationsCrop.clear()
            
            # Clear and setup the table if it exists
            if not hasattr(self, 'tblCrops') or self.tblCrops is None:
                LaUtils.debug.log("Cannot load crops: table widget not found", "Error")
                return
                
            self.tblCrops.clear()
            self.tblCrops.setRowCount(0)
            self.tblCrops.setColumnCount(4)
            
            # Initialize tracking variables
            myCurrentRow = 0
            myRunningPercentage = 0.0
            
            # Get available crops and parameters
            try:
                myCropsMap = LaUtils.getAvailableCrops()
                if not myCropsMap:
                    LaUtils.debug.log("No crops available to load", "Warning")
                    return
            except Exception as e:
                LaUtils.debug.log(f"Error getting available crops: {str(e)}", "Error")
                return
                
            try:
                myCropParametersMap = LaUtils.getAvailableCropParameters()
                if not myCropParametersMap:
                    LaUtils.debug.log("No crop parameters available", "Warning")
                    return
            except Exception as e:
                LaUtils.debug.log(f"Error getting crop parameters: {str(e)}", "Error")
                return
            
            # Initialize crops map if needed
            if not hasattr(self, 'mCropsMap'):
                self.mCropsMap = {}
                
            # Process each crop
            for myGuid, myCrop in myCropsMap.items():
                if myCrop is None or not hasattr(myCrop, 'name'):
                    LaUtils.debug.log(f"Invalid crop data for GUID: {myGuid}", "Warning")
                    continue
                    
                myName = myCrop.name
                myValue = self.mCropsMap.get(myGuid, (False, ""))
                
                # Update crops map
                if myGuid not in self.mCropsMap:
                    self.mCropsMap[myGuid] = myValue
                    
                # Create table row
                myIcon = QIcon(":/localdata.png")
                self.tblCrops.insertRow(myCurrentRow)
                
                # Used checkbox column
                mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
                mypUsedItem.setCheckState(QtCore.Qt.Checked if myValue[0] else QtCore.Qt.Unchecked)
                self.tblCrops.setItem(myCurrentRow, 0, mypUsedItem)
                
                # If checked, ensure it's in calculations list
                if myValue[0]:
                    try:
                        self.addCropToCalculationsList(myGuid)
                    except Exception as e:
                        LaUtils.debug.log(f"Error adding crop to calculations: {str(e)}", "Error")
                
                # Name column with GUID data
                mypNameItem = QtWidgets.QTableWidgetItem(myName)
                mypNameItem.setData(QtCore.Qt.UserRole, myGuid)
                self.tblCrops.setItem(myCurrentRow, 1, mypNameItem)
                mypNameItem.setIcon(myIcon)
                
                # Parameters combo box
                mypCombo = QtWidgets.QComboBox(self)
                
                # Add parameters to combo
                for myParameterGuid, myCropParameter in myCropParametersMap.items():
                    if myCropParameter is None:
                        continue
                        
                    if not hasattr(myCropParameter, 'cropGuid') or myCropParameter.cropGuid != myGuid:
                        continue
                        
                    # Format parameter name
                    myParameterName = f"{myCropParameter.name}  ({myCropParameter.description})"
                    
                    # Update value if needed
                    if not myValue[1]:
                        myValue = (myValue[0], myParameterGuid)
                        
                    # Update percentage if this is the selected parameter
                    if myValue[1] == myCropParameter.guid:
                        if myValue[0] and hasattr(myCropParameter, 'percentTameCrop'):
                            try:
                                myRunningPercentage += float(myCropParameter.percentTameCrop)
                            except (ValueError, TypeError):
                                LaUtils.debug.log(f"Invalid percentTameCrop for parameter {myParameterGuid}", "Warning")
                                
                        # Add percentage column
                        if hasattr(myCropParameter, 'percentTameCrop'):
                            mypPercentItem = QtWidgets.QTableWidgetItem(str(myCropParameter.percentTameCrop))
                            self.tblCrops.setItem(myCurrentRow, 3, mypPercentItem)
                            
                    # Add to combo box
                    mypCombo.addItem(myIcon, myParameterName, myParameterGuid)
                
                # Set default combo selection and add to table
                self.setComboToDefault(mypCombo, myValue[1])
                self.mCropsMap[myGuid] = myValue
                self.tblCrops.setCellWidget(myCurrentRow, 2, mypCombo)
                
                myCurrentRow += 1
            
            # Update total percentage display
            if hasattr(self, 'labelCropCheck'):
                self.labelCropCheck.setText(f"{myRunningPercentage:.1f}%")
                
            # Update status icon
            if hasattr(self, 'labelCropIcon'):
                iconPath = ":/status_ok.png" if abs(myRunningPercentage - 100.0) < 0.1 else ":/status_error.png"
                self.labelCropIcon.setPixmap(QIcon(iconPath).pixmap(16, 16))
                
            LaUtils.debug.log(f"Loaded {myCurrentRow} crops with total percentage {myRunningPercentage:.1f}%", "Crops")
            
        except Exception as e:
            LaUtils.debug.log(f"Error loading crops: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def setComboToDefault(self, combo, default):
        index = combo.findData(default)
        if index >= 0:
            combo.setCurrentIndex(index)

    def helpItemClicked(self, current, previous):
        """Handle help item click event.

        This method is called when a user clicks on an item in the help tree.
        It displays the corresponding help content in the help text browser.

        Args:
            current: The currently selected QTreeWidgetItem
            previous: The previously selected QTreeWidgetItem
        """
        if current is None:
            return

        # The item text is the name of the help file
        helpFileName = current.text(0)
        LaUtils.debug.log(f"Help item clicked: {helpFileName}", "Help")


        # Load the help file content
        try:
            helpFilePath = f":/{helpFileName}.html"
            myQFile = QFile(helpFilePath)
            if myQFile.open(QFile.ReadOnly | QFile.Text):
                istream = QTextStream(myQFile)
                self.textHelp.setHtml(istream.readAll())
                myQFile.close()
            else:
                self.textHelp.setHtml(f"<p>Could not open help file: {helpFilePath}</p>")
        except Exception as e:
            self.textHelp.setHtml(f"<p>Error loading help: {str(e)}</p>")
            LaUtils.debug.log(f"Error loading help file: {str(e)}", "Error")

    def cropCalcClicked(self, current, previous):
        """Handle crop calculation item click event.

        This method is called when a user clicks on a crop in the calculations list.
        It displays the crop details in the crop details panel.

        Args:
            current: The currently selected QListWidgetItem
            previous: The previously selected QListWidgetItem
        """
        if current is None:
            return

        # Get the crop GUID from the item's user role data
        cropGuid = current.data(QtCore.Qt.UserRole)
        if not cropGuid:
            return

        LaUtils.debug.log(f"Crop calculation clicked: {current.text()} (GUID: {cropGuid})", "Calculation")

        # Get the crop object
        crop = LaUtils.getCrop(cropGuid)
        if crop is None or crop.name == "":
            LaUtils.debug.log("Could not find crop", "Error")
            return

        # Display crop details in the text browser
        html_content = "<h2>" + crop.name + "</h2>"
        html_content += "<p><strong>Description:</strong> " + crop.description + "</p>"
        html_content += "<p><strong>Calories:</strong> " + str(crop.cropCalories) + "</p>"
        # Add any other crop properties you want to display
        self.textBrowserCropDefinition.setHtml(html_content)

        if hasattr(self, 'lblCropValueCalcs'):
            self.lblCropValueCalcs.setText(f"{crop.cropCalories}")

        # Display crop image if available
        if hasattr(crop, 'imageFile') and crop.imageFile:
            imagePath = LaUtils.resolvePath(crop.imageFile, 'image')
            LaUtils.debug.log(f"Attempting to load crop image for calculation: {imagePath}", "UI")

            if imagePath and os.path.exists(imagePath):
                pixmap = QPixmap(imagePath)
                if not pixmap.isNull():
                    self.lblCropPicCalcs.setPixmap(pixmap)
                    LaUtils.debug.log("Crop calculation image loaded successfully", "UI")
                else:
                    self.lblCropPicCalcs.clear()
                    LaUtils.debug.log(f"Failed to create pixmap for calculation from {imagePath}", "Error")
            else:
                self.lblCropPicCalcs.clear()
                LaUtils.debug.log(f"Calculation image path doesn't exist: {imagePath}", "Warning")
        else:
            self.lblCropPicCalcs.clear()

        # Update any calculations
        self.updateCropCalculations(crop)

    def animalCalcClicked(self, current, previous):
        """Handle animal calculation item click event.

        This method is called when a user clicks on an animal in the calculations list.
        It displays the animal details in the animal details panel.

        Args:
            current: The currently selected QListWidgetItem
            previous: The previously selected QListWidgetItem
        """
        if current is None:
            return

        # Get the animal GUID from the item's user role data
        animalGuid = current.data(QtCore.Qt.UserRole)
        if not animalGuid:
            return

        LaUtils.debug.log(f"Animal calculation clicked: {current.text()} (GUID: {animalGuid})", "Calculation")

        # Get the animal object
        animal = LaUtils.getAnimal(animalGuid)
        if animal is None or animal.name == "":
            LaUtils.debug.log("Could not find animal", "Error")
            return

        # Display animal details - check widget names based on the UI form design
        if hasattr(self, 'leAnimalName'):
            self.leAnimalName.setText(animal.name)
        if hasattr(self, 'leAnimalDescription'):
            self.leAnimalDescription.setText(animal.description)

        # Display animal image if available
        if hasattr(animal, 'imageFile') and animal.imageFile:
            imagePath = LaUtils.resolvePath(str(animal.imageFile), 'image')
            if os.path.exists(imagePath):
                pixmap = QtGui.QPixmap(imagePath)
                if not pixmap.isNull():
                    self.lblAnimalPicCalcs.setPixmap(pixmap)
                else:
                    self.lblAnimalPicCalcs.clear()
            else:
                self.lblAnimalPicCalcs.clear()
        else:
            self.lblAnimalPicCalcs.clear()

        # Update any calculations
        self.updateAnimalCalculations(animal)

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

        # Handle row selection for viewing details
        self.showSelectedAnimalDetails(row)

    def cropCellClicked(self, row, column):
        """Handle crop table cell click event.

        This method is called when a user clicks on a cell in the crops table.
        It handles the selection and display of crop details.

        Args:
            row: The row index of the clicked cell
            column: The column index of the clicked cell
        """
        if column == 0:  # Checkbox column
            item = self.tblCrops.item(row, column)
            guid = self.tblCrops.item(row, 1).data(QtCore.Qt.UserRole)

            # Get the current check state
            isChecked = item.checkState() == QtCore.Qt.Checked

            # Update the crops map
            if guid in self.mCropsMap:
                currentValue = self.mCropsMap[guid]
                self.mCropsMap[guid] = (isChecked, currentValue[1])

                # Update the crop calculations list
                if isChecked:
                    # Add to calculations list if not already there
                    self.addCropToCalculationsList(guid)
                else:
                    # Remove from calculations list
                    self.removeCropFromCalculationsList(guid)
                self.updateTotalPercentages()

        # Handle row selection for viewing details - this shows the crop details
        self.showSelectedCropDetails(row)

    def animalCalcSelectionChanged(self, row, column):
        """Handle changes in animal calculations table.

        This method is called when a selection in the animal calculations table changes.
        It updates the relevant data and UI elements accordingly.

        Args:
            row: The row index of the changed cell
            column: The column index of the changed cell
        """
        # Only process changes in the parameter selection column
        if column != 2:
            return

        try:
            # Get the animal GUID
            animalGuid = self.tblAnimals.item(row, 1).data(QtCore.Qt.UserRole)
            if not animalGuid:
                return

            # Get the selected parameter GUID
            comboBox = self.tblAnimals.cellWidget(row, column)
            if not comboBox:
                return
            parameterGuid = comboBox.currentData()

            # Get the current checked state
            isChecked = self.tblAnimals.item(row, 0).checkState() == QtCore.Qt.Checked

            # Update the animals map
            self.mAnimalsMap[animalGuid] = (isChecked, parameterGuid)

            # Update the percentage display
            myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()
            if parameterGuid in myAnimalParametersMap:
                parameter = myAnimalParametersMap[parameterGuid]
                percentItem = QtWidgets.QTableWidgetItem(str(parameter.percentTameMeat))
                self.tblAnimals.setItem(row, 3, percentItem)
                # Update the total percentages if this animal is checked
                self.updateTotalPercentages()
        except Exception as e:
            LaUtils.debug.log(f"Error in animalCalcSelectionChanged: {str(e)}", "Error")

    def cropCalcSelectionChanged(self, row, column):
        """Handle changes in crop calculations table.

        This method is called when a selection in the crop calculations table changes.
        It updates the relevant data and UI elements accordingly.

        Args:
            row: The row index of the changed cell
            column: The column index of the changed cell
        """
        # Only process changes in the parameter selection column
        if column != 2:
            return

        try:
            # Get the crop GUID
            cropGuid = self.tblCrops.item(row, 1).data(QtCore.Qt.UserRole)
            if not cropGuid:
                return

            # Get the selected parameter GUID
            comboBox = self.tblCrops.cellWidget(row, column)
            if not comboBox:
                return
            parameterGuid = comboBox.currentData()

            # Get the current checked state
            isChecked = self.tblCrops.item(row, 0).checkState() == QtCore.Qt.Checked

            # Update the crops map
            self.mCropsMap[cropGuid] = (isChecked, parameterGuid)

            # Update the percentage display
            myCropParametersMap = LaUtils.getAvailableCropParameters()
            if parameterGuid in myCropParametersMap:
                parameter = myCropParametersMap[parameterGuid]
                percentItem = QtWidgets.QTableWidgetItem(str(parameter.percentTameCrop))
                self.tblCrops.setItem(row, 3, percentItem)
                # Update the total percentages if this crop is checked
                self.updateTotalPercentages()
        except Exception as e:
            LaUtils.debug.log(f"Error in cropCalcSelectionChanged: {str(e)}", "Error")

    def on_cbDebug_clicked(self):
        """Handle debug checkbox clicked - toggle debug mode."""
        isChecked = self.cbDebug.isChecked()
        
        # Update the debug logger first
        LaUtils.debug.set_enabled(isChecked)
        
        try:
            # Import and use our debug dialog
            from la.gui.ladebugdialog import LaDebugDialog
            
            if isChecked:
                # Get dialog instance using proper singleton pattern
                if not hasattr(self, '_debug_dialog') or self._debug_dialog is None:
                    self._debug_dialog = LaDebugDialog.get_instance(parent=self)
                
                # Show the dialog and force it to appear at front
                self._debug_dialog.show()
                self._debug_dialog.raise_()
                self._debug_dialog.activateWindow()
                
                # Test message
                LaUtils.debug.log("Debug dialog opened", "Debug")
            else:
                # Hide the dialog but don't destroy it
                if hasattr(self, '_debug_dialog') and self._debug_dialog is not None:
                    self._debug_dialog.hide()
                    LaUtils.debug.log("Debug dialog hidden", "Debug")
        except Exception as e:
            LaUtils.debug.log(f"Debug dialog error: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
        
        # Keep the original debug UI components hidden
        if hasattr(self, 'tbLogs'):
            self.tbLogs.setVisible(False)
        if hasattr(self, 'tbReport'):
            self.tbReport.setVisible(False)
            
        # Save debug setting
        QSettings().setValue("landuse_analyst/debug", isChecked)

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

    def addAnimalToCalculationsList(self, animalGuid):
        """Add an animal to the calculations list.

        Args:
            animalGuid: The GUID of the animal to add
        """
        # Check if the animal is already in the list
        for i in range(self.listWidgetCalculationsAnimal.count()):
            item = self.listWidgetCalculationsAnimal.item(i)
            if item.data(QtCore.Qt.UserRole) == animalGuid:
                return

        # Add the animal to the list
        animal = LaUtils.getAnimal(animalGuid)
        if animal and animal.name:
            item = QListWidgetItem(str(animal.name))
            item.setData(QtCore.Qt.UserRole, animalGuid)
            self.listWidgetCalculationsAnimal.addItem(item)

    def removeAnimalFromCalculationsList(self, animalGuid):
        """Remove an animal from the calculations list.

        Args:
            animalGuid: The GUID of the animal to remove
        """
        for i in range(self.listWidgetCalculationsAnimal.count()):
            item = self.listWidgetCalculationsAnimal.item(i)
            if item.data(QtCore.Qt.UserRole) == animalGuid:
                self.listWidgetCalculationsAnimal.takeItem(i)
                break

    def addCropToCalculationsList(self, cropGuid):
        """Add a crop to the calculations list.

        Args:
            cropGuid: The GUID of the crop to add
        """
        # Check if the crop is already in the list
        for i in range(self.listWidgetCalculationsCrop.count()):
            item = self.listWidgetCalculationsCrop.item(i)
            if item.data(QtCore.Qt.UserRole) == cropGuid:
                return

        # Add the crop to the list
        crop = LaUtils.getCrop(cropGuid)
        if crop and crop.name:
            item = QtWidgets.QListWidgetItem(crop.name)
            item.setData(QtCore.Qt.UserRole, cropGuid)
            self.listWidgetCalculationsCrop.addItem(item)

    def removeCropFromCalculationsList(self, cropGuid):
        """Remove a crop from the calculations list.

        Args:
            cropGuid: The GUID of the crop to remove
        """
        for i in range(self.listWidgetCalculationsCrop.count()):
            item = self.listWidgetCalculationsCrop.item(i)
            if item.data(QtCore.Qt.UserRole) == cropGuid:
                self.listWidgetCalculationsCrop.takeItem(i)
                break

    def updateTotalPercentages(self):
        """Update the total percentages for crops and animals.

        This method calculates and updates the total percentages for tame crops
        and animals based on the selected parameters.
        """
        # Calculate animal percentages
        animalTotal = 0.0
        myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()
        for guid, value in self.mAnimalsMap.items():
            isChecked, parameterGuid = value
            if isChecked and parameterGuid in myAnimalParametersMap:
                animalTotal += float(str(myAnimalParametersMap[parameterGuid].percentTameMeat))

        # Calculate crop percentages
        cropTotal = 0.0
        myCropParametersMap = LaUtils.getAvailableCropParameters()
        for guid, value in self.mCropsMap.items():
            isChecked, parameterGuid = value
            if isChecked and parameterGuid in myCropParametersMap:
                # Use the instance property, not the class property
                parameter = myCropParametersMap[parameterGuid]
                if hasattr(parameter, 'percentTameCrop'):
                    try:
                        cropTotal += float(parameter.percentTameCrop)
                    except (ValueError, TypeError):
                        print(f"Warning: Invalid percentTameCrop for {parameterGuid}")

        # Update the totals display
        self.labelAnimalCheck.setText(f"{animalTotal:.1f}%")
        self.labelCropCheck.setText(f"{cropTotal:.1f}%")

        # Update status icons - using appropriate icon based on percentage
        animalIconPath = ":/status_ok.png" if abs(animalTotal - 100.0) < 0.1 else ":/status_error.png"
        cropIconPath = ":/status_ok.png" if abs(cropTotal - 100.0) < 0.1 else ":/status_error.png"

        # Check if the icon label widgets actually exist before setting pixmap
        # The variable names might be different from what we assumed
        try:
            # Try to find appropriate labels by name - adapt these to match what's in your UI
            if hasattr(self, 'labelAnimalIcon'):
                self.labelAnimalIcon.setPixmap(QIcon(animalIconPath).pixmap(16, 16))

            if hasattr(self, 'labelCropIcon'):
                self.labelCropIcon.setPixmap(QIcon(cropIconPath).pixmap(16, 16))
            # If the above doesn't work, we'll just skip setting the icons
            # but still log the percentages
        except Exception as e:
            LaUtils.debug.log(f"Warning: Could not update status icons: {str(e)}", "Warning")

        # Log the updated percentages regardless of icon status
        LaUtils.debug.log(f"Total percentages updated: Animals {animalTotal:.1f}%, Crops {cropTotal:.1f}%", "Calculation")

    def showSelectedAnimalDetails(self, row):
        """Show details for the selected animal."""
        if row < 0 or row >= self.tblAnimals.rowCount():
            return

        try:
            # Get name item which contains the GUID
            nameItem = self.tblAnimals.item(row, 1)
            if nameItem is None:
                LaUtils.debug.log(f"No name item found at row {row}", "Error")
                return

            # Get the actual GUID string
            guid = nameItem.data(QtCore.Qt.UserRole)
            if not guid:
                LaUtils.debug.log(f"No GUID found in name item at row {row}", "Error")
                return

            # If guid is a method (bound method of LaGuid), call it to get the string
            if hasattr(guid, '__call__'):
                guid = guid()

            LaUtils.debug.log(f"Getting animal with GUID string: {guid}", "UI")
            
            # Get the animal object and ensure it has name and description
            animal = LaUtils.getAnimal(guid)
            if not animal:
                LaUtils.debug.log(f"Could not get animal for GUID: {guid}", "Error")
                return

            # Dump animal object attributes for debugging
            LaUtils.debug.log(f"Animal object attributes: {dir(animal)}", "Debug")
            LaUtils.debug.log(f"Animal name: {getattr(animal, 'name', 'No name')}", "Debug")
            LaUtils.debug.log(f"Animal description: {getattr(animal, 'description', 'No description')}", "Debug")

            # Verify animal has required attributes
            if not hasattr(animal, 'name') or not animal.name:
                LaUtils.debug.log(f"Animal {guid} has no name attribute or name is empty", "Error")
                return

            LaUtils.debug.log(f"Retrieved animal: {animal.name}", "UI")

            # Format HTML content with verified data
            html_content = []
            html_content.append(f"<h2>{animal.name}</h2>")
            
            if hasattr(animal, 'description') and animal.description:
                html_content.append(f"<p><strong>Description:</strong> {animal.description}</p>")
            if hasattr(animal, 'animalCalories') and animal.animalCalories:
                html_content.append(f"<p><strong>Calories:</strong> {animal.animalCalories}</p>")

            # Get and display any animal parameters associated with this animal
            animalParams = LaUtils.getAvailableAnimalParameters()
            if animalParams:
                for paramGuid, param in animalParams.items():
                    # Check if param.animalGuid is a method and call it if needed
                    paramAnimalGuid = param.animalGuid() if hasattr(param.animalGuid, '__call__') else param.animalGuid
                    if paramAnimalGuid == guid:
                        html_content.append("<h3>Parameters</h3>")
                        if hasattr(param, 'percentTameMeat'):
                            html_content.append(f"<p><strong>% Tame Meat:</strong> {param.percentTameMeat}%</p>")
                        break

            # Join all HTML content
            final_html = "\n".join(html_content)

            # Set the content in the text browser
            if hasattr(self, 'textBrowserAnimalDefinition'):
                self.textBrowserAnimalDefinition.setHtml(final_html)
                LaUtils.debug.log(f"Displayed animal details for {animal.name}", "UI")
            else:
                LaUtils.debug.log("textBrowserAnimalDefinition not found", "Error")
                return

            # Handle image display
            if hasattr(self, 'lblAnimalPix'):
                self.lblAnimalPix.clear()  # Clear existing image
                
                if hasattr(animal, 'imageFile') and animal.imageFile:
                    # If imageFile is a method, call it
                    imagePath = animal.imageFile() if hasattr(animal.imageFile, '__call__') else animal.imageFile
                    imagePath = LaUtils.resolvePath(str(imagePath), 'image')
                    LaUtils.debug.log(f"Attempting to load animal image: {imagePath}", "UI")
                    
                    if os.path.exists(imagePath):
                        pixmap = QPixmap(imagePath)
                        if not pixmap.isNull():
                            self.lblAnimalPix.setPixmap(pixmap)
                            LaUtils.debug.log("Animal image loaded successfully", "UI")
                        else:
                            LaUtils.debug.log(f"Failed to create pixmap from {imagePath}", "Error")
                            # Try alternative path
                            imagesDir = LaUtils.userImagesDirPath()
                            imageFileName = os.path.basename(str(animal.imageFile))
                            alternativePath = os.path.join(imagesDir, imageFileName)
                            
                            if os.path.exists(alternativePath):
                                pixmap = QPixmap(alternativePath)
                                if not pixmap.isNull():
                                    self.lblAnimalPix.setPixmap(pixmap)
                                    LaUtils.debug.log(f"Successfully loaded image from alternative path: {alternativePath}", "UI")
                                else:
                                    LaUtils.debug.log(f"Failed to load image from alternative path: {alternativePath}", "Error")
                    else:
                        LaUtils.debug.log(f"Image path doesn't exist: {imagePath}", "Warning")
            else:
                LaUtils.debug.log("lblAnimalPix not found", "Error")

        except Exception as e:
            LaUtils.debug.log(f"Error showing animal details: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def showSelectedCropDetails(self, row):
        """Show details for the selected crop.

        Args:
            row: The row index of the selected crop
        """
        if row < 0 or row >= self.tblCrops.rowCount():
            return

        try:
            guid = self.tblCrops.item(row, 1).data(QtCore.Qt.UserRole)
            crop = LaUtils.getCrop(guid)
            if crop and crop.name:
                # Display basic crop details in the text browser
                html_content = "<h2>" + crop.name + "</h2>"
                html_content += "<p><strong>Description:</strong> " + crop.description + "</p>"
                html_content += "<p><strong>Calories:</strong> " + str(crop.cropCalories) + "</p>"
                # Add any other crop properties you want to display
                self.textBrowserCropDefinition.setHtml(html_content)

                # Clear existing image
                self.lblCropPix.clear()

                # Display image if available
                if hasattr(crop, 'imageFile') and crop.imageFile:
                    imagePath = LaUtils.resolvePath(crop.imageFile, 'image')
                    LaUtils.debug.log(f"Attempting to load crop image: {imagePath}", "UI")

                    if imagePath and os.path.exists(imagePath):
                        pixmap = QPixmap(imagePath)
                        if not pixmap.isNull():
                            self.lblCropPix.setPixmap(pixmap)
                            LaUtils.debug.log("Crop image loaded successfully", "UI")
                        else:
                            LaUtils.debug.log(f"Failed to create pixmap from {imagePath}", "Error")
                    else:
                        LaUtils.debug.log(f"Image path doesn't exist: {imagePath}", "Warning")
        except Exception as e:
            LaUtils.debug.log(f"Error showing crop details: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def updateCropCalculations(self, crop):
        """Update calculations for a crop.

        Args:
            crop: The crop object to calculate values for
        """
        # Implement any specific calculation logic for crops here
        # This method would typically update display values based on the crop's properties
        pass

    def updateAnimalCalculations(self, animal):
        """Update calculations for an animal.

        Args:
            animal: The animal object to calculate values for.
        """
        # Implement any specific calculation logic for animals here
        # This method would typically update display values based on the animal's properties
        pass

    def refresh(self):
        """Refresh all components of the form."""
        self.loadAnimals()
        self.loadCrops()
        self.setDietLabels()  # Update diet labels
        # Update any other UI elements or calculations as needed

    def connectSignalsSlots(self):
        """Connect signals to slots for UI interaction."""
        # TODO: Menu and toolbar actions will be implemented later
        # These will include:
        # - File menu: New, Open, Save, Save As, Preferences
        # - Help menu: About
        # - Toolbar: New, Open, Save, Save As, Preferences

        # Connect the existing buttons
        self.pushButtonExit.clicked.connect(self.close)
        self.pbnNewCrop.clicked.connect(self.on_clicked_pbnNewCrop)
        self.pbnNewCropParameter.clicked.connect(self.on_clicked_pbnNewCropParameter)
        self.pbnNewAnimal.clicked.connect(self.on_clicked_pbnNewAnimal)
        self.pbnNewAnimalParameter.clicked.connect(self.on_clicked_pbnNewAnimalParameter)

        # Connect tree widget
        self.treeHelp.currentItemChanged.connect(self.current_item_changed)

        # Connect sliders
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)

        # Connect list widgets and tables
        self.treeHelp.currentItemChanged.connect(self.helpItemClicked)
        self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)
        self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)
        self.tblAnimals.cellChanged.connect(self.animalCalcSelectionChanged)
        self.tblCrops.cellClicked.connect(self.cropCellClicked)
        self.tblCrops.cellChanged.connect(self.cropCalcSelectionChanged)
        self.cbDebug.clicked.connect(self.on_cbDebug_clicked)