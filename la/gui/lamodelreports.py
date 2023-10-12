from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt5.QtGui import QBrush, QColor

from lib.la import 


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


class LaModelReports:
    def __init__(self):
        self.reports = []

    def addReport(self, name, description):
        report = LaModelReport(name, description)
        self.reports.append(report)

    def removeReport(self, index):
        del self.reports[index]

    def getReport(self, index):
        return self.reports[index]

    def getReportCount(self):
        return len(self.reports)

    def getReportTableModel(self):
        return LaModelReportTableModel()

"""

LaModelReports class is rewritten in Python using PyQt5.

The LaModelReportTableModel class is also included as a subclass of
    QAbstractTableModel that provides the model for the model report table view.

LaModelReportTableModel class defines the necessary methods for a table model,
    including rowCount, columnCount, data, headerData, addReport, removeReport,
    and getReport.

    These methods are used to populate the model report table view with data and
    manage the model report data.

The LaModelReports class defines the necessary methods for managing the model
    report data, including addReport, removeReport, getReport, getReportCount,
    and getReportTableModel.

    These methods are used to add, remove, and retrieve model report data from
    the reports list, as well as to retrieve the model report table model.

"""