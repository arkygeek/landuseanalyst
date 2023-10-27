# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laanimalmanagerbase.ui'
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
    QDialog, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QToolButton, QWidget)
import resources_rc

class Ui_LaAnimalManagerBase(object):
    def setupUi(self, LaAnimalManagerBase):
        if not LaAnimalManagerBase.objectName():
            LaAnimalManagerBase.setObjectName(u"LaAnimalManagerBase")
        LaAnimalManagerBase.resize(806, 750)
        icon = QIcon(u":/la_icon.png")
        LaAnimalManagerBase.setWindowIcon(icon)
        self.gridLayout = QGridLayout(LaAnimalManagerBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxAnimalDescription = QGroupBox(LaAnimalManagerBase)
        self.groupBoxAnimalDescription.setObjectName(u"groupBoxAnimalDescription")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAnimalDescription.sizePolicy().hasHeightForWidth())
        self.groupBoxAnimalDescription.setSizePolicy(sizePolicy)
        self.gridLayout1 = QGridLayout(self.groupBoxAnimalDescription)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.groupBoxAnimalDescription)
        self.label.setObjectName(u"label")

        self.hboxLayout.addWidget(self.label)

        self.leName = QLineEdit(self.groupBoxAnimalDescription)
        self.leName.setObjectName(u"leName")

        self.hboxLayout.addWidget(self.leName)


        self.gridLayout1.addLayout(self.hboxLayout, 0, 0, 1, 2)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.label_4 = QLabel(self.groupBoxAnimalDescription)
        self.label_4.setObjectName(u"label_4")

        self.hboxLayout1.addWidget(self.label_4)

        self.leDescription = QLineEdit(self.groupBoxAnimalDescription)
        self.leDescription.setObjectName(u"leDescription")

        self.hboxLayout1.addWidget(self.leDescription)


        self.gridLayout1.addLayout(self.hboxLayout1, 1, 0, 1, 2)

        self.line_2 = QFrame(self.groupBoxAnimalDescription)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout1.addWidget(self.line_2, 2, 0, 1, 2)

        self.label_14 = QLabel(self.groupBoxAnimalDescription)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_14, 3, 0, 1, 1)

        self.sbMeatFoodValue = QSpinBox(self.groupBoxAnimalDescription)
        self.sbMeatFoodValue.setObjectName(u"sbMeatFoodValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sbMeatFoodValue.sizePolicy().hasHeightForWidth())
        self.sbMeatFoodValue.setSizePolicy(sizePolicy2)
        self.sbMeatFoodValue.setAlignment(Qt.AlignRight)
        self.sbMeatFoodValue.setMaximum(20000)
        self.sbMeatFoodValue.setValue(3000)

        self.gridLayout1.addWidget(self.sbMeatFoodValue, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBoxAnimalDescription)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_9, 4, 0, 1, 1)

        self.sbUsableMeatPercent = QSpinBox(self.groupBoxAnimalDescription)
        self.sbUsableMeatPercent.setObjectName(u"sbUsableMeatPercent")
        sizePolicy2.setHeightForWidth(self.sbUsableMeatPercent.sizePolicy().hasHeightForWidth())
        self.sbUsableMeatPercent.setSizePolicy(sizePolicy2)
        self.sbUsableMeatPercent.setAlignment(Qt.AlignRight)
        self.sbUsableMeatPercent.setMaximum(120)
        self.sbUsableMeatPercent.setValue(80)

        self.gridLayout1.addWidget(self.sbUsableMeatPercent, 4, 1, 1, 1)

        self.label_10 = QLabel(self.groupBoxAnimalDescription)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_10, 5, 0, 1, 1)

        self.sbKillWeight = QSpinBox(self.groupBoxAnimalDescription)
        self.sbKillWeight.setObjectName(u"sbKillWeight")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sbKillWeight.sizePolicy().hasHeightForWidth())
        self.sbKillWeight.setSizePolicy(sizePolicy3)
        self.sbKillWeight.setAlignment(Qt.AlignRight)
        self.sbKillWeight.setMaximum(2000)
        self.sbKillWeight.setValue(100)

        self.gridLayout1.addWidget(self.sbKillWeight, 5, 1, 1, 1)

        self.label_16 = QLabel(self.groupBoxAnimalDescription)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_16, 6, 0, 1, 1)

        self.sbWeaningWeight = QSpinBox(self.groupBoxAnimalDescription)
        self.sbWeaningWeight.setObjectName(u"sbWeaningWeight")
        sizePolicy2.setHeightForWidth(self.sbWeaningWeight.sizePolicy().hasHeightForWidth())
        self.sbWeaningWeight.setSizePolicy(sizePolicy2)
        self.sbWeaningWeight.setAlignment(Qt.AlignRight)
        self.sbWeaningWeight.setMaximum(120)
        self.sbWeaningWeight.setValue(80)

        self.gridLayout1.addWidget(self.sbWeaningWeight, 6, 1, 1, 1)

        self.label_11 = QLabel(self.groupBoxAnimalDescription)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_11, 7, 0, 1, 1)

        self.sbGrowTime = QSpinBox(self.groupBoxAnimalDescription)
        self.sbGrowTime.setObjectName(u"sbGrowTime")
        sizePolicy2.setHeightForWidth(self.sbGrowTime.sizePolicy().hasHeightForWidth())
        self.sbGrowTime.setSizePolicy(sizePolicy2)
        self.sbGrowTime.setAlignment(Qt.AlignRight)
        self.sbGrowTime.setMinimum(1)
        self.sbGrowTime.setMaximum(1000)
        self.sbGrowTime.setValue(60)

        self.gridLayout1.addWidget(self.sbGrowTime, 7, 1, 1, 1)

        self.label_12 = QLabel(self.groupBoxAnimalDescription)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_12, 8, 0, 1, 1)

        self.sbDeathRate = QSpinBox(self.groupBoxAnimalDescription)
        self.sbDeathRate.setObjectName(u"sbDeathRate")
        sizePolicy3.setHeightForWidth(self.sbDeathRate.sizePolicy().hasHeightForWidth())
        self.sbDeathRate.setSizePolicy(sizePolicy3)
        self.sbDeathRate.setAlignment(Qt.AlignRight)
        self.sbDeathRate.setMaximum(100)
        self.sbDeathRate.setValue(10)

        self.gridLayout1.addWidget(self.sbDeathRate, 8, 1, 1, 1)

        self.label_2 = QLabel(self.groupBoxAnimalDescription)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_2, 9, 0, 1, 1)

        self.sbSexualMaturity = QSpinBox(self.groupBoxAnimalDescription)
        self.sbSexualMaturity.setObjectName(u"sbSexualMaturity")
        sizePolicy2.setHeightForWidth(self.sbSexualMaturity.sizePolicy().hasHeightForWidth())
        self.sbSexualMaturity.setSizePolicy(sizePolicy2)
        self.sbSexualMaturity.setAlignment(Qt.AlignRight)
        self.sbSexualMaturity.setMaximum(240)
        self.sbSexualMaturity.setValue(18)

        self.gridLayout1.addWidget(self.sbSexualMaturity, 9, 1, 1, 1)

        self.label_17 = QLabel(self.groupBoxAnimalDescription)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_17, 10, 0, 1, 1)

        self.sbAdultWeight = QSpinBox(self.groupBoxAnimalDescription)
        self.sbAdultWeight.setObjectName(u"sbAdultWeight")
        sizePolicy3.setHeightForWidth(self.sbAdultWeight.sizePolicy().hasHeightForWidth())
        self.sbAdultWeight.setSizePolicy(sizePolicy3)
        self.sbAdultWeight.setAlignment(Qt.AlignRight)
        self.sbAdultWeight.setMaximum(2000)
        self.sbAdultWeight.setValue(100)

        self.gridLayout1.addWidget(self.sbAdultWeight, 10, 1, 1, 1)

        self.label_18 = QLabel(self.groupBoxAnimalDescription)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_18, 11, 0, 1, 1)

        self.sbFemalesToMales = QSpinBox(self.groupBoxAnimalDescription)
        self.sbFemalesToMales.setObjectName(u"sbFemalesToMales")
        sizePolicy3.setHeightForWidth(self.sbFemalesToMales.sizePolicy().hasHeightForWidth())
        self.sbFemalesToMales.setSizePolicy(sizePolicy3)
        self.sbFemalesToMales.setAlignment(Qt.AlignRight)
        self.sbFemalesToMales.setMinimum(1)
        self.sbFemalesToMales.setMaximum(2000)
        self.sbFemalesToMales.setValue(20)

        self.gridLayout1.addWidget(self.sbFemalesToMales, 11, 1, 1, 1)

        self.label_3 = QLabel(self.groupBoxAnimalDescription)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_3, 12, 0, 1, 1)

        self.sbBreedingLife = QSpinBox(self.groupBoxAnimalDescription)
        self.sbBreedingLife.setObjectName(u"sbBreedingLife")
        sizePolicy2.setHeightForWidth(self.sbBreedingLife.sizePolicy().hasHeightForWidth())
        self.sbBreedingLife.setSizePolicy(sizePolicy2)
        self.sbBreedingLife.setAlignment(Qt.AlignRight)
        self.sbBreedingLife.setMinimum(1)
        self.sbBreedingLife.setMaximum(120)
        self.sbBreedingLife.setValue(4)

        self.gridLayout1.addWidget(self.sbBreedingLife, 12, 1, 1, 1)

        self.label_19 = QLabel(self.groupBoxAnimalDescription)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_19, 13, 0, 1, 1)

        self.sbConceptionEfficiency = QSpinBox(self.groupBoxAnimalDescription)
        self.sbConceptionEfficiency.setObjectName(u"sbConceptionEfficiency")
        sizePolicy3.setHeightForWidth(self.sbConceptionEfficiency.sizePolicy().hasHeightForWidth())
        self.sbConceptionEfficiency.setSizePolicy(sizePolicy3)
        self.sbConceptionEfficiency.setAlignment(Qt.AlignRight)
        self.sbConceptionEfficiency.setMaximum(2000)
        self.sbConceptionEfficiency.setValue(100)

        self.gridLayout1.addWidget(self.sbConceptionEfficiency, 13, 1, 1, 1)

        self.label_5 = QLabel(self.groupBoxAnimalDescription)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_5, 14, 0, 1, 1)

        self.sbYoungPerBirth = QSpinBox(self.groupBoxAnimalDescription)
        self.sbYoungPerBirth.setObjectName(u"sbYoungPerBirth")
        sizePolicy2.setHeightForWidth(self.sbYoungPerBirth.sizePolicy().hasHeightForWidth())
        self.sbYoungPerBirth.setSizePolicy(sizePolicy2)
        self.sbYoungPerBirth.setAlignment(Qt.AlignRight)
        self.sbYoungPerBirth.setMinimum(1)
        self.sbYoungPerBirth.setMaximum(20)
        self.sbYoungPerBirth.setValue(1)

        self.gridLayout1.addWidget(self.sbYoungPerBirth, 14, 1, 1, 1)

        self.label_6 = QLabel(self.groupBoxAnimalDescription)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_6, 15, 0, 1, 1)

        self.sbWeaningAge = QSpinBox(self.groupBoxAnimalDescription)
        self.sbWeaningAge.setObjectName(u"sbWeaningAge")
        sizePolicy2.setHeightForWidth(self.sbWeaningAge.sizePolicy().hasHeightForWidth())
        self.sbWeaningAge.setSizePolicy(sizePolicy2)
        self.sbWeaningAge.setAlignment(Qt.AlignRight)
        self.sbWeaningAge.setMaximum(120)
        self.sbWeaningAge.setValue(80)

        self.gridLayout1.addWidget(self.sbWeaningAge, 15, 1, 1, 1)

        self.label_7 = QLabel(self.groupBoxAnimalDescription)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_7, 16, 0, 1, 1)

        self.sbGestationTime = QSpinBox(self.groupBoxAnimalDescription)
        self.sbGestationTime.setObjectName(u"sbGestationTime")
        sizePolicy2.setHeightForWidth(self.sbGestationTime.sizePolicy().hasHeightForWidth())
        self.sbGestationTime.setSizePolicy(sizePolicy2)
        self.sbGestationTime.setAlignment(Qt.AlignRight)
        self.sbGestationTime.setMinimum(1)
        self.sbGestationTime.setMaximum(365)
        self.sbGestationTime.setValue(120)

        self.gridLayout1.addWidget(self.sbGestationTime, 16, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxAnimalDescription)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_8, 17, 0, 1, 1)

        self.sbEstrousCycleTime = QSpinBox(self.groupBoxAnimalDescription)
        self.sbEstrousCycleTime.setObjectName(u"sbEstrousCycleTime")
        sizePolicy2.setHeightForWidth(self.sbEstrousCycleTime.sizePolicy().hasHeightForWidth())
        self.sbEstrousCycleTime.setSizePolicy(sizePolicy2)
        self.sbEstrousCycleTime.setAlignment(Qt.AlignRight)
        self.sbEstrousCycleTime.setMaximum(120)
        self.sbEstrousCycleTime.setValue(21)

        self.gridLayout1.addWidget(self.sbEstrousCycleTime, 17, 1, 1, 1)

        self.label_21 = QLabel(self.groupBoxAnimalDescription)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.label_21, 18, 0, 1, 1)

        self.sbLactationTime = QSpinBox(self.groupBoxAnimalDescription)
        self.sbLactationTime.setObjectName(u"sbLactationTime")
        sizePolicy2.setHeightForWidth(self.sbLactationTime.sizePolicy().hasHeightForWidth())
        self.sbLactationTime.setSizePolicy(sizePolicy2)
        self.sbLactationTime.setAlignment(Qt.AlignRight)
        self.sbLactationTime.setMaximum(1000)
        self.sbLactationTime.setValue(210)

        self.gridLayout1.addWidget(self.sbLactationTime, 18, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBoxAnimalDescription, 0, 0, 3, 1)

        self.grpProfiles = QGroupBox(LaAnimalManagerBase)
        self.grpProfiles.setObjectName(u"grpProfiles")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.grpProfiles.sizePolicy().hasHeightForWidth())
        self.grpProfiles.setSizePolicy(sizePolicy4)
        self.gridLayout2 = QGridLayout(self.grpProfiles)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.tblAnimals = QTableWidget(self.grpProfiles)
        if (self.tblAnimals.columnCount() < 2):
            self.tblAnimals.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblAnimals.setObjectName(u"tblAnimals")
        self.tblAnimals.setAlternatingRowColors(True)
        self.tblAnimals.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAnimals.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout2.addWidget(self.tblAnimals, 0, 0, 4, 1)

        self.gridLayout3 = QGridLayout()
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.toolCopy = QToolButton(self.grpProfiles)
        self.toolCopy.setObjectName(u"toolCopy")
        icon1 = QIcon(u":/copy.png")
        self.toolCopy.setIcon(icon1)

        self.gridLayout3.addWidget(self.toolCopy, 2, 1, 1, 1)

        self.toolNew = QToolButton(self.grpProfiles)
        self.toolNew.setObjectName(u"toolNew")
        icon2 = QIcon(u":/new.png")
        self.toolNew.setIcon(icon2)

        self.gridLayout3.addWidget(self.toolNew, 2, 0, 1, 1)

        self.toolDelete = QToolButton(self.grpProfiles)
        self.toolDelete.setObjectName(u"toolDelete")
        icon3 = QIcon(u":/delete.png")
        self.toolDelete.setIcon(icon3)

        self.gridLayout3.addWidget(self.toolDelete, 2, 2, 1, 1)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout3.addItem(self.spacerItem, 1, 1, 1, 1)

        self.lblAnimalPix = QLabel(self.grpProfiles)
        self.lblAnimalPix.setObjectName(u"lblAnimalPix")
        self.lblAnimalPix.setMinimumSize(QSize(100, 100))
        self.lblAnimalPix.setMaximumSize(QSize(100, 100))
        self.lblAnimalPix.setAlignment(Qt.AlignCenter)

        self.gridLayout3.addWidget(self.lblAnimalPix, 0, 0, 1, 3)


        self.gridLayout2.addLayout(self.gridLayout3, 0, 1, 1, 1)

        self.pbnAnimalPic = QPushButton(self.grpProfiles)
        self.pbnAnimalPic.setObjectName(u"pbnAnimalPic")

        self.gridLayout2.addWidget(self.pbnAnimalPic, 1, 1, 1, 1)

        self.pbnImport = QPushButton(self.grpProfiles)
        self.pbnImport.setObjectName(u"pbnImport")
        self.pbnImport.setMinimumSize(QSize(80, 0))

        self.gridLayout2.addWidget(self.pbnImport, 2, 1, 1, 1)

        self.pbnExport = QPushButton(self.grpProfiles)
        self.pbnExport.setObjectName(u"pbnExport")
        self.pbnExport.setMinimumSize(QSize(80, 0))

        self.gridLayout2.addWidget(self.pbnExport, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.grpProfiles, 0, 1, 1, 3)

        self.groupBoxFeedRequirements = QGroupBox(LaAnimalManagerBase)
        self.groupBoxFeedRequirements.setObjectName(u"groupBoxFeedRequirements")
        sizePolicy2.setHeightForWidth(self.groupBoxFeedRequirements.sizePolicy().hasHeightForWidth())
        self.groupBoxFeedRequirements.setSizePolicy(sizePolicy2)
        self.gridLayout4 = QGridLayout(self.groupBoxFeedRequirements)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout5 = QGridLayout()
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.label_13 = QLabel(self.groupBoxFeedRequirements)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout5.addWidget(self.label_13, 0, 0, 1, 1)

        self.cbFeedEnergyType = QComboBox(self.groupBoxFeedRequirements)
        self.cbFeedEnergyType.addItem("")
        self.cbFeedEnergyType.addItem("")
        self.cbFeedEnergyType.setObjectName(u"cbFeedEnergyType")

        self.gridLayout5.addWidget(self.cbFeedEnergyType, 0, 1, 1, 1)

        self.labelFeedRequirements2 = QLabel(self.groupBoxFeedRequirements)
        self.labelFeedRequirements2.setObjectName(u"labelFeedRequirements2")

        self.gridLayout5.addWidget(self.labelFeedRequirements2, 1, 0, 1, 1)

        self.sbEnergyForPregnant = QSpinBox(self.groupBoxFeedRequirements)
        self.sbEnergyForPregnant.setObjectName(u"sbEnergyForPregnant")
        sizePolicy3.setHeightForWidth(self.sbEnergyForPregnant.sizePolicy().hasHeightForWidth())
        self.sbEnergyForPregnant.setSizePolicy(sizePolicy3)
        self.sbEnergyForPregnant.setMaximum(20000)
        self.sbEnergyForPregnant.setValue(4000)

        self.gridLayout5.addWidget(self.sbEnergyForPregnant, 1, 1, 1, 1)

        self.labelFeedRequirements3 = QLabel(self.groupBoxFeedRequirements)
        self.labelFeedRequirements3.setObjectName(u"labelFeedRequirements3")

        self.gridLayout5.addWidget(self.labelFeedRequirements3, 2, 0, 1, 1)

        self.sbEnergyForLactating = QSpinBox(self.groupBoxFeedRequirements)
        self.sbEnergyForLactating.setObjectName(u"sbEnergyForLactating")
        sizePolicy3.setHeightForWidth(self.sbEnergyForLactating.sizePolicy().hasHeightForWidth())
        self.sbEnergyForLactating.setSizePolicy(sizePolicy3)
        self.sbEnergyForLactating.setMaximum(20000)
        self.sbEnergyForLactating.setValue(4000)

        self.gridLayout5.addWidget(self.sbEnergyForLactating, 2, 1, 1, 1)

        self.labelFeedRequirements3_2 = QLabel(self.groupBoxFeedRequirements)
        self.labelFeedRequirements3_2.setObjectName(u"labelFeedRequirements3_2")

        self.gridLayout5.addWidget(self.labelFeedRequirements3_2, 3, 0, 1, 1)

        self.sbEnergyForMaintenance = QSpinBox(self.groupBoxFeedRequirements)
        self.sbEnergyForMaintenance.setObjectName(u"sbEnergyForMaintenance")
        sizePolicy3.setHeightForWidth(self.sbEnergyForMaintenance.sizePolicy().hasHeightForWidth())
        self.sbEnergyForMaintenance.setSizePolicy(sizePolicy3)
        self.sbEnergyForMaintenance.setMaximum(20000)
        self.sbEnergyForMaintenance.setValue(4000)

        self.gridLayout5.addWidget(self.sbEnergyForMaintenance, 3, 1, 1, 1)

        self.labelFeedRequirements4 = QLabel(self.groupBoxFeedRequirements)
        self.labelFeedRequirements4.setObjectName(u"labelFeedRequirements4")

        self.gridLayout5.addWidget(self.labelFeedRequirements4, 4, 0, 1, 1)

        self.sbEnergyForJuvenilePerKg = QSpinBox(self.groupBoxFeedRequirements)
        self.sbEnergyForJuvenilePerKg.setObjectName(u"sbEnergyForJuvenilePerKg")
        sizePolicy3.setHeightForWidth(self.sbEnergyForJuvenilePerKg.sizePolicy().hasHeightForWidth())
        self.sbEnergyForJuvenilePerKg.setSizePolicy(sizePolicy3)
        self.sbEnergyForJuvenilePerKg.setMaximum(20000)
        self.sbEnergyForJuvenilePerKg.setValue(300)

        self.gridLayout5.addWidget(self.sbEnergyForJuvenilePerKg, 4, 1, 1, 1)


        self.gridLayout4.addLayout(self.gridLayout5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxFeedRequirements, 1, 1, 2, 1)

        self.groupBoxByProducts = QGroupBox(LaAnimalManagerBase)
        self.groupBoxByProducts.setObjectName(u"groupBoxByProducts")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBoxByProducts.sizePolicy().hasHeightForWidth())
        self.groupBoxByProducts.setSizePolicy(sizePolicy5)
        self.groupBoxByProducts.setMinimumSize(QSize(0, 0))
        self.gridLayout6 = QGridLayout(self.groupBoxByProducts)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.checkBoxMilk = QCheckBox(self.groupBoxByProducts)
        self.checkBoxMilk.setObjectName(u"checkBoxMilk")
        self.checkBoxMilk.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout6.addWidget(self.checkBoxMilk, 0, 0, 1, 1)

        self.sbMilk = QSpinBox(self.groupBoxByProducts)
        self.sbMilk.setObjectName(u"sbMilk")
        sizePolicy2.setHeightForWidth(self.sbMilk.sizePolicy().hasHeightForWidth())
        self.sbMilk.setSizePolicy(sizePolicy2)
        self.sbMilk.setAlignment(Qt.AlignRight)
        self.sbMilk.setMaximum(100000)
        self.sbMilk.setValue(18)

        self.gridLayout6.addWidget(self.sbMilk, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBoxByProducts)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout6.addWidget(self.label_15, 1, 0, 1, 1)

        self.sbMilkFoodValue = QSpinBox(self.groupBoxByProducts)
        self.sbMilkFoodValue.setObjectName(u"sbMilkFoodValue")
        sizePolicy2.setHeightForWidth(self.sbMilkFoodValue.sizePolicy().hasHeightForWidth())
        self.sbMilkFoodValue.setSizePolicy(sizePolicy2)
        self.sbMilkFoodValue.setAlignment(Qt.AlignRight)
        self.sbMilkFoodValue.setMinimum(1)
        self.sbMilkFoodValue.setMaximum(10000)
        self.sbMilkFoodValue.setValue(4)

        self.gridLayout6.addWidget(self.sbMilkFoodValue, 1, 1, 1, 1)

        self.line = QFrame(self.groupBoxByProducts)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout6.addWidget(self.line, 2, 0, 1, 2)

        self.checkBoxFleece = QCheckBox(self.groupBoxByProducts)
        self.checkBoxFleece.setObjectName(u"checkBoxFleece")

        self.gridLayout6.addWidget(self.checkBoxFleece, 3, 0, 1, 1)

        self.sbFleeceWeight = QSpinBox(self.groupBoxByProducts)
        self.sbFleeceWeight.setObjectName(u"sbFleeceWeight")
        sizePolicy2.setHeightForWidth(self.sbFleeceWeight.sizePolicy().hasHeightForWidth())
        self.sbFleeceWeight.setSizePolicy(sizePolicy2)
        self.sbFleeceWeight.setAlignment(Qt.AlignRight)
        self.sbFleeceWeight.setMinimum(1)
        self.sbFleeceWeight.setMaximum(200)
        self.sbFleeceWeight.setValue(1)

        self.gridLayout6.addWidget(self.sbFleeceWeight, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBoxByProducts, 1, 2, 1, 2)

        self.pbnApply = QPushButton(LaAnimalManagerBase)
        self.pbnApply.setObjectName(u"pbnApply")
        self.pbnApply.setCheckable(False)
        self.pbnApply.setFlat(False)

        self.gridLayout.addWidget(self.pbnApply, 2, 2, 1, 1)

        self.pbnClose = QPushButton(LaAnimalManagerBase)
        self.pbnClose.setObjectName(u"pbnClose")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pbnClose.sizePolicy().hasHeightForWidth())
        self.pbnClose.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.pbnClose, 2, 3, 1, 1)

        QWidget.setTabOrder(self.tblAnimals, self.pbnImport)
        QWidget.setTabOrder(self.pbnImport, self.pbnExport)
        QWidget.setTabOrder(self.pbnExport, self.toolNew)
        QWidget.setTabOrder(self.toolNew, self.toolCopy)
        QWidget.setTabOrder(self.toolCopy, self.toolDelete)
        QWidget.setTabOrder(self.toolDelete, self.leName)
        QWidget.setTabOrder(self.leName, self.leDescription)
        QWidget.setTabOrder(self.leDescription, self.sbUsableMeatPercent)
        QWidget.setTabOrder(self.sbUsableMeatPercent, self.sbKillWeight)
        QWidget.setTabOrder(self.sbKillWeight, self.sbGrowTime)
        QWidget.setTabOrder(self.sbGrowTime, self.sbDeathRate)
        QWidget.setTabOrder(self.sbDeathRate, self.sbEnergyForPregnant)
        QWidget.setTabOrder(self.sbEnergyForPregnant, self.sbEnergyForLactating)
        QWidget.setTabOrder(self.sbEnergyForLactating, self.sbEnergyForJuvenilePerKg)

        self.retranslateUi(LaAnimalManagerBase)
        self.pbnClose.clicked.connect(LaAnimalManagerBase.reject)

        QMetaObject.connectSlotsByName(LaAnimalManagerBase)
    # setupUi

    def retranslateUi(self, LaAnimalManagerBase):
        LaAnimalManagerBase.setWindowTitle(QCoreApplication.translate("LaAnimalManagerBase", u"Animal Profile Manager", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxAnimalDescription.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model any animal, several details must be entered to define specific types or breeds. Animal Manager asks for general information about the animal in this section. You might want to have more than one breed of the same species, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different breeds of the same species is quite easy. Let's say you want to have two kinds of cows for example. The Name: field is Cow for both, but in Notes: field, enter Dairy for one, and Beast of Burden for the o"
                        "ther. Then adjust the other parameters as you wish. Even though the name is the same, the animal is saved uniquely.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxAnimalDescription.setTitle(QCoreApplication.translate("LaAnimalManagerBase", u"Animal Description", None))
        self.label.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Name:", None))
#if QT_CONFIG(whatsthis)
        self.leName.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the animal you are defining in this field. You do not need a unique name. You can have, for example, 10 animals defined, all named \"Sheep\". Landuse Analyst uses a special method of saving the animals to eliminate the issue of duplicate filenames.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Notes:", None))
#if QT_CONFIG(whatsthis)
        self.leDescription.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because Landuse Analyst allows more than one type of animal to be defined, the Notes: field allows you to give a brief description of the the animal. For example, you may have two \"Sheep\" defined, and the Notes: fields could contain \"For Slaughter\" and \"Wool Producers\" to distinguish between them.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Food Value", None))
#if QT_CONFIG(tooltip)
        self.sbMeatFoodValue.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of live weight usable as meat</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbMeatFoodValue.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The production targets for animals are in Kg of meat, so to be compatible with animal numbers, you must know the percentage of the animal's live weight that is usable for food. You can also take into account here the efficiency of the butchering technique that the population used. In other words, if you believe they were wasteful, this is where you would make an adjustment to integrate that.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbMeatFoodValue.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" cal", None))
        self.sbMeatFoodValue.setPrefix("")
        self.label_9.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Usable Meat", None))
#if QT_CONFIG(tooltip)
        self.sbUsableMeatPercent.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of live weight usable as meat</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbUsableMeatPercent.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The production targets for animals are in Kg of meat, so to be compatible with animal numbers, you must know the percentage of the animal's live weight that is usable for food. You can also take into account here the efficiency of the butchering technique that the population used. In other words, if you believe they were wasteful, this is where you would make an adjustment to integrate that.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbUsableMeatPercent.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" %", None))
        self.sbUsableMeatPercent.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Kill Weight", None))
#if QT_CONFIG(tooltip)
        self.sbKillWeight.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbKillWeight.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but Landuse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbKillWeight.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Kg", None))
        self.sbKillWeight.setPrefix("")
        self.label_16.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Weaning Weight", None))
#if QT_CONFIG(tooltip)
        self.sbWeaningWeight.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weeks from birth to weaning</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbWeaningWeight.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The age of the babies, in weeks, at which they stop feeding from their mother. It is assumed by Landuse Analyst that mothers will become pregnant after one estrous cycle following weaning.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbWeaningWeight.setProperty("text", QCoreApplication.translate("LaAnimalManagerBase", u"80 Kg", None))
        self.sbWeaningWeight.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Kg", None))
        self.sbWeaningWeight.setPrefix("")
        self.label_11.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Grow Time", None))
#if QT_CONFIG(tooltip)
        self.sbGrowTime.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time from birth to slaughter weight</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbGrowTime.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grow time, or the length of time from birth to slaughter weight, is quite important for estimating the herd size. The longer it takes an animal to reach slaughter weight from birth, the higher the number of animals alive at any given time.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbGrowTime.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Weeks", None))
        self.sbGrowTime.setPrefix("")
        self.label_12.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Death Rate", None))
#if QT_CONFIG(tooltip)
        self.sbDeathRate.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of babies that do not survive to slaughter age.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbDeathRate.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst accommodates for birthing deaths only. If an animal survives to weaning age but dies before slaughter, it is not modelled at this time. However, you can adjust the death rate setting to indicate the average survival rate of births. This is important for determining herd size, as it affects the number of mothers needed to sustain the production levels required by the settlement.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbDeathRate.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" %", None))
        self.sbDeathRate.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Sexual Maturity", None))
#if QT_CONFIG(tooltip)
        self.sbSexualMaturity.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Age of females when they become sexually mature.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbSexualMaturity.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simply set the age, in months, at which the females become sexually mature, and are able to reliably breed.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbSexualMaturity.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Mths", None))
        self.sbSexualMaturity.setPrefix("")
        self.label_17.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Adult Weight", None))
#if QT_CONFIG(tooltip)
        self.sbAdultWeight.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbAdultWeight.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but Landuse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbAdultWeight.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Kg", None))
        self.sbAdultWeight.setPrefix("")
        self.label_18.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Females:Males", None))
#if QT_CONFIG(tooltip)
        self.sbFemalesToMales.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbFemalesToMales.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but Landuse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbFemalesToMales.setSuffix("")
        self.sbFemalesToMales.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Breeding Life", None))
#if QT_CONFIG(tooltip)
        self.sbBreedingLife.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of years females are useful for breeding</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbBreedingLife.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to determine the number of female offspring that need to be retained to sustain the adult female population (breeding herd) it is necessary to know how long a female of the species can be expected to breed reliably. This is <span style=\" font-weight:600;\">not</span> life expectancy.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbBreedingLife.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Years", None))
        self.sbBreedingLife.setPrefix("")
        self.label_19.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Conception %", None))
#if QT_CONFIG(tooltip)
        self.sbConceptionEfficiency.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbConceptionEfficiency.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but Landuse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbConceptionEfficiency.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u"  %", None))
        self.sbConceptionEfficiency.setPrefix("")
        self.label_5.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Young / birth", None))
#if QT_CONFIG(tooltip)
        self.sbYoungPerBirth.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of young born per birth (average)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbYoungPerBirth.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the number of babies born to a mother. This is total number, not surviving numbers. To account for deaths between birth and weaning, adjust the Death Rate.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbYoungPerBirth.setSuffix("")
        self.label_6.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Weaning Age", None))
#if QT_CONFIG(tooltip)
        self.sbWeaningAge.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weeks from birth to weaning</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbWeaningAge.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The age of the babies, in weeks, at which they stop feeding from their mother. It is assumed by Landuse Analyst that mothers will become pregnant after one estrous cycle following weaning.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbWeaningAge.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" days", None))
        self.sbWeaningAge.setPrefix("")
        self.label_7.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Gestation Time", None))
#if QT_CONFIG(tooltip)
        self.sbGestationTime.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gestation time in days</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbGestationTime.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days for gestation. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbGestationTime.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" days", None))
        self.sbGestationTime.setPrefix("")
        self.label_8.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Estrous Cycle", None))
#if QT_CONFIG(tooltip)
        self.sbEstrousCycleTime.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in their estrous cycle</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbEstrousCycleTime.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in the animal's estrous cycle.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbEstrousCycleTime.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" days", None))
        self.sbEstrousCycleTime.setPrefix("")
        self.label_21.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Lactation Time", None))
#if QT_CONFIG(tooltip)
        self.sbLactationTime.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in their estrous cycle</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbLactationTime.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in the animal's estrous cycle.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbLactationTime.setProperty("text", QCoreApplication.translate("LaAnimalManagerBase", u"210 days", None))
        self.sbLactationTime.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" days", None))
        self.sbLactationTime.setPrefix("")
        self.grpProfiles.setTitle(QCoreApplication.translate("LaAnimalManagerBase", u"Available Animal Profiles", None))
        ___qtablewidgetitem = self.tblAnimals.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaAnimalManagerBase", u"FileName", None));
        ___qtablewidgetitem1 = self.tblAnimals.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Name", None));
#if QT_CONFIG(tooltip)
        self.tblAnimals.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select an animal here to see and/or edit it's properties below.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblAnimals.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable Landuse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for these specifics. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals with the same name. Let's say you want to have two parameters set up for Cows as an example. The Name: field is Cow for bot"
                        "h, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, Landuse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.toolCopy.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected animal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolCopy.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new animal that is similar to one already defined, you can clone this animal to save time. All of the settings of the animal you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the animal you are cloning was).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note that the parameters are <span style=\" font-weight:600;\">not</span> transferred.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolCopy.setText(QCoreApplication.translate("LaAnimalManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolNew.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new animal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toolNew.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Animal Manager, you are just editing the animal currently selected. To create a new animal, you must click on the New button.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toolNew.setText(QCoreApplication.translate("LaAnimalManagerBase", u"...", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected animal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("LaAnimalManagerBase", u"...", None))
        self.lblAnimalPix.setText(QCoreApplication.translate("LaAnimalManagerBase", u"No Graphic\n"
"Selected", None))
        self.pbnAnimalPic.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Set Graphic", None))
        self.pbnImport.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Import", None))
        self.pbnExport.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Export", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxFeedRequirements.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst breaks down the calorie requirements for the animal being modelled into three categories: Gestating, Lactating, and Juvenile. Enter the average calories required per day for an animal in each of these categories.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxFeedRequirements.setTitle(QCoreApplication.translate("LaAnimalManagerBase", u"Daily Feed Requirements", None))
        self.label_13.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Select Units", None))
        self.cbFeedEnergyType.setItemText(0, QCoreApplication.translate("LaAnimalManagerBase", u"MCalories", None))
        self.cbFeedEnergyType.setItemText(1, QCoreApplication.translate("LaAnimalManagerBase", u"TDN", None))

        self.labelFeedRequirements2.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Pregnant Female", None))
#if QT_CONFIG(tooltip)
        self.sbEnergyForPregnant.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult female</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbEnergyForPregnant.setSuffix("")
#if QT_CONFIG(tooltip)
        self.labelFeedRequirements3.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult male</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFeedRequirements3.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Lactating Female", None))
#if QT_CONFIG(tooltip)
        self.sbEnergyForLactating.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a female that is lactating.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbEnergyForLactating.setSuffix("")
#if QT_CONFIG(tooltip)
        self.labelFeedRequirements3_2.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult male</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFeedRequirements3_2.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Maintenance (Adult)", None))
#if QT_CONFIG(tooltip)
        self.sbEnergyForMaintenance.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a female that is lactating.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sbEnergyForMaintenance.setSuffix("")
#if QT_CONFIG(tooltip)
        self.labelFeedRequirements4.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for a juvenile</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelFeedRequirements4.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Juvenile", None))
#if QT_CONFIG(tooltip)
        self.sbEnergyForJuvenilePerKg.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a juvenile.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbEnergyForJuvenilePerKg.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a juvenile. Landuse Analyst considers a Juvenile to be an animal after weaning and before slaughter.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbEnergyForJuvenilePerKg.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" per Kg", None))
#if QT_CONFIG(whatsthis)
        self.groupBoxByProducts.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All of the settings in Reproduction define an animal's reproductive characteristics. Landuse Analyst calculates the time between births by adding the gestation time, weaning age, and one estrous cycle.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBoxByProducts.setTitle(QCoreApplication.translate("LaAnimalManagerBase", u"By-Products", None))
        self.checkBoxMilk.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Milk", None))
#if QT_CONFIG(tooltip)
        self.sbMilk.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Age of females when they become sexually mature.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbMilk.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simply set the age, in months, at which the females become sexually mature, and are able to reliably breed.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbMilk.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" g", None))
        self.sbMilk.setPrefix("")
        self.label_15.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Food Value", None))
#if QT_CONFIG(tooltip)
        self.sbMilkFoodValue.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of years females are useful for breeding</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbMilkFoodValue.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to determine the number of female offspring that need to be retained to sustain the adult female population (breeding herd) it is necessary to know how long a female of the species can be expected to breed reliably. This is <span style=\" font-weight:600;\">not</span> life expectancy.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbMilkFoodValue.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Cals/Kg", None))
        self.sbMilkFoodValue.setPrefix("")
        self.checkBoxFleece.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Fleece", None))
#if QT_CONFIG(tooltip)
        self.sbFleeceWeight.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of young born per birth (average)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sbFleeceWeight.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the number of babies born to a mother. This is total number, not surviving numbers. To account for deaths between birth and weaning, adjust the Death Rate.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sbFleeceWeight.setSuffix(QCoreApplication.translate("LaAnimalManagerBase", u" Kg/year", None))
#if QT_CONFIG(tooltip)
        self.pbnApply.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pbnApply.setWhatsThis(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define an animal, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as Landuse Analyst has a special way of saving animals to allow for duplicate Animal names. It is helpful, however, to utilize the Notes field to distinguish between same-named animal definitions.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pbnApply.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.pbnClose.setToolTip(QCoreApplication.translate("LaAnimalManagerBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbnClose.setText(QCoreApplication.translate("LaAnimalManagerBase", u"Close", None))
    # retranslateUi

