import sys
import os

# Print the initial sys.path
print("Initial sys.path:", sys.path)

# Update the sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Print the updated sys.path
print("Updated sys.path:", sys.path)

import unittest

# Use relative imports to import modules from la/lib
from la.lib.la import La
from la.lib.lafoodsource import LaFoodSource

class TestLa(unittest.TestCase):

    def setUp(self):
        # Set up any necessary initial data or state
        self.la_instance = La()

    def test_la_triple_map(self):
        # Test the LaTripleMap attribute
        self.assertIsInstance(self.la_instance.LaTripleMap, dict)
        for key, value in self.la_instance.LaTripleMap.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, tuple)
            self.assertIsInstance(value[0], bool)
            self.assertIsInstance(value[1], str)

    def test_la_raster_info(self):
        # Test the LaRasterInfo attribute
        self.assertIsInstance(self.la_instance.LaRasterInfo, tuple)
        for item in self.la_instance.LaRasterInfo:
            self.assertIsInstance(item, tuple)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], str)

    def test_la_food_source_map(self):
        # Test the LaFoodSourceMap attribute
        self.assertIsInstance(self.la_instance.LaFoodSourceMap, dict)
        for key, value in self.la_instance.LaFoodSourceMap.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, LaFoodSource)

    def test_herd_size(self):
        # Test the HerdSize attribute
        self.assertIsInstance(self.la_instance.HerdSize, tuple)
        self.assertIsInstance(self.la_instance.HerdSize[0], float)
        self.assertIsInstance(self.la_instance.HerdSize[1], float)

if __name__ == '__main__':
    unittest.main()