"""Population & diet section with live donut. Manual tags A2, B1, B2."""

from typing import Optional

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QCheckBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel, QSlider, QVBoxLayout, QWidget,
)
from qgis.gui import QgsCollapsibleGroupBox, QgsSpinBox

from la.gui.lascenariocontroller import LaScenarioController
from la.gui.widgets.ladietdonut import LaDietDonut


class LaDietPanel(QgsCollapsibleGroupBox):
    """Population, calories, the four diet sliders and dairy options."""

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__("Population & diet", parent)
        self.setObjectName("grpPopulationDiet")
        self.setSaveCollapsedState(True)
        self.setSettingGroup("landuseAnalyst/panels")
        self.mController = theController
        self._mLoading = False

        myLayout = QVBoxLayout(self)
        myForm = QFormLayout()
        myForm.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.sbPopulation = QgsSpinBox(self)
        self.sbPopulation.setObjectName("sbPopulation")
        self.sbPopulation.setRange(1, 10_000_000)
        self.sbPopulation.setToolTip("Number of people the settlement must feed for a year.")
        myForm.addRow("Population", self.sbPopulation)
        self.sbDailyCalories = QgsSpinBox(self)
        self.sbDailyCalories.setObjectName("sbDailyCalories")
        self.sbDailyCalories.setRange(500, 6000)
        self.sbDailyCalories.setSingleStep(50)
        self.sbDailyCalories.setSuffix(" kcal")
        self.sbDailyCalories.setToolTip("Daily energy requirement per person (thesis: 2500 kcal).")
        myForm.addRow("Per person / day", self.sbDailyCalories)
        myLayout.addLayout(myForm)

        myGrid = QGridLayout()
        myGrid.setColumnStretch(1, 1)
        self.sliderAnimalShare = self._addSlider(
            myGrid, 0, "sliderAnimalShare", "Animal share of diet",
            "Share of all calories that comes from animals (meat and dairy). Thesis: 10 / 20 / 30 %.")
        self.sliderTameMeat = self._addSlider(
            myGrid, 1, "sliderTameMeat", "Domestic meat (vs wild)",
            "Share of meat calories from herded animals rather than hunting. Thesis: 99 %.")
        self.sliderDomesticCrops = self._addSlider(
            myGrid, 2, "sliderDomesticCrops", "Domestic crops (vs wild plants)",
            "Share of plant calories from cultivated crops rather than gathering. Thesis: 90 %.")
        self.sliderDairyUtilisation = self._addSlider(
            myGrid, 3, "sliderDairyUtilisation", "Dairy utilisation",
            "How much of the herds' potential milk is consumed. Thesis: 0 / 50 / 100 %.")
        myLayout.addLayout(myGrid)

        myDairyRow = QHBoxLayout()
        self.cbIncludeDairy = QCheckBox("Dairy counts toward the meat share", self)
        self.cbIncludeDairy.setObjectName("cbIncludeDairy")
        self.cbIncludeDairy.setToolTip(
            "Checked: 'Animals First, Include Dairy' — dairy calories are part of the animal share.\n"
            "Unchecked: 'Animals First, Dairy Separate' — the thesis method, dairy is added on top.")
        myDairyRow.addWidget(self.cbIncludeDairy)
        myLayout.addLayout(myDairyRow)

        myLimitRow = QHBoxLayout()
        self.cbLimitDairy = QCheckBox("Cap dairy at", self)
        self.cbLimitDairy.setObjectName("cbLimitDairy")
        self.sbLimitDairyPercent = QgsSpinBox(self)
        self.sbLimitDairyPercent.setObjectName("sbLimitDairyPercent")
        self.sbLimitDairyPercent.setRange(0, 100)
        self.sbLimitDairyPercent.setSuffix(" % of diet")
        myLimitRow.addWidget(self.cbLimitDairy)
        myLimitRow.addWidget(self.sbLimitDairyPercent)
        myLimitRow.addStretch()
        myLayout.addLayout(myLimitRow)

        self.cbBaseOnPlants = QCheckBox("Plants first (calculation not implemented yet)", self)
        self.cbBaseOnPlants.setObjectName("cbBaseOnPlants")
        self.cbBaseOnPlants.setToolTip(
            "The C++ original allocated land to crops before animals in this mode. The port "
            "falls back to Animals First and says so in the report.")
        myLayout.addWidget(self.cbBaseOnPlants)

        self.donut = LaDietDonut(self)
        self.donut.setObjectName("donutDiet")
        myLayout.addWidget(self.donut)

        self.sbPopulation.valueChanged.connect(lambda v: self._set(self.mController.setPopulation, v))
        self.sbDailyCalories.valueChanged.connect(lambda v: self._set(self.mController.setCaloriesPerPersonDaily, v))
        self.sliderAnimalShare.valueChanged.connect(lambda v: self._set(self.mController.setAnimalShareOfDiet, v))
        self.sliderTameMeat.valueChanged.connect(lambda v: self._set(self.mController.setTameMeatPercent, v))
        self.sliderDomesticCrops.valueChanged.connect(lambda v: self._set(self.mController.setDomesticCropPercent, v))
        self.sliderDairyUtilisation.valueChanged.connect(lambda v: self._set(self.mController.setDairyUtilisation, v))
        self.cbIncludeDairy.toggled.connect(lambda v: self._set(self.mController.setIncludeDairy, v))
        self.cbLimitDairy.toggled.connect(self._onLimitDairyToggled)
        self.sbLimitDairyPercent.valueChanged.connect(lambda v: self._set(self.mController.setLimitDairyPercent, v))
        self.cbBaseOnPlants.toggled.connect(lambda v: self._set(self.mController.setBaseOnPlants, v))
        self.mController.dietChanged.connect(self.donut.setLabels)
        self.loadFromController()

    def _addSlider(self, theGrid: QGridLayout, theRow: int, theName: str, theLabel: str, theTip: str) -> QSlider:
        myLabel = QLabel(theLabel, self)
        mySlider = QSlider(Qt.Horizontal, self)
        mySlider.setObjectName(theName)
        mySlider.setRange(0, 100)
        mySlider.setToolTip(theTip)
        myValue = QLabel("0 %", self)
        myValue.setObjectName(theName + "Value")
        myValue.setMinimumWidth(42)
        myValue.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        mySlider.valueChanged.connect(lambda v, lbl=myValue: lbl.setText(f"{v} %"))
        theGrid.addWidget(myLabel, theRow, 0)
        theGrid.addWidget(mySlider, theRow, 1)
        theGrid.addWidget(myValue, theRow, 2)
        return mySlider

    def _set(self, theSetter, theValue) -> None:
        if not self._mLoading:
            theSetter(theValue)

    def _onLimitDairyToggled(self, theChecked: bool) -> None:
        self.sbLimitDairyPercent.setEnabled(theChecked)
        self._set(self.mController.setLimitDairy, theChecked)

    def loadFromController(self) -> None:
        """Push the model's current values into the widgets without echoing them back."""
        myModel = self.mController.mModel
        self._mLoading = True
        try:
            self.sbPopulation.setValue(int(myModel.mPopulation))
            self.sbDailyCalories.setValue(int(myModel.mCaloriesPerPersonDaily))
            self.sliderAnimalShare.setValue(int(myModel.mDietPercent))
            self.sliderTameMeat.setValue(int(myModel.mMeatPercent))
            self.sliderDomesticCrops.setValue(int(myModel.mPercentOfDietThatIsFromCrops))
            self.sliderDairyUtilisation.setValue(int(myModel.mDairyUtilisation))
            self.cbIncludeDairy.setChecked(bool(myModel.mIncludeDairy))
            self.cbLimitDairy.setChecked(bool(myModel.mLimitDairy))
            self.sbLimitDairyPercent.setValue(int(myModel.mLimitDairyPercentage))
            self.sbLimitDairyPercent.setEnabled(bool(myModel.mLimitDairy))
            self.cbBaseOnPlants.setChecked(bool(myModel.mBaseOnPlants))
        finally:
            self._mLoading = False
