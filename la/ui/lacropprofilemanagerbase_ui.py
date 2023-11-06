# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lacropprofilemanagerbase.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_LaCropManagerBase(object):
    def setupUi(self, LaCropManagerBase):
        if not LaCropManagerBase.objectName():
            LaCropManagerBase.setObjectName(u"LaCropManagerBase")
        LaCropManagerBase.resize(454, 456)
        icon = QIcon()
        icon.addFile(u":/la_icon_small.png", QSize(), QIcon.Normal, QIcon.Off)
        LaCropManagerBase.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(LaCropManagerBase)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grpProfiles = QGroupBox(LaCropManagerBase)
        self.grpProfiles.setObjectName(u"grpProfiles")
        self.gridLayout = QGridLayout(self.grpProfiles)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout1 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout1.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
#endif
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon1 = QIcon()
        icon1.addFile(u":/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolNew.setIcon(icon1)

        self.gridLayout1.addWidget(self.toolNew, 2, 0, 1, 1)

        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon2 = QIcon()
        icon2.addFile(u":/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon2)

        self.gridLayout1.addWidget(self.toolDelete, 2, 2, 1, 1)

        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon3 = QIcon()
        icon3.addFile(u":/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolCopy.setIcon(icon3)

        self.gridLayout1.addWidget(self.toolCopy, 2, 1, 1, 1)

        self.spacerItem = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout1.addItem(self.spacerItem, 1, 1, 1, 1)

        self.lblCropPix = QLabel(self.grpProfiles)
        self.lblCropPix.setObjectName(u"lblCropPix")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCropPix.sizePolicy().hasHeightForWidth())
        self.lblCropPix.setSizePolicy(sizePolicy)
        self.lblCropPix.setMinimumSize(QSize(100, 100))
        self.lblCropPix.setMaximumSize(QSize(100, 100))
        self.lblCropPix.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.lblCropPix, 0, 0, 1, 3)


        self.gridLayout.addLayout(self.gridLayout1, 0, 3, 2, 1)

        self.tblCrops = QTableWidget(self.grpProfiles)
        if (self.tblCrops.columnCount() < 2):
            self.tblCrops.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCrops.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCrops.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblCrops.setObjectName(u"tblCrops")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tblCrops.sizePolicy().hasHeightForWidth())
        self.tblCrops.setSizePolicy(sizePolicy1)
        self.tblCrops.setMinimumSize(QSize(0, 0))
        self.tblCrops.setAlternatingRowColors(True)
        self.tblCrops.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblCrops.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tblCrops, 0, 0, 1, 3)

        self.pbnImport = QPushButton(self.grpProfiles)
        self.pbnImport.setObjectName(u"pbnImport")
        self.pbnImport.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.pbnImport, 1, 0, 1, 1)

        self.pbnExport = QPushButton(self.grpProfiles)
        self.pbnExport.setObjectName(u"pbnExport")
        self.pbnExport.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.pbnExport, 1, 1, 1, 1)

        self.spacerItem1 = QSpacerItem(111, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem1, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.grpProfiles, 0, 0, 1, 3)

        self.groupBoxPlantDescription = QGroupBox(LaCropManagerBase)
        self.groupBoxPlantDescription.setObjectName(u"groupBoxPlantDescription")
        self.gridLayout2 = QGridLayout(self.groupBoxPlantDescription)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.label = QLabel(self.groupBoxPlantDescription)
        self.label.setObjectName(u"label")

        self.gridLayout2.addWidget(self.label, 0, 0, 1, 2)

        self.leName = QLineEdit(self.groupBoxPlantDescription)
        self.leName.setObjectName(u"leName")

        self.gridLayout2.addWidget(self.leName, 0, 2, 1, 4)

        self.label_4 = QLabel(self.groupBoxPlantDescription)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout2.addWidget(self.label_4, 1, 0, 2, 2)

        self.leDescription = QLineEdit(self.groupBoxPlantDescription)
        self.leDescription.setObjectName(u"leDescription")

        self.gridLayout2.addWidget(self.leDescription, 1, 2, 1, 3)

        self.pbnCropPic = QPushButton(self.groupBoxPlantDescription)
        self.pbnCropPic.setObjectName(u"pbnCropPic")
        sizePolicy.setHeightForWidth(self.pbnCropPic.sizePolicy().hasHeightForWidth())
        self.pbnCropPic.setSizePolicy(sizePolicy)

        self.gridLayout2.addWidget(self.pbnCropPic, 1, 5, 1, 1)

        self.line_2 = QFrame(self.groupBoxPlantDescription)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout2.addWidget(self.line_2, 2, 1, 1, 5)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelPlantDescription4 = QLabel(self.groupBoxPlantDescription)
        self.labelPlantDescription4.setObjectName(u"labelPlantDescription4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelPlantDescription4.sizePolicy().hasHeightForWidth())
        self.labelPlantDescription4.setSizePolicy(sizePolicy2)
        self.labelPlantDescription4.setTextFormat(Qt.AutoText)
        self.labelPlantDescription4.setWordWrap(False)

        self.vboxLayout.addWidget(self.labelPlantDescription4)

        self.labelPlantDescription6 = QLabel(self.groupBoxPlantDescription)
        self.labelPlantDescription6.setObjectName(u"labelPlantDescription6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelPlantDescription6.sizePolicy().hasHeightForWidth())
        self.labelPlantDescription6.setSizePolicy(sizePolicy3)
        self.labelPlantDescription6.setTextFormat(Qt.AutoText)
        self.labelPlantDescription6.setWordWrap(False)

        self.vboxLayout.addWidget(self.labelPlantDescription6)

        self.label_3 = QLabel(self.groupBoxPlantDescription)
        self.label_3.setObjectName(u"label_3")

        self.vboxLayout.addWidget(self.label_3)


        self.gridLayout2.addLayout(self.vboxLayout, 3, 0, 5, 2)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.sbCropYield = QSpinBox(self.groupBoxPlantDescription)
        self.sbCropYield.setObjectName(u"sbCropYield")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sbCropYield.sizePolicy().hasHeightForWidth())
        self.sbCropYield.setSizePolicy(sizePolicy4)
        self.sbCropYield.setMaximum(400)
        self.sbCropYield.setValue(60)

        self.vboxLayout1.addWidget(self.sbCropYield)

        self.sbCropFodderProduction = QSpinBox(self.groupBoxPlantDescription)
        self.sbCropFodderProduction.setObjectName(u"sbCropFodderProduction")
        sizePolicy4.setHeightForWidth(self.sbCropFodderProduction.sizePolicy().hasHeightForWidth())
        self.sbCropFodderProduction.setSizePolicy(sizePolicy4)
        self.sbCropFodderProduction.setMaximum(400)
        self.sbCropFodderProduction.setValue(60)

        self.vboxLayout1.addWidget(self.sbCropFodderProduction)

        self.cbAreaUnits = QComboBox(self.groupBoxPlantDescription)
        self.cbAreaUnits.setObjectName(u"cbAreaUnits")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cbAreaUnits.sizePolicy().hasHeightForWidth())
        self.cbAreaUnits.setSizePolicy(sizePolicy5)

        self.vboxLayout1.addWidget(self.cbAreaUnits)


        self.gridLayout2.addLayout(self.vboxLayout1, 3, 2, 5, 1)

        self.label_2 = QLabel(self.groupBoxPlantDescription)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout2.addWidget(self.label_2, 4, 3, 1, 1)

        self.sbCropCalories = QSpinBox(self.groupBoxPlantDescription)
        self.sbCropCalories.setObjectName(u"sbCropCalories")
        sizePolicy.setHeightForWidth(self.sbCropCalories.sizePolicy().hasHeightForWidth())
        self.sbCropCalories.setSizePolicy(sizePolicy)
        self.sbCropCalories.setMinimum(1)
        self.sbCropCalories.setMaximum(5000)
        self.sbCropCalories.setValue(3000)

        self.gridLayout2.addWidget(self.sbCropCalories, 4, 4, 1, 2)

        self.line = QFrame(self.groupBoxPlantDescription)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout2.addWidget(self.line, 5, 3, 1, 3)

        self.label_5 = QLabel(self.groupBoxPlantDescription)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout2.addWidget(self.label_5, 6, 3, 1, 3)

        self.sbCropFodderValue = QSpinBox(self.groupBoxPlantDescription)
        self.sbCropFodderValue.setObjectName(u"sbCropFodderValue")
        sizePolicy.setHeightForWidth(self.sbCropFodderValue.sizePolicy().hasHeightForWidth())
        self.sbCropFodderValue.setSizePolicy(sizePolicy)
        self.sbCropFodderValue.setMinimum(1)
        self.sbCropFodderValue.setMaximum(500000)
        self.sbCropFodderValue.setSingleStep(1)
        self.sbCropFodderValue.setValue(1123)

        self.gridLayout2.addWidget(self.sbCropFodderValue, 7, 3, 1, 2)

        self.cbFodderEnergyType = QComboBox(self.groupBoxPlantDescription)
        self.cbFodderEnergyType.setObjectName(u"cbFodderEnergyType")

        self.gridLayout2.addWidget(self.cbFodderEnergyType, 7, 5, 1, 1)

        self.label.raise_()
        self.leName.raise_()
        self.label_4.raise_()
        self.leDescription.raise_()
        self.pbnCropPic.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.sbCropFodderValue.raise_()
        self.cbFodderEnergyType.raise_()

        self.gridLayout_2.addWidget(self.groupBoxPlantDescription, 1, 0, 1, 3)

        self.spacerItem2 = QSpacerItem(31, 31, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.spacerItem2, 2, 0, 1, 1)

        self.pbnApply = QPushButton(LaCropManagerBase)
        self.pbnApply.setObjectName(u"pbnApply")
        self.pbnApply.setCheckable(False)
        self.pbnApply.setFlat(False)

        self.gridLayout_2.addWidget(self.pbnApply, 2, 1, 1, 1)

        self.pbnClose = QPushButton(LaCropManagerBase)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.pbnClose, 2, 2, 1, 1)

        QWidget.setTabOrder(self.tblCrops, self.pbnImport)
        QWidget.setTabOrder(self.pbnImport, self.pbnExport)
        QWidget.setTabOrder(self.pbnExport, self.toolNew)
        QWidget.setTabOrder(self.toolNew, self.toolCopy)
        QWidget.setTabOrder(self.toolCopy, self.toolDelete)
        QWidget.setTabOrder(self.toolDelete, self.leName)
        QWidget.setTabOrder(self.leName, self.leDescription)
        QWidget.setTabOrder(self.leDescription, self.sbCropYield)
        QWidget.setTabOrder(self.sbCropYield, self.sbCropCalories)
        QWidget.setTabOrder(self.sbCropCalories, self.sbCropFodderProduction)
        QWidget.setTabOrder(self.sbCropFodderProduction, self.sbCropFodderValue)
        QWidget.setTabOrder(self.sbCropFodderValue, self.cbAreaUnits)
        QWidget.setTabOrder(self.cbAreaUnits, self.pbnApply)
        QWidget.setTabOrder(self.pbnApply, self.pbnClose)

        self.retranslateUi(LaCropManagerBase)
        self.pbnClose.clicked.connect(LaCropManagerBase.reject)

        QMetaObject.connectSlotsByName(LaCropManagerBase)
    # setupUi

    def retranslateUi(self, LaCropManagerBase):
        LaCropManagerBase.setWindowTitle(QCoreApplication.translate("LaCropManagerBase", u"Crop Profile Manager", None))
        self.grpProfiles.setTitle(QCoreApplication.translate("LaCropManagerBase", u"Available Crop Profiles", None))
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new crop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolNew.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Crop Manager, you are just editing the Crop currently selected. To create a new Crop, you must click on the New button.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolNew.setText(QCoreApplication.translate("LaCropManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected crop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaCropManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected crop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolCopy.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new crop that is similar to one already defined, you can clone this crop to save time. All of the settings of the crop you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the crop you are cloning was).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolCopy.setText(QCoreApplication.translate("LaCropManagerBase", u"...", None))
        self.lblCropPix.setText(QCoreApplication.translate("LaCropManagerBase", u"No Graphic\n"
"Selected", None))
        ___qtablewidgetitem = self.tblCrops.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaCropManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblCrops.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaCropManagerBase", u"Name", None));
#if QT_CONFIG(tooltip)
        self.tblCrops.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a crop here to see and/or edit it's properties below.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblCrops.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model any crop, several details must be entered to define specific varieties. Crop Manager asks for general information about the crop in this section. You might want to have more than one strain of the same variety, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different strains of the same variety is quite easy. Let's say you want to have two kinds of wheat for example. The Name: field is Wheat for both, but in Notes: field, enter Hard Red for one, and Soft White for the other. The"
                        "n adjust the other parameters as you wish. Even though the name is the same, the crop is saved uniquely.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnImport.setText(QCoreApplication.translate("LaCropManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaCropManagerBase", u"Export", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxPlantDescription.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model any crop, several details must be entered to define specific varieties. Crop Manager asks for general information about the crop in this section. You might want to have more than one strain of the same variety, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different strains of the same variety is quite easy. Let's say you want to have two kinds of wheat for example. The Name: field is Wheat for both, but in Notes: field, enter Hard Red for one, and Soft White for the other. The"
                        "n adjust the other parameters as you wish. Even though the name is the same, the crop is saved uniquely.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxPlantDescription.setTitle(QCoreApplication.translate("LaCropManagerBase", u"Crop Description", None))
        self.label.setText(QCoreApplication.translate("LaCropManagerBase", u"Name:", None))
#if QT_CONFIG(whatsthis)
        self.leName.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the crop you are defining in this field. You do not need a unique name. You can have, for example, 10 crops defined, all named \"Wheat\". Landuse Analyst uses a special method of saving the crops to eliminate the issue of duplicate filenames.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("LaCropManagerBase", u"Notes:", None))
#if QT_CONFIG(whatsthis)
        self.leDescription.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because Landuse Analyst allows more than one type of crop to be defined, the Notes: field allows you to give a brief description of the the crop. For example, you may have two \"Wheat\" crops defined, and the Notes: fields could contain \"Hard Red\" and \"Soft White\" to distinguish between them.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnCropPic.setText(QCoreApplication.translate("LaCropManagerBase", u"Set Graphic", None))
        self.labelPlantDescription4.setText(QCoreApplication.translate("LaCropManagerBase", u"Crop Yield", None))
#if QT_CONFIG(tooltip)
        self.labelPlantDescription6.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder produced from Wheat</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.labelPlantDescription6.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder is the straw and chaff left after harvesting the grain.  Enter the number of Kilograms expected for this crop per (either) dunum or hectare</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.labelPlantDescription6.setText(QCoreApplication.translate("LaCropManagerBase", u"Fodder", None))
        self.label_3.setText(QCoreApplication.translate("LaCropManagerBase", u"Area Units *", None))
#if QT_CONFIG(tooltip)
        self.sbCropYield.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yield of Crop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCropYield.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here you must enter what you think the average yield for the crop would have been. This is a measure of Kg produced per the given area of sown land.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbCropYield.setSuffix(QCoreApplication.translate("LaCropManagerBase", u" Kg/*", None))
#if QT_CONFIG(tooltip)
        self.sbCropFodderProduction.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder produced from Wheat</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCropFodderProduction.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Fodder Yield is how many Kg of Straw and Chaff (per area unit) that is <span style=\" font-weight:600;\">made available to animals for feed</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder is the straw and chaff left after harvesting the grain.  Enter the number of Kilograms expected to be produced from this crop per (either) dunum or hectare.  <span style=\" font-weight:600; color:#0000ff;\""
                        ">Note that this fodder amount is solely for consumption by animals.</span>  If straw or chaff is being used for other purposes, it must be taken out of the total expected fodder level.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbCropFodderProduction.setSuffix(QCoreApplication.translate("LaCropManagerBase", u" Kg/*", None))
#if QT_CONFIG(tooltip)
        self.cbAreaUnits.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cbAreaUnits.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("LaCropManagerBase", u"Crop Value:", None))
#if QT_CONFIG(tooltip)
        self.sbCropCalories.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories in 1 Kg of that part of the crop which is eaten (ie. the grain or fruit). </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCropCalories.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbCropCalories.setSuffix(QCoreApplication.translate("LaCropManagerBase", u" Cal/Kg", None))
        self.label_5.setText(QCoreApplication.translate("LaCropManagerBase", u"Food Value of Fodder:", None))
#if QT_CONFIG(tooltip)
        self.sbCropFodderValue.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calories per kilogram of fodder</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCropFodderValue.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food value of fodder when used as feed for domestic animals.  This is measured in calories per kilogram.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbCropFodderValue.setSuffix("")
#if QT_CONFIG(tooltip)
        self.pbnApply.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnApply.setWhatsThis(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a crop, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as Landuse Analyst has a special way of saving crops to allow for duplicate crop names. It is helpful, however, to utilize the Notes field to distinguish between same-named crop definitions.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnApply.setText(QCoreApplication.translate("LaCropManagerBase", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.pbnClose.setToolTip(QCoreApplication.translate("LaCropManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbnClose.setText(QCoreApplication.translate("LaCropManagerBase", u"Close", None))
    # retranslateUi

