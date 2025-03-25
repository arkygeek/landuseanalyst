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

    # @guid.setter
    def guid(self):
        """Method-style accessor for GUID - for backward compatibility."""
        return str(self._mGuid)

    def setGuid(self, guid=None):
        """
        Set the GUID to the given value or generate a new one.

        Args:
            guid: The GUID to set (optional)

        Returns:
            The new GUID
        """
        if guid is None:
            import uuid
            self._mGuid = str(uuid.uuid4())
        else:
            self._mGuid = str(guid)
        return self._mGuid