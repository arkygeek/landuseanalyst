# Landuse Analyst — Claude Code Context

## What this project is
A QGIS plugin (Python/PyQt5) that models the agricultural catchment area of
ancient settlements. It is a port of an original C++ plugin. The Python port
must replicate the C++ behaviour exactly — when in doubt, check `cppArchive/`.

## Coding standards (strictly enforced)
See `la/CODING_STANDARDS.md` and `la/NAMING_CONVENTIONS.md` for the full rules.
Key points an AI must not get wrong:

- **Classes** — `La`-prefix PascalCase: `LaCrop`, `LaModel`, `LaUtils`
- **Methods** — camelCase, no prefix: `calculateYield()`, `refreshTable()`
- **Parameters** — `the`-prefix: `theGuid`, `theCrop`, `theFileName`
- **Local variables** — `my`-prefix: `myCrop`, `mySettings`, `myGuid`
- **Member variables** — `m`-prefix: `mName`, `mCropYield`
- **Private/cache members** — `_m`-prefix: `_mCropsCache`, `_mGuid`
- **pyqtSignals** — plain `_`-prefix, no `m`: `_nameChanged = pyqtSignal(str)`
- **UI widgets** — type-prefix: `cb` combo box, `sb` spin box, `le` line edit,
  `pbn` push button, `lbl` label, `tbl` table, `grp` group box, `tool` tool button
- **Docstrings** — reStructuredText format (`:param x:`, `:type x:`, `:return:`, `:rtype:`)

## Data files — IMPORTANT
The app reads animal/crop/parameter profiles from `~/.landuseAnalyst/` at
runtime. These directories must be populated before the plugin shows any data:

```
~/.landuseAnalyst/
    animalProfiles/           ← one .xml per animal
    cropProfiles/             ← one .xml per crop
    animalParameterProfiles/  ← one .xml per animal parameter set
    cropParameterProfiles/    ← one .xml per crop parameter set
    images/                   ← thumbnails shown in UI
```

Sample data lives in `testData/` in this repo. Run `./install_sample_data.sh`
to copy it into place (safe to re-run; skips existing files by default).

`la/test/xmlData/` is a separate, minimal dataset used only by unit tests.
Do not confuse it with `testData/`.

## Key files
- `la/lib/lautils.py` — utility class; owns all path resolution and XML loading
- `la/lib/lamodel.py` — the calculation engine
- `la/gui/lamainform.py` — main window implementation
- `la/ui/lamainformbase.py` — Qt Designer base class for the main window
- `la/lib/lacrop.py`, `la/lib/laanimal.py` — core domain objects
- `cppArchive/src/` — original C++ source; the reference implementation

## Branch conventions
- Active development: `antigravity-collaboration`
- Main: `main`
- Always check `cppArchive/` before inventing new behaviour
