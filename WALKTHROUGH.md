# Walkthrough: the Shuna thesis scenario, end to end

This reproduces the Chalcolithic scenarios for Tell esh-Shuna North from
Jorgenson (2010) with the data bundled in this repository, and tells you the
numbers you should see at each step. It takes about ten minutes.

## 1. Install the plugin and the sample data

```bash
git clone https://github.com/arkygeek/landuseanalyst.git
cd landuseanalyst
./install_sample_data.sh          # profiles + thesis parameter sets → ~/.landuseAnalyst/
ln -s "$PWD/la" ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/la
```

Start QGIS (3.28 or newer), enable *Landuse Analyst* in the Plugin Manager and
click its toolbar button. Two docks open: **Landuse Analyst** (left) and
**LA Results** (right). If a yellow bar says scipy is missing, press *Install
scipy* (or see `requirements.txt`) and restart QGIS. The diet steps below work
without scipy; the catchment step needs it.

## 2. Diet and land requirement (no GIS data needed)

1. In the settings dock press **Open…** and choose
   `la/scenarios/thesis/shuna_chalcolithic_s01.lascenario.json`
   (population 100, 10 % of calories from animals, 99 % of meat from herds,
   90 % of plants from crops, no dairy, 90-day supplementary feed).
2. The donut fills as soon as the file loads. In the results dock you should read:

   | Tile | Value |
   |---|---|
   | Settlement energy | 91,250 MCal/yr |
   | Cropland | 191.9 Ha |
   | Grazing land | 82.4 Ha |
   | Total land needed | 274.3 Ha |
   | Domestic crops | 73,913 MCal (81.0 % of the diet) |

3. Press **Calculate**. The *Tables* tab lists the per-crop and per-animal
   targets (Emmer 77.6 Ha, Barley 82.3 Ha, Goat 29.4 Ha, Cow 27.3 Ha …) and
   the *Charts* tab renders the herd and land charts. **PDF…** and **Save
   JSON…** export the same report.
4. Open `shuna_chalcolithic_s05.lascenario.json` (dairy 100 %). Tick *Dairy
   counts toward the meat share* in *Population & diet* to switch to the
   Animals-First-Include-Dairy method and press **Calculate**: the animal
   area targets become Sheep 0.216 Ha, Goat 0.720 Ha, Cow 2.879 Ha, Pig
   2.207 Ha. (Before version 1.0 these were 1000× too small — that is the bug
   fixed in this release.)

Drag any slider: the donut, the tiles and the *Calculate* readiness update
live. Shares that do not total 100 % are called out in red under *Agriculture*.

## 3. Catchment on the map

1. Add the DEM `la/test/xmlData/GrassData/demShuna` to the project (it is a
   GRASS ASCII grid in EPSG:32636, 30 m cells).
2. Make a suitability raster: *Raster ▸ Raster Calculator*,
   expression `("demShuna@1" >= -100) AND ("demShuna@1" <= 100)`, output
   `lowground.tif`. This "low ground" band is the suitability the golden
   numbers were established with.
3. In the settings dock tick **Catchment search**, choose the DEM, and set
   *Common crop land* and *Common grazing* to `lowground`. Leave *Apply each
   item's preferred slope band* on (crops 9°, grazing 15°) or untick it to reproduce
   the pre-1.0 numbers. Type the seed
   easting **744800**, northing **3611100** (or press *Pick on map* and click
   the site). Distance: *Walking time (Tobler)*.
4. Press **Calculate**. Progress shows in the footer; after a few seconds the
   layer tree gains *Catchment Analysis ▸ ⟨scenario⟩* with a red *Settlement*
   point, *Crops* and *Animals* groups holding the converged masks, and the
   semi-transparent *Cost surface*.

### Rivers and lakes as barriers

Press **Digitise…** next to *Barriers* to get a scratch line layer with
`barrier_type` and `crossing_penalty` fields, draw the Jordan along the valley
floor (or pick an existing river / lake layer in the combo), and Calculate
again. Lines cost a 30-minute ford unless you set `crossing_penalty` (minutes;
negative = impassable); polygons are impassable. The results heading reports
how many features touched the working window — if it says none did, the
layer's CRS or extent is wrong and water has not been modelled.

To check the engine against its golden number run the bundled test instead:

```bash
QT_QPA_PLATFORM=offscreen python la/test/test_lacatchment_shuna.py
# → threshold: 1328.1 s walking time · achieved Ha: 49.140 (target 50.0)
```

(a single 50 Ha crop on the low-ground suitability, 200 × 200-cell window).

## 4. Save your own scenario

Change anything, press **Save as…**, and reopen it later from **Recent**. The
file is JSON whose `scenario` block uses the same field names as the web
version at <https://la.arkygeek.com>, so it can be posted to that API as is.

## 5. Run the test-suite

```bash
QT_QPA_PLATFORM=offscreen python -m pytest -q la/test   # QGIS Python
```

Expect every test to pass; the golden numbers above are asserted in
`la/test/model/test_thesis_golden.py` and `la/test/gui/test_catchment_task_offscreen.py`.
