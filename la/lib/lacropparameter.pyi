from typing import Optional, Union
from qgis.PyQt.QtCore import QObject, pyqtSignal
from la.lib.laserialisable import LaSerialisable
from la.lib.laguid import LaGuid
from la.lib.la import AreaUnits as LaAreaUnits
from la.lib.la import EnergyType as LaEnergyType

class LaCropParameter(QObject, LaSerialisable, LaGuid):
    """Type stub for LaCropParameter class"""

    # Signals
    nameChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    guidChanged = pyqtSignal(str)
    cropGuidChanged = pyqtSignal(str)
    percentTameCropChanged = pyqtSignal(float)
    spoilageChanged = pyqtSignal(float)
    reseedChanged = pyqtSignal(float)
    cropRotationChanged = pyqtSignal(bool)
    fallowRatioChanged = pyqtSignal(float)
    fallowEnergyTypeChanged = pyqtSignal(LaEnergyType)
    fallowValueChanged = pyqtSignal(int)
    areaUnitsChanged = pyqtSignal(LaAreaUnits)
    useCommonLandChanged = pyqtSignal(bool)
    useSpecificLandChanged = pyqtSignal(bool)
    rasterNameChanged = pyqtSignal(str)

    def __init__(self, theCropParameter: Optional['LaCropParameter'] = None, parent=None) -> None: ...

    # Properties with plain property decorators for Pylance
    @property
    def guid(self) -> str: ...
    
    # No setter for guid as it uses LaGuid's implementation

    @property
    def name(self) -> str: ...

    @name.setter
    def name(self, theName: str) -> None: ...

    @property
    def description(self) -> str: ...

    @description.setter
    def description(self, theDescription: str) -> None: ...

    @property
    def cropGuid(self) -> str: ...

    @cropGuid.setter
    def cropGuid(self, theGuid: str) -> None: ...

    @property
    def percentTameCrop(self) -> float: ...

    @percentTameCrop.setter
    def percentTameCrop(self, thePercentage: float) -> None: ...

    @property
    def spoilage(self) -> int: ...

    @spoilage.setter
    def spoilage(self, thePercentage: int) -> None: ...

    @property
    def reseed(self) -> int: ...

    @reseed.setter
    def reseed(self, thePercentage: int) -> None: ...

    @property
    def cropRotation(self) -> bool: ...

    @cropRotation.setter
    def cropRotation(self, theFlag: bool) -> None: ...

    @property
    def fallowRatio(self) -> float: ...

    @fallowRatio.setter
    def fallowRatio(self, theFallowRatio: float) -> None: ...


    @property
    def fallowEnergyType(self) -> Union[LaEnergyType, None]:
        return self._fallowEnergyType

    # Setter for fallowEnergyType
    # We use the same type hint as the property
    # to indicate that it can be None or an instance of LaEnergyType
    # This is a workaround for the fact that PyQt doesn't support None as a valid type
    @fallowEnergyType.setter
    def fallowEnergyType(self, theEnergyType: Union[LaEnergyType, None]) -> None:
        self._fallowEnergyType = theEnergyType

    @property
    def fallowValue(self) -> int: ...

    @fallowValue.setter
    def fallowValue(self, theKg: int) -> None: ...

    @property
    def areaUnits(self) -> LaAreaUnits: ...

    @areaUnits.setter
    def areaUnits(self, theAreaUnit: Optional[LaAreaUnits]) -> None: ...

    @property
    def useCommonLand(self) -> bool: ...

    @useCommonLand.setter
    def useCommonLand(self, theFlag: bool) -> None: ...

    @property
    def useSpecificLand(self) -> bool: ...

    @useSpecificLand.setter
    def useSpecificLand(self, theFlag: bool) -> None: ...

    @property
    def rasterName(self) -> str: ...

    @rasterName.setter
    def rasterName(self, theRasterName: str) -> None: ...

    # Methods from LaGuid
    def setGuid(self, theGuid: Optional[str] = None) -> None: ...

    # LaSerialisable methods
    def fromXml(self, theXml: str) -> bool: ...
    def toXml(self) -> str: ...
    def toText(self) -> str: ...
    def toHtml(self) -> str: ...
    def fromXmlFile(self, theFileName: str) -> bool: ...
    def toXmlFile(self, theFileName: str) -> bool: ...
    
    # Debugging helper
    def debug_info(self) -> str: ...