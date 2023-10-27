# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laassemblageconversionbase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)
import resources_rc

class Ui_LaAssemblageConversionBase(object):
    def setupUi(self, LaAssemblageConversionBase):
        if not LaAssemblageConversionBase.objectName():
            LaAssemblageConversionBase.setObjectName(u"LaAssemblageConversionBase")
        LaAssemblageConversionBase.resize(529, 393)
        icon = QIcon(u":/la_icon_small.png")
        LaAssemblageConversionBase.setWindowIcon(icon)
        self.gridLayout = QGridLayout(LaAssemblageConversionBase)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(LaAssemblageConversionBase)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.tblAnimals = QTableWidget(LaAssemblageConversionBase)
        if (self.tblAnimals.columnCount() < 5):
            self.tblAnimals.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblAnimals.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblAnimals.setObjectName(u"tblAnimals")
        self.tblAnimals.setAlternatingRowColors(True)
        self.tblAnimals.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAnimals.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblAnimals.setShowGrid(False)

        self.gridLayout.addWidget(self.tblAnimals, 1, 0, 1, 5)

        self.frame = QFrame(LaAssemblageConversionBase)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.frame)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.rbManual = QRadioButton(self.frame)
        self.rbManual.setObjectName(u"rbManual")

        self.gridLayout2.addWidget(self.rbManual, 0, 0, 1, 1)

        self.leAnimal = QLineEdit(self.frame)
        self.leAnimal.setObjectName(u"leAnimal")

        self.gridLayout2.addWidget(self.leAnimal, 0, 1, 1, 1)

        self.sbUsableMeat = QSpinBox(self.frame)
        self.sbUsableMeat.setObjectName(u"sbUsableMeat")

        self.gridLayout2.addWidget(self.sbUsableMeat, 0, 2, 1, 1)

        self.sbCalsPerKg = QSpinBox(self.frame)
        self.sbCalsPerKg.setObjectName(u"sbCalsPerKg")

        self.gridLayout2.addWidget(self.sbCalsPerKg, 0, 3, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout2.addWidget(self.line, 1, 0, 1, 4)

        self.rbAuto = QRadioButton(self.frame)
        self.rbAuto.setObjectName(u"rbAuto")

        self.gridLayout2.addWidget(self.rbAuto, 2, 0, 1, 1)

        self.cboAnimal = QComboBox(self.frame)
        self.cboAnimal.setObjectName(u"cboAnimal")

        self.gridLayout2.addWidget(self.cboAnimal, 2, 1, 1, 3)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout2.addWidget(self.line_4, 0, 4, 3, 1)


        self.hboxLayout.addLayout(self.gridLayout2)

        self.gridLayout3 = QGridLayout()
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.dsbNumber = QDoubleSpinBox(self.frame)
        self.dsbNumber.setObjectName(u"dsbNumber")

        self.gridLayout3.addWidget(self.dsbNumber, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout3.addWidget(self.line_2, 0, 1, 2, 1)

        self.pbnInsert = QPushButton(self.frame)
        self.pbnInsert.setObjectName(u"pbnInsert")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbnInsert.sizePolicy().hasHeightForWidth())
        self.pbnInsert.setSizePolicy(sizePolicy)
        self.pbnInsert.setMinimumSize(QSize(50, 0))
        self.pbnInsert.setMaximumSize(QSize(60, 16777215))

        self.gridLayout3.addWidget(self.pbnInsert, 0, 2, 2, 1)

        self.cboNumber = QComboBox(self.frame)
        self.cboNumber.addItem("")
        self.cboNumber.addItem("")
        self.cboNumber.addItem("")
        self.cboNumber.setObjectName(u"cboNumber")

        self.gridLayout3.addWidget(self.cboNumber, 1, 0, 1, 1)


        self.hboxLayout.addLayout(self.gridLayout3)


        self.gridLayout1.addLayout(self.hboxLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 5)

        self.pbnCalculate = QPushButton(LaAssemblageConversionBase)
        self.pbnCalculate.setObjectName(u"pbnCalculate")

        self.gridLayout.addWidget(self.pbnCalculate, 3, 0, 1, 1)

        self.pbnSave = QPushButton(LaAssemblageConversionBase)
        self.pbnSave.setObjectName(u"pbnSave")

        self.gridLayout.addWidget(self.pbnSave, 3, 1, 1, 1)

        self.pbnClearTable = QPushButton(LaAssemblageConversionBase)
        self.pbnClearTable.setObjectName(u"pbnClearTable")

        self.gridLayout.addWidget(self.pbnClearTable, 3, 2, 1, 1)

        self.spacerItem = QSpacerItem(121, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacerItem, 3, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(LaAssemblageConversionBase)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.NoButton|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 4, 1, 1)


        self.retranslateUi(LaAssemblageConversionBase)
        self.buttonBox.accepted.connect(LaAssemblageConversionBase.accept)
        self.buttonBox.rejected.connect(LaAssemblageConversionBase.reject)

        QMetaObject.connectSlotsByName(LaAssemblageConversionBase)
    # setupUi

    def retranslateUi(self, LaAssemblageConversionBase):
        LaAssemblageConversionBase.setWindowTitle(QCoreApplication.translate("LaAssemblageConversionBase", u"Assemblage Conversion Utility", None))
        self.label.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Enter the NISP and Kg usable meat for each animal in the model", None))
        ___qtablewidgetitem = self.tblAnimals.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Animal", None));
        ___qtablewidgetitem1 = self.tblAnimals.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Number", None));
        ___qtablewidgetitem2 = self.tblAnimals.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Usable Meat", None));
        ___qtablewidgetitem3 = self.tblAnimals.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Cals/Kg", None));
        ___qtablewidgetitem4 = self.tblAnimals.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"% of Diet", None));
#if QT_CONFIG(tooltip)
        self.tblAnimals.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tblAnimals.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.rbManual.setText("")
#if QT_CONFIG(tooltip)
        self.leAnimal.setToolTip(QCoreApplication.translate("LaAssemblageConversionBase", u"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animal Name</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rbAuto.setText("")
        self.pbnInsert.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Insert", None))
        self.cboNumber.setItemText(0, QCoreApplication.translate("LaAssemblageConversionBase", u"NISP", None))
        self.cboNumber.setItemText(1, QCoreApplication.translate("LaAssemblageConversionBase", u"MNI", None))
        self.cboNumber.setItemText(2, QCoreApplication.translate("LaAssemblageConversionBase", u"Kg Bone", None))

        self.pbnCalculate.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Calculate", None))
        self.pbnSave.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Save", None))
        self.pbnClearTable.setText(QCoreApplication.translate("LaAssemblageConversionBase", u"Clear Table", None))
    # retranslateUi

