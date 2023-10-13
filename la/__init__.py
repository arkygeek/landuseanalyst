"""
LanduseAnalyst plugin for QGIS
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

# This initializes the plugin and makes it known to QGIS.
from la.gui.lamainform import LanduseAnalyst


# def classFactory(iface):
#     """
#     Load LanduseAnalyst class from file LanduseAnalyst.

#     :param iface: A QGIS interface instance.
#     :type iface: QgsInterface
#     """
#     return LaMainForm(iface)

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LanduseAnalyst class from file LanduseAnalyst.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from la.gui.lamainform import LanduseAnalyst
    return LanduseAnalyst(iface)