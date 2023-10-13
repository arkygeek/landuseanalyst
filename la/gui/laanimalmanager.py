from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor

from la.lib.laanimal import LaAnimal


class LaAnimalTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animals = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.animals)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        animal = self.animals[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return animal.name
            elif col == 1:
                return animal.species
        elif role == Qt.BackgroundRole:
            if row % 2 == 0:
                return QBrush(QColor(240, 240, 240))
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "Name"
                elif section == 1:
                    return "Species"
            elif orientation == Qt.Vertical:
                return str(section + 1)

        return None

    def addAnimal(self, animal):
        self.beginInsertRows(QModelIndex(), len(self.animals), len(self.animals))
        self.animals.append(animal)
        self.endInsertRows()

    def removeAnimal(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.animals[index]
        self.endRemoveRows()

    def getAnimal(self, index):
        return self.animals[index]


class LaAnimalManager:
    def __init__(self):
        self.animals = []

    def addAnimal(self, name, species):
        animal = LaAnimal(name, species)
        self.animals.append(animal)

    def removeAnimal(self, index):
        del self.animals[index]

    def getAnimal(self, index):
        return self.animals[index]

    def getAnimalCount(self):
        return len(self.animals)

"""

LaAnimalManager class is rewritten in Python using PyQt5.

The LaAnimalTableModel class is also included as a subclass of
    QAbstractTableModel, which provides the model for the animal table view.

The LaAnimalTableModel class defines the necessary methods for a table model,
    including rowCount, columnCount, data, headerData, addAnimal, removeAnimal,
    and getAnimal. These methods are used to populate the animal table view with
    data and manage the animal data.

LaAnimalManager class defines the necessary methods for managing the animal data
    including addAnimal, removeAnimal, getAnimal, and getAnimalCount. These
    methods are used to add, remove, and retrieve data from the animals list.

"""