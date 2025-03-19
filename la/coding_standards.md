# Landuse Analyst QGIS Plugin Coding Standards

This document outlines the coding standards and naming conventions used in the PyQt port of the Landuse Analyst application.

## Class Naming Conventions

1. **Class Names**: Use PascalCase with the "La" prefix to maintain compatibility with the original C++ codebase.
   - Examples: `LaCrop`, `LaCropManager`, `LaCropParameterManager`

2. **Base Classes**: UI-related base classes that are generated from Qt Designer files should maintain the "Base" suffix.
   - Examples: `LaCropManagerBase`, `LaCropParameterManagerBase`

## Variable Naming Conventions

1. **Member Variables**: Use snake_case with a single underscore prefix for private member variables.
   - Examples: `_name`, `_description`, `_crop_yield`
   
2. **Properties**: Member variables should be exposed through Python properties (getters/setters). Properties should use camelCase without prefixes.
   - Examples: `name`, `description`, `cropYield`

3. **Constants**: Use UPPER_CASE with underscores for constants.
   - Examples: `MAX_CROP_YIELD`, `DEFAULT_CALORIES`

4. **Enumerations**: Enumerations should be implemented as Python Enum classes and use PascalCase for the enum name and UPPER_CASE for enum values.
   - Example: `AreaUnits.DUNUM`, `AreaUnits.HECTARE`

## Method Naming Conventions

1. **Public Methods**: Use camelCase for public methods to maintain compatibility with the original C++ codebase.
   - Examples: `refreshCropTable()`, `selectCrop()`, `showCrop()`

2. **Private Methods**: Use snake_case with a single underscore prefix for private methods.
   - Examples: `_load_settings()`, `_update_ui()`

3. **Event Handlers**: Use the "on_[widget]_[event]" naming pattern for event handlers.
   - Examples: `on_pbnApply_clicked()`, `on_toolNew_clicked()`

## UI Element Naming Conventions

Maintain the naming conventions from the original C++ codebase for UI element variables:

1. **Push Buttons**: Use "pbn" prefix.
   - Examples: `pbnApply`, `pbnClose`, `pbnCropPic`

2. **Line Edits**: Use "le" prefix.
   - Examples: `leName`, `leDescription`

3. **Spin Boxes**: Use "sb" prefix.
   - Examples: `sbCropYield`, `sbCropCalories`

4. **Combo Boxes**: Use "cb" prefix or "cbo" prefix.
   - Examples: `cbAreaUnits`, `cbFodderEnergyType` or `cboAreaUnits`

5. **Labels**: Use "lbl" prefix or "label" prefix.
   - Examples: `lblCropPix`, `labelPlantDescription`

6. **Tables**: Use "tbl" prefix.
   - Examples: `tblCrops`

7. **Group Boxes**: Use "grp" prefix.
   - Examples: `grpProfiles`

8. **Tool Buttons**: Use "tool" prefix.
   - Examples: `toolNew`, `toolCopy`, `toolDelete`

## File Organization

1. **Python Modules**: Organize code in a modular structure with these primary directories:
   - `la/`: Root package
   - `la/lib/`: Core business logic classes
   - `la/gui/`: UI-related code
   - `la/ui/`: Generated UI files 
   - `la/resources/`: Resources like images, icons, etc.

2. **File Naming**: Use lowercase with underscores for Python module files.
   - Examples: `lacrop.py`, `lacrop_manager.py`

## Code Style

1. **Imports**: Organize imports in three groups, separated by a blank line:
   - Standard library imports
   - Third-party library imports (including PyQt and QGIS)
   - Local application imports

2. **Docstrings**: Use triple double-quotes for docstrings. Include a brief description, followed by parameter descriptions and return value descriptions if applicable.

3. **Type Hints**: Use Python type hints where appropriate to enhance code clarity.

## Error Handling

1. Use try-except blocks appropriately for graceful error handling.
2. Log exceptions and errors rather than just printing them.
3. Present user-friendly error messages in the UI when appropriate.

## Testing

1. Write unit tests for core functionality.
2. Place test files in a separate 'test' directory.

## Version Control

1. Use descriptive commit messages that explain the "why" not just the "what".
2. Include references to issue numbers when applicable.

---

This document serves as a guide for maintaining consistency across the Landuse Analyst QGIS plugin codebase. It aims to balance Python best practices with maintaining compatibility with the original C++ codebase naming patterns.