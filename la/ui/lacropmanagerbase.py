# -*- coding: utf-8 -*-
"""
LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
of a settlement (with respect to required land needed for food production).
Land area targets for each food source supplied to the model are calculated based
on a multitude of demographic and dietary inputs.

This file defines the base UI class for the Crop Manager dialog.

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

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog
import os

# Load the UI file
FORM_CLASS, _ = uic.loadUiType(
    os.path.join(
        os.path.dirname(__file__),
        'lacropmanagerbase.ui'))


class LaCropManagerBase(QDialog, FORM_CLASS):
    """Base class for the Crop Manager dialog.

    This class only handles loading the UI. All implementation logic
    should be in the LaCropManager class.
    """

    def __init__(self, parent=None):
        """Constructor for LaCropManagerBase.

        :param parent: Parent widget
        :type parent: QWidget
        """
        super(LaCropManagerBase, self).__init__(parent)
        self.setupUi(self)

        # Basic UI initialization
        self.lblCropPix.setScaledContents(True)

        # Set up table headers
        self.tblCrops.horizontalHeader().hide()
        self.tblCrops.verticalHeader().hide()
