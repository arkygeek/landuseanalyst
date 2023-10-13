from PyQt5.QtCore import Qt, QSettings, QTranslator, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMainWindow

from .gui.lacropmanager import LaCropManager
# from landuse_analyst import LaPreferencess
from .gui.lamodelreport import LaModelReports


class LaMainForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the user interface from Designer.
        self.setupUi()

        # Set up the crop manager.
        self.cropManager = LaCropManager(self)
        self.cropManagerDockWidget.setWidget(self.cropManager)

        # Set up the preferences dialog.
        self.preferences = LaPreferences(self)

        # Set up the model reports dialog.
        self.modelReports = LaModelReports(self)

        # Set up the actions.
        self.actionPreferences.triggered.connect(self.showPreferences)
        self.actionModelReports.triggered.connect(self.showModelReports)

        # Set up the settings.
        self.settings = QSettings("LaTools", "LaFarm")

        # Set up the translator.
        self.translator = QTranslator()
        self.translator.load("LaFarm_" + QLocale.system().name(),
                             QCoreApplication.applicationDirPath())
        QCoreApplication.installTranslator(self.translator)

        # Set up the icon.
        self.setWindowIcon(QIcon(":/icons/LaFarm.png"))

    def setupUi(self):
        # Set up the user interface from Designer.
        pass

    def showPreferences(self):
        self.preferences.exec_()

    def showModelReports(self):
        self.modelReports.exec_()

    def closeEvent(self, event):
        # Save the settings.
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())

        super().closeEvent(event)