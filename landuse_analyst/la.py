#include <QMap>
#include <QPair>
#include <QString>
#include <lafoodsource.h>
from enum import Enum

# // < animal guid < enabled, animalparamters guid>>
# // or
# // < plant guid < enabled, animalparamters guid>>
# typedef QMap < QString, QPair < bool, QString > > LaTripleMap

# typedef QPair < QPair < QString, QString > , QPair < QString, QString > > LaRasterInfo
# typedef QMap < QString, LaFoodSource > LaFoodSourceMap
# typedef QPair < float, float > HerdSize
# typedef QMap < QString, QPair < QString, float > > LaReportMap

# enum Priority {None, High, Medium, Low}
# enum Status {MoreThanEnoughToCompletelySatisfy, NotEnoughToCompletelySatisfy}
# enum LandBeingGrazed {Common, Unique}
# enum AreaUnits {Dunum, Hectare}

class AreaUnits(Enum):
    Dunum = "Dunum"
    Hectare = "Hectare"
# enum LandFound {NotEnough, TooMuch, FoundTarget}
# enum EnergyType {KCalories, TDN}
