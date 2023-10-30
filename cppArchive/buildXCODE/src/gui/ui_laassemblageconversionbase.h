/********************************************************************************
** Form generated from reading ui file 'laassemblageconversionbase.ui'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LAASSEMBLAGECONVERSIONBASE_H
#define UI_LAASSEMBLAGECONVERSIONBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTableWidget>

QT_BEGIN_NAMESPACE

class Ui_LaAssemblageConversionBase
{
public:
    QGridLayout *gridLayout;
    QLabel *label;
    QTableWidget *tblAnimals;
    QFrame *frame;
    QGridLayout *gridLayout1;
    QHBoxLayout *hboxLayout;
    QGridLayout *gridLayout2;
    QRadioButton *rbManual;
    QLineEdit *leAnimal;
    QSpinBox *sbUsableMeat;
    QSpinBox *sbCalsPerKg;
    QFrame *line;
    QRadioButton *rbAuto;
    QComboBox *cboAnimal;
    QFrame *line_4;
    QGridLayout *gridLayout3;
    QDoubleSpinBox *dsbNumber;
    QFrame *line_2;
    QPushButton *pbnInsert;
    QComboBox *cboNumber;
    QPushButton *pbnCalculate;
    QPushButton *pbnSave;
    QPushButton *pbnClearTable;
    QSpacerItem *spacerItem;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *LaAssemblageConversionBase)
    {
    if (LaAssemblageConversionBase->objectName().isEmpty())
        LaAssemblageConversionBase->setObjectName(QString::fromUtf8("LaAssemblageConversionBase"));
    LaAssemblageConversionBase->resize(529, 393);
    const QIcon icon = QIcon(QString::fromUtf8(":/la_icon_small.png"));
    LaAssemblageConversionBase->setWindowIcon(icon);
    gridLayout = new QGridLayout(LaAssemblageConversionBase);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    label = new QLabel(LaAssemblageConversionBase);
    label->setObjectName(QString::fromUtf8("label"));

    gridLayout->addWidget(label, 0, 0, 1, 4);

    tblAnimals = new QTableWidget(LaAssemblageConversionBase);
    if (tblAnimals->columnCount() < 5)
        tblAnimals->setColumnCount(5);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(1, __colItem1);
    QTableWidgetItem *__colItem2 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(2, __colItem2);
    QTableWidgetItem *__colItem3 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(3, __colItem3);
    QTableWidgetItem *__colItem4 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(4, __colItem4);
    tblAnimals->setObjectName(QString::fromUtf8("tblAnimals"));
    tblAnimals->setAlternatingRowColors(true);
    tblAnimals->setSelectionMode(QAbstractItemView::SingleSelection);
    tblAnimals->setSelectionBehavior(QAbstractItemView::SelectRows);
    tblAnimals->setShowGrid(false);

    gridLayout->addWidget(tblAnimals, 1, 0, 1, 5);

    frame = new QFrame(LaAssemblageConversionBase);
    frame->setObjectName(QString::fromUtf8("frame"));
    frame->setMinimumSize(QSize(400, 70));
    frame->setFrameShape(QFrame::StyledPanel);
    frame->setFrameShadow(QFrame::Raised);
    gridLayout1 = new QGridLayout(frame);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    hboxLayout = new QHBoxLayout();
    hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
    gridLayout2 = new QGridLayout();
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    rbManual = new QRadioButton(frame);
    rbManual->setObjectName(QString::fromUtf8("rbManual"));

    gridLayout2->addWidget(rbManual, 0, 0, 1, 1);

    leAnimal = new QLineEdit(frame);
    leAnimal->setObjectName(QString::fromUtf8("leAnimal"));

    gridLayout2->addWidget(leAnimal, 0, 1, 1, 1);

    sbUsableMeat = new QSpinBox(frame);
    sbUsableMeat->setObjectName(QString::fromUtf8("sbUsableMeat"));

    gridLayout2->addWidget(sbUsableMeat, 0, 2, 1, 1);

    sbCalsPerKg = new QSpinBox(frame);
    sbCalsPerKg->setObjectName(QString::fromUtf8("sbCalsPerKg"));

    gridLayout2->addWidget(sbCalsPerKg, 0, 3, 1, 1);

    line = new QFrame(frame);
    line->setObjectName(QString::fromUtf8("line"));
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    gridLayout2->addWidget(line, 1, 0, 1, 4);

    rbAuto = new QRadioButton(frame);
    rbAuto->setObjectName(QString::fromUtf8("rbAuto"));

    gridLayout2->addWidget(rbAuto, 2, 0, 1, 1);

    cboAnimal = new QComboBox(frame);
    cboAnimal->setObjectName(QString::fromUtf8("cboAnimal"));

    gridLayout2->addWidget(cboAnimal, 2, 1, 1, 3);

    line_4 = new QFrame(frame);
    line_4->setObjectName(QString::fromUtf8("line_4"));
    line_4->setFrameShape(QFrame::VLine);
    line_4->setFrameShadow(QFrame::Sunken);

    gridLayout2->addWidget(line_4, 0, 4, 3, 1);


    hboxLayout->addLayout(gridLayout2);

    gridLayout3 = new QGridLayout();
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    dsbNumber = new QDoubleSpinBox(frame);
    dsbNumber->setObjectName(QString::fromUtf8("dsbNumber"));

    gridLayout3->addWidget(dsbNumber, 0, 0, 1, 1);

    line_2 = new QFrame(frame);
    line_2->setObjectName(QString::fromUtf8("line_2"));
    line_2->setLineWidth(3);
    line_2->setFrameShape(QFrame::VLine);
    line_2->setFrameShadow(QFrame::Sunken);

    gridLayout3->addWidget(line_2, 0, 1, 2, 1);

    pbnInsert = new QPushButton(frame);
    pbnInsert->setObjectName(QString::fromUtf8("pbnInsert"));
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Preferred);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(pbnInsert->sizePolicy().hasHeightForWidth());
    pbnInsert->setSizePolicy(sizePolicy);
    pbnInsert->setMinimumSize(QSize(50, 0));
    pbnInsert->setMaximumSize(QSize(60, 16777215));

    gridLayout3->addWidget(pbnInsert, 0, 2, 2, 1);

    cboNumber = new QComboBox(frame);
    cboNumber->setObjectName(QString::fromUtf8("cboNumber"));

    gridLayout3->addWidget(cboNumber, 1, 0, 1, 1);


    hboxLayout->addLayout(gridLayout3);


    gridLayout1->addLayout(hboxLayout, 0, 0, 1, 1);


    gridLayout->addWidget(frame, 2, 0, 1, 5);

    pbnCalculate = new QPushButton(LaAssemblageConversionBase);
    pbnCalculate->setObjectName(QString::fromUtf8("pbnCalculate"));

    gridLayout->addWidget(pbnCalculate, 3, 0, 1, 1);

    pbnSave = new QPushButton(LaAssemblageConversionBase);
    pbnSave->setObjectName(QString::fromUtf8("pbnSave"));

    gridLayout->addWidget(pbnSave, 3, 1, 1, 1);

    pbnClearTable = new QPushButton(LaAssemblageConversionBase);
    pbnClearTable->setObjectName(QString::fromUtf8("pbnClearTable"));

    gridLayout->addWidget(pbnClearTable, 3, 2, 1, 1);

    spacerItem = new QSpacerItem(121, 27, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout->addItem(spacerItem, 3, 3, 1, 1);

    buttonBox = new QDialogButtonBox(LaAssemblageConversionBase);
    buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
    buttonBox->setOrientation(Qt::Horizontal);
    buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::NoButton|QDialogButtonBox::Ok);

    gridLayout->addWidget(buttonBox, 3, 4, 1, 1);


    retranslateUi(LaAssemblageConversionBase);
    QObject::connect(buttonBox, SIGNAL(accepted()), LaAssemblageConversionBase, SLOT(accept()));
    QObject::connect(buttonBox, SIGNAL(rejected()), LaAssemblageConversionBase, SLOT(reject()));

    QMetaObject::connectSlotsByName(LaAssemblageConversionBase);
    } // setupUi

    void retranslateUi(QDialog *LaAssemblageConversionBase)
    {
    LaAssemblageConversionBase->setWindowTitle(QApplication::translate("LaAssemblageConversionBase", "Assemblage Conversion Utility", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaAssemblageConversionBase", "Enter the NISP and Kg usable meat for each animal in the model", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(0)->setText(QApplication::translate("LaAssemblageConversionBase", "Animal", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(1)->setText(QApplication::translate("LaAssemblageConversionBase", "Number", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(2)->setText(QApplication::translate("LaAssemblageConversionBase", "Usable Meat", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(3)->setText(QApplication::translate("LaAssemblageConversionBase", "Cals/Kg", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(4)->setText(QApplication::translate("LaAssemblageConversionBase", "% of Diet", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblAnimals->setToolTip(QString());
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblAnimals->setWhatsThis(QString());
#endif // QT_NO_WHATSTHIS

    rbManual->setText(QString());

#ifndef QT_NO_TOOLTIP
    leAnimal->setToolTip(QApplication::translate("LaAssemblageConversionBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animal Name</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    rbAuto->setText(QString());
    pbnInsert->setText(QApplication::translate("LaAssemblageConversionBase", "Insert", 0, QApplication::UnicodeUTF8));
    cboNumber->clear();
    cboNumber->insertItems(0, QStringList()
     << QApplication::translate("LaAssemblageConversionBase", "NISP", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaAssemblageConversionBase", "MNI", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaAssemblageConversionBase", "Kg Bone", 0, QApplication::UnicodeUTF8)
    );
    pbnCalculate->setText(QApplication::translate("LaAssemblageConversionBase", "Calculate", 0, QApplication::UnicodeUTF8));
    pbnSave->setText(QApplication::translate("LaAssemblageConversionBase", "Save", 0, QApplication::UnicodeUTF8));
    pbnClearTable->setText(QApplication::translate("LaAssemblageConversionBase", "Clear Table", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaAssemblageConversionBase);
    } // retranslateUi

};

namespace Ui {
    class LaAssemblageConversionBase: public Ui_LaAssemblageConversionBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LAASSEMBLAGECONVERSIONBASE_H
