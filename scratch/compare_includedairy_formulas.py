#!/usr/bin/env python3
"""
compare_includedairy_formulas.py — Side-by-side comparison

Compares two formulations of 'Animals First, Include Dairy':

  CURRENT   — the formula currently in la.lib.lacalculations.
              Direct port of C++ lamodel.cpp::doCalcsAnimalsFirstIncludeDiary
              (line 736 onwards). Dairy is computed *per offspring*:
              c21 = e7 * e3, where e7 is the offspring count solved from
              the meat target.

  AFID      — based on the abandoned C++ getAreaTargetsAnimalsMapAFID
              (line 1485 onwards). Dairy is computed *per animal*'s
              milk supply: kcal_from_milk = (lactationTime - weaningAge)
                                         * milkFoodValue * milkGramsPerDay
              and then dairy directly reduces the meat target.
              The * 1000 units bug in C++ is corrected here.

Inputs match the QGIS UI scenario the user verified earlier:
  pop=100, cal=2500/day, dietPercent=20 (animal), meatPercent=90 (tame),
  dairyUtilisation=100, percentFromCrops=90, 4 animals (Sheep/Cow/Pig/Goat)

Run from project root:
  python3 scratch/compare_includedairy_formulas.py
"""

import sys, os
sys.path.insert(0, '/usr/share/qgis/python')
sys.path.insert(0, '.')

from qgis.PyQt.QtCore import QCoreApplication
_app = QCoreApplication([])

from la.lib.lautils import LaUtils
LaUtils.debug.setEnabled(False)
from la.lib.lacalculations import doCalcsAnimalsFirstIncludeDairy
from types import SimpleNamespace
import xml.etree.ElementTree as ET


# -----------------------------------------------------------------------
# Build model inputs from the live data dir
# -----------------------------------------------------------------------
HOME = os.path.expanduser('~/.landuseAnalyst')

def load_param_map(subdir, parent_tag):
    """Return {parent_guid: param_guid} for selected animals/crops."""
    out = {}
    d = os.path.join(HOME, subdir)
    for f in os.listdir(d):
        if not f.endswith('.xml'):
            continue
        r = ET.parse(os.path.join(d, f)).getroot()
        parent = r.findtext(parent_tag, '')
        if parent:
            out[parent] = r.get('guid', '')
    return out

animal_param_by_animal = load_param_map('animalParameterProfiles', 'animal')
crop_param_by_crop = load_param_map('cropParameterProfiles', 'crop')

# All 4 animals selected (Sheep, Cow, Pig, Goat)
SHEEP = 'f1a2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6'
COW   = '2a3b4c5d-6e7f-8a9b-0c1d-e2f3a4b5c6d7'
PIG   = '1f2a3b4c-5d6e-7f8a-9b0c-d1e2f3a4b5c6'
GOAT  = '3b4c5d6e-7f8a-9b0c-1d2e-f3a4b5c6d7e8'

mAnimalsMap = {a: animal_param_by_animal[a] for a in (SHEEP, COW, PIG, GOAT)
               if a in animal_param_by_animal}

# Build crops map from all crops with matching params
mCropsMap = {}
for f in os.listdir(os.path.join(HOME, 'cropProfiles')):
    if not f.endswith('.xml'):
        continue
    r = ET.parse(os.path.join(HOME, 'cropProfiles', f)).getroot()
    g = r.get('guid', '')
    if g in crop_param_by_crop:
        mCropsMap[g] = crop_param_by_crop[g]

# UI scenario (matches the screenshot the user verified)
MODEL_INPUTS = dict(
    mPopulation=100,
    mCaloriesPerPersonDaily=2500,
    mDietPercent=20,
    mMeatPercent=90,
    mDairyUtilisation=100,
    mPercentOfDietThatIsFromCrops=90,
    mAnimalsMap=mAnimalsMap,
    mCropsMap=mCropsMap,
    mDietLabels=None,
)


# -----------------------------------------------------------------------
# AFID-variant formula (Python implementation; fixes C++ units bug)
# -----------------------------------------------------------------------
def afid_calc(theModel):
    """Pure AFID formula: per-animal milk supply for dairy, residual meat
    target split by percentTameMeat. Returns a dict of aggregate diet
    portions + per-animal contributions so we can compare to CURRENT."""
    pop  = theModel.mPopulation
    cal  = theModel.mCaloriesPerPersonDaily
    dietPct  = theModel.mDietPercent * 0.01
    meatPct  = theModel.mMeatPercent * 0.01
    dairyUtil = theModel.mDairyUtilisation * 0.01
    cropPct  = theModel.mPercentOfDietThatIsFromCrops * 0.01

    settlement_kcal = pop * cal * 365.0
    animal_target_kcal = settlement_kcal * dietPct

    # Per-animal dairy supply (AFID structure, units-corrected: * 0.001)
    per_animal = {}
    total_dairy_potential_kcal = 0.0
    for guid, param_guid in theModel.mAnimalsMap.items():
        a = LaUtils.getAnimal(guid)
        # AFID's intent: kcal_from_milk = days_milking * milkFoodValue * milkGramsPerDay_in_kg
        days_milking = a.lactationTime - a.weaningAge
        milk_kg_per_day = a.milkGramsPerDay * 0.001
        kcal_from_milk = days_milking * a.milkFoodValue * milk_kg_per_day
        per_animal[guid] = dict(
            name=a.name,
            dairy_potential_kcal=kcal_from_milk,
        )
        total_dairy_potential_kcal += kcal_from_milk

    dairy_kcal = dairyUtil * total_dairy_potential_kcal
    meat_target_kcal = max(0.0, animal_target_kcal - dairy_kcal)
    wild_meat_kcal = meat_target_kcal * (1.0 - meatPct)
    tame_meat_kcal = meat_target_kcal * meatPct

    # Per-animal: split tame_meat by percentTameMeat
    for guid, param_guid in theModel.mAnimalsMap.items():
        p = LaUtils.getAnimalParameter(param_guid)
        share = (p.percentTameMeat * 0.01) if p else 0.0
        # apportion this animal's contribution
        actual_dairy = per_animal[guid]['dairy_potential_kcal'] * dairyUtil
        per_animal[guid]['dairy_kcal'] = actual_dairy
        per_animal[guid]['tame_meat_kcal'] = tame_meat_kcal * share
        per_animal[guid]['wild_meat_share_kcal'] = wild_meat_kcal * share
        per_animal[guid]['share'] = share

    # Aggregate diet portions
    plants_kcal = settlement_kcal - tame_meat_kcal - wild_meat_kcal - dairy_kcal
    crops_kcal = plants_kcal * cropPct
    wild_plants_kcal = plants_kcal * (1.0 - cropPct)

    # CLEAN percentages: value / settlement (no AFID weird denominator)
    return dict(
        dairy_pct=100. * dairy_kcal / settlement_kcal,
        tame_meat_pct=100. * tame_meat_kcal / settlement_kcal,
        wild_meat_pct=100. * wild_meat_kcal / settlement_kcal,
        crops_pct=100. * crops_kcal / settlement_kcal,
        wild_plants_pct=100. * wild_plants_kcal / settlement_kcal,
        dairy_mcal=dairy_kcal * 1e-6,
        tame_meat_mcal=tame_meat_kcal * 1e-6,
        wild_meat_mcal=wild_meat_kcal * 1e-6,
        crops_mcal=crops_kcal * 1e-6,
        wild_plants_mcal=wild_plants_kcal * 1e-6,
        per_animal=per_animal,
        settlement_mcal=settlement_kcal * 1e-3,
    )


def current_calc_result(theModel):
    """Call the actual production CURRENT function and extract aggregates."""
    dl = doCalcsAnimalsFirstIncludeDairy(theModel)
    return dict(
        dairy_pct=dl.dairyPortionPct,
        tame_meat_pct=dl.tameMeatPortionPct,
        wild_meat_pct=dl.wildAnimalPortionPct,
        crops_pct=dl.cropsPortionPct,
        wild_plants_pct=dl.wildPlantsPortionPct,
        dairy_mcal=dl.dairyMCalories,
        tame_meat_mcal=dl.animalMCalories,
        wild_meat_mcal=dl.wildAnimalMCalories,
        crops_mcal=dl.cropMCalories,
        wild_plants_mcal=dl.wildPlantsMCalories,
        settlement_mcal=dl.megaCaloriesSettlementAnnual,
        per_animal_reports=dl.animalCalcsReportMap,
    )


# -----------------------------------------------------------------------
# Side-by-side display
# -----------------------------------------------------------------------
def main():
    print("=" * 78)
    print("  Animals First, Include Dairy — CURRENT vs AFID side-by-side")
    print("  Inputs: pop=100, cal=2500/day, diet=20% animal, meat=90% tame,")
    print("          dairy util=100%, percent from crops=90%, 4 animals")
    print("=" * 78)
    print()

    model = SimpleNamespace(**MODEL_INPUTS)
    cur = current_calc_result(model)
    # Need a fresh model — current_calc_result writes to mDietLabels
    model = SimpleNamespace(**MODEL_INPUTS)
    afid = afid_calc(model)

    W = 22
    print(f"  {'Metric':<{W}} {'CURRENT (c21/e7)':>20} {'AFID (milk supply)':>20} {'Δ':>10}")
    print(f"  {'-'*W} {'-'*20} {'-'*20} {'-'*10}")
    rows = [
        ('Dairy %',        cur['dairy_pct'],       afid['dairy_pct']),
        ('Tame Meat %',    cur['tame_meat_pct'],   afid['tame_meat_pct']),
        ('Wild Meat %',    cur['wild_meat_pct'],   afid['wild_meat_pct']),
        ('Crops %',        cur['crops_pct'],       afid['crops_pct']),
        ('Wild Plants %',  cur['wild_plants_pct'], afid['wild_plants_pct']),
        ('— sum %',
            cur['dairy_pct']+cur['tame_meat_pct']+cur['wild_meat_pct']
                +cur['crops_pct']+cur['wild_plants_pct'],
            afid['dairy_pct']+afid['tame_meat_pct']+afid['wild_meat_pct']
                +afid['crops_pct']+afid['wild_plants_pct']),
        ('Dairy MCals',     cur['dairy_mcal'],      afid['dairy_mcal']),
        ('Tame Meat MCals', cur['tame_meat_mcal'],  afid['tame_meat_mcal']),
        ('Wild Meat MCals', cur['wild_meat_mcal'],  afid['wild_meat_mcal']),
        ('Crops MCals',     cur['crops_mcal'],      afid['crops_mcal']),
        ('Wild Plants MCals', cur['wild_plants_mcal'], afid['wild_plants_mcal']),
        ('Settlement MCals', cur['settlement_mcal'], afid['settlement_mcal']),
    ]
    for label, c, a in rows:
        d = a - c
        print(f"  {label:<{W}} {c:>20.4f} {a:>20.4f} {d:>+10.4f}")

    # Per-animal AFID detail
    print()
    print("  AFID per-animal breakdown (MCals contributed):")
    print(f"  {'Animal':<10} {'share %':>10} {'dairy':>10} {'tame meat':>12} {'wild meat':>12}")
    print(f"  {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*12}")
    for guid, info in afid['per_animal'].items():
        print(f"  {info['name']:<10} {info['share']*100:>10.2f} "
              f"{info['dairy_kcal']*1e-6:>10.4f} "
              f"{info['tame_meat_kcal']*1e-6:>12.4f} "
              f"{info['wild_meat_share_kcal']*1e-6:>12.4f}")
    print()
    print("=" * 78)

if __name__ == '__main__':
    main()
