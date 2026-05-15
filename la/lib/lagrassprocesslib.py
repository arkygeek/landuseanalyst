"""
lagrassprocesslib.py — availability probe for the GRASS algorithms the
catchment analysis needs.

The original C++ class was an XML-driven workflow runner; the Python port
doesn't use that pattern (the LaModel already carries the state, and the
orchestrator is :class:`la.lib.lacatchment.LaCatchment`). This module now
exposes a small static helper the main form uses to decide whether to show
a friendly "enable GRASS provider" message before launching a run.
"""

from typing import Optional, Set, Tuple


class LaGrassProcessLib:
    """
    Static probes for the QGIS Processing algorithm registry.

    The QGIS GRASS provider exposes algorithms under either ``grass:`` or
    ``grass7:`` ids depending on the QGIS bundle. We probe both prefixes
    for each operation we need and treat the first match as canonical.
    """

    # Pairs of (preferred, fallback) ids per operation
    _PAIRS: Tuple[Tuple[str, str], ...] = (
        ("grass7:r.walk",           "grass:r.walk"),
        ("grass7:r.cost",           "grass:r.cost"),
        ("grass7:r.mapcalc.simple", "grass:r.mapcalc.simple"),
    )

    @classmethod
    def isAvailable(cls) -> bool:
        """
        True iff every algorithm the catchment analysis needs is registered.

        :return: ``True`` if r.walk OR r.cost AND r.mapcalc.simple are present
            (cost surface requires either walk or cost; mapcalc is mandatory).
        :rtype: bool
        """
        myFound = cls.availableAlgorithms()
        myHasCost = ("grass7:r.walk" in myFound or "grass:r.walk" in myFound
                     or "grass7:r.cost" in myFound or "grass:r.cost" in myFound)
        myHasMapcalc = ("grass7:r.mapcalc.simple" in myFound
                        or "grass:r.mapcalc.simple" in myFound)
        return bool(myHasCost and myHasMapcalc)

    @classmethod
    def availableAlgorithms(cls) -> Set[str]:
        """
        :return: Set of algorithm ids the Processing registry knows about,
            from the candidates this module probes for.
        :rtype: Set[str]
        """
        myResult: Set[str] = set()
        try:
            from qgis.core import QgsApplication
            myReg = QgsApplication.processingRegistry()
        except Exception:
            return myResult
        for myPair in cls._PAIRS:
            for myId in myPair:
                if myReg.algorithmById(myId) is not None:
                    myResult.add(myId)
        return myResult

    @classmethod
    def walkAlgorithmId(cls) -> Optional[str]:
        """
        :return: The first available id for ``r.walk``, or ``None``.
        :rtype: Optional[str]
        """
        return cls._firstAvailable(("grass7:r.walk", "grass:r.walk"))

    @classmethod
    def costAlgorithmId(cls) -> Optional[str]:
        """
        :return: The first available id for ``r.cost``, or ``None``.
        :rtype: Optional[str]
        """
        return cls._firstAvailable(("grass7:r.cost", "grass:r.cost"))

    @classmethod
    def mapcalcAlgorithmId(cls) -> Optional[str]:
        """
        :return: The first available id for ``r.mapcalc.simple``, or ``None``.
        :rtype: Optional[str]
        """
        return cls._firstAvailable(("grass7:r.mapcalc.simple", "grass:r.mapcalc.simple"))

    @classmethod
    def _firstAvailable(cls, theIds: Tuple[str, ...]) -> Optional[str]:
        try:
            from qgis.core import QgsApplication
            myReg = QgsApplication.processingRegistry()
        except Exception:
            return None
        for myId in theIds:
            if myReg.algorithmById(myId) is not None:
                return myId
        return None
