# laanimalparameter.py
from typing import Optional, Dict, List, Any
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from qgis.PyQt.QtXml import QDomDocument
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
# from la.lib.lautils import LaUtils
from la.lib.lafoodsource import LaFoodSource
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType
from la.lib.la import Priority

class Base(QObject):
    pass
class LaAnimalParameter(LaSerialisable, LaGuid):
    nameChanged: pyqtSignal = pyqtSignal(str)
    descriptionChanged: pyqtSignal = pyqtSignal()
    guidChanged: pyqtSignal = pyqtSignal()
    animalParameterGuidChanged: pyqtSignal = pyqtSignal()
    percentTameMeatChanged: pyqtSignal = pyqtSignal()
    valueSpecificGrazingLandChanged: pyqtSignal = pyqtSignal()
    valueCommonGrazingLandChanged: pyqtSignal = pyqtSignal()
    areaUnitsChanged: pyqtSignal = pyqtSignal()
    energyTypeChanged: pyqtSignal = pyqtSignal()
    fodderUseChanged: pyqtSignal = pyqtSignal()
    fodderSourceMapChanged: pyqtSignal = pyqtSignal()
    useSpecificGrazingLandChanged: pyqtSignal = pyqtSignal()
    useCommonGrazingLandChanged: pyqtSignal = pyqtSignal()
    fallowUsageChanged: pyqtSignal = pyqtSignal()
    rasterNameChanged: pyqtSignal = pyqtSignal()

    def __init__(self, theAnimalParameter: Optional[type['LaAnimalParameter']] = None):
        super().__init__()
        if theAnimalParameter is None:
            self._guid = LaGuid.setGuid
            self._name = ""
            self._description = ""
        else:
            self._name = theAnimalParameter.name
            self._description = theAnimalParameter.description
            self._guid = theAnimalParameter.guid
            self._animalGuid = theAnimalParameter.animalGuid
            self._percentTameMeat = theAnimalParameter.percentTameMeat
            self._valueSpecificGrazingLand = theAnimalParameter.valueSpecificGrazingLand
            self._valueCommonGrazingLand = theAnimalParameter.valueCommonGrazingLand
            self._areaUnits = theAnimalParameter.areaUnits
            self._energyType = theAnimalParameter.energyType
            self._fodderUse = theAnimalParameter.fodderUse
            self._foodSourceMap = theAnimalParameter.foodSourceMap
            self._useSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand
            self._useCommonGrazingLand = theAnimalParameter.useCommonGrazingLand
            self._fallowUsage = theAnimalParameter.fallowUsage
            self._rasterName = theAnimalParameter.rasterName


    def __del__(self):
        pass

    def __copy__(self):
        myAnimalParameter: LaAnimalParameter = LaAnimalParameter()
        myAnimalParameter.name = self.name()
        myAnimalParameter.description = self.description()
        myAnimalParameter.guid = self.guid()
        myAnimalParameter.animalGuid = self.animalGuid()
        myAnimalParameter.percentTameMeat = self.percentTameMeat()
        myAnimalParameter.valueSpecificGrazingLand = self.valueSpecificGrazingLand()
        myAnimalParameter.valueCommonGrazingLand = self.valueCommonGrazingLand()
        myAnimalParameter.areaUnits = self.areaUnits()
        myAnimalParameter.energyType = self.energyType()
        myAnimalParameter.fodderUse = self.fodderUse()
        myAnimalParameter.foodSourceMap = self.foodSourceMap().copy()  # Assuming this is a dictionary
        # Copy fodder stuff here
        myAnimalParameter.useSpecificGrazingLand = self.useSpecificGrazingLand()
        myAnimalParameter.useCommonGrazingLand = self.useCommonGrazingLand()
        myAnimalParameter.fallowUsage = self.fallowUsage()
        myAnimalParameter.rasterName = self.rasterName()
        return myAnimalParameter


    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self._name != name:
            self._name = name
            self.nameChanged.emit(name)


    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):  # type: ignore
        return self._description

    @description.setter
    def description(self, description): # type: ignore
        if self._description != description:
            self._description = description
            self.descriptionChanged.emit(description)

    @pyqtProperty(str, notify=guidChanged)
    def guid(self):  # type: ignore
        return self._guid

    @guid.setter
    def guid(self, guid): # type: ignore
        if self._guid != guid:
            self._guid = guid
            self.guidChanged.emit(guid)

    @pyqtProperty(str, notify=animalParameterGuidChanged)
    def animalGuid(self):  # type: ignore
        return self._animalParameterGuid

    @animalGuid.setter
    def animalGuid(self, animalGuid): # type: ignore
        if self._animalParameterGuid != animalGuid:
            self._animalParameterGuid = animalGuid
            self.animalParameterGuidChanged.emit(animalGuid)

    @pyqtProperty(float, notify=percentTameMeatChanged)
    def percentTameMeat(self):  # type: ignore
        return self._percentTameMeat

    @percentTameMeat.setter
    def percentTameMeat(self, percentTameMeat): # type: ignore
        if self._percentTameMeat != percentTameMeat:
            self._percentTameMeat = percentTameMeat
            self.percentTameMeatChanged.emit(percentTameMeat)

    @pyqtProperty(int, notify=valueSpecificGrazingLandChanged)
    def valueSpecificGrazingLand(self):  # type: ignore
        return self._valueSpecificGrazingLand

    @valueSpecificGrazingLand.setter
    def valueSpecificGrazingLand(self, valueSpecificGrazingLand): # type: ignore
        if self._valueSpecificGrazingLand != valueSpecificGrazingLand:
            self._valueSpecificGrazingLand = valueSpecificGrazingLand
            self.valueSpecificGrazingLandChanged.emit(valueSpecificGrazingLand)

    @pyqtProperty(int, notify=valueCommonGrazingLandChanged)
    def valueCommonGrazingLand(self):  # type: ignore
        return self._valueCommonGrazingLand

    @valueCommonGrazingLand.setter
    def valueCommonGrazingLand(self, valueCommonGrazingLand): # type: ignore
        if self._valueCommonGrazingLand != valueCommonGrazingLand:
            self._valueCommonGrazingLand = valueCommonGrazingLand
            self.valueCommonGrazingLandChanged.emit(valueCommonGrazingLand)

    @pyqtProperty(int, notify=areaUnitsChanged)
    def areaUnits(self):  # type: ignore
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, areaUnits): # type: ignore
        if self._areaUnits != areaUnits:
            self._areaUnits = areaUnits
            self.areaUnitsChanged.emit(areaUnits)

    @pyqtProperty(int, notify=energyTypeChanged)
    def energyType(self):  # type: ignore
        return self._energyType

    @energyType.setter
    def energyType(self, energyType): # type: ignore
        if self._energyType != energyType:
            self._energyType = energyType
            self.energyTypeChanged.emit(energyType)

    @pyqtProperty(int, notify=fodderUseChanged)
    def fodderUse(self):  # type: ignore
        return self._fodderUse

    @fodderUse.setter
    def fodderUse(self, fodderUse): # type: ignore
        if self._fodderUse != fodderUse:
            self._fodderUse = fodderUse
            self.fodderUseChanged.emit(fodderUse)

    @pyqtProperty(dict, notify=fodderSourceMapChanged)
    def foodSourceMap(self):  # type: ignore
        return self._foodSourceMap

    @foodSourceMap.setter
    def foodSourceMap(self, foodSourceMap): # type: ignore
        if self._foodSourceMap != foodSourceMap:
            self._foodSourceMap = foodSourceMap
            self.fodderSourceMapChanged.emit(foodSourceMap)

    @pyqtProperty(int, notify=useSpecificGrazingLandChanged)
    def useSpecificGrazingLand(self):  # type: ignore
        return self._useSpecificGrazingLand

    @useSpecificGrazingLand.setter
    def useSpecificGrazingLand(self, useSpecificGrazingLand): # type: ignore
        if self._useSpecificGrazingLand != useSpecificGrazingLand:
            self._useSpecificGrazingLand = useSpecificGrazingLand
            self.useSpecificGrazingLandChanged.emit(useSpecificGrazingLand)

    @pyqtProperty(int, notify=useCommonGrazingLandChanged)
    def useCommonGrazingLand(self):  # type: ignore
        return self._useCommonGrazingLand

    @useCommonGrazingLand.setter
    def useCommonGrazingLand(self, useCommonGrazingLand): # type: ignore
        if self._useCommonGrazingLand != useCommonGrazingLand:
            self._useCommonGrazingLand = useCommonGrazingLand
            self.useCommonGrazingLandChanged.emit(useCommonGrazingLand)

    @pyqtProperty(int, notify=fallowUsageChanged)
    def fallowUsage(self):  # type: ignore
        return self._fallowUsage

    @fallowUsage.setter
    def fallowUsage(self, fallowUsage): # type: ignore
        if self._fallowUsage != fallowUsage:
            self._fallowUsage = fallowUsage
            self.fallowUsageChanged.emit(fallowUsage)

    @pyqtProperty(str, notify=rasterNameChanged)
    def rasterName(self):  # type: ignore
        return self._rasterName

    @rasterName.setter
    def rasterName(self, rasterName): # type: ignore
        if self._rasterName != rasterName:
            self._rasterName = rasterName
            self.rasterNameChanged.emit(rasterName)

    def fromXml(self, theXml):
        from la.lib.lautils import LaUtils #, xmlEncode, xmlDecode
        myDocument = QDomDocument("mydocument")
        myDocument.setContent(theXml)
        myTopElement = myDocument.firstChildElement("animalParameter")
        if myTopElement.isNull():
            pass  # TODO - just make this a warning
        self.setGuid(myTopElement.attribute("guid"))
        self.name = LaUtils.xmlDecode(myTopElement.firstChildElement("name").text())
        self.description = LaUtils.xmlDecode(myTopElement.firstChildElement("description").text())
        self.animalGuid = LaUtils.xmlDecode(myTopElement.firstChildElement("animal").text())
        self.percentTameMeat = float(myTopElement.firstChildElement("percentTameMeat").text())
        self.useCommonGrazingLand = int(myTopElement.firstChildElement("useCommonGrazingLand").text())
        self.useSpecificGrazingLand = int(myTopElement.firstChildElement("useSpecificGrazingLand").text())
        self.valueCommonGrazingLand = int(myTopElement.firstChildElement("foodValueOfCommonGrazingLand").text())
        self.valueSpecificGrazingLand = int(myTopElement.firstChildElement("foodValueOfSpecificGrazingLand").text())

        myAreaUnits = myTopElement.firstChildElement("areaUnits").text()
        if myAreaUnits == "Dunum":
            self.areaUnits = LaAreaUnits.Dunum
        elif myAreaUnits == "Hectare":
            self.areaUnits = LaAreaUnits.Hectare

        myEnergyType = myTopElement.firstChildElement("energyType").text()
        if myEnergyType == "KCalories":
            self.energyType = LaEnergyType.KCalories
        elif myEnergyType == "TDN":
            self.energyType = LaEnergyType.TDN

        self.fodderUse = int(myTopElement.firstChildElement("fodderUse").text())

        self.foodSourceMap.clear()
        myFodderCropsList = myDocument.elementsByTagName("fodderCrop")
        for myCounter in range(myFodderCropsList.size()):
            myFoodSourceNode = myFodderCropsList.item(myCounter)
            myFoodSourceElement = myFoodSourceNode.toElement()

            myCropGuid = myFoodSourceElement.firstChildElement("fodderCropGuid").text()
            myFodderStrawChaff = int(myFoodSourceElement.firstChildElement("fodderStrawChaff").text())
            myGrain = int(myFoodSourceElement.firstChildElement("fodderGrain").text())
            myUsed = int(myFoodSourceElement.firstChildElement("fodderUse").text())
            myDays = int(myFoodSourceElement.firstChildElement("fodderDays").text())
            myFoodSource = LaFoodSource()

            myFoodSource.setFodder(myFodderStrawChaff)
            myFoodSource.setGrain(myGrain)
            myFoodSource.setDays(myDays)
            myFoodSource.setUsed(myUsed)
            myFoodSource.setCropGuid(myCropGuid)

            self.foodSourceMap[myCropGuid] = myFoodSource

        myFallowUsage = myTopElement.firstChildElement("fallowUsage").text()
        if myFallowUsage == "High":
            self.fallowUsage = Priority.High
        elif myFallowUsage == "Medium":
            self.fallowUsage = Priority.Medium
        elif myFallowUsage == "Low":
            self.fallowUsage = Priority.Low
        else:
            self.fallowUsage = Priority.None_

        self.rasterName = LaUtils.xmlDecode(myTopElement.firstChildElement("rasterName").text())
        return True

    def toXml(self):
        """Converts the LaAnimalParameter object to an XML string."""
        from la.lib.lautils import LaUtils
        myName:str = LaUtils.xmlEncode(self.name)
        myDescription: str = LaUtils.xmlEncode(self.description)
        myGuid: str = LaUtils.xmlEncode(self.guid())
        myAnimalGuid: str = LaUtils.xmlEncode(self.animalGuid)
        myPercentTameMeat: float = self.percentTameMeat
        myUseCommonGrazingLand: int = self.useCommonGrazingLand
        myUseSpecificGrazingLand: int = self.useSpecificGrazingLand
        myValueCommonGrazingLand: int = self.valueCommonGrazingLand
        myValueSpecificGrazingLand: int = self.valueSpecificGrazingLand

        if self.areaUnits == LaAreaUnits.Dunum:
            myAreaUnits: str = "Dunum"
        else:
            myAreaUnits: str = "Hectare"

        myFodderUse: int = self.fodderUse
        myFoodSourceMap: Dict[str, LaFoodSource] = self.foodSourceMap

        if self.fallowUsage == Priority.High:
            myFallowUsage: str = "High"
        elif self.fallowUsage == Priority.Medium:
            myFallowUsage: str = "Medium"
        elif self.fallowUsage == Priority.Low:
            myFallowUsage: str = "Low"
        else:
            myFallowUsage: str = ""

        myRasterName: str = self.rasterName



        myString = f'<animalParameter guid="{myGuid}">\n'
        myString += f'  <name>{myName}</name>\n'
        myString += f'  <description>{myDescription}</description>\n'
        myString += f'  <animal>{myAnimalGuid}</animal>\n'
        myString += f'  <percentTameMeat>{myPercentTameMeat}</percentTameMeat>\n'
        myString += f'  <useCommonGrazingLand>{myUseCommonGrazingLand}</useCommonGrazingLand>\n'
        myString += f'  <useSpecificGrazingLand>{myUseSpecificGrazingLand}</useSpecificGrazingLand>\n'
        myString += f'  <foodValueOfCommonGrazingLand>{myValueCommonGrazingLand}</foodValueOfCommonGrazingLand>\n'
        myString += f'  <foodValueOfSpecificGrazingLand>{myValueSpecificGrazingLand}</foodValueOfSpecificGrazingLand>\n'
        myString += f'  <areaUnits>{myAreaUnits}</areaUnits>\n'
        myString += f'  <energyType>{self.energyType}</energyType>\n'


        if self.energyType == 'KCalories':
            myString += '  <energyType>KCalories</energyType>\n'
        elif self.energyType == 'TDN':
            myString += '  <energyType>TDN</energyType>\n'

        myString += f'  <fodderUse>{self.fodderUse}</fodderUse>\n'

        if self.fodderUse:
            myString += '   <fodderCrops>\n'
            for myGuid, myFoodSource in self.foodSourceMap.items():
                myFodderStrawChaff = myFoodSource.fodder()
                myFodderGrain = myFoodSource.grain()
                myFodderDays = myFoodSource.days()
                myString += f'    <fodderCrop>\n'
                myString += f'      <fodderCropGuid>{myGuid}</fodderCropGuid>\n'
                myString += f'      <fodderStrawChaff>{myFodderStrawChaff}</fodderStrawChaff>\n'
                myString += f'      <fodderGrain>{myFodderGrain}</fodderGrain>\n'
                myString += f'      <fodderDays>{myFodderDays}</fodderDays>\n'
                myString += '    </fodderCrop>\n'
            myString += '   </fodderCrops>\n'
        myString += f'  <fallowUsage>{myFallowUsage}</fallowUsage>\n'
        myString += f'  <rasterName>{myRasterName}</RasterName>\n'
        myString += '</animalParameter>\n'
        return myString

    # def toXml(self) -> str:
    #     from la.lib.lautils import LaUtils
    #     """Converts the LaCropParameter object to an XML string."""
    #     myUnits = "Dunum" if self._areaUnits == 0 else "Hectare"
    #     myName: str = self._name
    #     myDescription: str = self._description
    #     myGuid: str = self._guid
    #     myCropGuid: str = self._cropGuid
    #     myPercentTameMeat: float = self._percentTameMeat
    #     mySpoilage: int = self._
    #     myString = f'<cropParameter guid="{self._guid()}">\n'
    #     myString += f'  <name>{LaUtils.xmlEncode(self._name)}</name>\n'
    #     myString += f'  <description>{LaUtils.xmlEncode(self._description)}</description>\n'
    #     myString += f'  <crop>{LaUtils.xmlEncode(self._cropGuid)}</crop>\n'
    #     myString += f'  <percentTameCrop>{self._percentTameMeat}</percentTameCrop>\n'
    #     myString += f'  <spoilage>{self.mSpoilage}</spoilage>\n'
    #     myString += f'  <reseed>{self.mReseed}</reseed>\n'
    #     myString += f'  <cropRotation>{self.mCropRotation}</cropRotation>\n'
    #     myString += f'  <fallowRatio>{self.mFallowRatio}</fallowRatio>\n'
    #     myString += f'  <fallowValue>{self.mFallowValue}</fallowValue>\n'
    #     myString += f'  <areaUnits>{myUnits}</areaUnits>\n'
    #     myString += f'  <useCommonLand>{self.mUseCommonLand}</useCommonLand>\n'
    #     myString += f'  <useSpecificLand>{self.mUseSpecificLand}</useSpecificLand>\n'
    #     myString += f'  <rasterName>{LaUtils.xmlEncode(self.mRasterName)}</rasterName>\n'
    #     myString += '</cropParameter>\n'
    #     return myString