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
import os

# region imports
from qgis.PyQt.QtWidgets import QListWidgetItem, QTableWidgetItem, QComboBox, QCheckBox
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFile, QSettings
from qgis.PyQt.QtCore import QTextStream
from qgis.PyQt.QtGui import QIcon

from qgis.PyQt import QtWidgets, QtCore, QtGui
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFile, QTextStream
from qgis.PyQt.QtGui import QIcon, QPixmap

from la.lib.lautils import LaUtils
from la.lib.ladietlabels import LaDietLabels

# Add imports for implementation classes
from la.lib.lacrop import LaCrop
from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.la import AreaUnits, EnergyType
from la.gui.lacropmanager import LaCropManager
from la.gui.lacropparametermanager import LaCropParameterManager
from la.gui.laanimalmanager import LaAnimalManager
from la.gui.laanimalparametermanager import LaAnimalParameterManager

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

        # Enable checkboxes that start disabled in the UI
        self.cboxIncludeDairy.setEnabled(True)
        self.cboxBaseOnPlants.setEnabled(True)

        # Initialize model with default values
        from la.lib.lamodel import LaModel
        self.model = LaModel()
        self.model.dietPercent = self.sliderDiet.value()
        self.model.meatPercent = self.sliderMeat.value()
        self.model.percentOfDietThatIsFromCrops = self.sliderCrop.value()

        # Initialize diet labels with default values
        self.initializeDietLabels()

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

        LaMainFormBase.setDietLabels(self)  # recalculates model (to update the diet labels!)

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

        # Connect tab widget change signal
        if hasattr(self, 'tabWidgetMain'):
            self.tabWidgetMain.currentChanged.connect(self.on_tabWidgetMain_currentChanged)

    def on_tabWidgetMain_currentChanged(self, index):
        """Handle tab changes in the main tab widget."""
        # Assuming Calculations tab is the 4th tab (index 3)
        if index == 3: # Index of the Calculations tab
            LaUtils.debug.log("Calculations tab selected", "UI")
            # Check if the animal list has items
            if self.listWidgetCalculationsAnimal.count() > 0:
                # Check if no item is currently selected or if the first item isn't selected
                if self.listWidgetCalculationsAnimal.currentRow() != 0:
                    LaUtils.debug.log("Selecting first animal in calculations list", "UI")
                    # Select the first item programmatically
                    self.listWidgetCalculationsAnimal.setCurrentRow(0)
                    # The currentItemChanged signal connected to animalCalcClicked should handle the rest
            else:
                LaUtils.debug.log("Animal calculations list is empty", "UI")

    def initializeDietLabels(self):
        """Initialize all diet labels with default values."""
        try:
            # Set default values for all diet labels
            self.labelPortionMeat.setText("0.0%")
            self.labelPortionCrops.setText("0.0%")
            self.labelPortionAllDairy.setText("0.0%")
            self.labelPortionDairy.setText("0.0%")
            self.labelPortionTameMeat.setText("0.0%")
            self.labelPortionWildMeat.setText("0.0%")
            self.labelPortionWildPlants.setText("0.0%")

            # Set default calorie values
            self.labelCaloriesCrops.setText("0.0")
            self.labelCaloriesTameMeat.setText("0.0")
            self.labelCaloriesDairy.setText("0.0")
            self.labelCaloriesWildMeat.setText("0.0")
            self.labelCaloriesWildPlants.setText("0.0")

            # Set default settlement and individual calorie labels
            self.labelCaloriesIndividual.setText("0.0")
            self.labelCaloriesSettlement.setText("0.0")

            # Set default dairy surplus
            self.labelDairySurplus.setText("0.0")

            from la.lib.lautils import LaUtils
            LaUtils.debug.log("Diet labels initialized with default values", "Diet")

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error initializing diet labels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

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
        # Update diet labels and recalculate model
        self.setDietLabels()  # Recalculates model to update the diet labels

    def on_sliderMeat_valueChanged(self, theValue):
        myWildPercent = str(100 - theValue)
        myTamePercent = str(theValue)
        # Fix for swapped labels - theValue is the wild meat percentage
        self.labelMeatWildPercent.setText(myWildPercent)  # Wild meat percentage
        self.labelMeatTamePercent.setText(myTamePercent)  # Tame meat percentage
        # Update diet labels and recalculate model
        self.setDietLabels()  # Recalculates model to update the diet labels

    def on_sliderCrop_valueChanged(self, theValue):
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelCropWildPercent.setText(myMinString)
        self.labelCropTamePercent.setText(myMaxString)
        # Update diet labels and recalculate model
        self.setDietLabels()  # Recalculates model to update the diet labels

    def setDietLabels(self):
        """
        Update the model from the UI, perform diet calculations, and update
        the diet information display labels. Mirrors C++ LaMainForm::setDietLabels.
        """
        try:
            LaUtils.debug.log("Starting setDietLabels", "Diet")

            # Critical early return: Don't perform heavy calculations unless percentages total 100%
            if hasattr(self, 'labelAnimalCheck') and hasattr(self, 'labelCropCheck'):
                if self.labelAnimalCheck.text() != "100.0%" or self.labelCropCheck.text() != "100.0%":
                    # Only update basic labels without performing heavy calculations
                    self.updateBasicLabels()
                    return

            # --- 1. Update self.model thoroughly from ALL relevant UI elements ---
            # (This replaces scattered updates and ensures model reflects current UI)
            if not hasattr(self, 'model'):
                LaUtils.debug.log("Model not initialized. Cannot set diet labels.", "Error")
                return

            # Site Info / Basic Params
            self.model.name = self.lineEditSiteName.text() # Assuming lineEditSiteName exists
            self.model.population = self.sbPopulation.value()
            self.model.period = self.lineEditPeriod.text() # Assuming lineEditPeriod exists
            self.model.mCaloriesPerPersonDaily = self.sbDailyCalories.value()

            # Location / Distance (Assuming these widgets exist based on C++ code)
            # Add try-except for text conversions that might fail
            try:
                self.model.easting = int(self.lineEditEasting.text() or 0) # type: ignore
            except ValueError: self.model.easting = 0 # type: ignore
            try:
                self.model.northing = int(self.lineEditNorthing.text() or 0) # type: ignore
            except ValueError: self.model.northing = 0 # type: ignore
            # Assuming radio buttons exist: radioButtonEuclidean, radioButtonWalkingTime, radioButtonPathDistance
            # self.model.euclideanDistance = self.radioButtonEuclidean.isChecked()
            # self.model.walkingTime = self.radioButtonWalkingTime.isChecked()
            # self.model.pathDistance = self.radioButtonPathDistance.isChecked()
            # Assuming sbModelPrecision exists
            # self.model.precision = self.sbModelPrecision.value()

            # Diet Sliders
            self.model.dietPercent = self.sliderDiet.value()
            self.model.meatPercent = self.sliderMeat.value() # This corresponds to TAME meat % in C++ slider logic, but WILD meat in model property logic? Check C++ UI vs Model property link. Let's assume model property is WILD animal %.
            self.model.percentOfDietThatIsFromCrops = self.sliderCrop.value() # This corresponds to TAME crop % in C++ slider logic, but WILD plant in model property logic? Check C++ UI vs Model property link. Let's assume model property is WILD plant %.

            # Dairy Settings
            self.model.mDairyUtilisation = self.sbDairyUtilisation.value()
            self.model.mIncludeDairy = self.cboxIncludeDairy.isChecked()
            self.model.mLimitDairy = self.cboxLimitDairy.isChecked()
            self.model.mLimitDairyPercent = self.sbLimitDairyPercent.value()

            # Calculation Base
            self.model.mBaseOnPlants = self.cboxBaseOnPlants.isChecked()

            # Common Land Settings
            selected_area_unit_text = self.cbAreaUnits.currentText()
            myAreaUnits = AreaUnits.Dunum if selected_area_unit_text == "Dunum" else AreaUnits.Hectare
            self.model.commonLandAreaUnits = myAreaUnits # type: ignore
            # Ensure the setter handles conversion if necessary, or pass units
            # Assuming commonLandValue property setter expects the raw value and units are handled internally or via separate property
            myCommonRasterValue = self.sbCommonRasterValue.value()
            self.model.commonLandValue = int(myCommonRasterValue) # type: ignore

            # Energy Type (Assuming this maps to model's specificLandEnergyType based on C++)
            mySelectedEnergyText = self.cbCommonLandEnergyType.currentText()
            myEnergyType: EnergyType = EnergyType.KCalories if mySelectedEnergyText == "KCalories" else EnergyType.TDN
            self.model.specificLandEnergyType = myEnergyType # type: ignore

            LaUtils.debug.log("Model updated from UI elements", "Diet")

            # --- 2. Collect Selected Animals and Crops ---
            # Build temporary dictionaries of selected items to pass to the model
            mySelectedAnimalsMap = {}
            if hasattr(self, 'mAnimalsMap'):
                 for myAnimalGuid, (myAnimalIsSelected, myParamGuid) in self.mAnimalsMap.items():
                     if myAnimalIsSelected:
                         # Ensure GUIDs are strings, handle potential None param_guid
                         mySelectedAnimalsMap[str(myAnimalGuid)] = str(myParamGuid) if myParamGuid else ""
            else:
                 LaUtils.debug.log("mAnimalsMap not found", "Warning")

            mySelectedCropsMap = {}
            if hasattr(self, 'mCropsMap'):
                for myCropGuid, (myCropIsSelected, myParamGuid) in self.mCropsMap.items():
                    if myCropIsSelected:
                        # Ensure GUIDs are strings, handle potential None myParamGuid
                        mySelectedCropsMap[str(myCropGuid)] = str(myParamGuid) if myParamGuid else ""
            else:
                LaUtils.debug.log("mCropsMap not found", "Warning")

            # Set the collected selections on the model
            self.model.animals = mySelectedAnimalsMap # type: ignore
            self.model.crops = mySelectedCropsMap # type: ignore
            LaUtils.debug.log(f"Selected Animals: {len(mySelectedAnimalsMap)}, Selected Crops: {len(mySelectedCropsMap)}", "Diet")
            myDietLabels = LaDietLabels() # Initialize empty labels

            # --- 3. Update Basic Percentages and Calories (These don't need full calculation) ---
            # Get values from UI
            overall_plant_percent = 100 - self.sliderDiet.value()  # Plant/Meat slider
            overall_meat_percent = self.sliderDiet.value()

            # Plant breakdown
            tame_crop_percent = 100 - self.sliderCrop.value()  # Tame/Wild plant slider
            wild_plant_percent = self.sliderCrop.value()

            # Meat breakdown
            tame_meat_percent = 100 - self.sliderMeat.value()  # Tame/Wild meat slider
            wild_meat_percent = self.sliderMeat.value()

            # Calculate actual percentages of total diet
            crop_portion = (overall_plant_percent * tame_crop_percent) / 100.0
            wild_plant_portion = (overall_plant_percent * wild_plant_percent) / 100.0
            tame_meat_portion = (overall_meat_percent * tame_meat_percent) / 100.0
            wild_meat_portion = (overall_meat_percent * wild_meat_percent) / 100.0

            # Update percentage labels
            self.labelPortionPlants.setText(f"{overall_plant_percent:.1f}")
            self.labelPortionMeat.setText(f"{overall_meat_percent:.1f}")
            self.labelPortionCrops.setText(f"{crop_portion:.1f}")
            self.labelPortionTameMeat.setText(f"{tame_meat_portion:.1f}")
            self.labelPortionWildMeat.setText(f"{wild_meat_portion:.1f}")
            self.labelPortionWildPlants.setText(f"{wild_plant_portion:.1f}")

            # Calculate calories
            daily_cals = self.sbDailyCalories.value()
            population = self.sbPopulation.value()
            total_annual_mcals = (daily_cals * population * 365) / 1000000.0  # Convert to MCals

            # Update calorie labels
            self.labelCaloriesSettlement.setText(f"{total_annual_mcals:.1f}")
            self.labelCaloriesIndividual.setText(f"{(daily_cals * 365 / 1000000.0):.1f}")

            crop_mcals = total_annual_mcals * crop_portion / 100.0
            tame_meat_mcals = total_annual_mcals * tame_meat_portion / 100.0
            wild_meat_mcals = total_annual_mcals * wild_meat_portion / 100.0
            wild_plant_mcals = total_annual_mcals * wild_plant_portion / 100.0

            self.labelCaloriesCrops.setText(f"{crop_mcals:.1f}")
            self.labelCaloriesTameMeat.setText(f"{tame_meat_mcals:.1f}")
            self.labelCaloriesWildMeat.setText(f"{wild_meat_mcals:.1f}")
            self.labelCaloriesWildPlants.setText(f"{wild_plant_mcals:.1f}")

            # --- 4. Check if we should do full calculation for dairy ---
            # Ensure the percentage check labels exist before accessing their text
            myAnimalCheckText = ""
            myCropCheckText = ""
            if hasattr(self, 'labelAnimalCheck'):
                myAnimalCheckText = self.labelAnimalCheck.text()
            if hasattr(self, 'labelCropCheck'):
                myCropCheckText = self.labelCropCheck.text()

            # Only proceed with full calculation if percentages total 100%
            if myAnimalCheckText != "100.0%" or myCropCheckText != "100.0%":
                LaUtils.debug.log(f"Skipping full calculation for dairy: Animal%={myAnimalCheckText}, Crop%={myCropCheckText}", "Diet")
                # Clear dairy-related labels since we can't calculate them
                self.labelPortionAllDairy.setText("0.0")
                self.labelPortionDairy.setText("0.0")
                self.labelCaloriesDairy.setText("0.0")
                self.labelDairySurplus.setText("No Surplus Dairy Produced")
                return

            # --- 4. Select and Run Calculation Method ---
            if self.model.mBaseOnPlants:
                if self.model.mIncludeDairy:
                    LaUtils.debug.log("Running doCalcsPlantsFirstIncludeDairy", "Diet")
                    myDietLabels = self.model.doCalcsPlantsFirstIncludeDairy()
                else:
                    LaUtils.debug.log("Running doCalcsPlantsFirstDairySeparate", "Diet")
                    myDietLabels = self.model.doCalcsPlantsFirstDairySeparate()
            else:
                if self.model.mIncludeDairy:
                    LaUtils.debug.log("Running doCalcsAnimalsFirstIncludeDairy", "Diet")
                    # NOTE: C++ calls doCalcsAnimalsFirstIncludeDiary (typo in original?)
                    # Assuming Python method is doCalcsAnimalsFirstIncludeDairy
                    myDietLabels = self.model.doCalcsAnimalsFirstIncludeDairy()
                else:
                    LaUtils.debug.log("Running doCalcsAnimalsFirstDairySeparate", "Diet")
                    myDietLabels = self.model.doCalcsAnimalsFirstDairySeparate()

            # --- 5. Update UI Labels with Results ---
            if myDietLabels: # Check if calculation returned valid labels
                # Use .1f formatting to match the previous Python version's precision
                # If C++ doesn't specify precision, adjust as needed.
                # Settlement / Individual Cals
                self.labelCaloriesIndividual.setText(f"{myDietLabels.kiloCaloriesIndividualAnnual:.1f}")
                self.labelCaloriesSettlement.setText(f"{myDietLabels.megaCaloriesSettlementAnnual:.1f}")

                # Overall Portions
                self.labelPortionPlants.setText(f"{myDietLabels.plantsPortionPct:.1f}") # Assuming labelPortionPlants exists
                self.labelPortionMeat.setText(f"{myDietLabels.animalPortionPct:.1f}")
                self.labelPortionAllDairy.setText(f"{myDietLabels.dairyPortionPct:.1f}") # Overall dairy

                # Detailed Portions
                self.labelPortionCrops.setText(f"{myDietLabels.cropsPortionPct:.1f}") # Tame Crops
                self.labelPortionTameMeat.setText(f"{myDietLabels.tameMeatPortionPct:.1f}")
                self.labelPortionDairy.setText(f"{myDietLabels.dairyPortionPct:.1f}") # Dairy again (matches C++)

                self.labelPortionWildMeat.setText(f"{myDietLabels.wildAnimalPortionPct:.1f}")
                self.labelPortionWildPlants.setText(f"{myDietLabels.wildPlantsPortionPct:.1f}")

                # Detailed Calories (MCals)
                self.labelCaloriesCrops.setText(f"{myDietLabels.cropMCalories:.1f}")
                self.labelCaloriesTameMeat.setText(f"{myDietLabels.animalMCalories:.1f}")
                self.labelCaloriesDairy.setText(f"{myDietLabels.dairyMCalories:.1f}")
                self.labelCaloriesWildMeat.setText(f"{myDietLabels.wildAnimalMCalories:.1f}")
                self.labelCaloriesWildPlants.setText(f"{myDietLabels.wildPlantsMCalories:.1f}")

                # Dairy Surplus Label (Conditional Text)
                if myDietLabels.dairySurplusMCalories > 0.0: # type: ignore
                    self.labelDairySurplus.setText(f"Dairy Surplus produced! {myDietLabels.dairySurplusMCalories:.1f} MCalories")
                else:
                    self.labelDairySurplus.setText("No Surplus Dairy Produced")

                LaUtils.debug.log("Diet labels updated with calculation results", "Diet")
            else:
                LaUtils.debug.log("Calculation did not return valid DietLabels object.", "Warning")
                # Optionally clear labels or display an error message

        except AttributeError as ae:
             # Catch missing attributes (e.g., UI elements not found)
             LaUtils.debug.log(f"Missing attribute during setDietLabels: {str(ae)}", "Error")
             import traceback
             LaUtils.debug.log(f"Traceback: {traceback.format_exc()}", "Error")
             # Optionally display error in UI
        except Exception as e:
            LaUtils.debug.log(f"Error during setDietLabels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            # Optionally display error in UI

    def setModel(self, *args):
        from la.lib.la import AreaUnits
        self.mSelectedCropsMap.clear()
        self.mSelectedAnimalsMap.clear()
        mySelectedAreaUnit = AreaUnits(self.cbAreaUnits.currentText())
        myCommonRasterValue = int(self.sbCommonRasterValue.value())
        myAreaUnits = 'Dunum' if mySelectedAreaUnit else 'Hectare'
        print(mySelectedAreaUnit, myAreaUnits, myCommonRasterValue)

    def loadAnimals(self):
        """Load animals into the table widget."""
        try:
            # Clear the lists first
            if hasattr(self, 'listWidgetCalculationsAnimal'):
                self.listWidgetCalculationsAnimal.clear()

            # Clear and setup the table if it exists
            if not hasattr(self, 'tblAnimals') or self.tblAnimals is None:
                LaUtils.debug.log("Cannot load animals: table widget not found", "Error")
                return

            self.tblAnimals.clear()
            self.tblAnimals.setRowCount(0)
            self.tblAnimals.setColumnCount(4)

            # Initialize tracking variables
            myCurrentRow = 0
            myRunningPercentage = 0.0

            # Get available animals and parameters
            try:
                myAnimalsMap = LaUtils.getAvailableAnimals()
                if not myAnimalsMap:
                    LaUtils.debug.log("No animals available to load", "Warning")
                    return
            except Exception as e:
                LaUtils.debug.log(f"Error getting available animals: {str(e)}", "Error")
                return

            try:
                myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()
                if not myAnimalParametersMap:
                    LaUtils.debug.log("No animal parameters available", "Warning")
                    return
            except Exception as e:
                LaUtils.debug.log(f"Error getting animal parameters: {str(e)}", "Error")
                return

            # Initialize animals map if needed
            if not hasattr(self, 'mAnimalsMap'):
                self.mAnimalsMap = {}

            # Process each animal
            for myGuid, myAnimal in myAnimalsMap.items():
                # Get the actual GUID string
                actualGuid = str(myAnimal.guid()) if callable(getattr(myAnimal, 'guid', None)) else str(myGuid)

                LaUtils.debug.log(f"Processing animal: {myAnimal.name} (GUID: {actualGuid})", "Animals")

                myName = myAnimal.name
                myValue = self.mAnimalsMap.get(actualGuid, (False, ""))

                # Update animals map
                if actualGuid not in self.mAnimalsMap:
                    self.mAnimalsMap[actualGuid] = myValue

                # Create table row
                myIcon = QIcon(":/localdata.png")
                self.tblAnimals.insertRow(myCurrentRow)

                # Used checkbox column
                mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
                mypUsedItem.setCheckState(QtCore.Qt.Checked if myValue[0] else QtCore.Qt.Unchecked)
                self.tblAnimals.setItem(myCurrentRow, 0, mypUsedItem)

                # If checked, ensure it's in calculations list
                if myValue[0]:
                    try:
                        self.addAnimalToCalculationsList(actualGuid)
                    except Exception as e:
                        LaUtils.debug.log(f"Error adding animal to calculations: {str(e)}", "Error")
                else:
                    # Remove from calculations list if unchecked
                    try:
                        self.removeAnimalFromCalculationsList(actualGuid)
                    except Exception as e:
                        LaUtils.debug.log(f"Error removing animal from calculations: {str(e)}", "Error")

                # Name column with GUID data
                mypNameItem = QtWidgets.QTableWidgetItem(str(myName))
                mypNameItem.setData(QtCore.Qt.UserRole, actualGuid)
                self.tblAnimals.setItem(myCurrentRow, 1, mypNameItem)
                mypNameItem.setIcon(myIcon)

                # Parameters combo box
                mypCombo = QtWidgets.QComboBox(self)

                # Add parameters to combo
                paramsFound = False
                for myParameterGuid, myAnimalParameter in myAnimalParametersMap.items():
                    if myAnimalParameter is None:
                        continue

                    # Get animal GUID from parameter, handling both property and method cases
                    paramAnimalGuid = None
                    if hasattr(myAnimalParameter, 'animalGuid'):
                        if isinstance(myAnimalParameter.animalGuid, str):
                            paramAnimalGuid = str(myAnimalParameter.animalGuid)
                        else:
                            paramAnimalGuid = str(myAnimalParameter.animalGuid)

                    # Skip if parameter is not for this animal
                    if str(actualGuid) != paramAnimalGuid:
                        continue

                    paramsFound = True
                    LaUtils.debug.log(f"Found parameter {myAnimalParameter.name} for animal {myName}", "Animals")

                    # Format parameter name
                    myParameterName = f"{myAnimalParameter.name}  ({myAnimalParameter.description})"

                    # Update value if needed
                    if not myValue[1]:
                        myValue = (myValue[0], str(myParameterGuid))

                    # Update percentage if this is the selected parameter
                    if str(myValue[1]) == str(myAnimalParameter.guid):
                        if myValue[0] and hasattr(myAnimalParameter, 'percentTameMeat'):
                            try:
                                myRunningPercentage += float(str(myAnimalParameter.percentTameMeat))
                            except (ValueError, TypeError):
                                LaUtils.debug.log(f"Invalid percentTameMeat for parameter {myParameterGuid}", "Warning")

                        # Add percentage column
                        if hasattr(myAnimalParameter, 'percentTameMeat'):
                            mypPercentItem = QtWidgets.QTableWidgetItem(str(myAnimalParameter.percentTameMeat))
                            self.tblAnimals.setItem(myCurrentRow, 3, mypPercentItem)

                    # Add to combo box
                    mypCombo.addItem(myIcon, myParameterName, str(myParameterGuid))

                if not paramsFound:
                    LaUtils.debug.log(f"No parameters found for animal {myName} with GUID {actualGuid}", "Warning")
                    # Add empty option
                    mypCombo.addItem(myIcon, "No Parameters Available", "")

                # Set default combo selection and add to table
                self.setComboToDefault(mypCombo, myValue[1])
                self.mAnimalsMap[str(actualGuid)] = myValue
                self.tblAnimals.setCellWidget(myCurrentRow, 2, mypCombo)

                myCurrentRow += 1

            # Update total percentage display
            if hasattr(self, 'labelAnimalCheck'):
                self.labelAnimalCheck.setText(f"{myRunningPercentage:.1f}%")

            # Update status icon
            if hasattr(self, 'labelAnimalIcon'):
                iconPath = ":/status_ok.png" if abs(myRunningPercentage - 100.0) < 0.1 else ":/status_error.png"
                self.labelAnimalIcon.setPixmap(QIcon(iconPath).pixmap(16, 16))

            LaUtils.debug.log(f"Loaded {myCurrentRow} animals with total percentage {myRunningPercentage:.1f}%", "Animals")

        except Exception as e:
            LaUtils.debug.log(f"Error loading animals: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

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

    def updateDietLabels(self, theDairyPortionPct, theTameMeatPortionPct, theCropsPortionPct):
        """
        Update diet labels based on the given portion percentages.
        """
        self.mDairyPortionPct = theDairyPortionPct
        self.mTameMeatPortionPct = theTameMeatPortionPct
        self.mCropsPortionPct = theCropsPortionPct

        LaUtils.debug.log(f"Updated diet labels: Dairy {self.mDairyPortionPct}, \
                          Tame Meat {self.mTameMeatPortionPct}, Crops {self.mCropsPortionPct}", "Diet")

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
        LaUtils.debug.setEnabled(isChecked)

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
        # Ensure we have a string GUID
        animalGuid = str(animalGuid)

        # Check if the animal is already in the list
        for i in range(self.listWidgetCalculationsAnimal.count()):
            item = self.listWidgetCalculationsAnimal.item(i)
            if str(item.data(QtCore.Qt.UserRole)) == animalGuid:
                return

        # Get the animal object
        animal = LaUtils.getAnimal(animalGuid)
        if animal and animal.name:
            item = QListWidgetItem(str(animal.name))
            # Store the actual GUID string
            item.setData(QtCore.Qt.UserRole, animalGuid)
            self.listWidgetCalculationsAnimal.addItem(item)
            LaUtils.debug.log(f"Added animal {animal.name} with GUID {animalGuid} to calculations list", "UI")

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

    def showSelectedAnimalDetails(self, theRow):
        """Show details for the selected animal."""
        if theRow < 0 or theRow >= self.tblAnimals.rowCount():
            return

        try:
            # Get the GUID from the selected row
            nameItem = self.tblAnimals.item(theRow, 1)
            if not nameItem:
                LaUtils.debug.log("No name item found", "Error")
                return

            # Get the GUID string
            guid = str(nameItem.data(QtCore.Qt.UserRole))
            if not guid:
                LaUtils.debug.log("No GUID found in name item", "Error")
                return

            LaUtils.debug.log(f"Getting animal details for GUID: {guid}", "UI")

            # Get the animal object
            animal = LaUtils.getAnimal(guid)
            if not animal:
                LaUtils.debug.log(f"Could not find animal for GUID: {guid}", "Error")
                return

            LaUtils.debug.log(f"Found animal: {animal.name}", "UI")

            # Get parameter from combobox
            paramCombo = self.tblAnimals.cellWidget(theRow, 2)
            if paramCombo:
                paramGuid = paramCombo.currentData()
                if paramGuid:
                    paramGuid = str(paramGuid)  # Ensure GUID is string
                    animalParametersMap = LaUtils.getAvailableAnimalParameters()
                    parameter = animalParametersMap.get(paramGuid)
                else:
                    parameter = None
            else:
                parameter = None

            # Display HTML report
            if hasattr(self, 'textBrowserAnimalDefinition'):
                html = self.generateAnimalDefinitionReport(animal, parameter)
                self.textBrowserAnimalDefinition.setHtml(html)
                LaUtils.debug.log(f"Displayed animal details for {animal.name}", "UI")

            # Handle image display
            if hasattr(self, 'lblAnimalPix'):
                self.lblAnimalPix.clear()

                # Get image file path
                image_file = None
                if hasattr(animal, 'imageFile'):
                    LaUtils.debug.log(f"Animal has imageFile attribute", "UI")
                    # Handle both property and method cases
                    if isinstance(animal.imageFile, str):
                        image_file = animal.imageFile
                        LaUtils.debug.log(f"imageFile is string property, value: {image_file}", "UI")
                    else:
                        try:
                            image_file = animal.imageFile()  # Call as method
                            LaUtils.debug.log(f"imageFile called as method, value: {image_file}", "UI")
                        except Exception as e:
                            LaUtils.debug.log(f"Error calling imageFile method: {str(e)}", "UI")
                            image_file = None

                if image_file:
                    # Try standard path first
                    resolved_path = LaUtils.resolvePath(str(image_file), 'image')
                    LaUtils.debug.log(f"Resolved image path: {resolved_path}", "UI")

                    if os.path.exists(resolved_path):
                        LaUtils.debug.log(f"Image file exists at: {resolved_path}", "UI")
                        pixmap = QPixmap(resolved_path)
                        if not pixmap.isNull():
                            self.lblAnimalPix.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))
                            LaUtils.debug.log(f"Set animal image from: {resolved_path}", "UI")
                        else:
                            LaUtils.debug.log(f"Could not create pixmap from: {resolved_path}", "Error")
                            self.lblAnimalPix.clear()
                    else:
                        # Try alternate path in images directory
                        imagesDir = LaUtils.userImagesDirPath()
                        imageFileName = os.path.basename(str(image_file))
                        alternativePath = os.path.join(imagesDir, imageFileName)
                        LaUtils.debug.log(f"Trying alternate image path: {alternativePath}", "UI")

                        if os.path.exists(alternativePath):
                            pixmap = QPixmap(alternativePath)
                            if not pixmap.isNull():
                                self.lblAnimalPix.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))
                                LaUtils.debug.log(f"Set animal image from alternate path: {alternativePath}", "UI")
                            else:
                                LaUtils.debug.log(f"Could not create pixmap from alternate path: {alternativePath}", "Error")
                                self.lblAnimalPix.clear()
                        else:
                            LaUtils.debug.log(f"No image file found at either path for animal: {animal.name}", "Warning")
                            self.lblAnimalPix.clear()

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
            # Get name item which contains the GUID
            nameItem = self.tblCrops.item(row, 1)
            if nameItem is None:
                LaUtils.debug.log(f"No name item found at row {row}", "Error")
                return

            # Get the GUID string
            guid = nameItem.data(QtCore.Qt.UserRole)
            if not guid:
                LaUtils.debug.log(f"No GUID found in name item at row {row}", "Error")
                return

            # Get the crop object
            crop = LaUtils.getCrop(guid)
            if not crop or not hasattr(crop, 'name') or not crop.name:
                LaUtils.debug.log(f"Could not find valid crop for GUID: {guid}", "Error")
                return

            # Get the parameter GUID from combobox
            comboBox = self.tblCrops.cellWidget(row, 2)
            parameterGuid = comboBox.currentData() if comboBox else None

            # Get the crop parameter
            cropParameter = None
            if parameterGuid:
                cropParametersMap = LaUtils.getAvailableCropParameters()
                if parameterGuid in cropParametersMap:
                    cropParameter = cropParametersMap[parameterGuid]

            # Generate HTML content combining crop and parameter details
            html_content = self.generateCropDefinitionReport(crop, cropParameter)

            # Display in text browser
            if hasattr(self, 'textBrowserCropDefinition'):
                self.textBrowserCropDefinition.setHtml(html_content)
                LaUtils.debug.log(f"Displayed crop details for {crop.name}", "UI")

            # Handle image display
            if hasattr(self, 'lblCropPix'):
                self.lblCropPix.clear()  # Clear existing image

                # Get image path, handling both property and method cases
                image_path = ""
                if hasattr(crop, 'imageFile'):
                    if isinstance(crop.imageFile, str):
                        image_path = crop.imageFile
                    else:
                        image_path = str(crop.imageFile)

                if image_path:
                    # Try to resolve the image path
                    resolved_path = LaUtils.resolvePath(str(image_path), 'image')
                    LaUtils.debug.log(f"Attempting to load crop image: {resolved_path}", "UI")

                    if os.path.exists(resolved_path):
                        pixmap = QPixmap(resolved_path)
                        if not pixmap.isNull():
                            self.lblCropPix.setPixmap(pixmap)
                            LaUtils.debug.log("Crop image loaded successfully", "UI")
                        else:
                            LaUtils.debug.log(f"Failed to create pixmap from: {resolved_path}", "Error")
                            self.lblCropPix.clear()
                    else:
                        # Try alternate path in user images directory
                        imagesDir = LaUtils.userImagesDirPath()
                        imageFileName = os.path.basename(str(image_path))
                        alternativePath = os.path.join(imagesDir, imageFileName)
                        LaUtils.debug.log(f"Trying alternate image path: {alternativePath}", "UI")

                        if os.path.exists(alternativePath):
                            pixmap = QPixmap(alternativePath)
                            if not pixmap.isNull():
                                self.lblCropPix.setPixmap(pixmap)
                                LaUtils.debug.log("Crop image loaded successfully from alternate path", "UI")
                            else:
                                LaUtils.debug.log(f"Failed to create pixmap from alternate path: {alternativePath}", "Error")
                                self.lblCropPix.clear()
                        else:
                            LaUtils.debug.log(f"No valid image path found for crop: {crop.name}", "Warning")
                            self.lblCropPix.clear()

        except Exception as e:
            LaUtils.debug.log(f"Error showing crop details: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def generateCropDefinitionReport(self, crop, cropParameter):
        """Generate an HTML report showing crop details and crop parameter details.

        Args:
            crop: The crop object
            cropParameter: The crop parameter object

        Returns:
            HTML string containing formatted crop and parameter details
        """
        # Start with the HTML structure
        html = "<body>"
        html += "<table width=\"100%\">"
        html += "<tr>"

        # Left column: Crop details
        html += "<td style=\"vertical-align:top; width:50%;\">"
        if crop:
            html += crop.toHtml()
        html += "</td>"

        # Right column: Parameter details
        html += "<td style=\"vertical-align:top; width:50%;\">"
        if cropParameter:
            # Add parameter details header
            html += f"<h3>Parameters for {crop.name}</h3>"
            html += "<table>"

            # Add parameter details
            html += f"<tr><td><b>Parameter Name:</b></td><td>{cropParameter.name}</td></tr>"
            html += f"<tr><td><b>Description:</b></td><td>{cropParameter.description}</td></tr>"
            html += f"<tr><td><b>Portion of Tame Crop Diet:</b></td><td>{cropParameter.percentTameCrop}%</td></tr>"

            # Add spoilage if it exists
            if hasattr(cropParameter, 'spoilage'):
                html += f"<tr><td><b>Spoilage:</b></td><td>{cropParameter.spoilage}%</td></tr>"

            # Add reseed if it exists
            if hasattr(cropParameter, 'reseed'):
                html += f"<tr><td><b>Reseed:</b></td><td>{cropParameter.reseed}%</td></tr>"

            # Add crop rotation if it exists
            if hasattr(cropParameter, 'cropRotation'):
                cropRotationText = "Yes" if cropParameter.cropRotation else "No"
                html += f"<tr><td><b>Crop Rotation:</b></td><td>{cropRotationText}</td></tr>"

            # Add fallow ratio if it exists
            if hasattr(cropParameter, 'fallowRatio') and cropParameter.fallowRatio > 0:
                html += f"<tr><td><b>Fallow Ratio:</b></td><td>{cropParameter.fallowRatio}</td></tr>"

                # Add fallow value if fallowRatio is used
                if hasattr(cropParameter, 'fallowValue'):
                    html += f"<tr><td><b>Fallow Value:</b></td><td>{cropParameter.fallowValue}</td></tr>"

            # Add land use information
            if hasattr(cropParameter, 'useCommonLand'):
                commonLandText = "Yes" if cropParameter.useCommonLand else "No"
                html += f"<tr><td><b>Use Common Land:</b></td><td>{commonLandText}</td></tr>"

            if hasattr(cropParameter, 'useSpecificLand'):
                specificLandText = "Yes" if cropParameter.useSpecificLand else "No"
                html += f"<tr><td><b>Use Specific Land:</b></td><td>{specificLandText}</td></tr>"

            # Add raster name if it exists and is being used
            if hasattr(cropParameter, 'rasterName') and cropParameter.rasterName:
                html += f"<tr><td><b>Raster:</b></td><td>{cropParameter.rasterName}</td></tr>"

            html += "</table>"
        else:
            html += "<p>No parameters selected for this crop.</p>"

        html += "</td>"
        html += "</tr>"
        html += "</table>"
        html += "</body>"

        return html

    def generateAnimalDefinitionReport(self, theAnimal: LaAnimal, theAnimalParameter: LaAnimalParameter):
        """Generate an HTML report showing animal details and animal parameter details.

        Args:
            animal: The animal object
            animalParameter: The animal parameter object

        Returns:
            HTML string containing formatted animal and parameter details
        """
        # Start with the HTML structure
        html = "<body>"
        html += "<table width=\"100%\">"
        html += "<tr>"

        # Left column: Animal details
        html += "<td style=\"vertical-align:top; width:50%;\">"
        if theAnimal:
            html += theAnimal.toHtml()
        html += "</td>"

        # Right column: Parameter details
        html += "<td style=\"vertical-align:top; width:50%;\">"
        if theAnimalParameter:
            # Add parameter details header
            html += f"<h3>Parameters for {theAnimal.name}</h3>"
            html += "<table>"

            # Add parameter details
            html += f"<tr><td><b>Parameter Name:</b></td><td>{theAnimalParameter.name}</td></tr>"
            html += f"<tr><td><b>Description:</b></td><td>{theAnimalParameter.description}</td></tr>"
            html += f"<tr><td><b>Portion of Tame Meat Diet:</b></td><td>{theAnimalParameter.percentTameMeat}%</td></tr>"

            # Add grazing land information
            if hasattr(theAnimalParameter, 'useCommonGrazingLand'):
                commonLandText = "Yes" if theAnimalParameter.useCommonGrazingLand else "No"
                html += f"<tr><td><b>Use Common Grazing Land:</b></td><td>{commonLandText}</td></tr>"

            if hasattr(theAnimalParameter, 'useSpecificGrazingLand'):
                specificLandText = "Yes" if theAnimalParameter.useSpecificGrazingLand else "No"
                html += f"<tr><td><b>Use Specific Grazing Land:</b></td><td>{specificLandText}</td></tr>"

            # Add fodder use if it exists
            if hasattr(theAnimalParameter, 'fodderUse') and theAnimalParameter.fodderUse:
                html += f"<tr><td><b>Fodder Use:</b></td><td>Yes</td></tr>"

            # Add fallow usage if it exists
            if hasattr(theAnimalParameter, 'fallowUsage'):
                fallowPriority = str(theAnimalParameter.fallowUsage).split('.')[-1].replace('_', ' ')
                html += f"<tr><td><b>Fallow Usage Priority:</b></td><td>{fallowPriority}</td></tr>"

            # Add raster name if it exists and is being used
            if hasattr(theAnimalParameter, 'rasterName') and theAnimalParameter.rasterName:
                html += f"<tr><td><b>Raster:</b></td><td>{theAnimalParameter.rasterName}</td></tr>"

            html += "</table>"
        else:
            html += "<p>No parameters selected for this animal.</p>"

        html += "</td>"
        html += "</tr>"
        html += "</table>"
        html += "</body>"

        return html

    def updateModelFromUI(self):
        """Update all model properties from the UI widgets."""
        if not hasattr(self, 'model'):
            LaUtils.debug.log("Model not found, cannot update from UI", "Error")
            return

        try:
            # Update slider values
            self.model.dietPercent = self.sliderDiet.value()
            self.model.meatPercent = self.sliderMeat.value() # Corresponds to wild animal %
            self.model.percentOfDietThatIsFromCrops = self.sliderCrop.value() # Corresponds to wild plant %

            # Update checkbox values
            self.model.mIncludeDairy = self.cboxIncludeDairy.isChecked()
            self.model.mLimitDairy = self.cboxLimitDairy.isChecked()
            self.model.mBaseOnPlants = self.cboxBaseOnPlants.isChecked()

            # Update spinbox values
            self.model.mLimitDairyPercent = self.sbLimitDairyPercent.value()
            self.model.mCaloriesPerPersonDaily = self.sbDailyCalories.value() # Check property name
            self.model.mDairyUtilisation = self.sbDairyUtilisation.value() # Check property name
            self.model.population = self.sbPopulation.value() # Check property name

            # Update combo box selections
            from la.lib.la import AreaUnits, EnergyType # Ensure imports
            self.model.commonLandAreaUnits = AreaUnits.Dunum if self.cbAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare
            self.model.specificLandEnergyType = EnergyType.KCalories if self.cbCommonLandEnergyType.currentText() == "KCalories" else EnergyType.TDN

            # Update common raster value
            myCommonRasterValue = self.sbCommonRasterValue.value()
            mySelectedAreaUnit = self.model.commonLandAreaUnits # Use the already set unit
            self.model.areaUnits = mySelectedAreaUnit
            self.model.commonLandValue = self.cbAreaUnits.currentText() # Ensure this is set correctly


            # Note: Selected animals/crops are updated directly in updateCrop/AnimalCalculations

            LaUtils.debug.log("Model updated successfully from UI", "Model")
        except Exception as e:
            LaUtils.debug.log(f"Error updating model from UI: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Traceback: {traceback.format_exc()}", "Error")

    def updateCropCalculations(self, theCrop: LaCrop):
        """Update calculations for a crop.
        Args:
            crop: The crop object to calculate values for
        """
        try:
            # Get the crop GUID
            myCropGuid = str(theCrop.guid) # Ensure string

            # Get parameter if available
            myParameterGuid = None
            if myCropGuid in self.mCropsMap:
                myParameterGuid = str(self.mCropsMap[myCropGuid][1]) # Ensure string

            # Setup model with proper parameters from UI first
            self.updateModelFromUI() # *** This call needs the method to exist ***

            # Get selected crops and animals for this specific calculation context
            mySelectedCropsDict: dict[str, str] = {myCropGuid: myParameterGuid} if myParameterGuid else {} # Only calculate for this crop
            mySelectedAnimalsDict: dict[str, str] = {}
            for guid, value in self.mAnimalsMap.items():
                if value[0]:  # If checked
                    mySelectedAnimalsDict[str(guid)] = str(value[1]) # Ensure strings

            # Check if essential selections are made
            if not mySelectedAnimalsDict:
                self.textBrowserResultsCrop.setText("No animals selected. Please select at least one animal on the 'Diet' tab.")
                return
            if not mySelectedCropsDict:
                self.textBrowserResultsCrop.setText("No parameter selected for this crop.")
                # Optionally clear other fields or return
                # return # Decide if calculation should proceed without parameters

            # Set model parameters for the calculation run
            self.model.animals = mySelectedAnimalsDict
            self.model.crops = mySelectedCropsDict

            # Calculate diet labels based on settings
            myDietLabels = None
            if self.model.mBaseOnPlants:
                if self.model.mIncludeDairy:
                    myDietLabels = self.model.doCalcsPlantsFirstIncludeDairy()
                else:
                    myDietLabels = self.model.doCalcsPlantsFirstDairySeparate()
            else:
                if self.model.mIncludeDairy:
                    myDietLabels = self.model.doCalcsAnimalsFirstIncludeDairy()
                else:
                    myDietLabels = self.model.doCalcsAnimalsFirstDairySeparate()

            # Get report from calculations
            if myDietLabels:
                report_map = myDietLabels.mCropCalcsReportMap
                if myCropGuid in report_map:
                    report_pair = report_map[myCropGuid]
                    report_string = report_pair[0]
                    self.textBrowserResultsCrop.setText(report_string)
                    LaUtils.debug.log("Crop calculation report displayed", "Calculation")
                else:
                    self.textBrowserResultsCrop.setText(f"No calculation results available for this crop (GUID: {myCropGuid}). Check parameters.")
            else:
                self.textBrowserResultsCrop.setText("Calculation failed or did not produce results. Check model configuration and logs.")
        except AttributeError as ae:
            # Catch the specific error if updateModelFromUI is still missing
            if 'updateModelFromUI' in str(ae):
                LaUtils.debug.log(f"Critical Error: updateModelFromUI method is missing!", "Error")
                self.textBrowserResultsCrop.setText("Error: Required method 'updateModelFromUI' is missing.")
            else:
                LaUtils.debug.log(f"Attribute error during crop calculations: {str(ae)}", "Error")
                self.textBrowserResultsCrop.setText(f"Error: {str(ae)}")
        except Exception as e:
            LaUtils.debug.log(f"Error updating crop calculations: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            self.textBrowserResultsCrop.setText(f"Error in calculations: {str(e)}")

    def updateAnimalCalculations(self, theAnimal: LaAnimal):
        """Update calculations for an animal.
        Args:
            animal: The animal object to calculate values for.
        """
        try:
            # Get the animal GUID
            animalGuid = str(theAnimal.guid) # Ensure string

            # Get parameter if available
            parameter_guid = None
            if animalGuid in self.mAnimalsMap:
                parameter_guid = str(self.mAnimalsMap[animalGuid][1]) # Ensure string

            # Setup model with proper parameters from UI first
            self.updateModelFromUI() # *** This call needs the method to exist ***

            # Get selected animals and crops for this specific calculation context
            selected_animals = {animalGuid: parameter_guid} if parameter_guid else {} # Only calculate for this animal
            selected_crops = {}
            for guid, value in self.mCropsMap.items():
                if value[0]:  # If checked
                    selected_crops[str(guid)] = str(value[1]) # Ensure strings

            # Check if essential selections are made
            if not selected_crops:
                self.textBrowserResultsAnimals.setText("No crops selected. Please select at least one crop on the 'Diet' tab.")
                return
            if not selected_animals:
                 self.textBrowserResultsAnimals.setText("No parameter selected for this animal.")
                 # Optionally clear other fields or return
                 # return # Decide if calculation should proceed without parameters

            # Set model parameters for the calculation run
            if hasattr(self, 'model'):
                self.model.animals = selected_animals
                self.model.crops = selected_crops

                # Calculate diet labels based on settings
                myDietLabels = LaDietLabels()
                if self.model.mBaseOnPlants:
                    if self.model.mIncludeDairy:
                        myDietLabels = self.model.doCalcsPlantsFirstIncludeDairy()
                    else:
                        myDietLabels = self.model.doCalcsPlantsFirstDairySeparate()
                else:
                    if self.model.mIncludeDairy:
                        myDietLabels = self.model.doCalcsAnimalsFirstIncludeDairy()
                    else:
                        myDietLabels = self.model.doCalcsAnimalsFirstDairySeparate()

                # Get report from calculations
                if myDietLabels and hasattr(myDietLabels, '_animalCalcsReportMap'):
                    report_map = myDietLabels.mAnimalCalcsReportMap
                    if animalGuid in report_map:
                        report_pair = report_map[animalGuid]
                        report_string = report_pair[0]
                        self.textBrowserResultsAnimals.setText(report_string)
                        LaUtils.debug.log("Animal calculation report displayed", "Calculation")
                    else:
                        self.textBrowserResultsAnimals.setText(f"No calculation results available for this animal (GUID: {animalGuid}). Check parameters.")
                elif myDietLabels:
                     self.textBrowserResultsAnimals.setText("Calculations completed but no specific animal report was generated.")
                else:
                    self.textBrowserResultsAnimals.setText("Calculation failed or did not produce results. Check model configuration and logs.")
        except AttributeError as ae:
             # Catch the specific error if updateModelFromUI is still missing
             if 'updateModelFromUI' in str(ae):
                  LaUtils.debug.log(f"Critical Error: updateModelFromUI method is missing!", "Error")
                  self.textBrowserResultsAnimals.setText("Error: Required method 'updateModelFromUI' is missing.")
             else:
                  LaUtils.debug.log(f"Attribute error during animal calculations: {str(ae)}", "Error")
                  self.textBrowserResultsAnimals.setText(f"Error: {str(ae)}")
        except Exception as e:
            LaUtils.debug.log(f"Error updating animal calculations: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
            self.textBrowserResultsAnimals.setText(f"Error in calculations: {str(e)}")

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

        # Connect checkboxes
        self.cboxIncludeDairy.toggled.connect(self.on_cboxIncludeDairy_toggled)
        self.cboxLimitDairy.toggled.connect(self.on_cboxLimitDairy_toggled)
        self.cboxBaseOnPlants.toggled.connect(self.on_cboxBaseOnPlants_toggled)

        # Connect spinboxes
        self.sbLimitDairyPercent.valueChanged.connect(self.on_sbLimitDairyPercent_valueChanged)
        self.sbDailyCalories.valueChanged.connect(self.on_sbDailyCalories_valueChanged)
        self.sbDairyUtilisation.valueChanged.connect(self.on_sbDairyUtilisation_valueChanged)
        self.sbPopulation.valueChanged.connect(self.on_sbPopulation_valueChanged)
        self.sbCommonRasterValue.valueChanged.connect(self.on_sbCommonRasterValue_valueChanged)

        # Connect combo boxes
        self.cbAreaUnits.currentIndexChanged.connect(self.on_cbAreaUnits_changed)
        self.cbCommonLandEnergyType.currentIndexChanged.connect(self.on_cbCommonLandEnergyType_changed)

        # Connect list widgets and tables
        self.treeHelp.currentItemChanged.connect(self.helpItemClicked)
        self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)
        self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)
        self.tblAnimals.cellChanged.connect(self.animalCalcSelectionChanged)
        self.tblCrops.cellClicked.connect(self.cropCellClicked)
        self.tblCrops.cellChanged.connect(self.cropCalcSelectionChanged)
        self.cbDebug.clicked.connect(self.on_cbDebug_clicked)

    def on_sbCommonRasterValue_valueChanged(self, value):
        """Handle common raster value changes.

        This method updates the model's common raster value when the user
        changes the value in the common raster value spinbox.

        Args:
            value: The new value from the spinbox
        """
        if hasattr(self, 'model'):
            from la.lib.la import AreaUnits
            LaUtils.debug.log(f"Common Raster Value changed to: {value}", "Settings")

            # Get the current area units
            selected_area_unit = AreaUnits.Dunum if self.cbAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare

            # Update the model with the new value
            if hasattr(self.model, 'setCommonLandValue'):
                self.model.setCommonLandValue(value, selected_area_unit)
            elif hasattr(self.model, 'commonLandValue'):
                self.model.commonLandValue = value

            # Recalculate with the new value
            self.setDietLabels()

    # Add the missing checkbox handlers here
    def on_cboxIncludeDairy_toggled(self, checked):
        """Handle include dairy checkbox changes.

        This method updates the model's includeDairy property when the user
        toggles the Include Dairy checkbox.

        Args:
            checked: Boolean indicating if the checkbox is checked
        """
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Include Dairy checkbox toggled: {checked}", "Diet")
            self.model.mIncludeDairy = checked
            self.setDietLabels()

    def on_cboxLimitDairy_toggled(self, checked):
        """Handle limit dairy checkbox changes.

        This method updates the model's limitDairy property when the user
        toggles the Limit Dairy checkbox.

        Args:
            checked: Boolean indicating if the checkbox is checked
        """
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Limit Dairy checkbox toggled: {checked}", "Diet")
            self.model.mLimitDairy = checked
            self.setDietLabels()

    def on_cboxBaseOnPlants_toggled(self, checked):
        """Handle base on plants checkbox changes."""
        # ... existing implementation ...
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Base On Plants checkbox toggled: {checked}", "Diet")
            self.model.mBaseOnPlants = checked
            self.setDietLabels()

    # Add the missing spinbox handlers here
    def on_sbLimitDairyPercent_valueChanged(self, value):
        """Handle limit dairy percent spinbox changes."""
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Limit Dairy Percent changed to: {value}", "Diet")
            self.model.mLimitDairyPercent = value
            self.setDietLabels()

    def on_sbDailyCalories_valueChanged(self, value):
        """Handle daily calories spinbox changes."""
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Daily Calories changed to: {value}", "Diet")
            # Update the correct model property (adjust name if needed)
            if hasattr(self.model, 'mCaloriesPerPersonDaily'):
                 self.model.mCaloriesPerPersonDaily = value
            elif hasattr(self.model, 'caloriesPerPersonDaily'):
                 self.model.mCaloriesPerPersonDaily = value
            self.setDietLabels()

    def on_sbDairyUtilisation_valueChanged(self, value):
        """Handle dairy utilisation spinbox changes."""
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Dairy Utilisation changed to: {value}", "Diet")
            # Update the correct model property (adjust name if needed)
            if hasattr(self.model, 'dairyUtilisation'):
                self.model.mDairyUtilisation = value
            self.setDietLabels()

    def on_sbPopulation_valueChanged(self, value):
        """Handle population spinbox changes."""
        if hasattr(self, 'model'):
            LaUtils.debug.log(f"Population changed to: {value}", "Diet")
            # Update the correct model property (adjust name if needed)
            if hasattr(self, 'model'):
                if hasattr(self.model, 'population'):
                    self.model.population = value
                elif hasattr(self.model, 'mPopulation'):
                     self.model.mPopulation = value
            self.setDietLabels()

    def on_cbAreaUnits_changed(self, index):
        """Handle area units combo box changes."""
        # ... existing implementation ...
        if hasattr(self, 'model'):
            from la.lib.la import AreaUnits # Ensure import is present
            selected_text = self.cbAreaUnits.currentText()
            selected_area_unit = AreaUnits.Dunum if selected_text == "Dunum" else AreaUnits.Hectare
            LaUtils.debug.log(f"Area Units changed to: {selected_text}", "Settings")
            # Update model property
            self.model.commonLandAreaUnits = selected_area_unit
            self.setDietLabels()

    def on_cbCommonLandEnergyType_changed(self, index):
        """Handle energy type combo box changes."""
        # ... existing implementation ...
        if hasattr(self, 'model'):
            from la.lib.la import EnergyType # Ensure import is present
            selected_text = self.cbCommonLandEnergyType.currentText()
            selected_energy_type = EnergyType.KCalories if selected_text == "KCalories" else EnergyType.TDN
            LaUtils.debug.log(f"Common Land Energy Type changed to: {selected_text}", "Settings")
            # Update model property
            self.model.specificLandEnergyType = selected_energy_type
            self.setDietLabels()

    def updateBasicLabels(self):
        """Update basic diet labels without performing heavy calculations.
        This is called when percentages don't total 100% to provide immediate feedback
        while avoiding unnecessary heavy computation."""
        try:
            # Get values from UI
            myOverallPlantPercent = 100 - self.sliderDiet.value()  # Plant/Meat slider
            myOverallMeatPercent = self.sliderDiet.value()

            # Plant breakdown
            myTameCropPercent = self.sliderCrop.value()  # Tame/Wild plant slider
            myWildPlantPercent = 100 - self.sliderCrop.value()

            # Meat breakdown
            myTameMeatPercent = self.sliderMeat.value()  # Tame/Wild meat slider
            myWildMeatPercent = 100 - self.sliderMeat.value()

            # Calculate actual percentages of total diet
            myCropPortion = (myOverallPlantPercent * myTameCropPercent) / 100.0
            myWildPlantPortion = (myOverallPlantPercent * myWildPlantPercent) / 100.0
            myTameMeatPortion = (myOverallMeatPercent * myTameMeatPercent) / 100.0
            myWildMeatPortion = (myOverallMeatPercent * myWildMeatPercent) / 100.0

            # Update percentage labels
            self.labelPortionPlants.setText(f"{myOverallPlantPercent:.1f}")
            self.labelPortionMeat.setText(f"{myOverallMeatPercent:.1f}")
            self.labelPortionCrops.setText(f"{myCropPortion:.1f}")
            self.labelPortionTameMeat.setText(f"{myTameMeatPortion:.1f}")
            self.labelPortionWildMeat.setText(f"{myWildMeatPortion:.1f}")
            self.labelPortionWildPlants.setText(f"{myWildPlantPortion:.1f}")

            # Calculate basic calories
            myDailyCals = self.sbDailyCalories.value()
            myPopulation = self.sbPopulation.value()
            myTotalAnnualMcals = (myDailyCals * myPopulation * 365) / 1000000.0  # Convert to MCals

            # Update calorie labels
            self.labelCaloriesSettlement.setText(f"{myTotalAnnualMcals:.1f}")
            self.labelCaloriesIndividual.setText(f"{(myDailyCals * 365 / 1000.0):.1f}") # this displays as kCals so we need to adjust it

            # Update component calorie labels
            myCropMcals = myTotalAnnualMcals * myCropPortion * 0.01
            myTameMeatMcals = myTotalAnnualMcals * myTameMeatPortion * 0.01
            myWildMeatMcals = myTotalAnnualMcals * myWildMeatPortion * 0.01
            myWildPlantMcals = myTotalAnnualMcals * myWildPlantPortion * 0.01

            self.labelCaloriesCrops.setText(f"{myCropMcals:.1f}")
            self.labelCaloriesTameMeat.setText(f"{myTameMeatMcals:.1f}")
            self.labelCaloriesWildMeat.setText(f"{myWildMeatMcals:.1f}")
            self.labelCaloriesWildPlants.setText(f"{myWildPlantMcals:.1f}")

            # Clear dairy-related labels since we can't calculate them
            self.labelPortionAllDairy.setText("0.0")
            self.labelPortionDairy.setText("0.0")
            self.labelCaloriesDairy.setText("0.0")
            self.labelDairySurplus.setText("Dairy contributions not calculated until plants and animals are both 100%")

            LaUtils.debug.log("Basic diet labels updated (no full calculation)", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error updating basic labels: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")
