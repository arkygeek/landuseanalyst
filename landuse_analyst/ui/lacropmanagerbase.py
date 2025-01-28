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

# lacropmanagerbase.py from lacropmanagerbase.ui

from datetime import datetime, timezone, timedelta
from enum import Enum

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QMessageBox, QTableWidgetItem, QWidget
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QPoint, QSize, QPoint, QSize, QSettings

## IMPORTS:
from landuse_analyst.ui import lacropmanagerbase
from landuse_analyst.lib.lautils import LaUtils
from landuse_analyst.lib.lacrop import LaCrop

class LaCropManagerBase(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), 'lacropmanagerbase.ui')
        uic.loadUi(ui_path, self)
        self.initUI()
        self.show()

    def initUI(self):
        self.readSettings()
        self.lblCropPix.setScaledContents(True)
        self.tblCrops.cellClicked.connect(self.cellClicked)
        self.cbAreaUnits.addItems(["Dunum", "Hectare"])
        self.cbFodderEnergyType.addItems(["KCalories", "TDN"])
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)
        self.refreshCropTable()
        self.mImageFile = ""

    def readSettings(self):
        mySettings = QSettings()
        pos = mySettings.value("mainwindow/pos", QPoint(200, 200))
        size = mySettings.value("mainwindow/size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        mySettings = QSettings()
        mySettings.setValue("mainwindow/pos", self.pos())
        mySettings.setValue("mainwindow/size", self.size())

    def on_pbnCropPic_clicked(self):
        myUtils = LaUtils()
        myFile = myUtils.openGraphicFile()
        self.lblCropPix.setPixmap(myFile)
        self.mImageFile = myFile

    def refreshCropTable(self, theGuid=""):
        self.mCropMap = {}
        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(2)

        self.mCropMap = LaUtils.getAvailableCrops()

        mySelectedRow = 0
        myCurrentRow = 0
        for myGuid, myCrop in self.mCropMap.items():
            if not theGuid:
                theGuid = myCrop.guid()
            if myCrop.guid() == theGuid:
                mySelectedRow = myCurrentRow

            self.tblCrops.insertRow(myCurrentRow)
            mypFileNameItem = QTableWidgetItem(myGuid)
            self.tblCrops.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(myCrop.name())
            self.tblCrops.setItem(myCurrentRow, 1, mypNameItem)

            myIcon = QIcon(":/localdata.png")
            mypNameItem.setIcon(myIcon)

            myCurrentRow += 1

        if myCurrentRow > 0:
            self.tblCrops.setCurrentCell(mySelectedRow, 1)
            self.cellClicked(mySelectedRow, 1)
        else:
            self.on_toolNew_clicked()

        headerLabels = ["File Name", "Name"]
        self.tblCrops.setHorizontalHeaderLabels(headerLabels)
        self.tblCrops.setColumnWidth(0, 0)
        self.tblCrops.setColumnWidth(1, self.tblCrops.width())
        self.tblCrops.horizontalHeader().hide()
        self.tblCrops.verticalHeader().hide()
        self.tblCrops.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def cellClicked(self, theRow, theColumn):
        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        myFileName = myGuid + ".xml"
        self.selectCrop(myFileName)

    def selectCrop(self, theFileName):
        myCropDir = LaUtils.userCropProfilesDirPath()
        myCrop = LaCrop()
        myCrop.fromXmlFile(os.path.join(myCropDir, theFileName))
        self.leName.setText(myCrop.name())
        self.mCrop = myCrop
        self.showCrop()

    def showCrop(self):
        self.leName.setText(self.mCrop.name())
        self.leDescription.setText(self.mCrop.description())
        self.sbCropYield.setValue(self.mCrop.cropYield())
        self.sbCropCalories.setValue(self.mCrop.cropCalories())
        self.sbCropFodderProduction.setValue(self.mCrop.fodderProduction())
        self.sbCropFodderValue.setValue(self.mCrop.fodderValue())
        self.cbAreaUnits.setCurrentIndex(self.mCrop.areaUnits())
        self.cbFodderEnergyType.setCurrentIndex(self.mCrop.cropFodderEnergyType())
        self.lblCropPix.setPixmap(self.mCrop.imageFile())

    def on_pushButtonLoad_clicked(self):
        self.mCrop.fromXmlFile("/tmp/crop.xml")
        self.showCrop()

    def on_pushButtonSave_clicked(self):
        pass

    def on_toolNew_clicked(self):
        myCrop = LaCrop()
        myCrop.setGuid()
        self.mCrop = myCrop
        self.showCrop()

    def resizeEvent(self, event):
        self.tblCrops.setColumnWidth(0, 0)
        self.tblCrops.setColumnWidth(1, self.tblCrops.width())
        self.tblCrops.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def on_toolCopy_clicked(self):
        if self.tblCrops.currentRow() < 0:
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if not myGuid:
            return

        myOriginalFileName = os.path.join(LaUtils.userCropProfilesDirPath(), myGuid + ".xml")
        myCrop = LaCrop()
        myCrop.fromXmlFile(myOriginalFileName)

        myCrop.setGuid()
        myNewFileName = os.path.join(LaUtils.userCropProfilesDirPath(), myCrop.guid() + ".xml")
        myCrop.setName("Copy of " + myCrop.name())
        myCrop.toXmlFile(myNewFileName)
        self.refreshCropTable(myCrop.guid())

    def on_toolDelete_clicked(self):
        if self.tblCrops.currentRow() < 0:
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if myGuid:
            myFile = os.path.join(LaUtils.userCropProfilesDirPath(), myGuid + ".xml")
            if not os.remove(myFile):
                QMessageBox.warning(self, "Landuse Analyst", "Unable to delete file \n" + myFile)
            self.refreshCropTable()

    def on_pbnApply_clicked(self):
        self.mCrop.setName(self.leName.text())
        self.mCrop.setDescription(self.leDescription.text())
        self.mCrop.setCropYield(self.sbCropYield.value())
        self.mCrop.setCropCalories(self.sbCropCalories.value())
        self.mCrop.setFodderProduction(self.sbCropFodderProduction.value())
        self.mCrop.setCropFodderValue(self.sbCropFodderValue.value())

        mySelectedAreaUnit = self.cbAreaUnits.currentText()
        if mySelectedAreaUnit == "Dunum":
            self.mCrop.setAreaUnits(LaCrop.Dunum)
        elif mySelectedAreaUnit == "Hectare":
            self.mCrop.setAreaUnits(LaCrop.Hectare)

        self.mCrop.setImageFile(self.mImageFile)
        self.mCrop.toXmlFile(os.path.join(LaUtils.userCropProfilesDirPath(), self.mCrop.guid() + ".xml"))
        self.refreshCropTable(self.mCrop.guid())

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()