# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LaMainForm
                                 A QGIS plugin
 Archaeological modelling
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-22
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Dr. Jason S. Jorgenson
        email                : jjorgenson@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
# import sys

# from qgis.PyQt.QtCore import QObject,  pyqtSignal,
# import qgis.PyQt.QtCore
# from qgis.PyQt.QtCore import uic
# from qgis.PyQt.QtCore import QtWidgets
# from qgis.PyQt import uic
# from qgis.PyQt import QtWidgets
from qgis.PyQt import QtWidgets, uic
from enum import Enum
# import la
# from la import AreaUnits

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'landuse_analyst_dialog_base.ui'))


# class AreaUnits(Enum):
#     Dunum = "Dunum"
#     Hectare = "Hectare"

class LaMainFormBase(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LaMainFormBase, self).__init__(parent)

        """ Set up the user interface from Designer through FORM_CLASS.
        After self.setupUi() you can access any designer object by doing
        self.<objectname>, and you can use autoconnect slots - see
        http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        #widgets-and-dialogs-with-auto-connect
        """
        self.setupUi(self)

        # everything below this Jason did

        # self.pushButtonExit.clicked.connect(self.exit_program)
        # QObject.connect(self.pushButtonExit, QObject.SIGNAL.clicked()), QtWidgets. qApp, SLOT(quit()))

        # notes for how to do this from:
        # https://stackoverflow.com/questions/27676034/pyqt-place-scaled-image-in-centre-of-label
        self.lblCropPix.setScaledContents(True)
        self.lblAnimalPix.setScaledContents(True)
        self.lblCropPicCalcs.setScaledContents(True)
        self.lblAnimalPicCalcs.setScaledContents(True)
        """ NOTES for setting the resize-mode for each column:
            The first section must stretch to take up the available space,
            whilst the last two sections just resize to their contents:

            PyQt4:
            header = self.table.horizontalHeader()
            header.setResizeMode(0, QtGui.QHeaderView.Stretch)
            header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
            header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

            PyQt5:
            header = self.table.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        """

        self.tblAnimals.horizontalHeader().hide()
        self.tblAnimals.verticalHeader().hide()
        self.tblAnimals.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tblCrops.horizontalHeader().hide()
        self.tblCrops.verticalHeader().hide()
        self.tblCrops.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView. Stretch)
        self.listWidgetCalculationsAnimal.clear()

        # the following should load from xml files that define animals and crops but prob will do now
        # with either JSON or storage in the database
        # loadAnimals()
        # loadCrops()

        # cbAreaUnits needs to be populated with two values. Let's add Dunums and Hectares for now
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")

        self.cbCommonLandEnergyType.addItem("KCalories")
        self.cbCommonLandEnergyType.addItem("TDN")

        # the diet slider works yay!
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)

        # the following, sadly, does NOT work
        # self.connect(self.treeHelp, Qt.Core.SIGNAL(currentItemChanged(QTreeWidgetItem *, QTreeWidgetItem * )),
        #         this, SLOT(helpItemClicked(QTreeWidgetItem * , QTreeWidgetItem * )))


        """
        QStringList myWholeList

        setDietLabels()
        # See the qtdocs on signals and slots to understand below.
        # we connect the currentItemChanged signal that a tree view emits when you
        # click on an item to a little method that sets the help viewer contents
        # appropriately. TS
        # Make sure this is the last stuff we do in the ctor! TS

        connect(treeHelp, SIGNAL(currentItemChanged(QTreeWidgetItem * ,QTreeWidgetItem *)),
            this, SLOT(helpItemClicked(QTreeWidgetItem * ,QTreeWidgetItem *)))
        connect(listWidgetCalculationsCrop, SIGNAL(currentItemChanged(QListWidgetItem * ,QListWidgetItem *)),
            this, SLOT(cropCalcClicked(QListWidgetItem * ,QListWidgetItem *)))
        connect(listWidgetCalculationsAnimal, SIGNAL(currentItemChanged(QListWidgetItem * ,QListWidgetItem *)),
            this, SLOT(animalCalcClicked(QListWidgetItem * ,QListWidgetItem *)))
        connect(pushButtonExit, SIGNAL(clicked()), qApp, SLOT(quit()))
        connect(tblAnimals, SIGNAL(cellClicked( int,int)),
            this, SLOT(animalCellClicked( int,int)))
        connect(tblAnimals, SIGNAL(cellChanged( int,int)),
            this, SLOT(animalCalcSelectionChanged( int,int)))
        connect(tblCrops, SIGNAL(cellClicked( int,int)),
            this, SLOT(cropCellClicked( int,int)))
        connect(tblCrops, SIGNAL(cellChanged( int,int)),
            this, SLOT(cropCalcSelectionChanged( int,int)))
        connect(cbDebug, SIGNAL(clicked()),
            this, SLOT(on_cbDebug_clicked())) """

    def on_sliderDiet_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelMeatPercent.setText(myMinString)
        self.labelCropPercent.setText(myMaxString)
        # setDietLabels()

    def on_sliderMeat_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelMeatWildPercent.setText(myMinString)
        self.labelMeatTamePercent.setText(myMaxString)
        # setDietLabels()

    def on_sliderCrop_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelCropWildPercent.setText(myMinString)
        self.labelCropTamePercent.setText(myMaxString)
        # setDietLabels()

    # Set's the model.  All data comes from the mainForm except for the map
    # of crops and animals which are being generated here.
    def setModel(self, *args):
        self.mSelectedCropsMap.clear()
        self.mSelectedAnimalsMap.clear()
        mySelectedAreaUnit = str(self.cbAreaUnits.currentText())
        myCommonRasterValue = int(self.sbCommonRasterValue.value())
        # a = (b == true ? "123": "456")
        # a = '123' if b else '456'
        # TODO this is quick and dirty
        myAreaUnits = 'Dunum' if mySelectedAreaUnit else 'Hectare'
        print(myAreaUnits, myCommonRasterValue)