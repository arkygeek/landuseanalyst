"""Scenario header: name, period and (Phase 6) open/save actions. Manual tag A1."""

from typing import Optional

import os

from qgis.PyQt.QtWidgets import (
    QComboBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QToolButton, QVBoxLayout, QWidget,
)

from la.gui.lascenariocontroller import LaScenarioController


class LaScenarioHeaderPanel(QWidget):
    """Inline-editable scenario title (name + period) with file actions."""

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("grpScenario")
        self.mController = theController
        self._mLoading = False

        myLayout = QVBoxLayout(self)
        myLayout.setContentsMargins(8, 8, 8, 4)
        myLayout.setSpacing(4)

        myTitleRow = QHBoxLayout()
        self.leScenarioName = QLineEdit(self)
        self.leScenarioName.setObjectName("leScenarioName")
        self.leScenarioName.setPlaceholderText("Scenario name (e.g. Shuna North, S05)")
        self.leScenarioName.setToolTip("Free-text name used in report headers and export file names.")
        myTitleRow.addWidget(self.leScenarioName, 1)
        for myName, myText, myTip in (
            ("pbnScenarioNew", "New", "Reset every input to the defaults."),
            ("pbnScenarioOpen", "Open…", "Load a scenario file (*.lascenario.json)."),
            ("pbnScenarioSave", "Save", "Save this scenario (Save As when it has no file yet)."),
            ("pbnScenarioSaveAs", "Save as…", "Save this scenario to a new file."),
        ):
            myButton = QToolButton(self)
            myButton.setObjectName(myName)
            myButton.setText(myText)
            myButton.setToolTip(myTip)
            myButton.setAutoRaise(True)
            setattr(self, myName, myButton)
            myTitleRow.addWidget(myButton)
        myLayout.addLayout(myTitleRow)

        myPeriodRow = QHBoxLayout()
        myPeriodRow.addWidget(QLabel("Period", self))
        self.lePeriod = QLineEdit(self)
        self.lePeriod.setObjectName("lePeriod")
        self.lePeriod.setPlaceholderText("e.g. Chalcolithic")
        myPeriodRow.addWidget(self.lePeriod, 1)
        myPeriodRow.addWidget(QLabel("Thesis", self))
        self.cboThesis = QComboBox(self)
        self.cboThesis.setObjectName("cboThesisScenarios")
        self.cboThesis.setToolTip("The 108 Jorgenson thesis scenarios bundled with the plugin.")
        self.cboThesis.setMinimumWidth(120)
        myPeriodRow.addWidget(self.cboThesis, 1)
        myPeriodRow.addWidget(QLabel("Recent", self))
        self.cboRecent = QComboBox(self)
        self.cboRecent.setObjectName("cboRecentScenarios")
        self.cboRecent.setToolTip("Recently opened or saved scenario files.")
        self.cboRecent.setMinimumWidth(120)
        myPeriodRow.addWidget(self.cboRecent, 1)
        myLayout.addLayout(myPeriodRow)

        self.leScenarioName.textEdited.connect(self._onNameEdited)
        self.lePeriod.textEdited.connect(self._onPeriodEdited)
        self.pbnScenarioNew.clicked.connect(self._onNew)
        self.pbnScenarioOpen.clicked.connect(self._onOpen)
        self.pbnScenarioSave.clicked.connect(self._onSave)
        self.pbnScenarioSaveAs.clicked.connect(self._onSaveAs)
        self.cboRecent.activated.connect(self._onRecentActivated)
        self.cboThesis.activated.connect(self._onThesisActivated)
        self.populateThesis()
        self.mController.recentScenariosChanged.connect(self.refreshRecent)
        self.refreshRecent()
        self.loadFromController()

    def loadFromController(self) -> None:
        self._mLoading = True
        self.leScenarioName.setText(self.mController.mModel.mName)
        self.lePeriod.setText(self.mController.mModel.mPeriod)
        self._mLoading = False

    def _onNameEdited(self, theText: str) -> None:
        if not self._mLoading:
            self.mController.setScenarioName(theText)

    def _onPeriodEdited(self, theText: str) -> None:
        if not self._mLoading:
            self.mController.setPeriod(theText)

    def _onNew(self) -> None:
        self.mController.resetToDefaults()

    def _onOpen(self) -> None:
        myStart = os.path.dirname(self.mController.mScenarioPath or "") or os.path.expanduser("~")
        myPath, _ = QFileDialog.getOpenFileName(
            self, "Open scenario", myStart, "Landuse Analyst scenarios (*.lascenario.json *.json *.xml)")
        if myPath:
            self.openPath(myPath)

    def openPath(self, thePath: str) -> None:
        try:
            self.mController.loadScenario(thePath)
        except Exception as e:
            QMessageBox.warning(self, "Landuse Analyst", f"Could not open {thePath}:\n{e}")

    def _onSave(self) -> None:
        if self.mController.mScenarioPath:
            self.mController.saveScenario(self.mController.mScenarioPath)
        else:
            self._onSaveAs()

    def _onSaveAs(self) -> None:
        from la.lib import lascenarioio
        myPath, _ = QFileDialog.getSaveFileName(
            self, "Save scenario as", lascenarioio.defaultFileName(self.mController.mModel),
            "Landuse Analyst scenarios (*.lascenario.json)")
        if myPath:
            self.mController.saveScenario(myPath)

    def _onRecentActivated(self, theIndex: int) -> None:
        myPath = self.cboRecent.itemData(theIndex)
        if myPath:
            self.openPath(myPath)

    def populateThesis(self) -> None:
        """List la/scenarios/thesis/*.lascenario.json (index.json order)."""
        import glob
        import json
        myDir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scenarios", "thesis")
        self.cboThesis.blockSignals(True)
        self.cboThesis.clear()
        self.cboThesis.addItem("—", "")
        myIndexPath = os.path.join(myDir, "index.json")
        myEntries = []
        if os.path.exists(myIndexPath):
            try:
                myEntries = [(e["name"], os.path.join(myDir, e["file"])) for e in json.load(open(myIndexPath, encoding="utf-8"))]
            except (OSError, ValueError, KeyError):
                myEntries = []
        if not myEntries:
            myEntries = [(os.path.basename(p), p) for p in sorted(glob.glob(os.path.join(myDir, "*.lascenario.json")))]
        for myName, myPath in myEntries:
            self.cboThesis.addItem(myName, myPath)
        self.cboThesis.blockSignals(False)

    def _onThesisActivated(self, theIndex: int) -> None:
        myPath = self.cboThesis.itemData(theIndex)
        if myPath:
            self.openPath(myPath)

    def refreshRecent(self) -> None:
        self.cboRecent.blockSignals(True)
        self.cboRecent.clear()
        self.cboRecent.addItem("—", "")
        for myPath in self.mController.recentScenarios():
            self.cboRecent.addItem(os.path.basename(myPath), myPath)
        self.cboRecent.blockSignals(False)
