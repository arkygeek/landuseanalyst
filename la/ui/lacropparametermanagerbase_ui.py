# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lacropparametermanagerbase.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QToolButton, QWidget)

class Ui_LaCropParameterManagerBase(object):
    def setupUi(self, LaCropParameterManagerBase):
        if not LaCropParameterManagerBase.objectName():
            LaCropParameterManagerBase.setObjectName(u"LaCropParameterManagerBase")
        LaCropParameterManagerBase.resize(520, 583)
        LaCropParameterManagerBase.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/la_icon_small.png", QSize(), QIcon.Normal, QIcon.Off)
        LaCropParameterManagerBase.setWindowIcon(icon)
        self.gridLayout = QGridLayout(LaCropParameterManagerBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grpProfiles = QGroupBox(LaCropParameterManagerBase)
        self.grpProfiles.setObjectName(u"grpProfiles")
        self.gridLayout1 = QGridLayout(self.grpProfiles)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon1 = QIcon()
        icon1.addFile(u":/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon1)

        self.gridLayout2.addWidget(self.toolDelete, 2, 2, 1, 1)

        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon2 = QIcon()
        icon2.addFile(u":/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolCopy.setIcon(icon2)

        self.gridLayout2.addWidget(self.toolCopy, 2, 1, 1, 1)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout2.addItem(self.spacerItem, 1, 1, 1, 1)

        self.lblCropPic = QLabel(self.grpProfiles)
        self.lblCropPic.setObjectName(u"lblCropPic")
        self.lblCropPic.setMinimumSize(QSize(100, 100))
        self.lblCropPic.setMaximumSize(QSize(100, 100))
        self.lblCropPic.setAlignment(Qt.AlignCenter)

        self.gridLayout2.addWidget(self.lblCropPic, 0, 0, 1, 3)

        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon3 = QIcon()
        icon3.addFile(u":/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolNew.setIcon(icon3)

        self.gridLayout2.addWidget(self.toolNew, 2, 0, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 3, 2, 1)

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

        self.gridLayout1.addWidget(self.tblCropParameterProfiles, 0, 0, 1, 3)


        self.gridLayout.addWidget(self.grpProfiles, 0, 0, 1, 6)

        self.label = QLabel(LaCropParameterManagerBase)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.leName = QLineEdit(LaCropParameterManagerBase)
        self.leName.setObjectName(u"leName")

        self.gridLayout.addWidget(self.leName, 1, 1, 1, 1)

        self.grpCropRotation = QGroupBox(LaCropParameterManagerBase)
        self.grpCropRotation.setObjectName(u"grpCropRotation")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpCropRotation.sizePolicy().hasHeightForWidth())
        self.grpCropRotation.setSizePolicy(sizePolicy)
        self.grpCropRotation.setMinimumSize(QSize(227, 100))
        self.grpCropRotation.setCheckable(True)
        self.grpCropRotation.setChecked(False)
        self.gridLayout3 = QGridLayout(self.grpCropRotation)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.labelFallow1 = QLabel(self.grpCropRotation)
        self.labelFallow1.setObjectName(u"labelFallow1")
        sizePolicy.setHeightForWidth(self.labelFallow1.sizePolicy().hasHeightForWidth())
        self.labelFallow1.setSizePolicy(sizePolicy)
        self.labelFallow1.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.labelFallow1, 0, 0, 1, 1)

        self.labelFallow3 = QLabel(self.grpCropRotation)
        self.labelFallow3.setObjectName(u"labelFallow3")
        self.labelFallow3.setLayoutDirection(Qt.LeftToRight)
        self.labelFallow3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout3.addWidget(self.labelFallow3, 0, 1, 1, 1)

        self.sbFallowRatio = QDoubleSpinBox(self.grpCropRotation)
        self.sbFallowRatio.setObjectName(u"sbFallowRatio")
        self.sbFallowRatio.setMinimumSize(QSize(0, 22))
        self.sbFallowRatio.setMaximum(5.000000000000000)
        self.sbFallowRatio.setSingleStep(0.250000000000000)
        self.sbFallowRatio.setValue(1.000000000000000)

        self.gridLayout3.addWidget(self.sbFallowRatio, 0, 2, 1, 1)

        self.labelFallow5 = QLabel(self.grpCropRotation)
        self.labelFallow5.setObjectName(u"labelFallow5")
        sizePolicy.setHeightForWidth(self.labelFallow5.sizePolicy().hasHeightForWidth())
        self.labelFallow5.setSizePolicy(sizePolicy)
        self.labelFallow5.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.labelFallow5, 0, 3, 1, 2)

        self.labelFallow2 = QLabel(self.grpCropRotation)
        self.labelFallow2.setObjectName(u"labelFallow2")
        self.labelFallow2.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.labelFallow2, 1, 0, 1, 5)

        self.sbFallowValue = QSpinBox(self.grpCropRotation)
        self.sbFallowValue.setObjectName(u"sbFallowValue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sbFallowValue.sizePolicy().hasHeightForWidth())
        self.sbFallowValue.setSizePolicy(sizePolicy1)
        self.sbFallowValue.setMinimumSize(QSize(0, 22))
        self.sbFallowValue.setMinimum(1)
        self.sbFallowValue.setMaximum(5000)
        self.sbFallowValue.setSingleStep(10)
        self.sbFallowValue.setValue(500)

        self.gridLayout3.addWidget(self.sbFallowValue, 2, 0, 1, 2)

        self.cbFallowEnergyType = QComboBox(self.grpCropRotation)
        self.cbFallowEnergyType.setObjectName(u"cbFallowEnergyType")
        self.cbFallowEnergyType.setMinimumSize(QSize(0, 22))

        self.gridLayout3.addWidget(self.cbFallowEnergyType, 2, 2, 1, 2)

        self.cbAreaUnits = QComboBox(self.grpCropRotation)
        self.cbAreaUnits.setObjectName(u"cbAreaUnits")
        sizePolicy.setHeightForWidth(self.cbAreaUnits.sizePolicy().hasHeightForWidth())
        self.cbAreaUnits.setSizePolicy(sizePolicy)
        self.cbAreaUnits.setMinimumSize(QSize(0, 22))

        self.gridLayout3.addWidget(self.cbAreaUnits, 2, 4, 1, 1)


        self.gridLayout.addWidget(self.grpCropRotation, 1, 2, 4, 4)

        self.label_4 = QLabel(LaCropParameterManagerBase)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.leDescription = QLineEdit(LaCropParameterManagerBase)
        self.leDescription.setObjectName(u"leDescription")
        sizePolicy.setHeightForWidth(self.leDescription.sizePolicy().hasHeightForWidth())
        self.leDescription.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.leDescription, 2, 1, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label_2 = QLabel(LaCropParameterManagerBase)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.hboxLayout.addWidget(self.label_2)

        self.cboCrop = QComboBox(LaCropParameterManagerBase)
        self.cboCrop.setObjectName(u"cboCrop")
        self.cboCrop.setMinimumSize(QSize(0, 26))

        self.hboxLayout.addWidget(self.cboCrop)


        self.gridLayout.addLayout(self.hboxLayout, 3, 0, 1, 2)

        self.groupBoxSuitableLand = QGroupBox(LaCropParameterManagerBase)
        self.groupBoxSuitableLand.setObjectName(u"groupBoxSuitableLand")
        sizePolicy.setHeightForWidth(self.groupBoxSuitableLand.sizePolicy().hasHeightForWidth())
        self.groupBoxSuitableLand.setSizePolicy(sizePolicy)
        self.groupBoxSuitableLand.setMinimumSize(QSize(115, 0))
        self.gridLayout4 = QGridLayout(self.groupBoxSuitableLand)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.checkBoxUseCommonLand = QCheckBox(self.groupBoxSuitableLand)
        self.checkBoxUseCommonLand.setObjectName(u"checkBoxUseCommonLand")
        sizePolicy.setHeightForWidth(self.checkBoxUseCommonLand.sizePolicy().hasHeightForWidth())
        self.checkBoxUseCommonLand.setSizePolicy(sizePolicy)
        self.checkBoxUseCommonLand.setChecked(True)

        self.gridLayout4.addWidget(self.checkBoxUseCommonLand, 0, 0, 1, 2)

        self.checkBoxUseSpecificLand = QCheckBox(self.groupBoxSuitableLand)
        self.checkBoxUseSpecificLand.setObjectName(u"checkBoxUseSpecificLand")
        sizePolicy.setHeightForWidth(self.checkBoxUseSpecificLand.sizePolicy().hasHeightForWidth())
        self.checkBoxUseSpecificLand.setSizePolicy(sizePolicy)

        self.gridLayout4.addWidget(self.checkBoxUseSpecificLand, 1, 0, 1, 2)

        self.label_3 = QLabel(self.groupBoxSuitableLand)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(0)
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout4.addWidget(self.label_3, 2, 0, 1, 1)

        self.cboRaster = QComboBox(self.groupBoxSuitableLand)
        self.cboRaster.setObjectName(u"cboRaster")

        self.gridLayout4.addWidget(self.cboRaster, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBoxSuitableLand, 4, 0, 4, 2)

        self.labelPortionDiet = QLabel(LaCropParameterManagerBase)
        self.labelPortionDiet.setObjectName(u"labelPortionDiet")
        sizePolicy.setHeightForWidth(self.labelPortionDiet.sizePolicy().hasHeightForWidth())
        self.labelPortionDiet.setSizePolicy(sizePolicy)
        self.labelPortionDiet.setFrameShape(QFrame.NoFrame)
        self.labelPortionDiet.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.labelPortionDiet, 5, 2, 1, 2)

        self.sbPercentTameCrop = QDoubleSpinBox(LaCropParameterManagerBase)
        self.sbPercentTameCrop.setObjectName(u"sbPercentTameCrop")
        self.sbPercentTameCrop.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sbPercentTameCrop.setAccelerated(True)
        self.sbPercentTameCrop.setMaximum(100.000000000000000)
        self.sbPercentTameCrop.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.sbPercentTameCrop, 5, 4, 1, 2)

        self.labelPortionDiet_2 = QLabel(LaCropParameterManagerBase)
        self.labelPortionDiet_2.setObjectName(u"labelPortionDiet_2")
        sizePolicy.setHeightForWidth(self.labelPortionDiet_2.sizePolicy().hasHeightForWidth())
        self.labelPortionDiet_2.setSizePolicy(sizePolicy)
        self.labelPortionDiet_2.setFrameShape(QFrame.NoFrame)
        self.labelPortionDiet_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.labelPortionDiet_2, 6, 2, 1, 3)

        self.sbReseed = QSpinBox(LaCropParameterManagerBase)
        self.sbReseed.setObjectName(u"sbReseed")
        self.sbReseed.setMaximum(100)

        self.gridLayout.addWidget(self.sbReseed, 6, 5, 1, 1)

        self.labelPortionDiet_3 = QLabel(LaCropParameterManagerBase)
        self.labelPortionDiet_3.setObjectName(u"labelPortionDiet_3")
        sizePolicy.setHeightForWidth(self.labelPortionDiet_3.sizePolicy().hasHeightForWidth())
        self.labelPortionDiet_3.setSizePolicy(sizePolicy)
        self.labelPortionDiet_3.setFrameShape(QFrame.NoFrame)
        self.labelPortionDiet_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.labelPortionDiet_3, 7, 2, 1, 3)

        self.sbSpoilage = QSpinBox(LaCropParameterManagerBase)
        self.sbSpoilage.setObjectName(u"sbSpoilage")
        self.sbSpoilage.setMaximum(100)

        self.gridLayout.addWidget(self.sbSpoilage, 7, 5, 1, 1)

        self.spacerItem2 = QSpacerItem(181, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem2, 8, 0, 1, 2)

        self.pbnApply = QPushButton(LaCropParameterManagerBase)
        self.pbnApply.setObjectName(u"pbnApply")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pbnApply.sizePolicy().hasHeightForWidth())
        self.pbnApply.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pbnApply, 8, 2, 1, 1)

        self.pbnClose = QPushButton(LaCropParameterManagerBase)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy2.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pbnClose, 8, 3, 1, 3)

        QWidget.setTabOrder(self.tblCropParameterProfiles, self.pbnImport)
        QWidget.setTabOrder(self.pbnImport, self.pbnExport)
        QWidget.setTabOrder(self.pbnExport, self.toolNew)
        QWidget.setTabOrder(self.toolNew, self.toolCopy)
        QWidget.setTabOrder(self.toolCopy, self.toolDelete)
        QWidget.setTabOrder(self.toolDelete, self.leName)
        QWidget.setTabOrder(self.leName, self.leDescription)
        QWidget.setTabOrder(self.leDescription, self.cboCrop)
        QWidget.setTabOrder(self.cboCrop, self.checkBoxUseCommonLand)
        QWidget.setTabOrder(self.checkBoxUseCommonLand, self.checkBoxUseSpecificLand)
        QWidget.setTabOrder(self.checkBoxUseSpecificLand, self.sbFallowRatio)
        QWidget.setTabOrder(self.sbFallowRatio, self.sbFallowValue)
        QWidget.setTabOrder(self.sbFallowValue, self.cbAreaUnits)
        QWidget.setTabOrder(self.cbAreaUnits, self.pbnApply)
        QWidget.setTabOrder(self.pbnApply, self.pbnClose)

        self.retranslateUi(LaCropParameterManagerBase)
        self.pbnClose.pressed.connect(LaCropParameterManagerBase.close)
        self.checkBoxUseSpecificLand.clicked.connect(self.checkBoxUseCommonLand.toggle)
        self.checkBoxUseCommonLand.clicked.connect(self.checkBoxUseSpecificLand.toggle)

        QMetaObject.connectSlotsByName(LaCropParameterManagerBase)
    # setupUi

    def retranslateUi(self, LaCropParameterManagerBase):
        LaCropParameterManagerBase.setWindowTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop Parameter Manager", None))
        self.grpProfiles.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Available Crop Parameter Settings", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolCopy.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new parameter that is similar to one already defined, you can clone this parameter to save time. All of the settings of the parameter you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the parameter you are cloning was).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolCopy.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
        self.lblCropPic.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"No Graphic\n"
"Selected", None))
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolNew.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Crop Parameter Manager, you are just editing the parameter currently selected. To create a new parameter, you <span style=\" font-weight:600;\">must</span> click on the New button.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolNew.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"...", None))
        self.pbnImport.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Export", None))
        ___qtablewidgetitem = self.tblCropParameterProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblCropParameterProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Name", None));
#if QT_CONFIG(tooltip)
        self.tblCropParameterProfiles.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a parameter here to see and/or edit it's properties below.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblCropParameterProfiles.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model crops, several details must be supplied. Crop Parameter Manager asks for these specifics. As with Crop Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same crop, follow the same procedure as for defining multiple crops with the same name. Let's say you want to have two parameters set up for Wheat as an example. The Name: field is Wheat for both, but "
                        "in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Name:", None))
#if QT_CONFIG(whatsthis)
        self.leName.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the crop parameter you are defining in this field. You do not need a unique name. You can have, for example, 10 different crop parameters defined, all named \"Jericho\". Landuse Analyst uses a special method of saving the crop to eliminate the issue of duplicate filenames. This way, you can have, for example, conservative and optimistic settings for each crop at a site. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.grpCropRotation.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If crops were rotated, the checkbox needs to be checked. The variables for crop rotation are unavailable until this has been done.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Keep in mind that animals can graze the fallow land. Because of this, you will need to estimate what the food value from the fallow land would have been, similar to what needs to be done when defining grazing land.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.grpCropRotation.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop Rotation", None))
#if QT_CONFIG(tooltip)
        self.labelFallow1.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFallow1.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Ratio", None))
        self.labelFallow3.setText(QCoreApplication.translate("LaCropParameterManagerBase", u" 1: ", None))
#if QT_CONFIG(tooltip)
        self.sbFallowRatio.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fallow Ratio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbFallowRatio.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When crop rotation is used, this field must be set. If the land grows a crop one year, and is left fallow the next, then the crop to fallow ratio is 1:1 so you would set the value to 1. For more complicated rotations, such as a cereal-legume-fallow rotation, it gets slightly more complicated. That situation would be one year out of three fallow and two years out of three crop. In this case, the setting would be 0.50 which might seem confusing.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Just remember that you need to <span style=\" font-weight:600;\">divi"
                        "de the </span><span style=\" font-weight:600; font-style:italic;\">number of years of fallow</span><span style=\" font-weight:600;\"> by the </span><span style=\" font-weight:600; font-style:italic;\">number of years of crop</span> to set this properly.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelFallow5.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFallow5.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop:Fallow ", None))
        self.labelFallow2.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Fallow's Food Value", None))
#if QT_CONFIG(tooltip)
        self.sbFallowValue.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food Value of Fallow Land</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbFallowValue.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the selected crop is being grown in a rotation, producing fallow land, that land can be grazed. Landuse Analyst needs to know how many calories this land can give grazing animals per year. These numbers are in KCalories per dunum/hectare. (you can select the area units)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbFallowValue.setSuffix("")
#if QT_CONFIG(tooltip)
        self.cbAreaUnits.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Notes:", None))
#if QT_CONFIG(whatsthis)
        self.leDescription.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because Landuse Analyst allows more than one type of parameter to be defined, the Notes: field allows you to give a brief description of the the parameter. For example, you may have two \"Shuna\" parameters defined, and the Notes: fields could contain \"Conservative\" and \"Optimistic\" to distinguish between them.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Crop:", None))
#if QT_CONFIG(tooltip)
        self.cboCrop.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Crop that these parameters are for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cboCrop.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is very important to select which crop your parameter settings are for. Once you slect the crop it appies to, simply click Apply, and it will then be properly allocated, and will show up in the dropdown list for that crop in the table on the top.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.groupBoxSuitableLand.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order for Landuse Analyst to create landuse maps, you must first create land suitability files to tell it what land is suitable for use by the crops and the crops. These files can be produced manually or automatically, but at the moment both must be done with external tools like QGis or GRASS. Future versions of Landuse Analyst will have the required features of these programs incorporated into it, but for now this step must be done externally. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxSuitableLand.setTitle(QCoreApplication.translate("LaCropParameterManagerBase", u"Suitability Masks", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseCommonLand.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"binary raster named: pigmask", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.checkBoxUseCommonLand.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes land is suitable for growing more than one type of crop. Landuse Analyst allows you to designate one suitability mask as common. Note that you can specify a crop to use both common land and specific land at the same time. If this is the case, equal preference is given to all crops using the common land.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxUseCommonLand.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Common Land", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseSpecificLand.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"binary raster named: pigmask", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.checkBoxUseSpecificLand.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes you may want to specify that land is suitable for growing only one type of crop. Landuse Analyst allows you to designate a land suitability mask as being unique to a certain crop. Note that you can specify a crop to use both common land and specific land at the same time. For more detailed information on this, see the help section on Crop Masks Common.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxUseSpecificLand.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Specific Land", None))
        self.label_3.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Raster\n"
"Mask", None))
        self.labelPortionDiet.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Portion of Tame Plant Diet", None))
        self.sbPercentTameCrop.setSuffix(QCoreApplication.translate("LaCropParameterManagerBase", u"%", None))
        self.labelPortionDiet_2.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Percent of harvest to re-seed", None))
        self.sbReseed.setSuffix(QCoreApplication.translate("LaCropParameterManagerBase", u"%", None))
        self.labelPortionDiet_3.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Percent of harvest to spoilage", None))
        self.sbSpoilage.setSuffix(QCoreApplication.translate("LaCropParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.pbnApply.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnApply.setWhatsThis(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a parameter, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as Landuse Analyst has a special way of saving parameters to allow for duplicate parameter names. It is helpful, however, to utilize the Notes field to distinguish between same-named parameter definitions.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnApply.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.pbnClose.setToolTip(QCoreApplication.translate("LaCropParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbnClose.setText(QCoreApplication.translate("LaCropParameterManagerBase", u"Close", None))
    # retranslateUi

