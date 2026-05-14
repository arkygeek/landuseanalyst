from qgis.PyQt.QtCore import QObject, pyqtProperty, pyqtSignal

class LaFoodSource(QObject):
    """
    A class representing a food source in the Land Use Analyst system.

    This class defines attributes and behaviors of food sources that can provide
    grain and fodder over a specified number of days. Food sources are typically
    crops that can be used to feed animals or humans in the simulation.

    Attributes:
        grain (int): Amount of grain produced by this food source.
        fodder (int): Amount of fodder produced by this food source.
        days (int): Number of days this food source is available/productive.
        used (bool): Flag indicating whether this food source is being used.
        cropGuid (str): Unique identifier for the associated crop.

    Signals:
        grainChanged: Emitted when grain value changes.
        fodderChanged: Emitted when fodder value changes.
        daysChanged: Emitted when days value changes.
        usedChanged: Emitted when used status changes.
        cropGuidChanged: Emitted when cropGuid changes.
    """

    _grainChanged = pyqtSignal(int)
    _fodderChanged = pyqtSignal(int)
    _daysChanged = pyqtSignal(int)
    _usedChanged = pyqtSignal(bool)
    _cropGuidChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Initialize a new LaFoodSource instance with default values.

        Args:
            parent (QObject, optional): The parent QObject. Defaults to None.
        """
        super().__init__(parent)
        self.mGrain = int()
        self.mFodder = int()
        self.mDays = int()
        self.mUsed = bool()
        self.mCropGuid = str()

    @pyqtProperty(int, notify=_grainChanged)
    def grain(self): #type: ignore
        """
        Get the amount of grain produced by this food source.

        Returns:
            int: The grain amount.
        """
        return int(self.mGrain)

    @grain.setter
    def grain(self, value):
        """
        Set the amount of grain produced by this food source.

        Args:
            value (int): The new grain amount.
        """
        if self.mGrain != value:
            self.mGrain = value
            self._grainChanged.emit(value)

    @pyqtProperty(int, notify=_fodderChanged)
    def fodder(self): #type: ignore
        """
        Get the amount of fodder produced by this food source.

        Returns:
            int: The fodder amount.
        """
        return int(self.mFodder)

    @fodder.setter
    def fodder(self, value):
        """
        Set the amount of fodder produced by this food source.

        Args:
            value (int): The new fodder amount.
        """
        if self.mFodder != value:
            self.mFodder = value
            self._fodderChanged.emit(value)

    @pyqtProperty(int, notify=_daysChanged)
    def days(self): #type: ignore
        """
        Get the number of days this food source is available/productive.

        Returns:
            int: Number of days.
        """
        return int(self.mDays)

    @days.setter
    def days(self, value):
        """
        Set the number of days this food source is available/productive.

        Args:
            value (int): The new number of days.
        """
        if self.mDays != value:
            self.mDays = value
            self._daysChanged.emit(value)

    @pyqtProperty(bool, notify=_usedChanged)
    def used(self): #type: ignore
        """
        Get whether this food source is being used in the current simulation.

        Returns:
            bool: True if the food source is used, False otherwise.
        """
        return bool(self.mUsed)

    @used.setter
    def used(self, value):
        """
        Set whether this food source is being used in the current simulation.

        Args:
            value (bool): The new used status.
        """
        if self.mUsed != value:
            self.mUsed = value
            self._usedChanged.emit(value)

    @pyqtProperty(str, notify=_cropGuidChanged)
    def cropGuid(self): #type: ignore
        """
        Get the unique identifier for the crop associated with this food source.

        Returns:
            str: The crop GUID (Globally Unique Identifier).
        """
        return str(self.mCropGuid)

    @cropGuid.setter
    def cropGuid(self, theCropGuid):
        """
        Set the unique identifier for the crop associated with this food source.

        :param theCropGuid: The new crop GUID.
        :type theCropGuid: str
        """
        if self.mCropGuid != theCropGuid:
            self.mCropGuid = theCropGuid
            self._cropGuidChanged.emit(theCropGuid)