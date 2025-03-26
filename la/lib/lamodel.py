from qgis.PyQt.QtCore import pyqtProperty, pyqtSignal, QUuid
from qgis.PyQt.QtWidgets import QDialog

import xml.etree.ElementTree as ET
import logging
from typing import Dict, List, Tuple

from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.ladietlabels import LaDietLabels
from la.lib.lautils import LaUtils, LaMessageBus
from la.lib.la import AreaUnits, Status, Priority, LandBeingGrazed, LandFound
from la.lib.laanimal import LaAnimal
from la.lib.lafoodsource import LaFoodSource

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
            self._mName = theModel.name
            self._mPopulation = theModel.population
            self.setGuid(str(theModel.guid))
            self._mPeriod = theModel.period
            self._mProjection = theModel.projection
            self._mEasting = theModel.easting
            self._mNorthing = theModel.northing
            self._mEuclideanDistance = theModel.euclideanDistance
            self._mWalkingTime = theModel.walkingTime
            self._mPathDistance = theModel.pathDistance
            self._mPrecision = theModel.precision
            self._mDietPercent = theModel.dietPercent
            self._mPercentOfDietThatIsFromCrops = theModel.percentOfDietThatIsFromCrops
            self._mMeatPercent = theModel.meatPercent
            self._mCaloriesPerPersonDaily = theModel.caloriesPerPersonDaily
            self._mDairyUtilisation = theModel.dairyUtilisation
            self._mBaseOnPlants = theModel.baseOnPlants
            self._mIncludeDairy = theModel.includeDairy
            self._mLimitDairy = theModel.limitDairy
            self._mLimitDairyPercent = theModel.limitDairyPercent
            self._mFallowStatus = theModel.fallowStatus
            self._mFallowRatio = theModel.fallowRatio
            self._mLandBeingGrazed = theModel.landBeingGrazed
            self._mLandFound = theModel.landFound
        else:
            self.setGuid(None)
            self._mName = "No Name Set"
            self._mPopulation = 1000
            self._mPeriod = "No Period Set"
            self._mProjection = 100
            self._mPrecision = 5
            self._mDietPercent = 25
            self._mPercentOfDietThatIsFromCrops = 10
            self._mMeatPercent = 10
            self._mCaloriesPerPersonDaily = 2500
            self._mDairyUtilisation = 100
            self._mBaseOnPlants = True
            self._mIncludeDairy = True
            self._mLimitDairy = False
            self._mLimitDairyPercent = 10
            self._mFallowStatus = Status.MoreThanEnoughToCompletelySatisfy
            self._mFallowRatio = 1
            self._mEasting = 0
            self._mNorthing = 0
            self._mEuclideanDistance = True
            self._mWalkingTime = False
            self._mPathDistance = False
            self._mCommonLandValue = 0.0
            self._mCommonLandAreaUnits = AreaUnits.Hectare
            self._mHerdSize = 0
            self._mAnimals = {}
            self._mCrops = {}
            self._mDiets = {}
            self._mDietLabels = []
            self._mLandBeingGrazed = LandBeingGrazed.Common
            self._mLandFound = LandFound.NotEnough
            self._mPriority = Priority.None_
            self._mDescription = "No Description Set"
            self._mAreaUnits = AreaUnits.Hectare
            self._mStatus = Status.MoreThanEnoughToCompletelySatisfy
            self._mIcon = None
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
        myModel.name = self.name

        return LaModel(self)

    def __deepcopy__(self, memo):
        return LaModel(self)

    @pyqtProperty(str, notify=nameChanged)
    def name(self) -> str: # type: ignore
        return self._mName

    @name.setter
    def name(self, theName: str):
        if self._mName != theName:
            self._mName = theName
            self.nameChanged.emit()

    @pyqtProperty(int, notify=populationChanged)
    def population(self) -> int: # type: ignore
        return int(str(self._mPopulation))

    @population.setter
    def population(self, thePopulation: int):
        if self._mPopulation != thePopulation:
            self._mPopulation = thePopulation
            self.populationChanged.emit()

    @pyqtProperty(str, notify=periodChanged)
    def period(self) -> str: # type: ignore
        return str(self._mPeriod)

    @period.setter
    def period(self, thePeriod: str):
        if self._mPeriod != thePeriod:
            self._mPeriod = thePeriod
            self.periodChanged.emit()



    @pyqtProperty(int, notify=projectionChanged)
    def projection(self) -> int: # type: ignore
        return int(str(self._mProjection))

    @projection.setter
    def projection(self, theProjection: int):
        if self._mProjection != theProjection:
            self._mProjection = theProjection
            self.projectionChanged.emit()

    @pyqtProperty(int, notify=precisionChanged)
    def precision(self) -> int: # type: ignore
        return int(str(self._mPrecision))

    @precision.setter
    def precision(self, thePrecision: int):
        if self._mPrecision != thePrecision:
            self._mPrecision = thePrecision
            self.precisionChanged.emit()

    @pyqtProperty(int, notify=dietPercentChanged)
    def dietPercent(self) -> int: # type: ignore
        return int(self._mDietPercent)

    @dietPercent.setter
    def dietPercent(self, theDietPercent: int):
        if self._mDietPercent != theDietPercent:
            self._mDietPercent = theDietPercent
            self.dietPercentChanged.emit()

    @pyqtProperty(int, notify=percentOfDietThatIsFromCropsChanged)
    def percentOfDietThatIsFromCrops(self) -> int: # type: ignore
        return int(self._mPercentOfDietThatIsFromCrops)

    @percentOfDietThatIsFromCrops.setter
    def percentOfDietThatIsFromCrops(self, thePercent: int):
        if self._mPercentOfDietThatIsFromCrops != thePercent:
            self._mPercentOfDietThatIsFromCrops = thePercent
            self.percentOfDietThatIsFromCropsChanged.emit()

    @pyqtProperty(int, notify=meatPercentChanged)
    def meatPercent(self) -> int: # type: ignore
        return int(self._mMeatPercent)

    @meatPercent.setter
    def meatPercent(self, theMeatPercent: int):
        if self._mMeatPercent != theMeatPercent:
            self._mMeatPercent = theMeatPercent
            self.meatPercentChanged.emit()

    @pyqtProperty(int, notify=caloriesPerPersonDailyChanged)
    def caloriesPerPersonDaily(self) -> int: # type: ignore
        return int(self._mCaloriesPerPersonDaily)

    @caloriesPerPersonDaily.setter
    def caloriesPerPersonDaily(self, theCaloriesPerPersonDaily: int):
        if self._mCaloriesPerPersonDaily != theCaloriesPerPersonDaily:
            self._mCaloriesPerPersonDaily = theCaloriesPerPersonDaily
            self.caloriesPerPersonDailyChanged.emit()

    @pyqtProperty(int, notify=dairyUtilisationChanged)
    def dairyUtilisation(self) -> int: # type: ignore
        return int(self._mDairyUtilisation)

    @dairyUtilisation.setter
    def dairyUtilisation(self, thePercent: int):
        if self._mDairyUtilisation != thePercent:
            self._mDairyUtilisation = thePercent
            self.dairyUtilisationChanged.emit()

    @pyqtProperty(bool, notify=baseOnPlantsChanged)
    def baseOnPlants(self) -> bool: # type: ignore
        return bool(self._mBaseOnPlants)
        """ Hint on usage to read and set the checkbox state
            # When reading from checkbox
            self._baseOnPlants = self.cboxBaseOnPlants.isChecked()
            # When setting checkbox state
            self.cboxBaseOnPlants.setChecked(self._baseOnPlants)
        """

    @baseOnPlants.setter
    def baseOnPlants(self, theBool: bool):
        if self._mBaseOnPlants != theBool:
            self._mBaseOnPlants = theBool
            self.baseOnPlantsChanged.emit()

    @pyqtProperty(bool, notify=includeDairyChanged)
    def includeDairy(self) -> bool: # type: ignore
        return bool(self._mIncludeDairy)

    @includeDairy.setter
    def includeDairy(self, theBool: bool):
        if self._mIncludeDairy != theBool:
            self._mIncludeDairy = theBool
            self.includeDairyChanged.emit()

    @pyqtProperty(bool, notify=limitDairyChanged)
    def limitDairy(self) -> bool: # type: ignore
        return bool(self._mLimitDairy)

    @limitDairy.setter
    def limitDairy(self, theBool: bool):
        if self._mLimitDairy != theBool:
            self._mLimitDairy = theBool
            self.limitDairyChanged.emit()

    @pyqtProperty(int, notify=limitDairyPercentChanged)
    def limitDairyPercent(self) -> int: # type: ignore
        return int(str(self._mLimitDairyPercent))

    @limitDairyPercent.setter
    def limitDairyPercent(self, thePercent: int):
        if self._mLimitDairyPercent != thePercent:
            self._mLimitDairyPercent = thePercent
            self.limitDairyPercentChanged.emit()

    @pyqtProperty(str, notify=fallowStatusChanged) # TODO: set this to the correct return type
    def fallowStatus(self) -> Status: # type: ignore
        return (self._mFallowStatus)

    @fallowStatus.setter
    def fallowStatus(self, theStatus: Status):
        if self._mFallowStatus != theStatus:
            self._mFallowStatus = theStatus
            self.fallowStatusChanged.emit()

    @pyqtProperty(int, notify=fallowRatioChanged)
    def fallowRatio(self) -> int: # type: ignore
        return int(str(self._mFallowRatio))

    @fallowRatio.setter
    def fallowRatio(self, theRatio: int):
        if self._mFallowRatio != theRatio:
            self._mFallowRatio = theRatio
            self.fallowRatioChanged.emit()

    @pyqtProperty(int, notify=eastingChanged)
    def easting(self) -> int: # type: ignore
        return int(str(self._mEasting))

    @easting.setter
    def easting(self, theEasting: int):
        if self._mEasting != theEasting:
            self._mEasting = theEasting
            self.eastingChanged.emit()

    @pyqtProperty(int, notify=northingChanged)
    def northing(self) -> int: # type: ignore
        return int(str(self._mNorthing))

    @northing.setter
    def northing(self, theNorthing: int):
        if self._mNorthing != theNorthing:
            self._mNorthing = theNorthing
            self.northingChanged.emit()

    @pyqtProperty(bool, notify=euclideanDistanceChanged)
    def euclideanDistance(self) -> bool: # type: ignore
        return bool(self._mEuclideanDistance)

    @euclideanDistance.setter
    def euclideanDistance(self, theBool: bool):
        if self._mEuclideanDistance != theBool:
            self._mEuclideanDistance = theBool
            self.euclideanDistanceChanged.emit()

    @pyqtProperty(bool, notify=walkingTimeChanged)
    def walkingTime(self) -> bool: # type: ignore
        return bool(self._mWalkingTime)

    @walkingTime.setter
    def walkingTime(self, theBool: bool):
        if self._mWalkingTime != theBool:
            self._mWalkingTime = theBool
            self.walkingTimeChanged.emit()

    @pyqtProperty(bool, notify=pathDistanceChanged)
    def pathDistance(self) -> bool: # type: ignore
        return bool(self._mPathDistance)

    @pathDistance.setter
    def pathDistance(self, theBool: bool):
        if self._mPathDistance != theBool:
            self._mPathDistance = theBool
            self.pathDistanceChanged.emit()

    @pyqtProperty(float, notify=commonLandValueChanged)
    def commonLandValue(self) -> float: # type: ignore
        return float(str(self._mCommonLandValue))

    @commonLandValue.setter
    def commonLandValue(self, theValue: float):
        if self._mCommonLandValue != theValue:
            self._mCommonLandValue = theValue
            self.commonLandValueChanged.emit()

    @pyqtProperty(AreaUnits, notify=commonLandAreaUnitsChanged)
    def commonLandAreaUnits(self) -> AreaUnits: # type: ignore
        return self._mCommonLandAreaUnits # TODO: figure out how to do this

    @commonLandAreaUnits.setter
    def commonLandAreaUnits(self, theAreaUnits: AreaUnits):
        if self._mCommonLandAreaUnits != theAreaUnits:
            self._mCommonLandAreaUnits = theAreaUnits
            self.commonLandAreaUnitsChanged.emit()

    @pyqtProperty(int, notify=herdSizeChanged)
    def herdSize(self) -> int: # type: ignore
        return int(str(self._mHerdSize))

    @herdSize.setter
    def herdSize(self, theAnimalGuid: str):
        if self._mHerdSize != theAnimalGuid:
            self._mHerdSize = theAnimalGuid
            self.herdSizeChanged.emit()

    @pyqtProperty(str, notify=animalsChanged) # TODO: check this I think Dict type might be wrong
    def animals(self) -> Dict[str, str]: # type: ignore
        return self._mAnimals

    @animals.setter
    def animals(self, theAnimals: Dict[str, str]):
        if self._mAnimals != theAnimals:
            self._mAnimals = theAnimals
            self.animalsChanged.emit()

    @pyqtProperty(str, notify=cropsChanged) # TODO: check this to see if it is correct
    def crops(self) -> Dict[str, str]: # type: ignore
        return self._mCrops

    @crops.setter
    def crops(self, theCrops: Dict[str, str]):
        if self._mCrops != theCrops:
            self._mCrops = theCrops
            self.cropsChanged.emit()

    @pyqtProperty(str, notify=dietsChanged) # TODO: check this to see if it is correct
    def diets(self) -> Dict[str, LaDietLabels]: # type: ignore
        return self._mDiets

    @diets.setter
    def diets(self, theDiets: Dict[str, LaDietLabels]):
        if self._mDiets != theDiets:
            self._mDiets = theDiets
            self.dietsChanged.emit()

    @pyqtProperty(str, notify=dietLabelsChanged) # TODO: check this to see if it is correct
    def dietLabels(self) -> List[LaDietLabels]: # type: ignore
        return self._mDietLabels

    @dietLabels.setter
    def dietLabels(self, theDietLabels: List[LaDietLabels]):
        if self._mDietLabels != theDietLabels:
            self._mDietLabels = theDietLabels
            self.dietLabelsChanged.emit()

    @pyqtProperty(str, notify=landBeingGrazedChanged) # TODO: check this to see if it is correct
    def landBeingGrazed(self) -> LandBeingGrazed: # type: ignore
        return self._mLandBeingGrazed

    @landBeingGrazed.setter
    def landBeingGrazed(self, theLandBeingGrazed: LandBeingGrazed):
        if self._mLandBeingGrazed != theLandBeingGrazed:
            self._mLandBeingGrazed = theLandBeingGrazed
            self.landBeingGrazedChanged.emit()

    @pyqtProperty(str, notify=landFoundChanged)
    def landFound(self) -> LandFound: # type: ignore
        return self._mLandFound

    @landFound.setter
    def landFound(self, theLandFound: LandFound):
        if self._mLandFound != theLandFound:
            self._mLandFound = theLandFound
            self.landFoundChanged.emit()

    @pyqtProperty(str, notify=priorityChanged)
    def priority(self) -> Priority: # type: ignore
        return self._mPriority

    @priority.setter
    def priority(self, thePriority: Priority):
        if self._mPriority != thePriority:
            self._mPriority = thePriority
            self.priorityChanged.emit()

    @pyqtProperty(str, notify=descriptionChanged)
    def description(self) -> str: # type: ignore
        return self._mDescription

    @description.setter
    def description(self, theDescription: str):
        if self._mDescription != theDescription:
            self._mDescription = theDescription
            self.descriptionChanged.emit()

    @pyqtProperty(str, notify=areaUnitsChanged)
    def areaUnits(self) -> AreaUnits: # type: ignore
        return self._mAreaUnits

    @areaUnits.setter
    def areaUnits(self, theAreaUnits: AreaUnits):
        if self._mAreaUnits != theAreaUnits:
            self._mAreaUnits = theAreaUnits
            self.areaUnitsChanged.emit()

    @pyqtProperty(str, notify=statusChanged)
    def status(self) -> Status: # type: ignore
        return self._mStatus

    @status.setter
    def status(self, theStatus: Status):
        if self._mStatus != theStatus:
            self._mStatus = theStatus
            self.statusChanged.emit()

    @property
    def guid(self) -> str:
        return self._mGuid

    @guid.setter
    def guid(self, theGuid: str):
        if self._mGuid != theGuid:
            self.setGuid(theGuid)
            self.guidChanged.emit()

    def requiredValue(self, theAnimalGuid: str) -> float:
        """Calculate required value for an animal.

        Args:
            theAnimalGuid (str): GUID of the animal to calculate for

        Returns:
            float: The required value
        """
        myAnimal = LaUtils.getAnimal(theAnimalGuid)
        myAnimalProductionTarget = 1
        myAnimalsRequired = (myAnimalProductionTarget / float(str(myAnimal.killWeight))) / (float(str(myAnimal.usableMeat)) * 0.01)
        myBirthsPerYear = 365.0 / (float(str(myAnimal.gestationTime)) + float(str(myAnimal.estrousCycle)) + float(str(myAnimal.weaningAge)))
        myOffspringPerMotherYearly = myBirthsPerYear * float(str(myAnimal.youngPerBirth)) * (1.0 - (0.01 * float(str(myAnimal.deathRate))))
        myMothersNeededStepOne = myAnimalsRequired / myOffspringPerMotherYearly
        myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly) / 2.0
        myFemalesStepOne = myMalesStepOne
        myMotherReplacementsPerYear = myMothersNeededStepOne / float(str(myAnimal.breedingExpectancy))
        myAdditionalMothers = (myMotherReplacementsPerYear / myOffspringPerMotherYearly) * 2.0
        myMalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myFemalesStepTwo = (myAdditionalMothers * myOffspringPerMotherYearly) / 2.0
        myTotalMothers = myMothersNeededStepOne + myAdditionalMothers
        myTotalMales = myMalesStepOne + myMalesStepTwo
        myTotalFemales = myFemalesStepOne - myFemalesStepTwo
        myTotalJuveniles = myTotalMales + myTotalFemales
        myTotalMothersValueRequired = myTotalMothers * float(str(myAnimal.gestating))
        myTotalJuvenilesValueRequired = myTotalJuveniles * float(str(myAnimal.juvenile))
        myValueNeededToFeedAnimals = myTotalMothersValueRequired + myTotalJuvenilesValueRequired
        myReturnValue = float(myValueNeededToFeedAnimals)

        # Log report
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
        self.logMessage("animal prodn target = calorie target of animal / food value")
        self.logMessage(f"Animal Production Target: {myAnimalProductionTarget}")
        self.logMessage(f"Slaughter animals required: {myAnimalsRequired}")
        self.logMessage(f"Birth events per year: {myBirthsPerYear}")
        self.logMessage(f"Offspring per mother yearly = {myOffspringPerMotherYearly}")
        self.logMessage(f"Mothers needed step one = {myMothersNeededStepOne}")
        self.logMessage(f"Males step one = {myMalesStepOne}")
        self.logMessage(f"Females step one = {myFemalesStepOne}")
        self.logMessage(f"Mother replacements per year = {myMotherReplacementsPerYear}")
        self.logMessage(f"Additional mothers = {myAdditionalMothers}")
        self.logMessage(f"Males step two = {myMalesStepTwo}")
        self.logMessage(f"Females step two = {myFemalesStepTwo}")
        self.logMessage(f"Total mothers = {myTotalMothers}")
        self.logMessage(f"Total males = {myTotalMales}")
        self.logMessage(f"Total females = {myTotalFemales}")
        self.logMessage(f"Total juveniles = {myTotalJuveniles}")
        self.logMessage(f"Total adult females value (Kg) = {myTotalMothersValueRequired}")
        self.logMessage(f"Total juveniles value (Kg) = {myTotalJuvenilesValueRequired}")
        self.logMessage(f"Total value (Kg) needed to feed animals = {myValueNeededToFeedAnimals}")
        self.logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)")
        self.logMessage(f"Animal: {myAnimal.name}")
        self.logMessage(f"Breeding stock: {myTotalMothers}")
        self.logMessage(f"Juveniles: {myTotalJuveniles}")
        self.logMessage(f"Kg value needed annually to feed the entire herd: {myReturnValue}")
        self.logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        return myReturnValue

    def fromXml(self, theXmlData):
        """
        Initialize the LaModel instance from an XML string.

        Args:
            theXmlData (str): The XML string containing the model data.
        """
        root = ET.fromstring(theXmlData)

        self._mGuid = root.attrib.get('guid', QUuid.createUuid().toString(QUuid.StringFormat.Id128))
        self._mName = root.findtext('name', default="No Name Set")
        self._mPopulation = int(root.findtext('population', default="1000"))
        self._mPeriod = root.findtext('period', default="No Period Set")
        self._mProjection = int(root.findtext('projection', default="100"))
        self._mEasting = int(root.findtext('easting', default="0"))
        self._mNorthing = int(root.findtext('northing', default="0"))
        self._mEuclideanDistance = root.findtext('euclideanDistance', default="True") == "True"
        self._mWalkingTime = root.findtext('walkingTime', default="False") == "False"
        self._mPathDistance = root.findtext('pathDistance', default="False") == "False"
        self._mPrecision = int(root.findtext('precision', default="5"))
        self._mDietPercent = int(root.findtext('dietPercent', default="25"))
        self._mPercentOfDietThatIsFromCrops = int(root.findtext('plantPercent', default="10"))
        self._mMeatPercent = int(root.findtext('meatPercent', default="10"))
        self._mCaloriesPerPersonDaily = int(root.findtext('caloriesPerPersonDaily', default="2500"))
        self._mBaseOnPlants = root.findtext('baseOnPlants', default="True") == "True"
        self._mIncludeDairy = root.findtext('includeDairy', default="True") == "True"
        self._mLimitDairy = root.findtext('limitDairy', default="False") == "False"
        self._mLimitDairyPercent = int(root.findtext('limitDairyPercent', default="10"))
        self._mDairyUtilisation = int(root.findtext('dairyUtilisation', default="100"))
        self._mFallowStatus = Status[root.findtext('fallowStatus', default="FALLOW")]
        self._mFallowRatio = int(root.findtext('fallowRatio', default="1"))
        self._mCommonLandValue = float(root.findtext('commonLandValue', default="0.0"))
        self._mCommonLandAreaUnits = AreaUnits[root.findtext('commonLandAreaUnits', default="HECTARES")]
        self._mHerdSize = int(root.findtext('herdSize', default="0"))
        self._mAnimals = {}  # Assuming animals are stored in a more complex structure
        self._mCrops = {}  # Assuming crops are stored in a more complex structure
        self._mDiets = {}  # Assuming diets are stored in a more complex structure
        self._mDietLabels = []  # Assuming diet labels are stored in a more complex structure
        self._mLandBeingGrazed = LandBeingGrazed[root.findtext('landBeingGrazed', default="NO")]
        self._mLandFound = LandFound[root.findtext('landFound', default="NO")]
        self._mPriority = Priority[root.findtext('priority', default="NORMAL")]
        self._mDescription = root.findtext('description', default="No Description Set")
        self._mAreaUnits = AreaUnits[root.findtext('areaUnits', default="HECTARES")]
        self._mStatus = Status[root.findtext('status', default="FALLOW")]
        self._mIcon = None  # Assuming icon is handled separately

    def toXml(self) -> str:
        myString = f'<model guid="{self.guid}">\n'
        myString += f'  <name>{LaUtils.xmlEncode(self._mName)}</name>\n'
        myString += f'  <population>{self._mPopulation}</population>\n'
        myString += f'  <period>{LaUtils.xmlEncode(self._mPeriod)}</period>\n'
        myString += f'  <projection>{self._mProjection}</projection>\n'
        myString += f'  <easting>{self._mEasting}</easting>\n'
        myString += f'  <northing>{self._mNorthing}</northing>\n'
        myString += f'  <euclideanDistance>{self._mEuclideanDistance}</euclideanDistance>\n'
        myString += f'  <walkingTime>{self._mWalkingTime}</walkingTime>\n'
        myString += f'  <pathDistance>{self._mPathDistance}</pathDistance>\n'
        myString += f'  <precision>{self._mPrecision}</precision>\n'
        myString += f'  <dietPercent>{self._mDietPercent}</dietPercent>\n'
        myString += f'  <plantPercent>{self._mPercentOfDietThatIsFromCrops}</plantPercent>\n'
        myString += f'  <meatPercent>{self._mMeatPercent}</meatPercent>\n'
        myString += f'  <caloriesPerPersonDaily>{self._mCaloriesPerPersonDaily}</caloriesPerPersonDaily>\n'
        myString += f'  <baseOnPlants>{self._mBaseOnPlants}</baseOnPlants>\n'
        myString += f'  <includeDairy>{self._mIncludeDairy}</includeDairy>\n'
        myString += f'  <limitDairy>{self._mLimitDairy}</limitDairy>\n'
        myString += f'  <limitDairyPercent>{self._mLimitDairyPercent}</limitDairyPercent>\n'
        myString += f'  <dairyUtilisation>{self._mDairyUtilisation}</dairyUtilisation>\n'
        myString += '</model>\n'
        return myString

    def _GetAnimalValue(self, animal, prop_name: str) -> float:
        """Helper method to safely get float values from animal properties."""
        prop = getattr(animal, prop_name, None)
        if prop is None:
            return 0.0
        if isinstance(prop, property):
            return float(prop.__get__(animal, type(animal)))
        return float(prop)

    def _getAnimalParamValue(self, param, prop_name: str) -> float:
        """Helper method to safely get float values from animal parameter properties."""
        prop = getattr(param, prop_name, None)
        if prop is None:
            return 0.0
        if isinstance(prop, property):
            return float(prop.__get__(param, type(param)))
        return float(prop)

    def _set_diet_labels(self, theDietLabels: LaDietLabels,
                        theOverallDairyMCals: float,
                        theOverallCropsMCals: float,
                        theOverallMeatMCals: float,
                        theOverallWildMeatMCals: float,
                        theOverallWildPlantsMCals: float,
                        theOverallDairyPercent: float,
                        theDomesticMeatPercent: float,
                        theOverallCropPercent: float,
                        theWildMeatPercent: float,
                        theOverallWildPlantPercent: float,
                        theOverallMeatPercent: float,
                        theOverallPlantPercent: float,
                        theMCalsIndividualAnnual: float,
                        theMCalsSettlementAnnual: float,
                        theOverallDairySurplusMCals: float,
                        theCropCalcsReportMap: Dict[str, Tuple[str, float]],
                        theAnimalCalcsReportMap: Dict[str, Tuple[str, float]]) -> None:
        """Helper method to safely set all diet label private attributes."""
        try:
            # Log the ID of the object we're updating to help with debugging
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Setting values for diet labels object with ID: {id(theDietLabels)}", "Diet")
            LaUtils.debug.log(f"Previous values - Dairy: {theDietLabels.dairyMCalories:.2f}, Crops: {theDietLabels.cropMCalories:.2f}", "Diet")
            
            # Set values directly to attributes first
            theDietLabels._dairyMCalories = theOverallDairyMCals
            theDietLabels._cropMCalories = theOverallCropsMCals
            theDietLabels._animalMCalories = theOverallMeatMCals
            theDietLabels._wildAnimalMCalories = theOverallWildMeatMCals
            theDietLabels._wildPlantsMCalories = theOverallWildPlantsMCals
            theDietLabels._dairyPortionPct = theOverallDairyPercent * 100.0
            theDietLabels._tameMeatPortionPct = theDomesticMeatPercent * 100.0
            theDietLabels._cropsPortionPct = theOverallCropPercent * 100.0
            theDietLabels._wildAnimalPortionPct = theWildMeatPercent * 100.0
            theDietLabels._wildPlantsPortionPct = theOverallWildPlantPercent * 100.0
            theDietLabels._plantsPortionPct = theOverallPlantPercent * 100.0
            theDietLabels._animalPortionPct = theOverallMeatPercent * 100.0
            theDietLabels._kiloCaloriesIndividualAnnual = theMCalsIndividualAnnual
            theDietLabels._megaCaloriesSettlementAnnual = theMCalsSettlementAnnual
            theDietLabels._dairySurplusMCalories = theOverallDairySurplusMCals
            theDietLabels._cropCalcsReportMap = theCropCalcsReportMap
            theDietLabels._animalCalcsReportMap = theAnimalCalcsReportMap
            
            # Log new values before emitting signals
            LaUtils.debug.log(f"New values set - Dairy: {theOverallDairyMCals:.2f}, Crops: {theOverallCropsMCals:.2f}", "Diet")
            LaUtils.debug.log(f"New percentages - Animal: {theOverallMeatPercent*100:.2f}%, Plants: {theOverallPlantPercent*100:.2f}%", "Diet")
            
            # Now emit all the signals after setting the attributes directly
            LaUtils.debug.log("Emitting diet value change signals", "Diet")
            
            try:
                theDietLabels.dairyMCaloriesChanged.emit(theOverallDairyMCals)
                LaUtils.debug.log(f"Emitted dairyMCaloriesChanged with value {theOverallDairyMCals:.2f}", "Diet")
                
                theDietLabels.cropMCaloriesChanged.emit(theOverallCropsMCals)
                LaUtils.debug.log(f"Emitted cropMCaloriesChanged with value {theOverallCropsMCals:.2f}", "Diet")
                
                theDietLabels.animalMCaloriesChanged.emit(theOverallMeatMCals)
                theDietLabels.wildAnimalMCaloriesChanged.emit(theOverallWildMeatMCals)
                theDietLabels.wildPlantsMCaloriesChanged.emit(theOverallWildPlantsMCals)
                theDietLabels.dairyPortionPctChanged.emit(theOverallDairyPercent * 100.0)
                theDietLabels.tameMeatPortionPctChanged.emit(theDomesticMeatPercent * 100.0)
                theDietLabels.cropsPortionPctChanged.emit(theOverallCropPercent * 100.0)
                theDietLabels.wildAnimalPortionPctChanged.emit(theWildMeatPercent * 100.0)
                theDietLabels.wildPlantsPortionPctChanged.emit(theOverallWildPlantPercent * 100.0)
                theDietLabels.plantsPortionPctChanged.emit(theOverallPlantPercent * 100.0)
                theDietLabels.animalPortionPctChanged.emit(theOverallMeatPercent * 100.0)
                theDietLabels.kiloCaloriesIndividualAnnualChanged.emit(theMCalsIndividualAnnual)
                theDietLabels.megaCaloriesSettlementAnnualChanged.emit(theMCalsSettlementAnnual)
                theDietLabels.dairySurplusMCaloriesChanged.emit(theOverallDairySurplusMCals)
                theDietLabels.cropCalcsReportMapChanged.emit(theCropCalcsReportMap)
                theDietLabels.animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)
                
                LaUtils.debug.log("All diet label signals emitted successfully", "Diet")
            except Exception as e:
                LaUtils.debug.log(f"Error emitting diet label signals: {str(e)}", "Error") 
                import traceback
                LaUtils.debug.log(f"Signal error details: {traceback.format_exc()}", "Error")
        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error updating diet labels in model: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is included with meat."""
        myDietLabels = LaDietLabels()
        
        # Get property values from internal attributes
        calories_daily = float(self._mCaloriesPerPersonDaily)
        population_count = float(self._mPopulation)
        meat_percent = float(self._mMeatPercent)
        diet_percent = float(self._mDietPercent)
        dairy_util = float(self._mDairyUtilisation)
        
        # Calculate base values
        myMCalsIndividualAnnual = calories_daily * 365.0
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count
        
        # Initialize counters
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0
        myWildMeatMCalorieCounter = 0.0
        
        # Basic ratios
        plantRatio = 1.0 - meat_percent
        
        # Calculate calorie targets
        totalAnnualCals = population_count * calories_daily * 365.0
        meatTarget = totalAnnualCals * diet_percent / 100.0
        
        # Set the calculated values using private attributes
        myDietLabels._dairyMCalories = myDairyMCalorieCounter
        myDietLabels._animalMCalories = myTameMeatMCalorieCounter
        myDietLabels._wildAnimalMCalories = myWildMeatMCalorieCounter
        myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
        
        # Calculate and set percentages
        myDietLabels._plantsPortionPct = (1.0 - diet_percent/100.0) * 100.0
        myDietLabels._animalPortionPct = diet_percent
        
        # Emit signals for changed values
        myDietLabels.dairyMCaloriesChanged.emit(myDairyMCalorieCounter)
        myDietLabels.animalMCaloriesChanged.emit(myTameMeatMCalorieCounter)
        myDietLabels.wildAnimalMCaloriesChanged.emit(myWildMeatMCalorieCounter)
        myDietLabels.kiloCaloriesIndividualAnnualChanged.emit(myMCalsIndividualAnnual)
        myDietLabels.megaCaloriesSettlementAnnualChanged.emit(myMCalsSettlementAnnual)
        myDietLabels.plantsPortionPctChanged.emit(myDietLabels._plantsPortionPct)
        myDietLabels.animalPortionPctChanged.emit(myDietLabels._animalPortionPct)
        
        return myDietLabels

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        myDietLabels = LaDietLabels()
        
        # Base calculations similar to include dairy but with separate dairy tracking
        calories_daily = float(self._mCaloriesPerPersonDaily)
        population_count = float(self._mPopulation)
        
        myMCalsIndividualAnnual = calories_daily * 365.0
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count
        
        # Initialize counters
        myDairyCounter = 0.0
        myMeatCounter = 0.0
        
        # Set calculated values using private attributes
        myDietLabels._dairyMCalories = myDairyCounter
        myDietLabels._animalMCalories = myMeatCounter
        myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
        
        # Emit signals for changed values
        myDietLabels.dairyMCaloriesChanged.emit(myDairyCounter)
        myDietLabels.animalMCaloriesChanged.emit(myMeatCounter)
        myDietLabels.kiloCaloriesIndividualAnnualChanged.emit(myMCalsIndividualAnnual)
        myDietLabels.megaCaloriesSettlementAnnualChanged.emit(myMCalsSettlementAnnual)
        
        return myDietLabels

    def doCalcsAnimalsFirstIncludeDiary(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is included with meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()

        # Log start of calculation
        LaUtils.debug.log("Starting doCalcsAnimalsFirstIncludeDiary calculation", "Diet")

        # Similar base calculations but prioritizing animal products
        calories_daily = float(self._mCaloriesPerPersonDaily)
        population_count = float(self._mPopulation)

        # Log input values
        LaUtils.debug.log(f"Calories per person daily: {calories_daily}", "Diet")
        LaUtils.debug.log(f"Population count: {population_count}", "Diet")

        myMCalsIndividualAnnual = calories_daily * 365.0
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

        # Log calculated values
        LaUtils.debug.log(f"Annual individual calories (MCal): {myMCalsIndividualAnnual}", "Diet")
        LaUtils.debug.log(f"Annual settlement calories (MCal): {myMCalsSettlementAnnual}", "Diet")

        # Set values using private attributes
        myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual

        # Emit signals for changed values
        myDietLabels.kiloCaloriesIndividualAnnualChanged.emit(myMCalsIndividualAnnual)
        myDietLabels.megaCaloriesSettlementAnnualChanged.emit(myMCalsSettlementAnnual)

        # Log signal emissions
        LaUtils.debug.log(f"Emitted kiloCaloriesIndividualAnnualChanged with value: {myMCalsIndividualAnnual}", "Diet")
        LaUtils.debug.log(f"Emitted megaCaloriesSettlementAnnualChanged with value: {myMCalsSettlementAnnual}", "Diet")

        # Log end of calculation
        LaUtils.debug.log("Completed doCalcsAnimalsFirstIncludeDiary calculation", "Diet")

        return myDietLabels

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is separate from meat."""
        myDietLabels = LaDietLabels()
        
        # Get base values from internal attributes
        calories_daily = float(self._mCaloriesPerPersonDaily)
        population_count = float(self._mPopulation)
        
        # Calculate base values
        myMCalsIndividualAnnual = calories_daily * 365.0
        myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count
        
        # Initialize calculation maps
        myCropCalcsReportMap = {}
        myAnimalCalcsReportMap = {}
        
        # Set calculated values using private attributes
        myDietLabels._kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels._megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
        myDietLabels._cropCalcsReportMap = myCropCalcsReportMap
        myDietLabels._animalCalcsReportMap = myAnimalCalcsReportMap
        
        # Emit signals for changed values
        myDietLabels.kiloCaloriesIndividualAnnualChanged.emit(myMCalsIndividualAnnual)
        myDietLabels.megaCaloriesSettlementAnnualChanged.emit(myMCalsSettlementAnnual)
        myDietLabels.cropCalcsReportMapChanged.emit(myCropCalcsReportMap)
        myDietLabels.animalCalcsReportMapChanged.emit(myAnimalCalcsReportMap)
        
        return myDietLabels
