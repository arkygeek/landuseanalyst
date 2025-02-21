import sys
import os
import unittest
import uuid
from unittest.mock import patch, MagicMock, mock_open
from qgis.PyQt.QtWidgets import QWidget, QInputDialog, QApplication  # Add this import
from qgis.PyQt.QtCore import QDir

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
        result = LaUtils.userSettingsDirPath()

        # Assert the default path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        theMockMakePath.assert_called_once_with(expected_path)

    @patch('la.lib.lautils.os.makedirs')
    @patch('la.lib.lautils.LaUtils.userSettingsDirPath', return_value='/mock/path/to/settings')
    def test_getModelOutputDir(self, mock_userSettingsDirPath, mock_makedirs):
        print(f"Test number 3: getModelOutputDir")
        # Call the static method
        result = LaUtils.getModelOutputDir()
        # Assert the expected path is returned
        self.assertEqual(result, '/mock/path/to/settings/modelOutputs')
        # Assert the directory creation was called
        mock_makedirs.assert_called_once_with('/mock/path/to/settings/modelOutputs', exist_ok=True)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userAnimalProfilesDirPath(self, mock_mkpath):
        print(f"Test number 4: userAnimalProfilesDirPath")
        # Call the static method
        result = LaUtils.userAnimalProfilesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/animalProfiles/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userCropProfilesDirPath(self, mock_mkpath):
        print(f"Test number 5: userCropProfilesDirPath")
        # Call the static method
        result = LaUtils.userCropProfilesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/cropProfiles/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)


    @patch('la.lib.lautils.QDir.mkpath')
    def test_userConversionTablesDirPath(self, mock_mkpath):
        print(f"Test number 6: userConversionTablesDirPath")
        # Call the static method
        result = LaUtils.userConversionTablesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/conversionTables/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userAnimalParameterProfilesDirPath(self, mock_mkpath):
        print(f"Test number 7: userAnimalParameterProfilesDirPath")
        # Call the static method
        result = LaUtils.userAnimalParameterProfilesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/animalParameterProfiles/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userImagesDirPath(self, mock_mkpath):
        print(f"Test number 8: userImagesDirPath")
        # Call the static method
        result = LaUtils.userImagesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/images/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)

    @patch('la.lib.lautils.QDir.mkpath')
    def test_userCropParameterProfilesDirPath(self, mock_mkpath):
        print(f"Test number 9: userCropParameterProfilesDirPath")
        # Call the static method
        result = LaUtils.userCropParameterProfilesDirPath()

        # Assert the expected path is returned
        expected_path = QDir.homePath() + "/.landuseAnalyst/cropParameterProfiles/"
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_mkpath.assert_called_once_with(expected_path)

    def test_convertAreaToHectares(self):
        print(f"Test number 10: convertAreaToHectares")
        # Test conversion from Dunum to Hectares
        result = LaUtils.convertAreaToHectares("Dunum", 5)
        self.assertEqual(result, 50)

        # Test conversion from Hectares to Hectares
        result = LaUtils.convertAreaToHectares("Hectare", 5)
        self.assertEqual(result, 5)

        # Test conversion with an unknown area unit (should return 0)
        result = LaUtils.convertAreaToHectares("Unknown", 5)
        self.assertEqual(result, 0)

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
        print(f"animal result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myAnimalsDict
        print(f"expected animals = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalProfilesDirPath')
    def test_getAnimal(self, theMockDirPath, theMockQDir):
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each animal by GUID
        for myGuid, myExpectedAnimal in myAnimalsDict.items():
            result = LaUtils.getAnimal(myGuid)
            self.assertEqual(result, myExpectedAnimal)

        # Test getting an animal with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        result = LaUtils.getAnimal(non_existent_guid)
        self.assertEqual(result.name, "No Name Set")

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalParameterProfilesDirPath')
    def test_getAvailableAnimalParameters(self, theMockDirPath, theMockQDir):
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Call the static method
        myResult = LaUtils.getAvailableAnimalParameters()
        print(f"animal parameter result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myAnimalParametersDict
        print(f"expected animal parameters = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)


    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropProfilesDirPath')
    def test_getAvailableCrops(self, theMockDirPath, theMockQDir):
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")
                    print(f"\n\n\n myGuid = {myGuid}")
                    print(f"\n myCropsDict = {myCropsDict}")
        # Call the static method
        myResult = LaUtils.getAvailableCrops()
        print(f"crop result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myCropsDict
        print(f"expected crops = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropProfilesDirPath')
    def test_getCrop(self, theMockDirPath, theMockQDir):
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each crop by GUID
        print("Test getting each crop by GUID \n")
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each animal parameter by GUID
        for myGuid, myExpectedAnimalParameter in myAnimalParametersDict.items():
            result = LaUtils.getAnimalParameter(myGuid)
            self.assertEqual(result, myExpectedAnimalParameter)

        # Test getting an animal parameter with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        result = LaUtils.getAnimalParameter(non_existent_guid)
        self.assertEqual(result.name, "No Name Set")

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropParameterProfilesDirPath')
    def test_getAvailableCropParameters(self, mock_userCropParameterProfilesDirPath, mock_QDir):
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropParameterProfiles')
        mock_userCropParameterProfilesDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        mock_QDir.return_value = myMockDir
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Call the static method
        myResult = LaUtils.getAvailableCropParameters()
        print(f"crop parameter result = {myResult}")

        # Adjust the expected result to match the actual result
        myExpectedResult = myCropParametersDict
        print(f"expected crop parameters = {myExpectedResult}")
        # Assert the expected dictionary is returned
        self.assertEqual(myResult, myExpectedResult)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userCropParameterProfilesDirPath')
    def test_getCropParameter(self, mock_userCropParameterProfilesDirPath, mock_QDir):
        # Set up the directory containing the XML files
        myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropParameterProfiles')
        mock_userCropParameterProfilesDirPath.return_value = myTestDir

        # Mock the QDir and QFileInfo
        myMockDir = MagicMock()
        mock_QDir.return_value = myMockDir
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
                    print(f"Contents of {myFilename}:\n{myXmlContent}\n")

        # Test getting each crop parameter by GUID
        for myGuid, myExpectedCropParameter in myCropParametersDict.items():
            result = LaUtils.getCropParameter(myGuid)
            self.assertEqual(result, myExpectedCropParameter)

        # Test getting a crop parameter with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        result = LaUtils.getCropParameter(non_existent_guid)
        self.assertEqual(result.name, "No Name Set")

    def test_sortList(self):
        # Test sorting a list of strings in descending alphabetical order
        input_list = ["banana", "apple", "cherry", "date"]
        expected_output = ["date", "cherry", "banana", "apple"]
        result = LaUtils.sortList(input_list)
        self.assertEqual(result, expected_output)

        # Test sorting an already sorted list
        input_list = ["date", "cherry", "banana", "apple"]
        expected_output = ["date", "cherry", "banana", "apple"]
        result = LaUtils.sortList(input_list)
        self.assertEqual(result, expected_output)

        # Test sorting a list with duplicate elements
        input_list = ["banana", "apple", "cherry", "banana", "date"]
        expected_output = ["date", "cherry", "banana", "banana", "apple"]
        result = LaUtils.sortList(input_list)
        self.assertEqual(result, expected_output)

    def test_uniqueList(self):
        # Test removing duplicates from a sorted list
        input_list = ["apple", "banana", "banana", "cherry", "date", "date"]
        expected_output = ["apple", "banana", "cherry", "date"]
        result = LaUtils.uniqueList(input_list)
        self.assertEqual(result, expected_output)

        # Test removing duplicates from an already unique list
        input_list = ["apple", "banana", "cherry", "date"]
        expected_output = ["apple", "banana", "cherry", "date"]
        result = LaUtils.uniqueList(input_list)
        self.assertEqual(result, expected_output)

        # Test removing duplicates from an empty list
        input_list = []
        expected_output = []
        result = LaUtils.uniqueList(input_list)
        self.assertEqual(result, expected_output)

        # Test removing duplicates from a list with one element
        input_list = ["apple"]
        expected_output = ["apple"]
        result = LaUtils.uniqueList(input_list)
        self.assertEqual(result, expected_output)

    @patch('os.path.expanduser')
    @patch('os.walk')
    def test_getExperimentsList(self, mock_os_walk, mock_expanduser):
        # Mock the expanduser method to return a specific directory
        mock_expanduser.return_value = '/mocked/home/.landuseAnalyst/modelOutputs/'

        # Mock the os.walk method to return a specific directory structure
        mock_os_walk.return_value = [
            ('/mocked/home/.landuseAnalyst/modelOutputs/', ('subdir',), ('experiment1.xml', 'experiment2.xml')),
            ('/mocked/home/.landuseAnalyst/modelOutputs/subdir', (), ('experiment3.xml',))
        ]

        expected_output = [
            '/mocked/home/.landuseAnalyst/modelOutputs/experiment1.xml',
            '/mocked/home/.landuseAnalyst/modelOutputs/experiment2.xml',
            '/mocked/home/.landuseAnalyst/modelOutputs/subdir/experiment3.xml'
        ]
        result = LaUtils.getExperimentsList()
        self.assertEqual(result, expected_output)

    @patch('builtins.open', new_callable=mock_open)
    def test_createTextFile(self, mock_open):
        # Test creating a text file and writing data to it
        file_name = 'test_file.txt'
        data = 'This is a test.'

        result = LaUtils.createTextFile(file_name, data)
        self.assertTrue(result)
        mock_open.assert_called_once_with(file_name, 'w')
        mock_open().write.assert_called_once_with(data)

        # Test handling an exception when creating a text file
        mock_open.side_effect = IOError
        result = LaUtils.createTextFile(file_name, data)
        self.assertFalse(result)

    def test_xmlEncode(self):
        # Test encoding a string with special characters
        input_string = "<test>&string"
        expected_output = "&lt;test&gt;&amp;string"
        result = LaUtils.xmlEncode(input_string)
        self.assertEqual(result, expected_output)

        # Test encoding a string without special characters
        input_string = "normalstring"
        expected_output = "normalstring"
        result = LaUtils.xmlEncode(input_string)
        self.assertEqual(result, expected_output)

        # Test encoding an empty string
        input_string = ""
        expected_output = ""
        result = LaUtils.xmlEncode(input_string)
        self.assertEqual(result, expected_output)

    def test_xmlDecode(self):
        # Test decoding a string with XML entities
        input_string = "&lt;test&gt;&amp;string"
        expected_output = "<test>&string"
        result = LaUtils.xmlDecode(input_string)
        self.assertEqual(result, expected_output)

        # Test decoding a string without XML entities
        input_string = "normalstring"
        expected_output = "normalstring"
        result = LaUtils.xmlDecode(input_string)
        self.assertEqual(result, expected_output)

        # Test decoding an empty string
        input_string = ""
        expected_output = ""
        result = LaUtils.xmlDecode(input_string)
        self.assertEqual(result, expected_output)

    def test_getStandardCss(self):
        # Test that the getStandardCss method returns the expected CSS string
        expected_output = (
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
        result = LaUtils.getStandardCss()
        self.assertEqual(result, expected_output)



    @patch('la.lib.laanimalparameter.LaAnimalParameter.getInstances')
    def test_getAnimalParameters(self, mock_getInstances):
        # Mock the getInstances method to return a list of LaAnimalParameter instances
        mock_animal_parameter_1 = MagicMock(spec=LaAnimalParameter)
        mock_animal_parameter_2 = MagicMock(spec=LaAnimalParameter)
        mock_getInstances.return_value = [mock_animal_parameter_1, mock_animal_parameter_2]
        result = LaUtils.getAnimalParameters()
        self.assertEqual(result, [mock_animal_parameter_1, mock_animal_parameter_2])
        mock_getInstances.assert_called_once()

    @patch.object(LaAnimalParameter, 'save')
    def test_addAnimalParameter(self, mock_save):
        # Create a mock LaAnimalParameter instance
        mock_animal_parameter = MagicMock(spec=LaAnimalParameter)
        # Call the addAnimalParameter method
        LaUtils.addAnimalParameter(mock_animal_parameter)
        # Verify that the save method was called on the mock instance
        mock_animal_parameter.save.assert_called_once_with()

    @patch.object(LaAnimalParameter, 'save')
    def test_editAnimalParameter(self, mock_save):
        # Create a mock LaAnimalParameter instance
        mock_animal_parameter = MagicMock(spec=LaAnimalParameter)
        # Call the editAnimalParameter method
        LaUtils.editAnimalParameter(mock_animal_parameter)
        # Verify that the save method was called on the mock instance
        mock_animal_parameter.save.assert_called_once_with()

    @patch.object(LaAnimalParameter, 'remove')
    @patch('la.lib.laanimalparameter.LaAnimalParameter.getInstanceByName')
    def test_removeAnimalParameter(self, mock_getInstanceByName, mock_remove):
        # Create a mock LaAnimalParameter instance
        mock_animal_parameter = MagicMock(spec=LaAnimalParameter)
        mock_getInstanceByName.return_value = mock_animal_parameter
        # Call the removeAnimalParameter method
        LaUtils.removeAnimalParameter("TestName")
        # Verify that the getInstanceByName method was called with the correct argument
        mock_getInstanceByName.assert_called_once_with("TestName")
        # Verify that the remove method was called on the mock instance
        mock_animal_parameter.remove.assert_called_once_with()


    def test_LaTripleMap(self):
        # Create a LaTripleMap instance
        la_triple_map: LaTripleMap = {
            "animal1": (True, "param1"),
            "animal2": (False, "param2")
        }

        # Verify the contents of the LaTripleMap
        self.assertEqual(la_triple_map["animal1"], (True, "param1"))
        self.assertEqual(la_triple_map["animal2"], (False, "param2"))


    def test_generateGuid(self):
        # Call the generateGuid method
        result = LaUtils.generateGuid()

        # Verify that the result is a valid UUID
        try:
            uuid_obj = uuid.UUID(result, version=4)
        except ValueError:
            self.fail("generateGuid did not return a valid UUID")

        # Verify that the result is a string
        self.assertIsInstance(result, str)

    @patch('la.lib.lautils.QFileDialog.getOpenFileName')
    @patch('la.lib.lautils.QFile.copy')
    @patch('la.lib.lautils.LaUtils.userImagesDirPath', return_value=QDir.homePath() + "/.landuseAnalyst/images")
    def test_openGraphicFile(self, mock_userImagesDirPath, mock_copy, mock_getOpenFileName):
        # Mock the QFileDialog.getOpenFileName method
        mock_getOpenFileName.return_value = ("/mock/path/to/image.png", "")

        # Call the openGraphicFile method
        result = LaUtils.openGraphicFile()

        # Verify the result
        expected_path = QDir.homePath() + "/.landuseAnalyst/images/image.png"
        self.assertEqual(result, expected_path)

        # Verify that the QFileDialog.getOpenFileName method was called with the correct arguments
        mock_getOpenFileName.assert_called_once_with(None, "Choose an image", QDir.homePath(), "Images (*.png *.xpm *.jpg)")

        # Verify that the QFile.copy method was called with the correct arguments
        mock_copy.assert_called_once_with("/mock/path/to/image.png", expected_path)

    @patch('la.lib.lautils.QFileDialog.getSaveFileName')
    @patch('la.lib.lautils.LaUtils.userConversionTablesDirPath', return_value=QDir.homePath() + "/.landuseAnalyst/conversionTables")
    def test_saveFile(self, mock_userConversionTablesDirPath, mock_getSaveFileName):
        # Mock the QFileDialog.getSaveFileName method
        mock_getSaveFileName.return_value = ("/Users/arkygeek/.landuseAnalyst/conversionTables/file.csv", "")

        # Call the saveFile method
        result = LaUtils.saveFile()

        # Verify the result
        expected_path = QDir.homePath() + "/.landuseAnalyst/conversionTables/file.csv"
        self.assertEqual(result, expected_path)

        # Verify that the QFileDialog.getSaveFileName method was called with the correct arguments
        mock_getSaveFileName.assert_called_once_with(None, "Choose a file name", QDir.homePath() + "/.landuseAnalyst/conversionTables", "*.csv")



if __name__ == '__main__':
    class CustomTestRunner(unittest.TextTestRunner):
        def run(self, test):
            result = super().run(test)
            if result.wasSuccessful():
                print("All tests passed successfully!")
            return result

    unittest.main(testRunner=CustomTestRunner())