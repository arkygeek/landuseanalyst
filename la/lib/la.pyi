from typing import Dict, Tuple, Any, Callable, Optional, Type

from qgis.PyQt.QtCore import pyqtSignal

from la.lib.lafoodsource import LaFoodSource

class pyqtProperty:
    """A decorator for defining Qt properties in Python.

    Args:
        type: The type of the property.
        fget: The getter function for the property.
        fset: The setter function for the property.
        fdel: The deleter function for the property.
        doc: The docstring for the property.
        designable: Whether the property is designable.
        scriptable: Whether the property is scriptable.
        stored: Whether the property is stored.
        user: Whether the property is a user property.
        constant: Whether the property is constant.
        final: Whether the property is final.
        notify: The notify signal for the property.
        revision: The revision number for the property.
        reset: The reset function for the property.
        read: The read function for the property.
        write: The write function for the property.
        designable: The designable function for the property.
        resolveDesignable: The resolveDesignable function for the property.
        scriptable: The scriptable function for the property.
        resolveScriptable: The resolveScriptable function for the property.
        stored: The stored function for the property.
        user: The user function for the property.
        constant: The constant function for the property.
        final: The final function for the property.
    """
    def __init__(
        self,
        type: Type[Any],
        fget: Optional[Callable[[], Any]] = None,
        fset: Optional[Callable[[Any], None]] = None,
        fdel: Optional[Callable[[], None]] = None,
        doc: Optional[str] = None,
        designable: bool = True,
        scriptable: bool = True,
        stored: bool = True,
        user: bool = False,
        constant: bool = False,
        final: bool = False,
        notify: Optional[pyqtSignal] = None,
        revision: int = 0,
        reset: Optional[Callable[[], None]] = None,
        read: Optional[Callable[[], Any]] = None,
        write: Optional[Callable[[Any], None]] = None,
        resolveDesignable: Optional[Callable[[Any], bool]] = None,
        resolveScriptable: Optional[Callable[[Any], bool]] = None,
        resolveStored: Optional[Callable[[Any], bool]] = None,
): ...

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