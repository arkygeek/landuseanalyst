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

import os

from la.lib.la import *  # my own classes
from la.ui.lacropmanagerbase import LaCropManagerBase
# endregion

# This loads your .ui file so that PyQt can
# populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(
                    os.path.join(
                        os.path.dirname(__file__),
                        'lamainformbase.ui'))


class LaMainFormBase(QtWidgets.QDialog, FORM_CLASS):
    # pass

    def __init__(self, parent=None):
        """Constructor for LaMainFormBase (.ui file)"""
        super(LaMainFormBase, self).__init__(parent)

        """ Set up the user interface from Designer through FORM_CLASS.
        After self.setupUi() you can access any designer object by doing
        self.<objectname>, and you can use autoconnect slots - see
        http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        #widgets-and-dialogs-with-auto-connect
        """
        self.setupUi(self)

        # NOTE everything below this Jason did

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
        # the following SHOULD load from XML files that define animals and crops
        # but probably will use either JSON, or store it in a database
        # The following could possibly come from utils? - JJ

        # loadAnimals()
        # loadCrops()
        # endregion

        # region COMBO BOX ITEMS LOADED
        # cbAreaUnits needs populating with values; Dunums & Hectares for now...
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.cbCommonLandEnergyType.addItem("KCalories")
        self.cbCommonLandEnergyType.addItem("TDN")
        # endregion

        # region DIET SLIDERS CONNECTED
        # the diet sliders get connected here
        self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
        self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
        self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)
        # endregion

        # connect the change in tree to it's def
        self.treeHelp.currentItemChanged.connect(self.current_item_changed)

        """ this is c++ code that needs translation
        QStringList myWholeList

        setDietLabels()  # <-- This is actually the modelling here!

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
            this, SLOT(on_cbDebug_clicked()))

        # the above code (roughly) ported to python is shown below - Jason

        # Connect signals to slots
        self.treeHelp.currentItemChanged.connect(self.helpItemClicked)
        self.listWidgetCalculationsCrop.currentItemChanged.connect(self.cropCalcClicked)
        self.listWidgetCalculationsAnimal.currentItemChanged.connect(self.animalCalcClicked)
        self.pushButtonExit.clicked.connect(qApp.quit)  #not right
        self.tblAnimals.cellClicked.connect(self.animalCellClicked)
        self.tblAnimals.cellChanged.connect(self.animalCalcSelectionChanged)
        self.tblCrops.cellClicked.connect(self.cropCellClicked)
        self.tblCrops.cellChanged.connect(self.cropCalcSelectionChanged)
        self.cbDebug.clicked.connect(self.on_cbDebug_clicked)

        """

        # This is the end of the constructor


    # read/load/display help file corresponding to selected item in helpTree
    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, QtWidgets.QTreeWidgetItem)
    def current_item_changed(self, theCurrentItem, thePreviousItem):
        self.tbReport.append("Item clicked in help browser: " + theCurrentItem.text(0))
        myQFile = QFile(":/" + theCurrentItem.text(0) + ".html")
        myQFile.open(QFile.ReadOnly | QFile.Text)
        istream = QTextStream(myQFile)

        self.textHelp.setHtml(istream.readAll())
        myQFile.close()


    def on_clicked_pbnNewCrop(self, parent=None):
        print("open Manage Crops window printed")
        self.tbReport.append("Manage Crops button clicked")

        Ui_CropManagerBase, _ = uic.loadUiType(
            os.path.join(
                os.path.dirname(__file__),
                'ui/lacropmanagerbase.ui'))

        super(self, Ui_CropManagerBase).__init__(parent)
        self.setupUi(Ui_CropManagerBase)
        Ui_CropManagerBase.show()
        Ui_CropManagerBase.exec()


    def on_clicked_pbnNewCropParameter(self):
        print("open Crop Parameters window")
        self.tbReport.append("Manage Crop Parameters button clicked")


    def on_clicked_pbnNewAnimal(self):
        print("open Manage Animals window printed")
        self.tbReport.append("Manage Animals button clicked")


    def on_clicked_pbnNewAnimalParameter(self):
        print("open Animal Parameters window")
        self.tbReport.append("Manage Animal Parameters button clicked")


    def on_sliderDiet_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelMeatPercent.setText(myMinString)
        self.labelCropPercent.setText(myMaxString)
        # setDietLabels()  # recalculates model (to update the diet labels!)s


    def on_sliderMeat_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelMeatWildPercent.setText(myMinString)
        self.labelMeatTamePercent.setText(myMaxString)
        # setDietLabels()  # recalculates model (to update the diet labels!)


    def on_sliderCrop_valueChanged(self,  theValue):
        myMinString = str(theValue)
        myMaxString = str(100-theValue)
        self.labelCropWildPercent.setText(myMinString)
        self.labelCropTamePercent.setText(myMaxString)
        # setDietLabels()  # recalculates model (to update the diet labels!)


    # Set's the model.  All data comes from laMainForm EXCEPT for
    # the map of crops and animals, which are being generated here.
    def setModel(self, *args):
        self.mSelectedCropsMap.clear()
        self.mSelectedAnimalsMap.clear()
        mySelectedAreaUnit = AreaUnits(self.cbAreaUnits.currentText())
        myCommonRasterValue = int(self.sbCommonRasterValue.value())

        # TODO this is quick and dirty
        myAreaUnits = 'Dunum' if mySelectedAreaUnit else 'Hectare'
        print(AreaUnits, myAreaUnits, myCommonRasterValue)
