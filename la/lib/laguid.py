import uuid

class LaGuid:
    """Base class for objects that need a GUID.

    Backing field is `self._mGuid`; public accessor is the `guid` property.
    Subclasses that define their own pyqtProperty for `guid` must read and
    write `self._mGuid` (not a separate `self.mGuid`) so the storage stays
    consistent with `setGuid()`.
    """

    def __init__(self):
        self._mGuid = ""

    @property
    def guid(self) -> str:
        return str(self._mGuid)

    @guid.setter
    def guid(self, theGuid) -> None:
        """Assign the GUID. Subclasses that override `guid` with a
        pyqtProperty should still write to `self._mGuid` so the storage
        stays consistent with `setGuid()` calls."""
        self._mGuid = str(theGuid) if theGuid is not None else ""

    def setGuid(self, theGuid=None) -> str:
        """Set the GUID. If `theGuid` is None, generate a new one.

        Returns the new GUID value.
        """
        if theGuid is None:
            self._mGuid = str(uuid.uuid4())
        else:
            self._mGuid = str(theGuid)
        return self._mGuid
