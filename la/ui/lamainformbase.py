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
from qgis.PyQt import QtWidgets
from qgis.PyQt import uic
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QFile
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

        # make the form's buttons work
        # region PUSH BUTTONS
        self.pushButtonExit.clicked.connect(self.close)
        self.pbnNewCrop.clicked.connect(self.on_clicked_pbnNewCrop)
        self.pbnNewCropParameter.clicked.connect(self.on_clicked_pbnNewCropParameter)
        self.pbnNewAnimal.clicked.connect(self.on_clicked_pbnNewAnimal)
        self.pbnNewAnimalParameter.clicked.connect(self.on_clicked_pbnNewAnimalParameter)
        #endregion

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
        self.tbReport.append("Item clicked in help browser: " + theCurrentItem.text(0))
        myQFile = QFile(":/" + theCurrentItem.text(0) + ".html")
        myQFile.open(QFile.ReadOnly | QFile.Text)
        istream = QTextStream(myQFile)
        self.textHelp.setHtml(istream.readAll())
        myQFile.close()

    def on_clicked_pbnNewCrop(self):
        print("open Manage Crops window printed")
        self.tbReport.append("Manage Crops button clicked")
        myCropManager = LaCropManager()  # Use implementation class
        myCropManager.show()
        myCropManager.exec_()

    def on_clicked_pbnNewCropParameter(self):
        print("open Crop Parameters window printed")
        self.tbReport.append("Manage Crop Parameters button clicked")
        myCropParameterManager = LaCropParameterManager()  # Use implementation class
        myCropParameterManager.show()
        myCropParameterManager.exec_()

    def on_clicked_pbnNewAnimal(self):
        print("open Manage Animals window printed")
        self.tbReport.append("Manage Animals button clicked")
        myAnimalManager = LaAnimalManager()  # Use implementation class
        myAnimalManager.show()
        myAnimalManager.exec_()

    def on_clicked_pbnNewAnimalParameter(self):
        print("open Animal Parameters window")
        self.tbReport.append("Manage Animal Parameters button clicked")
        myAnimalParameterManager = LaAnimalParameterManager()  # Use implementation class
        myAnimalParameterManager.show()
        myAnimalParameterManager.exec_()

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
        myAnimalsMap = LaUtils.getAvailableAnimals()
        myAnimalParametersMap = LaUtils.getAvailableAnimalParameters()
        for myGuid, myAnimal in myAnimalsMap.items():
            myName = myAnimal.name
            myValue = self.mAnimalsMap.get(myGuid, (False, ""))
            if myGuid not in self.mAnimalsMap:
                self.mAnimalsMap[myGuid] = myValue
            myIcon = QIcon(":/localdata.png")
            self.tblAnimals.insertRow(myCurrentRow)
            mypUsedItem = QtWidgets.QTableWidgetItem("Used?")
            if myValue[0]:
                mypUsedItem.setCheckState(QtCore.Qt.Checked)
                myItem = QtWidgets.QListWidgetItem(myAnimal.name)
                myItem.setData(QtCore.Qt.UserRole, myAnimal.guid)
                self.listWidgetCalculationsAnimal.addItem(myItem)
            else:
                mypUsedItem.setCheckState(QtCore.Qt.Unchecked)
                myItem = QtWidgets.QListWidgetItem(myAnimal.name)
                myItem.setData(QtCore.Qt.UserRole, myAnimal.guid)
                self.listWidgetCalculationsAnimal.takeItem(self.listWidgetCalculationsAnimal.row(myItem))
            self.tblAnimals.setItem(myCurrentRow, 0, mypUsedItem)
            mypNameItem = QtWidgets.QTableWidgetItem(myAnimal.name)
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
                myItem = QtWidgets.QListWidgetItem(myCrop.name)
                myItem.setData(QtCore.Qt.UserRole, myCrop.guid)
                self.listWidgetCalculationsCrop.addItem(myItem)
            else:
                mypUsedItem.setCheckState(QtCore.Qt.Unchecked)
            self.tblCrops.setItem(myCurrentRow, 0, mypUsedItem)
            mypNameItem = QtWidgets.QTableWidgetItem(myCrop.name)
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
                        myRunningPercentage += myCropParameter.percentTameCrop
                        myItem = QtWidgets.QListWidgetItem(myCrop.name)
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
        index = combo.findData(default)
        if index >= 0:
            combo.setCurrentIndex(index)

    def setDietLabels(self):
        # Implement the logic to set diet labels based on the current model
        pass

    def helpItemClicked(self, current, previous):
        # Implement the logic to handle help item clicked
        pass

    def cropCalcClicked(self, current, previous):
        # Implement the logic to handle crop calculation item clicked
        pass

    def animalCalcClicked(self, current, previous):
        # Implement the logic to handle animal calculation item clicked
        pass

    def animalCellClicked(self, row, column):
        # Implement the logic to handle animal cell clicked
        pass

    def animalCalcSelectionChanged(self, row, column):
        # Implement the logic to handle animal calculation selection changed
        pass

    def cropCellClicked(self, row, column):
        # Implement the logic to handle crop cell clicked
        pass

    def cropCalcSelectionChanged(self, row, column):
        # Implement the logic to handle crop calculation selection changed
        pass

    def on_cbDebug_clicked(self):
        # Implement the logic to handle debug checkbox clicked
        pass