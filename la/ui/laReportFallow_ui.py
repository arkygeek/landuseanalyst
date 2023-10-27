# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laReportFallow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTableWidget, QTableWidgetItem, QWidget)

class Ui_ModelTargets(object):
    def setupUi(self, ModelTargets):
        if not ModelTargets.objectName():
            ModelTargets.setObjectName(u"ModelTargets")
        ModelTargets.resize(529, 217)
        self.gridLayout = QGridLayout(ModelTargets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbnClose = QPushButton(ModelTargets)
        self.pbnClose.setObjectName(u"pbnClose")

        self.gridLayout.addWidget(self.pbnClose, 1, 3, 1, 1)

        self.pbnExport = QPushButton(ModelTargets)
        self.pbnExport.setObjectName(u"pbnExport")

        self.gridLayout.addWidget(self.pbnExport, 1, 1, 1, 1)

        self.pbnPrint = QPushButton(ModelTargets)
        self.pbnPrint.setObjectName(u"pbnPrint")

        self.gridLayout.addWidget(self.pbnPrint, 1, 2, 1, 1)

        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 1)

        self.splitter = QSplitter(ModelTargets)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.tblFallow = QTableWidget(self.splitter)
        if (self.tblFallow.columnCount() < 5):
            self.tblFallow.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblFallow.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblFallow.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblFallow.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblFallow.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblFallow.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblFallow.setObjectName(u"tblFallow")
        self.tblFallow.setAlternatingRowColors(True)
        self.tblFallow.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblFallow.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.splitter.addWidget(self.tblFallow)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 4)


        self.retranslateUi(ModelTargets)
        self.pbnClose.clicked.connect(ModelTargets.close)
        self.pbnClose.clicked.connect(ModelTargets.close)

        QMetaObject.connectSlotsByName(ModelTargets)
    # setupUi

    def retranslateUi(self, ModelTargets):
        ModelTargets.setWindowTitle(QCoreApplication.translate("ModelTargets", u"Model Targets", None))
        self.pbnClose.setText(QCoreApplication.translate("ModelTargets", u"Close", None))
        self.pbnExport.setText(QCoreApplication.translate("ModelTargets", u"Export", None))
        self.pbnPrint.setText(QCoreApplication.translate("ModelTargets", u"Print", None))
        ___qtablewidgetitem = self.tblFallow.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ModelTargets", u"Crop", None));
        ___qtablewidgetitem1 = self.tblFallow.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ModelTargets", u"Area Available", None));
        ___qtablewidgetitem2 = self.tblFallow.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ModelTargets", u"Animal", None));
        ___qtablewidgetitem3 = self.tblFallow.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ModelTargets", u"Allocated", None));
        ___qtablewidgetitem4 = self.tblFallow.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ModelTargets", u"New Target", None));
#if QT_CONFIG(tooltip)
        self.tblFallow.setToolTip(QCoreApplication.translate("ModelTargets", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a crop here to see and/or edit it's properties below.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblFallow.setWhatsThis(QCoreApplication.translate("ModelTargets", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model any crop, several details must be entered to define specific varieties. Crop Manager asks for general information about the crop in this section. You might want to have more than one strain of the same variety, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different strains of the same variety is quite easy. Let's say you want to have two kinds of wheat for example. The Name: field is Wheat for both, but in Notes: field, enter Hard Red for one, and Soft White for the other. The"
                        "n adjust the other parameters as you wish. Even though the name is the same, the crop is saved uniquely.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

