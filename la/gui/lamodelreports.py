"""
lamodelreports.py - Contains the LaModelReport and LaModelReportTableModel classes.

Author: [Your Name]
Date created: [DD/MM/YYYY]
Python Version: [X.Y.Z]
PyQt5 Version: [X.Y.Z]

Description: This file contains the LaModelReport and LaModelReportTableModel
             classes, and are used to manage and display reports in the Landuse
             Analyst plugin for QGIS.

Classes:
- LaModelReport: Represents a single report, with a name and description.
- LaModelReportTableModel: A table model used to display a list of LaModelReport objects.

Usage: This file is used by other modules in the Land Use Analyst plugin to manage and display reports.

Notes: This file requires PyQt5 to be installed.

Issues: None known.

License: [Your license information (if applicable)]
"""


from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt5.QtGui import QBrush, QColor

from la.lib.lamodel import LaModel
from la.gui.lamainform import LaMainForm


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


class LaModelReport:
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
