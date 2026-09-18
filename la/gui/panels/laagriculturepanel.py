"""Agriculture section: crop and animal pickers with inline parameter choice. Manual tag A3."""

from typing import Callable, Dict, Optional

from qgis.PyQt.QtCore import QSize, Qt
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import (
    QCheckBox, QComboBox, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget,
)
from qgis.gui import QgsCollapsibleGroupBox

from la.gui.lascenariocontroller import LaScenarioController
from la.lib.lacatalogue import LaCatalogue
from la.lib.lautils import LaUtils

_OK_STYLE = "QLabel { color: #1f7a3a; font-weight: 600; }"
_BAD_STYLE = "QLabel { color: #a33a2a; font-weight: 600; }"
_MUTED_STYLE = "QLabel { color: palette(mid); }"


class LaPickerList(QWidget):
    """
    Checkable rows of catalogue items, each with a parameter-set combo and its share.

    :param theKind: ``"crop"`` or ``"animal"`` — selects catalogue and controller calls.
    """

    def __init__(self, theKind: str, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.mKind = theKind
        self.mController = theController
        self.mCatalogue: LaCatalogue = theController.mCatalogue
        self._mRows: Dict[str, Dict[str, QWidget]] = {}
        self._mLoading = False
        self.mGrid = QGridLayout(self)
        self.mGrid.setContentsMargins(0, 0, 0, 0)
        self.mGrid.setHorizontalSpacing(6)
        self.mGrid.setVerticalSpacing(2)
        self.mGrid.setColumnStretch(0, 1)
        self.mGrid.setColumnStretch(1, 1)
        self.rebuild()

    # -- catalogue access -------------------------------------------------
    def _items(self):
        return self.mCatalogue.crops() if self.mKind == "crop" else self.mCatalogue.animals()

    def _parametersFor(self, theGuid: str):
        return (self.mCatalogue.cropParametersFor(theGuid) if self.mKind == "crop"
                else self.mCatalogue.animalParametersFor(theGuid))

    def _selected(self) -> Dict[str, str]:
        return self.mController.mSelectedCrops if self.mKind == "crop" else self.mController.mSelectedAnimals

    def _percentOf(self, theParameter) -> float:
        myAttr = "percentTameCrop" if self.mKind == "crop" else "percentTameMeat"
        return float(getattr(theParameter, myAttr, 0.0) or 0.0)

    # -- build ------------------------------------------------------------
    def rebuild(self) -> None:
        """Recreate every row from the catalogue and current selection."""
        self._mLoading = True
        try:
            while self.mGrid.count():
                myItem = self.mGrid.takeAt(0)
                if myItem.widget() is not None:
                    myItem.widget().deleteLater()
            self._mRows.clear()
            mySelected = self._selected()
            myItems = sorted(self._items().items(), key=lambda kv: str(getattr(kv[1], "name", "")).lower())
            if not myItems:
                myEmpty = QLabel(
                    f"No {self.mKind}s in the catalogue yet — use the Manage buttons below "
                    f"or run install_sample_data.sh.", self)
                myEmpty.setWordWrap(True)
                myEmpty.setStyleSheet(_MUTED_STYLE)
                self.mGrid.addWidget(myEmpty, 0, 0, 1, 3)
                return
            for myRow, (myGuid, myItem) in enumerate(myItems):
                myCheck = QCheckBox(str(getattr(myItem, "name", myGuid)), self)
                myCheck.setObjectName(f"cb{self.mKind.capitalize()}_{myGuid[:8]}")
                myIconPath = LaCatalogue.imagePath(str(getattr(myItem, "imageFile", "") or ""))
                if myIconPath:
                    myCheck.setIcon(QIcon(QPixmap(myIconPath)))
                    myCheck.setIconSize(QSize(22, 22))
                myCheck.setChecked(myGuid in mySelected)
                myCombo = QComboBox(self)
                myCombo.setObjectName(f"cbo{self.mKind.capitalize()}Parameter_{myGuid[:8]}")
                myCombo.setToolTip("Parameter set (share of the diet, yields, fallow, grazing values).")
                myParameters = self._parametersFor(myGuid)
                for myParameterGuid, myParameter in sorted(
                        myParameters.items(), key=lambda kv: str(getattr(kv[1], "name", "")).lower()):
                    myCombo.addItem(str(getattr(myParameter, "name", myParameterGuid)), myParameterGuid)
                if not myParameters:
                    myCombo.addItem("no parameter set", "")
                    myCombo.setEnabled(False)
                    myCheck.setToolTip("This item has no parameter set yet, so it cannot be selected.")
                    myCheck.setEnabled(False)
                myCurrent = mySelected.get(myGuid, "")
                myIndex = myCombo.findData(myCurrent) if myCurrent else -1
                myCombo.setCurrentIndex(myIndex if myIndex >= 0 else 0)
                myCombo.setEnabled(myCombo.isEnabled() and myGuid in mySelected)
                myPercent = QLabel(self)
                myPercent.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                myPercent.setMinimumWidth(52)
                myPercent.setToolTip("Share of the domestic crop / domestic meat calories this item supplies.")
                self.mGrid.addWidget(myCheck, myRow, 0)
                self.mGrid.addWidget(myCombo, myRow, 1)
                self.mGrid.addWidget(myPercent, myRow, 2)
                self._mRows[myGuid] = {"check": myCheck, "combo": myCombo, "percent": myPercent}
                self._refreshPercent(myGuid)
                myCheck.toggled.connect(lambda checked, g=myGuid: self._onToggled(g, checked))
                myCombo.currentIndexChanged.connect(lambda _i, g=myGuid: self._onParameterChanged(g))
        finally:
            self._mLoading = False

    def _refreshPercent(self, theGuid: str) -> None:
        myRow = self._mRows.get(theGuid)
        if not myRow:
            return
        myCombo: QComboBox = myRow["combo"]
        myParameterGuid = myCombo.currentData() or ""
        myParameter = self._parametersFor(theGuid).get(myParameterGuid)
        myLabel: QLabel = myRow["percent"]
        if myParameter is None:
            myLabel.setText("—")
            myLabel.setStyleSheet(_MUTED_STYLE)
        else:
            myLabel.setText(f"{self._percentOf(myParameter):.1f} %")
            myLabel.setStyleSheet("" if myRow["check"].isChecked() else _MUTED_STYLE)

    def _onToggled(self, theGuid: str, theChecked: bool) -> None:
        if self._mLoading:
            return
        myRow = self._mRows[theGuid]
        myRow["combo"].setEnabled(theChecked and myRow["combo"].count() > 0 and bool(myRow["combo"].currentData()))
        myParameterGuid = myRow["combo"].currentData() or ""
        if self.mKind == "crop":
            self.mController.setCropSelected(theGuid, theChecked, myParameterGuid)
        else:
            self.mController.setAnimalSelected(theGuid, theChecked, myParameterGuid)
        self._refreshPercent(theGuid)

    def _onParameterChanged(self, theGuid: str) -> None:
        if self._mLoading:
            return
        myParameterGuid = self._mRows[theGuid]["combo"].currentData() or ""
        if self.mKind == "crop":
            self.mController.setCropParameter(theGuid, myParameterGuid)
        else:
            self.mController.setAnimalParameter(theGuid, myParameterGuid)
        self._refreshPercent(theGuid)

    def syncFromController(self) -> None:
        """Reflect a selection change made elsewhere (e.g. Select all) without rebuilding."""
        mySelected = self._selected()
        self._mLoading = True
        try:
            for myGuid, myRow in self._mRows.items():
                myRow["check"].setChecked(myGuid in mySelected)
                myParameterGuid = mySelected.get(myGuid, "")
                myIndex = myRow["combo"].findData(myParameterGuid) if myParameterGuid else -1
                if myIndex >= 0:
                    myRow["combo"].setCurrentIndex(myIndex)
                myRow["combo"].setEnabled(myGuid in mySelected and bool(myRow["combo"].currentData()))
                self._refreshPercent(myGuid)
        finally:
            self._mLoading = False


class LaAgriculturePanel(QgsCollapsibleGroupBox):
    """Crops and animals with their parameter sets, share chips and manage buttons."""

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__("Agriculture", parent)
        self.setObjectName("grpAgriculture")
        self.setSaveCollapsedState(True)
        self.setSettingGroup("landuseAnalyst/panels")
        self.mController = theController

        myLayout = QVBoxLayout(self)

        myCropHeader = QHBoxLayout()
        myCropTitle = QLabel("<b>Crops</b>", self)
        self.lblCropsChip = QLabel(self)
        self.lblCropsChip.setObjectName("lblCropsChip")
        myCropHeader.addWidget(myCropTitle)
        myCropHeader.addStretch()
        myCropHeader.addWidget(self.lblCropsChip)
        myLayout.addLayout(myCropHeader)
        self.cropList = LaPickerList("crop", theController, self)
        self.cropList.setObjectName("listCrops")
        myLayout.addWidget(self.cropList)
        myCropButtons = QHBoxLayout()
        self.pbnManageCrops = self._button("pbnManageCrops", "Manage crops…", myCropButtons)
        self.pbnManageCropParameters = self._button("pbnManageCropParameters", "Crop parameters…", myCropButtons)
        myCropButtons.addStretch()
        myLayout.addLayout(myCropButtons)

        myAnimalHeader = QHBoxLayout()
        myAnimalTitle = QLabel("<b>Animals</b>", self)
        self.lblAnimalsChip = QLabel(self)
        self.lblAnimalsChip.setObjectName("lblAnimalsChip")
        myAnimalHeader.addWidget(myAnimalTitle)
        myAnimalHeader.addStretch()
        myAnimalHeader.addWidget(self.lblAnimalsChip)
        myLayout.addLayout(myAnimalHeader)
        self.animalList = LaPickerList("animal", theController, self)
        self.animalList.setObjectName("listAnimals")
        myLayout.addWidget(self.animalList)
        myAnimalButtons = QHBoxLayout()
        self.pbnManageAnimals = self._button("pbnManageAnimals", "Manage animals…", myAnimalButtons)
        self.pbnManageAnimalParameters = self._button("pbnManageAnimalParameters", "Animal parameters…", myAnimalButtons)
        myAnimalButtons.addStretch()
        self.pbnSelectAll = self._button("pbnSelectAll", "Select all", myAnimalButtons)
        self.pbnSelectAll.setToolTip("Select every crop and animal that has a parameter set (the thesis scenarios use all of them).")
        myLayout.addLayout(myAnimalButtons)

        self.pbnManageCrops.clicked.connect(lambda: self._openManager(self._cropManager))
        self.pbnManageCropParameters.clicked.connect(lambda: self._openManager(self._cropParameterManager))
        self.pbnManageAnimals.clicked.connect(lambda: self._openManager(self._animalManager))
        self.pbnManageAnimalParameters.clicked.connect(lambda: self._openManager(self._animalParameterManager))
        self.pbnSelectAll.clicked.connect(self.mController.selectAll)
        self.mController.selectionChanged.connect(self._onSelectionChanged)
        self.mController.mCatalogue.changed.connect(self._onCatalogueChanged)
        self._updateChips()

    def _button(self, theName: str, theText: str, theLayout: QHBoxLayout) -> QPushButton:
        myButton = QPushButton(theText, self)
        myButton.setObjectName(theName)
        myButton.setFlat(False)
        theLayout.addWidget(myButton)
        return myButton

    # -- editors ----------------------------------------------------------
    def _cropManager(self):
        from la.gui.lacropmanager import LaCropManager
        return LaCropManager(LaUtils.getAvailableCrops(), self.window())

    def _cropParameterManager(self):
        from la.gui.lacropparametermanager import LaCropParameterManager
        return LaCropParameterManager(self.window())

    def _animalManager(self):
        from la.gui.laanimalmanager import LaAnimalManager
        return LaAnimalManager(parent=self.window())

    def _animalParameterManager(self):
        from la.gui.laanimalparametermanager import LaAnimalParameterManager
        return LaAnimalParameterManager(parent=self.window())

    def _openManager(self, theFactory: Callable) -> None:
        try:
            myDialog = theFactory()
        except Exception as e:
            LaUtils.debug.log(f"Could not open editor: {e}", "Error")
            return
        myDialog.exec_()
        self.mController.mCatalogue.refresh()

    # -- updates ----------------------------------------------------------
    def _onSelectionChanged(self) -> None:
        self.cropList.syncFromController()
        self.animalList.syncFromController()
        self._updateChips()

    def _onCatalogueChanged(self) -> None:
        self.cropList.rebuild()
        self.animalList.rebuild()
        self._updateChips()

    def _updateChips(self) -> None:
        myCropTotal, myAnimalTotal = self.mController.percentTotals()
        self._setChip(self.lblCropsChip, len(self.mController.mSelectedCrops), myCropTotal, "crop")
        self._setChip(self.lblAnimalsChip, len(self.mController.mSelectedAnimals), myAnimalTotal, "animal")

    @staticmethod
    def _setChip(theLabel: QLabel, theCount: int, theTotal: float, theNoun: str) -> None:
        if theCount == 0:
            theLabel.setText(f"no {theNoun}s selected")
            theLabel.setStyleSheet(_MUTED_STYLE)
            return
        myPlural = "" if theCount == 1 else "s"
        theLabel.setText(f"{theCount} {theNoun}{myPlural} · {theTotal:.1f} %")
        theLabel.setStyleSheet(_OK_STYLE if abs(theTotal - 100.0) <= 0.1 else _BAD_STYLE)
        theLabel.setToolTip("Shares must total 100 %." if abs(theTotal - 100.0) > 0.1 else "Shares total 100 %.")
