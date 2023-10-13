"""
lautils.py - A PyQt5 implementation of the LaUtils class.

This file contains the LaUtils class, which is a PyQt5 implementation of the
LaUtils class from the original C++ code. The class is responsible for providing
utility functions for the simulation.

Author: [Your Name]
Date created: [Date]
"""

import os
import sys
import random
import string
from qgis.PyQt.QtWidgets import QMessageBox
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QColor
from la.lib.laanimalparameter import LaAnimalParameter


class LaUtils:
    @staticmethod
    def getAnimalParameters():
        """
        Returns a list of all animal parameters.
        """
        return LaAnimalParameter.getInstances()

    @staticmethod
    def addAnimalParameter(animalParameter):
        """
        Adds a new animal parameter.
        """
        animalParameter.save()

    @staticmethod
    def removeAnimalParameter(name):
        """
        Removes an animal parameter by name.
        """
        animalParameter = LaAnimalParameter.getInstanceByName(name)
        if animalParameter is not None:
            animalParameter.remove()

    @staticmethod
    def editAnimalParameter(animalParameter):
        """
        Edits an existing animal parameter.
        """
        animalParameter.save()

    @staticmethod
    def showInputDialog(parent, title, text=""):
        """
        Shows an input dialog and returns the entered text and a boolean indicating whether
        the OK button was pressed.
        """
        inputDialog = QInputDialog(parent)
        inputDialog.setWindowTitle(title)
        inputDialog.setTextValue(text)
        inputDialog.setLabelText(title)
        inputDialog.setInputMode(QInputDialog.TextInput)
        inputDialog.setOkButtonText("OK")
        inputDialog.setCancelButtonText("Cancel")
        if inputDialog.exec_() == QInputDialog.Accepted:
            return inputDialog.textValue(), True
        else:
            return "", False

    @staticmethod
    def showMessageBox(parent, title, text, icon=QMessageBox.Information):
        """
        Shows a message box with the specified title, text, and icon.
        """
        messageBox = QMessageBox(parent)
        messageBox.setWindowTitle(title)
        messageBox.setText(text)
        messageBox.setIcon(icon)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec_()

    @staticmethod
    def showColorDialog(parent, title, color=QColor()):
        """
        Shows a color dialog and returns the selected color.
        """
        colorDialog = QColorDialog(parent)
        colorDialog.setWindowTitle(title)
        colorDialog.setCurrentColor(color)
        if colorDialog.exec_() == QColorDialog.Accepted:
            return colorDialog.selectedColor()
        else:
            return color

    @staticmethod
    def generateGuid():
        """
        Generates a new GUID.
        """
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

    @staticmethod
    def saveToFile(filename, data):
        """
        Saves data to a file with the specified filename.
        """
        file = QFile(filename)
        if file.open(QFile.WriteOnly | QFile.Text):
            stream = QTextStream(file)
            stream << data
            file.close()

    @staticmethod
    def loadFromFile(filename):
        """
        Loads data from a file with the specified filename.
        """
        file = QFile(filename)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            data = stream.readAll()
            file.close()
            return data
        else:
            return ""

    @staticmethod
    def getApplicationDirPath():
        """
        Returns the path to the directory containing the application executable.
        """
        return os.path.dirname(sys.argv[0])


"""

In this modified code, the contents of lautils.cpp and lautils.h are combined
    into a single Python file.

The LaUtils class is implemented using PyQt5, and includes methods for managing
    animal parameters, showing input and message dialogs, generating GUIDs,
    and reading and writing data to files.

The necessary imports are included at the beginning of the file, and a file
    comment header provides a brief description of the file and its contents.

"""