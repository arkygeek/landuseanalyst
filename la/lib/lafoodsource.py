from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal

class LaFoodSource(QObject):
    """ This class defines a LaFoodSource object """

    grainChanged = pyqtSignal(int)
    fodderChanged = pyqtSignal(int)
    daysChanged = pyqtSignal(int)
    usedChanged = pyqtSignal(bool)
    cropGuidChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._grain = 0
        self._fodder = 0
        self._days = 0
        self._used = False
        self._cropGuid = ""

    @pyqtProperty(int, notify=grainChanged)
    def grain(self):
        return self._grain

    @grain.setter
    def grain(self, value):
        if self._grain != value:
            self._grain = value
            self.grainChanged.emit(value)

    @pyqtProperty(int, notify=fodderChanged)
    def fodder(self):
        return self._fodder

    @fodder.setter
    def fodder(self, value):
        if self._fodder != value:
            self._fodder = value
            self.fodderChanged.emit(value)

    @pyqtProperty(int, notify=daysChanged)
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        if self._days != value:
            self._days = value
            self.daysChanged.emit(value)

    @pyqtProperty(bool, notify=usedChanged)
    def used(self):
        return self._used

    @used.setter
    def used(self, value):
        if self._used != value:
            self._used = value
            self.usedChanged.emit(value)

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self):
        return self._cropGuid

    @cropGuid.setter
    def cropGuid(self, value):
        if self._cropGuid != value:
            self._cropGuid = value
            self.cropGuidChanged.emit(value)