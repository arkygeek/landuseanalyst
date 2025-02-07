import sys
import os
import unittest

class TestSysPath(unittest.TestCase):
    def test_sys_path(self):
        # Get the parent directory
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Check if the parent directory is in sys.path
        self.assertIn(parent_dir, sys.path, "Parent directory not in sys.path")

        # Try importing a module from the parent directory
        try:
            from landuse_analyst.lib import lautils
        except ImportError as e:
            self.fail(f"Failed to import module from parent directory: {e}")

if __name__ == "__main__":
    unittest.main()