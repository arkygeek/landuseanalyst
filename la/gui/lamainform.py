# FILEPATH: /Users/arkygeek/dev/QGisPlugins/landuseanalyst/cppArchive/src/gui/lamainform.cpp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QSpinBox, QLineEdit, QRadioButton,\
                          QCheckBox, QTextBrowser, QProgressBar, QPushButton,\
                          QComboBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from typing import Dict, Tuple, List
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils
from la.lib.laanimal import LaAnimal
from la.lib.lacrop import LaCrop
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacropparameter import LaCropParameter
from la.lib.ladietlabels import LaDietLabels
from la.gui.lamodelreports import LaModelReport


from la.ui.lamainformbase import LaMainFormBase
from la.gui.lamainform import LaMainForm
from la.lib.version import VERSION
# class LaMainForm(QMainWindow, LaMainFormBase):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

class LaMainForm(QMainWindow, LaMainFormBase):
  def __init__(self, parent=None):
    super().__init__(parent)
    # self.setWindowTitle("Land Use Analyst")
    # self.setGeometry(100, 100, 800, 600)
    self.setupUi(self)
    self.myModel = LaModel()
    self.mAnimalsMap = {}
    self.mCropsMap = {}
    self.initUI()

  def initUI(self):
    # create widgets
    self.sbPopulation = QSpinBox(self)
    self.sbPopulation.setRange(1, 1000000)
    self.sbPopulation.setValue(1000)
    self.lineEditPeriod = QLineEdit(self)
    self.lineEditEasting = QLineEdit(self)
    self.lineEditNorthing = QLineEdit(self)
    self.radioButtonEuclidean = QRadioButton("Euclidean Distance", self)
    self.radioButtonWalkingTime = QRadioButton("Walking Time", self)
    self.radioButtonPathDistance = QRadioButton("Path Distance", self)
    self.sbModelPrecision = QSpinBox(self)
    self.sbModelPrecision.setRange(1, 100)
    self.sbModelPrecision.setValue(10)
    self.labelCropCheck = QLabel("100%", self)
    self.labelAnimalCheck = QLabel("100%", self)
    self.cboxBaseOnPlants = QCheckBox("Base on Plants", self)
    self.cboxIncludeDairy = QCheckBox("Include Dairy", self)
    self.tbReport = QTextBrowser(self)
    self.lblAnimalPicCalcs = QLabel(self)
    self.textBrowserResultsAnimals = QTextBrowser(self)
    self.progressBarCalcs = QProgressBar(self)
    self.tbLogs = QTextBrowser(self)
    self.textBrowserAnimalDefinition = QWebEngineView(self)
    self.textBrowserCropDefinition = QWebEngineView(self)
    self.btnCalculate = QPushButton("Calculate", self)
    self.btnCalculate.clicked.connect(self.calculate)
    self.btnPrintCropsAndAnimals = QPushButton("Print Crops and Animals", self)
    self.btnPrintCropsAndAnimals.clicked.connect(self.printCropsAndAnimals)

    # set widget positions and sizes
    self.sbPopulation.setGeometry(20, 20, 100, 20)
    self.lineEditPeriod.setGeometry(20, 50, 100, 20)
    self.lineEditEasting.setGeometry(20, 80, 100, 20)
    self.lineEditNorthing.setGeometry(20, 110, 100, 20)
    self.radioButtonEuclidean.setGeometry(20, 140, 150, 20)
    self.radioButtonWalkingTime.setGeometry(20, 170, 150, 20)
    self.radioButtonPathDistance.setGeometry(20, 200, 150, 20)
    self.sbModelPrecision.setGeometry(20, 230, 100, 20)
    self.labelCropCheck.setGeometry(20, 260, 100, 20)
    self.labelAnimalCheck.setGeometry(20, 290, 100, 20)
    self.cboxBaseOnPlants.setGeometry(20, 320, 150, 20)
    self.cboxIncludeDairy.setGeometry(20, 350, 150, 20)
    self.tbReport.setGeometry(20, 380, 400, 200)
    self.lblAnimalPicCalcs.setGeometry(450, 20, 300, 200)
    self.textBrowserResultsAnimals.setGeometry(450, 230, 300, 200)
    self.progressBarCalcs.setGeometry(20, 590, 400, 20)
    self.tbLogs.setGeometry(450, 440, 300, 170)
    self.textBrowserAnimalDefinition.setGeometry(20, 440, 400, 170)
    self.textBrowserCropDefinition.setGeometry(20, 440, 400, 170)
    self.btnCalculate.setGeometry(20, 520, 100, 30)
    self.btnPrintCropsAndAnimals.setGeometry(20, 560, 150, 30)

    # set widget properties
    self.tbReport.setReadOnly(True)
    self.tbLogs.setReadOnly(True)
    self.textBrowserAnimalDefinition.setHtml("")
    self.textBrowserCropDefinition.setHtml("")

    # set layout
    self.tbReport.moveCursor(self.tbReport.textCursor().End)
    self.tbLogs.moveCursor(self.tbLogs.textCursor().End)

  def calculate(self):
    self.myModel.setPopulation(self.sbPopulation.value())
    self.myModel.setPeriod(self.lineEditPeriod.text())
    self.myModel.setEasting(int(self.lineEditEasting.text()))
    self.myModel.setNorthing(int(self.lineEditNorthing.text()))
    self.myModel.setEuclideanDistance(self.radioButtonEuclidean.isChecked())
    self.myModel.setWalkingTime(self.radioButtonWalkingTime.isChecked())
    self.myModel.setPathDistance(self.radioButtonPathDistance.isChecked())
    self.myModel.setPrecision(self.sbModelPrecision.value())

    if self.labelCropCheck.text() != "100%" or self.labelAnimalCheck.text() != "100%":
      return
    else:
      if self.cboxBaseOnPlants.isChecked():
        if self.cboxIncludeDairy.isChecked():
          self.myDietLabels = self.myModel.doCalcsPlantsFirstIncludeDairy()
        else:
          self.myDietLabels = self.myModel.doCalcsPlantsFirstDairySeperate()
      else:
        if self.cboxIncludeDairy.isChecked():
          self.myDietLabels = self.myModel.doCalcsAnimalsFirstIncludeDiary()
        else:
          self.myDietLabels = self.myModel.doCalcsAnimalsFirstDairySeparate()

    self.tbReport.setHtml(self.myModel.toHtml())

    myGuid = self.thepCurrentItem.data(Qt.UserRole)
    myAnimal = LaUtils.getAnimal(myGuid)
    self.lblAnimalPicCalcs.setPixmap(QPixmap(myAnimal.imageFile()))
    myCalcsMap = self.myModel.calcsAnimalsMap()
    myReportPair: Tuple[str, float]
    myReportMap: LaReportMap = self.myDietLabels.animalCalcsReportMap()
    myReportPair = myReportMap.value(myGuid)
    myReportString = myReportPair.first
    self.textBrowserResultsAnimals.setText(myReportString)
    self.progressBarCalcs.setMaximum(100)

  def printCropsAndAnimals(self):
    self.tbReport.clear()
    myAnimalIterator = iter(self.mAnimalsMap)
    while True:
      try:
        myAnimalGuid = next(myAnimalIterator)
        myPair = self.mAnimalsMap[myAnimalGuid]
        mySelectedFlag = myPair[0]
        myAnimalParameterGuid = myPair[1]
        myText = "Animal <" + myAnimalGuid.toLocal8Bit() + " , <"
        mySelectedFlag ? myText += "true," : myText += "false,"
        myText += myAnimalParameterGuid.toLocal8Bit()
        myText += "> >"
        self.tbLogs.append(myText)
      except StopIteration:
        break

    myCropIterator = iter(self.mCropsMap)
    while True:
      try:
        myCropGuid = next(myCropIterator)
        myPair = self.mCropsMap[myCropGuid]
        mySelectedFlag = myPair[0]
        myCropParameterGuid = myPair[1]
        myText = "Crop <" + myCropGuid.toLocal8Bit() + " , <"
        mySelectedFlag ? myText += "true," : myText += "false,"
        myText += myCropParameterGuid.toLocal8Bit()
        myText += "> >"
        self.tbLogs.append(myText)
      except StopIteration:
        break

  def logMessage(self, theMessage: str):
    self.tbLogs.append(theMessage)
    self.tbLogs.ensureCursorVisible()

  def showAnimalDefinitionReport(self, theAnimal: LaAnimal, theAnimalParameter: LaAnimalParameter):
    myHtml = "<body>"
    myHtml += "<table width=\"100%\">"
    myHtml += "<tr>"
    myHtml += "<td>"
    myHtml += theAnimal.toHtml()
    myHtml += "</td>"
    myHtml += "<td>"
    myHtml += theAnimalParameter.toHtml()
    myHtml += "</td>"
    myHtml += "</tr>"
    myHtml += "</table>"
    myHtml += "</body>"
    self.textBrowserAnimalDefinition.setHtml(myHtml)

  def showCropDefinitionReport(self, theCrop: LaCrop, theCropParameter: LaCropParameter):
    myHtml = "<body>"
    myHtml += "<table width=\"100%\">"
    myHtml += "<tr>"
    myHtml += "<td>"
    myHtml += theCrop.toHtml()
    myHtml += "</td>"
    myHtml += "<td>"
    myHtml += theCropParameter.toHtml()
    myHtml += "</td>"
    myHtml += "</tr>"
    myHtml += "</table>"
    myHtml += "</body>"
    self.textBrowserCropDefinition.setHtml(myHtml)






















# from PyQt5.QtCore import Qt, QSettings, QTranslator, QCoreApplication
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QAction, QMainWindow, QFileDialog, QMessageBox

# from la.ui.lamainformbase import LaMainFormBase
# from la.gui.lacropmanager import LaCropManager


# class LaMainForm(QMainWindow, LaMainFormBase):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

#         # Initialize the crop manager
#         self.cropManager = LaCropManager(self)

#         # Set up the menu actions
#         self.actionNew.triggered.connect(self.newFile)
#         self.actionOpen.triggered.connect(self.openFile)
#         self.actionSave.triggered.connect(self.saveFile)
#         self.actionSaveAs.triggered.connect(self.saveFileAs)
#         self.actionPreferences.triggered.connect(self.showPreferences)
#         self.actionAbout.triggered.connect(self.showAbout)

#         # Set up the toolbar actions
#         self.actionNewToolbar.triggered.connect(self.newFile)
#         self.actionOpenToolbar.triggered.connect(self.openFile)
#         self.actionSaveToolbar.triggered.connect(self.saveFile)

#         # Set up the status bar
#         self.statusBar().showMessage("Ready")

#         # Set up the window icon
#         self.setWindowIcon(QIcon(":/icons/landuseanalyst.png"))

#         # Set up the settings
#         self.settings = QSettings("Linfiniti", "LandUseAnalyst")
#         self.loadSettings()

#     def newFile(self):
#         # TODO: Implement new file functionality
#         pass

#     def openFile(self):
#         # TODO: Implement open file functionality
#         pass

#     def saveFile(self):
#         # TODO: Implement save file functionality
#         pass

#     def saveFileAs(self):
#         # TODO: Implement save file as functionality
#         pass

#     def showPreferences(self):
#         preferences = LaPreferences(self)
#         preferences.exec_()
#         self.loadSettings()

#     def showAbout(self):
#         about = LaAbout(self)
#         about.exec_()

#     def closeEvent(self, event):
#         # Save the settings
#         self.saveSettings()

#         # Confirm exit
#         reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?",
#                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()

#     def loadSettings(self):
#         # Load the language settings
#         language = self.settings.value("language", "en")
#         translator = QTranslator()
#         translator.load(f":/translations/landuseanalyst_{language}.qm")
#         QCoreApplication.installTranslator(translator)

#     def saveSettings(self):
#         # Save the language settings
#         language = QCoreApplication.translate("LaMainForm", "English")
#         if QCoreApplication.translate("LaMainForm", "French") in self.languageComboBox.currentText():
#             language = "fr"
#         self.settings.setValue("language", language)

# """

# LaMainForm class is rewritten in Python using PyQt5.

# The necessary imports are included, including QAction, QFileDialog, QMessageBox,
#     QMainWindow, QSettings, QTranslator, QCoreApplication, QIcon, and the
#     Ui_LaMainFormBase class generated by Qt Designer.

# The LaMainForm class defines the necessary methods for managing the main form,
#     including __init__, newFile, openFile, saveFile, saveFileAs, showPreferences,
#     showAbout, closeEvent, loadSettings, and saveSettings.  These methods are
#     used to manage the main form, including the menu actions, toolbar actions,
#     status bar, window icon, settings, and language translations.

# """