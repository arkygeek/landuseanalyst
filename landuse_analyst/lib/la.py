#include <QMap>
#include <QPair>
#include <QString>
#include <lafoodsource.h>
from enum import Enum
from PyQt5.QtCore import QMap, QString, QPair
from typing import List, NewType


# typedef QMap < QString, QPair < bool, QString > > LaTripleMap
LaTripleMap = NewType("LaTripleMap", QMap(QString(), QPair(bool, QString())))

# typedef QPair < QPair < QString, QString > , QPair < QString, QString > > LaRasterInfo
LaRasterInfo = NewType("LaRasterInfo", QMap((QPair(QString(), QString())), (QPair(QString(), QString()))))

# typedef QMap < QString, LaFoodSource > LaFoodSourceMap
# typedef QPair < float, float > HerdSize
# typedef QMap < QString, QPair < QString, float > > LaReportMap

# enum Priority {None, High, Medium, Low}
# enum Status {MoreThanEnoughToCompletelySatisfy, NotEnoughToCompletelySatisfy}
# enum LandBeingGrazed {Common, Unique}
# enum AreaUnits {Dunum, Hectare}

# class LaRasterInfo:
#     def __init__(self, QMap( (QPair(**kwargs,**kwargs)) , (QPair(**kwargs,**kwargs)))):
#         self.myPair1 = QPair(QString, QString)
#         myPair2 = QPair(QString, QString)
#         myMap = QMap(myPair1, myPair2)
#         return myMap



class AreaUnits(Enum):
    Dunum = "Dunum"
    Hectare = "Hectare"

# enum LandFound {NotEnough, TooMuch, FoundTarget}
class LandFound(Enum):
    NotEnough="NotEnough"
    TooMuch="TooMuch"
    FoundTarget="FoundTarget"


# enum EnergyType {KCalories, TDN}
class EnergyType(Enum):
    KCalories="KCalories"
    TDN="TDN"
