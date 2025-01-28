from qgis.PyQt.QtCore import QObject, pyqtSlot
from typing import Dict
from .la import La
from .ladietlabels import LaDietLabels

class LaGrass(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.diets = {}

    @pyqtSlot(str, result=La)
    def getDiet(self, guid: str) -> La:
        return self.diets.get(guid)

    @pyqtSlot(str, La)
    def addDiet(self, guid: str, diet: La):
        self.diets[guid] = diet

    @pyqtSlot(str)
    def removeDiet(self, guid: str):
        if guid in self.diets:
            del self.diets[guid]

    @pyqtSlot(result=dict)
    def getDiets(self) -> Dict[str, La]:
        return self.diets

    @pyqtSlot(str, LaDietLabels)
    def addDietLabel(self, guid: str, label: LaDietLabels):
        if guid in self.diets:
            self.diets[guid].addLabel(label)