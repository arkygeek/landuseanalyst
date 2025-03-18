# Landuse Analyst PyQt Port Coding Standards

This document outlines the coding standards and naming conventions for the PyQt rewrite of the Landuse Analyst QGIS plugin. These standards aim to maintain consistency with the original C++ codebase while adapting to Python best practices.

## Class Names

- Use PascalCase for class names: `LaCrop`, `LaCropManager`, `LaUtils`
- Maintain the "La" prefix (for Landuse Analyst) for all project-specific classes
- Example: `LaGuid`, `LaCrop`, `LaAnimal`

## Member Variables

- Use underscore prefix for private/protected member variables: `_name`, `_description`, `_cropYield`
- This replaces the C++ "m" prefix convention (`mName` → `_name`)
- Example: `self._name = name`

## Public Properties

- Use property decorators for getters and setters when appropriate
- Property names should use camelCase without prefix: `name`, `description`, `cropYield`
- Example:
  ```python
  @property
  def name(self):
      return self._name
      
  @name.setter
  def name(self, value):
      self._name = value
  ```

## Methods

- Use camelCase for method names: `getName()`, `setName()`, `cropYield()`
- Maintain the same method names as the original C++ code where possible
- Example: `def cropYield(self):`, `def setCropYield(self, value):`

## UI Element Naming

Maintain the same prefixes used in the C++ codebase:

| Element Type    | Prefix | Example         |
|-----------------|--------|-----------------|
| Label           | lbl    | lblCropPix      |
| Generic Label   | label  | label_2         |
| Push Button     | pbn    | pbnApply        |
| Spin Box        | sb     | sbCropYield     |
| Combo Box       | cb     | cbAreaUnits     |
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
- Example:
  ```python
  def cropYield(self):
      """Get the crop yield.
      
      Returns:
          int: The crop yield value
      """
      return self._cropYield
  ```

## Type Hints

- Use type hints for function parameters and return values
- Example:
  ```python
  def setCropYield(self, yield_value: int) -> None:
      """Set the crop yield.
      
      Args:
          yield_value: The new crop yield value
      """
      self._cropYield = yield_value
  ```

## Signal/Slot Naming Conventions

- Follow Qt conventions for signal/slot connections
- Slot method names should indicate the sender and the signal
- Example: `on_pbnApply_clicked()`, `on_tblCrops_itemSelectionChanged()`

## Exceptions and Error Handling

- Use try/except blocks for error handling
- Log errors appropriately
- Provide user-friendly error messages

This document will evolve as the project progresses. Always prioritize readability and consistency.