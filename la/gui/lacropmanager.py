from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor, QPixmap
from qgis.PyQt.QtWidgets import QLabel

from la.lib.lacrop import LaCrop
from la.lib.lautils import LaUtils

class LaCropTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lblCropPix = QLabel(self)
        self.mImageFile = None
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
                return crop.name
            elif col == 1:
                return crop.description
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

     

class LaCropManager:
    def __init__(self, parent=None):
        self.crops = []
        self.parent = parent

    def addCrop(self, name, description):
        crop = LaCrop(name, description)
        self.crops.append(crop)

    def removeCrop(self, index):
        del self.crops[index]

    def getCrop(self, index):
        return self.crops[index]

    def getCropCount(self):
        return len(self.crops)

    def getCropTableModel(self):
        return LaCropTableModel(self.parent)
    
    def on_pbnCropPic_clicked(self):
        myUtils = LaUtils()
        myFile = myUtils.openGraphicFile()
        self.lblCropPix.setPixmap(QPixmap(myFile))
        self.mImageFile = myFile  

"""

LaCropManager class is rewritten in Python using PyQt5.

The LaCropTableModel class is also included as a subclass of QAbstractTableModel
    which provides the model for the crop table view.

The LaCropTableModel class defines the necessary methods for a table model,
    including rowCount, columnCount, data, headerData, addCrop, removeCrop,
    and getCrop.

    These methods are used to populate the crop table view with data and manage
    the crop data.

The LaCropManager class defines the necessary methods for managing the crop data
    including addCrop, removeCrop, getCrop, getCropCount, and getCropTableModel.

    These methods are used to add, remove, and retrieve crop data from the crops
    list, as well as to retrieve the crop table model.

"""