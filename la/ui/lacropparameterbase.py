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

# lacropparameterbase.py  from lacropparameterbase.ui

import os

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.uic import loadUiType
from qgis.PyQt.QtWidgets import QDialog

## IMPORTS:

Ui_LaCropParameterBase, _ = loadUiType(
	os.path.join(os.path.dirname(__file__), 
	"../ui/lacropparameterbase.ui"
	)
)

class LaCropParameterBase(QDialog, Ui_LaCropParameterBase):
	def __init__(self, parent=None, flags=Qt.WindowFlags()):
		super(LaCropParameterBase, self).__init__(parent, flags)
		self.setupUi(self)
		self.readSettings()
		self.lblCropParameterName.setText("Crop Parameter Name")
		self.lblCropParameterDescription.setText("Crop Parameter Description")
		self.lblCropParameterGuid.setText("Crop Parameter Guid")
		self.sbPercentTameCrop.setValue(0.0)
		self.sbSpoilage.setValue(0.0)
		self.sbReseed.setValue(0.0)
		self.sbCropRotation.setValue(0.0)
		self.sbFallowRatio.setValue(0.0)
		self.checkBoxUseCommonLand.setChecked(False)
		self.checkBoxUseSpecificLand.setChecked(False)
		self.lblRasterName.setText("Raster Name")


	def initUI(self):
		pass


	def __str__(self):
 		return
