"""
la.py - A PyQt5 implementation of the La class.

This file contains the La class, which is a PyQt5 implementation of thetoggle
La class from the original C++ code. The class is responsible for defining
various enums and typedefs used throughout the simulation.

Author: [Your Name]
Date created: [Date]
"""
from builtins import dict as Dict
from typing import Tuple

from la.lib.lafoodsource import LaFoodSource


class La:
    """
    The La class defines several class-level attributes that are used throughout the code.
    """
    # LaTripleMap is a dictionary where each key is a string and each value is a tuple.
    # The tuple contains a boolean and a string.
    LaTripleMap: Dict[str, Tuple[bool, str]] = {}

    # LaRasterInfo is a tuple of two tuples, each containing two strings.
    # This could represent information about a raster image, such as its dimensions and resolution.
    LaRasterInfo: Tuple[Tuple[str, str], Tuple[str, str]] = (("",""),("",""))

    # LaFoodSourceMap is a dictionary where each key is a string and each value is an instance of LaFoodSource.
    # This could represent a mapping from food source names to food source objects.
    LaFoodSourceMap: Dict[str, LaFoodSource] = {}

    # HerdSize is a tuple of two floats.
    # This could represent the minimum and maximum size of a herd.
    HerdSize: Tuple[float, float] = (0.0, 0.0)

    # LaReportMap is a dictionary where each key is a string and each value is a tuple.
    # The tuple contains a string and a float.
    # This could represent a mapping from report names to report data.
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