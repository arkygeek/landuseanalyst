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
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog, QComboBox
from qgis.PyQt.uic import loadUiType

# Load the UI form for the crop parameter manager
Ui_LaCropParameterManagerBase, _ = loadUiType(
    os.path.join(os.path.dirname(__file__), "lacropparametermanagerbase.ui")
)

class LaCropParameterManagerBase(QDialog, Ui_LaCropParameterManagerBase):
    """Base class for the crop parameter manager.

    This class loads the UI form and provides a basic interface
    that the implementation class can build upon.
    """
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        """Initialize the crop parameter manager base.

        Args:
            parent: The parent widget
            flags: Window flags
        """
        super(LaCropParameterManagerBase, self).__init__(parent, flags)
        self.setupUi(self)

        # Basic initialization of UI elements
        self.mCropParameter = None

    def setAreaUnitsIndex(self, area_units):
        """Set the area units combo box to the appropriate index for the given enum value.

        Args:
            area_units: An AreaUnits enum value or integer

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # If it's already an integer, use it directly
            if isinstance(area_units, int):
                self.cbAreaUnits.setCurrentIndex(area_units)
                return True

            # If it's an enum, get its integer value
            if hasattr(area_units, 'value'):
                self.cbAreaUnits.setCurrentIndex(area_units.value)
                return True

            # Otherwise try direct conversion
            self.cbAreaUnits.setCurrentIndex(int(area_units))
            return True
        except (ValueError, TypeError, AttributeError) as e:
            print(f"Error setting area units: {e}")
            # Default to first item
            self.cbAreaUnits.setCurrentIndex(0)
            return False

    def setComboToDefault(self, combo_box, default_value):
        """Set a combo box to the item matching the given value.

        Args:
            combo_box: QComboBox to modify
            default_value: Value to match in the user role data

        Returns:
            bool: True if found and set, False otherwise
        """
        if not default_value:
            return False

        # Search for matching item
        for i in range(combo_box.count()):
            combo_box.setCurrentIndex(i)
            if combo_box.itemData(i, Qt.UserRole) == default_value:
                return True

        return False
