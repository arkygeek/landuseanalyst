from qgis.PyQt.QtCore import QUuid
from typing import Optional

class LaGuid:
    """
    A class that represents a unique identifier (GUID) used in Land Use Analyst.

    The class provides two methods:
    - guid: Returns the GUID value.
    - setGuid: Sets the GUID value.
    """
    def __init__(self):
        self._guid = QUuid.createUuid().toString(QUuid.Id128)

    def guid(self) -> str:
        """
        Returns the GUID value.
        """
        return self._guid

    def setGuid(self, theGuid: Optional[str]) -> None:
        """
        Sets the GUID value.
        """
        if theGuid is None:
            self._guid = QUuid.createUuid().toString(QUuid.Id128)
        else:
            self._guid = theGuid