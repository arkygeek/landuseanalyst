"""
laassemblageconversion.py - A dialog for converting assemblage data into diet percentages.

This class implements a dialog for the Assemblage Conversion Utility which helps users
convert animal counts from archaeological assemblages into relative percentages of
the diet. It supports both manual entry and automatic calculations based on predefined
animal data.

Author: Jason Jorgenson (arkygeek@gmail.com) and Tim Sutton (tim@linfiniti.com)
Date created: March 2024
"""

import os
from qgis.PyQt.QtCore import Qt, QSettings, QPoint, QSize
from qgis.PyQt.QtGui import QIcon, QResizeEvent
from qgis.PyQt.QtWidgets import (QDialog, QTableWidgetItem, QComboBox,
                                QHeaderView, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QPushButton, QLineEdit, QSpinBox, QDoubleSpinBox,
                                QRadioButton, QGroupBox, QTableWidget, QFileDialog)

from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal


class LaAssemblageConversion(QDialog):
    """
    Dialog for converting assemblage data into diet percentages.

    This dialog allows users to input animal assemblage data and convert
    it to estimated dietary contributions based on meat yields and caloric values.
    """

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        """Initialize the dialog."""
        super().__init__(parent, flags)
        self.setupUi()
        self.readSettings()

        # Connect signals to slots
        self.pbnInsert.clicked.connect(self.on_pbnInsert_clicked)
        self.pbnCalculate.clicked.connect(self.on_pbnCalculate_clicked)
        self.pbnSave.clicked.connect(self.on_pbnSave_clicked)
        self.pbnClearTable.clicked.connect(self.on_pbnClearTable_clicked)

        # Setup the animals table
        self.tblAnimals.setColumnCount(5)
        self.tblAnimals.setHorizontalHeaderLabels(["Animal", "Number", "Usable Meat (kg)", "Calories per kg", "% of Diet"])

        # Populate the animals combo box
        self.setupAnimalsCombo()

    def setupUi(self):
        """Set up the user interface."""
        self.setWindowTitle("Assemblage Conversion Utility")
        self.resize(600, 500)

        # Main layout
        mainLayout = QVBoxLayout(self)

        # Input section
        inputGroupBox = QGroupBox("Input Data")
        inputLayout = QVBoxLayout(inputGroupBox)

        # Radio button section
        radioLayout = QHBoxLayout()
        self.rbAuto = QRadioButton("Use predefined animal data")
        self.rbManual = QRadioButton("Manual entry")
        self.rbAuto.setChecked(True)
        radioLayout.addWidget(self.rbAuto)
        radioLayout.addWidget(self.rbManual)
        inputLayout.addLayout(radioLayout)

        # Animal selection (predefined)
        autoLayout = QHBoxLayout()
        autoLayout.addWidget(QLabel("Animal:"))
        self.cboAnimal = QComboBox()
        autoLayout.addWidget(self.cboAnimal)
        inputLayout.addLayout(autoLayout)

        # Manual entry fields
        manualLayout = QHBoxLayout()
        manualLayout.addWidget(QLabel("Animal name:"))
        self.leAnimal = QLineEdit()
        manualLayout.addWidget(self.leAnimal)

        manualLayout.addWidget(QLabel("Usable meat (kg):"))
        self.sbUsableMeat = QSpinBox()
        self.sbUsableMeat.setMaximum(1000)
        self.sbUsableMeat.setValue(10)
        manualLayout.addWidget(self.sbUsableMeat)

        manualLayout.addWidget(QLabel("Calories per kg:"))
        self.sbCalsPerKg = QSpinBox()
        self.sbCalsPerKg.setMaximum(10000)
        self.sbCalsPerKg.setValue(1500)
        manualLayout.addWidget(self.sbCalsPerKg)

        inputLayout.addLayout(manualLayout)

        # Common fields (number of animals)
        commonLayout = QHBoxLayout()
        commonLayout.addWidget(QLabel("Number:"))
        self.dsbNumber = QDoubleSpinBox()
        self.dsbNumber.setMaximum(1000)
        self.dsbNumber.setValue(1.0)
        self.dsbNumber.setDecimals(1)
        commonLayout.addWidget(self.dsbNumber)
        commonLayout.addStretch()
        inputLayout.addLayout(commonLayout)

        # Insert button
        self.pbnInsert = QPushButton("Insert")
        inputLayout.addWidget(self.pbnInsert)

        # Add input group box to main layout
        mainLayout.addWidget(inputGroupBox)

        # Table section
        self.tblAnimals = QTableWidget()
        self.tblAnimals.setSelectionBehavior(QTableWidget.SelectRows)
        self.tblAnimals.setAlternatingRowColors(True)
        mainLayout.addWidget(self.tblAnimals)

        # Buttons section
        buttonsLayout = QHBoxLayout()
        self.pbnCalculate = QPushButton("Calculate")
        self.pbnSave = QPushButton("Save")
        self.pbnClearTable = QPushButton("Clear Table")
        buttonsLayout.addWidget(self.pbnCalculate)
        buttonsLayout.addWidget(self.pbnSave)
        buttonsLayout.addWidget(self.pbnClearTable)
        mainLayout.addLayout(buttonsLayout)

        # Set the layout
        self.setLayout(mainLayout)

    def setupAnimalsCombo(self):
        """Populate the animals combo box with available animals."""
        self.cboAnimal.clear()
        myAnimalsMap = LaUtils.getAvailableAnimals()

        for guid, animal in myAnimalsMap.items():
            if hasattr(animal, 'name'):
                name = animal.name
                if callable(name):
                    name = name()

                icon = QIcon()
                icon.addFile(":/localdata.png")
                self.cboAnimal.addItem(icon, name, guid)

    def readSettings(self):
        """Read dialog position and size settings."""
        settings = QSettings()
        pos = settings.value("laassemblageconversion/pos", QPoint(200, 200))
        size = settings.value("laassemblageconversion/size", QSize(600, 500))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        """Save dialog position and size settings."""
        settings = QSettings()
        settings.setValue("laassemblageconversion/pos", self.pos())
        settings.setValue("laassemblageconversion/size", self.size())

    def resizeEvent(self, event: QResizeEvent):
        """Handle resize events to adjust table column widths."""
        super().resizeEvent(event)
        if hasattr(self, 'tblAnimals'):
            self.tblAnimals.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def on_pbnInsert_clicked(self):
        """Add an animal to the table."""
        row_count = self.tblAnimals.rowCount()

        if self.rbManual.isChecked():
            # Add item to table from manual inputs
            self.tblAnimals.insertRow(row_count)

            name = self.leAnimal.text()
            usable_meat = self.sbUsableMeat.value()
            cals_per_kg = self.sbCalsPerKg.value()
            number = self.dsbNumber.value()

            name_item = QTableWidgetItem(name)
            self.tblAnimals.setItem(row_count, 0, name_item)

            number_item = QTableWidgetItem(str(number))
            self.tblAnimals.setItem(row_count, 1, number_item)

            usable_meat_item = QTableWidgetItem(str(usable_meat))
            self.tblAnimals.setItem(row_count, 2, usable_meat_item)

            cals_per_kg_item = QTableWidgetItem(str(cals_per_kg))
            self.tblAnimals.setItem(row_count, 3, cals_per_kg_item)

        elif self.rbAuto.isChecked():
            # Add item to table from predefined animals
            animal_guid = self.cboAnimal.currentData()
            animal = LaUtils.getAnimal(animal_guid)

            if not animal:
                return

            self.tblAnimals.insertRow(row_count)

            name = animal.name
            if callable(name):
                name = name()

            usable_meat_percent = animal.usableMeat
            if callable(usable_meat_percent):
                usable_meat_percent = animal.usableMeat()

            kill_weight = animal.killWeight
            if callable(kill_weight):
                kill_weight = animal.killWeight()

            cals_per_kg = animal.meatFoodValue
            if callable(cals_per_kg):
                cals_per_kg = animal.meatFoodValue()

            usable_meat = (0.01 * usable_meat_percent) * kill_weight
            number = self.dsbNumber.value()

            name_item = QTableWidgetItem(name)
            self.tblAnimals.setItem(row_count, 0, name_item)

            number_item = QTableWidgetItem(str(number))
            self.tblAnimals.setItem(row_count, 1, number_item)

            usable_meat_item = QTableWidgetItem(str(usable_meat))
            self.tblAnimals.setItem(row_count, 2, usable_meat_item)

            cals_per_kg_item = QTableWidgetItem(str(cals_per_kg))
            self.tblAnimals.setItem(row_count, 3, cals_per_kg_item)

    def on_pbnCalculate_clicked(self):
        """Calculate the percent of diet based on entries in the table."""
        # Calculate sum of adjusted meat value (NISP * usable meat * calories per kg)
        adjustment_sum = 0.0

        for row in range(self.tblAnimals.rowCount()):
            number_widget = self.tblAnimals.item(row, 1)
            usable_meat_widget = self.tblAnimals.item(row, 2)
            cals_per_kg_widget = self.tblAnimals.item(row, 3)

            if number_widget and usable_meat_widget and cals_per_kg_widget:
                adjustment_sum += (float(number_widget.text()) *
                                 float(usable_meat_widget.text()) *
                                 float(cals_per_kg_widget.text()) *
                                 0.001)  # to keep figures within limits

        # Calculate percentage contribution to diet for each animal
        debug_sum_check = 0.0

        for row in range(self.tblAnimals.rowCount()):
            number_widget = self.tblAnimals.item(row, 1)
            usable_meat_widget = self.tblAnimals.item(row, 2)
            cals_per_kg_widget = self.tblAnimals.item(row, 3)

            if number_widget and usable_meat_widget and cals_per_kg_widget:
                contribution = (float(number_widget.text()) *
                              float(usable_meat_widget.text()) *
                              float(cals_per_kg_widget.text()) *
                              0.001) / adjustment_sum * 100.0

                debug_sum_check += contribution

                contribution_item = QTableWidgetItem(f"{contribution:.2f}")
                self.tblAnimals.setItem(row, 4, contribution_item)

    def on_pbnSave_clicked(self):
        """Save the table data to a CSV file."""
        csv_string = "Name,Number,UsableMeat,CalsPerKg,PercentDiet\n"

        for row in range(self.tblAnimals.rowCount()):
            name_widget = self.tblAnimals.item(row, 0)
            number_widget = self.tblAnimals.item(row, 1)
            usable_meat_widget = self.tblAnimals.item(row, 2)
            cals_per_kg_widget = self.tblAnimals.item(row, 3)
            contribution_widget = self.tblAnimals.item(row, 4)

            if all([name_widget, number_widget, usable_meat_widget,
                  cals_per_kg_widget, contribution_widget]):

                csv_string += (f"{name_widget.text()},"
                            f"{number_widget.text()},"
                            f"{usable_meat_widget.text()},"
                            f"{cals_per_kg_widget.text()},"
                            f"{contribution_widget.text()}\n")

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Assemblage Data",
            os.path.expanduser("~"),
            "CSV Files (*.csv);;All Files (*)"
        )

        if filename:
            with open(filename, 'w') as f:
                f.write(csv_string)

    def on_pbnClearTable_clicked(self):
        """Clear all rows from the table."""
        self.tblAnimals.setRowCount(0)
        self.tblAnimals.clearContents()

    def setComboToDefault(self, combo: QComboBox, default_value: str):
        """Set a combo box to a default value based on user data."""
        if not default_value:
            return False

        for i in range(combo.count()):
            if combo.itemData(i) == default_value:
                combo.setCurrentIndex(i)
                return True

        return False

    def closeEvent(self, event):
        """Handle the dialog close event."""
        self.writeSettings()
        super().closeEvent(event)