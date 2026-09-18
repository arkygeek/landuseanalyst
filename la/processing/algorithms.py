"""
algorithms.py — the Processing algorithms Landuse Analyst contributes.

Populated as the regional engines (:mod:`la.lib.laregional`,
:mod:`la.lib.laxtent`, :mod:`la.lib.lapathnetwork`) land; ``allAlgorithms``
tolerates a module that is not there yet so the provider always loads.
"""

from typing import List

from qgis.core import QgsProcessingAlgorithm


def allAlgorithms() -> List[QgsProcessingAlgorithm]:
    """Fresh instances of every available algorithm."""
    myAlgorithms: List[QgsProcessingAlgorithm] = []
    for myModuleName, myClassName in (
        ("la.processing.lathiessenalgorithm", "LaThiessenAlgorithm"),
        ("la.processing.laxtentalgorithm", "LaXtentAlgorithm"),
        ("la.processing.lawalkingroutesalgorithm", "LaWalkingRoutesAlgorithm"),
    ):
        try:
            myModule = __import__(myModuleName, fromlist=[myClassName])
            myAlgorithms.append(getattr(myModule, myClassName)())
        except ImportError:
            continue
    return myAlgorithms
