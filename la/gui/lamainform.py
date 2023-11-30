# Standard library imports
from typing import Tuple

# Third-party imports
from qgis.PyQt.QtCore import Qt, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import (QAction, QComboBox, QLabel, QLineEdit, QMainWindow, QSlider, QSpinBox,
                                 QTextBrowser,
                                 QTextEdit, QTreeWidget, QMessageBox)

# Local application/library specific imports
# from lib.la import La
from la.resources_rc import *


from la.ui.lamainformbase import LaMainFormBase
# from la.ui.lacropparameterbase import LaCropParameterManagerBase

from la.lib.lautils import LaUtils

from la.lib.laanimal import LaAnimal
from la.lib.laanimalparameter import LaAnimalParameter
from la.lib.lacrop import LaCrop
from la.lib.lacropparameter import LaCropParameter
from la.lib.lamodel import LaModel
from la.lib.lautils import LaUtils
from la.lib.la import La

class LaMainForm(QMainWindow):
  def __init__(self, iface):
      super().__init__()
      self.iface = iface
      self.myModel = LaModel()
      self.mAnimalsMap = {}
      self.mCropsMap = {}
      self.menu = None  # Define the menu attribute
      self.initGUI()
      # self.setupUi(self)
      # Set up the menu actions
      self.actionNew.triggered.connect(self.newFile)
      self.actionOpen.triggered.connect(self.openFile)
      self.actionSave.triggered.connect(self.saveFile)
      self.actionSaveAs.triggered.connect(self.saveFileAs)
      self.actionPreferences.triggered.connect(self.showPreferences)
      self.actionAbout.triggered.connect(self.showAbout)

      # Set up the toolbar actions
      self.actionNewToolbar.triggered.connect(self.newFile)
      self.actionOpenToolbar.triggered.connect(self.openFile)
      self.actionSaveToolbar.triggered.connect(self.saveFile)

      # Set up the status bar
      self.statusBar().showMessage("Ready")

      # Set up the window icon
      self.setWindowIcon(QIcon(":/icons/landuseanalyst.png"))

      # Set up the settings
      # self.settings = QSettings("Linfiniti", "LandUseAnalyst")
      self.loadSettings()

  def initGUI(self):
    # create widgets
    self.cbAreaUnits = QComboBox(self)
    self.treeWidget = QTreeWidget(self)
    self.treeWidget.setHeaderLabels(["Parameter", "Value"])
    self.treeWidget.setColumnWidth(0, 200)
    self.treeWidget.setColumnWidth(1, 100)
    self.cbAreaUnits.addItem("Dunum")
    self.cbAreaUnits.addItem("Hectare")
    self.cbCommonLandEnergyType = QComboBox(self)
    self.cbCommonLandEnergyType.addItem("KCalories")
    self.cbCommonLandEnergyType.addItem("TDN")
    self.sliderDiet = QSlider(Qt.Horizontal, self)
    self.sliderDiet.setRange(0, 100)
    self.sliderDiet.setValue(50)
    self.sliderMeat = QSlider(Qt.Horizontal, self)
    self.sliderMeat.setRange(0, 100)
    self.sliderMeat.setValue(50)
    self.sliderCrop = QSlider(Qt.Horizontal, self)
    self.sliderCrop.setRange(0, 100)
    self.sliderCrop.setValue(50)
    self.sliderDiet.valueChanged.connect(self.on_sliderDiet_valueChanged)
    self.sliderMeat.valueChanged.connect(self.on_sliderMeat_valueChanged)
    self.sliderCrop.valueChanged.connect(self.on_sliderCrop_valueChanged)
    self.treeWidget.currentItemChanged.connect(self.current_item_changed)

    self.sbPopulation = QSpinBox(self)
    self.sbPopulation.setRange(1, 1000000)
    self.sbPopulation.setValue(1000)
    self.lineEditPeriod = QLineEdit(self)

    # create actions
    self.actionNew = QAction("New", self)
    self.actionNew.setShortcut("Ctrl+N")
    self.actionNew.triggered.connect(self.newFile)

    # set widget properties
    self.tbReport = QTextEdit(self)
    self.tbReport.setReadOnly(True)
    self.tbLogs = QTextEdit(self)
    self.tbLogs.setReadOnly(True)
    self.textBrowserAnimalDefinition = QTextBrowser(self)
    self.textBrowserAnimalDefinition.setHtml("")
    self.textBrowserCropDefinition = QTextBrowser(self)
    self.textBrowserCropDefinition.setHtml("")

    # set layout
    self.tbReport.moveCursor(self.tbReport.textCursor().End)
    self.tbLogs.moveCursor(self.tbLogs.textCursor().End)

  def on_sliderDiet_valueChanged(self, value):
    myMinString = str(value)
    myMaxString = str(100 - value)
    self.labelMeatPercent = QLabel(self)
    self.labelMeatPercent.setText(myMinString)
    self.labelCropPercent = QLabel(self)
    self.labelCropPercent.setText(myMaxString)
    self.setDietLabels()

  def on_sbDailyCalories_valueChanged(self, theValue):
    self.setDietLabels()

  def on_cboxIncludeDairy_clicked(self, theBool):
    self.setDietLabels()

  def on_sbLimitDairyPercent_valueChanged(self, theValue):
    self.setDietLabels()

  def on_cboxBaseOnPlants_clicked(self, theBool):
    self.setDietLabels()

  def on_cboxLimitDairy_clicked(self, theBool):
    self.setDietLabels()

  def on_sliderMeat_valueChanged(self, theValue):
    myMinString = str(100 - theValue)
    myMaxString = str(theValue)
    self.labelMeatWildPercent.setText(myMinString)
    self.labelMeatTamePercent.setText(myMaxString)
    self.setDietLabels()

  def on_sliderDiet_valueChanged(self, theValue):
    myMinString = str(theValue)
    myMaxString = str(100 - theValue)
    self.labelMeatPercent.setText(myMinString)
    self.labelCropPercent.setText(myMaxString)
    self.setDietLabels()

  def on_sbDairyUtilisation_valueChanged(self, theValue):
    self.setDietLabels()

  def on_sliderCrop_valueChanged(self, theValue):
    myMinString = str(100 - theValue)
    myMaxString = str(theValue)
    self.labelCropWildPercent.setText(myMinString)
    self.labelCropTamePercent.setText(myMaxString)
    self.setDietLabels()




  def current_item_changed(self, current, previous):
    # TODO: Implement current_item_changed functionality
    pass

  def on_sliderMeat_valueChanged(self, value):
    # TODO: Implement slider value changed functionality
    pass

  def on_sliderCrop_valueChanged(self, value):
    # TODO: Implement slider value changed functionality
    pass

  def newFile(self):
    # TODO: Implement new file functionality
    pass

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
    myReportMap: La.LaReportMap = self.myDietLabels.animalCalcsReportMap()
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
        if mySelectedFlag:
          myText += "true,"
        else:
          myText += "false,"
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
        if mySelectedFlag:
          myText += "true,"
        else:
          myText += "false,"
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


  def openFile(self):
      # TODO: Implement open file functionality
      pass

  def saveFile(self):
      # TODO: Implement save file functionality
      pass

  def saveFileAs(self):
      # TODO: Implement save file as functionality
      pass

  # def showPreferences(self):
  #     preferences = LaPreferences(self)
  #     preferences.exec_()
  #     self.loadSettings()

  # def showAbout(self):
  #     about = LaAbout(self)
  #     about.exec_()

  def closeEvent(self, event):
      # Save the settings
      self.saveSettings()

      # Confirm exit
      reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if reply == QMessageBox.Yes:
          event.accept()
      else:
          event.ignore()

  def loadSettings(self):
      # Load the language settings
      language = self.settings.value("language", "en")
      translator = QTranslator()
      translator.load(f":/translations/landuseanalyst_{language}.qm")
      QCoreApplication.installTranslator(translator)

  def saveSettings(self):
    # Save the language settings
    language = QCoreApplication.translate("LaMainForm", "English")
    if QCoreApplication.translate("LaMainForm", "French") in self.languageComboBox.currentText():
        language = "fr"
    self.settings.setValue("language", language)





  # noinspection PyMethodMayBeStatic
  def tr(self, message):
      """Get the translation for a string using Qt translation API.

      We implement this ourselves since we do not inherit QObject.

      :param message: String for translation.
      :type message: str, QString

      :returns: Translated version of message.
      :rtype: QString
      """
      # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
      return QCoreApplication.translate('LanduseAnalyst', message)


  def add_action(
      self,
      icon_path,
      text,
      callback,
      enabled_flag=True,
      add_to_menu=True,
      add_to_toolbar=True,
      status_tip=None,
      whats_this=None,
      parent=None):
      """Add a toolbar icon to the toolbar.

      :param icon_path: Path to the icon for this action. Can be a resource
          path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
      :type icon_path: str

      :param text: Text that should be shown in menu items for this action.
      :type text: str

      :param callback: Function to be called when the action is triggered.
      :type callback: function

      :param enabled_flag: A flag indicating if the action should be enabled
          by default. Defaults to True.
      :type enabled_flag: bool

      :param add_to_menu: Flag indicating whether the action should also
          be added to the menu. Defaults to True.
      :type add_to_menu: bool

      :param add_to_toolbar: Flag indicating whether the action should also
          be added to the toolbar. Defaults to True.
      :type add_to_toolbar: bool

      :param status_tip: Optional text to show in a popup when mouse pointer
          hovers over the action.
      :type status_tip: str

      :param parent: Parent widget for the new action. Defaults None.
      :type parent: QWidget

      :param whats_this: Optional text to show in the status bar when the
          mouse pointer hovers over the action.

      :returns: The action that was created. Note that the action is also
          added to self.actions list.
      :rtype: QAction
      """

      icon = QIcon(icon_path)
      action = QAction(icon, text, parent)
      action.triggered.connect(callback)
      action.setEnabled(enabled_flag)

      if status_tip is not None:
          action.setStatusTip(status_tip)

      if whats_this is not None:
          action.setWhatsThis(whats_this)

      if add_to_toolbar:
          # Adds plugin icon to Plugins toolbar
          self.iface.addToolBarIcon(action)

      if add_to_menu:
          self.iface.addPluginToMenu(
              self.menu,
              action)

      self.actions.append(action)

      return action

  def initGui(self):
      """Create the menu entries and toolbar icons inside the QGIS GUI."""

      icon_path = ':/la_icon_small.png'
      self.add_action(
          icon_path,
          text=self.tr(u'Model archaeological site'),
          callback=self.run,
          parent=self.iface.mainWindow())

      # will be set False in run()
      self.first_start = True


  def unload(self):
      """Removes the plugin menu item and icon from QGIS GUI."""
      for action in self.actions:
          self.iface.removePluginMenu(
              self.tr(u'&Landuse Analyst'),
              action)
          self.iface.removeToolBarIcon(action)


  def run(self):
      """Run method that performs all the real work"""

      # Create the dialog with elements (after translation) and keep reference
      # Only create GUI ONCE in callback, so that it will only load when the plugin is started
      if self.first_start == True:
          self.first_start = False
          self.dlg = LaMainFormBase()

      # show the dialog
      self.dlg.show()
      # Run the dialog event loop
      result = self.dlg.exec_()
      # See if OK was pressed
      if result:
          # Do something useful here - delete the line containing pass and
          # substitute with your code.
          print("thisIsOutput")
          pass















# from qgis.PyQt.QtCore import Qt, QSettings, QTranslator, QCoreApplication
# from qgis.PyQt.QtGui import QIcon
# from qgis.PyQt.QtWidgets import QAction, QMainWindow, QFileDialog, QMessageBox

# from ui.lamainformbase import LaMainFormBase
# from gui.lacropmanager import LaCropManager


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