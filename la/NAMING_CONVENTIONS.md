# Naming Conventions for Land Use Analyst PyQt Port

This document outlines the naming conventions used in the PyQt port of Land Use Analyst.
These conventions are consistent with the original C++ codebase with adaptations for Python
best practices where appropriate.

## Classes

- Classes start with `La` prefix and use PascalCase
  - Example: `LaCrop`, `LaCropManager`, `LaGuid`
- UI classes that derive from Qt Designer forms maintain the same naming
  - Example: `LaCropManagerBase` (base UI class), `LaCropManager` (implementation)

## Methods/Functions

- Methods and functions use camelCase without prefixes.
  - Example: `calculateYield()`, `refreshCropTable()`
- Properties exposed to Qt via `pyqtProperty` use camelCase without prefixes.
  - Getter and setter methods referenced by `pyqtProperty` (if needed) also follow the standard method naming convention (camelCase, no prefix). If it is signal or slot related variable, it should be prefixed with `_` and use camelCase.
  - Example:
    ```python
    # In a class definition
    _cropYieldChanged = pyqtSignal() # Define the notify signal

    def getCropYield(self) -> int:
        """Getter for cropYield property."""
        return self.mCropYield

    def setCropYield(self, theValue: int):
        """Setter for cropYield property."""
        if self.mCropYield != theValue:
            self.mCropYield = theValue
            self._cropYieldChanged.emit() # Emit signal on change

    # Define the property
    cropYield = pyqtProperty(int, fget=getCropYield, fset=setCropYield, notify=cropYieldChanged)
    ```
- For standard Python properties (not directly exposed via `pyqtProperty` or when providing a Pythonic interface), use `@property` and `@<propertyName>.setter` decorators.
  - The property name itself uses camelCase without prefixes.
  - The internal member variable follows the `_m` prefix convention.
  - Example (Read/Write):
    ```python
    @property
    def description(self) -> str:
        return self._mDescription

    @description.setter
    def description(self, theValue: str):
        self._mDescription = theValue
    ```
  - Example (Read-Only):
    ```python
    @property
    def guid(self) -> str:
        # Assuming mGuid is intended to be read-only after creation
        return self.mGuid
    ```
- **Type Hinting with `pyqtProperty`:** Since `pyqtProperty` can obscure type information from static analyzers, consider using `.pyi` stub files to declare the properties with standard `@property` syntax for improved type checking and autocompletion in the IDE.
- Event handlers (slots) connected to Qt signals follow the `on_<objectName>_<signalName>` convention.
  - Example: `on_pbnApply_clicked()`, `on_tblCrops_itemSelectionChanged()`

### Special Case: Class Methods

- Class methods decorated with `@classmethod` use `cls` as the first parameter name, not `theCls`
  - This is a deliberate exception to our naming convention to maintain compatibility with standard Python practices
  - The `cls` parameter name is so universally recognized in Python that deviating would reduce code readability
  - Example:
    ```python
    @classmethod
    def initialize(cls, theEnabled: bool = False):
        # Use cls here, not theCls
        cls._mDebug_enabled = theEnabled
    ```
- Other parameters in class methods still follow the `the` prefix convention
  - Example: `@classmethod def fromXml(cls, theXmlString)`

## Variables

### Parameter Naming (Very Important)
- Function parameters use `the` prefix (maintained from C++ convention)
  - Example: `theGuid`, `theCrop`, `theFileName`, `theData`
  - This prefix is crucial and must be maintained for consistency with the original C++ codebase

### Local Variables (Very Important)
- Temporary/local variables use `my` prefix (maintained from C++ convention)
  - Example: `myAnimal`, `mySettings`, `myCropsMap`, `myEncodedString`
  - This prefix is crucial and must be maintained for consistency with the original C++ codebase

### Member Variables
- Class member variables use `m` prefix (maintained from C++ convention)
  - Example: `mName`, `mCropYield` (instead of Python-style `_name`, `_cropYield`)
- Class members that should be treated as "private" start with underscore + m
  - Example: `_mCropMap`, `_mImageFile`
- Public properties should not have prefixes

### Pointer-like References
- When porting C++ pointer semantics to Python, maintain clear naming by using:
  - Suffix `Ref` for references to shared objects
    - Example: `mCropManagerRef` (equivalent to C++ pointer)
  - Use proper Python pass-by-reference patterns where C++ used pointers
  - For collections that contained pointers in C++, use explicit type hints
    - Example: `mCropsMap: Dict[str, LaCrop]`  # In C++, this might have been Map<QString, LaCrop*>

## PyQt Properties and Custom Types

### PyQt Property Naming
- Properties defined with pyqtProperty should use camelCase without prefixes
  - Example: `name`, `description`, `cropYield`
- Getter and setter methods for properties follow standard method naming conventions
  - Example: `name()`, `setName(theValue)`

### Custom Class Handling with PyQt Properties
- When using pyqtProperty with custom classes, be aware of these limitations:
  - PyQt properties have limited support for custom Python classes that aren't explicitly supported by Qt
  - For complex custom types, use one of these approaches:
    1. Use basic types for properties (int, float, str, list, etc.) and handle conversion in getter/setter methods
    2. Register custom types with Qt's type system using `qRegisterMetaType()`
    3. Use QVariant for properties that need to hold custom types
  - When properties need to reference custom classes, follow this naming pattern:
    - Use `mObjectRef` for the actual object reference (member variable)
    - Use `objectId` or similar for the property (typically a string GUID)
    - Example:
      ```python
      # Member variable (reference to object)
      self.mCropRef = None

      # Property (stores ID)
      @pyqtProperty(str)
      def cropId(self):
          return self.mCropRef.guid if self.mCropRef else ""

      @cropId.setter
      def cropId(self, theGuid):
          self.mCropRef = LaUtils.getCrop(theGuid)
      ```

## UI Elements

Qt Designer widgets should maintain consistent prefixes to indicate their type:

- `le`: Line edit widgets
  - Example: `leName`, `leDescription`
- `sb`: Spin box widgets
  - Example: `sbCropYield`, `sbCropCalories`
- `tbl`: Table widgets
  - Example: `tblCrops`
- `pbn`: Push buttons
  - Example: `pbnApply`, `pbnCropPic`
- `lbl`: Labels
  - Example: `lblCropPix`
- `cb`: Combo boxes
  - Example: `cbAreaUnits`, `cbFodderEnergyType`
- `grp`: Group boxes
  - Example: `grpProfiles`
- `tool`: Tool buttons
  - Example: `toolCopy`, `toolNew`

## Signals and Slots

- Connect signals and slots using the PyQt5 syntax
- Use meaningful method names that describe the action
- For custom signals, use verb phrases
  - Example: `cropSelected`, `cropChanged`
  - Signal connections should follow this pattern:
  ```python
  # Signal connection
  self.pbnApply.clicked.connect(self.on_pbnApply_clicked)
  ```

## Enums

- Enum classes use PascalCase with `La` prefix where appropriate
- Individual enum values use PascalCase
  - Example: `AreaUnits.Hectare`, `AreaUnits.Dunum`

## Constants

- Module-level constants use UPPER_CASE_WITH_UNDERSCORES
  - Example: `DEFAULT_CROP_YIELD`, `MAX_CALORIES`

## File Names

- Python module files use all lowercase with no underscores
  - Example: `lacrop.py`, `lacropmanager.py`
- UI files follow Qt Designer naming convention
  - Example: `lacropmanagerbase.ui`

## Imports

- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports (PyQt, etc.)
  3. Local application/library imports
- Within each group, imports should be sorted alphabetically

## Type Hints

- Use Python type hints for function parameters and return values
- Example:
  ```python
  def setCropYield(self, theYield: int) -> None:
      self.mCropYield = theYield
  ```

## Documentation

- Use docstrings for classes and methods
- Follow reStructuredText (ReST) format
- Example:
  ```python
  def cropYield(self) -> int:
      """
      Get the crop yield.

      :return: The crop yield value in kg/ha or kg/dunum
      :rtype: int
      """
      return self.mCropYield

  def calculateYield(self, theArea: float, theUnitType: str) -> float:
      """
      Calculate total yield based on area and unit type.

      :param theArea: The area value to use for calculation
      :type theArea: float
      :param theUnitType: The unit type ('Hectare' or 'Dunum')
      :type theUnitType: str
      :return: The calculated total yield
      :rtype: float
      :raises ValueError: If theUnitType is not supported
      """
      # Implementation here
  ```

---

*Note: These conventions aim to maintain consistency with the original C++ codebase while adopting Python-specific best practices where appropriate. The `the` prefix for parameters, `my` prefix for local variables, and `m` prefix for member variables are particularly important to maintain consistency with the original code.*