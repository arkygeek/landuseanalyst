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
import uuid
from builtins import dict as Dict
from builtins import list as List
from typing import Tuple
# Third party imports
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.PyQt.QtCore import QFile, QTextStream, QObject, QDir, QSettings, QFileInfo, pyqtSignal
# Local application imports
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.laanimal import LaAnimal
from la.lib.lacropparameter import LaCropParameter
from la.lib.lacrop import LaCrop

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
    
    This class provides various static methods for getting and manipulating data 
    directories, animal and crop profiles, conversion tables, animal and crop 
    parameter profiles, and images. It also provides methods for encoding and decoding
    XML strings, sorting and removing duplicates from lists, and creating text files.
    """
    @staticmethod
    def userSettingsDirPath() -> str:
        """
        Returns the path to the user settings directory.

        If the directory does not exist, it is created.

        :return: A string representing the path to the user settings directory
        :rtype: str
        """
        # Get the user settings directory path from QSettings
        mySettings = QSettings()
        myPath = mySettings.value("dataDirs/dataDir", QDir.homePath() + "/.landuseAnalyst/")
        # Ensure myPath is a string
        if not isinstance(myPath, str):
            myPath = QDir.homePath() + "/.landuseAnalyst/"
        # Create the directory if it does not exist
        QDir().mkpath(myPath)
        # Return the path to the user settings directory
        return myPath

    @staticmethod
    def getModelOutputDir() -> str:
        """
        Returns the path to the model outputs directory.

        If the directory does not exist, it is created.

        :return: A string representing the path to the model outputs directory
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

        :return: A string representing the path to the animal profiles directory
        :rtype: str
        """
        path = os.path.join(LaUtils.userDataPath(), 'animalProfiles')
        LaUtils.ensureDirectoryExists(path)
        return path

    @staticmethod
    def userCropProfilesDirPath() -> str:
        """
        Returns the path to the crop profiles directory.

        If the directory does not exist, it is created.

        :return: A string representing the path to the crop profiles directory
        :rtype: str
        """
        path = os.path.join(LaUtils.userDataPath(), 'cropProfiles')
        LaUtils.ensureDirectoryExists(path)
        return path

    @staticmethod
    def getAvailableAnimals() -> Dict[str, LaAnimal]:
        """
        Returns a dictionary of available animals.

        The keys are the GUIDs of the animals, and the values are the animal objects.

        :return: A dictionary of available animals
        :rtype: Dict[str, LaAnimal]
        """
        myAnimalsMap = {}
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
                myAnimalsMap[myAnimal.guid] = myAnimal
        return myAnimalsMap

    @staticmethod
    def getAnimal(theGuid: str) -> LaAnimal:
        """
        Returns an animal object with the given GUID.

        If no such animal exists, returns a blank animal.

        :param theGuid: The GUID of the animal to return
        :type theGuid: str
        :return: An animal object
        :rtype: LaAnimal
        """
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
                if myAnimal.guid == theGuid:
                    return myAnimal
        return LaAnimal()

    @staticmethod
    def getAvailableCrops() -> Dict[str, LaCrop]:
        """
        Returns a dictionary of available crops.

        The keys are the GUIDs of the crops, and the values are the crop objects.

        :return: A dictionary of available crops
        :rtype: Dict[str, LaCrop]
        """
        myCropsMap = {}
        myDirectory = QDir(LaUtils.userCropProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Files | QDir.NoSymLinks, QDir.Name)
        print(f"DEBUG: Looking for crops in directory: {LaUtils.userCropProfilesDirPath()}")
        print(f"DEBUG: Found {len(myList)} files")
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our crops listing
            if myFileInfo.completeSuffix() == "xml":
                filePath = myFileInfo.absoluteFilePath()
                print(f"DEBUG: Loading crop from file: {filePath}")
                myCrop = LaCrop()
                loadSuccess = myCrop.fromXmlFile(filePath)
                if not loadSuccess:
                    print(f"DEBUG: Failed to load crop from {filePath}")
                    continue
                if myCrop.name == "":
                    print(f"DEBUG: Crop from {filePath} has no name, skipping")
                    continue
                myCropsMap[myCrop.guid] = myCrop
                print(f"DEBUG: Successfully loaded crop: {myCrop.name}, cropYield: {myCrop.cropYield}")
        print(f"DEBUG: Returning {len(myCropsMap)} crops")
        return myCropsMap

    @staticmethod
    def getCrop(theGuid: str) -> LaCrop:
        """
        Returns a crop object with the given GUID.

        If no such crop exists, returns a blank crop.

        :param theGuid: The GUID of the crop to return
        :type theGuid: str
        :return: A crop object
        :rtype: LaCrop
        """
        myDirectory = QDir(LaUtils.userCropProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myCrop = LaCrop()
                myCrop.fromXmlFile(myFileInfo.absoluteFilePath())
                if myCrop.name == "":
                    continue
                if myCrop.guid == theGuid:
                    return myCrop
        return LaCrop()

    @staticmethod
    def userConversionTablesDirPath() -> str:
        """
        Returns the path to the user's conversion tables directory.

        If the directory does not exist, it will be created.

        :return: The path to the user's conversion tables directory
        :rtype: str
        """
        myPath = QDir.homePath() + "/.landuseAnalyst/conversionTables/"
        QDir().mkpath(myPath)
        return myPath

    @staticmethod
    def userAnimalParameterProfilesDirPath() -> str:
        path = os.path.join(LaUtils.userDataPath(), 'animalParameterProfiles')
        LaUtils.ensureDirectoryExists(path)
        return path

    @staticmethod
    def userImagesDirPath() -> str:
        """
        Returns the path to the user's images directory.

        :return: The path to the user's images directory
        :rtype: str
        """
        myPath = QDir.homePath() + "/.landuseAnalyst/images/"
        QDir().mkpath(myPath)
        return myPath

    @staticmethod
    def userCropParameterProfilesDirPath() -> str:
        """
        Returns the path to the directory where crop parameter profiles are stored.

        Creates the directory if it doesn't exist.

        :return: The path to the directory where crop parameter profiles are stored
        :rtype: str
        """
        import os
        myPath = os.path.join(os.path.expanduser("~"), ".landuseAnalyst", "cropParameterProfiles")
        os.makedirs(myPath, exist_ok=True)
        return myPath

    @staticmethod
    def convertAreaToHectares(theAreaUnit: str, theArea: float) -> int:
        """
        Converts an area in the specified area unit to hectares.

        :param theAreaUnit: The area unit name to use for conversion
        :type theAreaUnit: str
        :param theArea: The area to convert
        :type theArea: float
        :return: The area in hectares
        :rtype: int
        """
        # this may seem ridiculous to do it this way, but
        # i plan to include other area units and this way
        # it will make it very easy to work with in the future
        # all need be done is add new units to la.h enum and add
        # into the following code...
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
        Returns a dictionary of available animal parameters.

        This method scans the directory returned by `userCropProfilesDirPath()`
        for XML files, each of which is expected to define an animal parameter.
        Each file is parsed into an `LaAnimalParameter` object.

        :return: A dictionary of available animal parameters
        :rtype: Dict[str, LaAnimalParameter]
        """
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
                if myAnimalParameter.name == "":
                    continue
                myMap[myAnimalParameter.guid] = myAnimalParameter
        return myMap

    @staticmethod
    def getAnimalParameter(theGuid: str) -> LaAnimalParameter:
        """
        Returns an animal parameter object with the given GUID.

        If no such animal parameter exists, returns a blank animal parameter.

        :param theGuid: The GUID of the animal parameter to return
        :type theGuid: str
        :return: An animal parameter object
        :rtype: LaAnimalParameter
        """
        myDirectory = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Files | QDir.NoSymLinks)
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it into our layerSets listing
            if myFileInfo.completeSuffix() == "xml":
                myAnimalParameter = LaAnimalParameter()
                myAnimalParameter.fromXmlFile(myFileInfo.absoluteFilePath())
                if myAnimalParameter.name == "":
                    continue
                if myAnimalParameter.guid == theGuid:
                    return myAnimalParameter
        return LaAnimalParameter()

    @staticmethod
    def getAvailableCropParameters() -> Dict[str, LaCropParameter]:
        """
        Returns a dictionary of available crop parameters.

        This method scans the directory returned by `userCropParameterProfilesDirPath()`
        for XML files, each of which is expected to define a crop parameter.
        Each file is parsed into an `LaCropParameter` object.

        :return: A dictionary of available crop parameters
        :rtype: Dict[str, LaCropParameter]
        """
        myMap = {}
        myDirectory = QDir(LaUtils.userCropParameterProfilesDirPath())
        myList = myDirectory.entryInfoList(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        print(f"Scanning for crop parameters in: {LaUtils.userCropParameterProfilesDirPath()}")
        print(f"Found {len(myList)} entries")
        for myFileInfo in myList:
            # Ignore directories
            if myFileInfo.fileName() in [".", ".."]:
                continue
            # if the filename ends in .xml try to load it
            if myFileInfo.completeSuffix() == "xml":
                try:
                    filePath = myFileInfo.absoluteFilePath()
                    print(f"Loading crop parameter from: {filePath}")
                    myCropParameter = LaCropParameter()
                    success = myCropParameter.fromXmlFile(filePath)
                    if not success:
                        print(f"Failed to load crop parameter from file: {filePath}")
                        continue
                    if not myCropParameter.name:
                        print(f"Crop parameter from {filePath} has no name, skipping")
                        continue
                    # Debug the parameter values
                    print(f"Loaded crop parameter: '{myCropParameter.name}', percentTameCrop={myCropParameter.percentTameCrop}")
                    myMap[myCropParameter.guid] = myCropParameter
                except Exception as e:
                    print(f"Error loading crop parameter: {str(e)}")
        print(f"Returning {len(myMap)} crop parameters")
        return myMap

    @staticmethod
    def getCropParameter(theGuid: str) -> LaCropParameter:
        """
        Returns a crop parameter object with the given GUID.

        If no such crop parameter exists, returns a blank crop parameter.

        :param theGuid: The GUID of the crop parameter to return
        :type theGuid: str
        :return: A crop parameter object
        :rtype: LaCropParameter
        """
        from la.lib.lacropparameter import LaCropParameter  # Move the import here to avoid circular import
        myCropParameter = LaCropParameter()
        myFilePath = os.path.join(LaUtils.userCropParameterProfilesDirPath(), f"{theGuid}.xml")
        if os.path.exists(myFilePath):
            with open(myFilePath, 'r') as myFile:
                myXmlContent = myFile.read()
                myCropParameter.fromXml(myXmlContent)
        if myCropParameter.name == "":
            return LaCropParameter()
        return myCropParameter

    @staticmethod
    def sortList(theList: List[str]) -> List[str]:
        """
        Sorts a list of strings in descending alphabetical order.

        :param theList: The list of strings to sort
        :type theList: List[str]
        :return: The input list sorted in descending alphabetical order
        :rtype: List[str]
        """
        # sort the taxon list alphabetically descending order
        mySortedList = sorted(theList, reverse=True)  # this sorts descending!
        # TODO use :reverse option of sort() method instead of reversing the list
        # flip the sort order
        # mySortedList: List[str] = theList[::-1]
        return mySortedList

    @staticmethod
    def uniqueList(theList: List[str]) -> List[str]:
        """
        Returns a list with duplicates removed from the input list.

        :param theList: The list from which to remove duplicates
        :type theList: List[str]
        :return: A new list with duplicates removed
        :rtype: List[str]
        """
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
        """
        Returns a list of all experiment XML files in the model outputs directory.

        :return: A list of the paths of all experiment XML files
        :rtype: List[str]
        """
        myExperimentList = []
        myWorkDir = os.path.expanduser("~/.landuseAnalyst/modelOutputs/")
        for root, dirs, files in os.walk(myWorkDir):
            for file in files:
                if file.endswith(".xml"):
                    myExperimentList.append(os.path.join(root, file))
        return myExperimentList

    @staticmethod
    def createTextFile(theFileName: str, theData: str) -> bool:
        """
        Creates a text file with the given name and writes the given data to it.

        :param theFileName: The name of the file to create
        :type theFileName: str
        :param theData: The data to write to the file
        :type theData: str
        :return: True if the file was successfully created and the data was written to it, False otherwise
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
        """
        Encodes a string for use in XML.

        :param theString: The string to encode
        :type theString: str
        :return: The encoded string
        :rtype: str
        """
        myEncodedString = theString.replace("&", "&amp;")
        myEncodedString = myEncodedString.replace("<", "&lt;")
        myEncodedString = myEncodedString.replace(">", "&gt;")
        return myEncodedString

    @staticmethod
    def xmlDecode(theString: str) -> str:
        """
        Decodes a string from XML encoding.

        :param theString: The string to decode
        :type theString: str
        :return: The decoded string
        :rtype: str
        """
        myDecodedString = theString.replace("&lt;", "<")
        myDecodedString = myDecodedString.replace("&gt;", ">")
        myDecodedString = myDecodedString.replace("&amp;", "&")
        return myDecodedString

    @staticmethod
    def getStandardCss() -> str:
        """
        Returns a string of standard CSS styles.

        :return: A string of CSS styles
        :rtype: str
        """
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
    def getAnimalParameters() -> List[LaAnimalParameter]:
        """
        Returns a list of all animal parameters.

        :return: A list of all `LaAnimalParameter` instances
        :rtype: List[LaAnimalParameter]
        """
        myList = LaAnimalParameter.getInstances()
        return myList

    @staticmethod
    def addAnimalParameter(theAnimalParameter: LaAnimalParameter) -> None:
        """
        Adds a new animal parameter.

        :param theAnimalParameter: The `LaAnimalParameter` instance to save
        :type theAnimalParameter: LaAnimalParameter
        """
        theAnimalParameter.save()

    @staticmethod
    def removeAnimalParameter(theName: str) -> None:
        """
        Removes an animal parameter by name.

        :param theName: The name of the `LaAnimalParameter` instance to remove
        :type theName: str
        """
        myAnimalParameter = LaAnimalParameter.getInstanceByName(theName)
        if myAnimalParameter is not None:
            myAnimalParameter.remove()

    @staticmethod
    def editAnimalParameter(theAnimalParameter: LaAnimalParameter) -> None:
        """
        Edits an existing animal parameter by saving changes.

        :param theAnimalParameter: The `LaAnimalParameter` instance to edit and save
        :type theAnimalParameter: LaAnimalParameter
        """
        theAnimalParameter.save()

    @staticmethod
    def generateGuid() -> str:
        """
        Generates a new GUID.

        :return: The generated GUID
        :rtype: str
        """
        return str(uuid.uuid4())

    @staticmethod
    def saveToFile(theFilename: str, theData: str) -> None:
        """
        Saves data to a file with the specified filename.

        :param theFilename: The name of the file to write to
        :type theFilename: str
        :param theData: The data to write to the file
        :type theData: str
        """
        myFile = QFile(theFilename)
        if myFile.open(QFile.WriteOnly | QFile.Text):
            # Encode the string data to bytes and write directly to the file
            myFile.write(theData.encode("utf-8"))
            myFile.close()

    @staticmethod
    def loadFromFile(theFilename: str) -> str:
        """
        Loads data from a file with the specified filename.

        :param theFilename: The name of the file to read from
        :type theFilename: str
        :return: The data read from the file, or an empty string if the file could not be opened
        :rtype: str
        """
        myFile = QFile(theFilename)
        if myFile.open(QFile.ReadOnly | QFile.Text):
            myStream = QTextStream(myFile)
            myData = myStream.readAll()
            myFile.close()
            return myData
        else:
            return ""

    @staticmethod
    def getApplicationDirPath() -> str:
        """
        Returns the path to the directory containing the application executable.

        :return: The path to the directory containing the application executable
        :rtype: str
        """
        myOsPath = os.path.dirname(sys.argv[0])
        return myOsPath

    @staticmethod
    def openGraphicFile() -> str:
        """
        Opens a file dialog to choose an image file and copies it to the user's images directory.

        :return: The file path of the copied image file
        :rtype: str
        """
        myHomePath = QDir.homePath()
        myFileName, _ = QFileDialog.getOpenFileName(None, "Choose an image", myHomePath, "Images (*.png *.xpm *.jpg)")
        if not myFileName:
            return ""
        fi = QFileInfo(myFileName)
        myName = fi.fileName()
        myDestinationFilePathName = LaUtils.userImagesDirPath() + "/" + myName
        QFile.copy(myFileName, myDestinationFilePathName)
        return myDestinationFilePathName

    @staticmethod
    def saveFile() -> str:
        """
        Opens a file dialog to choose a file name and returns the selected file path.

        :return: The file path of the chosen file
        :rtype: str
        """
        myHomePath = QDir.homePath()
        myFileName, _ = QFileDialog.getSaveFileName(None, "Choose a file name", LaUtils.userConversionTablesDirPath(), "*.csv")
        if not myFileName:
            return ""
        fi = QFileInfo(myFileName)
        myName = fi.fileName()
        myDestinationFilePathName = LaUtils.userConversionTablesDirPath() + "/" + myName
        return myDestinationFilePathName

    @staticmethod
    def resolvePath(path: str, fileType: str = None) -> str:
        """
        Resolve path across platforms maintaining consistency with C++ version.

        :param path: The path to resolve
        :type path: str
        :param fileType: The type of file (optional)
        :type fileType: str
        :return: The resolved path
        :rtype: str
        """
        # If path exists as-is, use it (matches original C++ behavior)
        if path and os.path.exists(path):
            return path
        # If not found as absolute path, try user data directory
        basename = os.path.basename(path) if path else ''
        if not basename:
            return ""
        # Define standard locations based on original C++ structure
        userDataPath = os.path.join(os.path.expanduser('~'), '.landuseAnalyst')
        # Try standard locations
        if fileType == 'image':
            userPath = os.path.join(userDataPath, 'images', basename)
            if os.path.exists(userPath):
                return userPath
        # Try resource path as fallback (matching Qt resource system)
        resourcePath = f":/images/{basename}"
        return resourcePath

    @staticmethod
    def userDataPath() -> str:
        """
        Returns the path to the user's data directory.

        :return: The path to the user's data directory
        :rtype: str
        """
        home = os.path.expanduser('~')
        base_dir = '.landuseAnalyst'
        return os.path.join(home, base_dir)

    @staticmethod
    def ensureDirectoryExists(path: str) -> str:
        """
        Ensures that the directory exists, creating it if necessary.

        :param path: The path to the directory
        :type path: str
        :return: The path to the directory
        :rtype: str
        """
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def saveFilePath(sourceFile: str, fileType: str) -> str:
        """
        Returns a path where a file should be saved based on its type.

        :param sourceFile: The source file
        :type sourceFile: str
        :param fileType: The type of file
        :type fileType: str
        :return: The path where the file should be saved
        :rtype: str
        """
        subdir = {
            'image': 'images',
            'crop': 'cropProfiles',
            'cropParameter': 'cropParameterProfiles',
            'animal': 'animalProfiles',
            'animalParameter': 'animalParameterProfiles'
        }.get(fileType, '')
        target_dir = os.path.join(LaUtils.userDataPath(), subdir)
        LaUtils.ensureDirectoryExists(target_dir)
        return os.path.join(target_dir, os.path.basename(sourceFile))
