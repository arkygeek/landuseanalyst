"""
lacatalogue.py — in-memory view of the crop / animal profile catalogue.

Wraps the cached loaders on :class:`la.lib.lautils.LaUtils` and watches the
profile directories so the UI can refresh itself when an editor dialog (or
the user, on disk) adds or changes a profile.
"""

import os
from typing import Dict, Optional

from qgis.PyQt.QtCore import QFileSystemWatcher, QObject, QTimer, pyqtSignal

from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.lautils import LaUtils


class LaCatalogue(QObject):
    """
    Read-only catalogue of crops, animals and their parameter sets.

    :signal changed: Emitted (debounced) after any watched profile directory
        changes on disk.
    """

    changed = pyqtSignal()

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._mWatcher = QFileSystemWatcher(self)
        self._mDebounce = QTimer(self)
        self._mDebounce.setSingleShot(True)
        self._mDebounce.setInterval(400)
        self._mDebounce.timeout.connect(self._onDirectoriesChanged)
        self._mWatcher.directoryChanged.connect(lambda _path: self._mDebounce.start())
        self.watchDirectories()

    # ------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------
    @staticmethod
    def profileDirectories() -> Dict[str, str]:
        """Kind → absolute directory for the four profile folders."""
        return {
            "crops": LaUtils.userCropProfilesDirPath(),
            "animals": LaUtils.userAnimalProfilesDirPath(),
            "cropParameters": LaUtils.userCropParameterProfilesDirPath(),
            "animalParameters": LaUtils.userAnimalParameterProfilesDirPath(),
        }

    def watchDirectories(self) -> None:
        """(Re)register the profile directories with the file-system watcher."""
        myExisting = self._mWatcher.directories()
        if myExisting:
            self._mWatcher.removePaths(myExisting)
        myPaths = [p for p in self.profileDirectories().values() if os.path.isdir(p)]
        if myPaths:
            self._mWatcher.addPaths(myPaths)

    def _onDirectoriesChanged(self) -> None:
        LaUtils.invalidateProfileCache()
        self.changed.emit()

    def refresh(self) -> None:
        """Force a reload on the next access and notify listeners."""
        self._onDirectoriesChanged()

    # ------------------------------------------------------------------
    # Lookups (always fresh objects, served from the text cache)
    # ------------------------------------------------------------------
    def crops(self) -> Dict[str, LaCrop]:
        return LaUtils.getAvailableCrops()

    def animals(self) -> Dict[str, LaAnimal]:
        return LaUtils.getAvailableAnimals()

    def cropParameters(self) -> Dict[str, LaCropParameter]:
        return LaUtils.getAvailableCropParameters()

    def animalParameters(self) -> Dict[str, LaAnimalParameter]:
        return LaUtils.getAvailableAnimalParameters()

    def crop(self, theGuid: str) -> LaCrop:
        return LaUtils.getCrop(theGuid)

    def animal(self, theGuid: str) -> LaAnimal:
        return LaUtils.getAnimal(theGuid)

    def cropParameter(self, theGuid: str) -> LaCropParameter:
        return LaUtils.getCropParameter(theGuid)

    def animalParameter(self, theGuid: str) -> LaAnimalParameter:
        return LaUtils.getAnimalParameter(theGuid)

    def cropParametersFor(self, theCropGuid: str) -> Dict[str, LaCropParameter]:
        """Parameter sets whose ``cropGuid`` is ``theCropGuid``."""
        return {
            g: p for g, p in self.cropParameters().items()
            if str(getattr(p, "cropGuid", "")) == str(theCropGuid)
        }

    def animalParametersFor(self, theAnimalGuid: str) -> Dict[str, LaAnimalParameter]:
        """Parameter sets whose ``animalGuid`` is ``theAnimalGuid``."""
        return {
            g: p for g, p in self.animalParameters().items()
            if str(getattr(p, "animalGuid", "")) == str(theAnimalGuid)
        }

    @staticmethod
    def imagePath(theImageFile: str) -> Optional[str]:
        """Absolute path of a profile thumbnail, or None when it does not exist."""
        if not theImageFile:
            return None
        if os.path.isabs(theImageFile) and os.path.exists(theImageFile):
            return theImageFile
        myPath = os.path.join(LaUtils.userImagesDirPath(), os.path.basename(str(theImageFile)))
        return myPath if os.path.exists(myPath) else None
