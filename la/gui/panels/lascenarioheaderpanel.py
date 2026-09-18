"""Scenario header: name, period and (Phase 6) open/save actions. Manual tag A1."""

from typing import Optional

from qgis.PyQt.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QToolButton, QVBoxLayout, QWidget

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
            ("pbnScenarioOpen", "Open…", "Load a saved scenario file (available in a later release)."),
            ("pbnScenarioSave", "Save…", "Save this scenario to a file (available in a later release)."),
        ):
            myButton = QToolButton(self)
            myButton.setObjectName(myName)
            myButton.setText(myText)
            myButton.setToolTip(myTip)
            myButton.setAutoRaise(True)
            setattr(self, myName, myButton)
            myTitleRow.addWidget(myButton)
        self.pbnScenarioOpen.setEnabled(False)
        self.pbnScenarioSave.setEnabled(False)
        myLayout.addLayout(myTitleRow)

        myPeriodRow = QHBoxLayout()
        myPeriodRow.addWidget(QLabel("Period", self))
        self.lePeriod = QLineEdit(self)
        self.lePeriod.setObjectName("lePeriod")
        self.lePeriod.setPlaceholderText("e.g. Chalcolithic")
        myPeriodRow.addWidget(self.lePeriod, 1)
        myLayout.addLayout(myPeriodRow)

        self.leScenarioName.textEdited.connect(self._onNameEdited)
        self.lePeriod.textEdited.connect(self._onPeriodEdited)
        self.pbnScenarioNew.clicked.connect(self._onNew)
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
