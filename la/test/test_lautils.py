import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Update sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the LaUtils class
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop

class TestLaUtils(unittest.TestCase):
    myTestNumber = 1

    @patch('la.lib.lautils.QSettings')
    @patch('la.lib.lautils.os.makedirs')
    def test_userSettingsDirPath(self, mock_makedirs, mock_qsettings):
        print(f"Test number {self.myTestNumber}: userSettingsDirPath")
        # Mock the QSettings value method
        mock_settings_instance = MagicMock()
        mock_settings_instance.value.return_value = '/mock/path/to/settings'
        mock_qsettings.return_value = mock_settings_instance
        # Call the static method
        result = LaUtils.userSettingsDirPath()
        # Assert the expected path is returned
        self.assertEqual(result, '/mock/path/to/settings')
        # Assert the directory creation was called
        mock_makedirs.assert_called_once_with('/mock/path/to/settings', exist_ok=True)

    @patch('la.lib.lautils.os.makedirs')
    def test_userSettingsDirPath_default(self, mock_makedirs):
        # Mock the QSettings value method to return None
        with patch('la.lib.lautils.QSettings') as mock_qsettings:
            mock_settings_instance = MagicMock()
            mock_settings_instance.value.return_value = None
            mock_qsettings.return_value = mock_settings_instance
            # Call the static method
            result = LaUtils.userSettingsDirPath()
            # Assert the default path is returned
            self.assertEqual(result, os.path.expanduser("~/.landuseAnalyst/"))
            # Assert the directory creation was called
            mock_makedirs.assert_called_once_with(os.path.expanduser("~/.landuseAnalyst/"), exist_ok=True)

    @patch('la.lib.lautils.os.makedirs')
    @patch('la.lib.lautils.LaUtils.userSettingsDirPath', return_value='/mock/path/to/settings')
    def test_getModelOutputDir(self, mock_userSettingsDirPath, mock_makedirs):
        # Call the static method
        result = LaUtils.getModelOutputDir()
        # Assert the expected path is returned
        self.assertEqual(result, '/mock/path/to/settings/modelOutputs')
        # Assert the directory creation was called
        mock_makedirs.assert_called_once_with('/mock/path/to/settings/modelOutputs', exist_ok=True)

    @patch('la.lib.lautils.os.makedirs')
    def test_userAnimalProfilesDirPath(self, mock_makedirs):
        # Call the static method
        result = LaUtils.userAnimalProfilesDirPath()

        # Assert the expected path is returned
        expected_path = os.path.expanduser("~/.landuseAnalyst/animalProfiles")
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_makedirs.assert_called_once_with(expected_path, exist_ok=True)

    @patch('la.lib.lautils.os.makedirs')
    def test_userCropProfilesDirPath(self, mock_makedirs):
        # Call the static method
        result = LaUtils.userCropProfilesDirPath()

        # Assert the expected path is returned
        expected_path = os.path.expanduser("~/.landuseAnalyst/cropProfiles")
        self.assertEqual(result, expected_path)

        # Assert the directory creation was called
        mock_makedirs.assert_called_once_with(expected_path, exist_ok=True)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalProfilesDirPath')
    def test_getAvailableAnimals(self, theMockDirPath, theMockQDir):
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

    # @patch('la.lib.lautils.QDir')
    # @patch('la.lib.lautils.LaUtils.userCropProfilesDirPath')
    # def test_getCrop(self, theMockDirPath, theMockQDir):
    #     self.maxDiff = None  # Allow full diff to be displayed
    #     # Set up the directory containing the XML files
    #     myTestDir = os.path.join(os.path.dirname(__file__), 'xmlData', 'cropProfiles')
    #     theMockDirPath.return_value = myTestDir

    #     # Mock the QDir and QFileInfo
    #     myMockDir = MagicMock()
    #     theMockQDir.return_value = myMockDir
    #     myMockFileInfoList = []
    #     for myFilename in os.listdir(myTestDir):
    #         if myFilename.endswith(".xml"):
    #             myMockFileInfo = MagicMock()
    #             myMockFileInfo.fileName.return_value = myFilename
    #             myMockFileInfo.completeSuffix.return_value = "xml"
    #             myMockFileInfo.absoluteFilePath.return_value = os.path.join(myTestDir, myFilename)
    #             myMockFileInfoList.append(myMockFileInfo)
    #     myMockDir.entryInfoList.return_value = myMockFileInfoList

    #     # Load all crops and print XML contents
    #     myCropsDict = {}
    #     for myFilename in os.listdir(myTestDir):
    #         if myFilename.endswith(".xml"):
    #             myFilepath = os.path.join(myTestDir, myFilename)
    #             myCrop = LaCrop()
    #             with open(myFilepath, 'r') as myFile:
    #                 myXmlContent = myFile.read()
    #                 myCrop.fromXml(myXmlContent)
    #                 # myGuid = myCrop.guid()  # Use the guid attribute as a string
    #                 myGuid = myFilename.split('.')[0]  # Assuming the file name is the guid
    #                 myCropsDict[myGuid] = myCrop

    #                 # Print the XML file contents
    #                 print(f"Contents of {myFilename}:\n{myXmlContent}\n")

    #     # Test getting each crop by GUID
    #     print("Test getting each crop by GUID \n")
    #     for myGuid, myExpectedCrop in myCropsDict.items():
    #         myResult = LaUtils.getCrop(myGuid)
    #         self.assertEqual(myResult, myExpectedCrop)

    #     # Test getting a crop with a non-existent GUID
    #     myNonExistantGuid = "non-existent-guid"
    #     myResult = LaUtils.getCrop(myNonExistantGuid)
    #     self.assertEqual(myResult.name, "No Name Set")


if __name__ == '__main__':
    class CustomTestRunner(unittest.TextTestRunner):
        def run(self, test):
            result = super().run(test)
            if result.wasSuccessful():
                print("All tests passed successfully!")
            return result

    unittest.main(testRunner=CustomTestRunner())