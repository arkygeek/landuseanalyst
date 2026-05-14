import os
import re

def update_tag(content, animal_guid, tag, new_value):
    # Find the animal block
    pattern = rf'(<animal guid="{animal_guid}">.*?</animal>)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content
    
    animal_block = match.group(1)
    # Check if tag exists
    tag_pattern = rf'<{tag}>.*?</{tag}>'
    if re.search(tag_pattern, animal_block):
        new_tag = f'<{tag}>{new_value}</{tag}>'
        new_animal_block = re.sub(tag_pattern, new_tag, animal_block)
    else:
        # Append before closing tag
        new_tag = f'      <{tag}>{new_value}</{tag}>\n    '
        new_animal_block = animal_block.replace('</animal>', f'{new_tag}</animal>')
    
    return content.replace(animal_block, new_animal_block)

# Table F.1 Data
animal_updates = {
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
    },
    "3b4c5d6e-7f8a-9b0c-1d2e-f3a4b5c6d7e8": { # Goat
        "gestating": 3970,
        "lactating": 5410,
        "maintenance": 3200,
        "juvenile": 30,
        "deathRate": 30,
        "killWeight": 30,
        "adultWeight": 60,
    }
}

target_file = "/home/arkygeek/dev/QGis-Projects/landuseanalyst/la/Animals.xml"
with open(target_file, 'r') as f:
    content = f.read()

for guid, updates in animal_updates.items():
    for tag, val in updates.items():
        content = update_tag(content, guid, tag, val)

with open(target_file, 'w') as f:
    f.write(content)
print(f"Updated {target_file}")
