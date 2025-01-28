from qgis.PyQt.QtCore import QObject, pyqtSlot
from typing import Dict, List, Tuple
from .la import La
from .ladietlabels import LaDietLabels

class LaModelInterface(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.diets = {}

    @pyqtSlot(str, str)
    def setName(self, guid: str, name: str):
        if guid in self.diets:
            self.diets[guid].setName(name)

    @pyqtSlot(str, str)
    def setDescription(self, guid: str, description: str):
        if guid in self.diets:
            self.diets[guid].setDescription(description)

    @pyqtSlot(str, result=dict)
    def getDiet(self, guid: str) -> dict:
        if guid in self.diets:
            diet = self.diets[guid]
            return {
                'guid': diet.guid(),
                'name': diet.name(),
                'description': diet.description(),
                # Add other relevant fields here
            }
        return {}

    @pyqtSlot(result=dict)
    def getDiets(self) -> Dict[str, dict]:
        return {guid: self.getDiet(guid) for guid in self.diets}

    @pyqtSlot(str, La)
    def addDiet(self, guid: str, diet: La):
        self.diets[guid] = diet

    @pyqtSlot(str)
    def removeDiet(self, guid: str):
        if guid in self.diets:
            del self.diets[guid]

    @pyqtSlot(str, LaDietLabels)
    def addDietLabel(self, guid: str, label: LaDietLabels):
        if guid in self.diets:
            self.diets[guid].addLabel(label)