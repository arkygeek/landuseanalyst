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
import os
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from landuse_analyst.lib.laserialisable import LaSerialisable
from landuse_analyst.lib.lautils import LaUtils
from landuse_analyst.lib.lacrop import LaCrop

class LaCropManagerBase(QDialog, LaSerialisable):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("Initializing LaCropManagerBase")
        ui_path = os.path.join(os.path.dirname(__file__), 'lacropmanagerbase.ui')
        print(f"Loading UI from: {ui_path}")
        uic.loadUi(ui_path, self)
        self.initUI()
        self.show()


    def initUI(self):
        print("Initializing UI components")
        self.readSettings()
        self.lblCropPix.setScaledContents(True)
        self.tblCrops.cellClicked.connect(self.cellClicked)
        self.cbAreaUnits.addItems(["Dunum", "Hectare"])
        self.cbFodderEnergyType.addItems(["KCalories", "TDN"])
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)
        self.refreshCropTable()
        self.mImageFile = ""

        # Connect buttons to their respective methods
        self.pbnCropPic.clicked.connect(self.on_pbnCropPic_clicked)

    def refreshCropTable(self, theGuid=""):
        print("Refreshing crop table")
        self.mCropMap = {}
        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(2)

        crop_profiles_dir = LaUtils.userCropProfilesDirPath()
        print(f"Loading crop profiles from: {crop_profiles_dir}")

        self.mCropMap = LaCropManagerBase.getAvailableCrops()

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

    def on_pbnCropPic_clicked(self):
        print("on_pbnCropPic_clicked called")
        myFile = LaUtils.openGraphicFile(self)
        if myFile:
            self.lblCropPix.setPixmap(myFile)
            self.mImageFile = myFile

    @staticmethod
    def getAvailableCrops():
        """
        Returns a dictionary of available crops.
        """
        crop_profiles_dir = LaUtils.userCropProfilesDirPath()
        print(f"Looking for crop profiles in: {crop_profiles_dir}")
        crops = {}
        if not os.path.exists(crop_profiles_dir):
            print(f"Directory does not exist: {crop_profiles_dir}")
            return crops

        for file_name in os.listdir(crop_profiles_dir):
            if file_name.endswith(".xml"):
                print(f"Found crop profile: {file_name}")
                crop = LaCrop()
                crop.fromXmlFile(os.path.join(crop_profiles_dir, file_name))
                crops[crop.guid()] = crop
            else:
                print(f"Skipping non-XML file: {file_name}")
        print(f"Total crops loaded: {len(crops)}")
        return crops

    def cellClicked(self, theRow, theColumn):
        print(f"Cell clicked at row {theRow}, column {theColumn}")
        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        myFileName = myGuid + ".xml"
        self.selectCrop(myFileName)

    def selectCrop(self, theFileName):
        print(f"Selecting crop from file: {theFileName}")
        myCropDir = LaUtils.userCropProfilesDirPath()
        myCrop = LaCrop()
        myCrop.fromXmlFile(os.path.join(myCropDir, theFileName))
        self.leName.setText(myCrop.name())
        self.mCrop = myCrop
        self.showCrop()

    def showCrop(self):
        print("Showing crop details")
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
        print("on_pushButtonLoad_clicked called")
        self.mCrop.fromXmlFile("/tmp/crop.xml")
        self.showCrop()

    def on_pushButtonSave_clicked(self):
        print("on_pushButtonSave_clicked called")
        # Implement save functionality here

    def on_toolNew_clicked(self):
        print("on_toolNew_clicked called")
        myCrop = LaCrop()
        myCrop.setGuid()
        self.mCrop = myCrop
        self.showCrop()

    def resizeEvent(self, event):
        self.tblCrops.setColumnWidth(0, 0)
        self.tblCrops.setColumnWidth(1, self.tblCrops.width())
        self.tblCrops.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def on_toolCopy_clicked(self):
        print("on_toolCopy_clicked called")
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
        print("on_toolDelete_clicked called")
        if self.tblCrops.currentRow() < 0:
            return

        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if myGuid:
            myFile = os.path.join(LaUtils.userCropProfilesDirPath(), myGuid + ".xml")
            if not os.remove(myFile):
                QMessageBox.warning(self, "Landuse Analyst", "Unable to delete file \n" + myFile)
            self.refreshCropTable()

    def on_pbnApply_clicked(self):
        print("on_pbnApply_clicked called")
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

    def readSettings(self):
        """Placeholder for restoring UI settings"""
        print("readSettings() called, but not implemented yet.")

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()