# lamodel.py
from qgis.PyQt.QtCore import (
    QObject, pyqtSignal, pyqtSlot, Qt, QSettings, QProcess, QFile, QTextStream)
from qgis.PyQt.QtWidgets import (
    QDialog, QTreeWidget, QTreeWidgetItem, QTableWidgetItem, QListWidget, QComboBox, QHeaderView)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtXml import QDomDocument, QDomElement
from qgis.PyQt.QtCore import qDebug
from qgis.core import QgsProperty
from typing import Tuple
from builtins import dict as Dict
from builtins import list as List

from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from qgis.PyQt.QtWidgets import QDialog
from typing import Dict, List, Tuple
from lib.la import La
from lib.laserialisable import LaSerialisable
from lib.laguid import LaGuid
from lib.ladietlabels import LaDietLabels
from lib.lautils import LaMessageBus
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
message_bus: LaMessageBus = LaMessageBus()


class LaModel(QDialog, LaSerialisable, LaGuid):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self._name: str = "No Name Set"
        self._population: int = 1000
        self._period: str = "No Period Set"
        self._projection: int = 100
        self._precision: int = 5
        self._dietPercent: int = 25
        self._percentOfDietThatIsFromCrops: int = 10
        self._meatPercent: int = 10
        self._caloriesPerPersonDaily: int = 2500
        self._dairyUtilisation: int = 100
        self._baseOnPlants: bool = True
        self._includeDairy: bool = True
        self._limitDairy: bool = False
        self._limitDairyPercent: int = 10
        self._fallowStatus: Status = Status.FALLOW
        self._fallowRatio: int = 10
        self._easting: int = 0
        self._northing: int = 0
        self._euclideanDistance: bool = True
        self._walkingTime: bool = False
        self._pathDistance: bool = False
        self._commonLandValue: float = 0.0
        self._commonLandAreaUnits: AreaUnits = AreaUnits.HECTARES
        self._herdSize: int = 0
        self._animals: Dict[str, str] = {}
        self._crops: Dict[str, str] = {}
        self._diets: Dict[str, La] = {}
        self._dietLabels: List[LaDietLabels] = []
        self._landBeingGrazed: LandBeingGrazed = LandBeingGrazed.NO
        self._landFound: LandFound = LandFound.NO
        self._priority: Priority = Priority.NORMAL
        self._description: str = "No Description Set"
        self._areaUnits: AreaUnits = AreaUnits.HECTARES
        self._status: Status = Status.FALLOW
        self._guid: str = self.generateGuid()
        self._icon: QIcon = QIcon()
        

    def __del__(self):
        pass

    def __copy__(self):
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
    
    @LandBeingGrazed.setter
    def landBeingGrazed(self, theLandBeingGrazed: LandBeingGrazed):
        if self._landBeingGrazed != theLandBeingGrazed:
            self._landBeingGrazed = theLandBeingGrazed
            self.landBeingGrazedChanged.emit()

    @property
    def landFound(self) -> LandFound:
        return self._landFound
    
    @LandFound.setter
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



"""

This code defines a LaModel class in Python using PyQt5.

The class inherits from QDialog, LaSerialisable, and LaGuid.

It has several properties, including name, description, diets, and dietLabels,
    which are defined using the @pyqtProperty decorator.

It defines slots, including setName, setDescription, setDiets, and setDietLabels
    which are used to set the values of the properties.

The class has several signals including nameChanged, descriptionChanged,
    dietsChanged, and dietLabelsChanged, which are emitted whenever the
    corresponding property is changed.

The lamodel.cpp file defines the implementation of the LaModel class in C++.

The Python version of the class does not require an implementation file, as the
    properties and slots are defined using decorators in the class definition.

"""