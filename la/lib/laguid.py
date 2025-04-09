from qgis.PyQt.QtCore import QUuid
from typing import Optional

class LaGuid:
    """Base class for objects that need a GUID."""

    def __init__(self):
        """Initialize the guid."""
        self._mGuid = ""

    @property
    def guid(self):
        """Get the GUID as a string."""
        return str(self._mGuid)

    # Method-style accessor for GUID - for backward compatibility.
    def guid(self, value=None):
        if value is not None:
            self.setGuid(value)
        else:
            return str(self._mGuid)

    def setGuid(self, theGuid=None):
        """
        Set the GUID to the given value or generate a new one.

        Args:
            guid: The GUID to set (optional)

        Returns:
            The new GUID
        """
        if theGuid is None:
            import uuid
            self._mGuid = str(uuid.uuid4())
        else:
            self._mGuid = str(theGuid)
        return self._mGuid