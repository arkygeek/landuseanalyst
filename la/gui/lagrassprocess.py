from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class LaGrassProcess(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.process = None

    @pyqtSlot()
    def start(self):
        pass

    @pyqtSlot()
    def cancel(self):
        pass

    def setProcess(self, process):
        self.process = process

    def getProcess(self):
        return self.process

"""

LaGrassProcess class is rewritten in Python using PyQt5.

The finished and progress signals are defined using the pyqtSignal decorator.

The start and cancel methods are defined using the pyqtSlot decorator, which
    allows them to be connected to signals.

The setProcess and getProcess methods are used to set and retrieve the Grass
    process associated with the LaGrassProcess object.

"""