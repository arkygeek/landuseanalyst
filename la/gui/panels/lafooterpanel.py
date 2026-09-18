"""Sticky footer: live summary, readiness reason, progress and the Calculate button. Manual tag A5."""

from typing import Optional

from qgis.PyQt.QtWidgets import QHBoxLayout, QLabel, QProgressBar, QPushButton, QVBoxLayout, QWidget


class LaFooterPanel(QWidget):
    """Always-visible strip at the bottom of the settings dock."""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("panelFooter")
        myLayout = QVBoxLayout(self)
        myLayout.setContentsMargins(8, 4, 8, 8)
        myLayout.setSpacing(4)

        self.lblSummary = QLabel(self)
        self.lblSummary.setObjectName("lblSummary")
        self.lblSummary.setWordWrap(True)
        self.lblSummary.setStyleSheet("QLabel { color: palette(mid); }")
        myLayout.addWidget(self.lblSummary)

        self.lblStage = QLabel(self)
        self.lblStage.setObjectName("lblStage")
        self.lblStage.setWordWrap(True)
        myLayout.addWidget(self.lblStage)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximumHeight(10)
        self.progressBar.setTextVisible(False)
        self.progressBar.hide()
        myLayout.addWidget(self.progressBar)

        myButtons = QHBoxLayout()
        self.pbnCancel = QPushButton("Cancel", self)
        self.pbnCancel.setObjectName("pbnCancel")
        self.pbnCancel.hide()
        myButtons.addWidget(self.pbnCancel)
        myButtons.addStretch()
        self.pbnCalculate = QPushButton("Calculate", self)
        self.pbnCalculate.setObjectName("pbnCalculate")
        self.pbnCalculate.setDefault(True)
        self.pbnCalculate.setMinimumWidth(120)
        myButtons.addWidget(self.pbnCalculate)
        myLayout.addLayout(myButtons)

    def setSummary(self, theText: str) -> None:
        self.lblSummary.setText(theText)

    def setReady(self, theReady: bool, theReason: str) -> None:
        self.pbnCalculate.setEnabled(theReady)
        self.pbnCalculate.setToolTip("" if theReady else theReason)
        if not theReady:
            self.lblStage.setText(theReason)
            self.lblStage.setStyleSheet("QLabel { color: #a33a2a; }")
        elif not self.progressBar.isVisible():
            self.lblStage.setStyleSheet("")

    def setIdle(self, theText: str = "") -> None:
        self.progressBar.hide()
        self.pbnCancel.hide()
        self.pbnCalculate.setEnabled(True)
        self.lblStage.setStyleSheet("")
        self.lblStage.setText(theText)

    def setBusy(self, theStage: str) -> None:
        self.progressBar.setRange(0, 0)
        self.progressBar.show()
        self.pbnCancel.show()
        self.pbnCalculate.setEnabled(False)
        self.lblStage.setStyleSheet("")
        self.lblStage.setText(theStage)

    def setProgress(self, theValue: int, theMaximum: int, theStage: Optional[str] = None) -> None:
        if theMaximum > 0:
            self.progressBar.setRange(0, theMaximum)
            self.progressBar.setValue(max(0, min(theValue, theMaximum)))
        if theStage:
            self.lblStage.setText(theStage)
