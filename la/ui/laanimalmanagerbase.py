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

# laanimalmanagerbase.py  from laanimalmanagerbase.ui

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

## IMPORTS:
# from landuse_analyst.ui import laanimalmanagerbase # <-- this cannot be resolved
# from landuse_analyst import laanimalmanagerbase  # <-- this CAN be resolved

# Load the UI file
FORM_CLASS, _ = uic.loadUiType(
    os.path.join(
        os.path.dirname(__file__),
        'laanimalmanagerbase.ui'))

class LaAnimalManagerBase(QDialog, FORM_CLASS):
    """Base class for the Animal Manager dialog.

    This class handles loading the UI. All implementation logic
    should be in the LaAnimalManager class.
    """
    def __init__(self, parent=None):
        super(LaAnimalManagerBase, self).__init__(parent)
        self.setupUi(self)

        # Basic UI initialization
        self.lblAnimalPix.setScaledContents(True)

        # Set up table headers
        self.tblAnimals.horizontalHeader().hide()
        self.tblAnimals.verticalHeader().hide()
