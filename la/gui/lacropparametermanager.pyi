from typing import Any, Optional

class LaCropParameterManager:
    def __init__(self, parent: Optional[Any] = None, fl: Optional[Any] = None) -> None: ...
    def __del__(self) -> None: ...
    def cellClicked(self, theRow: int, theColumn: int) -> None: ...
    def on_cboCrop_changed(self, theIndex: int) -> None: ...
    def showCropParameter(self) -> None: ...
    def on_toolCopy_clicked(self) -> None: ...
    def on_toolNew_clicked(self) -> None: ...
    def on_toolDelete_clicked(self) -> None: ...
    def on_pbnApply_clicked(self) -> None: ...
    def resizeEvent(self, event: Any) -> None: ...
    def refreshCropParameterTable(self, theGuid: Optional[str] = None) -> None: ...
    def selectCropParameter(self, theFileName: str) -> None: ...
    def readSettings(self) -> None: ...
    def writeSettings(self) -> None: ...
    def setComboToDefault(self, thepCombo: Any, theDefault: str) -> bool: ...

""" here is a list of the original c++ functions along with their parameter types and return types:

1. `LaCropParameterManager::LaCropParameterManager(QWidget* parent, Qt::WindowFlags fl)`: 
        Constructor with parameters `parent` of type `QWidget*` and `fl` of type `Qt::WindowFlags`. 
        Returns nothing.

2. `LaCropParameterManager::~LaCropParameterManager()`: 
        Destructor with no parameters. 
        Returns nothing.

3. `LaCropParameterManager::readSettings()`: 
        Function with no parameters. 
        Returns nothing.

4. `LaCropParameterManager::writeSettings()`: 
        Function with no parameters. 
        Returns nothing.

5. `LaCropParameterManager::refreshCropParameterTable(QString theGuid)`: 
        Function with parameter `theGuid` of type `QString`. 
        Returns nothing.

6. `LaCropParameterManager::on_cboCrop_changed(int theIndex)`: 
        Function with parameter `theIndex` of type `int`. 
        Returns nothing.

7. `LaCropParameterManager::cellClicked(int theRow, int theColumn)`: 
        Function with parameters `theRow` and `theColumn` of type `int`. 
        Returns nothing.

8. `LaCropParameterManager::selectCropParameter(QString theFileName)`: 
        Function with parameter `theFileName` of type `QString`. 
        Returns nothing.

9. `LaCropParameterManager::showCropParameter()`: 
        Function with no parameters. 
        Returns nothing.

10. `LaCropParameterManager::on_toolNew_clicked()`: 
        Function with no parameters. 
        Returns nothing.

11. `LaCropParameterManager::resizeEvent(QResizeEvent * theEvent)`: 
        Function with parameter `theEvent` of type `QResizeEvent*`. 
        Returns nothing.

12. `LaCropParameterManager::on_toolCopy_clicked()`: 
        Function with no parameters. 
        Returns nothing.

13. `LaCropParameterManager::on_toolDelete_clicked()`: 
        Function with no parameters. 
        Returns nothing.

14. `LaCropParameterManager::on_pbnApply_clicked()`: 
        Function with no parameters. 
        Returns nothing.

15. `LaCropParameterManager::setComboToDefault(QComboBox * thepCombo, QString theDefault)`: 
        Function with parameters `thepCombo` of type `QComboBox*` and `theDefault` of type `QString`. 
        Returns `bool`.
"""