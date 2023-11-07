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

# lacropparametermanagerbase.py from lacropparametermanagerbase.ui

import os

from qgis.PyQt.uic import loadUiType

from qgis.PyQt.QtWidgets import QDialog, QWidget
from qgis.PyQt.QtCore import Qt
## IMPORTS:
from la.gui.lacropparametermanager import LaCropParameterManager
# from la.resources_rc import *
# from la.ui.lacropparametermanagerbase import lacropparametermanagerbase
Ui_LaCropParameterManagerBase, _ = loadUiType(os.path.join(os.path.dirname(__file__),"lacropparametermanagerbase.ui"))

class LaCropParameterManagerBase(QWidget, Ui_LaCropParameterManagerBase):
	def __init__(self, parent=None, flags=Qt.WindowFlags()):
		super(LaCropParameterManagerBase, self).__init__(parent, flags)
		self.setupUi(self)


	def initUI(self):
		pass


	def __str__(self):
 		return
