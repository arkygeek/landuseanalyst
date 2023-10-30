/********************************************************************************
** Form generated from reading ui file 'lagrassprocessbase.ui'
**
** Created: Thu Apr 9 10:03:09 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LAGRASSPROCESSBASE_H
#define UI_LAGRASSPROCESSBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextBrowser>

QT_BEGIN_NAMESPACE

class Ui_LaGrassProcessBase
{
public:
    QGridLayout *gridLayout;
    QGroupBox *grpPreview;
    QGridLayout *gridLayout1;
    QLabel *lblPreview;
    QGroupBox *grpCurrentTarget;
    QGridLayout *gridLayout2;
    QLabel *lblGraphic;
    QLabel *lblCurrentArea;
    QGroupBox *grpProgress;
    QGridLayout *gridLayout3;
    QLabel *label;
    QProgressBar *pbarBusy;
    QLabel *lblAreaTarget;
    QProgressBar *pbarTarget;
    QLabel *label_6;
    QProgressBar *pbarOverall;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout4;
    QTextBrowser *tbGrass;
    QSpacerItem *spacerItem;
    QLabel *label_2;
    QComboBox *cbPeriod;
    QComboBox *cbPopulation;
    QComboBox *cbDietRatio;
    QComboBox *cbDairy;
    QComboBox *cbAnimalsFed;
    QLabel *label_3;
    QLineEdit *leOtherText;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *LaGrassProcessBase)
    {
    if (LaGrassProcessBase->objectName().isEmpty())
        LaGrassProcessBase->setObjectName(QString::fromUtf8("LaGrassProcessBase"));
    LaGrassProcessBase->resize(593, 763);
    LaGrassProcessBase->setMinimumSize(QSize(0, 400));
    const QIcon icon = QIcon(QString::fromUtf8(":/la_icon_small.png"));
    LaGrassProcessBase->setWindowIcon(icon);
    gridLayout = new QGridLayout(LaGrassProcessBase);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    grpPreview = new QGroupBox(LaGrassProcessBase);
    grpPreview->setObjectName(QString::fromUtf8("grpPreview"));
    QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(grpPreview->sizePolicy().hasHeightForWidth());
    grpPreview->setSizePolicy(sizePolicy);
    gridLayout1 = new QGridLayout(grpPreview);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    lblPreview = new QLabel(grpPreview);
    lblPreview->setObjectName(QString::fromUtf8("lblPreview"));
    QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Preferred);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(lblPreview->sizePolicy().hasHeightForWidth());
    lblPreview->setSizePolicy(sizePolicy1);
    lblPreview->setAlignment(Qt::AlignCenter);

    gridLayout1->addWidget(lblPreview, 0, 0, 1, 1);


    gridLayout->addWidget(grpPreview, 0, 0, 3, 4);

    grpCurrentTarget = new QGroupBox(LaGrassProcessBase);
    grpCurrentTarget->setObjectName(QString::fromUtf8("grpCurrentTarget"));
    QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Preferred);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(grpCurrentTarget->sizePolicy().hasHeightForWidth());
    grpCurrentTarget->setSizePolicy(sizePolicy2);
    grpCurrentTarget->setMaximumSize(QSize(200, 16777215));
    gridLayout2 = new QGridLayout(grpCurrentTarget);
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    lblGraphic = new QLabel(grpCurrentTarget);
    lblGraphic->setObjectName(QString::fromUtf8("lblGraphic"));
    lblGraphic->setMinimumSize(QSize(100, 100));
    lblGraphic->setMaximumSize(QSize(1000000, 1000000));
    lblGraphic->setAlignment(Qt::AlignCenter);

    gridLayout2->addWidget(lblGraphic, 0, 0, 1, 1);

    lblCurrentArea = new QLabel(grpCurrentTarget);
    lblCurrentArea->setObjectName(QString::fromUtf8("lblCurrentArea"));
    sizePolicy1.setHeightForWidth(lblCurrentArea->sizePolicy().hasHeightForWidth());
    lblCurrentArea->setSizePolicy(sizePolicy1);
    lblCurrentArea->setAlignment(Qt::AlignCenter);

    gridLayout2->addWidget(lblCurrentArea, 1, 0, 1, 1);


    gridLayout->addWidget(grpCurrentTarget, 0, 4, 1, 2);

    grpProgress = new QGroupBox(LaGrassProcessBase);
    grpProgress->setObjectName(QString::fromUtf8("grpProgress"));
    sizePolicy2.setHeightForWidth(grpProgress->sizePolicy().hasHeightForWidth());
    grpProgress->setSizePolicy(sizePolicy2);
    grpProgress->setMinimumSize(QSize(0, 0));
    grpProgress->setMaximumSize(QSize(200, 16777215));
    gridLayout3 = new QGridLayout(grpProgress);
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    label = new QLabel(grpProgress);
    label->setObjectName(QString::fromUtf8("label"));
    label->setMinimumSize(QSize(0, 16));

    gridLayout3->addWidget(label, 0, 0, 1, 1);

    pbarBusy = new QProgressBar(grpProgress);
    pbarBusy->setObjectName(QString::fromUtf8("pbarBusy"));
    QSizePolicy sizePolicy3(QSizePolicy::Preferred, QSizePolicy::Preferred);
    sizePolicy3.setHorizontalStretch(0);
    sizePolicy3.setVerticalStretch(0);
    sizePolicy3.setHeightForWidth(pbarBusy->sizePolicy().hasHeightForWidth());
    pbarBusy->setSizePolicy(sizePolicy3);
    pbarBusy->setMinimumSize(QSize(0, 19));
    pbarBusy->setMaximumSize(QSize(16777215, 1677772));
    pbarBusy->setValue(0);
    pbarBusy->setTextVisible(false);
    pbarBusy->setOrientation(Qt::Horizontal);

    gridLayout3->addWidget(pbarBusy, 1, 0, 1, 1);

    lblAreaTarget = new QLabel(grpProgress);
    lblAreaTarget->setObjectName(QString::fromUtf8("lblAreaTarget"));
    lblAreaTarget->setMinimumSize(QSize(0, 16));
    lblAreaTarget->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(lblAreaTarget, 2, 0, 1, 1);

    pbarTarget = new QProgressBar(grpProgress);
    pbarTarget->setObjectName(QString::fromUtf8("pbarTarget"));
    sizePolicy3.setHeightForWidth(pbarTarget->sizePolicy().hasHeightForWidth());
    pbarTarget->setSizePolicy(sizePolicy3);
    pbarTarget->setMinimumSize(QSize(45, 19));
    pbarTarget->setValue(24);
    pbarTarget->setAlignment(Qt::AlignCenter);
    pbarTarget->setTextVisible(false);
    pbarTarget->setOrientation(Qt::Horizontal);

    gridLayout3->addWidget(pbarTarget, 3, 0, 1, 1);

    label_6 = new QLabel(grpProgress);
    label_6->setObjectName(QString::fromUtf8("label_6"));
    label_6->setMinimumSize(QSize(0, 16));
    label_6->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(label_6, 4, 0, 1, 1);

    pbarOverall = new QProgressBar(grpProgress);
    pbarOverall->setObjectName(QString::fromUtf8("pbarOverall"));
    sizePolicy3.setHeightForWidth(pbarOverall->sizePolicy().hasHeightForWidth());
    pbarOverall->setSizePolicy(sizePolicy3);
    pbarOverall->setMinimumSize(QSize(45, 19));
    pbarOverall->setValue(24);
    pbarOverall->setTextVisible(false);
    pbarOverall->setOrientation(Qt::Horizontal);

    gridLayout3->addWidget(pbarOverall, 5, 0, 1, 1);


    gridLayout->addWidget(grpProgress, 1, 4, 1, 2);

    groupBox_2 = new QGroupBox(LaGrassProcessBase);
    groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
    QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Minimum);
    sizePolicy4.setHorizontalStretch(0);
    sizePolicy4.setVerticalStretch(0);
    sizePolicy4.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
    groupBox_2->setSizePolicy(sizePolicy4);
    gridLayout4 = new QGridLayout(groupBox_2);
    gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
    tbGrass = new QTextBrowser(groupBox_2);
    tbGrass->setObjectName(QString::fromUtf8("tbGrass"));
    sizePolicy3.setHeightForWidth(tbGrass->sizePolicy().hasHeightForWidth());
    tbGrass->setSizePolicy(sizePolicy3);

    gridLayout4->addWidget(tbGrass, 0, 0, 1, 1);


    gridLayout->addWidget(groupBox_2, 3, 0, 1, 6);

    spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout->addItem(spacerItem, 4, 5, 1, 1);

    label_2 = new QLabel(LaGrassProcessBase);
    label_2->setObjectName(QString::fromUtf8("label_2"));

    gridLayout->addWidget(label_2, 5, 0, 1, 6);

    cbPeriod = new QComboBox(LaGrassProcessBase);
    cbPeriod->setObjectName(QString::fromUtf8("cbPeriod"));

    gridLayout->addWidget(cbPeriod, 6, 0, 1, 1);

    cbPopulation = new QComboBox(LaGrassProcessBase);
    cbPopulation->setObjectName(QString::fromUtf8("cbPopulation"));

    gridLayout->addWidget(cbPopulation, 6, 1, 1, 1);

    cbDietRatio = new QComboBox(LaGrassProcessBase);
    cbDietRatio->setObjectName(QString::fromUtf8("cbDietRatio"));

    gridLayout->addWidget(cbDietRatio, 6, 2, 1, 1);

    cbDairy = new QComboBox(LaGrassProcessBase);
    cbDairy->setObjectName(QString::fromUtf8("cbDairy"));

    gridLayout->addWidget(cbDairy, 6, 3, 1, 2);

    cbAnimalsFed = new QComboBox(LaGrassProcessBase);
    cbAnimalsFed->setObjectName(QString::fromUtf8("cbAnimalsFed"));

    gridLayout->addWidget(cbAnimalsFed, 6, 5, 1, 1);

    label_3 = new QLabel(LaGrassProcessBase);
    label_3->setObjectName(QString::fromUtf8("label_3"));

    gridLayout->addWidget(label_3, 7, 0, 1, 2);

    leOtherText = new QLineEdit(LaGrassProcessBase);
    leOtherText->setObjectName(QString::fromUtf8("leOtherText"));

    gridLayout->addWidget(leOtherText, 7, 2, 1, 3);

    buttonBox = new QDialogButtonBox(LaGrassProcessBase);
    buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
    buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::NoButton|QDialogButtonBox::Ok);

    gridLayout->addWidget(buttonBox, 7, 5, 1, 1);


    retranslateUi(LaGrassProcessBase);
    QObject::connect(buttonBox, SIGNAL(accepted()), LaGrassProcessBase, SLOT(accept()));
    QObject::connect(buttonBox, SIGNAL(rejected()), LaGrassProcessBase, SLOT(reject()));

    QMetaObject::connectSlotsByName(LaGrassProcessBase);
    } // setupUi

    void retranslateUi(QDialog *LaGrassProcessBase)
    {
    LaGrassProcessBase->setWindowTitle(QApplication::translate("LaGrassProcessBase", "Grass Processing", 0, QApplication::UnicodeUTF8));
    grpPreview->setTitle(QApplication::translate("LaGrassProcessBase", "Preview", 0, QApplication::UnicodeUTF8));
    lblPreview->setText(QApplication::translate("LaGrassProcessBase", "Preview feature not available in Beta Version", 0, QApplication::UnicodeUTF8));
    grpCurrentTarget->setTitle(QApplication::translate("LaGrassProcessBase", "Current Target", 0, QApplication::UnicodeUTF8));
    lblGraphic->setText(QApplication::translate("LaGrassProcessBase", "No Graphic", 0, QApplication::UnicodeUTF8));
    lblCurrentArea->setText(QApplication::translate("LaGrassProcessBase", "123456", 0, QApplication::UnicodeUTF8));
    grpProgress->setTitle(QApplication::translate("LaGrassProcessBase", "Progress", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaGrassProcessBase", "Current GRASS Command", 0, QApplication::UnicodeUTF8));
    pbarBusy->setFormat(QString());
    lblAreaTarget->setText(QApplication::translate("LaGrassProcessBase", "Target: 123456", 0, QApplication::UnicodeUTF8));
    pbarTarget->setFormat(QString());
    label_6->setText(QApplication::translate("LaGrassProcessBase", "Overall Progress", 0, QApplication::UnicodeUTF8));
    pbarOverall->setFormat(QString());
    groupBox_2->setTitle(QApplication::translate("LaGrassProcessBase", "Log", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    tbGrass->setWhatsThis(QApplication::translate("LaGrassProcessBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for a crop simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_2->setText(QApplication::translate("LaGrassProcessBase", "Select the PERIOD, POPULATION, & DIET RATIO.", 0, QApplication::UnicodeUTF8));
    cbPeriod->clear();
    cbPeriod->insertItems(0, QStringList()
     << QApplication::translate("LaGrassProcessBase", "Chalcolithic", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "EEB1", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "LEB1", 0, QApplication::UnicodeUTF8)
    );
    cbPopulation->clear();
    cbPopulation->insertItems(0, QStringList()
     << QApplication::translate("LaGrassProcessBase", "Max", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "Min", 0, QApplication::UnicodeUTF8)
    );
    cbDietRatio->clear();
    cbDietRatio->insertItems(0, QStringList()
     << QApplication::translate("LaGrassProcessBase", "Meat 10%", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "Meat 20%", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "Meat 30%", 0, QApplication::UnicodeUTF8)
    );
    cbDairy->clear();
    cbDairy->insertItems(0, QStringList()
     << QApplication::translate("LaGrassProcessBase", "Dairy 100%", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "Dairy 50%", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "No Dairy", 0, QApplication::UnicodeUTF8)
    );
    cbAnimalsFed->clear();
    cbAnimalsFed->insertItems(0, QStringList()
     << QApplication::translate("LaGrassProcessBase", "Animals Fed", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaGrassProcessBase", "Animals Not Fed", 0, QApplication::UnicodeUTF8)
    );
    label_3->setText(QApplication::translate("LaGrassProcessBase", "Other text to include in filename:", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaGrassProcessBase);
    } // retranslateUi

};

namespace Ui {
    class LaGrassProcessBase: public Ui_LaGrassProcessBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LAGRASSPROCESSBASE_H
