import xml.etree.ElementTree as ET
from abc import ABCMeta, abstractmethod
from qgis.PyQt import QtWidgets

class MetaSerialisable(ABCMeta, type(QtWidgets.QDialog)):
    pass

class LaSerialisable(metaclass=MetaSerialisable):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toXml(self):
        """Convert the object to an XML string."""
        pass

    @abstractmethod
    def fromXml(self, xml_string):
        """Initialize the object from an XML string."""
        pass

    def toXmlFile(self, file_name):
        """Write the object to an XML file."""
        try:
            with open(file_name, 'w') as file:
                file.write(self.toXml())
            return True
        except IOError as e:
            print(f"Failed to write to file {file_name}: {e}")
            return False

    def fromXmlFile(self, file_name):
        """Read the object from an XML file."""
        try:
            with open(file_name, 'r') as file:
                xml_string = file.read()
            return self.fromXml(xml_string)
        except IOError as e:
            print(f"Failed to read from file {file_name}: {e}")
            return False