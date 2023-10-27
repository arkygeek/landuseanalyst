# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laanimalparameterbase.ui'
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
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_LaAnimalParameterManagerBase(object):
    def setupUi(self, LaAnimalParameterManagerBase):
        if not LaAnimalParameterManagerBase.objectName():
            LaAnimalParameterManagerBase.setObjectName(u"LaAnimalParameterManagerBase")
        LaAnimalParameterManagerBase.resize(513, 366)
        LaAnimalParameterManagerBase.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(LaAnimalParameterManagerBase)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxFodderUse = QGroupBox(LaAnimalParameterManagerBase)
        self.groupBoxFodderUse.setObjectName(u"groupBoxFodderUse")
        self.groupBoxFodderUse.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBoxFodderUse.setCheckable(True)
        self.groupBoxFodderUse.setChecked(False)
        self.gridLayout1 = QGridLayout(self.groupBoxFodderUse)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setContentsMargins(2, 2, 2, 2)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.labelFodderFodder = QLabel(self.groupBoxFodderUse)
        self.labelFodderFodder.setObjectName(u"labelFodderFodder")
        self.labelFodderFodder.setLayoutDirection(Qt.LeftToRight)
        self.labelFodderFodder.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelFodderFodder, 0, 1, 1, 2)

        self.labelFodderGrain = QLabel(self.groupBoxFodderUse)
        self.labelFodderGrain.setObjectName(u"labelFodderGrain")
        self.labelFodderGrain.setLayoutDirection(Qt.RightToLeft)
        self.labelFodderGrain.setAlignment(Qt.AlignCenter)

        self.gridLayout1.addWidget(self.labelFodderGrain, 0, 3, 1, 1)

        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout1.addItem(self.spacerItem, 0, 0, 1, 1)

        self.sbFodderLentilsGrain = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderLentilsGrain.setObjectName(u"sbFodderLentilsGrain")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbFodderLentilsGrain.sizePolicy().hasHeightForWidth())
        self.sbFodderLentilsGrain.setSizePolicy(sizePolicy)
        self.sbFodderLentilsGrain.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderLentilsGrain, 3, 3, 1, 1)

        self.sbFodderLentils = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderLentils.setObjectName(u"sbFodderLentils")
        sizePolicy.setHeightForWidth(self.sbFodderLentils.sizePolicy().hasHeightForWidth())
        self.sbFodderLentils.setSizePolicy(sizePolicy)
        self.sbFodderLentils.setMinimum(-3)
        self.sbFodderLentils.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderLentils, 3, 2, 1, 1)

        self.labelFodderLentils = QLabel(self.groupBoxFodderUse)
        self.labelFodderLentils.setObjectName(u"labelFodderLentils")

        self.gridLayout1.addWidget(self.labelFodderLentils, 3, 0, 1, 2)

        self.sbFodderBarleyGrain = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderBarleyGrain.setObjectName(u"sbFodderBarleyGrain")
        sizePolicy.setHeightForWidth(self.sbFodderBarleyGrain.sizePolicy().hasHeightForWidth())
        self.sbFodderBarleyGrain.setSizePolicy(sizePolicy)
        self.sbFodderBarleyGrain.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderBarleyGrain, 2, 3, 1, 1)

        self.sbFodderBarley = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderBarley.setObjectName(u"sbFodderBarley")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sbFodderBarley.sizePolicy().hasHeightForWidth())
        self.sbFodderBarley.setSizePolicy(sizePolicy1)
        self.sbFodderBarley.setMinimum(-3)
        self.sbFodderBarley.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderBarley, 2, 2, 1, 1)

        self.labelFodderBarley = QLabel(self.groupBoxFodderUse)
        self.labelFodderBarley.setObjectName(u"labelFodderBarley")

        self.gridLayout1.addWidget(self.labelFodderBarley, 2, 0, 1, 2)

        self.sbFodderWheatGrain = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderWheatGrain.setObjectName(u"sbFodderWheatGrain")
        sizePolicy1.setHeightForWidth(self.sbFodderWheatGrain.sizePolicy().hasHeightForWidth())
        self.sbFodderWheatGrain.setSizePolicy(sizePolicy1)
        self.sbFodderWheatGrain.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderWheatGrain, 1, 3, 1, 1)

        self.sbFodderWheat = QSpinBox(self.groupBoxFodderUse)
        self.sbFodderWheat.setObjectName(u"sbFodderWheat")
        sizePolicy1.setHeightForWidth(self.sbFodderWheat.sizePolicy().hasHeightForWidth())
        self.sbFodderWheat.setSizePolicy(sizePolicy1)
        self.sbFodderWheat.setMinimum(-3)
        self.sbFodderWheat.setMaximum(100)

        self.gridLayout1.addWidget(self.sbFodderWheat, 1, 2, 1, 1)

        self.labelFodderWheat = QLabel(self.groupBoxFodderUse)
        self.labelFodderWheat.setObjectName(u"labelFodderWheat")

        self.gridLayout1.addWidget(self.labelFodderWheat, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBoxFodderUse, 1, 2, 5, 3)

        self.cbFallowUsage = QComboBox(LaAnimalParameterManagerBase)
        self.cbFallowUsage.addItem("")
        self.cbFallowUsage.addItem("")
        self.cbFallowUsage.addItem("")
        self.cbFallowUsage.addItem("")
        self.cbFallowUsage.setObjectName(u"cbFallowUsage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbFallowUsage.sizePolicy().hasHeightForWidth())
        self.cbFallowUsage.setSizePolicy(sizePolicy2)
        self.cbFallowUsage.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.cbFallowUsage, 5, 0, 1, 2)

        self.sbUniqueRasterCalories = QSpinBox(LaAnimalParameterManagerBase)
        self.sbUniqueRasterCalories.setObjectName(u"sbUniqueRasterCalories")
        self.sbUniqueRasterCalories.setMaximum(99999999)
        self.sbUniqueRasterCalories.setSingleStep(100)
        self.sbUniqueRasterCalories.setValue(10000)

        self.gridLayout.addWidget(self.sbUniqueRasterCalories, 2, 1, 1, 1)

        self.cbGrazingUnits = QComboBox(LaAnimalParameterManagerBase)
        self.cbGrazingUnits.addItem("")
        self.cbGrazingUnits.addItem("")
        self.cbGrazingUnits.setObjectName(u"cbGrazingUnits")
        sizePolicy2.setHeightForWidth(self.cbGrazingUnits.sizePolicy().hasHeightForWidth())
        self.cbGrazingUnits.setSizePolicy(sizePolicy2)
        self.cbGrazingUnits.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.cbGrazingUnits, 4, 0, 1, 2)

        self.sbCommonRasterCalories = QSpinBox(LaAnimalParameterManagerBase)
        self.sbCommonRasterCalories.setObjectName(u"sbCommonRasterCalories")
        self.sbCommonRasterCalories.setMaximum(99999999)
        self.sbCommonRasterCalories.setSingleStep(100)
        self.sbCommonRasterCalories.setValue(10000)

        self.gridLayout.addWidget(self.sbCommonRasterCalories, 3, 1, 1, 1)

        self.checkBoxCommonRaster = QCheckBox(LaAnimalParameterManagerBase)
        self.checkBoxCommonRaster.setObjectName(u"checkBoxCommonRaster")

        self.gridLayout.addWidget(self.checkBoxCommonRaster, 3, 0, 1, 1)

        self.checkBoxUniqueRaster = QCheckBox(LaAnimalParameterManagerBase)
        self.checkBoxUniqueRaster.setObjectName(u"checkBoxUniqueRaster")

        self.gridLayout.addWidget(self.checkBoxUniqueRaster, 2, 0, 1, 1)

        self.sbPercentOfTameMeat = QSpinBox(LaAnimalParameterManagerBase)
        self.sbPercentOfTameMeat.setObjectName(u"sbPercentOfTameMeat")
        sizePolicy2.setHeightForWidth(self.sbPercentOfTameMeat.sizePolicy().hasHeightForWidth())
        self.sbPercentOfTameMeat.setSizePolicy(sizePolicy2)
        self.sbPercentOfTameMeat.setMaximum(100)
        self.sbPercentOfTameMeat.setValue(50)

        self.gridLayout.addWidget(self.sbPercentOfTameMeat, 1, 1, 1, 1)

        self.labelPortionDiet = QLabel(LaAnimalParameterManagerBase)
        self.labelPortionDiet.setObjectName(u"labelPortionDiet")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelPortionDiet.sizePolicy().hasHeightForWidth())
        self.labelPortionDiet.setSizePolicy(sizePolicy3)
        self.labelPortionDiet.setFrameShape(QFrame.NoFrame)
        self.labelPortionDiet.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.labelPortionDiet, 1, 0, 1, 1)

        self.pbnClose = QPushButton(LaAnimalParameterManagerBase)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy2.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pbnClose, 6, 4, 1, 1)

        self.pbnApply = QPushButton(LaAnimalParameterManagerBase)
        self.pbnApply.setObjectName(u"pbnApply")
        sizePolicy1.setHeightForWidth(self.pbnApply.sizePolicy().hasHeightForWidth())
        self.pbnApply.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.pbnApply, 6, 3, 1, 1)

        self.spacerItem1 = QSpacerItem(391, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem1, 6, 0, 1, 3)

        self.grpProfiles = QGroupBox(LaAnimalParameterManagerBase)
        self.grpProfiles.setObjectName(u"grpProfiles")
        self.gridLayout2 = QGridLayout(self.grpProfiles)
#ifndef Q_OS_MAC
        self.gridLayout2.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout2.setObjectName(u"gridLayout2")
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

        self.gridLayout2.addWidget(self.tblAnimalParameterProfiles, 0, 0, 1, 6)

        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon = QIcon()
        icon.addFile(u":/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolNew.setIcon(icon)

        self.gridLayout2.addWidget(self.toolNew, 1, 3, 1, 1)

        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon1 = QIcon()
        icon1.addFile(u":/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolCopy.setIcon(icon1)

        self.gridLayout2.addWidget(self.toolCopy, 1, 4, 1, 1)

        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon2 = QIcon()
        icon2.addFile(u":/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolDelete.setIcon(icon2)

        self.gridLayout2.addWidget(self.toolDelete, 1, 5, 1, 1)

        self.pbnImport = QPushButton(self.grpProfiles)
        self.pbnImport.setObjectName(u"pbnImport")
        self.pbnImport.setMinimumSize(QSize(80, 0))

        self.gridLayout2.addWidget(self.pbnImport, 1, 0, 1, 1)

        self.pbnExport = QPushButton(self.grpProfiles)
        self.pbnExport.setObjectName(u"pbnExport")
        self.pbnExport.setMinimumSize(QSize(80, 0))

        self.gridLayout2.addWidget(self.pbnExport, 1, 1, 1, 1)

        self.spacerItem2 = QSpacerItem(71, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout2.addItem(self.spacerItem2, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.grpProfiles, 0, 0, 1, 5)


        self.retranslateUi(LaAnimalParameterManagerBase)
        self.pbnClose.clicked.connect(LaAnimalParameterManagerBase.close)

        QMetaObject.connectSlotsByName(LaAnimalParameterManagerBase)
    # setupUi

    def retranslateUi(self, LaAnimalParameterManagerBase):
        LaAnimalParameterManagerBase.setWindowTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Animal Parameter Manager", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxFodderUse.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Select Fodder if you believe the animals were fed grain to supplement their grazing.  You will then have to select how many kg of the selected grain you believe they fed each animal either every day, week, or month.", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxFodderUse.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Fodder", None))
#if QT_CONFIG(tooltip)
        self.labelFodderFodder.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by <span style=\" font-weight:600;\">FODDER</span>.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0000ff;\">To use </span><span style=\" font-style:italic; color:#0000ff;\">all</span><span style=\" color:#0000ff;\"> that is available use a </span><span style=\" font-weight:600; color:#0000ff;\">negative number:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">-1</span> for HIGH priority"
                        " total utilization</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">-2</span> for MED priority total utilization</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">-3</span> for LOW priority total utilization</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFodderFodder.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Fodder", None))
        self.labelFodderGrain.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Grain", None))
#if QT_CONFIG(tooltip)
        self.sbFodderLentilsGrain.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by LENTILS</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderLentilsGrain.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.sbFodderLentils.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by <span style=\" color:#0000ff;\">LENTIL FODDER</span>.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderLentils.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.labelFodderLentils.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by LENTILS</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFodderLentils.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Lentils", None))
#if QT_CONFIG(tooltip)
        self.sbFodderBarleyGrain.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by BARLEY</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderBarleyGrain.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.sbFodderBarley.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by <span style=\" color:#0000ff;\">BARLEY FODDER</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderBarley.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.labelFodderBarley.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by BARLEY</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFodderBarley.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Barley", None))
#if QT_CONFIG(tooltip)
        self.sbFodderWheatGrain.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by WHEAT</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderWheatGrain.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.sbFodderWheat.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by <span style=\" color:#0000ff;\">WHEAT FODDER.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbFodderWheat.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u"%", None))
#if QT_CONFIG(tooltip)
        self.labelFodderWheat.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of animals diet provided by WHEAT</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFodderWheat.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Wheat", None))
        self.cbFallowUsage.setItemText(0, QCoreApplication.translate("LaAnimalParameterManagerBase", u"Do Not Graze Fallow", None))
        self.cbFallowUsage.setItemText(1, QCoreApplication.translate("LaAnimalParameterManagerBase", u"HIGH Fallow Priority", None))
        self.cbFallowUsage.setItemText(2, QCoreApplication.translate("LaAnimalParameterManagerBase", u"MED Fallow Priority", None))
        self.cbFallowUsage.setItemText(3, QCoreApplication.translate("LaAnimalParameterManagerBase", u"LOW Fallow Priority", None))

#if QT_CONFIG(tooltip)
        self.cbFallowUsage.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your animal is to be allowed to graze fallow land resulting from crop rotation, set the priority of their access to this fallow land here.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbUniqueRasterCalories.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u" KCal", None))
        self.cbGrazingUnits.setItemText(0, QCoreApplication.translate("LaAnimalParameterManagerBase", u"* KCal per Dunum per Year", None))
        self.cbGrazingUnits.setItemText(1, QCoreApplication.translate("LaAnimalParameterManagerBase", u"* KCal per Hectare per Year", None))

#if QT_CONFIG(tooltip)
        self.cbGrazingUnits.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbCommonRasterCalories.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u" KCal", None))
#if QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named common.grazing.mask which more than one animal can graze from</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxCommonRaster.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Common Grazing Land", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUniqueRaster.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named: animalName.mask  where animalName is the name of the animal you are setting these parameters for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUniqueRaster.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Specific Grazing Land", None))
#if QT_CONFIG(tooltip)
        self.sbPercentOfTameMeat.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This animal contiributes this percent towards the tame meat portion of the diet</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbPercentOfTameMeat.setSuffix(QCoreApplication.translate("LaAnimalParameterManagerBase", u" %", None))
        self.labelPortionDiet.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Portion of Tame Meat Diet", None))
        self.pbnClose.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Close", None))
        self.pbnApply.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Apply", None))
        self.grpProfiles.setTitle(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Available Animal Parameter Settings", None))
        ___qtablewidgetitem = self.tblAnimalParameterProfiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblAnimalParameterProfiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Name", None));
#if QT_CONFIG(whatsthis)
        self.tblAnimalParameterProfiles.setWhatsThis(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Table of the currently available layersets", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"New", None))
#endif // QT_CONFIG(tooltip)
        self.toolNew.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Clone", None))
#endif // QT_CONFIG(tooltip)
        self.toolCopy.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Delete", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"...", None))
        self.pbnImport.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaAnimalParameterManagerBase", u"Export", None))
    # retranslateUi

