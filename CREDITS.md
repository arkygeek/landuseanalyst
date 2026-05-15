# Credits & Acknowledgments

The Landuse Analyst QGIS plugin is built on the work of many people and
projects. The list below highlights the credits we want to call out
explicitly. Anything missing is an oversight — please open an issue.

## Original Landuse Analyst (C++)

The mathematical model, terminology, parameter conventions, and the
end-to-end workflow ported here were developed by:

- **Jason S. Jorgenson** — original Landuse Analyst (C++ / Qt4), thesis
  (*"Landuse Analyst: a tool for predicting the agricultural catchment
  area of archaeological settlements"*), and continued maintenance of
  the Python port.

The legacy C++ source is preserved under `cppArchive/` in this
repository as the reference implementation for every behavioural decision
in the Python port.

## GRASS GIS — `r.walk` algorithm

`la/lib/lagrass.py::LaGrass._makeWalkCostPure` is a pure-Python
re-implementation of the algorithm of GRASS GIS's `r.walk` module. We
ship the Python fallback because the QGIS Processing GRASS provider
intermittently excludes `r.walk` across QGIS bundles (even when GRASS
itself is installed), and we want every QGIS user to be able to run the
Walking Time analysis with zero extra setup.

The reference algorithm — `r.walk` — was originally written by:

- **Steno Fontanari** — Initial port to GRASS (ITC-IRST, 1992)
- **Pierre de Mouveaux** — Co-author of the original implementation
- **GRASS Development Team** — Continued maintenance by, among others,
  Markus Neteler, Hamish Bowman, Roberto Flor, Glynn Clements,
  Andrea Aime, and many others over three decades

Source code: <https://github.com/OSGeo/grass/tree/main/raster/r.walk>
Module manual: <https://grass.osgeo.org/grass-stable/manuals/r.walk.html>
License: GNU GPL v2 or later

The walking-velocity model uses Tobler's hiking function:

> Tobler, W. (1993). "Three Presentations on Geographical Analysis and
> Modeling: Non-Isotropic Geographic Modeling; Speculations on the
> Geometry of Geography; and Global Spatial Analysis." National Center
> for Geographic Information and Analysis, Technical Report 93-1.

## Other GRASS algorithms used

The catchment pipeline also relies on these GRASS algorithms through the
QGIS Processing framework (no shell-out, no hard-coded paths):

- `grass:r.cost` — Euclidean and friction-weighted cost-distance. Original
  authors include **Antony Awaida** (initial implementation), **James
  Hinthorne** (enhancements), and many GRASS Development Team
  contributors.
- `grass:r.mapcalc.simple` — Raster algebra. Authored by **Glynn
  Clements** with extensive contributions from the GRASS team.
- `grass:r.stats` — Cell-area statistics. Authored by **Michael Shapiro**
  with subsequent contributions from the GRASS team.

## Python ecosystem

The plugin's runtime depends only on libraries bundled with every QGIS
install, so end users need no extra setup:

- **Qt / PyQt5** — UI framework. © The Qt Company / Riverbank Computing.
- **matplotlib** — Chart rendering (report tab pie/bar/stacked charts
  embedded as base64 PNG `<img>` tags in QTextBrowser). © Matplotlib
  development team.
- **NumPy + SciPy** — Numerical work in the diet engine and the
  pure-Python `r.walk` fallback (especially `scipy.sparse.csgraph.dijkstra`
  for cost-distance propagation). © NumPy / SciPy developers.
- **GDAL / OGR** — Raster I/O and reprojection. © Open Source Geospatial
  Foundation.

## QGIS

The plugin is hosted in QGIS Desktop and uses QGIS APIs throughout:
`QgsTask`, `QgsMapLayerComboBox`, `QgsProcessingUtils`, `QgsRasterLayer`,
the Processing framework, and many more. © The QGIS Development Team.

## AI-assisted development

Substantial portions of the Python port — including the chart layer, the
GIS pipeline scaffolding, the orchestrator's binary-search loop, and the
synthetic test-data generator — were developed in collaboration with
Anthropic's Claude (Claude Opus 4.7) acting as a pair-programming
assistant. Every commit in this repository attributes specific changes
that benefited from AI assistance via `Co-Authored-By:` trailers.
