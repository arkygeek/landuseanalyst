# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laexperimentbase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_ExperimentMainForm(object):
    def setupUi(self, ExperimentMainForm):
        if not ExperimentMainForm.objectName():
            ExperimentMainForm.setObjectName(u"ExperimentMainForm")
        ExperimentMainForm.resize(778, 768)
        self.buttonBox = QDialogButtonBox(ExperimentMainForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(420, 731, 349, 27))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.twExperiment = QTabWidget(ExperimentMainForm)
        self.twExperiment.setObjectName(u"twExperiment")
        self.twExperiment.setGeometry(QRect(10, 10, 745, 691))
        self.tabExperiment = QWidget()
        self.tabExperiment.setObjectName(u"tabExperiment")
        self.gridLayout = QGridLayout(self.tabExperiment)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_67 = QLabel(self.tabExperiment)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout.addWidget(self.label_67, 0, 0, 1, 3)

        self.label_68 = QLabel(self.tabExperiment)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout.addWidget(self.label_68, 1, 0, 1, 4)

        self.groupBoxManualSiteEntry = QGroupBox(self.tabExperiment)
        self.groupBoxManualSiteEntry.setObjectName(u"groupBoxManualSiteEntry")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxManualSiteEntry.sizePolicy().hasHeightForWidth())
        self.groupBoxManualSiteEntry.setSizePolicy(sizePolicy)
        self.groupBoxManualSiteEntry.setCheckable(False)
        self.groupBoxManualSiteEntry.setChecked(False)
        self.gridLayout1 = QGridLayout(self.groupBoxManualSiteEntry)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.textLabel2_4 = QLabel(self.groupBoxManualSiteEntry)
        self.textLabel2_4.setObjectName(u"textLabel2_4")
        self.textLabel2_4.setWordWrap(False)

        self.gridLayout1.addWidget(self.textLabel2_4, 0, 0, 1, 1)

        self.lineEditSiteName = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditSiteName.setObjectName(u"lineEditSiteName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditSiteName.sizePolicy().hasHeightForWidth())
        self.lineEditSiteName.setSizePolicy(sizePolicy1)

        self.gridLayout1.addWidget(self.lineEditSiteName, 0, 1, 1, 2)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label_70 = QLabel(self.groupBoxManualSiteEntry)
        self.label_70.setObjectName(u"label_70")

        self.hboxLayout.addWidget(self.label_70)

        self.lineEditEasting = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditEasting.setObjectName(u"lineEditEasting")

        self.hboxLayout.addWidget(self.lineEditEasting)


        self.gridLayout1.addLayout(self.hboxLayout, 1, 1, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label_71 = QLabel(self.groupBoxManualSiteEntry)
        self.label_71.setObjectName(u"label_71")

        self.hboxLayout1.addWidget(self.label_71)

        self.lineEditNorthing = QLineEdit(self.groupBoxManualSiteEntry)
        self.lineEditNorthing.setObjectName(u"lineEditNorthing")

        self.hboxLayout1.addWidget(self.lineEditNorthing)


        self.gridLayout1.addLayout(self.hboxLayout1, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBoxManualSiteEntry, 2, 0, 1, 2)

        self.gbxGrass = QGroupBox(self.tabExperiment)
        self.gbxGrass.setObjectName(u"gbxGrass")
        self.gridLayout2 = QGridLayout(self.gbxGrass)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.lblGrass = QLabel(self.gbxGrass)
        self.lblGrass.setObjectName(u"lblGrass")
        self.lblGrass.setMaximumSize(QSize(80, 80))
        self.lblGrass.setPixmap(QPixmap(u":/icona_grass.gif"))
        self.lblGrass.setScaledContents(True)

        self.gridLayout2.addWidget(self.lblGrass, 0, 0, 1, 1)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label_69 = QLabel(self.gbxGrass)
        self.label_69.setObjectName(u"label_69")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy2)

        self.hboxLayout2.addWidget(self.label_69)

        self.cboMapSet = QComboBox(self.gbxGrass)
        self.cboMapSet.setObjectName(u"cboMapSet")

        self.hboxLayout2.addWidget(self.cboMapSet)


        self.vboxLayout.addLayout(self.hboxLayout2)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.label_72 = QLabel(self.gbxGrass)
        self.label_72.setObjectName(u"label_72")
        sizePolicy2.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy2)
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout3.addWidget(self.label_72)

        self.cboDEM = QComboBox(self.gbxGrass)
        self.cboDEM.setObjectName(u"cboDEM")

        self.hboxLayout3.addWidget(self.cboDEM)


        self.vboxLayout.addLayout(self.hboxLayout3)


        self.gridLayout2.addLayout(self.vboxLayout, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.gbxGrass, 2, 2, 1, 2)

        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem, 2, 4, 1, 1)

        self.model_method_box = QGroupBox(self.tabExperiment)
        self.model_method_box.setObjectName(u"model_method_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.model_method_box.sizePolicy().hasHeightForWidth())
        self.model_method_box.setSizePolicy(sizePolicy3)
        self.gridLayout3 = QGridLayout(self.model_method_box)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.checkBox_81 = QCheckBox(self.model_method_box)
        self.checkBox_81.setObjectName(u"checkBox_81")

        self.gridLayout3.addWidget(self.checkBox_81, 0, 0, 1, 1)

        self.checkBox_82 = QCheckBox(self.model_method_box)
        self.checkBox_82.setObjectName(u"checkBox_82")

        self.gridLayout3.addWidget(self.checkBox_82, 1, 0, 1, 1)

        self.checkBox_83 = QCheckBox(self.model_method_box)
        self.checkBox_83.setObjectName(u"checkBox_83")

        self.gridLayout3.addWidget(self.checkBox_83, 2, 0, 1, 1)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setSpacing(0)
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.label_73 = QLabel(self.model_method_box)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout4.addWidget(self.label_73)

        self.sbModelPrecision = QSpinBox(self.model_method_box)
        self.sbModelPrecision.setObjectName(u"sbModelPrecision")
        sizePolicy3.setHeightForWidth(self.sbModelPrecision.sizePolicy().hasHeightForWidth())
        self.sbModelPrecision.setSizePolicy(sizePolicy3)
        self.sbModelPrecision.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sbModelPrecision.setMinimum(1)
        self.sbModelPrecision.setMaximum(50)
        self.sbModelPrecision.setValue(5)

        self.hboxLayout4.addWidget(self.sbModelPrecision)


        self.gridLayout3.addLayout(self.hboxLayout4, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.model_method_box, 3, 0, 3, 1)

        self.groupBox_25 = QGroupBox(self.tabExperiment)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.gridLayout4 = QGridLayout(self.groupBox_25)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.checkBox_75 = QCheckBox(self.groupBox_25)
        self.checkBox_75.setObjectName(u"checkBox_75")

        self.gridLayout4.addWidget(self.checkBox_75, 0, 0, 1, 1)

        self.checkBox_78 = QCheckBox(self.groupBox_25)
        self.checkBox_78.setObjectName(u"checkBox_78")

        self.gridLayout4.addWidget(self.checkBox_78, 0, 1, 1, 1)

        self.checkBox_76 = QCheckBox(self.groupBox_25)
        self.checkBox_76.setObjectName(u"checkBox_76")

        self.gridLayout4.addWidget(self.checkBox_76, 1, 0, 1, 1)

        self.checkBox_79 = QCheckBox(self.groupBox_25)
        self.checkBox_79.setObjectName(u"checkBox_79")

        self.gridLayout4.addWidget(self.checkBox_79, 1, 1, 1, 1)

        self.checkBox_77 = QCheckBox(self.groupBox_25)
        self.checkBox_77.setObjectName(u"checkBox_77")

        self.gridLayout4.addWidget(self.checkBox_77, 2, 0, 1, 1)

        self.checkBox_80 = QCheckBox(self.groupBox_25)
        self.checkBox_80.setObjectName(u"checkBox_80")

        self.gridLayout4.addWidget(self.checkBox_80, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_25, 3, 1, 3, 1)

        self.pushButton_13 = QPushButton(self.tabExperiment)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_13, 3, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.tabExperiment)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_14, 4, 2, 1, 1)

        self.spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem1, 4, 3, 1, 1)

        self.pushButton_15 = QPushButton(self.tabExperiment)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy4.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_15, 5, 2, 1, 1)

        self.spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacerItem2, 6, 1, 1, 1)

        self.twExperiment.addTab(self.tabExperiment, "")
        self.tabPeriod1 = QWidget()
        self.tabPeriod1.setObjectName(u"tabPeriod1")
        self.gridLayout5 = QGridLayout(self.tabPeriod1)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.comboBox_5 = QComboBox(self.tabPeriod1)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout5.addWidget(self.comboBox_5, 0, 0, 1, 2)

        self.label_3 = QLabel(self.tabPeriod1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout5.addWidget(self.label_3, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.tabPeriod1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout5.addWidget(self.lineEdit, 0, 3, 1, 3)

        self.line_7 = QFrame(self.tabPeriod1)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout5.addWidget(self.line_7, 0, 6, 2, 1)

        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout5.addItem(self.spacerItem3)

        self.pushButton = QPushButton(self.tabPeriod1)
        self.pushButton.setObjectName(u"pushButton")

        self.hboxLayout5.addWidget(self.pushButton)

        self.spacerItem4 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout5.addItem(self.spacerItem4)


        self.gridLayout5.addLayout(self.hboxLayout5, 0, 7, 1, 1)

        self.label_5 = QLabel(self.tabPeriod1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout5.addWidget(self.label_5, 1, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.tabPeriod1)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(20000)
        self.spinBox_4.setValue(500)

        self.gridLayout5.addWidget(self.spinBox_4, 1, 1, 1, 3)

        self.spinBox_3 = QSpinBox(self.tabPeriod1)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(20000)
        self.spinBox_3.setValue(1000)

        self.gridLayout5.addWidget(self.spinBox_3, 1, 4, 1, 2)

        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout6.addItem(self.spacerItem5)

        self.pushButton_2 = QPushButton(self.tabPeriod1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.hboxLayout6.addWidget(self.pushButton_2)

        self.spacerItem6 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout6.addItem(self.spacerItem6)


        self.gridLayout5.addLayout(self.hboxLayout6, 1, 7, 1, 1)

        self.gbDietComaprison = QGroupBox(self.tabPeriod1)
        self.gbDietComaprison.setObjectName(u"gbDietComaprison")
        self.gbDietComaprison.setCheckable(True)
        self.gridLayout6 = QGridLayout(self.gbDietComaprison)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.diet_comp_box = QGroupBox(self.gbDietComaprison)
        self.diet_comp_box.setObjectName(u"diet_comp_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.diet_comp_box.sizePolicy().hasHeightForWidth())
        self.diet_comp_box.setSizePolicy(sizePolicy5)
        self.gridLayout7 = QGridLayout(self.diet_comp_box)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.hboxLayout7 = QHBoxLayout()
        self.hboxLayout7.setObjectName(u"hboxLayout7")
        self.label6 = QLabel(self.diet_comp_box)
        self.label6.setObjectName(u"label6")
        self.label6.setWordWrap(False)

        self.hboxLayout7.addWidget(self.label6)

        self.spinBoxDailyCalories = QSpinBox(self.diet_comp_box)
        self.spinBoxDailyCalories.setObjectName(u"spinBoxDailyCalories")
        self.spinBoxDailyCalories.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories.setMinimum(1)
        self.spinBoxDailyCalories.setMaximum(5000)
        self.spinBoxDailyCalories.setSingleStep(1)
        self.spinBoxDailyCalories.setValue(2500)

        self.hboxLayout7.addWidget(self.spinBoxDailyCalories)


        self.gridLayout7.addLayout(self.hboxLayout7, 2, 0, 1, 2)

        self.groupplantpercent = QGroupBox(self.diet_comp_box)
        self.groupplantpercent.setObjectName(u"groupplantpercent")
        self.gridLayout8 = QGridLayout(self.groupplantpercent)
        self.gridLayout8.setObjectName(u"gridLayout8")
        self.spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout8.addItem(self.spacerItem7, 1, 1, 1, 1)

        self.labelCropTamePercent = QLabel(self.groupplantpercent)
        self.labelCropTamePercent.setObjectName(u"labelCropTamePercent")
        self.labelCropTamePercent.setAlignment(Qt.AlignCenter)

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
        self.labelCropWildPercent.setAlignment(Qt.AlignCenter)

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


        self.gridLayout7.addWidget(self.groupplantpercent, 1, 0, 1, 1)

        self.hboxLayout8 = QHBoxLayout()
        self.hboxLayout8.setObjectName(u"hboxLayout8")
        self.labelCropPercent = QLabel(self.diet_comp_box)
        self.labelCropPercent.setObjectName(u"labelCropPercent")

        self.hboxLayout8.addWidget(self.labelCropPercent)

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

        self.hboxLayout8.addWidget(self.sliderDiet)

        self.labelMeatPercent = QLabel(self.diet_comp_box)
        self.labelMeatPercent.setObjectName(u"labelMeatPercent")
        self.labelMeatPercent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout8.addWidget(self.labelMeatPercent)


        self.gridLayout7.addLayout(self.hboxLayout8, 0, 0, 1, 2)

        self.groupmeatpercent = QGroupBox(self.diet_comp_box)
        self.groupmeatpercent.setObjectName(u"groupmeatpercent")
        self.groupmeatpercent.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout9 = QGridLayout(self.groupmeatpercent)
        self.gridLayout9.setObjectName(u"gridLayout9")
        self.label_14 = QLabel(self.groupmeatpercent)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout9.addWidget(self.label_14, 0, 0, 1, 1)

        self.spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout9.addItem(self.spacerItem9, 1, 1, 1, 1)

        self.labelMeatWildPercent = QLabel(self.groupmeatpercent)
        self.labelMeatWildPercent.setObjectName(u"labelMeatWildPercent")
        self.labelMeatWildPercent.setAlignment(Qt.AlignCenter)

        self.gridLayout9.addWidget(self.labelMeatWildPercent, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupmeatpercent)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout9.addWidget(self.label_13, 0, 2, 1, 1)

        self.labelMeatTamePercent = QLabel(self.groupmeatpercent)
        self.labelMeatTamePercent.setObjectName(u"labelMeatTamePercent")
        self.labelMeatTamePercent.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent.setAlignment(Qt.AlignCenter)

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

        self.spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout9.addItem(self.spacerItem10, 0, 1, 1, 1)


        self.gridLayout7.addWidget(self.groupmeatpercent, 1, 1, 1, 1)

        self.spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout7.addItem(self.spacerItem11, 3, 0, 1, 2)


        self.gridLayout6.addWidget(self.diet_comp_box, 0, 0, 1, 1)

        self.line = QFrame(self.gbDietComaprison)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout6.addWidget(self.line, 0, 1, 1, 1)

        self.diet_comp_box_2 = QGroupBox(self.gbDietComaprison)
        self.diet_comp_box_2.setObjectName(u"diet_comp_box_2")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_2.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_2.setSizePolicy(sizePolicy5)
        self.gridLayout10 = QGridLayout(self.diet_comp_box_2)
        self.gridLayout10.setObjectName(u"gridLayout10")
        self.hboxLayout9 = QHBoxLayout()
        self.hboxLayout9.setObjectName(u"hboxLayout9")
        self.label6_2 = QLabel(self.diet_comp_box_2)
        self.label6_2.setObjectName(u"label6_2")
        self.label6_2.setWordWrap(False)

        self.hboxLayout9.addWidget(self.label6_2)

        self.spinBoxDailyCalories_2 = QSpinBox(self.diet_comp_box_2)
        self.spinBoxDailyCalories_2.setObjectName(u"spinBoxDailyCalories_2")
        self.spinBoxDailyCalories_2.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_2.setMinimum(1)
        self.spinBoxDailyCalories_2.setMaximum(5000)
        self.spinBoxDailyCalories_2.setSingleStep(1)
        self.spinBoxDailyCalories_2.setValue(2500)

        self.hboxLayout9.addWidget(self.spinBoxDailyCalories_2)


        self.gridLayout10.addLayout(self.hboxLayout9, 2, 0, 1, 2)

        self.groupplantpercent_2 = QGroupBox(self.diet_comp_box_2)
        self.groupplantpercent_2.setObjectName(u"groupplantpercent_2")
        self.gridLayout11 = QGridLayout(self.groupplantpercent_2)
        self.gridLayout11.setObjectName(u"gridLayout11")
        self.spacerItem12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout11.addItem(self.spacerItem12, 1, 1, 1, 1)

        self.labelCropTamePercent_2 = QLabel(self.groupplantpercent_2)
        self.labelCropTamePercent_2.setObjectName(u"labelCropTamePercent_2")
        self.labelCropTamePercent_2.setAlignment(Qt.AlignCenter)

        self.gridLayout11.addWidget(self.labelCropTamePercent_2, 1, 2, 1, 1)

        self.sliderCrop_2 = QSlider(self.groupplantpercent_2)
        self.sliderCrop_2.setObjectName(u"sliderCrop_2")
        self.sliderCrop_2.setMaximum(100)
        self.sliderCrop_2.setSingleStep(1)
        self.sliderCrop_2.setPageStep(1)
        self.sliderCrop_2.setValue(90)
        self.sliderCrop_2.setSliderPosition(90)
        self.sliderCrop_2.setOrientation(Qt.Horizontal)
        self.sliderCrop_2.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_2.setTickInterval(25)

        self.gridLayout11.addWidget(self.sliderCrop_2, 2, 0, 1, 3)

        self.labelCropWildPercent_2 = QLabel(self.groupplantpercent_2)
        self.labelCropWildPercent_2.setObjectName(u"labelCropWildPercent_2")
        self.labelCropWildPercent_2.setAlignment(Qt.AlignCenter)

        self.gridLayout11.addWidget(self.labelCropWildPercent_2, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupplantpercent_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout11.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupplantpercent_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout11.addWidget(self.label_12, 0, 2, 1, 1)

        self.spacerItem13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout11.addItem(self.spacerItem13, 0, 1, 1, 1)


        self.gridLayout10.addWidget(self.groupplantpercent_2, 1, 0, 1, 1)

        self.hboxLayout10 = QHBoxLayout()
        self.hboxLayout10.setObjectName(u"hboxLayout10")
        self.labelCropPercent_2 = QLabel(self.diet_comp_box_2)
        self.labelCropPercent_2.setObjectName(u"labelCropPercent_2")

        self.hboxLayout10.addWidget(self.labelCropPercent_2)

        self.sliderDiet_2 = QSlider(self.diet_comp_box_2)
        self.sliderDiet_2.setObjectName(u"sliderDiet_2")
        self.sliderDiet_2.setMaximum(100)
        self.sliderDiet_2.setSingleStep(1)
        self.sliderDiet_2.setPageStep(1)
        self.sliderDiet_2.setValue(50)
        self.sliderDiet_2.setSliderPosition(50)
        self.sliderDiet_2.setOrientation(Qt.Horizontal)
        self.sliderDiet_2.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_2.setTickInterval(25)

        self.hboxLayout10.addWidget(self.sliderDiet_2)

        self.labelMeatPercent_2 = QLabel(self.diet_comp_box_2)
        self.labelMeatPercent_2.setObjectName(u"labelMeatPercent_2")
        self.labelMeatPercent_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout10.addWidget(self.labelMeatPercent_2)


        self.gridLayout10.addLayout(self.hboxLayout10, 0, 0, 1, 2)

        self.groupmeatpercent_2 = QGroupBox(self.diet_comp_box_2)
        self.groupmeatpercent_2.setObjectName(u"groupmeatpercent_2")
        self.groupmeatpercent_2.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout12 = QGridLayout(self.groupmeatpercent_2)
        self.gridLayout12.setObjectName(u"gridLayout12")
        self.label_15 = QLabel(self.groupmeatpercent_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout12.addWidget(self.label_15, 0, 0, 1, 1)

        self.spacerItem14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout12.addItem(self.spacerItem14, 1, 1, 1, 1)

        self.labelMeatWildPercent_2 = QLabel(self.groupmeatpercent_2)
        self.labelMeatWildPercent_2.setObjectName(u"labelMeatWildPercent_2")
        self.labelMeatWildPercent_2.setAlignment(Qt.AlignCenter)

        self.gridLayout12.addWidget(self.labelMeatWildPercent_2, 1, 2, 1, 1)

        self.label_16 = QLabel(self.groupmeatpercent_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout12.addWidget(self.label_16, 0, 2, 1, 1)

        self.labelMeatTamePercent_2 = QLabel(self.groupmeatpercent_2)
        self.labelMeatTamePercent_2.setObjectName(u"labelMeatTamePercent_2")
        self.labelMeatTamePercent_2.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_2.setAlignment(Qt.AlignCenter)

        self.gridLayout12.addWidget(self.labelMeatTamePercent_2, 1, 0, 1, 1)

        self.sliderMeat_2 = QSlider(self.groupmeatpercent_2)
        self.sliderMeat_2.setObjectName(u"sliderMeat_2")
        self.sliderMeat_2.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_2.setMaximum(100)
        self.sliderMeat_2.setSingleStep(1)
        self.sliderMeat_2.setPageStep(1)
        self.sliderMeat_2.setValue(90)
        self.sliderMeat_2.setSliderPosition(90)
        self.sliderMeat_2.setOrientation(Qt.Horizontal)
        self.sliderMeat_2.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_2.setTickInterval(25)

        self.gridLayout12.addWidget(self.sliderMeat_2, 2, 0, 1, 3)

        self.spacerItem15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout12.addItem(self.spacerItem15, 0, 1, 1, 1)


        self.gridLayout10.addWidget(self.groupmeatpercent_2, 1, 1, 1, 1)

        self.spacerItem16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout10.addItem(self.spacerItem16, 3, 0, 1, 2)


        self.gridLayout6.addWidget(self.diet_comp_box_2, 0, 2, 1, 1)


        self.gridLayout5.addWidget(self.gbDietComaprison, 2, 0, 1, 8)

        self.gbCropMasks = QGroupBox(self.tabPeriod1)
        self.gbCropMasks.setObjectName(u"gbCropMasks")
        self.gbCropMasks.setCheckable(True)
        self.gridLayout13 = QGridLayout(self.gbCropMasks)
        self.gridLayout13.setObjectName(u"gridLayout13")
        self.radioButton = QRadioButton(self.gbCropMasks)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout13.addWidget(self.radioButton, 0, 0, 1, 2)

        self.doubleSpinBox = QDoubleSpinBox(self.gbCropMasks)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout13.addWidget(self.doubleSpinBox, 0, 2, 1, 2)

        self.spacerItem17 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout13.addItem(self.spacerItem17, 0, 4, 1, 1)

        self.radioButton_2 = QRadioButton(self.gbCropMasks)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout13.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gbCropMasks)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout13.addWidget(self.comboBox, 1, 1, 1, 4)

        self.radioButton_3 = QRadioButton(self.gbCropMasks)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout13.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gbCropMasks)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout13.addWidget(self.comboBox_2, 2, 1, 1, 4)

        self.groupBox = QGroupBox(self.gbCropMasks)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.gridLayout14 = QGridLayout(self.groupBox)
        self.gridLayout14.setObjectName(u"gridLayout14")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout14.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout14.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout14.addWidget(self.checkBox_3, 2, 0, 1, 1)


        self.gridLayout13.addWidget(self.groupBox, 3, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.gbCropMasks)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.gridLayout15 = QGridLayout(self.groupBox_2)
        self.gridLayout15.setObjectName(u"gridLayout15")
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout15.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout15.addWidget(self.checkBox_5, 1, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout15.addWidget(self.checkBox_6, 2, 0, 1, 1)


        self.gridLayout13.addWidget(self.groupBox_2, 3, 3, 1, 2)


        self.gridLayout5.addWidget(self.gbCropMasks, 3, 0, 1, 5)

        self.gbCropMasks_2 = QGroupBox(self.tabPeriod1)
        self.gbCropMasks_2.setObjectName(u"gbCropMasks_2")
        self.gbCropMasks_2.setCheckable(True)
        self.gridLayout16 = QGridLayout(self.gbCropMasks_2)
        self.gridLayout16.setObjectName(u"gridLayout16")
        self.radioButton_7 = QRadioButton(self.gbCropMasks_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout16.addWidget(self.radioButton_7, 0, 0, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.gbCropMasks_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout16.addWidget(self.doubleSpinBox_5, 0, 1, 1, 1)

        self.label = QLabel(self.gbCropMasks_2)
        self.label.setObjectName(u"label")

        self.gridLayout16.addWidget(self.label, 0, 2, 1, 2)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.gbCropMasks_2)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout16.addWidget(self.doubleSpinBox_4, 0, 4, 1, 1)

        self.spacerItem18 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout16.addItem(self.spacerItem18, 0, 5, 1, 1)

        self.radioButton_8 = QRadioButton(self.gbCropMasks_2)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout16.addWidget(self.radioButton_8, 1, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.gbCropMasks_2)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout16.addWidget(self.comboBox_6, 1, 1, 1, 5)

        self.radioButton_9 = QRadioButton(self.gbCropMasks_2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout16.addWidget(self.radioButton_9, 2, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.gbCropMasks_2)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout16.addWidget(self.comboBox_7, 2, 1, 1, 5)

        self.groupBox_3 = QGroupBox(self.gbCropMasks_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.gridLayout17 = QGridLayout(self.groupBox_3)
        self.gridLayout17.setObjectName(u"gridLayout17")
        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout17.addWidget(self.checkBox_7, 0, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout17.addWidget(self.checkBox_8, 1, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_3)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout17.addWidget(self.checkBox_9, 2, 0, 1, 1)


        self.gridLayout16.addWidget(self.groupBox_3, 3, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.gbCropMasks_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.gridLayout18 = QGridLayout(self.groupBox_4)
        self.gridLayout18.setObjectName(u"gridLayout18")
        self.checkBox_10 = QCheckBox(self.groupBox_4)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout18.addWidget(self.checkBox_10, 0, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.groupBox_4)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout18.addWidget(self.checkBox_11, 1, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox_4)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout18.addWidget(self.checkBox_12, 2, 0, 1, 1)


        self.gridLayout16.addWidget(self.groupBox_4, 3, 3, 1, 3)


        self.gridLayout5.addWidget(self.gbCropMasks_2, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod1, "")
        self.tabPeriod2 = QWidget()
        self.tabPeriod2.setObjectName(u"tabPeriod2")
        self.gridLayout19 = QGridLayout(self.tabPeriod2)
        self.gridLayout19.setObjectName(u"gridLayout19")
        self.comboBox_10 = QComboBox(self.tabPeriod2)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout19.addWidget(self.comboBox_10, 0, 0, 1, 2)

        self.label_4 = QLabel(self.tabPeriod2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout19.addWidget(self.label_4, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tabPeriod2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout19.addWidget(self.lineEdit_2, 0, 3, 1, 3)

        self.line_8 = QFrame(self.tabPeriod2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout19.addWidget(self.line_8, 0, 6, 2, 1)

        self.hboxLayout11 = QHBoxLayout()
        self.hboxLayout11.setObjectName(u"hboxLayout11")
        self.spacerItem19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout11.addItem(self.spacerItem19)

        self.pushButton_4 = QPushButton(self.tabPeriod2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.hboxLayout11.addWidget(self.pushButton_4)

        self.spacerItem20 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout11.addItem(self.spacerItem20)


        self.gridLayout19.addLayout(self.hboxLayout11, 0, 7, 1, 1)

        self.label_6 = QLabel(self.tabPeriod2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout19.addWidget(self.label_6, 1, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.tabPeriod2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(20000)
        self.spinBox_5.setValue(500)

        self.gridLayout19.addWidget(self.spinBox_5, 1, 1, 1, 3)

        self.spinBox_6 = QSpinBox(self.tabPeriod2)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(20000)
        self.spinBox_6.setValue(1000)

        self.gridLayout19.addWidget(self.spinBox_6, 1, 4, 1, 2)

        self.hboxLayout12 = QHBoxLayout()
        self.hboxLayout12.setObjectName(u"hboxLayout12")
        self.spacerItem21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout12.addItem(self.spacerItem21)

        self.pushButton_3 = QPushButton(self.tabPeriod2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.hboxLayout12.addWidget(self.pushButton_3)

        self.spacerItem22 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout12.addItem(self.spacerItem22)


        self.gridLayout19.addLayout(self.hboxLayout12, 1, 7, 1, 1)

        self.gbDietComaprison_2 = QGroupBox(self.tabPeriod2)
        self.gbDietComaprison_2.setObjectName(u"gbDietComaprison_2")
        self.gbDietComaprison_2.setCheckable(True)
        self.gridLayout20 = QGridLayout(self.gbDietComaprison_2)
        self.gridLayout20.setObjectName(u"gridLayout20")
        self.diet_comp_box_3 = QGroupBox(self.gbDietComaprison_2)
        self.diet_comp_box_3.setObjectName(u"diet_comp_box_3")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_3.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_3.setSizePolicy(sizePolicy5)
        self.gridLayout21 = QGridLayout(self.diet_comp_box_3)
        self.gridLayout21.setObjectName(u"gridLayout21")
        self.hboxLayout13 = QHBoxLayout()
        self.hboxLayout13.setObjectName(u"hboxLayout13")
        self.label6_3 = QLabel(self.diet_comp_box_3)
        self.label6_3.setObjectName(u"label6_3")
        self.label6_3.setWordWrap(False)

        self.hboxLayout13.addWidget(self.label6_3)

        self.spinBoxDailyCalories_3 = QSpinBox(self.diet_comp_box_3)
        self.spinBoxDailyCalories_3.setObjectName(u"spinBoxDailyCalories_3")
        self.spinBoxDailyCalories_3.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_3.setMinimum(1)
        self.spinBoxDailyCalories_3.setMaximum(5000)
        self.spinBoxDailyCalories_3.setSingleStep(1)
        self.spinBoxDailyCalories_3.setValue(2500)

        self.hboxLayout13.addWidget(self.spinBoxDailyCalories_3)


        self.gridLayout21.addLayout(self.hboxLayout13, 2, 0, 1, 2)

        self.groupplantpercent_3 = QGroupBox(self.diet_comp_box_3)
        self.groupplantpercent_3.setObjectName(u"groupplantpercent_3")
        self.gridLayout22 = QGridLayout(self.groupplantpercent_3)
        self.gridLayout22.setObjectName(u"gridLayout22")
        self.spacerItem23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout22.addItem(self.spacerItem23, 1, 1, 1, 1)

        self.labelCropTamePercent_3 = QLabel(self.groupplantpercent_3)
        self.labelCropTamePercent_3.setObjectName(u"labelCropTamePercent_3")
        self.labelCropTamePercent_3.setAlignment(Qt.AlignCenter)

        self.gridLayout22.addWidget(self.labelCropTamePercent_3, 1, 2, 1, 1)

        self.sliderCrop_3 = QSlider(self.groupplantpercent_3)
        self.sliderCrop_3.setObjectName(u"sliderCrop_3")
        self.sliderCrop_3.setMaximum(100)
        self.sliderCrop_3.setSingleStep(1)
        self.sliderCrop_3.setPageStep(1)
        self.sliderCrop_3.setValue(90)
        self.sliderCrop_3.setSliderPosition(90)
        self.sliderCrop_3.setOrientation(Qt.Horizontal)
        self.sliderCrop_3.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_3.setTickInterval(25)

        self.gridLayout22.addWidget(self.sliderCrop_3, 2, 0, 1, 3)

        self.labelCropWildPercent_3 = QLabel(self.groupplantpercent_3)
        self.labelCropWildPercent_3.setObjectName(u"labelCropWildPercent_3")
        self.labelCropWildPercent_3.setAlignment(Qt.AlignCenter)

        self.gridLayout22.addWidget(self.labelCropWildPercent_3, 1, 0, 1, 1)

        self.label_17 = QLabel(self.groupplantpercent_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout22.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_18 = QLabel(self.groupplantpercent_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout22.addWidget(self.label_18, 0, 2, 1, 1)

        self.spacerItem24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout22.addItem(self.spacerItem24, 0, 1, 1, 1)


        self.gridLayout21.addWidget(self.groupplantpercent_3, 1, 0, 1, 1)

        self.hboxLayout14 = QHBoxLayout()
        self.hboxLayout14.setObjectName(u"hboxLayout14")
        self.labelCropPercent_3 = QLabel(self.diet_comp_box_3)
        self.labelCropPercent_3.setObjectName(u"labelCropPercent_3")

        self.hboxLayout14.addWidget(self.labelCropPercent_3)

        self.sliderDiet_3 = QSlider(self.diet_comp_box_3)
        self.sliderDiet_3.setObjectName(u"sliderDiet_3")
        self.sliderDiet_3.setMaximum(100)
        self.sliderDiet_3.setSingleStep(1)
        self.sliderDiet_3.setPageStep(1)
        self.sliderDiet_3.setValue(50)
        self.sliderDiet_3.setSliderPosition(50)
        self.sliderDiet_3.setOrientation(Qt.Horizontal)
        self.sliderDiet_3.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_3.setTickInterval(25)

        self.hboxLayout14.addWidget(self.sliderDiet_3)

        self.labelMeatPercent_3 = QLabel(self.diet_comp_box_3)
        self.labelMeatPercent_3.setObjectName(u"labelMeatPercent_3")
        self.labelMeatPercent_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout14.addWidget(self.labelMeatPercent_3)


        self.gridLayout21.addLayout(self.hboxLayout14, 0, 0, 1, 2)

        self.groupmeatpercent_3 = QGroupBox(self.diet_comp_box_3)
        self.groupmeatpercent_3.setObjectName(u"groupmeatpercent_3")
        self.groupmeatpercent_3.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout23 = QGridLayout(self.groupmeatpercent_3)
        self.gridLayout23.setObjectName(u"gridLayout23")
        self.label_19 = QLabel(self.groupmeatpercent_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout23.addWidget(self.label_19, 0, 0, 1, 1)

        self.spacerItem25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout23.addItem(self.spacerItem25, 1, 1, 1, 1)

        self.labelMeatWildPercent_3 = QLabel(self.groupmeatpercent_3)
        self.labelMeatWildPercent_3.setObjectName(u"labelMeatWildPercent_3")
        self.labelMeatWildPercent_3.setAlignment(Qt.AlignCenter)

        self.gridLayout23.addWidget(self.labelMeatWildPercent_3, 1, 2, 1, 1)

        self.label_20 = QLabel(self.groupmeatpercent_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout23.addWidget(self.label_20, 0, 2, 1, 1)

        self.labelMeatTamePercent_3 = QLabel(self.groupmeatpercent_3)
        self.labelMeatTamePercent_3.setObjectName(u"labelMeatTamePercent_3")
        self.labelMeatTamePercent_3.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_3.setAlignment(Qt.AlignCenter)

        self.gridLayout23.addWidget(self.labelMeatTamePercent_3, 1, 0, 1, 1)

        self.sliderMeat_3 = QSlider(self.groupmeatpercent_3)
        self.sliderMeat_3.setObjectName(u"sliderMeat_3")
        self.sliderMeat_3.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_3.setMaximum(100)
        self.sliderMeat_3.setSingleStep(1)
        self.sliderMeat_3.setPageStep(1)
        self.sliderMeat_3.setValue(90)
        self.sliderMeat_3.setSliderPosition(90)
        self.sliderMeat_3.setOrientation(Qt.Horizontal)
        self.sliderMeat_3.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_3.setTickInterval(25)

        self.gridLayout23.addWidget(self.sliderMeat_3, 2, 0, 1, 3)

        self.spacerItem26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout23.addItem(self.spacerItem26, 0, 1, 1, 1)


        self.gridLayout21.addWidget(self.groupmeatpercent_3, 1, 1, 1, 1)

        self.spacerItem27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout21.addItem(self.spacerItem27, 3, 0, 1, 2)


        self.gridLayout20.addWidget(self.diet_comp_box_3, 0, 0, 1, 1)

        self.line_2 = QFrame(self.gbDietComaprison_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout20.addWidget(self.line_2, 0, 1, 1, 1)

        self.diet_comp_box_4 = QGroupBox(self.gbDietComaprison_2)
        self.diet_comp_box_4.setObjectName(u"diet_comp_box_4")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_4.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_4.setSizePolicy(sizePolicy5)
        self.gridLayout24 = QGridLayout(self.diet_comp_box_4)
        self.gridLayout24.setObjectName(u"gridLayout24")
        self.hboxLayout15 = QHBoxLayout()
        self.hboxLayout15.setObjectName(u"hboxLayout15")
        self.label6_4 = QLabel(self.diet_comp_box_4)
        self.label6_4.setObjectName(u"label6_4")
        self.label6_4.setWordWrap(False)

        self.hboxLayout15.addWidget(self.label6_4)

        self.spinBoxDailyCalories_4 = QSpinBox(self.diet_comp_box_4)
        self.spinBoxDailyCalories_4.setObjectName(u"spinBoxDailyCalories_4")
        self.spinBoxDailyCalories_4.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_4.setMinimum(1)
        self.spinBoxDailyCalories_4.setMaximum(5000)
        self.spinBoxDailyCalories_4.setSingleStep(1)
        self.spinBoxDailyCalories_4.setValue(2500)

        self.hboxLayout15.addWidget(self.spinBoxDailyCalories_4)


        self.gridLayout24.addLayout(self.hboxLayout15, 2, 0, 1, 2)

        self.groupplantpercent_4 = QGroupBox(self.diet_comp_box_4)
        self.groupplantpercent_4.setObjectName(u"groupplantpercent_4")
        self.gridLayout25 = QGridLayout(self.groupplantpercent_4)
        self.gridLayout25.setObjectName(u"gridLayout25")
        self.spacerItem28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout25.addItem(self.spacerItem28, 1, 1, 1, 1)

        self.labelCropTamePercent_4 = QLabel(self.groupplantpercent_4)
        self.labelCropTamePercent_4.setObjectName(u"labelCropTamePercent_4")
        self.labelCropTamePercent_4.setAlignment(Qt.AlignCenter)

        self.gridLayout25.addWidget(self.labelCropTamePercent_4, 1, 2, 1, 1)

        self.sliderCrop_4 = QSlider(self.groupplantpercent_4)
        self.sliderCrop_4.setObjectName(u"sliderCrop_4")
        self.sliderCrop_4.setMaximum(100)
        self.sliderCrop_4.setSingleStep(1)
        self.sliderCrop_4.setPageStep(1)
        self.sliderCrop_4.setValue(90)
        self.sliderCrop_4.setSliderPosition(90)
        self.sliderCrop_4.setOrientation(Qt.Horizontal)
        self.sliderCrop_4.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_4.setTickInterval(25)

        self.gridLayout25.addWidget(self.sliderCrop_4, 2, 0, 1, 3)

        self.labelCropWildPercent_4 = QLabel(self.groupplantpercent_4)
        self.labelCropWildPercent_4.setObjectName(u"labelCropWildPercent_4")
        self.labelCropWildPercent_4.setAlignment(Qt.AlignCenter)

        self.gridLayout25.addWidget(self.labelCropWildPercent_4, 1, 0, 1, 1)

        self.label_21 = QLabel(self.groupplantpercent_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout25.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.groupplantpercent_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout25.addWidget(self.label_22, 0, 2, 1, 1)

        self.spacerItem29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout25.addItem(self.spacerItem29, 0, 1, 1, 1)


        self.gridLayout24.addWidget(self.groupplantpercent_4, 1, 0, 1, 1)

        self.hboxLayout16 = QHBoxLayout()
        self.hboxLayout16.setObjectName(u"hboxLayout16")
        self.labelCropPercent_4 = QLabel(self.diet_comp_box_4)
        self.labelCropPercent_4.setObjectName(u"labelCropPercent_4")

        self.hboxLayout16.addWidget(self.labelCropPercent_4)

        self.sliderDiet_4 = QSlider(self.diet_comp_box_4)
        self.sliderDiet_4.setObjectName(u"sliderDiet_4")
        self.sliderDiet_4.setMaximum(100)
        self.sliderDiet_4.setSingleStep(1)
        self.sliderDiet_4.setPageStep(1)
        self.sliderDiet_4.setValue(50)
        self.sliderDiet_4.setSliderPosition(50)
        self.sliderDiet_4.setOrientation(Qt.Horizontal)
        self.sliderDiet_4.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_4.setTickInterval(25)

        self.hboxLayout16.addWidget(self.sliderDiet_4)

        self.labelMeatPercent_4 = QLabel(self.diet_comp_box_4)
        self.labelMeatPercent_4.setObjectName(u"labelMeatPercent_4")
        self.labelMeatPercent_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout16.addWidget(self.labelMeatPercent_4)


        self.gridLayout24.addLayout(self.hboxLayout16, 0, 0, 1, 2)

        self.groupmeatpercent_4 = QGroupBox(self.diet_comp_box_4)
        self.groupmeatpercent_4.setObjectName(u"groupmeatpercent_4")
        self.groupmeatpercent_4.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout26 = QGridLayout(self.groupmeatpercent_4)
        self.gridLayout26.setObjectName(u"gridLayout26")
        self.label_23 = QLabel(self.groupmeatpercent_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout26.addWidget(self.label_23, 0, 0, 1, 1)

        self.spacerItem30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout26.addItem(self.spacerItem30, 1, 1, 1, 1)

        self.labelMeatWildPercent_4 = QLabel(self.groupmeatpercent_4)
        self.labelMeatWildPercent_4.setObjectName(u"labelMeatWildPercent_4")
        self.labelMeatWildPercent_4.setAlignment(Qt.AlignCenter)

        self.gridLayout26.addWidget(self.labelMeatWildPercent_4, 1, 2, 1, 1)

        self.label_24 = QLabel(self.groupmeatpercent_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout26.addWidget(self.label_24, 0, 2, 1, 1)

        self.labelMeatTamePercent_4 = QLabel(self.groupmeatpercent_4)
        self.labelMeatTamePercent_4.setObjectName(u"labelMeatTamePercent_4")
        self.labelMeatTamePercent_4.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_4.setAlignment(Qt.AlignCenter)

        self.gridLayout26.addWidget(self.labelMeatTamePercent_4, 1, 0, 1, 1)

        self.sliderMeat_4 = QSlider(self.groupmeatpercent_4)
        self.sliderMeat_4.setObjectName(u"sliderMeat_4")
        self.sliderMeat_4.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_4.setMaximum(100)
        self.sliderMeat_4.setSingleStep(1)
        self.sliderMeat_4.setPageStep(1)
        self.sliderMeat_4.setValue(90)
        self.sliderMeat_4.setSliderPosition(90)
        self.sliderMeat_4.setOrientation(Qt.Horizontal)
        self.sliderMeat_4.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_4.setTickInterval(25)

        self.gridLayout26.addWidget(self.sliderMeat_4, 2, 0, 1, 3)

        self.spacerItem31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout26.addItem(self.spacerItem31, 0, 1, 1, 1)


        self.gridLayout24.addWidget(self.groupmeatpercent_4, 1, 1, 1, 1)

        self.spacerItem32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout24.addItem(self.spacerItem32, 3, 0, 1, 2)


        self.gridLayout20.addWidget(self.diet_comp_box_4, 0, 2, 1, 1)


        self.gridLayout19.addWidget(self.gbDietComaprison_2, 2, 0, 1, 8)

        self.gbCropMasks_3 = QGroupBox(self.tabPeriod2)
        self.gbCropMasks_3.setObjectName(u"gbCropMasks_3")
        self.gbCropMasks_3.setCheckable(True)
        self.gridLayout27 = QGridLayout(self.gbCropMasks_3)
        self.gridLayout27.setObjectName(u"gridLayout27")
        self.radioButton_4 = QRadioButton(self.gbCropMasks_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout27.addWidget(self.radioButton_4, 0, 0, 1, 2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.gbCropMasks_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout27.addWidget(self.doubleSpinBox_2, 0, 2, 1, 2)

        self.spacerItem33 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout27.addItem(self.spacerItem33, 0, 4, 1, 1)

        self.radioButton_5 = QRadioButton(self.gbCropMasks_3)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout27.addWidget(self.radioButton_5, 1, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.gbCropMasks_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout27.addWidget(self.comboBox_3, 1, 1, 1, 4)

        self.radioButton_6 = QRadioButton(self.gbCropMasks_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout27.addWidget(self.radioButton_6, 2, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.gbCropMasks_3)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout27.addWidget(self.comboBox_4, 2, 1, 1, 4)

        self.groupBox_5 = QGroupBox(self.gbCropMasks_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        self.gridLayout28 = QGridLayout(self.groupBox_5)
        self.gridLayout28.setObjectName(u"gridLayout28")
        self.checkBox_15 = QCheckBox(self.groupBox_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout28.addWidget(self.checkBox_15, 0, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.groupBox_5)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout28.addWidget(self.checkBox_16, 1, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.groupBox_5)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout28.addWidget(self.checkBox_17, 2, 0, 1, 1)


        self.gridLayout27.addWidget(self.groupBox_5, 3, 0, 1, 3)

        self.groupBox_6 = QGroupBox(self.gbCropMasks_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setChecked(False)
        self.gridLayout29 = QGridLayout(self.groupBox_6)
        self.gridLayout29.setObjectName(u"gridLayout29")
        self.checkBox_18 = QCheckBox(self.groupBox_6)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout29.addWidget(self.checkBox_18, 0, 0, 1, 1)

        self.checkBox_19 = QCheckBox(self.groupBox_6)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout29.addWidget(self.checkBox_19, 1, 0, 1, 1)

        self.checkBox_20 = QCheckBox(self.groupBox_6)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout29.addWidget(self.checkBox_20, 2, 0, 1, 1)


        self.gridLayout27.addWidget(self.groupBox_6, 3, 3, 1, 2)


        self.gridLayout19.addWidget(self.gbCropMasks_3, 3, 0, 1, 5)

        self.gbCropMasks_4 = QGroupBox(self.tabPeriod2)
        self.gbCropMasks_4.setObjectName(u"gbCropMasks_4")
        self.gbCropMasks_4.setCheckable(True)
        self.gridLayout30 = QGridLayout(self.gbCropMasks_4)
        self.gridLayout30.setObjectName(u"gridLayout30")
        self.radioButton_10 = QRadioButton(self.gbCropMasks_4)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout30.addWidget(self.radioButton_10, 0, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.gbCropMasks_4)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout30.addWidget(self.doubleSpinBox_6, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gbCropMasks_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout30.addWidget(self.label_2, 0, 2, 1, 2)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.gbCropMasks_4)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout30.addWidget(self.doubleSpinBox_7, 0, 4, 1, 1)

        self.spacerItem34 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout30.addItem(self.spacerItem34, 0, 5, 1, 1)

        self.radioButton_11 = QRadioButton(self.gbCropMasks_4)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout30.addWidget(self.radioButton_11, 1, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.gbCropMasks_4)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout30.addWidget(self.comboBox_8, 1, 1, 1, 5)

        self.radioButton_12 = QRadioButton(self.gbCropMasks_4)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout30.addWidget(self.radioButton_12, 2, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.gbCropMasks_4)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout30.addWidget(self.comboBox_9, 2, 1, 1, 5)

        self.groupBox_7 = QGroupBox(self.gbCropMasks_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.gridLayout31 = QGridLayout(self.groupBox_7)
        self.gridLayout31.setObjectName(u"gridLayout31")
        self.checkBox_21 = QCheckBox(self.groupBox_7)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout31.addWidget(self.checkBox_21, 0, 0, 1, 1)

        self.checkBox_22 = QCheckBox(self.groupBox_7)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout31.addWidget(self.checkBox_22, 1, 0, 1, 1)

        self.checkBox_23 = QCheckBox(self.groupBox_7)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout31.addWidget(self.checkBox_23, 2, 0, 1, 1)


        self.gridLayout30.addWidget(self.groupBox_7, 3, 0, 1, 3)

        self.groupBox_8 = QGroupBox(self.gbCropMasks_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setCheckable(True)
        self.groupBox_8.setChecked(False)
        self.gridLayout32 = QGridLayout(self.groupBox_8)
        self.gridLayout32.setObjectName(u"gridLayout32")
        self.checkBox_24 = QCheckBox(self.groupBox_8)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout32.addWidget(self.checkBox_24, 0, 0, 1, 1)

        self.checkBox_25 = QCheckBox(self.groupBox_8)
        self.checkBox_25.setObjectName(u"checkBox_25")

        self.gridLayout32.addWidget(self.checkBox_25, 1, 0, 1, 1)

        self.checkBox_26 = QCheckBox(self.groupBox_8)
        self.checkBox_26.setObjectName(u"checkBox_26")

        self.gridLayout32.addWidget(self.checkBox_26, 2, 0, 1, 1)


        self.gridLayout30.addWidget(self.groupBox_8, 3, 3, 1, 3)


        self.gridLayout19.addWidget(self.gbCropMasks_4, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod2, "")
        self.tabPeriod3 = QWidget()
        self.tabPeriod3.setObjectName(u"tabPeriod3")
        self.gridLayout33 = QGridLayout(self.tabPeriod3)
        self.gridLayout33.setObjectName(u"gridLayout33")
        self.comboBox_13 = QComboBox(self.tabPeriod3)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.gridLayout33.addWidget(self.comboBox_13, 0, 0, 1, 2)

        self.label_33 = QLabel(self.tabPeriod3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout33.addWidget(self.label_33, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tabPeriod3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout33.addWidget(self.lineEdit_3, 0, 3, 1, 3)

        self.line_9 = QFrame(self.tabPeriod3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout33.addWidget(self.line_9, 0, 6, 2, 1)

        self.hboxLayout17 = QHBoxLayout()
        self.hboxLayout17.setObjectName(u"hboxLayout17")
        self.spacerItem35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout17.addItem(self.spacerItem35)

        self.pushButton_6 = QPushButton(self.tabPeriod3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.hboxLayout17.addWidget(self.pushButton_6)

        self.spacerItem36 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout17.addItem(self.spacerItem36)


        self.gridLayout33.addLayout(self.hboxLayout17, 0, 7, 1, 1)

        self.label_7 = QLabel(self.tabPeriod3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout33.addWidget(self.label_7, 1, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.tabPeriod3)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(20000)
        self.spinBox_7.setValue(500)

        self.gridLayout33.addWidget(self.spinBox_7, 1, 1, 1, 3)

        self.spinBox_8 = QSpinBox(self.tabPeriod3)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(20000)
        self.spinBox_8.setValue(1000)

        self.gridLayout33.addWidget(self.spinBox_8, 1, 4, 1, 2)

        self.hboxLayout18 = QHBoxLayout()
        self.hboxLayout18.setObjectName(u"hboxLayout18")
        self.spacerItem37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout18.addItem(self.spacerItem37)

        self.pushButton_5 = QPushButton(self.tabPeriod3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.hboxLayout18.addWidget(self.pushButton_5)

        self.spacerItem38 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout18.addItem(self.spacerItem38)


        self.gridLayout33.addLayout(self.hboxLayout18, 1, 7, 1, 1)

        self.gbDietComaprison_3 = QGroupBox(self.tabPeriod3)
        self.gbDietComaprison_3.setObjectName(u"gbDietComaprison_3")
        self.gbDietComaprison_3.setCheckable(True)
        self.gridLayout34 = QGridLayout(self.gbDietComaprison_3)
        self.gridLayout34.setObjectName(u"gridLayout34")
        self.diet_comp_box_5 = QGroupBox(self.gbDietComaprison_3)
        self.diet_comp_box_5.setObjectName(u"diet_comp_box_5")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_5.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_5.setSizePolicy(sizePolicy5)
        self.gridLayout35 = QGridLayout(self.diet_comp_box_5)
        self.gridLayout35.setObjectName(u"gridLayout35")
        self.hboxLayout19 = QHBoxLayout()
        self.hboxLayout19.setObjectName(u"hboxLayout19")
        self.label6_5 = QLabel(self.diet_comp_box_5)
        self.label6_5.setObjectName(u"label6_5")
        self.label6_5.setWordWrap(False)

        self.hboxLayout19.addWidget(self.label6_5)

        self.spinBoxDailyCalories_5 = QSpinBox(self.diet_comp_box_5)
        self.spinBoxDailyCalories_5.setObjectName(u"spinBoxDailyCalories_5")
        self.spinBoxDailyCalories_5.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_5.setMinimum(1)
        self.spinBoxDailyCalories_5.setMaximum(5000)
        self.spinBoxDailyCalories_5.setSingleStep(1)
        self.spinBoxDailyCalories_5.setValue(2500)

        self.hboxLayout19.addWidget(self.spinBoxDailyCalories_5)


        self.gridLayout35.addLayout(self.hboxLayout19, 2, 0, 1, 2)

        self.groupplantpercent_5 = QGroupBox(self.diet_comp_box_5)
        self.groupplantpercent_5.setObjectName(u"groupplantpercent_5")
        self.gridLayout36 = QGridLayout(self.groupplantpercent_5)
        self.gridLayout36.setObjectName(u"gridLayout36")
        self.spacerItem39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout36.addItem(self.spacerItem39, 1, 1, 1, 1)

        self.labelCropTamePercent_5 = QLabel(self.groupplantpercent_5)
        self.labelCropTamePercent_5.setObjectName(u"labelCropTamePercent_5")
        self.labelCropTamePercent_5.setAlignment(Qt.AlignCenter)

        self.gridLayout36.addWidget(self.labelCropTamePercent_5, 1, 2, 1, 1)

        self.sliderCrop_5 = QSlider(self.groupplantpercent_5)
        self.sliderCrop_5.setObjectName(u"sliderCrop_5")
        self.sliderCrop_5.setMaximum(100)
        self.sliderCrop_5.setSingleStep(1)
        self.sliderCrop_5.setPageStep(1)
        self.sliderCrop_5.setValue(90)
        self.sliderCrop_5.setSliderPosition(90)
        self.sliderCrop_5.setOrientation(Qt.Horizontal)
        self.sliderCrop_5.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_5.setTickInterval(25)

        self.gridLayout36.addWidget(self.sliderCrop_5, 2, 0, 1, 3)

        self.labelCropWildPercent_5 = QLabel(self.groupplantpercent_5)
        self.labelCropWildPercent_5.setObjectName(u"labelCropWildPercent_5")
        self.labelCropWildPercent_5.setAlignment(Qt.AlignCenter)

        self.gridLayout36.addWidget(self.labelCropWildPercent_5, 1, 0, 1, 1)

        self.label_25 = QLabel(self.groupplantpercent_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout36.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.groupplantpercent_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout36.addWidget(self.label_26, 0, 2, 1, 1)

        self.spacerItem40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout36.addItem(self.spacerItem40, 0, 1, 1, 1)


        self.gridLayout35.addWidget(self.groupplantpercent_5, 1, 0, 1, 1)

        self.hboxLayout20 = QHBoxLayout()
        self.hboxLayout20.setObjectName(u"hboxLayout20")
        self.labelCropPercent_5 = QLabel(self.diet_comp_box_5)
        self.labelCropPercent_5.setObjectName(u"labelCropPercent_5")

        self.hboxLayout20.addWidget(self.labelCropPercent_5)

        self.sliderDiet_5 = QSlider(self.diet_comp_box_5)
        self.sliderDiet_5.setObjectName(u"sliderDiet_5")
        self.sliderDiet_5.setMaximum(100)
        self.sliderDiet_5.setSingleStep(1)
        self.sliderDiet_5.setPageStep(1)
        self.sliderDiet_5.setValue(50)
        self.sliderDiet_5.setSliderPosition(50)
        self.sliderDiet_5.setOrientation(Qt.Horizontal)
        self.sliderDiet_5.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_5.setTickInterval(25)

        self.hboxLayout20.addWidget(self.sliderDiet_5)

        self.labelMeatPercent_5 = QLabel(self.diet_comp_box_5)
        self.labelMeatPercent_5.setObjectName(u"labelMeatPercent_5")
        self.labelMeatPercent_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout20.addWidget(self.labelMeatPercent_5)


        self.gridLayout35.addLayout(self.hboxLayout20, 0, 0, 1, 2)

        self.groupmeatpercent_5 = QGroupBox(self.diet_comp_box_5)
        self.groupmeatpercent_5.setObjectName(u"groupmeatpercent_5")
        self.groupmeatpercent_5.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout37 = QGridLayout(self.groupmeatpercent_5)
        self.gridLayout37.setObjectName(u"gridLayout37")
        self.label_27 = QLabel(self.groupmeatpercent_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout37.addWidget(self.label_27, 0, 0, 1, 1)

        self.spacerItem41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout37.addItem(self.spacerItem41, 1, 1, 1, 1)

        self.labelMeatWildPercent_5 = QLabel(self.groupmeatpercent_5)
        self.labelMeatWildPercent_5.setObjectName(u"labelMeatWildPercent_5")
        self.labelMeatWildPercent_5.setAlignment(Qt.AlignCenter)

        self.gridLayout37.addWidget(self.labelMeatWildPercent_5, 1, 2, 1, 1)

        self.label_28 = QLabel(self.groupmeatpercent_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout37.addWidget(self.label_28, 0, 2, 1, 1)

        self.labelMeatTamePercent_5 = QLabel(self.groupmeatpercent_5)
        self.labelMeatTamePercent_5.setObjectName(u"labelMeatTamePercent_5")
        self.labelMeatTamePercent_5.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_5.setAlignment(Qt.AlignCenter)

        self.gridLayout37.addWidget(self.labelMeatTamePercent_5, 1, 0, 1, 1)

        self.sliderMeat_5 = QSlider(self.groupmeatpercent_5)
        self.sliderMeat_5.setObjectName(u"sliderMeat_5")
        self.sliderMeat_5.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_5.setMaximum(100)
        self.sliderMeat_5.setSingleStep(1)
        self.sliderMeat_5.setPageStep(1)
        self.sliderMeat_5.setValue(90)
        self.sliderMeat_5.setSliderPosition(90)
        self.sliderMeat_5.setOrientation(Qt.Horizontal)
        self.sliderMeat_5.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_5.setTickInterval(25)

        self.gridLayout37.addWidget(self.sliderMeat_5, 2, 0, 1, 3)

        self.spacerItem42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout37.addItem(self.spacerItem42, 0, 1, 1, 1)


        self.gridLayout35.addWidget(self.groupmeatpercent_5, 1, 1, 1, 1)

        self.spacerItem43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout35.addItem(self.spacerItem43, 3, 0, 1, 2)


        self.gridLayout34.addWidget(self.diet_comp_box_5, 0, 0, 1, 1)

        self.line_3 = QFrame(self.gbDietComaprison_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout34.addWidget(self.line_3, 0, 1, 1, 1)

        self.diet_comp_box_6 = QGroupBox(self.gbDietComaprison_3)
        self.diet_comp_box_6.setObjectName(u"diet_comp_box_6")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_6.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_6.setSizePolicy(sizePolicy5)
        self.gridLayout38 = QGridLayout(self.diet_comp_box_6)
        self.gridLayout38.setObjectName(u"gridLayout38")
        self.hboxLayout21 = QHBoxLayout()
        self.hboxLayout21.setObjectName(u"hboxLayout21")
        self.label6_6 = QLabel(self.diet_comp_box_6)
        self.label6_6.setObjectName(u"label6_6")
        self.label6_6.setWordWrap(False)

        self.hboxLayout21.addWidget(self.label6_6)

        self.spinBoxDailyCalories_6 = QSpinBox(self.diet_comp_box_6)
        self.spinBoxDailyCalories_6.setObjectName(u"spinBoxDailyCalories_6")
        self.spinBoxDailyCalories_6.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_6.setMinimum(1)
        self.spinBoxDailyCalories_6.setMaximum(5000)
        self.spinBoxDailyCalories_6.setSingleStep(1)
        self.spinBoxDailyCalories_6.setValue(2500)

        self.hboxLayout21.addWidget(self.spinBoxDailyCalories_6)


        self.gridLayout38.addLayout(self.hboxLayout21, 2, 0, 1, 2)

        self.groupplantpercent_6 = QGroupBox(self.diet_comp_box_6)
        self.groupplantpercent_6.setObjectName(u"groupplantpercent_6")
        self.gridLayout39 = QGridLayout(self.groupplantpercent_6)
        self.gridLayout39.setObjectName(u"gridLayout39")
        self.spacerItem44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout39.addItem(self.spacerItem44, 1, 1, 1, 1)

        self.labelCropTamePercent_6 = QLabel(self.groupplantpercent_6)
        self.labelCropTamePercent_6.setObjectName(u"labelCropTamePercent_6")
        self.labelCropTamePercent_6.setAlignment(Qt.AlignCenter)

        self.gridLayout39.addWidget(self.labelCropTamePercent_6, 1, 2, 1, 1)

        self.sliderCrop_6 = QSlider(self.groupplantpercent_6)
        self.sliderCrop_6.setObjectName(u"sliderCrop_6")
        self.sliderCrop_6.setMaximum(100)
        self.sliderCrop_6.setSingleStep(1)
        self.sliderCrop_6.setPageStep(1)
        self.sliderCrop_6.setValue(90)
        self.sliderCrop_6.setSliderPosition(90)
        self.sliderCrop_6.setOrientation(Qt.Horizontal)
        self.sliderCrop_6.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_6.setTickInterval(25)

        self.gridLayout39.addWidget(self.sliderCrop_6, 2, 0, 1, 3)

        self.labelCropWildPercent_6 = QLabel(self.groupplantpercent_6)
        self.labelCropWildPercent_6.setObjectName(u"labelCropWildPercent_6")
        self.labelCropWildPercent_6.setAlignment(Qt.AlignCenter)

        self.gridLayout39.addWidget(self.labelCropWildPercent_6, 1, 0, 1, 1)

        self.label_29 = QLabel(self.groupplantpercent_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout39.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_30 = QLabel(self.groupplantpercent_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout39.addWidget(self.label_30, 0, 2, 1, 1)

        self.spacerItem45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout39.addItem(self.spacerItem45, 0, 1, 1, 1)


        self.gridLayout38.addWidget(self.groupplantpercent_6, 1, 0, 1, 1)

        self.hboxLayout22 = QHBoxLayout()
        self.hboxLayout22.setObjectName(u"hboxLayout22")
        self.labelCropPercent_6 = QLabel(self.diet_comp_box_6)
        self.labelCropPercent_6.setObjectName(u"labelCropPercent_6")

        self.hboxLayout22.addWidget(self.labelCropPercent_6)

        self.sliderDiet_6 = QSlider(self.diet_comp_box_6)
        self.sliderDiet_6.setObjectName(u"sliderDiet_6")
        self.sliderDiet_6.setMaximum(100)
        self.sliderDiet_6.setSingleStep(1)
        self.sliderDiet_6.setPageStep(1)
        self.sliderDiet_6.setValue(50)
        self.sliderDiet_6.setSliderPosition(50)
        self.sliderDiet_6.setOrientation(Qt.Horizontal)
        self.sliderDiet_6.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_6.setTickInterval(25)

        self.hboxLayout22.addWidget(self.sliderDiet_6)

        self.labelMeatPercent_6 = QLabel(self.diet_comp_box_6)
        self.labelMeatPercent_6.setObjectName(u"labelMeatPercent_6")
        self.labelMeatPercent_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout22.addWidget(self.labelMeatPercent_6)


        self.gridLayout38.addLayout(self.hboxLayout22, 0, 0, 1, 2)

        self.groupmeatpercent_6 = QGroupBox(self.diet_comp_box_6)
        self.groupmeatpercent_6.setObjectName(u"groupmeatpercent_6")
        self.groupmeatpercent_6.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout40 = QGridLayout(self.groupmeatpercent_6)
        self.gridLayout40.setObjectName(u"gridLayout40")
        self.label_31 = QLabel(self.groupmeatpercent_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout40.addWidget(self.label_31, 0, 0, 1, 1)

        self.spacerItem46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout40.addItem(self.spacerItem46, 1, 1, 1, 1)

        self.labelMeatWildPercent_6 = QLabel(self.groupmeatpercent_6)
        self.labelMeatWildPercent_6.setObjectName(u"labelMeatWildPercent_6")
        self.labelMeatWildPercent_6.setAlignment(Qt.AlignCenter)

        self.gridLayout40.addWidget(self.labelMeatWildPercent_6, 1, 2, 1, 1)

        self.label_32 = QLabel(self.groupmeatpercent_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout40.addWidget(self.label_32, 0, 2, 1, 1)

        self.labelMeatTamePercent_6 = QLabel(self.groupmeatpercent_6)
        self.labelMeatTamePercent_6.setObjectName(u"labelMeatTamePercent_6")
        self.labelMeatTamePercent_6.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_6.setAlignment(Qt.AlignCenter)

        self.gridLayout40.addWidget(self.labelMeatTamePercent_6, 1, 0, 1, 1)

        self.sliderMeat_6 = QSlider(self.groupmeatpercent_6)
        self.sliderMeat_6.setObjectName(u"sliderMeat_6")
        self.sliderMeat_6.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_6.setMaximum(100)
        self.sliderMeat_6.setSingleStep(1)
        self.sliderMeat_6.setPageStep(1)
        self.sliderMeat_6.setValue(90)
        self.sliderMeat_6.setSliderPosition(90)
        self.sliderMeat_6.setOrientation(Qt.Horizontal)
        self.sliderMeat_6.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_6.setTickInterval(25)

        self.gridLayout40.addWidget(self.sliderMeat_6, 2, 0, 1, 3)

        self.spacerItem47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout40.addItem(self.spacerItem47, 0, 1, 1, 1)


        self.gridLayout38.addWidget(self.groupmeatpercent_6, 1, 1, 1, 1)

        self.spacerItem48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout38.addItem(self.spacerItem48, 3, 0, 1, 2)


        self.gridLayout34.addWidget(self.diet_comp_box_6, 0, 2, 1, 1)


        self.gridLayout33.addWidget(self.gbDietComaprison_3, 2, 0, 1, 8)

        self.gbCropMasks_6 = QGroupBox(self.tabPeriod3)
        self.gbCropMasks_6.setObjectName(u"gbCropMasks_6")
        self.gbCropMasks_6.setCheckable(True)
        self.gridLayout41 = QGridLayout(self.gbCropMasks_6)
        self.gridLayout41.setObjectName(u"gridLayout41")
        self.radioButton_16 = QRadioButton(self.gbCropMasks_6)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout41.addWidget(self.radioButton_16, 0, 0, 1, 2)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.gbCropMasks_6)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout41.addWidget(self.doubleSpinBox_3, 0, 2, 1, 2)

        self.spacerItem49 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout41.addItem(self.spacerItem49, 0, 4, 1, 1)

        self.radioButton_17 = QRadioButton(self.gbCropMasks_6)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout41.addWidget(self.radioButton_17, 1, 0, 1, 1)

        self.comboBox_14 = QComboBox(self.gbCropMasks_6)
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.gridLayout41.addWidget(self.comboBox_14, 1, 1, 1, 4)

        self.radioButton_18 = QRadioButton(self.gbCropMasks_6)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout41.addWidget(self.radioButton_18, 2, 0, 1, 1)

        self.comboBox_15 = QComboBox(self.gbCropMasks_6)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout41.addWidget(self.comboBox_15, 2, 1, 1, 4)

        self.groupBox_11 = QGroupBox(self.gbCropMasks_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setCheckable(True)
        self.groupBox_11.setChecked(False)
        self.gridLayout42 = QGridLayout(self.groupBox_11)
        self.gridLayout42.setObjectName(u"gridLayout42")
        self.checkBox_33 = QCheckBox(self.groupBox_11)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.gridLayout42.addWidget(self.checkBox_33, 0, 0, 1, 1)

        self.checkBox_34 = QCheckBox(self.groupBox_11)
        self.checkBox_34.setObjectName(u"checkBox_34")

        self.gridLayout42.addWidget(self.checkBox_34, 1, 0, 1, 1)

        self.checkBox_35 = QCheckBox(self.groupBox_11)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.gridLayout42.addWidget(self.checkBox_35, 2, 0, 1, 1)


        self.gridLayout41.addWidget(self.groupBox_11, 3, 0, 1, 3)

        self.groupBox_12 = QGroupBox(self.gbCropMasks_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setCheckable(True)
        self.groupBox_12.setChecked(False)
        self.gridLayout43 = QGridLayout(self.groupBox_12)
        self.gridLayout43.setObjectName(u"gridLayout43")
        self.checkBox_36 = QCheckBox(self.groupBox_12)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.gridLayout43.addWidget(self.checkBox_36, 0, 0, 1, 1)

        self.checkBox_37 = QCheckBox(self.groupBox_12)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.gridLayout43.addWidget(self.checkBox_37, 1, 0, 1, 1)

        self.checkBox_38 = QCheckBox(self.groupBox_12)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.gridLayout43.addWidget(self.checkBox_38, 2, 0, 1, 1)


        self.gridLayout41.addWidget(self.groupBox_12, 3, 3, 1, 2)


        self.gridLayout33.addWidget(self.gbCropMasks_6, 3, 0, 1, 5)

        self.gbCropMasks_5 = QGroupBox(self.tabPeriod3)
        self.gbCropMasks_5.setObjectName(u"gbCropMasks_5")
        self.gbCropMasks_5.setCheckable(True)
        self.gridLayout44 = QGridLayout(self.gbCropMasks_5)
        self.gridLayout44.setObjectName(u"gridLayout44")
        self.radioButton_13 = QRadioButton(self.gbCropMasks_5)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout44.addWidget(self.radioButton_13, 0, 0, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.gbCropMasks_5)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout44.addWidget(self.doubleSpinBox_8, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gbCropMasks_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout44.addWidget(self.label_8, 0, 2, 1, 2)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.gbCropMasks_5)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout44.addWidget(self.doubleSpinBox_9, 0, 4, 1, 1)

        self.spacerItem50 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout44.addItem(self.spacerItem50, 0, 5, 1, 1)

        self.radioButton_14 = QRadioButton(self.gbCropMasks_5)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout44.addWidget(self.radioButton_14, 1, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.gbCropMasks_5)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout44.addWidget(self.comboBox_11, 1, 1, 1, 5)

        self.radioButton_15 = QRadioButton(self.gbCropMasks_5)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout44.addWidget(self.radioButton_15, 2, 0, 1, 1)

        self.comboBox_12 = QComboBox(self.gbCropMasks_5)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout44.addWidget(self.comboBox_12, 2, 1, 1, 5)

        self.groupBox_9 = QGroupBox(self.gbCropMasks_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setCheckable(True)
        self.groupBox_9.setChecked(False)
        self.gridLayout45 = QGridLayout(self.groupBox_9)
        self.gridLayout45.setObjectName(u"gridLayout45")
        self.checkBox_27 = QCheckBox(self.groupBox_9)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.gridLayout45.addWidget(self.checkBox_27, 0, 0, 1, 1)

        self.checkBox_28 = QCheckBox(self.groupBox_9)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.gridLayout45.addWidget(self.checkBox_28, 1, 0, 1, 1)

        self.checkBox_29 = QCheckBox(self.groupBox_9)
        self.checkBox_29.setObjectName(u"checkBox_29")

        self.gridLayout45.addWidget(self.checkBox_29, 2, 0, 1, 1)


        self.gridLayout44.addWidget(self.groupBox_9, 3, 0, 1, 3)

        self.groupBox_10 = QGroupBox(self.gbCropMasks_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setCheckable(True)
        self.groupBox_10.setChecked(False)
        self.gridLayout46 = QGridLayout(self.groupBox_10)
        self.gridLayout46.setObjectName(u"gridLayout46")
        self.checkBox_30 = QCheckBox(self.groupBox_10)
        self.checkBox_30.setObjectName(u"checkBox_30")

        self.gridLayout46.addWidget(self.checkBox_30, 0, 0, 1, 1)

        self.checkBox_31 = QCheckBox(self.groupBox_10)
        self.checkBox_31.setObjectName(u"checkBox_31")

        self.gridLayout46.addWidget(self.checkBox_31, 1, 0, 1, 1)

        self.checkBox_32 = QCheckBox(self.groupBox_10)
        self.checkBox_32.setObjectName(u"checkBox_32")

        self.gridLayout46.addWidget(self.checkBox_32, 2, 0, 1, 1)


        self.gridLayout44.addWidget(self.groupBox_10, 3, 3, 1, 3)


        self.gridLayout33.addWidget(self.gbCropMasks_5, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod3, "")
        self.tabPeriod4 = QWidget()
        self.tabPeriod4.setObjectName(u"tabPeriod4")
        self.gridLayout47 = QGridLayout(self.tabPeriod4)
        self.gridLayout47.setObjectName(u"gridLayout47")
        self.comboBox_18 = QComboBox(self.tabPeriod4)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout47.addWidget(self.comboBox_18, 0, 0, 1, 2)

        self.label_44 = QLabel(self.tabPeriod4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout47.addWidget(self.label_44, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tabPeriod4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout47.addWidget(self.lineEdit_4, 0, 3, 1, 3)

        self.line_10 = QFrame(self.tabPeriod4)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout47.addWidget(self.line_10, 0, 6, 2, 1)

        self.hboxLayout23 = QHBoxLayout()
        self.hboxLayout23.setObjectName(u"hboxLayout23")
        self.spacerItem51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout23.addItem(self.spacerItem51)

        self.pushButton_7 = QPushButton(self.tabPeriod4)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.hboxLayout23.addWidget(self.pushButton_7)

        self.spacerItem52 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout23.addItem(self.spacerItem52)


        self.gridLayout47.addLayout(self.hboxLayout23, 0, 7, 1, 1)

        self.label_34 = QLabel(self.tabPeriod4)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout47.addWidget(self.label_34, 1, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.tabPeriod4)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(20000)
        self.spinBox_9.setValue(500)

        self.gridLayout47.addWidget(self.spinBox_9, 1, 1, 1, 3)

        self.spinBox_10 = QSpinBox(self.tabPeriod4)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(20000)
        self.spinBox_10.setValue(1000)

        self.gridLayout47.addWidget(self.spinBox_10, 1, 4, 1, 2)

        self.hboxLayout24 = QHBoxLayout()
        self.hboxLayout24.setObjectName(u"hboxLayout24")
        self.spacerItem53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout24.addItem(self.spacerItem53)

        self.pushButton_8 = QPushButton(self.tabPeriod4)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.hboxLayout24.addWidget(self.pushButton_8)

        self.spacerItem54 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout24.addItem(self.spacerItem54)


        self.gridLayout47.addLayout(self.hboxLayout24, 1, 7, 1, 1)

        self.gbDietComaprison_4 = QGroupBox(self.tabPeriod4)
        self.gbDietComaprison_4.setObjectName(u"gbDietComaprison_4")
        self.gbDietComaprison_4.setCheckable(True)
        self.gridLayout48 = QGridLayout(self.gbDietComaprison_4)
        self.gridLayout48.setObjectName(u"gridLayout48")
        self.diet_comp_box_7 = QGroupBox(self.gbDietComaprison_4)
        self.diet_comp_box_7.setObjectName(u"diet_comp_box_7")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_7.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_7.setSizePolicy(sizePolicy5)
        self.gridLayout49 = QGridLayout(self.diet_comp_box_7)
        self.gridLayout49.setObjectName(u"gridLayout49")
        self.hboxLayout25 = QHBoxLayout()
        self.hboxLayout25.setObjectName(u"hboxLayout25")
        self.label6_7 = QLabel(self.diet_comp_box_7)
        self.label6_7.setObjectName(u"label6_7")
        self.label6_7.setWordWrap(False)

        self.hboxLayout25.addWidget(self.label6_7)

        self.spinBoxDailyCalories_7 = QSpinBox(self.diet_comp_box_7)
        self.spinBoxDailyCalories_7.setObjectName(u"spinBoxDailyCalories_7")
        self.spinBoxDailyCalories_7.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_7.setMinimum(1)
        self.spinBoxDailyCalories_7.setMaximum(5000)
        self.spinBoxDailyCalories_7.setSingleStep(1)
        self.spinBoxDailyCalories_7.setValue(2500)

        self.hboxLayout25.addWidget(self.spinBoxDailyCalories_7)


        self.gridLayout49.addLayout(self.hboxLayout25, 2, 0, 1, 2)

        self.groupplantpercent_7 = QGroupBox(self.diet_comp_box_7)
        self.groupplantpercent_7.setObjectName(u"groupplantpercent_7")
        self.gridLayout50 = QGridLayout(self.groupplantpercent_7)
        self.gridLayout50.setObjectName(u"gridLayout50")
        self.spacerItem55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout50.addItem(self.spacerItem55, 1, 1, 1, 1)

        self.labelCropTamePercent_7 = QLabel(self.groupplantpercent_7)
        self.labelCropTamePercent_7.setObjectName(u"labelCropTamePercent_7")
        self.labelCropTamePercent_7.setAlignment(Qt.AlignCenter)

        self.gridLayout50.addWidget(self.labelCropTamePercent_7, 1, 2, 1, 1)

        self.sliderCrop_7 = QSlider(self.groupplantpercent_7)
        self.sliderCrop_7.setObjectName(u"sliderCrop_7")
        self.sliderCrop_7.setMaximum(100)
        self.sliderCrop_7.setSingleStep(1)
        self.sliderCrop_7.setPageStep(1)
        self.sliderCrop_7.setValue(90)
        self.sliderCrop_7.setSliderPosition(90)
        self.sliderCrop_7.setOrientation(Qt.Horizontal)
        self.sliderCrop_7.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_7.setTickInterval(25)

        self.gridLayout50.addWidget(self.sliderCrop_7, 2, 0, 1, 3)

        self.labelCropWildPercent_7 = QLabel(self.groupplantpercent_7)
        self.labelCropWildPercent_7.setObjectName(u"labelCropWildPercent_7")
        self.labelCropWildPercent_7.setAlignment(Qt.AlignCenter)

        self.gridLayout50.addWidget(self.labelCropWildPercent_7, 1, 0, 1, 1)

        self.label_35 = QLabel(self.groupplantpercent_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout50.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_36 = QLabel(self.groupplantpercent_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout50.addWidget(self.label_36, 0, 2, 1, 1)

        self.spacerItem56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout50.addItem(self.spacerItem56, 0, 1, 1, 1)


        self.gridLayout49.addWidget(self.groupplantpercent_7, 1, 0, 1, 1)

        self.hboxLayout26 = QHBoxLayout()
        self.hboxLayout26.setObjectName(u"hboxLayout26")
        self.labelCropPercent_7 = QLabel(self.diet_comp_box_7)
        self.labelCropPercent_7.setObjectName(u"labelCropPercent_7")

        self.hboxLayout26.addWidget(self.labelCropPercent_7)

        self.sliderDiet_7 = QSlider(self.diet_comp_box_7)
        self.sliderDiet_7.setObjectName(u"sliderDiet_7")
        self.sliderDiet_7.setMaximum(100)
        self.sliderDiet_7.setSingleStep(1)
        self.sliderDiet_7.setPageStep(1)
        self.sliderDiet_7.setValue(50)
        self.sliderDiet_7.setSliderPosition(50)
        self.sliderDiet_7.setOrientation(Qt.Horizontal)
        self.sliderDiet_7.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_7.setTickInterval(25)

        self.hboxLayout26.addWidget(self.sliderDiet_7)

        self.labelMeatPercent_7 = QLabel(self.diet_comp_box_7)
        self.labelMeatPercent_7.setObjectName(u"labelMeatPercent_7")
        self.labelMeatPercent_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout26.addWidget(self.labelMeatPercent_7)


        self.gridLayout49.addLayout(self.hboxLayout26, 0, 0, 1, 2)

        self.groupmeatpercent_7 = QGroupBox(self.diet_comp_box_7)
        self.groupmeatpercent_7.setObjectName(u"groupmeatpercent_7")
        self.groupmeatpercent_7.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout51 = QGridLayout(self.groupmeatpercent_7)
        self.gridLayout51.setObjectName(u"gridLayout51")
        self.label_37 = QLabel(self.groupmeatpercent_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout51.addWidget(self.label_37, 0, 0, 1, 1)

        self.spacerItem57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout51.addItem(self.spacerItem57, 1, 1, 1, 1)

        self.labelMeatWildPercent_7 = QLabel(self.groupmeatpercent_7)
        self.labelMeatWildPercent_7.setObjectName(u"labelMeatWildPercent_7")
        self.labelMeatWildPercent_7.setAlignment(Qt.AlignCenter)

        self.gridLayout51.addWidget(self.labelMeatWildPercent_7, 1, 2, 1, 1)

        self.label_38 = QLabel(self.groupmeatpercent_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout51.addWidget(self.label_38, 0, 2, 1, 1)

        self.labelMeatTamePercent_7 = QLabel(self.groupmeatpercent_7)
        self.labelMeatTamePercent_7.setObjectName(u"labelMeatTamePercent_7")
        self.labelMeatTamePercent_7.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_7.setAlignment(Qt.AlignCenter)

        self.gridLayout51.addWidget(self.labelMeatTamePercent_7, 1, 0, 1, 1)

        self.sliderMeat_7 = QSlider(self.groupmeatpercent_7)
        self.sliderMeat_7.setObjectName(u"sliderMeat_7")
        self.sliderMeat_7.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_7.setMaximum(100)
        self.sliderMeat_7.setSingleStep(1)
        self.sliderMeat_7.setPageStep(1)
        self.sliderMeat_7.setValue(90)
        self.sliderMeat_7.setSliderPosition(90)
        self.sliderMeat_7.setOrientation(Qt.Horizontal)
        self.sliderMeat_7.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_7.setTickInterval(25)

        self.gridLayout51.addWidget(self.sliderMeat_7, 2, 0, 1, 3)

        self.spacerItem58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout51.addItem(self.spacerItem58, 0, 1, 1, 1)


        self.gridLayout49.addWidget(self.groupmeatpercent_7, 1, 1, 1, 1)

        self.spacerItem59 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout49.addItem(self.spacerItem59, 3, 0, 1, 2)


        self.gridLayout48.addWidget(self.diet_comp_box_7, 0, 0, 1, 1)

        self.line_4 = QFrame(self.gbDietComaprison_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout48.addWidget(self.line_4, 0, 1, 1, 1)

        self.diet_comp_box_8 = QGroupBox(self.gbDietComaprison_4)
        self.diet_comp_box_8.setObjectName(u"diet_comp_box_8")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_8.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_8.setSizePolicy(sizePolicy5)
        self.gridLayout52 = QGridLayout(self.diet_comp_box_8)
        self.gridLayout52.setObjectName(u"gridLayout52")
        self.hboxLayout27 = QHBoxLayout()
        self.hboxLayout27.setObjectName(u"hboxLayout27")
        self.label6_8 = QLabel(self.diet_comp_box_8)
        self.label6_8.setObjectName(u"label6_8")
        self.label6_8.setWordWrap(False)

        self.hboxLayout27.addWidget(self.label6_8)

        self.spinBoxDailyCalories_8 = QSpinBox(self.diet_comp_box_8)
        self.spinBoxDailyCalories_8.setObjectName(u"spinBoxDailyCalories_8")
        self.spinBoxDailyCalories_8.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_8.setMinimum(1)
        self.spinBoxDailyCalories_8.setMaximum(5000)
        self.spinBoxDailyCalories_8.setSingleStep(1)
        self.spinBoxDailyCalories_8.setValue(2500)

        self.hboxLayout27.addWidget(self.spinBoxDailyCalories_8)


        self.gridLayout52.addLayout(self.hboxLayout27, 2, 0, 1, 2)

        self.groupplantpercent_8 = QGroupBox(self.diet_comp_box_8)
        self.groupplantpercent_8.setObjectName(u"groupplantpercent_8")
        self.gridLayout53 = QGridLayout(self.groupplantpercent_8)
        self.gridLayout53.setObjectName(u"gridLayout53")
        self.spacerItem60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout53.addItem(self.spacerItem60, 1, 1, 1, 1)

        self.labelCropTamePercent_8 = QLabel(self.groupplantpercent_8)
        self.labelCropTamePercent_8.setObjectName(u"labelCropTamePercent_8")
        self.labelCropTamePercent_8.setAlignment(Qt.AlignCenter)

        self.gridLayout53.addWidget(self.labelCropTamePercent_8, 1, 2, 1, 1)

        self.sliderCrop_8 = QSlider(self.groupplantpercent_8)
        self.sliderCrop_8.setObjectName(u"sliderCrop_8")
        self.sliderCrop_8.setMaximum(100)
        self.sliderCrop_8.setSingleStep(1)
        self.sliderCrop_8.setPageStep(1)
        self.sliderCrop_8.setValue(90)
        self.sliderCrop_8.setSliderPosition(90)
        self.sliderCrop_8.setOrientation(Qt.Horizontal)
        self.sliderCrop_8.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_8.setTickInterval(25)

        self.gridLayout53.addWidget(self.sliderCrop_8, 2, 0, 1, 3)

        self.labelCropWildPercent_8 = QLabel(self.groupplantpercent_8)
        self.labelCropWildPercent_8.setObjectName(u"labelCropWildPercent_8")
        self.labelCropWildPercent_8.setAlignment(Qt.AlignCenter)

        self.gridLayout53.addWidget(self.labelCropWildPercent_8, 1, 0, 1, 1)

        self.label_39 = QLabel(self.groupplantpercent_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout53.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_40 = QLabel(self.groupplantpercent_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout53.addWidget(self.label_40, 0, 2, 1, 1)

        self.spacerItem61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout53.addItem(self.spacerItem61, 0, 1, 1, 1)


        self.gridLayout52.addWidget(self.groupplantpercent_8, 1, 0, 1, 1)

        self.hboxLayout28 = QHBoxLayout()
        self.hboxLayout28.setObjectName(u"hboxLayout28")
        self.labelCropPercent_8 = QLabel(self.diet_comp_box_8)
        self.labelCropPercent_8.setObjectName(u"labelCropPercent_8")

        self.hboxLayout28.addWidget(self.labelCropPercent_8)

        self.sliderDiet_8 = QSlider(self.diet_comp_box_8)
        self.sliderDiet_8.setObjectName(u"sliderDiet_8")
        self.sliderDiet_8.setMaximum(100)
        self.sliderDiet_8.setSingleStep(1)
        self.sliderDiet_8.setPageStep(1)
        self.sliderDiet_8.setValue(50)
        self.sliderDiet_8.setSliderPosition(50)
        self.sliderDiet_8.setOrientation(Qt.Horizontal)
        self.sliderDiet_8.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_8.setTickInterval(25)

        self.hboxLayout28.addWidget(self.sliderDiet_8)

        self.labelMeatPercent_8 = QLabel(self.diet_comp_box_8)
        self.labelMeatPercent_8.setObjectName(u"labelMeatPercent_8")
        self.labelMeatPercent_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout28.addWidget(self.labelMeatPercent_8)


        self.gridLayout52.addLayout(self.hboxLayout28, 0, 0, 1, 2)

        self.groupmeatpercent_8 = QGroupBox(self.diet_comp_box_8)
        self.groupmeatpercent_8.setObjectName(u"groupmeatpercent_8")
        self.groupmeatpercent_8.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout54 = QGridLayout(self.groupmeatpercent_8)
        self.gridLayout54.setObjectName(u"gridLayout54")
        self.label_41 = QLabel(self.groupmeatpercent_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout54.addWidget(self.label_41, 0, 0, 1, 1)

        self.spacerItem62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout54.addItem(self.spacerItem62, 1, 1, 1, 1)

        self.labelMeatWildPercent_8 = QLabel(self.groupmeatpercent_8)
        self.labelMeatWildPercent_8.setObjectName(u"labelMeatWildPercent_8")
        self.labelMeatWildPercent_8.setAlignment(Qt.AlignCenter)

        self.gridLayout54.addWidget(self.labelMeatWildPercent_8, 1, 2, 1, 1)

        self.label_42 = QLabel(self.groupmeatpercent_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout54.addWidget(self.label_42, 0, 2, 1, 1)

        self.labelMeatTamePercent_8 = QLabel(self.groupmeatpercent_8)
        self.labelMeatTamePercent_8.setObjectName(u"labelMeatTamePercent_8")
        self.labelMeatTamePercent_8.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_8.setAlignment(Qt.AlignCenter)

        self.gridLayout54.addWidget(self.labelMeatTamePercent_8, 1, 0, 1, 1)

        self.sliderMeat_8 = QSlider(self.groupmeatpercent_8)
        self.sliderMeat_8.setObjectName(u"sliderMeat_8")
        self.sliderMeat_8.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_8.setMaximum(100)
        self.sliderMeat_8.setSingleStep(1)
        self.sliderMeat_8.setPageStep(1)
        self.sliderMeat_8.setValue(90)
        self.sliderMeat_8.setSliderPosition(90)
        self.sliderMeat_8.setOrientation(Qt.Horizontal)
        self.sliderMeat_8.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_8.setTickInterval(25)

        self.gridLayout54.addWidget(self.sliderMeat_8, 2, 0, 1, 3)

        self.spacerItem63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout54.addItem(self.spacerItem63, 0, 1, 1, 1)


        self.gridLayout52.addWidget(self.groupmeatpercent_8, 1, 1, 1, 1)

        self.spacerItem64 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout52.addItem(self.spacerItem64, 3, 0, 1, 2)


        self.gridLayout48.addWidget(self.diet_comp_box_8, 0, 2, 1, 1)


        self.gridLayout47.addWidget(self.gbDietComaprison_4, 2, 0, 1, 8)

        self.gbCropMasks_7 = QGroupBox(self.tabPeriod4)
        self.gbCropMasks_7.setObjectName(u"gbCropMasks_7")
        self.gbCropMasks_7.setCheckable(True)
        self.gridLayout55 = QGridLayout(self.gbCropMasks_7)
        self.gridLayout55.setObjectName(u"gridLayout55")
        self.radioButton_19 = QRadioButton(self.gbCropMasks_7)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.gridLayout55.addWidget(self.radioButton_19, 0, 0, 1, 2)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.gbCropMasks_7)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")

        self.gridLayout55.addWidget(self.doubleSpinBox_10, 0, 2, 1, 2)

        self.spacerItem65 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout55.addItem(self.spacerItem65, 0, 4, 1, 1)

        self.radioButton_20 = QRadioButton(self.gbCropMasks_7)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.gridLayout55.addWidget(self.radioButton_20, 1, 0, 1, 1)

        self.comboBox_16 = QComboBox(self.gbCropMasks_7)
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.gridLayout55.addWidget(self.comboBox_16, 1, 1, 1, 4)

        self.radioButton_21 = QRadioButton(self.gbCropMasks_7)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.gridLayout55.addWidget(self.radioButton_21, 2, 0, 1, 1)

        self.comboBox_17 = QComboBox(self.gbCropMasks_7)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout55.addWidget(self.comboBox_17, 2, 1, 1, 4)

        self.groupBox_13 = QGroupBox(self.gbCropMasks_7)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setCheckable(True)
        self.groupBox_13.setChecked(False)
        self.gridLayout56 = QGridLayout(self.groupBox_13)
        self.gridLayout56.setObjectName(u"gridLayout56")
        self.checkBox_39 = QCheckBox(self.groupBox_13)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.gridLayout56.addWidget(self.checkBox_39, 0, 0, 1, 1)

        self.checkBox_40 = QCheckBox(self.groupBox_13)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.gridLayout56.addWidget(self.checkBox_40, 1, 0, 1, 1)

        self.checkBox_41 = QCheckBox(self.groupBox_13)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.gridLayout56.addWidget(self.checkBox_41, 2, 0, 1, 1)


        self.gridLayout55.addWidget(self.groupBox_13, 3, 0, 1, 3)

        self.groupBox_14 = QGroupBox(self.gbCropMasks_7)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setCheckable(True)
        self.groupBox_14.setChecked(False)
        self.gridLayout57 = QGridLayout(self.groupBox_14)
        self.gridLayout57.setObjectName(u"gridLayout57")
        self.checkBox_42 = QCheckBox(self.groupBox_14)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.gridLayout57.addWidget(self.checkBox_42, 0, 0, 1, 1)

        self.checkBox_43 = QCheckBox(self.groupBox_14)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.gridLayout57.addWidget(self.checkBox_43, 1, 0, 1, 1)

        self.checkBox_44 = QCheckBox(self.groupBox_14)
        self.checkBox_44.setObjectName(u"checkBox_44")

        self.gridLayout57.addWidget(self.checkBox_44, 2, 0, 1, 1)


        self.gridLayout55.addWidget(self.groupBox_14, 3, 3, 1, 2)


        self.gridLayout47.addWidget(self.gbCropMasks_7, 3, 0, 1, 5)

        self.gbCropMasks_8 = QGroupBox(self.tabPeriod4)
        self.gbCropMasks_8.setObjectName(u"gbCropMasks_8")
        self.gbCropMasks_8.setCheckable(True)
        self.gridLayout58 = QGridLayout(self.gbCropMasks_8)
        self.gridLayout58.setObjectName(u"gridLayout58")
        self.radioButton_22 = QRadioButton(self.gbCropMasks_8)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.gridLayout58.addWidget(self.radioButton_22, 0, 0, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.gbCropMasks_8)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")

        self.gridLayout58.addWidget(self.doubleSpinBox_11, 0, 1, 1, 1)

        self.label_43 = QLabel(self.gbCropMasks_8)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout58.addWidget(self.label_43, 0, 2, 1, 2)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.gbCropMasks_8)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")

        self.gridLayout58.addWidget(self.doubleSpinBox_12, 0, 4, 1, 1)

        self.spacerItem66 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout58.addItem(self.spacerItem66, 0, 5, 1, 1)

        self.radioButton_23 = QRadioButton(self.gbCropMasks_8)
        self.radioButton_23.setObjectName(u"radioButton_23")

        self.gridLayout58.addWidget(self.radioButton_23, 1, 0, 1, 1)

        self.comboBox_19 = QComboBox(self.gbCropMasks_8)
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.gridLayout58.addWidget(self.comboBox_19, 1, 1, 1, 5)

        self.radioButton_24 = QRadioButton(self.gbCropMasks_8)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.gridLayout58.addWidget(self.radioButton_24, 2, 0, 1, 1)

        self.comboBox_20 = QComboBox(self.gbCropMasks_8)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout58.addWidget(self.comboBox_20, 2, 1, 1, 5)

        self.groupBox_15 = QGroupBox(self.gbCropMasks_8)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setCheckable(True)
        self.groupBox_15.setChecked(False)
        self.gridLayout59 = QGridLayout(self.groupBox_15)
        self.gridLayout59.setObjectName(u"gridLayout59")
        self.checkBox_45 = QCheckBox(self.groupBox_15)
        self.checkBox_45.setObjectName(u"checkBox_45")

        self.gridLayout59.addWidget(self.checkBox_45, 0, 0, 1, 1)

        self.checkBox_46 = QCheckBox(self.groupBox_15)
        self.checkBox_46.setObjectName(u"checkBox_46")

        self.gridLayout59.addWidget(self.checkBox_46, 1, 0, 1, 1)

        self.checkBox_47 = QCheckBox(self.groupBox_15)
        self.checkBox_47.setObjectName(u"checkBox_47")

        self.gridLayout59.addWidget(self.checkBox_47, 2, 0, 1, 1)


        self.gridLayout58.addWidget(self.groupBox_15, 3, 0, 1, 3)

        self.groupBox_16 = QGroupBox(self.gbCropMasks_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setCheckable(True)
        self.groupBox_16.setChecked(False)
        self.gridLayout60 = QGridLayout(self.groupBox_16)
        self.gridLayout60.setObjectName(u"gridLayout60")
        self.checkBox_48 = QCheckBox(self.groupBox_16)
        self.checkBox_48.setObjectName(u"checkBox_48")

        self.gridLayout60.addWidget(self.checkBox_48, 0, 0, 1, 1)

        self.checkBox_49 = QCheckBox(self.groupBox_16)
        self.checkBox_49.setObjectName(u"checkBox_49")

        self.gridLayout60.addWidget(self.checkBox_49, 1, 0, 1, 1)

        self.checkBox_50 = QCheckBox(self.groupBox_16)
        self.checkBox_50.setObjectName(u"checkBox_50")

        self.gridLayout60.addWidget(self.checkBox_50, 2, 0, 1, 1)


        self.gridLayout58.addWidget(self.groupBox_16, 3, 3, 1, 3)


        self.gridLayout47.addWidget(self.gbCropMasks_8, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod4, "")
        self.tabPeriod5 = QWidget()
        self.tabPeriod5.setObjectName(u"tabPeriod5")
        self.gridLayout61 = QGridLayout(self.tabPeriod5)
        self.gridLayout61.setObjectName(u"gridLayout61")
        self.comboBox_25 = QComboBox(self.tabPeriod5)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")

        self.gridLayout61.addWidget(self.comboBox_25, 0, 0, 1, 2)

        self.label_55 = QLabel(self.tabPeriod5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout61.addWidget(self.label_55, 0, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.tabPeriod5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout61.addWidget(self.lineEdit_5, 0, 3, 1, 3)

        self.line_11 = QFrame(self.tabPeriod5)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout61.addWidget(self.line_11, 0, 6, 2, 1)

        self.hboxLayout29 = QHBoxLayout()
        self.hboxLayout29.setObjectName(u"hboxLayout29")
        self.spacerItem67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout29.addItem(self.spacerItem67)

        self.pushButton_9 = QPushButton(self.tabPeriod5)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.hboxLayout29.addWidget(self.pushButton_9)

        self.spacerItem68 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout29.addItem(self.spacerItem68)


        self.gridLayout61.addLayout(self.hboxLayout29, 0, 7, 1, 1)

        self.label_45 = QLabel(self.tabPeriod5)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout61.addWidget(self.label_45, 1, 0, 1, 1)

        self.spinBox_12 = QSpinBox(self.tabPeriod5)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setMaximum(20000)
        self.spinBox_12.setValue(500)

        self.gridLayout61.addWidget(self.spinBox_12, 1, 1, 1, 3)

        self.spinBox_11 = QSpinBox(self.tabPeriod5)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(20000)
        self.spinBox_11.setValue(1000)

        self.gridLayout61.addWidget(self.spinBox_11, 1, 4, 1, 2)

        self.hboxLayout30 = QHBoxLayout()
        self.hboxLayout30.setObjectName(u"hboxLayout30")
        self.spacerItem69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout30.addItem(self.spacerItem69)

        self.pushButton_10 = QPushButton(self.tabPeriod5)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.hboxLayout30.addWidget(self.pushButton_10)

        self.spacerItem70 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout30.addItem(self.spacerItem70)


        self.gridLayout61.addLayout(self.hboxLayout30, 1, 7, 1, 1)

        self.gbDietComaprison_5 = QGroupBox(self.tabPeriod5)
        self.gbDietComaprison_5.setObjectName(u"gbDietComaprison_5")
        self.gbDietComaprison_5.setCheckable(True)
        self.gridLayout62 = QGridLayout(self.gbDietComaprison_5)
        self.gridLayout62.setObjectName(u"gridLayout62")
        self.diet_comp_box_9 = QGroupBox(self.gbDietComaprison_5)
        self.diet_comp_box_9.setObjectName(u"diet_comp_box_9")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_9.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_9.setSizePolicy(sizePolicy5)
        self.gridLayout63 = QGridLayout(self.diet_comp_box_9)
        self.gridLayout63.setObjectName(u"gridLayout63")
        self.hboxLayout31 = QHBoxLayout()
        self.hboxLayout31.setObjectName(u"hboxLayout31")
        self.label6_9 = QLabel(self.diet_comp_box_9)
        self.label6_9.setObjectName(u"label6_9")
        self.label6_9.setWordWrap(False)

        self.hboxLayout31.addWidget(self.label6_9)

        self.spinBoxDailyCalories_9 = QSpinBox(self.diet_comp_box_9)
        self.spinBoxDailyCalories_9.setObjectName(u"spinBoxDailyCalories_9")
        self.spinBoxDailyCalories_9.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_9.setMinimum(1)
        self.spinBoxDailyCalories_9.setMaximum(5000)
        self.spinBoxDailyCalories_9.setSingleStep(1)
        self.spinBoxDailyCalories_9.setValue(2500)

        self.hboxLayout31.addWidget(self.spinBoxDailyCalories_9)


        self.gridLayout63.addLayout(self.hboxLayout31, 2, 0, 1, 2)

        self.groupplantpercent_9 = QGroupBox(self.diet_comp_box_9)
        self.groupplantpercent_9.setObjectName(u"groupplantpercent_9")
        self.gridLayout64 = QGridLayout(self.groupplantpercent_9)
        self.gridLayout64.setObjectName(u"gridLayout64")
        self.spacerItem71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout64.addItem(self.spacerItem71, 1, 1, 1, 1)

        self.labelCropTamePercent_9 = QLabel(self.groupplantpercent_9)
        self.labelCropTamePercent_9.setObjectName(u"labelCropTamePercent_9")
        self.labelCropTamePercent_9.setAlignment(Qt.AlignCenter)

        self.gridLayout64.addWidget(self.labelCropTamePercent_9, 1, 2, 1, 1)

        self.sliderCrop_9 = QSlider(self.groupplantpercent_9)
        self.sliderCrop_9.setObjectName(u"sliderCrop_9")
        self.sliderCrop_9.setMaximum(100)
        self.sliderCrop_9.setSingleStep(1)
        self.sliderCrop_9.setPageStep(1)
        self.sliderCrop_9.setValue(90)
        self.sliderCrop_9.setSliderPosition(90)
        self.sliderCrop_9.setOrientation(Qt.Horizontal)
        self.sliderCrop_9.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_9.setTickInterval(25)

        self.gridLayout64.addWidget(self.sliderCrop_9, 2, 0, 1, 3)

        self.labelCropWildPercent_9 = QLabel(self.groupplantpercent_9)
        self.labelCropWildPercent_9.setObjectName(u"labelCropWildPercent_9")
        self.labelCropWildPercent_9.setAlignment(Qt.AlignCenter)

        self.gridLayout64.addWidget(self.labelCropWildPercent_9, 1, 0, 1, 1)

        self.label_46 = QLabel(self.groupplantpercent_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout64.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_47 = QLabel(self.groupplantpercent_9)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout64.addWidget(self.label_47, 0, 2, 1, 1)

        self.spacerItem72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout64.addItem(self.spacerItem72, 0, 1, 1, 1)


        self.gridLayout63.addWidget(self.groupplantpercent_9, 1, 0, 1, 1)

        self.hboxLayout32 = QHBoxLayout()
        self.hboxLayout32.setObjectName(u"hboxLayout32")
        self.labelCropPercent_9 = QLabel(self.diet_comp_box_9)
        self.labelCropPercent_9.setObjectName(u"labelCropPercent_9")

        self.hboxLayout32.addWidget(self.labelCropPercent_9)

        self.sliderDiet_9 = QSlider(self.diet_comp_box_9)
        self.sliderDiet_9.setObjectName(u"sliderDiet_9")
        self.sliderDiet_9.setMaximum(100)
        self.sliderDiet_9.setSingleStep(1)
        self.sliderDiet_9.setPageStep(1)
        self.sliderDiet_9.setValue(50)
        self.sliderDiet_9.setSliderPosition(50)
        self.sliderDiet_9.setOrientation(Qt.Horizontal)
        self.sliderDiet_9.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_9.setTickInterval(25)

        self.hboxLayout32.addWidget(self.sliderDiet_9)

        self.labelMeatPercent_9 = QLabel(self.diet_comp_box_9)
        self.labelMeatPercent_9.setObjectName(u"labelMeatPercent_9")
        self.labelMeatPercent_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout32.addWidget(self.labelMeatPercent_9)


        self.gridLayout63.addLayout(self.hboxLayout32, 0, 0, 1, 2)

        self.groupmeatpercent_9 = QGroupBox(self.diet_comp_box_9)
        self.groupmeatpercent_9.setObjectName(u"groupmeatpercent_9")
        self.groupmeatpercent_9.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout65 = QGridLayout(self.groupmeatpercent_9)
        self.gridLayout65.setObjectName(u"gridLayout65")
        self.label_48 = QLabel(self.groupmeatpercent_9)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout65.addWidget(self.label_48, 0, 0, 1, 1)

        self.spacerItem73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout65.addItem(self.spacerItem73, 1, 1, 1, 1)

        self.labelMeatWildPercent_9 = QLabel(self.groupmeatpercent_9)
        self.labelMeatWildPercent_9.setObjectName(u"labelMeatWildPercent_9")
        self.labelMeatWildPercent_9.setAlignment(Qt.AlignCenter)

        self.gridLayout65.addWidget(self.labelMeatWildPercent_9, 1, 2, 1, 1)

        self.label_49 = QLabel(self.groupmeatpercent_9)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout65.addWidget(self.label_49, 0, 2, 1, 1)

        self.labelMeatTamePercent_9 = QLabel(self.groupmeatpercent_9)
        self.labelMeatTamePercent_9.setObjectName(u"labelMeatTamePercent_9")
        self.labelMeatTamePercent_9.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_9.setAlignment(Qt.AlignCenter)

        self.gridLayout65.addWidget(self.labelMeatTamePercent_9, 1, 0, 1, 1)

        self.sliderMeat_9 = QSlider(self.groupmeatpercent_9)
        self.sliderMeat_9.setObjectName(u"sliderMeat_9")
        self.sliderMeat_9.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_9.setMaximum(100)
        self.sliderMeat_9.setSingleStep(1)
        self.sliderMeat_9.setPageStep(1)
        self.sliderMeat_9.setValue(90)
        self.sliderMeat_9.setSliderPosition(90)
        self.sliderMeat_9.setOrientation(Qt.Horizontal)
        self.sliderMeat_9.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_9.setTickInterval(25)

        self.gridLayout65.addWidget(self.sliderMeat_9, 2, 0, 1, 3)

        self.spacerItem74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout65.addItem(self.spacerItem74, 0, 1, 1, 1)


        self.gridLayout63.addWidget(self.groupmeatpercent_9, 1, 1, 1, 1)

        self.spacerItem75 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout63.addItem(self.spacerItem75, 3, 0, 1, 2)


        self.gridLayout62.addWidget(self.diet_comp_box_9, 0, 0, 1, 1)

        self.line_5 = QFrame(self.gbDietComaprison_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout62.addWidget(self.line_5, 0, 1, 1, 1)

        self.diet_comp_box_10 = QGroupBox(self.gbDietComaprison_5)
        self.diet_comp_box_10.setObjectName(u"diet_comp_box_10")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_10.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_10.setSizePolicy(sizePolicy5)
        self.gridLayout66 = QGridLayout(self.diet_comp_box_10)
        self.gridLayout66.setObjectName(u"gridLayout66")
        self.hboxLayout33 = QHBoxLayout()
        self.hboxLayout33.setObjectName(u"hboxLayout33")
        self.label6_10 = QLabel(self.diet_comp_box_10)
        self.label6_10.setObjectName(u"label6_10")
        self.label6_10.setWordWrap(False)

        self.hboxLayout33.addWidget(self.label6_10)

        self.spinBoxDailyCalories_10 = QSpinBox(self.diet_comp_box_10)
        self.spinBoxDailyCalories_10.setObjectName(u"spinBoxDailyCalories_10")
        self.spinBoxDailyCalories_10.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_10.setMinimum(1)
        self.spinBoxDailyCalories_10.setMaximum(5000)
        self.spinBoxDailyCalories_10.setSingleStep(1)
        self.spinBoxDailyCalories_10.setValue(2500)

        self.hboxLayout33.addWidget(self.spinBoxDailyCalories_10)


        self.gridLayout66.addLayout(self.hboxLayout33, 2, 0, 1, 2)

        self.groupplantpercent_10 = QGroupBox(self.diet_comp_box_10)
        self.groupplantpercent_10.setObjectName(u"groupplantpercent_10")
        self.gridLayout67 = QGridLayout(self.groupplantpercent_10)
        self.gridLayout67.setObjectName(u"gridLayout67")
        self.spacerItem76 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout67.addItem(self.spacerItem76, 1, 1, 1, 1)

        self.labelCropTamePercent_10 = QLabel(self.groupplantpercent_10)
        self.labelCropTamePercent_10.setObjectName(u"labelCropTamePercent_10")
        self.labelCropTamePercent_10.setAlignment(Qt.AlignCenter)

        self.gridLayout67.addWidget(self.labelCropTamePercent_10, 1, 2, 1, 1)

        self.sliderCrop_10 = QSlider(self.groupplantpercent_10)
        self.sliderCrop_10.setObjectName(u"sliderCrop_10")
        self.sliderCrop_10.setMaximum(100)
        self.sliderCrop_10.setSingleStep(1)
        self.sliderCrop_10.setPageStep(1)
        self.sliderCrop_10.setValue(90)
        self.sliderCrop_10.setSliderPosition(90)
        self.sliderCrop_10.setOrientation(Qt.Horizontal)
        self.sliderCrop_10.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_10.setTickInterval(25)

        self.gridLayout67.addWidget(self.sliderCrop_10, 2, 0, 1, 3)

        self.labelCropWildPercent_10 = QLabel(self.groupplantpercent_10)
        self.labelCropWildPercent_10.setObjectName(u"labelCropWildPercent_10")
        self.labelCropWildPercent_10.setAlignment(Qt.AlignCenter)

        self.gridLayout67.addWidget(self.labelCropWildPercent_10, 1, 0, 1, 1)

        self.label_50 = QLabel(self.groupplantpercent_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout67.addWidget(self.label_50, 0, 0, 1, 1)

        self.label_51 = QLabel(self.groupplantpercent_10)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout67.addWidget(self.label_51, 0, 2, 1, 1)

        self.spacerItem77 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout67.addItem(self.spacerItem77, 0, 1, 1, 1)


        self.gridLayout66.addWidget(self.groupplantpercent_10, 1, 0, 1, 1)

        self.hboxLayout34 = QHBoxLayout()
        self.hboxLayout34.setObjectName(u"hboxLayout34")
        self.labelCropPercent_10 = QLabel(self.diet_comp_box_10)
        self.labelCropPercent_10.setObjectName(u"labelCropPercent_10")

        self.hboxLayout34.addWidget(self.labelCropPercent_10)

        self.sliderDiet_10 = QSlider(self.diet_comp_box_10)
        self.sliderDiet_10.setObjectName(u"sliderDiet_10")
        self.sliderDiet_10.setMaximum(100)
        self.sliderDiet_10.setSingleStep(1)
        self.sliderDiet_10.setPageStep(1)
        self.sliderDiet_10.setValue(50)
        self.sliderDiet_10.setSliderPosition(50)
        self.sliderDiet_10.setOrientation(Qt.Horizontal)
        self.sliderDiet_10.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_10.setTickInterval(25)

        self.hboxLayout34.addWidget(self.sliderDiet_10)

        self.labelMeatPercent_10 = QLabel(self.diet_comp_box_10)
        self.labelMeatPercent_10.setObjectName(u"labelMeatPercent_10")
        self.labelMeatPercent_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout34.addWidget(self.labelMeatPercent_10)


        self.gridLayout66.addLayout(self.hboxLayout34, 0, 0, 1, 2)

        self.groupmeatpercent_10 = QGroupBox(self.diet_comp_box_10)
        self.groupmeatpercent_10.setObjectName(u"groupmeatpercent_10")
        self.groupmeatpercent_10.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout68 = QGridLayout(self.groupmeatpercent_10)
        self.gridLayout68.setObjectName(u"gridLayout68")
        self.label_52 = QLabel(self.groupmeatpercent_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout68.addWidget(self.label_52, 0, 0, 1, 1)

        self.spacerItem78 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout68.addItem(self.spacerItem78, 1, 1, 1, 1)

        self.labelMeatWildPercent_10 = QLabel(self.groupmeatpercent_10)
        self.labelMeatWildPercent_10.setObjectName(u"labelMeatWildPercent_10")
        self.labelMeatWildPercent_10.setAlignment(Qt.AlignCenter)

        self.gridLayout68.addWidget(self.labelMeatWildPercent_10, 1, 2, 1, 1)

        self.label_53 = QLabel(self.groupmeatpercent_10)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout68.addWidget(self.label_53, 0, 2, 1, 1)

        self.labelMeatTamePercent_10 = QLabel(self.groupmeatpercent_10)
        self.labelMeatTamePercent_10.setObjectName(u"labelMeatTamePercent_10")
        self.labelMeatTamePercent_10.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_10.setAlignment(Qt.AlignCenter)

        self.gridLayout68.addWidget(self.labelMeatTamePercent_10, 1, 0, 1, 1)

        self.sliderMeat_10 = QSlider(self.groupmeatpercent_10)
        self.sliderMeat_10.setObjectName(u"sliderMeat_10")
        self.sliderMeat_10.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_10.setMaximum(100)
        self.sliderMeat_10.setSingleStep(1)
        self.sliderMeat_10.setPageStep(1)
        self.sliderMeat_10.setValue(90)
        self.sliderMeat_10.setSliderPosition(90)
        self.sliderMeat_10.setOrientation(Qt.Horizontal)
        self.sliderMeat_10.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_10.setTickInterval(25)

        self.gridLayout68.addWidget(self.sliderMeat_10, 2, 0, 1, 3)

        self.spacerItem79 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout68.addItem(self.spacerItem79, 0, 1, 1, 1)


        self.gridLayout66.addWidget(self.groupmeatpercent_10, 1, 1, 1, 1)

        self.spacerItem80 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout66.addItem(self.spacerItem80, 3, 0, 1, 2)


        self.gridLayout62.addWidget(self.diet_comp_box_10, 0, 2, 1, 1)


        self.gridLayout61.addWidget(self.gbDietComaprison_5, 2, 0, 1, 8)

        self.gbCropMasks_9 = QGroupBox(self.tabPeriod5)
        self.gbCropMasks_9.setObjectName(u"gbCropMasks_9")
        self.gbCropMasks_9.setCheckable(True)
        self.gridLayout69 = QGridLayout(self.gbCropMasks_9)
        self.gridLayout69.setObjectName(u"gridLayout69")
        self.radioButton_25 = QRadioButton(self.gbCropMasks_9)
        self.radioButton_25.setObjectName(u"radioButton_25")

        self.gridLayout69.addWidget(self.radioButton_25, 0, 0, 1, 2)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.gbCropMasks_9)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")

        self.gridLayout69.addWidget(self.doubleSpinBox_13, 0, 2, 1, 2)

        self.spacerItem81 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout69.addItem(self.spacerItem81, 0, 4, 1, 1)

        self.radioButton_26 = QRadioButton(self.gbCropMasks_9)
        self.radioButton_26.setObjectName(u"radioButton_26")

        self.gridLayout69.addWidget(self.radioButton_26, 1, 0, 1, 1)

        self.comboBox_21 = QComboBox(self.gbCropMasks_9)
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.gridLayout69.addWidget(self.comboBox_21, 1, 1, 1, 4)

        self.radioButton_27 = QRadioButton(self.gbCropMasks_9)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.gridLayout69.addWidget(self.radioButton_27, 2, 0, 1, 1)

        self.comboBox_22 = QComboBox(self.gbCropMasks_9)
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.gridLayout69.addWidget(self.comboBox_22, 2, 1, 1, 4)

        self.groupBox_17 = QGroupBox(self.gbCropMasks_9)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setCheckable(True)
        self.groupBox_17.setChecked(False)
        self.gridLayout70 = QGridLayout(self.groupBox_17)
        self.gridLayout70.setObjectName(u"gridLayout70")
        self.checkBox_51 = QCheckBox(self.groupBox_17)
        self.checkBox_51.setObjectName(u"checkBox_51")

        self.gridLayout70.addWidget(self.checkBox_51, 0, 0, 1, 1)

        self.checkBox_52 = QCheckBox(self.groupBox_17)
        self.checkBox_52.setObjectName(u"checkBox_52")

        self.gridLayout70.addWidget(self.checkBox_52, 1, 0, 1, 1)

        self.checkBox_53 = QCheckBox(self.groupBox_17)
        self.checkBox_53.setObjectName(u"checkBox_53")

        self.gridLayout70.addWidget(self.checkBox_53, 2, 0, 1, 1)


        self.gridLayout69.addWidget(self.groupBox_17, 3, 0, 1, 3)

        self.groupBox_18 = QGroupBox(self.gbCropMasks_9)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setCheckable(True)
        self.groupBox_18.setChecked(False)
        self.gridLayout71 = QGridLayout(self.groupBox_18)
        self.gridLayout71.setObjectName(u"gridLayout71")
        self.checkBox_54 = QCheckBox(self.groupBox_18)
        self.checkBox_54.setObjectName(u"checkBox_54")

        self.gridLayout71.addWidget(self.checkBox_54, 0, 0, 1, 1)

        self.checkBox_55 = QCheckBox(self.groupBox_18)
        self.checkBox_55.setObjectName(u"checkBox_55")

        self.gridLayout71.addWidget(self.checkBox_55, 1, 0, 1, 1)

        self.checkBox_56 = QCheckBox(self.groupBox_18)
        self.checkBox_56.setObjectName(u"checkBox_56")

        self.gridLayout71.addWidget(self.checkBox_56, 2, 0, 1, 1)


        self.gridLayout69.addWidget(self.groupBox_18, 3, 3, 1, 2)


        self.gridLayout61.addWidget(self.gbCropMasks_9, 3, 0, 1, 5)

        self.gbCropMasks_10 = QGroupBox(self.tabPeriod5)
        self.gbCropMasks_10.setObjectName(u"gbCropMasks_10")
        self.gbCropMasks_10.setCheckable(True)
        self.gridLayout72 = QGridLayout(self.gbCropMasks_10)
        self.gridLayout72.setObjectName(u"gridLayout72")
        self.radioButton_28 = QRadioButton(self.gbCropMasks_10)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.gridLayout72.addWidget(self.radioButton_28, 0, 0, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.gbCropMasks_10)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.gridLayout72.addWidget(self.doubleSpinBox_14, 0, 1, 1, 1)

        self.label_54 = QLabel(self.gbCropMasks_10)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout72.addWidget(self.label_54, 0, 2, 1, 2)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.gbCropMasks_10)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.gridLayout72.addWidget(self.doubleSpinBox_15, 0, 4, 1, 1)

        self.spacerItem82 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout72.addItem(self.spacerItem82, 0, 5, 1, 1)

        self.radioButton_29 = QRadioButton(self.gbCropMasks_10)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.gridLayout72.addWidget(self.radioButton_29, 1, 0, 1, 1)

        self.comboBox_23 = QComboBox(self.gbCropMasks_10)
        self.comboBox_23.setObjectName(u"comboBox_23")

        self.gridLayout72.addWidget(self.comboBox_23, 1, 1, 1, 5)

        self.radioButton_30 = QRadioButton(self.gbCropMasks_10)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.gridLayout72.addWidget(self.radioButton_30, 2, 0, 1, 1)

        self.comboBox_24 = QComboBox(self.gbCropMasks_10)
        self.comboBox_24.setObjectName(u"comboBox_24")

        self.gridLayout72.addWidget(self.comboBox_24, 2, 1, 1, 5)

        self.groupBox_19 = QGroupBox(self.gbCropMasks_10)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setCheckable(True)
        self.groupBox_19.setChecked(False)
        self.gridLayout73 = QGridLayout(self.groupBox_19)
        self.gridLayout73.setObjectName(u"gridLayout73")
        self.checkBox_57 = QCheckBox(self.groupBox_19)
        self.checkBox_57.setObjectName(u"checkBox_57")

        self.gridLayout73.addWidget(self.checkBox_57, 0, 0, 1, 1)

        self.checkBox_58 = QCheckBox(self.groupBox_19)
        self.checkBox_58.setObjectName(u"checkBox_58")

        self.gridLayout73.addWidget(self.checkBox_58, 1, 0, 1, 1)

        self.checkBox_59 = QCheckBox(self.groupBox_19)
        self.checkBox_59.setObjectName(u"checkBox_59")

        self.gridLayout73.addWidget(self.checkBox_59, 2, 0, 1, 1)


        self.gridLayout72.addWidget(self.groupBox_19, 3, 0, 1, 3)

        self.groupBox_20 = QGroupBox(self.gbCropMasks_10)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setCheckable(True)
        self.groupBox_20.setChecked(False)
        self.gridLayout74 = QGridLayout(self.groupBox_20)
        self.gridLayout74.setObjectName(u"gridLayout74")
        self.checkBox_60 = QCheckBox(self.groupBox_20)
        self.checkBox_60.setObjectName(u"checkBox_60")

        self.gridLayout74.addWidget(self.checkBox_60, 0, 0, 1, 1)

        self.checkBox_61 = QCheckBox(self.groupBox_20)
        self.checkBox_61.setObjectName(u"checkBox_61")

        self.gridLayout74.addWidget(self.checkBox_61, 1, 0, 1, 1)

        self.checkBox_62 = QCheckBox(self.groupBox_20)
        self.checkBox_62.setObjectName(u"checkBox_62")

        self.gridLayout74.addWidget(self.checkBox_62, 2, 0, 1, 1)


        self.gridLayout72.addWidget(self.groupBox_20, 3, 3, 1, 3)


        self.gridLayout61.addWidget(self.gbCropMasks_10, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod5, "")
        self.tabPeriod6 = QWidget()
        self.tabPeriod6.setObjectName(u"tabPeriod6")
        self.gridLayout75 = QGridLayout(self.tabPeriod6)
        self.gridLayout75.setObjectName(u"gridLayout75")
        self.comboBox_30 = QComboBox(self.tabPeriod6)
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.setObjectName(u"comboBox_30")

        self.gridLayout75.addWidget(self.comboBox_30, 0, 0, 1, 2)

        self.label_56 = QLabel(self.tabPeriod6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.gridLayout75.addWidget(self.label_56, 0, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.tabPeriod6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout75.addWidget(self.lineEdit_6, 0, 3, 1, 3)

        self.line_12 = QFrame(self.tabPeriod6)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout75.addWidget(self.line_12, 0, 6, 2, 1)

        self.hboxLayout35 = QHBoxLayout()
        self.hboxLayout35.setObjectName(u"hboxLayout35")
        self.spacerItem83 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout35.addItem(self.spacerItem83)

        self.pushButton_11 = QPushButton(self.tabPeriod6)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.hboxLayout35.addWidget(self.pushButton_11)

        self.spacerItem84 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout35.addItem(self.spacerItem84)


        self.gridLayout75.addLayout(self.hboxLayout35, 0, 7, 1, 1)

        self.label_57 = QLabel(self.tabPeriod6)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout75.addWidget(self.label_57, 1, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.tabPeriod6)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(20000)
        self.spinBox_13.setValue(500)

        self.gridLayout75.addWidget(self.spinBox_13, 1, 1, 1, 3)

        self.spinBox_14 = QSpinBox(self.tabPeriod6)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(20000)
        self.spinBox_14.setValue(1000)

        self.gridLayout75.addWidget(self.spinBox_14, 1, 4, 1, 2)

        self.hboxLayout36 = QHBoxLayout()
        self.hboxLayout36.setObjectName(u"hboxLayout36")
        self.spacerItem85 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout36.addItem(self.spacerItem85)

        self.pushButton_12 = QPushButton(self.tabPeriod6)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.hboxLayout36.addWidget(self.pushButton_12)

        self.spacerItem86 = QSpacerItem(221, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hboxLayout36.addItem(self.spacerItem86)


        self.gridLayout75.addLayout(self.hboxLayout36, 1, 7, 1, 1)

        self.gbDietComaprison_6 = QGroupBox(self.tabPeriod6)
        self.gbDietComaprison_6.setObjectName(u"gbDietComaprison_6")
        self.gbDietComaprison_6.setCheckable(True)
        self.gridLayout76 = QGridLayout(self.gbDietComaprison_6)
        self.gridLayout76.setObjectName(u"gridLayout76")
        self.diet_comp_box_11 = QGroupBox(self.gbDietComaprison_6)
        self.diet_comp_box_11.setObjectName(u"diet_comp_box_11")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_11.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_11.setSizePolicy(sizePolicy5)
        self.gridLayout77 = QGridLayout(self.diet_comp_box_11)
        self.gridLayout77.setObjectName(u"gridLayout77")
        self.hboxLayout37 = QHBoxLayout()
        self.hboxLayout37.setObjectName(u"hboxLayout37")
        self.label6_11 = QLabel(self.diet_comp_box_11)
        self.label6_11.setObjectName(u"label6_11")
        self.label6_11.setWordWrap(False)

        self.hboxLayout37.addWidget(self.label6_11)

        self.spinBoxDailyCalories_11 = QSpinBox(self.diet_comp_box_11)
        self.spinBoxDailyCalories_11.setObjectName(u"spinBoxDailyCalories_11")
        self.spinBoxDailyCalories_11.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_11.setMinimum(1)
        self.spinBoxDailyCalories_11.setMaximum(5000)
        self.spinBoxDailyCalories_11.setSingleStep(1)
        self.spinBoxDailyCalories_11.setValue(2500)

        self.hboxLayout37.addWidget(self.spinBoxDailyCalories_11)


        self.gridLayout77.addLayout(self.hboxLayout37, 2, 0, 1, 2)

        self.groupplantpercent_11 = QGroupBox(self.diet_comp_box_11)
        self.groupplantpercent_11.setObjectName(u"groupplantpercent_11")
        self.gridLayout78 = QGridLayout(self.groupplantpercent_11)
        self.gridLayout78.setObjectName(u"gridLayout78")
        self.spacerItem87 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout78.addItem(self.spacerItem87, 1, 1, 1, 1)

        self.labelCropTamePercent_11 = QLabel(self.groupplantpercent_11)
        self.labelCropTamePercent_11.setObjectName(u"labelCropTamePercent_11")
        self.labelCropTamePercent_11.setAlignment(Qt.AlignCenter)

        self.gridLayout78.addWidget(self.labelCropTamePercent_11, 1, 2, 1, 1)

        self.sliderCrop_11 = QSlider(self.groupplantpercent_11)
        self.sliderCrop_11.setObjectName(u"sliderCrop_11")
        self.sliderCrop_11.setMaximum(100)
        self.sliderCrop_11.setSingleStep(1)
        self.sliderCrop_11.setPageStep(1)
        self.sliderCrop_11.setValue(90)
        self.sliderCrop_11.setSliderPosition(90)
        self.sliderCrop_11.setOrientation(Qt.Horizontal)
        self.sliderCrop_11.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_11.setTickInterval(25)

        self.gridLayout78.addWidget(self.sliderCrop_11, 2, 0, 1, 3)

        self.labelCropWildPercent_11 = QLabel(self.groupplantpercent_11)
        self.labelCropWildPercent_11.setObjectName(u"labelCropWildPercent_11")
        self.labelCropWildPercent_11.setAlignment(Qt.AlignCenter)

        self.gridLayout78.addWidget(self.labelCropWildPercent_11, 1, 0, 1, 1)

        self.label_58 = QLabel(self.groupplantpercent_11)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout78.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_59 = QLabel(self.groupplantpercent_11)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout78.addWidget(self.label_59, 0, 2, 1, 1)

        self.spacerItem88 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout78.addItem(self.spacerItem88, 0, 1, 1, 1)


        self.gridLayout77.addWidget(self.groupplantpercent_11, 1, 0, 1, 1)

        self.hboxLayout38 = QHBoxLayout()
        self.hboxLayout38.setObjectName(u"hboxLayout38")
        self.labelCropPercent_11 = QLabel(self.diet_comp_box_11)
        self.labelCropPercent_11.setObjectName(u"labelCropPercent_11")

        self.hboxLayout38.addWidget(self.labelCropPercent_11)

        self.sliderDiet_11 = QSlider(self.diet_comp_box_11)
        self.sliderDiet_11.setObjectName(u"sliderDiet_11")
        self.sliderDiet_11.setMaximum(100)
        self.sliderDiet_11.setSingleStep(1)
        self.sliderDiet_11.setPageStep(1)
        self.sliderDiet_11.setValue(50)
        self.sliderDiet_11.setSliderPosition(50)
        self.sliderDiet_11.setOrientation(Qt.Horizontal)
        self.sliderDiet_11.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_11.setTickInterval(25)

        self.hboxLayout38.addWidget(self.sliderDiet_11)

        self.labelMeatPercent_11 = QLabel(self.diet_comp_box_11)
        self.labelMeatPercent_11.setObjectName(u"labelMeatPercent_11")
        self.labelMeatPercent_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout38.addWidget(self.labelMeatPercent_11)


        self.gridLayout77.addLayout(self.hboxLayout38, 0, 0, 1, 2)

        self.groupmeatpercent_11 = QGroupBox(self.diet_comp_box_11)
        self.groupmeatpercent_11.setObjectName(u"groupmeatpercent_11")
        self.groupmeatpercent_11.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout79 = QGridLayout(self.groupmeatpercent_11)
        self.gridLayout79.setObjectName(u"gridLayout79")
        self.label_60 = QLabel(self.groupmeatpercent_11)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout79.addWidget(self.label_60, 0, 0, 1, 1)

        self.spacerItem89 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout79.addItem(self.spacerItem89, 1, 1, 1, 1)

        self.labelMeatWildPercent_11 = QLabel(self.groupmeatpercent_11)
        self.labelMeatWildPercent_11.setObjectName(u"labelMeatWildPercent_11")
        self.labelMeatWildPercent_11.setAlignment(Qt.AlignCenter)

        self.gridLayout79.addWidget(self.labelMeatWildPercent_11, 1, 2, 1, 1)

        self.label_61 = QLabel(self.groupmeatpercent_11)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout79.addWidget(self.label_61, 0, 2, 1, 1)

        self.labelMeatTamePercent_11 = QLabel(self.groupmeatpercent_11)
        self.labelMeatTamePercent_11.setObjectName(u"labelMeatTamePercent_11")
        self.labelMeatTamePercent_11.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_11.setAlignment(Qt.AlignCenter)

        self.gridLayout79.addWidget(self.labelMeatTamePercent_11, 1, 0, 1, 1)

        self.sliderMeat_11 = QSlider(self.groupmeatpercent_11)
        self.sliderMeat_11.setObjectName(u"sliderMeat_11")
        self.sliderMeat_11.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_11.setMaximum(100)
        self.sliderMeat_11.setSingleStep(1)
        self.sliderMeat_11.setPageStep(1)
        self.sliderMeat_11.setValue(90)
        self.sliderMeat_11.setSliderPosition(90)
        self.sliderMeat_11.setOrientation(Qt.Horizontal)
        self.sliderMeat_11.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_11.setTickInterval(25)

        self.gridLayout79.addWidget(self.sliderMeat_11, 2, 0, 1, 3)

        self.spacerItem90 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout79.addItem(self.spacerItem90, 0, 1, 1, 1)


        self.gridLayout77.addWidget(self.groupmeatpercent_11, 1, 1, 1, 1)

        self.spacerItem91 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout77.addItem(self.spacerItem91, 3, 0, 1, 2)


        self.gridLayout76.addWidget(self.diet_comp_box_11, 0, 0, 1, 1)

        self.line_6 = QFrame(self.gbDietComaprison_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout76.addWidget(self.line_6, 0, 1, 1, 1)

        self.diet_comp_box_12 = QGroupBox(self.gbDietComaprison_6)
        self.diet_comp_box_12.setObjectName(u"diet_comp_box_12")
        sizePolicy5.setHeightForWidth(self.diet_comp_box_12.sizePolicy().hasHeightForWidth())
        self.diet_comp_box_12.setSizePolicy(sizePolicy5)
        self.gridLayout80 = QGridLayout(self.diet_comp_box_12)
        self.gridLayout80.setObjectName(u"gridLayout80")
        self.hboxLayout39 = QHBoxLayout()
        self.hboxLayout39.setObjectName(u"hboxLayout39")
        self.label6_12 = QLabel(self.diet_comp_box_12)
        self.label6_12.setObjectName(u"label6_12")
        self.label6_12.setWordWrap(False)

        self.hboxLayout39.addWidget(self.label6_12)

        self.spinBoxDailyCalories_12 = QSpinBox(self.diet_comp_box_12)
        self.spinBoxDailyCalories_12.setObjectName(u"spinBoxDailyCalories_12")
        self.spinBoxDailyCalories_12.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBoxDailyCalories_12.setMinimum(1)
        self.spinBoxDailyCalories_12.setMaximum(5000)
        self.spinBoxDailyCalories_12.setSingleStep(1)
        self.spinBoxDailyCalories_12.setValue(2500)

        self.hboxLayout39.addWidget(self.spinBoxDailyCalories_12)


        self.gridLayout80.addLayout(self.hboxLayout39, 2, 0, 1, 2)

        self.groupplantpercent_12 = QGroupBox(self.diet_comp_box_12)
        self.groupplantpercent_12.setObjectName(u"groupplantpercent_12")
        self.gridLayout81 = QGridLayout(self.groupplantpercent_12)
        self.gridLayout81.setObjectName(u"gridLayout81")
        self.spacerItem92 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout81.addItem(self.spacerItem92, 1, 1, 1, 1)

        self.labelCropTamePercent_12 = QLabel(self.groupplantpercent_12)
        self.labelCropTamePercent_12.setObjectName(u"labelCropTamePercent_12")
        self.labelCropTamePercent_12.setAlignment(Qt.AlignCenter)

        self.gridLayout81.addWidget(self.labelCropTamePercent_12, 1, 2, 1, 1)

        self.sliderCrop_12 = QSlider(self.groupplantpercent_12)
        self.sliderCrop_12.setObjectName(u"sliderCrop_12")
        self.sliderCrop_12.setMaximum(100)
        self.sliderCrop_12.setSingleStep(1)
        self.sliderCrop_12.setPageStep(1)
        self.sliderCrop_12.setValue(90)
        self.sliderCrop_12.setSliderPosition(90)
        self.sliderCrop_12.setOrientation(Qt.Horizontal)
        self.sliderCrop_12.setTickPosition(QSlider.TicksBelow)
        self.sliderCrop_12.setTickInterval(25)

        self.gridLayout81.addWidget(self.sliderCrop_12, 2, 0, 1, 3)

        self.labelCropWildPercent_12 = QLabel(self.groupplantpercent_12)
        self.labelCropWildPercent_12.setObjectName(u"labelCropWildPercent_12")
        self.labelCropWildPercent_12.setAlignment(Qt.AlignCenter)

        self.gridLayout81.addWidget(self.labelCropWildPercent_12, 1, 0, 1, 1)

        self.label_62 = QLabel(self.groupplantpercent_12)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout81.addWidget(self.label_62, 0, 0, 1, 1)

        self.label_63 = QLabel(self.groupplantpercent_12)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout81.addWidget(self.label_63, 0, 2, 1, 1)

        self.spacerItem93 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout81.addItem(self.spacerItem93, 0, 1, 1, 1)


        self.gridLayout80.addWidget(self.groupplantpercent_12, 1, 0, 1, 1)

        self.hboxLayout40 = QHBoxLayout()
        self.hboxLayout40.setObjectName(u"hboxLayout40")
        self.labelCropPercent_12 = QLabel(self.diet_comp_box_12)
        self.labelCropPercent_12.setObjectName(u"labelCropPercent_12")

        self.hboxLayout40.addWidget(self.labelCropPercent_12)

        self.sliderDiet_12 = QSlider(self.diet_comp_box_12)
        self.sliderDiet_12.setObjectName(u"sliderDiet_12")
        self.sliderDiet_12.setMaximum(100)
        self.sliderDiet_12.setSingleStep(1)
        self.sliderDiet_12.setPageStep(1)
        self.sliderDiet_12.setValue(50)
        self.sliderDiet_12.setSliderPosition(50)
        self.sliderDiet_12.setOrientation(Qt.Horizontal)
        self.sliderDiet_12.setTickPosition(QSlider.TicksBothSides)
        self.sliderDiet_12.setTickInterval(25)

        self.hboxLayout40.addWidget(self.sliderDiet_12)

        self.labelMeatPercent_12 = QLabel(self.diet_comp_box_12)
        self.labelMeatPercent_12.setObjectName(u"labelMeatPercent_12")
        self.labelMeatPercent_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hboxLayout40.addWidget(self.labelMeatPercent_12)


        self.gridLayout80.addLayout(self.hboxLayout40, 0, 0, 1, 2)

        self.groupmeatpercent_12 = QGroupBox(self.diet_comp_box_12)
        self.groupmeatpercent_12.setObjectName(u"groupmeatpercent_12")
        self.groupmeatpercent_12.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout82 = QGridLayout(self.groupmeatpercent_12)
        self.gridLayout82.setObjectName(u"gridLayout82")
        self.label_64 = QLabel(self.groupmeatpercent_12)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout82.addWidget(self.label_64, 0, 0, 1, 1)

        self.spacerItem94 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout82.addItem(self.spacerItem94, 1, 1, 1, 1)

        self.labelMeatWildPercent_12 = QLabel(self.groupmeatpercent_12)
        self.labelMeatWildPercent_12.setObjectName(u"labelMeatWildPercent_12")
        self.labelMeatWildPercent_12.setAlignment(Qt.AlignCenter)

        self.gridLayout82.addWidget(self.labelMeatWildPercent_12, 1, 2, 1, 1)

        self.label_65 = QLabel(self.groupmeatpercent_12)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout82.addWidget(self.label_65, 0, 2, 1, 1)

        self.labelMeatTamePercent_12 = QLabel(self.groupmeatpercent_12)
        self.labelMeatTamePercent_12.setObjectName(u"labelMeatTamePercent_12")
        self.labelMeatTamePercent_12.setLayoutDirection(Qt.LeftToRight)
        self.labelMeatTamePercent_12.setAlignment(Qt.AlignCenter)

        self.gridLayout82.addWidget(self.labelMeatTamePercent_12, 1, 0, 1, 1)

        self.sliderMeat_12 = QSlider(self.groupmeatpercent_12)
        self.sliderMeat_12.setObjectName(u"sliderMeat_12")
        self.sliderMeat_12.setLayoutDirection(Qt.LeftToRight)
        self.sliderMeat_12.setMaximum(100)
        self.sliderMeat_12.setSingleStep(1)
        self.sliderMeat_12.setPageStep(1)
        self.sliderMeat_12.setValue(90)
        self.sliderMeat_12.setSliderPosition(90)
        self.sliderMeat_12.setOrientation(Qt.Horizontal)
        self.sliderMeat_12.setTickPosition(QSlider.TicksBelow)
        self.sliderMeat_12.setTickInterval(25)

        self.gridLayout82.addWidget(self.sliderMeat_12, 2, 0, 1, 3)

        self.spacerItem95 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout82.addItem(self.spacerItem95, 0, 1, 1, 1)


        self.gridLayout80.addWidget(self.groupmeatpercent_12, 1, 1, 1, 1)

        self.spacerItem96 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout80.addItem(self.spacerItem96, 3, 0, 1, 2)


        self.gridLayout76.addWidget(self.diet_comp_box_12, 0, 2, 1, 1)


        self.gridLayout75.addWidget(self.gbDietComaprison_6, 2, 0, 1, 8)

        self.gbCropMasks_11 = QGroupBox(self.tabPeriod6)
        self.gbCropMasks_11.setObjectName(u"gbCropMasks_11")
        self.gbCropMasks_11.setCheckable(True)
        self.gridLayout83 = QGridLayout(self.gbCropMasks_11)
        self.gridLayout83.setObjectName(u"gridLayout83")
        self.radioButton_31 = QRadioButton(self.gbCropMasks_11)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.gridLayout83.addWidget(self.radioButton_31, 0, 0, 1, 2)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.gbCropMasks_11)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout83.addWidget(self.doubleSpinBox_16, 0, 2, 1, 2)

        self.spacerItem97 = QSpacerItem(61, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout83.addItem(self.spacerItem97, 0, 4, 1, 1)

        self.radioButton_32 = QRadioButton(self.gbCropMasks_11)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.gridLayout83.addWidget(self.radioButton_32, 1, 0, 1, 1)

        self.comboBox_26 = QComboBox(self.gbCropMasks_11)
        self.comboBox_26.setObjectName(u"comboBox_26")

        self.gridLayout83.addWidget(self.comboBox_26, 1, 1, 1, 4)

        self.radioButton_33 = QRadioButton(self.gbCropMasks_11)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.gridLayout83.addWidget(self.radioButton_33, 2, 0, 1, 1)

        self.comboBox_27 = QComboBox(self.gbCropMasks_11)
        self.comboBox_27.setObjectName(u"comboBox_27")

        self.gridLayout83.addWidget(self.comboBox_27, 2, 1, 1, 4)

        self.groupBox_21 = QGroupBox(self.gbCropMasks_11)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setCheckable(True)
        self.groupBox_21.setChecked(False)
        self.gridLayout84 = QGridLayout(self.groupBox_21)
        self.gridLayout84.setObjectName(u"gridLayout84")
        self.checkBox_63 = QCheckBox(self.groupBox_21)
        self.checkBox_63.setObjectName(u"checkBox_63")

        self.gridLayout84.addWidget(self.checkBox_63, 0, 0, 1, 1)

        self.checkBox_64 = QCheckBox(self.groupBox_21)
        self.checkBox_64.setObjectName(u"checkBox_64")

        self.gridLayout84.addWidget(self.checkBox_64, 1, 0, 1, 1)

        self.checkBox_65 = QCheckBox(self.groupBox_21)
        self.checkBox_65.setObjectName(u"checkBox_65")

        self.gridLayout84.addWidget(self.checkBox_65, 2, 0, 1, 1)


        self.gridLayout83.addWidget(self.groupBox_21, 3, 0, 1, 3)

        self.groupBox_22 = QGroupBox(self.gbCropMasks_11)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setCheckable(True)
        self.groupBox_22.setChecked(False)
        self.gridLayout85 = QGridLayout(self.groupBox_22)
        self.gridLayout85.setObjectName(u"gridLayout85")
        self.checkBox_66 = QCheckBox(self.groupBox_22)
        self.checkBox_66.setObjectName(u"checkBox_66")

        self.gridLayout85.addWidget(self.checkBox_66, 0, 0, 1, 1)

        self.checkBox_67 = QCheckBox(self.groupBox_22)
        self.checkBox_67.setObjectName(u"checkBox_67")

        self.gridLayout85.addWidget(self.checkBox_67, 1, 0, 1, 1)

        self.checkBox_68 = QCheckBox(self.groupBox_22)
        self.checkBox_68.setObjectName(u"checkBox_68")

        self.gridLayout85.addWidget(self.checkBox_68, 2, 0, 1, 1)


        self.gridLayout83.addWidget(self.groupBox_22, 3, 3, 1, 2)


        self.gridLayout75.addWidget(self.gbCropMasks_11, 3, 0, 1, 5)

        self.gbCropMasks_12 = QGroupBox(self.tabPeriod6)
        self.gbCropMasks_12.setObjectName(u"gbCropMasks_12")
        self.gbCropMasks_12.setCheckable(True)
        self.gridLayout86 = QGridLayout(self.gbCropMasks_12)
        self.gridLayout86.setObjectName(u"gridLayout86")
        self.radioButton_34 = QRadioButton(self.gbCropMasks_12)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.gridLayout86.addWidget(self.radioButton_34, 0, 0, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.gbCropMasks_12)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")

        self.gridLayout86.addWidget(self.doubleSpinBox_17, 0, 1, 1, 1)

        self.label_66 = QLabel(self.gbCropMasks_12)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout86.addWidget(self.label_66, 0, 2, 1, 2)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.gbCropMasks_12)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")

        self.gridLayout86.addWidget(self.doubleSpinBox_18, 0, 4, 1, 1)

        self.spacerItem98 = QSpacerItem(20, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout86.addItem(self.spacerItem98, 0, 5, 1, 1)

        self.radioButton_35 = QRadioButton(self.gbCropMasks_12)
        self.radioButton_35.setObjectName(u"radioButton_35")

        self.gridLayout86.addWidget(self.radioButton_35, 1, 0, 1, 1)

        self.comboBox_28 = QComboBox(self.gbCropMasks_12)
        self.comboBox_28.setObjectName(u"comboBox_28")

        self.gridLayout86.addWidget(self.comboBox_28, 1, 1, 1, 5)

        self.radioButton_36 = QRadioButton(self.gbCropMasks_12)
        self.radioButton_36.setObjectName(u"radioButton_36")

        self.gridLayout86.addWidget(self.radioButton_36, 2, 0, 1, 1)

        self.comboBox_29 = QComboBox(self.gbCropMasks_12)
        self.comboBox_29.setObjectName(u"comboBox_29")

        self.gridLayout86.addWidget(self.comboBox_29, 2, 1, 1, 5)

        self.groupBox_23 = QGroupBox(self.gbCropMasks_12)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setCheckable(True)
        self.groupBox_23.setChecked(False)
        self.gridLayout87 = QGridLayout(self.groupBox_23)
        self.gridLayout87.setObjectName(u"gridLayout87")
        self.checkBox_69 = QCheckBox(self.groupBox_23)
        self.checkBox_69.setObjectName(u"checkBox_69")

        self.gridLayout87.addWidget(self.checkBox_69, 0, 0, 1, 1)

        self.checkBox_70 = QCheckBox(self.groupBox_23)
        self.checkBox_70.setObjectName(u"checkBox_70")

        self.gridLayout87.addWidget(self.checkBox_70, 1, 0, 1, 1)

        self.checkBox_71 = QCheckBox(self.groupBox_23)
        self.checkBox_71.setObjectName(u"checkBox_71")

        self.gridLayout87.addWidget(self.checkBox_71, 2, 0, 1, 1)


        self.gridLayout86.addWidget(self.groupBox_23, 3, 0, 1, 3)

        self.groupBox_24 = QGroupBox(self.gbCropMasks_12)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setCheckable(True)
        self.groupBox_24.setChecked(False)
        self.gridLayout88 = QGridLayout(self.groupBox_24)
        self.gridLayout88.setObjectName(u"gridLayout88")
        self.checkBox_72 = QCheckBox(self.groupBox_24)
        self.checkBox_72.setObjectName(u"checkBox_72")

        self.gridLayout88.addWidget(self.checkBox_72, 0, 0, 1, 1)

        self.checkBox_73 = QCheckBox(self.groupBox_24)
        self.checkBox_73.setObjectName(u"checkBox_73")

        self.gridLayout88.addWidget(self.checkBox_73, 1, 0, 1, 1)

        self.checkBox_74 = QCheckBox(self.groupBox_24)
        self.checkBox_74.setObjectName(u"checkBox_74")

        self.gridLayout88.addWidget(self.checkBox_74, 2, 0, 1, 1)


        self.gridLayout86.addWidget(self.groupBox_24, 3, 3, 1, 3)


        self.gridLayout75.addWidget(self.gbCropMasks_12, 3, 5, 1, 3)

        self.twExperiment.addTab(self.tabPeriod6, "")
        self.checkBox_13 = QCheckBox(ExperimentMainForm)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setGeometry(QRect(9, 713, 760, 22))
        self.checkBox_14 = QCheckBox(ExperimentMainForm)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setGeometry(QRect(9, 737, 400, 22))

        self.retranslateUi(ExperimentMainForm)
        self.buttonBox.accepted.connect(ExperimentMainForm.accept)
        self.buttonBox.rejected.connect(ExperimentMainForm.reject)
        self.doubleSpinBox.valueChanged.connect(self.doubleSpinBox_5.setValue)

        self.twExperiment.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ExperimentMainForm)
    # setupUi

    def retranslateUi(self, ExperimentMainForm):
        ExperimentMainForm.setWindowTitle(QCoreApplication.translate("ExperimentMainForm", u"Experiment Setup", None))
        self.label_67.setText(QCoreApplication.translate("ExperimentMainForm", u"Experiment Setup Page", None))
        self.label_68.setText(QCoreApplication.translate("ExperimentMainForm", u"After Setting all values for the Periods you wish to use, check them off below, then click run", None))
#if QT_CONFIG(tooltip)
        self.groupBoxManualSiteEntry.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The information entered here will be inserted as Meta-Data into the resulting maps.  However, Name and Period are optional.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.groupBoxManualSiteEntry.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The name of the site, it's period, and the estimated population.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxManualSiteEntry.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Settlement Information", None))
        self.textLabel2_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Name:", None))
#if QT_CONFIG(tooltip)
        self.lineEditSiteName.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the site you are modelling here. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditSiteName.setText(QCoreApplication.translate("ExperimentMainForm", u"Shuna", None))
#if QT_CONFIG(tooltip)
        self.label_70.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">E</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEditEasting.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting (required)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEditEasting.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Easting of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEditEasting.setText(QCoreApplication.translate("ExperimentMainForm", u"744800", None))
#if QT_CONFIG(tooltip)
        self.label_71.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_71.setText(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">N</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEditNorthing.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing (required)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEditNorthing.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Northing of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEditNorthing.setText(QCoreApplication.translate("ExperimentMainForm", u"3611100", None))
        self.gbxGrass.setTitle("")
        self.lblGrass.setText("")
        self.label_69.setText(QCoreApplication.translate("ExperimentMainForm", u"Mapset:", None))
        self.label_72.setText(QCoreApplication.translate("ExperimentMainForm", u"DEM: ", None))
#if QT_CONFIG(whatsthis)
        self.model_method_box.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst currently offers three types of analysis. Here you select which one you want to use.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Euclidean method starts looking for suitable land at the site and moves outwards from that point 'as the crow flies'. In other words, using Euclidean geometry (or even more simply, it draws circles!)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Walking Time method uses the same basic principle except that it moves outward from t"
                        "he site based on walking time instead of distance. This method is probably the most realistic scenario to run, but it is interesting to compare the results of the three different methods.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Path Distance is very similar to Eucidean, except that this method considers topography when calculating distance from the site.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.model_method_box.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Modelling Method", None))
        self.checkBox_81.setText(QCoreApplication.translate("ExperimentMainForm", u"Walking Time", None))
        self.checkBox_82.setText(QCoreApplication.translate("ExperimentMainForm", u"Path Distance", None))
        self.checkBox_83.setText(QCoreApplication.translate("ExperimentMainForm", u"Euclidean", None))
#if QT_CONFIG(tooltip)
        self.label_73.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_73.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_73.setText(QCoreApplication.translate("ExperimentMainForm", u"Precision: ", None))
#if QT_CONFIG(tooltip)
        self.sbModelPrecision.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbModelPrecision.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox_25.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Select Periods", None))
        self.checkBox_75.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 1", None))
        self.checkBox_78.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 4", None))
        self.checkBox_76.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 2", None))
        self.checkBox_79.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 5", None))
        self.checkBox_77.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 3", None))
        self.checkBox_80.setText(QCoreApplication.translate("ExperimentMainForm", u"Period 6", None))
        self.pushButton_13.setText(QCoreApplication.translate("ExperimentMainForm", u"Load", None))
        self.pushButton_14.setText(QCoreApplication.translate("ExperimentMainForm", u"Save", None))
        self.pushButton_15.setText(QCoreApplication.translate("ExperimentMainForm", u"Run", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabExperiment), QCoreApplication.translate("ExperimentMainForm", u"Experiment", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_5.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_5.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_5.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_5.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_5.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_5.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_5.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_5.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_5.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_5.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_3.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_4.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_3.setSuffix("")
        self.spinBox_3.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_2.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_9.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_11.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_14.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_13.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_2.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_2.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_2.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_2.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_10.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_12.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_2.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_15.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_16.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_2.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_2.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_2.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_2.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_3.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_2.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_3.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_7.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_5.setSuffix("")
        self.label.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_4.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_8.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_9.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_7.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_8.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_9.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_10.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_11.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_12.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod1), QCoreApplication.translate("ExperimentMainForm", u"Period 1", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_10.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_10.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_10.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_10.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_10.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_10.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_10.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_10.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_10.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_10.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_10.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_10.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_10.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_10.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_10.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_10.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_4.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit_2.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_5.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_6.setSuffix("")
        self.spinBox_6.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_3.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison_2.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_3.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_3.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_3.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_3.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_17.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_18.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_3.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_19.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_20.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_3.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_3.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_3.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_4.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_4.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_4.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_21.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_22.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_4.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_23.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_24.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_4.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_4.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_4.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox_2.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_15.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_16.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_17.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_18.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_19.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_20.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_10.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_6.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_7.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_11.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_12.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_21.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_22.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_23.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_24.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_25.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_26.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod2), QCoreApplication.translate("ExperimentMainForm", u"Period 2", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_13.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_13.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_13.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_13.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_13.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_13.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_13.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_13.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_13.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_13.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_13.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_13.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_13.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_13.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_13.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_13.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_13.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_13.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_13.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_13.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_13.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_33.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit_3.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_7.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_7.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_8.setSuffix("")
        self.spinBox_8.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison_3.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_5.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_5.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_5.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_25.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_26.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_5.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_27.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_28.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_5.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_5.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_5.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_29.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_30.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_31.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_32.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_6.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_6.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_6.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton_16.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox_3.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_17.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_18.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_33.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_34.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_35.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_36.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_37.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_38.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_13.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_8.setSuffix("")
        self.label_8.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_9.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_14.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_15.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_27.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_28.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_29.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_30.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_31.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_32.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod3), QCoreApplication.translate("ExperimentMainForm", u"Period 3", None))
        self.comboBox_18.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_18.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_18.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_18.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_18.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_18.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_18.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_18.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_18.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_18.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_18.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_18.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_18.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_18.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_18.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_18.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_18.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_18.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_18.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_18.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_18.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_18.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_18.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_44.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit_4.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton_7.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_34.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_9.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_10.setSuffix("")
        self.spinBox_10.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_8.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison_4.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box_7.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_7.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_7.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_7.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_7.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_7.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_35.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_36.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_7.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_7.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_37.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_38.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_7.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_7.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_7.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_8.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_8.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_8.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_8.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_8.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_8.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_39.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_40.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_8.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_8.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_41.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_42.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_8.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_8.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_8.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks_7.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton_19.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox_10.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_20.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_21.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_39.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_40.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_41.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_42.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_43.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_44.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_8.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_22.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_11.setSuffix("")
        self.label_43.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_12.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_23.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_24.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_45.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_46.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_47.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_48.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_49.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_50.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod4), QCoreApplication.translate("ExperimentMainForm", u"Period 4", None))
        self.comboBox_25.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_25.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_25.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_25.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_25.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_25.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_25.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_25.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_25.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_25.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_25.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_25.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_25.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_25.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_25.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_25.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_25.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_25.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_25.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_25.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_25.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_25.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_25.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_55.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit_5.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton_9.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_45.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_12.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_11.setSuffix("")
        self.spinBox_11.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_10.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison_5.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box_9.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_9.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_9.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_9.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_9.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_9.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_46.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_47.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_9.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_9.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_48.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_49.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_9.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_9.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_9.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_10.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_10.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_10.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_10.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_10.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_10.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_50.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_51.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_10.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_10.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_52.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_53.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_10.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_10.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_10.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks_9.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton_25.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox_13.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_26.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_27.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_51.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_52.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_53.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_54.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_55.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_56.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_10.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_28.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_14.setSuffix("")
        self.label_54.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_15.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_29.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_30.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_57.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_58.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_59.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_60.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_61.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_62.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod5), QCoreApplication.translate("ExperimentMainForm", u"Period 5", None))
        self.comboBox_30.setItemText(0, QCoreApplication.translate("ExperimentMainForm", u"Select Period", None))
        self.comboBox_30.setItemText(1, QCoreApplication.translate("ExperimentMainForm", u"Custom", None))
        self.comboBox_30.setItemText(2, QCoreApplication.translate("ExperimentMainForm", u"Lower Paleolithic", None))
        self.comboBox_30.setItemText(3, QCoreApplication.translate("ExperimentMainForm", u"Middle Paleolithic", None))
        self.comboBox_30.setItemText(4, QCoreApplication.translate("ExperimentMainForm", u"Upper Paleolithic", None))
        self.comboBox_30.setItemText(5, QCoreApplication.translate("ExperimentMainForm", u"Epipaleolithic", None))
        self.comboBox_30.setItemText(6, QCoreApplication.translate("ExperimentMainForm", u"Pre-pottery Neolithic", None))
        self.comboBox_30.setItemText(7, QCoreApplication.translate("ExperimentMainForm", u"Pottery Neolithic", None))
        self.comboBox_30.setItemText(8, QCoreApplication.translate("ExperimentMainForm", u"Early Chalcolithic", None))
        self.comboBox_30.setItemText(9, QCoreApplication.translate("ExperimentMainForm", u"Late Chalcolithic ", None))
        self.comboBox_30.setItemText(10, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age I", None))
        self.comboBox_30.setItemText(11, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age II", None))
        self.comboBox_30.setItemText(12, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age III", None))
        self.comboBox_30.setItemText(13, QCoreApplication.translate("ExperimentMainForm", u"Early Bronze Age IV", None))
        self.comboBox_30.setItemText(14, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age I", None))
        self.comboBox_30.setItemText(15, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age II", None))
        self.comboBox_30.setItemText(16, QCoreApplication.translate("ExperimentMainForm", u"Middle Bronze Age III", None))
        self.comboBox_30.setItemText(17, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age I", None))
        self.comboBox_30.setItemText(18, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II A", None))
        self.comboBox_30.setItemText(19, QCoreApplication.translate("ExperimentMainForm", u"Late Bronze Age II B", None))
        self.comboBox_30.setItemText(20, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I A", None))
        self.comboBox_30.setItemText(21, QCoreApplication.translate("ExperimentMainForm", u"Iron Age I B", None))
        self.comboBox_30.setItemText(22, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II A", None))
        self.comboBox_30.setItemText(23, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II B", None))
        self.comboBox_30.setItemText(24, QCoreApplication.translate("ExperimentMainForm", u"Iron Age II C", None))

        self.label_56.setText(QCoreApplication.translate("ExperimentMainForm", u"or", None))
        self.lineEdit_6.setText(QCoreApplication.translate("ExperimentMainForm", u"Enter Custom Name", None))
        self.pushButton_11.setText(QCoreApplication.translate("ExperimentMainForm", u"Crops", None))
        self.label_57.setText(QCoreApplication.translate("ExperimentMainForm", u"Population Range", None))
        self.spinBox_13.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Min ", None))
        self.spinBox_14.setSuffix("")
        self.spinBox_14.setPrefix(QCoreApplication.translate("ExperimentMainForm", u"Max ", None))
        self.pushButton_12.setText(QCoreApplication.translate("ExperimentMainForm", u"Animals", None))
        self.gbDietComaprison_6.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Diet Comparison", None))
        self.diet_comp_box_11.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'A' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_11.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_11.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_11.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_11.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_11.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_58.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_59.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_11.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_11.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_60.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_61.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_11.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_11.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_11.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.diet_comp_box_12.setTitle(QCoreApplication.translate("ExperimentMainForm", u"'B' Settings", None))
#if QT_CONFIG(tooltip)
        self.label6_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label6_12.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label6_12.setText(QCoreApplication.translate("ExperimentMainForm", u"Calories per\n"
"Person per Day", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDailyCalories_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.spinBoxDailyCalories_12.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of Landuse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupplantpercent_12.setTitle(QCoreApplication.translate("ExperimentMainForm", u"PLANT", None))
#if QT_CONFIG(tooltip)
        self.labelCropTamePercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropTamePercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderCrop_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderCrop_12.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelCropWildPercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropWildPercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_62.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
        self.label_63.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelCropPercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCropPercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
#if QT_CONFIG(tooltip)
        self.sliderDiet_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderDiet_12.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.labelMeatPercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatPercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"50", None))
        self.groupmeatpercent_12.setTitle(QCoreApplication.translate("ExperimentMainForm", u"MEAT", None))
        self.label_64.setText(QCoreApplication.translate("ExperimentMainForm", u"Tame", None))
#if QT_CONFIG(tooltip)
        self.labelMeatWildPercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatWildPercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"10", None))
        self.label_65.setText(QCoreApplication.translate("ExperimentMainForm", u"Wild", None))
#if QT_CONFIG(tooltip)
        self.labelMeatTamePercent_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMeatTamePercent_12.setText(QCoreApplication.translate("ExperimentMainForm", u"90", None))
#if QT_CONFIG(tooltip)
        self.sliderMeat_12.setToolTip(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sliderMeat_12.setWhatsThis(QCoreApplication.translate("ExperimentMainForm", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.gbCropMasks_11.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Crop Masks", None))
        self.radioButton_31.setText(QCoreApplication.translate("ExperimentMainForm", u"Max Slope", None))
        self.doubleSpinBox_16.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" deg", None))
        self.radioButton_32.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_33.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_63.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_64.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_65.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_66.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_67.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_68.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.gbCropMasks_12.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Animal Masks", None))
        self.radioButton_34.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.doubleSpinBox_17.setSuffix("")
        self.label_66.setText(QCoreApplication.translate("ExperimentMainForm", u"to", None))
        self.doubleSpinBox_18.setSuffix(QCoreApplication.translate("ExperimentMainForm", u" (max)", None))
        self.radioButton_35.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.radioButton_36.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 1", None))
        self.checkBox_69.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_70.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_71.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("ExperimentMainForm", u"Combination 2", None))
        self.checkBox_72.setText(QCoreApplication.translate("ExperimentMainForm", u"Slope", None))
        self.checkBox_73.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 1", None))
        self.checkBox_74.setText(QCoreApplication.translate("ExperimentMainForm", u"Mask 2", None))
        self.twExperiment.setTabText(self.twExperiment.indexOf(self.tabPeriod6), QCoreApplication.translate("ExperimentMainForm", u"Period 6", None))
        self.checkBox_13.setText(QCoreApplication.translate("ExperimentMainForm", u"Run with and without considering fallow for grazing", None))
        self.checkBox_14.setText(QCoreApplication.translate("ExperimentMainForm", u"Run with and without considering fodder being used as feed", None))
    # retranslateUi

