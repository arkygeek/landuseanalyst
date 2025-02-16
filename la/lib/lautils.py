"""
lautils.py - A PyQt5 implementation of the LaUtils class.

This file contains the LaUtils class, which is a PyQt5 implementation of the
LaUtils class from the original C++ code. The class is responsible for providing
utility functions for the simulation.

Author: [Your Name]
Date created: [Date]
"""

# Standard library imports
import os
import sys
import shutil
import random
import string
from builtins import dict as Dict
from builtins import list as List
from builtins import classmethod
from typing import Tuple

# Third party imports
from qgis.PyQt .QtWidgets import (
    QMessageBox, QColorDialog, QInputDialog, QFileDialog, QWidget)
from qgis.PyQt.QtCore import (
    QFile, QTextStream, QObject, QDir, QSettings, QFileInfo, QObject, pyqtSignal)
from qgis.PyQt.QtGui import QColor

# Local application imports
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter

class LaMessageBus(QObject):
    """Super minimal implementation of a message bus.
    Allows communication between unrelated parts of the plugin.

    This class inherits from QObject and provides a PyQt signal for message passing.

    Attributes:
        messaged (pyqtSignal): The signal that passes the message. Emits a string.
    """
    # The signal that passes the message.
    messaged: pyqtSignal = pyqtSignal(str)

# Modules are evaluated only once, therefore it works as a poor man version of singleton.
MESSAGE_BUS: LaMessageBus = LaMessageBus()


class LaUtils:
    """
    A utility class for Land Use Analyst.

    This class provides various static methods for getting and manipulating data directories, animal and crop profiles,
    conversion tables, animal and crop parameter profiles, and images. It also provides methods for encoding and decoding
    XML strings, sorting and removing duplicates from lists, and creating text files.

    Static Methods:
        userSettingsDirPath: Returns the path to the user settings directory.
        getModelOutputDir: Returns the path to the model outputs directory.
        userAnimalProfilesDirPath: Returns the path to the animal profiles directory.
        userCropProfilesDirPath: Returns the path to the crop profiles directory.
        getAvailableAnimals: Returns a dictionary of available animals.
        getAnimal: Returns an animal object with the given GUID.
        getAvailableCrops: Returns a dictionary of available crops.
        getCrop: Returns a crop object with the given GUID.
        userConversionTablesDirPath: Returns the path to the user's conversion tables directory.
        userAnimalParameterProfilesDirPath: Returns the path to the user's animal parameter profiles directory.
        userImagesDirPath: Returns the path to the user's images directory.
        userCropParameterProfilesDirPath: Returns the path to the user's crop parameter profiles directory.
        convertAreaToHectares: Converts an area in the specified area unit to hectares.
        getAvailableAnimalParameters: Returns a dictionary of available animal parameters.
        getAnimalParameter: Returns an animal parameter with the given GUID.
        getAvailableCropParameters: Returns a dictionary of available crop parameters.
        getCropParameter: Returns a crop parameter with the given GUID.
        sortList: Sorts a list of strings in descending alphabetical order.
        uniqueList: Returns a list with duplicates removed from the input list.
        getExperimentsList: Returns a list of all experiment XML files in the model outputs directory.
        createTextFile: Creates a text file with the given name and writes the given data to it.
        xmlEncode: Encodes a string for use in XML.
        xmlDecode: Decodes a string from XML encoding.
        getStandardCss: Returns a string of standard CSS styles.
        getAnimalParameters: Returns a list of animal parameters.
        addAnimalParameter: Adds an animal parameter to the list of animal parameters.
        removeAnimalParameter: Removes an animal parameter from the list of animal parameters.
        editAnimalParameter: Edits an animal parameter in the list of animal parameters.
        showInputDialog: Displays an input dialog.
        showMessageBox: Displays a message box.
        showColorDialog: Displays a color dialog.
        generateGuid: Generates a GUID.
        saveToFile: Saves the given data to the given file.
        loadFromFile: Loads data from the given file.
        getApplicationDirPath: Returns the path to the application directory.
        openGraphicFile: Opens a graphic file.
        saveFile: Saves a file.
    """

    @staticmethod
    def userSettingsDirPath() -> str:
        """
        Returns the path to the user settings directory.
        If the directory does not exist, it is created.
        :return: A string representing the path to the user settings directory.
        :rtype: str
        """
        # Get the user settings directory path from QSettings
        mySettings = QSettings()
        myPath = mySettings.value("dataDirs/dataDir", os.path.expanduser("~/.landuseAnalyst/"))

        # Ensure myPath is a string
        if not isinstance(myPath, str):
            myPath = os.path.expanduser("~/.landuseAnalyst/")

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

        from PyQt5.QtCore import QDir

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
        myList = myDirectory.entryInfoList(QDir.Files | QDir.NoSymLinks, QDir.Name)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimal = LaAnimal()
                myAnimal.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimal.name == "":
                    continue
                myMap[myAnimal.guid] = myAnimal
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
        myList = myDirectory.entryInfoList(QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimal = LaAnimal()
                myAnimal.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimal.name == "":
                    continue
                if myAnimal.guid == theGuid:
                    return myAnimal
        return LaAnimal()


    @staticmethod
    def getAvailableCrops() -> Dict[str, LaCrop]:
        """Returns a dict of available crops; keys: crop GUIDs, values: LaCrop objects

            :return: A dictionary of available crops.
            :rtype: Dict[str, LaCrop]

            This function, getAvailableCrops(), is part of the LaUtils class. It returns a
            dictionary of available crops. The dictionary's keys are the GUIDs of the crops,
            and the values are the LaCrop objects themselves.

            Here's a step-by-step explanation of what the function does:

            1. It creates an empty dictionary named myMap to store the available crops.
            2. It creates a QDir object named myDirectory that represents the directory
                where the user's crop profiles are stored.
            3. It gets a list of QFileInfo objects representing the entries in myDirectory
                and stores this list in myList.
            4. It then loops over each entry in myList.
            5. For each entry, it checks if the entry is a directory (by checking if the
                filename is "." or ".."). If it is, it skips to the next iteration of the loop.
            6. If the entry is not a directory, it checks if the entry is an XML file (by
                checking if the file's suffix is "xml"). If it's not an XML file, it skips to
                the next iteration of the loop.
            7. If the entry is an XML file, it creates a new LaCrop object named myCrop and
                attempts to load the crop data from the XML file.
            8. If the crop's name is empty, it skips to the next iteration of the loop.
            9. If the crop's name is not empty, it adds the crop to myMap, using the crop's
                GUID as the key and the LaCrop object as the value.
            10. After it has looped over all the entries in myList, it returns myMap.

            This function is used to load all the available crops from the user's crop
            profiles directory. Each crop is represented by an XML file in this directory.

            NOTE please ensure the following:

            - LaCrop class has a method fromXmlFile() that correctly parses an XML
                file and populates the LaCrop object.
            - LaCrop class has methods guid() and name() to get the GUID and name of the crop.
            - LaUtils class has a method userCropProfilesDirPath() that returns the
                correct directory path.
            - QDir and QFileInfo classes are correctly imported from PyQt5.QtCore.
            - The XML files in the directory are well-formed and contain all the
                necessary information for creating LaCrop objects.
        """
        myMap = {}
        myDirectory = QDir(LaUtils.userCropProfilesDirPath())
        myList: List = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
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
    def getCrop(
            theGuid: str
        ) -> LaCrop:
        """ This method searches for a crop with the specified GUID in the user's crop profiles directory.
            If a matching crop is found, it is returned as a LaCrop object. Otherwise, a blank LaCrop object is returned.
            :param theGuid: The GUID of the crop to search for.
            :type theGuid: str
            :return: The LaCrop object with the specified GUID, or a blank LaCrop object if no match is found.
            :rtype: LaCrop
        """
        myUserCropProfilesDirPath = LaUtils.userCropProfilesDirPath()
        myDirectory = QDir(myUserCropProfilesDirPath)
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
    def userConversionTablesDirPath(
        ) -> str:
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
    def userAnimalParameterProfilesDirPath(
        ) -> str:
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
    def convertAreaToHectares(
            theAreaUnit: str,
            theArea: float
        ) -> int:
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
    def getAvailableAnimalParameters(
        ) -> Dict[str, LaAnimalParameter]:
        """Returns a dictionary of available animal parameters.

        This method scans the directory returned by `userCropProfilesDirPath()`
        for XML files, each of which is expected to define an animal parameter.
        Each file is parsed into an `LaAnimalParameter` object.

        Returns:
        A dictionary mapping the GUIDs of the animal parameters to the
        corresponding `LaAnimalParameter` objects. If no animal parameters
        are found, returns an empty dictionary.

        :return: A dictionary of available animal parameters.
        :rtype: Dict[str, LaAnimalParameter]
        """
        myMap: Dict[str, LaAnimalParameter] = {}
        myDirectory: QDir = QDir(LaUtils.userCropProfilesDirPath())
        # In PyQt5, there is no specific QFileInfoList class. Given that the
        # QDir.entryInfoList() method returns a Python list of QFileInfo objects,
        # you only need to import QFileInfo from QtCore
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
        """Returns an animal parameter with the given GUID.

        This method scans the directory returned by `userAnimalParameterProfilesDirPath()`
        for XML files, each of which is expected to define an animal parameter.
        Each file is parsed into an `LaAnimalParameter` object. If an animal parameter
        with a matching GUID is found, it is returned.

        If no animal parameter with the given GUID is found, this method returns a blank
        `LaAnimalParameter` object.

        Args:
            theGuid (str): The GUID of the animal parameter to retrieve.

        Returns:
            LaAnimalParameter: The animal parameter with the given GUID, or a blank
            `LaAnimalParameter` object if no such animal parameter is found.

        :param theGuid: The GUID of the animal parameter to retrieve.
        :type theGuid: str

        :return: The animal parameter with the given GUID, or a blank `LaAnimalParameter` object.
        :rtype: LaAnimalParameter
        """
        myDirectory: QDir = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        myList: List[QFileInfo] = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            if myFileInfo.fileName() in [".", ".."]:
                continue
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
        """ Returns a dictionary of available crop parameters.

        This method scans the directory returned by `userCropParameterProfilesDirPath()`
        for XML files, each of which is expected to define a crop parameter.
        Each file is parsed into an `LaCropParameter` object.

        Returns:
            A dictionary mapping the GUIDs of the crop parameters to the
            corresponding `LaCropParameter` objects. If no crop parameters
            are found, returns an empty dictionary.

        :return: A dictionary of available crop parameters.
        :rtype: Dict[str, LaCropParameter]
        """
        myMap: Dict [str, LaCropParameter] = {}
        myDirectory: QDir = QDir(LaUtils.userCropParameterProfilesDirPath())
        myList: List[QFileInfo] = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
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
        """Returns a crop parameter with the given GUID.

        This method scans the directory returned by `userCropParameterProfilesDirPath()`
        for XML files, each of which is expected to define a crop parameter.
        Each file is parsed into an `LaCropParameter` object. If a crop parameter
        with a matching GUID is found, it is returned.

        If no crop parameter with the given GUID is found, this method returns a blank
        `LaCropParameter` object.

        Args:
            theGuid (str): The GUID of the crop parameter to retrieve.

        Returns:
            LaCropParameter: The crop parameter with the given GUID, or a blank
            `LaCropParameter` object if no such crop parameter is found.

        :param theGuid: The GUID of the crop parameter to retrieve.
        :type theGuid: str
        :return: The crop parameter with the given GUID, or a blank `LaCropParameter` object.
        :rtype: LaCropParameter
        """
        myDirectory: QDir = QDir(LaUtils.userCropParameterProfilesDirPath())
        myList: List[QFileInfo] = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
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
        """Sorts a list of strings in descending alphabetical order.

        This method sorts the input list in ascending alphabetical order first,
        then reverses the order of the list to achieve descending alphabetical order.

        Args:
            theList (List[str]): The list of strings to sort.

        Returns:
            List[str]: The input list sorted in descending alphabetical order.

        :param theList: The list of strings to sort.
        :type theList: List[str]
        :return: The input list sorted in descending alphabetical order.
        :rtype: List[str]
        """
        # sort the taxon list alphabetically descending order
        mySortedList: List[str] = sorted(theList, reverse=True)  # this sorts descending!
        # TODO use :reverse option of sort() method instead of reversing the list
        # flip the sort order
        # mySortedList: List[str] = theList[::-1]
        return mySortedList

    @staticmethod
    def uniqueList(theList: List[str]) -> List[str]:
        """Returns a list with duplicates removed from the input list.

        This method iterates over the input list and adds each item to a new list
        only if it's not the same as the last item added. This effectively removes
        duplicates from the list, but only if the input list is sorted.

        Args:
            theList (List[str]): The list from which to remove duplicates.

        Returns:
            List[str]: A new list with duplicates removed.

        :param theList: The list from which to remove duplicates.
        :type theList: List[str]
        :return: A new list with duplicates removed.
        :rtype: List[str]
        """
        # remove any duplicates from a sorted list
        myUniqueList: List[str] = []
        myLast: str = ""
        for myCurrent in theList:
            if myCurrent != myLast:
                myUniqueList.append(myCurrent)
            myLast = myCurrent
        return myUniqueList

    @staticmethod
    def getExperimentsList() -> List[str]:
        """Returns a list of all experiment XML files in the model outputs directory.

        This method scans the directory returned by `os.path.expanduser("~/.landuseAnalyst/modelOutputs/")`
        for XML files, each of which is expected to define an experiment.
        Each file's path is added to a list.

        Returns:
            List[str]: A list of the paths of all experiment XML files in the model outputs directory.
            If no experiment files are found, returns an empty list.

        :return: A list of the paths of all experiment XML files.
        :rtype: List[str]
        """
        myExperimentList: List[str] = []
        myWorkDir: str = os.path.expanduser("~/.landuseAnalyst/modelOutputs/")
        for root, dirs, files in os.walk(myWorkDir):
            for file in files:
                if file.endswith(".xml"):
                    myExperimentList.append(os.path.join(root, file))
        return myExperimentList

    @staticmethod
    def createTextFile(theFileName: str, theData: str) -> bool:
        """Creates a text file with the given name and writes the given data to it.

        This method attempts to open a file with the given name in write mode.
        If successful, it writes the given data to the file and returns True.
        If an error occurs (such as if the file cannot be opened), it returns False.

        Args:
            theFileName (str): The name of the file to create.
            theData (str): The data to write to the file.

        Returns:
            bool: True if the file was successfully created and the data was written to it,
            False otherwise.

        :param theFileName: The name of the file to create.
        :type theFileName: str
        :param theData: The data to write to the file.
        :type theData: str
        :return: True if the file was successfully created and the data was written to it, False otherwise.
        :rtype: bool
        """
        # create the txt file
        try:
            with open(theFileName, 'w') as myFile:
                myFile.write(theData)
            return True
        except:
            return False

    @staticmethod
    def xmlEncode(theString: str) -> str:
        """Encodes a string for use in XML.

        This method replaces certain characters in the input string with their
        corresponding XML entities to prevent them from being interpreted as XML markup.
        Specifically, it replaces "<" with "&lt;", ">" with "&gt;", and "&" with "&amp;".

        Args:
            theString (str): The string to encode.

        Returns:
            myEncodedString: The encoded string.

        :param theString: The string to encode.
        :type theString: str
        :return: The encoded string.
        :rtype: str
        """
        myEncodedString = theString.replace("<", "&lt;")
        myEncodedString = myEncodedString.replace(">", "&gt;")
        myEncodedString = myEncodedString.replace("&", "&amp;")
        return myEncodedString

    @staticmethod
    def xmlDecode(theString: str) -> str:
        """Decodes a string from XML encoding.

        This method replaces certain XML entities in the input string with their
        corresponding characters. Specifically, it replaces "&lt;" with "<",
        "&gt;" with ">", and "&amp;" with "&".

        Args:
            theString (str): The string to decode.

        Returns:
            myString: The decoded string.

        :param theString: The string to decode.
        :type theString: str
        :return: The decoded string.
        :rtype: str
        """
        myDecodedString: str = theString.replace("&lt;", "<")
        myDecodedString = myDecodedString.replace("&gt;", ">")
        myDecodedString = myDecodedString.replace("&amp;", "&")
        return myDecodedString

    @staticmethod
    def getStandardCss() -> str:
        """Returns a string of standard CSS styles.

        This method generates a string of CSS styles that can be used to style a webpage or a GUI.
        The styles include definitions for a glossy gradient background, text colors, font sizes,
        table styles, and more.

        Returns:
            str: A string of CSS styles.

        :return: A string of CSS styles.
        :rtype: str
        """
        myStyle: str = ".glossy{"
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
    def getAnimalParameters() -> List[LaAnimalParameter]:
        """Returns a list of all animal parameters.

        This method retrieves all instances of `LaAnimalParameter` by calling the `getInstances` method
        of the `LaAnimalParameter` class.

        Returns:
            List[LaAnimalParameter]: A list of all `LaAnimalParameter` instances.

        :return: A list of all `LaAnimalParameter` instances.
        :rtype: List[LaAnimalParameter]
        """
        myList: List[LaAnimalParameter] = LaAnimalParameter.getInstances()
        return myList

    @staticmethod
    def addAnimalParameter(theAnimalParameter: LaAnimalParameter) -> None:
        """Adds a new animal parameter.

        This method saves a new instance of `LaAnimalParameter` by calling the `save` method
        of the `LaAnimalParameter` instance.

        Args:
            animalParameter (LaAnimalParameter): The `LaAnimalParameter` instance to save.

        :param theAnimalParameter: The `LaAnimalParameter` instance to save.
        :type theAnimalParameter: LaAnimalParameter
        """
        theAnimalParameter.save()

    @staticmethod
    def removeAnimalParameter(theName: str) -> None:
        """Removes an animal parameter by name.

        This method retrieves an instance of `LaAnimalParameter` by its name by calling the
        `getInstanceByName` method of the `LaAnimalParameter` class. If such an instance exists,
        it is removed by calling its `remove` method.

        Args:
            theName (str): The name of the `LaAnimalParameter` instance to remove.

        :param theName: The name of the `LaAnimalParameter` instance to remove.
        :type theName: str
        """
        myAnimalParameter: LaAnimalParameter = LaAnimalParameter.getInstanceByName(theName)
        if myAnimalParameter is not None:
            myAnimalParameter.remove()

    @staticmethod
    def editAnimalParameter(theAnimalParameter: LaAnimalParameter) -> None:
        """Edits an existing animal parameter by saving changes.

        This method saves changes to an existing instance of `LaAnimalParameter` by calling the
        `save` method of the `LaAnimalParameter` instance.

        Args:
            theAnimalParameter (LaAnimalParameter): The `LaAnimalParameter` instance to edit and save.

        :param theAnimalParameter: The `LaAnimalParameter` instance to edit and save.
        :type theAnimalParameter: LaAnimalParameter
        """
        theAnimalParameter.save()

    @staticmethod
    def showInputDialog(theParent: QWidget, theTitle: str, theText: str = "") -> Tuple[str, bool]:
        """Shows an input dialog and returns the entered text and a boolean indicating whether
        the OK button was pressed.

        This method creates a `QInputDialog` with the given parent and title, and an optional
        initial text value. It sets the input mode to text input, and the OK and Cancel button
        texts to "OK" and "Cancel", respectively. It then executes the dialog and returns the
        entered text and a boolean indicating whether the OK button was pressed.

        Args:
            parent (QWidget): The parent widget of the dialog.
            title (str): The title of the dialog.
            text (str, optional): The initial text value of the dialog. Defaults to "".

        Returns:
            Tuple[str, bool]: A tuple where the first element is the entered text and the second
            element is a boolean indicating whether the OK button was pressed.

        :param parent: The parent widget of the dialog.
        :type parent: QWidget
        :param title: The title of the dialog.
        :type title: str
        :param text: The initial text value of the dialog. Defaults to "".
        :type text: str
        :return: A tuple where the first element is the entered text and the second element is a boolean indicating whether the OK button was pressed.
        :rtype: Tuple[str, bool]
        """
        print("showInputDialog")
        myInputDialog: QInputDialog = QInputDialog(theParent)
        myInputDialog.setWindowTitle(theTitle)
        myInputDialog.setTextValue(theText)
        myInputDialog.setLabelText(theTitle)
        myInputDialog.setInputMode(QInputDialog.TextInput)
        myInputDialog.setOkButtonText("OK")
        myInputDialog.setCancelButtonText("Cancel")
        if myInputDialog.exec_() == QInputDialog.Accepted:
            return myInputDialog.textValue(), True
        else:
            return "", False

    @staticmethod
    def showMessageBox(
            theParent: QWidget,
            theTitle: str,
            text: str,
            theIcon: QMessageBox.Icon = QMessageBox.Information
        ) -> None:
        """Shows a message box with the specified title, text, and icon.

        This method creates a `QMessageBox` with the given parent, title, text, and icon.
        It sets the standard buttons to OK and then executes the message box.

        Args:
            theParent (QWidget): The parent widget of the message box.
            ttheTitle (str): The title of the message box.
            theText (str): The text of the message box.
            theIcon (QMessageBox.Icon, optional): The icon of the message box. Defaults to QMessageBox.Information.

        :param parent: The parent widget of the message box.
        :type parent: QWidget
        :param title: The title of the message box.
        :type title: str
        :param text: The text of the message box.
        :type text: str
        :param icon: The icon of the message box. Defaults to QMessageBox.Information.
        :type icon: QMessageBox.Icon
        """
        myMessageBox: QMessageBox = QMessageBox(theParent)
        myMessageBox.setWindowTitle(theTitle)
        myMessageBox.setText(text)
        myMessageBox.setIcon(theIcon)
        myMessageBox.setStandardButtons(QMessageBox.Ok)
        myMessageBox.exec_()

    @staticmethod
    def showColorDialog(
            theParent: QWidget,
            theTitle: str,
            theColor: QColor = QColor()
        ) -> QColor:
        """Shows a color dialog and returns the selected color.

        This method creates a `QColorDialog` with the given parent and title, and an optional
        initial color. It sets the current color to the given color and then executes the dialog.
        If the user presses the OK button, it returns the selected color. If the user presses
        the Cancel button or closes the dialog, it returns the initial color.

        Args:
            theParent (QWidget): The parent widget of the dialog.
            theTitle (str): The title of the dialog.
            theColor (QColor, optional): The initial color of the dialog. Defaults to QColor().

        Returns:
            QColor: The selected color if the OK button was pressed, otherwise the initial color.

        :param theParent: The parent widget of the dialog.
        :type theParent: QWidget
        :param theTitle: The title of the dialog.
        :type theTitle: str
        :param theColor: The initial color of the dialog. Defaults to QColor().
        :type theColor: QColor
        :return: The selected color if the OK button was pressed, otherwise the initial color.
        :rtype: QColor
        """
        myColorDialog: QColorDialog = QColorDialog(theParent)
        myColorDialog.setWindowTitle(theTitle)
        myColorDialog.setCurrentColor(theColor)
        if myColorDialog.exec_() == QColorDialog.Accepted:
            return myColorDialog.selectedColor()
        else:
            return theColor

    @staticmethod
    def generateGuid() -> str:
        """Generates a new GUID.

        This method generates a new globally unique identifier (GUID) string.
        The GUID is composed of 16 characters, each of which is a randomly
        chosen uppercase letter or digit.

        Returns:
            str: The generated GUID.

        :return: The generated GUID.
        :rtype: str
        """
        myNewGuid: str = ''.join(
            random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(16)
        )
        return  myNewGuid

    @staticmethod
    def saveToFile(theFilename: str, theData: str) -> None:
        """Saves data to a file with the specified filename.

        This method creates a `QFile` with the given filename and opens it for writing. If the file
        is successfully opened, it creates a `QTextStream` for the file and writes the data to the file.
        After writing the data, it closes the file.

        Args:
            theFilename (str): The name of the file to write to.
            theData (str): The data to write to the file.

        :param theFilename: The name of the file to write to.
        :type theFilename: str
        :param theData: The data to write to the file.
        :type theData: str
        """
        myFile: QFile = QFile(theFilename)
        if myFile.open(QFile.WriteOnly | QFile.Text):
            myStream: QTextStream = QTextStream(myFile)
            myStream.write(theData)
            myFile.close()

    @staticmethod
    def loadFromFile(theFilename: str) -> str:
        """Loads data from a file with the specified filename.

        This method creates a `QFile` with the given filename and opens it for reading. If the file
        is successfully opened, it creates a `QTextStream` for the file and reads all data from the file.
        After reading the data, it closes the file and returns the data. If the file cannot be opened,
        it returns an empty string.

        Args:
            theFilename (str): The name of the file to read from.

        Returns:
            str: The data read from the file, or an empty string if the file could not be opened.

        :param theFilename: The name of the file to read from.
        :type theFilename: str
        :return: The data read from the file, or an empty string if the file could not be opened.
        :rtype: str
        """
        myFile: QFile = QFile(theFilename)
        if myFile.open(QFile.ReadOnly | QFile.Text):
            myStream: QTextStream = QTextStream(myFile)
            myData: str = myStream.readAll()
            myFile.close()
            return myData
        else:
            return ""

    @staticmethod
    def getApplicationDirPath() -> str:
        """Returns the path to the directory containing the application executable.

        This method retrieves the path to the directory containing the application executable.
        It uses the `os.path.dirname` function with the first command line argument, which is
        typically the path of the script that was invoked.

        Returns:
            str: The path to the directory containing the application executable.

        :return: The path to the directory containing the application executable.
        :rtype: str
        """
        myOsPath: str = os.path.dirname(sys.argv[0])
        return myOsPath

    @staticmethod
    def openGraphicFile() -> str:
        """Opens a file dialog to choose an image file and copies it to the user's images directory.

        This method opens a file dialog that starts at the user's home directory and filters for image files.
        The user can choose an image file to open. The method then copies the chosen file to the user's images
        directory and returns the file path of the copied image file.

        Returns:
            str: The file path of the copied image file.

        :return: The file path of the copied image file.
        :rtype: str
        """
        myHomePath: str = os.path.expanduser("~")
        myFileName: str
        # Since we're only interested in the file name and not the filter,
        # we can ignore the second element with _
        myFileName, _ = QFileDialog.getOpenFileName(
                            None,
                            "Choose an image",
                            myHomePath,
                            "Images (*.png *.xpm *.jpg)"
                        )
        myName: str = os.path.basename(myFileName)
        myDestinationFilePathName: str = os.path.join(
                                            LaUtils.userImagesDirPath(),
                                            myName
                                        )
        shutil.copy(myFileName, myDestinationFilePathName)
        return myDestinationFilePathName

    @staticmethod
    def saveFile() -> str:
        """Opens a file dialog to choose a file name and returns the selected file path.

        This method opens a file dialog that starts at the user's conversion tables directory
        and filters for CSV files. The user can choose a file name to save. The method then
        returns the file path of the chosen file.

        Returns:
            str: The file path of the chosen file.

        :return: The file path of the chosen file.
        :rtype: str
        """
        myFileName: str
        # Since we're only interested in the file name and not the filter,
        # we can ignore the second element with _
        myFileName, _ = QFileDialog.getSaveFileName(
                            None,
                            "Choose a file name",
                            LaUtils.userConversionTablesDirPath(),
                            "*.csv"
                        )
        myName: str = os.path.basename(myFileName)
        myDestinationFilePathName: str = os.path.join(LaUtils.userConversionTablesDirPath(), myName)
        return myDestinationFilePathName
