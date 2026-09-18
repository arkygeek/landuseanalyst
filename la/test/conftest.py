"""
Shared pytest fixtures for the Landuse Analyst plugin test-suite.

Two kinds of tests live under ``la/test``:

* ``la/test/engine``: pure numpy + GDAL, no Qt or QGIS import. Runnable
  with any Python that has ``numpy`` and ``osgeo``.
* everything else: needs ``qgis.PyQt`` (and sometimes ``qgis.core``), so
  run these with the QGIS Python (``qgis_dev`` conda env locally, or the
  ``qgis/qgis`` container in CI).
"""

import os
import sys

import pytest

# Qt must never try to open a display under pytest.
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

try:
    from qgis.PyQt import sip as _sip
    from qgis.PyQt.QtWidgets import QApplication as _QApplication

    # Qt/QGIS C++ objects (QDialog-based LaModel, module-level QObjects) are
    # torn down in arbitrary order at interpreter exit and segfault the test
    # process (exit 139) even when every test passed. Let the OS reclaim them.
    _sip.setdestroyonexit(False)
    _APP = _QApplication.instance() or _QApplication([])
except ImportError:  # pragma: no cover - engine-only environments without Qt
    _APP = None

_TEST_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def repoRoot() -> str:
    """Absolute path of the repository root (the directory containing ``la/``)."""
    return _REPO_ROOT


@pytest.fixture(scope="session")
def testDataDir() -> str:
    """``la/test/xmlData``: the minimal profile + raster fixtures used by tests."""
    return os.path.join(_TEST_DIR, "xmlData")


@pytest.fixture(scope="session")
def shunaDemPath(testDataDir) -> str:
    """
    GRASS-ASCII DEM of the Shuna (Jordan Valley) study area, UTM 36N.

    Canonical thesis settlement: easting 744800, northing 3611100.
    """
    myPath = os.path.join(testDataDir, "GrassData", "demShuna")
    if not os.path.exists(myPath):
        pytest.skip(f"Shuna DEM fixture missing: {myPath}")
    return myPath


@pytest.fixture(scope="session")
def thesisScenarioCsvDir() -> str:
    """Thesis Numbers-spreadsheet dumps for the min-pop Chalcolithic scenario."""
    return os.path.join(_TEST_DIR, "data", "thesis_scenarios", "min_pop_chalcolithic")


@pytest.fixture
def sampleProfilesDir(repoRoot, monkeypatch) -> str:
    """
    Point ``LaUtils`` at the repo's ``testData/`` profile catalogue.

    ``testData/`` holds the thesis-canonical Chalcolithic crop/animal
    profiles (Table E.1/F.1 values), so calculations run against it can be
    compared with the published thesis numbers and the web app's
    ``tests/test_thesis_golden_numbers.py``.
    """
    from la.lib.lautils import LaUtils

    myDir = os.path.join(repoRoot, "testData")
    monkeypatch.setattr(LaUtils, "userDataPath", staticmethod(lambda: myDir))
    monkeypatch.setattr(LaUtils, "userSettingsDirPath", staticmethod(lambda: myDir))
    return myDir


@pytest.fixture(scope="session")
def qtApp():
    """A ``QApplication`` for tests that construct QObject-based model classes."""
    if _APP is None:
        pytest.skip("Qt is not available in this environment")
    return _APP
