"""Advanced section: precision, live preview, common-land value, developer console."""

from typing import Optional

from qgis.PyQt.QtWidgets import QCheckBox, QComboBox, QFormLayout, QHBoxLayout, QPushButton, QVBoxLayout, QWidget
from qgis.gui import QgsCollapsibleGroupBox, QgsDoubleSpinBox, QgsSpinBox

from la.gui.lascenariocontroller import LaScenarioController
from la.lib.la import AreaUnits, EnergyType
from la.lib.lautils import LaUtils


class LaAdvancedPanel(QgsCollapsibleGroupBox):
    """Rarely-touched settings; collapsed by default."""

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__("Advanced", parent)
        self.setObjectName("grpAdvanced")
        self.setSaveCollapsedState(True)
        self.setSettingGroup("landuseAnalyst/panels")
        self.setCollapsed(True)
        self.mController = theController
        self._mLoading = False

        myLayout = QVBoxLayout(self)
        myForm = QFormLayout()
        myForm.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.sbPrecision = QgsSpinBox(self)
        self.sbPrecision.setObjectName("sbPrecision")
        self.sbPrecision.setRange(1, 50)
        self.sbPrecision.setSuffix(" %")
        self.sbPrecision.setToolTip(
            "Catchment search stops when the found area is within ± precision/2 of the target (thesis: 5 %).")
        myForm.addRow("Precision", self.sbPrecision)

        self.sbCommonLandValue = QgsDoubleSpinBox(self)
        self.sbCommonLandValue.setObjectName("sbCommonLandValue")
        self.sbCommonLandValue.setRange(0, 1e9)
        self.sbCommonLandValue.setDecimals(0)
        self.sbCommonLandValue.setToolTip("Area of common land available to the settlement.")
        myUnitsRow = QHBoxLayout()
        myUnitsRow.addWidget(self.sbCommonLandValue, 1)
        self.cboAreaUnits = QComboBox(self)
        self.cboAreaUnits.setObjectName("cboAreaUnits")
        self.cboAreaUnits.addItems(["Hectare", "Dunum"])
        myUnitsRow.addWidget(self.cboAreaUnits)
        myForm.addRow("Common land", myUnitsRow)

        self.cboEnergyType = QComboBox(self)
        self.cboEnergyType.setObjectName("cboEnergyType")
        self.cboEnergyType.addItems(["KCalories", "TDN"])
        self.cboEnergyType.setToolTip("Energy unit of the specific grazing land food value.")
        myForm.addRow("Land energy unit", self.cboEnergyType)
        myLayout.addLayout(myForm)

        self.cbLivePreview = QCheckBox("Recalculate the diet while I change inputs", self)
        self.cbLivePreview.setObjectName("cbLivePreview")
        self.cbLivePreview.setChecked(True)
        myLayout.addWidget(self.cbLivePreview)

        self.pbnDeveloperConsole = QPushButton("Developer console…", self)
        self.pbnDeveloperConsole.setObjectName("pbnDeveloperConsole")
        self.pbnDeveloperConsole.setToolTip("Show the debug log with per-component filters.")
        myLayout.addWidget(self.pbnDeveloperConsole)

        self.sbPrecision.valueChanged.connect(lambda v: self._set(self.mController.setPrecision, v))
        self.sbCommonLandValue.valueChanged.connect(lambda _v: self._pushCommonLand())
        self.cboAreaUnits.currentIndexChanged.connect(lambda _i: self._pushCommonLand())
        self.cboEnergyType.currentIndexChanged.connect(self._onEnergyTypeChanged)
        self.cbLivePreview.toggled.connect(self.mController.setLivePreview)
        self.pbnDeveloperConsole.clicked.connect(self._openDeveloperConsole)
        self.loadFromController()

    def _set(self, theSetter, theValue) -> None:
        if not self._mLoading:
            theSetter(theValue)

    def _pushCommonLand(self) -> None:
        if self._mLoading:
            return
        myUnits = AreaUnits.Dunum if self.cboAreaUnits.currentText() == "Dunum" else AreaUnits.Hectare
        self.mController.setCommonLandValue(self.sbCommonLandValue.value(), myUnits)

    def _onEnergyTypeChanged(self, _index: int) -> None:
        if self._mLoading:
            return
        myType = EnergyType.TDN if self.cboEnergyType.currentText() == "TDN" else EnergyType.KCalories
        self.mController.setSpecificLandEnergyType(myType)

    def _openDeveloperConsole(self) -> None:
        from la.gui.ladebugdialog import LaDebugDialog
        LaUtils.debug.setEnabled(True)
        myDialog = LaDebugDialog.get_instance(self.window())
        myDialog.show()
        myDialog.raise_()

    def loadFromController(self) -> None:
        myModel = self.mController.mModel
        self._mLoading = True
        try:
            self.sbPrecision.setValue(int(myModel.mPrecision or 5))
            self.sbCommonLandValue.setValue(float(myModel.mCommonLandValue or 0.0))
            self.cboAreaUnits.setCurrentText("Dunum" if myModel.mCommonLandAreaUnits == AreaUnits.Dunum else "Hectare")
            self.cboEnergyType.setCurrentText("TDN" if myModel.mSpecificLandEnergyType == EnergyType.TDN else "KCalories")
            self.cbLivePreview.setChecked(self.mController.mLivePreview)
        finally:
            self._mLoading = False
