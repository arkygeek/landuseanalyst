from typing import TypeVar, Generic, Callable, Any, Optional
from qgis.PyQt.QtCore import pyqtProperty, pyqtSignal

T = TypeVar('T')

def safe_property(type_class: Any,
                  notify_signal: Optional[pyqtSignal] = None,
                  doc: str = None):
    """
    A wrapper around pyqtProperty that works better with type checkers.

    Args:
        type_class: The class representing the property type
        notify_signal: Signal to emit when property changes
        doc: Documentation string

    Returns:
        A property decorator that works with type checkers
    """
    def decorator(func):
        return pyqtProperty(type_class, func, notify=notify_signal, doc=doc)
    return decorator
