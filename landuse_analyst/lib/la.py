# la.py
from typing import Dict, List, Tuple

class LaFoodSource:
    def __init__(self):
        self.guid = ""
        self.name = ""
        self.description = ""
        self.energy = 0.0
        self.protein = 0.0
        self.fiber = 0.0
        self.calcium = 0.0
        self.phosphorus = 0.0
        self.magnesium = 0.0
        self.potassium = 0.0
        self.sodium = 0.0
        self.zinc = 0.0
        self.copper = 0.0
        self.manganese = 0.0
        self.selenium = 0.0
        self.vitamin_a = 0.0
        self.vitamin_d = 0.0
        self.vitamin_e = 0.0
        self.vitamin_c = 0.0
        self.vitamin_b1 = 0.0
        self.vitamin_b2 = 0.0
        self.vitamin_b3 = 0.0
        self.vitamin_b6 = 0.0
        self.vitamin_b12 = 0.0
        self.folate = 0.0
        self.pantothenic_acid = 0.0
        self.biotin = 0.0
        self.choline = 0.0
        self.inositol = 0.0
        self.vitamin_k = 0.0
        self.nutrient_density = 0.0
        self.cost = 0.0

class La:
    def __init__(self):
        self.guid = ""
        self.name = ""
        self.description = ""
        self.land_area = 0.0
        self.herd_size = (0.0, 0.0)
        self.herd_size_units = ""
        self.land_being_grazed = ""
        self.area_units = ""
        self.land_found = ""
        self.energy_type = ""
        self.energy_required = 0.0
        self.energy_provided = 0.0
        self.protein_required = 0.0
        self.protein_provided = 0.0
        self.fiber_required = 0.0
        self.fiber_provided = 0.0
        self.calcium_required = 0.0
        self.calcium_provided = 0.0
        self.phosphorus_required = 0.0
        self.phosphorus_provided = 0.0
        self.magnesium_required = 0.0
        self.magnesium_provided = 0.0
        self.potassium_required = 0.0
        self.potassium_provided = 0.0
        self.sodium_required = 0.0
        self.sodium_provided = 0.0
        self.zinc_required = 0.0
        self.zinc_provided = 0.0
        self.copper_required = 0.0
        self.copper_provided = 0.0
        self.manganese_required = 0.0
        self.manganese_provided = 0.0
        self.selenium_required = 0.0
        self.selenium_provided = 0.0
        self.vitamin_a_required = 0.0
        self.vitamin_a_provided = 0.0
        self.vitamin_d_required = 0.0
        self.vitamin_d_provided = 0.0
        self.vitamin_e_required = 0.0
        self.vitamin_e_provided = 0.0
        self.vitamin_c_required = 0.0
        self.vitamin_c_provided = 0.0
        self.vitamin_b1_required = 0.0
        self.vitamin_b1_provided = 0.0
        self.vitamin_b2_required = 0.0
        self.vitamin_b2_provided = 0.0
        self.vitamin_b3_required = 0.0
        self.vitamin_b3_provided = 0.0
        self.vitamin_b6_required = 0.0
        self.vitamin_b6_provided = 0.0
        self.vitamin_b12_required = 0.0
        self.vitamin_b12_provided = 0.0
        self.folate_required = 0.0
        self.folate_provided = 0.0
        self.pantothenic_acid_required = 0.0
        self.pantothenic_acid_provided = 0.0
        self.biotin_required = 0.0
        self.biotin_provided = 0.0
        self.choline_required = 0.0
        self.choline_provided = 0.0
        self.inositol_required = 0.0
        self.inositol_provided = 0.0
        self.vitamin_k_required = 0.0
        self.vitamin_k_provided = 0.0
        self.nutrient_density_required = 0.0
        self.nutrient_density_provided = 0.0
        self.cost_required = 0.0
        self.cost_provided = 0.0
        self.food_sources = {}
        self.raster_info = ((("", ""), ("", "")),)
        self.report = {}

class LaTripleMap:
    def __init__(self):
        self.animal_guid = ""
        self.enabled = False
        self.animal_parameters_guid = ""

class LaRasterInfo:
    def __init__(self):
        self.animal_raster = (("",""), ("",""))
        self.plant_raster = (("",""), ("",""))

class HerdSize:
    def __init__(self):
        self.min_size = 0.0
        self.max_size = 0.0

class LaReportMap:
    def __init__(self):
        self.guid = ""
        self.name = ""
        self.value = 0.0

class Priority:
    NoPriority = 0 # this was None but that is reserved in Python so changed to this - JJ
    High = 1
    Medium = 2
    Low = 3

class Status:
    MoreThanEnoughToCompletelySatisfy = 0
    NotEnoughToCompletelySatisfy = 1

class LandBeingGrazed:
    Common = 0
    Unique = 1

class AreaUnits:
    Dunum = 0
    Hectare = 1

class LandFound:
    NotEnough = 0
    TooMuch = 1
    FoundTarget = 2

class EnergyType:
    KCalories = 0
    TDN = 1


"""

This code defines several classes and enums in Python that correspond to the
    classes and enums defined in the original C++ la.h file.

LaFoodSource, La, LaTripleMap, LaRasterInfo, HerdSize, and LaReportMap classes
    are equivalent to their counterparts in the original file.

Priority, Status, LandBeingGrazed, AreaUnits, LandFound, and EnergyType enums
    are also equivalent to their counterparts in the original file.

"""