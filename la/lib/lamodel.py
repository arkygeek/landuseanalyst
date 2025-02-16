# lamodel.py
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import QDialog

from typing import Dict, List
from la.lib.la import La
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound

""" NOTES ON THE CODE - Python and PyQt

    The messaged signal in LaMessageBus is used for inter-object communication in the application.

    In PyQt, signals and slots are used for communication between objects. A signal is emitted when
    a particular event occurs, and slots can be connected to a signal. When the signal is emitted,
    the connected slots are automatically executed.

    In the context of the LaMessageBus class, the messaged signal would be emitted when there's a
    new message to be broadcasted across the system.

    Other parts of the application can connect slots to this signal to react to new messages.
    For example, a logging system might connect a slot to the messaged signal to log all messages,
    or a GUI might connect a slot to update a message display whenever a new message is sent.

    This allows for a decoupled architecture where the LaMessageBus doesn't need to know what
    parts of the system are interested in messages, it just emits the messaged signal whenever it
    has a new message. Any part of the system interested in these messages can simply connect a slot
    to the messaged signal to handle them.
"""
MESSAGE_BUS: LaMessageBus = LaMessageBus()


class LaModel(QDialog, LaSerialisable, LaGuid):
    nameChanged = pyqtSignal()
    populationChanged = pyqtSignal()
    periodChanged = pyqtSignal()
    projectionChanged = pyqtSignal()
    precisionChanged = pyqtSignal()
    dietPercentChanged = pyqtSignal()
    percentOfDietThatIsFromCropsChanged = pyqtSignal()
    meatPercentChanged = pyqtSignal()
    caloriesPerPersonDailyChanged = pyqtSignal()
    dairyUtilisationChanged = pyqtSignal()
    baseOnPlantsChanged = pyqtSignal()
    includeDairyChanged = pyqtSignal()
    limitDairyChanged = pyqtSignal()
    limitDairyPercentChanged = pyqtSignal()
    fallowStatusChanged = pyqtSignal()
    fallowRatioChanged = pyqtSignal()
    eastingChanged = pyqtSignal()
    northingChanged = pyqtSignal()
    euclideanDistanceChanged = pyqtSignal()
    walkingTimeChanged = pyqtSignal()
    pathDistanceChanged = pyqtSignal()
    commonLandValueChanged = pyqtSignal()
    commonLandAreaUnitsChanged = pyqtSignal()
    herdSizeChanged = pyqtSignal()
    animalsChanged = pyqtSignal()
    cropsChanged = pyqtSignal()
    dietsChanged = pyqtSignal()
    dietLabelsChanged = pyqtSignal()
    landBeingGrazedChanged = pyqtSignal()
    landFoundChanged = pyqtSignal()
    priorityChanged = pyqtSignal()
    descriptionChanged = pyqtSignal()
    areaUnitsChanged = pyqtSignal()
    statusChanged = pyqtSignal()
    guidChanged = pyqtSignal()
    iconChanged = pyqtSignal()

    def __init__(self, parent=None, theModel=None):
        QDialog.__init__(self, parent)
        if theModel is not None:
            self._name = theModel.name
            self._population = theModel.population
            self.setGuid(theModel.guid)
            self._period = theModel.period
            self._projection = theModel.projection
            self._easting = theModel.easting
            self._northing = theModel.northing
            self._euclideanDistance = theModel.euclideanDistance
            self._walkingTime = theModel.walkingTime
            self._pathDistance = theModel.pathDistance
            self._precision = theModel.precision
            self._dietPercent = theModel.dietPercent
            self._percentOfDietThatIsFromCrops = theModel.plantPercent
            self._meatPercent = theModel.meatPercent
            self._caloriesPerPersonDaily = theModel.caloriesPerPersonDaily
            self._dairyUtilisation = theModel.dairyUtilisation
            self._baseOnPlants = theModel.baseOnPlants
            self._includeDairy = theModel.includeDairy
            self._limitDairy = theModel.limitDairy
            self._limitDairyPercentage = theModel.limitDairyPercent
            self._fallowStatus = theModel.fallowStatus
            self._fallowRatio = theModel.fallowRatio
            self._landBeingGrazed = theModel.landBeingGrazed
            self._landFound = theModel.landFound
        else:
            self.setGuid(None)
            self._name: str = "No Name Set"
            self._population: int = 1000
            self._period: str = "No Period Set"
            self._projection: int = 100
            self._precision: int = 5
            self._dietPercent: int = 25
            self._percentOfDietThatIsFromCrops: int = 10
            self._meatPercent: int = 10
            self._caloriesPerPersonDaily: int = 2500
            self._landBeingGrazed: LandBeingGrazed = LandBeingGrazed.Common
            self._landFound: LandFound = LandFound.NO
            # self._dairyUtilisation: int = 100
            # self._baseOnPlants: bool = True
            # self._includeDairy: bool = True
            # self._limitDairy: bool = False
            # self._limitDairyPercent: int = 10
            # self._fallowStatus: Status = Status.FALLOW)
            # self._easting: int = 0
            # self._northing: int = 0
            # self._euclideanDistance: bool = True
            # self._walkingTime: bool = False
            # self._pathDistance: bool = False
            # self._commonLandValue: float = 0.0
            # self._commonLandAreaUnits: AreaUnits = AreaUnits.HECTARES
            # self._herdSize: int = 0
            # self._animals: Dict[str, str] = {}
            # self._crops: Dict[str, str] = {}
            # self._diets: Dict[str, La] = {}
            # self._dietLabels: List[LaDietLabels] = []
            # self._landBeingGrazed: LandBeingGrazed = LandBeingGrazed.NO
            # self._landFound: LandFound = LandFound.NO
            # self._priority: Priority = Priority.NORMAL
            # self._description: str = "No Description Set"
            # self._areaUnits: AreaUnits = AreaUnits.HECTARES
            # self._status: Status = Status.FALLOW
            # self._icon: QIcon = QIcon()


    def __del__(self):
        pass

    def __copy__(self):
        myModel: LaModel = LaModel()
        myModel.name = self._name

        return LaModel(self)

    def __deepcopy__(self, memo):
        return LaModel(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, theName: str):
        if self._name != theName:
            self._name = theName
            self.nameChanged.emit()

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, thePopulation: int):
        if self._population != thePopulation:
            self._population = thePopulation
            self.populationChanged.emit()

    @property
    def period(self) -> str:
        return self._period

    @period.setter
    def period(self, thePeriod: str):
        if self._period != thePeriod:
            self._period = thePeriod
            self.periodChanged.emit()

    @property
    def projection(self) -> int:
        return self._projection

    @projection.setter
    def projection(self, theProjection: int):
        if self._projection != theProjection:
            self._projection = theProjection
            self.projectionChanged.emit()

    @property
    def precision(self) -> int:
        return self._precision

    @precision.setter
    def precision(self, thePrecision: int):
        if self._precision != thePrecision:
            self._precision = thePrecision
            self.precisionChanged.emit()

    @property
    def dietPercent(self) -> int:
        return self._dietPercent

    @dietPercent.setter
    def dietPercent(self, theDietPercent: int):
        if self._dietPercent != theDietPercent:
            self._dietPercent = theDietPercent
            self.dietPercentChanged.emit()

    @property
    def percentOfDietThatIsFromCrops(self) -> int:
        return self._percentOfDietThatIsFromCrops

    @percentOfDietThatIsFromCrops.setter
    def percentOfDietThatIsFromCrops(self, thePercent: int):
        if self._percentOfDietThatIsFromCrops != thePercent:
            self._percentOfDietThatIsFromCrops = thePercent
            self.percentOfDietThatIsFromCropsChanged.emit()

    @property
    def meatPercent(self) -> int:
        return self._meatPercent

    @meatPercent.setter
    def meatPercent(self, theMeatPercent: int):
        if self._meatPercent != theMeatPercent:
            self._meatPercent = theMeatPercent
            self.meatPercentChanged.emit()

    @property
    def caloriesPerPersonDaily(self) -> int:
        return self._caloriesPerPersonDaily

    @caloriesPerPersonDaily.setter
    def caloriesPerPersonDaily(self, theCaloriesPerPersonDaily: int):
        if self._caloriesPerPersonDaily != theCaloriesPerPersonDaily:
            self._caloriesPerPersonDaily = theCaloriesPerPersonDaily
            self.caloriesPerPersonDailyChanged.emit()

    @property
    def dairyUtilisation(self) -> int:
        return self._dairyUtilisation

    @dairyUtilisation.setter
    def dairyUtilisation(self, thePercent: int):
        if self._dairyUtilisation != thePercent:
            self._dairyUtilisation = thePercent
            self.dairyUtilisationChanged.emit()

    @property
    def baseOnPlants(self) -> bool:
        return self._baseOnPlants

    @baseOnPlants.setter
    def baseOnPlants(self, theBool: bool):
        if self._baseOnPlants != theBool:
            self._baseOnPlants = theBool
            self.baseOnPlantsChanged.emit()

    @property
    def includeDairy(self) -> bool:
        return self._includeDairy

    @includeDairy.setter
    def includeDairy(self, theBool: bool):
        if self._includeDairy != theBool:
            self._includeDairy = theBool
            self.includeDairyChanged.emit()

    @property
    def limitDairy(self) -> bool:
        return self._limitDairy

    @limitDairy.setter
    def limitDairy(self, theBool: bool):
        if self._limitDairy != theBool:
            self._limitDairy = theBool
            self.limitDairyChanged.emit()

    @property
    def limitDairyPercent(self) -> int:
        return self._limitDairyPercent

    @limitDairyPercent.setter
    def limitDairyPercent(self, thePercent: int):
        if self._limitDairyPercent != thePercent:
            self._limitDairyPercent = thePercent
            self.limitDairyPercentChanged.emit()

    @property
    def fallowStatus(self) -> Status:
        return self._fallowStatus

    @fallowStatus.setter
    def fallowStatus(self, theStatus: Status):
        if self._fallowStatus != theStatus:
            self._fallowStatus = theStatus
            self.fallowStatusChanged.emit()

    @property
    def fallowRatio(self) -> int:
        return self._fallowRatio

    @fallowRatio.setter
    def fallowRatio(self, theRatio: int):
        if self._fallowRatio != theRatio:
            self._fallowRatio = theRatio
            self.fallowRatioChanged.emit()

    @property
    def easting(self) -> int:
        return self._easting

    @easting.setter
    def easting(self, theEasting: int):
        if self._easting != theEasting:
            self._easting = theEasting
            self.eastingChanged.emit()

    @property
    def northing(self) -> int:
        return self._northing

    @northing.setter
    def northing(self, theNorthing: int):
        if self._northing != theNorthing:
            self._northing = theNorthing
            self.northingChanged.emit()

    @property
    def euclideanDistance(self) -> bool:
        return self._euclideanDistance

    @euclideanDistance.setter
    def euclideanDistance(self, theBool: bool):
        if self._euclideanDistance != theBool:
            self._euclideanDistance = theBool
            self.euclideanDistanceChanged.emit()

    @property
    def walkingTime(self) -> bool:
        return self._walkingTime

    @walkingTime.setter
    def walkingTime(self, theBool: bool):
        if self._walkingTime != theBool:
            self._walkingTime = theBool
            self.walkingTimeChanged.emit()

    @property
    def pathDistance(self) -> bool:
        return self._pathDistance

    @pathDistance.setter
    def pathDistance(self, theBool: bool):
        if self._pathDistance != theBool:
            self._pathDistance = theBool
            self.pathDistanceChanged.emit()

    @property
    def commonLandValue(self) -> float:
        return self._commonLandValue

    @commonLandValue.setter
    def commonLandValue(self, theValue: float):
        if self._commonLandValue != theValue:
            self._commonLandValue = theValue
            self.commonLandValueChanged.emit()

    @property
    def commonLandAreaUnits(self) -> AreaUnits:
        return self._commonLandAreaUnits

    @commonLandAreaUnits.setter
    def commonLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self._commonLandAreaUnits != theAreaUnits:
            self._commonLandAreaUnits = theAreaUnits
            self.commonLandAreaUnitsChanged.emit()

    @property
    def herdSize(self) -> int:
        return self._herdSize

    @herdSize.setter
    def herdSize(self, theAnimalGuid: str):
        if self._herdSize != theAnimalGuid:
            self._herdSize = theAnimalGuid
            self.herdSizeChanged.emit()

    @property
    def animals(self) -> Dict[str, str]:
        return self._animals

    @animals.setter
    def animals(self, theAnimals: Dict[str, str]):
        if self._animals != theAnimals:
            self._animals = theAnimals
            self.animalsChanged.emit()

    @property
    def crops(self) -> Dict[str, str]:
        return self._crops

    @crops.setter
    def crops(self, theCrops: Dict[str, str]):
        if self._crops != theCrops:
            self._crops = theCrops
            self.cropsChanged.emit()

    @property
    def diets(self) -> Dict[str, La]:
        return self._diets

    @diets.setter
    def diets(self, theDiets: Dict[str, La]):
        if self._diets != theDiets:
            self._diets = theDiets
            self.dietsChanged.emit()

    @property
    def dietLabels(self) -> List[LaDietLabels]:
        return self._dietLabels

    @dietLabels.setter
    def dietLabels(self, theDietLabels: List[LaDietLabels]):
        if self._dietLabels != theDietLabels:
            self._dietLabels = theDietLabels
            self.dietLabelsChanged.emit()

    @property
    def landBeingGrazed(self) -> LandBeingGrazed:
        return self._landBeingGrazed

    @landBeingGrazed.setter
    def landBeingGrazed(self, theLandBeingGrazed: LandBeingGrazed):
        if self._landBeingGrazed != theLandBeingGrazed:
            self._landBeingGrazed = theLandBeingGrazed
            self.landBeingGrazedChanged.emit()

    @property
    def landFound(self) -> LandFound:
        return self._landFound

    @landFound.setter
    def landFound(self, theLandFound: LandFound):
        if self._landFound != theLandFound:
            self._landFound = theLandFound
            self.landFoundChanged.emit()

    @property
    def priority(self) -> Priority:
        return self._priority

    @priority.setter
    def priority(self, thePriority: Priority):
        if self._priority != thePriority:
            self._priority = thePriority
            self.priorityChanged.emit()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, theDescription: str):
        if self._description != theDescription:
            self._description = theDescription
            self.descriptionChanged.emit()

    @property
    def areaUnits(self) -> AreaUnits:
        return self._areaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnits: AreaUnits):
        if self._areaUnits != theAreaUnits:
            self._areaUnits = theAreaUnits
            self.areaUnitsChanged.emit()

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, theStatus: Status):
        if self._status != theStatus:
            self._status = theStatus
            self.statusChanged.emit()

    @property
    def guid(self) -> str:
        return self._guid

    @guid.setter
    def guid(self, theGuid: str):
        if self._guid != theGuid:
            self._guid = LaGuid.setGuid()
            self.guidChanged.emit()

    def toXml(self) -> str:
        myString = f'<model guid="{self.guid}">\n'
        myString += f'  <name>{xmlEncode(self._name)}</name>\n'
        myString += f'  <population>{self._population}</population>\n'
        myString += f'  <period>{LaUtils.xmlEncode(self._period)}</period>\n'
        myString += f'  <projection>{self._projection}</projection>\n'
        myString += f'  <easting>{self._easting}</easting>\n'
        myString += f'  <northing>{self._northing}</northing>\n'
        myString += f'  <euclideanDistance>{self._euclideanDistance}</euclideanDistance>\n'
        myString += f'  <walkingTime>{self._walkingTime}</walkingTime>\n'
        myString += f'  <pathDistance>{self._pathDistance}</pathDistance>\n'
        myString += f'  <precision>{self._precision}</precision>\n'
        myString += f'  <dietPercent>{self._dietPercent}</dietPercent>\n'
        myString += f'  <plantPercent>{self._percentOfDietThatIsFromCrops}</plantPercent>\n'
        myString += f'  <meatPercent>{self._meatPercent}</meatPercent>\n'
        myString += f'  <caloriesPerPersonDaily>{self._caloriesPerPersonDaily}</caloriesPerPersonDaily>\n'
        myString += f'  <baseOnPlants>{self._baseOnPlants}</baseOnPlants>\n'
        myString += f'  <includeDairy>{self._includeDairy}</includeDairy>\n'
        myString += f'  <limitDairy>{self._limitDairy}</limitDairy>\n'
        myString += f'  <limitDairyPercent>{self._limitDairyPercentage}</limitDairyPercent>\n'
        myString += f'  <dairyUtilisation>{self._dairyUtilisation}</dairyUtilisation>\n'
        myString += '</model>\n'
        return myString


    """ The following defines a series of PyQt signals.

        These signals are used in PyQt to facilitate communication between different parts of a Qt application.
        Each of these signals is associated with a specific property of the LaModel class.

        When the value of the property changes, the corresponding signal is emitted.

        Other parts of the application can connect to these signals to be notified when the
        properties change, allowing them to react accordingly.

        For example, if a GUI element displays the name property of a LaModel instance, it could
        connect a slot to the nameChanged signal. Then, whenever the name property changes and the
        nameChanged signal is emitted, the GUI element automatically updates to display the new name.

        This is a fundamental part of the signal-slot mechanism in Qt, which is used for
        event-driven programming.

    """
