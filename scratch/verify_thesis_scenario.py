#!/usr/bin/env python3
"""
verify_thesis_scenario.py — Thesis Scenario 1 verification
==========================================================
Compares the live production calculation engine against the worked example
in Chapter 5 of Jason Jorgenson's PhD thesis (Figure 5.13).

Thesis reference
----------------
  Section 5.7.1 (Chalcolithic Results), Figure 5.13:
    "Scenario 1: Chalcolithic, Minimum Population (100), Meat Portion 10%,
     Potential Dairy Utilisation = 0%, Gestating animals are fed
     supplementary feed for 90 days"

Mode used in the plugin
-----------------------
  doCalcsAnimalsFirstIncludeDairy  (Animals First, Include Dairy)
  — Dairy Utilisation is 0% in this scenario, so dairy contribution
    collapses to zero regardless of the mode; this scenario is therefore
    cleanest for verifying the percentage / Mcal split math without
    needing to trust the dairy-per-offspring formula.

Thesis inputs (Scenario 1 / Figure 5.13)
----------------------------------------
  Population                            : 100
  Calories per person per day           : 2,500  (=> 912.5 MCal/person/year)
  Diet portion from animals             : 10%
  Meat portion that is tame             : 90%   (=> 10% wild meat)
  Dairy utilisation                     : 0%
  Percent of plant diet from crops      : 90%
  Animals selected (4)                  : Sheep, Pig, Cow, Goat
  Crops selected (8)                    : Horse Bean, Einkorn, Emmer,
                                          Lentils, Peas, Olives,
                                          Bitter Vetch, Barley
  percentTameMeat per animal            : taken from live data
                                          (Sheep 3.59, Pig 36.65,
                                           Cow 47.81, Goat 11.95)
  percentTameCrop per crop              : taken from live data
                                          (Horse Bean 1.09, Einkorn 5.47,
                                           Emmer 52.52, Lentils 1.09,
                                           Peas 3.28, Olives 1.53,
                                           Bitter Vetch 2.19,
                                           Barley 32.83)
  Limit Dairy / supplementary feeding   : not consumed by the IncludeDairy
                                          aggregate formula

  Note: the thesis figure also lists a separate "Animal Crop Selection"
  (Horse Bean / Emmer / Peas / Bitter Vetch) for fodder/grain feeding;
  IncludeDairy mode does not act on the per-animal fodder map, so this
  is informational only for this test.

Thesis outputs (the values to match)
------------------------------------
  Aggregate diet split (overall %):
    Domestic Meat (tame meat)           :  9 %
    Wild Meat                           :  1 %
    Dairy                               :  0 %
    Crops (domestic plants)             : 81 %
    Wild Plants                         :  9 %
  Settlement totals:
    MCals per person per year           :    912.5
    City MCals per year                 : 91,250

How this script works
---------------------
* Builds a `SimpleNamespace` that quacks like an LaModel, populated with
  the live animal/crop selections from `~/.landuseAnalyst/`. (Same idiom
  as `scratch/parity_test.py` and `scratch/compare_includedairy_formulas.py`.)
* Calls the production `doCalcsAnimalsFirstIncludeDairy`.
* Prints THESIS EXPECTED vs PRODUCTION ACTUAL side by side.
* Reports PASS only if every metric is within tolerance.

This is a draft. Do not run automatically — review first.
"""

import os
import sys

# QGIS Python bindings + project root on path
sys.path.insert(0, '/usr/share/qgis/python')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qgis.PyQt.QtCore import QCoreApplication
_app = QCoreApplication([])

from la.lib.lautils import LaUtils
LaUtils.debug.setEnabled(False)
from la.lib.lacalculations import doCalcsAnimalsFirstIncludeDairy

from types import SimpleNamespace
import xml.etree.ElementTree as ET


HOME = os.path.expanduser('~/.landuseAnalyst')


# -------------------------------------------------------------------------
# Helpers — discover the animal/crop guid <-> parameter guid mappings
# -------------------------------------------------------------------------
def _read_text(el, tag):
    t = el.findtext(tag, '') or ''
    return t.strip()


def load_param_map(subdir, parent_tag):
    """Return {parent_guid: param_guid} for every .xml in the given dir.

    parent_tag is the tag inside the parameter file that names the
    associated animal/crop guid (e.g. 'animal' or 'crop').
    """
    out = {}
    folder = os.path.join(HOME, subdir)
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith('.xml'):
            continue
        tree = ET.parse(os.path.join(folder, fname))
        root = tree.getroot()
        param_guid  = root.get('guid', fname.replace('.xml', ''))
        parent_guid = _read_text(root, parent_tag)
        if parent_guid:
            out[parent_guid] = param_guid
    return out


def load_name_to_guid(subdir):
    """Return {profile_name: guid} for animal or crop profiles."""
    out = {}
    folder = os.path.join(HOME, subdir)
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith('.xml'):
            continue
        tree = ET.parse(os.path.join(folder, fname))
        root = tree.getroot()
        name = _read_text(root, 'name')
        guid = root.get('guid', fname.replace('.xml', ''))
        if name:
            out[name] = guid
    return out


# -------------------------------------------------------------------------
# Thesis Scenario 1 inputs
# -------------------------------------------------------------------------
SCENARIO_NAME = "Scenario 1 (Chalcolithic, Min Pop 100, Meat 10%, Dairy 0%, Foddered)"

THESIS_ANIMALS = ['Sheep', 'Pig', 'Cow', 'Goat']
THESIS_CROPS   = ['Horse Bean', 'Einkorn', 'Emmer', 'Lentils',
                  'Peas', 'Olives', 'Bitter Vetch', 'Barley']

# Expected thesis outputs (overall diet percentages and settlement totals)
EXPECTED = {
    'tameMeatPortionPct':       9.00,
    'wildAnimalPortionPct':     1.00,
    'dairyPortionPct':          0.00,
    'cropsPortionPct':         81.00,
    'wildPlantsPortionPct':     9.00,
    'kiloCaloriesIndividualAnnual': 912_500.0,   # = 2500 * 365  (kcal)
    'megaCaloriesSettlementAnnual':  91_250.0,   # = 912500 * 100 / 1000  (MCal)
}

# Tolerances — thesis values are reported to whole percent, so allow 0.5%
# slack on percentage rows; settlement Mcal totals must be exact.
TOL_PCT  = 0.5
TOL_ABS  = 1e-3


# -------------------------------------------------------------------------
# Build the model
# -------------------------------------------------------------------------
def build_model():
    animal_name_to_guid = load_name_to_guid('animalProfiles')
    crop_name_to_guid   = load_name_to_guid('cropProfiles')
    animal_param_map    = load_param_map('animalParameterProfiles', 'animal')
    crop_param_map      = load_param_map('cropParameterProfiles',   'crop')

    # Selected animal/crop maps: {parent_guid: param_guid}
    selected_animals = {}
    for nm in THESIS_ANIMALS:
        g = animal_name_to_guid.get(nm)
        if not g:
            print(f"  [WARN] thesis animal '{nm}' not in live data — skipping")
            continue
        p = animal_param_map.get(g)
        if not p:
            print(f"  [WARN] no parameter file for animal '{nm}' (guid={g})")
            continue
        selected_animals[g] = p

    selected_crops = {}
    for nm in THESIS_CROPS:
        g = crop_name_to_guid.get(nm)
        if not g:
            print(f"  [WARN] thesis crop '{nm}' not in live data — skipping")
            continue
        p = crop_param_map.get(g)
        if not p:
            print(f"  [WARN] no parameter file for crop '{nm}' (guid={g})")
            continue
        selected_crops[g] = p

    model = SimpleNamespace(
        mPopulation=100,
        mCaloriesPerPersonDaily=2500.0,
        mDietPercent=10.0,         # 10% animal
        mMeatPercent=90.0,         # 90% tame meat (=> 10% wild)
        mDairyUtilisation=0.0,     # NO dairy in Scenario 1
        mPercentOfDietThatIsFromCrops=90.0,
        mLimitDairy=False,
        mLimitDairyPercentage=100.0,
        mAnimalsMap=selected_animals,
        mCropsMap=selected_crops,
        # Production function reads/writes these and uses LaUtils for the
        # rest of the data; placeholders below keep attribute lookups safe.
        mDietLabels=None,
        mCalcsCropsMap={},
        mCalcsAnimalsMap={},
        mValueMap={},
        mAnimalCalcReport={},
        mAreaTargetsCropsMap={},
        mCommonGrazingValue=1.0,   # not consumed by IncludeDairy aggregate
    )
    return model, selected_animals, selected_crops


# -------------------------------------------------------------------------
# Run + compare
# -------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"  Thesis Scenario Verification — {SCENARIO_NAME}")
    print(f"  Mode: doCalcsAnimalsFirstIncludeDairy (Animals First, Include Dairy)")
    print(f"  Data: {HOME}")
    print("=" * 78)

    model, animals, crops = build_model()
    print(f"\n  Animals selected: {len(animals)} (expected {len(THESIS_ANIMALS)})")
    print(f"  Crops selected:   {len(crops)} (expected {len(THESIS_CROPS)})")

    dl = doCalcsAnimalsFirstIncludeDairy(model)

    actual = {
        'tameMeatPortionPct':       dl.tameMeatPortionPct,
        'wildAnimalPortionPct':     dl.wildAnimalPortionPct,
        'dairyPortionPct':          dl.dairyPortionPct,
        'cropsPortionPct':          dl.cropsPortionPct,
        'wildPlantsPortionPct':     dl.wildPlantsPortionPct,
        'kiloCaloriesIndividualAnnual': dl.kiloCaloriesIndividualAnnual,
        'megaCaloriesSettlementAnnual': dl.megaCaloriesSettlementAnnual,
    }

    # Display
    W = 32
    print()
    print(f"  {'Metric':<{W}} {'Thesis (expected)':>20} {'Plugin (actual)':>20} {'Δ':>10} {'OK':>4}")
    print(f"  {'-'*W} {'-'*20} {'-'*20} {'-'*10} {'-'*4}")
    all_ok = True
    for k in EXPECTED:
        exp = EXPECTED[k]
        act = actual[k]
        if k.endswith('Pct'):
            tol = TOL_PCT
        else:
            # Mcal/Kcal totals must be exact (these are derived from the
            # raw inputs, not the thesis figure read-out)
            tol = max(TOL_ABS, abs(exp) * 1e-9)
        diff = act - exp
        ok = abs(diff) <= tol
        mark = 'PASS' if ok else 'FAIL'
        if not ok:
            all_ok = False
        print(f"  {k:<{W}} {exp:>20,.4f} {act:>20,.4f} {diff:>10,.4f} {mark:>4}")

    print()
    print("=" * 78)
    print(f"  Result: {'PASS — plugin matches thesis Scenario 1' if all_ok else 'FAIL — see rows marked FAIL above'}")
    print("=" * 78)

    # Also expose the per-crop area targets if the production code populated
    # them — useful for cross-checking the 158 ha cropland figure on
    # Fig 5.13. (Note: 158 ha includes fallow land, while the IncludeDairy
    # Python enhancement reports core crop area only.)
    if getattr(dl, 'cropAreaTargetsMap', None):
        print("\n  Per-crop area target (ha) — informational, no thesis row to match exactly:")
        total = 0.0
        for guid, ha in dl.cropAreaTargetsMap.items():
            print(f"    {guid[:8]}...: {ha:>10,.2f} ha")
            total += ha
        print(f"    {'TOTAL':<11}: {total:>10,.2f} ha   (thesis Fig 5.13 reports 158 ha including fallow)")

    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
