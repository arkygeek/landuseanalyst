# laserialisable.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
import pickle

class LaSerialisable(QObject):
    def __init__(self):
        super().__init__()

    def __del__(self):
        pass

    def __copy__(self):
        return self.__class__(self)

    def __deepcopy__(self, memo):
        return self.__class__(self)

    def toByteArray(self):
        return pickle.dumps(self)

    def fromByteArray(self, data):
        return pickle.loads(data)

"""

This code defines a LaSerialisable class in Python using PyQt5.

The class provides two methods, toByteArray and fromByteArray, which can be used
    to serialize and deserialize objects of its derived classes.

    toByteArray uses the pickle module to convert the object into a byte stream

    fromByteArray uses pickle to restore an object from a byte stream

laserialisable.cpp defines the implementation of LaSerialisable class in C++.

The Python version of the class does not require an implementation file, as the
    serialization and deserialization methods are defined in the class
    definition using Python's built-in pickle module.

"""