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

Refer to [CODING_STANDARDS.md](./CODING_STANDARDS.md) for detailed guidelines on:
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

## Contact

For any questions or contributions, please contact Jason Jorgenson at [jjorgenson a@t gmail.com].

---

By following these guidelines and utilizing the provided resources, you can contribute effectively to the Landuse Analyst QGIS Plugin project. Thank you for your collaboration and commitment to maintaining high standards in our codebase.
