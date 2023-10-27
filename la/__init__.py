"""
LanduseAnalyst plugin for QGIS
"""

# def classFactory(iface):
#     """
#     Load LanduseAnalyst class from file LanduseAnalyst.
#     :param iface: A QGIS interface instance.
#     :type iface: QgsInterface
#     """
#     return LaMainForm(iface)

# from qgis.PyQt.QtCore import Qt
# from qgis.PyQt.QtWidgets import QApplication
# QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

# import qgis.utils
# This initializes the plugin and makes it known to QGIS.

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LaMainForm class from gui/lamainform.py

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from la.landuse_analyst import LanduseAnalyst
    return LanduseAnalyst(iface)