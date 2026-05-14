import xml.etree.ElementTree as ET
import os

def update_animal(guid, updates):
    filepath = os.path.expanduser(f"~/.landuseAnalyst/animalProfiles/{guid}.xml")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    tree = ET.parse(filepath)
    root = tree.getroot()

    for tag, value in updates.items():
        elem = root.find(tag)
        if elem is not None:
            elem.text = str(value)
        else:
            # Add missing tag
            new_elem = ET.SubElement(root, tag)
            new_elem.text = str(value)

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Updated {guid}")

# Table F.1 Data
updates = {
    "f1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6": { # Sheep
        "gestating": 3970,
        "lactating": 5410,
        "maintenance": 3200,
        "juvenile": 30,
        "deathRate": 30,
        "growTime": 40,
        "breedingExpectancy": 5,
        "youngPerBirth": 1,
        "sexualMaturity": 18,
        "gestationTime": 150,
        "lactationTime": 210,
        "killWeight": 30,
        "adultWeight": 60,
        "milkGramsPerDay": 940,
        "milkFoodValue": 940,
    },
    "1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c6": { # Pig
        "gestating": 3970,
        "lactating": 5410,
        "maintenance": 0,
        "juvenile": 30,
        "deathRate": 30,
        "killWeight": 100,
        "adultWeight": 200,
        "youngPerBirth": 6,
        "gestationTime": 115,
        "lactationTime": 30,
    },
    "2a3b4c5d-6e7f-8a9b-0c1d-e2f3a4b5c6d7": { # Cow
        "gestating": 6000,
        "lactating": 7500,
        "maintenance": 5800,
        "juvenile": 30,
        "deathRate": 20,
        "growTime": 50,
        "breedingExpectancy": 8,
        "killWeight": 400,
        "adultWeight": 625,
        "milkGramsPerDay": 6000,
        "milkFoodValue": 940,
    },
    "3b4c5d6e-7f8a-9b0c-1d2e-f3a4b5c6d7e8": { # Goat
        "gestating": 3970,
        "lactating": 5410,
        "maintenance": 3200,
        "juvenile": 30,
        "deathRate": 30,
        "killWeight": 30,
        "adultWeight": 60,
        "milkGramsPerDay": 900,
        "milkFoodValue": 940,
    }
}

for guid, data in updates.items():
    update_animal(guid, data)
