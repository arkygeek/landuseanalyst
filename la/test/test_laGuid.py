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
        # Test that a new LaGuid object has an empty GUID by default
        # (setGuid must be called explicitly to populate it)
        myLaGuid = LaGuid()
        self.assertEqual(myLaGuid.guid, "")

    def test_setGuid_generates_new(self):
        # Test that setGuid(None) generates a valid GUID
        myLaGuid = LaGuid()
        myLaGuid.setGuid(None)
        self.assertTrue(QUuid(myLaGuid.guid).isNull() == False)

    def test_setGuid_explicit(self):
        # Test that setGuid sets the GUID correctly
        myLaGuid = LaGuid()
        myNewGuid = QUuid.createUuid().toString(QUuid.StringFormat.WithoutBraces)
        myLaGuid.setGuid(myNewGuid)
        self.assertEqual(myNewGuid, myLaGuid.guid)

        # Test that setGuid(None) generates a new GUID different from the previous one
        myLaGuid.setGuid(None)
        self.assertTrue(QUuid(myLaGuid.guid).isNull() == False)
        self.assertNotEqual(myNewGuid, myLaGuid.guid)

    def test_guid_setter_property(self):
        # Test that the property setter also writes _mGuid consistently
        myLaGuid = LaGuid()
        myNewGuid = QUuid.createUuid().toString(QUuid.StringFormat.WithoutBraces)
        myLaGuid.guid = myNewGuid  # via property
        self.assertEqual(myNewGuid, myLaGuid.guid)
        # And setGuid afterwards should still work
        myLaGuid.setGuid(None)
        self.assertNotEqual(myNewGuid, myLaGuid.guid)

if __name__ == '__main__':
    unittest.main()
