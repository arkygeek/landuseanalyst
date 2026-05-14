import os
import xml.etree.ElementTree as ET

def verify_animals():
    animals_xml_path = "la/Animals.xml"
    profiles_dir = "la/test/xmlData/animalProfiles"
    
    if not os.path.exists(animals_xml_path):
        print(f"Error: {animals_xml_path} not found.")
        return

    with open(animals_xml_path, 'r') as f:
        content = f.read()
    
    # Wrap in a dummy root to handle multiple top-level elements
    wrapped_content = f"<root>{content}</root>"
    root = ET.fromstring(wrapped_content)
    
    # la/Animals.xml seems to have a different structure, let's check
    # Usually it's <animals><animal>...</animal></animals>
    
    animals_in_master = root.findall(".//animal")
    print(f"Found {len(animals_in_master)} animals in master file.")
    
    for master_animal in animals_in_master:
        guid = master_animal.get("guid")
        name = master_animal.findtext("name")
        print(f"\nChecking animal: {name} ({guid})")
        
        profile_path = os.path.join(profiles_dir, f"{guid}.xml")
        if not os.path.exists(profile_path):
            print(f"  [MISSING] Individual profile file not found: {profile_path}")
            continue
            
        profile_tree = ET.parse(profile_path)
        profile_root = profile_tree.getroot()
        
        # Compare tags
        master_tags = {child.tag: child.text for child in master_animal if child.tag != "guid"}
        profile_tags = {child.tag: child.text for child in profile_root if child.tag != "guid"}
        
        all_tags = set(master_tags.keys()) | set(profile_tags.keys())
        
        for tag in sorted(all_tags):
            master_val = master_tags.get(tag)
            profile_val = profile_tags.get(tag)
            
            if master_val != profile_val:
                print(f"  [DIFF] {tag:25}: Master='{master_val}' vs Profile='{profile_val}'")

if __name__ == "__main__":
    verify_animals()
