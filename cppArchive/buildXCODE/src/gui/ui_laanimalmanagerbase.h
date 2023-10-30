/********************************************************************************
** Form generated from reading ui file 'laanimalmanagerbase.ui'
**
** Created: Wed Mar 25 15:53:07 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LAANIMALMANAGERBASE_H
#define UI_LAANIMALMANAGERBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolButton>

QT_BEGIN_NAMESPACE

class Ui_LaAnimalManagerBase
{
public:
    QGridLayout *gridLayout;
    QGroupBox *groupBoxAnimalDescription;
    QGridLayout *gridLayout1;
    QHBoxLayout *hboxLayout;
    QLabel *label;
    QLineEdit *leName;
    QHBoxLayout *hboxLayout1;
    QLabel *label_4;
    QLineEdit *leDescription;
    QFrame *line_2;
    QLabel *label_14;
    QSpinBox *sbMeatFoodValue;
    QLabel *label_9;
    QSpinBox *sbUsableMeatPercent;
    QLabel *label_10;
    QSpinBox *sbKillWeight;
    QLabel *label_16;
    QSpinBox *sbWeaningWeight;
    QLabel *label_11;
    QSpinBox *sbGrowTime;
    QLabel *label_12;
    QSpinBox *sbDeathRate;
    QLabel *label_2;
    QSpinBox *sbSexualMaturity;
    QLabel *label_17;
    QSpinBox *sbAdultWeight;
    QLabel *label_18;
    QSpinBox *sbFemalesToMales;
    QLabel *label_3;
    QSpinBox *sbBreedingLife;
    QLabel *label_19;
    QSpinBox *sbConceptionEfficiency;
    QLabel *label_5;
    QSpinBox *sbYoungPerBirth;
    QLabel *label_6;
    QSpinBox *sbWeaningAge;
    QLabel *label_7;
    QSpinBox *sbGestationTime;
    QLabel *label_8;
    QSpinBox *sbEstrousCycleTime;
    QLabel *label_21;
    QSpinBox *sbLactationTime;
    QGroupBox *grpProfiles;
    QGridLayout *gridLayout2;
    QTableWidget *tblAnimals;
    QGridLayout *gridLayout3;
    QToolButton *toolCopy;
    QToolButton *toolNew;
    QToolButton *toolDelete;
    QSpacerItem *spacerItem;
    QLabel *lblAnimalPix;
    QPushButton *pbnAnimalPic;
    QPushButton *pbnImport;
    QPushButton *pbnExport;
    QGroupBox *groupBoxFeedRequirements;
    QGridLayout *gridLayout4;
    QGridLayout *gridLayout5;
    QLabel *label_13;
    QComboBox *cbFeedEnergyType;
    QLabel *labelFeedRequirements2;
    QSpinBox *sbEnergyForPregnant;
    QLabel *labelFeedRequirements3;
    QSpinBox *sbEnergyForLactating;
    QLabel *labelFeedRequirements3_2;
    QSpinBox *sbEnergyForMaintenance;
    QLabel *labelFeedRequirements4;
    QSpinBox *sbEnergyForJuvenilePerKg;
    QGroupBox *groupBoxByProducts;
    QGridLayout *gridLayout6;
    QCheckBox *checkBoxMilk;
    QSpinBox *sbMilk;
    QLabel *label_15;
    QSpinBox *sbMilkFoodValue;
    QFrame *line;
    QCheckBox *checkBoxFleece;
    QSpinBox *sbFleeceWeight;
    QPushButton *pbnApply;
    QPushButton *pbnClose;

    void setupUi(QDialog *LaAnimalManagerBase)
    {
    if (LaAnimalManagerBase->objectName().isEmpty())
        LaAnimalManagerBase->setObjectName(QString::fromUtf8("LaAnimalManagerBase"));
    LaAnimalManagerBase->resize(806, 750);
    const QIcon icon = QIcon(QString::fromUtf8(":/la_icon.png"));
    LaAnimalManagerBase->setWindowIcon(icon);
    gridLayout = new QGridLayout(LaAnimalManagerBase);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    groupBoxAnimalDescription = new QGroupBox(LaAnimalManagerBase);
    groupBoxAnimalDescription->setObjectName(QString::fromUtf8("groupBoxAnimalDescription"));
    QSizePolicy sizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(groupBoxAnimalDescription->sizePolicy().hasHeightForWidth());
    groupBoxAnimalDescription->setSizePolicy(sizePolicy);
    gridLayout1 = new QGridLayout(groupBoxAnimalDescription);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    hboxLayout = new QHBoxLayout();
    hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
    label = new QLabel(groupBoxAnimalDescription);
    label->setObjectName(QString::fromUtf8("label"));

    hboxLayout->addWidget(label);

    leName = new QLineEdit(groupBoxAnimalDescription);
    leName->setObjectName(QString::fromUtf8("leName"));

    hboxLayout->addWidget(leName);


    gridLayout1->addLayout(hboxLayout, 0, 0, 1, 2);

    hboxLayout1 = new QHBoxLayout();
    hboxLayout1->setObjectName(QString::fromUtf8("hboxLayout1"));
    label_4 = new QLabel(groupBoxAnimalDescription);
    label_4->setObjectName(QString::fromUtf8("label_4"));

    hboxLayout1->addWidget(label_4);

    leDescription = new QLineEdit(groupBoxAnimalDescription);
    leDescription->setObjectName(QString::fromUtf8("leDescription"));

    hboxLayout1->addWidget(leDescription);


    gridLayout1->addLayout(hboxLayout1, 1, 0, 1, 2);

    line_2 = new QFrame(groupBoxAnimalDescription);
    line_2->setObjectName(QString::fromUtf8("line_2"));
    line_2->setFrameShape(QFrame::HLine);
    line_2->setFrameShadow(QFrame::Sunken);

    gridLayout1->addWidget(line_2, 2, 0, 1, 2);

    label_14 = new QLabel(groupBoxAnimalDescription);
    label_14->setObjectName(QString::fromUtf8("label_14"));
    QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Preferred);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(label_14->sizePolicy().hasHeightForWidth());
    label_14->setSizePolicy(sizePolicy1);
    label_14->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_14, 3, 0, 1, 1);

    sbMeatFoodValue = new QSpinBox(groupBoxAnimalDescription);
    sbMeatFoodValue->setObjectName(QString::fromUtf8("sbMeatFoodValue"));
    QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(sbMeatFoodValue->sizePolicy().hasHeightForWidth());
    sbMeatFoodValue->setSizePolicy(sizePolicy2);
    sbMeatFoodValue->setAlignment(Qt::AlignRight);
    sbMeatFoodValue->setMaximum(20000);
    sbMeatFoodValue->setValue(3000);

    gridLayout1->addWidget(sbMeatFoodValue, 3, 1, 1, 1);

    label_9 = new QLabel(groupBoxAnimalDescription);
    label_9->setObjectName(QString::fromUtf8("label_9"));
    sizePolicy1.setHeightForWidth(label_9->sizePolicy().hasHeightForWidth());
    label_9->setSizePolicy(sizePolicy1);
    label_9->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_9, 4, 0, 1, 1);

    sbUsableMeatPercent = new QSpinBox(groupBoxAnimalDescription);
    sbUsableMeatPercent->setObjectName(QString::fromUtf8("sbUsableMeatPercent"));
    sizePolicy2.setHeightForWidth(sbUsableMeatPercent->sizePolicy().hasHeightForWidth());
    sbUsableMeatPercent->setSizePolicy(sizePolicy2);
    sbUsableMeatPercent->setAlignment(Qt::AlignRight);
    sbUsableMeatPercent->setMaximum(120);
    sbUsableMeatPercent->setValue(80);

    gridLayout1->addWidget(sbUsableMeatPercent, 4, 1, 1, 1);

    label_10 = new QLabel(groupBoxAnimalDescription);
    label_10->setObjectName(QString::fromUtf8("label_10"));
    sizePolicy1.setHeightForWidth(label_10->sizePolicy().hasHeightForWidth());
    label_10->setSizePolicy(sizePolicy1);
    label_10->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_10, 5, 0, 1, 1);

    sbKillWeight = new QSpinBox(groupBoxAnimalDescription);
    sbKillWeight->setObjectName(QString::fromUtf8("sbKillWeight"));
    QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Fixed);
    sizePolicy3.setHorizontalStretch(0);
    sizePolicy3.setVerticalStretch(0);
    sizePolicy3.setHeightForWidth(sbKillWeight->sizePolicy().hasHeightForWidth());
    sbKillWeight->setSizePolicy(sizePolicy3);
    sbKillWeight->setAlignment(Qt::AlignRight);
    sbKillWeight->setMaximum(2000);
    sbKillWeight->setValue(100);

    gridLayout1->addWidget(sbKillWeight, 5, 1, 1, 1);

    label_16 = new QLabel(groupBoxAnimalDescription);
    label_16->setObjectName(QString::fromUtf8("label_16"));
    label_16->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_16, 6, 0, 1, 1);

    sbWeaningWeight = new QSpinBox(groupBoxAnimalDescription);
    sbWeaningWeight->setObjectName(QString::fromUtf8("sbWeaningWeight"));
    sizePolicy2.setHeightForWidth(sbWeaningWeight->sizePolicy().hasHeightForWidth());
    sbWeaningWeight->setSizePolicy(sizePolicy2);
    sbWeaningWeight->setAlignment(Qt::AlignRight);
    sbWeaningWeight->setMaximum(120);
    sbWeaningWeight->setValue(80);

    gridLayout1->addWidget(sbWeaningWeight, 6, 1, 1, 1);

    label_11 = new QLabel(groupBoxAnimalDescription);
    label_11->setObjectName(QString::fromUtf8("label_11"));
    sizePolicy1.setHeightForWidth(label_11->sizePolicy().hasHeightForWidth());
    label_11->setSizePolicy(sizePolicy1);
    label_11->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_11, 7, 0, 1, 1);

    sbGrowTime = new QSpinBox(groupBoxAnimalDescription);
    sbGrowTime->setObjectName(QString::fromUtf8("sbGrowTime"));
    sizePolicy2.setHeightForWidth(sbGrowTime->sizePolicy().hasHeightForWidth());
    sbGrowTime->setSizePolicy(sizePolicy2);
    sbGrowTime->setAlignment(Qt::AlignRight);
    sbGrowTime->setMinimum(1);
    sbGrowTime->setMaximum(1000);
    sbGrowTime->setValue(60);

    gridLayout1->addWidget(sbGrowTime, 7, 1, 1, 1);

    label_12 = new QLabel(groupBoxAnimalDescription);
    label_12->setObjectName(QString::fromUtf8("label_12"));
    sizePolicy1.setHeightForWidth(label_12->sizePolicy().hasHeightForWidth());
    label_12->setSizePolicy(sizePolicy1);
    label_12->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_12, 8, 0, 1, 1);

    sbDeathRate = new QSpinBox(groupBoxAnimalDescription);
    sbDeathRate->setObjectName(QString::fromUtf8("sbDeathRate"));
    sizePolicy3.setHeightForWidth(sbDeathRate->sizePolicy().hasHeightForWidth());
    sbDeathRate->setSizePolicy(sizePolicy3);
    sbDeathRate->setAlignment(Qt::AlignRight);
    sbDeathRate->setMaximum(100);
    sbDeathRate->setValue(10);

    gridLayout1->addWidget(sbDeathRate, 8, 1, 1, 1);

    label_2 = new QLabel(groupBoxAnimalDescription);
    label_2->setObjectName(QString::fromUtf8("label_2"));
    label_2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_2, 9, 0, 1, 1);

    sbSexualMaturity = new QSpinBox(groupBoxAnimalDescription);
    sbSexualMaturity->setObjectName(QString::fromUtf8("sbSexualMaturity"));
    sizePolicy2.setHeightForWidth(sbSexualMaturity->sizePolicy().hasHeightForWidth());
    sbSexualMaturity->setSizePolicy(sizePolicy2);
    sbSexualMaturity->setAlignment(Qt::AlignRight);
    sbSexualMaturity->setMaximum(240);
    sbSexualMaturity->setValue(18);

    gridLayout1->addWidget(sbSexualMaturity, 9, 1, 1, 1);

    label_17 = new QLabel(groupBoxAnimalDescription);
    label_17->setObjectName(QString::fromUtf8("label_17"));
    sizePolicy1.setHeightForWidth(label_17->sizePolicy().hasHeightForWidth());
    label_17->setSizePolicy(sizePolicy1);
    label_17->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_17, 10, 0, 1, 1);

    sbAdultWeight = new QSpinBox(groupBoxAnimalDescription);
    sbAdultWeight->setObjectName(QString::fromUtf8("sbAdultWeight"));
    sizePolicy3.setHeightForWidth(sbAdultWeight->sizePolicy().hasHeightForWidth());
    sbAdultWeight->setSizePolicy(sizePolicy3);
    sbAdultWeight->setAlignment(Qt::AlignRight);
    sbAdultWeight->setMaximum(2000);
    sbAdultWeight->setValue(100);

    gridLayout1->addWidget(sbAdultWeight, 10, 1, 1, 1);

    label_18 = new QLabel(groupBoxAnimalDescription);
    label_18->setObjectName(QString::fromUtf8("label_18"));
    sizePolicy1.setHeightForWidth(label_18->sizePolicy().hasHeightForWidth());
    label_18->setSizePolicy(sizePolicy1);
    label_18->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_18, 11, 0, 1, 1);

    sbFemalesToMales = new QSpinBox(groupBoxAnimalDescription);
    sbFemalesToMales->setObjectName(QString::fromUtf8("sbFemalesToMales"));
    sizePolicy3.setHeightForWidth(sbFemalesToMales->sizePolicy().hasHeightForWidth());
    sbFemalesToMales->setSizePolicy(sizePolicy3);
    sbFemalesToMales->setAlignment(Qt::AlignRight);
    sbFemalesToMales->setMinimum(1);
    sbFemalesToMales->setMaximum(2000);
    sbFemalesToMales->setValue(20);

    gridLayout1->addWidget(sbFemalesToMales, 11, 1, 1, 1);

    label_3 = new QLabel(groupBoxAnimalDescription);
    label_3->setObjectName(QString::fromUtf8("label_3"));
    label_3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_3, 12, 0, 1, 1);

    sbBreedingLife = new QSpinBox(groupBoxAnimalDescription);
    sbBreedingLife->setObjectName(QString::fromUtf8("sbBreedingLife"));
    sizePolicy2.setHeightForWidth(sbBreedingLife->sizePolicy().hasHeightForWidth());
    sbBreedingLife->setSizePolicy(sizePolicy2);
    sbBreedingLife->setAlignment(Qt::AlignRight);
    sbBreedingLife->setMinimum(1);
    sbBreedingLife->setMaximum(120);
    sbBreedingLife->setValue(4);

    gridLayout1->addWidget(sbBreedingLife, 12, 1, 1, 1);

    label_19 = new QLabel(groupBoxAnimalDescription);
    label_19->setObjectName(QString::fromUtf8("label_19"));
    sizePolicy1.setHeightForWidth(label_19->sizePolicy().hasHeightForWidth());
    label_19->setSizePolicy(sizePolicy1);
    label_19->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_19, 13, 0, 1, 1);

    sbConceptionEfficiency = new QSpinBox(groupBoxAnimalDescription);
    sbConceptionEfficiency->setObjectName(QString::fromUtf8("sbConceptionEfficiency"));
    sizePolicy3.setHeightForWidth(sbConceptionEfficiency->sizePolicy().hasHeightForWidth());
    sbConceptionEfficiency->setSizePolicy(sizePolicy3);
    sbConceptionEfficiency->setAlignment(Qt::AlignRight);
    sbConceptionEfficiency->setMaximum(2000);
    sbConceptionEfficiency->setValue(100);

    gridLayout1->addWidget(sbConceptionEfficiency, 13, 1, 1, 1);

    label_5 = new QLabel(groupBoxAnimalDescription);
    label_5->setObjectName(QString::fromUtf8("label_5"));
    label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_5, 14, 0, 1, 1);

    sbYoungPerBirth = new QSpinBox(groupBoxAnimalDescription);
    sbYoungPerBirth->setObjectName(QString::fromUtf8("sbYoungPerBirth"));
    sizePolicy2.setHeightForWidth(sbYoungPerBirth->sizePolicy().hasHeightForWidth());
    sbYoungPerBirth->setSizePolicy(sizePolicy2);
    sbYoungPerBirth->setAlignment(Qt::AlignRight);
    sbYoungPerBirth->setMinimum(1);
    sbYoungPerBirth->setMaximum(20);
    sbYoungPerBirth->setValue(1);

    gridLayout1->addWidget(sbYoungPerBirth, 14, 1, 1, 1);

    label_6 = new QLabel(groupBoxAnimalDescription);
    label_6->setObjectName(QString::fromUtf8("label_6"));
    label_6->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_6, 15, 0, 1, 1);

    sbWeaningAge = new QSpinBox(groupBoxAnimalDescription);
    sbWeaningAge->setObjectName(QString::fromUtf8("sbWeaningAge"));
    sizePolicy2.setHeightForWidth(sbWeaningAge->sizePolicy().hasHeightForWidth());
    sbWeaningAge->setSizePolicy(sizePolicy2);
    sbWeaningAge->setAlignment(Qt::AlignRight);
    sbWeaningAge->setMaximum(120);
    sbWeaningAge->setValue(80);

    gridLayout1->addWidget(sbWeaningAge, 15, 1, 1, 1);

    label_7 = new QLabel(groupBoxAnimalDescription);
    label_7->setObjectName(QString::fromUtf8("label_7"));
    label_7->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_7, 16, 0, 1, 1);

    sbGestationTime = new QSpinBox(groupBoxAnimalDescription);
    sbGestationTime->setObjectName(QString::fromUtf8("sbGestationTime"));
    sizePolicy2.setHeightForWidth(sbGestationTime->sizePolicy().hasHeightForWidth());
    sbGestationTime->setSizePolicy(sizePolicy2);
    sbGestationTime->setAlignment(Qt::AlignRight);
    sbGestationTime->setMinimum(1);
    sbGestationTime->setMaximum(365);
    sbGestationTime->setValue(120);

    gridLayout1->addWidget(sbGestationTime, 16, 1, 1, 1);

    label_8 = new QLabel(groupBoxAnimalDescription);
    label_8->setObjectName(QString::fromUtf8("label_8"));
    label_8->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_8, 17, 0, 1, 1);

    sbEstrousCycleTime = new QSpinBox(groupBoxAnimalDescription);
    sbEstrousCycleTime->setObjectName(QString::fromUtf8("sbEstrousCycleTime"));
    sizePolicy2.setHeightForWidth(sbEstrousCycleTime->sizePolicy().hasHeightForWidth());
    sbEstrousCycleTime->setSizePolicy(sizePolicy2);
    sbEstrousCycleTime->setAlignment(Qt::AlignRight);
    sbEstrousCycleTime->setMaximum(120);
    sbEstrousCycleTime->setValue(21);

    gridLayout1->addWidget(sbEstrousCycleTime, 17, 1, 1, 1);

    label_21 = new QLabel(groupBoxAnimalDescription);
    label_21->setObjectName(QString::fromUtf8("label_21"));
    label_21->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout1->addWidget(label_21, 18, 0, 1, 1);

    sbLactationTime = new QSpinBox(groupBoxAnimalDescription);
    sbLactationTime->setObjectName(QString::fromUtf8("sbLactationTime"));
    sizePolicy2.setHeightForWidth(sbLactationTime->sizePolicy().hasHeightForWidth());
    sbLactationTime->setSizePolicy(sizePolicy2);
    sbLactationTime->setAlignment(Qt::AlignRight);
    sbLactationTime->setMaximum(1000);
    sbLactationTime->setValue(210);

    gridLayout1->addWidget(sbLactationTime, 18, 1, 1, 1);


    gridLayout->addWidget(groupBoxAnimalDescription, 0, 0, 3, 1);

    grpProfiles = new QGroupBox(LaAnimalManagerBase);
    grpProfiles->setObjectName(QString::fromUtf8("grpProfiles"));
    QSizePolicy sizePolicy4(QSizePolicy::Preferred, QSizePolicy::Expanding);
    sizePolicy4.setHorizontalStretch(0);
    sizePolicy4.setVerticalStretch(0);
    sizePolicy4.setHeightForWidth(grpProfiles->sizePolicy().hasHeightForWidth());
    grpProfiles->setSizePolicy(sizePolicy4);
    gridLayout2 = new QGridLayout(grpProfiles);
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    tblAnimals = new QTableWidget(grpProfiles);
    if (tblAnimals->columnCount() < 2)
        tblAnimals->setColumnCount(2);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(1, __colItem1);
    tblAnimals->setObjectName(QString::fromUtf8("tblAnimals"));
    tblAnimals->setAlternatingRowColors(true);
    tblAnimals->setSelectionMode(QAbstractItemView::SingleSelection);
    tblAnimals->setSelectionBehavior(QAbstractItemView::SelectRows);

    gridLayout2->addWidget(tblAnimals, 0, 0, 4, 1);

    gridLayout3 = new QGridLayout();
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    toolCopy = new QToolButton(grpProfiles);
    toolCopy->setObjectName(QString::fromUtf8("toolCopy"));
    const QIcon icon1 = QIcon(QString::fromUtf8(":/copy.png"));
    toolCopy->setIcon(icon1);

    gridLayout3->addWidget(toolCopy, 2, 1, 1, 1);

    toolNew = new QToolButton(grpProfiles);
    toolNew->setObjectName(QString::fromUtf8("toolNew"));
    const QIcon icon2 = QIcon(QString::fromUtf8(":/new.png"));
    toolNew->setIcon(icon2);

    gridLayout3->addWidget(toolNew, 2, 0, 1, 1);

    toolDelete = new QToolButton(grpProfiles);
    toolDelete->setObjectName(QString::fromUtf8("toolDelete"));
    const QIcon icon3 = QIcon(QString::fromUtf8(":/delete.png"));
    toolDelete->setIcon(icon3);

    gridLayout3->addWidget(toolDelete, 2, 2, 1, 1);

    spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout3->addItem(spacerItem, 1, 1, 1, 1);

    lblAnimalPix = new QLabel(grpProfiles);
    lblAnimalPix->setObjectName(QString::fromUtf8("lblAnimalPix"));
    lblAnimalPix->setMinimumSize(QSize(100, 100));
    lblAnimalPix->setMaximumSize(QSize(100, 100));
    lblAnimalPix->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(lblAnimalPix, 0, 0, 1, 3);


    gridLayout2->addLayout(gridLayout3, 0, 1, 1, 1);

    pbnAnimalPic = new QPushButton(grpProfiles);
    pbnAnimalPic->setObjectName(QString::fromUtf8("pbnAnimalPic"));

    gridLayout2->addWidget(pbnAnimalPic, 1, 1, 1, 1);

    pbnImport = new QPushButton(grpProfiles);
    pbnImport->setObjectName(QString::fromUtf8("pbnImport"));
    pbnImport->setMinimumSize(QSize(80, 0));

    gridLayout2->addWidget(pbnImport, 2, 1, 1, 1);

    pbnExport = new QPushButton(grpProfiles);
    pbnExport->setObjectName(QString::fromUtf8("pbnExport"));
    pbnExport->setMinimumSize(QSize(80, 0));

    gridLayout2->addWidget(pbnExport, 3, 1, 1, 1);


    gridLayout->addWidget(grpProfiles, 0, 1, 1, 3);

    groupBoxFeedRequirements = new QGroupBox(LaAnimalManagerBase);
    groupBoxFeedRequirements->setObjectName(QString::fromUtf8("groupBoxFeedRequirements"));
    sizePolicy2.setHeightForWidth(groupBoxFeedRequirements->sizePolicy().hasHeightForWidth());
    groupBoxFeedRequirements->setSizePolicy(sizePolicy2);
    gridLayout4 = new QGridLayout(groupBoxFeedRequirements);
    gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
    gridLayout5 = new QGridLayout();
    gridLayout5->setObjectName(QString::fromUtf8("gridLayout5"));
    label_13 = new QLabel(groupBoxFeedRequirements);
    label_13->setObjectName(QString::fromUtf8("label_13"));

    gridLayout5->addWidget(label_13, 0, 0, 1, 1);

    cbFeedEnergyType = new QComboBox(groupBoxFeedRequirements);
    cbFeedEnergyType->setObjectName(QString::fromUtf8("cbFeedEnergyType"));

    gridLayout5->addWidget(cbFeedEnergyType, 0, 1, 1, 1);

    labelFeedRequirements2 = new QLabel(groupBoxFeedRequirements);
    labelFeedRequirements2->setObjectName(QString::fromUtf8("labelFeedRequirements2"));

    gridLayout5->addWidget(labelFeedRequirements2, 1, 0, 1, 1);

    sbEnergyForPregnant = new QSpinBox(groupBoxFeedRequirements);
    sbEnergyForPregnant->setObjectName(QString::fromUtf8("sbEnergyForPregnant"));
    sizePolicy3.setHeightForWidth(sbEnergyForPregnant->sizePolicy().hasHeightForWidth());
    sbEnergyForPregnant->setSizePolicy(sizePolicy3);
    sbEnergyForPregnant->setMaximum(20000);
    sbEnergyForPregnant->setValue(4000);

    gridLayout5->addWidget(sbEnergyForPregnant, 1, 1, 1, 1);

    labelFeedRequirements3 = new QLabel(groupBoxFeedRequirements);
    labelFeedRequirements3->setObjectName(QString::fromUtf8("labelFeedRequirements3"));

    gridLayout5->addWidget(labelFeedRequirements3, 2, 0, 1, 1);

    sbEnergyForLactating = new QSpinBox(groupBoxFeedRequirements);
    sbEnergyForLactating->setObjectName(QString::fromUtf8("sbEnergyForLactating"));
    sizePolicy3.setHeightForWidth(sbEnergyForLactating->sizePolicy().hasHeightForWidth());
    sbEnergyForLactating->setSizePolicy(sizePolicy3);
    sbEnergyForLactating->setMaximum(20000);
    sbEnergyForLactating->setValue(4000);

    gridLayout5->addWidget(sbEnergyForLactating, 2, 1, 1, 1);

    labelFeedRequirements3_2 = new QLabel(groupBoxFeedRequirements);
    labelFeedRequirements3_2->setObjectName(QString::fromUtf8("labelFeedRequirements3_2"));

    gridLayout5->addWidget(labelFeedRequirements3_2, 3, 0, 1, 1);

    sbEnergyForMaintenance = new QSpinBox(groupBoxFeedRequirements);
    sbEnergyForMaintenance->setObjectName(QString::fromUtf8("sbEnergyForMaintenance"));
    sizePolicy3.setHeightForWidth(sbEnergyForMaintenance->sizePolicy().hasHeightForWidth());
    sbEnergyForMaintenance->setSizePolicy(sizePolicy3);
    sbEnergyForMaintenance->setMaximum(20000);
    sbEnergyForMaintenance->setValue(4000);

    gridLayout5->addWidget(sbEnergyForMaintenance, 3, 1, 1, 1);

    labelFeedRequirements4 = new QLabel(groupBoxFeedRequirements);
    labelFeedRequirements4->setObjectName(QString::fromUtf8("labelFeedRequirements4"));

    gridLayout5->addWidget(labelFeedRequirements4, 4, 0, 1, 1);

    sbEnergyForJuvenilePerKg = new QSpinBox(groupBoxFeedRequirements);
    sbEnergyForJuvenilePerKg->setObjectName(QString::fromUtf8("sbEnergyForJuvenilePerKg"));
    sizePolicy3.setHeightForWidth(sbEnergyForJuvenilePerKg->sizePolicy().hasHeightForWidth());
    sbEnergyForJuvenilePerKg->setSizePolicy(sizePolicy3);
    sbEnergyForJuvenilePerKg->setMaximum(20000);
    sbEnergyForJuvenilePerKg->setValue(300);

    gridLayout5->addWidget(sbEnergyForJuvenilePerKg, 4, 1, 1, 1);


    gridLayout4->addLayout(gridLayout5, 0, 0, 1, 1);


    gridLayout->addWidget(groupBoxFeedRequirements, 1, 1, 2, 1);

    groupBoxByProducts = new QGroupBox(LaAnimalManagerBase);
    groupBoxByProducts->setObjectName(QString::fromUtf8("groupBoxByProducts"));
    QSizePolicy sizePolicy5(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
    sizePolicy5.setHorizontalStretch(0);
    sizePolicy5.setVerticalStretch(0);
    sizePolicy5.setHeightForWidth(groupBoxByProducts->sizePolicy().hasHeightForWidth());
    groupBoxByProducts->setSizePolicy(sizePolicy5);
    groupBoxByProducts->setMinimumSize(QSize(0, 0));
    gridLayout6 = new QGridLayout(groupBoxByProducts);
    gridLayout6->setObjectName(QString::fromUtf8("gridLayout6"));
    checkBoxMilk = new QCheckBox(groupBoxByProducts);
    checkBoxMilk->setObjectName(QString::fromUtf8("checkBoxMilk"));
    checkBoxMilk->setLayoutDirection(Qt::LeftToRight);

    gridLayout6->addWidget(checkBoxMilk, 0, 0, 1, 1);

    sbMilk = new QSpinBox(groupBoxByProducts);
    sbMilk->setObjectName(QString::fromUtf8("sbMilk"));
    sizePolicy2.setHeightForWidth(sbMilk->sizePolicy().hasHeightForWidth());
    sbMilk->setSizePolicy(sizePolicy2);
    sbMilk->setAlignment(Qt::AlignRight);
    sbMilk->setMaximum(100000);
    sbMilk->setValue(18);

    gridLayout6->addWidget(sbMilk, 0, 1, 1, 1);

    label_15 = new QLabel(groupBoxByProducts);
    label_15->setObjectName(QString::fromUtf8("label_15"));
    label_15->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout6->addWidget(label_15, 1, 0, 1, 1);

    sbMilkFoodValue = new QSpinBox(groupBoxByProducts);
    sbMilkFoodValue->setObjectName(QString::fromUtf8("sbMilkFoodValue"));
    sizePolicy2.setHeightForWidth(sbMilkFoodValue->sizePolicy().hasHeightForWidth());
    sbMilkFoodValue->setSizePolicy(sizePolicy2);
    sbMilkFoodValue->setAlignment(Qt::AlignRight);
    sbMilkFoodValue->setMinimum(1);
    sbMilkFoodValue->setMaximum(10000);
    sbMilkFoodValue->setValue(4);

    gridLayout6->addWidget(sbMilkFoodValue, 1, 1, 1, 1);

    line = new QFrame(groupBoxByProducts);
    line->setObjectName(QString::fromUtf8("line"));
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    gridLayout6->addWidget(line, 2, 0, 1, 2);

    checkBoxFleece = new QCheckBox(groupBoxByProducts);
    checkBoxFleece->setObjectName(QString::fromUtf8("checkBoxFleece"));

    gridLayout6->addWidget(checkBoxFleece, 3, 0, 1, 1);

    sbFleeceWeight = new QSpinBox(groupBoxByProducts);
    sbFleeceWeight->setObjectName(QString::fromUtf8("sbFleeceWeight"));
    sizePolicy2.setHeightForWidth(sbFleeceWeight->sizePolicy().hasHeightForWidth());
    sbFleeceWeight->setSizePolicy(sizePolicy2);
    sbFleeceWeight->setAlignment(Qt::AlignRight);
    sbFleeceWeight->setMinimum(1);
    sbFleeceWeight->setMaximum(200);
    sbFleeceWeight->setValue(1);

    gridLayout6->addWidget(sbFleeceWeight, 3, 1, 1, 1);


    gridLayout->addWidget(groupBoxByProducts, 1, 2, 1, 2);

    pbnApply = new QPushButton(LaAnimalManagerBase);
    pbnApply->setObjectName(QString::fromUtf8("pbnApply"));
    pbnApply->setCheckable(false);
    pbnApply->setFlat(false);

    gridLayout->addWidget(pbnApply, 2, 2, 1, 1);

    pbnClose = new QPushButton(LaAnimalManagerBase);
    pbnClose->setObjectName(QString::fromUtf8("pbnClose"));
    QSizePolicy sizePolicy6(QSizePolicy::Minimum, QSizePolicy::Fixed);
    sizePolicy6.setHorizontalStretch(0);
    sizePolicy6.setVerticalStretch(0);
    sizePolicy6.setHeightForWidth(pbnClose->sizePolicy().hasHeightForWidth());
    pbnClose->setSizePolicy(sizePolicy6);

    gridLayout->addWidget(pbnClose, 2, 3, 1, 1);

    QWidget::setTabOrder(tblAnimals, pbnImport);
    QWidget::setTabOrder(pbnImport, pbnExport);
    QWidget::setTabOrder(pbnExport, toolNew);
    QWidget::setTabOrder(toolNew, toolCopy);
    QWidget::setTabOrder(toolCopy, toolDelete);
    QWidget::setTabOrder(toolDelete, leName);
    QWidget::setTabOrder(leName, leDescription);
    QWidget::setTabOrder(leDescription, sbUsableMeatPercent);
    QWidget::setTabOrder(sbUsableMeatPercent, sbKillWeight);
    QWidget::setTabOrder(sbKillWeight, sbGrowTime);
    QWidget::setTabOrder(sbGrowTime, sbDeathRate);
    QWidget::setTabOrder(sbDeathRate, sbEnergyForPregnant);
    QWidget::setTabOrder(sbEnergyForPregnant, sbEnergyForLactating);
    QWidget::setTabOrder(sbEnergyForLactating, sbEnergyForJuvenilePerKg);

    retranslateUi(LaAnimalManagerBase);
    QObject::connect(pbnClose, SIGNAL(clicked()), LaAnimalManagerBase, SLOT(reject()));

    QMetaObject::connectSlotsByName(LaAnimalManagerBase);
    } // setupUi

    void retranslateUi(QDialog *LaAnimalManagerBase)
    {
    LaAnimalManagerBase->setWindowTitle(QApplication::translate("LaAnimalManagerBase", "Animal Profile Manager", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    groupBoxAnimalDescription->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model any animal, several details must be entered to define specific types or breeds. Animal Manager asks for general information about the animal in this section. You might want to have more than one breed of the same species, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different breeds of the same species is quite easy. Let's say you want to have two kinds of cows for example. The Name: field is Cow for both, but in Notes: field, enter Dairy for one, and Beast of Burden for the o"
        "ther. Then adjust the other parameters as you wish. Even though the name is the same, the animal is saved uniquely.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxAnimalDescription->setTitle(QApplication::translate("LaAnimalManagerBase", "Animal Description", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaAnimalManagerBase", "Name:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leName->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the animal you are defining in this field. You do not need a unique name. You can have, for example, 10 animals defined, all named \"Sheep\". LandUse Analyst uses a special method of saving the animals to eliminate the issue of duplicate filenames.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_4->setText(QApplication::translate("LaAnimalManagerBase", "Notes:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leDescription->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because LandUse Analyst allows more than one type of animal to be defined, the Notes: field allows you to give a brief description of the the animal. For example, you may have two \"Sheep\" defined, and the Notes: fields could contain \"For Slaughter\" and \"Wool Producers\" to distinguish between them.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_14->setText(QApplication::translate("LaAnimalManagerBase", "Food Value", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbMeatFoodValue->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of live weight usable as meat</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbMeatFoodValue->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The production targets for animals are in Kg of meat, so to be compatible with animal numbers, you must know the percentage of the animal's live weight that is usable for food. You can also take into account here the efficiency of the butchering technique that the population used. In other words, if you believe they were wasteful, this is where you would make an adjustment to integrate that.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbMeatFoodValue->setSuffix(QApplication::translate("LaAnimalManagerBase", " cal", 0, QApplication::UnicodeUTF8));
    sbMeatFoodValue->setPrefix(QString());
    label_9->setText(QApplication::translate("LaAnimalManagerBase", "Usable Meat", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbUsableMeatPercent->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of live weight usable as meat</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbUsableMeatPercent->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The production targets for animals are in Kg of meat, so to be compatible with animal numbers, you must know the percentage of the animal's live weight that is usable for food. You can also take into account here the efficiency of the butchering technique that the population used. In other words, if you believe they were wasteful, this is where you would make an adjustment to integrate that.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbUsableMeatPercent->setSuffix(QApplication::translate("LaAnimalManagerBase", " %", 0, QApplication::UnicodeUTF8));
    sbUsableMeatPercent->setPrefix(QString());
    label_10->setText(QApplication::translate("LaAnimalManagerBase", "Kill Weight", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbKillWeight->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbKillWeight->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but LandUse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbKillWeight->setSuffix(QApplication::translate("LaAnimalManagerBase", " Kg", 0, QApplication::UnicodeUTF8));
    sbKillWeight->setPrefix(QString());
    label_16->setText(QApplication::translate("LaAnimalManagerBase", "Weaning Weight", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbWeaningWeight->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weeks from birth to weaning</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbWeaningWeight->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The age of the babies, in weeks, at which they stop feeding from their mother. It is assumed by LandUse Analyst that mothers will become pregnant after one estrous cycle following weaning.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbWeaningWeight->setProperty("text", QVariant(QApplication::translate("LaAnimalManagerBase", "80 Kg", 0, QApplication::UnicodeUTF8)));
    sbWeaningWeight->setSuffix(QApplication::translate("LaAnimalManagerBase", " Kg", 0, QApplication::UnicodeUTF8));
    sbWeaningWeight->setPrefix(QString());
    label_11->setText(QApplication::translate("LaAnimalManagerBase", "Grow Time", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbGrowTime->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time from birth to slaughter weight</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbGrowTime->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grow time, or the length of time from birth to slaughter weight, is quite important for estimating the herd size. The longer it takes an animal to reach slaughter weight from birth, the higher the number of animals alive at any given time.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbGrowTime->setSuffix(QApplication::translate("LaAnimalManagerBase", " Weeks", 0, QApplication::UnicodeUTF8));
    sbGrowTime->setPrefix(QString());
    label_12->setText(QApplication::translate("LaAnimalManagerBase", "Death Rate", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbDeathRate->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Percent of babies that do not survive to slaughter age.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbDeathRate->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analyst accommodates for birthing deaths only. If an animal survives to weaning age but dies before slaughter, it is not modelled at this time. However, you can adjust the death rate setting to indicate the average survival rate of births. This is important for determining herd size, as it affects the number of mothers needed to sustain the production levels required by the settlement.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbDeathRate->setSuffix(QApplication::translate("LaAnimalManagerBase", " %", 0, QApplication::UnicodeUTF8));
    sbDeathRate->setPrefix(QString());
    label_2->setText(QApplication::translate("LaAnimalManagerBase", "Sexual Maturity", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbSexualMaturity->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Age of females when they become sexually mature.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbSexualMaturity->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simply set the age, in months, at which the females become sexually mature, and are able to reliably breed.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbSexualMaturity->setSuffix(QApplication::translate("LaAnimalManagerBase", " Mths", 0, QApplication::UnicodeUTF8));
    sbSexualMaturity->setPrefix(QString());
    label_17->setText(QApplication::translate("LaAnimalManagerBase", "Adult Weight", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbAdultWeight->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbAdultWeight->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but LandUse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbAdultWeight->setSuffix(QApplication::translate("LaAnimalManagerBase", " Kg", 0, QApplication::UnicodeUTF8));
    sbAdultWeight->setPrefix(QString());
    label_18->setText(QApplication::translate("LaAnimalManagerBase", "Females:Males", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbFemalesToMales->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbFemalesToMales->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but LandUse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbFemalesToMales->setSuffix(QString());
    sbFemalesToMales->setPrefix(QString());
    label_3->setText(QApplication::translate("LaAnimalManagerBase", "Breeding Life", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbBreedingLife->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of years females are useful for breeding</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbBreedingLife->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to determine the number of female offspring that need to be retained to sustain the adult female population (breeding herd) it is necessary to know how long a female of the species can be expected to breed reliably. This is <span style=\" font-weight:600;\">not</span> life expectancy.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbBreedingLife->setSuffix(QApplication::translate("LaAnimalManagerBase", " Years", 0, QApplication::UnicodeUTF8));
    sbBreedingLife->setPrefix(QString());
    label_19->setText(QApplication::translate("LaAnimalManagerBase", "Conception %", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbConceptionEfficiency->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average weight of animal (Kg) when slaughtered</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbConceptionEfficiency->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals can be slaughtered for butchering at any weight, but LandUse Analyst needs to know the average weight of the animals when they are slaughtered. This is their <span style=\" font-weight:600;\">live weight.</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbConceptionEfficiency->setSuffix(QApplication::translate("LaAnimalManagerBase", "  %", 0, QApplication::UnicodeUTF8));
    sbConceptionEfficiency->setPrefix(QString());
    label_5->setText(QApplication::translate("LaAnimalManagerBase", "Young / birth", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbYoungPerBirth->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of young born per birth (average)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbYoungPerBirth->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the number of babies born to a mother. This is total number, not surviving numbers. To account for deaths between birth and weaning, adjust the Death Rate.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbYoungPerBirth->setSuffix(QString());
    label_6->setText(QApplication::translate("LaAnimalManagerBase", "Weaning Age", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbWeaningAge->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weeks from birth to weaning</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbWeaningAge->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The age of the babies, in weeks, at which they stop feeding from their mother. It is assumed by LandUse Analyst that mothers will become pregnant after one estrous cycle following weaning.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbWeaningAge->setSuffix(QApplication::translate("LaAnimalManagerBase", " days", 0, QApplication::UnicodeUTF8));
    sbWeaningAge->setPrefix(QString());
    label_7->setText(QApplication::translate("LaAnimalManagerBase", "Gestation Time", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbGestationTime->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gestation time in days</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbGestationTime->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days for gestation. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbGestationTime->setSuffix(QApplication::translate("LaAnimalManagerBase", " days", 0, QApplication::UnicodeUTF8));
    sbGestationTime->setPrefix(QString());
    label_8->setText(QApplication::translate("LaAnimalManagerBase", "Estrous Cycle", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbEstrousCycleTime->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in their estrous cycle</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbEstrousCycleTime->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in the animal's estrous cycle.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbEstrousCycleTime->setSuffix(QApplication::translate("LaAnimalManagerBase", " days", 0, QApplication::UnicodeUTF8));
    sbEstrousCycleTime->setPrefix(QString());
    label_21->setText(QApplication::translate("LaAnimalManagerBase", "Lactation Time", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbLactationTime->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in their estrous cycle</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbLactationTime->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of days in the animal's estrous cycle.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbLactationTime->setProperty("text", QVariant(QApplication::translate("LaAnimalManagerBase", "210 days", 0, QApplication::UnicodeUTF8)));
    sbLactationTime->setSuffix(QApplication::translate("LaAnimalManagerBase", " days", 0, QApplication::UnicodeUTF8));
    sbLactationTime->setPrefix(QString());
    grpProfiles->setTitle(QApplication::translate("LaAnimalManagerBase", "Available Animal Profiles", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(0)->setText(QApplication::translate("LaAnimalManagerBase", "FileName", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(1)->setText(QApplication::translate("LaAnimalManagerBase", "Name", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblAnimals->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select an animal here to see and/or edit it's properties below.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblAnimals->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for these specifics. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals with the same name. Let's say you want to have two parameters set up for Cows as an example. The Name: field is Cow for bot"
        "h, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    toolCopy->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected animal</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolCopy->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new animal that is similar to one already defined, you can clone this animal to save time. All of the settings of the animal you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the animal you are cloning was).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note that the parameters are <span style=\" font-weight:600;\">not</span> transferred.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolCopy->setText(QApplication::translate("LaAnimalManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolNew->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new animal</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolNew->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Animal Manager, you are just editing the animal currently selected. To create a new animal, you must click on the New button.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolNew->setText(QApplication::translate("LaAnimalManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolDelete->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected animal</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    toolDelete->setText(QApplication::translate("LaAnimalManagerBase", "...", 0, QApplication::UnicodeUTF8));
    lblAnimalPix->setText(QApplication::translate("LaAnimalManagerBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));
    pbnAnimalPic->setText(QApplication::translate("LaAnimalManagerBase", "Set Graphic", 0, QApplication::UnicodeUTF8));
    pbnImport->setText(QApplication::translate("LaAnimalManagerBase", "Import", 0, QApplication::UnicodeUTF8));
    pbnExport->setText(QApplication::translate("LaAnimalManagerBase", "Export", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    groupBoxFeedRequirements->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analyst breaks down the calorie requirements for the animal being modelled into three categories: Gestating, Lactating, and Juvenile. Enter the average calories required per day for an animal in each of these categories.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxFeedRequirements->setTitle(QApplication::translate("LaAnimalManagerBase", "Daily Feed Requirements", 0, QApplication::UnicodeUTF8));
    label_13->setText(QApplication::translate("LaAnimalManagerBase", "Select Units", 0, QApplication::UnicodeUTF8));
    cbFeedEnergyType->clear();
    cbFeedEnergyType->insertItems(0, QStringList()
     << QApplication::translate("LaAnimalManagerBase", "MCalories", 0, QApplication::UnicodeUTF8)
     << QApplication::translate("LaAnimalManagerBase", "TDN", 0, QApplication::UnicodeUTF8)
    );
    labelFeedRequirements2->setText(QApplication::translate("LaAnimalManagerBase", "Pregnant Female", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbEnergyForPregnant->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult female</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    sbEnergyForPregnant->setSuffix(QString());

#ifndef QT_NO_TOOLTIP
    labelFeedRequirements3->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult male</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelFeedRequirements3->setText(QApplication::translate("LaAnimalManagerBase", "Lactating Female", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbEnergyForLactating->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a female that is lactating.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    sbEnergyForLactating->setSuffix(QString());

#ifndef QT_NO_TOOLTIP
    labelFeedRequirements3_2->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for an adult male</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelFeedRequirements3_2->setText(QApplication::translate("LaAnimalManagerBase", "Maintenance (Adult)", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbEnergyForMaintenance->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a female that is lactating.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    sbEnergyForMaintenance->setSuffix(QString());

#ifndef QT_NO_TOOLTIP
    labelFeedRequirements4->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Annual TDN (kg) required for a juvenile</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelFeedRequirements4->setText(QApplication::translate("LaAnimalManagerBase", "Juvenile", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbEnergyForJuvenilePerKg->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a juvenile.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbEnergyForJuvenilePerKg->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories required per day for a juvenile. LandUse Analyst considers a Juvenile to be an animal after weaning and before slaughter.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbEnergyForJuvenilePerKg->setSuffix(QApplication::translate("LaAnimalManagerBase", " per Kg", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    groupBoxByProducts->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All of the settings in Reproduction define an animal's reproductive characteristics. LandUse Analyst calculates the time between births by adding the gestation time, weaning age, and one estrous cycle.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxByProducts->setTitle(QApplication::translate("LaAnimalManagerBase", "By-Products", 0, QApplication::UnicodeUTF8));
    checkBoxMilk->setText(QApplication::translate("LaAnimalManagerBase", "Milk", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbMilk->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Age of females when they become sexually mature.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbMilk->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simply set the age, in months, at which the females become sexually mature, and are able to reliably breed.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbMilk->setSuffix(QApplication::translate("LaAnimalManagerBase", " g", 0, QApplication::UnicodeUTF8));
    sbMilk->setPrefix(QString());
    label_15->setText(QApplication::translate("LaAnimalManagerBase", "Food Value", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbMilkFoodValue->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of years females are useful for breeding</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbMilkFoodValue->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to determine the number of female offspring that need to be retained to sustain the adult female population (breeding herd) it is necessary to know how long a female of the species can be expected to breed reliably. This is <span style=\" font-weight:600;\">not</span> life expectancy.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbMilkFoodValue->setSuffix(QApplication::translate("LaAnimalManagerBase", " Cals/Kg", 0, QApplication::UnicodeUTF8));
    sbMilkFoodValue->setPrefix(QString());
    checkBoxFleece->setText(QApplication::translate("LaAnimalManagerBase", "Fleece", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbFleeceWeight->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of young born per birth (average)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbFleeceWeight->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the number of babies born to a mother. This is total number, not surviving numbers. To account for deaths between birth and weaning, adjust the Death Rate.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbFleeceWeight->setSuffix(QApplication::translate("LaAnimalManagerBase", " Kg/year", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnApply->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnApply->setWhatsThis(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define an animal, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as LandUse Analyst has a special way of saving animals to allow for duplicate Animal names. It is helpful, however, to utilize the Notes field to distinguish between same-named animal definitions.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnApply->setText(QApplication::translate("LaAnimalManagerBase", "Apply", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnClose->setToolTip(QApplication::translate("LaAnimalManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pbnClose->setText(QApplication::translate("LaAnimalManagerBase", "Close", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaAnimalManagerBase);
    } // retranslateUi

};

namespace Ui {
    class LaAnimalManagerBase: public Ui_LaAnimalManagerBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LAANIMALMANAGERBASE_H
