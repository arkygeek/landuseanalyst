# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lacropparameterbase.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_LaCropParameterManagerBase(object):
    def setupUi(self, LaCropParameterManagerBase):
        if not LaCropParameterManagerBase.objectName():
            LaCropParameterManagerBase.setObjectName(u"LaCropParameterManagerBase")
        LaCropParameterManagerBase.resize(585, 341)
        LaCropParameterManagerBase.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(LaCropParameterManagerBase)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.spacerItem = QSpacerItem(361, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem, 3, 0, 1, 2)

        self.grpProfiles = QGroupBox(LaCropParameterManagerBase)
        self.grpProfiles.setObjectName(u"grpProfiles")
        self.gridLayout1 = QGridLayout(self.grpProfiles)
#ifndef Q_OS_MAC
        self.gridLayout1.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.tblCropParameterProfiles = QTableWidget(self.grpProfiles)
        if (self.tblCropParameterProfiles.columnCount() < 2):
            self.tblCropParameterProfiles.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCropParameterProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCropParameterProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCropParameterProfiles.setObjectName(u"tblCropParameterProfiles")
        self.tblCropParameterProfiles.setAlternatingRowColors(True)
        self.tblCropParameterProfiles.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblCropParameterProfiles.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout1.addWidget(self.tblCropParameterProfiles, 0, 0, 1, 6)

        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon = QIcon()
        icon.addFile(u":/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolNew.setIcon(icon)

        self.gridLayout1.addWidget(self.toolNew, 1, 3, 1, 1)

        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon1 = QIcon()
        icon1.addFile(u":/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolCopy.setIcon(icon1)

        self.gridLayout1.addWidget(self.toolCopy, 1, 4, 1, 1)

        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon2 = QIcon()
        icon2.addFile(u":/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon2)

        self.gridLayout1.addWidget(self.toolDelete, 1, 5, 1, 1)

        self.pbnImport = QPushButton(self.grpProfiles)
        self.pbnImport.setObjectName(u"pbnImport")
        self.pbnImport.setMinimumSize(QSize(80, 0))

        self.gridLayout1.addWidget(self.pbnImport, 1, 0, 1, 1)

        self.pbnExport = QPushButton(self.grpProfiles)
        self.pbnExport.setObjectName(u"pbnExport")
        self.pbnExport.setMinimumSize(QSize(80, 0))

        self.gridLayout1.addWidget(self.pbnExport, 1, 1, 1, 1)

        self.spacerItem1 = QSpacerItem(71, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout1.addItem(self.spacerItem1, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.grpProfiles, 0, 0, 1, 4)

        self.groupBoxPortionOfDiet = QGroupBox(LaCropParameterManagerBase)
        self.groupBoxPortionOfDiet.setObjectName(u"groupBoxPortionOfDiet")
        self.gridLayout2 = QGridLayout(self.groupBoxPortionOfDiet)
        self.gridLayout2.setSpacing(3)
        self.gridLayout2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.labelPortionDiet = QLabel(self.groupBoxPortionOfDiet)
        self.labelPortionDiet.setObjectName(u"labelPortionDiet")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPortionDiet.sizePolicy().hasHeightForWidth())
        self.labelPortionDiet.setSizePolicy(sizePolicy)
        self.labelPortionDiet.setFrameShape(QFrame.NoFrame)
        self.labelPortionDiet.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout2.addWidget(self.labelPortionDiet, 0, 0, 1, 1)

        self.sbPercentOfTameCrop = QSpinBox(self.groupBoxPortionOfDiet)
        self.sbPercentOfTameCrop.setObjectName(u"sbPercentOfTameCrop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sbPercentOfTameCrop.sizePolicy().hasHeightForWidth())
        self.sbPercentOfTameCrop.setSizePolicy(sizePolicy1)
        self.sbPercentOfTameCrop.setMaximum(100)
        self.sbPercentOfTameCrop.setValue(50)

        self.gridLayout2.addWidget(self.sbPercentOfTameCrop, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBoxPortionOfDiet, 1, 0, 1, 1)

        self.groupBoxSuitableLand = QGroupBox(LaCropParameterManagerBase)
        self.groupBoxSuitableLand.setObjectName(u"groupBoxSuitableLand")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxSuitableLand.sizePolicy().hasHeightForWidth())
        self.groupBoxSuitableLand.setSizePolicy(sizePolicy2)
        self.groupBoxSuitableLand.setMinimumSize(QSize(115, 0))
        self.gridLayout3 = QGridLayout(self.groupBoxSuitableLand)
        self.gridLayout3.setSpacing(3)
        self.gridLayout3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.checkBoxCommonRaster = QCheckBox(self.groupBoxSuitableLand)
        self.checkBoxCommonRaster.setObjectName(u"checkBoxCommonRaster")
        sizePolicy1.setHeightForWidth(self.checkBoxCommonRaster.sizePolicy().hasHeightForWidth())
        self.checkBoxCommonRaster.setSizePolicy(sizePolicy1)

        self.gridLayout3.addWidget(self.checkBoxCommonRaster, 0, 1, 1, 1)

        self.checkBoxUniqueRaster = QCheckBox(self.groupBoxSuitableLand)
        self.checkBoxUniqueRaster.setObjectName(u"checkBoxUniqueRaster")
        sizePolicy1.setHeightForWidth(self.checkBoxUniqueRaster.sizePolicy().hasHeightForWidth())
        self.checkBoxUniqueRaster.setSizePolicy(sizePolicy1)

        self.gridLayout3.addWidget(self.checkBoxUniqueRaster, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxSuitableLand, 2, 0, 1, 1)

        self.groupBoxFallowUse = QGroupBox(LaCropParameterManagerBase)
        self.groupBoxFallowUse.setObjectName(u"groupBoxFallowUse")
        sizePolicy2.setHeightForWidth(self.groupBoxFallowUse.sizePolicy().hasHeightForWidth())
        self.groupBoxFallowUse.setSizePolicy(sizePolicy2)
        self.groupBoxFallowUse.setMinimumSize(QSize(227, 100))
        self.groupBoxFallowUse.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBoxFallowUse.setCheckable(True)
        self.groupBoxFallowUse.setChecked(False)
        self.gridLayout4 = QGridLayout(self.groupBoxFallowUse)
        self.gridLayout4.setSpacing(3)
        self.gridLayout4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout5 = QGridLayout()
        self.gridLayout5.setSpacing(0)
#ifndef Q_OS_MAC
        self.gridLayout5.setContentsMargins(0, 0, 0, 0)
#endif
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.sbFallowRatio = QDoubleSpinBox(self.groupBoxFallowUse)
        self.sbFallowRatio.setObjectName(u"sbFallowRatio")
        self.sbFallowRatio.setMaximum(5.000000000000000)
        self.sbFallowRatio.setSingleStep(0.250000000000000)
        self.sbFallowRatio.setValue(1.000000000000000)

        self.gridLayout5.addWidget(self.sbFallowRatio, 1, 1, 1, 1)

        self.labelFallow1 = QLabel(self.groupBoxFallowUse)
        self.labelFallow1.setObjectName(u"labelFallow1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelFallow1.sizePolicy().hasHeightForWidth())
        self.labelFallow1.setSizePolicy(sizePolicy3)
        self.labelFallow1.setAlignment(Qt.AlignCenter)

        self.gridLayout5.addWidget(self.labelFallow1, 0, 0, 1, 2)

        self.labelFallow3 = QLabel(self.groupBoxFallowUse)
        self.labelFallow3.setObjectName(u"labelFallow3")
        self.labelFallow3.setLayoutDirection(Qt.LeftToRight)
        self.labelFallow3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout5.addWidget(self.labelFallow3, 1, 0, 1, 1)


        self.gridLayout4.addLayout(self.gridLayout5, 0, 0, 1, 1)

        self.labelFallow5 = QLabel(self.groupBoxFallowUse)
        self.labelFallow5.setObjectName(u"labelFallow5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelFallow5.sizePolicy().hasHeightForWidth())
        self.labelFallow5.setSizePolicy(sizePolicy4)
        self.labelFallow5.setAlignment(Qt.AlignCenter)

        self.gridLayout4.addWidget(self.labelFallow5, 1, 0, 1, 1)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelFallow2 = QLabel(self.groupBoxFallowUse)
        self.labelFallow2.setObjectName(u"labelFallow2")
        self.labelFallow2.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.labelFallow2)

        self.hboxLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.labelFallow4 = QLabel(self.groupBoxFallowUse)
        self.labelFallow4.setObjectName(u"labelFallow4")
        sizePolicy3.setHeightForWidth(self.labelFallow4.sizePolicy().hasHeightForWidth())
        self.labelFallow4.setSizePolicy(sizePolicy3)
        self.labelFallow4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout.addWidget(self.labelFallow4)

        self.sbFallowFoodValueToGrazers = QSpinBox(self.groupBoxFallowUse)
        self.sbFallowFoodValueToGrazers.setObjectName(u"sbFallowFoodValueToGrazers")
        sizePolicy1.setHeightForWidth(self.sbFallowFoodValueToGrazers.sizePolicy().hasHeightForWidth())
        self.sbFallowFoodValueToGrazers.setSizePolicy(sizePolicy1)
        self.sbFallowFoodValueToGrazers.setMinimum(1)
        self.sbFallowFoodValueToGrazers.setMaximum(500)
        self.sbFallowFoodValueToGrazers.setValue(8)

        self.hboxLayout.addWidget(self.sbFallowFoodValueToGrazers)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.gridLayout4.addLayout(self.vboxLayout, 0, 2, 1, 2)

        self.cbAreaUnits = QComboBox(self.groupBoxFallowUse)
        self.cbAreaUnits.addItem("")
        self.cbAreaUnits.addItem("")
        self.cbAreaUnits.setObjectName(u"cbAreaUnits")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cbAreaUnits.sizePolicy().hasHeightForWidth())
        self.cbAreaUnits.setSizePolicy(sizePolicy5)

        self.gridLayout4.addWidget(self.cbAreaUnits, 1, 3, 1, 1)

        self.labelFallow6 = QLabel(self.groupBoxFallowUse)
        self.labelFallow6.setObjectName(u"labelFallow6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.labelFallow6.sizePolicy().hasHeightForWidth())
        self.labelFallow6.setSizePolicy(sizePolicy6)
        self.labelFallow6.setTextFormat(Qt.AutoText)
        self.labelFallow6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelFallow6.setWordWrap(False)

        self.gridLayout4.addWidget(self.labelFallow6, 1, 2, 1, 1)

        self.line = QFrame(self.groupBoxFallowUse)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout4.addWidget(self.line, 0, 1, 2, 1)


        self.gridLayout.addWidget(self.groupBoxFallowUse, 1, 1, 2, 3)

        self.pbnClose = QPushButton(LaCropParameterManagerBase)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.pbnClose, 3, 3, 1, 1)

        self.pbnApply = QPushButton(LaCropParameterManagerBase)
        self.pbnApply.setObjectName(u"pbnApply")
        sizePolicy7.setHeightForWidth(self.pbnApply.sizePolicy().hasHeightForWidth())
        self.pbnApply.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.pbnApply, 3, 2, 1, 1)


        self.retranslateUi(LaCropParameterManagerBase)
        self.pbnClose.pressed.connect(LaCropParameterManagerBase.close)
        self.checkBoxCommonRaster.clicked.connect(self.checkBoxUniqueRaster.toggle)
        self.checkBoxUniqueRaster.clicked.connect(self.checkBoxCommonRaster.toggle)

        QMetaObject.connectSlotsByName(LaCropParameterManagerBase)
    # setupUi

    def retranslateUi(self, LaCropParameterManagerBase):
        LaCropParameterManagerBase.setWindowTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop Parameter Manager", None))
        self.grpProfiles.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Available Plant Parameter Settings", None))
        ___qtablewidgetitem = self.tblCropParameterProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblCropParameterProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Name", None));
#if QT_CONFIG(whatsthis)
        self.tblCropParameterProfiles.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"Table of the currently available layersets", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"New", None))
#endif // QT_CONFIG(tooltip)
        self.toolNew.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"Clone", None))
#endif // QT_CONFIG(tooltip)
        self.toolCopy.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
        self.pbnImport.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Export", None))
        self.groupBoxPortionOfDiet.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Portion of Diet", None))
        self.labelPortionDiet.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Portion of Tame Plant Diet", None))
#if QT_CONFIG(tooltip)
        self.sbPercentOfTameCrop.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pigs contiribute this percent towards the tame meat portion of the diet</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxSuitableLand.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Suitable Land", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"binary raster named: pigmask", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Common Raster ", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUniqueRaster.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"binary raster named: pigmask", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUniqueRaster.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Unique Raster", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxFallowUse.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"Select Fodder if you believe the animals were fed grain to supplement their grazing.  You will then have to select how many kg of the selected grain you believe they fed each animal either every day, week, or month.", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxFallowUse.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop Rotation", None))
#if QT_CONFIG(tooltip)
        self.sbFallowRatio.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fallow</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelFallow1.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFallow1.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Ratio", None))
        self.labelFallow3.setText(QCoreApplication.translate("LaCropParameterManagerBase", u" 1: ", None))
#if QT_CONFIG(tooltip)
        self.labelFallow5.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFallow5.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop:Fallow ", None))
        self.labelFallow2.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Food Value*", None))
        self.labelFallow4.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"kCalories", None))
        self.cbAreaUnits.setItemText(0, QCoreApplication.translate("LaCropParameterManagerBase", u"Dunum", None))
        self.cbAreaUnits.setItemText(1, QCoreApplication.translate("LaCropParameterManagerBase", u"Hectare", None))

#if QT_CONFIG(tooltip)
        self.cbAreaUnits.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelFallow6.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weeks from birth to kill weight</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFallow6.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"*per ", None))
        self.pbnClose.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Close", None))
        self.pbnApply.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Apply", None))
    # retranslateUi

