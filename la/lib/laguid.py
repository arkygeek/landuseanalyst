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
        """Initialize with a new GUID - matches C++ behavior"""
        self._guid = ""
        self.setGuid()  # Automatically generate GUID like C++ version

    def guid(self) -> str:
        """
        Returns the GUID value.
        """
        return self._guid

    def setGuid(self, theGuid: Optional[str] = None) -> None:
        """
        Sets the GUID value. If no GUID is provided, generates a new one.
        Matches C++ behavior by stripping braces.
        """
        if theGuid is None or theGuid == "":
            # Match C++ behavior of removing braces
            self._guid = QUuid.createUuid().toString(QUuid.StringFormat.WithoutBraces)
        else:
            self._guid = theGuid