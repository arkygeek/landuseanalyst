import xml.etree.ElementTree as ET
import os

def update_crop(guid, updates):
    filepath = os.path.expanduser(f"~/.landuseAnalyst/cropProfiles/{guid}.xml")
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
            new_elem = ET.SubElement(root, tag)
            new_elem.text = str(value)

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Updated {guid}")

# Table E.1 Data
updates = {
    "a1b2c3d4-e5f6-7890-abcd-ef1234567890": { # Horse Bean
        "cropYield": 500, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 800
    },
    "b2c3d4e5-f6a7-8901-bcde-f23456789012": { # Einkorn
        "cropYield": 500, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 800
    },
    "c3d4e5f6-a7b8-9012-cdef-34567890123a": { # Emmer
        "cropYield": 500, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 800
    },
    "d4e5f6a7-b8c9-0123-defg-4567890123bc": { # Lentils
        "cropYield": 500, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 800
    },
    "e5f6a7b8-c9d0-1234-efgh-567890123cde": { # Peas
        "cropYield": 300, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 800
    },
    "f6a7b8c9-d0e1-2345-fghi-67890123def4": { # Olives
        "cropYield": 150, "cropCalories": 3250, "fodderProduction": 100, "fodderCalories": 800
    },
    "d0e1f2a3-b4c5-6789-jklm-0123b8901234": { # Barley
        "cropYield": 400, "cropCalories": 3000, "fodderProduction": 300, "fodderCalories": 1420
    }
}

for guid, data in updates.items():
    update_crop(guid, data)
