# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laanimalparametermanagerbase.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)
import resources_rc

class Ui_LaAnimalParameterManagerBase(object):
    def setupUi(self, LaAnimalParameterManagerBase):
        if not LaAnimalParameterManagerBase.objectName():
            LaAnimalParameterManagerBase.setObjectName(u"LaAnimalParameterManagerBase")
        LaAnimalParameterManagerBase.resize(587, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LaAnimalParameterManagerBase.sizePolicy().hasHeightForWidth())
        LaAnimalParameterManagerBase.setSizePolicy(sizePolicy)
        LaAnimalParameterManagerBase.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/la_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        LaAnimalParameterManagerBase.setWindowIcon(icon)
        self.gridLayout_4 = QGridLayout(LaAnimalParameterManagerBase)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(LaAnimalParameterManagerBase)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.grpProfiles = QGroupBox(self.splitter)
        self.grpProfiles.setObjectName(u"grpProfiles")
        self.gridLayout_2 = QGridLayout(self.grpProfiles)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tblAnimalParameterProfiles = QTableWidget(self.grpProfiles)
        if (self.tblAnimalParameterProfiles.columnCount() < 2):
            self.tblAnimalParameterProfiles.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAnimalParameterProfiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAnimalParameterProfiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblAnimalParameterProfiles.setObjectName(u"tblAnimalParameterProfiles")
        self.tblAnimalParameterProfiles.setAlternatingRowColors(True)
        self.tblAnimalParameterProfiles.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAnimalParameterProfiles.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tblAnimalParameterProfiles, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(6)
#endif
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon1 = QIcon()
        icon1.addFile(u":/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolCopy.setIcon(icon1)

        self.gridLayout.addWidget(self.toolCopy, 3, 1, 1, 1)

        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon2 = QIcon()
        icon2.addFile(u":/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon2)

        self.gridLayout.addWidget(self.toolDelete, 3, 2, 1, 1)

        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon3 = QIcon()
        icon3.addFile(u":/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolNew.setIcon(icon3)

        self.gridLayout.addWidget(self.toolNew, 3, 0, 1, 1)

        self.lblAnimalPic = QLabel(self.grpProfiles)
        self.lblAnimalPic.setObjectName(u"lblAnimalPic")
        self.lblAnimalPic.setMinimumSize(QSize(100, 100))
        self.lblAnimalPic.setMaximumSize(QSize(100, 100))
        self.lblAnimalPic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblAnimalPic, 0, 0, 1, 3)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.splitter.addWidget(self.grpProfiles)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout1 = QGridLayout(self.groupBox)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.hboxLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
#endif
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.hboxLayout.addWidget(self.label)

        self.leName = QLineEdit(self.groupBox)
        self.leName.setObjectName(u"leName")
        self.leName.setMinimumSize(QSize(0, 21))

        self.hboxLayout.addWidget(self.leName)


        self.gridLayout1.addLayout(self.hboxLayout, 0, 0, 1, 2)

        self.hboxLayout1 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout1.setSpacing(6)
#endif
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.hboxLayout1.addWidget(self.label_4)

        self.leDescription = QLineEdit(self.groupBox)
        self.leDescription.setObjectName(u"leDescription")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leDescription.sizePolicy().hasHeightForWidth())
        self.leDescription.setSizePolicy(sizePolicy2)
        self.leDescription.setMinimumSize(QSize(0, 21))

        self.hboxLayout1.addWidget(self.leDescription)


        self.gridLayout1.addLayout(self.hboxLayout1, 1, 0, 1, 2)

        self.hboxLayout2 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout2.setSpacing(6)
#endif
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.hboxLayout2.addWidget(self.label_2)

        self.cboAnimal = QComboBox(self.groupBox)
        self.cboAnimal.setObjectName(u"cboAnimal")
        self.cboAnimal.setMinimumSize(QSize(0, 21))

        self.hboxLayout2.addWidget(self.cboAnimal)


        self.gridLayout1.addLayout(self.hboxLayout2, 2, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout1.addWidget(self.label_3, 3, 0, 1, 1)

        self.cboRaster = QComboBox(self.groupBox)
        self.cboRaster.setObjectName(u"cboRaster")
        sizePolicy2.setHeightForWidth(self.cboRaster.sizePolicy().hasHeightForWidth())
        self.cboRaster.setSizePolicy(sizePolicy2)

        self.gridLayout1.addWidget(self.cboRaster, 3, 1, 1, 1)

        self.cbFallowUsage = QComboBox(self.groupBox)
        self.cbFallowUsage.setObjectName(u"cbFallowUsage")
        sizePolicy2.setHeightForWidth(self.cbFallowUsage.sizePolicy().hasHeightForWidth())
        self.cbFallowUsage.setSizePolicy(sizePolicy2)

        self.gridLayout1.addWidget(self.cbFallowUsage, 4, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.grpFodderUse = QGroupBox(self.widget)
        self.grpFodderUse.setObjectName(u"grpFodderUse")
        self.grpFodderUse.setMinimumSize(QSize(343, 0))
        self.grpFodderUse.setCheckable(True)
        self.grpFodderUse.setChecked(False)
        self.gridLayout_5 = QGridLayout(self.grpFodderUse)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tblFodder = QTableWidget(self.grpFodderUse)
        if (self.tblFodder.columnCount() < 4):
            self.tblFodder.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblFodder.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblFodder.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblFodder.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblFodder.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.tblFodder.setObjectName(u"tblFodder")
        self.tblFodder.setAlternatingRowColors(True)
        self.tblFodder.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblFodder.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblFodder.setShowGrid(False)

        self.gridLayout_5.addWidget(self.tblFodder, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.grpFodderUse, 0, 1, 3, 4)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout2 = QGridLayout(self.groupBox_3)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.hboxLayout3 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout3.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout3.setContentsMargins(0, 0, 0, 0)
#endif
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.checkBoxCommonRaster = QCheckBox(self.groupBox_3)
        self.checkBoxCommonRaster.setObjectName(u"checkBoxCommonRaster")

        self.hboxLayout3.addWidget(self.checkBoxCommonRaster)

        self.sbCommonRasterValue = QSpinBox(self.groupBox_3)
        self.sbCommonRasterValue.setObjectName(u"sbCommonRasterValue")
        sizePolicy2.setHeightForWidth(self.sbCommonRasterValue.sizePolicy().hasHeightForWidth())
        self.sbCommonRasterValue.setSizePolicy(sizePolicy2)
        self.sbCommonRasterValue.setReadOnly(True)
        self.sbCommonRasterValue.setMaximum(50000)
        self.sbCommonRasterValue.setSingleStep(1)
        self.sbCommonRasterValue.setValue(0)

        self.hboxLayout3.addWidget(self.sbCommonRasterValue)


        self.gridLayout2.addLayout(self.hboxLayout3, 0, 0, 1, 3)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout2.addWidget(self.line, 1, 0, 2, 3)

        self.checkBoxSpecificRaster = QCheckBox(self.groupBox_3)
        self.checkBoxSpecificRaster.setObjectName(u"checkBoxSpecificRaster")
        self.checkBoxSpecificRaster.setChecked(True)
        self.checkBoxSpecificRaster.setTristate(False)

        self.gridLayout2.addWidget(self.checkBoxSpecificRaster, 3, 0, 1, 2)

        self.sbSpecificRasterValue = QSpinBox(self.groupBox_3)
        self.sbSpecificRasterValue.setObjectName(u"sbSpecificRasterValue")
        sizePolicy2.setHeightForWidth(self.sbSpecificRasterValue.sizePolicy().hasHeightForWidth())
        self.sbSpecificRasterValue.setSizePolicy(sizePolicy2)
        self.sbSpecificRasterValue.setMinimum(1)
        self.sbSpecificRasterValue.setMaximum(500000)
        self.sbSpecificRasterValue.setSingleStep(1)
        self.sbSpecificRasterValue.setValue(10)

        self.gridLayout2.addWidget(self.sbSpecificRasterValue, 2, 2, 2, 1)

        self.cbSpecificLandEnergyType = QComboBox(self.groupBox_3)
        self.cbSpecificLandEnergyType.setObjectName(u"cbSpecificLandEnergyType")

        self.gridLayout2.addWidget(self.cbSpecificLandEnergyType, 4, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_5, 4, 1, 1, 1)

        self.cbAreaUnits = QComboBox(self.groupBox_3)
        self.cbAreaUnits.setObjectName(u"cbAreaUnits")
        sizePolicy2.setHeightForWidth(self.cbAreaUnits.sizePolicy().hasHeightForWidth())
        self.cbAreaUnits.setSizePolicy(sizePolicy2)

        self.gridLayout2.addWidget(self.cbAreaUnits, 4, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(173, 0))
        self.gridLayout3 = QGridLayout(self.groupBox_2)
        self.gridLayout3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.sbPercentTameMeat = QDoubleSpinBox(self.groupBox_2)
        self.sbPercentTameMeat.setObjectName(u"sbPercentTameMeat")
        self.sbPercentTameMeat.setAccelerated(True)
        self.sbPercentTameMeat.setMaximum(100.000000000000000)
        self.sbPercentTameMeat.setSingleStep(0.010000000000000)

        self.gridLayout3.addWidget(self.sbPercentTameMeat, 0, 0, 1, 1)

        self.pbnMore = QPushButton(self.groupBox_2)
        self.pbnMore.setObjectName(u"pbnMore")
        self.pbnMore.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pbnMore.sizePolicy().hasHeightForWidth())
        self.pbnMore.setSizePolicy(sizePolicy3)
        self.pbnMore.setMaximumSize(QSize(41, 22))

        self.gridLayout3.addWidget(self.pbnMore, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 2, 1)

        self.pbnImport = QPushButton(self.widget)
        self.pbnImport.setObjectName(u"pbnImport")
        sizePolicy2.setHeightForWidth(self.pbnImport.sizePolicy().hasHeightForWidth())
        self.pbnImport.setSizePolicy(sizePolicy2)
        self.pbnImport.setMinimumSize(QSize(80, 0))

        self.gridLayout_3.addWidget(self.pbnImport, 3, 1, 1, 1)

        self.pbnExport = QPushButton(self.widget)
        self.pbnExport.setObjectName(u"pbnExport")
        self.pbnExport.setMinimumSize(QSize(80, 0))

        self.gridLayout_3.addWidget(self.pbnExport, 3, 2, 1, 1)

        self.pbnApply = QPushButton(self.widget)
        self.pbnApply.setObjectName(u"pbnApply")
        sizePolicy2.setHeightForWidth(self.pbnApply.sizePolicy().hasHeightForWidth())
        self.pbnApply.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pbnApply, 3, 3, 1, 1)

        self.pbnClose = QPushButton(self.widget)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy2.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pbnClose, 3, 4, 1, 1)

        self.splitter.addWidget(self.widget)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)

        self.grpProfiles.raise_()
        self.pbnImport.raise_()
        self.pbnApply.raise_()
        self.grpFodderUse.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.pbnExport.raise_()
        QWidget.setTabOrder(self.tblAnimalParameterProfiles, self.toolNew)
        QWidget.setTabOrder(self.toolNew, self.toolCopy)
        QWidget.setTabOrder(self.toolCopy, self.toolDelete)
        QWidget.setTabOrder(self.toolDelete, self.leName)
        QWidget.setTabOrder(self.leName, self.leDescription)
        QWidget.setTabOrder(self.leDescription, self.cboAnimal)
        QWidget.setTabOrder(self.cboAnimal, self.checkBoxSpecificRaster)
        QWidget.setTabOrder(self.checkBoxSpecificRaster, self.checkBoxCommonRaster)
        QWidget.setTabOrder(self.checkBoxCommonRaster, self.sbSpecificRasterValue)
        QWidget.setTabOrder(self.sbSpecificRasterValue, self.sbCommonRasterValue)
        QWidget.setTabOrder(self.sbCommonRasterValue, self.cbAreaUnits)
        QWidget.setTabOrder(self.cbAreaUnits, self.cbFallowUsage)
        QWidget.setTabOrder(self.cbFallowUsage, self.pbnClose)

        self.retranslateUi(LaAnimalParameterManagerBase)
        self.pbnClose.clicked.connect(LaAnimalParameterManagerBase.close)
        self.checkBoxSpecificRaster.clicked.connect(self.checkBoxCommonRaster.toggle)
        self.checkBoxCommonRaster.clicked.connect(self.checkBoxSpecificRaster.toggle)

        QMetaObject.connectSlotsByName(LaAnimalParameterManagerBase)
    # setupUi

    def retranslateUi(self, LaAnimalParameterManagerBase):
        LaAnimalParameterManagerBase.setWindowTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Animal Parameter Manager", None))
#if QT_CONFIG(whatsthis)
        self.grpProfiles.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for the specific information about the animal which tells the program how the animal was fed, and how big a part of the settlements diet it was. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals"
                        " with the same name. Let's say you want to have two parameters set up for cows as an example. The Name: field is Cow for both, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will ahve these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.grpProfiles.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Available Animal Parameter Settings", None))
        ___qtablewidgetitem = self.tblAnimalParameterProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblAnimalParameterProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Name", None));
#if QT_CONFIG(tooltip)
        self.tblAnimalParameterProfiles.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a parameter here to see and/or edit it's properties below.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblAnimalParameterProfiles.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for these specifics. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals with the same name. Let's say you want to have two parameters set up for Cows as an example. The Name: field is Cow for bot"
                        "h, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolCopy.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new parameter that is similar to one already defined, you can clone this parameter to save time. All of the settings of the parameter you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the parameter you are cloning was).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolCopy.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new parameter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolNew.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Animal Parameter Manager, you are just editing the parameter currently selected. To create a new parameter, you <span style=\" font-weight:600;\">must</span> click on the New button.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolNew.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
        self.lblAnimalPic.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"No Graphic\n"
"Selected", None))
        self.groupBox.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Details", None))
        self.label.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Name:", None))
#if QT_CONFIG(whatsthis)
        self.leName.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the animal parameter you are defining in this field. You do not need a unique name. You can have, for example, 10 different animal parameters defined, all named \"Jericho\". Landuse Analyst uses a special method of saving the animals to eliminate the issue of duplicate filenames. This way, you can have, for example, conservative and optimistic settings for each animal at a site.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Notes:", None))
#if QT_CONFIG(whatsthis)
        self.leDescription.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because Landuse Analyst allows more than one type of parameter to be defined, the Notes: field allows you to give a brief description of the the parameter. For example, you may have two \"Shuna\" parameters defined, and the Notes: fields could contain \"Conservative\" and \"Optimistic\" to distinguish between them.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Animal:", None))
#if QT_CONFIG(tooltip)
        self.cboAnimal.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal that these parameters are for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cboAnimal.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is very important to select which animal your parameter settings are for. Once you slect the animal it appies to, simply click Apply, and it will then be properly allocated, and will show up in the dropdown list for that animal in the table on the top.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Raster Mask ", None))
#if QT_CONFIG(tooltip)
        self.cbFallowUsage.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your animal is to be allowed to graze fallow land resulting from crop rotation, set the priority of their access to this fallow land here.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cbFallowUsage.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst allows animals to utilize fallow crop land as grazing land. There are many difficult aspects to including this in a model, but these difficulties are mostly transparent to the user. Essentially, you need to indicate only whether the animal will be allowed to graze fallow, and if so, what is it's access priority in relation to the other animals grazing the same fallow land. Given this, the software handles the rest!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because some animals may have been given preferential access to the fallow land, Landuse Analyst has given three different priority levels to fallow access. The software first looks at the HIGH priority animals, and designates all fallow land to them, until either their needs are satisfied, or the available fallow land is all used. If there is more than enough fallow land for the HIGH priority animals, the remaining amount is then made available to the MED priority animals, and this repeats for the LOW priority ones as well.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.grpFodderUse.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your settlement fed the animal fodder, check off the Fodder section to enable the Fodder options to be accessible. Straw/Chaff is a percentage of what is available.  Grain is a percentage of the animals diet.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.grpFodderUse.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Select Fodder if you believe the animals were fed grain to supplement their grazing.  You will then have to select how many kg of the selected grain you believe they fed each animal either every day, week, or month.", None))
#endif // QT_CONFIG(whatsthis)
        self.grpFodderUse.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Fodder", None))
        ___qtablewidgetitem2 = self.tblFodder.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Used", None));
        ___qtablewidgetitem3 = self.tblFodder.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Crop", None));
        ___qtablewidgetitem4 = self.tblFodder.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Fodder", None));
        ___qtablewidgetitem5 = self.tblFodder.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Grain", None));
#if QT_CONFIG(tooltip)
        self.tblFodder.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The animal selected here will be displayed below.  If the animal is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each animal being modelled.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblFodder.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal Interface has been designed to be very simple and easy to use. The top section lists all of the defined animals, and selecting one will display its settings in the two lower sections. The lower sections are divided into the animal definition details on the left, and the model parameter settings for the currently selected animal on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the animal or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.groupBox_3.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order for Landuse Analyst to create landuse maps, you must first create land suitability files to tell it what land is suitable for use by the crops and the animals. These files can be produced manually or automatically, but at the moment both must be done with external tools like QGis or GRASS. Future versions of Landuse Analyst will have the required features of these programs incorporated into it, but for now this step must be done externally. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox_3.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Land Suitability Selection", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named common.grazing.mask which more than one animal can graze from</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Common Land", None))
#if QT_CONFIG(tooltip)
        self.sbCommonRasterValue.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TDN loaded from main form</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCommonRasterValue.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0000ff;\">This value </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">MUST</span><span style=\" font-weight:600; color:#0000ff;\"> be the same for all animals grazing common land.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes land is suitable for grazing by more than one type of animal. Landuse Analyst allows you to designate one suitability mask as common grazing land. Note that you can specify an animal to use both common land and specific land at t"
                        "he same time. If this is the case, equal preference is given to all animals grazing the common land. This is not always ideal, as it may have been the case that some animals were given preference to the common land if the other suitable land was further away than the other animals using it.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A workaround for this problem is that Landuse Analyst produces classified maps of the land being used, so if it is the case that you find one animal being forced to travel much further than others, you can simply change settings to balance this. This can be accomplished by removing the other animals one at a time from using the common grazing land. It may be the case, however, that there is no ideal solution, and that they simply had to travel the extra distance!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Not"
                        "e that this setting is the number of KCalories per land area unit available for grazing animals <span style=\" font-weight:600;\">per year</span>.  This value applies to all of the land selected in the common raster mask file.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbCommonRasterValue.setSuffix("")
        self.sbCommonRasterValue.setPrefix("")
#if QT_CONFIG(tooltip)
        self.checkBoxSpecificRaster.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named: animalName.mask  where animalName is the name of the animal you are setting these parameters for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.checkBoxSpecificRaster.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes you may want to specify that land is suitable for grazing by only one type of animal. Landuse Analyst allows you to designate a land suitability mask as being unique to that animal. Note that you can specify an animal to use both common land and specific land at the same time. For more detailed information on this, see the help section on Animal Common Land.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBoxSpecificRaster.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Specific Land", None))
#if QT_CONFIG(tooltip)
        self.sbSpecificRasterValue.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TDN (Total Digestive Nutrients) available</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbSpecificRasterValue.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note that this setting is the number of KCalories per land area unit available for grazing animals <span style=\" font-weight:600;\">per year</span>.  This value applies to only the land selected in the unique raster mask file created for this animal.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbSpecificRasterValue.setSuffix("")
        self.sbSpecificRasterValue.setPrefix("")
        self.label_5.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"per  ", None))
#if QT_CONFIG(tooltip)
        self.cbAreaUnits.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cbAreaUnits.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox_2.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Portion of Domestic Meat Diet", None))
        self.sbPercentTameMeat.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.pbnMore.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click here to get help determining this figure</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbnMore.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"More", None))
        self.pbnImport.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Export", None))
#if QT_CONFIG(tooltip)
        self.pbnApply.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnApply.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a parameter, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as Landuse Analyst has a special way of saving parameters to allow for duplicate parameter names. It is helpful, however, to utilize the Notes field to distinguish between same-named parameter definitions.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnApply.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.pbnClose.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbnClose.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Close", None))
    # retranslateUi

