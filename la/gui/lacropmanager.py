from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel
from qgis.PyQt.QtGui import QBrush, QColor, QPixmap, QIcon
from qgis.PyQt.QtWidgets import QLabel, QTableWidgetItem, QDialog, QHeaderView, QMessageBox

from la.lib.lacrop import LaCrop
from la.lib.lautils import LaUtils
from la.ui.lacropmanagerbase import LaCropManagerBase

class LaCropTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.crops = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.crops)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, theIndex, theRole=Qt.DisplayRole):
        if not theIndex.isValid():
            return None

        myRow = theIndex.row()
        myCol = theIndex.column()
        myCrop = self.crops[myRow]

        if theRole == Qt.DisplayRole:
            if myCol == 0:
                return myCrop.name
            elif myCol == 1:
                return myCrop.description
        elif theRole == Qt.BackgroundRole:
            if myRow % 2 == 0:
                return QBrush(QColor(240, 240, 240))
        elif theRole == Qt.TextAlignmentRole:
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

class LaCropManager(QDialog, LaCropManagerBase):
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
        self.crops = []

    def addCrop(self, name, description):
        crop = LaCrop(name, description)
        self.crops.append(crop)
        self.refreshCropTable()

    def removeCrop(self, index):
        del self.crops[index]
        self.refreshCropTable()

    def getCrop(self, index):
        return self.crops[index]

    def getCropCount(self):
        return len(self.crops)

    def refreshCropTable(self, theGuid=None):
        print("Refreshing crop table")
        self.mCropMap = LaUtils.getAvailableCrops()
        print(f"Available crops: {self.mCropMap}")

        self.tblCrops.clear()
        self.tblCrops.setRowCount(0)
        self.tblCrops.setColumnCount(2)

        mySelectedRow = 0
        myCurrentRow = 0
        for myCrop in self.mCropMap.values():
            print(f"Processing crop: {myCrop.name()} with GUID: {myCrop.guid()}")
            if theGuid is None:
                theGuid = myCrop.guid()
            if myCrop.guid() == theGuid:
                mySelectedRow = myCurrentRow

            self.tblCrops.insertRow(myCurrentRow)
            myGuid = myCrop.guid()

            mypFileNameItem = QTableWidgetItem(myGuid)
            self.tblCrops.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(myCrop.name())
            self.tblCrops.setItem(myCurrentRow, 1, mypNameItem)

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
        print("Crop table refreshed")

    def on_pbnCropPic_clicked(self):
        myUtils = LaUtils()
        myFile = myUtils.openGraphicFile()
        self.lblCropPix.setPixmap(QPixmap(myFile))
        self.mImageFile = myFile

    def cellClicked(self, row, column):
        print(f"Cell clicked at row: {row}, column: {column}")
        myGuid = self.tblCrops.item(row, 0).text()
        print(f"Guid is: {myGuid}")
        myFileName = f"{myGuid}.xml"
        self.selectCrop(myFileName)

    def selectCrop(self, theFileName):
        print(f"selectCrop Called: {theFileName}")
        myCropDir = LaUtils.userCropProfilesDirPath()
        myCrop = LaCrop()
        myCrop.fromXmlFile(os.path.join(myCropDir, theFileName))
        self.leName.setText(myCrop.name())
        self.mCrop = myCrop
        self.showCrop()

    def showCrop(self):
        self.leName.setText(self.mCrop.name())
        self.leDescription.setText(self.mCrop.description())
        self.sbCropYield.setValue(self.mCrop.cropYield())
        self.sbCropCalories.setValue(self.mCrop.cropCalories())
        self.sbCropFodderProduction.setValue(self.mCrop.fodderProduction())
        self.sbCropFodderValue.setValue(self.mCrop.fodderValue())
        self.cbAreaUnits.setCurrentIndex(self.mCrop.areaUnits())
        self.cbFodderEnergyType.setCurrentIndex(self.mCrop.cropFodderEnergyType())
        self.lblCropPix.setPixmap(self.mCrop.imageFile())

    def on_toolNew_clicked(self):
        print("New toolbutton clicked")
        myCrop = LaCrop()
        myCrop.setGuid()
        self.mCrop = myCrop
        self.showCrop()

    def on_toolCopy_clicked(self):
        print("Copy toolbutton clicked")
        if self.tblCrops.currentRow() < 0:
            return
        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if not myGuid:
            return
        myOriginalFileName = os.path.join(LaUtils.userCropProfilesDirPath(), f"{myGuid}.xml")
        myCrop = LaCrop()
        myCrop.fromXmlFile(myOriginalFileName)
        myCrop.setGuid()
        myNewFileName = os.path.join(LaUtils.userCropProfilesDirPath(), f"{myCrop.guid()}.xml")
        myCrop.setName(f"Copy of {myCrop.name()}")
        myCrop.toXmlFile(myNewFileName)
        self.refreshCropTable(myCrop.guid())

    def on_toolDelete_clicked(self):
        print("Delete toolbutton clicked")
        if self.tblCrops.currentRow() < 0:
            return
        myGuid = self.tblCrops.item(self.tblCrops.currentRow(), 0).text()
        if myGuid:
            myFile = os.path.join(LaUtils.userCropProfilesDirPath(), f"{myGuid}.xml")
            if not os.remove(myFile):
                QMessageBox.warning(self, "Landuse Analyst", f"Unable to delete file \n{myFile}")
            self.refreshCropTable()

    def on_pbnApply_clicked(self):
        self.mCrop.setName(self.leName.text())
        self.mCrop.setDescription(self.leDescription.text())
        self.mCrop.setCropYield(self.sbCropYield.value())
        self.mCrop.setCropCalories(self.sbCropCalories.value())
        self.mCrop.setFodderProduction(self.sbCropFodderProduction.value())
        self.mCrop.setCropFodderValue(self.sbCropFodderValue.value())
        self.mCrop.setAreaUnits(self.cbAreaUnits.currentIndex())
        self.mCrop.setCropFodderEnergyType(self.cbFodderEnergyType.currentIndex())
        self.mCrop.setImageFile(self.mImageFile)
        self.mCrop.toXmlFile(os.path.join(LaUtils.userCropProfilesDirPath(), f"{self.mCrop.guid()}.xml"))
        self.refreshCropTable(self.mCrop.guid())


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