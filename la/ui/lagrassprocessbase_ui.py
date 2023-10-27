# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lagrassprocessbase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QProgressBar, QSizePolicy, QSpacerItem,
    QTextBrowser, QWidget)
import resources_rc

class Ui_LaGrassProcessBase(object):
    def setupUi(self, LaGrassProcessBase):
        if not LaGrassProcessBase.objectName():
            LaGrassProcessBase.setObjectName(u"LaGrassProcessBase")
        LaGrassProcessBase.resize(593, 763)
        LaGrassProcessBase.setMinimumSize(QSize(0, 400))
        icon = QIcon(u":/la_icon_small.png")
        LaGrassProcessBase.setWindowIcon(icon)
        self.gridLayout = QGridLayout(LaGrassProcessBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grpPreview = QGroupBox(LaGrassProcessBase)
        self.grpPreview.setObjectName(u"grpPreview")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpPreview.sizePolicy().hasHeightForWidth())
        self.grpPreview.setSizePolicy(sizePolicy)
        self.gridLayout1 = QGridLayout(self.grpPreview)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.lblPreview = QLabel(self.grpPreview)
        self.lblPreview.setObjectName(u"lblPreview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy1)
        self.lblPreview.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.lblPreview, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.grpPreview, 0, 0, 3, 4)

        self.grpCurrentTarget = QGroupBox(LaGrassProcessBase)
        self.grpCurrentTarget.setObjectName(u"grpCurrentTarget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.grpCurrentTarget.sizePolicy().hasHeightForWidth())
        self.grpCurrentTarget.setSizePolicy(sizePolicy2)
        self.grpCurrentTarget.setMaximumSize(QSize(200, 16777215))
        self.gridLayout2 = QGridLayout(self.grpCurrentTarget)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.lblGraphic = QLabel(self.grpCurrentTarget)
        self.lblGraphic.setObjectName(u"lblGraphic")
        self.lblGraphic.setMinimumSize(QSize(100, 100))
        self.lblGraphic.setMaximumSize(QSize(1000000, 1000000))
        self.lblGraphic.setAlignment(Qt.AlignCenter)

        self.gridLayout2.addWidget(self.lblGraphic, 0, 0, 1, 1)

        self.lblCurrentArea = QLabel(self.grpCurrentTarget)
        self.lblCurrentArea.setObjectName(u"lblCurrentArea")
        sizePolicy1.setHeightForWidth(self.lblCurrentArea.sizePolicy().hasHeightForWidth())
        self.lblCurrentArea.setSizePolicy(sizePolicy1)
        self.lblCurrentArea.setAlignment(Qt.AlignCenter)

        self.gridLayout2.addWidget(self.lblCurrentArea, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.grpCurrentTarget, 0, 4, 1, 2)

        self.grpProgress = QGroupBox(LaGrassProcessBase)
        self.grpProgress.setObjectName(u"grpProgress")
        sizePolicy2.setHeightForWidth(self.grpProgress.sizePolicy().hasHeightForWidth())
        self.grpProgress.setSizePolicy(sizePolicy2)
        self.grpProgress.setMinimumSize(QSize(0, 0))
        self.grpProgress.setMaximumSize(QSize(200, 16777215))
        self.gridLayout3 = QGridLayout(self.grpProgress)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.label = QLabel(self.grpProgress)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 16))

        self.gridLayout3.addWidget(self.label, 0, 0, 1, 1)

        self.pbarBusy = QProgressBar(self.grpProgress)
        self.pbarBusy.setObjectName(u"pbarBusy")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pbarBusy.sizePolicy().hasHeightForWidth())
        self.pbarBusy.setSizePolicy(sizePolicy3)
        self.pbarBusy.setMinimumSize(QSize(0, 19))
        self.pbarBusy.setMaximumSize(QSize(16777215, 1677772))
        self.pbarBusy.setValue(0)
        self.pbarBusy.setTextVisible(False)
        self.pbarBusy.setOrientation(Qt.Horizontal)

        self.gridLayout3.addWidget(self.pbarBusy, 1, 0, 1, 1)

        self.lblAreaTarget = QLabel(self.grpProgress)
        self.lblAreaTarget.setObjectName(u"lblAreaTarget")
        self.lblAreaTarget.setMinimumSize(QSize(0, 16))
        self.lblAreaTarget.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.lblAreaTarget, 2, 0, 1, 1)

        self.pbarTarget = QProgressBar(self.grpProgress)
        self.pbarTarget.setObjectName(u"pbarTarget")
        sizePolicy3.setHeightForWidth(self.pbarTarget.sizePolicy().hasHeightForWidth())
        self.pbarTarget.setSizePolicy(sizePolicy3)
        self.pbarTarget.setMinimumSize(QSize(45, 19))
        self.pbarTarget.setValue(24)
        self.pbarTarget.setAlignment(Qt.AlignCenter)
        self.pbarTarget.setTextVisible(False)
        self.pbarTarget.setOrientation(Qt.Horizontal)

        self.gridLayout3.addWidget(self.pbarTarget, 3, 0, 1, 1)

        self.label_6 = QLabel(self.grpProgress)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 16))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.label_6, 4, 0, 1, 1)

        self.pbarOverall = QProgressBar(self.grpProgress)
        self.pbarOverall.setObjectName(u"pbarOverall")
        sizePolicy3.setHeightForWidth(self.pbarOverall.sizePolicy().hasHeightForWidth())
        self.pbarOverall.setSizePolicy(sizePolicy3)
        self.pbarOverall.setMinimumSize(QSize(45, 19))
        self.pbarOverall.setValue(24)
        self.pbarOverall.setTextVisible(False)
        self.pbarOverall.setOrientation(Qt.Horizontal)

        self.gridLayout3.addWidget(self.pbarOverall, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.grpProgress, 1, 4, 1, 2)

        self.groupBox_2 = QGroupBox(LaGrassProcessBase)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.gridLayout4 = QGridLayout(self.groupBox_2)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.tbGrass = QTextBrowser(self.groupBox_2)
        self.tbGrass.setObjectName(u"tbGrass")
        sizePolicy3.setHeightForWidth(self.tbGrass.sizePolicy().hasHeightForWidth())
        self.tbGrass.setSizePolicy(sizePolicy3)

        self.gridLayout4.addWidget(self.tbGrass, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 6)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 4, 5, 1, 1)

        self.label_2 = QLabel(LaGrassProcessBase)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 6)

        self.cbPeriod = QComboBox(LaGrassProcessBase)
        self.cbPeriod.addItem("")
        self.cbPeriod.addItem("")
        self.cbPeriod.addItem("")
        self.cbPeriod.setObjectName(u"cbPeriod")

        self.gridLayout.addWidget(self.cbPeriod, 6, 0, 1, 1)

        self.cbPopulation = QComboBox(LaGrassProcessBase)
        self.cbPopulation.addItem("")
        self.cbPopulation.addItem("")
        self.cbPopulation.setObjectName(u"cbPopulation")

        self.gridLayout.addWidget(self.cbPopulation, 6, 1, 1, 1)

        self.cbDietRatio = QComboBox(LaGrassProcessBase)
        self.cbDietRatio.addItem("")
        self.cbDietRatio.addItem("")
        self.cbDietRatio.addItem("")
        self.cbDietRatio.setObjectName(u"cbDietRatio")

        self.gridLayout.addWidget(self.cbDietRatio, 6, 2, 1, 1)

        self.cbDairy = QComboBox(LaGrassProcessBase)
        self.cbDairy.addItem("")
        self.cbDairy.addItem("")
        self.cbDairy.addItem("")
        self.cbDairy.setObjectName(u"cbDairy")

        self.gridLayout.addWidget(self.cbDairy, 6, 3, 1, 2)

        self.cbAnimalsFed = QComboBox(LaGrassProcessBase)
        self.cbAnimalsFed.addItem("")
        self.cbAnimalsFed.addItem("")
        self.cbAnimalsFed.setObjectName(u"cbAnimalsFed")

        self.gridLayout.addWidget(self.cbAnimalsFed, 6, 5, 1, 1)

        self.label_3 = QLabel(LaGrassProcessBase)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 2)

        self.leOtherText = QLineEdit(LaGrassProcessBase)
        self.leOtherText.setObjectName(u"leOtherText")

        self.gridLayout.addWidget(self.leOtherText, 7, 2, 1, 3)

        self.buttonBox = QDialogButtonBox(LaGrassProcessBase)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.NoButton|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 7, 5, 1, 1)


        self.retranslateUi(LaGrassProcessBase)
        self.buttonBox.accepted.connect(LaGrassProcessBase.accept)
        self.buttonBox.rejected.connect(LaGrassProcessBase.reject)

        QMetaObject.connectSlotsByName(LaGrassProcessBase)
    # setupUi

    def retranslateUi(self, LaGrassProcessBase):
        LaGrassProcessBase.setWindowTitle(QCoreApplication.translate("LaGrassProcessBase", u"Grass Processing", None))
        self.grpPreview.setTitle(QCoreApplication.translate("LaGrassProcessBase", u"Preview", None))
        self.lblPreview.setText(QCoreApplication.translate("LaGrassProcessBase", u"Preview feature not available in Beta Version", None))
        self.grpCurrentTarget.setTitle(QCoreApplication.translate("LaGrassProcessBase", u"Current Target", None))
        self.lblGraphic.setText(QCoreApplication.translate("LaGrassProcessBase", u"No Graphic", None))
        self.lblCurrentArea.setText(QCoreApplication.translate("LaGrassProcessBase", u"123456", None))
        self.grpProgress.setTitle(QCoreApplication.translate("LaGrassProcessBase", u"Progress", None))
        self.label.setText(QCoreApplication.translate("LaGrassProcessBase", u"Current GRASS Command", None))
        self.pbarBusy.setFormat("")
        self.lblAreaTarget.setText(QCoreApplication.translate("LaGrassProcessBase", u"Target: 123456", None))
        self.pbarTarget.setFormat("")
        self.label_6.setText(QCoreApplication.translate("LaGrassProcessBase", u"Overall Progress", None))
        self.pbarOverall.setFormat("")
        self.groupBox_2.setTitle(QCoreApplication.translate("LaGrassProcessBase", u"Log", None))
#if QT_CONFIG(whatsthis)
        self.tbGrass.setWhatsThis(QCoreApplication.translate("LaGrassProcessBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for a crop simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("LaGrassProcessBase", u"Select the PERIOD, POPULATION, & DIET RATIO.", None))
        self.cbPeriod.setItemText(0, QCoreApplication.translate("LaGrassProcessBase", u"Chalcolithic", None))
        self.cbPeriod.setItemText(1, QCoreApplication.translate("LaGrassProcessBase", u"EEB1", None))
        self.cbPeriod.setItemText(2, QCoreApplication.translate("LaGrassProcessBase", u"LEB1", None))

        self.cbPopulation.setItemText(0, QCoreApplication.translate("LaGrassProcessBase", u"Max", None))
        self.cbPopulation.setItemText(1, QCoreApplication.translate("LaGrassProcessBase", u"Min", None))

        self.cbDietRatio.setItemText(0, QCoreApplication.translate("LaGrassProcessBase", u"Meat 10%", None))
        self.cbDietRatio.setItemText(1, QCoreApplication.translate("LaGrassProcessBase", u"Meat 20%", None))
        self.cbDietRatio.setItemText(2, QCoreApplication.translate("LaGrassProcessBase", u"Meat 30%", None))

        self.cbDairy.setItemText(0, QCoreApplication.translate("LaGrassProcessBase", u"Dairy 100%", None))
        self.cbDairy.setItemText(1, QCoreApplication.translate("LaGrassProcessBase", u"Dairy 50%", None))
        self.cbDairy.setItemText(2, QCoreApplication.translate("LaGrassProcessBase", u"No Dairy", None))

        self.cbAnimalsFed.setItemText(0, QCoreApplication.translate("LaGrassProcessBase", u"Animals Fed", None))
        self.cbAnimalsFed.setItemText(1, QCoreApplication.translate("LaGrassProcessBase", u"Animals Not Fed", None))

        self.label_3.setText(QCoreApplication.translate("LaGrassProcessBase", u"Other text to include in filename:", None))
    # retranslateUi

