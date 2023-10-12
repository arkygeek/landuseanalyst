"""
laanimalparametermanager.py - A PyQt5 implementation of the LaAnimalParameterManager class.

This file contains the LaAnimalParameterManager class, which is a PyQt5 implementation of the
LaAnimalParameterManager class from the original C++ code. The class is responsible for managing
animal parameters, including adding, removing, and editing animal parameters.

Author: [Jason Jorgenson]
Date created: [12-OCT-2023]
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QSpinBox
from PyQt5.uic import loadUi
from lib.laanimalparameter import LaAnimalParameter
from lib.lautils import LaUtils
from ui.ui_laanimalparametermanagerbase import Ui_LaAnimalParameterManagerBase


class LaAnimalParameterManager(QDialog, Ui_LaAnimalParameterManagerBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connect signals and slots
        self.btnAdd.clicked.connect(self.addAnimalParameter)
        self.btnRemove.clicked.connect(self.removeAnimalParameter)
        self.btnEdit.clicked.connect(self.editAnimalParameter)
        self.treeWidget.itemDoubleClicked.connect(self.editAnimalParameter)

        # Populate the tree widget with animal parameters
        self.populateTreeWidget()

    def populateTreeWidget(self):
        """
        Populates the tree widget with animal parameters.
        """
        self.treeWidget.clear()
        for animalParameter in LaUtils.getAnimalParameters():
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, animalParameter.getName())
            item.setText(1, str(animalParameter.getValue()))

    def addAnimalParameter(self):
        """
        Adds a new animal parameter to the tree widget.
        """
        name, ok = LaUtils.showInputDialog(self, "Enter the name of the new animal parameter:")
        if ok:
            value, ok = LaUtils.showInputDialog(self, "Enter the value of the new animal parameter:")
            if ok:
                animalParameter = LaAnimalParameter(name, float(value))
                LaUtils.addAnimalParameter(animalParameter)
                item = QTreeWidgetItem(self.treeWidget)
                item.setText(0, animalParameter.getName())
                item.setText(1, str(animalParameter.getValue()))

    def removeAnimalParameter(self):
        """
        Removes the selected animal parameter from the tree widget.
        """
        item = self.treeWidget.currentItem()
        if item is not None:
            name = item.text(0)
            LaUtils.removeAnimalParameter(name)
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item))

    def editAnimalParameter(self):
        """
        Edits the selected animal parameter in the tree widget.
        """
        item = self.treeWidget.currentItem()
        if item is not None:
            name = item.text(0)
            value, ok = LaUtils.showInputDialog(self, "Enter the new value for the animal parameter:", item.text(1))
            if ok:
                animalParameter = LaAnimalParameter(name, float(value))
                LaUtils.editAnimalParameter(animalParameter)
                item.setText(1, str(animalParameter.getValue()))