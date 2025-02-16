import os
import sys
import unittest
from qgis.PyQt.QtCore import QUuid
# Update sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the LaUtils class
from la.lib.laguid import LaGuid

class TestLaGuid(unittest.TestCase):

    def test_initialization(self):
        # Test that a new LaGuid object generates a valid GUID
        laguid = LaGuid()
        guid = laguid.guid()
        self.assertTrue(QUuid(guid).isNull() == False)

    def test_guid_method(self):
        # Test that the guid method returns the correct GUID
        laguid = LaGuid()
        guid = laguid.guid()
        self.assertEqual(guid, laguid.guid())

    def test_setGuid_method(self):
        # Test that setGuid method sets the GUID correctly
        laguid = LaGuid()
        new_guid = QUuid.createUuid().toString(QUuid.StringFormat.WithoutBraces)
        laguid.setGuid(new_guid)
        self.assertEqual(new_guid, laguid.guid())

        # Test that setGuid method generates a new GUID when None is provided
        laguid.setGuid(None)
        self.assertTrue(QUuid(laguid.guid()).isNull() == False)
        self.assertNotEqual(new_guid, laguid.guid())

if __name__ == '__main__':
    unittest.main()