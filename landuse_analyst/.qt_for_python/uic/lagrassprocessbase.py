# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/arkygeek/dev/QGisPlugins/landuseanalyst/landuse_analyst/src/ui/lagrassprocessbase.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LaGrassProcessBase(object):
    def setupUi(self, LaGrassProcessBase):
        LaGrassProcessBase.setObjectName("LaGrassProcessBase")
        LaGrassProcessBase.resize(593, 763)
        LaGrassProcessBase.setMinimumSize(QtCore.QSize(0, 400))
        icon = QtGui.QIcon()
        icon.addFile(":/la_icon_small.png")
        LaGrassProcessBase.setWindowIcon(icon)
        self.gridlayout = QtWidgets.QGridLayout(LaGrassProcessBase)
        self.gridlayout.setObjectName("gridlayout")
        self.grpPreview = QtWidgets.QGroupBox(LaGrassProcessBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpPreview.sizePolicy().hasHeightForWidth())
        self.grpPreview.setSizePolicy(sizePolicy)
        self.grpPreview.setObjectName("grpPreview")
        self.gridlayout1 = QtWidgets.QGridLayout(self.grpPreview)
        self.gridlayout1.setObjectName("gridlayout1")
        self.lblPreview = QtWidgets.QLabel(self.grpPreview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPreview.sizePolicy().hasHeightForWidth())
        self.lblPreview.setSizePolicy(sizePolicy)
        self.lblPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPreview.setObjectName("lblPreview")
        self.gridlayout1.addWidget(self.lblPreview, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.grpPreview, 0, 0, 3, 4)
        self.grpCurrentTarget = QtWidgets.QGroupBox(LaGrassProcessBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpCurrentTarget.sizePolicy().hasHeightForWidth())
        self.grpCurrentTarget.setSizePolicy(sizePolicy)
        self.grpCurrentTarget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.grpCurrentTarget.setObjectName("grpCurrentTarget")
        self.gridlayout2 = QtWidgets.QGridLayout(self.grpCurrentTarget)
        self.gridlayout2.setObjectName("gridlayout2")
        self.lblGraphic = QtWidgets.QLabel(self.grpCurrentTarget)
        self.lblGraphic.setMinimumSize(QtCore.QSize(100, 100))
        self.lblGraphic.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.lblGraphic.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGraphic.setObjectName("lblGraphic")
        self.gridlayout2.addWidget(self.lblGraphic, 0, 0, 1, 1)
        self.lblCurrentArea = QtWidgets.QLabel(self.grpCurrentTarget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurrentArea.sizePolicy().hasHeightForWidth())
        self.lblCurrentArea.setSizePolicy(sizePolicy)
        self.lblCurrentArea.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentArea.setObjectName("lblCurrentArea")
        self.gridlayout2.addWidget(self.lblCurrentArea, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.grpCurrentTarget, 0, 4, 1, 2)
        self.grpProgress = QtWidgets.QGroupBox(LaGrassProcessBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpProgress.sizePolicy().hasHeightForWidth())
        self.grpProgress.setSizePolicy(sizePolicy)
        self.grpProgress.setMinimumSize(QtCore.QSize(0, 0))
        self.grpProgress.setMaximumSize(QtCore.QSize(200, 16777215))
        self.grpProgress.setObjectName("grpProgress")
        self.gridlayout3 = QtWidgets.QGridLayout(self.grpProgress)
        self.gridlayout3.setObjectName("gridlayout3")
        self.label = QtWidgets.QLabel(self.grpProgress)
        self.label.setMinimumSize(QtCore.QSize(0, 16))
        self.label.setObjectName("label")
        self.gridlayout3.addWidget(self.label, 0, 0, 1, 1)
        self.pbarBusy = QtWidgets.QProgressBar(self.grpProgress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbarBusy.sizePolicy().hasHeightForWidth())
        self.pbarBusy.setSizePolicy(sizePolicy)
        self.pbarBusy.setMinimumSize(QtCore.QSize(0, 19))
        self.pbarBusy.setMaximumSize(QtCore.QSize(16777215, 1677772))
        self.pbarBusy.setProperty("value", 0)
        self.pbarBusy.setTextVisible(False)
        self.pbarBusy.setOrientation(QtCore.Qt.Horizontal)
        self.pbarBusy.setFormat("")
        self.pbarBusy.setObjectName("pbarBusy")
        self.gridlayout3.addWidget(self.pbarBusy, 1, 0, 1, 1)
        self.lblAreaTarget = QtWidgets.QLabel(self.grpProgress)
        self.lblAreaTarget.setMinimumSize(QtCore.QSize(0, 16))
        self.lblAreaTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAreaTarget.setObjectName("lblAreaTarget")
        self.gridlayout3.addWidget(self.lblAreaTarget, 2, 0, 1, 1)
        self.pbarTarget = QtWidgets.QProgressBar(self.grpProgress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbarTarget.sizePolicy().hasHeightForWidth())
        self.pbarTarget.setSizePolicy(sizePolicy)
        self.pbarTarget.setMinimumSize(QtCore.QSize(45, 19))
        self.pbarTarget.setProperty("value", 24)
        self.pbarTarget.setAlignment(QtCore.Qt.AlignCenter)
        self.pbarTarget.setTextVisible(False)
        self.pbarTarget.setOrientation(QtCore.Qt.Horizontal)
        self.pbarTarget.setFormat("")
        self.pbarTarget.setObjectName("pbarTarget")
        self.gridlayout3.addWidget(self.pbarTarget, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.grpProgress)
        self.label_6.setMinimumSize(QtCore.QSize(0, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridlayout3.addWidget(self.label_6, 4, 0, 1, 1)
        self.pbarOverall = QtWidgets.QProgressBar(self.grpProgress)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbarOverall.sizePolicy().hasHeightForWidth())
        self.pbarOverall.setSizePolicy(sizePolicy)
        self.pbarOverall.setMinimumSize(QtCore.QSize(45, 19))
        self.pbarOverall.setProperty("value", 24)
        self.pbarOverall.setTextVisible(False)
        self.pbarOverall.setOrientation(QtCore.Qt.Horizontal)
        self.pbarOverall.setFormat("")
        self.pbarOverall.setObjectName("pbarOverall")
        self.gridlayout3.addWidget(self.pbarOverall, 5, 0, 1, 1)
        self.gridlayout.addWidget(self.grpProgress, 1, 4, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(LaGrassProcessBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridlayout4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridlayout4.setObjectName("gridlayout4")
        self.tbGrass = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbGrass.sizePolicy().hasHeightForWidth())
        self.tbGrass.setSizePolicy(sizePolicy)
        self.tbGrass.setObjectName("tbGrass")
        self.gridlayout4.addWidget(self.tbGrass, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.groupBox_2, 3, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 4, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(LaGrassProcessBase)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 5, 0, 1, 6)
        self.cbPeriod = QtWidgets.QComboBox(LaGrassProcessBase)
        self.cbPeriod.setObjectName("cbPeriod")
        self.cbPeriod.addItem("")
        self.cbPeriod.addItem("")
        self.cbPeriod.addItem("")
        self.gridlayout.addWidget(self.cbPeriod, 6, 0, 1, 1)
        self.cbPopulation = QtWidgets.QComboBox(LaGrassProcessBase)
        self.cbPopulation.setObjectName("cbPopulation")
        self.cbPopulation.addItem("")
        self.cbPopulation.addItem("")
        self.gridlayout.addWidget(self.cbPopulation, 6, 1, 1, 1)
        self.cbDietRatio = QtWidgets.QComboBox(LaGrassProcessBase)
        self.cbDietRatio.setObjectName("cbDietRatio")
        self.cbDietRatio.addItem("")
        self.cbDietRatio.addItem("")
        self.cbDietRatio.addItem("")
        self.gridlayout.addWidget(self.cbDietRatio, 6, 2, 1, 1)
        self.cbDairy = QtWidgets.QComboBox(LaGrassProcessBase)
        self.cbDairy.setObjectName("cbDairy")
        self.cbDairy.addItem("")
        self.cbDairy.addItem("")
        self.cbDairy.addItem("")
        self.gridlayout.addWidget(self.cbDairy, 6, 3, 1, 2)
        self.cbAnimalsFed = QtWidgets.QComboBox(LaGrassProcessBase)
        self.cbAnimalsFed.setObjectName("cbAnimalsFed")
        self.cbAnimalsFed.addItem("")
        self.cbAnimalsFed.addItem("")
        self.gridlayout.addWidget(self.cbAnimalsFed, 6, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(LaGrassProcessBase)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 7, 0, 1, 2)
        self.leOtherText = QtWidgets.QLineEdit(LaGrassProcessBase)
        self.leOtherText.setObjectName("leOtherText")
        self.gridlayout.addWidget(self.leOtherText, 7, 2, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(LaGrassProcessBase)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.NoButton|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 7, 5, 1, 1)

        self.retranslateUi(LaGrassProcessBase)
        self.buttonBox.accepted.connect(LaGrassProcessBase.accept) # type: ignore
        self.buttonBox.rejected.connect(LaGrassProcessBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LaGrassProcessBase)

    def retranslateUi(self, LaGrassProcessBase):
        _translate = QtCore.QCoreApplication.translate
        LaGrassProcessBase.setWindowTitle(_translate("LaGrassProcessBase", "Grass Processing"))
        self.grpPreview.setTitle(_translate("LaGrassProcessBase", "Preview"))
        self.lblPreview.setText(_translate("LaGrassProcessBase", "Preview feature not available in Beta Version"))
        self.grpCurrentTarget.setTitle(_translate("LaGrassProcessBase", "Current Target"))
        self.lblGraphic.setText(_translate("LaGrassProcessBase", "No Graphic"))
        self.lblCurrentArea.setText(_translate("LaGrassProcessBase", "123456"))
        self.grpProgress.setTitle(_translate("LaGrassProcessBase", "Progress"))
        self.label.setText(_translate("LaGrassProcessBase", "Current GRASS Command"))
        self.lblAreaTarget.setText(_translate("LaGrassProcessBase", "Target: 123456"))
        self.label_6.setText(_translate("LaGrassProcessBase", "Overall Progress"))
        self.groupBox_2.setTitle(_translate("LaGrassProcessBase", "Log"))
        self.tbGrass.setWhatsThis(_translate("LaGrassProcessBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for a crop simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>"))
        self.label_2.setText(_translate("LaGrassProcessBase", "Select the PERIOD, POPULATION, & DIET RATIO."))
        self.cbPeriod.setItemText(0, _translate("LaGrassProcessBase", "Chalcolithic"))
        self.cbPeriod.setItemText(1, _translate("LaGrassProcessBase", "EEB1"))
        self.cbPeriod.setItemText(2, _translate("LaGrassProcessBase", "LEB1"))
        self.cbPopulation.setItemText(0, _translate("LaGrassProcessBase", "Max"))
        self.cbPopulation.setItemText(1, _translate("LaGrassProcessBase", "Min"))
        self.cbDietRatio.setItemText(0, _translate("LaGrassProcessBase", "Meat 10%"))
        self.cbDietRatio.setItemText(1, _translate("LaGrassProcessBase", "Meat 20%"))
        self.cbDietRatio.setItemText(2, _translate("LaGrassProcessBase", "Meat 30%"))
        self.cbDairy.setItemText(0, _translate("LaGrassProcessBase", "Dairy 100%"))
        self.cbDairy.setItemText(1, _translate("LaGrassProcessBase", "Dairy 50%"))
        self.cbDairy.setItemText(2, _translate("LaGrassProcessBase", "No Dairy"))
        self.cbAnimalsFed.setItemText(0, _translate("LaGrassProcessBase", "Animals Fed"))
        self.cbAnimalsFed.setItemText(1, _translate("LaGrassProcessBase", "Animals Not Fed"))
        self.label_3.setText(_translate("LaGrassProcessBase", "Other text to include in filename:"))
import resources_rc