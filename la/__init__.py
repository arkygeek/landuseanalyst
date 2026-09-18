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
    """Load the LanduseAnalyst plugin class from landuse_analyst.py

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    import sys
    import importlib
    
    # Reload all plugin submodules recursively so that QGIS plugin reloader
    # actually updates the code in memory rather than using python's cache.
    mySubmodules = [
        "la.lib.la", "la.lib.laguid", "la.lib.laserialisable", "la.lib.lautils",
        "la.lib.lagrassprocesslib", "la.lib.laraster", "la.lib.labarriers", "la.lib.lagrass",
        "la.lib.lacrop", "la.lib.lacropparameter", "la.lib.laanimal", "la.lib.laanimalparameter",
        "la.lib.lafoodsource", "la.lib.ladietlabels", "la.lib.lamodel", "la.lib.lacalculations",
        "la.lib.lacatchment", "la.lib.lareports", "la.lib.lacatalogue", "la.lib.lascenarioio",
        "la.lib.ladependencies", "la.lib.laregional", "la.lib.laxtent", "la.lib.lapathnetwork",
        "la.gui.ladebugdialog", "la.gui.lareportdialog", "la.gui.lalayerstyles",
        "la.gui.lacatchmenttask", "la.gui.lamaptools", "la.gui.widgets.ladietdonut",
        "la.gui.widgets.lapreferredlandwidget", "la.gui.lacropmanager", "la.gui.lacropparametermanager",
        "la.gui.laanimalmanager", "la.gui.laanimalparametermanager", "la.gui.laassemblageconversion",
        "la.gui.lascenariocontroller", "la.gui.panels.lascenarioheaderpanel", "la.gui.panels.ladietpanel",
        "la.gui.panels.laagriculturepanel", "la.gui.panels.lacatchmentpanel", "la.gui.panels.laadvancedpanel",
        "la.gui.panels.lafooterpanel", "la.gui.lasettingsdock", "la.gui.laresultsdock",
        "la.processing.labasealgorithm", "la.processing.lathiessenalgorithm", "la.processing.laxtentalgorithm",
        "la.processing.lawalkingroutesalgorithm", "la.processing.lacatchmentalgorithm",
        "la.processing.algorithms", "la.processing.laprovider", "la.landuse_analyst",
    ]
    
    for myModName in mySubmodules:
        if myModName in sys.modules:
            try:
                importlib.reload(sys.modules[myModName])
            except Exception as e:
                print(f"Failed to reload submodule {myModName}: {e}")

    from la.landuse_analyst import LanduseAnalyst
    return LanduseAnalyst(iface)