"""
lautils.py - A PyQt5 implementation of the LaUtils class.

This file contains the LaUtils class, which is a PyQt5 implementation of the
LaUtils class from the original C++ code. The class is responsible for providing
utility functions for the simulation.

Author: [Your Name]
Date created: [Date]
"""

# Importing necessary modules
import os
import sys
import shutil
import random
import string

# Importing typing for type hinting
from typing import Dict, List, Tuple

# Importing necessary PyQt5 modules
from qgis.PyQt.QtWidgets import QMessageBox, QColorDialog, QInputDialog, QFileDialog
from qgis.PyQt.QtCore import QFile, QTextStream, QObject, QDir, QSettings, QFileInfo
from qgis.PyQt.QtGui import QColor

# Importing custom classes
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter

# Importing necessary PyQt5 modules
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
    """
    A utility class for Land Use Analyst.

    This class provides various static methods for getting and manipulating data directories, animal and crop profiles,
    conversion tables, animal and crop parameter profiles, and images. It also provides methods for encoding and decoding
    XML strings, sorting and removing duplicates from lists, and creating text files.
    """

        
    @staticmethod
    def userSettingsDirPath() -> str:
        """
        Returns the path to the user settings directory.
        If the directory does not exist, it is created.
        :param thePath: A string representing the path to the user settings directory.
        :type thePath: str
        :return: A string representing the path to the user settings directory.
        :rtype: str
        """
        # Get the user settings directory path from QSettings
        mySettings = QSettings()
        myPath = mySettings.value(
            "dataDirs/dataDir", 
            os.path.expanduser("~/.landuseAnalyst/"))
        # Create the directory if it does not exist
        os.makedirs(myPath, exist_ok=True)
        # Return the path to the user settings directory
        return myPath

    @staticmethod
    def getModelOutputDir() -> str:
        """
        Returns the path to the model outputs directory.
        If the directory does not exist, it is created.
        :return: A string representing the path to the model outputs directory.
        :rtype: str
        """
        myPath = os.path.join(LaUtils.userSettingsDirPath(), "modelOutputs")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userAnimalProfilesDirPath() -> str:
        """
        Returns the path to the animal profiles directory.
        If the directory does not exist, it is created.
        :return: A string representing the path to the animal profiles directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/animalProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userCropProfilesDirPath() -> str:
        """
        Returns the path to the crop profiles directory.
        If the directory does not exist, it is created.
        :return: A string representing the path to the crop profiles directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/cropProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def getAvailableAnimals() -> Dict[str, LaAnimal]:
        """
        Returns a dictionary of available animals.
        The keys are the GUIDs of the animals, and the values are the animal objects.
        :return: A dictionary of available animals.
        :rtype: Dict[str, LaAnimal]
        """
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
        """
        Returns an animal object with the given GUID.
        If no such animal exists, returns a blank animal.
        :param theGuid: The GUID of the animal to return.
        :type theGuid: str
        :return: An animal object.
        :rtype: LaAnimal
        """
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
        """
        Returns a dictionary of available crops, where the keys are the 
        crop GUIDs and the values are LaCrop objects.
        :return: A dictionary of available crops.
        :rtype: Dict[str, LaCrop]
        """
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
    def getCrop(theGuid: str) -> LaCrop:
        """
        This method searches for a crop with the specified GUID in the user's crop profiles directory.
        If a matching crop is found, it is returned as a LaCrop object. Otherwise, a blank LaCrop object is returned.
        :param theGuid: The GUID of the crop to search for.
        :type theGuid: str
        :return: The LaCrop object with the specified GUID, or a blank LaCrop object if no match is found.
        :rtype: LaCrop
        """
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
        """
        Returns the path to the user's conversion tables directory.
        If the directory does not exist, it will be created.
        :return: The path to the user's conversion tables directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/conversionTables")
        os.makedirs(myPath, exist_ok=True) # create directory if it doesn't exist
        return myPath

    @staticmethod
    def userAnimalParameterProfilesDirPath() -> str:
        """ 
        Returns the path to the user's animal parameter profiles directory.
        :return: The path to the user's animal parameter profiles directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/animalParameterProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userImagesDirPath() -> str:
        """ 
        Returns the path to the user's images directory. 
        :return: The path to the user's images directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/images")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def userCropParameterProfilesDirPath() -> str:
        """
        Returns the path to the user's crop parameter profiles directory.
        :return: The path to the user's crop parameter profiles directory.
        :rtype: str
        """
        myPath = os.path.expanduser("~/.landuseAnalyst/cropParameterProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath
    
    @staticmethod
    def convertAreaToHectares(theAreaUnit: str, theArea: float) -> int:
        """
        The method converts an area in the specified area unit to hectares.
        :param theAreaUnit: The area unit name to use for conversion. 
        :type theAreaUnit: str
        :return: The area in hectares.
        :rtype: int
        """
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
        """
        This method returns a dictionary of available animal parameters.
        :return: A dictionary of available animal parameters.
        :rtype: Dict[str, LaAnimalParameter]
        """
        myMap: Dict[str, LaAnimalParameter] = {}
        myDirectory: QDir = QDir(LaUtils.userCropProfilesDirPath())
        
        """ 
        In PyQt5, there is no specific QFileInfoList class. Given that the
        QDir.entryInfoList() method returns a Python list of QFileInfo objects, 
        you only need to import QFileInfo from PyQt5.QtCore
        """
        myList: List[QFileInfo] = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)

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
        myStyle = ".glossy{"
        myStyle += "  background-color: qlineargradient("
        myStyle += "    x1:0, y1:0, x2:0, y2:1, stop:0 #616161,"
        myStyle += "    stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);"
        myStyle += "  color: white; padding-left: 4px; "
        myStyle += "  border: 1px solid #6c6c6c; }"
        myStyle += "body {background: white;}"
        myStyle += "h1 {font-size : 22pt; color: #0063F7; }"
        myStyle += "h2 {font-size : 18pt; color: #0063F7; }"
        myStyle += "h3 {font-size : 14pt; color: #0063F7; }"
        myStyle += ".cellHeader {color:#466aa5; font-size : 12pt;}"
        myStyle += ".parameterHeader {font-weight: bold;}"
        myStyle += ".largeCell {color:#000000; font-size : 12pt;}"
        myStyle += ".table {"
        myStyle += "  border-width: 1px 1px 1px 1px;"
        myStyle += "  border-spacing: 2px;"
        myStyle += "  border-style: solid solid solid solid;"
        myStyle += "  border-color: black black black black;"
        myStyle += "  border-collapse: separate;"
        myStyle += "  background-color: white;"
        myStyle += "}"
        return myStyle

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
    def openGraphicFile() -> str:
        """
        Opens a file dialog to choose an image file and copies it to the user's images directory.

        Returns:
        str: The file path of the copied image file.
        """
        myHomePath = os.path.expanduser("~")
        myFileName, _ = QFileDialog.getOpenFileName(
                            None,
                            "Choose an image",
                            myHomePath,
                            "Images (*.png *.xpm *.jpg)"
                        )
        myName = os.path.basename(myFileName)
        myDestinationFilePathName = os.path.join(
                                        LaUtils.userImagesDirPath(), 
                                        myName
                                    )
        shutil.copy(myFileName, myDestinationFilePathName)
        return myDestinationFilePathName

    @staticmethod
    def saveFile() -> str:
        # myHomePath: str = os.path.expanduser("~")
        myFileName: str
        _ : str
        myFileName, _ = QFileDialog.getSaveFileName(
                            None, 
                            "Choose a file name", 
                            LaUtils.userConversionTablesDirPath(), 
                            "*.csv"
                            )
        myName: str = os.path.basename(myFileName)
        myDestinationFilePathName: str = os.path.join(LaUtils.userConversionTablesDirPath(), myName)
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