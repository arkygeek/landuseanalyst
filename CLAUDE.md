# Landuse Analyst — Claude Code Context

## Session startup checklist (do this before anything else)

1. Read `.ai-project-history/landuse-analyst/memories/` — persistent rules and
   decisions that apply to every session.
2. Read the most recent `session-YYYY-MM-DD/task.md` in
   `.ai-project-history/landuse-analyst/` — what is done vs. still pending.
3. Read that session's `walkthrough.md` for context on why decisions were made.

The sparse-checkout on the submodule should already limit the view to
`landuse-analyst/` only. If other project folders are visible, run:

```bash
git -C .ai-project-history sparse-checkout init --cone
git -C .ai-project-history sparse-checkout set landuse-analyst
```

## Session shutdown checklist (do this before ending)

1. Update or create `session-YYYY-MM-DD/task.md` and `walkthrough.md`.
2. If any new persistent rule or decision was made, add a file to `memories/`.
3. Commit inside the submodule, then advance the pointer in the main repo.

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

```text
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

- Active development: `main`
- Always check `cppArchive/` before inventing new behaviour

The `antigravity-collaboration` branch was retired on 2026-05-14 once its
work was force-pushed onto `main`. The old pre-merge `main` is preserved
as `origin/backup-main-2026-05-14` in case anything ever needs to be
recovered from it.
