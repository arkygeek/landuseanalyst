# Thesis verification scenario — "Min Pop" / Chalcolithic / Shuna

CSV dump of the user's authoritative macOS Numbers spreadsheet for the
**Minimum Population, Chalcolithic** scenario from his PhD thesis. Every
worked-example figure in the thesis was produced by this spreadsheet (or
a sibling); the maps in the thesis were produced by Landuse Analyst.

## Scenario inputs

| Field | Value |
|---|---|
| Settlement | Shuna (Chalcolithic) |
| Maximum Population | 100 |
| MCals/person/day | 2.500 |
| **ALL Meat %** | **10%** (input — "meat portion of diet") |
| **Domestic Animal Contribution** | **99%** (tame meat fraction; wild = 1%) |
| **Crop Contribution** | **90%** (domestic-crop fraction of plants) |
| **Dairy Utilisation** | **50%** |
| Dairy Limit | FALSE (cap = 100%) |
| Supplemental feed | 90 days |

Animals selected (`percentTameMeat` sums to 100%):

| Animal | % |
|---|---|
| Sheep | 3.59 |
| Pig | 36.65 |
| Cow | 47.81 |
| Goat | 11.95 |

Crops selected (`percentTameCrop` sums to 100%) — **8 crops, including Bitter Vetch**:

| Crop | % |
|---|---|
| Horse Bean | 1.09 |
| Einkorn | 5.47 |
| Emmer | 52.52 |
| Lentils | 1.09 |
| Peas | 3.28 |
| Olives | 1.53 |
| Bitter Vetch | 2.19 |
| Barley | 32.83 |

Crops *not* selected: Grapes, Grass Peas, FreeHull Barley.

## Authoritative expected outputs

Settlement-annual totals (file `11_diet_calculations.csv`):

| Category | MCals | % of diet |
|---|---|---|
| Domestic Meat | 9,033.750 | 9.90% |
| Wild Meat | 91.250 | 0.10% |
| Dairy | 4,338.044 | 4.75% |
| Crops | 70,008.261 | 76.72% |
| Wild Plants | 7,778.696 | 8.52% |
| **Total** | **91,250** | 99.99% |

MCals/person/year = 912.5
Total cropland area = 184 Ha; total grazing area (incl. fallow) = 84 Ha
(see `07_calculations_summary.csv` for the human/animal split).

Per-animal targets in `05_animal_targets.csv`; per-crop targets in
`10_crop_targets.csv`; per-animal calculation intermediates in
`06_calculations.csv`.

## Notes for plugin verification

1. The thesis scenario uses **Bitter Vetch**, which we moved to
   `testData/cropProfiles/_extras/` in commit 4a2fdf8. To run this
   scenario through the plugin, Bitter Vetch needs to be back in
   `testData/cropProfiles/` (or the install script needs to pick it up
   from `_extras/`). See `scratch/verify_thesis_scenario.py` for the
   loader pattern.

2. Spreadsheet column labels and units don't always match the XML:
   - "Milk grams day-1" actually holds kg/day (0.94 for Sheep ≈ 1 kg/day).
     Our XML uses grams/day directly (`<milkGramsPerDay>940</milkGramsPerDay>`)
     and the code does `* 0.001` internally to convert.
   - Spreadsheet "Gestation Req'd 3.97" means **MCal/day**; the XML stores
     it as kcal/day (`3970`) and the code does `* 0.001` to convert.

3. The output category convention:
   - `Meat % (10%) + Dairy % (4.75%) + Plants % (85.25%) = 100%` (full partition)
   - Animal sector total = 14.75% (meat + dairy)
   - In the plugin code, `mDietPercent` corresponds to the spreadsheet's
     "ALL Meat %" (so 10 here), and dairy is computed on top of that as a
     byproduct of the meat herd.

4. The mode this represents is `doCalcsAnimalsFirstIncludeDairy`
   (offspring-derived dairy formula — thesis-canonical per the earlier
   agent research).
