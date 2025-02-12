from qgis.PyQt.QtCore import QDir, QFile, QIODevice, QSettings, QTextStream, QFileInfo
from qgis.PyQt.QtWidgets import QFileDialog
from typing import Dict, List
import os
import xml.etree.ElementTree as ET

from landuse_analyst.lib.laanimal import LaAnimal
from landuse_analyst.lib.lacrop import LaCrop
from landuse_analyst.lib.laanimalparameter import LaAnimalParameter
from landuse_analyst.lib.lacropparameter import LaCropParameter

class LaUtils:
    @staticmethod
    def openGraphicFile(parent=None):
        """
        Opens a file dialog to select a graphic file and returns the file path.
        """
        print("openGraphicFile called")
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            parent,
            "Open Graphic File",
            QDir.homePath(),
            "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)",
            options=options
        )
        print(f"Selected file path: {file_path}")
        return file_path

    @staticmethod
    def userSettingsDirPath():
        """
        Returns the path to the settings directory in user's home dir.
        """
        settings = QSettings()
        path = settings.value("dataDirs/dataDir", QDir.homePath() + "/.landuseAnalyst/")
        QDir().mkpath(path)
        return path

    @staticmethod
    def getModelOutputDir():
        """
        Returns the path to the model output directory.
        """
        path = LaUtils.userSettingsDirPath() + QDir.separator() + "modelOutputs" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def userAnimalProfilesDirPath():
        """
        Returns the path to the user animal profiles directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst/" + QDir.separator() + "animalProfiles" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def userCropProfilesDirPath():
        """
        Returns the path to the user crop profiles directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst/" + QDir.separator() + "cropProfiles" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def getAvailableCrops() -> Dict[str, LaCrop]:
        """
        Returns a dictionary of available crops.
        """
        # Initialize an empty dictionary to store the crops
        crop_map = {}

        # Get the path to the user crop profiles directory
        directory = QDir(LaUtils.userCropProfilesDirPath())
        print(f"Crop profiles directory: {directory.absolutePath()}")

        # Set the filter to include directories and files, but exclude symbolic links
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)

        # Get the list of files and directories in the crop profiles directory
        file_list = directory.entryInfoList()
        print(f"Number of files found: {len(file_list)}")

        # Iterate through the list of files and directories
        for file_info in file_list:
            print(f"Processing file: {file_info.fileName()}")

            # Ignore the current directory (.) and parent directory (..)
            if file_info.fileName() in [".", ".."]:
                print("Ignoring current or parent directory")
                continue

            # If the file has an XML extension, try to load it as a crop profile
            if file_info.completeSuffix() == "xml":
                print(f"Found XML file: {file_info.fileName()}")
                # Create a LaCrop object and load the crop profile from the XML file
                crop = LaCrop()
                crop.fromXmlFile(file_info.absoluteFilePath())

                # If the crop name is not empty, add it to the dictionary
                if crop.name():
                    print(f"Loaded crop: {crop.name()} with GUID: {crop.guid()}")
                    crop_map[crop.guid()] = crop
                else:
                    print("Crop name is empty, skipping file")
            else:
                print(f"Skipping non-XML file: {file_info.fileName()}")

        # Return the dictionary of available crops
        print(f"Total crops loaded: {len(crop_map)}")
        return crop_map

    @staticmethod
    def userConversionTablesDirPath():
        """
        Returns the path to the user conversion tables directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst/" + QDir.separator() + "conversionTables" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def userAnimalParameterProfilesDirPath():
        """
        Returns the path to the user animal parameter profiles directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst/" + QDir.separator() + "animalParameterProfiles" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def userImagesDirPath():
        """
        Returns the path to the user images directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst" + QDir.separator() + "images" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def userCropParameterProfilesDirPath():
        """
        Returns the path to the user crop parameter profiles directory.
        """
        path = QDir.homePath() + "/.landuseAnalyst/" + QDir.separator() + "cropParameterProfiles" + QDir.separator()
        QDir().mkpath(path)
        return path

    @staticmethod
    def convertAreaToHectares(area_unit: int, area: int) -> int:
        """
        Converts area to hectares.
        """
        hectares = 0.0
        if area_unit == 0:  # Dunum
            hectares = area * 0.1
        elif area_unit == 1:  # Hectare
            hectares = area
        return int(hectares)

    @staticmethod
    def getAvailableAnimalParameters() -> Dict[str, LaAnimalParameter]:
        """
        Returns a dictionary of available animal parameters.
        """
        animal_parameter_map = {}
        directory = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        file_list = directory.entryInfoList()
        for file_info in file_list:
            if file_info.fileName() in [".", ".."]:
                continue
            if file_info.completeSuffix() == "xml":
                animal_parameter = LaAnimalParameter()
                animal_parameter.fromXmlFile(file_info.absoluteFilePath())
                if animal_parameter.name():
                    animal_parameter_map[animal_parameter.guid()] = animal_parameter
        return animal_parameter_map

    @staticmethod
    def getAnimalParameter(guid: str) -> LaAnimalParameter:
        """
        Returns an animal parameter by its GUID.
        """
        directory = QDir(LaUtils.userAnimalParameterProfilesDirPath())
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        file_list = directory.entryInfoList()
        for file_info in file_list:
            if file_info.fileName() in [".", ".."]:
                continue
            if file_info.completeSuffix() == "xml":
                animal_parameter = LaAnimalParameter()
                animal_parameter.fromXmlFile(file_info.absoluteFilePath())
                if animal_parameter.name() and animal_parameter.guid() == guid:
                    return animal_parameter
        return LaAnimalParameter()  # Return a blank animal parameter if no match found

    @staticmethod
    def getAvailableCropParameters() -> Dict[str, LaCropParameter]:
        """
        Returns a dictionary of available crop parameters.
        """
        crop_parameter_map = {}
        directory = QDir(LaUtils.userCropParameterProfilesDirPath())
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        file_list = directory.entryInfoList()
        for file_info in file_list:
            if file_info.fileName() in [".", ".."]:
                continue
            if file_info.completeSuffix() == "xml":
                crop_parameter = LaCropParameter()
                crop_parameter.fromXmlFile(file_info.absoluteFilePath())
                if crop_parameter.name():
                    crop_parameter_map[crop_parameter.guid()] = crop_parameter
        return crop_parameter_map

    @staticmethod
    def getCropParameter(guid: str) -> LaCropParameter:
        """
        Returns a crop parameter by its GUID.
        """
        directory = QDir(LaUtils.userCropParameterProfilesDirPath())
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        file_list = directory.entryInfoList()
        for file_info in file_list:
            if file_info.fileName() in [".", ".."]:
                continue
            if file_info.completeSuffix() == "xml":
                crop_parameter = LaCropParameter()
                crop_parameter.fromXmlFile(file_info.absoluteFilePath())
                if crop_parameter.name() and crop_parameter.guid() == guid:
                    return crop_parameter
        return LaCropParameter()  # Return a blank crop parameter if no match found

    @staticmethod
    def sortList(the_list: List[str]) -> List[str]:
        """
        Sorts the list alphabetically in descending order.
        """
        the_list.sort()
        return the_list[::-1]

    @staticmethod
    def uniqueList(the_list: List[str]) -> List[str]:
        """
        Removes duplicates from a sorted list.
        """
        unique_list = []
        last = ""
        for current in the_list:
            if current != last:
                unique_list.append(current)
            last = current
        return unique_list

    @staticmethod
    def getExperimentsList() -> List[str]:
        """
        Returns a list of all the experiment files.
        """
        experiment_list = []
        settings = QSettings()
        work_dir = settings.value("dataDirs/dataDir", QDir.homePath() + QDir.separator() + ".landuseAnalyst") + "/modelOutputs/"
        directory = QDir(work_dir)
        directory.setFilter(QDir.Dirs | QDir.Files | QDir.NoSymLinks)
        file_list = directory.entryInfoList()
        for file_info in file_list:
            if file_info.fileName() in [".", ".."]:
                continue
            if file_info.absoluteDir().count() < 1:
                continue
            experiment_file = file_info.absolutePath() + QDir.separator() + file_info.fileName() + QDir.separator() + file_info.fileName() + ".xml"
            if QFile.exists(experiment_file):
                experiment_list.append(experiment_file)
        return experiment_list

    @staticmethod
    def createTextFile(file_name: str, data: str) -> bool:
        """
        Creates a text file with the given data.
        """
        file = QFile(file_name)
        if file.open(QIODevice.WriteOnly):
            text_stream = QTextStream(file)
            text_stream << data
            file.close()
            return True
        return False

    @staticmethod
    def xmlEncode(string: str) -> str:
        """
        Encodes a string for XML.
        """
        string = string.replace("<", "&lt;")
        string = string.replace(">", "&gt;")
        string = string.replace("&", "&amp;")
        return string

    @staticmethod
    def xmlDecode(string: str) -> str:
        """
        Decodes a string from XML.
        """
        string = string.replace("&lt;", "<")
        string = string.replace("&gt;", ">")
        string = string.replace("&amp;", "&")
        return string

    @staticmethod
    def getStandardCss() -> str:
        """
        Returns the standard CSS.
        """
        style = ".glossy{ background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565); color: white; padding-left: 4px; border: 1px solid #6c6c6c; }"
        style += "body {background: white;}"
        style += "h1 {font-size : 22pt; color: #0063F7; }"
        style += "h2 {font-size : 18pt; color: #0063F7; }"
        style += "h3 {font-size : 14pt; color: #0063F7; }"
        style += ".cellHeader {color:#466aa5; font-size : 12pt;}"
        style += ".parameterHeader {font-weight: bold;}"
        style += ".largeCell {color:#000000; font-size : 12pt;}"
        style += ".table {"
        style += "  border-width: 1px 1px 1px 1px;"
        style += "  border-spacing: 2px;"
        style += "  border-style: solid solid solid solid;"
        style += "  border-color: black black black black;"
        style += "  border-collapse: separate;"
        style += "  background-color: white;"
        style += "}"
        return style

    @staticmethod
    def openGraphicFile() -> str:
        """
        Opens a file dialog to select a graphic file and returns the file path.
        """
        home_path = QDir.homePath()
        file_name = QFileDialog.getOpenFileName(None, "Choose an image", home_path, "Images (*.png *.xpm *.jpg)")
        if file_name:
            file_info = QFileInfo(file_name)
            name = file_info.fileName()
            destination_file_path_name = LaUtils.userImagesDirPath() + name
            QFile.copy(file_name, destination_file_path_name)
            return destination_file_path_name
        return ""

    @staticmethod
    def saveFile() -> str:
        """
        Opens a file dialog to save a file and returns the file path.
        """
        home_path = QDir.homePath()
        file_name = QFileDialog.getSaveFileName(None, "Choose a file name", LaUtils.userConversionTablesDirPath(), "*.csv")
        if file_name:
            file_info = QFileInfo(file_name)
            name = file_info.fileName()
            destination_file_path_name = LaUtils.userConversionTablesDirPath() + name
            return destination_file_path_name
        return ""