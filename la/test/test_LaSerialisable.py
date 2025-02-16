import sys
import os

# Print the initial sys.path
print("Initial sys.path:", sys.path)

# Update the sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Print the updated sys.path
print("Updated sys.path:", sys.path)

import unittest
from la.lib.laserialisable import LaSerialisable

class TestSerialisable(LaSerialisable):
    def __init__(self, name="", guid=""):
        super().__init__()
        self.name = name
        self.guid = guid

    def toXml(self):
        return f"<test><name>{self.name}</name><guid>{self.guid}</guid></test>"

    def fromXml(self, xml_string):
        import xml.etree.ElementTree as ET
        tree = ET.ElementTree(ET.fromstring(xml_string))
        root = tree.getroot()
        self.name = root.find("name").text
        self.guid = root.find("guid").text

class TestLaSerialisable(unittest.TestCase):
    def test_toXml(self):
        obj = TestSerialisable(name="TestName", guid="1234")
        xml = obj.toXml()
        expected_xml = "<test><name>TestName</name><guid>1234</guid></test>"
        self.assertEqual(xml, expected_xml)

    def test_fromXml(self):
        xml = "<test><name>TestName</name><guid>1234</guid></test>"
        obj = TestSerialisable()
        obj.fromXml(xml)
        self.assertEqual(obj.name, "TestName")
        self.assertEqual(obj.guid, "1234")

    def test_toXmlFile(self):
        obj = TestSerialisable(name="TestName", guid="1234")
        result = obj.toXmlFile("/tmp/test.xml")
        self.assertTrue(result)
        with open("/tmp/test.xml", "r") as file:
            content = file.read()
        expected_xml = "<test><name>TestName</name><guid>1234</guid></test>"
        self.assertEqual(content, expected_xml)

    def test_fromXmlFile(self):
        xml = "<test><name>TestName</name><guid>1234</guid></test>"
        with open("/tmp/test.xml", "w") as file:
            file.write(xml)
        obj = TestSerialisable()
        result = obj.fromXmlFile("/tmp/test.xml")
        self.assertTrue(result)
        self.assertEqual(obj.name, "TestName")
        self.assertEqual(obj.guid, "1234")

if __name__ == "__main__":
    unittest.main()