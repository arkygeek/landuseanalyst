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
    import sys
    import importlib
    
    # Reload all plugin submodules recursively so that QGIS plugin reloader
    # actually updates the code in memory rather than using python's cache.
    mySubmodules = [
        "la.lib.lautils",
        "la.lib.lagrassprocesslib",
        "la.lib.lagrass",
        "la.lib.lacrop",
        "la.lib.lacropparameter",
        "la.lib.laanimal",
        "la.lib.laanimalparameter",
        "la.lib.lamodel",
        "la.lib.lacatchment",
        "la.lib.lacalculations",
        "la.gui.ladebugdialog",
        "la.gui.lareportdialog",
        "la.gui.lacatchmenttask",
        "la.gui.lamainform",
        "la.processing.la_catchment_algorithm",
        "la.processing.la_processing_provider",
        "la.landuse_analyst",
    ]
    
    for myModName in mySubmodules:
        if myModName in sys.modules:
            try:
                importlib.reload(sys.modules[myModName])
            except Exception as e:
                print(f"Failed to reload submodule {myModName}: {e}")

    from la.landuse_analyst import LanduseAnalyst
    return LanduseAnalyst(iface)