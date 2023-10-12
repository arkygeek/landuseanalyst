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

#  This  initializes the plugin, and makes it known to QGIS.
from la.ui.lamainformbase import LaMainFormBase


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LanduseAnalyst class from file LanduseAnalyst.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from la.gui.lamainform import  LaMainForm
    return LaMainForm(iface)
