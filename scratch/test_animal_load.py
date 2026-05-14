import sys
import os

# Mock QGIS environment
from qgis.PyQt.QtCore import QDir, QSettings
from qgis.PyQt.QtXml import QDomDocument

# Add project to path
sys.path.append('/home/arkygeek/dev/QGis-Projects/landuseanalyst')

from la.lib.laanimal import LaAnimal
from la.lib.lautils import LaUtils

# Set debug enabled
LaUtils.debug.setEnabled(True)

# Path to one of the animal files I updated
path = os.path.expanduser('~/.landuseAnalyst/animalProfiles/f1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6.xml')

with open(path, 'r') as f:
    xml_content = f.read()

print(f"Testing load from: {path}")
print(f"Content length: {len(xml_content)}")
print(f"First 100 chars: {xml_content[:100]}")

animal = LaAnimal()
success = animal.fromXml(xml_content)

print(f"Success: {success}")
print(f"Name: {animal.name}")
print(f"GUID: {animal.guid}")
