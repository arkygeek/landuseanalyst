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
        myModel.name = self._mName

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
        return int(str(self._mDietPercent))

    @dietPercent.setter
    def dietPercent(self, theDietPercent: int):
        if self._mDietPercent != theDietPercent:
            self._mDietPercent = theDietPercent
            self.dietPercentChanged.emit()

    @pyqtProperty(int, notify=percentOfDietThatIsFromCropsChanged)
    def percentOfDietThatIsFromCrops(self) -> int: # type: ignore
        return int(str(self._mPercentOfDietThatIsFromCrops))

    @percentOfDietThatIsFromCrops.setter
    def percentOfDietThatIsFromCrops(self, thePercent: int):
        if self._mPercentOfDietThatIsFromCrops != thePercent:
            self._mPercentOfDietThatIsFromCrops = thePercent
            self.percentOfDietThatIsFromCropsChanged.emit()

    @pyqtProperty(int, notify=meatPercentChanged)
    def meatPercent(self) -> int: # type: ignore
        return int(str(self._mMeatPercent))

    @meatPercent.setter
    def meatPercent(self, theMeatPercent: int):
        if self._mMeatPercent != theMeatPercent:
            self._mMeatPercent = theMeatPercent
            self.meatPercentChanged.emit()

    @pyqtProperty(int, notify=caloriesPerPersonDailyChanged)
    def caloriesPerPersonDaily(self) -> int: # type: ignore
        return int(str(self._mCaloriesPerPersonDaily))

    @caloriesPerPersonDaily.setter
    def caloriesPerPersonDaily(self, theCaloriesPerPersonDaily: int):
        if self._mCaloriesPerPersonDaily != theCaloriesPerPersonDaily:
            self._mCaloriesPerPersonDaily = theCaloriesPerPersonDaily
            self.caloriesPerPersonDailyChanged.emit()

    @pyqtProperty(int, notify=dairyUtilisationChanged)
    def dairyUtilisation(self) -> int: # type: ignore
        return int(str(self._mDairyUtilisation))

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

    def _getAnimalValue(self, animal, prop_name: str) -> float:
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
            # Set values using private attributes
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

            # Emit all the change signals
            theDietLabels.dairyMCaloriesChanged.emit(theOverallDairyMCals)
            theDietLabels.cropMCaloriesChanged.emit(theOverallCropsMCals)
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

            # Debug log the updates
            from la.lib.lautils import LaUtils
            LaUtils.debug.log("Diet labels updated in model", "Diet")
            LaUtils.debug.log(f"Animal: {theOverallMeatPercent*100:.1f}%, Plant: {theOverallPlantPercent*100:.1f}%", "Diet")
            LaUtils.debug.log(f"Wild Animal: {theWildMeatPercent*100:.1f}%, Tame Animal: {theDomesticMeatPercent*100:.1f}%", "Diet")
            LaUtils.debug.log(f"Wild Plant: {theOverallWildPlantPercent*100:.1f}%, Tame Plant: {theOverallCropPercent*100:.1f}%", "Diet")

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error updating diet labels in model: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet portions with animals first and dairy separate.
        
        Dairy products from animal herds are considered separately from meat.
        Plant-based portion is derived from these calculations.
        
        Returns:
            LaDietLabels: Object containing all diet calculations and reports
        """
        # Clear calculation maps
        self._mCalcsCropsMap = {}
        self._mCalcsAnimalsMap = {}
        self._mValueMap = {}
        self._mAnimalCalcReport = {}
        
        myCropCalcsReportMap = {}
        myAnimalCalcsReportMap = {}
        myAnimalsMap = {}  # For storing calculations to send to fallow allocation
        
        # Initialize counters
        myFoodSourceMapCounter = {}
        for myCropGuid in self._mCrops.keys():
            myFoodSourceMapCounter[myCropGuid] = 0
            
        # Basic calorie calculations
        myCalsIndividualAnnual = self._mCaloriesPerPersonDaily * 365.0 * 0.001  # Convert to MCal
        myCalsSettlementAnnual = myCalsIndividualAnnual * self._mPopulation
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0
        
        # Diet percentage calculations
        myPlantPercent = 1.0 - self._mDietPercent
        myDomesticCropPortion = self._mPercentOfDietThatIsFromCrops
        myWildMeatPortion = 1.0 - self._mMeatPercent
        myDairyUtilization = self._mDairyUtilisation * 0.01
        
        # Process each animal
        for myAnimalGuid, myAnimalParamGuid in self._mAnimals.items():
            myAnimal = LaUtils.getAnimal(myAnimalGuid)
            myAnimalParam = LaUtils.getAnimalParameter(myAnimalParamGuid)
            
            # Basic animal parameters
            myMilkKgPerDay = self._getAnimalValue(myAnimal, 'milkGramsPerDay') * 0.001
            myMilkFoodValue = self._getAnimalValue(myAnimal, 'milkFoodValue') * 0.001
            myLactationTime = self._getAnimalValue(myAnimal, 'lactationTime')
            myWeaningAge = self._getAnimalValue(myAnimal, 'weaningAge')
            myGestatingTime = self._getAnimalValue(myAnimal, 'gestationTime')
            myEstrousCycle = self._getAnimalValue(myAnimal, 'estrousCycle')
            myBabiesPerBirth = self._getAnimalValue(myAnimal, 'youngPerBirth')
            
            myDeathRate = self._getAnimalValue(myAnimal, 'deathRate') * 0.01
            myBreedingRatio = self._getAnimalValue(myAnimal, 'femalesPerMale')
            myKillWeight = self._getAnimalValue(myAnimal, 'killWeight')
            myUsablePortionOfAnimal = self._getAnimalValue(myAnimal, 'usableMeat') * 0.01
            myAdultWeight = self._getAnimalValue(myAnimal, 'adultWeight')
            myFemalesToMales = self._getAnimalValue(myAnimal, 'femalesPerMale')
            myConceptionEfficiency = self._getAnimalValue(myAnimal, 'conceptionEfficiency') * 0.01
            myMeatValueMCal = self._getAnimalValue(myAnimal, 'meatFoodValue') * 0.001
            mySexualMaturity = self._getAnimalValue(myAnimal, 'sexualMaturity')  # in months
            myBreedingYears = self._getAnimalValue(myAnimal, 'breedingExpectancy')  # in years
            
            # Calculate animal contribution to meat portion
            myAnimalContributionToMeatPortion = self._getAnimalParamValue(myAnimalParam, 'percentTameMeat') * 0.01
            myAnimalMCalTarget = (myAnimalContributionToMeatPortion * myCalsSettlementAnnual * 
                              self._mDietPercent * self._mMeatPercent)
            
            # Calculate dairy values
            myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge)
            myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal
            myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization
            
            # Calculate birthing events
            myBirthingEventsPerYear1 = 365.0 / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime)
            myBirthingEventsPerYear = 1.0 if myBirthingEventsPerYear1 < 1.0 else myBirthingEventsPerYear1
            
            # Calculate culling values
            myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal * 
                                 (1.0 / ((mySexualMaturity / 12.0) + myBreedingYears)))
            myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear)
            myCulledAdultMalesValue = myCulledMothersValue / myFemalesToMales
            myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue
            
            # Calculate offspring needed and resulting calories
            myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue
            myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue
            myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear
            
            # Update calorie counters
            myTameMeatMCalorieCounter += myMCalsFromTheMeat
            myDairyMCalorieCounter += myMCalsUtilizedFromDairy
            
            # Process fodder requirements
            myFodderSourceMap: Dict[str, str] = self._getAnimalParamValue(myAnimalParam, 'fodderSources')
            myMeatPercent = myMCalsFromTheMeat / myCalsSettlementAnnual
            myDairyPercent = myMCalsUtilizedFromDairy / myCalsSettlementAnnual
            
            # Calculate herd size
            myOffspringPerMotherPerYear = (myBirthingEventsPerYear * myBabiesPerBirth * 
                                       (1.0 - myDeathRate) * myConceptionEfficiency)
            myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear
            myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5
            myFemalesStepOne = myMalesStepOne
            
            myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity/12.0)) / myBreedingYears
            myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio
            myAdditionalMothers = ((myReplacementMothersPerYear/myOffspringPerMotherPerYear)*2.0) + (myBreedingMalesRequired * 2.0)
            myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5
            myFemalesStepTwo = myMalesStepTwo
            
            myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear
            myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo
            myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo
            totalOffspring = myTotalMaleOffspring * 2.0
            
            # Calculate feed requirements
            myFeedForGestating = self._getAnimalValue(myAnimal, 'gestating') * 0.001
            myFeedForLactating = self._getAnimalValue(myAnimal, 'lactating') * 0.001
            myFeedForMaintenance = self._getAnimalValue(myAnimal, 'maintenance') * 0.001
            myFeedForOffspringPerKg = self._getAnimalValue(myAnimal, 'juvenile') * 0.001
            
            myGestatingMCals = totalOffspring * myGestatingTime * myFeedForGestating
            myLactatingMCals = totalOffspring * myLactationTime * myFeedForLactating
            
            # Calculate maintenance requirements
            myDaysForMaintenance = max(0, 365 - (myGestatingTime + myLactationTime))
            myDryMothers = max(0, myTotalMothers - totalOffspring)
            myDryMothersMCals = myDryMothers * 365.0 * myFeedForMaintenance
            myOtherMaintenanceMCals = myDaysForMaintenance * totalOffspring * myFeedForMaintenance
            myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals
            myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.0
            offspringMCals = totalOffspring * myKillWeight * myFeedForOffspringPerKg * (365.0 - myWeaningAge)
            
            # Process fodder sources
            myAdditionalMCalCounter = 0.0
            myAdditionalMCalCounter1 = 0.0
            myFoodSource = LaFoodSource()
            for myCropGuid, myFoodSource in myFodderSourceMap.items():
                grain = myFoodSource.grain * 0.001
                fodder = myFoodSource.fodder * 0.001
                days = myFoodSource.days
                grainToAdd = grain * days * totalOffspring
                grainTotal = myFoodSourceMapCounter.get(myCropGuid, 0) + grainToAdd
                myFoodSourceMapCounter[myCropGuid] = grainTotal
                
                crop = LaUtils.getCrop(myCropGuid)
                foodValueOfCrop = self._getAnimalValue(crop, 'cropCalories') * 0.001
                foodValueOfFodder = self._getAnimalValue(crop, 'fodderEnergy') * 0.001  # Using fodderEnergy instead
                
                grainMCal = grainToAdd * foodValueOfCrop
                fodderMCal = fodder * days * foodValueOfFodder * totalOffspring
                myAdditionalMCalCounter1 += fodderMCal
                myAdditionalMCalCounter += grainMCal + fodderMCal
            
            # Calculate total herd requirements
            animalHerdMCalsRequired1 = (myGestatingMCals + myLactatingMCals + myMaintenanceMCals + 
                                      myAdultMalesMCals + offspringMCals)
            animalHerdMCalsRequired = animalHerdMCalsRequired1 - myAdditionalMCalCounter
            
            # Store calculations in report map
            animalReport = self._generateAnimalReport(
                myAnimal.name, myMilkKgPerDay, myMilkFoodValue, myLactationTime, myWeaningAge,
                myKillWeight, myUsablePortionOfAnimal, myAdultWeight, myFemalesToMales,
                myMeatValueMCal, mySexualMaturity, myBreedingYears, myAnimalContributionToMeatPortion,
                myAnimalMCalTarget, myPotentialDairyPerOffspring, myValuePerOffspring,
                myActualDairyValueOfOffspring, myCulledMothersValue, myCulledAdultMalesValue,
                myFinalOffspringValue, myOffspringNeededPerYear, myMCalsFromTheMeat,
                myMCalsUtilizedFromDairy, myTameMeatMCalorieCounter, myDairyMCalorieCounter,
                myBirthingEventsPerYear, myOffspringPerMotherPerYear, myMothersNeededStepOne,
                myMalesStepOne, myFemalesStepOne, myReplacementMothersPerYear, myBreedingMalesRequired,
                myAdditionalMothers, myMalesStepTwo, myFemalesStepTwo, myTotalMothers,
                myTotalMaleOffspring, myTotalFemaleOffspring, totalOffspring, myFeedForGestating,
                myFeedForLactating, myFeedForMaintenance, myFeedForOffspringPerKg, myGestatingMCals,
                myLactatingMCals, myDaysForMaintenance, myGestatingTime, myLactationTime,
                myDryMothers, myDryMothersMCals, myOtherMaintenanceMCals, myMaintenanceMCals,
                myAdultMalesMCals, offspringMCals, animalHerdMCalsRequired1,
                animalHerdMCalsRequired, myMeatPercent, myDairyPercent)
            
            reportAndAreaTarget = (animalReport, animalHerdMCalsRequired)
            myAnimalCalcsReportMap[myAnimalGuid] = reportAndAreaTarget
            myAnimalsMap[myAnimalGuid] = animalHerdMCalsRequired
            self._mValueMap[myAnimalGuid] = animalHerdMCalsRequired
        
        # Calculate dairy limits
        dairyLimit = self._mLimitDairyPercent * 0.01 if self._mLimitDairy else 1.0
        domesticMeatPercent = myTameMeatMCalorieCounter / myCalsSettlementAnnual
        wildMeatPercent = myWildMeatPortion * self._mDietPercent
        limitSatisfies = (domesticMeatPercent + wildMeatPercent + dairyLimit) > 1.0
        newLimit = (1.0 - domesticMeatPercent - wildMeatPercent) if limitSatisfies else dairyLimit
        
        # Calculate final percentages
        potentialDairyLessThanLimitBool = (myDairyMCalorieCounter / myCalsSettlementAnnual) < dairyLimit
        newDairy = myDairyMCalorieCounter if potentialDairyLessThanLimitBool else newLimit * myCalsSettlementAnnual
        overallDairyPercent = newDairy / myCalsSettlementAnnual
        
        overallMeatPercent = wildMeatPercent + domesticMeatPercent
        overallPlantPercent = 1.0 - overallMeatPercent - overallDairyPercent
        
        # Calculate crop percentages
        overallCropPercent = overallPlantPercent * myDomesticCropPortion
        overallWildPlantPercent = overallPlantPercent * (1.0 - myPlantPercent)
        
        # Calculate final calorie values
        overallDomesticMeatMCals = myTameMeatMCalorieCounter
        overallDairyMCals = overallDairyPercent * myCalsSettlementAnnual
        overallWildMeatMCals = wildMeatPercent * myCalsSettlementAnnual
        overallCropsMCals = overallCropPercent * myCalsSettlementAnnual
        overallWildPlantsMCals = overallWildPlantPercent * myCalsSettlementAnnual
        
        overallMeatMCals = overallWildMeatMCals + overallDomesticMeatMCals
        firstDairySurplusBool = myDairyMCalorieCounter - overallDairyMCals
        overallDairySurplusMCals = max(0, firstDairySurplusBool)
        
        # Create and populate diet labels
        myDietLabels = LaDietLabels()
        
        # Set values using properties
        myDietLabels.dairyMCalories = overallDairyMCals
        myDietLabels.cropMCalories = overallCropsMCals
        myDietLabels.animalMCalories = overallMeatMCals
        myDietLabels.wildAnimalMCalories = overallWildMeatMCals
        myDietLabels.wildPlantsMCalories = overallWildPlantsMCals
        myDietLabels.dairyPortionPct = overallDairyPercent * 100.0
        myDietLabels.tameMeatPortionPct = domesticMeatPercent * 100.0
        myDietLabels.cropsPortionPct = overallCropPercent * 100.0
        myDietLabels.wildAnimalPortionPct = wildMeatPercent * 100.0
        myDietLabels.wildPlantsPortionPct = overallWildPlantPercent * 100.0
        myDietLabels.animalPortionPct = overallMeatPercent * 100.0
        myDietLabels.plantsPortionPct = overallPlantPercent * 100.0
        myDietLabels.kiloCaloriesIndividualAnnual = myCalsIndividualAnnual
        myDietLabels.megaCaloriesSettlementAnnual = myCalsSettlementAnnual
        myDietLabels.dairySurplusMCalories = overallDairySurplusMCals
        
        # Set report maps
        myDietLabels.cropCalcsReportMap = myCropCalcsReportMap
        myDietLabels.animalCalcsReportMap = myAnimalCalcsReportMap
        
        return myDietLabels

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

    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        """Calculate diet portions with plants first and dairy included.
        
        In this calculation method:
        1. Plants portion is calculated first
        2. Dairy products are included with meat calculations
        3. All components must sum to 100% of diet
        
        Returns:
            LaDietLabels: Object containing all diet calculations and reports
        """
        # Initialize diet labels
        dietLabels = LaDietLabels()
        
        # Basic calorie calculations
        mCalsIndividualAnnual = self._mCaloriesPerPersonDaily * 365.0
        mCalsSettlementAnnual = mCalsIndividualAnnual * self._mPopulation
        
        # Initialize counters
        dairyMCalorieCounter = 0.0
        tameMeatMCalorieCounter = 0.0
        wildMeatMCalorieCounter = 0.0
        
        # Calculate basic ratios
        plantVsAnimalRatio = 1.0 - self._mMeatPercent  # c1
        dairyUtilization = self._mDairyUtilisation * 0.01  # c8
        population = self._mPopulation  # c10
        caloriesPerPersonDaily = self._mCaloriesPerPersonDaily  # c11
        totalAnnualCalories = population * caloriesPerPersonDaily * 365.0  # c14
        dietPercent = self._mDietPercent * 0.01  # c15
        cropPercent = self._mPercentOfDietThatIsFromCrops * 0.01  # c12
        
        # Calculate target calories for animals
        targetAnimalCalories = totalAnnualCalories * dietPercent  # e15
        
        # Process each animal
        for animalGuid, animalParamGuid in self._mAnimals.items():
            animal = LaUtils.getAnimal(animalGuid)
            animalParam = LaUtils.getAnimalParameter(animalParamGuid)
            
            # Get milk production values
            milkKgPerDay = self._getAnimalValue(animal, 'milkGramsPerDay') * 0.001  # c2
            milkFoodValue = self._getAnimalValue(animal, 'milkFoodValue')  # c3
            lactationTime = self._getAnimalValue(animal, 'lactationTime')  # c4
            weaningAge = self._getAnimalValue(animal, 'weaningAge')  # c5
            killWeight = self._getAnimalValue(animal, 'killWeight')  # c6
            usablePortionOfAnimal = self._getAnimalValue(animal, 'usableMeat') * 0.01  # c7
            
            # Calculate dairy potential
            dairyValuePerDay = milkKgPerDay * milkFoodValue  # e2 part 1
            potentialDairyValue = dairyValuePerDay * (lactationTime - weaningAge)  # e2
            actualDairyValue = potentialDairyValue * dairyUtilization  # e3
            
            # Calculate meat value
            meatFoodValue = self._getAnimalValue(animal, 'meatFoodValue')  # c9
            meatValue = killWeight * usablePortionOfAnimal * meatFoodValue  # meat portion of e10
            totalAnimalValue = actualDairyValue + meatValue  # e10
            
            # Calculate portion of diet from this animal
            animalPortion = (targetAnimalCalories * (1.0 - plantVsAnimalRatio)) / totalAnimalValue  # e7
            dairyCalories = animalPortion * actualDairyValue  # c21
            meatCalories = animalPortion * killWeight * usablePortionOfAnimal * meatFoodValue  # c23
            wildMeatCalories = targetAnimalCalories - dairyCalories - meatCalories  # c22
            
            # Update calorie counters
            dairyMCalorieCounter += dairyCalories
            wildMeatMCalorieCounter += wildMeatCalories
            tameMeatMCalorieCounter += meatCalories
            
        # Calculate final portions
        wildPlantCalories = (1.0 - cropPercent) * (totalAnnualCalories - targetAnimalCalories)  # c24
        cropCalories = cropPercent * (totalAnnualCalories - targetAnimalCalories)  # c25
        
        # Calculate percentages
        wildPlantPercent = wildPlantCalories / totalAnnualCalories  # c30
        cropPercent_final = cropCalories / totalAnnualCalories  # c31
        wildMeatPercent = wildMeatMCalorieCounter / totalAnnualCalories  # c28
        tameMeatPercent = tameMeatMCalorieCounter / totalAnnualCalories  # c29
        dairyPercent = dairyMCalorieCounter / totalAnnualCalories  # c27
        
        # Create report maps - empty for now
        cropCalcsReportMap = {}
        animalCalcsReportMap = {}
        
        # Convert values to megacalories for output
        dairyMCals = dairyMCalorieCounter * 0.001 * 0.001
        cropMCals = cropCalories * 0.001 * 0.001
        tameMeatMCals = tameMeatMCalorieCounter * 0.001 * 0.001
        wildMeatMCals = wildMeatMCalorieCounter * 0.001 * 0.001
        wildPlantMCals = wildPlantCalories * 0.001 * 0.001
        
        # Set diet label values safely using _set_diet_labels helper method
        self._set_diet_labels(
            theDietLabels=dietLabels,
            theOverallDairyMCals=dairyMCals,
            theOverallCropsMCals=cropMCals,
            theOverallMeatMCals=tameMeatMCals,
            theOverallWildMeatMCals=wildMeatMCals,
            theOverallWildPlantsMCals=wildPlantMCals,
            theOverallDairyPercent=dairyPercent,
            theDomesticMeatPercent=tameMeatPercent,
            theOverallCropPercent=cropPercent_final,
            theWildMeatPercent=wildMeatPercent,
            theOverallWildPlantPercent=wildPlantPercent,
            theOverallMeatPercent=self._mDietPercent - dairyPercent,
            theOverallPlantPercent=(1.0 - self._mDietPercent),
            theMCalsIndividualAnnual=mCalsIndividualAnnual * 0.001,
            theMCalsSettlementAnnual=mCalsSettlementAnnual * 0.001 * 0.001,
            theOverallDairySurplusMCals=0.0,
            theCropCalcsReportMap=cropCalcsReportMap,
            theAnimalCalcsReportMap=animalCalcsReportMap
        )
        
        return dietLabels

    def doCalcsPlantsFirstDairySeperate(self) -> LaDietLabels:
        """Calculate diet portions with plants first and dairy separate from meat.
        
        In this calculation method:
        1. Plants portion is calculated first
        2. Dairy products are considered separately from meat
        3. All components must sum to 100% of diet
        
        Returns:
            LaDietLabels: Object containing all diet calculations and reports
        """
        # Initialize diet labels and counters
        dietLabels = LaDietLabels()
        
        # Basic calorie calculations - these stay in calories (not MCal) until the end
        mCalsIndividualAnnual = self._mCaloriesPerPersonDaily * 365.0
        mCalsSettlementAnnual = mCalsIndividualAnnual * self._mPopulation
        
        # Initialize counters
        dairyMCalorieCounter = 0.0
        tameMeatMCalorieCounter = 0.0
        wildMeatMCalorieCounter = 0.0
        wildPlantsMCalorieCounter = 0.0
        cropsMCalorieCounter = 0.0
        
        # Calculate the percent of diet from each source
        dairyPortionPct = 0.0
        tameMeatPortionPct = 0.0
        cropsPortionPct = 0.0
        wildAnimalPortionPct = 0.0
        wildPlantsPortionPct = 0.0
        
        # First, process all the animals to calculate dairy and meat contributions
        for animalGuid, animalParamGuid in self._mAnimals.items():
            animal = LaUtils.getAnimal(animalGuid)
            animalParam = LaUtils.getAnimalParameter(animalParamGuid)
            
            # Calculate dairy contribution
            milkKgPerDay = self._getAnimalValue(animal, 'milkGramsPerDay') * 0.001
            milkFoodValue = self._getAnimalValue(animal, 'milkFoodValue')
            lactationTime = self._getAnimalValue(animal, 'lactationTime')
            weaningAge = self._getAnimalValue(animal, 'weaningAge')
            
            # Calculate dairy calories per animal
            dairyCaloriesPerAnimal = milkKgPerDay * milkFoodValue * (lactationTime - weaningAge)
            
            # Apply dairy utilization percentage
            dairyCaloriesPerAnimal *= (self._mDairyUtilisation * 0.01)
            
            # Calculate meat contribution
            killWeight = self._getAnimalValue(animal, 'killWeight')
            usableMeat = self._getAnimalValue(animal, 'usableMeat') * 0.01
            meatFoodValue = self._getAnimalValue(animal, 'meatFoodValue')
            
            # Calculate meat calories per animal
            meatCaloriesPerAnimal = killWeight * usableMeat * meatFoodValue
            
            # Get the percentage this animal contributes to meat portion
            animalContribution = self._getAnimalParamValue(animalParam, 'percentTameMeat') * 0.01
            
            # Calculate target calories for this animal
            targetCalories = mCalsSettlementAnnual * self._mDietPercent * (1.0 - self._mPercentOfDietThatIsFromCrops * 0.01) * animalContribution
            
            # If the animal provides both dairy and meat, calculate the split
            totalAnimalCalories = dairyCaloriesPerAnimal + meatCaloriesPerAnimal
            
            # Number of animals needed
            animalsNeeded = targetCalories / totalAnimalCalories
            
            # Total dairy and meat calories from this animal
            dairyCalories = animalsNeeded * dairyCaloriesPerAnimal
            meatCalories = animalsNeeded * meatCaloriesPerAnimal
            
            # Add to counters
            dairyMCalorieCounter += dairyCalories
            tameMeatMCalorieCounter += meatCalories
        
        # Calculate remaining calories for wild meat (this could be more sophisticated)
        wildMeatCalories = (mCalsSettlementAnnual * self._mDietPercent * 
                          (1.0 - self._mPercentOfDietThatIsFromCrops * 0.01) - 
                          tameMeatMCalorieCounter - dairyMCalorieCounter)
        
        # Make sure wild meat calories don't go negative
        wildMeatMCalorieCounter = max(0, wildMeatCalories)
        
        # Calculate plant portions
        plantCalories = mCalsSettlementAnnual * (1.0 - self._mDietPercent)
        cropsMCalorieCounter = plantCalories * (self._mPercentOfDietThatIsFromCrops * 0.01)
        wildPlantsMCalorieCounter = plantCalories * (1.0 - self._mPercentOfDietThatIsFromCrops * 0.01)
        
        # Calculate the percentage each source makes up of the total diet
        totalCalories = mCalsSettlementAnnual
        dairyPortionPct = (dairyMCalorieCounter / totalCalories) * 100.0
        tameMeatPortionPct = (tameMeatMCalorieCounter / totalCalories) * 100.0
        wildAnimalPortionPct = (wildMeatMCalorieCounter / totalCalories) * 100.0
        cropsPortionPct = (cropsMCalorieCounter / totalCalories) * 100.0
        wildPlantsPortionPct = (wildPlantsMCalorieCounter / totalCalories) * 100.0
        
        # Calculate other percentages
        plantsPortionPct = cropsPortionPct + wildPlantsPortionPct
        animalPortionPct = tameMeatPortionPct + wildAnimalPortionPct
        
        # Set diet label values - convert to megacalories (MCal)
        dietLabels.dairyMCalories = dairyMCalorieCounter * 0.001 * 0.001  # Convert to MCal
        dietLabels.cropMCalories = cropsMCalorieCounter * 0.001 * 0.001
        dietLabels.animalMCalories = tameMeatMCalorieCounter * 0.001 * 0.001
        dietLabels.wildAnimalMCalories = wildMeatMCalorieCounter * 0.001 * 0.001
        dietLabels.wildPlantsMCalories = wildPlantsMCalorieCounter * 0.001 * 0.001
        
        # Set percentages
        dietLabels.dairyPortionPct = dairyPortionPct
        dietLabels.tameMeatPortionPct = tameMeatPortionPct
        dietLabels.cropsPortionPct = cropsPortionPct
        dietLabels.wildAnimalPortionPct = wildAnimalPortionPct
        dietLabels.wildPlantsPortionPct = wildPlantsPortionPct
        dietLabels.plantsPortionPct = plantsPortionPct
        dietLabels.animalPortionPct = animalPortionPct
        
        # Set calorie values
        dietLabels.kiloCaloriesIndividualAnnual = mCalsIndividualAnnual * 0.001  # Convert to KCal
        dietLabels.megaCaloriesSettlementAnnual = mCalsSettlementAnnual * 0.001 * 0.001  # Convert to MCal
        
        # No dairy surplus in this method
        dietLabels.dairySurplusMCalories = 0.0
        
        # Set empty report maps for now
        dietLabels.cropCalcsReportMap = {}
        dietLabels.animalCalcsReportMap = {}
        
        return dietLabels

    def doCalcsAnimalsFirstIncludeDiary(self) -> LaDietLabels:
        """Calculate diet portions with animals first and dairy included with meat.
        
        In this calculation method:
        1. Animal portion (meat + dairy) is calculated first
        2. Dairy products are included with meat calculations
        3. Plant-based portion is derived from these calculations
        
        Returns:
            LaDietLabels: Object containing all diet calculations and reports
        """
        # Initialize diet labels and counters
        dietLabels = LaDietLabels()
        
        # Basic calorie calculations
        mCalsIndividualAnnual = self._mCaloriesPerPersonDaily * 365.0
        mCalsSettlementAnnual = mCalsIndividualAnnual * self._mPopulation
        
        # Initialize counters
        dairyMCalorieCounter = 0.0
        tameMeatMCalorieCounter = 0.0
        wildMeatMCalorieCounter = 0.0
        
        # Calculate basic ratios
        c1 = 1.0 - self._mMeatPercent  # Plant vs Animal ratio
        c8 = self._mDairyUtilisation * 0.01  # Dairy utilization percentage
        c10 = self._mPopulation  # Population
        c11 = self._mCaloriesPerPersonDaily  # Calories per person daily
        c14 = c10 * c11 * 365.0  # Total annual calories
        c15 = self._mDietPercent * 0.01  # Diet percentage
        c12 = self._mPercentOfDietThatIsFromCrops * 0.01  # Crop percentage
        
        # Calculate target calories for this calculation
        e15 = c14 * c15  # Target animal calories
        
        # Process each animal
        for animalGuid, animalParamGuid in self._mAnimals.items():
            animal = LaUtils.getAnimal(animalGuid)
            animalParam = LaUtils.getAnimalParameter(animalParamGuid)
            
            # Get milk production values
            c2 = self._getAnimalValue(animal, 'milkGramsPerDay') * 0.001  # Milk kg per day
            c3 = self._getAnimalValue(animal, 'milkFoodValue')  # Milk food value
            c4 = self._getAnimalValue(animal, 'lactationTime')  # Lactation time
            c5 = self._getAnimalValue(animal, 'weaningAge')  # Weaning age
            c6 = self._getAnimalValue(animal, 'killWeight')  # Kill weight
            c7 = self._getAnimalValue(animal, 'usableMeat') * 0.01  # Usable portion
            
            # Calculate dairy potential
            e2 = c2 * c3 * (c4 - c5)  # Potential dairy value
            e3 = e2 * c8  # Actual dairy value
            
            # Calculate meat value
            c9 = self._getAnimalValue(animal, 'meatFoodValue')  # Meat food value
            e10 = e3 + (c9 * c7 * c6)  # Total animal value (dairy + meat)
            
            # Calculate portion of diet from this animal
            e7 = (e15 * (1.0 - c1)) / e10  # Animal portion
            c21 = e7 * e3  # Dairy calories
            c23 = e7 * c6 * c7 * c9  # Meat calories
            c22 = e15 - c21 - c23  # Wild meat calories
            
            # Update calorie counters
            dairyMCalorieCounter += c21
            wildMeatMCalorieCounter += c22
            tameMeatMCalorieCounter += c23
        
        # Calculate plant portions
        c24 = (1.0 - c12) * (c14 - e15)  # Wild plant calories
        c25 = c12 * (c14 - e15)  # Crop calories
        
        # Calculate percentages
        c30 = c24 / c14  # Wild plant percentage
        c31 = c25 / c14  # Crop percentage
        c28 = wildMeatMCalorieCounter / c14  # Wild meat percentage
        c29 = tameMeatMCalorieCounter / c14  # Tame meat percentage
        c27 = dairyMCalorieCounter / c14  # Dairy percentage
        
        # Create and populate diet labels
        dietLabels.dairyMCalories = dairyMCalorieCounter * 0.001 * 0.001  # Convert to megacalories
        dietLabels.cropMCalories = c25 * 0.001 * 0.001
        dietLabels.animalMCalories = tameMeatMCalorieCounter * 0.001 * 0.001
        dietLabels.wildAnimalMCalories = wildMeatMCalorieCounter * 0.001 * 0.001
        dietLabels.wildPlantsMCalories = c24 * 0.001 * 0.001
        
        # Set percentages
        dietLabels.dairyPortionPct = c27 * 100.0
        dietLabels.tameMeatPortionPct = c29 * 100.0
        dietLabels.cropsPortionPct = c31 * 100.0
        dietLabels.wildAnimalPortionPct = c28 * 100.0
        dietLabels.wildPlantsPortionPct = c30 * 100.0
        dietLabels.animalPortionPct = self._mDietPercent - (c27 * 100.0)
        dietLabels.plantsPortionPct = (1.0 - self._mDietPercent) * 100.0
        
        # Set calorie values
        dietLabels.kiloCaloriesIndividualAnnual = mCalsIndividualAnnual * 0.001
        dietLabels.megaCaloriesSettlementAnnual = mCalsSettlementAnnual * 0.001 * 0.001
        
        # No dairy surplus calculation in this method
        dietLabels.dairySurplusMCalories = 0.0
        
        # Set empty report maps for now
        dietLabels.cropCalcsReportMap = {}
        dietLabels.animalCalcsReportMap = {}
        
        return dietLabels

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
