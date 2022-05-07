from enum import Enum
# from PyQt5.QtCore import QMap, QString, QPair
# from PyQt5.QtCore  import QMap, QString, QPair
from typing import List, NewType

# LaRasterInfo = NewType("LaRasterInfo", QMap((QPair(QString(), QString())), (QPair(QString(), QString()))))
LaRasterInfo = NewType("LaRasterInfo", ((()(str(), str())), ((str(), str()))))

print(LaRasterInfo)
