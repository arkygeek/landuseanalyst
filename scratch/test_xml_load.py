
import sys
import os
# Add the project root to sys.path
sys.path.append('/home/arkygeek/dev/QGis-Projects/landuseanalyst')

from qgis.PyQt.QtXml import QDomDocument
from la.lib.laanimal import LaAnimal

xml_file = '/home/arkygeek/dev/QGis-Projects/landuseanalyst/la/test/xmlData/animalProfiles/261b36dc-a9b9-4995-9c9f-15e19949c10a.xml'

with open(xml_file, 'r') as f:
    xml_content = f.read()

animal = LaAnimal()
try:
    success = animal.fromXml(xml_content)
    print(f"Load success: {success}")
    print(f"Animal Name: {animal.name}")
except Exception as e:
    print(f"Error loading animal: {e}")
    import traceback
    traceback.print_exc()
