from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor

from la.lib.lacropparameter import LaCropParameter


class LaCropParameterTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parameters = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.parameters)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        parameter = self.parameters[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return parameter.name
            elif col == 1:
                return parameter.description
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

    def addParameter(self, parameter):
        self.beginInsertRows(QModelIndex(), len(self.parameters), len(self.parameters))
        self.parameters.append(parameter)
        self.endInsertRows()

    def removeParameter(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.parameters[index]
        self.endRemoveRows()

    def getParameter(self, index):
        return self.parameters[index]


class LaCropParameterManager:
    def __init__(self):
        self.parameters = []

    def addParameter(self, name, description):
        parameter = LaCropParameter(name, description)
        self.parameters.append(parameter)

    def removeParameter(self, index):
        del self.parameters[index]

    def getParameter(self, index):
        return self.parameters[index]

    def getParameterCount(self):
        return len(self.parameters)

    def getParameterTableModel(self):
        return LaCropParameterTableModel()

"""

LaCropParameterManager class is rewritten in Python using PyQt5.

The LaCropParameterTableModel class is also included as a subclass of
    QAbstractTableModel, which provides the model for crop parameter table view.

The LaCropParameterTableModel class defines the necessary methods for a table
    model, including rowCount, columnCount, data, headerData, addParameter,
    removeParameter, and getParameter.

    These methods are used to populate the crop parameter table view with data
    and manage the crop parameter data.

The LaCropParameterManager class defines the necessary methods for managing the
    crop parameter data, including addParameter, removeParameter, getParameter,
    getParameterCount, and getParameterTableModel.

    These methods are used to add, remove, and retrieve crop parameter data from
    the parameters list, as well as to retrieve the crop parameter table model.

"""