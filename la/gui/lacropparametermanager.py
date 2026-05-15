from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel, QDir, QPoint, QSize, QSettings
from qgis.PyQt.QtGui import QBrush, QColor, QIcon, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QHeaderView, QFileDialog, QTableWidgetItem, QApplication

# Import only the base class from UI
from la.ui.lacropparametermanagerbase import LaCropParameterManagerBase

from la.lib.lacropparameter import LaCropParameter
from la.lib.lautils import LaUtils
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits, EnergyType as LaEnergyType
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
        """Initialize the crop parameter manager."""
        super(LaCropParameterManager, self).__init__(parent, flags)
        self.readSettings()
        self.tblCropParameterProfiles.cellClicked.connect(self.cellClicked)
        # Promote cboRaster from a plain QComboBox to a QgsMapLayerComboBox
        # so users can pick a loaded raster layer as the suitability surface
        # for this crop parameter. See _upgradeRasterCombo for details.
        self._upgradeRasterCombo()
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
        
        # Initialize the fallow energy type combo box
        self.cbFallowEnergyType.clear()
        self.cbFallowEnergyType.addItem("KCalories", LaEnergyType.KCalories)
        self.cbFallowEnergyType.addItem("TDN", LaEnergyType.TDN)
        
        # Connect the combo box changed signal
        self.cbFallowEnergyType.currentIndexChanged.connect(self.on_cbFallowEnergyType_changed)

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
        self.updateCropPicture()

    def updateCropPicture(self):
        """Update the crop picture based on the selected crop"""
        if self.cboCrop.currentIndex() >= 0:
            myCrop = LaUtils.getCrop(self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole))
            if myCrop and myCrop.imageFile:
                # Resolve the image path
                imagePath = LaUtils.resolvePath(myCrop.imageFile, 'image')
                if os.path.exists(imagePath):
                    pixmap = QPixmap(imagePath)
                    if not pixmap.isNull():
                        self.lblCropPic.setPixmap(pixmap)
                        return

                # Try alternative path in images directory
                imagesDir = LaUtils.userImagesDirPath()
                imageFileName = os.path.basename(myCrop.imageFile)
                alternativePath = os.path.join(imagesDir, imageFileName)

                if os.path.exists(alternativePath):
                    pixmap = QPixmap(alternativePath)
                    if not pixmap.isNull():
                        self.lblCropPic.setPixmap(pixmap)
                        return

            # Clear the label if no valid image was found
            self.lblCropPic.clear()

    def on_cboCrop_changed(self, theIndex):
        """Handle change in crop selection"""
        self.updateCropPicture()

    def on_cbFallowEnergyType_changed(self, index):
        """Handle changes to the fallow energy type combo box."""
        if not self.mCropParameter:
            return
            
        energyType = self.cbFallowEnergyType.itemData(index)
        if isinstance(energyType, LaEnergyType):
            self.mCropParameter.fallowEnergyType = energyType

    def showCropParameter(self):
        """Display crop parameter in the form."""
        if not self.mCropParameter:
            return

        self.leName.setText(self.mCropParameter.name)
        self.leDescription.setText(self.mCropParameter.description)
        self.setComboToDefault(self.cboCrop, self.mCropParameter.cropGuid)

        # Handle numeric values with proper type conversion
        self.sbPercentTameCrop.setValue(float(self.mCropParameter.percentTameCrop))
        self.sbFallowRatio.setValue(float(self.mCropParameter.fallowRatio))
        self.sbSpoilage.setValue(int(self.mCropParameter.spoilage))
        self.sbReseed.setValue(int(self.mCropParameter.reseed))
        self.grpCropRotation.setChecked(self.mCropParameter.cropRotation)
        # Remove float conversion since fallowValue is already an integer
        self.sbFallowValue.setValue(self.mCropParameter.fallowValue)

        # Handle fallow energy type
        energyType = self.mCropParameter.fallowEnergyType
        for i in range(self.cbFallowEnergyType.count()):
            if self.cbFallowEnergyType.itemData(i) == energyType:
                self.cbFallowEnergyType.setCurrentIndex(i)
                break

        self.cbAreaUnits.setCurrentIndex(self.mCropParameter.areaUnits.value)
        self._restoreRasterCombo(self.mCropParameter.rasterName)
        self.updateCropPicture()

    def _upgradeRasterCombo(self):
        """Replace ``cboRaster`` (plain QComboBox in the .ui) with a
        ``QgsMapLayerComboBox`` filtered to raster layers, so the user can
        pick the suitability surface for this crop parameter directly from
        currently-loaded QGIS layers.

        Falls back silently if ``cboRaster`` isn't present (some forms may
        not have it) or if ``qgis.gui`` isn't importable in the host.
        """
        try:
            from qgis.gui import QgsMapLayerComboBox
            from qgis.core import QgsMapLayerProxyModel
        except ImportError:
            return

        myOld = getattr(self, "cboRaster", None)
        if myOld is None:
            return
        myParent = myOld.parentWidget()
        myLayout = myParent.layout() if myParent else None
        if myLayout is None:
            return
        myNew = QgsMapLayerComboBox(myParent)
        myNew.setObjectName("cboRaster")
        myNew.setFilters(QgsMapLayerProxyModel.RasterLayer)
        myNew.setAllowEmptyLayer(True, "(no suitability raster)")
        myLayout.replaceWidget(myOld, myNew)
        myOld.deleteLater()
        self.cboRaster = myNew

    def _restoreRasterCombo(self, theRasterName: str) -> None:
        """Set cboRaster's current layer to whichever loaded layer's
        ``source()`` matches the given path. Empty/missing → no selection."""
        try:
            from qgis.core import QgsProject
        except ImportError:
            return
        if not theRasterName:
            self.cboRaster.setCurrentIndex(0)  # the empty entry
            return
        for myLayer in QgsProject.instance().mapLayers().values():
            if getattr(myLayer, "source", lambda: "")() == theRasterName:
                self.cboRaster.setLayer(myLayer)
                return
        # No matching loaded layer — leave selection empty
        self.cboRaster.setCurrentIndex(0)

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

            # Convert both GUIDs to safe strings for comparison
            if myCropParameter.guid == theGuid:
                mySelectedRow = myCurrentRow

            self.tblCropParameterProfiles.insertRow(myCurrentRow)
            # Use the safe GUID string for display and storage
            mypFileNameItem = QTableWidgetItem(myCropParameter.guid)
            self.tblCropParameterProfiles.setItem(myCurrentRow, 0, mypFileNameItem)
            mypNameItem = QTableWidgetItem(str(myCropParameter.name) + "  (" + str(myCropParameter.description) + ")")
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
        filePath = os.path.join(myCropParameterDir, theFileName)
        myCropParameter = LaCropParameter()
        if os.path.exists(filePath):
            myCropParameter.fromXmlFile(filePath)
            self.mCropParameter = myCropParameter
            self.showCropParameter()
        else:
            print(f"Error: File does not exist: {filePath}")

    def on_toolNew_clicked(self):
        """Create a new crop parameter"""
        myCropParameter = LaCropParameter()
        myCropParameter.setGuid(None)  # Generate new GUID
        self.mCropParameter = myCropParameter
        self.showCropParameter()

    def on_toolCopy_clicked(self):
        """Copy the selected crop parameter"""
        # Don't attempt to copy if no row is selected
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        # Get the GUID of the selected crop parameter
        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if not myGuid:
            return

        # Load the original crop parameter
        myOriginalFileName = os.path.join(LaUtils.userCropParameterProfilesDirPath(), f"{myGuid}.xml")
        myCropParameter = LaCropParameter()
        myCropParameter.fromXmlFile(myOriginalFileName)

        # Generate a new GUID for the copy
        myCropParameter.setGuid()  # This will automatically generate a new GUID

        # Set the name to indicate it's a copy
        myCropParameter.name = "Copy of " + myCropParameter.name

        # Save the copy to a new file named with its GUID
        myNewFileName = os.path.join(LaUtils.userCropParameterProfilesDirPath(),
                                   f"{myCropParameter.guid}.xml")
        myCropParameter.toXmlFile(myNewFileName)

        # Refresh the table and select the new item
        self.refreshCropParameterTable(myCropParameter.guid)

    def on_toolDelete_clicked(self):
        """Delete the selected crop parameter"""
        if self.tblCropParameterProfiles.currentRow() < 0:
            return

        myGuid = self.tblCropParameterProfiles.item(self.tblCropParameterProfiles.currentRow(), 0).text()
        if myGuid:
            from qgis.PyQt.QtCore import QFile
            filePath = os.path.join(LaUtils.userCropParameterProfilesDirPath(), f"{myGuid}.xml")
            myFile = QFile(filePath)
            if not myFile.remove():
                QMessageBox.warning(self, "Landuse Analyst", f"Unable to delete file: {myFile.fileName()}")
            self.refreshCropParameterTable()

    def on_pbnApply_clicked(self):
        """Apply changes to the crop parameter"""
        if not self.mCropParameter:
            return

        # Save current values to the crop parameter
        self.mCropParameter.name = self.leName.text()
        self.mCropParameter.description = self.leDescription.text()
        self.mCropParameter.cropGuid = self.cboCrop.itemData(self.cboCrop.currentIndex(), Qt.UserRole)

        try:
            # Convert numeric values properly
            self.mCropParameter.percentTameCrop = float(self.sbPercentTameCrop.value())
            self.mCropParameter.spoilage = int(self.sbSpoilage.value())
            self.mCropParameter.reseed = int(self.sbReseed.value())
            self.mCropParameter.fallowRatio = float(self.sbFallowRatio.value())
            self.mCropParameter.fallowValue = int(self.sbFallowValue.value())
        except (ValueError, TypeError) as e:
            print(f"Error converting values in on_pbnApply_clicked: {e}")

        # Boolean values
        self.mCropParameter.cropRotation = self.grpCropRotation.isChecked()
        self.mCropParameter.useCommonLand = self.checkBoxUseCommonLand.isChecked()
        self.mCropParameter.useSpecificLand = self.checkBoxUseSpecificLand.isChecked()

        # Handle area units
        from la.lib.la import AreaUnits
        unit_text = self.cbAreaUnits.currentText()
        if unit_text == "Dunum":
            self.mCropParameter.areaUnits = AreaUnits.Dunum
        elif unit_text == "Hectare":
            self.mCropParameter.areaUnits = AreaUnits.Hectare

        # Save the suitability raster's source path. cboRaster is a
        # QgsMapLayerComboBox after _upgradeRasterCombo runs, so currentLayer()
        # gives the QgsMapLayer; we persist its source() (file path) so the
        # rasterName survives across QGIS sessions.
        if hasattr(self, 'cboRaster'):
            myLayer = self.cboRaster.currentLayer() if hasattr(self.cboRaster, "currentLayer") else None
            self.mCropParameter.rasterName = myLayer.source() if myLayer is not None else ""

        # Use safe_guid for consistent string representation
        target_file = os.path.join(LaUtils.userCropParameterProfilesDirPath(), f"{self.mCropParameter.guid}.xml")

        # Save to file
        success = self.mCropParameter.toXmlFile(target_file)
        if success:
            self.refreshCropParameterTable(self.mCropParameter.guid)
        else:
            QMessageBox.warning(self, "Landuse Analyst", f"Failed to save crop parameter to {target_file}")

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