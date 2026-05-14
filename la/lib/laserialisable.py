import xml.etree.ElementTree as ET
from abc import ABCMeta, abstractmethod
from qgis.PyQt import QtWidgets
import logging

logging.basicConfig(level=logging.ERROR)

class MetaSerialisable(ABCMeta, type(QtWidgets.QDialog)):
    pass

class LaSerialisable(metaclass=MetaSerialisable):
    """
        Abstract base class for objects that can be serialized to and from XML.

        This class provides a common interface for objects that need to be
        persisted to XML format. It defines abstract methods for converting
        the object to and from XML strings, as well as methods for writing
        the XML representation to a file and reading it back from a file.

        Classes that inherit from LaSerialisable must implement the toXml()
        and fromXml() methods.
        """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toXml(self):
        """Convert the object to an XML string."""
        pass

    @abstractmethod
    def fromXml(self, theXmlString):
        """Initialize the object from an XML string."""
        pass

    def toXmlFile(self, file_name):
        """Write the object to an XML file."""
        try:
            with open(file_name, 'w') as file:
                xml_string = self.toXml() or ""
                file.write(xml_string)
            return True
        except IOError as e:
            logging.error(f"Failed to write to file {file_name}: {e}")
            return False

    def fromXmlFile(self, file_name):
        """Read the object from an XML file."""
        try:
            with open(file_name, 'r') as file:
                xml_string = file.read()
            self.fromXml(xml_string)
            return True
        except IOError as e:
            logging.error(f"Failed to read from file {file_name}: {e}")
            return False




# # laserialisable.py
# from qgis.PyQt.QtCore import QObject, QFile, QIODevice, QTextStream

# from abc import ABC, abstractmethod
# # import pickle

# from abc import ABC, abstractmethod

# class LaSerialisable(ABC):
#     """
#     LaSerialisable class is an abstract base class (ABC), and the toXml and
#     fromXml methods are abstract methods.
#     This means that any class that inherits from LaSerialisable must
#     implement these methods.

#     The toXmlFile and fromXmlFile methods provide default implementations
#     that call toXml and fromXml, respectively.

#     Attributes:
#     -----------
#     None

#     Methods:
#     --------
#     toXml() -> str:
#         Write this object to xml and return result as string.
#         This method must be implemented by subclasses.

#     toXmlFile(theFileName: str) -> bool:
#         Write this object to xml and return result as string.
#         We provide a basic default implementation where given a file name,
#         we will write the serialised xml to that file.
#         Internally it uses toXml() method above so that must be properly implemented.

#     fromXml(theXml: str) -> bool:
#         Read this object from xml and return result as true for success, false for failure.
#         This method must be implemented by subclasses.

#     fromXmlFile(theFileName: str) -> bool:
#         Read this object from xml in a file and return result as true for success, false for failure.
#         Internally it uses fromXml(QString) method above so that must be properly implemented.
#     """
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def toXml(self) -> str:
#         """
#         Write this object to xml and return result as string.
#         This method must be implemented by subclasses.
#         """
#         pass

#     def toXmlFile(self, theFileName: str) -> bool:
#         """
#         Write this object to xml and return result as string.
#         We provide a basic default implementation where given a file name,
#         we will write the serialised xml to that file.
#         Internally it uses toXml() method above so that must be properly implemented.
#         """
#         xml_str = self.toXml()
#         with open(theFileName, 'w') as f:
#             f.write(xml_str)
#         return True

#     @abstractmethod
#     def fromXml(self, theXml: str) -> bool:
#         """
#         Read this object from xml and return result as true for success, false for failure.
#         This method must be implemented by subclasses.
#         """
#         pass

#     def fromXmlFile(self, theFileName: str) -> bool:
#         """
#         Read this object from xml in a file and return result as true for success, false for failure.
#         Internally it uses fromXml(QString) method above so that must be properly implemented.
#         """
#         with open(theFileName, 'r') as f:
#             xml_str = f.read()
#         return self.fromXml(xml_str)
