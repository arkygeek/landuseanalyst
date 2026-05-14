#!/usr/bin/env python3
"""
verify_thesis_scenario.py — Min Pop / Chalcolithic / Shuna verification

Compares the live production calculation engine's output against the
authoritative values from the user's macOS Numbers spreadsheet — the
same spreadsheet that produced the thesis figures.

Spreadsheet CSV dump:    scratch/thesis_scenarios/min_pop_chalcolithic/
Mode used:               doCalcsAnimalsFirstDairySeparate

The spreadsheet uses DairySeparate's "Final Value per juvenile = meat +
culled_mothers + culled_adult_males" (no dairy in e10), confirmed by
06_calculations.csv: Cow "Value per juvenile = 640 MCal" (meat-only)
and "Final Value per juvenile = 750.53 MCal" (meat + culled). The
IncludeDairy mode uses e10 = meat + dairy, a different formula that
produces different offspring counts. So even though "dairy" appears in
the spreadsheet's diet output, the underlying algorithm is DairySeparate's.

Verified metrics:
  - 5 diet-MCal categories (Domestic Meat, Wild Meat, Dairy, Crops, Wild Plants)
  - 5 diet portion percentages
  - Settlement and per-person MCal totals
  - Per-crop area targets (Ha) — fed to QGIS land identification

Run from project root:
  python3 scratch/verify_thesis_scenario.py
"""
import os, sys
sys.path.insert(0, '/usr/share/qgis/python')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qgis.PyQt.QtCore import QCoreApplication
_app = QCoreApplication([])
from la.lib.lautils import LaUtils
LaUtils.debug.setEnabled(False)
from la.lib.lacalculations import doCalcsAnimalsFirstDairySeparate
from types import SimpleNamespace
import xml.etree.ElementTree as ET

HOME = os.path.expanduser('~/.landuseAnalyst')


def _t(el, tag):
    return (el.findtext(tag, '') or '').strip()


def load_name_to_guid(subdir):
    out = {}
    for fname in sorted(os.listdir(os.path.join(HOME, subdir))):
        if not fname.endswith('.xml'):
            continue
        r = ET.parse(os.path.join(HOME, subdir, fname)).getroot()
        out[_t(r, 'name')] = r.get('guid', fname[:-4])
    return out


def load_param_by_parent(subdir, parent_tag):
    out = {}
    for fname in sorted(os.listdir(os.path.join(HOME, subdir))):
        if not fname.endswith('.xml'):
            continue
        r = ET.parse(os.path.join(HOME, subdir, fname)).getroot()
        parent = _t(r, parent_tag)
        if parent:
            out[parent] = r.get('guid', fname[:-4])
    return out


# Scenario per scratch/thesis_scenarios/min_pop_chalcolithic/03_animal_selection.csv
# and 09_crop_selection.csv
SELECTED_ANIMALS = ['Sheep', 'Pig', 'Cow', 'Goat']
SELECTED_CROPS   = ['Horse Bean', 'Einkorn', 'Emmer', 'Lentils',
                    'Peas', 'Olives', 'Bitter Vetch', 'Barley']

# Inputs per 03_animal_selection.csv + 09_crop_selection.csv
MODEL_INPUTS = dict(
    mPopulation=100,
    mCaloriesPerPersonDaily=2500,
    mDietPercent=10,         # "ALL Meat %" — meat portion of diet
    mMeatPercent=99,         # "Domestic Animal Contribution" — tame meat fraction
    mDairyUtilisation=50,
    mPercentOfDietThatIsFromCrops=90,
    mLimitDairy=False,
    mLimitDairyPercentage=100,
)

# Expected outputs per 11_diet_calculations.csv
EXPECTED = {
    'animalMCalories':                  9_033.750,
    'wildAnimalMCalories':                 91.250,
    'dairyMCalories':                   4_338.044,
    'cropMCalories':                   70_008.261,
    'wildPlantsMCalories':              7_778.696,
    'megaCaloriesSettlementAnnual':    91_250.000,
    'kiloCaloriesIndividualAnnual':   912_500.000,
    'tameMeatPortionPct':                   9.90,
    'wildAnimalPortionPct':                 0.10,
    'dairyPortionPct':                      4.75,
    'cropsPortionPct':                     76.72,
    'wildPlantsPortionPct':                 8.52,
}
TOL_PCT_ABS = 0.5
TOL_REL = 0.005

# Per-crop area targets in Ha (from 10_crop_targets.csv "Area Target Ha")
EXPECTED_CROP_HA = {
    'Horse Bean':    2,
    'Einkorn':       8,
    'Emmer':        74,
    'Lentils':       3,
    'Peas':         14,
    'Olives':        1,
    'Bitter Vetch':  4,
    'Barley':       80,
}
TOL_CROP_HA = 1.5

# Per-animal grazing-land area targets in Ha (from 05_animal_targets.csv "Ha Required")
EXPECTED_ANIMAL_HA = {
    'Sheep':   9,
    'Pig':    17,
    'Cow':    28,
    'Goat':   30,
}
TOL_ANIMAL_HA = 1.5


def build_model():
    an_name_to_guid = load_name_to_guid('animalProfiles')
    cr_name_to_guid = load_name_to_guid('cropProfiles')
    an_param_by_parent = load_param_by_parent('animalParameterProfiles', 'animal')
    cr_param_by_parent = load_param_by_parent('cropParameterProfiles', 'crop')

    selected_animals_map = {}
    for n in SELECTED_ANIMALS:
        guid = an_name_to_guid.get(n)
        if guid and guid in an_param_by_parent:
            selected_animals_map[guid] = an_param_by_parent[guid]

    selected_crops_map = {}
    for n in SELECTED_CROPS:
        guid = cr_name_to_guid.get(n)
        if guid and guid in cr_param_by_parent:
            selected_crops_map[guid] = cr_param_by_parent[guid]

    m = SimpleNamespace(**MODEL_INPUTS,
                        mAnimalsMap=selected_animals_map,
                        mCropsMap=selected_crops_map,
                        mDietLabels=None,
                        mCalcsCropsMap={}, mCalcsAnimalsMap={},
                        mValueMap={}, mAnimalCalcReport={},
                        mAreaTargetsCropsMap={},
                        mCommonGrazingValue=1.0)

    name_by_guid_crop = {v: k for k, v in cr_name_to_guid.items()}
    return m, selected_animals_map, selected_crops_map, name_by_guid_crop


def check(name, expected, actual, tol_abs=None, rel=None):
    if expected == 0:
        ok = abs(actual) <= (tol_abs or 1e-9)
    elif tol_abs is not None:
        ok = abs(actual - expected) <= tol_abs
    elif rel is not None:
        ok = abs(actual - expected) <= abs(expected) * rel
    else:
        ok = abs(actual - expected) <= max(0.01, abs(expected) * 1e-4)
    mark = 'PASS' if ok else 'FAIL'
    delta = actual - expected
    print(f"  {name:<35} {expected:>16,.4f} {actual:>16,.4f} {delta:>+12,.4f} {mark:>5}")
    return ok


def main():
    print("=" * 100)
    print("  Thesis Verification — Min Pop / Chalcolithic / Shuna")
    print("  Source: scratch/thesis_scenarios/min_pop_chalcolithic/ (CSV dump)")
    print("  Mode:   doCalcsAnimalsFirstDairySeparate")
    print("=" * 100)

    model, animals, crops, name_by_guid = build_model()
    print(f"\n  Animals selected: {len(animals)}/{len(SELECTED_ANIMALS)}   "
          f"Crops selected: {len(crops)}/{len(SELECTED_CROPS)}")

    dl = doCalcsAnimalsFirstDairySeparate(model)

    # --- Diet aggregates ---
    print("\n  --- Diet aggregates ---")
    print(f"  {'Metric':<35} {'Spreadsheet':>16} {'Plugin':>16} {'Δ':>12} {'':>5}")
    print(f"  {'-'*35} {'-'*16} {'-'*16} {'-'*12} {'-'*5}")
    all_ok = True
    pct_keys = {'tameMeatPortionPct', 'wildAnimalPortionPct', 'dairyPortionPct',
                'cropsPortionPct', 'wildPlantsPortionPct'}
    for key, exp in EXPECTED.items():
        act = getattr(dl, key)
        if key in pct_keys:
            ok = check(key, exp, act, tol_abs=TOL_PCT_ABS)
        else:
            ok = check(key, exp, act, rel=TOL_REL)
        all_ok &= ok

    # --- Per-crop areas ---
    print("\n  --- Per-crop area targets (Ha) — what QGIS uses for land identification ---")
    print(f"  {'Crop':<35} {'Spreadsheet':>16} {'Plugin':>16} {'Δ':>12} {'':>5}")
    print(f"  {'-'*35} {'-'*16} {'-'*16} {'-'*12} {'-'*5}")
    for crop_name, exp_ha in EXPECTED_CROP_HA.items():
        guid = next((g for g, n in name_by_guid.items() if n == crop_name), None)
        if guid is None or guid not in dl.cropCalcsReportMap:
            print(f"  {crop_name:<35} {'N/A':>16} {'MISSING':>16}")
            all_ok = False
            continue
        actual_ha = dl.cropCalcsReportMap[guid][1]
        ok = check(crop_name, exp_ha, actual_ha, tol_abs=TOL_CROP_HA)
        all_ok &= ok

    # --- Per-animal grazing-land areas ---
    print("\n  --- Per-animal grazing-land area targets (Ha) — for grazing identification ---")
    print(f"  {'Animal':<35} {'Spreadsheet':>16} {'Plugin':>16} {'Δ':>12} {'':>5}")
    print(f"  {'-'*35} {'-'*16} {'-'*16} {'-'*12} {'-'*5}")
    an_name_by_guid = {v: k for k, v in load_name_to_guid('animalProfiles').items()}
    for an_name, exp_ha in EXPECTED_ANIMAL_HA.items():
        guid = next((g for g, n in an_name_by_guid.items() if n == an_name), None)
        animal_report_map = getattr(model, 'mAnimalCalcReport', {}) or {}
        if guid is None or guid not in animal_report_map:
            print(f"  {an_name:<35} {exp_ha:>16,.4f} {'MISSING':>16}")
            all_ok = False
            continue
        actual_ha = animal_report_map[guid][1]
        ok = check(an_name, exp_ha, actual_ha, tol_abs=TOL_ANIMAL_HA)
        all_ok &= ok

    print(f"\n  totalLandNeeded (sum of crop + animal Ha): {dl.totalLandNeeded:.2f} Ha")
    print(f"  Spreadsheet total (crops 184 + animals 84):    268 Ha")
    print(f"  (Approximate; spreadsheet rounds individual values to nearest int.)")

    print(f"\n  Result: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
