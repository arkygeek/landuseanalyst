from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt5.QtGui import QBrush, QColor

from ..lib.la import LaAssemblage


class LaAssemblageTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.assemblages = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.assemblages)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        assemblage = self.assemblages[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return assemblage.name
            elif col == 1:
                return assemblage.description
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
                    return "Description"
            elif orientation == Qt.Vertical:
                return str(section + 1)

        return None

    def addAssemblage(self, assemblage):
        self.beginInsertRows(QModelIndex(), len(self.assemblages), len(self.assemblages))
        self.assemblages.append(assemblage)
        self.endInsertRows()

    def removeAssemblage(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.assemblages[index]
        self.endRemoveRows()

    def getAssemblage(self, index):
        return self.assemblages[index]


class LaAssemblageConversion:
    def __init__(self):
        self.assemblages = []

    def addAssemblage(self, name, description):
        assemblage = LaAssemblage(name, description)
        self.assemblages.append(assemblage)

    def removeAssemblage(self, index):
        del self.assemblages[index]

    def getAssemblage(self, index):
        return self.assemblages[index]

    def getAssemblageCount(self):
        return len(self.assemblages)

"""

LaAssemblageConversion class is rewritten in Python using PyQt5.

The LaAssemblageTableModel class is also included as a subclass of
    QAbstractTableModel, which provides the model for the assemblage table view.

LaAssemblageTableModel class defines the necessary methods for a table model,
    including rowCount, columnCount, data, headerData, addAssemblage,
    removeAssemblage, and getAssemblage. These methods are used to populate the
    assemblage table view with data and manage the assemblage data.

The LaAssemblageConversion class defines the necessary methods for managing the
    assemblage data, including addAssemblage, removeAssemblage, getAssemblage,
    and getAssemblageCount.

    These methods are used to add, remove, and retrieve assemblage data from the
    assemblages list.

"""