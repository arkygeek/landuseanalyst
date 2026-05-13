# Copilot Instructions for Landuse Analyst

## Project Overview

**Landuse Analyst** is a QGIS PyQt5 plugin that determines the catchment area needed for food production to supply a settlement. It's an archaeological modeling tool that calculates land area requirements based on demographic inputs, dietary profiles, and animal/crop productivity parameters. This is a Python port of an original C++ codebase.

**Key Architecture Pattern**: Model-View separation with Qt signals/slots for reactive updates between business logic and UI.

## Directory Structure & Responsibilities

- `la/lib/` - **Core business logic**: Models (LaModel), calculations (lacalculations.py), serialization, utility functions
- `la/gui/` - **UI controllers**: Main form (lamainform.py), manager dialogs, signal/slot implementations
- `la/ui/` - **Qt Designer UI files**: Base UI classes generated from `.ui` files (do not edit directly)
- `la/scripts/` - **Build helpers**: Resource compilation, string translation
- `la/test/` - **Test suite**: Unit tests using nosetests, QGIS mock interface

## Critical Naming Conventions

This project maintains **strict naming consistency with its C++ heritage**. Violations break existing patterns:

### Member Variables (C++ style, NOT Python style)
- **Regular members**: `mVariableName` (e.g., `mPopulation`, `mCropYield`)
  - Directly accessible throughout class and externally
- **Protected members**: `_mVariableName` (e.g., `_mDescription`)
  - For internal/derived-class access only
- **DO NOT** use Python's `_variable` or `variable_name` conventions

### Function Parameters (Very Important)
- **Always** use `the` prefix: `theValue`, `theModel`, `thePath`
- Example: `def setCropYield(self, theYield: int) -> None:`
- This consistency is critical for maintaining C++ compatibility during porting

### Local Variables
- **Always** use `my` prefix: `myList`, `myCrop`, `mySettings`
- Example: `myDietLabels = LaDietLabels()`

### Classes & UI Elements
- All project classes: `La` prefix + PascalCase (e.g., `LaCrop`, `LaCropManager`, `LaModel`)
- UI elements follow Qt prefixes: `lbl` (label), `pbn` (button), `sb` (spinbox), `tbl` (table), `le` (line edit), `cbo` (combo box), `grp` (group box)

See [NAMING_CONVENTIONS.md](../la/NAMING_CONVENTIONS.md) and [CODING_STANDARDS.md](../la/CODING_STANDARDS.md) for exhaustive reference.

## Core Data Flow Pattern

```
User Input (GUI) → Qt Signal → Slot in LaMainForm → LaMainController → LaModel
                                                              ↓
                                                         lacalculations.py
                                                              ↓
                                                    LaAnimal/LaCrop managers
                                                              ↓
                                               Update mAnimalsMap/mCropsMap
                                                              ↓
                                          Emit pyqtSignals (_*Changed) → UI refresh
```

### Key Entry Points
- **GUI Entry**: `la/gui/lamainform.py` - Main UI controller, coordinates all user interactions
- **Main Model**: `la/lib/lamodel.py` - Central data holder with 50+ pyqtSignals for reactive updates
- **Calculations**: `la/lib/lacalculations.py` - Extracted calculation functions (1460+ lines); methods receive model as `theModel` parameter
- **Managers**: `la/gui/la*manager.py` - Dialog controllers for Animals, Crops, Parameters (follow MVC pattern)

## XML Serialization Pattern

The project uses **XML for persistent storage** of all data (animals, crops, profiles, models):

```python
# All serializable objects inherit from LaSerialisable
class LaCrop(LaSerialisable):
    def toXml(self) -> str:
        """Return XML string representation"""
        myXml = f"<crop name='{self.mName}'>...</crop>"
        return myXml
    
    def fromXml(self, theXmlString: str):
        """Parse XML and populate member variables"""
        # Parse theXmlString, populate self.m* variables
```

- **Config location**: `~/.landuseAnalyst/` (user's home directory)
- **Stored objects**: Animal profiles, crop profiles, animal parameters, crop parameters, model saves
- Use `LaUtils.userSettingsDirPath()` to get base directory
- Always use `LaSerialisable.toXmlFile()` / `fromXmlFile()` for file I/O

## PyQt Signal/Slot Conventions

Signals enable reactive updates across the model-view boundary:

```python
# In LaModel class definition:
_cropYieldChanged = pyqtSignal()  # Signal definition (prefix with _)

# Property with notification
@pyqtProperty(int, notify=_cropYieldChanged)  
def cropYield(self):
    return self.mCropYield

@cropYield.setter
def cropYield(self, theValue: int):
    if self.mCropYield != theValue:
        self.mCropYield = theValue
        self._cropYieldChanged.emit()  # Emit signal on change

# In LaMainForm (slot handler):
def on_pbnApply_clicked(self):  # Slot naming: on_<objectName>_<signalName>
    """Handle apply button click"""
    # Update model → signals fire → UI refreshes automatically
```

**Signal naming**: `_mVariableChanged` (underscore prefix for internal signals)  
**Slot naming**: `on_<uiElementName>_<signalName>()`

## Testing & Build Workflow

### Build/Compile
```bash
# Compile Qt resources (must do before running)
pyrcc5 -o la/resources_rc.py la/resources.qrc

# Recommended: use pb_tool (see Makefile)
# pb_tool handles resource compilation, deployment, testing
```

### Testing
```bash
# From la/ directory:
make test              # Runs nosetests (requires QGIS environment)
make pylint            # Check code style
make pep8              # PEP8 style checks
```

**Test Files**: `la/test/` contains unit tests with mock QGIS interface (`qgis_interface.py`) for isolated testing.

## Important File Cross-References

- **UI Base Classes** (auto-generated, don't edit): `la/ui/laCropManagerBase.ui` → `la/ui/lacropmanagerbase.py`
- **Type Hints**: Some complex types use `.pyi` stub files (e.g., `lacrop.pyi`) for IDE support
- **Debug Logging**: Use `LaUtils.debug.log(theMessage, theComponent)` throughout codebase
- **Configuration**: `QSettings` keys use `landuse_analyst/` namespace

## Common Patterns & Anti-Patterns

### ✅ DO: Access model data through properties
```python
myPopulation = self.model.population  # Via pyqtProperty
myCals = theModel.mCaloriesPerPersonDaily  # Direct member access (internal use)
```

### ✅ DO: Connect signals for reactive updates
```python
self.model._populationChanged.connect(self.on_population_changed)
```

### ❌ DON'T: Use Python naming conventions
```python
# ❌ Wrong - violates project conventions
self._name = "test"           # Don't use single _
self.name_value = 100         # Don't use underscores
def calc_yield(self):         # Don't use underscores
```

### ❌ DON'T: Modify UI files directly
Edit `.ui` files only in Qt Designer, then regenerate Python files with `pyuic5`.

## Calculation Pattern (lacalculations.py)

Calculations are extracted into module-level functions that receive the model as a parameter:

```python
def doCalcsPlantsFirstIncludeDairy(theModel: 'LaModel') -> LaDietLabels:
    """Calculation logic (formerly LaModel methods)"""
    myDietLabels = LaDietLabels()
    myMCalsSettlementAnnual = theModel.mPopulation * theModel.mCaloriesPerPersonDaily * 365.0 / 1000.0
    # ... calculation logic ...
    return myDietLabels
```

**Pattern**: Receive `theModel`, read from `theModel.m*` member variables, return results.

## Platform-Specific Notes

The plugin runs on **Linux, Windows, macOS**. Key differences:
- Plugin directory: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/` (Linux)
- See README.md for Windows/macOS paths
- Windows may need `plastique` style set explicitly (`app.setStyle('plastique')`)
- macOS bundles Qt frameworks; check library paths in `gui/main.py`

## Integration with QGIS

The plugin hooks into QGIS via:
- `landuse_analyst.py` - Plugin entry point, implements QGIS plugin interface
- `iface` parameter - QGIS interface object for toolbar/menu integration
- QSettings namespace: `landuse_analyst/`
- QGIS compatibility: Tested with QGIS 3.x, Python 3.12+

## Next Steps for Contributors

1. Review [NAMING_CONVENTIONS.md](../la/NAMING_CONVENTIONS.md) thoroughly
2. Study [LaModel](../la/lib/lamodel.py) to understand central data structure
3. Run `make compile` to generate resources before any development
4. Examine existing managers (e.g., [LaCropManager](../la/gui/lacropmanager.py)) for UI pattern
5. Trace signal connections in [LaMainForm](../la/gui/lamainform.py) to understand reactivity pattern
