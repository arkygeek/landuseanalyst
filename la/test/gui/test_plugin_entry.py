"""The plugin class must init, open its docks and unload against a QGIS-like interface."""

import pytest
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QMainWindow
from qgis.gui import QgsMapCanvas, QgsMessageBar


class _StubIface:
    """The handful of QgisInterface methods the plugin touches."""

    def __init__(self):
        self._mWindow = QMainWindow()
        self._mCanvas = QgsMapCanvas(self._mWindow)
        self._mWindow.setCentralWidget(self._mCanvas)
        self._mBar = QgsMessageBar(self._mWindow)
        self.toolbarActions = []
        self.menuActions = []
        self.docks = []

    def mainWindow(self):
        return self._mWindow

    def mapCanvas(self):
        return self._mCanvas

    def messageBar(self):
        return self._mBar

    def addToolBarIcon(self, theAction):
        self.toolbarActions.append(theAction)

    def removeToolBarIcon(self, theAction):
        if theAction in self.toolbarActions:
            self.toolbarActions.remove(theAction)

    def addPluginToMenu(self, theMenu, theAction):
        self.menuActions.append((theMenu, theAction))

    def removePluginMenu(self, theMenu, theAction):
        self.menuActions = [m for m in self.menuActions if m[1] is not theAction]

    def addDockWidget(self, theArea, theDock):
        self._mWindow.addDockWidget(theArea, theDock)
        self.docks.append(theDock)

    def removeDockWidget(self, theDock):
        self._mWindow.removeDockWidget(theDock)
        self.docks.remove(theDock)


@pytest.mark.usefixtures("qtApp", "sampleProfilesDir")
def test_plugin_lifecycle():
    from la.landuse_analyst import LanduseAnalyst

    myIface = _StubIface()
    myPlugin = LanduseAnalyst(myIface)
    myPlugin.initGui()
    assert len(myIface.toolbarActions) == 1
    assert len(myIface.menuActions) == 2

    myPlugin.openWorkspace()
    assert len(myIface.docks) == 2
    assert myIface.mainWindow().dockWidgetArea(myPlugin.mSettingsDock) == Qt.LeftDockWidgetArea
    assert myIface.mainWindow().dockWidgetArea(myPlugin.mResultsDock) == Qt.RightDockWidgetArea
    myPlugin.openWorkspace()          # idempotent
    assert len(myIface.docks) == 2

    # Seed picking uses the iface canvas; toggling on and off must not raise.
    myPanel = myPlugin.mSettingsDock.catchmentPanel
    myPanel.pbnPickSeed.setChecked(True)
    assert myIface.mapCanvas().mapTool() is myPlugin.mSettingsDock.mSeedTool
    myPanel.pbnPickSeed.setChecked(False)

    myPlugin.unload()
    assert not myIface.toolbarActions and not myIface.menuActions and not myIface.docks
