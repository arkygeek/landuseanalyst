from qgis.PyQt.QtCore import pyqtSignal, QUuid
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging
from typing import Dict, List

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound
from la.lib.laanimal import LaAnimal

MESSAGE_BUS: LaMessageBus = LaMessageBus()

class LaModel(QDialog, LaSerialisable, LaGuid):
    """
    LaModel class represents the main model for the Landuse Analyst plugin.

    Attributes:
        nameChanged (pyqtSignal): Signal emitted when the name changes.
        populationChanged (pyqtSignal): Signal emitted when the population changes.
        periodChanged (pyqtSignal): Signal emitted when the period changes.
        projectionChanged (pyqtSignal): Signal emitted when the projection changes.
        precisionChanged (pyqtSignal): Signal emitted when the precision changes.
        dietPercentChanged (pyqtSignal): Signal emitted when the diet percent changes.
        percentOfDietThatIsFromCropsChanged (pyqtSignal): Signal emitted when the percent of diet from crops changes.
        meatPercentChanged (pyqtSignal): Signal emitted when the meat percent changes.
        caloriesPerPersonDailyChanged (pyqtSignal): Signal emitted when the calories per person daily changes.
        dairyUtilisationChanged (pyqtSignal): Signal emitted when the dairy utilisation changes.
        baseOnPlantsChanged (pyqtSignal): Signal emitted when the base on plants changes.
        includeDairyChanged (pyqtSignal): Signal emitted when the include dairy changes.
        limitDairyChanged (pyqtSignal): Signal emitted when the limit dairy changes.
        limitDairyPercentChanged (pyqtSignal): Signal emitted when the limit dairy percent changes.
        fallowStatusChanged (pyqtSignal): Signal emitted when the fallow status changes.
        fallowRatioChanged (pyqtSignal): Signal emitted when the fallow ratio changes.
        eastingChanged (pyqtSignal): Signal emitted when the easting changes.
        northingChanged (pyqtSignal): Signal emitted when the northing changes.
        euclideanDistanceChanged (pyqtSignal): Signal emitted when the euclidean distance changes.
        walkingTimeChanged (pyqtSignal): Signal emitted when the walking time changes.
        pathDistanceChanged (pyqtSignal): Signal emitted when the path distance changes.
        commonLandValueChanged (pyqtSignal): Signal emitted when the common land value changes.
        commonLandAreaUnitsChanged (pyqtSignal): Signal emitted when the common land area units changes.
        herdSizeChanged (pyqtSignal): Signal emitted when the herd size changes.
        animalsChanged (pyqtSignal): Signal emitted when the animals change.
        cropsChanged (pyqtSignal): Signal emitted when the crops change.
        dietsChanged (pyqtSignal): Signal emitted when the diets change.
        dietLabelsChanged (pyqtSignal): Signal emitted when the diet labels change.
        landBeingGrazedChanged (pyqtSignal): Signal emitted when the land being grazed changes.
        landFoundChanged (pyqtSignal): Signal emitted when the land found changes.
        priorityChanged (pyqtSignal): Signal emitted when the priority changes.
        descriptionChanged (pyqtSignal): Signal emitted when the description changes.
        areaUnitsChanged (pyqtSignal): Signal emitted when the area units change.
        statusChanged (pyqtSignal): Signal emitted when the status changes.
        guidChanged (pyqtSignal): Signal emitted when the GUID changes.
        iconChanged (pyqtSignal): Signal emitted when the icon changes.
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

    def __init__(self, parent=None, theModel=None):
        """
        Initialize the LaModel instance.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
            theModel (LaModel, optional): An existing LaModel instance to copy attributes from. Defaults to None.
        """
        super().__init__(parent)
        if theModel is not None:
            self._name = theModel.name
            self._population = theModel.population
            self.setGuid(str(theModel.guid))
            self._period = theModel.period
            self._projection = theModel.projection
            self._easting = theModel.easting
            self._northing = theModel.northing
            self._euclideanDistance = theModel.euclideanDistance
            self._walkingTime = theModel.walkingTime
            self._pathDistance = theModel.pathDistance
            self._precision = theModel.precision
            self._dietPercent = theModel.dietPercent
            self._percentOfDietThatIsFromCrops = theModel.percentOfDietThatIsFromCrops
            self._meatPercent = theModel.meatPercent
            self._caloriesPerPersonDaily = theModel.caloriesPerPersonDaily
            self._dairyUtilisation = theModel.dairyUtilisation
            self._baseOnPlants = theModel.baseOnPlants
            self._includeDairy = theModel.includeDairy
            self._limitDairy = theModel.limitDairy
            self._limitDairyPercent = theModel.limitDairyPercent
            self._fallowStatus = theModel.fallowStatus
            self._fallowRatio = theModel.fallowRatio
            self._landBeingGrazed = theModel.landBeingGrazed
            self._landFound = theModel.landFound
        else:
            self.setGuid(None)
            self._name = "No Name Set"
            self._population = 1000
            self._period = "No Period Set"
            self._projection = 100
            self._precision = 5
            self._dietPercent = 25
            self._percentOfDietThatIsFromCrops = 10
            self._meatPercent = 10
            self._caloriesPerPersonDaily = 2500
            self._dairyUtilisation = 100
            self._baseOnPlants = True
            self._includeDairy = True
            self._limitDairy = False
            self._limitDairyPercent = 10
            self._fallowStatus = Status.MoreThanEnoughToCompletelySatisfy
            self._fallowRatio = 1
            self._easting = 0
            self._northing = 0
            self._euclideanDistance = True
            self._walkingTime = False
            self._pathDistance = False
            self._commonLandValue = 0.0
            self._commonLandAreaUnits = AreaUnits.Hectare
            self._herdSize = 0
            self._animals = {}
            self._crops = {}
            self._diets = {}
            self._dietLabels = []
            self._landBeingGrazed = LandBeingGrazed.Common
            self._landFound = LandFound.NotEnough
            self._priority = Priority.None_
            self._description = "No Description Set"
            self._areaUnits = AreaUnits.Hectare
            self._status = Status.MoreThanEnoughToCompletelySatisfy
            self._icon = None
        self.logger = logging.getLogger(__name__)

    def logMessage(self, theMessage: str):
        """
        Logs a message using the logger.

        Args:
            message (str): The message to log.
        """
        self.logger.info(theMessage)

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
        return int(self._herdSize)

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
    def diets(self) -> Dict[str, LaDietLabels]:
        return self._diets

    @diets.setter
    def diets(self, theDiets: Dict[str, LaDietLabels]):
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
            self.setGuid(theGuid)
            self.guidChanged.emit()

    def requiredValue(self, theAnimalGuid):
        """
        Calculates the required value for the given animal GUID.

        Args:
            theAnimalGuid (str): The GUID of the animal.

        Returns:
            float: The required value.
        """
        myAnimal = LaUtils.getAnimal(theAnimalGuid)
        myAnimalProductionTarget = 1
        myAnimalsRequired = (myAnimalProductionTarget / myAnimal.killWeight()) / (myAnimal.usableMeat() * 0.01)
        myBirthsPerYear = 365.0 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + myAnimal.weaningAge())
        myOffspringPerMotherYearly = myBirthsPerYear * myAnimal.youngPerBirth() * (1.0 - (0.01 * myAnimal.deathRate()))
        myMothersNeededStepOne = myAnimalsRequired / myOffspringPerMotherYearly
        myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly) / 2.0
        myFemalesStepOne = myMalesStepOne
        myMotherReplacementsPerYear = myMothersNeededStepOne / myAnimal.breedingExpectancy()
        myAdditionalMothers = (myMotherReplacementsPerYear / myOffspringPerMotherYearly) * 2.0
        myMalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myFemalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myTotalMothers = myMothersNeededStepOne + myAdditionalMothers
        myTotalMales = myMalesStepOne + myMalesStepTwo
        myTotalFemales = myFemalesStepOne - myFemalesStepTwo
        myTotalJuveniles = myTotalMales + myTotalFemales
        myTotalMothersValueRequired = myTotalMothers * myAnimal.gestating()
        myTotalJuvenilesValueRequired = myTotalJuveniles * myAnimal.juvenile()
        myValueNeededToFeedAnimals = myTotalMothersValueRequired + myTotalJuvenilesValueRequired
        myReturnValue = float(myValueNeededToFeedAnimals)

        # Log report
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
        self.logMessage("animal prodn target = calorie target of animal / food value")
        self.logMessage(f"mCaloriesProvidedByMeatMap.value(theAnimalGuid): {self.mCaloriesProvidedByMeatMap.get(theAnimalGuid, 0)}")
        self.logMessage(f"myAnimal.meatFoodValue(): {myAnimal.meatFoodValue() / 1000.0}")
        self.logMessage(f"myAnimalProductionTarget = {myAnimalProductionTarget}")
        self.logMessage(f"slaughter animals reqd: {myAnimalsRequired}")
        self.logMessage(f"BirthEventsPerYear: {myBirthsPerYear}")
        self.logMessage(f"OffspringPerMotherYearly = {myOffspringPerMotherYearly}")
        self.logMessage(f"MothersNeededStepOne = {myMothersNeededStepOne}")
        self.logMessage(f"MalesStepOne = {myMalesStepOne}")
        self.logMessage(f"FemalesStepOne = {myFemalesStepOne}")
        self.logMessage(f"MotherReplacementsPerYear = {myMotherReplacementsPerYear}")
        self.logMessage(f"AdditionalMothers = {myAdditionalMothers}")
        self.logMessage(f"MalesStepTwo = {myMalesStepTwo}")
        self.logMessage(f"FemalesStepTwo = {myFemalesStepTwo}")
        self.logMessage(f"TotalMothers = {myTotalMothers}")
        self.logMessage(f"TotalMales = {myTotalMales}")
        self.logMessage(f"TotalFemales = {myTotalFemales}")
        self.logMessage(f"TotalJuveniles = {myTotalJuveniles}")
        self.logMessage(f"Total Adult Females Value(Kg) = {myTotalMothersValueRequired}")
        self.logMessage(f"Total Juveniles Value(Kg) = {myTotalJuvenilesValueRequired}")
        self.logMessage(f"Total Value (Kg) Needed To Feed Animals = {myValueNeededToFeedAnimals}")
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
        self.logMessage(f"Animal: {myAnimal.name()}")
        self.logMessage(f"Breeding Stock: {myTotalMothers}")
        self.logMessage(f"Juveniles: {myTotalJuveniles}")
        self.logMessage(f"Kg Value needed annually to feed the entire herd: {myReturnValue}")
        self.logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        return myReturnValue

    def fromXml(self, theXmlData):
        """
        Initialize the LaModel instance from an XML string.

        Args:
            theXmlData (str): The XML string containing the model data.
        """
        root = ET.fromstring(theXmlData)

        self._guid = root.attrib.get('guid', QUuid.createUuid().toString(QUuid.StringFormat.Id128))
        self._name = root.findtext('name', default="No Name Set")
        self._population = int(root.findtext('population', default="1000"))
        self._period = root.findtext('period', default="No Period Set")
        self._projection = int(root.findtext('projection', default="100"))
        self._easting = int(root.findtext('easting', default="0"))
        self._northing = int(root.findtext('northing', default="0"))
        self._euclideanDistance = root.findtext('euclideanDistance', default="True") == "True"
        self._walkingTime = root.findtext('walkingTime', default="False") == "False"
        self._pathDistance = root.findtext('pathDistance', default="False") == "False"
        self._precision = int(root.findtext('precision', default="5"))
        self._dietPercent = int(root.findtext('dietPercent', default="25"))
        self._percentOfDietThatIsFromCrops = int(root.findtext('plantPercent', default="10"))
        self._meatPercent = int(root.findtext('meatPercent', default="10"))
        self._caloriesPerPersonDaily = int(root.findtext('caloriesPerPersonDaily', default="2500"))
        self._baseOnPlants = root.findtext('baseOnPlants', default="True") == "True"
        self._includeDairy = root.findtext('includeDairy', default="True") == "True"
        self._limitDairy = root.findtext('limitDairy', default="False") == "False"
        self._limitDairyPercent = int(root.findtext('limitDairyPercent', default="10"))
        self._dairyUtilisation = int(root.findtext('dairyUtilisation', default="100"))
        self._fallowStatus = Status[root.findtext('fallowStatus', default="FALLOW")]
        self._fallowRatio = int(root.findtext('fallowRatio', default="1"))
        self._commonLandValue = float(root.findtext('commonLandValue', default="0.0"))
        self._commonLandAreaUnits = AreaUnits[root.findtext('commonLandAreaUnits', default="HECTARES")]
        self._herdSize = int(root.findtext('herdSize', default="0"))
        self._animals = {}  # Assuming animals are stored in a more complex structure
        self._crops = {}  # Assuming crops are stored in a more complex structure
        self._diets = {}  # Assuming diets are stored in a more complex structure
        self._dietLabels = []  # Assuming diet labels are stored in a more complex structure
        self._landBeingGrazed = LandBeingGrazed[root.findtext('landBeingGrazed', default="NO")]
        self._landFound = LandFound[root.findtext('landFound', default="NO")]
        self._priority = Priority[root.findtext('priority', default="NORMAL")]
        self._description = root.findtext('description', default="No Description Set")
        self._areaUnits = AreaUnits[root.findtext('areaUnits', default="HECTARES")]
        self._status = Status[root.findtext('status', default="FALLOW")]
        self._icon = None  # Assuming icon is handled separately

    def toXml(self) -> str:
        myString = f'<model guid="{self.guid}">\n'
        myString += f'  <name>{LaUtils.xmlEncode(self._name)}</name>\n'
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
        myString += f'  <limitDairyPercent>{self._limitDairyPercent}</limitDairyPercent>\n'
        myString += f'  <dairyUtilisation>{self._dairyUtilisation}</dairyUtilisation>\n'
        myString += '</model>\n'
        return myString

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """
        Calculate diet portions with animals first and dairy separate.
        Dairy products from animal herds are considered separately from meat.
        Plant-based portion is derived from these calculations.

        Returns:
            LaDietLabels: Object containing all diet calculations and reports
        """
        # Clear calculation maps
        self._calcsCropsMap = {}
        self._calcsAnimalsMap = {}
        self._valueMap = {}
        self._animalCalcReport = {}

        cropCalcsReportMap = {}
        animalCalcsReportMap = {}
        animalsMap = {}  # For storing calculations to send to fallow allocation

        # Initialize counters
        foodSourceMapCounter = {}
        for cropGuid in self._crops.keys():
            foodSourceMapCounter[cropGuid] = 0

        # Basic calorie calculations
        mCalsIndividualAnnual = self._caloriesPerPersonDaily * 365.0 * 0.001  # Convert to MCal
        mCalsSettlementAnnual = mCalsIndividualAnnual * self._population
        dairyMCalorieCounter = 0.0
        tameMeatMCalorieCounter = 0.0

        # Diet percentage calculations
        plantPercent = 1.0 - self._dietPercent
        domesticCropPortion = self._percentOfDietThatIsFromCrops
        wildMeatPortion = 1.0 - self._meatPercent
        dairyUtilization = self._dairyUtilisation * 0.01

        # Process each animal
        for animalGuid, animalParamGuid in self._animals.items():
            animal = LaUtils.getAnimal(animalGuid)
            animalParam = LaUtils.getAnimalParameter(animalParamGuid)

            # Basic animal parameters
            milkKgPerDay = animal.milkGramsPerDay * 0.001
            milkFoodValue = animal.milkFoodValue * 0.001
            lactationTime = animal.lactationTime
            weaningAge = animal.weaningAge
            gestatingTime = animal.gestationTime
            estrousCycle = animal.estrousCycle
            babiesPerBirth = animal.youngPerBirth

            deathRate = animal.deathRate * 0.01
            breedingRatio = animal.femalesPerMale
            killWeight = animal.killWeight
            usablePortionOfAnimal = animal.usableMeat * 0.01
            adultWeight = animal.adultWeight
            femalesToMales = animal.femalesPerMale
            conceptionEfficiency = animal.conceptionEfficiency * 0.01
            meatValueMCal = animal.meatFoodValue * 0.001
            sexualMaturity = animal.sexualMaturity  # in months
            breedingYears = animal.breedingExpectancy  # in years

            # Calculate animal contribution to meat portion
            animalContributionToMeatPortion = animalParam.percentTameMeat * 0.01
            animalMCalTarget = (animalContributionToMeatPortion * mCalsSettlementAnnual *
                              self._dietPercent * self._meatPercent)

            # Calculate dairy values
            potentialDairyPerOffspring = milkKgPerDay * milkFoodValue * (lactationTime - weaningAge)
            valuePerOffspring = killWeight * usablePortionOfAnimal * meatValueMCal
            actualDairyValueOfOffspring = potentialDairyPerOffspring * dairyUtilization

            # Calculate birthing events
            birthingEventsPerYear1 = 365.0 / (weaningAge + gestatingTime + estrousCycle + lactationTime)
            birthingEventsPerYear = 1.0 if birthingEventsPerYear1 < 1.0 else birthingEventsPerYear1

            # Calculate culling values
            culledMothersValue1 = (adultWeight * meatValueMCal * usablePortionOfAnimal *
                                 (1.0 / ((sexualMaturity / 12.0) + breedingYears)))
            culledMothersValue = culledMothersValue1 / (babiesPerBirth * birthingEventsPerYear)
            culledAdultMalesValue = culledMothersValue / femalesToMales
            finalOffspringValue = valuePerOffspring + culledMothersValue + culledAdultMalesValue

            # Calculate offspring needed and resulting calories
            offspringNeededPerYear = animalMCalTarget / finalOffspringValue
            mCalsFromTheMeat = offspringNeededPerYear * finalOffspringValue
            mCalsUtilizedFromDairy = actualDairyValueOfOffspring * offspringNeededPerYear

            # Update calorie counters
            tameMeatMCalorieCounter += mCalsFromTheMeat
            dairyMCalorieCounter += mCalsUtilizedFromDairy

            # Process fodder requirements
            foodSourceMap = animalParam.fodderSourceMap
            meatPercent = mCalsFromTheMeat / mCalsSettlementAnnual
            dairyPercent = mCalsUtilizedFromDairy / mCalsSettlementAnnual

            # Calculate herd size
            offspringPerMotherPerYear = (birthingEventsPerYear * babiesPerBirth *
                                       (1.0 - deathRate) * conceptionEfficiency)
            mothersNeededStepOne = offspringNeededPerYear / offspringPerMotherPerYear
            malesStepOne = mothersNeededStepOne * offspringPerMotherPerYear * 0.5
            femalesStepOne = malesStepOne

            replacementMothersPerYear = (mothersNeededStepOne + (sexualMaturity/12.0)) / breedingYears
            breedingMalesRequired = ((mothersNeededStepOne / breedingRatio) + mothersNeededStepOne) / breedingRatio
            additionalMothers = ((replacementMothersPerYear/offspringPerMotherPerYear)*2.0) + (breedingMalesRequired * 2.0)
            malesStepTwo = additionalMothers * offspringPerMotherPerYear * 0.5
            femalesStepTwo = malesStepTwo

            totalMothers = mothersNeededStepOne + replacementMothersPerYear
            totalMaleOffspring = malesStepOne + malesStepTwo
            totalFemaleOffspring = femalesStepOne - femalesStepTwo
            totalOffspring = totalMaleOffspring * 2.0

            # Calculate feed requirements
            feedForGestating = animal.gestating * 0.001
            feedForLactating = animal.lactating * 0.001
            feedForMaintenance = animal.maintenance * 0.001
            feedForOffspringPerKg = animal.juvenile * 0.001

            gestatingMCals = totalOffspring * gestatingTime * feedForGestating
            lactatingMCals = totalOffspring * lactationTime * feedForLactating

            # Calculate maintenance requirements
            daysForMaintenance = max(0, 365 - (gestatingTime + lactationTime))
            dryMothers = max(0, totalMothers - totalOffspring)
            dryMothersMCals = dryMothers * 365.0 * feedForMaintenance
            otherMaintenanceMCals = daysForMaintenance * totalOffspring * feedForMaintenance
            maintenanceMCals = dryMothersMCals + otherMaintenanceMCals
            adultMalesMCals = breedingMalesRequired * feedForMaintenance * 365.0
            offspringMCals = totalOffspring * killWeight * feedForOffspringPerKg * (365.0 - weaningAge)

            # Process fodder sources
            additionalMCalCounter = 0.0
            additionalMCalCounter1 = 0.0
            for cropGuid, foodSource in foodSourceMap.items():
                grain = foodSource.grain * 0.001
                fodder = foodSource.fodder * 0.001
                days = foodSource.days
                grainToAdd = grain * days * totalOffspring
                grainTotal = foodSourceMapCounter.get(cropGuid, 0) + grainToAdd
                foodSourceMapCounter[cropGuid] = grainTotal

                crop = LaUtils.getCrop(cropGuid)
                foodValueOfCrop = crop.cropCalories * 0.001
                foodValueOfFodder = crop.fodderValue * 0.001

                grainMCal = grainToAdd * foodValueOfCrop
                fodderMCal = fodder * days * foodValueOfFodder * totalOffspring
                additionalMCalCounter1 += fodderMCal
                additionalMCalCounter += grainMCal + fodderMCal

            # Calculate total herd requirements
            animalHerdMCalsRequired1 = (gestatingMCals + lactatingMCals + maintenanceMCals +
                                      adultMalesMCals + offspringMCals)
            animalHerdMCalsRequired = animalHerdMCalsRequired1 - additionalMCalCounter

            # Store calculations in report map
            animalReport = self._generateAnimalReport(
                animal.name, milkKgPerDay, milkFoodValue, lactationTime, weaningAge,
                killWeight, usablePortionOfAnimal, adultWeight, femalesToMales,
                meatValueMCal, sexualMaturity, breedingYears, animalContributionToMeatPortion,
                animalMCalTarget, potentialDairyPerOffspring, valuePerOffspring,
                actualDairyValueOfOffspring, culledMothersValue, culledAdultMalesValue,
                finalOffspringValue, offspringNeededPerYear, mCalsFromTheMeat,
                mCalsUtilizedFromDairy, tameMeatMCalorieCounter, dairyMCalorieCounter,
                birthingEventsPerYear, offspringPerMotherPerYear, mothersNeededStepOne,
                malesStepOne, femalesStepOne, replacementMothersPerYear, breedingMalesRequired,
                additionalMothers, malesStepTwo, femalesStepTwo, totalMothers,
                totalMaleOffspring, totalFemaleOffspring, totalOffspring, feedForGestating,
                feedForLactating, feedForMaintenance, feedForOffspringPerKg, gestatingMCals,
                lactatingMCals, daysForMaintenance, gestatingTime, lactationTime,
                dryMothers, dryMothersMCals, otherMaintenanceMCals, maintenanceMCals,
                adultMalesMCals, offspringMCals, animalHerdMCalsRequired1,
                animalHerdMCalsRequired, meatPercent, dairyPercent)

            reportAndAreaTarget = (animalReport, animalHerdMCalsRequired)
            animalCalcsReportMap[animalGuid] = reportAndAreaTarget
            animalsMap[animalGuid] = animalHerdMCalsRequired
            self._valueMap[animalGuid] = animalHerdMCalsRequired

        # Calculate dairy limits
        dairyLimit = self._limitDairyPercent * 0.01 if self._limitDairy else 1.0
        domesticMeatPercent = tameMeatMCalorieCounter / mCalsSettlementAnnual
        wildMeatPercent = wildMeatPortion * self._dietPercent
        limitSatisfies = (domesticMeatPercent + wildMeatPercent + dairyLimit) > 1.0
        newLimit = (1.0 - domesticMeatPercent - wildMeatPercent) if limitSatisfies else dairyLimit

        # Calculate final percentages
        potentialDairyLessThanLimitBool = (dairyMCalorieCounter / mCalsSettlementAnnual) < dairyLimit
        newDairy = dairyMCalorieCounter if potentialDairyLessThanLimitBool else newLimit * mCalsSettlementAnnual
        overallDairyPercent = newDairy / mCalsSettlementAnnual

        overallMeatPercent = wildMeatPercent + domesticMeatPercent
        overallPlantPercent = 1.0 - overallMeatPercent - overallDairyPercent

        # Calculate crop percentages
        overallCropPercent = overallPlantPercent * domesticCropPortion
        overallWildPlantPercent = overallPlantPercent * (1.0 - plantPercent)

        # Calculate final calorie values
        overallDomesticMeatMCals = tameMeatMCalorieCounter
        overallDairyMCals = overallDairyPercent * mCalsSettlementAnnual
        overallWildMeatMCals = wildMeatPercent * mCalsSettlementAnnual
        overallCropsMCals = overallCropPercent * mCalsSettlementAnnual
        overallWildPlantsMCals = overallWildPlantPercent * mCalsSettlementAnnual

        overallMeatMCals = overallWildMeatMCals + overallDomesticMeatMCals
        firstDairySurplusBool = dairyMCalorieCounter - overallDairyMCals
        overallDairySurplusMCals = max(0, firstDairySurplusBool)

        # Create and populate diet labels
        dietLabels = LaDietLabels()
        dietLabels.dairyMCalories = overallDairyMCals
        dietLabels.cropMCalories = overallCropsMCals
        dietLabels.animalMCalories = overallMeatMCals
        dietLabels.wildAnimalMCalories = overallWildMeatMCals
        dietLabels.wildPlantsMCalories = overallWildPlantsMCals
        dietLabels.dairyPortionPct = overallDairyPercent * 100.0
        dietLabels.tameMeatPortionPct = domesticMeatPercent * 100.0
        dietLabels.cropsPortionPct = overallCropPercent * 100.0
        dietLabels.wildAnimalPortionPct = wildMeatPercent * 100.0
        dietLabels.wildPlantsPortionPct = overallWildPlantPercent * 100.0
        dietLabels.animalPortionPct = overallMeatPercent * 100.0
        dietLabels.plantsPortionPct = overallPlantPercent * 100.0
        dietLabels.kiloCaloriesIndividualAnnual = mCalsIndividualAnnual
        dietLabels.megaCaloriesSettlementAnnual = mCalsSettlementAnnual
        dietLabels.dairySurplusMCalories = overallDairySurplusMCals

        # Set report maps
        dietLabels.cropCalcsReportMap = cropCalcsReportMap
        dietLabels.animalCalcsReportMap = animalCalcsReportMap

        return dietLabels

    def _generateAnimalReport(self, *args) -> str:
        """Generate a formatted report string for animal calculations."""
        # Template for animal report - actual implementation would format all the args
        report = []
        params = [
            "Animal Name", "Milk kg/day", "Milk food value", "Lactation time",
            "Weaning age", "Kill weight", "Usable portion", "Adult weight",
            "Females to males ratio", "Meat value (MCal)", "Sexual maturity",
            "Breeding years", "Meat portion contribution", "MCal target",
            "Potential dairy per offspring", "Value per offspring",
            "Actual dairy value", "Culled mothers value", "Culled males value",
            "Final offspring value", "Offspring needed/year", "MCals from meat",
            "MCals from dairy", "Total tame meat MCals", "Total dairy MCals",
            "Birthing events/year", "Offspring per mother/year", "Mothers needed",
            "Males step 1", "Females step 1", "Replacement mothers/year",
            "Breeding males required", "Additional mothers", "Males step 2",
            "Females step 2", "Total mothers", "Total male offspring",
            "Total female offspring", "Total offspring", "Feed for gestating",
            "Feed for lactating", "Feed for maintenance", "Feed for offspring/kg",
            "Gestating MCals", "Lactating MCals", "Days for maintenance",
            "Gestating time", "Lactation time", "Dry mothers",
            "Dry mothers MCals", "Other maintenance MCals", "Total maintenance MCals",
            "Adult males MCals", "Offspring MCals", "Herd MCals required (initial)",
            "Herd MCals required (final)", "Meat percent", "Dairy percent"
        ]

        for param, value in zip(params, args):
            report.append(f"{param} = {value}")

        return "\n".join(report)

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
