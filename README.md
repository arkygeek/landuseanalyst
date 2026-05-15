# Landuse Analyst QGIS Plugin

## Overview

Landuse Analyst is a comprehensive QGIS plugin designed to facilitate land use analysis and management. This project is a port of the original C++ codebase to Python, leveraging the PyQt framework for seamless integration with QGIS.

## Collaboration Guidelines

Please submit all pull requests from the Developer Branch. Ensure that your code adheres to the coding standards and naming conventions outlined in the [CODING_STANDARDS.md](./la/CODING_STANDARDS.md) and [NAMING_CONVENTIONS.md](./la/NAMING_CONVENTIONS.md) files.

## Project Authors

Jason Jorgenson

## Build and Installation Instructions

### Prerequisites

Ensure you have the following installed:
- QGIS (latest version)
- Python 3.12 or later
- PyQt5
- Other dependencies as listed in `requirements.txt`

### Building the Plugin

To build the plugin, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/landuseanalyst.git
    cd landuseanalyst
    ```

2. **Set Up the Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Compile Resources:**
    ```bash
    pyrcc5 -o resources_rc.py resources.qrc
    ```

4. **Install the Plugin:**
    Copy the `landuseanalyst` directory to your QGIS plugins directory. The location of this directory varies by operating system:
    - **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
    - **Windows:** `C:\Users\<YourUsername>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
    - **macOS:** `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`

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
