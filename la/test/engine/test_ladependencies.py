"""Dependency probe reports what the engine can use (no QGIS needed)."""

import sys

from la.lib import ladependencies


def test_probe_reports_scipy_state_consistently():
    myReport = ladependencies.probe()
    try:
        import scipy  # noqa: F401
        assert myReport.hasScipy
        assert myReport.canWalkingTime
    except ImportError:
        assert not myReport.hasScipy
    assert isinstance(myReport.problems(), list)


def test_pip_command_targets_this_interpreter():
    myCommand = ladependencies.pipInstallCommand("scipy")
    assert myCommand[0] == sys.executable
    assert myCommand[-1] == "scipy" and "pip" in myCommand
