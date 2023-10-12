"""
LaCropManager.py - A Python implementation of the LaCropManager class using PyQt5.

This file contains the LaCropManager class, which is a Python implementation of the
LaCropManager class from the original C++ code. The class is rewritten in Python using
PyQt5, and includes the LaCropTableModel and LaCropManagerWidget classes as subclasses
of QAbstractTableModel and QWidget, respectively.

The LaCropTableModel class defines the necessary methods for a table model, including
rowCount, columnCount, data, headerData, addCrop, removeCrop, and getCrop. These methods
are used to populate the crop table view with data and manage the crop data.

The LaCropManagerWidget class defines the necessary methods for managing crop data,
including addCrop and removeCrop. These methods are used to add and remove crop data
from the cropManager and cropTableModel.

The LaCropManager class defines the necessary methods for managing the crop data,
including crops, addCrop, and removeCrop. These methods retrieve, add, and remove crop
data from the mCrops list.

Author: [Jason Jorgenson]
Date created: [10-OCT-2023]
"""

from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableView, QPushButton, QGroupBox, QLabel, QLineEdit

from la.lib import  LaCrop, LaCropType, LaCropManager


class LaCropTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.crops = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.crops)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        crop = self.crops[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return crop.name()
            elif col == 1:
                return crop.type().name()
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
                    return "Type"
            elif orientation == Qt.Vertical:
                return str(section + 1)

        return None

    def addCrop(self, crop):
        self.beginInsertRows(QModelIndex(), len(self.crops), len(self.crops))
        self.crops.append(crop)
        self.endInsertRows()

    def removeCrop(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.crops[index]
        self.endRemoveRows()

    def getCrop(self, index):
        return self.crops[index]


class LaCropManagerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the crop manager.
        self.cropManager = LaCropManager()

        # Set up the crop table model.
        self.cropTableModel = LaCropTableModel(self)
        self.cropTableModel.crops = self.cropManager.crops()

        # Set up the crop table view.
        self.cropTableView = QTableView(self)
        self.cropTableView.setModel(self.cropTableModel)
        self.cropTableView.setSelectionBehavior(QTableView.SelectRows)
        self.cropTableView.setSelectionMode(QTableView.SingleSelection)
        self.cropTableView.verticalHeader().setVisible(False)
        self.cropTableView.horizontalHeader().setStretchLastSection(True)

        # Set up the add crop button.
        self.addCropButton = QPushButton("Add Crop", self)
        self.addCropButton.clicked.connect(self.addCrop)

        # Set up the remove crop button.
        self.removeCropButton = QPushButton("Remove Crop", self)
        self.removeCropButton.clicked.connect(self.removeCrop)

        # Set up the crop name label.
        self.cropNameLabel = QLabel("Name:", self)

        # Set up the crop name line edit.
        self.cropNameLineEdit = QLineEdit(self)

        # Set up the crop type label.
        self.cropTypeLabel = QLabel("Type:", self)

        # Set up the crop type line edit.
        self.cropTypeLineEdit = QLineEdit(self)

        # Set up the crop type group box.
        self.cropTypeGroupBox = QGroupBox("Crop Type", self)
        self.cropTypeGroupBoxLayout = QVBoxLayout(self.cropTypeGroupBox)
        self.cropTypeGroupBoxLayout.addWidget(self.cropNameLabel)
        self.cropTypeGroupBoxLayout.addWidget(self.cropNameLineEdit)
        self.cropTypeGroupBoxLayout.addWidget(self.cropTypeLabel)
        self.cropTypeGroupBoxLayout.addWidget(self.cropTypeLineEdit)

        # Set up the main layout.
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.cropTableView)
        self.mainLayout.addWidget(self.cropTypeGroupBox)
        self.mainLayout.addWidget(self.addCropButton)
        self.mainLayout.addWidget(self.removeCropButton)

    def addCrop(self):
        name = self.cropNameLineEdit.text()
        typeName = self.cropTypeLineEdit.text()
        cropType = LaCropType(typeName)
        crop = LaCrop(name, cropType)
        self.cropManager.addCrop(crop)
        self.cropTableModel.addCrop(crop)

    def removeCrop(self):
        index = self.cropTableView.currentIndex().row()
        crop = self.cropTableModel.getCrop(index)
        self.cropManager.removeCrop(crop)
        self.cropTableModel.removeCrop(index)


class LaCropManager:
    def __init__(self):
        self.mCrops = []

    def __del__(self):
        pass

    def crops(self):
        return self.mCrops

    def addCrop(self, crop):
        self.mCrops.append(crop)

    def removeCrop(self, crop):
        self.mCrops.remove(crop)
