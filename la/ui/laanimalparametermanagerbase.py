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

# laanimalparametermanagerbase.py  from laanimalparametermanagerbase.ui

import sys
from datetime import datetime, timezone, timedelta
import numpy as np
from enum import Enum

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtWidgets import QMessageBox, QToolTip, QStackedWidget, QHBoxLayout, QVBoxLayout, QSplitter, QFormLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem, QDialog
from qgis.PyQt.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QHeaderView
from qgis.PyQt.QtGui import QPainter, QBrush, QPen, QColor, QFont, QIcon
from qgis.PyQt.QtCore import Qt, QPoint, QRect, QObject, QEvent, pyqtSignal, pyqtSlot, QSize, QDir
import os

# Load the UI file
FORM_CLASS, _ = uic.loadUiType(
    os.path.join(
        os.path.dirname(__file__),
        'laanimalparametermanagerbase.ui'))

class LaAnimalParameterManagerBase(QDialog, FORM_CLASS):
    """Base class for the Animal Parameter Manager dialog.

    This class handles loading the UI. All implementation logic
    should be in the LaAnimalParameterManager class.
    """
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(LaAnimalParameterManagerBase, self).__init__(parent, flags)
        self.setupUi(self)

        # Basic UI initialization
        self.lblAnimalPic.setScaledContents(True)

        # Set up table headers
        self.tblAnimalParameterProfiles.horizontalHeader().hide()
        self.tblAnimalParameterProfiles.verticalHeader().hide()

    def setAreaUnitsIndex(self, area_units):
        """Helper method to set the correct area units in combo box."""
        if hasattr(self, 'cbAreaUnits'):
            from la.lib.la import AreaUnits
            if area_units == AreaUnits.Dunum:
                self.cbAreaUnits.setCurrentText("Dunum")
            elif area_units == AreaUnits.Hectare:
                self.cbAreaUnits.setCurrentText("Hectare")

    def setComboToDefault(self, combo_box, default_value):
        """Helper method to set a combo box to a default value."""
        if combo_box:
            index = combo_box.findText(str(default_value))
            if index >= 0:
                combo_box.setCurrentIndex(index)
