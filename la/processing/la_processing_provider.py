# -*- coding: utf-8 -*-
"""
Provider registration for Landuse Analyst.
"""

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon
import os

from la.processing.la_catchment_algorithm import LaCatchmentAlgorithm


class LaProcessingProvider(QgsProcessingProvider):
    """QGIS Processing Provider for Landuse Analyst."""

    def __init__(self):
        super(LaProcessingProvider, self).__init__()

    def unload(self):
        """Unregister the provider."""
        pass

    def loadAlgorithms(self):
        """Load and register algorithms."""
        self.addAlgorithm(LaCatchmentAlgorithm())

    def id(self) -> str:
        """Provider ID."""
        return 'la'

    def name(self) -> str:
        """Provider display name."""
        return 'Landuse Analyst'

    def icon(self) -> QIcon:
        """Provider icon."""
        myIconPath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'resources',
            'la_icon_small.png'
        )
        if os.path.exists(myIconPath):
            return QIcon(myIconPath)
        return QIcon(':/la_icon_small.png')
