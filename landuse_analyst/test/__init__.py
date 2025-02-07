# import qgis libs so that ve set the correct sip api version
import qgis   # NOQA
import landuse_analyst

# Ensure the parent directory is in the Python path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
