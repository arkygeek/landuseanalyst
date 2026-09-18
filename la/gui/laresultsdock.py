"""
laresultsdock.py — the right-hand "LA Results" dock.

Summary tiles (live), charts and tables (after Calculate), catchment run
tiles, exports and the embedded help. Manual tag A7.
"""

import os
from typing import List, Optional

from qgis.PyQt.QtCore import QDir, QFile, QIODevice, Qt, QTextStream
from qgis.PyQt.QtWidgets import (
    QApplication, QFileDialog, QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSplitter, QTabWidget, QTextBrowser, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,
)
from qgis.gui import QgsDockWidget

from la.gui.lascenariocontroller import LaScenarioController
from la.lib.lacatchment import SearchStatus
from la.lib.lautils import LaUtils

_TILE_STYLE = """
QFrame#laTile { border: 1px solid palette(mid); border-radius: 6px; background: palette(base); }
QFrame#laTileAccent { border: 1px solid #3B5A8C; border-radius: 6px; background: palette(base); }
QLabel#laTileTitle { color: palette(mid); font-size: 11px; }
QLabel#laTileValue { font-size: 18px; font-weight: 600; }
QLabel#laTileSub { color: palette(mid); font-size: 11px; }
"""


class LaResultsDock(QgsDockWidget):
    """Results column of the Landuse Analyst workspace."""

    def __init__(self, theController: LaScenarioController, parent: Optional[QWidget] = None) -> None:
        super().__init__("LA Results", parent)
        self.setObjectName("LaResultsDock")
        self.mController = theController
        self._mTiles: List[QWidget] = []

        myContent = QWidget(self)
        myContent.setStyleSheet(_TILE_STYLE)
        myLayout = QVBoxLayout(myContent)
        myLayout.setContentsMargins(6, 6, 6, 6)
        myLayout.setSpacing(6)

        myToolbar = QHBoxLayout()
        self.lblInputsEcho = QLabel(myContent)
        self.lblInputsEcho.setObjectName("lblInputsEcho")
        self.lblInputsEcho.setWordWrap(True)
        self.lblInputsEcho.setStyleSheet("QLabel { color: palette(mid); }")
        myToolbar.addWidget(self.lblInputsEcho, 1)
        self.pbnCopyJson = self._button("pbnCopyJson", "Copy JSON", "Copy the results as JSON to the clipboard.", myToolbar)
        self.pbnSaveJson = self._button("pbnSaveJson", "Save JSON…", "Save the results as a JSON file.", myToolbar)
        self.pbnExportPdf = self._button("pbnExportPdf", "PDF…", "Export the full report (tables + charts) as PDF.", myToolbar)
        myLayout.addLayout(myToolbar)

        self.tabs = QTabWidget(myContent)
        self.tabs.setObjectName("tabsResults")

        mySummaryScroll = QScrollArea(self.tabs)
        mySummaryScroll.setWidgetResizable(True)
        mySummaryScroll.setFrameShape(QFrame.NoFrame)
        self.summaryWidget = QWidget(mySummaryScroll)
        mySummaryLayout = QVBoxLayout(self.summaryWidget)
        self.tilesLayout = QGridLayout()
        self.tilesLayout.setSpacing(6)
        mySummaryLayout.addLayout(self.tilesLayout)
        self.lblCatchmentHeading = QLabel("<b>Catchment runs</b>", self.summaryWidget)
        self.lblCatchmentHeading.hide()
        mySummaryLayout.addWidget(self.lblCatchmentHeading)
        self.catchmentTilesLayout = QGridLayout()
        self.catchmentTilesLayout.setSpacing(6)
        mySummaryLayout.addLayout(self.catchmentTilesLayout)
        self.summaryText = QTextBrowser(self.summaryWidget)
        self.summaryText.setObjectName("textSummary")
        self.summaryText.setOpenExternalLinks(True)
        self.summaryText.setMinimumHeight(160)
        mySummaryLayout.addWidget(self.summaryText, 1)
        mySummaryScroll.setWidget(self.summaryWidget)
        self.tabs.addTab(mySummaryScroll, "Summary")

        self.chartsView = QTextBrowser(self.tabs)
        self.chartsView.setObjectName("textCharts")
        self.tabs.addTab(self.chartsView, "Charts")
        self.tablesView = QTextBrowser(self.tabs)
        self.tablesView.setObjectName("textTables")
        self.tabs.addTab(self.tablesView, "Tables")
        self.tabs.addTab(self._buildHelpTab(), "Help")
        myLayout.addWidget(self.tabs, 1)
        self.setWidget(myContent)

        self.pbnCopyJson.clicked.connect(self._onCopyJson)
        self.pbnSaveJson.clicked.connect(self._onSaveJson)
        self.pbnExportPdf.clicked.connect(self._onExportPdf)
        theController.dietChanged.connect(self._onDietChanged)
        theController.calculationFinished.connect(self._onCalculationFinished)
        theController.catchmentFinished.connect(self._onCatchmentFinished)
        theController.settingsChanged.connect(self._updateEcho)
        self._onDietChanged(theController.mLastLabels)
        self._setExportsEnabled(False)

    def _button(self, theName: str, theText: str, theTip: str, theLayout: QHBoxLayout) -> QPushButton:
        myButton = QPushButton(theText, self)
        myButton.setObjectName(theName)
        myButton.setToolTip(theTip)
        theLayout.addWidget(myButton)
        return myButton

    def _setExportsEnabled(self, theFlag: bool) -> None:
        for myButton in (self.pbnCopyJson, self.pbnSaveJson, self.pbnExportPdf):
            myButton.setEnabled(theFlag)

    # ------------------------------------------------------------------
    # Tiles
    # ------------------------------------------------------------------
    @staticmethod
    def _clearLayout(theLayout: QGridLayout) -> None:
        while theLayout.count():
            myItem = theLayout.takeAt(0)
            if myItem.widget() is not None:
                myItem.widget().deleteLater()

    def _tile(self, theTitle: str, theValue: str, theSub: str = "", theAccent: bool = False) -> QFrame:
        myFrame = QFrame(self.summaryWidget)
        myFrame.setObjectName("laTileAccent" if theAccent else "laTile")
        myLayout = QVBoxLayout(myFrame)
        myLayout.setContentsMargins(8, 6, 8, 6)
        myLayout.setSpacing(1)
        myTitle = QLabel(theTitle, myFrame)
        myTitle.setObjectName("laTileTitle")
        myValue = QLabel(theValue, myFrame)
        myValue.setObjectName("laTileValue")
        myValue.setTextInteractionFlags(Qt.TextSelectableByMouse)
        myLayout.addWidget(myTitle)
        myLayout.addWidget(myValue)
        if theSub:
            mySub = QLabel(theSub, myFrame)
            mySub.setObjectName("laTileSub")
            mySub.setWordWrap(True)
            myLayout.addWidget(mySub)
        return myFrame

    def _onDietChanged(self, theLabels) -> None:
        self._clearLayout(self.tilesLayout)
        self._updateEcho()
        if theLabels is None:
            myHint = QLabel(
                "Set the population, diet and at least one crop or animal, then press Calculate.\n"
                "The tiles update live once the inputs are complete.", self.summaryWidget)
            myHint.setWordWrap(True)
            myHint.setStyleSheet("QLabel { color: palette(mid); }")
            self.tilesLayout.addWidget(myHint, 0, 0, 1, 2)
            self.summaryText.setHtml("")
            self._setExportsEnabled(False)
            return
        myModel = self.mController.mModel
        myCropHa = sum(myModel.mAreaTargetsCropsMap.values())
        myGrazingHa = sum(myModel.mAreaTargetsAnimalsMap.values())
        myTiles = [
            ("Total land needed", f"{myCropHa + myGrazingHa:,.1f} Ha", "cropland + grazing land"),
            ("Settlement energy", f"{float(theLabels.megaCaloriesSettlementAnnual):,.0f} MCal/yr",
             f"{float(theLabels.kiloCaloriesIndividualAnnual):,.0f} kcal per person per year"),
            ("Cropland", f"{myCropHa:,.1f} Ha", f"{len(myModel.mAreaTargetsCropsMap)} crops"),
            ("Grazing land", f"{myGrazingHa:,.1f} Ha", f"{len(myModel.mAreaTargetsAnimalsMap)} animals"),
            ("Domestic crops", f"{float(theLabels.cropMCalories):,.0f} MCal",
             f"{float(theLabels.cropsPortionPct):.1f} % of the diet"),
            ("Domestic meat", f"{float(theLabels.animalMCalories):,.0f} MCal",
             f"{float(theLabels.tameMeatPortionPct):.1f} % of the diet"),
            ("Dairy", f"{float(theLabels.dairyMCalories):,.0f} MCal",
             f"{float(theLabels.dairyPortionPct):.1f} % of the diet"
             + (f" · surplus {float(theLabels.dairySurplusMCalories):,.0f} MCal"
                if float(theLabels.dairySurplusMCalories or 0) > 0 else "")),
            ("Wild foods", f"{float(theLabels.wildAnimalMCalories) + float(theLabels.wildPlantsMCalories):,.0f} MCal",
             f"{float(theLabels.wildAnimalPortionPct) + float(theLabels.wildPlantsPortionPct):.1f} % of the diet"),
        ]
        for myIndex, (myTitle, myValue, mySub) in enumerate(myTiles):
            self.tilesLayout.addWidget(self._tile(myTitle, myValue, mySub, theAccent=myIndex == 0), myIndex // 2, myIndex % 2)
        self._setExportsEnabled(True)

    def _updateEcho(self) -> None:
        myModel = self.mController.mModel
        myParts = [p for p in (myModel.mName, myModel.mPeriod) if p]
        myParts.append(f"pop {myModel.mPopulation:,}")
        myParts.append(f"animal share {myModel.mDietPercent} %")
        myParts.append(f"dairy {myModel.mDairyUtilisation} %")
        self.lblInputsEcho.setText(" · ".join(myParts))

    def _onCalculationFinished(self, theCalculationType: str) -> None:
        self.summaryText.setHtml(self.mController.reportHtml(theIncludeCharts=False))
        self.tablesView.setHtml(self.mController.tablesHtml())
        self.chartsView.setHtml(self.mController.chartsHtml())
        self.tabs.setCurrentIndex(0)
        self.setUserVisible(True)
        self.raise_()

    def _onCatchmentFinished(self, theSuccess: bool, theText: str) -> None:
        self._clearLayout(self.catchmentTilesLayout)
        myResults = self.mController.mLastCatchmentResults
        if not theSuccess or myResults is None:
            self.lblCatchmentHeading.setVisible(not theSuccess)
            if not theSuccess:
                myLabel = QLabel(theText, self.summaryWidget)
                myLabel.setWordWrap(True)
                myLabel.setStyleSheet("QLabel { color: #a33a2a; }")
                self.catchmentTilesLayout.addWidget(myLabel, 0, 0, 1, 2)
            return
        self.lblCatchmentHeading.show()
        for myIndex, myItem in enumerate(myResults.items):
            myStatus = {SearchStatus.Converged: "converged", SearchStatus.Failed: "did not converge",
                        SearchStatus.Skipped: "skipped"}.get(myItem.status, str(myItem.status))
            mySub = f"target {myItem.targetHa:,.1f} Ha · {myStatus} · threshold {myItem.threshold:,.0f} s"
            if myItem.message:
                mySub += f"\n{myItem.message}"
            self.catchmentTilesLayout.addWidget(
                self._tile(myItem.itemName, f"{myItem.achievedHa:,.1f} Ha", mySub,
                           theAccent=myItem.status is SearchStatus.Converged),
                myIndex // 2, myIndex % 2)

    # ------------------------------------------------------------------
    # Exports
    # ------------------------------------------------------------------
    def _onCopyJson(self) -> None:
        if not self.mController.hasResults():
            return
        QApplication.clipboard().setText(self.mController.reportJson())
        LaUtils.debug.log("Results JSON copied to clipboard", "Setup")

    def _onSaveJson(self) -> None:
        if not self.mController.hasResults():
            return
        myPath, _ = QFileDialog.getSaveFileName(
            self, "Save results as JSON", self.mController.defaultExportFilename("json"), "JSON files (*.json)")
        if myPath:
            self.mController.exportJson(myPath)

    def _onExportPdf(self) -> None:
        if not self.mController.hasResults():
            return
        myPath, _ = QFileDialog.getSaveFileName(
            self, "Export report as PDF", self.mController.defaultExportFilename("pdf"), "PDF files (*.pdf)")
        if myPath:
            self.mController.exportPdf(myPath)

    # ------------------------------------------------------------------
    # Help (the 102 embedded field descriptions)
    # ------------------------------------------------------------------
    def _buildHelpTab(self) -> QWidget:
        mySplitter = QSplitter(Qt.Vertical, self.tabs)
        self.treeHelp = QTreeWidget(mySplitter)
        self.treeHelp.setObjectName("treeHelp")
        self.treeHelp.setHeaderHidden(True)
        self.textHelp = QTextBrowser(mySplitter)
        self.textHelp.setObjectName("textHelp")
        self.textHelp.setHtml("<p>Select a topic above. Each entry explains one input field.</p>")
        mySplitter.addWidget(self.treeHelp)
        mySplitter.addWidget(self.textHelp)
        mySplitter.setStretchFactor(1, 1)
        myGroups = {}
        for myName in sorted(QDir(":/").entryList(["*.html"], QDir.Files)):
            myTitle = os.path.splitext(myName)[0]
            myGroupName = myTitle.split(" ")[0] if " " in myTitle else "General"
            myGroup = myGroups.get(myGroupName)
            if myGroup is None:
                myGroup = QTreeWidgetItem(self.treeHelp, [myGroupName])
                myGroups[myGroupName] = myGroup
            myItem = QTreeWidgetItem(myGroup, [myTitle])
            myItem.setData(0, Qt.UserRole, ":/" + myName)
        self.treeHelp.currentItemChanged.connect(self._onHelpItemChanged)
        return mySplitter

    def _onHelpItemChanged(self, theCurrent: QTreeWidgetItem, _thePrevious) -> None:
        if theCurrent is None:
            return
        myPath = theCurrent.data(0, Qt.UserRole)
        if not myPath:
            return
        myFile = QFile(myPath)
        if myFile.open(QIODevice.ReadOnly | QIODevice.Text):
            self.textHelp.setHtml(QTextStream(myFile).readAll())
            myFile.close()
        else:
            self.textHelp.setHtml(f"<p>Could not open help topic {myPath}</p>")
