from typing import Dict, Tuple
from la.lib.lafoodsource import LaFoodSource

class La:
    LaTripleMap: Dict[str, Tuple[bool, str]]
    LaRasterInfo: Tuple[Tuple[str, str], Tuple[str, str]]
    LaFoodSourceMap: Dict[str, LaFoodSource]
    HerdSize: Tuple[float, float]
    LaReportMap: Dict[str, Tuple[str, float]]

class Priority:
    None_: int
    High: int
    Medium: int
    Low: int

class Status:
    MoreThanEnoughToCompletelySatisfy: int
    NotEnoughToCompletelySatisfy: int

class LandBeingGrazed:
    Common: int
    Unique: int

class AreaUnits:
    Dunum: int
    Hectare: int

class LandFound:
    NotEnough: int
    TooMuch: int
    FoundTarget: int

class EnergyType:
    KCalories: int
    TDN: int