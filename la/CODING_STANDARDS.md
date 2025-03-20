# Landuse Analyst PyQt Port Coding Standards

This document outlines the coding standards and naming conventions for the PyQt rewrite of the Landuse Analyst QGIS plugin. These standards aim to maintain consistency with the original C++ codebase while adapting to Python best practices.

## Class Names

- Use PascalCase for class names: `LaCrop`, `LaCropManager`, `LaUtils`
- Maintain the "La" prefix (for Landuse Analyst) for all project-specific classes
- Example: `LaGuid`, `LaCrop`, `LaAnimal`

## Member Variables

- Use `mVarName` for regular member variables: `mName`, `mDescription`, `mCropYield`
- Regular member variables are accessible throughout the class and from outside

- Use `_mVarName` for protected member variables: `_mName`, `_mDescription`, `_mCropYield`
- Use protected members when you want to allow access in derived classes but not externally
- Example: `self.mName = name` (regular), `self._mName = name` (protected)

- Note that Python does not enforce access restrictions on member variables
- The naming conventions above are just that - conventions
- Python's philosophy is "we're all consenting adults here" - access control is by convention, not enforcement

## Public Properties

- Use property decorators for getters and setters when appropriate
- Property names should use camelCase without prefix: `name`, `description`, `cropYield`
- Example:
  ```python
  @property
  def name(self):
      return self.mName

  @name.setter
  def name(self, value):
      self.mName = value
  ```

## Methods

- Use camelCase for method names: `getName()`, `setName()`, `cropYield()`
- Maintain the same method names as the original C++ code where possible
- Example: `def getName(self):`, `def setName(self, value):`
- When accessing member variables inside methods, use the appropriate prefix:
  ```python
  def getName(self):
      return self.mName  # Use mName for regular member variables

  def setName(self, value):
      self.mName = value  # Use mName for regular member variables

  def getProtectedName(self):
      return self._mName  # Use _mName for protected member variables
  ```

## UI Element Naming

Maintain the same prefixes used in the C++ codebase, but note these are separate from the member variable naming convention:

| Element Type    | Prefix | Example         |
|-----------------|--------|-----------------|
| Label           | lbl    | lblCropPix      |
| Generic Label   | label  | label_2         |
| Push Button     | pbn    | pbnApply        |
| Spin Box        | sb     | sbCropYield     |
| Combo Box       | cbo    | cboCrop         | <!-- Fixed inconsistency from cb to cbo -->
| Table Widget    | tbl    | tblCrops        |
| Line Edit       | le     | leName          |
| Group Box       | grp    | grpProfiles     |
| Tool Button     | tool   | toolNew         |

## Constants and Enumerations

- Use all uppercase with underscores for constants: `MAX_YIELD`, `DEFAULT_VALUE`
- Use PascalCase for enumeration values: `Dunum`, `Hectare`, `KCalories`
- Example:
  ```python
  class AreaUnits(Enum):
      Dunum = 0
      Hectare = 1
  ```

## File Organization

- Group related methods together
- Keep initialization code at the top
- Keep UI-related code separate from business logic where possible
- Use appropriate docstrings for classes and methods

## Comments and Documentation

- Use docstrings for classes and methods following the Google Python Style Guide
- Reference member variables with appropriate prefix in documentation
- Example:
  ```python
  def cropYield(self):
      """Get the crop yield.

      Returns:
          int: The crop yield value from the mCropYield member variable
      """
      return self.mCropYield
  ```

## Type Hints

- Use type hints for function parameters and return values
- Example:
  ```python
  def setCropYield(self, yield_value: int) -> None:
      """Set the crop yield.

      Args:
          yield_value: The new crop yield value to store in mCropYield
      """
      self.mCropYield = yield_value
  ```

## Signal/Slot Naming Conventions

- Follow Qt conventions for signal/slot connections
- Slot method names should indicate the sender and the signal
- Example: `on_pbnApply_clicked()`, `on_tblCrops_itemSelectionChanged()`

## Exceptions and Error Handling

- Use try/except blocks for error handling
- Log errors appropriately
- Provide user-friendly error messages

## Migration Notes

- When updating existing code, be sure to follow the member variable naming conventions:
  - Regular member variables use mPrefix (e.g., mName)
  - Protected member variables use _mPrefix (e.g., _mName)
  - Update all direct member variable access
  - Property accessor methods
  - Documentation and comments
  - Type stubs (.pyi files)

This document will evolve as the project progresses. Always prioritize readability and consistency.