# Landuse Analyst QGIS Plugin

[![tests](https://github.com/arkygeek/landuseanalyst/actions/workflows/test.yml/badge.svg)](https://github.com/arkygeek/landuseanalyst/actions/workflows/test.yml)

Landuse Analyst models the agricultural catchment of an archaeological
settlement. A diet/herd model turns population, diet composition and
crop/animal profiles into land-area targets; a walking-time (Tobler) cost
surface and a binary-search threshold sweep then locate that land around the
site on a DEM, honouring per-item suitability rasters and slope limits.

It is the QGIS port of the C++ Landuse Analyst written for Jorgenson (2010,
University of Liverpool) and shares its engine and golden numbers with the web
version at <https://la.arkygeek.com>
([landuseanalyst-web](https://github.com/arkygeek/landuseanalyst-web)).

## What you get

- **Dockable workspace** — a settings dock (scenario, population & diet with a
  live donut, crops/animals with parameter sets, optional catchment search,
  advanced) and a results dock (stat tiles, charts, tables, help, JSON/PDF
  export). QGIS stays usable while the plugin is open.
- **Catchment analysis** on the map: pick the DEM and suitability rasters from
  the project, click the settlement on the canvas, press Calculate. Result
  masks arrive as styled layers in *Catchment Analysis → ⟨scenario⟩ →
  Crops / Animals*, with the settlement marker and the walking-cost surface.
- **Per-item preferred land**: each crop / animal parameter set carries a
  slope band (thesis defaults 9° crops, 15° grazing) edited in the parameter
  dialogs.
- **Thesis parity** pinned by tests (Shuna Chalcolithic S01: 91,250 MCal/yr,
  191.91 Ha cropland, 82.36 Ha grazing; Shuna catchment 1328.125 s /
  49.14 Ha).

## Requirements

- QGIS ≥ 3.28 (developed and tested on 3.42).
- Everything the diet model needs ships with QGIS.
- Catchment analysis needs **scipy** in the QGIS Python, or the GRASS
  Processing provider as a fallback. The plugin warns and offers a one-click
  install when scipy is missing; manual instructions are in
  [requirements.txt](requirements.txt).

## Installation

1. Clone into your QGIS plugin directory (or clone anywhere and symlink `la/`):

    ```bash
    git clone https://github.com/arkygeek/landuseanalyst.git
    ln -s "$PWD/landuseanalyst/la" ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/la
    ```

    Plugin directories: Linux
    `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`, Windows
    `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`, macOS
    `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`.

2. Install the sample profiles (see below), enable *Landuse Analyst* in the
   Plugin Manager, and click the toolbar icon.

Resources are pre-compiled (`la/resources_rc.py`); rebuild only after editing
`la/resources.qrc`:

```bash
pyrcc5 -o la/resources_rc.py la/resources.qrc
```

## Walkthrough

[WALKTHROUGH.md](WALKTHROUGH.md) runs the bundled Shuna data end to end with
the numbers you should see.

## Development

```bash
# tests (needs the QGIS Python; the engine tests need only numpy + GDAL)
QT_QPA_PLATFORM=offscreen python -m pytest -q la/test
ruff check la
```

Coding standards and naming conventions live in
[la/CODING_STANDARDS.md](la/CODING_STANDARDS.md) and
[la/NAMING_CONVENTIONS.md](la/NAMING_CONVENTIONS.md). Please branch from
`main` for pull requests. The original C++ (`cppArchive/`) is the reference
for engine behaviour.

## Citation

See [CITATION.cff](CITATION.cff).

### Sample Data Setup (Required — animals and crops will be empty without this)

The plugin reads animal and crop profiles from `~/.landuseAnalyst/` on your
operating system. This directory is **not** created automatically — you must
populate it before the plugin will show any data.

Sample data is bundled in the `testData/` directory of this repository.
Run the install script once after cloning:

```bash
./install_sample_data.sh
```

This copies the following into `~/.landuseAnalyst/`:

| Source in repo                      | Installed to                                    | Contents                        |
|-------------------------------------|-------------------------------------------------|---------------------------------|
| `testData/animalProfiles/`          | `~/.landuseAnalyst/animalProfiles/`             | One `.xml` file per animal      |
| `testData/cropProfiles/`            | `~/.landuseAnalyst/cropProfiles/`               | One `.xml` file per crop        |
| `testData/animalParameterProfiles/` | `~/.landuseAnalyst/animalParameterProfiles/`    | One `.xml` file per animal set  |
| `testData/cropParameterProfiles/`   | `~/.landuseAnalyst/cropParameterProfiles/`      | One `.xml` file per crop set    |
| `testData/images/`                  | `~/.landuseAnalyst/images/`                     | Thumbnails shown in the UI      |

The script skips files that already exist (safe to re-run). Use `--force` to
overwrite everything with the bundled defaults.

To add your own animals or crops, drop additional `.xml` files into the
appropriate subdirectory under `~/.landuseAnalyst/` — the app picks them up
automatically on next launch.

### Running the Plugin

1. **Launch QGIS:**
    Open QGIS and navigate to the Plugins menu.

2. **Enable the Plugin:**
    Go to `Manage and Install Plugins`, find `Landuse Analyst`, and enable it.

3. **Using the Plugin:**
    Access the plugin from the QGIS toolbar or the Plugins menu.

## Coding and Naming Conventions

To maintain consistency and readability, all contributions must adhere to the following conventions:

### Coding Standards

Refer to [CODING_STANDARDS.md](./la/CODING_STANDARDS.md) for detailed guidelines on:
- Class and method naming
- Member variable conventions
- Type hints
- Signal/slot naming conventions
- Exception and error handling

### Naming Conventions

Refer to [NAMING_CONVENTIONS.md](./la/NAMING_CONVENTIONS.md) for detailed guidelines on:
- Class names
- Method and function names
- Variable names (including the use of `the`, `my`, and `m` prefixes)
- PyQt property naming
- Handling custom classes with PyQt properties

## Cross-Platform Compatibility

This plugin is designed to work across multiple platforms, including Linux, Windows, and macOS. Ensure that any platform-specific code is appropriately guarded and tested on all supported platforms.

## Additional Resources

For more detailed information on the project, including design decisions and implementation details, refer to the following documents:
- [Thesis available here](https://www.researchgate.net/publication/311589270_The_Impact_of_South_Levantine_Early_Bronze_Age_Communities_On_Their_Landscapes)
- [Class Documentation](https://arkygeek.github.io/landuseanalyst)

## Acknowledgments

This plugin's GIS catchment analysis ports the workflow of the original
C++ Landuse Analyst into Python + QGIS Processing. Several pieces of
upstream work are essential to it:

### GRASS r.walk

The reference cost-distance algorithm for the **Walking Time** distance
method is GRASS `r.walk`. When the QGIS Processing GRASS provider on a
user's system has `r.walk` registered, the plugin invokes it directly
via `processing.run("grass:r.walk", …)`. When `r.walk` isn't registered
(a common situation across QGIS bundles, even with GRASS itself
installed), the plugin falls back to a pure-Python implementation in
`la.lib.lagrass.LaGrass._makeWalkCostPure` that uses **Tobler's hiking
function** + scipy's Dijkstra to produce a co-registered cost surface.

The reference GRASS implementation was originally written by **Steno
Fontanari** (ITC-IRST, 1992) and **Pierre de Mouveaux**, and is
maintained by the GRASS GIS development team — Markus Neteler, Hamish
Bowman, Roberto Flor and many others.

GRASS r.walk source:
[OSGeo/grass — raster/r.walk](https://github.com/OSGeo/grass/tree/main/raster/r.walk)

### Tobler's hiking function

The pure-Python fallback uses Waldo Tobler's hiking function, a
canonical model for anisotropic walking-velocity over terrain:

> Tobler, W. (1993). *Three Presentations on Geographical Analysis and
> Modeling: Non-Isotropic Geographic Modeling; Speculations on the
> Geometry of Geography; and Global Spatial Analysis.* National Center
> for Geographic Information and Analysis, Technical Report 93-1.

### Other GRASS algorithms

The catchment workflow also uses `grass:r.cost` (for the Euclidean
distance method) and `grass:r.mapcalc.simple` (for raster reclassing,
masking, and merging). Same upstream credit to the GRASS GIS
development team.

## Contact

For any questions or contributions, please contact Jason Jorgenson at [jjorgenson a@t gmail.com].

---

By following these guidelines and utilizing the provided resources, you can contribute effectively to the Landuse Analyst QGIS Plugin project. Thank you for your collaboration and commitment to maintaining high standards in our codebase.
