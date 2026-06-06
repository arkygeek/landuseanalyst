#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_thesis_scenarios.py — Generate the 108 thesis scenarios as unified XML files.
"""

import os
import sys
import uuid
import xml.etree.ElementTree as ET

# Prepend paths for QGIS import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test")))

from la.test.utilities import get_qgis_app
QGIS_APP = get_qgis_app()

from la.lib.lamodel import LaModel
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lautils import LaUtils

# Define Periods
class PeriodInfo:
    def __init__(self, key, label, pop_min, pop_max, crops, animals):
        self.key = key
        self.label = label
        self.pop_min = pop_min
        self.pop_max = pop_max
        self.crops = crops
        self.animals = animals

CHALCOLITHIC = PeriodInfo(
    key="chalcolithic",
    label="Chalcolithic",
    pop_min=100.0,
    pop_max=600.0,
    animals={
        "Sheep": 3.59,
        "Goat": 11.95,
        "Cow": 47.81,
        "Pig": 36.65,
    },
    crops={
        "Horse Bean": 1.09,
        "Einkorn": 5.47,
        "Emmer": 52.52,
        "Lentils": 1.09,
        "Peas": 3.28,
        "Olives": 1.53,
        "Bitter Vetch": 2.19,
        "Barley": 32.83,
    }
)

EEB1 = PeriodInfo(
    key="eeb1",
    label="Early EB I",
    pop_min=1000.0,
    pop_max=3000.0,
    animals={
        "Sheep": 12.26,
        "Goat": 10.38,
        "Cow": 37.74,
        "Pig": 39.62,
    },
    crops={
        "Horse Bean": 0.81,
        "Einkorn": 1.54,
        "Emmer": 44.00,
        "Lentils": 32.00,
        "Peas": 11.79,
        "Olives": 3.58,
        "Bitter Vetch": 0.13,
        "Barley": 6.15,
    }
)

LEB1 = PeriodInfo(
    key="leb1",
    label="Late EB I",
    pop_min=2000.0,
    pop_max=6000.0,
    animals={
        "Sheep": 7.75,
        "Goat": 7.75,
        "Cow": 78.87,
        "Pig": 5.63,
    },
    crops={
        "Horse Bean": 1.00,
        "Einkorn": 11.79,
        "Emmer": 46.00,
        "Lentils": 4.13,
        "Peas": 15.38,
        "Olives": 4.69,
        "Bitter Vetch": 1.12,
        "Barley": 15.89,
    }
)

PERIODS = [CHALCOLITHIC, EEB1, LEB1]
MEAT_LEVELS = [10.0, 20.0, 30.0]
DAIRY_FEED_COMBOS = [
    (0.0, True),
    (0.0, False),
    (50.0, True),
    (50.0, False),
    (100.0, True),
    (100.0, False),
]

def generate_scenarios():
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "thesis_scenarios"))
    os.makedirs(output_dir, exist_ok=True)
    print(f"Generating scenarios to: {output_dir}")

    # Load baseline crops and animals from the user settings directory
    available_crops = LaUtils.getAvailableCrops()
    available_animals = LaUtils.getAvailableAnimals()

    print(f"Loaded {len(available_crops)} crops and {len(available_animals)} animals from system.")

    for period in PERIODS:
        print(f"\nProcessing Period: {period.label}...")
        
        # 1. Resolve crop parameters for this period
        resolved_crop_params = {}
        for crop_name, pct in period.crops.items():
            # Find crop by name
            crop = None
            for c in available_crops.values():
                if c.name == crop_name:
                    crop = c
                    break
            
            if crop is None:
                print(f"Error: Crop '{crop_name}' not found!")
                continue
            
            # Find default crop parameter for this crop
            baseline_param = None
            crop_param_dir = LaUtils.userCropParameterProfilesDirPath()
            for filename in os.listdir(crop_param_dir):
                if filename.endswith(".xml"):
                    param = LaCropParameter()
                    with open(os.path.join(crop_param_dir, filename), "r") as f:
                        if param.fromXml(f.read()) and param.cropGuid == crop.guid:
                            baseline_param = param
                            break
            
            if baseline_param is None:
                print(f"Warning: Baseline parameter for crop '{crop_name}' not found. Creating a blank one.")
                baseline_param = LaCropParameter()
                baseline_param.cropGuid = crop.guid
                baseline_param.name = f"{crop_name} Baseline Params"
                baseline_param.useCommonLand = True
                baseline_param.useSpecificLand = False
                baseline_param.rasterName = ""
            
            # Create period specific parameter
            new_param = LaCropParameter()
            new_param.fromXml(baseline_param.toXml())
            
            if period.key == "chalcolithic":
                # Keep exact GUID for Chalcolithic if available
                new_param_guid = baseline_param.guid
            else:
                # Generate a deterministic new parameter GUID for other periods
                new_param_guid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{crop.guid}_{period.key}"))
                
            new_param.setGuid(new_param_guid)
            new_param.name = f"{crop_name} · {period.label} params"
            new_param.percentTameCrop = pct
            
            resolved_crop_params[crop.guid] = new_param

        # 2. Loop over configurations to generate the 36 scenarios per period
        scenario_idx = 0
        for meat in MEAT_LEVELS:
            for pop in [period.pop_min, period.pop_max]:
                for combo_idx, (dairy, feed) in enumerate(DAIRY_FEED_COMBOS):
                    scenario_num = scenario_idx * 6 + combo_idx + 1
                    
                    # Create model
                    model = LaModel()
                    
                    # Generate deterministic model GUID
                    model_guid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"shuna_{period.key}_s{scenario_num:02d}"))
                    model.setGuid(model_guid)
                    
                    feed_tag = "feed" if feed else "no feed"
                    model.mName = (
                        f"Shuna · {period.label} · S{scenario_num:02d} · "
                        f"pop {int(pop):,} · meat {int(meat)}% · "
                        f"dairy {int(dairy)}% · {feed_tag}"
                    )
                    model.mPopulation = int(pop)
                    model.mPeriod = period.label
                    model.mProjection = 32636
                    model.mEasting = 744800.0
                    model.mNorthing = 3611100.0
                    model.mEuclideanDistance = False
                    model.mWalkingTime = True
                    model.mPathDistance = False
                    model.mPrecision = 5
                    model.mDietPercent = int(meat)
                    model.mPercentOfDietThatIsFromCrops = 90
                    model.mMeatPercent = 99
                    model.mCaloriesPerPersonDaily = 2500
                    model.mBaseOnPlants = False
                    model.mIncludeDairy = True
                    model.mLimitDairy = False
                    model.mLimitDairyPercentage = 0
                    model.mDairyUtilisation = int(dairy)
                    
                    # Clear/override registries in LaUtils
                    LaUtils.clearRegistries()
                    
                    # Register the crops and resolved crop parameter sets in-memory
                    for crop_guid, crop_param in resolved_crop_params.items():
                        crop = available_crops[crop_guid]
                        LaUtils.registerCrop(crop)
                        LaUtils.registerCropParameter(crop_param)
                        model.mCropsMap[crop_guid] = crop_param.guid
                    
                    # Resolve animal parameters for this configuration
                    for animal_name, pct in period.animals.items():
                        animal = None
                        for a in available_animals.values():
                            if a.name == animal_name:
                                animal = a
                                break
                        if animal is None:
                            print(f"Error: Animal '{animal_name}' not found!")
                            continue
                        
                        # Find default animal parameter
                        baseline_param = None
                        animal_param_dir = LaUtils.userAnimalParameterProfilesDirPath()
                        for filename in os.listdir(animal_param_dir):
                            if filename.endswith(".xml"):
                                param = LaAnimalParameter()
                                with open(os.path.join(animal_param_dir, filename), "r") as f:
                                    if param.fromXml(f.read()) and param.animalGuid == animal.guid:
                                        baseline_param = param
                                        break
                        
                        if baseline_param is None:
                            print(f"Warning: Baseline parameter for animal '{animal_name}' not found. Creating a blank one.")
                            baseline_param = LaAnimalParameter()
                            baseline_param.animalGuid = animal.guid
                            baseline_param.name = f"{animal_name} Baseline Params"
                        
                        new_param = LaAnimalParameter()
                        new_param.fromXml(baseline_param.toXml())
                        
                        if period.key == "chalcolithic" and feed:
                            # Keep baseline GUID for Chalcolithic with feed
                            new_param_guid = baseline_param.guid
                        else:
                            new_param_guid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{animal.guid}_{period.key}_{feed}"))
                        
                        new_param.setGuid(new_param_guid)
                        new_param.name = f"{animal_name} · {period.label} · {'with feed' if feed else 'no feed'}"
                        new_param.percentTameMeat = pct
                        new_param.fodderUse = feed
                        
                        # If feed is False, make sure it has no fodder crops registered or fodderUse is set to False
                        if not feed:
                            new_param.fodderUse = False
                        
                        # Register in-memory
                        LaUtils.registerAnimal(animal)
                        LaUtils.registerAnimalParameter(new_param)
                        model.mAnimalsMap[animal.guid] = new_param.guid
                    
                    # Export unified XML
                    xml_data = model.exportScenario()
                    
                    # Save XML to thesis_scenarios folder
                    xml_filename = f"shuna_{period.key}_s{scenario_num:02d}.xml"
                    xml_path = os.path.join(output_dir, xml_filename)
                    with open(xml_path, "w", encoding="utf-8") as f:
                        f.write(xml_data)
                
                scenario_idx += 1

    print("\nGeneration complete!")

if __name__ == "__main__":
    generate_scenarios()
