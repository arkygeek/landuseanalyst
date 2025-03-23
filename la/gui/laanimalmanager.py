from qgis.PyQt.QtCore import Qt, QModelIndex, QAbstractTableModel, QSettings
from qgis.PyQt.QtGui import QBrush, QColor, QIcon, QPixmap
from qgis.PyQt.QtWidgets import QDialog, QTreeWidgetItem, QMessageBox, QTableWidgetItem, QFileDialog, QHeaderView, QComboBox
from qgis.PyQt import uic
import os

from la.lib.laanimal import LaAnimal
from la.lib.lautils import LaUtils
from la.lib.la import EnergyType as LaEnergyType
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import Priority

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(
        os.path.dirname(__file__),
        '../ui/laanimalmanagerbase.ui'
    )
)

class LaAnimalTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animals = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.animals)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        animal = self.animals[row]

        if role == Qt.DisplayRole:
            if col == 0:
                return animal.name
            elif col == 1:
                return animal.description
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

    def addAnimal(self, animal):
        self.beginInsertRows(QModelIndex(), len(self.animals), len(self.animals))
        self.animals.append(animal)
        self.endInsertRows()

    def removeAnimal(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.animals[index]
        self.endRemoveRows()

    def getAnimal(self, index):
        return self.animals[index]


class LaAnimalManagerBase(QDialog, FORM_CLASS):
    """Base class for the Animal Manager dialog.

    This class handles loading the UI. All implementation logic
    should be in the LaAnimalManager class.
    """
    def __init__(self, parent=None):
        super(LaAnimalManagerBase, self).__init__(parent)
        self.setupUi(self)

        # Basic UI initialization
        self.lblAnimalPix.setScaledContents(True)

        # Set up table headers
        self.tblAnimals.horizontalHeader().hide()
        self.tblAnimals.verticalHeader().hide()


class LaAnimalManager(LaAnimalManagerBase):
    """The Animal Manager dialog.

    This class provides the implementation for managing animals, including
    creating, editing, copying, and deleting animals.
    """
    def __init__(self, theAnimalsMap=None, parent=None):
        # Initialize UI from base class first
        super(LaAnimalManager, self).__init__(parent)

        # Store a working copy of the animals map
        self.mAnimalsMap = theAnimalsMap.copy() if theAnimalsMap else {}

        # Initialize other variables
        self.imageFile = ""
        self.animal = LaAnimal()

        # Connect signals/slots
        self.connectSignalsSlots()

        # Populate the table with animals
        self.refreshAnimalTable()

        # Read window settings
        self.readSettings()

    def connectSignalsSlots(self):
        """Connect signals to slots for UI interaction."""
        self.tblAnimals.cellClicked.connect(self.cellClicked)
        self.toolNew.clicked.connect(self.on_toolNew_clicked)
        self.toolCopy.clicked.connect(self.on_toolCopy_clicked)
        self.toolDelete.clicked.connect(self.on_toolDelete_clicked)
        self.pbnApply.clicked.connect(self.on_pbnApply_clicked)
        self.pbnAnimalPic.clicked.connect(self.on_pbnAnimalPic_clicked)
        self.tblAnimals.itemSelectionChanged.connect(self.on_tblAnimals_itemSelectionChanged)

    def readSettings(self):
        """Read window settings from QSettings."""
        settings = QSettings()
        pos = settings.value("AnimalManager/pos", None)
        size = settings.value("AnimalManager/size", None)

        if pos is not None:
            self.move(pos)
        if size is not None:
            self.resize(size)

    def writeSettings(self):
        """Save window settings to QSettings."""
        settings = QSettings()
        settings.setValue("AnimalManager/pos", self.pos())
        settings.setValue("AnimalManager/size", self.size())

    def refreshAnimalTable(self, theGuid=None):
        """Refresh the table of animals.

        Args:
            theGuid (str, optional): GUID of the animal to select.
        """
        # Clear the table
        self.tblAnimals.clear()
        self.tblAnimals.setRowCount(0)
        self.tblAnimals.setColumnCount(2)

        # Set the headers
        headerLabels = ["File Name", "Name"]
        self.tblAnimals.setHorizontalHeaderLabels(headerLabels)
        self.tblAnimals.setColumnWidth(0, 0)  # Hide first column
        self.tblAnimals.setColumnWidth(1, self.tblAnimals.width())
        self.tblAnimals.horizontalHeader().hide()
        self.tblAnimals.verticalHeader().hide()
        self.tblAnimals.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # Get animals
        animals_map = LaUtils.getAvailableAnimals()

        # Populate the table
        mySelectedRow = 0
        myCurrentRow = 0
        for guid, animal in animals_map.items():
            if theGuid is None and myCurrentRow == 0:  # Default to first item
                theGuid = guid

            # Select the row if the GUID matches
            if animal.guid() == theGuid:  # Call guid() method
                mySelectedRow = myCurrentRow

            # Add row
            self.tblAnimals.insertRow(myCurrentRow)

            # Add GUID (hidden)
            mypFileNameItem = QTableWidgetItem(animal.guid())  # Call guid() method
            self.tblAnimals.setItem(myCurrentRow, 0, mypFileNameItem)

            # Add name and description
            mypNameItem = QTableWidgetItem(f"{animal.name} ({animal.description})")
            self.tblAnimals.setItem(myCurrentRow, 1, mypNameItem)

            # Add icon
            myIcon = QIcon()
            myIcon.addFile(":/localdata.png")
            mypNameItem.setIcon(myIcon)

            myCurrentRow += 1

        # Select a row if there are any
        if myCurrentRow > 0:
            self.tblAnimals.setCurrentCell(mySelectedRow, 1)
            self.cellClicked(mySelectedRow, 1)
        else:
            self.on_toolNew_clicked()

    def cellClicked(self, row, column):
        """Handle cell clicked event."""
        myGuid = self.tblAnimals.item(row, 0).text()
        self.selectAnimal(f"{myGuid}.xml")

        # Update the image if available
        if hasattr(self, 'animal') and self.animal and hasattr(self.animal, 'imageFile') and self.animal.imageFile:
            image_path = LaUtils.resolvePath(str(self.animal.imageFile), 'image')
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    self.lblAnimalPix.setPixmap(pixmap)
                else:
                    self.lblAnimalPix.clear()
            else:
                self.lblAnimalPix.clear()

    def selectAnimal(self, theFileName):
        """Load an animal from a file."""
        myAnimalDir = LaUtils.userAnimalProfilesDirPath()
        filePath = os.path.join(myAnimalDir, theFileName)
        myAnimal = LaAnimal()

        if os.path.exists(filePath):
            myAnimal.fromXmlFile(filePath)
            self.animal = myAnimal
            self.showAnimal()
        else:
            LaUtils.debug.log(f"Error: File does not exist: {filePath}")

    def showAnimal(self):
        """Display animal in the form."""
        if not self.animal:
            return

        # Basic info
        self.leName.setText(self.animal.name)
        self.leDescription.setText(self.animal.description)

        # Meat production
        self.sbMeatFoodValue.setValue(self.animal.meatFoodValue)
        self.sbUsableMeatPercent.setValue(self.animal.usableMeat)
        self.sbKillWeight.setValue(self.animal.killWeight)
        self.sbAdultWeight.setValue(self.animal.adultWeight)
        self.sbConceptionEfficiency.setValue(self.animal.conceptionEfficiency)
        self.sbFemalesToMales.setValue(self.animal.femalesPerMale)
        self.sbGrowTime.setValue(self.animal.growTime)
        self.sbDeathRate.setValue(self.animal.deathRate)

        # Handle feed energy type - get the actual enum value
        energy_type = self.animal._feedEnergyType  # Access the internal value directly
        try:
            if isinstance(energy_type, LaEnergyType):
                energy_index = energy_type.value
            else:
                energy_index = 0  # Default to first item
        except (ValueError, TypeError):
            energy_index = 0

        energy_index = max(0, min(self.cbFeedEnergyType.count() - 1, energy_index))
        self.cbFeedEnergyType.setCurrentIndex(energy_index)

        # Energy values
        self.sbEnergyForPregnant.setValue(self.animal.gestating)
        self.sbEnergyForLactating.setValue(self.animal.lactating)
        self.sbEnergyForMaintenance.setValue(self.animal.maintenance)
        self.sbEnergyForJuvenilePerKg.setValue(self.animal.juvenile)

        # Reproduction
        self.sbSexualMaturity.setValue(self.animal.sexualMaturity)
        self.sbBreedingLife.setValue(self.animal.breedingExpectancy)
        self.sbYoungPerBirth.setValue(self.animal.youngPerBirth)
        self.sbWeaningAge.setValue(self.animal.weaningAge)
        self.sbWeaningWeight.setValue(self.animal.weaningWeight)

        # Update the image display
        image_file = getattr(self.animal, '_imageFile', '')  # Access internal value directly
        if image_file:
            # Use LaUtils.resolveImagePath to find the image
            image_path = LaUtils.resolveImagePath(image_file)
            LaUtils.debug.log(f"Loading animal image from: {image_path}")

            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    # Scale the pixmap to fit the label while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.lblAnimalPix.width(),
                        self.lblAnimalPix.height(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                    self.lblAnimalPix.setPixmap(scaled_pixmap)
                    LaUtils.debug.log(f"Successfully loaded and displayed image: {image_path}")
                else:
                    LaUtils.debug.log(f"Failed to load image into pixmap: {image_path}")
                    self.lblAnimalPix.clear()
            else:
                LaUtils.debug.log(f"Image file not found: {image_path}")
                self.lblAnimalPix.clear()
        else:
            LaUtils.debug.log("No image file specified for animal")
            self.lblAnimalPix.clear()

    def on_toolNew_clicked(self):
        """Create a new animal."""
        myAnimal = LaAnimal()
        myAnimal.setGuid(None)  # Generate new GUID
        self.animal = myAnimal
        self.showAnimal()

    def on_toolCopy_clicked(self):
        """Copy the selected animal."""
        if not self.animal:
            return

        myAnimal = LaAnimal(self.animal)
        myAnimal.setGuid(None)  # Generate new GUID
        self.animal = myAnimal
        self.showAnimal()

    def on_toolDelete_clicked(self):
        """Delete the selected animal."""
        if not self.animal:
            return

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete {self.animal.name}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Delete the file
            myAnimalDir = LaUtils.userAnimalProfilesDirPath()
            filePath = os.path.join(myAnimalDir, f"{self.animal.guid}.xml")

            try:
                os.remove(filePath)
                LaUtils.debug.log(f"Deleted animal file: {filePath}")

                # Refresh the table
                self.refreshAnimalTable()
            except Exception as e:
                LaUtils.debug.log(f"Failed to delete animal file: {str(e)}")
                QMessageBox.warning(self, "Delete Failed", f"Failed to delete animal: {str(e)}")

    def on_pbnApply_clicked(self):
        """Apply changes to the animal."""
        if not self.animal:
            return

        # Update animal with form values
        self.animal.name = self.leName.text()
        self.animal.description = self.leDescription.text()

        # Set basic properties
        self.animal.meatFoodValue = self.sbMeatFoodValue.value()
        self.animal.usableMeat = self.sbUsableMeatPercent.value()
        self.animal.killWeight = self.sbKillWeight.value()
        self.animal.adultWeight = self.sbAdultWeight.value()
        self.animal.growTime = self.sbGrowTime.value()
        self.animal.deathRate = self.sbDeathRate.value()

        # Set feed energy type using internal attribute
        self.animal._feedEnergyType = LaEnergyType(self.cbFeedEnergyType.currentIndex())

        # Set reproduction parameters
        self.animal.sexualMaturity = self.sbSexualMaturity.value()
        self.animal.breedingExpectancy = self.sbBreedingLife.value()
        self.animal.youngPerBirth = self.sbYoungPerBirth.value()
        self.animal.weaningAge = self.sbWeaningAge.value()
        self.animal.weaningWeight = self.sbWeaningWeight.value()

        # Handle image file
        if self.imageFile:
            # Get just the filename
            image_filename = os.path.basename(self.imageFile)
            # Copy image to images directory if needed
            target_image_path = os.path.join(LaUtils.userImagesDirPath(), image_filename)

            if self.imageFile != target_image_path:  # Only copy if source is different
                try:
                    # Ensure images directory exists
                    os.makedirs(LaUtils.userImagesDirPath(), exist_ok=True)
                    # Copy the image file
                    import shutil
                    shutil.copy2(self.imageFile, target_image_path)
                    LaUtils.debug.log(f"Copied image to: {target_image_path}")
                    # Update animal's image file property to just the filename
                    self.animal._imageFile = image_filename  # Set internal attribute directly
                except Exception as e:
                    LaUtils.debug.log(f"Failed to copy image file: {str(e)}")
                    QMessageBox.warning(self, "Image Copy Failed",
                                     f"Failed to copy image file to {target_image_path}: {str(e)}")
                    return

        # Save animal to file
        target_file = os.path.join(LaUtils.userAnimalProfilesDirPath(), f"{self.animal.guid}.xml")
        LaUtils.debug.log(f"Saving animal to: {target_file}")
        success = self.animal.toXmlFile(target_file)

        if success:
            self.refreshAnimalTable(self.animal.guid)
        else:
            QMessageBox.warning(self, "Landuse Analyst", f"Failed to save animal to {target_file}")
            return

    def on_pbnAnimalPic_clicked(self):
        """Select an image for the animal."""
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        if fileDialog.exec_():
            filenames = fileDialog.selectedFiles()
            if filenames:
                imagePath = filenames[0]
                self.imageFile = imagePath

                # Display the image
                pixmap = QPixmap(imagePath)
                if not pixmap.isNull():
                    self.lblAnimalPix.setPixmap(pixmap)

    def on_tblAnimals_itemSelectionChanged(self):
        """Handle selection change in the animals table."""
        # Get selected row
        selectedRows = self.tblAnimals.selectedItems()
        if selectedRows:
            selectedRow = selectedRows[0].row()
            self.cellClicked(selectedRow, 1)

    def resizeEvent(self, event):
        """Handle resize event to adjust table columns."""
        super(LaAnimalManager, self).resizeEvent(event)
        # Adjust column widths
        self.tblAnimals.setColumnWidth(0, 0)  # Hide first column
        self.tblAnimals.setColumnWidth(1, self.tblAnimals.width())