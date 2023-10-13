import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication, QFile
from la.gui.lamainform import LanduseAnalyst

# the following two imports should be enabled if splashscreen is enabled
# from qgis.PyQt.QtWidgets import QSplashScreen
# from qgis.PyQt.QtGui import QPixmap

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # NOTE: make sure these lines stay after app init above
    QCoreApplication.setOrganizationName("linfiniti.com")
    QCoreApplication.setOrganizationDomain("landuseanalyst.linfiniti.com")
    QCoreApplication.setApplicationName("LanduseAnalyst")

    # for windows lets use plastique style!
    if sys.platform == 'win32':
        app.setStyle('plastique')

    # Install OpenDocuments AppleEvent handler after application object is initialized
    # but before any other event handling (including dialogs or splash screens) occurs.
    # If an OpenDocuments event has been created before the application was launched,
    # it must be handled before some other event handler runs and dismisses it as unknown.
    # If run at startup, the handler will set either or both of myProjectFileName and myFileList.
    # AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments, openDocumentsAEHandler, 0, false);
    if sys.platform == 'darwin':
        # If the QtCore framework is bundled with the application, clear the library search path
        # and look for Qt plugins only within the application bundle.
        bundledQtCore = QCoreApplication.applicationDirPath() + "/lib/QtCore.framework"
        if QFile.exists(bundledQtCore):
            QCoreApplication.setLibraryPaths([QCoreApplication.applicationDirPath()])

    # dont display the splash on first run...
    # mySettings = QSettings()
    # if mySettings.value("firstRun/firstRun", True, type=bool) == False:
    #     myPixmap = QPixmap(":/zintatu_logo.png")
    #     mypSplash = QSplashScreen(myPixmap)
    #     myMaskPixmap = QPixmap(":/zintatu_logo_mask.png").createHeuristicMask()
    #     myMaskPixmap.setThreshold(0.5)
    #     mypSplash.setMask(myMaskPixmap)
    #     mypSplash.show()

    #     mypZintatu = ZintatuForm()
    #     mypZintatu.show()
    #     mypSplash.finish(mypZintatu)
    #     del mypSplash
    #     # note if the widget does not inherit qdialog
    #     # (as in the case of our main window)
    #     # you must call app exec!
    # else:
    #     mypZintatu = ZintatuForm()
    #     mypZintatu.show()
    ''
    mypForm = LanduseAnalyst()
    mypForm.show()
    sys.exit(app.exec_())