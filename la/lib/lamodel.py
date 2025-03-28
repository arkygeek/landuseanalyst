from la.lib.laanimalparameter import LaAnimalParameter
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
        animalsChanged (pyqtSignal): Signal emitted when the animals change.
        areaUnitsChanged (pyqtSignal): Signal emitted when the area units change.
        baseOnPlantsChanged (pyqtSignal): Signal emitted when the base on plants changes.
        caloriesPerPersonDailyChanged (pyqtSignal): Signal emitted when the calories per person daily changes.
        commonLandAreaUnitsChanged (pyqtSignal): Signal emitted when the common land area units changes.
        commonLandValueChanged (pyqtSignal): Signal emitted when the common land value changes.
        cropsChanged (pyqtSignal): Signal emitted when the crops change.
        dairyUtilisationChanged (pyqtSignal): Signal emitted when the dairy utilisation changes.
        descriptionChanged (pyqtSignal): Signal emitted when the description changes.
        dietLabelsChanged (pyqtSignal): Signal emitted when the diet labels change.
        dietPercentChanged (pyqtSignal): Signal emitted when the diet percent changes.
        dietsChanged (pyqtSignal): Signal emitted when the diets change.
        eastingChanged (pyqtSignal): Signal emitted when the easting changes.
        euclideanDistanceChanged (pyqtSignal): Signal emitted when the euclidean distance changes.
        fallowRatioChanged (pyqtSignal): Signal emitted when the fallow ratio changes.
        fallowStatusChanged (pyqtSignal): Signal emitted when the fallow status changes.
        guidChanged (pyqtSignal): Signal emitted when the GUID changes.
        herdSizeChanged (pyqtSignal): Signal emitted when the herd size changes.
        iconChanged (pyqtSignal): Signal emitted when the icon changes.
        includeDairyChanged (pyqtSignal): Signal emitted when the include dairy changes.
        landBeingGrazedChanged (pyqtSignal): Signal emitted when the land being grazed changes.
        landFoundChanged (pyqtSignal): Signal emitted when the land found changes.
        limitDairyChanged (pyqtSignal): Signal emitted when the limit dairy changes.
        limitDairyPercentChanged (pyqtSignal): Signal emitted when the limit dairy percent changes.
        meatPercentChanged (pyqtSignal): Signal emitted when the meat percent changes.
        nameChanged (pyqtSignal): Signal emitted when the name changes.
        northingChanged (pyqtSignal): Signal emitted when the northing changes.
        pathDistanceChanged (pyqtSignal): Signal emitted when the path distance changes.
        percentOfDietThatIsFromCropsChanged (pyqtSignal): Signal emitted when the percent of diet from crops changes.
        periodChanged (pyqtSignal): Signal emitted when the period changes.
        populationChanged (pyqtSignal): Signal emitted when the population changes.
        precisionChanged (pyqtSignal): Signal emitted when the precision changes.
        priorityChanged (pyqtSignal): Signal emitted when the priority changes.
        projectionChanged (pyqtSignal): Signal emitted when the projection changes.
        statusChanged (pyqtSignal): Signal emitted when the status changes.
        walkingTimeChanged (pyqtSignal): Signal emitted when the walking time changes.
    """
    animalsChanged = pyqtSignal()
    areaUnitsChanged = pyqtSignal()
    baseOnPlantsChanged = pyqtSignal()
    caloriesPerPersonDailyChanged = pyqtSignal()
    commonLandAreaUnitsChanged = pyqtSignal()
    commonLandValueChanged = pyqtSignal()
    cropsChanged = pyqtSignal()
    dairyUtilisationChanged = pyqtSignal()
    descriptionChanged = pyqtSignal()
    dietLabelsChanged = pyqtSignal()
    dietPercentChanged = pyqtSignal()
    dietsChanged = pyqtSignal()
    eastingChanged = pyqtSignal()
    euclideanDistanceChanged = pyqtSignal()
    fallowRatioChanged = pyqtSignal()
    fallowStatusChanged = pyqtSignal()
    guidChanged = pyqtSignal()
    herdSizeChanged = pyqtSignal()
    iconChanged = pyqtSignal()
    includeDairyChanged = pyqtSignal()
    landBeingGrazedChanged = pyqtSignal()
    landFoundChanged = pyqtSignal()
    limitDairyChanged = pyqtSignal()
    limitDairyPercentChanged = pyqtSignal()
    meatPercentChanged = pyqtSignal()
    nameChanged = pyqtSignal()
    northingChanged = pyqtSignal()
    pathDistanceChanged = pyqtSignal()
    percentOfDietThatIsFromCropsChanged = pyqtSignal()
    periodChanged = pyqtSignal()
    populationChanged = pyqtSignal()
    precisionChanged = pyqtSignal()
    priorityChanged = pyqtSignal()
    projectionChanged = pyqtSignal()
    statusChanged = pyqtSignal()
    walkingTimeChanged = pyqtSignal()

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
            self._mCommonLandValue = theModel.commonLandValue
            self._mCommonLandAreaUnits = theModel.commonLandAreaUnits
            self._mHerdSize = theModel.herdSize
            self._mAnimals = theModel.animals
            self._mCrops = theModel.crops
            self._mDiets = theModel.diets
            self._mDietLabels = theModel.dietLabels
            self._mPriority = theModel.priority
            self._mDescription = theModel.description
            self._mAreaUnits = theModel.areaUnits
            self._mStatus = theModel.status
            self._mIcon = theModel.icon
        else:
            self.setGuid(None)
            self._mName = "Default Site"
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

        # Initialize value map for fallow allocation
        self._mValueMap = {}
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

    def getAnimalValue(self, animal, prop_name: str) -> float:
        """Helper method to safely get float values from animal properties."""
        prop = getattr(animal, prop_name, None)
        if prop is None:
            return 0.0
        if isinstance(prop, property):
            return float(prop.__get__(animal, type(animal)))
        return float(prop)

    def getAnimalParamValue(self, param, prop_name: str) -> float:
        """Helper method to safely get float values from animal parameter properties."""
        prop = getattr(param, prop_name, None)
        if prop is None:
            return 0.0
        if isinstance(prop, property):
            return float(prop.__get__(param, type(param)))
        return float(prop)

    def setDietLabels(self, theDietLabels: LaDietLabels,
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
        try:
            # Ensure all percentages are within valid range (0-100%)
            theDietLabels.dairyPortionPct = min(100.0, max(0.0, theOverallDairyPercent * 100))
            theDietLabels.tameMeatPortionPct = min(100.0, max(0.0, theDomesticMeatPercent * 100))
            theDietLabels.cropsPortionPct = min(100.0, max(0.0, theOverallCropPercent * 100))
            theDietLabels.wildAnimalPortionPct = min(100.0, max(0.0, theWildMeatPercent * 100))
            theDietLabels.wildPlantsPortionPct = min(100.0, max(0.0, theOverallWildPlantPercent * 100))
            
            # Calculate animal and plant portions as sums of their components
            # This ensures consistency in the percentages
            animalPortion = theDietLabels.tameMeatPortionPct + theDietLabels.wildAnimalPortionPct
            plantPortion = theDietLabels.cropsPortionPct + theDietLabels.wildPlantsPortionPct
            
            theDietLabels.animalPortionPct = animalPortion
            theDietLabels.plantsPortionPct = plantPortion
            
            # Set calorie values - ensure they're non-negative
            theDietLabels.megaCaloriesSettlementAnnual = max(0.0, theMCalsSettlementAnnual)
            theDietLabels.kiloCaloriesIndividualAnnual = max(0.0, theMCalsIndividualAnnual)
            theDietLabels.dairySurplusMCalories = max(0.0, theOverallDairySurplusMCals)
            
            # Set MCal values - ensure they're non-negative
            theDietLabels.dairyMCalories = max(0.0, theOverallDairyMCals)
            theDietLabels.animalMCalories = max(0.0, theOverallMeatMCals - theOverallWildMeatMCals)
            theDietLabels.cropMCalories = max(0.0, theOverallCropsMCals)
            theDietLabels.wildAnimalMCalories = max(0.0, theOverallWildMeatMCals)
            theDietLabels.wildPlantsMCalories = max(0.0, theOverallWildPlantsMCals)
            
            # Set report maps
            theDietLabels.cropCalcsReportMap = theCropCalcsReportMap
            theDietLabels.animalCalcsReportMap = theAnimalCalcsReportMap
            
            from la.lib.lautils import LaUtils
            LaUtils.debug.log("Diet labels updated successfully", "Diet")
            LaUtils.debug.log(f"Animal: {animalPortion:.1f}%, Plant: {plantPortion:.1f}%", "Diet")
            LaUtils.debug.log(f"Wild Animal: {theDietLabels.wildAnimalPortionPct:.1f}%, Tame Animal: {theDietLabels.tameMeatPortionPct:.1f}%", "Diet")
            LaUtils.debug.log(f"Wild Plant: {theDietLabels.wildPlantsPortionPct:.1f}%, Tame Plant: {theDietLabels.cropsPortionPct:.1f}%", "Diet")

        except Exception as e:
            from la.lib.lautils import LaUtils
            LaUtils.debug.log(f"Error setting diet labels: {str(e)}", "Diet")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Diet")

    def doCalcsPlantsFirstIncludeDairy(self) -> LaDietLabels:
        from la.lib.lautils import LaUtils
        myMCalsIndividualAnnual: float = self.caloriesPerPersonDaily * 365.0;
        myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * self.population;
        myDietLabels = LaDietLabels()
        myDairyMCalorieCounter = 0.0
        myTameMeatMCalorieCounter = 0.0
        myWildMeatMCalorieCounter = 0.0
        myCropCalcsReportMap = {}
        myAnimalCalcsReportMap = {}
        
        # Log base parameters
        LaUtils.debug.log(f"Calories per person daily: {self.caloriesPerPersonDaily}", "Diet")
        LaUtils.debug.log(f"Annual settlement calories (MCal): {self.caloriesPerPersonDaily * 365.0 * self.population / 1000.0}", "Diet")
        
        # Initialize calculation variables
        c1: float = 1.0 - self.meatPercent
        c8: float = self.dairyUtilisation
        c10: float = self.population
        c11: float = self.caloriesPerPersonDaily
        c14: float = c10 * c11 * 365.0
        c15: float = self.dietPercent
        c12: float = self.percentOfDietThatIsFromCrops
        e15: float = c14 * c15
        
        # Process each animal
        mySelectedAnimalsMap: dict[str, str] = self._mAnimals.copy() if hasattr(self, '_mAnimals') else {}
        
        # Loop through each animal to calculate its contribution
        for animalGuid, animalParamGuid in mySelectedAnimalsMap.items():
            from la.lib.lautils import LaUtils
            myAnimal: LaAnimal = LaUtils.getAnimal(animalGuid)
            myAnimalParameter: LaAnimalParameter = LaUtils.getAnimalParameter(animalParamGuid)
            
            if not myAnimal or not myAnimalParameter:
                LaUtils.debug.log(f"Could not find animal or parameter for GUID {animalGuid}", "Diet")
                continue
                
            # Calculate dairy contribution for this animal
            c2: float = myAnimal.milkGramsPerDay * 0.001
            c3: float = myAnimal.milkFoodValue
            c4: float = myAnimal.lactationTime
            c5: float = myAnimal.weaningAge
            c6: float = myAnimal.killWeight
            c7: float = myAnimal.usableMeat * 0.01
            
            e2: float = c2 * c3 * (c4 - c5)
            e3: float = e2 * c8
            c9: float = myAnimal.meatFoodValue
            e10: float = e3 + (c9 * c7 * c6)
            
            e7 = (e15 * (1.0 - c1)) / e10
            c21 = e7 * e3
            c23 = e7 * c6 * c7 * c9
            c22 = e15 - c21 - c23
            
            # Add to counters
            myDairyMCalorieCounter += c21
            myWildMeatMCalorieCounter += c22
            myTameMeatMCalorieCounter += c23
            
        
        c24: float = (1.0 - c12) * (c14 - e15)
        c25: float = c12 * (c14 - e15)
        c30: float = c24 / c14
        c31: float = c25 / c14

        c28: float = myWildMeatMCalorieCounter / c14
        c29: float = myTameMeatMCalorieCounter / c14
        c27: float = myDairyMCalorieCounter / c14
        
        myDietLabels.dairyMCalories = myDairyMCalorieCounter * .001 * .001
        myDietLabels.cropMCalories = c25 * .001 * .001
        myDietLabels.wildAnimalMCalories = myWildMeatMCalorieCounter * .001 * .001
        myDietLabels.wildPlantsMCalories = c24 * .001 * .001
        myDietLabels.dairyPortionPct = c27 *100.
        myDietLabels.tameMeatPortionPct = c29 * 100.
        myDietLabels.cropsPortionPct = c31 * 100.
        myDietLabels.wildAnimalPortionPct = c28 * 100.
        myDietLabels.wildPlantsPortionPct = c30 * 100.
        myDietLabels.animalPortionPct = self._mDietPercent * 100. - c27 * 100.
        myDietLabels.plantsPortionPct = (1. - self._mDietPercent) * 100.
        myDietLabels.kiloCaloriesIndividualAnnual = myMCalsIndividualAnnual
        myDietLabels.megaCaloriesSettlementAnnual = myMCalsSettlementAnnual
    
        return myDietLabels

    def doCalcsAnimalsFirstIncludeDairy(self) -> LaDietLabels:
        """
        Calculates diet portions for setting the diet labels.
        This method calculates the diet values when animals are prioritized, and dairy products 
        from the animal herds are considered as part of the animals' contribution to the diet. 
        The plant-based portion is derived from these calculations. It assumes that the model 
        has been properly set before invoking this method.
        The calculations require the following pieces of information:
        1. The overall settlement calorie target.
        2. The percent of the diet that animals are responsible for.
        3. The number of calories that plants are going to supply.
        4. The percent of the animals that are domestic sources.
        5. The percent of the plants that are domestic sources (crops).
        Returns:
            LaDietLabels: An object containing the calculated diet labels.
        """
        # Log start of calculation
        from la.lib.lautils import LaUtils
        LaUtils.debug.log("Starting doCalcsAnimalsFirstIncludeDairy calculation", "Diet")
        
        myDietLabels = LaDietLabels()
        myAnimal = LaAnimal()  # Matches C++ declaration but not used in this simplified version

        try:
            # Base values - matching C++ variable names
            myMCalsIndividualAnnual: float = self._mCaloriesPerPersonDaily * 365.0 # / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual: float = myMCalsIndividualAnnual * self._mPopulation
            myDairyMCalorieCounter: float = 0.0
            myTameMeatMCalorieCounter: float = 0.0
            myWildMeatMCalorieCounter: float = 0.0
            mySelectedAnimalsMap: Dict[str, str] = self._mAnimals  # Similar to C++ QMap<QString,QString>
            
            # C++ style variable declarations (c1, c8, etc.)
            c1 = 1.0 - self._mMeatPercent    # Wild meat percent (1 - meat percent)
            c8 = self._mDairyUtilisation      # Dairy utilization as decimal
            c10 = self._mPopulation                    # Population count
            c11 = self._mCaloriesPerPersonDaily        # Calories per person daily
            c14 = c10 * c11 * 365.0          # Settlement MCal per year
            c15 = self._mDietPercent        # Diet percent as decimal
            c12 = self._mPercentOfDietThatIsFromCrops   # Percent of diet from crops
            e15 = c14 * c15
            
            # Log input values
            LaUtils.debug.log(f"Calories per person daily: {c11}", "Diet")
            LaUtils.debug.log(f"Population count: {c10}", "Diet")
            LaUtils.debug.log(f"Meat percent: {self._mMeatPercent}%, Diet percent: {self._mDietPercent}%", "Diet")
            LaUtils.debug.log(f"Annual individual calories (MCal): {myMCalsIndividualAnnual}", "Diet")
            LaUtils.debug.log(f"Annual settlement calories (MCal): {myMCalsSettlementAnnual}", "Diet")

            # Calculate MCals for different food sources (simplified for example)
            myDairyMCalorieCounter = myMCalsSettlementAnnual * c15 * 0.05      # 5% of animal diet as dairy
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * (self._mMeatPercent / 100.0) # Tame meat portion
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * c15 * c1      # Wild meat portion
            myCropMCalorieCounter = myMCalsSettlementAnnual * (1.0 - c15) * (self._mPercentOfDietThatIsFromCrops / 100.0)  # Crops portion
            myWildPlantMCalorieCounter = myMCalsSettlementAnnual * (1.0 - c15) * (1.0 - self._mPercentOfDietThatIsFromCrops / 100.0)  # Wild plants

            # Calculate percentages of total diet
            myDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual
            myTameMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual
            myWildMeatPercent = myWildMeatMCalorieCounter / myMCalsSettlementAnnual
            myCropPercent = myCropMCalorieCounter / myMCalsSettlementAnnual
            myWildPlantPercent = myWildPlantMCalorieCounter / myMCalsSettlementAnnual
            
            animalPercent = (myTameMeatMCalorieCounter + myWildMeatMCalorieCounter) / myMCalsSettlementAnnual
            plantPercent = (myCropMCalorieCounter + myWildPlantMCalorieCounter) / myMCalsSettlementAnnual

            # Create report maps (empty in simplified version)
            myCropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}

            # Set all values in the diet labels object
            self.setDietLabels(
                myDietLabels,
                myDairyMCalorieCounter,      # Overall dairy MCals
                myCropMCalorieCounter,        # Overall crop MCals
                myTameMeatMCalorieCounter,    # Overall meat MCals
                myWildMeatMCalorieCounter,    # Overall wild meat MCals
                myWildPlantMCalorieCounter,   # Overall wild plants MCals
                myDairyPercent,               # Overall dairy percent
                myTameMeatPercent,            # Domestic meat percent
                myCropPercent,                # Overall crop percent
                myWildMeatPercent,            # Wild meat percent
                myWildPlantPercent,           # Overall wild plant percent
                animalPercent,                # Overall animal percent
                plantPercent,                 # Overall plant percent
                myMCalsIndividualAnnual * 1000.0,  # Convert to kCal
                myMCalsSettlementAnnual,      # Settlement annual MCal
                0.0,                          # No dairy surplus in simplified calculation
                myCropCalcsReportMap,         # Empty crop calcs report map
                myAnimalCalcsReportMap        # Empty animal calcs report map
            )

            # Log results
            LaUtils.debug.log(f"Final percentages - Animal: {animalPercent*100:.1f}%, Plant: {plantPercent*100:.1f}%", "Diet")
            LaUtils.debug.log("doCalcsAnimalsFirstIncludeDairy calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels

    def doCalcsPlantsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when plants are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()
        LaAnimal = None  # Matches C++ declaration but not used in this simplified version

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsPlantsFirstDairySeparate calculation", "Diet")

        try:
            # Base values - matching C++ variable names
            myMCalsIndividualAnnual = self._mCaloriesPerPersonDaily * 365.0 / 1000.0  # Convert to annual MCals
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * self._mPopulation
            myDairyMCalorieCounter = 0.0
            myTameMeatMCalorieCounter = 0.0
            myWildMeatMCalorieCounter = 0.0
            mySelectedAnimalsMap = self._mAnimals  # Similar to C++ QMap<QString,QString>
            
            # C++ style variable declarations
            myWildMeatPortion = 1.0 - (self._mMeatPercent / 100.0)  # Wild meat percent (as in C++)
            myDairyUtilization = self._mDairyUtilisation / 100.0    # Decimal form of dairy utilization
            myDairyLimitPercent = self._mLimitDairyPercent / 100.0  # Decimal form of dairy limit
            myLimitDairyBool = self._mLimitDairy                    # Boolean for dairy limit
            myPlantPercent = 1.0 - (self._mDietPercent / 100.0)     # Plant percent (matches C++ myPlantPercent)
            myDomesticCropPortion = self._mPercentOfDietThatIsFromCrops / 100.0  # Decimal form of crop portion

            LaUtils.debug.log(f"Input parameters - calories_daily: {self._mCaloriesPerPersonDaily}, population: {self._mPopulation}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {self._mMeatPercent}%, diet_percent: {self._mDietPercent}%", "Diet")
            LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters with simplified approach to match C++ variable names
            myDairyMCalorieCounter = myMCalsSettlementAnnual * 0.05  # Separate counter for dairy (5% of total)
            myTameMeatMCalorieCounter = myMCalsSettlementAnnual * (self._mDietPercent / 100.0) * (self._mMeatPercent / 100.0)  # tame meat
            myWildMeatMCalorieCounter = myMCalsSettlementAnnual * (self._mDietPercent / 100.0) * myWildMeatPortion  # wild meat
            
            # Following the same pattern from C++ for crop and plant calculations
            myOverallPlantPercent = myPlantPercent
            myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion
            myOverallWildPlantPercent = myOverallPlantPercent * (1.0 - myDomesticCropPortion)
            
            # Calculate MCals for different components
            myOverallDomesticMeatMCals = myTameMeatMCalorieCounter
            myOverallDairyMCals = myDairyMCalorieCounter
            myOverallWildMeatMCals = myWildMeatMCalorieCounter
            myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual
            myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual
            
            # Calculate overall percentages - key values for UI display
            myOverallMeatPercent = (myTameMeatMCalorieCounter + myWildMeatMCalorieCounter) / myMCalsSettlementAnnual
            myOverallDairyPercent = myDairyMCalorieCounter / myMCalsSettlementAnnual
            
            # Check for dairy surplus (from C++)
            myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals
            myOVerallDairySurplusMCals = myFirstDairySurplusBool if myFirstDairySurplusBool > 0 else 0.0
            
            # Calculate percentages of the total settlement MCals
            myDomesticMeatPercent = myOverallDomesticMeatMCals / myMCalsSettlementAnnual
            myWildMeatPercent = myOverallWildMeatMCals / myMCalsSettlementAnnual
            myCropPercent = myOverallCropsMCals / myMCalsSettlementAnnual
            myWildPlantPercent = myOverallWildPlantsMCals / myMCalsSettlementAnnual

            # Create report maps (empty in simplified version)
            myCropCalcsReportMap = {}
            myAnimalCalcsReportMap = {}

            # Set all values in the diet labels object
            self.setDietLabels(
                myDietLabels,
                myDairyMCalorieCounter,     # Overall dairy MCals
                myOverallCropsMCals,        # Overall crop MCals
                myTameMeatMCalorieCounter,  # Tame meat MCals
                myWildMeatMCalorieCounter,  # Wild meat MCals
                myOverallWildPlantsMCals,   # Wild plants MCals
                myOverallDairyPercent,      # Overall dairy percent
                myDomesticMeatPercent,      # Domestic meat percent
                myCropPercent,              # Overall crop percent
                myWildMeatPercent,          # Wild meat percent
                myWildPlantPercent,         # Overall wild plant percent
                myOverallMeatPercent,       # Overall meat percent
                myOverallPlantPercent,      # Overall plant percent
                myMCalsIndividualAnnual * 1000.0,  # Convert back to kCal
                myMCalsSettlementAnnual,    # MCals settlement annual
                myOVerallDairySurplusMCals, # Dairy surplus MCals
                myCropCalcsReportMap,       # Crop calcs report map
                myAnimalCalcsReportMap      # Animal calcs report map
            )

            # Log results matching the pattern in C++ implementation
            LaUtils.debug.log(f"Results - Meat: {myOverallMeatPercent*100:.2f}%, Plant: {myOverallPlantPercent*100:.2f}%, Dairy: {myOverallDairyPercent*100:.2f}%", "Diet")
            LaUtils.debug.log("doCalcsPlantsFirstDairySeparate calculation completed successfully", "Diet")

        except Exception as e:
            LaUtils.debug.log(f"Error in diet calculation: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels

    def doCalcsAnimalsFirstDairySeparate(self) -> LaDietLabels:
        """Calculate diet values when animals are prioritized and dairy is separate from meat."""
        from la.lib.lautils import LaUtils
        myDietLabels = LaDietLabels()

        # Log calculation start
        LaUtils.debug.log("Starting doCalcsAnimalsFirstDairySeparate calculation", "Diet")

        try:
            # Get base values from internal attributes
            calories_daily = float(self._mCaloriesPerPersonDaily)
            population_count = float(self._mPopulation)
            meat_percent = float(self._mMeatPercent) / 100.0  # Convert to decimal
            diet_percent = float(self._mDietPercent) / 100.0  # Convert to decimal

            LaUtils.debug.log(f"Input parameters - calories_daily: {calories_daily}, population: {population_count}", "Diet")
            LaUtils.debug.log(f"Diet parameters - meat_percent: {meat_percent*100}%, diet_percent: {diet_percent*100}%", "Diet")

            # Calculate basic values
            myMCalsIndividualAnnual = calories_daily * 365.0 / 1000.0  # Convert to MCal
            myMCalsSettlementAnnual = myMCalsIndividualAnnual * population_count

            LaUtils.debug.log(f"Calculated annual MCals - individual: {myMCalsIndividualAnnual}, settlement: {myMCalsSettlementAnnual}", "Diet")

            # Initialize counters with a simplified calculation approach
            myDairyCounter = myMCalsSettlementAnnual * 0.05  # Separate dairy calculation (5% of total)
            myTameMeatCounter = myMCalsSettlementAnnual * diet_percent * meat_percent  # Tame meat portion
            myWildMeatCounter = myMCalsSettlementAnnual * diet_percent * (1.0 - meat_percent)  # Wild meat portion
            myCropCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.8  # Crops portion (80% of plant calories)
            myWildPlantCounter = myMCalsSettlementAnnual * (1.0 - diet_percent) * 0.2  # Wild plants (20% of plant calories)

            # Calculate percentages
            totalMCalories = myMCalsSettlementAnnual

            dairyPercent = myDairyCounter / totalMCalories
            tameMeatPercent = myTameMeatCounter / totalMCalories
            wildMeatPercent = myWildMeatCounter / totalMCalories
            cropPercent = myCropCounter / totalMCalories
            wildPlantPercent = myWildPlantCounter / totalMCalories

            animalPercent = (myTameMeatCounter + myWildMeatCounter) / totalMCalories
            plantPercent = (myCropCounter + myWildPlantCounter) / totalMCalories

            # Create report maps for crops and animals
            cropCalcsReportMap = {}
            animalCalcsReportMap = {}

            # Populate crop report map with some sample data for each crop
            for cropGuid, paramGuid in self._mCrops.items():
                try:
                    crop = LaUtils.getCrop(cropGuid)
                    cropParameter = LaUtils.getCropParameter(paramGuid)

                    if crop and cropParameter:
                        # Calculate this crop's share of the total crop calories using crop parameter percentages
                        cropContributionPercent = 1.0
                        try:
                            # Use the crop parameter's percent tame crop value if available
                            cropContributionPercent = float(str(cropParameter.percentTameCrop)) * 0.01
                        except:
                            # Fall back to equal distribution if parameter not available
                            cropContributionPercent = 1.0 / len(self._mCrops) if self._mCrops else 0.0

                        # Calculate crop calories following the C++ approach
                        cropPercent = cropContributionPercent * cropPercent
                        myCropFoodValue = float(str(crop.cropCalories)) * 0.001  # Convert to MCal/kg
                        myMCalsFromTheCrop = cropPercent * myMCalsSettlementAnnual

                        # Calculate kg needed for people (initial calculation before adjustments)
                        myKgForPeople1 = myMCalsFromTheCrop / myCropFoodValue

                        # Get spoilage and reseeding percentages from crop parameters
                        mySpoilagePercent = 0.1  # Default 10% if not available
                        myReseedPercent = 0.1    # Default 10% if not available

                        try:
                            mySpoilagePercent = float(str(cropParameter.spoilage)) * 0.01
                            myReseedPercent = float(str(cropParameter.reseed)) * 0.01
                        except Exception as e:
                            LaUtils.debug.log(f"Error getting spoilage/reseed parameters for {crop.name}: {e}", "Warning")

                        # Calculate additional kg needed for spoilage and reseeding
                        myKgForPeopleSpoilage = myKgForPeople1 * mySpoilagePercent
                        myKgForPeopleReseed = myKgForPeople1 * myReseedPercent

                        # Total kg needed for people after accounting for spoilage and reseeding
                        myKgForPeople = myKgForPeople1 + myKgForPeopleSpoilage + myKgForPeopleReseed

                        # Calculate area needed based on yield
                        myCropYield = float(str(crop.cropYield))

                        # Determine area units and convert values if needed
                        areaUnitName = "hectares"
                        if hasattr(self, '_mAreaUnits') and self._mAreaUnits == AreaUnits.Dunum:
                            areaUnitName = "dunums"
                            # If crop yield is in hectares but we want dunums, adjust the yield
                            if hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Hectare":
                                myCropYield = myCropYield / 10.0  # Convert hectares to dunums
                        elif hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Dunum":
                            # If crop yield is in dunums but we want hectares, adjust the yield
                            myCropYield = myCropYield * 10.0  # Convert dunums to hectares

                        # Calculate area needed in the appropriate units
                        myCropAreaTarget = myKgForPeople / myCropYield

                        # Calculate fallow land area if applicable
                        myFallowArea = 0.0
                        myFallowMCals = 0.0
                        myTotalAreaNeeded = myCropAreaTarget

                        if hasattr(cropParameter, 'fallowRatio') and cropParameter.fallowRatio > 0:
                            myRatio = float(str(cropParameter.fallowRatio))
                            myFallowValue = 0.0
                            if hasattr(cropParameter, 'fallowValue'):
                                myFallowValue = float(str(cropParameter.fallowValue))

                            myFallowArea = myCropAreaTarget * (myRatio / (1.0 + myRatio))
                            myFallowMCals = myFallowArea * myFallowValue
                            myTotalAreaNeeded = myCropAreaTarget + myFallowArea

                        # Create detailed report for this crop including all calculation steps
                        cropReport = f"Calculation Report for {crop.name}\n"
                        cropReport += f"===========================\n"
                        cropReport += f"Crop calories: {myMCalsFromTheCrop:.2f} MCal\n"
                        cropReport += f"Population: {population_count} people\n"
                        cropReport += f"Individual needs: {myMCalsIndividualAnnual:.2f} MCal/year\n"
                        cropReport += f"Settlement needs: {myMCalsSettlementAnnual:.2f} MCal/year\n"
                        cropReport += f"Plant portion: {plantPercent*100:.2f}% of diet\n"
                        cropReport += f"Crop portion: {cropPercent*100:.2f}% of diet\n"
                        cropReport += f"Crop food value: {myCropFoodValue:.2f} MCal/kg\n"

                        cropReport += f"\nProduction Calculations:\n"
                        cropReport += f"Base production needed: {myKgForPeople1:.2f} kg\n"
                        cropReport += f"Spoilage adjustment ({mySpoilagePercent*100:.1f}%): {myKgForPeopleSpoilage:.2f} kg\n"
                        cropReport += f"Reseed adjustment ({myReseedPercent*100:.1f}%): {myKgForPeopleReseed:.2f} kg\n"
                        cropReport += f"Total production needed: {myKgForPeople:.2f} kg\n"

                        cropReport += f"\nArea Calculations:\n"
                        cropReport += f"Crop yield: {myCropYield:.2f} kg/{areaUnitName}\n"
                        cropReport += f"Required crop area: {myCropAreaTarget:.2f} {areaUnitName}\n"

                        if myFallowArea > 0:
                            cropReport += f"Fallow land area: {myFallowArea:.2f} {areaUnitName}\n"
                            cropReport += f"Fallow land value: {myFallowValue:.2f} MCal/{areaUnitName}\n"
                            cropReport += f"Fallow land calories: {myFallowMCals:.2f} MCal\n"
                            cropReport += f"Total area needed (crop + fallow): {myTotalAreaNeeded:.2f} {areaUnitName}\n"

                        # Store the report in the map with the required production as the second value
                        cropCalcsReportMap[cropGuid] = (cropReport, myKgForPeople)
                        LaUtils.debug.log(f"Added detailed crop calculation for {crop.name}", "Diet")
                    else:
                        LaUtils.debug.log(f"Missing crop or crop parameter for GUID {cropGuid}", "Warning")

                except Exception as e:
                    LaUtils.debug.log(f"Error creating crop report for GUID {cropGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Detailed error: {traceback.format_exc()}", "Error")

            # Populate animal report map with some sample data for each animal
            for animalGuid, paramGuid in self._mAnimals.items():
                try:
                    animal = LaUtils.getAnimal(animalGuid)
                    animalParameter = LaUtils.getAnimalParameter(paramGuid)

                    # Initialize variables at the start
                    myAnimalReport = ""
                    myAnimalHerdMCalsRequired = 0.0

                    if animal:
                        LaUtils.debug.log(f"Processing animal: {animal.name} (GUID: {animalGuid})", "Diet")

                        # Get animal values safely
                        myMilkKgPerDay = float(str(animal.milkGramsPerDay)) * 0.001  # Convert g to kg
                        myMilkFoodValue = float(str(animal.milkFoodValue)) * 0.001   # Convert to MCal
                        myLactationTime = float(str(animal.lactationTime))
                        myWeaningAge = float(str(animal.weaningAge))
                        myGestatingTime = float(str(animal.gestationTime))
                        myEstrousCycle = float(str(animal.estrousCycle))
                        myBabiesPerBirth = float(str(animal.youngPerBirth))
                        myDeathRate = float(str(animal.deathRate)) * 0.01  # Convert from percent
                        myBreedingRatio = float(str(animal.femalesPerMale))

                        # Check for zero breeding ratio to avoid division by zero
                        if myBreedingRatio <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has a breeding ratio of {myBreedingRatio}, using default of 1.0", "Warning")
                            myBreedingRatio = 1.0  # Default to 1 if zero or negative

                        myKillWeight = float(str(animal.killWeight))
                        myUsablePortionOfAnimal = float(str(animal.usableMeat)) * 0.01  # Convert from percent
                        myAdultWeight = float(str(animal.adultWeight))
                        myConceptionEfficiency = float(str(animal.conceptionEfficiency)) * 0.01  # Convert from percent
                        myMeatValueMCal = float(str(animal.meatFoodValue)) * 0.001  # Convert to MCal
                        mySexualMaturity = float(str(animal.sexualMaturity))
                        myBreedingYears = float(str(animal.breedingExpectancy))

                        # Get parameter values
                        myAnimalContributionToMeatPortion = 0
                        if animalParameter:
                            try:
                                myAnimalContributionToMeatPortion = float(str(animalParameter.percentTameMeat)) * 0.01
                            except:
                                myAnimalContributionToMeatPortion = 1.0 / len(self._mAnimals) if len(self._mAnimals) > 0 else 0

                        # Calculate animal targets using the C++ approach
                        myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * diet_percent * meat_percent
                        myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge)
                        myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal

                        # Get dairy utilization as a decimal (0-1)
                        myDairyUtilization = float(self._mDairyUtilisation) / 100.0
                        myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization

                        # Calculate birthing events per year, handling edge case for too many days
                        myBirthingEventsPerYear1 = 365.0 / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime)
                        myBirthingEventsPerYear = 1.0 if myBirthingEventsPerYear1 < 1.0 else myBirthingEventsPerYear1

                        # Calculate culled mothers value
                        myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal *
                                                (1.0 / ((mySexualMaturity / 12.0) + myBreedingYears)))
                        myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear)

                        # Calculate culled adult males value
                        myCulledAdultMalesValue = myCulledMothersValue / myBreedingRatio

                        # Calculate final offspring value
                        myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue

                        # Calculate number of offspring needed per year
                        myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue

                        # Calculate MCals from meat and utilized from dairy
                        myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue
                        myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear

                        # Add to the diet counters
                        myTameMeatCounter += myMCalsFromTheMeat
                        myDairyCounter += myMCalsUtilizedFromDairy

                        # Calculate meat and dairy percentages
                        myMeatPercent = myMCalsFromTheMeat / myMCalsSettlementAnnual
                        myDairyPercent = myMCalsUtilizedFromDairy / myMCalsSettlementAnnual

                        # Calculate herd size based on birthing cycles
                        myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1.0 - myDeathRate) * myConceptionEfficiency

                        # Check for zero offspring per mother per year to avoid division by zero
                        if myOffspringPerMotherPerYear <= 0:
                            LaUtils.debug.log(f"Warning: Animal {animal.name} has zero or negative offspring per mother per year calculation. Using default value of 1.0", "Warning")
                            myOffspringPerMotherPerYear = 1.0  # Default to 1 if zero or negative

                        myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear
                        myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5
                        myFemalesStepOne = myMalesStepOne
                        myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity / 12.0)) / myBreedingYears
                        # Match original C++ implementation exactly
                        myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio
                        myAdditionalMothers = ((myReplacementMothersPerYear / myOffspringPerMotherPerYear) * 2.0) + (myBreedingMalesRequired * 2.0)

                        myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5
                        myFemalesStepTwo = myMalesStepTwo
                        myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear
                        myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo
                        myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo
                        myTotalOffspring = myTotalMaleOffspring * 2.0  # Total offspring

                        # Calculate feed requirements
                        try:
                            # Get animal feed values from animal parameters
                            myFeedForMaintenance = float(str(animal.maintenance))  # kg feed per day
                            myFeedForGestating = float(str(animal.gestating))      # kg feed per day
                            myFeedForLactating = float(str(animal.lactating))      # kg feed per day
                            myFeedForOffspringPerKg = float(str(animal.juvenile))  # kg feed per kg weight of offspring

                            # Get values needed for grazing land calculations from animal parameter
                            myUseCommonGrazingLand = True
                            myUseSpecificGrazingLand = False

                            # Get grazing land productivity from parameters - critical for correct area calculation
                            # In the original C++ code, this is ValueCommonGrazingLand or ValueSpecificGrazingLand
                            # representing calories per hectare/dunum
                            myGrazingLandCalories: float = 0.0

                            if animalParameter:
                                if hasattr(animalParameter, 'useCommonGrazingLand'):
                                    myUseCommonGrazingLand = bool(animalParameter.useCommonGrazingLand)
                                if hasattr(animalParameter, 'useSpecificGrazingLand'):
                                    myUseSpecificGrazingLand = bool(animalParameter.useSpecificGrazingLand)

                                # Get the correct grazing land caloric value
                                if myUseCommonGrazingLand and hasattr(animalParameter, 'ValueCommonGrazingLand'):
                                    myGrazingLandCalories = float(str(animalParameter.valueCommonGrazingLand))
                                elif myUseSpecificGrazingLand and hasattr(animalParameter, 'ValueSpecificGrazingLand'):
                                    myGrazingLandCalories = float(str(animalParameter.valueSpecificGrazingLand))

                            # If we couldn't get a value from parameters, use the model's common grazing value
                            if myGrazingLandCalories <= 0.0 and hasattr(self, '_mCommonLandValue'):
                                myGrazingLandCalories = float(str(self._mCommonLandValue))

                            # Default fallback if no values available
                            if myGrazingLandCalories <= 0.0:
                                myGrazingLandCalories = 7500.0  # Default calories per hectare (reasonable value)
                                LaUtils.debug.log(f"Using default grazing land value of {myGrazingLandCalories} calories/hectare", "Warning")

                        except Exception as e:
                            # Default values if there's an error getting feed requirements
                            LaUtils.debug.log(f"Error getting feed requirements for {animal.name}: {e}", "Error")
                            myFeedForMaintenance = 1.0  # Default values
                            myFeedForGestating = 1.5
                            myFeedForLactating = 2.0
                            myFeedForOffspringPerKg = 0.1
                            myUseCommonGrazingLand = True
                            myUseSpecificGrazingLand = False
                            myGrazingLandCalories = 7500.0  # Default calories per hectare

                        # Calculate MCals needed for each phase
                        myGestatingMCals = myTotalMothers * myGestatingTime * myFeedForGestating
                        myLactatingMCals = myTotalMothers * myLactationTime * myFeedForLactating
                        myDaysForMaintenance = max(0, 365 - (myGestatingTime + myLactationTime))

                        myDryMothers = max(0, myTotalMothers - myTotalOffspring)
                        myDryMothersMCals = myDryMothers * 365.0 * myFeedForMaintenance
                        myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance
                        myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals
                        myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.0
                        myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365.0 - myWeaningAge)

                        # Set the total herd requirements in kg feed per year
                        myAnimalHerdMCalsRequired = (myGestatingMCals + myLactatingMCals +
                                                   myMaintenanceMCals + myAdultMalesMCals +
                                                   myOffspringMCals)

                        # Calculate total feed required in kg - this is what was missing
                        myTotalFeedRequiredKg = myAnimalHerdMCalsRequired

                        # Calculate grazing land area needed
                        # Convert feed requirements to calories using an approximation
                        # Average feed is about 2000 calories per kg (rough estimate)
                        feedToCaloriesFactor = 2000.0  # calories per kg of feed
                        totalCaloriesRequired = myAnimalHerdMCalsRequired * feedToCaloriesFactor

                        # Calculate area needed - divide total calories needed by calories per hectare provided by land
                        myGrazingAreaNeeded = totalCaloriesRequired / myGrazingLandCalories if myGrazingLandCalories > 0 else 0

                        # Convert to appropriate area units for display
                        areaUnitName = "hectares"
                        if hasattr(self, '_mAreaUnits') and self._mAreaUnits == AreaUnits.Dunum:
                            myGrazingAreaNeeded = myGrazingAreaNeeded * 10.0  # Convert hectares to dunum
                            areaUnitName = "dunums"

                        # Format the herd information for the report
                        totalHerd = myTotalMothers + myBreedingMalesRequired + myTotalOffspring

                        # Create the animal report
                        myAnimalReport = f"Calculation Report for {animal.name}\n"
                        myAnimalReport += f"===========================\n"
                        myAnimalReport += f"Animal meat calories: {myMCalsFromTheMeat:.2f} MCal\n"
                        myAnimalReport += f"Animal dairy calories: {myMCalsUtilizedFromDairy:.2f} MCal\n"
                        myAnimalReport += f"Population: {population_count} people\n"
                        myAnimalReport += f"Individual needs: {myMCalsIndividualAnnual:.2f} MCal/year\n"
                        myAnimalReport += f"Settlement needs: {myMCalsSettlementAnnual:.2f} MCal/year\n\n"

                        myAnimalReport += f"Herd Composition:\n"
                        myAnimalReport += f"- Adult females (breeding): {myTotalMothers:.1f}\n"
                        myAnimalReport += f"- Adult males (breeding): {myBreedingMalesRequired:.1f}\n"
                        myAnimalReport += f"- Offspring: {myTotalOffspring:.1f}\n"
                        myAnimalReport += f"- Total herd size: {totalHerd:.1f}\n\n"

                        myAnimalReport += f"Feed Requirements:\n"
                        myAnimalReport += f"- Gestating females: {myGestatingMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Lactating females: {myLactatingMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Adult maintenance: {myMaintenanceMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Adult males: {myAdultMalesMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Offspring growth: {myOffspringMCals:.1f} kg/year\n"
                        myAnimalReport += f"- Total feed required: {myTotalFeedRequiredKg:.1f} kg/year\n\n"

                        myAnimalReport += f"Land Requirements:\n"
                        myAnimalReport += f"- Grazing land productivity: {myGrazingLandCalories:.1f} calories/{areaUnitName}\n"
                        myAnimalReport += f"- Grazing area needed: {myGrazingAreaNeeded:.2f} {areaUnitName}\n"

                        if myUseCommonGrazingLand:
                            myAnimalReport += f"- Using common grazing land: Yes\n"
                        if myUseSpecificGrazingLand:
                            myAnimalReport += f"- Using specific grazing land: Yes\n"

                    # Now we can safely store both the report and requirements
                    animalCalcsReportMap[animalGuid] = (myAnimalReport, myAnimalHerdMCalsRequired)
                    LaUtils.debug.log(f"Added detailed animal calculation for {animal.name if animal else animalGuid}", "Diet")

                except Exception as e:
                    LaUtils.debug.log(f"Error in animal calculation for GUID {animalGuid}: {str(e)}", "Error")
                    import traceback
                    LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

            # Set all values in the diet labels object
            self.setDietLabels(
                myDietLabels,
                myDairyCounter,           # Overall dairy MCals
                myCropCounter,            # Overall crop MCals
                myTameMeatCounter,        # Overall meat MCals
                myWildMeatCounter,        # Overall wild meat MCals
                myWildPlantCounter,       # Overall wild plants MCals
                dairyPercent,             # Overall dairy percent
                tameMeatPercent,          # Domestic meat percent
                cropPercent,              # Overall crop percent
                wildMeatPercent,          # Wild meat percent
                wildPlantPercent,         # Overall wild plant percent
                animalPercent,            # Overall meat percent
                plantPercent,             # Overall plant percent
                myMCalsIndividualAnnual,  # MCals individual annual
                myMCalsSettlementAnnual,  # MCals settlement annual
                0.0,                      # Overall dairy surplus MCals
                cropCalcsReportMap,       # Crop calcs report map
                animalCalcsReportMap      # Animal calcs report map
            )

            LaUtils.debug.log(f"Created report maps with {len(cropCalcsReportMap)} crops and {len(animalCalcsReportMap)} animals", "Diet")
            LaUtils.debug.log("doCalcsAnimalsFirstDairySeparate calculation completed successfully", "Diet")

            # Calculate fallow MCals from crops for animal grazing
            myMCalsFromFallowCounter = 0.0
            for cropGuid, reportPair in cropCalcsReportMap.items():
                cropParameter = LaUtils.getCropParameter(self._mCrops.get(cropGuid, ""))
                if cropParameter and hasattr(cropParameter, 'fallowRatio') and hasattr(cropParameter, 'fallowValue'):
                    try:
                        fallowRatio = float(str(cropParameter.fallowRatio))
                        fallowValue = float(str(cropParameter.fallowValue))

                        # Get the area from the report pair's second value
                        productionTarget = reportPair[1]

                        # Get the crop to calculate yield
                        crop = LaUtils.getCrop(cropGuid)
                        if crop:
                            myCropYield = float(str(crop.cropYield))
                            if hasattr(crop, 'areaUnits') and str(crop.areaUnits) == "Dunum":
                                myCropYield = myCropYield * 10.0  # Convert from Dunum to hectare

                            # Calculate area and fallow MCals
                            cropArea = productionTarget / myCropYield
                            fallowArea = cropArea * (fallowRatio / (1.0 + fallowRatio))
                            fallowMCals = fallowArea * fallowValue

                            myMCalsFromFallowCounter += fallowMCals
                            LaUtils.debug.log(f"Fallow from crop {crop.name}: {fallowArea:.2f} ha producing {fallowMCals:.2f} MCal", "Diet")
                    except Exception as e:
                        LaUtils.debug.log(f"Error calculating fallow for crop {cropGuid}: {str(e)}", "Error")

            # Now allocate the fallow grazing calories to reduce animal requirements
            if myMCalsFromFallowCounter > 0:
                LaUtils.debug.log(f"Allocating {myMCalsFromFallowCounter:.2f} MCal from fallow land to animals", "Diet")

                # Create a map of animal requirements for allocation
                animalMCalRequirementMap = {}
                for animalGuid in self._mValueMap:
                    if animalGuid in self._mAnimals:  # Only include animals in the current diet
                        animalMCalRequirementMap[animalGuid] = self._mValueMap[animalGuid]

                # Allocate the fallow land to animals
                self.allocateFallowGrazingLand(myMCalsFromFallowCounter, animalMCalRequirementMap)

                # Update the animal calculation reports with the new values after fallow allocation
                for animalGuid, requirements in self._mValueMap.items():
                    if animalGuid in animalCalcsReportMap:
                        myAnimalReport, oldRequirements = animalCalcsReportMap[animalGuid]
                        myAnimalReport = myAnimalReport or ""  # Initialize as an empty string if None or unbound
                        if oldRequirements > requirements:
                            reductionAmount = oldRequirements - requirements
                            myAnimalReport += f"\nFallow Land Grazing:\n"
                            myAnimalReport += f"Feed requirement reduced by {reductionAmount:.2f} MCal from fallow grazing\n"
                            myAnimalReport += f"Final feed requirement: {requirements:.2f} MCal\n"

                            # Update the report with new value
                            animalCalcsReportMap[animalGuid] = (myAnimalReport, requirements)
                            LaUtils.debug.log(f"Updated animal {animalGuid} with fallow grazing allocation", "Diet")

                # Recalculate overall values with the reduced requirements
                LaUtils.debug.log("Recalculating targets after fallow allocation", "Diet")

                # Update crop area targets to account for animal feed requirements
                for cropGuid, reportPair in cropCalcsReportMap.items():
                    cropReport, productionTarget = reportPair

                    # Check if any animals need grain from this crop
                    totalGrainNeeded = 0.0
                    for animalGuid, (myAnimalReport, requirements) in animalCalcsReportMap.items():
                        myAnimalReport = myAnimalReport or ""  # Initialize as an empty string if None or unbound

                        animalParameter = LaUtils.getAnimalParameter(self._mAnimals.get(animalGuid, ""))
                        if animalParameter and hasattr(animalParameter, 'fodderSourceMap'):
                            try:
                                fodderSources = animalParameter.fodderSourceMap()
                                if cropGuid in fodderSources:
                                    # Calculate requirement (simplified example)
                                    foodSource = fodderSources[cropGuid]
                                    totalGrainNeeded += requirements * 0.1  # Simplified calculation
                            except Exception as e:
                                LaUtils.debug.log(f"Error accessing fodderSourceMap for animal {animalGuid}: {e}", "Diet")

                    cropReport = cropReport or ""  # Initialize as an empty string if None or unbound

                    if totalGrainNeeded > 0:
                        newProductionTarget = productionTarget + totalGrainNeeded
                        cropReport += f"\nGrain for Animal Feed:\n"
                        cropReport += f"Additional production for animal feed: {totalGrainNeeded:.2f} kg\n"
                        cropReport += f"Total production target: {newProductionTarget:.2f} kg\n"

                        # Update the report
                        cropCalcsReportMap[cropGuid] = (cropReport, newProductionTarget)
                        LaUtils.debug.log(f"Updated crop {cropGuid} with animal feed requirements", "Diet")

            # Final diet percentages may need adjustment after all calculations
            LaUtils.debug.log("Finalizing diet calculations", "Diet")

            # Update the diet labels with final values including all reports
            myDietLabels._cropCalcsReportMap = cropCalcsReportMap
            myDietLabels._animalCalcsReportMap = animalCalcsReportMap

        except Exception as e:
            LaUtils.debug.log(f"Error in doCalcsAnimalsFirstDairySeparate: {str(e)}", "Error")
            import traceback
            LaUtils.debug.log(f"Error details: {traceback.format_exc()}", "Error")

        return myDietLabels

    def toHtml(self) -> str:
        """Generate an HTML representation of the model."""
        html = f"<h1>Model Report</h1>\n"
        html += f"<p><strong>Name:</strong> {self.name}</p>\n"
        html += f"<p><strong>Population:</strong> {self.population}</p>\n"
        html += f"<p><strong>Period:</strong> {self.period}</p>\n"
        html += f"<p><strong>Projection:</strong> {self.projection}</p>\n"
        html += f"<p><strong>Easting:</strong> {self.easting}</p>\n"
        html += f"<p><strong>Northing:</strong> {self.northing}</p>\n"
        html += f"<p><strong>Diet Percent:</strong> {self.dietPercent}%</p>\n"
        html += f"<p><strong>Meat Percent:</strong> {self.meatPercent}%</p>\n"
        html += f"<p><strong>Calories Per Person Daily:</strong> {self.caloriesPerPersonDaily}</p>\n"
        html += f"<p><strong>Dairy Utilisation:</strong> {self.dairyUtilisation}%</p>\n"
        html += f"<p><strong>Base on Plants:</strong> {self.baseOnPlants}</p>\n"
        html += f"<p><strong>Include Dairy:</strong> {self.includeDairy}</p>\n"
        html += f"<p><strong>Limit Dairy:</strong> {self.limitDairy}</p>\n"
        html += f"<p><strong>Limit Dairy Percent:</strong> {self.limitDairyPercent}%</p>\n"
        html += f"<p><strong>Common Land Value:</strong> {self.commonLandValue}</p>\n"
        html += f"<p><strong>Common Land Area Units:</strong> {self.commonLandAreaUnits}</p>\n"
        return html

    def allocateFallowGrazingLand(self, theFallowMCalsAvailable: float, theAnimalMCalRequirementMap: Dict[str, float]) -> None:
        """Allocate fallow grazing land to animals based on their priority.

        Args:
            theFallowMCalsAvailable: MCals available from fallow land
            theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements
        """
        from la.lib.lautils import LaUtils
        from la.lib.la import Priority

        LaUtils.debug.log(f"Starting fallow grazing land allocation with {theFallowMCalsAvailable:.2f} MCal available", "Diet")

        if theFallowMCalsAvailable <= 0 or not theAnimalMCalRequirementMap:
            LaUtils.debug.log("No fallow land or no animals to allocate to", "Diet")
            return

        # Create maps to hold animals by priority
        highPriorityMap = {}
        mediumPriorityMap = {}
        lowPriorityMap = {}

        # Group animals by fallow access priority
        for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
            if mCalRequirement <= 0:
                continue

            # Get animal parameter
            paramGuid = self._mAnimals.get(animalGuid, "")
            if not paramGuid:
                continue

            animalParameter = LaUtils.getAnimalParameter(paramGuid)
            if not animalParameter:
                continue

            # Get fallow usage priority
            try:
                fallowUsage = getattr(animalParameter, 'fallowUsage', Priority.None_)
                if fallowUsage == Priority.High:
                    highPriorityMap[animalGuid] = mCalRequirement
                elif fallowUsage == Priority.Medium:
                    mediumPriorityMap[animalGuid] = mCalRequirement
                elif fallowUsage == Priority.Low:
                    lowPriorityMap[animalGuid] = mCalRequirement
            except Exception as e:
                LaUtils.debug.log(f"Error getting fallow usage for animal {animalGuid}: {str(e)}", "Error")

        # Track remaining MCals to distribute
        remainingMCals = theFallowMCalsAvailable

        # Allocate to high priority animals first
        if highPriorityMap:
            LaUtils.debug.log(f"Allocating to {len(highPriorityMap)} high priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.High, remainingMCals, highPriorityMap)

        # Then to medium priority animals
        if mediumPriorityMap and remainingMCals > 0:
            LaUtils.debug.log(f"Allocating to {len(mediumPriorityMap)} medium priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.Medium, remainingMCals, mediumPriorityMap)

        # Finally to low priority animals
        if lowPriorityMap and remainingMCals > 0:
            LaUtils.debug.log(f"Allocating to {len(lowPriorityMap)} low priority animals", "Diet")
            remainingMCals = self.doTheFallowAllocation(Priority.Low, remainingMCals, lowPriorityMap)

        LaUtils.debug.log(f"Fallow allocation complete. {remainingMCals:.2f} MCal remains unallocated.", "Diet")

    def doTheFallowAllocation(self, thePriority: Priority, theAvailableFallowValue: float,
                            theAnimalMCalRequirementMap: Dict[str, float]) -> float:
        """Allocate fallow land to animals of a specific priority.

        Args:
            thePriority: Priority level being processed
            theAvailableFallowValue: MCals available from fallow land
            theAnimalMCalRequirementMap: Map of animal GUIDs to MCal requirements

        Returns:
            float: Remaining MCals after allocation
        """
        from la.lib.lautils import LaUtils

        if theAvailableFallowValue <= 0 or not theAnimalMCalRequirementMap:
            return theAvailableFallowValue

        # Calculate total MCals needed by this priority group
        totalNeeded = sum(theAnimalMCalRequirementMap.values())

        # If we have more than enough fallow land
        if theAvailableFallowValue >= totalNeeded:
            # Each animal gets 100% of what it needs
            LaUtils.debug.log(f"Enough fallow land for all {thePriority} priority animals", "Diet")
            for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
                # Adjust the animal's MCal requirement in the value map
                if animalGuid in self._mValueMap:
                    self._mValueMap[animalGuid] = max(0, self._mValueMap[animalGuid] - mCalRequirement)
                    LaUtils.debug.log(f"Animal {animalGuid} requirement reduced by {mCalRequirement:.2f} MCal", "Diet")

            # Return remaining MCals
            return theAvailableFallowValue - totalNeeded

        # Otherwise, distribute proportionally
        else:
            LaUtils.debug.log(f"Not enough fallow land for all {thePriority} priority animals. Distributing {theAvailableFallowValue:.2f} MCal proportionally.", "Diet")
            for animalGuid, mCalRequirement in theAnimalMCalRequirementMap.items():
                # Calculate proportion
                proportion = mCalRequirement / totalNeeded
                allocatedMCals = theAvailableFallowValue * proportion

                # Adjust the animal's MCal requirement
                if animalGuid in self._mValueMap:
                    self._mValueMap[animalGuid] = max(0, self._mValueMap[animalGuid] - allocatedMCals)
                    LaUtils.debug.log(f"Animal {animalGuid} requirement reduced by {allocatedMCals:.2f} MCal", "Diet")

            # All MCals have been allocated
            return 0.0
