"""
lasettingsdock.py — the left-hand "Landuse Analyst" dock.

Scenario header, an accordion of collapsible sections (diet, agriculture,
catchment, advanced) inside a scroll area, and a sticky footer with the
Calculate button. Everything binds to one :class:`LaScenarioController`.
"""

from typing import Optional

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QFrame, QScrollArea, QVBoxLayout, QWidget
from qgis.core import Qgis, QgsCoordinateTransform, QgsPointXY, QgsProject
from qgis.gui import QgsDockWidget

from la.gui.lascenariocontroller import LaScenarioController
from la.gui.panels.laadvancedpanel import LaAdvancedPanel
from la.gui.panels.laagriculturepanel import LaAgriculturePanel
from la.gui.panels.lacatchmentpanel import LaCatchmentPanel
from la.gui.panels.ladietpanel import LaDietPanel
from la.gui.panels.lafooterpanel import LaFooterPanel
from la.gui.panels.lascenarioheaderpanel import LaScenarioHeaderPanel
from la.lib.lautils import LaUtils


class LaSettingsDock(QgsDockWidget):
    """
    Settings column of the Landuse Analyst workspace.

    :param theController: Shared scenario controller.
    :param theIface: ``QgisInterface`` (None in tests; disables the map tool
        and message-bar notifications).
    """

    def __init__(self, theController: LaScenarioController, theIface=None, parent: Optional[QWidget] = None) -> None:
        super().__init__("Landuse Analyst", parent)
        self.setObjectName("LaSettingsDock")
        self.mController = theController
        self.mIface = theIface
        self.mSeedTool = None

        myContent = QWidget(self)
        myLayout = QVBoxLayout(myContent)
        myLayout.setContentsMargins(0, 0, 0, 0)
        myLayout.setSpacing(0)

        self.header = LaScenarioHeaderPanel(theController, myContent)
        myLayout.addWidget(self.header)
        myLayout.addWidget(self._separator(myContent))

        self.scrollArea = QScrollArea(myContent)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        mySections = QWidget(self.scrollArea)
        mySectionsLayout = QVBoxLayout(mySections)
        mySectionsLayout.setContentsMargins(6, 6, 6, 6)
        mySectionsLayout.setSpacing(6)
        self.dietPanel = LaDietPanel(theController, mySections)
        self.agriculturePanel = LaAgriculturePanel(theController, mySections)
        self.catchmentPanel = LaCatchmentPanel(theController, mySections)
        self.advancedPanel = LaAdvancedPanel(theController, mySections)
        for myPanel in (self.dietPanel, self.agriculturePanel, self.catchmentPanel, self.advancedPanel):
            mySectionsLayout.addWidget(myPanel)
        mySectionsLayout.addStretch(1)
        self.scrollArea.setWidget(mySections)
        myLayout.addWidget(self.scrollArea, 1)

        myLayout.addWidget(self._separator(myContent))
        self.footer = LaFooterPanel(myContent)
        myLayout.addWidget(self.footer)
        self.setWidget(myContent)

        theController.settingsChanged.connect(self.updateSummary)
        theController.selectionChanged.connect(self.updateSummary)
        theController.readinessChanged.connect(self.footer.setReady)
        theController.calculationFinished.connect(self._onCalculationFinished)
        theController.calculationFailed.connect(self._onCalculationFailed)
        theController.catchmentStarted.connect(lambda: self.footer.setBusy("Building the walking-cost surface…"))
        theController.catchmentProgress.connect(self._onCatchmentProgress)
        theController.catchmentMessage.connect(self._onCatchmentMessage)
        theController.catchmentFinished.connect(self._onCatchmentFinished)
        theController.modelReplaced.connect(self._onModelReplaced)
        self.footer.pbnCalculate.clicked.connect(self.onCalculate)
        self.footer.pbnCancel.clicked.connect(theController.cancelCatchment)
        self.catchmentPanel.pickSeedToggled.connect(self._onPickSeedToggled)

        self.updateSummary()
        myReady, myReason = theController.readiness()
        self.footer.setReady(myReady, myReason)

    @staticmethod
    def _separator(theParent: QWidget) -> QFrame:
        myLine = QFrame(theParent)
        myLine.setFrameShape(QFrame.HLine)
        myLine.setFrameShadow(QFrame.Sunken)
        return myLine

    # ------------------------------------------------------------------
    # Summary + readiness
    # ------------------------------------------------------------------
    def updateSummary(self) -> None:
        myModel = self.mController.mModel
        myParts = [
            f"{len(self.mController.mSelectedCrops)} crops",
            f"{len(self.mController.mSelectedAnimals)} animals",
            f"{myModel.mPopulation:,} people",
            f"{myModel.mDietPercent} % animal share",
        ]
        if self.catchmentPanel.isChecked():
            myParts.append("catchment on")
        self.footer.setSummary(" · ".join(myParts))

    # ------------------------------------------------------------------
    # Calculate
    # ------------------------------------------------------------------
    def onCalculate(self) -> None:
        """Run the diet calculation and, if the catchment section is on, the GIS step."""
        myGisInputs = None
        if self.catchmentPanel.isChecked():
            myProblem = self.catchmentPanel.validate()
            if myProblem:
                self._notify(myProblem, Qgis.Warning)
                return
            myGisInputs = self.catchmentPanel.gisInputs()
        self.mController.setGisInputs(myGisInputs)
        if not self.mController.runFullCalculation():
            myReady, myReason = self.mController.readiness()
            if not myReady:
                self._notify(myReason, Qgis.Warning)

    def _onCalculationFinished(self, theCalculationType: str) -> None:
        self.footer.setIdle(f"Calculated — {theCalculationType}")

    def _onCalculationFailed(self, theMessage: str) -> None:
        self.footer.setIdle("Calculation failed: " + theMessage)
        self._notify("Calculation failed: " + theMessage, Qgis.Critical)

    def _onCatchmentProgress(self, theDone: int, theIteration: int, theMaximum: int) -> None:
        if theMaximum > 0:
            self.footer.setProgress(theIteration, theMaximum,
                                    f"Catchment search — iteration {theIteration}/{theMaximum}")
        elif theDone >= 0:
            self.footer.setProgress(0, 0, f"Catchment search — {theDone} item(s) done")

    def _onCatchmentMessage(self, theMessage: str) -> None:
        LaUtils.debug.log(theMessage, "Calculation")
        myText = str(theMessage).strip()
        if myText.startswith("[") and "]" in myText:
            myText = myText.split("]", 1)[1].strip()
        if myText:
            self.footer.lblStage.setText(myText[:160])

    def _onCatchmentFinished(self, theSuccess: bool, theText: str) -> None:
        self.footer.setIdle(theText)
        self._notify(theText, Qgis.Success if theSuccess else Qgis.Warning)

    def _onModelReplaced(self) -> None:
        for myPanel in (self.header, self.dietPanel, self.catchmentPanel, self.advancedPanel):
            myPanel.loadFromController()
        self.agriculturePanel.cropList.rebuild()
        self.agriculturePanel.animalList.rebuild()
        self.updateSummary()

    def _notify(self, theText: str, theLevel) -> None:
        if self.mIface is not None:
            self.mIface.messageBar().pushMessage("Landuse Analyst", theText, theLevel, 6)
        else:
            LaUtils.debug.log(theText, "MainForm")

    # ------------------------------------------------------------------
    # Seed picking on the canvas
    # ------------------------------------------------------------------
    def _onPickSeedToggled(self, theChecked: bool) -> None:
        if self.mIface is None:
            self.catchmentPanel.pbnPickSeed.setChecked(False)
            return
        myCanvas = self.mIface.mapCanvas()
        if theChecked:
            if self.mSeedTool is None:
                from la.gui.lamaptools import LaSeedMapTool
                self.mSeedTool = LaSeedMapTool(myCanvas)
                self.mSeedTool.seedPicked.connect(self._onSeedPicked)
                self.mSeedTool.deactivatedTool.connect(
                    lambda: self.catchmentPanel.pbnPickSeed.setChecked(False))
            myCanvas.setMapTool(self.mSeedTool)
        elif self.mSeedTool is not None and myCanvas.mapTool() is self.mSeedTool:
            myCanvas.unsetMapTool(self.mSeedTool)

    def _onSeedPicked(self, theCanvasPoint: QgsPointXY) -> None:
        myPoint = QgsPointXY(theCanvasPoint)
        myDemCrs = self.catchmentPanel.demCrs()
        myCanvasCrs = self.mIface.mapCanvas().mapSettings().destinationCrs()
        if myDemCrs is not None and myDemCrs.isValid() and myCanvasCrs.isValid() and myDemCrs != myCanvasCrs:
            try:
                myPoint = QgsCoordinateTransform(myCanvasCrs, myDemCrs, QgsProject.instance()).transform(myPoint)
            except Exception as e:
                self._notify(f"Could not transform the clicked point into the DEM CRS: {e}", Qgis.Warning)
                return
        self.catchmentPanel.setSeed(myPoint.x(), myPoint.y())
        self.catchmentPanel.pbnPickSeed.setChecked(False)
