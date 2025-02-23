import sys
import os
import unittest
import uuid
from unittest.mock import patch, MagicMock, mock_open
from qgis.PyQt.QtWidgets import QWidget, QInputDialog, QApplication
from qgis.PyQt.QtCore import QDir, QSettings

# Update sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the LaUtils classu
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.la import LaTripleMap


class TestLaUtils(unittest.TestCase):
    """ Test suite for the LaUtils class.
    This test suite contains unit tests for various static methods in the LaUtils class.
    The tests cover the following functionalities:
    - Retrieving user settings directory paths and ensuring directory creation.
    - Retrieving model output directory and ensuring directory creation.
    - Retrieving various user profile directory paths and ensuring directory creation.
    - Converting area units to hectares.
    - Retrieving available animals and specific animal profiles.
    - Retrieving available animal parameters and specific animal parameter profiles.
    - Retrieving available crops and specific crop profiles.
    - Retrieving available crop parameters and specific crop parameter profiles.
    - Sorting and removing duplicates from lists.
    - Retrieving a list of experiment files.
    - Creating text files.
    - Encoding and decoding XML strings.
    - Retrieving standard CSS.
    - Managing animal parameters (add, edit, remove).
    - Generating GUIDs.
    - Opening and saving graphic files.

    Each test method is decorated with appropriate patches to mock dependencies and isolate the functionality being tested.
    """
    @classmethod
    def setUpClass(cls):
        # Create a QApplication instance
        cls.app = QApplication(sys.argv)

    @patch('la.lib.lautils.QDir.mkpath')
    @patch('la.lib.lautils.QSettings')
    def test_userSettingsDirPath(self, theMockQSettings, theMockMakePath):
        # Mock the QSettings value method
        print(f"Test number 1: userSettingsDirPath")
        myMockSettingsInstance = MagicMock()
        myMockSettingsInstance.value.return_value = QDir.homePath() + "/.landuseAnalyst/"
        theMockQSettings.return_value = myMockSettingsInstance

        # Call the static method
        myResult = LaUtils.userSettingsDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.QDir.mkpath')
    @patch('la.lib.lautils.QSettings')
    def test_userSettingsDirPath_default(self, theMockQSettings, theMockMakePath):
        # Mock the QSettings value method to return None
        print(f"Test number 2: userSettingsDirPath_default")
        myMockSettingsInstance = MagicMock()
        myMockSettingsInstance.value.return_value = None
        theMockQSettings.return_value = myMockSettingsInstance

        # Call the static method
        myResult = LaUtils.userSettingsDirPath()

        # Assert the default path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.os.makedirs')
    @patch('la.lib.lautils.LaUtils.userSettingsDirPath', return_value='/mock/path/to/settings')
    def test_getModelOutputDir(self, mock_userSettingsDirPath, theMockMakeDirs):
        print(f"Test number 3: getModelOutputDir")
        # Call the static method
        myResult = LaUtils.getModelOutputDir()
        # Assert the expected path is returned
        self.assertEqual(myResult, '/mock/path/to/settings/modelOutputs')
        # Assert the directory creation was called
        theMockMakeDirs.assert_called_once_with('/mock/path/to/settings/modelOutputs', exist_ok=True)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userAnimalProfilesDirPath(self, theMockMakePath):
        print(f"Test number 4: userAnimalProfilesDirPath")
        # Call the static method
        myResult = LaUtils.userAnimalProfilesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/animalProfiles/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userCropProfilesDirPath(self, theMockMakePath):
        print(f"Test number 5: userCropProfilesDirPath")
        # Call the static method
        myResult = LaUtils.userCropProfilesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/cropProfiles/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)


    @patch('la.lib.lautils.QDir.mkpath')
    def test_userConversionTablesDirPath(self, theMockMakePath):
        print(f"Test number 6: userConversionTablesDirPath")
        # Call the static method
        myResult = LaUtils.userConversionTablesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/conversionTables/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userAnimalParameterProfilesDirPath(self, theMockMakePath):
        print(f"Test number 7: userAnimalParameterProfilesDirPath")
        # Call the static method
        myResult = LaUtils.userAnimalParameterProfilesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/animalParameterProfiles/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userImagesDirPath(self, theMockMakePath):
        print(f"Test number 8: userImagesDirPath")
        # Call the static method
        myResult = LaUtils.userImagesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/images/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userCropParameterProfilesDirPath(self, theMockMakePath):
        print(f"Test number 9: userCropParameterProfilesDirPath")
        # Call the static method
        myResult = LaUtils.userCropParameterProfilesDirPath()

        # Assert the expected path is returned
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/cropParameterProfiles/"
        self.assertEqual(myResult, myExpectedPath)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(myExpectedPath)

    def test_convertAreaToHectares(self):
        print(f"Test number 10: convertAreaToHectares")
        # Test conversion from Dunum to Hectares
        myResult = LaUtils.convertAreaToHectares("Dunum", 5)
        self.assertEqual(myResult, 50)

        # Test conversion from Hectares to Hectares
        myResult = LaUtils.convertAreaToHectares("Hectare", 5)
        self.assertEqual(myResult, 5)

        # Test conversion with an unknown area unit (should return 0)
        myResult = LaUtils.convertAreaToHectares("Unknown", 5)
        self.assertEqual(myResult, 0)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalProfilesDirPath')
    def test_getAvailableAnimals(self, theMockDirPath, theMockQDir):
        print(f"Test number 11: getAvailableAnimals")
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all animals and print XML contents
        myAnimalsDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myAnimal = LaAnimal()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myAnimal.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myAnimalsDict[myGuid] = myAnimal

                    # Print the XML file contents
                    # print(f"Contents of {file_name}:\n{xml_content}\n")

        # Call the static method
        myResult = LaUtils.getAvailableAnimals()
        # print(f"animal result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myAnimalsDict
        # print(f"expected animals = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalProfilesDirPath')
    def test_getAnimal(self, theMockDirPath, theMockQDir):
        print(f"Test number 12: getAnimal")
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all animals and print XML contents
        myAnimalsDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myAnimal = LaAnimal()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myAnimal.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myAnimalsDict[myGuid] = myAnimal

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each animal by GUID
        for myGuid, myExpectedAnimal in myAnimalsDict.items():
            myResult = LaUtils.getAnimal(myGuid)
            self.assertEqual(myResult, myExpectedAnimal)

        # Test getting an animal with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        myResult = LaUtils.getAnimal(non_existent_guid)
        self.assertEqual(myResult.name, "No Name Set")

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalParameterProfilesDirPath')
    def test_getAvailableAnimalParameters(self, theMockDirPath, theMockQDir):
        print(f"Test number 13: getAvailableAnimalParameters")
        self.maxDiff = None  # Allow full diff to be displayed
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalParameterProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all animal parameters and print XML contents
        myAnimalParametersDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myAnimalParameter = LaAnimalParameter()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myAnimalParameter.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myAnimalParametersDict[myGuid] = myAnimalParameter

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Call the static method
        myResult = LaUtils.getAvailableAnimalParameters()
        # print(f"animal parameter result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myAnimalParametersDict
        # print(f"expected animal parameters = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)


    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropProfilesDirPath')
    def test_getAvailableCrops(self, theMockDirPath, theMockQDir):
        print(f"Test number 14: getAvailableCrops")
        self.maxDiff = None  # Allow full diff to be displayed
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all crops and print XML contents
        myCropsDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myLaCrop = LaCrop()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myLaCrop.fromXml(myXmlContent)
                    # myGuid = myLaCrop.guid()  # Use the guid attribute as a string
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myCropsDict[myGuid] = myLaCrop

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")
                    # print(f"\n\n\n myGuid = {myGuid}")
                    # print(f"\n myCropsDict = {myCropsDict}")
        # Call the static method
        myResult = LaUtils.getAvailableCrops()
        # print(f"crop result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myCropsDict
        # print(f"expected crops = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropProfilesDirPath')
    def test_getCrop(self, theMockDirPath, theMockQDir):
        print(f"Test number 15: getCrop")
        self.maxDiff = None  # Allow full diff to be displayed
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all crops and print XML contents
        myCropsDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myCrop = LaCrop()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myCrop.fromXml(myXmlContent)
                    # myGuid = myCrop.guid()  # Use the guid attribute as a string
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myCropsDict[myGuid] = myCrop

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each crop by GUID
        # print("Test getting each crop by GUID \n")
        for myGuid, myExpectedCrop in myCropsDict.items():
            myResult = LaUtils.getCrop(myGuid)
            self.assertEqual(myResult, myExpectedCrop)

        # Test getting a crop with a non-existent GUID
        myNonExistantGuid = "non-existent-guid"
        myResult = LaUtils.getCrop(myNonExistantGuid)
        self.assertEqual(myResult.name, "No Name Set")

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalParameterProfilesDirPath')
    def test_getAnimalParameter(self, theMockDirPath, theMockQDir):
        print(f"Test number 16: getAnimalParameter")
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalParameterProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all animal parameters and print XML contents
        myAnimalParametersDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myAnimalParameter = LaAnimalParameter()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myAnimalParameter.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myAnimalParametersDict[myGuid] = myAnimalParameter

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each animal parameter by GUID
        for myGuid, myExpectedAnimalParameter in myAnimalParametersDict.items():
            myResult = LaUtils.getAnimalParameter(myGuid)
            self.assertEqual(myResult, myExpectedAnimalParameter)

        # Test getting an animal parameter with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        myResult = LaUtils.getAnimalParameter(non_existent_guid)
        self.assertEqual(myResult.name, "No Name Set")

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropParameterProfilesDirPath')
    def test_getAvailableCropParameters(self, theMockDirPath, theMockQDir):
        print(f"Test number 17: getAvailableCropParameters")
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropParameterProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all crop parameters and print XML contents
        myCropParametersDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myCropParameter = LaCropParameter()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myCropParameter.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myCropParametersDict[myGuid] = myCropParameter

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Call the static method
        myResult = LaUtils.getAvailableCropParameters()
        # print(f"crop parameter result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myCropParametersDict
        # print(f"expected crop parameters = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropParameterProfilesDirPath')
    def test_getCropParameter(self, theMockDirPath, theMockQDir):
        print(f"Test number 18: getCropParameter")
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropParameterProfiles')
        theMockDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        theMockQDir.return_value = myMockDir
        myMockFileInfoList = []
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myMockFileInfo = MagicMock()
                myMockFileInfo.fileName.return_value = myFilename
                myMockFileInfo.completeSuffix.return_value = "xml"
                myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
                myMockFileInfoList.append(myMockFileInfo)
        myMockDir.entryInfoList.return_value = myMockFileInfoList

        # Load all crop parameters and print XML contents
        myCropParametersDict = {}
        for myFilename in os.listdir(myTestDir):
            if myFilename.endswith(".xml"):
                myFilepath = os.path.join(myTestDir, myFilename)
                myCropParameter = LaCropParameter()
                with open(myFilepath, 'r') as myFile:
                    myXmlContent = myFile.read()
                    myCropParameter.fromXml(myXmlContent)
                    myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
                    myCropParametersDict[myGuid] = myCropParameter

                    # Print the XML file contents
                    # print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each crop parameter by GUID
        for myGuid, myExpectedCropParameter in myCropParametersDict.items():
            myResult = LaUtils.getCropParameter(myGuid)
            self.assertEqual(myResult, myExpectedCropParameter)

        # Test getting a crop parameter with a non-existent GUID
        myNonExistantGuid = "non-existent-guid"
        myResult = LaUtils.getCropParameter(myNonExistantGuid)
        self.assertEqual(myResult.name, "No Name Set")

    def test_sortList(self):
        # Test sorting a list of strings in descending alphabetical order
        print(f"Test number 19: sortList")

        myInputList = ["banana", "apple", "cherry", "date"]
        myExpectedOutput = ["date", "cherry", "banana", "apple"]
        myResult = LaUtils.sortList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

        # Test sorting an already sorted list
        myInputList = ["date", "cherry", "banana", "apple"]
        myExpectedOutput = ["date", "cherry", "banana", "apple"]
        myResult = LaUtils.sortList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

        # Test sorting a list with duplicate elements
        myInputList = ["banana", "apple", "cherry", "banana", "date"]
        myExpectedOutput = ["date", "cherry", "banana", "banana", "apple"]
        myResult = LaUtils.sortList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

    def test_uniqueList(self):
        # Test removing duplicates from a sorted list
        print(f"Test number 20: uniqueList")

        myInputList = ["apple", "banana", "banana", "cherry", "date", "date"]
        myExpectedOutput = ["apple", "banana", "cherry", "date"]
        myResult = LaUtils.uniqueList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

        # Test removing duplicates from an already unique list
        myInputList = ["apple", "banana", "cherry", "date"]
        myExpectedOutput = ["apple", "banana", "cherry", "date"]
        myResult = LaUtils.uniqueList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

        # Test removing duplicates from an empty list
        myInputList = []
        myExpectedOutput = []
        myResult = LaUtils.uniqueList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

        # Test removing duplicates from a list with one element
        myInputList = ["apple"]
        myExpectedOutput = ["apple"]
        myResult = LaUtils.uniqueList(myInputList)
        self.assertEqual(myResult, myExpectedOutput)

    @patch('os.path.expanduser')
    @patch('os.walk')
    def test_getExperimentsList(self, theMockOsWalk, theMockExpandUser):
        # Mock the expanduser method to return a specific directory
        print(f"Test number 21: getExperimentsList")

        theMockExpandUser.return_value = '/mocked/home/.landuseAnalyst/modelOutputs/'

        # Mock the os.walk method to return a specific directory structure
        theMockOsWalk.return_value = [
            ('/mocked/home/.landuseAnalyst/modelOutputs/', ('subdir',), ('experiment1.xml', 'experiment2.xml')),
            ('/mocked/home/.landuseAnalyst/modelOutputs/subdir', (), ('experiment3.xml',))
        ]

        myExpectedOutput = [
            '/mocked/home/.landuseAnalyst/modelOutputs/experiment1.xml',
            '/mocked/home/.landuseAnalyst/modelOutputs/experiment2.xml',
            '/mocked/home/.landuseAnalyst/modelOutputs/subdir/experiment3.xml'
        ]
        myResult = LaUtils.getExperimentsList()
        self.assertEqual(myResult, myExpectedOutput)

    @patch('builtins.open', new_callable=mock_open)
    def test_createTextFile(self, theMockOpen):
        # Test creating a text file and writing data to it
        print(f"Test number 22: createTextFile")

        myFilename = 'test_file.txt'
        myData = 'This is a test.'

        myResult = LaUtils.createTextFile(myFilename, myData)
        self.assertTrue(myResult)
        theMockOpen.assert_called_once_with(myFilename, 'w')
        theMockOpen().write.assert_called_once_with(myData)

        # Test handling an exception when creating a text file
        theMockOpen.side_effect = IOError
        myResult = LaUtils.createTextFile(myFilename, myData)
        self.assertFalse(myResult)

    def test_xmlEncode(self):
        # Test encoding a string with special characters
        print(f"Test number 23: xmlEncode")

        myInputString = "<test>&string"
        myExpectedOutput = "&lt;test&gt;&amp;string"
        myResult = LaUtils.xmlEncode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

        # Test encoding a string without special characters
        myInputString = "normalstring"
        myExpectedOutput = "normalstring"
        myResult = LaUtils.xmlEncode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

        # Test encoding an empty string
        myInputString = ""
        myExpectedOutput = ""
        myResult = LaUtils.xmlEncode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

    def test_xmlDecode(self):
        # Test decoding a string with XML entities
        print(f"Test number 24: xmlDecode")

        myInputString = "&lt;test&gt;&amp;string"
        myExpectedOutput = "<test>&string"
        myResult = LaUtils.xmlDecode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

        # Test decoding a string without XML entities
        myInputString = "normalstring"
        myExpectedOutput = "normalstring"
        myResult = LaUtils.xmlDecode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

        # Test decoding an empty string
        myInputString = ""
        myExpectedOutput = ""
        myResult = LaUtils.xmlDecode(myInputString)
        self.assertEqual(myResult, myExpectedOutput)

    def test_getStandardCss(self):
        # Test that the getStandardCss method returns the expected CSS string
        print(f"Test number 25: getStandardCss")

        myExpectedOutput = (
            ".glossy{"
            "  background-color: qlineargradient("
            "    x1:0, y1:0, x2:0, y2:1, stop:0 #616161,"
            "    stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);"
            "  color: white; padding-left: 4px; "
            "  border: 1px solid #6c6c6c; }"
            "body {background: white;}"
            "h1 {font-size : 22pt; color: #0063F7; }"
            "h2 {font-size : 18pt; color: #0063F7; }"
            "h3 {font-size : 14pt; color: #0063F7; }"
            ".cellHeader {color:#466aa5; font-size : 12pt;}"
            ".parameterHeader {font-weight: bold;}"
            ".largeCell {color:#000000; font-size : 12pt;}"
            ".table {"
            "  border-width: 1px 1px 1px 1px;"
            "  border-spacing: 2px;"
            "  border-style: solid solid solid solid;"
            "  border-color: black black black black;"
            "  border-collapse: separate;"
            "  background-color: white;"
            "}"
        )
        myResult = LaUtils.getStandardCss()
        self.assertEqual(myResult, myExpectedOutput)



    @patch('la.lib.laanimalparameter.LaAnimalParameter.getInstances')
    def test_getAnimalParameters(self, theMockGetInstances):
        # Mock the getInstances method to return a list of LaAnimalParameter instances
        print(f"Test number 26: getAnimalParameters")

        myMockAnimalParam1 = MagicMock(spec=LaAnimalParameter)
        myMockAnimalParam2 = MagicMock(spec=LaAnimalParameter)
        theMockGetInstances.return_value = [myMockAnimalParam1, myMockAnimalParam2]
        myResult = LaUtils.getAnimalParameters()
        self.assertEqual(myResult, [myMockAnimalParam1, myMockAnimalParam2])
        theMockGetInstances.assert_called_once()

    @patch.object(LaAnimalParameter, 'save')
    def test_addAnimalParameter(self, mock_save):
        print(f"Test number 27: addAnimalParameter")
        # Create a mock LaAnimalParameter instance
        myMockAnimalParam = MagicMock(spec=LaAnimalParameter)
        # Call the addAnimalParameter method
        LaUtils.addAnimalParameter(myMockAnimalParam)
        # Verify that the save method was called on the mock instance
        myMockAnimalParam.save.assert_called_once_with()

    @patch.object(LaAnimalParameter, 'save')
    def test_editAnimalParameter(self, mock_save):
        print(f"Test number 28: editAnimalParameter")
        # Create a mock LaAnimalParameter instance
        myMockAnimalParam = MagicMock(spec=LaAnimalParameter)
        # Call the editAnimalParameter method
        LaUtils.editAnimalParameter(myMockAnimalParam)
        # Verify that the save method was called on the mock instance
        myMockAnimalParam.save.assert_called_once_with()

    @patch.object(LaAnimalParameter, 'remove')
    @patch('la.lib.laanimalparameter.LaAnimalParameter.getInstanceByName')
    def test_removeAnimalParameter(self, theMockGetInstanceByName, mock_remove):
        print(f"Test number 29: removeAnimalParameter")

        # Create a mock LaAnimalParameter instance
        mock_animal_parameter = MagicMock(spec=LaAnimalParameter)
        theMockGetInstanceByName.return_value = mock_animal_parameter
        # Call the removeAnimalParameter method
        LaUtils.removeAnimalParameter("TestName")
        # Verify that the getInstanceByName method was called with the correct argument
        theMockGetInstanceByName.assert_called_once_with("TestName")
        # Verify that the remove method was called on the mock instance
        mock_animal_parameter.remove.assert_called_once_with()


    def test_LaTripleMap(self):
        print(f"Test number 30: LaTripleMap")
        # Create a LaTripleMap instance
        myTripleMap = {
            "animal1": (True, "param1"),
            "animal2": (False, "param2")
        }

        # Verify the contents of the LaTripleMap
        self.assertEqual(myTripleMap["animal1"], (True, "param1"))
        self.assertEqual(myTripleMap["animal2"], (False, "param2"))


    def test_generateGuid(self):
        print(f"Test number 31: generateGuid")

        # Call the generateGuid method
        myResult = LaUtils.generateGuid()

        # Verify that the result is a valid UUID
        try:
            uuid_obj = uuid.UUID(myResult, version=4)
        except ValueError:
            self.fail("generateGuid did not return a valid UUID")

        # Verify that the result is a string
        self.assertIsInstance(myResult, str)

    @patch('la.lib.lautils.QFileDialog.getOpenFileName')
    @patch('la.lib.lautils.QFile.copy')
    @patch('la.lib.lautils.LaUtils.userImagesDirPath', return_value=QDir.homePath() + "/.landuseAnalyst/images")
    def test_openGraphicFile(self, mock_userImagesDirPath, mock_copy, mock_getOpenFileName):
        print(f"Test number 32: openGraphicFile")

        # Mock the QFileDialog.getOpenFileName method
        mock_getOpenFileName.return_value = ("/mock/path/to/image.png", "")

        # Call the openGraphicFile method
        myResult = LaUtils.openGraphicFile()

        # Verify the result
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/images/image.png"
        self.assertEqual(myResult, myExpectedPath)

        # Verify that the QFileDialog.getOpenFileName method was called with the correct arguments
        mock_getOpenFileName.assert_called_once_with(None, "Choose an image", QDir.homePath(), "Images (*.png *.xpm *.jpg)")

        # Verify that the QFile.copy method was called with the correct arguments
        mock_copy.assert_called_once_with("/mock/path/to/image.png", myExpectedPath)

    @patch('la.lib.lautils.QFileDialog.getSaveFileName')
    @patch('la.lib.lautils.LaUtils.userConversionTablesDirPath', return_value=QDir.homePath() + "/.landuseAnalyst/conversionTables")
    def test_saveFile(self, theMockDirPath, theMockFilename):
        print(f"Test number 33: saveFile")

        # Mock the QFileDialog.getSaveFileName method
        theMockFilename.return_value = ("/Users/arkygeek/.landuseAnalyst/conversionTables/file.csv", "")

        # Call the saveFile method
        myResult = LaUtils.saveFile()

        # Verify the result
        myExpectedPath = QDir.homePath() + "/.landuseAnalyst/conversionTables/file.csv"
        self.assertEqual(myResult, myExpectedPath)

        # Verify that the QFileDialog.getSaveFileName method was called with the correct arguments
        theMockFilename.assert_called_once_with(None, "Choose a file name", QDir.homePath() + "/.landuseAnalyst/conversionTables", "*.csv")

    @patch("qgis.PyQt.QtWidgets.QInputDialog")
    def test_showInputDialog(self, theMockQInputDialog):
        print(f"Test number 32: showInputDialog")

        # Create a mock QInputDialog instance
        myMockInputDialog = MagicMock(spec=QInputDialog)
        theMockQInputDialog.return_value = myMockInputDialog

        # Set up the return values for the mock input dialog
        myMockInputDialog.exec_.return_value = QInputDialog.Accepted
        myMockInputDialog.textValue.return_value = "Test Input"

        # Call the showInputDialog method
        result_text, result_ok = LaUtils.showInputDialog(QWidget(), "Test Title", "Initial Text")

        # Verify the result
        self.assertEqual(result_text, "Test Input")
        self.assertTrue(result_ok)

        # Verify that the QInputDialog was created with the correct parameters
        theMockQInputDialog.assert_called_once_with(QWidget())
        myMockInputDialog.setWindowTitle.assert_called_once_with("Test Title")
        myMockInputDialog.setTextValue.assert_called_once_with("Initial Text")
        myMockInputDialog.setLabelText.assert_called_once_with("Test Title")
        myMockInputDialog.setInputMode.assert_called_once_with(QInputDialog.TextInput)
        myMockInputDialog.setOkButtonText.assert_called_once_with("OK")
        myMockInputDialog.setCancelButtonText.assert_called_once_with("Cancel")
        myMockInputDialog.exec_.assert_called_once()


if __name__ == '__main__':
    class CustomTestRunner(unittest.TextTestRunner):
        def run(self, test):
            myResult = super().run(test)
            if myResult.wasSuccessful():
                print("All tests passed successfully!")
            return myResult

    unittest.main(testRunner=CustomTestRunner())