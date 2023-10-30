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
import shutil
import random
import string

from typing import Dict, List, Tuple

from qgis.PyQt.QtWidgets import QMessageBox, QColorDialog, QInputDialog, QFileDialog
from qgis.PyQt.QtCore import QFile, QTextStream, QObject, QDir, QSettings
from qgis.PyQt.QtGui import QColor
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter


from qgis.PyQt.QtCore import QObject, pyqtSignal


class LaMessageBus(QObject):
    """Super minimal implementation of a message bus.
    Allows communication between unrelated parts of the plugin.
    """
    # The signal that passes the message.
    messaged = pyqtSignal(str)


# Modules are evaluated only once, therefore it works as a poor man version of singleton.
message_bus = LaMessageBus()


class LaUtils:
    @staticmethod
    def userSettingsDirPath() -> str:
        mySettings = QSettings()
        myPath = mySettings.value("dataDirs/dataDir", os.path.expanduser("~/.landuseAnalyst/"))
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def getModelOutputDir() -> str:
        myPath = os.path.join(LaUtils.userSettingsDirPath(), "modelOutputs")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userAnimalProfilesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/animalProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath
    
    @staticmethod
    def userCropProfilesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/cropProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath
    
    @staticmethod
    def getAvailableAnimals() -> Dict[str, LaAnimal]:
        myMap = {}
        myDirectory = QDir(LaUtils.userAnimalProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimal = LaAnimal()
                myAnimal.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimal.name() == "":
                    continue
                myMap[myAnimal.guid()] = myAnimal
        return myMap
    
    @staticmethod
    def getAnimal(theGuid: str) -> LaAnimal:
        myDirectory = QDir(LaUtils.userAnimalProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimal = LaAnimal()
                myAnimal.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimal.name() == "":
                    continue
                if myAnimal.guid() == theGuid:
                    return myAnimal
        return LaAnimal()  # Return a blank animal if no match is found
    
    @staticmethod
    def getAvailableCrops() -> Dict[str, LaCrop]:
        myMap = {}
        myDirectory = QDir(LaUtils.userCropProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myCrop = LaCrop()
                myCrop.fromXmlFile(myFileInfo.absoluteFilePath())
                if myCrop.name() == "":
                    continue
                myMap[myCrop.guid()] = myCrop
        return myMap

    @staticmethod
    def getCrop(theGuid) -> LaCrop:
        myDirectory = QDir(LaUtils.userCropProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myCrop = LaCrop()
                myCrop.fromXmlFile(myFileInfo.absoluteFilePath())
                if myCrop.name() == "":
                    continue
                if myCrop.guid() == theGuid:
                    return myCrop
        return LaCrop()  # Return a blank crop if no match is found
    
    @staticmethod
    def userConversionTablesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/conversionTables")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userAnimalParameterProfilesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/animalParameterProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userImagesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/images")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userCropParameterProfilesDirPath() -> str:
        myPath = os.path.expanduser("~/.landuseAnalyst/cropParameterProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath
    
    @staticmethod
    def convertAreaToHectares(theAreaUnit: str, theArea: float) -> int:
        # this may seem ridiculous to do it this way, but
        # i plan to include other area units and this way
        # it will make it very easy to work with in the future
        # all need be done is add new units to la.h enum and enter
        # into the following switch...

        myHectares = 0.

        if theAreaUnit == "Dunum":
            myHectares = theArea * 10.
        elif theAreaUnit == "Hectare":
            myHectares = theArea
        # add new units here after updating la.h enum ex:
        # elif theAreaUnit == "Acre":
        #     myHectares = theArea / 2.47105381
        # TODO check why this value is an int. I think it should be a float.
        return int(myHectares)
    
    @staticmethod
    def getAvailableAnimalParameters() -> Dict[str, LaAnimalParameter]:
        myMap = {}
        myDirectory = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimalParameter = LaAnimalParameter()
                myAnimalParameter.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimalParameter.name() == "":
                    continue
                myMap[myAnimalParameter.guid()] = myAnimalParameter
        return myMap
    
    @staticmethod
    def getAnimalParameter(theGuid: str) -> LaAnimalParameter:
        myDirectory = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimalParameter = LaAnimalParameter()
                myAnimalParameter.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimalParameter.name() == "":
                    continue
                if myAnimalParameter.guid() == theGuid:
                    return myAnimalParameter
        return LaAnimalParameter()  # Return a blank one since no match found
    
    @staticmethod
    def getAvailableCropParameters() -> Dict[str, LaCropParameter]:
        myMap = {}
        myDirectory = QDir(LaUtils.userCropParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myCropParameter = LaCropParameter()
                myCropParameter.fromXmlFile(myFileInfo.absoluteFilePath())
                if myCropParameter.name() == "":
                    continue
                myMap[myCropParameter.guid()] = myCropParameter
        return myMap
    
    @staticmethod
    def getCropParameter(theGuid: str) -> LaCropParameter:
        myDirectory = QDir(LaUtils.userCropParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myCropParameter = LaCropParameter()
                myCropParameter.fromXmlFile(myFileInfo.absoluteFilePath())
                if myCropParameter.name() == "":
                    continue
                if myCropParameter.guid() == theGuid:
                    return myCropParameter
        return LaCropParameter()  # Return a blank one since no match found
    
    @staticmethod
    def sortList(theList: List[str]) -> List[str]:
        # sort the taxon list alphabetically descending order
        theList.sort()  # this sorts ascending!
        # flip the sort order
        mySortedList = theList[::-1]
        return mySortedList

    @staticmethod
    def uniqueList(theList: List[str]) -> List[str]:
        # remove any duplicates from a sorted list
        myUniqueList = []
        myLast = ""
        for myCurrent in theList:
            if myCurrent != myLast:
                myUniqueList.append(myCurrent)
            myLast = myCurrent
        return myUniqueList
    
    @staticmethod
    def getExperimentsList() -> List[str]:
        myExperimentList = []
        myWorkDir = os.path.expanduser("~/.landuseAnalyst/modelOutputs/")
        for root, dirs, files in os.walk(myWorkDir):
            for file in files:
                if file.endswith(".xml"):
                    myExperimentList.append(os.path.join(root, file))
        return myExperimentList
    
    @staticmethod
    def createTextFile(theFileName: str, theData: str) -> bool:
        # create the txt file
        try:
            with open(theFileName, 'w') as myFile:
                myFile.write(theData)
            return True
        except:
            return False
        
    @staticmethod
    def xmlEncode(theString: str) -> str:
        theString = theString.replace("<", "&lt;")
        theString = theString.replace(">", "&gt;")
        theString = theString.replace("&", "&amp;")
        return theString

    @staticmethod
    def xmlDecode(theString: str) -> str:
        theString = theString.replace("&lt;", "<")
        theString = theString.replace("&gt;", ">")
        theString = theString.replace("&amp;", "&")
        return theString

    @staticmethod
    def getStandardCss() -> str:
        myStyle = ".glossy{ background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565); color: white; padding-left: 4px; border: 1px solid #6c6c6c; }"
        myStyle += "body {background: white;}"
        myStyle += "h1 {font-size : 22pt; color: #0063F7; }"
        myStyle += "h2 {font-size : 18pt; color: #0063F7; }"
        myStyle += "h3 {font-size : 14pt; color: #0063F7; }"
        myStyle += ".cellHeader {color:#466aa5; font-size : 12pt;}"
        myStyle += ".parameterHeader {font-weight: bold;}"
        myStyle += ".largeCell {color:#000000; font-size : 12pt;}"
        myStyle += ".table {" \
                    "  border-width: 1px 1px 1px 1px;" \
                    "  border-spacing: 2px;" \
                    "  border-style: solid solid solid solid;" \
                    "  border-color: black black black black;" \
                    "  border-collapse: separate;" \
                    "  background-color: white;" \
                    "}"
        return myStyle

    @staticmethod
    def openGraphicFile() -> str:
        myHomePath = os.path.expanduser("~")
        myFileName, _ = QFileDialog.getOpenFileName(None, "Choose an image", myHomePath, "Images (*.png *.xpm *.jpg)")
        myName = os.path.basename(myFileName)
        myDestinationFilePathName = os.path.join(LaUtils.userImagesDirPath(), myName)
        shutil.copy(myFileName, myDestinationFilePathName)
        return myDestinationFilePathName

    @staticmethod
    def saveFile() -> str:
        # myHomePath: str = os.path.expanduser("~")
        myFileName: str
        _ : str
        myFileName, _ = QFileDialog.getSaveFileName(None, "Choose a file name", LaUtils.userConversionTablesDirPath(), "*.csv")
        myName: str = os.path.basename(myFileName)
        myDestinationFilePathName: str = os.path.join(LaUtils.userConversionTablesDirPath(), myName)
        return myDestinationFilePathName

        


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
        print("showInputDialog")
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
    
    @staticmethod
    def openGraphicFile():
        myHomePath = os.path.expanduser("~")
        myFileName, _ = QFileDialog.getOpenFileName(
                            None, 
                            "Choose an image", 
                            myHomePath, 
                            "Images (*.png *.xpm *.jpg)"
                        )
        myName = os.path.basename(myFileName)
        myDestinationFilePathName = os.path.join(LaUtils.userImagesDirPath(), myName)
        shutil.copy(myFileName, myDestinationFilePathName)
        return myDestinationFilePathName


"""

In this modified code, the contents of lautils.cpp and lautils.h are combined
    into a single Python file.

The LaUtils class is implemented using PyQt5, and includes methods for managing
    animal parameters, showing input and message dialogs, generating GUIDs,
    and reading and writing data to files.

The necessary imports are included at the beginning of the file, and a file
    comment header provides a brief description of the file and its contents.

"""