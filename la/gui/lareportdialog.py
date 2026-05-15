"""
lareportdialog.py - Modal full-report viewer.

Shows the thesis-style report (styled tables + inline chart PNGs) in a
resizable QDialog hosting a plain QTextBrowser. matplotlib generates the
charts and embeds them as base64-encoded <img> tags, so no extra Qt
dependency is needed beyond what every QGIS install ships.

The dialog itself is just a viewer; export actions (PDF, JSON) live in
the main form's Results-tab toolbar so they're discoverable without
opening this dialog first.
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTextBrowser,
)

from la.lib.lautils import LaUtils
from la.lib import lareports


class LaReportDialog(QDialog):
    """Modal full-report viewer with tables + charts in a QTextBrowser."""

    def __init__(self, theModel, theCalculationType: str = "", parent=None):
        super().__init__(parent)
        self.mModel = theModel
        self.mCalculationType = theCalculationType

        self.setWindowTitle("Landuse Analyst — Full Report")
        self.setModal(False)
        self.resize(1100, 800)

        myLayout = QVBoxLayout(self)
        myLayout.setContentsMargins(8, 8, 8, 8)
        myLayout.setSpacing(6)

        myToolbar = QHBoxLayout()
        myToolbar.addStretch()
        self.pbnClose = QPushButton("Close", self)
        self.pbnClose.clicked.connect(self.accept)
        myToolbar.addWidget(self.pbnClose)
        myLayout.addLayout(myToolbar)

        self.mView = QTextBrowser(self)
        self.mView.setOpenExternalLinks(True)
        myLayout.addWidget(self.mView, stretch=1)

        self._renderReport()

    def _renderReport(self):
        """Build the full HTML report (with charts) and load it into the view."""
        myHtml = lareports.buildFullReportHtml(
            self.mModel, theCalculationType=self.mCalculationType
        )
        self.mView.setHtml(myHtml)
