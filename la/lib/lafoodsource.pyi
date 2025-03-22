from typing import Optional, Union
from qgis.PyQt.QtCore import QObject, pyqtSignal

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

    # Signal declarations
    grainChanged: pyqtSignal
    fodderChanged: pyqtSignal
    daysChanged: pyqtSignal
    usedChanged: pyqtSignal
    cropGuidChanged: pyqtSignal

    def __init__(self, parent: Optional[QObject] = None) -> None:
        """
        Initialize a new LaFoodSource instance with default values.

        Args:
            parent: The parent QObject. Defaults to None.
        """
        ...

    # Property: grain
    @property
    def grain(self) -> int:
        """
        Get the amount of grain produced by this food source.

        Returns:
            The grain amount.
        """
        ...

    @grain.setter
    def grain(self, value: int) -> None:
        """
        Set the amount of grain produced by this food source.

        Args:
            value: The new grain amount.
        """
        ...

    # Property: fodder
    @property
    def fodder(self) -> int:
        """
        Get the amount of fodder produced by this food source.

        Returns:
            The fodder amount.
        """
        ...

    @fodder.setter
    def fodder(self, value: int) -> None:
        """
        Set the amount of fodder produced by this food source.

        Args:
            value: The new fodder amount.
        """
        ...

    # Property: days
    @property
    def days(self) -> int:
        """
        Get the number of days this food source is available/productive.

        Returns:
            Number of days.
        """
        ...

    @days.setter
    def days(self, value: int) -> None:
        """
        Set the number of days this food source is available/productive.

        Args:
            value: The new number of days.
        """
        ...

    # Property: used
    @property
    def used(self) -> bool:
        """
        Get whether this food source is being used in the current simulation.

        Returns:
            True if the food source is used, False otherwise.
        """
        ...

    @used.setter
    def used(self, value: bool) -> None:
        """
        Set whether this food source is being used in the current simulation.

        Args:
            value: The new used status.
        """
        ...

    # Property: cropGuid
    @property
    def cropGuid(self) -> str:
        """
        Get the unique identifier for the crop associated with this food source.

        Returns:
            The crop GUID (Globally Unique Identifier).
        """
        ...

    @cropGuid.setter
    def cropGuid(self, value: str) -> None:
        """
        Set the unique identifier for the crop associated with this food source.

        Args:
            value: The new crop GUID.
        """
        ...
