"""
ladependencies.py — runtime dependency probing for the catchment engine.

The diet calculation needs nothing beyond QGIS. The walking-cost engine
needs either ``scipy`` (pure-Python Dijkstra) or the GRASS Processing
provider (``grass:r.walk``). This module answers "what can run here?" and
knows how to install scipy into the QGIS Python.
"""

import importlib.util
import subprocess
import sys
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class LaDependencyReport:
    """Snapshot of what the engine can use on this machine."""
    hasScipy: bool
    hasGrassWalk: bool
    hasGrassCost: bool
    hasMatplotlib: bool
    scipyVersion: Optional[str] = None

    @property
    def canWalkingTime(self) -> bool:
        return self.hasScipy or self.hasGrassWalk

    @property
    def canEuclidean(self) -> bool:
        return self.hasScipy or self.hasGrassCost

    def problems(self) -> List[str]:
        """Human-readable list of what is missing (empty when everything works)."""
        myProblems = []
        if not self.hasScipy:
            if self.hasGrassWalk:
                myProblems.append(
                    "scipy is not installed in the QGIS Python; walking-time catchments will use "
                    "GRASS r.walk instead of the (faster, windowed) pure-Python engine.")
            else:
                myProblems.append(
                    "scipy is not installed in the QGIS Python and the GRASS provider is not "
                    "available, so catchment analysis cannot run. Diet calculations still work.")
        if not self.hasMatplotlib:
            myProblems.append("matplotlib is missing; report charts will be skipped.")
        return myProblems


def _hasModule(theName: str) -> bool:
    try:
        return importlib.util.find_spec(theName) is not None
    except (ImportError, ValueError):
        return False


def probe() -> LaDependencyReport:
    """Check scipy, matplotlib and the GRASS algorithms without importing heavy modules."""
    myScipyVersion = None
    myHasScipy = _hasModule("scipy")
    if myHasScipy:
        try:
            from importlib.metadata import version
            myScipyVersion = version("scipy")
        except Exception:
            myScipyVersion = None
    myHasWalk = myHasCost = False
    try:
        from la.lib.lagrassprocesslib import LaGrassProcessLib
        myHasWalk = LaGrassProcessLib.walkAlgorithmId() is not None
        myHasCost = LaGrassProcessLib.costAlgorithmId() is not None
    except Exception:
        pass
    return LaDependencyReport(
        hasScipy=myHasScipy, hasGrassWalk=myHasWalk, hasGrassCost=myHasCost,
        hasMatplotlib=_hasModule("matplotlib"), scipyVersion=myScipyVersion,
    )


def pipInstallCommand(thePackage: str = "scipy") -> List[str]:
    """The command that installs ``thePackage`` into *this* interpreter."""
    return [sys.executable, "-m", "pip", "install", "--user", thePackage]


def installPackage(thePackage: str = "scipy", theTimeoutSec: int = 600) -> "tuple[bool, str]":
    """
    Run pip for ``thePackage`` in this interpreter (blocking).

    :return: (success, combined stdout/stderr tail)
    """
    try:
        myResult = subprocess.run(
            pipInstallCommand(thePackage), capture_output=True, text=True, timeout=theTimeoutSec,
        )
    except (OSError, subprocess.TimeoutExpired) as e:
        return False, str(e)
    myOutput = (myResult.stdout or "") + (myResult.stderr or "")
    importlib.invalidate_caches()
    return myResult.returncode == 0, myOutput[-2000:]
