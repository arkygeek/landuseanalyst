from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel, QDir, QPoint, QSize, QSettings
from qgis.PyQt.QtGui import QBrush, QColor, QIcon
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QHeaderView, QFileDialog, QTableWidgetItem, QApplication

# Import only the base class from UI
from la.ui.lacropparametermanagerbase import LaCropParameterManagerBase

from la.lib.lacropparameter import LaCropParameter
from la.lib.lautils import LaUtils
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits
from la.lib.lagrass import LaGrass
import os

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


class LaCropParameterManager(LaCropParameterManagerBase):
    """
    Manager for crop parameters.

    This class provides the functionality for managing crop parameters, including
    creating, editing, copying, and deleting crop parameters.
    """

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        """
        Initializes a new instance of the LaCropParameterManager class.

        Args:
            parent: The parent widget.
            flags: Window flags.
        """
        super(LaCropParameterManager, self).__init__(parent, flags)
        self.readSettings()
        self.tblCropParameterProfiles.cellClicked.connect(self.cellClicked)
        myList = []
        myGrass = LaGrass()
        myMapsetList = ""  # myGrass.getMapsetList() @TODO get Grass stuff working

        # Set up the raster combo box
        self.cboRaster.addItems(myList)
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)
        self.lblCropPic.setScaledContents(True)

        self.mCropParameterMap = {}  # Add dictionary to store crop parameters
        self.mCropParameter = None  # Initialize to avoid attribute errors

        # Set up the crops combobox
        myCropsMap = LaUtils.getAvailableCrops()

        for cropGuid, myCrop in myCropsMap.items():
            myGuid = myCrop.guid
            myName = myCrop.name
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            self.cboCrop.addItem(myName, myGuid)

        self.cboCrop.currentIndexChanged.connect(self.on_cboCrop_changed)
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")

        # Connect signals
        self.toolNew.clicked.connect(self.on_toolNew_clicked)
        self.toolCopy.clicked.connect(self.on_toolCopy_clicked)
        self.toolDelete.clicked.connect(self.on_toolDelete_clicked)
        self.pbnApply.clicked.connect(self.on_pbnApply_clicked)

        # Initialize the table
        self.refreshCropParameterTable()

    def readSettings(self):
        """
        Reads the settings of the main window's position and size from QSettings
        and sets the position and size of the current window accordingly.
        """
        mySettings = QSettings()
        pos = mySettings.value("mainwindow/pos", QPoint(200, 200))
        size = mySettings.value("mainwindow/size", QSize(400, 400))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        """Save window position and size to settings"""
        mySettings = QSettings()
        mySettings.setValue("mainwindow/pos", self.pos())
        mySettings.setValue("mainwindow/size", self.size())

    def cellClicked(self, theRow, theColumn):
        """Handle cell click in the table"""
        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        myFileName = myGuid + ".xml"
        self.selectCropParameter(myFileName)
        myCrop = LaUtils.getCrop(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole))
        myAnimalPic = myCrop.imageFile()
        self.lblCropPic.setPixmap(myAnimalPic)

    def on_cboCrop_changed(self, theIndex):
        """Handle change in crop selection"""
        myCrop = LaUtils.getCrop(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole))
        myCropPic = myCrop.imageFile
        self.lblCropPic.setPixmap(myCropPic)

    def showCropParameter(self):
        """Display crop parameter in the form"""
        if not self.mCropParameter:
            return

        self.leName.setText(self.mCropParameter.name)
        self.leDescription.setText(self.mCropParameter.description)
        self.setComboToDefault(self.cboCrop, self.mCropParameter.cropGuid)

        # Handle numeric values with proper type conversion
        try:
            # Check if these are QDoubleSpinBox or QSpinBox widgets
            if hasattr(self.sbPercentTameCrop, 'decimals'):  # It's a QDoubleSpinBox
                self.sbPercentTameCrop.setValue(self.mCropParameter.percentTameCrop)
                self.sbSpoilage.setValue(self.mCropParameter.spoilage)
                self.sbReseed.setValue(self.mCropParameter.reseed)
                self.sbFallowRatio.setValue(self.mCropParameter.fallowRatio)
            else:  # It's a QSpinBox
                self.sbPercentTameCrop.setValue(self.mCropParameter.percentTameCrop)
                self.sbSpoilage.setValue(self.mCropParameter.spoilage)
                self.sbReseed.setValue(self.mCropParameter.reseed)
                self.sbFallowRatio.setValue(self.mCropParameter.fallowRatio)

            # FallowValue should be an integer
            self.sbFallowValue.setValue(self.mCropParameter.fallowValue)
        except (ValueError, TypeError) as e:
            print(f"Error converting values in showCropParameter: {e}")

        # Boolean values
        self.grpCropRotation.setChecked(bool(self.mCropParameter.cropRotation))
        self.checkBoxUseCommonLand.setChecked(bool(self.mCropParameter.useCommonLand))
        self.checkBoxUseSpecificLand.setChecked(bool(self.mCropParameter.useSpecificLand))

        # Area units
        try:
            self.cbAreaUnits.setCurrentIndex(self.mCropParameter.areaUnits)
        except (ValueError, TypeError) as e:
            print(f"Error setting area units: {e}")

    def resizeEvent(self, theEvent):
        """Handle resize event to adjust table columns"""
        self.tblCropParameterProfiles.setColumnWidth(0, 0)
        self.tblCropParameterProfiles.setColumnWidth(1, self.tblCropParameterProfiles.width())
        self.tblCropParameterProfiles.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def refreshCropParameterTable(self, theGuid=None):
        """
        Refreshes the crop parameter table with all available crop parameters.

        Args:
            theGuid (str, optional): The GUID of the crop parameter to select. If None,
                                     the first crop parameter will be selected.
        """
        # Clear everything
        self.mCropParameterMap = {}
        self.tblCropParameterProfiles.clear()
        self.tblCropParameterProfiles.setRowCount(0)
        self.tblCropParameterProfiles.setColumnCount(2)

        # Get available crop parameters
        self.mCropParameterMap = LaUtils.getAvailableCropParameters()

        # Populate the table
        mySelectedRow = 0
        myCurrentRow = 0
        for myGuid, myCropParameter in self.mCropParameterMap.items():
            if theGuid is None and myCurrentRow == 0:  # Default to first item if no GUID specified
                theGuid = myCropParameter.guid

            if myCropParameter.guid == theGuid:
                mySelectedRow = myCurrentRow

            self.tblCropParameterProfiles.insertRow(myCurrentRow)
            mypFileNameItem = QTableWidgetItem(myGuid)
            self.tblCropParameterProfiles.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(myCropParameter.name + "  (" + myCropParameter.description + ")")
            self.tblCropParameterProfiles.setItem(myCurrentRow, 1, mypNameItem)

            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            mypNameItem.setIcon(myIcon)

            myCurrentRow += 1

        if myCurrentRow > 0:
            self.tblCropParameterProfiles.setCurrentCell(mySelectedRow, 1)
            self.cellClicked(mySelectedRow, 1)
        else:
            self.on_toolNew_clicked()

        headerLabels = ["File Name", "Name"]
        self.tblCropParameterProfiles.setHorizontalHeaderLabels(headerLabels)
        self.tblCropParameterProfiles.setColumnWidth(0, 0)
        self.tblCropParameterProfiles.setColumnWidth(1, self.tblCropParameterProfiles.width())
        self.tblCropParameterProfiles.horizontalHeader().hide()
        self.tblCropParameterProfiles.verticalHeader().hide()
        self.tblCropParameterProfiles.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def selectCropParameter(self, theFileName):
        """Load a crop parameter from a file"""
        myCropParameterDir = LaUtils.userCropParameterProfilesDirPath()
        myCropParameter = LaCropParameter()
        myCropParameter.fromXmlFile(myCropParameterDir + QDir.separator() + theFileName)
        self.leName.setText(myCropParameter.name)
        self.mCropParameter = myCropParameter
        self.showCropParameter()

    def on_toolNew_clicked(self):
        """Create a new crop parameter"""
        myCropParameter = LaCropParameter()
        myCropParameter.setGuid()
        self.mCropParameter = myCropParameter
        self.showCropParameter()

    def on_toolCopy_clicked(self):
        """Copy the selected crop parameter"""
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if not myGuid:
            return

        myOriginalFileName = LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myGuid + ".xml"
        myCropParameter = LaCropParameter()
        myCropParameter.fromXmlFile(myOriginalFileName)
        myCropParameter.setGuid()
        myNewFileName = LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myCropParameter.guid + ".xml"
        myCropParameter.name = "Copy of " + myCropParameter.name
        myCropParameter.toXmlFile(myNewFileName)
        self.refreshCropParameterTable(myCropParameter.guid)

    def on_toolDelete_clicked(self):
        """Delete the selected crop parameter"""
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if myGuid:
            from qgis.PyQt.QtCore import QFile
            myFile = QFile(LaUtils.userCropParameterProfilesDirPath() + QDir.separator() + myGuid + ".xml")
            if not myFile.remove():
                QMessageBox.warning(self, "Landuse Analyst", "Unable to delete file: " + myFile.fileName())
            self.refreshCropParameterTable()

    def on_pbnApply_clicked(self):
        """Apply changes to the crop parameter"""
        if not self.mCropParameter:
            return

        self.mCropParameter.name = self.leName.text()
        self.mCropParameter.description = self.leDescription.text()
        self.mCropParameter.cropGuid = self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole)

        # Handle numeric values with proper type conversion
        try:
            # Always store as float in the model, regardless of widget type
            self.mCropParameter.percentTameCrop = float(self.sbPercentTameCrop.value())
            self.mCropParameter.spoilage = float(self.sbSpoilage.value())
            self.mCropParameter.reseed = float(self.sbReseed.value())
            self.mCropParameter.fallowRatio = float(self.sbFallowRatio.value())
            self.mCropParameter.fallowValue = int(self.sbFallowValue.value())
        except (ValueError, TypeError) as e:
            print(f"Error converting values in on_pbnApply_clicked: {e}")

        # Boolean values
        self.mCropParameter.cropRotation = self.grpCropRotation.isChecked()
        self.mCropParameter.useCommonLand = self.checkBoxUseCommonLand.isChecked()
        self.mCropParameter.useSpecificLand = self.checkBoxUseSpecificLand.isChecked()

        # Handle area units
        mySelectedAreaUnit = self.cbAreaUnits.currentText()
        from la.lib.la import AreaUnits
        if mySelectedAreaUnit == "Dunum":
            self.mCropParameter.areaUnits = AreaUnits.Dunum
        elif mySelectedAreaUnit == "Hectare":
            self.mCropParameter.areaUnits = AreaUnits.Hectare

        self.mCropParameter.rasterName = self.cboRaster.currentText()
        self.mCropParameter.toXmlFile(LaUtils.userCropParameterProfilesDirPath() + QDir.separator() +
                                     self.mCropParameter.guid + ".xml")
        self.refreshCropParameterTable(self.mCropParameter.guid)

    def setComboToDefault(self, thepCombo, theDefault):
        """
        Sets a combo box to the item with the given default value.

        Args:
            thepCombo (QComboBox): The combo box to set.
            theDefault: The default value to set the combo box to.

        Returns:
            bool: True if successful, False otherwise.
        """
        if not theDefault:
            return False

        for myCounter in range(thepCombo.count()):
            thepCombo.setCurrentIndex(myCounter)
            if thepCombo.itemData(myCounter, Qt.UserRole) == theDefault:
                return True

        return False