from qgis.PyQt.QtCore import QObject, pyqtSlot, QProcess, QStringListModel, QRegExp
from typing import Dict, List
import os

class LaGrass(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.diets = {}

    @pyqtSlot(str, result=object)
    def getDiet(self, guid: str):
        return self.diets.get(guid)

    @pyqtSlot(str, object)
    def addDiet(self, guid: str, diet):
        self.diets[guid] = diet

    @pyqtSlot(str)
    def removeDiet(self, guid: str):
        if guid in self.diets:
            del self.diets[guid]

    @pyqtSlot(result=dict)
    def getDiets(self) -> Dict[str, object]:
        return self.diets

    def runCommand(self, command: str, arguments: List[str], error_log: str = "") -> str:
        program = f"/usr/lib/grass/bin/{command}"
        process = QProcess()
        process.start(program, arguments)

        if not process.waitForStarted():
            self.logMessage("The process never started.....aaargh")
            return ""

        while process.waitForReadyRead(-1):
            pass

        log = ""
        process.setReadChannel(QProcess.StandardOutput)
        log += process.readAll().data().decode()
        process.setReadChannel(QProcess.StandardError)
        error_log += process.readAll().data().decode()

        log = log.replace("----------------------------------------------", "")
        return log

    def getMapsetList(self) -> List[str]:
        command = "g.mapsets"
        arguments = ["-l"]
        result = self.runCommand(command, arguments)
        result = result.strip()
        return result.split()

    def getRasterList(self, mapset: str, prepend_mapset_flag: bool = True) -> List[str]:
        command = "g.list"
        arguments = ["type=rast", f"mapset={mapset}"]
        result = self.runCommand(command, arguments)

        if "no raster files available" in result:
            return []

        result = result.replace(f"raster files available in mapset {mapset}:", "").strip()
        raster_list = result.split()
        if prepend_mapset_flag:
            return [f"{raster}@{mapset}" for raster in raster_list]
        return raster_list

    def copyMap(self, original_raster: str, copy: str) -> bool:
        command = "g.copy"
        arguments = [f"rast={original_raster},{copy}"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def createFrictionMap(self, base_raster: str, output_raster: str) -> bool:
        command = "r.mapcalc"
        arguments = [f"{output_raster} = if(isnull({base_raster}), null(), 1)"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def createInverseMask(self, min_value: float, mask_raster: str) -> bool:
        command = "r.mapcalc"
        arguments = [f"laCostMapReclassed=if(laWalkCost>{min_value},1,0)"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        self.createCombinedMask("laCostMapReclassed", mask_raster)
        return error_log == ""

    def createMask(self, cost_surface: str, mask_raster: str) -> bool:
        command = "r.mapcalc"
        mask_name = "tmpMask"
        arguments = [f"{mask_name}={cost_surface}*{mask_raster}"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def createCombinedMask(self, cost_surface: str, mask_raster: str) -> bool:
        command = "r.mapcalc"
        mask_name = "laLeftOver"
        arguments = [f"{mask_name}={cost_surface}*{mask_raster}"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def mergeMaps(self, leftovers_go_here: str) -> bool:
        error_log = ""
        command = "r.mapcalc"

        arguments = [f"mergeTmp = if(isnull({leftovers_go_here}),0,{leftovers_go_here})"]
        result = self.runCommand(command, arguments, error_log)

        arguments = [f"laLeftOverTmp = if(isnull(laLeftOver),0,laLeftOver)"]
        result = self.runCommand(command, arguments, error_log)

        arguments = [f"laCombinedMasks = laLeftOverTmp + mergeTmp"]
        result = self.runCommand(command, arguments, error_log)

        self.removeFile("mergeTmp")
        self.removeFile("laLeftOverTmp")

        return error_log == ""

    def getArea(self, layer_name: str) -> float:
        self.logMessage("method ==> void LaGrass::getArea(float theArea)")
        command = "r.stats"
        arguments = ["-a", "-n", "fs=,", f"input={layer_name}"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)

        if error_log:
            return 0

        result = result.strip()
        result_list = result.split()
        if len(result_list) < 2:
            return 0

        area_list = result_list[1].split(",")
        if len(area_list) < 2:
            return 0

        area = float(area_list[1]) * 0.0001  # adjust for hectares
        return area

    def makeWalkCost(self, x: int, y: int, dem: str) -> bool:
        self.logMessage("method ==> void LaGrass::makeWalkCost(int theX, int theY)")
        command = "r.walk"
        arguments = [
            "max_cost=40000",
            f"elevation={dem}",
            "friction=frictionMap",
            "output=laWalkCost",
            f"coordinate={x},{y}",
            "percent_memory=100",
            "nseg=4",
            "walk_coeff=0.72,6.0,1.9998,-1.999",
            "lambda=0.75",
            "slope_factor=-0.2125",
            "-k",
            "--overwrite"
        ]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def makeEuclideanCost(self, x: int, y: int):
        self.logMessage("method ==> void LaGrass::makeEuclideanCost(int theX, int theY)")

    def makePathDistanceCost(self, x: int, y: int):
        self.logMessage("method ==> void LaGrass::makePathDistanceCost(int theX, int theY)")

    def writeMetaData(self, meta_data: List[str]):
        self.logMessage("method ==> void LaGrass::writeMetaData(QString theValue)")

    def reclass(self, raster: str, max_value: int) -> bool:
        command = "r.mapcalc"
        arguments = [f"laCostMapReclassed=if({raster}<{max_value},1,0)"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def removeFile(self, file: str) -> bool:
        command = "g.remove"
        arguments = [f"rast={file}"]
        error_log = ""
        result = self.runCommand(command, arguments, error_log)
        return error_log == ""

    def logMessage(self, message: str):
        self.message.emit(message)