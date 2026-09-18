# -*- coding: utf-8 -*-
"""
landuse_analyst.py — QGIS plugin entry point for Landuse Analyst.

Registers a toolbar button / menu that opens the two-dock workspace
(:class:`la.gui.lasettingsdock.LaSettingsDock` on the left,
:class:`la.gui.laresultsdock.LaResultsDock` on the right), plus a menu entry
for the deprecated single-window form.
"""

import os

from qgis.PyQt.QtCore import QCoreApplication, QSettings, Qt, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from la.resources_rc import *  # noqa: F401,F403 - registers the Qt resources (icon, help pages)

_MENU = "&Landuse Analyst"
_ICON = ":/la_icon_small.png"


class LanduseAnalyst:
    """QGIS plugin implementation."""

    def __init__(self, iface):
        """
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []
        self.mController = None
        self.mSettingsDock = None
        self.mResultsDock = None
        self.mLegacyForm = None
        self._installTranslator()

    def _installTranslator(self) -> None:
        myLocale = QSettings().value("locale/userLocale", "")
        myLocale = str(myLocale)[0:2] if myLocale else ""
        if not myLocale:
            return
        myPath = os.path.join(self.plugin_dir, "i18n", f"la_{myLocale}.qm")
        if os.path.exists(myPath):
            self.translator = QTranslator()
            self.translator.load(myPath)
            QCoreApplication.installTranslator(self.translator)

    @staticmethod
    def tr(theMessage: str) -> str:
        return QCoreApplication.translate("LanduseAnalyst", theMessage)

    # ------------------------------------------------------------------
    # QGIS plugin protocol
    # ------------------------------------------------------------------
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.actionOpen = QAction(QIcon(_ICON), self.tr("Landuse Analyst"), self.iface.mainWindow())
        self.actionOpen.setStatusTip(self.tr("Open the Landuse Analyst workspace"))
        self.actionOpen.triggered.connect(self.openWorkspace)
        self.iface.addToolBarIcon(self.actionOpen)
        self.iface.addPluginToMenu(_MENU, self.actionOpen)
        self.actions.append(self.actionOpen)

        self.actionLegacy = QAction(self.tr("Legacy form (deprecated)…"), self.iface.mainWindow())
        self.actionLegacy.setStatusTip(self.tr("Open the previous single-window interface"))
        self.actionLegacy.triggered.connect(self.openLegacyForm)
        self.iface.addPluginToMenu(_MENU, self.actionLegacy)
        self.actions.append(self.actionLegacy)

    def unload(self):
        """Removes the plugin menu items, icon and docks from the QGIS GUI."""
        for myAction in self.actions:
            self.iface.removePluginMenu(_MENU, myAction)
            self.iface.removeToolBarIcon(myAction)
        self.actions = []
        for myDock in (self.mSettingsDock, self.mResultsDock):
            if myDock is not None:
                self.iface.removeDockWidget(myDock)
                myDock.deleteLater()
        self.mSettingsDock = None
        self.mResultsDock = None
        self.mController = None
        if self.mLegacyForm is not None:
            self.mLegacyForm.close()
            self.mLegacyForm = None

    # ------------------------------------------------------------------
    # Workspace
    # ------------------------------------------------------------------
    def openWorkspace(self):
        """Create the docks on first use, then show and raise them."""
        if self.mController is None:
            from la.gui.lascenariocontroller import LaScenarioController
            from la.gui.lasettingsdock import LaSettingsDock
            from la.gui.laresultsdock import LaResultsDock

            self.mController = LaScenarioController(self.iface.mainWindow())
            self.mSettingsDock = LaSettingsDock(self.mController, self.iface, self.iface.mainWindow())
            self.mResultsDock = LaResultsDock(self.mController, self.iface.mainWindow())
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.mSettingsDock)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.mResultsDock)
        for myDock in (self.mSettingsDock, self.mResultsDock):
            myDock.setUserVisible(True)
            myDock.raise_()

    def openLegacyForm(self):
        """Show the previous single-window dialog (modeless, so QGIS stays usable)."""
        if self.mLegacyForm is None:
            from la.gui.lamainform import LaMainForm
            self.mLegacyForm = LaMainForm(self.iface.mainWindow())
            self.mLegacyForm.setWindowFlags(self.mLegacyForm.windowFlags() | Qt.Window)
        self.mLegacyForm.show()
        self.mLegacyForm.raise_()
        self.mLegacyForm.activateWindow()

    def run(self):
        """Backwards-compatible alias for the toolbar action."""
        self.openWorkspace()
