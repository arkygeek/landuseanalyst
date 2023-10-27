# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lamainformbase.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_LaMainFormBase(object):
    def setupUi(self, LaMainFormBase):
        if not LaMainFormBase.objectName():
            LaMainFormBase.setObjectName(u"LaMainFormBase")
        LaMainFormBase.resize(1090, 783)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LaMainFormBase.sizePolicy().hasHeightForWidth())
        LaMainFormBase.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/la_icon_small.png", QSize(), QIcon.Normal, QIcon.Off)
        LaMainFormBase.setWindowIcon(icon)
        self.gridLayout = QGridLayout(LaMainFormBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(LaMainFormBase)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 2, 5, 1, 1)

        self.labelAnimalCheck = QLabel(LaMainFormBase)
        self.labelAnimalCheck.setObjectName(u"labelAnimalCheck")
        self.labelAnimalCheck.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelAnimalCheck, 2, 1, 1, 1)

        self.labelCropCheck = QLabel(LaMainFormBase)
        self.labelCropCheck.setObjectName(u"labelCropCheck")
        self.labelCropCheck.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCropCheck, 2, 3, 1, 1)

        self.label_3 = QLabel(LaMainFormBase)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.progressBarCalcs = QProgressBar(LaMainFormBase)
        self.progressBarCalcs.setObjectName(u"progressBarCalcs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarCalcs.sizePolicy().hasHeightForWidth())
        self.progressBarCalcs.setSizePolicy(sizePolicy1)
        self.progressBarCalcs.setMaximumSize(QSize(16777215, 10))
        self.progressBarCalcs.setValue(0)
        self.progressBarCalcs.setTextVisible(False)
        self.progressBarCalcs.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.progressBarCalcs, 3, 0, 1, 11)

        self.pushButtonLoad = QPushButton(LaMainFormBase)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")
        sizePolicy.setHeightForWidth(self.pushButtonLoad.sizePolicy().hasHeightForWidth())
        self.pushButtonLoad.setSizePolicy(sizePolicy)
        self.pushButtonLoad.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButtonLoad, 2, 8, 1, 1)

        self.pushButtonRun = QPushButton(LaMainFormBase)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        sizePolicy.setHeightForWidth(self.pushButtonRun.sizePolicy().hasHeightForWidth())
        self.pushButtonRun.setSizePolicy(sizePolicy)
        self.pushButtonRun.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButtonRun, 2, 7, 1, 1)

        self.pushButtonExit = QPushButton(LaMainFormBase)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        sizePolicy.setHeightForWidth(self.pushButtonExit.sizePolicy().hasHeightForWidth())
        self.pushButtonExit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButtonExit, 2, 10, 1, 1)

        self.pushButtonSave = QPushButton(LaMainFormBase)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        sizePolicy.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButtonSave, 2, 9, 1, 1)

        self.spacerItem = QSpacerItem(308, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 11)

        self.spacerItem1 = QSpacerItem(224, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem1, 2, 4, 1, 1)

        self.label_5 = QLabel(LaMainFormBase)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.spacerItem2 = QSpacerItem(223, 37, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem2, 2, 6, 1, 1)

        self.MainTabs = QTabWidget(LaMainFormBase)
        self.MainTabs.setObjectName(u"MainTabs")
        sizePolicy1.setHeightForWidth(self.MainTabs.sizePolicy().hasHeightForWidth())
        self.MainTabs.setSizePolicy(sizePolicy1)
        self.MainTabs.setMinimumSize(QSize(620, 280))
        self.MainTabs.setMaximumSize(QSize(16777215, 16777215))
        self.MainTabs.setTabShape(QTabWidget.Rounded)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.gridLayout1 = QGridLayout(self.main_tab)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.frame_2 = QFrame(self.main_tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(222, 230))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout2 = QGridLayout(self.frame_2)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setPixmap(QPixmap(u":/la_icon.png"))
        self.label_17.setScaledContents(False)

        self.gridLayout2.addWidget(self.label_17, 0, 0, 1, 1)

        self.lblVersion = QLabel(self.frame_2)
        self.lblVersion.setObjectName(u"lblVersion")
        self.lblVersion.setAlignment(Qt.AlignCenter)

        self.gridLayout2.addWidget(self.lblVersion, 1, 0, 1, 1)


        self.gridLayout1.addWidget(self.frame_2, 0, 0, 2, 1)

        self.groupBoxManualSiteEntry = QGroupBox(self.main_tab)
        self.groupBoxManualSiteEntry.setObjectName(u"groupBoxManualSiteEntry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxManualSiteEntry.sizePolicy().hasHeightForWidth())
        self.groupBoxManualSiteEntry.setSizePolicy(sizePolicy2)
        self.groupBoxManualSiteEntry.setCheckable(False)
        self.groupBoxManualSiteEntry.setChecked(False)
        self.gridLayout3 = QGridLayout(self.groupBoxManualSiteEntry)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.lineEditSiteName = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditSiteName.setObjectName(u"lineEditSiteName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEditSiteName.sizePolicy().hasHeightForWidth())
        self.lineEditSiteName.setSizePolicy(sizePolicy3)

        self.gridLayout3.addWidget(self.lineEditSiteName, 0, 1, 1, 2)

        self.sbPopulation = QSpinBox(self.groupBoxManualSiteEntry)
        self.sbPopulation.setObjectName(u"sbPopulation")
        sizePolicy.setHeightForWidth(self.sbPopulation.sizePolicy().hasHeightForWidth())
        self.sbPopulation.setSizePolicy(sizePolicy)
        self.sbPopulation.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbPopulation.setMinimum(1)
        self.sbPopulation.setMaximum(20000)
        self.sbPopulation.setSingleStep(1)
        self.sbPopulation.setValue(500)

        self.gridLayout3.addWidget(self.sbPopulation, 2, 1, 1, 1)

        self.lineEditPeriod = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditPeriod.setObjectName(u"lineEditPeriod")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(254)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEditPeriod.sizePolicy().hasHeightForWidth())
        self.lineEditPeriod.setSizePolicy(sizePolicy4)

        self.gridLayout3.addWidget(self.lineEditPeriod, 1, 1, 1, 1)

        self.textLabel2_4 = QLabel(self.groupBoxManualSiteEntry)
        self.textLabel2_4.setObjectName(u"textLabel2_4")
        self.textLabel2_4.setWordWrap(False)

        self.gridLayout3.addWidget(self.textLabel2_4, 0, 0, 1, 1)

        self.label = QLabel(self.groupBoxManualSiteEntry)
        self.label.setObjectName(u"label")

        self.gridLayout3.addWidget(self.label, 1, 0, 1, 1)

        self.label5 = QLabel(self.groupBoxManualSiteEntry)
        self.label5.setObjectName(u"label5")
        self.label5.setWordWrap(False)

        self.gridLayout3.addWidget(self.label5, 2, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label_6 = QLabel(self.groupBoxManualSiteEntry)
        self.label_6.setObjectName(u"label_6")

        self.hboxLayout.addWidget(self.label_6)

        self.lineEditEasting = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditEasting.setObjectName(u"lineEditEasting")

        self.hboxLayout.addWidget(self.lineEditEasting)


        self.gridLayout3.addLayout(self.hboxLayout, 1, 2, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label_22 = QLabel(self.groupBoxManualSiteEntry)
        self.label_22.setObjectName(u"label_22")

        self.hboxLayout1.addWidget(self.label_22)

        self.lineEditNorthing = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditNorthing.setObjectName(u"lineEditNorthing")

        self.hboxLayout1.addWidget(self.lineEditNorthing)


        self.gridLayout3.addLayout(self.hboxLayout1, 2, 2, 1, 1)


        self.gridLayout1.addWidget(self.groupBoxManualSiteEntry, 0, 1, 1, 1)

        self.model_method_box = QGroupBox(self.main_tab)
        self.model_method_box.setObjectName(u"model_method_box")
        sizePolicy.setHeightForWidth(self.model_method_box.sizePolicy().hasHeightForWidth())
        self.model_method_box.setSizePolicy(sizePolicy)
        self.gridLayout4 = QGridLayout(self.model_method_box)
        self.gridLayout4.setSpacing(0)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout4.setContentsMargins(8, 8, 8, 8)
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(0)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label_2 = QLabel(self.model_method_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout2.addWidget(self.label_2)

        self.sbModelPrecision = QSpinBox(self.model_method_box)
        self.sbModelPrecision.setObjectName(u"sbModelPrecision")
        sizePolicy.setHeightForWidth(self.sbModelPrecision.sizePolicy().hasHeightForWidth())
        self.sbModelPrecision.setSizePolicy(sizePolicy)
        self.sbModelPrecision.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbModelPrecision.setMinimum(1)
        self.sbModelPrecision.setMaximum(50)
        self.sbModelPrecision.setValue(5)

        self.hboxLayout2.addWidget(self.sbModelPrecision)


        self.gridLayout4.addLayout(self.hboxLayout2, 3, 0, 1, 1)

        self.radioButtonPathDistance = QRadioButton(self.model_method_box)
        self.radioButtonPathDistance.setObjectName(u"radioButtonPathDistance")

        self.gridLayout4.addWidget(self.radioButtonPathDistance, 2, 0, 1, 1)

        self.radioButtonWalkingTime = QRadioButton(self.model_method_box)
        self.radioButtonWalkingTime.setObjectName(u"radioButtonWalkingTime")
        self.radioButtonWalkingTime.setChecked(True)

        self.gridLayout4.addWidget(self.radioButtonWalkingTime, 1, 0, 1, 1)

        self.radioButtonEuclidean = QRadioButton(self.model_method_box)
        self.radioButtonEuclidean.setObjectName(u"radioButtonEuclidean")
        self.radioButtonEuclidean.setChecked(False)

        self.gridLayout4.addWidget(self.radioButtonEuclidean, 0, 0, 1, 1)


        self.gridLayout1.addWidget(self.model_method_box, 0, 2, 1, 1)

        self.gbxGrass = QGroupBox(self.main_tab)
        self.gbxGrass.setObjectName(u"gbxGrass")
        self.gridLayout5 = QGridLayout(self.gbxGrass)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.lblGrass = QLabel(self.gbxGrass)
        self.lblGrass.setObjectName(u"lblGrass")
        self.lblGrass.setMaximumSize(QSize(80, 80))
        self.lblGrass.setPixmap(QPixmap(u":/icona_grass.gif"))
        self.lblGrass.setScaledContents(True)

        self.gridLayout5.addWidget(self.lblGrass, 0, 0, 2, 1)

        self.label_29 = QLabel(self.gbxGrass)
        self.label_29.setObjectName(u"label_29")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy5)

        self.gridLayout5.addWidget(self.label_29, 0, 1, 1, 1)

        self.cboMapSet = QComboBox(self.gbxGrass)
        self.cboMapSet.setObjectName(u"cboMapSet")

        self.gridLayout5.addWidget(self.cboMapSet, 0, 2, 1, 1)

        self.label_24 = QLabel(self.gbxGrass)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout5.addWidget(self.label_24, 1, 1, 1, 1)

        self.cboDEM = QComboBox(self.gbxGrass)
        self.cboDEM.setObjectName(u"cboDEM")

        self.gridLayout5.addWidget(self.cboDEM, 1, 2, 1, 1)


        self.gridLayout1.addWidget(self.gbxGrass, 1, 1, 1, 2)

        self.spacerItem3 = QSpacerItem(308, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout1.addItem(self.spacerItem3, 2, 1, 1, 1)

        self.MainTabs.addTab(self.main_tab, "")
        self.diet_tab = QWidget()
        self.diet_tab.setObjectName(u"diet_tab")
        self.gridLayout6 = QGridLayout(self.diet_tab)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout6.addItem(self.spacerItem4, 1, 0, 1, 1)

        self.spacerItem5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout6.addItem(self.spacerItem5, 2, 1, 1, 1)

        self.diet_comp_box = QGroupBox(self.diet_tab)
        self.diet_comp_box.setObjectName(u"diet_comp_box")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.diet_comp_box.sizePolicy().hasHeightForWidth())
        self.diet_comp_box.setSizePolicy(sizePolicy6)
        self.gridLayout7 = QGridLayout(self.diet_comp_box)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.cboxBaseOnPlants = QCheckBox(self.diet_comp_box)
        self.cboxBaseOnPlants.setObjectName(u"cboxBaseOnPlants")
        self.cboxBaseOnPlants.setEnabled(False)

        self.hboxLayout3.addWidget(self.cboxBaseOnPlants)

        self.spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout3.addItem(self.spacerItem6)

        self.cboxIncludeDairy = QCheckBox(self.diet_comp_box)
        self.cboxIncludeDairy.setObjectName(u"cboxIncludeDairy")
        self.cboxIncludeDairy.setEnabled(False)
        self.cboxIncludeDairy.setLayoutDirection(Qt.RightToLeft)

        self.hboxLayout3.addWidget(self.cboxIncludeDairy)


        self.gridLayout7.addLayout(self.hboxLayout3, 0, 0, 1, 2)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.labelCropPercent = QLabel(self.diet_comp_box)
        self.labelCropPercent.setObjectName(u"labelCropPercent")

        self.hboxLayout4.addWidget(self.labelCropPercent)

        self.sliderDiet = QSlider(self.diet_comp_box)
        self.sliderDiet.setObjectName(u"sliderDiet")
        self.sliderDiet.setMaximum(100)
        self.sliderDiet.setSingleStep(1)
        self.sliderDiet.setPageStep(1)
        self.sliderDiet.setValue(50)
        self.sliderDiet.setSliderPosition(50)
        self.sliderDiet.setOrientation(Qt.Horizontal)
        self.sliderDiet.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet.setTickInterval(25)

        self.hboxLayout4.addWidget(self.sliderDiet)

        self.labelMeatPercent = QLabel(self.diet_comp_box)
        self.labelMeatPercent.setObjectName(u"labelMeatPercent")
        self.labelMeatPercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout4.addWidget(self.labelMeatPercent)


        self.gridLayout7.addLayout(self.hboxLayout4, 1, 0, 1, 2)

        self.groupplantpercent = QGroupBox(self.diet_comp_box)
        self.groupplantpercent.setObjectName(u"groupplantpercent")
        self.gridLayout8 = QGridLayout(self.groupplantpercent)
        self.gridLayout8.setObjectName(u"gridLayout8")
        self.spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout8.addItem(self.spacerItem7, 1, 1, 1, 1)

        self.labelCropTamePercent = QLabel(self.groupplantpercent)
        self.labelCropTamePercent.setObjectName(u"labelCropTamePercent")
        self.labelCropTamePercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout8.addWidget(self.labelCropTamePercent, 1, 2, 1, 1)

        self.sliderCrop = QSlider(self.groupplantpercent)
        self.sliderCrop.setObjectName(u"sliderCrop")
        self.sliderCrop.setMaximum(100)
        self.sliderCrop.setSingleStep(1)
        self.sliderCrop.setPageStep(1)
        self.sliderCrop.setValue(90)
        self.sliderCrop.setSliderPosition(90)
        self.sliderCrop.setOrientation(Qt.Horizontal)
        self.sliderCrop.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop.setTickInterval(25)

        self.gridLayout8.addWidget(self.sliderCrop, 2, 0, 1, 3)

        self.labelCropWildPercent = QLabel(self.groupplantpercent)
        self.labelCropWildPercent.setObjectName(u"labelCropWildPercent")
        self.labelCropWildPercent.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout8.addWidget(self.labelCropWildPercent, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupplantpercent)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout8.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupplantpercent)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout8.addWidget(self.label_11, 0, 2, 1, 1)

        self.spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout8.addItem(self.spacerItem8, 0, 1, 1, 1)


        self.gridLayout7.addWidget(self.groupplantpercent, 2, 0, 1, 1)

        self.groupmeatpercent = QGroupBox(self.diet_comp_box)
        self.groupmeatpercent.setObjectName(u"groupmeatpercent")
        self.groupmeatpercent.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout9 = QGridLayout(self.groupmeatpercent)
        self.gridLayout9.setObjectName(u"gridLayout9")
        self.spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout9.addItem(self.spacerItem9, 1, 1, 1, 1)

        self.spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout9.addItem(self.spacerItem10, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupmeatpercent)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout9.addWidget(self.label_14, 0, 0, 1, 1)

        self.labelMeatWildPercent = QLabel(self.groupmeatpercent)
        self.labelMeatWildPercent.setObjectName(u"labelMeatWildPercent")
        self.labelMeatWildPercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout9.addWidget(self.labelMeatWildPercent, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupmeatpercent)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout9.addWidget(self.label_13, 0, 2, 1, 1)

        self.labelMeatTamePercent = QLabel(self.groupmeatpercent)
        self.labelMeatTamePercent.setObjectName(u"labelMeatTamePercent")
        self.labelMeatTamePercent.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout9.addWidget(self.labelMeatTamePercent, 1, 0, 1, 1)

        self.sliderMeat = QSlider(self.groupmeatpercent)
        self.sliderMeat.setObjectName(u"sliderMeat")
        self.sliderMeat.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat.setMaximum(100)
        self.sliderMeat.setSingleStep(1)
        self.sliderMeat.setPageStep(1)
        self.sliderMeat.setValue(90)
        self.sliderMeat.setSliderPosition(90)
        self.sliderMeat.setOrientation(Qt.Horizontal)
        self.sliderMeat.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat.setTickInterval(25)

        self.gridLayout9.addWidget(self.sliderMeat, 2, 0, 1, 3)


        self.gridLayout7.addWidget(self.groupmeatpercent, 2, 1, 1, 1)

        self.line = QFrame(self.diet_comp_box)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout7.addWidget(self.line, 3, 0, 1, 2)

        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.label6 = QLabel(self.diet_comp_box)
        self.label6.setObjectName(u"label6")
        self.label6.setWordWrap(False)

        self.hboxLayout6.addWidget(self.label6)

        self.sbDailyCalories = QSpinBox(self.diet_comp_box)
        self.sbDailyCalories.setObjectName(u"sbDailyCalories")
        self.sbDailyCalories.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbDailyCalories.setMinimum(1)
        self.sbDailyCalories.setMaximum(5000)
        self.sbDailyCalories.setSingleStep(1)
        self.sbDailyCalories.setValue(2500)

        self.hboxLayout6.addWidget(self.sbDailyCalories)


        self.hboxLayout5.addLayout(self.hboxLayout6)

        self.line_2 = QFrame(self.diet_comp_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.hboxLayout5.addWidget(self.line_2)

        self.hboxLayout7 = QHBoxLayout()
        self.hboxLayout7.setObjectName(u"hboxLayout7")
        self.label6_2 = QLabel(self.diet_comp_box)
        self.label6_2.setObjectName(u"label6_2")
        self.label6_2.setWordWrap(False)

        self.hboxLayout7.addWidget(self.label6_2)

        self.sbDairyUtilisation = QSpinBox(self.diet_comp_box)
        self.sbDairyUtilisation.setObjectName(u"sbDairyUtilisation")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.sbDairyUtilisation.sizePolicy().hasHeightForWidth())
        self.sbDairyUtilisation.setSizePolicy(sizePolicy7)
        self.sbDairyUtilisation.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbDairyUtilisation.setMaximum(100)
        self.sbDairyUtilisation.setSingleStep(1)
        self.sbDairyUtilisation.setValue(100)

        self.hboxLayout7.addWidget(self.sbDairyUtilisation)

        self.line_8 = QFrame(self.diet_comp_box)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.hboxLayout7.addWidget(self.line_8)

        self.cboxLimitDairy = QCheckBox(self.diet_comp_box)
        self.cboxLimitDairy.setObjectName(u"cboxLimitDairy")

        self.hboxLayout7.addWidget(self.cboxLimitDairy)

        self.sbLimitDairyPercent = QSpinBox(self.diet_comp_box)
        self.sbLimitDairyPercent.setObjectName(u"sbLimitDairyPercent")
        self.sbLimitDairyPercent.setMaximum(100)

        self.hboxLayout7.addWidget(self.sbLimitDairyPercent)


        self.hboxLayout5.addLayout(self.hboxLayout7)


        self.gridLayout7.addLayout(self.hboxLayout5, 4, 0, 1, 2)

        self.spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout7.addItem(self.spacerItem11, 6, 1, 1, 1)

        self.labelDairySurplus = QLabel(self.diet_comp_box)
        self.labelDairySurplus.setObjectName(u"labelDairySurplus")

        self.gridLayout7.addWidget(self.labelDairySurplus, 5, 1, 1, 1)


        self.gridLayout6.addWidget(self.diet_comp_box, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.diet_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 200))
        self.gridLayout10 = QGridLayout(self.groupBox_2)
        self.gridLayout10.setObjectName(u"gridLayout10")
        self.hboxLayout8 = QHBoxLayout()
        self.hboxLayout8.setObjectName(u"hboxLayout8")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.hboxLayout8.addWidget(self.label_10)

        self.labelCaloriesSettlement = QLabel(self.groupBox_2)
        self.labelCaloriesSettlement.setObjectName(u"labelCaloriesSettlement")

        self.hboxLayout8.addWidget(self.labelCaloriesSettlement)

        self.label_37 = QLabel(self.groupBox_2)
        self.label_37.setObjectName(u"label_37")

        self.hboxLayout8.addWidget(self.label_37)


        self.gridLayout10.addLayout(self.hboxLayout8, 2, 0, 1, 1)

        self.hboxLayout9 = QHBoxLayout()
        self.hboxLayout9.setObjectName(u"hboxLayout9")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.hboxLayout9.addWidget(self.label_12)

        self.labelPortionPlants = QLabel(self.groupBox_2)
        self.labelPortionPlants.setObjectName(u"labelPortionPlants")

        self.hboxLayout9.addWidget(self.labelPortionPlants)

        self.label_38 = QLabel(self.groupBox_2)
        self.label_38.setObjectName(u"label_38")

        self.hboxLayout9.addWidget(self.label_38)


        self.gridLayout10.addLayout(self.hboxLayout9, 4, 0, 1, 1)

        self.hboxLayout10 = QHBoxLayout()
        self.hboxLayout10.setObjectName(u"hboxLayout10")
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.hboxLayout10.addWidget(self.label_16)

        self.labelPortionMeat = QLabel(self.groupBox_2)
        self.labelPortionMeat.setObjectName(u"labelPortionMeat")

        self.hboxLayout10.addWidget(self.labelPortionMeat)

        self.label_39 = QLabel(self.groupBox_2)
        self.label_39.setObjectName(u"label_39")

        self.hboxLayout10.addWidget(self.label_39)


        self.gridLayout10.addLayout(self.hboxLayout10, 5, 0, 1, 1)

        self.hboxLayout11 = QHBoxLayout()
        self.hboxLayout11.setObjectName(u"hboxLayout11")
        self.label_54 = QLabel(self.groupBox_2)
        self.label_54.setObjectName(u"label_54")

        self.hboxLayout11.addWidget(self.label_54)

        self.labelPortionAllDairy = QLabel(self.groupBox_2)
        self.labelPortionAllDairy.setObjectName(u"labelPortionAllDairy")

        self.hboxLayout11.addWidget(self.labelPortionAllDairy)

        self.label_55 = QLabel(self.groupBox_2)
        self.label_55.setObjectName(u"label_55")

        self.hboxLayout11.addWidget(self.label_55)


        self.gridLayout10.addLayout(self.hboxLayout11, 6, 0, 1, 1)

        self.hboxLayout12 = QHBoxLayout()
        self.hboxLayout12.setObjectName(u"hboxLayout12")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.hboxLayout12.addWidget(self.label_18)

        self.labelPortionCrops = QLabel(self.groupBox_2)
        self.labelPortionCrops.setObjectName(u"labelPortionCrops")

        self.hboxLayout12.addWidget(self.labelPortionCrops)

        self.label_40 = QLabel(self.groupBox_2)
        self.label_40.setObjectName(u"label_40")

        self.hboxLayout12.addWidget(self.label_40)


        self.gridLayout10.addLayout(self.hboxLayout12, 8, 0, 1, 1)

        self.hboxLayout13 = QHBoxLayout()
        self.hboxLayout13.setObjectName(u"hboxLayout13")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.hboxLayout13.addWidget(self.label_19)

        self.labelPortionTameMeat = QLabel(self.groupBox_2)
        self.labelPortionTameMeat.setObjectName(u"labelPortionTameMeat")

        self.hboxLayout13.addWidget(self.labelPortionTameMeat)

        self.label_41 = QLabel(self.groupBox_2)
        self.label_41.setObjectName(u"label_41")

        self.hboxLayout13.addWidget(self.label_41)


        self.gridLayout10.addLayout(self.hboxLayout13, 9, 0, 1, 1)

        self.hboxLayout14 = QHBoxLayout()
        self.hboxLayout14.setObjectName(u"hboxLayout14")
        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")

        self.hboxLayout14.addWidget(self.label_31)

        self.labelPortionDairy = QLabel(self.groupBox_2)
        self.labelPortionDairy.setObjectName(u"labelPortionDairy")

        self.hboxLayout14.addWidget(self.labelPortionDairy)

        self.label_42 = QLabel(self.groupBox_2)
        self.label_42.setObjectName(u"label_42")

        self.hboxLayout14.addWidget(self.label_42)


        self.gridLayout10.addLayout(self.hboxLayout14, 10, 0, 1, 1)

        self.hboxLayout15 = QHBoxLayout()
        self.hboxLayout15.setObjectName(u"hboxLayout15")
        self.label_51 = QLabel(self.groupBox_2)
        self.label_51.setObjectName(u"label_51")

        self.hboxLayout15.addWidget(self.label_51)

        self.labelPortionWildMeat = QLabel(self.groupBox_2)
        self.labelPortionWildMeat.setObjectName(u"labelPortionWildMeat")

        self.hboxLayout15.addWidget(self.labelPortionWildMeat)

        self.label_50 = QLabel(self.groupBox_2)
        self.label_50.setObjectName(u"label_50")

        self.hboxLayout15.addWidget(self.label_50)


        self.gridLayout10.addLayout(self.hboxLayout15, 12, 0, 1, 1)

        self.hboxLayout16 = QHBoxLayout()
        self.hboxLayout16.setObjectName(u"hboxLayout16")
        self.label_53 = QLabel(self.groupBox_2)
        self.label_53.setObjectName(u"label_53")

        self.hboxLayout16.addWidget(self.label_53)

        self.labelPortionWildPlants = QLabel(self.groupBox_2)
        self.labelPortionWildPlants.setObjectName(u"labelPortionWildPlants")

        self.hboxLayout16.addWidget(self.labelPortionWildPlants)

        self.label_52 = QLabel(self.groupBox_2)
        self.label_52.setObjectName(u"label_52")

        self.hboxLayout16.addWidget(self.label_52)


        self.gridLayout10.addLayout(self.hboxLayout16, 13, 0, 1, 1)

        self.hboxLayout17 = QHBoxLayout()
        self.hboxLayout17.setObjectName(u"hboxLayout17")
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.hboxLayout17.addWidget(self.label_23)

        self.labelCaloriesCrops = QLabel(self.groupBox_2)
        self.labelCaloriesCrops.setObjectName(u"labelCaloriesCrops")

        self.hboxLayout17.addWidget(self.labelCaloriesCrops)

        self.label_43 = QLabel(self.groupBox_2)
        self.label_43.setObjectName(u"label_43")

        self.hboxLayout17.addWidget(self.label_43)


        self.gridLayout10.addLayout(self.hboxLayout17, 15, 0, 1, 1)

        self.hboxLayout18 = QHBoxLayout()
        self.hboxLayout18.setObjectName(u"hboxLayout18")
        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.hboxLayout18.addWidget(self.label_21)

        self.labelCaloriesTameMeat = QLabel(self.groupBox_2)
        self.labelCaloriesTameMeat.setObjectName(u"labelCaloriesTameMeat")

        self.hboxLayout18.addWidget(self.labelCaloriesTameMeat)

        self.label_44 = QLabel(self.groupBox_2)
        self.label_44.setObjectName(u"label_44")

        self.hboxLayout18.addWidget(self.label_44)


        self.gridLayout10.addLayout(self.hboxLayout18, 16, 0, 1, 1)

        self.hboxLayout19 = QHBoxLayout()
        self.hboxLayout19.setObjectName(u"hboxLayout19")
        self.label_35 = QLabel(self.groupBox_2)
        self.label_35.setObjectName(u"label_35")

        self.hboxLayout19.addWidget(self.label_35)

        self.labelCaloriesDairy = QLabel(self.groupBox_2)
        self.labelCaloriesDairy.setObjectName(u"labelCaloriesDairy")

        self.hboxLayout19.addWidget(self.labelCaloriesDairy)

        self.label_45 = QLabel(self.groupBox_2)
        self.label_45.setObjectName(u"label_45")

        self.hboxLayout19.addWidget(self.label_45)


        self.gridLayout10.addLayout(self.hboxLayout19, 17, 0, 1, 1)

        self.hboxLayout20 = QHBoxLayout()
        self.hboxLayout20.setObjectName(u"hboxLayout20")
        self.label_46 = QLabel(self.groupBox_2)
        self.label_46.setObjectName(u"label_46")

        self.hboxLayout20.addWidget(self.label_46)

        self.labelCaloriesWildMeat = QLabel(self.groupBox_2)
        self.labelCaloriesWildMeat.setObjectName(u"labelCaloriesWildMeat")

        self.hboxLayout20.addWidget(self.labelCaloriesWildMeat)

        self.label_47 = QLabel(self.groupBox_2)
        self.label_47.setObjectName(u"label_47")

        self.hboxLayout20.addWidget(self.label_47)


        self.gridLayout10.addLayout(self.hboxLayout20, 19, 0, 1, 1)

        self.hboxLayout21 = QHBoxLayout()
        self.hboxLayout21.setObjectName(u"hboxLayout21")
        self.label_48 = QLabel(self.groupBox_2)
        self.label_48.setObjectName(u"label_48")

        self.hboxLayout21.addWidget(self.label_48)

        self.labelCaloriesWildPlants = QLabel(self.groupBox_2)
        self.labelCaloriesWildPlants.setObjectName(u"labelCaloriesWildPlants")

        self.hboxLayout21.addWidget(self.labelCaloriesWildPlants)

        self.label_49 = QLabel(self.groupBox_2)
        self.label_49.setObjectName(u"label_49")

        self.hboxLayout21.addWidget(self.label_49)


        self.gridLayout10.addLayout(self.hboxLayout21, 20, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout10.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout10.addWidget(self.label_15, 3, 0, 1, 1)

        self.line_5 = QFrame(self.groupBox_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout10.addWidget(self.line_5, 7, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout10.addWidget(self.label_20, 14, 0, 1, 1)

        self.line_4 = QFrame(self.groupBox_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout10.addWidget(self.line_4, 18, 0, 1, 1)

        self.line_7 = QFrame(self.groupBox_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout10.addWidget(self.line_7, 11, 0, 1, 1)

        self.hboxLayout22 = QHBoxLayout()
        self.hboxLayout22.setObjectName(u"hboxLayout22")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.hboxLayout22.addWidget(self.label_8)

        self.labelCaloriesIndividual = QLabel(self.groupBox_2)
        self.labelCaloriesIndividual.setObjectName(u"labelCaloriesIndividual")

        self.hboxLayout22.addWidget(self.labelCaloriesIndividual)

        self.label_36 = QLabel(self.groupBox_2)
        self.label_36.setObjectName(u"label_36")

        self.hboxLayout22.addWidget(self.label_36)


        self.gridLayout10.addLayout(self.hboxLayout22, 1, 0, 1, 1)


        self.gridLayout6.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.MainTabs.addTab(self.diet_tab, "")
        self.crops_tab = QWidget()
        self.crops_tab.setObjectName(u"crops_tab")
        self.gridLayout11 = QGridLayout(self.crops_tab)
        self.gridLayout11.setObjectName(u"gridLayout11")
        self.splitter_7 = QSplitter(self.crops_tab)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.hboxLayout23 = QHBoxLayout(self.layoutWidget)
        self.hboxLayout23.setObjectName(u"hboxLayout23")
        self.hboxLayout23.setContentsMargins(0, 0, 0, 0)
        self.tblCrops = QTableWidget(self.layoutWidget)
        if (self.tblCrops.columnCount() < 3):
            self.tblCrops.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblCrops.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblCrops.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblCrops.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblCrops.setObjectName(u"tblCrops")
        self.tblCrops.setAlternatingRowColors(True)
        self.tblCrops.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblCrops.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblCrops.setShowGrid(False)

        self.hboxLayout23.addWidget(self.tblCrops)

        self.lblCropPix = QLabel(self.layoutWidget)
        self.lblCropPix.setObjectName(u"lblCropPix")
        self.lblCropPix.setMinimumSize(QSize(128, 128))
        self.lblCropPix.setMaximumSize(QSize(128, 128))
        self.lblCropPix.setAlignment(Qt.AlignCenter)

        self.hboxLayout23.addWidget(self.lblCropPix)

        self.splitter_7.addWidget(self.layoutWidget)
        self.textBrowserCropDefinition = QTextBrowser(self.splitter_7)
        self.textBrowserCropDefinition.setObjectName(u"textBrowserCropDefinition")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.textBrowserCropDefinition.sizePolicy().hasHeightForWidth())
        self.textBrowserCropDefinition.setSizePolicy(sizePolicy8)
        self.splitter_7.addWidget(self.textBrowserCropDefinition)

        self.gridLayout11.addWidget(self.splitter_7, 0, 0, 1, 2)

        self.gbCustomCropMask = QGroupBox(self.crops_tab)
        self.gbCustomCropMask.setObjectName(u"gbCustomCropMask")
        self.gbCustomCropMask.setCheckable(True)
        self.gbCustomCropMask.setChecked(False)
        self.gridLayout12 = QGridLayout(self.gbCustomCropMask)
        self.gridLayout12.setObjectName(u"gridLayout12")
        self.label_26 = QLabel(self.gbCustomCropMask)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)

        self.gridLayout12.addWidget(self.label_26, 0, 0, 1, 1)

        self.cboCommonCropRaster = QComboBox(self.gbCustomCropMask)
        self.cboCommonCropRaster.setObjectName(u"cboCommonCropRaster")

        self.gridLayout12.addWidget(self.cboCommonCropRaster, 0, 1, 1, 1)


        self.gridLayout11.addWidget(self.gbCustomCropMask, 1, 0, 1, 2)

        self.gbSlopeMaskCropLand = QGroupBox(self.crops_tab)
        self.gbSlopeMaskCropLand.setObjectName(u"gbSlopeMaskCropLand")
        self.gbSlopeMaskCropLand.setCheckable(True)
        self.gridLayout13 = QGridLayout(self.gbSlopeMaskCropLand)
        self.gridLayout13.setObjectName(u"gridLayout13")
        self.hboxLayout24 = QHBoxLayout()
        self.hboxLayout24.setObjectName(u"hboxLayout24")
        self.label_30 = QLabel(self.gbSlopeMaskCropLand)
        self.label_30.setObjectName(u"label_30")

        self.hboxLayout24.addWidget(self.label_30)

        self.dsbMinSlopeCropMask = QDoubleSpinBox(self.gbSlopeMaskCropLand)
        self.dsbMinSlopeCropMask.setObjectName(u"dsbMinSlopeCropMask")
        self.dsbMinSlopeCropMask.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.hboxLayout24.addWidget(self.dsbMinSlopeCropMask)

        self.label_32 = QLabel(self.gbSlopeMaskCropLand)
        self.label_32.setObjectName(u"label_32")

        self.hboxLayout24.addWidget(self.label_32)


        self.gridLayout13.addLayout(self.hboxLayout24, 0, 0, 1, 1)


        self.gridLayout11.addWidget(self.gbSlopeMaskCropLand, 2, 0, 1, 1)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.pbnNewCropParameter = QPushButton(self.crops_tab)
        self.pbnNewCropParameter.setObjectName(u"pbnNewCropParameter")
        sizePolicy8.setHeightForWidth(self.pbnNewCropParameter.sizePolicy().hasHeightForWidth())
        self.pbnNewCropParameter.setSizePolicy(sizePolicy8)

        self.vboxLayout.addWidget(self.pbnNewCropParameter)

        self.pbnNewCrop = QPushButton(self.crops_tab)
        self.pbnNewCrop.setObjectName(u"pbnNewCrop")
        sizePolicy8.setHeightForWidth(self.pbnNewCrop.sizePolicy().hasHeightForWidth())
        self.pbnNewCrop.setSizePolicy(sizePolicy8)

        self.vboxLayout.addWidget(self.pbnNewCrop)


        self.gridLayout11.addLayout(self.vboxLayout, 2, 1, 1, 1)

        self.MainTabs.addTab(self.crops_tab, "")
        self.animals_tab = QWidget()
        self.animals_tab.setObjectName(u"animals_tab")
        self.gridLayout14 = QGridLayout(self.animals_tab)
        self.gridLayout14.setObjectName(u"gridLayout14")
        self.splitter_3 = QSplitter(self.animals_tab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout15 = QGridLayout(self.layoutWidget1)
        self.gridLayout15.setObjectName(u"gridLayout15")
        self.gridLayout15.setContentsMargins(0, 0, 0, 0)
        self.tblAnimals = QTableWidget(self.layoutWidget1)
        if (self.tblAnimals.columnCount() < 4):
            self.tblAnimals.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tblAnimals.setObjectName(u"tblAnimals")
        self.tblAnimals.setAlternatingRowColors(True)
        self.tblAnimals.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAnimals.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblAnimals.setShowGrid(False)

        self.gridLayout15.addWidget(self.tblAnimals, 0, 0, 2, 1)

        self.spacerItem12 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout15.addItem(self.spacerItem12, 1, 1, 1, 1)

        self.lblAnimalPix = QLabel(self.layoutWidget1)
        self.lblAnimalPix.setObjectName(u"lblAnimalPix")
        self.lblAnimalPix.setMinimumSize(QSize(128, 128))
        self.lblAnimalPix.setMaximumSize(QSize(128, 128))
        self.lblAnimalPix.setAlignment(Qt.AlignCenter)

        self.gridLayout15.addWidget(self.lblAnimalPix, 0, 1, 1, 1)

        self.splitter_3.addWidget(self.layoutWidget1)
        self.textBrowserAnimalDefinition = QTextBrowser(self.splitter_3)
        self.textBrowserAnimalDefinition.setObjectName(u"textBrowserAnimalDefinition")
        self.splitter_3.addWidget(self.textBrowserAnimalDefinition)

        self.gridLayout14.addWidget(self.splitter_3, 0, 0, 1, 2)

        self.gbCustomMaskGrazingLand = QGroupBox(self.animals_tab)
        self.gbCustomMaskGrazingLand.setObjectName(u"gbCustomMaskGrazingLand")
        self.gbCustomMaskGrazingLand.setCheckable(True)
        self.gbCustomMaskGrazingLand.setChecked(False)
        self.gridLayout16 = QGridLayout(self.gbCustomMaskGrazingLand)
        self.gridLayout16.setObjectName(u"gridLayout16")
        self.label_25 = QLabel(self.gbCustomMaskGrazingLand)
        self.label_25.setObjectName(u"label_25")
        sizePolicy5.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy5)

        self.gridLayout16.addWidget(self.label_25, 0, 0, 1, 1)

        self.cboCommonGrazingRaster = QComboBox(self.gbCustomMaskGrazingLand)
        self.cboCommonGrazingRaster.setObjectName(u"cboCommonGrazingRaster")

        self.gridLayout16.addWidget(self.cboCommonGrazingRaster, 0, 1, 1, 1)


        self.gridLayout14.addWidget(self.gbCustomMaskGrazingLand, 1, 0, 1, 2)

        self.gbGenerateMaskGrazingLand = QGroupBox(self.animals_tab)
        self.gbGenerateMaskGrazingLand.setObjectName(u"gbGenerateMaskGrazingLand")
        self.gbGenerateMaskGrazingLand.setCheckable(True)
        self.gridLayout17 = QGridLayout(self.gbGenerateMaskGrazingLand)
        self.gridLayout17.setObjectName(u"gridLayout17")
        self.label_33 = QLabel(self.gbGenerateMaskGrazingLand)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout17.addWidget(self.label_33, 0, 0, 1, 1)

        self.dsbMinimumSlopeGrazingMask = QDoubleSpinBox(self.gbGenerateMaskGrazingLand)
        self.dsbMinimumSlopeGrazingMask.setObjectName(u"dsbMinimumSlopeGrazingMask")
        self.dsbMinimumSlopeGrazingMask.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dsbMinimumSlopeGrazingMask.setSingleStep(0.010000000000000)
        self.dsbMinimumSlopeGrazingMask.setValue(8.000000000000000)

        self.gridLayout17.addWidget(self.dsbMinimumSlopeGrazingMask, 0, 1, 1, 1)

        self.label_34 = QLabel(self.gbGenerateMaskGrazingLand)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout17.addWidget(self.label_34, 0, 2, 1, 1)

        self.dsbMaximumSlopeGrazingMask = QDoubleSpinBox(self.gbGenerateMaskGrazingLand)
        self.dsbMaximumSlopeGrazingMask.setObjectName(u"dsbMaximumSlopeGrazingMask")
        self.dsbMaximumSlopeGrazingMask.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dsbMaximumSlopeGrazingMask.setValue(13.000000000000000)

        self.gridLayout17.addWidget(self.dsbMaximumSlopeGrazingMask, 0, 3, 1, 1)


        self.gridLayout14.addWidget(self.gbGenerateMaskGrazingLand, 2, 0, 1, 2)

        self.gbFoodValue = QGroupBox(self.animals_tab)
        self.gbFoodValue.setObjectName(u"gbFoodValue")
        self.gridLayout18 = QGridLayout(self.gbFoodValue)
        self.gridLayout18.setObjectName(u"gridLayout18")
        self.sbCommonRasterValue = QSpinBox(self.gbFoodValue)
        self.sbCommonRasterValue.setObjectName(u"sbCommonRasterValue")
        self.sbCommonRasterValue.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbCommonRasterValue.setMinimum(1)
        self.sbCommonRasterValue.setMaximum(5000)
        self.sbCommonRasterValue.setSingleStep(1)
        self.sbCommonRasterValue.setValue(8)

        self.gridLayout18.addWidget(self.sbCommonRasterValue, 0, 0, 1, 1)

        self.cbCommonLandEnergyType = QComboBox(self.gbFoodValue)
        self.cbCommonLandEnergyType.setObjectName(u"cbCommonLandEnergyType")

        self.gridLayout18.addWidget(self.cbCommonLandEnergyType, 0, 1, 1, 1)

        self.label_28 = QLabel(self.gbFoodValue)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout18.addWidget(self.label_28, 0, 2, 1, 1)

        self.cbAreaUnits = QComboBox(self.gbFoodValue)
        self.cbAreaUnits.setObjectName(u"cbAreaUnits")
        sizePolicy2.setHeightForWidth(self.cbAreaUnits.sizePolicy().hasHeightForWidth())
        self.cbAreaUnits.setSizePolicy(sizePolicy2)
        self.cbAreaUnits.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout18.addWidget(self.cbAreaUnits, 0, 3, 1, 1)

        self.label_27 = QLabel(self.gbFoodValue)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout18.addWidget(self.label_27, 0, 4, 1, 1)


        self.gridLayout14.addWidget(self.gbFoodValue, 3, 0, 1, 1)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.pbnNewAnimal = QPushButton(self.animals_tab)
        self.pbnNewAnimal.setObjectName(u"pbnNewAnimal")
        sizePolicy8.setHeightForWidth(self.pbnNewAnimal.sizePolicy().hasHeightForWidth())
        self.pbnNewAnimal.setSizePolicy(sizePolicy8)

        self.vboxLayout1.addWidget(self.pbnNewAnimal)

        self.pbnNewAnimalParameter = QPushButton(self.animals_tab)
        self.pbnNewAnimalParameter.setObjectName(u"pbnNewAnimalParameter")
        sizePolicy8.setHeightForWidth(self.pbnNewAnimalParameter.sizePolicy().hasHeightForWidth())
        self.pbnNewAnimalParameter.setSizePolicy(sizePolicy8)

        self.vboxLayout1.addWidget(self.pbnNewAnimalParameter)


        self.gridLayout14.addLayout(self.vboxLayout1, 3, 1, 1, 1)

        self.MainTabs.addTab(self.animals_tab, "")
        self.results_tab = QWidget()
        self.results_tab.setObjectName(u"results_tab")
        self.gridLayout19 = QGridLayout(self.results_tab)
        self.gridLayout19.setObjectName(u"gridLayout19")
        self.splitter_5 = QSplitter(self.results_tab)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(self.splitter_5)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget2 = QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.vboxLayout2 = QVBoxLayout(self.layoutWidget2)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.vboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.lblCropPicCalcs = QLabel(self.layoutWidget2)
        self.lblCropPicCalcs.setObjectName(u"lblCropPicCalcs")
        self.lblCropPicCalcs.setMinimumSize(QSize(70, 70))
        self.lblCropPicCalcs.setMaximumSize(QSize(70, 70))
        self.lblCropPicCalcs.setAlignment(Qt.AlignCenter)

        self.vboxLayout2.addWidget(self.lblCropPicCalcs)

        self.listWidgetCalculationsCrop = QListWidget(self.layoutWidget2)
        self.listWidgetCalculationsCrop.setObjectName(u"listWidgetCalculationsCrop")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.listWidgetCalculationsCrop.sizePolicy().hasHeightForWidth())
        self.listWidgetCalculationsCrop.setSizePolicy(sizePolicy9)
        self.listWidgetCalculationsCrop.setMinimumSize(QSize(70, 0))

        self.vboxLayout2.addWidget(self.listWidgetCalculationsCrop)

        self.splitter_2.addWidget(self.layoutWidget2)
        self.textBrowserResultsCrop = QTextBrowser(self.splitter_2)
        self.textBrowserResultsCrop.setObjectName(u"textBrowserResultsCrop")
        sizePolicy9.setHeightForWidth(self.textBrowserResultsCrop.sizePolicy().hasHeightForWidth())
        self.textBrowserResultsCrop.setSizePolicy(sizePolicy9)
        self.splitter_2.addWidget(self.textBrowserResultsCrop)
        self.splitter_5.addWidget(self.splitter_2)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.layoutWidget3 = QWidget(self.splitter_4)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.vboxLayout3 = QVBoxLayout(self.layoutWidget3)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.vboxLayout3.setContentsMargins(0, 0, 0, 0)
        self.lblAnimalPicCalcs = QLabel(self.layoutWidget3)
        self.lblAnimalPicCalcs.setObjectName(u"lblAnimalPicCalcs")
        self.lblAnimalPicCalcs.setMinimumSize(QSize(70, 70))
        self.lblAnimalPicCalcs.setMaximumSize(QSize(70, 70))
        self.lblAnimalPicCalcs.setAlignment(Qt.AlignCenter)

        self.vboxLayout3.addWidget(self.lblAnimalPicCalcs)

        self.listWidgetCalculationsAnimal = QListWidget(self.layoutWidget3)
        self.listWidgetCalculationsAnimal.setObjectName(u"listWidgetCalculationsAnimal")
        sizePolicy9.setHeightForWidth(self.listWidgetCalculationsAnimal.sizePolicy().hasHeightForWidth())
        self.listWidgetCalculationsAnimal.setSizePolicy(sizePolicy9)
        self.listWidgetCalculationsAnimal.setMinimumSize(QSize(70, 0))

        self.vboxLayout3.addWidget(self.listWidgetCalculationsAnimal)

        self.splitter_4.addWidget(self.layoutWidget3)
        self.textBrowserResultsAnimals = QTextBrowser(self.splitter_4)
        self.textBrowserResultsAnimals.setObjectName(u"textBrowserResultsAnimals")
        sizePolicy6.setHeightForWidth(self.textBrowserResultsAnimals.sizePolicy().hasHeightForWidth())
        self.textBrowserResultsAnimals.setSizePolicy(sizePolicy6)
        self.splitter_4.addWidget(self.textBrowserResultsAnimals)
        self.splitter_5.addWidget(self.splitter_4)

        self.gridLayout19.addWidget(self.splitter_5, 0, 0, 1, 6)

        self.spacerItem13 = QSpacerItem(341, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout19.addItem(self.spacerItem13, 1, 0, 1, 1)

        self.pbnTargets = QPushButton(self.results_tab)
        self.pbnTargets.setObjectName(u"pbnTargets")

        self.gridLayout19.addWidget(self.pbnTargets, 1, 1, 1, 1)

        self.pbnFallow = QPushButton(self.results_tab)
        self.pbnFallow.setObjectName(u"pbnFallow")

        self.gridLayout19.addWidget(self.pbnFallow, 1, 2, 1, 1)

        self.pbnHerds = QPushButton(self.results_tab)
        self.pbnHerds.setObjectName(u"pbnHerds")

        self.gridLayout19.addWidget(self.pbnHerds, 1, 3, 1, 1)

        self.pbnText = QPushButton(self.results_tab)
        self.pbnText.setObjectName(u"pbnText")

        self.gridLayout19.addWidget(self.pbnText, 1, 4, 1, 1)

        self.pbnHtml = QPushButton(self.results_tab)
        self.pbnHtml.setObjectName(u"pbnHtml")

        self.gridLayout19.addWidget(self.pbnHtml, 1, 5, 1, 1)

        self.MainTabs.addTab(self.results_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout20 = QGridLayout(self.tab)
        self.gridLayout20.setObjectName(u"gridLayout20")
        self.splitter_6 = QSplitter(self.tab)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.tbReport = QTextBrowser(self.splitter_6)
        self.tbReport.setObjectName(u"tbReport")
        sizePolicy.setHeightForWidth(self.tbReport.sizePolicy().hasHeightForWidth())
        self.tbReport.setSizePolicy(sizePolicy)
        self.splitter_6.addWidget(self.tbReport)

        self.gridLayout20.addWidget(self.splitter_6, 0, 0, 1, 1)

        self.MainTabs.addTab(self.tab, "")
        self.tabLogs = QWidget()
        self.tabLogs.setObjectName(u"tabLogs")
        self.gridLayout21 = QGridLayout(self.tabLogs)
        self.gridLayout21.setObjectName(u"gridLayout21")
        self.tbLogs = QTextBrowser(self.tabLogs)
        self.tbLogs.setObjectName(u"tbLogs")

        self.gridLayout21.addWidget(self.tbLogs, 0, 0, 1, 1)

        self.MainTabs.addTab(self.tabLogs, "")
        self.help_tab = QWidget()
        self.help_tab.setObjectName(u"help_tab")
        self.gridLayout22 = QGridLayout(self.help_tab)
        self.gridLayout22.setObjectName(u"gridLayout22")
        self.vboxLayout4 = QVBoxLayout()
        self.vboxLayout4.setSpacing(1)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.treeHelp = QTreeWidget(self.help_tab)
        __qtreewidgetitem = QTreeWidgetItem(self.treeHelp)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem6 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem7)
        QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem8)
        QTreeWidgetItem(__qtreewidgetitem10)
        QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem12 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem12)
        QTreeWidgetItem(__qtreewidgetitem12)
        QTreeWidgetItem(__qtreewidgetitem12)
        QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem13)
        QTreeWidgetItem(__qtreewidgetitem13)
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem11)
        QTreeWidgetItem(__qtreewidgetitem14)
        QTreeWidgetItem(__qtreewidgetitem14)
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem15)
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem15)
        QTreeWidgetItem(__qtreewidgetitem16)
        QTreeWidgetItem(__qtreewidgetitem16)
        QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem17)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        QTreeWidgetItem(__qtreewidgetitem19)
        __qtreewidgetitem20 = QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem20)
        QTreeWidgetItem(__qtreewidgetitem21)
        QTreeWidgetItem(__qtreewidgetitem21)
        QTreeWidgetItem(__qtreewidgetitem21)
        __qtreewidgetitem22 = QTreeWidgetItem(__qtreewidgetitem15)
        QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem23 = QTreeWidgetItem(__qtreewidgetitem22)
        QTreeWidgetItem(__qtreewidgetitem23)
        QTreeWidgetItem(__qtreewidgetitem23)
        QTreeWidgetItem(__qtreewidgetitem23)
        QTreeWidgetItem(__qtreewidgetitem23)
        __qtreewidgetitem24 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem25 = QTreeWidgetItem(__qtreewidgetitem24)
        QTreeWidgetItem(__qtreewidgetitem25)
        __qtreewidgetitem26 = QTreeWidgetItem(__qtreewidgetitem24)
        QTreeWidgetItem(__qtreewidgetitem26)
        QTreeWidgetItem(__qtreewidgetitem24)
        __qtreewidgetitem27 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem28 = QTreeWidgetItem(__qtreewidgetitem27)
        QTreeWidgetItem(__qtreewidgetitem28)
        QTreeWidgetItem(__qtreewidgetitem28)
        __qtreewidgetitem29 = QTreeWidgetItem(__qtreewidgetitem22)
        QTreeWidgetItem(__qtreewidgetitem29)
        QTreeWidgetItem(__qtreewidgetitem29)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem30 = QTreeWidgetItem(self.treeHelp)
        __qtreewidgetitem31 = QTreeWidgetItem(__qtreewidgetitem30)
        QTreeWidgetItem(__qtreewidgetitem31)
        __qtreewidgetitem32 = QTreeWidgetItem(__qtreewidgetitem31)
        QTreeWidgetItem(__qtreewidgetitem32)
        QTreeWidgetItem(__qtreewidgetitem32)
        QTreeWidgetItem(__qtreewidgetitem30)
        self.treeHelp.setObjectName(u"treeHelp")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.treeHelp.sizePolicy().hasHeightForWidth())
        self.treeHelp.setSizePolicy(sizePolicy10)
        self.treeHelp.setMaximumSize(QSize(16777215, 16777215))

        self.vboxLayout4.addWidget(self.treeHelp)

        self.cbDebug = QCheckBox(self.help_tab)
        self.cbDebug.setObjectName(u"cbDebug")

        self.vboxLayout4.addWidget(self.cbDebug)


        self.gridLayout22.addLayout(self.vboxLayout4, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.helpHeaderLabel = QLabel(self.help_tab)
        self.helpHeaderLabel.setObjectName(u"helpHeaderLabel")
        self.helpHeaderLabel.setPixmap(QPixmap(u":/laHelpHeader.png"))
        self.helpHeaderLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.helpHeaderLabel)

        self.textHelp = QTextBrowser(self.help_tab)
        self.textHelp.setObjectName(u"textHelp")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(255)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.textHelp.sizePolicy().hasHeightForWidth())
        self.textHelp.setSizePolicy(sizePolicy11)

        self.verticalLayout.addWidget(self.textHelp)


        self.gridLayout22.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.MainTabs.addTab(self.help_tab, "")

        self.gridLayout.addWidget(self.MainTabs, 0, 0, 1, 11)

        QWidget.setTabOrder(self.lineEditSiteName, self.lineEditPeriod)
        QWidget.setTabOrder(self.lineEditPeriod, self.sbPopulation)
        QWidget.setTabOrder(self.sbPopulation, self.lineEditEasting)
        QWidget.setTabOrder(self.lineEditEasting, self.lineEditNorthing)
        QWidget.setTabOrder(self.lineEditNorthing, self.radioButtonEuclidean)
        QWidget.setTabOrder(self.radioButtonEuclidean, self.radioButtonWalkingTime)
        QWidget.setTabOrder(self.radioButtonWalkingTime, self.radioButtonPathDistance)
        QWidget.setTabOrder(self.radioButtonPathDistance, self.sbModelPrecision)
        QWidget.setTabOrder(self.sbModelPrecision, self.cboMapSet)
        QWidget.setTabOrder(self.cboMapSet, self.cboDEM)
        QWidget.setTabOrder(self.cboDEM, self.pushButtonRun)
        QWidget.setTabOrder(self.pushButtonRun, self.pushButtonLoad)
        QWidget.setTabOrder(self.pushButtonLoad, self.pushButtonSave)
        QWidget.setTabOrder(self.pushButtonSave, self.pushButtonExit)
        QWidget.setTabOrder(self.pushButtonExit, self.sliderDiet)
        QWidget.setTabOrder(self.sliderDiet, self.sliderCrop)
        QWidget.setTabOrder(self.sliderCrop, self.sliderMeat)
        QWidget.setTabOrder(self.sliderMeat, self.sbDailyCalories)
        QWidget.setTabOrder(self.sbDailyCalories, self.tblCrops)
        QWidget.setTabOrder(self.tblCrops, self.textBrowserCropDefinition)
        QWidget.setTabOrder(self.textBrowserCropDefinition, self.cboCommonCropRaster)
        QWidget.setTabOrder(self.cboCommonCropRaster, self.pbnNewCrop)
        QWidget.setTabOrder(self.pbnNewCrop, self.pbnNewCropParameter)
        QWidget.setTabOrder(self.pbnNewCropParameter, self.tblAnimals)
        QWidget.setTabOrder(self.tblAnimals, self.textBrowserAnimalDefinition)
        QWidget.setTabOrder(self.textBrowserAnimalDefinition, self.cboCommonGrazingRaster)
        QWidget.setTabOrder(self.cboCommonGrazingRaster, self.sbCommonRasterValue)
        QWidget.setTabOrder(self.sbCommonRasterValue, self.cbAreaUnits)
        QWidget.setTabOrder(self.cbAreaUnits, self.pbnNewAnimal)
        QWidget.setTabOrder(self.pbnNewAnimal, self.pbnNewAnimalParameter)
        QWidget.setTabOrder(self.pbnNewAnimalParameter, self.listWidgetCalculationsCrop)
        QWidget.setTabOrder(self.listWidgetCalculationsCrop, self.textBrowserResultsCrop)
        QWidget.setTabOrder(self.textBrowserResultsCrop, self.listWidgetCalculationsAnimal)
        QWidget.setTabOrder(self.listWidgetCalculationsAnimal, self.textBrowserResultsAnimals)
        QWidget.setTabOrder(self.textBrowserResultsAnimals, self.pbnTargets)
        QWidget.setTabOrder(self.pbnTargets, self.pbnFallow)
        QWidget.setTabOrder(self.pbnFallow, self.pbnHerds)
        QWidget.setTabOrder(self.pbnHerds, self.pbnText)
        QWidget.setTabOrder(self.pbnText, self.pbnHtml)
        QWidget.setTabOrder(self.pbnHtml, self.tbReport)
        QWidget.setTabOrder(self.tbReport, self.tbLogs)
        QWidget.setTabOrder(self.tbLogs, self.treeHelp)
        QWidget.setTabOrder(self.treeHelp, self.cbDebug)
        QWidget.setTabOrder(self.cbDebug, self.textHelp)

        self.retranslateUi(LaMainFormBase)

        self.MainTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LaMainFormBase)
    # setupUi

    def retranslateUi(self, LaMainFormBase):
        LaMainFormBase.setWindowTitle(QCoreApplication.translate("LaMainFormBase", u"Landuse Analyst", None))
        self.label_7.setText(QCoreApplication.translate("LaMainFormBase", u"Copyright 2008 Jason Jorgenson", None))
#if QT_CONFIG(tooltip)
        self.labelAnimalCheck.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the animals being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelAnimalCheck.setText(QCoreApplication.translate("LaMainFormBase", u"100%", None))
#if QT_CONFIG(tooltip)
        self.labelCropCheck.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the crops being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropCheck.setText(QCoreApplication.translate("LaMainFormBase", u"100%", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the crops being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("LaMainFormBase", u"  Crops:", None))
#if QT_CONFIG(tooltip)
        self.progressBarCalcs.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shows when program is busy, or progress of tasks.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.progressBarCalcs.setFormat(QCoreApplication.translate("LaMainFormBase", u"%p%", None))
#if QT_CONFIG(tooltip)
        self.pushButtonLoad.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Load previously saved model parameters.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLoad.setText(QCoreApplication.translate("LaMainFormBase", u"Load", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRun.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Run the model.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButtonRun.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pressing Calculate! will attempt to run the model with the parameters you have chosen.  If there are any errors, this process will fail, and indicate to you what the problem was.  To be on the safe side, always save your model before attempting to Calculate! it.  All results will be saved if the model runs correctly.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButtonRun.setText(QCoreApplication.translate("LaMainFormBase", u"Run", None))
        self.pushButtonExit.setText(QCoreApplication.translate("LaMainFormBase", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSave.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save all settings of this model to a file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSave.setText(QCoreApplication.translate("LaMainFormBase", u"Save", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the animals being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("LaMainFormBase", u"Animals:", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">To learn more about a feature or field in Landuse Analyst, you can do one of four things.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. <span style=\" font-size:10pt; color:#0000ff;\">Hover over it</span> with your mouse arrow for a brief description (like you are doing now to see this)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Click the <span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">?</span> i"
                        "n the top right of the main window and then click on the item you want detailed help for.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. RIght Click on the thing you want help for.  If there is detailed help for it, you will see a <span style=\" font-weight:600; color:#0000ff;\">What is this?</span> option that you can then click on.  Again, you can click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Go to the <span style=\" font-weight:600; color:#0000ff;\">Help</span> <span style=\" font-weight:600; color:#0000ff;\">Tab</span> and click on the item you want help with on the left for an even more detailed description of what things"
                        " are and how they work</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.frame_2.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst is a program that attempts to identify how much of the land surrounding an archaeological site would have been needed to sustain its population. <a href=\"http://www.arkygeek.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Land Analyst</span></a>, is Free Open Source Software (FOSS). That means that this program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_17.setText("")
        self.lblVersion.setText(QCoreApplication.translate("LaMainFormBase", u"Version: 99.99", None))
#if QT_CONFIG(tooltip)
        self.groupBoxManualSiteEntry.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The information entered here will be inserted as Meta-Data into the resulting maps.  However, Name and Period are optional.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.groupBoxManualSiteEntry.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The name of the site, it's period, and the estimated population.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxManualSiteEntry.setTitle(QCoreApplication.translate("LaMainFormBase", u"Settlement Information", None))
#if QT_CONFIG(tooltip)
        self.lineEditSiteName.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the site you are modelling here. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditSiteName.setText(QCoreApplication.translate("LaMainFormBase", u"Shuna", None))
#if QT_CONFIG(tooltip)
        self.sbPopulation.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Estimated population of the settlement (required)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.textLabel2_4.setText(QCoreApplication.translate("LaMainFormBase", u"Name:", None))
        self.label.setText(QCoreApplication.translate("LaMainFormBase", u"Period", None))
        self.label5.setText(QCoreApplication.translate("LaMainFormBase", u"Pop'n", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">E</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEditEasting.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting (required)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEditEasting.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Easting of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEditEasting.setText(QCoreApplication.translate("LaMainFormBase", u"744800", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">N</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEditNorthing.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing (required)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEditNorthing.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Northing of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEditNorthing.setText(QCoreApplication.translate("LaMainFormBase", u"3611100", None))
#if QT_CONFIG(whatsthis)
        self.model_method_box.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst currently offers three types of analysis. Here you select which one you want to use.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Euclidean method starts looking for suitable land at the site and moves outwards from that point 'as the crow flies'. In other words, using Euclidean geometry (or even more simply, it draws circles!)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Walking Time method uses the same basic principle except that it moves outward from t"
                        "he site based on walking time instead of distance. This method is probably the most realistic scenario to run, but it is interesting to compare the results of the three different methods.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Path Distance is very similar to Eucidean, except that this method considers topography when calculating distance from the site.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.model_method_box.setTitle(QCoreApplication.translate("LaMainFormBase", u"Modelling Method", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("LaMainFormBase", u"Precision: ", None))
#if QT_CONFIG(tooltip)
        self.sbModelPrecision.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbModelPrecision.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.radioButtonPathDistance.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate catchment by growing distance based on path distance (considers topography)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.radioButtonPathDistance.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Path Distance is selected, a cost map for the area is created that calculates how far it is  to all areas of the map from the site.  This is very similar to Eucidean, except that path distance considers topography.  The program then calculates area contained within a certain distance of the site.  If the derived area is insufficient to support the population, the distance is increased, and it tries again.  This repeats until the required area is contained.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButtonPathDistance.setText(QCoreApplication.translate("LaMainFormBase", u"Path Distance", None))
#if QT_CONFIG(tooltip)
        self.radioButtonWalkingTime.setToolTip(QCoreApplication.translate("LaMainFormBase", u"Calculate catchment by growing distance based on walking time", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.radioButtonWalkingTime.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Walking Time is selected, a cost map for the area is created that predicts how long it takes to get to any area on the map from the settlement.  The program then calculates the suitable area contained within the time it takes to walk.  If the derived area is insufficient to support the population, the walking time is increased, and it tries again.  This repeats until the required area is contained.  This method is probably the most realistic scenario to run, but it is interesting to compare the results of the three different methods.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButtonWalkingTime.setText(QCoreApplication.translate("LaMainFormBase", u"Walking Time", None))
#if QT_CONFIG(tooltip)
        self.radioButtonEuclidean.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate catchment by growing distance based on distance from the site ('as the crow flies')</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.radioButtonEuclidean.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Euclidean is selected, a cost map for the area is created that calculates how far it is  to all areas of the map from the site.  This distance does NOT consider topography.  In other words, it is simply as the crow flies.  The program then calculates area contained within a certain distance of the site.  If the derived area is insufficient to support the population, the distance is increased, and it tries again.  This repeats until the required area is contained.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButtonEuclidean.setText(QCoreApplication.translate("LaMainFormBase", u"Euclidean", None))
        self.gbxGrass.setTitle("")
        self.lblGrass.setText("")
        self.label_29.setText(QCoreApplication.translate("LaMainFormBase", u"Mapset:", None))
        self.label_24.setText(QCoreApplication.translate("LaMainFormBase", u"DEM: ", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.main_tab), QCoreApplication.translate("LaMainFormBase", u"Main", None))
        self.diet_comp_box.setTitle(QCoreApplication.translate("LaMainFormBase", u"Dietary Composition Percentages (Calories!)", None))
        self.cboxBaseOnPlants.setText(QCoreApplication.translate("LaMainFormBase", u"Base Calcs on Plant Percentage", None))
        self.cboxIncludeDairy.setText(QCoreApplication.translate("LaMainFormBase", u"Include Calories from Dairy", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent.setText(QCoreApplication.translate("LaMainFormBase", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent.setText(QCoreApplication.translate("LaMainFormBase", u"50", None))
        self.groupplantpercent.setTitle(QCoreApplication.translate("LaMainFormBase", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent.setText(QCoreApplication.translate("LaMainFormBase", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent.setText(QCoreApplication.translate("LaMainFormBase", u"10", None))
        self.label_9.setText(QCoreApplication.translate("LaMainFormBase", u"Wild", None))
        self.label_11.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic", None))
        self.groupmeatpercent.setTitle(QCoreApplication.translate("LaMainFormBase", u"MEAT", None))
        self.label_14.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent.setText(QCoreApplication.translate("LaMainFormBase", u"10", None))
        self.label_13.setText(QCoreApplication.translate("LaMainFormBase", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent.setText(QCoreApplication.translate("LaMainFormBase", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label6.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6.setText(QCoreApplication.translate("LaMainFormBase", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.sbDailyCalories.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbDailyCalories.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label6_2.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_2.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_2.setText(QCoreApplication.translate("LaMainFormBase", u"Dairy Use", None))
#if QT_CONFIG(tooltip)
        self.sbDairyUtilisation.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbDairyUtilisation.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbDairyUtilisation.setSuffix(QCoreApplication.translate("LaMainFormBase", u" %", None))
        self.cboxLimitDairy.setText(QCoreApplication.translate("LaMainFormBase", u"Limit to", None))
#if QT_CONFIG(tooltip)
        self.sbLimitDairyPercent.setToolTip(QCoreApplication.translate("LaMainFormBase", u"If selected, dairy products cannot contribute more than this percentage towards the overall diet.  If this level is achieved, surplus will be reported", None))
#endif // QT_CONFIG(tooltip)
        self.sbLimitDairyPercent.setSuffix(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.labelDairySurplus.setText(QCoreApplication.translate("LaMainFormBase", u"Surplus Dairy Produced", None))
#if QT_CONFIG(whatsthis)
        self.groupBox_2.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analsyt needs area targets before it can determine landuse for a site. In order to calculate the area requirements for crops and animals, calorie targets must first be determined. The Diet section makes this task very straight forward. It is important to note that all dietary considerations in this program are based on calories (or in some cases KCalories).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With this in mind, the first step is to define their diets as a ratio between calories provided by <span style=\" font-weight:600;\">Plants</span> an"
                        "d calories provided by <span style=\" font-weight:600;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes all sources of the diet.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The second level of adjustment is to set the proportions between tame and wild sources. This works the same way as the top slider. Things to consider when setting these sliders are fishing, hunting, wild plant foraging, etc.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox_2.setTitle(QCoreApplication.translate("LaMainFormBase", u"Breakdown of Diet", None))
        self.label_10.setText(QCoreApplication.translate("LaMainFormBase", u"Settlement:", None))
        self.labelCaloriesSettlement.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_37.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_12.setText(QCoreApplication.translate("LaMainFormBase", u"All Plants:", None))
        self.labelPortionPlants.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_38.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_16.setText(QCoreApplication.translate("LaMainFormBase", u"All Meat:", None))
        self.labelPortionMeat.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_39.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_54.setText(QCoreApplication.translate("LaMainFormBase", u"All Dairy", None))
        self.labelPortionAllDairy.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_55.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_18.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic Crops:", None))
        self.labelPortionCrops.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_40.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_19.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic Meat:", None))
        self.labelPortionTameMeat.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_41.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_31.setText(QCoreApplication.translate("LaMainFormBase", u"Dairy Products:", None))
        self.labelPortionDairy.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_42.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_51.setText(QCoreApplication.translate("LaMainFormBase", u"Wild Meat: ", None))
        self.labelPortionWildMeat.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_50.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_53.setText(QCoreApplication.translate("LaMainFormBase", u"Wild Plants: ", None))
        self.labelPortionWildPlants.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_52.setText(QCoreApplication.translate("LaMainFormBase", u"%", None))
        self.label_23.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic Crops", None))
        self.labelCaloriesCrops.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_43.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_21.setText(QCoreApplication.translate("LaMainFormBase", u"Domestic Meat", None))
        self.labelCaloriesTameMeat.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_44.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_35.setText(QCoreApplication.translate("LaMainFormBase", u"Dairy Products", None))
        self.labelCaloriesDairy.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_45.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_46.setText(QCoreApplication.translate("LaMainFormBase", u"Wild Meat", None))
        self.labelCaloriesWildMeat.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_47.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_48.setText(QCoreApplication.translate("LaMainFormBase", u"Wild Plants", None))
        self.labelCaloriesWildPlants.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_49.setText(QCoreApplication.translate("LaMainFormBase", u"MCals", None))
        self.label_4.setText(QCoreApplication.translate("LaMainFormBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Calories required Annum</span><span style=\" font-size:11pt; font-weight:600; font-style:italic; vertical-align:super;\">-1</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("LaMainFormBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Contribution to Diet</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("LaMainFormBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Calories Supplied by:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("LaMainFormBase", u"Individual:", None))
        self.labelCaloriesIndividual.setText(QCoreApplication.translate("LaMainFormBase", u"Adjust Diet Settings", None))
        self.label_36.setText(QCoreApplication.translate("LaMainFormBase", u"kCals", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.diet_tab), QCoreApplication.translate("LaMainFormBase", u"Diet", None))
        ___qtablewidgetitem = self.tblCrops.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaMainFormBase", u"Use?", None));
        ___qtablewidgetitem1 = self.tblCrops.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaMainFormBase", u"Crop", None));
        ___qtablewidgetitem2 = self.tblCrops.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LaMainFormBase", u"Parameters", None));
#if QT_CONFIG(tooltip)
        self.tblCrops.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The crop selected here will be displayed below.  If the crop is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each crop being modelled.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblCrops.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Crop Interface has been designed to be very simple and easy to use. The top section lists all of the defined crops, and selecting one will display its settings in the two lower sections. The lower sections are divided into the crop definition details on the left, and the model parameter settings for the currently selected crop on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the crop or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lblCropPix.setText(QCoreApplication.translate("LaMainFormBase", u"No Graphic\n"
"Selected", None))
#if QT_CONFIG(tooltip)
        self.textBrowserCropDefinition.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a crop above to refresh this window</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gbCustomCropMask.setTitle(QCoreApplication.translate("LaMainFormBase", u"Use Custom Suitability Mask for Common Cropland", None))
        self.label_26.setText(QCoreApplication.translate("LaMainFormBase", u"Common Crop Land Raster Mask", None))
        self.gbSlopeMaskCropLand.setTitle(QCoreApplication.translate("LaMainFormBase", u"Generate Suitability Mask for Common Cropland", None))
        self.label_30.setText(QCoreApplication.translate("LaMainFormBase", u"If the slope is less than", None))
        self.dsbMinSlopeCropMask.setSuffix(QCoreApplication.translate("LaMainFormBase", u" degrees", None))
        self.label_32.setText(QCoreApplication.translate("LaMainFormBase", u"consider it ok for crop use", None))
#if QT_CONFIG(tooltip)
        self.pbnNewCropParameter.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Crop Parameter Manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnNewCropParameter.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model crops, several details must be supplied. Crop Parameter Manager asks for these specifics. As with Crop Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same crop, follow the same procedure as for defining multiple crops with the same name. Let's say you want to have two parameters set up for Wheat as an example. The Name: field is Wheat for both, but "
                        "in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnNewCropParameter.setText(QCoreApplication.translate("LaMainFormBase", u"Set Parameters", None))
#if QT_CONFIG(tooltip)
        self.pbnNewCrop.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Crop Manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnNewCrop.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pressing this button will open up the Crop Manager.  There, you can create new crops from scratch, or clone previously defined crops to make changes to.  You can also delete crops if you wish.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnNewCrop.setText(QCoreApplication.translate("LaMainFormBase", u"Manage Crops", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.crops_tab), QCoreApplication.translate("LaMainFormBase", u"Crops", None))
        ___qtablewidgetitem3 = self.tblAnimals.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LaMainFormBase", u"Use?", None));
        ___qtablewidgetitem4 = self.tblAnimals.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LaMainFormBase", u"Animal", None));
        ___qtablewidgetitem5 = self.tblAnimals.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LaMainFormBase", u"Parameters", None));
        ___qtablewidgetitem6 = self.tblAnimals.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LaMainFormBase", u"Percentage", None));
#if QT_CONFIG(tooltip)
        self.tblAnimals.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The animal selected here will be displayed below.  If the animal is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each animal being modelled.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblAnimals.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal Interface has been designed to be very simple and easy to use. The top section lists all of the defined animals, and selecting one will display its settings in the two lower sections. The lower sections are divided into the animal definition details on the left, and the model parameter settings for the currently selected animal on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the animal or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lblAnimalPix.setText(QCoreApplication.translate("LaMainFormBase", u"No Graphic\n"
"Selected", None))
#if QT_CONFIG(tooltip)
        self.textBrowserAnimalDefinition.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select an animal above to refresh this window</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gbCustomMaskGrazingLand.setTitle(QCoreApplication.translate("LaMainFormBase", u"Use Custom Suitability mask for Common Grazing Land", None))
        self.label_25.setText(QCoreApplication.translate("LaMainFormBase", u"Select Mask: ", None))
        self.gbGenerateMaskGrazingLand.setTitle(QCoreApplication.translate("LaMainFormBase", u"Generate Suitability Mask for Common Grazing Land", None))
        self.label_33.setText(QCoreApplication.translate("LaMainFormBase", u"Slope is greater than ", None))
        self.dsbMinimumSlopeGrazingMask.setSuffix(QCoreApplication.translate("LaMainFormBase", u" degrees", None))
        self.label_34.setText(QCoreApplication.translate("LaMainFormBase", u"and less than", None))
        self.dsbMaximumSlopeGrazingMask.setSuffix(QCoreApplication.translate("LaMainFormBase", u" degrees", None))
        self.gbFoodValue.setTitle(QCoreApplication.translate("LaMainFormBase", u"Food Value of Common Grazing Land (Required)", None))
#if QT_CONFIG(tooltip)
        self.sbCommonRasterValue.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food Value of grazing land in Kilo Calories</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbCommonRasterValue.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
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
        self.label_28.setText(QCoreApplication.translate("LaMainFormBase", u"per", None))
#if QT_CONFIG(tooltip)
        self.cbAreaUnits.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.cbAreaUnits.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_27.setText(QCoreApplication.translate("LaMainFormBase", u"(per annum)", None))
#if QT_CONFIG(tooltip)
        self.pbnNewAnimal.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Animal Manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnNewAnimal.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By pressing on the Manage Animals... button you will be brought to the Animal Manager. Here, you can create new animals from scratch, or clone previously defined animals to make changes to. You can also delete animals if you wish. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnNewAnimal.setText(QCoreApplication.translate("LaMainFormBase", u"Manage Animals", None))
#if QT_CONFIG(tooltip)
        self.pbnNewAnimalParameter.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Animal Parameter Manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnNewAnimalParameter.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for the specific information about the animal which tells the program how the animal was fed, and how big a part of the settlements diet it was. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals"
                        " with the same name. Let's say you want to have two parameters set up for cows as an example. The Name: field is Cow for both, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will ahve these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnNewAnimalParameter.setText(QCoreApplication.translate("LaMainFormBase", u"Set Parameters", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.animals_tab), QCoreApplication.translate("LaMainFormBase", u"Animals", None))
        self.lblCropPicCalcs.setText(QCoreApplication.translate("LaMainFormBase", u"No Image\n"
"Selected", None))
#if QT_CONFIG(tooltip)
        self.listWidgetCalculationsCrop.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select which crop you want to see the calculations for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.listWidgetCalculationsCrop.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for all of the crops and animals being modelled, simply select them from the list, and the results will be displayed in the area to the right. This information is meant to give the user an opportunity to make sure that the target look feasible before running the model (which can be very time consuming).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.textBrowserResultsCrop.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for a crop simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lblAnimalPicCalcs.setText(QCoreApplication.translate("LaMainFormBase", u"No Image\n"
"Selected", None))
#if QT_CONFIG(tooltip)
        self.listWidgetCalculationsAnimal.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select which animal you want to see the calculations for.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.listWidgetCalculationsAnimal.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for all of the crops and animals being modelled, simply select them from the list, and the results will be displayed in the area to the right. This information is meant to give the user an opportunity to make sure that the target look feasible before running the model (which can be very time consuming).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.textBrowserResultsAnimals.setWhatsThis(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for an animal simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnTargets.setText(QCoreApplication.translate("LaMainFormBase", u"Targets", None))
        self.pbnFallow.setText(QCoreApplication.translate("LaMainFormBase", u"Fallow", None))
        self.pbnHerds.setText(QCoreApplication.translate("LaMainFormBase", u"Herds", None))
        self.pbnText.setText(QCoreApplication.translate("LaMainFormBase", u"Text Report", None))
        self.pbnHtml.setText(QCoreApplication.translate("LaMainFormBase", u"HTML", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.results_tab), QCoreApplication.translate("LaMainFormBase", u"Calculations", None))
#if QT_CONFIG(tooltip)
        self.tbReport.setToolTip(QCoreApplication.translate("LaMainFormBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The results produced by running the model are displayed here.  This feature, however, is not yet implemented in the Alpha version of Landuse Analyst, but is planned for the Initial Release.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab), QCoreApplication.translate("LaMainFormBase", u"Results", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tabLogs), QCoreApplication.translate("LaMainFormBase", u"Log", None))
        ___qtreewidgetitem = self.treeHelp.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("LaMainFormBase", u"Help", None));

        __sortingEnabled = self.treeHelp.isSortingEnabled()
        self.treeHelp.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeHelp.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("LaMainFormBase", u"Model", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("LaMainFormBase", u"Main", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("LaMainFormBase", u"Settlement Information", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("LaMainFormBase", u"Site Name", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem3.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("LaMainFormBase", u"Population", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem3.child(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("LaMainFormBase", u"Period", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("LaMainFormBase", u"Location", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("LaMainFormBase", u"Easting", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("LaMainFormBase", u"Northing", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem7.child(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("LaMainFormBase", u"JADIS Database", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("LaMainFormBase", u"Modelling Method", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("LaMainFormBase", u"Euclidean", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("LaMainFormBase", u"Walking Time", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem11.child(2)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("LaMainFormBase", u"Path Distance", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem11.child(3)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("LaMainFormBase", u"Precision", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("LaMainFormBase", u"Diet", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("LaMainFormBase", u"Plant to Meat Ratio", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem16.child(1)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("LaMainFormBase", u"Wild to Tame Ratio", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem16.child(2)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("LaMainFormBase", u"Calories per person per day", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem16.child(3)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("LaMainFormBase", u"Breakdown", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem16.child(4)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("LaMainFormBase", u"Clear", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crops", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("LaMainFormBase", u"Using the Crop Interface", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("LaMainFormBase", u"Managing Crops", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("LaMainFormBase", u"Clone a crop", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem24.child(1)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("LaMainFormBase", u"Create a new crop", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem24.child(2)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("LaMainFormBase", u"Saving crops", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem24.child(3)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Descriptions", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Name", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem28.child(1)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Notes", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem28.child(2)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Yield", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem31.child(0)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Food Value", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem28.child(3)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("LaMainFormBase", u"Fodder Yield", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem33.child(0)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Fodder Food Value", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem28.child(4)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Area Units", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem22.child(2)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Parameters", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem36.child(0)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Parameter Description", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem37.child(0)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Parameter Name", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem37.child(1)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Parameter Notes", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem37.child(2)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("LaMainFormBase", u"Linking to a crop", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem37.child(3)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Portion of diet", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem36.child(1)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Suitability masks", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem42.child(0)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Masks Common", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem42.child(1)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Masks Specific", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem36.child(2)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Rotation", None));
        ___qtreewidgetitem46 = ___qtreewidgetitem45.child(0)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop to Fallow Ratio", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem45.child(1)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("LaMainFormBase", u"Crop Fallow Food Value", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animals", None));
        ___qtreewidgetitem49 = ___qtreewidgetitem48.child(0)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("LaMainFormBase", u"Using the Animals Interface", None));
        ___qtreewidgetitem50 = ___qtreewidgetitem48.child(1)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("LaMainFormBase", u"Managing Animals", None));
        ___qtreewidgetitem51 = ___qtreewidgetitem50.child(0)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("LaMainFormBase", u"Clone an animal", None));
        ___qtreewidgetitem52 = ___qtreewidgetitem50.child(1)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("LaMainFormBase", u"Create a new animal", None));
        ___qtreewidgetitem53 = ___qtreewidgetitem50.child(2)
        ___qtreewidgetitem53.setText(0, QCoreApplication.translate("LaMainFormBase", u"Saving animals", None));
        ___qtreewidgetitem54 = ___qtreewidgetitem50.child(3)
        ___qtreewidgetitem54.setText(0, QCoreApplication.translate("LaMainFormBase", u"Defining an animal", None));
        ___qtreewidgetitem55 = ___qtreewidgetitem54.child(0)
        ___qtreewidgetitem55.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Description", None));
        ___qtreewidgetitem56 = ___qtreewidgetitem55.child(0)
        ___qtreewidgetitem56.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Name", None));
        ___qtreewidgetitem57 = ___qtreewidgetitem55.child(1)
        ___qtreewidgetitem57.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Notes", None));
        ___qtreewidgetitem58 = ___qtreewidgetitem55.child(2)
        ___qtreewidgetitem58.setText(0, QCoreApplication.translate("LaMainFormBase", u"Usable Meat", None));
        ___qtreewidgetitem59 = ___qtreewidgetitem55.child(3)
        ___qtreewidgetitem59.setText(0, QCoreApplication.translate("LaMainFormBase", u"Kill Weight", None));
        ___qtreewidgetitem60 = ___qtreewidgetitem55.child(4)
        ___qtreewidgetitem60.setText(0, QCoreApplication.translate("LaMainFormBase", u"Grow Time", None));
        ___qtreewidgetitem61 = ___qtreewidgetitem55.child(5)
        ___qtreewidgetitem61.setText(0, QCoreApplication.translate("LaMainFormBase", u"Death Rate", None));
        ___qtreewidgetitem62 = ___qtreewidgetitem54.child(1)
        ___qtreewidgetitem62.setText(0, QCoreApplication.translate("LaMainFormBase", u"Reproduction", None));
        ___qtreewidgetitem63 = ___qtreewidgetitem62.child(0)
        ___qtreewidgetitem63.setText(0, QCoreApplication.translate("LaMainFormBase", u"Sexual Maturity", None));
        ___qtreewidgetitem64 = ___qtreewidgetitem62.child(1)
        ___qtreewidgetitem64.setText(0, QCoreApplication.translate("LaMainFormBase", u"Breeding Life", None));
        ___qtreewidgetitem65 = ___qtreewidgetitem62.child(2)
        ___qtreewidgetitem65.setText(0, QCoreApplication.translate("LaMainFormBase", u"Young per birth", None));
        ___qtreewidgetitem66 = ___qtreewidgetitem62.child(3)
        ___qtreewidgetitem66.setText(0, QCoreApplication.translate("LaMainFormBase", u"Weaning Age", None));
        ___qtreewidgetitem67 = ___qtreewidgetitem62.child(4)
        ___qtreewidgetitem67.setText(0, QCoreApplication.translate("LaMainFormBase", u"Gestation Time", None));
        ___qtreewidgetitem68 = ___qtreewidgetitem62.child(5)
        ___qtreewidgetitem68.setText(0, QCoreApplication.translate("LaMainFormBase", u"Estrous cycle", None));
        ___qtreewidgetitem69 = ___qtreewidgetitem54.child(2)
        ___qtreewidgetitem69.setText(0, QCoreApplication.translate("LaMainFormBase", u"Feeding Requirements", None));
        ___qtreewidgetitem70 = ___qtreewidgetitem69.child(0)
        ___qtreewidgetitem70.setText(0, QCoreApplication.translate("LaMainFormBase", u"Calories per animal per day", None));
        ___qtreewidgetitem71 = ___qtreewidgetitem70.child(0)
        ___qtreewidgetitem71.setText(0, QCoreApplication.translate("LaMainFormBase", u"While Gestating", None));
        ___qtreewidgetitem72 = ___qtreewidgetitem70.child(1)
        ___qtreewidgetitem72.setText(0, QCoreApplication.translate("LaMainFormBase", u"While Lactating", None));
        ___qtreewidgetitem73 = ___qtreewidgetitem70.child(2)
        ___qtreewidgetitem73.setText(0, QCoreApplication.translate("LaMainFormBase", u"Juveniles", None));
        ___qtreewidgetitem74 = ___qtreewidgetitem48.child(2)
        ___qtreewidgetitem74.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Parameters", None));
        ___qtreewidgetitem75 = ___qtreewidgetitem74.child(0)
        ___qtreewidgetitem75.setText(0, QCoreApplication.translate("LaMainFormBase", u"Setting Animal Parameters", None));
        ___qtreewidgetitem76 = ___qtreewidgetitem74.child(1)
        ___qtreewidgetitem76.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Parameter Details", None));
        ___qtreewidgetitem77 = ___qtreewidgetitem76.child(0)
        ___qtreewidgetitem77.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Parameter Name", None));
        ___qtreewidgetitem78 = ___qtreewidgetitem76.child(1)
        ___qtreewidgetitem78.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Parameter Notes", None));
        ___qtreewidgetitem79 = ___qtreewidgetitem76.child(2)
        ___qtreewidgetitem79.setText(0, QCoreApplication.translate("LaMainFormBase", u"Linking to an animal", None));
        ___qtreewidgetitem80 = ___qtreewidgetitem76.child(3)
        ___qtreewidgetitem80.setText(0, QCoreApplication.translate("LaMainFormBase", u"Portion of tame meat diet", None));
        ___qtreewidgetitem81 = ___qtreewidgetitem74.child(2)
        ___qtreewidgetitem81.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Land Suitability", None));
        ___qtreewidgetitem82 = ___qtreewidgetitem81.child(0)
        ___qtreewidgetitem82.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Specific Land", None));
        ___qtreewidgetitem83 = ___qtreewidgetitem82.child(0)
        ___qtreewidgetitem83.setText(0, QCoreApplication.translate("LaMainFormBase", u"KCal setting", None));
        ___qtreewidgetitem84 = ___qtreewidgetitem81.child(1)
        ___qtreewidgetitem84.setText(0, QCoreApplication.translate("LaMainFormBase", u"Animal Common Land", None));
        ___qtreewidgetitem85 = ___qtreewidgetitem84.child(0)
        ___qtreewidgetitem85.setText(0, QCoreApplication.translate("LaMainFormBase", u"KCal setting", None));
        ___qtreewidgetitem86 = ___qtreewidgetitem81.child(2)
        ___qtreewidgetitem86.setText(0, QCoreApplication.translate("LaMainFormBase", u"Selecting Area Units", None));
        ___qtreewidgetitem87 = ___qtreewidgetitem74.child(3)
        ___qtreewidgetitem87.setText(0, QCoreApplication.translate("LaMainFormBase", u"Fodder as feed", None));
        ___qtreewidgetitem88 = ___qtreewidgetitem87.child(0)
        ___qtreewidgetitem88.setText(0, QCoreApplication.translate("LaMainFormBase", u"Choosing feed", None));
        ___qtreewidgetitem89 = ___qtreewidgetitem88.child(0)
        ___qtreewidgetitem89.setText(0, QCoreApplication.translate("LaMainFormBase", u"Fodder feed", None));
        ___qtreewidgetitem90 = ___qtreewidgetitem88.child(1)
        ___qtreewidgetitem90.setText(0, QCoreApplication.translate("LaMainFormBase", u"Grain feed", None));
        ___qtreewidgetitem91 = ___qtreewidgetitem74.child(4)
        ___qtreewidgetitem91.setText(0, QCoreApplication.translate("LaMainFormBase", u"Fallow Use", None));
        ___qtreewidgetitem92 = ___qtreewidgetitem91.child(0)
        ___qtreewidgetitem92.setText(0, QCoreApplication.translate("LaMainFormBase", u"Grazing Fallow", None));
        ___qtreewidgetitem93 = ___qtreewidgetitem91.child(1)
        ___qtreewidgetitem93.setText(0, QCoreApplication.translate("LaMainFormBase", u"Fallow Priority", None));
        ___qtreewidgetitem94 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem94.setText(0, QCoreApplication.translate("LaMainFormBase", u"Calculations", None));
        ___qtreewidgetitem95 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem95.setText(0, QCoreApplication.translate("LaMainFormBase", u"Results", None));
        ___qtreewidgetitem96 = self.treeHelp.topLevelItem(1)
        ___qtreewidgetitem96.setText(0, QCoreApplication.translate("LaMainFormBase", u"Requirements", None));
        ___qtreewidgetitem97 = ___qtreewidgetitem96.child(0)
        ___qtreewidgetitem97.setText(0, QCoreApplication.translate("LaMainFormBase", u"File Preparation", None));
        ___qtreewidgetitem98 = ___qtreewidgetitem97.child(0)
        ___qtreewidgetitem98.setText(0, QCoreApplication.translate("LaMainFormBase", u"DEM", None));
        ___qtreewidgetitem99 = ___qtreewidgetitem97.child(1)
        ___qtreewidgetitem99.setText(0, QCoreApplication.translate("LaMainFormBase", u"Masks", None));
        ___qtreewidgetitem100 = ___qtreewidgetitem99.child(0)
        ___qtreewidgetitem100.setText(0, QCoreApplication.translate("LaMainFormBase", u"Digitizing", None));
        ___qtreewidgetitem101 = ___qtreewidgetitem99.child(1)
        ___qtreewidgetitem101.setText(0, QCoreApplication.translate("LaMainFormBase", u"Naming", None));
        ___qtreewidgetitem102 = ___qtreewidgetitem96.child(1)
        ___qtreewidgetitem102.setText(0, QCoreApplication.translate("LaMainFormBase", u"Numbers", None));
        self.treeHelp.setSortingEnabled(__sortingEnabled)

        self.cbDebug.setText(QCoreApplication.translate("LaMainFormBase", u"Debugging Mode", None))
        self.helpHeaderLabel.setText("")
        self.textHelp.setStyleSheet(QCoreApplication.translate("LaMainFormBase", u"<CENTER>", None))
        self.textHelp.setHtml(QCoreApplication.translate("LaMainFormBase", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:10pt; font-weight:600;\">To learn more about a feature or field in Landuse Analyst, you can do one of four things.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">1. </span><span style=\" font-family:'Sans Serif'; font-size:10pt; color:#0000ff;\">Hover over it</span><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> with your mouse arrow for a brief descript"
                        "ion</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">2. Click the </span><span style=\" font-family:'Sans Serif'; font-size:12pt; font-weight:600; color:#0000ff;\">?</span><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> in the top right of the main window and then click on the item you want detailed help for.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> Click anywhere to make the help box go away.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">3. RIght Click on the thing you want help for.  If there is detailed help for it, you will see a </span><span style=\" font-"
                        "family:'Sans Serif'; font-size:9pt; font-weight:600; color:#0000ff;\">What is this?</span><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> option that you can then click on.  Again, you can click anywhere to make the help box go away.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Sans Serif'; font-size:9pt;\">4. Go to the </span><span style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:600; color:#0000ff;\">Help</span><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> </span><span style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:600; color:#0000ff;\">Tab</span><span style=\" font-family:'Sans Serif'; font-size:9pt;\"> and click on the item you want help with on the left for an even more detailed description of what things are and how they work</span></p></body></html>", None))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.help_tab), QCoreApplication.translate("LaMainFormBase", u"Help", None))
    # retranslateUi

