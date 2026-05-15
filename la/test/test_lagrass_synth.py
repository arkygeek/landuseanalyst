"""
test_lagrass_synth.py — synthesise test rasters for the catchment pipeline.

Generates a small DEM + per-crop + per-animal + common-crop + common-grazing
suitability rasters, writes them to ``testData/syntheticRasters/``, and
patches each ``testData/*ParameterProfiles/*.xml`` file's ``<rasterName>``
field with the absolute path of its assigned suitability raster.

**Dev-workflow note**

This script writes machine-specific absolute paths into the XML profile
files in your working tree. **Do not commit those XML changes.** When
you're done testing the catchment pipeline, revert them with::

    git checkout testData/animalParameterProfiles testData/cropParameterProfiles

The generated rasters under ``testData/syntheticRasters/`` are
gitignored, so they don't show up in ``git status``.

Run from the QGIS Python Console::

    exec(open('/path/to/la/test/test_lagrass_synth.py').read())

Standalone use (no QGIS — only NumPy + GDAL required)::

    python3 la/test/test_lagrass_synth.py

The script is idempotent: re-running it regenerates the rasters and
re-patches the XML. Safe to run multiple times during development.
"""

import os
import random
import xml.etree.ElementTree as ET
from typing import List, Tuple

import numpy as np
from osgeo import gdal, osr


# ---------------------------------------------------------------------------
# Grid layout
# ---------------------------------------------------------------------------
# 200×200 cells at 20 m resolution = 4 km × 4 km = 1600 ha total.
# Comfortably bigger than the Min-Pop scenario's ~268 ha demand.
_GRID_W      = 200
_GRID_H      = 200
_CELL_SIZE   = 20.0
_ORIGIN_X    = 500000.0 - (_GRID_W * _CELL_SIZE) / 2.0   # UTM-like centre
_ORIGIN_Y    = 4000000.0 + (_GRID_H * _CELL_SIZE) / 2.0   # GDAL uses upper-left origin
_CRS_EPSG    = 32633   # UTM 33N — any metric CRS is fine for a synth scenario

# Settlement at the centre — easting/northing the orchestrator will use.
SETTLEMENT_X = 500000.0
SETTLEMENT_Y = 4000000.0

# Project paths
_PROJECT_ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_OUTPUT_DIR    = os.path.join(_PROJECT_ROOT, "testData", "syntheticRasters")
_CROP_PROF_DIR = os.path.join(_PROJECT_ROOT, "testData", "cropParameterProfiles")
_ANIM_PROF_DIR = os.path.join(_PROJECT_ROOT, "testData", "animalParameterProfiles")


# ---------------------------------------------------------------------------
# Raster-write helpers
# ---------------------------------------------------------------------------
def _writeGeoTiff(theArray: np.ndarray, thePath: str, theIsBinary: bool) -> None:
    """Write a 2D ``numpy`` array as a GeoTIFF, georeferenced to the synth grid."""
    myDriver = gdal.GetDriverByName("GTiff")
    myDataType = gdal.GDT_Byte if theIsBinary else gdal.GDT_Float32
    myDataset = myDriver.Create(
        thePath, _GRID_W, _GRID_H, 1, myDataType,
        options=["COMPRESS=LZW", "TILED=YES"],
    )
    myDataset.SetGeoTransform((_ORIGIN_X, _CELL_SIZE, 0.0, _ORIGIN_Y, 0.0, -_CELL_SIZE))
    mySrs = osr.SpatialReference()
    mySrs.ImportFromEPSG(_CRS_EPSG)
    myDataset.SetProjection(mySrs.ExportToWkt())
    myBand = myDataset.GetRasterBand(1)
    if theIsBinary:
        myBand.SetNoDataValue(0)
        myBand.WriteArray(theArray.astype(np.uint8))
    else:
        myBand.WriteArray(theArray.astype(np.float32))
    myBand.FlushCache()
    myDataset.FlushCache()


def _makeCoordinateGrids() -> Tuple[np.ndarray, np.ndarray]:
    """Return (X, Y) arrays of CRS-unit coordinates for each cell centre."""
    myXs = _ORIGIN_X + (np.arange(_GRID_W) + 0.5) * _CELL_SIZE
    myYs = _ORIGIN_Y - (np.arange(_GRID_H) + 0.5) * _CELL_SIZE  # top-down rows
    return np.meshgrid(myXs, myYs)


# ---------------------------------------------------------------------------
# Layer factories
# ---------------------------------------------------------------------------
def _buildDem() -> str:
    """A gentle bowl: z = 100 + 0.0005 * r²  (centred on the settlement)."""
    myXGrid, myYGrid = _makeCoordinateGrids()
    myRsq = (myXGrid - SETTLEMENT_X) ** 2 + (myYGrid - SETTLEMENT_Y) ** 2
    myDem = 100.0 + 0.0005 * myRsq
    myPath = os.path.join(_OUTPUT_DIR, "dem.tif")
    _writeGeoTiff(myDem, myPath, theIsBinary=False)
    return myPath


def _suitabilityBlob(
    theShape:    str,
    theParamA:   float,
    theParamB:   float,
    theMinFrac:  float = 0.10,
) -> np.ndarray:
    """
    Build a 1/0 suitability mask with a recognisable spatial pattern.

    :param theShape: one of "quadNE", "quadSW", "quadNW", "quadSE",
        "ring", "stripeH", "stripeV", "sine", "blob".
    :param theParamA: shape-specific parameter (radius, threshold, etc.).
    :param theParamB: shape-specific second parameter.
    :param theMinFrac: minimum fraction of cells that must end up as 1 —
        if the synthesised shape covers less, the function jitters until
        the area is acceptable.
    """
    myXGrid, myYGrid = _makeCoordinateGrids()
    myDx = myXGrid - SETTLEMENT_X
    myDy = myYGrid - SETTLEMENT_Y
    myR  = np.sqrt(myDx ** 2 + myDy ** 2)
    if theShape == "quadNE":
        myMask = (myDx > 0) & (myDy > 0)
    elif theShape == "quadSW":
        myMask = (myDx < 0) & (myDy < 0)
    elif theShape == "quadNW":
        myMask = (myDx < 0) & (myDy > 0)
    elif theShape == "quadSE":
        myMask = (myDx > 0) & (myDy < 0)
    elif theShape == "ring":
        myMask = (myR > theParamA) & (myR < theParamB)
    elif theShape == "stripeH":
        myMask = np.abs(myDy) < theParamA
    elif theShape == "stripeV":
        myMask = np.abs(myDx) < theParamA
    elif theShape == "sine":
        myMask = np.sin(myDx / theParamA) > theParamB
    elif theShape == "blob":
        myMask = (myDx + myDy) > theParamA
    else:
        myMask = np.ones_like(myDx, dtype=bool)
    return myMask.astype(np.uint8)


# ---------------------------------------------------------------------------
# Crop / animal raster generation
# ---------------------------------------------------------------------------
# Each entry: (xml-stem-prefix-in-name-tag, shape-key, param-a, param-b)
# Order matters only for stable filename assignment.
_CROP_SHAPES = [
    ("quadNE",  0.0,   0.0),
    ("quadSW",  0.0,   0.0),
    ("quadNW",  0.0,   0.0),
    ("quadSE",  0.0,   0.0),
    ("stripeH", 600.0, 0.0),
    ("stripeV", 600.0, 0.0),
    ("sine",    300.0, 0.2),
    ("blob",    -300.0, 0.0),
    ("ring",    600.0, 1600.0),
    ("ring",    200.0, 1200.0),
    ("ring",    400.0, 1400.0),
]

_ANIMAL_SHAPES = [
    ("ring",    300.0, 1500.0),
    ("ring",    500.0, 1700.0),
    ("ring",    200.0, 1300.0),
    ("ring",    700.0, 1900.0),
    ("ring",    100.0, 1100.0),
    ("blob",    0.0,   0.0),
    ("stripeV", 400.0, 0.0),
]


def _listXmlFiles(theDir: str) -> List[str]:
    if not os.path.isdir(theDir):
        return []
    return sorted(
        os.path.join(theDir, n) for n in os.listdir(theDir)
        if n.lower().endswith(".xml")
    )


def _findOrCreateChild(theParent, theTagName: str):
    myChild = theParent.find(theTagName)
    if myChild is None:
        myChild = ET.SubElement(theParent, theTagName)
    return myChild


def _patchRasterName(theXmlPath: str, theRasterPath: str) -> None:
    """Set ``<rasterName>`` to ``theRasterPath`` in an LA parameter XML."""
    myTree = ET.parse(theXmlPath)
    myRoot = myTree.getroot()
    myNode = _findOrCreateChild(myRoot, "rasterName")
    myNode.text = theRasterPath
    myTree.write(theXmlPath, encoding="utf-8", xml_declaration=True)


def _generateForProfiles(
    theDir:    str,
    theShapes: List[Tuple[str, float, float]],
    thePrefix: str,
) -> List[str]:
    """For every XML in ``theDir``, write a suitability raster + patch XML."""
    myXmlPaths = _listXmlFiles(theDir)
    myOutputs: List[str] = []
    for myIndex, myXmlPath in enumerate(myXmlPaths):
        myShape, myParamA, myParamB = theShapes[myIndex % len(theShapes)]
        myMask = _suitabilityBlob(myShape, myParamA, myParamB)
        myFileStem = os.path.splitext(os.path.basename(myXmlPath))[0]
        myRasterPath = os.path.join(_OUTPUT_DIR, f"{thePrefix}_{myFileStem}.tif")
        _writeGeoTiff(myMask, myRasterPath, theIsBinary=True)
        _patchRasterName(myXmlPath, myRasterPath)
        myOutputs.append(myRasterPath)
        print(f"  {thePrefix}/{myFileStem} ← {myShape}  → {os.path.relpath(myRasterPath, _PROJECT_ROOT)}")
    return myOutputs


def _buildCommonRasters() -> Tuple[str, str]:
    """
    Common-crop raster: inner-medium ring (cells closer than 1500 m, outside
    a 200 m exclusion buffer around the settlement).

    Common-grazing raster: outer ring (cells between 1200 m and 2000 m).
    """
    myXGrid, myYGrid = _makeCoordinateGrids()
    myR = np.sqrt((myXGrid - SETTLEMENT_X) ** 2 + (myYGrid - SETTLEMENT_Y) ** 2)

    myCommonCrop    = ((myR > 200.0)  & (myR < 1500.0)).astype(np.uint8)
    myCommonGrazing = ((myR > 1200.0) & (myR < 2000.0)).astype(np.uint8)
    myCropPath    = os.path.join(_OUTPUT_DIR, "commonCrop.tif")
    myGrazingPath = os.path.join(_OUTPUT_DIR, "commonGrazing.tif")
    _writeGeoTiff(myCommonCrop,    myCropPath,    theIsBinary=True)
    _writeGeoTiff(myCommonGrazing, myGrazingPath, theIsBinary=True)
    return myCropPath, myGrazingPath


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    random.seed(0)
    os.makedirs(_OUTPUT_DIR, exist_ok=True)

    print(f"Writing synth rasters to {_OUTPUT_DIR}")
    myDem = _buildDem()
    print(f"  DEM           → {os.path.relpath(myDem, _PROJECT_ROOT)}")

    myCrop, myGrazing = _buildCommonRasters()
    print(f"  Common-crop   → {os.path.relpath(myCrop, _PROJECT_ROOT)}")
    print(f"  Common-grazing→ {os.path.relpath(myGrazing, _PROJECT_ROOT)}")

    print("Generating per-crop suitability rasters + patching XML:")
    _generateForProfiles(_CROP_PROF_DIR, _CROP_SHAPES, "crop")

    print("Generating per-animal suitability rasters + patching XML:")
    _generateForProfiles(_ANIM_PROF_DIR, _ANIMAL_SHAPES, "animal")

    print("\nDone. Settlement coordinates for the model:")
    print(f"  easting  = {SETTLEMENT_X}")
    print(f"  northing = {SETTLEMENT_Y}")
    print("\nLoad dem.tif, commonCrop.tif, commonGrazing.tif in QGIS, then run.")


if __name__ == "__main__":
    main()
