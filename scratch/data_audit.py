#!/usr/bin/env python3
"""
data_audit.py - Input Data Equivalence Audit
=============================================
Compares:
  1. The old C++ test profile data (cppArchive/test_data/) -- the original app data
  2. The live plugin data (~/.landuseAnalyst/)              -- new formatted data
  3. The Animals.xml master file (la/Animals.xml)           -- reference definitions

For fields present in the old C++ profiles, checks if the live data
matches. For NEW fields (milk, fleece, lactationTime, etc.) that were
missing from old profiles, reports them as additions to review.

The C++ default constructor shows NO defaults for milkGramsPerDay, 
milkFoodValue, lactationTime -- so old code ran with value=0 for these.

Run from the project root:
  python3 scratch/data_audit.py
"""

import os
import xml.etree.ElementTree as ET

PROJECT_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CPP_TEST_DIR   = os.path.join(PROJECT_ROOT, 'cppArchive', 'test_data')
LIVE_DATA      = os.path.expanduser('~/.landuseAnalyst')
ANIMALS_XML    = os.path.join(PROJECT_ROOT, 'la', 'Animals.xml')

def _f(el, tag, default='0'):
    return el.findtext(tag, default) or default

def load_xml_profile(path):
    """Load any XML profile as a flat dict of tag->text."""
    try:
        tree = ET.parse(path)
        r = tree.getroot()
        return {child.tag: child.text for child in r}
    except Exception as e:
        return {'_error': str(e)}

def load_all_from_dir(directory, root_tag=None):
    """Load all XML files in a directory, return {guid: {tag: value}}."""
    result = {}
    if not os.path.isdir(directory):
        return result
    for fname in sorted(os.listdir(directory)):
        if not fname.endswith('.xml'):
            continue
        path = os.path.join(directory, fname)
        data = load_xml_profile(path)
        # Try to find the guid from the root element attribute
        try:
            tree = ET.parse(path)
            r = tree.getroot()
            guid = r.get('guid', fname.replace('.xml', ''))
            name = r.findtext('name', '?')
            data['_guid'] = guid
            data['_name'] = name
            result[guid] = data
        except Exception:
            pass
    return result

def colour(text, ok):
    GREEN = '\033[92m'
    RED   = '\033[91m'
    YELLOW= '\033[93m'
    RESET = '\033[0m'
    if ok is True:
        return f"{GREEN}{text}{RESET}"
    elif ok is False:
        return f"{RED}{text}{RESET}"
    else:
        return f"{YELLOW}{text}{RESET}"

def audit_animals():
    print("\n" + "="*70)
    print("  ANIMAL DATA AUDIT")
    print("  Comparing: cppArchive test data vs live plugin data")
    print("="*70)

    cpp_animals  = load_all_from_dir(os.path.join(CPP_TEST_DIR, 'animalProfiles'))
    live_animals = load_all_from_dir(os.path.join(LIVE_DATA, 'animalProfiles'))

    # Fields the C++ constructor DID NOT initialize (so old code used 0 or garbage)
    NEW_FIELDS = {'milk', 'milkGramsPerDay', 'milkFoodValue', 'fleece',
                  'fleeceWeightKg', 'lactationTime', 'adultWeight',
                  'conceptionEfficiency', 'femalesToMales', 'maintenance',
                  'weaningWeight', 'feedEnergyType'}

    # Fields that exist in old C++ profiles
    OLD_FIELDS = {'meatFoodValue', 'usableMeat', 'killWeight', 'growTime',
                  'deathRate', 'gestating', 'lactating', 'juvenile',
                  'sexualMaturity', 'breedingExpectancy', 'youngPerBirth',
                  'weaningAge', 'gestationTime', 'estrousCycle'}

    print(f"\n  Old C++ profiles found: {len(cpp_animals)}")
    print(f"  Live profiles found:    {len(live_animals)}")

    # Match by name since GUIDs differ between old and new
    cpp_by_name  = {d.get('name','?'): d for d in cpp_animals.values()}
    live_by_name = {d.get('name','?'): d for d in live_animals.values()}

    all_names = sorted(set(list(cpp_by_name.keys()) + list(live_by_name.keys())))
    issues = []

    for name in all_names:
        cpp  = cpp_by_name.get(name)
        live = live_by_name.get(name)

        print(f"\n  {'─'*66}")
        print(f"  Animal: {name}")
        print(f"  {'─'*66}")

        if cpp is None:
            print(f"  {colour('[NEW]', None)} Only in live data (not in cppArchive test profiles)")
            continue
        if live is None:
            print(f"  {colour('[MISSING]', False)} In cppArchive but NOT in live data!")
            issues.append(f"{name}: missing from live data")
            continue

        print(f"  {'Field':<28} {'C++ test':>12} {'Live':>12} {'Status':>10}")
        print(f"  {'-'*28} {'-'*12} {'-'*12} {'-'*10}")

        # Compare fields present in both
        for field in sorted(OLD_FIELDS):
            cpp_val  = cpp.get(field,  '—')
            live_val = live.get(field, '—')
            if cpp_val == '—' and live_val == '—':
                continue
            match = cpp_val == live_val
            status = colour('MATCH', True) if match else colour('DIFFER', False)
            print(f"  {field:<28} {str(cpp_val):>12} {str(live_val):>12} {status:>10}")
            if not match:
                issues.append(f"{name}.{field}: C++ had '{cpp_val}', live has '{live_val}'")

        # Report new fields (not in old C++ profiles — these were added/discovered)
        print(f"\n  {'─ New fields (not in old C++ profiles, C++ used 0 as default) ─':>66}")
        for field in sorted(NEW_FIELDS):
            live_val = live.get(field, '—')
            if live_val == '—':
                print(f"  {field:<28} {'(missing)':>12} {'(missing)':>12} {colour('CHECK', None):>10}")
                issues.append(f"{name}.{field}: missing from live data!")
            else:
                print(f"  {field:<28} {'0 (default)':>12} {str(live_val):>12} {colour('ADDED', None):>10}")

    return issues

def audit_animal_params():
    print("\n\n" + "="*70)
    print("  ANIMAL PARAMETER DATA AUDIT")
    print("="*70)

    cpp_params  = load_all_from_dir(os.path.join(CPP_TEST_DIR, 'animalParameterProfiles'))
    live_params = load_all_from_dir(os.path.join(LIVE_DATA, 'animalParameterProfiles'))

    cpp_by_name  = {d.get('name','?'): d for d in cpp_params.values()}
    live_by_name = {d.get('name','?'): d for d in live_params.values()}

    print(f"\n  Old C++ param profiles found: {len(cpp_params)}")
    print(f"  Live param profiles found:    {len(live_params)}")

    # Key field for calculations
    KEY_FIELDS = {'percentTameMeat', 'useCommonGrazingLand', 'useSpecificGrazingLand',
                  'fallowUsage', 'fodderUse'}

    issues = []
    for name in sorted(set(list(cpp_by_name.keys()) + list(live_by_name.keys()))):
        cpp  = cpp_by_name.get(name)
        live = live_by_name.get(name)

        print(f"\n  Animal Param: {name}")
        if cpp is None:
            print(f"  {colour('[NEW]', None)} Only in live data")
            continue
        if live is None:
            print(f"  {colour('[MISSING]', False)} Only in C++ archive")
            continue

        print(f"  {'Field':<30} {'C++ test':>14} {'Live':>14} {'Status':>10}")
        print(f"  {'-'*30} {'-'*14} {'-'*14} {'-'*10}")
        for field in sorted(KEY_FIELDS):
            cv = cpp.get(field, '—')
            lv = live.get(field, '—')
            match = cv == lv
            status = colour('MATCH', True) if match else colour('DIFFER', False)
            print(f"  {field:<30} {str(cv):>14} {str(lv):>14} {status:>10}")
            if not match and cv != '—' and lv != '—':
                issues.append(f"Param {name}.{field}: C++ '{cv}' vs live '{lv}'")

    return issues

def main():
    print("\nLanduse Analyst — Input Data Equivalence Audit")
    print("Checking that live plugin data is consistent with C++ test data")

    issues_a = audit_animals()
    issues_p = audit_animal_params()
    all_issues = issues_a + issues_p

    print("\n\n" + "="*70)
    if all_issues:
        print(f"  ISSUES FOUND ({len(all_issues)}):")
        for i in all_issues:
            print(f"  • {i}")
    else:
        print("  No critical data mismatches found.")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
