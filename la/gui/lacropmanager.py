from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor, QPixmap, QIcon
from qgis.PyQt.QtWidgets import QLabel, QTableWidgetItem, QDialog

from la.lib.lacrop import LaCrop
from la.lib.lautils import LaUtils

class LaCropTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lblCropPix = QLabel()
        self.mImageFile = None
        self.crops = []
        self.tblCrops = []

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

class LaCropManager(QDialog):
    def __init__(self, parent=None, fl=Qt.WindowFlags()):
        super().__init__(parent, fl)
        self.setupUi(self)
        self.readSettings()
        self.lblCropPix.setScaledContents(True)
        self.tblCrops.cellClicked.connect(self.cellClicked)
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.cbFodderEnergyType.addItem("KCalories")
        self.cbFodderEnergyType.addItem("TDN")
        self.refreshCropTable()
        self.pbnImport.setVisible(True)
        self.pbnExport.setVisible(True)


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

    def refreshCropTable(self, theGuid=None):
        self.mCropMap.clear()
        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(2)

        # we do this in two passes
        # in the first pass we populate a qmap with all the layersets
        # we find....
        self.mCropMap = LaUtils.getAvailableCrops()

        # the second pass populates the table
        # doing it from the map ensures that the rows
        # are sorted by layerset name

        mySelectedRow = 0
        myCurrentRow = 0
        for myCrop in self.mCropMap.values():
            if theGuid is None:
                theGuid = myCrop.guid()
            if myCrop.guid() == theGuid:
                mySelectedRow = myCurrentRow

            # Insert new row ready to fill with details
            self.tblCrops.insertRow(myCurrentRow)
            myGuid = myCrop.guid()

            # Add details to the new row
            mypFileNameItem = QTableWidgetItem(myGuid)
            self.tblCrops.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(myCrop.name())
            self.tblCrops.setItem(myCurrentRow, 1, mypNameItem)

            # display an icon indicating if the layerset is local or remote (e.g. terralib)
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            mypNameItem.setIcon(myIcon)

            myCurrentRow += 1

        if myCurrentRow > 0:
            self.tblCrops.setCurrentCell(mySelectedRow, 1)
            self.cellClicked(mySelectedRow, 1)
        else:
            self.on_toolNew_clicked()

        headerLabels = ["File Name", "Name"]
        self.tblCrops.setHorizontalHeaderLabels(headerLabels)
        self.tblCrops.setColumnWidth(0, 0)
        self.tblCrops.setColumnWidth(1, self.tblCrops.width())
        self.tblCrops.horizontalHeader().hide()
        self.tblCrops.verticalHeader().hide()
        self.tblCrops.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
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