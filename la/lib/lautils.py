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
from typing import Dict, List, Tuple, TYPE_CHECKING
import sys
# Third party imports
from qgis.PyQt.QtWidgets import (
    QFileDialog
)
from qgis.PyQt.QtCore import QFile, QTextStream, QObject, QDir, QSettings, QFileInfo, pyqtSignal
# Local application imports
from la.lib.la import AreaUnits
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.laanimal import LaAnimal
from la.lib.lacropparameter import LaCropParameter

if TYPE_CHECKING:  # pragma: no cover - avoids the lacrop <-> lautils import cycle
    from la.lib.lacrop import LaCrop

# from la.gui.ladebugdialog import LaDebugDialog
# from la.lib.lacrop import LaCrop

class LaMessageBus(QObject):
    """Message bus for communication between components."""
    debugMessaged = pyqtSignal(str)  # Signal emitted when debug messages are logged

    def debug(self, theMessage: str, theComponent: str = "General") -> None:
        """
        Emit ``debugMessaged`` for ``theMessage``.

        Convenience wrapper so callers (notably the test-suite) can log without
        going through :class:`LaDebugLogger`.

        :param theMessage: Text to broadcast.
        :param theComponent: Component tag prefixed to the message.
        """
        self.debugMessaged.emit(f"{theComponent}: {theMessage}")

# Create a global instance of the message bus that can be imported
MESSAGE_BUS = LaMessageBus()


class LaDebugLogger:
    """Debug logger with component filtering support."""
    mHistory = []  # List of tuples (component, message)
    mKnownComponents = set()  # Track all unique component types
    mMaxHistory = 25000  # Maximum number of messages to keep in history

    def __init__(self):
        self.mEnabled = False
        self.mShowLineNumbers = False

    def setEnabled(self, theDebugEnabledBool: bool):
        """Enable or disable debug logging.

        Args:
            theBool: Boolean indicating whether debug logging should be enabled
        """
        self.mEnabled = theDebugEnabledBool

    def isEnabled(self) -> bool:
        """Return whether debug logging is enabled.

        Returns:
            bool: True if debug logging is enabled, False otherwise
        """
        return self.mEnabled

    def log(self, theMessage: str, theComponent: str = "General"):
        """Log a debug message with component type.

        Args:
            theMessage: The message to log
            theComponent: The component/category of the message (e.g., "Error", "Diet", "Calcs")
        """
        # Track the component type
        self.mKnownComponents.add(theComponent)

        # Add to history
        self.mHistory.append((theComponent, theMessage))
        if len(self.mHistory) > self.mMaxHistory:
            self.mHistory = self.mHistory[-self.mMaxHistory:]

        # Print the message
        if self.mEnabled or theComponent == "Error":
            print(f"[{theComponent}] {theMessage}")

        # Emit the signal via MESSAGE_BUS if available
        try:
            MESSAGE_BUS.debugMessaged.emit(f"{theComponent}: {theMessage}")
        except:
            pass

    def getComponents(self) -> list:
        """Get a sorted list of all known message components/categories.

        Returns:
            List of unique component names
        """
        return sorted(self.mKnownComponents)

    def getHistory(self, component_filter: str = None, with_line_numbers: bool = False) -> list:
        """Get the message history with optional filtering and line numbers.

        Args:
            component_filter: If provided, only return messages of this component type
            with_line_numbers: Whether to include line numbers in the output

        Returns:
            List of formatted log messages
        """
        # Filter messages by component if requested
        myFilteredHistory = [
            (myComp, myMsg) for myComp, myMsg in self.mHistory
            if component_filter is None or myComp == component_filter
        ]

        # Format the messages
        if with_line_numbers:
            return [
                f'<span style="color:red">{i}:</span> {comp}: {msg}'
                for i, (comp, msg) in enumerate(myFilteredHistory, 1)
            ]
        else:
            return [f"{comp}: {msg}" for comp, msg in myFilteredHistory]


class LaUtils:
    """
    A utility class for Land Use Analyst.

    This class provides various static methods for getting and manipulating data
    directories, animal and crop profiles, conversion tables, animal and crop
    parameter profiles, and images. It also provides methods for encoding and decoding
    XML strings, sorting and removing duplicates from lists, and creating text files.
    """
    # Initialize the debug logger
    debug = LaDebugLogger()

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

    # ------------------------------------------------------------------
    # Profile catalogue cache
    # ------------------------------------------------------------------
    # Every getX()/getAvailableX() used to re-scan its directory and re-parse
    # every XML file on each call; the calculation engine calls them dozens
    # of times per run and the UI on every slider tick. We now cache the raw
    # XML text per directory, keyed by a cheap (name, mtime, size) signature
    # from os.scandir, and build fresh objects from the cached text so that
    # callers can never mutate a shared instance.
    _mProfileTextCache: Dict[str, Tuple[tuple, Dict[str, str]]] = {}

    @staticmethod
    def _directorySignature(theDirPath: str) -> tuple:
        """(name, mtime_ns, size) for every .xml file in ``theDirPath``, sorted by name."""
        try:
            myEntries = []
            for myEntry in os.scandir(theDirPath):
                if myEntry.is_file() and myEntry.name.lower().endswith(".xml"):
                    myStat = myEntry.stat()
                    myEntries.append((myEntry.name, myStat.st_mtime_ns, myStat.st_size))
        except OSError:
            return ()
        return tuple(sorted(myEntries))

    @staticmethod
    def _profileTexts(theDirPath: str) -> Dict[str, str]:
        """Map of ``filename → xml text`` for ``theDirPath``, served from cache when unchanged."""
        LaUtils.ensureDirectoryExists(theDirPath)
        mySignature = LaUtils._directorySignature(theDirPath)
        myCached = LaUtils._mProfileTextCache.get(theDirPath)
        if myCached is not None and myCached[0] == mySignature:
            return myCached[1]
        myTexts: Dict[str, str] = {}
        for myName, _, _ in mySignature:
            myPath = os.path.join(theDirPath, myName)
            try:
                with open(myPath, "r", encoding="utf-8") as myFile:
                    myTexts[myName] = myFile.read()
            except OSError as e:
                LaUtils.debug.log(f"Could not read profile {myPath}: {e}", "Warning")
        LaUtils._mProfileTextCache[theDirPath] = (mySignature, myTexts)
        return myTexts

    @staticmethod
    def _loadProfiles(theDirPath: str, theFactory, theComponent: str) -> Dict[str, object]:
        """
        Build ``guid → object`` for every valid profile in ``theDirPath``.

        :param theDirPath: Directory holding one XML file per profile.
        :param theFactory: Zero-argument callable returning a fresh, empty object
            with ``fromXml``/``name``/``guid``.
        :param theComponent: Debug-log component tag.
        """
        myMap: Dict[str, object] = {}
        for myFileName, myText in LaUtils._profileTexts(theDirPath).items():
            myObject = theFactory()
            try:
                myObject.fromXml(myText)
            except Exception as e:  # malformed profile: skip, never abort the catalogue
                LaUtils.debug.log(f"Failed to parse {myFileName}: {e}", theComponent)
                continue
            if not getattr(myObject, "name", ""):
                continue
            myGuid = str(getattr(myObject, "guid", "") or "") or os.path.splitext(myFileName)[0]
            myMap[myGuid] = myObject
        return myMap

    @staticmethod
    def invalidateProfileCache() -> None:
        """Drop the cached profile texts (call after writing profiles programmatically)."""
        LaUtils._mProfileTextCache.clear()

    @staticmethod
    def _findProfile(theDirPath: str, theFactory, theGuid: str, theComponent: str):
        """Return the profile whose GUID (or file stem) is ``theGuid``, else a blank object."""
        myMap = LaUtils._loadProfiles(theDirPath, theFactory, theComponent)
        myObject = myMap.get(str(theGuid))
        if myObject is not None:
            return myObject
        for myFileName in LaUtils._profileTexts(theDirPath):
            if os.path.splitext(myFileName)[0] == str(theGuid):
                myCandidate = theFactory()
                myCandidate.fromXml(LaUtils._profileTexts(theDirPath)[myFileName])
                if getattr(myCandidate, "name", ""):
                    return myCandidate
        return theFactory()

    @staticmethod
    def getAvailableAnimals() -> Dict[str, LaAnimal]:
        """
        Returns a dictionary of available animals keyed by GUID.

        :rtype: Dict[str, LaAnimal]
        """
        return LaUtils._loadProfiles(LaUtils.userAnimalProfilesDirPath(), LaAnimal, "Animals")

    @staticmethod
    def getAnimal(theGuid: str) -> LaAnimal:
        """
        Returns the animal with the given GUID, or a blank ``LaAnimal`` if none exists.

        :param theGuid: The GUID of the animal to return
        :rtype: LaAnimal
        """
        return LaUtils._findProfile(LaUtils.userAnimalProfilesDirPath(), LaAnimal, theGuid, "Animals")

    @staticmethod
    def getAvailableCrops() -> Dict[str, "LaCrop"]:
        """
        Returns a dictionary of available crops keyed by GUID.

        :rtype: Dict[str, LaCrop]
        """
        from la.lib.lacrop import LaCrop
        return LaUtils._loadProfiles(LaUtils.userCropProfilesDirPath(), LaCrop, "Crops")

    @staticmethod
    def getCrop(theGuid: str) -> "LaCrop":
        """
        Returns the crop with the given GUID, or a blank ``LaCrop`` if none exists.

        :param theGuid: The GUID of the crop to return
        :rtype: LaCrop
        """
        from la.lib.lacrop import LaCrop
        return LaUtils._findProfile(LaUtils.userCropProfilesDirPath(), LaCrop, theGuid, "Crops")

    @staticmethod
    def userConversionTablesDirPath() -> str:
        """
        Returns the path to the user's conversion tables directory.

        If the directory does not exist, it will be created.

        :return: The path to the user's conversion tables directory
        :rtype: str
        """
        myPath = os.path.join(LaUtils.userDataPath(), "conversionTables")
        LaUtils.ensureDirectoryExists(myPath)
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
        myPath = os.path.join(LaUtils.userDataPath(), "images")
        LaUtils.ensureDirectoryExists(myPath)
        return myPath

    @staticmethod
    def userCropParameterProfilesDirPath() -> str:
        """
        Returns the path to the directory where crop parameter profiles are stored.

        Creates the directory if it doesn't exist.

        :return: The path to the directory where crop parameter profiles are stored
        :rtype: str
        """
        myPath = os.path.join(LaUtils.userDataPath(), "cropParameterProfiles")
        LaUtils.ensureDirectoryExists(myPath)
        return myPath

    @staticmethod
    def convertAreaToHectares(theAreaUnit: AreaUnits, theArea: int) -> int:
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
        myHectares: float = 0.
        if theAreaUnit == AreaUnits.Dunum:
            myHectares = float(theArea) * 10.
        elif theAreaUnit == AreaUnits.Hectare:
            myHectares = theArea
        # add new units here after updating la.h enum ex:
        # elif theAreaUnit == "Acre":
        #     myHectares = theArea / 2.47105381
        # TODO check why this value is an int. I think it should be a float.
        return int(myHectares)

    @staticmethod
    def getAvailableAnimalParameters() -> Dict[str, LaAnimalParameter]:
        """
        Returns a dictionary of available animal parameter sets keyed by GUID.

        :rtype: Dict[str, LaAnimalParameter]
        """
        return LaUtils._loadProfiles(
            LaUtils.userAnimalParameterProfilesDirPath(), LaAnimalParameter, "AnimalParams"
        )

    @staticmethod
    def getAnimalParameter(theGuid: str) -> LaAnimalParameter:
        """
        Returns the animal parameter set with the given GUID, or a blank one if none exists.

        :param theGuid: The GUID of the animal parameter to return
        :rtype: LaAnimalParameter
        """
        return LaUtils._findProfile(
            LaUtils.userAnimalParameterProfilesDirPath(), LaAnimalParameter, theGuid, "AnimalParams"
        )

    @staticmethod
    def getAvailableCropParameters() -> Dict[str, LaCropParameter]:
        """
        Returns a dictionary of available crop parameter sets keyed by GUID.

        :rtype: Dict[str, LaCropParameter]
        """
        return LaUtils._loadProfiles(
            LaUtils.userCropParameterProfilesDirPath(), LaCropParameter, "CropParams"
        )

    @staticmethod
    def getCropParameter(theGuid: str) -> LaCropParameter:
        """
        Returns the crop parameter set with the given GUID, or a blank one if none exists.

        :param theGuid: The GUID of the crop parameter to return
        :rtype: LaCropParameter
        """
        return LaUtils._findProfile(
            LaUtils.userCropParameterProfilesDirPath(), LaCropParameter, theGuid, "CropParams"
        )

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
    def resolvePath(path: str, type: str = '') -> str:
        """Resolve a path to a resource, searching in multiple possible locations.

        Args:
            path: The path or filename to resolve
            type: The type of resource ('image', 'data', etc.)

        Returns:
            str: The full resolved path if found, otherwise the original path
        """
        if not path:
            return path

        # If it's already an absolute path and exists, return it
        if os.path.isabs(path) and os.path.exists(path):
            return path

        # Get the filename only
        filename = os.path.basename(path)

        # List of possible directories to search in
        search_paths = []

        if type.lower() == 'image':
            # Add image-specific paths
            search_paths.extend([
                LaUtils.userImagesDirPath(),
                os.path.join(LaUtils.userProfilesDirPath(), 'images'),
                os.path.join(LaUtils.pluginPath(), 'images')
            ])

        # Add general paths
        search_paths.extend([
            LaUtils.userProfilesDirPath(),
            LaUtils.pluginPath()
        ])

        # Search for the file
        for search_path in search_paths:
            full_path = os.path.join(search_path, filename)
            if os.path.exists(full_path):
                LaUtils.debug.log(f"Found resource at: {full_path}")
                return full_path

        # If not found, return original path
        LaUtils.debug.log(f"Could not resolve path: {path}", "Warning")
        return path

    @staticmethod
    def userDataPath() -> str:
        """
        Returns the path to the user's data directory.

        :return: The path to the user's data directory
        :rtype: str
        """
        # Single source of truth: the QSettings-backed settings dir (default
        # ~/.landuseAnalyst/), normalised without a trailing separator so the
        # per-profile helpers can os.path.join onto it.
        return os.path.normpath(LaUtils.userSettingsDirPath())

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

    @staticmethod
    def userProfilesDirPath() -> str:
        """Returns the path to user profiles directory."""
        return os.path.join(LaUtils.userSettingsDirPath(), "profiles")

    @staticmethod
    def pluginPath() -> str:
        """Returns the path to the plugin directory."""
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def get_message_history() -> List[str]:
        """Returns the debug message history."""
        return LaDebugLogger.mHistory.copy()

    @staticmethod
    def userImagesPaths() -> List[str]:
        """Returns a list of paths where images may be located."""
        paths = [
            LaUtils.userImagesDirPath(),  # User's images directory
            os.path.join(LaUtils.userDataPath(), 'images'),  # User data images
            os.path.join(LaUtils.pluginPath(), 'images')  # Plugin images
        ]
        return [p for p in paths if os.path.exists(p)]

    @staticmethod
    def resolveImagePath(filename: str) -> str:
        """Resolve the path to an image file by searching in multiple locations.

        Args:
            filename: Name of the image file to find

        Returns:
            Full path to the image if found, empty string if not found
        """
        if not filename:
            return ""

        # If it's an absolute path and exists, return it
        if os.path.isabs(filename) and os.path.exists(filename):
            return filename

        # Search in each images directory
        for path in LaUtils.userImagesPaths():
            full_path = os.path.join(path, filename)
            if os.path.exists(full_path):
                LaUtils.debug.log(f"Found image at: {full_path}")
                return full_path

        LaUtils.debug.log(f"Could not find image: {filename}")
        return ""

    @staticmethod
    def getDebugDialog(parent=None):
        """Returns the debug dialog singleton instance.
        
        Args:
            parent: Optional parent widget for the dialog
            
        Returns:
            LaDebugDialog: The debug dialog instance
        """
        from la.gui.ladebugdialog import LaDebugDialog
        return LaDebugDialog.get_instance(parent)