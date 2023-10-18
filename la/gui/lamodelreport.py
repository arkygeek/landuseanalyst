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


from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor

# from la.gui.lamainform import LaMainForm
from lib.lamodel import LaModel
from gui.lamodelreporttablemodel import LaModelReportTableModel



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
