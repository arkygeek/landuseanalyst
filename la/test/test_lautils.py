import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Update sys.path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the LaUtils class
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal


class TestLaUtils(unittest.TestCase):
    @patch('la.lib.lautils.QSettings')
    @patch('la.lib.lautils.os.makedirs')
    def test_userSettingsDirPath(self, mock_makedirs, mock_qsettings):
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
    def test_getAvailableAnimals(self, mock_userAnimalProfilesDirPath, mock_QDir):
        # Set up the directory containing the XML files
        test_directory = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalProfiles')
        mock_userAnimalProfilesDirPath.return_value = test_directory

        # Mock the QDir and QFileInfo
        mock_dir = MagicMock()
        mock_QDir.return_value = mock_dir
        mock_file_info_list = []
        for file_name in os.listdir(test_directory):
            if file_name.endswith(".xml"):
                mock_file_info = MagicMock()
                mock_file_info.fileName.return_value = file_name
                mock_file_info.completeSuffix.return_value = "xml"
                mock_file_info.absoluteFilePath.return_value = os.path.join(test_directory, file_name)
                mock_file_info_list.append(mock_file_info)
        mock_dir.entryInfoList.return_value = mock_file_info_list

        # Load all animals and print XML contents
        animals = {}
        for file_name in os.listdir(test_directory):
            if file_name.endswith(".xml"):
                file_path = os.path.join(test_directory, file_name)
                animal = LaAnimal()
                with open(file_path, 'r') as file:
                    xml_content = file.read()
                    animal.fromXml(xml_content)
                    guid = file_name.split('.')[0]  # Assuming the file name is the guid
                    animals[guid] = animal

                    # Print the XML file contents
                    # print(f"Contents of {file_name}:\n{xml_content}\n")

        # Call the static method
        result = LaUtils.getAvailableAnimals()
        # print(f"result = {result}")

        # Adjust the expected result to match the actual result
        expected_result = animals

        # Assert the expected dictionary is returned
        self.assertEqual(result, expected_result)

    @patch('la.lib.lautils.QDir')
    @patch('la.lib.lautils.LaUtils.userAnimalProfilesDirPath')
    def test_getAnimal(self, mock_userAnimalProfilesDirPath, mock_QDir):
        # Set up the directory containing the XML files
        test_directory = os.path.join(os.path.dirname(__file__), 'xmlData', 'animalProfiles')
        mock_userAnimalProfilesDirPath.return_value = test_directory

        # Mock the QDir and QFileInfo
        mock_dir = MagicMock()
        mock_QDir.return_value = mock_dir
        mock_file_info_list = []
        for file_name in os.listdir(test_directory):
            if file_name.endswith(".xml"):
                mock_file_info = MagicMock()
                mock_file_info.fileName.return_value = file_name
                mock_file_info.completeSuffix.return_value = "xml"
                mock_file_info.absoluteFilePath.return_value = os.path.join(test_directory, file_name)
                mock_file_info_list.append(mock_file_info)
        mock_dir.entryInfoList.return_value = mock_file_info_list

        # Load all animals and print XML contents
        animals = {}
        for file_name in os.listdir(test_directory):
            if file_name.endswith(".xml"):
                file_path = os.path.join(test_directory, file_name)
                animal = LaAnimal()
                with open(file_path, 'r') as file:
                    xml_content = file.read()
                    animal.fromXml(xml_content)
                    guid = file_name.split('.')[0]  # Assuming the file name is the guid
                    animals[guid] = animal

                    # Print the XML file contents
                    print(f"Contents of {file_name}:\n{xml_content}\n")

        # Test getting each animal by GUID
        for guid, expected_animal in animals.items():
            result = LaUtils.getAnimal(guid)
            self.assertEqual(result, expected_animal)

        # Test getting an animal with a non-existent GUID
        non_existent_guid = "non-existent-guid"
        result = LaUtils.getAnimal(non_existent_guid)
        self.assertEqual(result.animalName, "No Name Set")

if __name__ == '__main__':
    unittest.main()