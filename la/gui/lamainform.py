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

from la.lib.laanimal import LaAnimal
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QFile, QTextStream
from qgis.PyQt.QtGui import QIcon

# Import the base UI class
from la.ui.lamainformbase import LaMainFormBase

# Import dialog forms (implementation classes, not base classes)
from la.gui.lacropmanager import LaCropManager
from la.gui.lacropparametermanager import LaCropParameterManager
from la.gui.laanimalmanager import LaAnimalManager
from la.gui.laanimalparametermanager import LaAnimalParameterManager

# Import library classes
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils


class LaMainForm(LaMainFormBase):
    """Main form for the LanduseAnalyst plugin."""

    def __init__(self, parent=None):
        """Constructor for LaMainForm."""
        super(LaMainForm, self).__init__(parent)

        # Initialize maps
        self.mAnimalsMap = {}
        self.mCropsMap = {}
        self.mSelectedAnimalsMap = {}
        self.mSelectedCropsMap = {}
        self.mWeightCounter = 0

        # Connect all signals and slots
        self.connectSignalsSlots()

        # Initialize combo boxes
        self.initializeComboBoxes()

        # Load data
        self.loadAnimals()
        self.loadCrops()

    def connectSignalsSlots(self):
        """Connect all signals to their corresponding slots."""
        # Button connections
        self.pushButtonExit.clicked.connect(self.close)
        self.pbnNewCrop.clicked.connect(self.on_clicked_pbnNewCrop)
        self.pbnNewCropParameter.clicked.connect(self.on_clicked_pbnNewCropParameter)
        self.pbnNewAnimal.clicked.connect(self.on_clicked_pbnNewAnimal)
        self.pbnNewAnimalParameter.clicked.connect(self.on_clicked_pbnNewAnimalParameter)

        # Slider connections
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)

        # Tree and list widget connections
        self.treeHelp.currentItemChanged.connect(self.current_item_changed)
        self.treeHelp.currentItemChanged.connect(self.helpItemClicked)
        self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)
        self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)

        # Table connections
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)
        self.tblAnimals.cellChanged.connect(self.animalCalcSelectionChanged)
        self.tblCrops.cellClicked.connect(self.cropCellClicked)
        self.tblCrops.cellChanged.connect(self.cropCalcSelectionChanged)

        # Miscellaneous connections
        self.cbDebug.clicked.connect(self.on_cbDebug_clicked)
        self.pushButtonExit.clicked.connect(QtWidgets.qApp.quit)

    def initializeComboBoxes(self):
        """Initialize combo box items."""
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.cbCommonLandEnergyType.addItem("KCalories")
        self.cbCommonLandEnergyType.addItem("TDN")

    def on_clicked_pbnNewCrop(self):
        """Open the Crop Manager dialog."""
        print("open Manage Crops window printed")
        self.tbReport.append("Manage Crops button clicked")

        # Create and show the crop manager form
        myCropManager = LaCropManager(self.mCropsMap, self)
        result = myCropManager.exec_()

        # Handle the result
        if result == QtWidgets.QDialog.Accepted:
            self.mCropsMap = myCropManager.getCrops()
            self.loadCrops()  # Refresh crops list

    def on_clicked_pbnNewCropParameter(self):
        """Open the Crop Parameter Manager dialog."""
        print("open Crop Parameters window printed")
        self.tbReport.append("Manage Crop Parameters button clicked")

        # Create and show the crop parameter form
        myCropParameterManager = LaCropParameterManager(self)
        result = myCropParameterManager.exec_()

        # Handle the result
        if result == QtWidgets.QDialog.Accepted:
            self.loadCrops()  # Refresh crops list

    def on_clicked_pbnNewAnimal(self):
        """Open the Animal Manager dialog."""
        print("open Manage Animals window printed")
        self.tbReport.append("Manage Animals button clicked")

        # Create and show the animal manager form
        myAnimalManager = LaAnimalManager(self.mAnimalsMap, self)
        result = myAnimalManager.exec_()

        # Handle the result
        if result == QtWidgets.QDialog.Accepted:
            self.mAnimalsMap = myAnimalManager.getAnimals()
            self.loadAnimals()  # Refresh animals list

    def on_clicked_pbnNewAnimalParameter(self):
        """Open the Animal Parameter Manager dialog."""
        print("open Animal Parameters window")
        self.tbReport.append("Manage Animal Parameters button clicked")

        # Create and show the animal parameter form
        myAnimalParameterManager = LaAnimalParameterManager(self)
        result = myAnimalParameterManager.exec_()

        # Handle the result
        if result == QtWidgets.QDialog.Accepted:
            self.loadAnimals()  # Refresh animals list

    def on_sliderDiet_valueChanged(self, theValue):
        """Handle diet slider value change."""
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelMeatPercent.setText(myMinString)
        self.labelCropPercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def on_sliderMeat_valueChanged(self, theValue):
        """Handle meat slider value change."""
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelMeatWildPercent.setText(myMinString)
        self.labelMeatTamePercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def on_sliderCrop_valueChanged(self, theValue):
        """Handle crop slider value change."""
        myMinString = str(theValue)
        myMaxString = str(100 - theValue)
        self.labelCropWildPercent.setText(myMinString)
        self.labelCropTamePercent.setText(myMaxString)
        self.setDietLabels()  # recalculates model (to update the diet labels!)

    def setModel(self, *args):
        """Set up the model based on current form values."""
        from la.lib.la import AreaUnits
        self.mSelectedCropsMap.clear()
        self.mSelectedAnimalsMap.clear()
        mySelectedAreaUnit = AreaUnits(self.cbAreaUnits.currentText())
        myCommonRasterValue = int(self.sbCommonRasterValue.value())
        myAreaUnits = 'Dunum' if mySelectedAreaUnit else 'Hectare'
        print(mySelectedAreaUnit, myAreaUnits, myCommonRasterValue)

    def loadAnimals(self):
        """Load animals from disk and populate the UI."""
        self.listWidgetCalculationsAnimal.clear()
        myModel = LaModel()
        self.tblAnimals.clear()
        self.tblAnimals.setRowCount(0)
        self.tblAnimals.setColumnCount(4)
        myCurrentRow = 0
        myRunningPercentage = 0.0
        myAnimalsMap: dict[str, LaAnimal] = LaUtils.getAvailableAnimals()
        myAnimalParametersMap    = LaUtils.getAvailableAnimalParameters()
        for myGuid, myAnimal in myAnimalsMap.items():
            myName: QtCore.pyqtProperty = myAnimal.name
            myValue = self.mAnimalsMap.get(myGuid, (False, ""))
            if myGuid not in self.mAnimalsMap:
                self.mAnimalsMap[myGuid] = myValue
            myIcon = QIcon(":/localdata.png")
            self.tblAnimals.insertRow(myCurrentRow)
            mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
            if myValue[0]:
                mypUsedItem.setCheckState(QtCore.Qt.Checked)
                myItem = QtWidgets.QListWidgetItem(str(myAnimal.name))
                myItem.setData(QtCore.Qt.UserRole, myAnimal.guid)
                self.listWidgetCalculationsAnimal.addItem(myItem)
            else:
                mypUsedItem.setCheckState(QtCore.Qt.Unchecked)
                myItem = QtWidgets.QListWidgetItem(str(myAnimal.name))
                myItem.setData(QtCore.Qt.UserRole, myAnimal.guid)
                self.listWidgetCalculationsAnimal.takeItem(self.listWidgetCalculationsAnimal.row(myItem))
            self.tblAnimals.setItem(myCurrentRow, 0, mypUsedItem)
            mypNameItem = QtWidgets.QTableWidgetItem(str(myAnimal.name))
            mypNameItem.setData(QtCore.Qt.UserRole, myGuid)
            self.tblAnimals.setItem(myCurrentRow, 1, mypNameItem)
            mypNameItem.setIcon(myIcon)
            mypCombo = QtWidgets.QComboBox(self)
            for myParameterGuid, myAnimalParameter in myAnimalParametersMap.items():
                myParameterName = f"{myAnimalParameter.name}  ({myAnimalParameter.description})"
                if myGuid != myAnimalParameter.animalGuid:
                    continue
                if not myValue[1]:
                    myValue = (myValue[0], myParameterGuid)
                if myValue[1] == myAnimalParameter.guid:
                    if myValue[0]:
                        myRunningPercentage += myAnimalParameter.percentTameMeat
                    mypPercentItem = QtWidgets.QTableWidgetItem(str(myAnimalParameter.percentTameMeat))
                    self.tblAnimals.setItem(myCurrentRow, 3, mypPercentItem)
                mypCombo.addItem(myIcon, myParameterName, myParameterGuid)
            self.setComboToDefault(mypCombo, myValue[1])
            self.mAnimalsMap[myGuid] = myValue
            self.tblAnimals.setCellWidget(myCurrentRow, 2, mypCombo)
            myCurrentRow += 1
        myIcon = QIcon(":/status_ok.png") if myRunningPercentage == 100 else QIcon(":/status_error.png")
        myPercentItem = str(myRunningPercentage)
        self.labelAnimalCheck.setText(f"{myPercentItem}%")

    def loadCrops(self):
        """Load crops from disk and populate the UI."""
        self.listWidgetCalculationsCrop.clear()
        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(4)
        myCurrentRow = 0
        myRunningPercentage = 0.0
        myCropsMap = LaUtils.getAvailableCrops()
        myCropParametersMap = LaUtils.getAvailableCropParameters()
        for myGuid, myCrop in myCropsMap.items():
            myName = myCrop.name
            myValue = self.mCropsMap.get(myGuid, (False, ""))
            if myGuid not in self.mCropsMap:
                self.mCropsMap[myGuid] = myValue
            myIcon = QIcon(":/localdata.png")
            self.tblCrops.insertRow(myCurrentRow)
            mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
            if myValue[0]:
                mypUsedItem.setCheckState(QtCore.Qt.Checked)
                myItem = QtWidgets.QListWidgetItem(str(myCrop.name))
                myItem.setData(QtCore.Qt.UserRole, myCrop.guid)
                self.listWidgetCalculationsCrop.addItem(myItem)
            else:
                mypUsedItem.setCheckState(QtCore.Qt.Unchecked)
            self.tblCrops.setItem(myCurrentRow, 0, mypUsedItem)
            mypNameItem = QtWidgets.QTableWidgetItem(str(myCrop.name))
            mypNameItem.setData(QtCore.Qt.UserRole, myGuid)
            self.tblCrops.setItem(myCurrentRow, 1, mypNameItem)
            mypNameItem.setIcon(myIcon)
            mypCombo = QtWidgets.QComboBox(self)
            for myParameterGuid, myCropParameter in myCropParametersMap.items():
                myParameterName = f"{myCropParameter.name}  ({myCropParameter.description})"
                if myGuid != myCropParameter.cropGuid:
                    continue
                if not myValue[1]:
                    myValue = (myValue[0], myParameterGuid)
                if myValue[1] == myCropParameter.guid:
                    if myValue[0]:
                        myRunningPercentage += float(str(myCropParameter.percentTameCrop))
                        myItem = QtWidgets.QListWidgetItem(str(myCrop.name))
                        myItem.setData(QtCore.Qt.UserRole, myCrop.guid)
                        self.listWidgetCalculationsCrop.addItem(myItem)
                    mypPercentItem = QtWidgets.QTableWidgetItem(str(myCropParameter.percentTameCrop))
                    self.tblCrops.setItem(myCurrentRow, 3, mypPercentItem)
                mypCombo.addItem(myIcon, myParameterName, myParameterGuid)
            self.setComboToDefault(mypCombo, myValue[1])
            self.mCropsMap[myGuid] = myValue
            self.tblCrops.setCellWidget(myCurrentRow, 2, mypCombo)
            myCurrentRow += 1
        myIcon = QIcon(":/status_ok.png") if myRunningPercentage == 100 else QIcon(":/status_error.png")
        myPercentItem = str(myRunningPercentage)
        self.labelCropCheck.setText(f"{myPercentItem}%")

    def setComboToDefault(self, combo, default):
        """Set a combo box to a specified default value."""
        index = combo.findData(default)
        if index >= 0:
            combo.setCurrentIndex(index)

    def current_item_changed(self, theCurrentItem, thePreviousItem):
        """Handle the change of current item in help tree."""
        self.tbReport.append("Item clicked in help browser: " + theCurrentItem.text(0))
        myQFile = QFile(":/" + theCurrentItem.text(0) + ".html")
        myQFile.open(QFile.ReadOnly | QFile.Text)
        istream = QTextStream(myQFile)
        self.textHelp.setHtml(istream.readAll())
        myQFile.close()

    def setDietLabels(self):
        """Set diet labels based on the current model state."""
        # Implement setting diet labels logic here
        pass

    def helpItemClicked(self, current, previous):
        """Handle help item selection."""
        # Additional help item processing logic here
        pass

    def cropCalcClicked(self, current, previous):
        """Handle click on crop calculation item."""
        # Implement crop calculation click handling here
        pass

    def animalCalcClicked(self, current, previous):
        """Handle click on animal calculation item."""
        # Implement animal calculation click handling here
        pass

    def animalCellClicked(self, row, column):
        """Handle click on animal table cell."""
        # Implement animal cell click handling here
        pass

    def cropCellClicked(self, row, column):
        """Handle click on crop table cell."""
        # Implement crop cell click handling here
        pass

    def animalCalcSelectionChanged(self, row, column):
        """Handle change in animal calculation selection."""
        # Implement animal calculation selection change handling here
        pass

    def cropCalcSelectionChanged(self, row, column):
        """Handle change in crop calculation selection."""
        # Implement crop calculation selection change handling here
        pass

    def on_cbDebug_clicked(self):
        """Handle debug checkbox click."""
        # Implement debug checkbox handling here
        pass