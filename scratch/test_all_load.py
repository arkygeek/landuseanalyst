import sys
import os

# Mock QGIS environment
from qgis.PyQt.QtCore import QDir, QSettings
from qgis.PyQt.QtXml import QDomDocument

# Add project to path
sys.path.append('/home/arkygeek/dev/QGis-Projects/landuseanalyst')

from la.lib.lautils import LaUtils, MESSAGE_BUS

# Set debug enabled
LaUtils.debug.setEnabled(True)

def on_message(msg):
    print(f"LOG: {msg}")

MESSAGE_BUS.debugMessaged.connect(on_message)

print("--- Testing getAvailableAnimals ---")
animals = LaUtils.getAvailableAnimals()
print(f"Animals found: {len(animals)}")
for guid, a in animals.items():
    print(f"  - {a.name} ({guid})")

print("\n--- Testing getAvailableAnimalParameters ---")
params = LaUtils.getAvailableAnimalParameters()
print(f"Params found: {len(params)}")
for guid, p in params.items():
    print(f"  - {p.name} (links to: {p.animalGuid})")

print("\n--- Testing getAvailableCrops ---")
crops = LaUtils.getAvailableCrops()
print(f"Crops found: {len(crops)}")
for guid, c in crops.items():
    print(f"  - {c.name} ({guid})")

print("\n--- Testing getAvailableCropParameters ---")
cparams = LaUtils.getAvailableCropParameters()
print(f"Crop Params found: {len(cparams)}")
for guid, cp in cparams.items():
    print(f"  - {cp.name} (links to: {cp.cropGuid})")
