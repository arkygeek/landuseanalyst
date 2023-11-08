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
from qgis.PyQt.uic import loadUiType
from qgis.PyQt.QtCore import (
        QSettings, QDir, QFile, QTextStream, QProcess, QSettings, QPoint, QSize, Qt)
from qgis.PyQt.QtWidgets import (
        QDialog, QComboBox, QTreeWidget, QTreeWidgetItem, QTableWidgetItem, 
        QMessageBox, QHeaderView, QTableWidget, QFileDialog, QListWidgetItem)
from qgis.PyQt.QtGui import QIcon

# local imports
from la.lib.lacrop import LaCrop
from la.lib.lautils import LaUtils
from la.gui.lacropparametermanager import LaCropParameterManager
from la.lib.lagrass import LaGrass

# import os

# from qgis.PyQt.uic import loadUiType

# from qgis.PyQt.QtWidgets import QDialog, QWidget
# from qgis.PyQt.QtCore import Qt
# ## IMPORTS:
# from la.gui.lacropparametermanager import LaCropParameterManager
# from la.resources_rc import *
# # from la.ui.lacropparametermanagerbase import lacropparametermanagerbase
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
        super(LaCropParameterManager, self).__init__(parent, flags)
        self.setupUi(self)
        self.readSettings()
        self.tblCropParameterProfiles.cellClicked.connect(self.cellClicked)
        myList = []
        myGrass = LaGrass()
        myMapsetList = myGrass.getMapsetList()
        myIterator1 = iter(myMapsetList)
        while myIterator1.hasNext():
            myList += myGrass.getRasterList(myIterator1.next())
        self.cboRaster.addItems(myList)
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)
        self.lblCropPic.setScaledContents(True)
        
        myCropsMap = LaUtils.getAvailableCrops()
        
        # This creates an iterator for myCropsMap in Python, which you can then iterate over
        # using the next function, similar to how you would use QMapIterator in PyQt4. 
        # In Python, dictionaries (which are similar to QMap in Qt) are iterable, and you can
        # use the items() method to get an iterable that yields pairs of keys and values. 
        # The iter function then creates an iterator from this iterable.
        myIterator = iter(myCropsMap.items)

        while myIterator.hasNext():
            myIterator.next()
            myCrop = myIterator.value()
            myGuid = myCrop.guid()
            myName = myCrop.name()
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            self.cboCrop.addItem(myName, myGuid)
        self.cboCrop.currentIndexChanged.connect(self.on_cboCrop_changed)
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.refreshCropParameterTable()    
    
    def readSettings(self):
        """
        Reads the settings from QSettings and sets the position and size of the window.
        It then reads the window position and size from the application settings and applies them to the current window. 
        The QSettings class is used to read and write application settings, and the QPoint and QSize classes are used to represent the position and size of the window.
                """
        mySettings = QSettings()
        pos = mySettings.value("mainwindow/pos", QPoint(200, 200))
        size = mySettings.value("mainwindow/size", QSize(400, 400))
        self.resize(size)
        self.move(pos)


    def cellClicked(self, theRow, theColumn):
        pass

    def on_cboCrop_changed(self, theIndex):
        pass

    def showCropParameter(self):
        pass

    def on_toolCopy_clicked(self):
        pass

    def on_toolNew_clicked(self):
        pass

    def on_toolDelete_clicked(self):
        pass

    def on_pbnApply_clicked(self):
        pass

    def resizeEvent(self, event):
        pass

    def refreshCropParameterTable(self, theGuid=0):
        pass

    def selectCropParameter(self, theFileName):
        pass

    def readSettings(self):
        pass

    def writeSettings(self):
        pass

    def setComboToDefault(self, thepCombo: QComboBox, theDefault: str) -> bool:
        pass



