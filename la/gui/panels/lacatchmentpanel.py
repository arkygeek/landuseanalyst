"""Catchment search section: DEM, suitability rasters, seed and distance method. Manual tags A4, A6."""

from typing import Optional

from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import (
    QButtonGroup, QCheckBox, QComboBox, QFormLayout, QHBoxLayout, QLabel, QRadioButton, QToolButton,
    QVBoxLayout, QWidget,
)
from qgis.core import Qgis, QgsMapLayerProxyModel, QgsPointXY, QgsRasterLayer
from qgis.gui import QgsCollapsibleGroupBox, QgsDoubleSpinBox, QgsMapLayerComboBox, QgsMessageBar, QgsSpinBox

from la.gui.lascenariocontroller import LaScenarioController
from la.lib.lacatchment import DistanceMethod, LaCatchmentInputs


class LaCatchmentPanel(QgsCollapsibleGroupBox):
    """
    Optional GIS step. The group box's check box gates the whole block, as the
    web app's "Run catchment after diet calc" toggle does.

    :signal pickSeedToggled(bool): the user pressed / released "Pick on map".
    """

    pickSeedToggled = pyqtSignal(bool)

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__("Catchment search (optional)", parent)
        self.setObjectName("grpCatchment")
        self.setCheckable(True)
        self.setChecked(False)
        self.setSaveCheckedState(True)
        self.setSaveCollapsedState(True)
        self.setSettingGroup("landuseAnalyst/panels")
        self.setToolTip("When checked, Calculate also solves the walking-cost catchment for every selected item.")
        self.mController = theController
        self._mLoading = False

        myLayout = QVBoxLayout(self)
        self.messageBar = QgsMessageBar(self)
        myLayout.addWidget(self.messageBar)

        myForm = QFormLayout()
        myForm.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.cboDem = self._rasterCombo("cboDem", "Digital elevation model the walking cost is derived from.", False)
        myForm.addRow("DEM", self.cboDem)
        self.cboCommonCrop = self._rasterCombo(
            "cboCommonCrop", "Suitability raster (1 = suitable) for crops that use common land.", True)
        myForm.addRow("Common crop land", self.cboCommonCrop)
        self.cboCommonGrazing = self._rasterCombo(
            "cboCommonGrazing", "Suitability raster (1 = suitable) for animals that use common grazing.", True)
        myForm.addRow("Common grazing", self.cboCommonGrazing)
        myLayout.addLayout(myForm)

        mySeedRow = QHBoxLayout()
        self.sbEasting = self._coordinateSpin("sbEasting", "Settlement easting in the DEM's CRS.")
        self.sbNorthing = self._coordinateSpin("sbNorthing", "Settlement northing in the DEM's CRS.")
        mySeedRow.addWidget(QLabel("Seed", self))
        mySeedRow.addWidget(self.sbEasting, 1)
        mySeedRow.addWidget(self.sbNorthing, 1)
        self.pbnPickSeed = QToolButton(self)
        self.pbnPickSeed.setObjectName("pbnPickSeed")
        self.pbnPickSeed.setText("⌖ Pick on map")
        self.pbnPickSeed.setCheckable(True)
        self.pbnPickSeed.setToolTip("Click the settlement location on the map canvas (Esc to stop).")
        mySeedRow.addWidget(self.pbnPickSeed)
        myLayout.addLayout(mySeedRow)
        self.lblCrs = QLabel(self)
        self.lblCrs.setObjectName("lblSeedCrs")
        self.lblCrs.setStyleSheet("QLabel { color: palette(mid); }")
        myLayout.addWidget(self.lblCrs)

        myMethodRow = QHBoxLayout()
        myMethodRow.addWidget(QLabel("Distance", self))
        self.radioWalkingTime = QRadioButton("Walking time (Tobler)", self)
        self.radioWalkingTime.setObjectName("radioWalkingTime")
        self.radioWalkingTime.setChecked(True)
        self.radioWalkingTime.setToolTip("Anisotropic walking time from Tobler's hiking function over the DEM.")
        self.radioEuclidean = QRadioButton("Euclidean", self)
        self.radioEuclidean.setObjectName("radioEuclidean")
        self.radioEuclidean.setToolTip("Straight-line distance (needs the GRASS provider until the pure-Python port lands).")
        self.mMethodGroup = QButtonGroup(self)
        self.mMethodGroup.addButton(self.radioWalkingTime)
        self.mMethodGroup.addButton(self.radioEuclidean)
        myMethodRow.addWidget(self.radioWalkingTime)
        myMethodRow.addWidget(self.radioEuclidean)
        myMethodRow.addStretch()
        myLayout.addLayout(myMethodRow)

        self.cbApplySlopeLimits = QCheckBox("Apply each item's preferred slope band", self)
        self.cbApplySlopeLimits.setObjectName("cbApplySlopeLimits")
        self.cbApplySlopeLimits.setChecked(True)
        self.cbApplySlopeLimits.setToolTip(
            "Intersect every suitability raster with the slope band from the crop / animal parameter set "
            "(thesis: 9° crops, 15° grazing). Untick to reproduce runs made before slope limits existed.")
        myLayout.addWidget(self.cbApplySlopeLimits)
        self.cbSlopeOnly = QCheckBox("Items without a suitability raster use the slope band alone", self)
        self.cbSlopeOnly.setObjectName("cbSlopeOnlySuitability")
        self.cbSlopeOnly.setToolTip("Lets a scenario run anywhere with only a DEM: suitable land = cells inside the slope band.")
        myLayout.addWidget(self.cbSlopeOnly)
        self.cbSplitFallow = QCheckBox("Split cropland into sown and fallow masks", self)
        self.cbSplitFallow.setObjectName("cbSplitFallow")
        self.cbSplitFallow.setChecked(True)
        self.cbSplitFallow.setToolTip("Search the cultivated area and the total cropland separately; fallow = total − sown.")
        myLayout.addWidget(self.cbSplitFallow)

        myAdvancedRow = QHBoxLayout()
        myAdvancedRow.addWidget(QLabel("Window", self))
        self.sbWindowPixels = QgsSpinBox(self)
        self.sbWindowPixels.setObjectName("sbWindowPixels")
        self.sbWindowPixels.setRange(0, 1500)
        self.sbWindowPixels.setSingleStep(50)
        self.sbWindowPixels.setSpecialValueText("auto")
        self.sbWindowPixels.setSuffix(" cells")
        self.sbWindowPixels.setToolTip(
            "Working window around the seed, in DEM cells. Auto = sized from the land targets and widened "
            "when a catchment reaches the edge. Cap 1500 (≈630 MB of memory).")
        myAdvancedRow.addWidget(self.sbWindowPixels)
        myAdvancedRow.addWidget(QLabel("Engine", self))
        self.cboEngine = QComboBox(self)
        self.cboEngine.setObjectName("cboEngine")
        self.cboEngine.addItem("Pure Python (scipy)", "pure")
        self.cboEngine.addItem("GRASS r.walk / r.cost", "grass")
        self.cboEngine.setToolTip("Pure Python matches the web version exactly and supports windows, slope bands and barriers. "
                                  "GRASS is the legacy path; it falls back to pure Python for anything GRASS lacks.")
        myAdvancedRow.addWidget(self.cboEngine, 1)
        myLayout.addLayout(myAdvancedRow)

        self.cboDem.layerChanged.connect(self._onDemChanged)
        self.cboCommonCrop.layerChanged.connect(lambda _l: self.validate())
        self.cboCommonGrazing.layerChanged.connect(lambda _l: self.validate())
        self.sbEasting.valueChanged.connect(self._onSeedEdited)
        self.sbNorthing.valueChanged.connect(self._onSeedEdited)
        self.pbnPickSeed.toggled.connect(self.pickSeedToggled)
        self.toggled.connect(lambda _c: self.validate())
        self.loadFromController()
        self._onDemChanged(self.cboDem.currentLayer())

    # ------------------------------------------------------------------
    def _rasterCombo(self, theName: str, theTip: str, theAllowEmpty: bool) -> QgsMapLayerComboBox:
        myCombo = QgsMapLayerComboBox(self)
        myCombo.setObjectName(theName)
        myCombo.setFilters(QgsMapLayerProxyModel.RasterLayer)
        myCombo.setAllowEmptyLayer(theAllowEmpty)
        if theAllowEmpty:
            myCombo.setLayer(None)   # default to "none", not the first raster in the project
        myCombo.setToolTip(theTip)
        return myCombo

    def _coordinateSpin(self, theName: str, theTip: str) -> QgsDoubleSpinBox:
        mySpin = QgsDoubleSpinBox(self)
        mySpin.setObjectName(theName)
        mySpin.setRange(-1e8, 1e8)
        mySpin.setDecimals(1)
        mySpin.setClearValue(0.0)
        mySpin.setToolTip(theTip)
        mySpin.setKeyboardTracking(False)
        return mySpin

    def demLayer(self) -> Optional[QgsRasterLayer]:
        myLayer = self.cboDem.currentLayer()
        return myLayer if isinstance(myLayer, QgsRasterLayer) else None

    def demCrs(self):
        myLayer = self.demLayer()
        return myLayer.crs() if myLayer is not None else None

    def method(self) -> DistanceMethod:
        return DistanceMethod.Euclidean if self.radioEuclidean.isChecked() else DistanceMethod.WalkingTime

    def gisInputs(self) -> Optional[LaCatchmentInputs]:
        """Inputs for the catchment task, or None when the section is off / has no DEM."""
        if not self.isChecked():
            return None
        myDem = self.demLayer()
        if myDem is None:
            return None
        myCrop = self.cboCommonCrop.currentLayer()
        myGrazing = self.cboCommonGrazing.currentLayer()
        return LaCatchmentInputs(
            demLayerId=myDem.id(),
            commonCropLayerId=myCrop.id() if myCrop is not None else None,
            commonGrazingLayerId=myGrazing.id() if myGrazing is not None else None,
            method=self.method(),
            windowPixels=self.sbWindowPixels.value() or None,
            applySlopeLimits=self.cbApplySlopeLimits.isChecked(),
            useSlopeOnlySuitability=self.cbSlopeOnly.isChecked(),
            splitFallow=self.cbSplitFallow.isChecked(),
            engine=self.cboEngine.currentData() or "pure",
        )

    def optionsBlock(self) -> dict:
        """Catchment options for the scenario file's plugin block."""
        return {
            "windowPixels": int(self.sbWindowPixels.value()),
            "applySlopeLimits": self.cbApplySlopeLimits.isChecked(),
            "useSlopeOnlySuitability": self.cbSlopeOnly.isChecked(),
            "splitFallow": self.cbSplitFallow.isChecked(),
            "engine": self.cboEngine.currentData() or "pure",
        }

    def applyOptionsBlock(self, theBlock: dict) -> None:
        if "windowPixels" in theBlock:
            self.sbWindowPixels.setValue(int(theBlock.get("windowPixels") or 0))
        if "applySlopeLimits" in theBlock:
            self.cbApplySlopeLimits.setChecked(bool(theBlock["applySlopeLimits"]))
        if "useSlopeOnlySuitability" in theBlock:
            self.cbSlopeOnly.setChecked(bool(theBlock["useSlopeOnlySuitability"]))
        if "splitFallow" in theBlock:
            self.cbSplitFallow.setChecked(bool(theBlock["splitFallow"]))
        myIndex = self.cboEngine.findData(theBlock.get("engine", "pure"))
        if myIndex >= 0:
            self.cboEngine.setCurrentIndex(myIndex)

    def setSeed(self, theX: float, theY: float) -> None:
        """Set the seed (DEM CRS) from the map tool and push it to the controller."""
        self._mLoading = True
        try:
            self.sbEasting.setValue(theX)
            self.sbNorthing.setValue(theY)
        finally:
            self._mLoading = False
        self._pushSeed()

    def loadFromController(self) -> None:
        myModel = self.mController.mModel
        self._mLoading = True
        try:
            self.sbEasting.setValue(float(myModel.mEasting))
            self.sbNorthing.setValue(float(myModel.mNorthing))
        finally:
            self._mLoading = False

    # ------------------------------------------------------------------
    def _onDemChanged(self, theLayer) -> None:
        myCrs = self.demCrs()
        self.lblCrs.setText(f"Seed coordinates in {myCrs.authid()} ({myCrs.description()})"
                            if myCrs is not None and myCrs.isValid() else "Pick a DEM to define the seed CRS.")
        self.validate()

    def _onSeedEdited(self, _value) -> None:
        if not self._mLoading:
            self._pushSeed()

    def _pushSeed(self) -> None:
        myCrs = self.demCrs()
        myEpsg = 0
        if myCrs is not None and myCrs.isValid() and myCrs.authid().upper().startswith("EPSG:"):
            try:
                myEpsg = int(myCrs.authid().split(":")[1])
            except ValueError:
                myEpsg = 0
        self.mController.setSettlement(self.sbEasting.value(), self.sbNorthing.value(), myEpsg)
        self.validate()

    def validate(self) -> Optional[str]:
        """Show inline warnings for common mistakes. Returns the blocking problem, if any."""
        self.messageBar.clearWidgets()
        if not self.isChecked():
            return None
        myDem = self.demLayer()
        if myDem is None:
            myText = "Pick a DEM layer, or untick this section to run the diet calculation only."
            self.messageBar.pushMessage(myText, Qgis.Warning, 0)
            return myText
        mySeed = QgsPointXY(self.sbEasting.value(), self.sbNorthing.value())
        if not myDem.extent().contains(mySeed):
            myText = "The seed lies outside the DEM extent — check the coordinates or pick it on the map."
            self.messageBar.pushMessage(myText, Qgis.Warning, 0)
            return myText
        for myCombo, myLabel in ((self.cboCommonCrop, "common crop"), (self.cboCommonGrazing, "common grazing")):
            myLayer = myCombo.currentLayer()
            if myLayer is not None and myLayer.crs() != myDem.crs():
                self.messageBar.pushMessage(
                    f"The {myLabel} raster is in {myLayer.crs().authid()} but the DEM is in "
                    f"{myDem.crs().authid()}; results will be wrong unless they are aligned.",
                    Qgis.Warning, 0)
        return None
