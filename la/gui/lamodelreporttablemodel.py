from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor

# from la.lib.lamodel import LaModel
# from la.gui.lamodelreport import LaModelReport

class LaModelReportTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reports = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.reports)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        report = self.reports[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return report.name
            elif col == 1:
                return report.description
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

    def addReport(self, report):
        self.beginInsertRows(QModelIndex(), len(self.reports), len(self.reports))
        self.reports.append(report)
        self.endInsertRows()

    def removeReport(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.reports[index]
        self.endRemoveRows()

    def getReport(self, index):
        return self.reports[index]
