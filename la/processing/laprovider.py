"""
laprovider.py — ``QgsProcessingProvider`` for Landuse Analyst.

Regional tools (Thiessen territories, XTent influence, walking routes) are
delivered as Processing algorithms rather than dock panels: that gives batch
mode, the graphical modeller, history and parameter dialogs for free and keeps
the docks focused on the single-site catchment.
"""

from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProcessingProvider

PROVIDER_ID = "la"


class LaProcessingProvider(QgsProcessingProvider):
    """Registers every algorithm in :mod:`la.processing.algorithms`."""

    def id(self) -> str:  # noqa: A003 - QGIS API name
        return PROVIDER_ID

    def name(self) -> str:
        return "Landuse Analyst"

    def longName(self) -> str:
        return "Landuse Analyst — regional tools"

    def icon(self) -> QIcon:
        return QIcon(":/la_icon_small.png")

    def loadAlgorithms(self) -> None:
        from la.processing import algorithms
        for myAlgorithm in algorithms.allAlgorithms():
            self.addAlgorithm(myAlgorithm)
