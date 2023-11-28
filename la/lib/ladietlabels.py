# ladietlabels.py
from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot, Qt
from lib.laserialisable import LaSerialisable
from lib.laguid import LaGuid
from la.lib.la import La
class LaDietLabels(LaSerialisable, LaGuid):
    def __init__(self):
        super().__init__()
        self._dairyMCalories: float = 0.0
        self._cropMCalories: float = 0.0
        self._animalMCalories: float = 0.0
        self._wildAnimalMCalories: float = 0.0
        self._wildPlantsMCalories: float = 0.0
        self._dairyPortionPct: float = 0.0
        self._tameMeatPortionPct: float = 0.0
        self._cropsPortionPct: float = 0.0
        self._wildAnimalPortionPct: float = 0.0
        self._wildPlantsPortionPct: float = 0.0
        self._plantsPortionPct: float = 0.0
        self._animalPortionPct: float = 0.0
        self._kiloCaloriesIndividualAnnual: float = 0.0
        self._megaCaloriesSettlementAnnual: float = 0.0
        self._dairySurplusMCalories: float = 0.0
        self._cropCalcsReportMap: La.LaReportMap = La.LaReportMap()
        self._animalCalcsReportMap: La.LaReportMap = La.LaReportMap()


    def __del__(self):
        pass

    def __copy__(self):
        return LaDietLabels(self)

    def __deepcopy__(self, memo):
        return LaDietLabels(self)

    @property
    def dairyMCalories(self):
        return self._dairyMCalories

    @dairyMCalories.setter
    def dairyMCalories(self, theDairyMCalories):
        if self._dairyMCalories != theDairyMCalories:
            self._dairyMCalories = theDairyMCalories
            self.dairyMCaloriesChanged.emit(theDairyMCalories)

    @property
    def cropMCalories(self):
        return self._cropMCalories

    @cropMCalories.setter
    def cropMCalories(self, theCropMCalories):
        if self._cropMCalories != theCropMCalories:
            self._cropMCalories = theCropMCalories
            self.cropMCaloriesChanged.emit(theCropMCalories)

    @property
    def animalMCalories(self):
        return self._animalMCalories

    @animalMCalories.setter
    def animalMCalories(self, theAnimalMCalories):
        if self._animalMCalories != theAnimalMCalories:
            self._animalMCalories = theAnimalMCalories
            self.animalMCaloriesChanged.emit(theAnimalMCalories)

    @property
    def wildAnimalMCalories(self):
        return self._wildAnimalMCalories

    @wildAnimalMCalories.setter
    def wildAnimalMCalories(self, theWildAnimalMCalories):
        if self._wildAnimalMCalories != theWildAnimalMCalories:
            self._wildAnimalMCalories = theWildAnimalMCalories
            self.wildAnimalMCaloriesChanged.emit(theWildAnimalMCalories)

    @property
    def wildPlantsMCalories(self):
        return self._wildPlantsMCalories

    @wildPlantsMCalories.setter
    def wildPlantsMCalories(self, theWildPlantsMCalories):
        if self._wildPlantsMCalories != theWildPlantsMCalories:
            self._wildPlantsMCalories = theWildPlantsMCalories
            self.wildPlantsMCaloriesChanged.emit(theWildPlantsMCalories)

    @property
    def dairyPortionPct(self):
        return self._dairyPortionPct

    @dairyPortionPct.setter
    def dairyPortionPct(self, theDairyPortionPct):
        if self._dairyPortionPct != theDairyPortionPct:
            self._dairyPortionPct = theDairyPortionPct
            self.dairyPortionPctChanged.emit(theDairyPortionPct)

    @property
    def tameMeatPortionPct(self):
        return self._tameMeatPortionPct

    @tameMeatPortionPct.setter
    def tameMeatPortionPct(self, theTameMeatPortionPct):
        if self._tameMeatPortionPct != theTameMeatPortionPct:
            self._tameMeatPortionPct = theTameMeatPortionPct
            self.tameMeatPortionPctChanged.emit(theTameMeatPortionPct)

    @property
    def cropsPortionPct(self):
        return self._cropsPortionPct

    @cropsPortionPct.setter
    def cropsPortionPct(self, theCropsPortionPct):
        if self._cropsPortionPct != theCropsPortionPct:
            self._cropsPortionPct = theCropsPortionPct
            self.cropsPortionPctChanged.emit(theCropsPortionPct)

    @property
    def wildAnimalPortionPct(self):
        return self._wildAnimalPortionPct

    @wildAnimalPortionPct.setter
    def wildAnimalPortionPct(self, theWildAnimalPortionPct):
        if self._wildAnimalPortionPct != theWildAnimalPortionPct:
            self._wildAnimalPortionPct = theWildAnimalPortionPct
            self.wildAnimalPortionPctChanged.emit(theWildAnimalPortionPct)

    @property
    def wildPlantsPortionPct(self):
        return self._wildPlantsPortionPct

    @wildPlantsPortionPct.setter
    def wildPlantsPortionPct(self, theWildPlantsPortionPct):
        if self._wildPlantsPortionPct != theWildPlantsPortionPct:
            self._wildPlantsPortionPct = theWildPlantsPortionPct
            self.wildPlantsPortionPctChanged.emit(theWildPlantsPortionPct)

    @property
    def plantsPortionPct(self):
        return self._plantsPortionPct

    @plantsPortionPct.setter
    def plantsPortionPct(self, thePlantsPortionPct):
        if self._plantsPortionPct != thePlantsPortionPct:
            self._plantsPortionPct = thePlantsPortionPct
            self.plantsPortionPctChanged.emit(thePlantsPortionPct)

    @property
    def animalPortionPct(self):
        return self._animalPortionPct

    @animalPortionPct.setter
    def animalPortionPct(self, theAnimalPortionPct):
        if self._animalPortionPct != theAnimalPortionPct:
            self._animalPortionPct = theAnimalPortionPct
            self.animalPortionPctChanged.emit(theAnimalPortionPct)

    @property
    def kiloCaloriesIndividualAnnual(self):
        return self._kiloCaloriesIndividualAnnual

    @kiloCaloriesIndividualAnnual.setter
    def kiloCaloriesIndividualAnnual(self, theKiloCaloriesIndividualAnnual):
        if self._kiloCaloriesIndividualAnnual != theKiloCaloriesIndividualAnnual:
            self._kiloCaloriesIndividualAnnual = theKiloCaloriesIndividualAnnual
            self.kiloCaloriesIndividualAnnualChanged.emit(theKiloCaloriesIndividualAnnual)

    @property
    def megaCaloriesSettlementAnnual(self):
        return self._megaCaloriesSettlementAnnual

    @megaCaloriesSettlementAnnual.setter
    def megaCaloriesSettlementAnnual(self, theMegaCaloriesSettlementAnnual):
        if self._megaCaloriesSettlementAnnual != theMegaCaloriesSettlementAnnual:
            self._megaCaloriesSettlementAnnual = theMegaCaloriesSettlementAnnual
            self.megaCaloriesSettlementAnnualChanged.emit(theMegaCaloriesSettlementAnnual)

    @property
    def dairySurplusMCalories(self):
        return self._dairySurplusMCalories

    @dairySurplusMCalories.setter
    def dairySurplusMCalories(self, theDairySurplusMCalories):
        if self._dairySurplusMCalories != theDairySurplusMCalories:
            self._dairySurplusMCalories = theDairySurplusMCalories
            self.dairySurplusMCaloriesChanged.emit(theDairySurplusMCalories)

    @property
    def cropCalcsReportMap(self):
        return self._cropCalcsReportMap

    @cropCalcsReportMap.setter
    def cropCalcsReportMap(self, theCropCalcsReportMap):
        if self._cropCalcsReportMap != theCropCalcsReportMap:
            self._cropCalcsReportMap = theCropCalcsReportMap
            self.cropCalcsReportMapChanged.emit(theCropCalcsReportMap)

    @property
    def animalCalcsReportMap(self):
        return self._animalCalcsReportMap

    @animalCalcsReportMap.setter
    def animalCalcsReportMap(self, theAnimalCalcsReportMap):
        if self._animalCalcsReportMap != theAnimalCalcsReportMap:
            self._animalCalcsReportMap = theAnimalCalcsReportMap
            self.animalCalcsReportMapChanged.emit(theAnimalCalcsReportMap)

    dairyMCaloriesChanged = pyqtSignal(float)
    cropMCaloriesChanged = pyqtSignal(float)
    animalMCaloriesChanged = pyqtSignal(float)
    wildAnimalMCaloriesChanged = pyqtSignal(float)
    wildPlantsMCaloriesChanged = pyqtSignal(float)
    dairyPortionPctChanged = pyqtSignal(float)
    tameMeatPortionPctChanged = pyqtSignal(float)
    cropsPortionPctChanged = pyqtSignal(float)
    wildAnimalPortionPctChanged = pyqtSignal(float)
    wildPlantsPortionPctChanged = pyqtSignal(float)
    plantsPortionPctChanged = pyqtSignal(float)
    animalPortionPctChanged = pyqtSignal(float)
    kiloCaloriesIndividualAnnualChanged = pyqtSignal(float)
    megaCaloriesSettlementAnnualChanged = pyqtSignal(float)
    dairySurplusMCaloriesChanged = pyqtSignal(float)
    cropCalcsReportMapChanged = pyqtSignal(La.LaReportMap)
    animalCalcsReportMapChanged = pyqtSignal(La.LaReportMap)


"""
This code defines a LaDietLabels class in Python using PyQt5. The class inherits
    from LaSerialisable and LaGuid, which are assumed to be defined elsewhere.

The class has several properties, including name, description, and labels, which
    are defined using the @pyqtProperty decorator.

The class has several slots, including setName, setDescription, and setLabels,
    which are used to set the values of the properties.

The class has several signals including nameChanged, descriptionChanged, and
    labelsChanged, and are emitted whenever a corresponding property is changed.

ladietlabels.cpp defines the implementation of the LaDietLabels class in C++.

The Python version of the class does not require an implementation file, as the
properties and slots are defined using decorators in the class definition.



based on this c++ code:

# ladietlabels.cpp
#include "ladietlabels.h"

LaDietLabels::LaDietLabels()
{
    _name = "";
    _description = "";
}

LaDietLabels::~LaDietLabels()
{
}

LaDietLabels::LaDietLabels(const LaDietLabels &other)
{
    _name = other._name;
    _description = other._description;
    _labels = other._labels;
}

LaDietLabels &LaDietLabels::operator=(const LaDietLabels &other)
{
    if (this != &other) {
        _name = other._name;
        _description = other._description;
        _labels = other._labels;
    }
    return *this;
}

QString LaDietLabels::name() const
{
    return _name;
}

QString LaDietLabels::description() const
{
    return _description;
}

QList<QString> LaDietLabels::labels() const
{
    return _labels;
}

void LaDietLabels::setName(const QString &name)
{
    _name = name;
}

void LaDietLabels::setDescription(const QString &description)
{
    _description = description;
}

void LaDietLabels::setLabels(const QList<QString> &labels)
{
    _labels = labels;
}

"""