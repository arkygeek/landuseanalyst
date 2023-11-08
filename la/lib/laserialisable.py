# laserialisable.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
import pickle

class LaSerialisable(QObject):
    """
    This code defines a LaSerialisable class in Python using PyQt5.

    The class provides two methods, toByteArray and fromByteArray, which can be used
    to serialize and deserialize objects of its derived classes.

    toByteArray uses the pickle module to convert the object into a byte stream.

    fromByteArray uses pickle to restore an object from a byte stream.

    laserialisable.cpp defines the implementation of LaSerialisable class in C++.

    The Python version of the class does not require an implementation file, as the
    serialization and deserialization methods are defined in the class
    definition using Python's built-in pickle module.

    Attributes:
        None

    Methods:
        toByteArray: Returns the byte representation of the object using pickle.
        fromByteArray: Returns the object after deserializing the given byte data using pickle.
    """
    def __init__(self):
        super().__init__()

    def __del__(self):
        pass

    def __copy__(self):
        return self.__class__(self)

    def __deepcopy__(self, memo):
        return self.__class__(self)

    def toByteArray(self):
            """
            Serializes the object using pickle and returns the resulting byte array.

            Returns:
                bytes: The serialized object as a byte array.
            """
            return pickle.dumps(self)

    def fromByteArray(self, data):
            """
            Deserialize an object from a byte array using pickle.

            Args:
                data (bytes): The byte array to deserialize.

            Returns:
                The deserialized object.
            """
            return pickle.loads(data)
