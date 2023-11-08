"""
la.py - A PyQt5 implementation of the La class.

This file contains the La class, which is a PyQt5 implementation of thetoggle
La class from the original C++ code. The class is responsible for defining
various enums and typedefs used throughout the simulation.

Author: [Your Name]
Date created: [Date]
"""

from la.lib.lafoodsource import LaFoodSource

from typing import Tuple
from typing import Dict
# Python 3.9
from typing import Dict, Tuple

class La:
    # Equivalent to QMap<QString,QPair<bool,QString>>
    LaTripleMap: Dict[str, Tuple[bool, str]] = {}

    # Equivalent to QPair<QPair<QString,QString>, QPair<QString,QString>>
    LaRasterInfo: Tuple[Tuple[str, str], Tuple[str, str]] = (("",""),("",""))

    # Equivalent to QMap<QString, LaFoodSource>
    LaFoodSourceMap: Dict[str, LaFoodSource] = {}

    # Equivalent to QPair<float,float>
    HerdSize: Tuple[float, float] = (0.0, 0.0)

    # Equivalent to QMap<QString,QPair<QString,float>>
    LaReportMap: Dict[str, Tuple[str, float]] = {}

# Equivalent to enum types
class Priority:
    None_ = 0
    High = 1
    Medium = 2
    Low = 3

class Status:
    MoreThanEnoughToCompletelySatisfy = 0
    NotEnoughToCompletelySatisfy = 1

class LandBeingGrazed:
    Common = 0
    Unique = 1

class AreaUnits:
    """
    This class is an enumeration of area units.

    Attributes:
        Dunum: Represents the Dunum unit of area.
        Hectare: Represents the Hectare unit of area.
    """
    Dunum = 0  # Represents the Dunum unit of area.
    Hectare = 1  # Represents the Hectare unit of area.

class LandFound:
    """
    A class representing the possible outcomes of a land search operation.

    Attributes:
    -----------
    NotEnough : int
        Indicates that the search did not yield enough land.
    TooMuch : int
        Indicates that the search yielded too much land.
    FoundTarget : int
        Indicates that the search successfully found the target land.
    """
    NotEnough = 0
    TooMuch = 1
    FoundTarget = 2

class EnergyType:
    KCalories = 0
    TDN = 1