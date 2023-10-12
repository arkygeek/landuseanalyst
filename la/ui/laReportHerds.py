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

# laReportHerds.py from laReportHerds.ui

import sys
from datetime import datetime, timezone, timedelta
import numpy as np
from enum import Enum

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QToolTip, QStackedWidget, QHBoxLayout, QVBoxLayout, QSplitter, QFormLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QHeaderView
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, QEvent, pyqtSignal, pyqtSlot, QSize, QDir

# IMPORTS:
from la.ui import laReportHerds


class laReportHerds(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent=parent) # Call the inherited classes __init__ method
		self.ui = uic.loadUi("landuse_analyst/ui/laReportHerds.ui", self) # Load the .ui file


		self.initUI()
		self.show() # Show the GUI


	def initUI(self):
		pass


	def __str__(self):
 		return
