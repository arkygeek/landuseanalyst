# -*- coding: utf-8 -*-
"""****************************************************************
 LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
 of a settlement (with respect to required land needed for food production).
 Land area targets for each food source supplied to the model are calculated based
 on a multitude of demographic and dietary inputs.
******************************************************************
    begin                : 2022-03-22
    copyright            : (C) 2022 by Dr. Jason S. Jorgenson
    email                : jjorgenson@gmail.com
    git sha              : $Format:%H$
******************************************************************
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
***************************************************************"""

import os
from typing import Dict

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUiType
from qgis.PyQt.QtCore import (
        QSettings, QDir, QSettings, QPoint, QSize, Qt)
from qgis.PyQt.QtWidgets import (
        QTableWidgetItem, QMessageBox, QHeaderView, QTableWidgetItem)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import Qt
# local imports
from la.lib.lacrop import LaCrop
from la.gui.lacropparametermanager import LaCropParameterManager
from la.lib.lautils import LaUtils
from la.lib.lagrass import LaGrass
from la.lib.laanimal import LaAnimal
from la.lib.lacropparameter import LaCropParameter
from la.lib.la import AreaUnits
from la.lib.laguid import LaGuid

Ui_LaCropParameterManagerBase, _ = loadUiType(
	os.path.join(
		os.path.dirname(__file__),
		"lacropparametermanagerbase.ui"
	)
)

print(f"Ui_LaCropParameterManagerBase: {Ui_LaCropParameterManagerBase}")
# @TODO remove the above print statement after testing

class LaCropParameterManagerBase(QDialog, Ui_LaCropParameterManagerBase):
	
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(LaCropParameterManagerBase, self).__init__(parent, flags)
        self.setupUi(self)
        self.readSettings()
        self.tblCropParameterProfiles.cellClicked.connect(self.cellClicked)
        myList = []
        myGrass = LaGrass()
        myMapsetList = "" #myGrass.getMapsetList() @TODO get Grass stuff working
        # myIterator1 = iter(myMapsetList)
        # while myIterator1.hasNext():
        #     myList += myGrass.getRasterList(myIterator1.next())
        self.cboRaster.addItems(myList)
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)
        self.lblCropPic.setScaledContents(True)
        
        # myCropsMap: Dict[str, LaCrop] = LaUtils.getAvailableCrops()
        
        # for _ , myCrop in myCropsMap.items(): # if at some point in the future I do need to use the keys, I can simply change the _ back to key and add code that uses the key variable.
        #     myGuid = myCrop.guid()
        #     myName = myCrop.name()
        #     myIcon = QIcon()
        #     myIcon.addFile(":/localdata.png")
        #     self.cboCrop.addItem(myName, myGuid)
        self.cboCrop.currentIndexChanged.connect(self.on_cboCrop_changed)
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.refreshCropParameterTable()    
    
    def readSettings(self):
        """
        Reads the settings of the main window's position and size from QSettings 
        and sets the position and size of the current window accordingly.
        """
        mySettings = QSettings()
        pos = mySettings.value("mainwindow/pos", QPoint(200, 200))
        size = mySettings.value("mainwindow/size", QSize(400, 400))
        self.resize(size)
        self.move(pos)
    
    def writeSettings(self):
        mySettings = QSettings()
        mySettings.setValue("mainwindow/pos", self.pos())
        mySettings.setValue("mainwindow/size", self.size())

    def cellClicked(self, theRow, theColumn):
        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        myFileName = myGuid + ".xml"
        self.selectCropParameter(myFileName)
        myCrop = LaUtils.getCrop(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt))
        myAnimalPic = myCrop.imageFile()
        self.lblCropPic.setPixmap(myAnimalPic)

    def on_cboCrop_changed(self, theIndex):
        from PyQt5.QtCore import Qt
        myCrop = LaUtils.getCrop(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole))
        myCropPic = myCrop.imageFile()
        self.lblCropPic.setPixmap(myCropPic)

    def showCropParameter(self):
        self.leName.setText(self.mCropParameter.name())
        self.leDescription.setText(self.mCropParameter.description())
        self.setComboToDefault(self.cboCrop, self.mCropParameter.cropGuid())
        self.sbPercentTameCrop.setValue(self.mCropParameter.percentTameCrop())
        self.sbSpoilage.setValue(self.mCropParameter.spoilage())
        self.sbReseed.setValue(self.mCropParameter.reseed())
        self.grpCropRotation.setChecked(self.mCropParameter.cropRotation())
        self.sbFallowRatio.setValue(self.mCropParameter.fallowRatio())
        self.sbFallowValue.setValue(self.mCropParameter.fallowValue())
        self.cbAreaUnits.setCurrentIndex(self.mCropParameter.areaUnits())
        self.checkBoxUseCommonLand.setChecked(self.mCropParameter.useCommonLand())
        self.checkBoxUseSpecificLand.setChecked(self.mCropParameter.useSpecificLand())
        # self.cboRastere.setText(self.mCropParameter.rasterName())

    def on_toolCopy_clicked(self):
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if myGuid == "":
            return

        myOriginalFileName = LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myGuid + ".xml"
        myCropParameter = LaCropParameter()
        myCropParameter.fromXmlFile(myOriginalFileName)

        myCropParameter.guid = LaGuid()
        myNewFileName = LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myCropParameter.guid() + ".xml"
        myCropParameter.name = "Copy of " + myCropParameter.name()
        myCropParameter.toXmlFile(myNewFileName)
        self.refreshCropParameterTable(myCropParameter.guid())

    def on_toolNew_clicked(self):
        myCropParameter = LaCropParameter()
        myCropParameter.guid = LaGuid()
        self.mCropParameter = myCropParameter
        self.showCropParameter()

    def on_toolDelete_clicked(self):
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if myGuid != "":
            myFile = LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myGuid + ".xml"
            try:
                os.remove(myFile)
            except OSError:
                QMessageBox.warning(self, "Landuse Analyst", "Unable to delete file \n" + myFile)
            self.refreshCropParameterTable()

    def on_pbnApply_clicked(self):
        self.mCropParameter.setName(self.leName.text())
        self.mCropParameter.setDescription(self.leDescription.text())
        self.mCropParameter.setCropGuid(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole))
        self.mCropParameter.setPercentTameCrop(self.sbPercentTameCrop.value())
        self.mCropParameter.setSpoilage(self.sbSpoilage.value())
        self.mCropParameter.setReseed(self.sbReseed.value())
        self.mCropParameter.setCropRotation(self.grpCropRotation.isChecked())
        self.mCropParameter.setFallowRatio(self.sbFallowRatio.value())
        self.mCropParameter.setFallowValue(self.sbFallowValue.value())

        mySelectedAreaUnit = self.cbAreaUnits.currentText()
        if mySelectedAreaUnit == "Dunum":
            self.mCropParameter.setAreaUnits(AreaUnits.Dunum)
        elif mySelectedAreaUnit == "Hectare":
            self.mCropParameter.setAreaUnits(AreaUnits.Hectare)

        self.mCropParameter.setUseCommonLand(self.checkBoxUseCommonLand.isChecked())
        self.mCropParameter.setUseSpecificLand(self.checkBoxUseSpecificLand.isChecked())
        self.mCropParameter.setRasterName(self.cboRaster.currentText())
        self.mCropParameter.toXmlFile(LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + self.mCropParameter.guid() + ".xml")
        self.refreshCropParameterTable(self.mCropParameter.guid())

    def resizeEvent(self, theEvent):
        self.tblCropParameterProfiles.setColumnWidth(0, 0)
        self.tblCropParameterProfiles.setColumnWidth(1, self.tblCropParameterProfiles.width())
        self.tblCropParameterProfiles.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def refreshCropParameterTable(self, theGuid=None):
        pass
        """# self.mCropParameterMap.clear()
        self.tblCropParameterProfiles.clear()
        self.tblCropParameterProfiles.setRowCount(0)
        self.tblCropParameterProfiles.setColumnCount(2)

        # self.mCropParameterMap = LaUtils.getAvailableCropParameters()

        mySelectedRow = 0
        myCurrentRow = 0
        for myGuid, myCropParameter in self.mCropParameterMap.items():
            if theGuid == "":
                theGuid = myCropParameter.guid()
            if myCropParameter.guid() == theGuid:
                mySelectedRow = myCurrentRow

            self.tblCropParameterProfiles.insertRow(myCurrentRow)
            mypFileNameItem = QTableWidgetItem(myGuid)
            self.tblCropParameterProfiles.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(myCropParameter.name() + "  (" + myCropParameter.description() + ")")
            self.tblCropParameterProfiles.setItem(myCurrentRow, 1, mypNameItem)

            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            mypNameItem.setIcon(myIcon)

            myCurrentRow += 1

        if myCurrentRow > 0:
            self.tblCropParameterProfiles.setCurrentCell(mySelectedRow, 1)
            self.cellClicked(mySelectedRow, 1)
        else:
            self.on_toolNew_clicked()

        headerLabels = ["File Name", "Name"]
        self.tblCropParameterProfiles.setHorizontalHeaderLabels(headerLabels)
        self.tblCropParameterProfiles.setColumnWidth(0, 0)
        self.tblCropParameterProfiles.setColumnWidth(1, self.tblCropParameterProfiles.width())
        self.tblCropParameterProfiles.horizontalHeader().hide()
        self.tblCropParameterProfiles.verticalHeader().hide()
        self.tblCropParameterProfiles.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        """
    def selectCropParameter(self, theFileName):
        myCropParameterDir = LaUtils.userCropParameterProfilesDirPath()
        myCropParameter = LaCropParameter()
        myCropParameter.fromXmlFile(myCropParameterDir + QDir.separator() + theFileName)
        self.leName.setText(myCropParameter.name())
        self.mCropParameter = myCropParameter
        self.showCropParameter()

    

    def setComboToDefault(self, thepCombo, theDefault):
        if theDefault != "":
            for myCounter in range(thepCombo.count()):
                thepCombo.setCurrentIndex(myCounter)
                if thepCombo.itemData(myCounter, Qt.UserRole) == theDefault:
                    break
        else:
            return False
        return True



