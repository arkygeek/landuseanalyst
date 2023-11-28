# lacropparameter.py
from typing import Optional, Type

from qgis.PyQt.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
from qgis.PyQt.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, Qt
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits
#, LaTripleMap, LaRasterInfo, LaFoodSourceMap, HerdSize, LaReportMap

# from la.lib.lautils import LaUtils

class LaCropParameter(LaSerialisable, LaGuid):

    nameChanged: pyqtSignal = pyqtSignal()
    descriptionChanged: pyqtSignal = pyqtSignal()
    cropGuidChanged: pyqtSignal = pyqtSignal()
    percentTameCropChanged: pyqtSignal = pyqtSignal(float)
    spoilageChanged: pyqtSignal = pyqtSignal(float)
    reseedChanged: pyqtSignal = pyqtSignal(float)
    cropRotationChanged: pyqtSignal = pyqtSignal(float)
    fallowRatioChanged: pyqtSignal = pyqtSignal(float)
    fallowValueChanged: pyqtSignal = pyqtSignal(float)
    areaUnitsChanged: pyqtSignal = pyqtSignal(LaAreaUnits)
    useCommonLandChanged: pyqtSignal = pyqtSignal(bool)
    useSpecificLandChanged: pyqtSignal = pyqtSignal(bool)
    rasterNameChanged: pyqtSignal = pyqtSignal(str)

    def __init__(self, theCropParameter: Optional[Type['LaCropParameter']] = None):
        """
        Initializes a new instance of the LaCropParameter class.

        Args:
            theCropParameter (LaCropParameter, optional): An existing LaCropParameter object to copy. Defaults to None.
        """
        super().__init__()
        if theCropParameter is None:
            self._guid = LaGuid()
            self._name = "No Name Set"
            self._description = "Not Set"
        else:
            self._name = theCropParameter.name
            self._description = theCropParameter.description
            self._guid = theCropParameter.guid
            self._cropGuid = theCropParameter.cropGuid
            self._percentTameCrop = theCropParameter.percentTameCrop
            self._spoilage = theCropParameter.spoilage
            self._reseed = theCropParameter.reseed
            self._cropRotation = theCropParameter.cropRotation
            self._fallowRatio = theCropParameter.fallowRatio
            self._fallowValue = theCropParameter.fallowValue
            self._areaUnits = theCropParameter.areaUnits
            self._useCommonLand = theCropParameter.useCommonLand
            self._useSpecificLand = theCropParameter.useSpecificLand
            self._rasterName = theCropParameter.rasterName


    def __del__(self):
        pass

    def __copy__(self) -> 'LaCropParameter':
        myNewCropParameter: LaCropParameter = LaCropParameter()
        myNewCropParameter._name = self._name
        myNewCropParameter._description = self._description
        myNewCropParameter._cropGuid = self._cropGuid
        myNewCropParameter._percentTameCrop = self._percentTameCrop
        myNewCropParameter._spoilage = self._spoilage
        myNewCropParameter._reseed = self._reseed
        myNewCropParameter._cropRotation = self._cropRotation
        myNewCropParameter._fallowRatio = self._fallowRatio
        myNewCropParameter._fallowValue = self._fallowValue
        myNewCropParameter._areaUnits = self._areaUnits
        myNewCropParameter._useCommonLand = self._useCommonLand
        myNewCropParameter._useSpecificLand = self._useSpecificLand
        myNewCropParameter._rasterName = self._rasterName
        return myNewCropParameter


    @pyqtProperty(str, notify=nameChanged)
    def name(self): # type: ignore
        return self._name

    @name.setter
    def name(self, theName):
        if self._name != theName:
            self._name = theName
            self.nameChanged.emit(theName)

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self): # type: ignore
        return self._description

    @description.setter
    def description(self, description):
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description) # type: ignore

    @pyqtProperty(str, notify=cropGuidChanged)
    def cropGuid(self): # type: ignore
        return self._cropGuid

    @cropGuid.setter
    def cropGuid(self, cropGuid):
        if self._cropGuid != cropGuid:
            self._cropGuid = cropGuid
            self.cropGuidChanged.emit(cropGuid) # type: ignore

    @pyqtProperty(float, notify=percentTameCropChanged)
    def percentTameCrop(self): # type: ignore
        return self._percentTameCrop

    @percentTameCrop.setter
    def percentTameCrop(self, percentTameCrop):
        if self._percentTameCrop != percentTameCrop:
            self._percentTameCrop = percentTameCrop
            self.percentTameCropChanged.emit(percentTameCrop) # type: ignore

    @pyqtProperty(float, notify=spoilageChanged)
    def spoilage(self): # type: ignore
        return self._spoilage

    @spoilage.setter
    def spoilage(self, spoilage):
        if self._spoilage != spoilage:
            self._spoilage = spoilage
            self.spoilageChanged.emit(spoilage) # type: ignore

    @pyqtProperty(float, notify=reseedChanged)
    def reseed(self): # type: ignore
        return self._reseed

    @reseed.setter
    def reseed(self, reseed):
        if self._reseed != reseed:
            self._reseed = reseed
            self.reseedChanged.emit(reseed) # type: ignore

    @pyqtProperty(float, notify=cropRotationChanged)
    def cropRotation(self): # type: ignore
        return self._cropRotation

    @cropRotation.setter
    def cropRotation(self, cropRotation):
        if self._cropRotation != cropRotation:
            self._cropRotation = cropRotation
            self.cropRotationChanged.emit(cropRotation) # type: ignore

    @pyqtProperty(float, notify=fallowRatioChanged)
    def fallowRatio(self): # type: ignore
        return self._fallowRatio

    @fallowRatio.setter
    def fallowRatio(self, fallowRatio):
        if self._fallowRatio != fallowRatio:
            self._fallowRatio = fallowRatio
            self.fallowRatioChanged.emit(fallowRatio) # type: ignore

    @pyqtProperty(float, notify=fallowValueChanged)
    def fallowValue(self): # type: ignore
        return self._fallowValue

    @fallowValue.setter
    def fallowValue(self, fallowValue):
        if self._fallowValue != fallowValue:
            self._fallowValue = fallowValue
            self.fallowValueChanged.emit(fallowValue) # type: ignore

    @pyqtProperty(LaAreaUnits, notify=areaUnitsChanged)
    def areaUnits(self): # type: ignore
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, areaUnits):
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits) # type: ignore

    @pyqtProperty(bool, notify=useCommonLandChanged)
    def useCommonLand(self): # type: ignore
        return self._useCommonLand

    @useCommonLand.setter
    def useCommonLand(self, useCommonLand):
        if self._useCommonLand != useCommonLand:
            self._useCommonLand = useCommonLand
            self.useCommonLandChanged.emit(useCommonLand) # type: ignore

    @pyqtProperty(bool, notify=useSpecificLandChanged)
    def useSpecificLand(self): # type: ignore
        return self._useSpecificLand

    @useSpecificLand.setter
    def useSpecificLand(self, useSpecificLand):
        if self._useSpecificLand != useSpecificLand:
            self._useSpecificLand = useSpecificLand
            self.useSpecificLandChanged.emit(useSpecificLand) # type: ignore

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self): # type: ignore
        return self._rasterName

    @rasterName.setter
    def rasterName(self, rasterName):
        if self._rasterName != rasterName:
            self._rasterName = rasterName
            self.rasterNameChanged.emit(rasterName) # type: ignore

    def fromXml(self, theXml: str) -> bool:
        from la.lib.lautils import LaUtils
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("cropParameter")
        if myTopElement.isNull():
            # TODO - just make this a warning
            pass
        self.guid = LaGuid.setGuid.myTopElement.attribute("guid")
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        self.cropGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("crop").text())
        self.percentTameCrop = float(myTopElement.firstChildElement("percentTameCrop").text())
        self.spoilage = float(myTopElement.firstChildElement("spoilage").text())
        self.reseed = float(myTopElement.firstChildElement("reseed").text())
        self.cropRotation = int(myTopElement.firstChildElement("cropRotation").text())
        self.fallowRatio = float(myTopElement.firstChildElement("fallowRatio").text())
        self.fallowValue = int(myTopElement.firstChildElement("fallowValue").text())
        my_area_units = myTopElement.firstChildElement("areaUnits").text()
        # doing area units this way makes the xml files PROFOUNDLY easier to read
        if my_area_units == "Dunum":
            self.areaUnits = LaAreaUnits.Dunum
        elif my_area_units == "Hectare":
            self.areaUnits = LaAreaUnits.Hectare
        self.useCommonLand = int(myTopElement.firstChildElement("useCommonLand").text())
        self.useSpecificLand = int(myTopElement.firstChildElement("useSpecificLand").text())
        self.rasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
        #
        return True

    def toXml(self):
        """Converts the LaCropParameter object to an XML string."""
        from la.lib.lautils import LaUtils
        myName = LaUtils.xmlEncode(self.name)
        myDescription = LaUtils.xmlEncode(self.description)
        myGuid = LaUtils.xmlEncode(self.cropGuid)
        myCropGuid = LaUtils.xmlEncode(self.cropGuid)
        myPercentTameCrop = str(self.percentTameCrop)
        mySpoilage = str(self.spoilage)
        myReseed = str(self.reseed)
        myCropRotation = str(self.cropRotation)
        myFallowRatio = str(self.fallowRatio)
        myFallowValue = str(self.fallowValue)
        myAreaUnits = str(self.areaUnits)
        myUseCommonLand = str(self.useCommonLand)
        myUseSpecificLand = str(self.useSpecificLand)
        myRasterName = LaUtils.xmlEncode(self.rasterName)

        myString: str = f'<cropParameter guid="{myGuid}">\n'
        myString += f'  <name>{myName}</name>\n'
        myString += f'  <description>{myDescription}</description>\n'
        myString += f'  <crop>{myCropGuid}</crop>\n'
        myString += f'  <percentTameCrop>{myPercentTameCrop}</percentTameCrop>\n'
        myString += f'  <spoilage>{mySpoilage}</spoilage>\n'
        myString += f'  <reseed>{myReseed}</reseed>\n'
        myString += f'  <cropRotation>{myCropRotation}</cropRotation>\n'
        myString += f'  <fallowRatio>{myFallowRatio}</fallowRatio>\n'
        myString += f'  <fallowValue>{myFallowValue}</fallowValue>\n'
        myString += f'  <areaUnits>{myAreaUnits}</areaUnits>\n'
        myString += f'  <useCommonLand>{myUseCommonLand}</useCommonLand>\n'
        myString += f'  <useSpecificLand>{myUseSpecificLand}</useSpecificLand>\n'
        myString += f'  <rasterName>{myRasterName}</rasterName>\n'
        myString += '</cropParameter>\n'

        return myString
    