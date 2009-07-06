/********************************************************************************
** Form generated from reading ui file 'lamainformbase.ui'
**
** Created: Wed Mar 25 15:53:07 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LAMAINFORMBASE_H
#define UI_LAMAINFORMBASE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QListWidget>
#include <QtGui/QProgressBar>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QSlider>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QSplitter>
#include <QtGui/QTabWidget>
#include <QtGui/QTableWidget>
#include <QtGui/QTextBrowser>
#include <QtGui/QTreeWidget>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LaMainFormBase
{
public:
    QGridLayout *gridLayout;
    QSpacerItem *spacerItem;
    QSpacerItem *spacerItem1;
    QSpacerItem *spacerItem2;
    QLabel *label_5;
    QLabel *labelAnimalCheck;
    QLabel *label_3;
    QLabel *labelCropCheck;
    QLabel *label_7;
    QPushButton *pushButtonRun;
    QPushButton *pushButtonLoad;
    QPushButton *pushButtonSave;
    QPushButton *pushButtonExit;
    QProgressBar *progressBarCalcs;
    QTabWidget *MainTabs;
    QWidget *main_tab;
    QGridLayout *gridLayout1;
    QFrame *frame_2;
    QGridLayout *gridLayout2;
    QLabel *label_17;
    QLabel *lblVersion;
    QGroupBox *groupBoxManualSiteEntry;
    QGridLayout *gridLayout3;
    QLineEdit *lineEditSiteName;
    QSpinBox *sbPopulation;
    QLineEdit *lineEditPeriod;
    QLabel *textLabel2_4;
    QLabel *label;
    QLabel *label5;
    QHBoxLayout *hboxLayout;
    QLabel *label_6;
    QLineEdit *lineEditEasting;
    QHBoxLayout *hboxLayout1;
    QLabel *label_22;
    QLineEdit *lineEditNorthing;
    QGroupBox *model_method_box;
    QGridLayout *gridLayout4;
    QHBoxLayout *hboxLayout2;
    QLabel *label_2;
    QSpinBox *sbModelPrecision;
    QRadioButton *radioButtonPathDistance;
    QRadioButton *radioButtonWalkingTime;
    QRadioButton *radioButtonEuclidean;
    QGroupBox *gbxGrass;
    QGridLayout *gridLayout5;
    QLabel *lblGrass;
    QLabel *label_29;
    QComboBox *cboMapSet;
    QLabel *label_24;
    QComboBox *cboDEM;
    QSpacerItem *spacerItem3;
    QWidget *diet_tab;
    QGridLayout *gridLayout6;
    QSpacerItem *spacerItem4;
    QSpacerItem *spacerItem5;
    QGroupBox *diet_comp_box;
    QGridLayout *gridLayout7;
    QHBoxLayout *hboxLayout3;
    QCheckBox *cboxBaseOnPlants;
    QSpacerItem *spacerItem6;
    QCheckBox *cboxIncludeDairy;
    QHBoxLayout *hboxLayout4;
    QLabel *labelCropPercent;
    QSlider *sliderDiet;
    QLabel *labelMeatPercent;
    QGroupBox *groupplantpercent;
    QGridLayout *gridLayout8;
    QSpacerItem *spacerItem7;
    QLabel *labelCropTamePercent;
    QSlider *sliderCrop;
    QLabel *labelCropWildPercent;
    QLabel *label_9;
    QLabel *label_11;
    QSpacerItem *spacerItem8;
    QGroupBox *groupmeatpercent;
    QGridLayout *gridLayout9;
    QSpacerItem *spacerItem9;
    QSpacerItem *spacerItem10;
    QLabel *label_14;
    QLabel *labelMeatWildPercent;
    QLabel *label_13;
    QLabel *labelMeatTamePercent;
    QSlider *sliderMeat;
    QFrame *line;
    QHBoxLayout *hboxLayout5;
    QHBoxLayout *hboxLayout6;
    QLabel *label6;
    QSpinBox *sbDailyCalories;
    QFrame *line_2;
    QHBoxLayout *hboxLayout7;
    QLabel *label6_2;
    QSpinBox *sbDairyUtilisation;
    QFrame *line_8;
    QCheckBox *cboxLimitDairy;
    QSpinBox *sbLimitDairyPercent;
    QSpacerItem *spacerItem11;
    QLabel *labelDairySurplus;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout10;
    QHBoxLayout *hboxLayout8;
    QLabel *label_10;
    QLabel *labelCaloriesSettlement;
    QLabel *label_37;
    QHBoxLayout *hboxLayout9;
    QLabel *label_12;
    QLabel *labelPortionPlants;
    QLabel *label_38;
    QHBoxLayout *hboxLayout10;
    QLabel *label_16;
    QLabel *labelPortionMeat;
    QLabel *label_39;
    QHBoxLayout *hboxLayout11;
    QLabel *label_54;
    QLabel *labelPortionAllDairy;
    QLabel *label_55;
    QHBoxLayout *hboxLayout12;
    QLabel *label_18;
    QLabel *labelPortionCrops;
    QLabel *label_40;
    QHBoxLayout *hboxLayout13;
    QLabel *label_19;
    QLabel *labelPortionTameMeat;
    QLabel *label_41;
    QHBoxLayout *hboxLayout14;
    QLabel *label_31;
    QLabel *labelPortionDairy;
    QLabel *label_42;
    QHBoxLayout *hboxLayout15;
    QLabel *label_51;
    QLabel *labelPortionWildMeat;
    QLabel *label_50;
    QHBoxLayout *hboxLayout16;
    QLabel *label_53;
    QLabel *labelPortionWildPlants;
    QLabel *label_52;
    QHBoxLayout *hboxLayout17;
    QLabel *label_23;
    QLabel *labelCaloriesCrops;
    QLabel *label_43;
    QHBoxLayout *hboxLayout18;
    QLabel *label_21;
    QLabel *labelCaloriesTameMeat;
    QLabel *label_44;
    QHBoxLayout *hboxLayout19;
    QLabel *label_35;
    QLabel *labelCaloriesDairy;
    QLabel *label_45;
    QHBoxLayout *hboxLayout20;
    QLabel *label_46;
    QLabel *labelCaloriesWildMeat;
    QLabel *label_47;
    QHBoxLayout *hboxLayout21;
    QLabel *label_48;
    QLabel *labelCaloriesWildPlants;
    QLabel *label_49;
    QLabel *label_4;
    QLabel *label_15;
    QFrame *line_5;
    QLabel *label_20;
    QFrame *line_4;
    QFrame *line_7;
    QHBoxLayout *hboxLayout22;
    QLabel *label_8;
    QLabel *labelCaloriesIndividual;
    QLabel *label_36;
    QWidget *crops_tab;
    QGridLayout *gridLayout11;
    QSplitter *splitter_7;
    QWidget *layoutWidget;
    QHBoxLayout *hboxLayout23;
    QTableWidget *tblCrops;
    QLabel *lblCropPix;
    QTextBrowser *textBrowserCropDefinition;
    QGroupBox *gbCustomCropMask;
    QGridLayout *gridLayout12;
    QLabel *label_26;
    QComboBox *cboCommonCropRaster;
    QGroupBox *gbSlopeMaskCropLand;
    QGridLayout *gridLayout13;
    QHBoxLayout *hboxLayout24;
    QLabel *label_30;
    QDoubleSpinBox *dsbMinSlopeCropMask;
    QLabel *label_32;
    QVBoxLayout *vboxLayout;
    QPushButton *pbnNewCropParameter;
    QPushButton *pbnNewCrop;
    QWidget *animals_tab;
    QGridLayout *gridLayout14;
    QSplitter *splitter_3;
    QWidget *layoutWidget1;
    QGridLayout *gridLayout15;
    QTableWidget *tblAnimals;
    QSpacerItem *spacerItem12;
    QLabel *lblAnimalPix;
    QTextBrowser *textBrowserAnimalDefinition;
    QGroupBox *gbCustomMaskGrazingLand;
    QGridLayout *gridLayout16;
    QLabel *label_25;
    QComboBox *cboCommonGrazingRaster;
    QGroupBox *gbGenerateMaskGrazingLand;
    QGridLayout *gridLayout17;
    QLabel *label_33;
    QDoubleSpinBox *dsbMinimumSlopeGrazingMask;
    QLabel *label_34;
    QDoubleSpinBox *dsbMaximumSlopeGrazingMask;
    QGroupBox *gbFoodValue;
    QGridLayout *gridLayout18;
    QSpinBox *sbCommonRasterValue;
    QComboBox *cbCommonLandEnergyType;
    QLabel *label_28;
    QComboBox *cbAreaUnits;
    QLabel *label_27;
    QVBoxLayout *vboxLayout1;
    QPushButton *pbnNewAnimal;
    QPushButton *pbnNewAnimalParameter;
    QWidget *results_tab;
    QGridLayout *gridLayout19;
    QSplitter *splitter_5;
    QSplitter *splitter_2;
    QWidget *layoutWidget2;
    QVBoxLayout *vboxLayout2;
    QLabel *lblCropPicCalcs;
    QListWidget *listWidgetCalculationsCrop;
    QTextBrowser *textBrowserResultsCrop;
    QSplitter *splitter_4;
    QWidget *layoutWidget3;
    QVBoxLayout *vboxLayout3;
    QLabel *lblAnimalPicCalcs;
    QListWidget *listWidgetCalculationsAnimal;
    QTextBrowser *textBrowserResultsAnimals;
    QSpacerItem *spacerItem13;
    QPushButton *pbnTargets;
    QPushButton *pbnFallow;
    QPushButton *pbnHerds;
    QPushButton *pbnText;
    QPushButton *pbnHtml;
    QWidget *tab;
    QGridLayout *gridLayout20;
    QSplitter *splitter_6;
    QTextBrowser *tbReport;
    QWidget *tabLogs;
    QGridLayout *gridLayout21;
    QTextBrowser *tbLogs;
    QWidget *help_tab;
    QGridLayout *gridLayout22;
    QSplitter *splitter;
    QWidget *layoutWidget4;
    QVBoxLayout *vboxLayout4;
    QTreeWidget *treeHelp;
    QCheckBox *cbDebug;
    QTextBrowser *textHelp;

    void setupUi(QDialog *LaMainFormBase)
    {
    if (LaMainFormBase->objectName().isEmpty())
        LaMainFormBase->setObjectName(QString::fromUtf8("LaMainFormBase"));
    LaMainFormBase->resize(1057, 733);
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(LaMainFormBase->sizePolicy().hasHeightForWidth());
    LaMainFormBase->setSizePolicy(sizePolicy);
    const QIcon icon = QIcon(QString::fromUtf8(":/la_icon_small.png"));
    LaMainFormBase->setWindowIcon(icon);
    gridLayout = new QGridLayout(LaMainFormBase);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    spacerItem = new QSpacerItem(308, 17, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout->addItem(spacerItem, 1, 0, 1, 11);

    spacerItem1 = new QSpacerItem(224, 37, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout->addItem(spacerItem1, 2, 4, 1, 1);

    spacerItem2 = new QSpacerItem(223, 37, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout->addItem(spacerItem2, 2, 6, 1, 1);

    label_5 = new QLabel(LaMainFormBase);
    label_5->setObjectName(QString::fromUtf8("label_5"));

    gridLayout->addWidget(label_5, 2, 0, 1, 1);

    labelAnimalCheck = new QLabel(LaMainFormBase);
    labelAnimalCheck->setObjectName(QString::fromUtf8("labelAnimalCheck"));
    labelAnimalCheck->setAlignment(Qt::AlignCenter);

    gridLayout->addWidget(labelAnimalCheck, 2, 1, 1, 1);

    label_3 = new QLabel(LaMainFormBase);
    label_3->setObjectName(QString::fromUtf8("label_3"));

    gridLayout->addWidget(label_3, 2, 2, 1, 1);

    labelCropCheck = new QLabel(LaMainFormBase);
    labelCropCheck->setObjectName(QString::fromUtf8("labelCropCheck"));
    labelCropCheck->setAlignment(Qt::AlignCenter);

    gridLayout->addWidget(labelCropCheck, 2, 3, 1, 1);

    label_7 = new QLabel(LaMainFormBase);
    label_7->setObjectName(QString::fromUtf8("label_7"));
    QFont font;
    font.setPointSize(8);
    label_7->setFont(font);

    gridLayout->addWidget(label_7, 2, 5, 1, 1);

    pushButtonRun = new QPushButton(LaMainFormBase);
    pushButtonRun->setObjectName(QString::fromUtf8("pushButtonRun"));
    sizePolicy.setHeightForWidth(pushButtonRun->sizePolicy().hasHeightForWidth());
    pushButtonRun->setSizePolicy(sizePolicy);
    pushButtonRun->setMinimumSize(QSize(0, 0));

    gridLayout->addWidget(pushButtonRun, 2, 7, 1, 1);

    pushButtonLoad = new QPushButton(LaMainFormBase);
    pushButtonLoad->setObjectName(QString::fromUtf8("pushButtonLoad"));
    sizePolicy.setHeightForWidth(pushButtonLoad->sizePolicy().hasHeightForWidth());
    pushButtonLoad->setSizePolicy(sizePolicy);
    pushButtonLoad->setMinimumSize(QSize(0, 0));

    gridLayout->addWidget(pushButtonLoad, 2, 8, 1, 1);

    pushButtonSave = new QPushButton(LaMainFormBase);
    pushButtonSave->setObjectName(QString::fromUtf8("pushButtonSave"));
    sizePolicy.setHeightForWidth(pushButtonSave->sizePolicy().hasHeightForWidth());
    pushButtonSave->setSizePolicy(sizePolicy);

    gridLayout->addWidget(pushButtonSave, 2, 9, 1, 1);

    pushButtonExit = new QPushButton(LaMainFormBase);
    pushButtonExit->setObjectName(QString::fromUtf8("pushButtonExit"));
    sizePolicy.setHeightForWidth(pushButtonExit->sizePolicy().hasHeightForWidth());
    pushButtonExit->setSizePolicy(sizePolicy);

    gridLayout->addWidget(pushButtonExit, 2, 10, 1, 1);

    progressBarCalcs = new QProgressBar(LaMainFormBase);
    progressBarCalcs->setObjectName(QString::fromUtf8("progressBarCalcs"));
    QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Preferred);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(progressBarCalcs->sizePolicy().hasHeightForWidth());
    progressBarCalcs->setSizePolicy(sizePolicy1);
    progressBarCalcs->setMaximumSize(QSize(16777215, 10));
    progressBarCalcs->setValue(0);
    progressBarCalcs->setTextVisible(false);
    progressBarCalcs->setOrientation(Qt::Horizontal);

    gridLayout->addWidget(progressBarCalcs, 3, 0, 1, 11);

    MainTabs = new QTabWidget(LaMainFormBase);
    MainTabs->setObjectName(QString::fromUtf8("MainTabs"));
    sizePolicy1.setHeightForWidth(MainTabs->sizePolicy().hasHeightForWidth());
    MainTabs->setSizePolicy(sizePolicy1);
    MainTabs->setMinimumSize(QSize(620, 280));
    MainTabs->setMaximumSize(QSize(16777215, 16777215));
    MainTabs->setTabShape(QTabWidget::Rounded);
    main_tab = new QWidget();
    main_tab->setObjectName(QString::fromUtf8("main_tab"));
    gridLayout1 = new QGridLayout(main_tab);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    frame_2 = new QFrame(main_tab);
    frame_2->setObjectName(QString::fromUtf8("frame_2"));
    sizePolicy.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
    frame_2->setSizePolicy(sizePolicy);
    frame_2->setMinimumSize(QSize(222, 230));
    frame_2->setFrameShape(QFrame::StyledPanel);
    frame_2->setFrameShadow(QFrame::Raised);
    gridLayout2 = new QGridLayout(frame_2);
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    label_17 = new QLabel(frame_2);
    label_17->setObjectName(QString::fromUtf8("label_17"));
    sizePolicy.setHeightForWidth(label_17->sizePolicy().hasHeightForWidth());
    label_17->setSizePolicy(sizePolicy);
    label_17->setPixmap(QPixmap(QString::fromUtf8(":/la_icon.png")));
    label_17->setScaledContents(false);

    gridLayout2->addWidget(label_17, 0, 0, 1, 1);

    lblVersion = new QLabel(frame_2);
    lblVersion->setObjectName(QString::fromUtf8("lblVersion"));
    lblVersion->setAlignment(Qt::AlignCenter);

    gridLayout2->addWidget(lblVersion, 1, 0, 1, 1);


    gridLayout1->addWidget(frame_2, 0, 0, 2, 1);

    groupBoxManualSiteEntry = new QGroupBox(main_tab);
    groupBoxManualSiteEntry->setObjectName(QString::fromUtf8("groupBoxManualSiteEntry"));
    QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(groupBoxManualSiteEntry->sizePolicy().hasHeightForWidth());
    groupBoxManualSiteEntry->setSizePolicy(sizePolicy2);
    groupBoxManualSiteEntry->setCheckable(false);
    groupBoxManualSiteEntry->setChecked(false);
    gridLayout3 = new QGridLayout(groupBoxManualSiteEntry);
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    lineEditSiteName = new QLineEdit(groupBoxManualSiteEntry);
    lineEditSiteName->setObjectName(QString::fromUtf8("lineEditSiteName"));
    QSizePolicy sizePolicy3(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy3.setHorizontalStretch(2);
    sizePolicy3.setVerticalStretch(0);
    sizePolicy3.setHeightForWidth(lineEditSiteName->sizePolicy().hasHeightForWidth());
    lineEditSiteName->setSizePolicy(sizePolicy3);

    gridLayout3->addWidget(lineEditSiteName, 0, 1, 1, 2);

    sbPopulation = new QSpinBox(groupBoxManualSiteEntry);
    sbPopulation->setObjectName(QString::fromUtf8("sbPopulation"));
    sizePolicy.setHeightForWidth(sbPopulation->sizePolicy().hasHeightForWidth());
    sbPopulation->setSizePolicy(sizePolicy);
    sbPopulation->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    sbPopulation->setMinimum(1);
    sbPopulation->setMaximum(20000);
    sbPopulation->setSingleStep(1);
    sbPopulation->setValue(500);

    gridLayout3->addWidget(sbPopulation, 2, 1, 1, 1);

    lineEditPeriod = new QLineEdit(groupBoxManualSiteEntry);
    lineEditPeriod->setObjectName(QString::fromUtf8("lineEditPeriod"));
    QSizePolicy sizePolicy4(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy4.setHorizontalStretch(254);
    sizePolicy4.setVerticalStretch(0);
    sizePolicy4.setHeightForWidth(lineEditPeriod->sizePolicy().hasHeightForWidth());
    lineEditPeriod->setSizePolicy(sizePolicy4);

    gridLayout3->addWidget(lineEditPeriod, 1, 1, 1, 1);

    textLabel2_4 = new QLabel(groupBoxManualSiteEntry);
    textLabel2_4->setObjectName(QString::fromUtf8("textLabel2_4"));
    textLabel2_4->setWordWrap(false);

    gridLayout3->addWidget(textLabel2_4, 0, 0, 1, 1);

    label = new QLabel(groupBoxManualSiteEntry);
    label->setObjectName(QString::fromUtf8("label"));

    gridLayout3->addWidget(label, 1, 0, 1, 1);

    label5 = new QLabel(groupBoxManualSiteEntry);
    label5->setObjectName(QString::fromUtf8("label5"));
    label5->setWordWrap(false);

    gridLayout3->addWidget(label5, 2, 0, 1, 1);

    hboxLayout = new QHBoxLayout();
    hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
    label_6 = new QLabel(groupBoxManualSiteEntry);
    label_6->setObjectName(QString::fromUtf8("label_6"));

    hboxLayout->addWidget(label_6);

    lineEditEasting = new QLineEdit(groupBoxManualSiteEntry);
    lineEditEasting->setObjectName(QString::fromUtf8("lineEditEasting"));

    hboxLayout->addWidget(lineEditEasting);


    gridLayout3->addLayout(hboxLayout, 1, 2, 1, 1);

    hboxLayout1 = new QHBoxLayout();
    hboxLayout1->setObjectName(QString::fromUtf8("hboxLayout1"));
    label_22 = new QLabel(groupBoxManualSiteEntry);
    label_22->setObjectName(QString::fromUtf8("label_22"));

    hboxLayout1->addWidget(label_22);

    lineEditNorthing = new QLineEdit(groupBoxManualSiteEntry);
    lineEditNorthing->setObjectName(QString::fromUtf8("lineEditNorthing"));

    hboxLayout1->addWidget(lineEditNorthing);


    gridLayout3->addLayout(hboxLayout1, 2, 2, 1, 1);


    gridLayout1->addWidget(groupBoxManualSiteEntry, 0, 1, 1, 1);

    model_method_box = new QGroupBox(main_tab);
    model_method_box->setObjectName(QString::fromUtf8("model_method_box"));
    sizePolicy.setHeightForWidth(model_method_box->sizePolicy().hasHeightForWidth());
    model_method_box->setSizePolicy(sizePolicy);
    gridLayout4 = new QGridLayout(model_method_box);
    gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
    gridLayout4->setHorizontalSpacing(0);
    gridLayout4->setVerticalSpacing(0);
    gridLayout4->setContentsMargins(8, 8, 8, 8);
    hboxLayout2 = new QHBoxLayout();
    hboxLayout2->setSpacing(0);
    hboxLayout2->setObjectName(QString::fromUtf8("hboxLayout2"));
    label_2 = new QLabel(model_method_box);
    label_2->setObjectName(QString::fromUtf8("label_2"));
    label_2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    hboxLayout2->addWidget(label_2);

    sbModelPrecision = new QSpinBox(model_method_box);
    sbModelPrecision->setObjectName(QString::fromUtf8("sbModelPrecision"));
    sizePolicy.setHeightForWidth(sbModelPrecision->sizePolicy().hasHeightForWidth());
    sbModelPrecision->setSizePolicy(sizePolicy);
    sbModelPrecision->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    sbModelPrecision->setMinimum(1);
    sbModelPrecision->setMaximum(50);
    sbModelPrecision->setValue(5);

    hboxLayout2->addWidget(sbModelPrecision);


    gridLayout4->addLayout(hboxLayout2, 3, 0, 1, 1);

    radioButtonPathDistance = new QRadioButton(model_method_box);
    radioButtonPathDistance->setObjectName(QString::fromUtf8("radioButtonPathDistance"));

    gridLayout4->addWidget(radioButtonPathDistance, 2, 0, 1, 1);

    radioButtonWalkingTime = new QRadioButton(model_method_box);
    radioButtonWalkingTime->setObjectName(QString::fromUtf8("radioButtonWalkingTime"));
    radioButtonWalkingTime->setChecked(true);

    gridLayout4->addWidget(radioButtonWalkingTime, 1, 0, 1, 1);

    radioButtonEuclidean = new QRadioButton(model_method_box);
    radioButtonEuclidean->setObjectName(QString::fromUtf8("radioButtonEuclidean"));
    radioButtonEuclidean->setChecked(false);

    gridLayout4->addWidget(radioButtonEuclidean, 0, 0, 1, 1);


    gridLayout1->addWidget(model_method_box, 0, 2, 1, 1);

    gbxGrass = new QGroupBox(main_tab);
    gbxGrass->setObjectName(QString::fromUtf8("gbxGrass"));
    gridLayout5 = new QGridLayout(gbxGrass);
    gridLayout5->setObjectName(QString::fromUtf8("gridLayout5"));
    lblGrass = new QLabel(gbxGrass);
    lblGrass->setObjectName(QString::fromUtf8("lblGrass"));
    lblGrass->setMaximumSize(QSize(80, 80));
    lblGrass->setPixmap(QPixmap(QString::fromUtf8(":/icona_grass.gif")));
    lblGrass->setScaledContents(true);

    gridLayout5->addWidget(lblGrass, 0, 0, 2, 1);

    label_29 = new QLabel(gbxGrass);
    label_29->setObjectName(QString::fromUtf8("label_29"));
    QSizePolicy sizePolicy5(QSizePolicy::Fixed, QSizePolicy::Preferred);
    sizePolicy5.setHorizontalStretch(0);
    sizePolicy5.setVerticalStretch(0);
    sizePolicy5.setHeightForWidth(label_29->sizePolicy().hasHeightForWidth());
    label_29->setSizePolicy(sizePolicy5);

    gridLayout5->addWidget(label_29, 0, 1, 1, 1);

    cboMapSet = new QComboBox(gbxGrass);
    cboMapSet->setObjectName(QString::fromUtf8("cboMapSet"));

    gridLayout5->addWidget(cboMapSet, 0, 2, 1, 1);

    label_24 = new QLabel(gbxGrass);
    label_24->setObjectName(QString::fromUtf8("label_24"));
    sizePolicy5.setHeightForWidth(label_24->sizePolicy().hasHeightForWidth());
    label_24->setSizePolicy(sizePolicy5);
    label_24->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout5->addWidget(label_24, 1, 1, 1, 1);

    cboDEM = new QComboBox(gbxGrass);
    cboDEM->setObjectName(QString::fromUtf8("cboDEM"));

    gridLayout5->addWidget(cboDEM, 1, 2, 1, 1);


    gridLayout1->addWidget(gbxGrass, 1, 1, 1, 2);

    spacerItem3 = new QSpacerItem(308, 83, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout1->addItem(spacerItem3, 2, 1, 1, 1);

    MainTabs->addTab(main_tab, QString());
    diet_tab = new QWidget();
    diet_tab->setObjectName(QString::fromUtf8("diet_tab"));
    gridLayout6 = new QGridLayout(diet_tab);
    gridLayout6->setObjectName(QString::fromUtf8("gridLayout6"));
    spacerItem4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout6->addItem(spacerItem4, 1, 0, 1, 1);

    spacerItem5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout6->addItem(spacerItem5, 2, 1, 1, 1);

    diet_comp_box = new QGroupBox(diet_tab);
    diet_comp_box->setObjectName(QString::fromUtf8("diet_comp_box"));
    QSizePolicy sizePolicy6(QSizePolicy::Expanding, QSizePolicy::Fixed);
    sizePolicy6.setHorizontalStretch(0);
    sizePolicy6.setVerticalStretch(0);
    sizePolicy6.setHeightForWidth(diet_comp_box->sizePolicy().hasHeightForWidth());
    diet_comp_box->setSizePolicy(sizePolicy6);
    gridLayout7 = new QGridLayout(diet_comp_box);
    gridLayout7->setObjectName(QString::fromUtf8("gridLayout7"));
    hboxLayout3 = new QHBoxLayout();
    hboxLayout3->setObjectName(QString::fromUtf8("hboxLayout3"));
    cboxBaseOnPlants = new QCheckBox(diet_comp_box);
    cboxBaseOnPlants->setObjectName(QString::fromUtf8("cboxBaseOnPlants"));
    cboxBaseOnPlants->setEnabled(false);

    hboxLayout3->addWidget(cboxBaseOnPlants);

    spacerItem6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    hboxLayout3->addItem(spacerItem6);

    cboxIncludeDairy = new QCheckBox(diet_comp_box);
    cboxIncludeDairy->setObjectName(QString::fromUtf8("cboxIncludeDairy"));
    cboxIncludeDairy->setEnabled(false);
    cboxIncludeDairy->setLayoutDirection(Qt::RightToLeft);

    hboxLayout3->addWidget(cboxIncludeDairy);


    gridLayout7->addLayout(hboxLayout3, 0, 0, 1, 2);

    hboxLayout4 = new QHBoxLayout();
    hboxLayout4->setObjectName(QString::fromUtf8("hboxLayout4"));
    labelCropPercent = new QLabel(diet_comp_box);
    labelCropPercent->setObjectName(QString::fromUtf8("labelCropPercent"));

    hboxLayout4->addWidget(labelCropPercent);

    sliderDiet = new QSlider(diet_comp_box);
    sliderDiet->setObjectName(QString::fromUtf8("sliderDiet"));
    sliderDiet->setMaximum(100);
    sliderDiet->setSingleStep(1);
    sliderDiet->setPageStep(1);
    sliderDiet->setValue(50);
    sliderDiet->setSliderPosition(50);
    sliderDiet->setOrientation(Qt::Horizontal);
    sliderDiet->setTickPosition(QSlider::TicksBothSides);
    sliderDiet->setTickInterval(25);

    hboxLayout4->addWidget(sliderDiet);

    labelMeatPercent = new QLabel(diet_comp_box);
    labelMeatPercent->setObjectName(QString::fromUtf8("labelMeatPercent"));
    labelMeatPercent->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    hboxLayout4->addWidget(labelMeatPercent);


    gridLayout7->addLayout(hboxLayout4, 1, 0, 1, 2);

    groupplantpercent = new QGroupBox(diet_comp_box);
    groupplantpercent->setObjectName(QString::fromUtf8("groupplantpercent"));
    gridLayout8 = new QGridLayout(groupplantpercent);
    gridLayout8->setObjectName(QString::fromUtf8("gridLayout8"));
    spacerItem7 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout8->addItem(spacerItem7, 1, 1, 1, 1);

    labelCropTamePercent = new QLabel(groupplantpercent);
    labelCropTamePercent->setObjectName(QString::fromUtf8("labelCropTamePercent"));
    labelCropTamePercent->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout8->addWidget(labelCropTamePercent, 1, 2, 1, 1);

    sliderCrop = new QSlider(groupplantpercent);
    sliderCrop->setObjectName(QString::fromUtf8("sliderCrop"));
    sliderCrop->setMaximum(100);
    sliderCrop->setSingleStep(1);
    sliderCrop->setPageStep(1);
    sliderCrop->setValue(90);
    sliderCrop->setSliderPosition(90);
    sliderCrop->setOrientation(Qt::Horizontal);
    sliderCrop->setTickPosition(QSlider::TicksBelow);
    sliderCrop->setTickInterval(25);

    gridLayout8->addWidget(sliderCrop, 2, 0, 1, 3);

    labelCropWildPercent = new QLabel(groupplantpercent);
    labelCropWildPercent->setObjectName(QString::fromUtf8("labelCropWildPercent"));
    labelCropWildPercent->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

    gridLayout8->addWidget(labelCropWildPercent, 1, 0, 1, 1);

    label_9 = new QLabel(groupplantpercent);
    label_9->setObjectName(QString::fromUtf8("label_9"));
    label_9->setAlignment(Qt::AlignCenter);

    gridLayout8->addWidget(label_9, 0, 0, 1, 1);

    label_11 = new QLabel(groupplantpercent);
    label_11->setObjectName(QString::fromUtf8("label_11"));
    label_11->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout8->addWidget(label_11, 0, 2, 1, 1);

    spacerItem8 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout8->addItem(spacerItem8, 0, 1, 1, 1);


    gridLayout7->addWidget(groupplantpercent, 2, 0, 1, 1);

    groupmeatpercent = new QGroupBox(diet_comp_box);
    groupmeatpercent->setObjectName(QString::fromUtf8("groupmeatpercent"));
    groupmeatpercent->setLayoutDirection(Qt::RightToLeft);
    gridLayout9 = new QGridLayout(groupmeatpercent);
    gridLayout9->setObjectName(QString::fromUtf8("gridLayout9"));
    spacerItem9 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout9->addItem(spacerItem9, 1, 1, 1, 1);

    spacerItem10 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout9->addItem(spacerItem10, 0, 1, 1, 1);

    label_14 = new QLabel(groupmeatpercent);
    label_14->setObjectName(QString::fromUtf8("label_14"));
    label_14->setAlignment(Qt::AlignCenter);

    gridLayout9->addWidget(label_14, 0, 0, 1, 1);

    labelMeatWildPercent = new QLabel(groupmeatpercent);
    labelMeatWildPercent->setObjectName(QString::fromUtf8("labelMeatWildPercent"));
    labelMeatWildPercent->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout9->addWidget(labelMeatWildPercent, 1, 2, 1, 1);

    label_13 = new QLabel(groupmeatpercent);
    label_13->setObjectName(QString::fromUtf8("label_13"));
    label_13->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout9->addWidget(label_13, 0, 2, 1, 1);

    labelMeatTamePercent = new QLabel(groupmeatpercent);
    labelMeatTamePercent->setObjectName(QString::fromUtf8("labelMeatTamePercent"));
    labelMeatTamePercent->setLayoutDirection(Qt::LeftToRight);
    labelMeatTamePercent->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout9->addWidget(labelMeatTamePercent, 1, 0, 1, 1);

    sliderMeat = new QSlider(groupmeatpercent);
    sliderMeat->setObjectName(QString::fromUtf8("sliderMeat"));
    sliderMeat->setLayoutDirection(Qt::LeftToRight);
    sliderMeat->setMaximum(100);
    sliderMeat->setSingleStep(1);
    sliderMeat->setPageStep(1);
    sliderMeat->setValue(90);
    sliderMeat->setSliderPosition(90);
    sliderMeat->setOrientation(Qt::Horizontal);
    sliderMeat->setTickPosition(QSlider::TicksBelow);
    sliderMeat->setTickInterval(25);

    gridLayout9->addWidget(sliderMeat, 2, 0, 1, 3);


    gridLayout7->addWidget(groupmeatpercent, 2, 1, 1, 1);

    line = new QFrame(diet_comp_box);
    line->setObjectName(QString::fromUtf8("line"));
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    gridLayout7->addWidget(line, 3, 0, 1, 2);

    hboxLayout5 = new QHBoxLayout();
    hboxLayout5->setObjectName(QString::fromUtf8("hboxLayout5"));
    hboxLayout6 = new QHBoxLayout();
    hboxLayout6->setObjectName(QString::fromUtf8("hboxLayout6"));
    label6 = new QLabel(diet_comp_box);
    label6->setObjectName(QString::fromUtf8("label6"));
    label6->setWordWrap(false);

    hboxLayout6->addWidget(label6);

    sbDailyCalories = new QSpinBox(diet_comp_box);
    sbDailyCalories->setObjectName(QString::fromUtf8("sbDailyCalories"));
    sbDailyCalories->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    sbDailyCalories->setMinimum(1);
    sbDailyCalories->setMaximum(5000);
    sbDailyCalories->setSingleStep(1);
    sbDailyCalories->setValue(2500);

    hboxLayout6->addWidget(sbDailyCalories);


    hboxLayout5->addLayout(hboxLayout6);

    line_2 = new QFrame(diet_comp_box);
    line_2->setObjectName(QString::fromUtf8("line_2"));
    line_2->setFrameShape(QFrame::VLine);
    line_2->setFrameShadow(QFrame::Sunken);

    hboxLayout5->addWidget(line_2);

    hboxLayout7 = new QHBoxLayout();
    hboxLayout7->setObjectName(QString::fromUtf8("hboxLayout7"));
    label6_2 = new QLabel(diet_comp_box);
    label6_2->setObjectName(QString::fromUtf8("label6_2"));
    label6_2->setWordWrap(false);

    hboxLayout7->addWidget(label6_2);

    sbDairyUtilisation = new QSpinBox(diet_comp_box);
    sbDairyUtilisation->setObjectName(QString::fromUtf8("sbDairyUtilisation"));
    QSizePolicy sizePolicy7(QSizePolicy::Minimum, QSizePolicy::Fixed);
    sizePolicy7.setHorizontalStretch(0);
    sizePolicy7.setVerticalStretch(0);
    sizePolicy7.setHeightForWidth(sbDairyUtilisation->sizePolicy().hasHeightForWidth());
    sbDairyUtilisation->setSizePolicy(sizePolicy7);
    sbDairyUtilisation->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    sbDairyUtilisation->setMaximum(100);
    sbDairyUtilisation->setSingleStep(1);
    sbDairyUtilisation->setValue(100);

    hboxLayout7->addWidget(sbDairyUtilisation);

    line_8 = new QFrame(diet_comp_box);
    line_8->setObjectName(QString::fromUtf8("line_8"));
    line_8->setFrameShape(QFrame::VLine);
    line_8->setFrameShadow(QFrame::Sunken);

    hboxLayout7->addWidget(line_8);

    cboxLimitDairy = new QCheckBox(diet_comp_box);
    cboxLimitDairy->setObjectName(QString::fromUtf8("cboxLimitDairy"));

    hboxLayout7->addWidget(cboxLimitDairy);

    sbLimitDairyPercent = new QSpinBox(diet_comp_box);
    sbLimitDairyPercent->setObjectName(QString::fromUtf8("sbLimitDairyPercent"));
    sbLimitDairyPercent->setMaximum(100);

    hboxLayout7->addWidget(sbLimitDairyPercent);


    hboxLayout5->addLayout(hboxLayout7);


    gridLayout7->addLayout(hboxLayout5, 4, 0, 1, 2);

    spacerItem11 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout7->addItem(spacerItem11, 6, 1, 1, 1);

    labelDairySurplus = new QLabel(diet_comp_box);
    labelDairySurplus->setObjectName(QString::fromUtf8("labelDairySurplus"));

    gridLayout7->addWidget(labelDairySurplus, 5, 1, 1, 1);


    gridLayout6->addWidget(diet_comp_box, 0, 0, 1, 1);

    groupBox_2 = new QGroupBox(diet_tab);
    groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
    sizePolicy.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
    groupBox_2->setSizePolicy(sizePolicy);
    groupBox_2->setMinimumSize(QSize(0, 200));
    gridLayout10 = new QGridLayout(groupBox_2);
    gridLayout10->setObjectName(QString::fromUtf8("gridLayout10"));
    hboxLayout8 = new QHBoxLayout();
    hboxLayout8->setObjectName(QString::fromUtf8("hboxLayout8"));
    label_10 = new QLabel(groupBox_2);
    label_10->setObjectName(QString::fromUtf8("label_10"));

    hboxLayout8->addWidget(label_10);

    labelCaloriesSettlement = new QLabel(groupBox_2);
    labelCaloriesSettlement->setObjectName(QString::fromUtf8("labelCaloriesSettlement"));

    hboxLayout8->addWidget(labelCaloriesSettlement);

    label_37 = new QLabel(groupBox_2);
    label_37->setObjectName(QString::fromUtf8("label_37"));

    hboxLayout8->addWidget(label_37);


    gridLayout10->addLayout(hboxLayout8, 2, 0, 1, 1);

    hboxLayout9 = new QHBoxLayout();
    hboxLayout9->setObjectName(QString::fromUtf8("hboxLayout9"));
    label_12 = new QLabel(groupBox_2);
    label_12->setObjectName(QString::fromUtf8("label_12"));

    hboxLayout9->addWidget(label_12);

    labelPortionPlants = new QLabel(groupBox_2);
    labelPortionPlants->setObjectName(QString::fromUtf8("labelPortionPlants"));

    hboxLayout9->addWidget(labelPortionPlants);

    label_38 = new QLabel(groupBox_2);
    label_38->setObjectName(QString::fromUtf8("label_38"));

    hboxLayout9->addWidget(label_38);


    gridLayout10->addLayout(hboxLayout9, 4, 0, 1, 1);

    hboxLayout10 = new QHBoxLayout();
    hboxLayout10->setObjectName(QString::fromUtf8("hboxLayout10"));
    label_16 = new QLabel(groupBox_2);
    label_16->setObjectName(QString::fromUtf8("label_16"));

    hboxLayout10->addWidget(label_16);

    labelPortionMeat = new QLabel(groupBox_2);
    labelPortionMeat->setObjectName(QString::fromUtf8("labelPortionMeat"));

    hboxLayout10->addWidget(labelPortionMeat);

    label_39 = new QLabel(groupBox_2);
    label_39->setObjectName(QString::fromUtf8("label_39"));

    hboxLayout10->addWidget(label_39);


    gridLayout10->addLayout(hboxLayout10, 5, 0, 1, 1);

    hboxLayout11 = new QHBoxLayout();
    hboxLayout11->setObjectName(QString::fromUtf8("hboxLayout11"));
    label_54 = new QLabel(groupBox_2);
    label_54->setObjectName(QString::fromUtf8("label_54"));

    hboxLayout11->addWidget(label_54);

    labelPortionAllDairy = new QLabel(groupBox_2);
    labelPortionAllDairy->setObjectName(QString::fromUtf8("labelPortionAllDairy"));

    hboxLayout11->addWidget(labelPortionAllDairy);

    label_55 = new QLabel(groupBox_2);
    label_55->setObjectName(QString::fromUtf8("label_55"));

    hboxLayout11->addWidget(label_55);


    gridLayout10->addLayout(hboxLayout11, 6, 0, 1, 1);

    hboxLayout12 = new QHBoxLayout();
    hboxLayout12->setObjectName(QString::fromUtf8("hboxLayout12"));
    label_18 = new QLabel(groupBox_2);
    label_18->setObjectName(QString::fromUtf8("label_18"));

    hboxLayout12->addWidget(label_18);

    labelPortionCrops = new QLabel(groupBox_2);
    labelPortionCrops->setObjectName(QString::fromUtf8("labelPortionCrops"));

    hboxLayout12->addWidget(labelPortionCrops);

    label_40 = new QLabel(groupBox_2);
    label_40->setObjectName(QString::fromUtf8("label_40"));

    hboxLayout12->addWidget(label_40);


    gridLayout10->addLayout(hboxLayout12, 8, 0, 1, 1);

    hboxLayout13 = new QHBoxLayout();
    hboxLayout13->setObjectName(QString::fromUtf8("hboxLayout13"));
    label_19 = new QLabel(groupBox_2);
    label_19->setObjectName(QString::fromUtf8("label_19"));

    hboxLayout13->addWidget(label_19);

    labelPortionTameMeat = new QLabel(groupBox_2);
    labelPortionTameMeat->setObjectName(QString::fromUtf8("labelPortionTameMeat"));

    hboxLayout13->addWidget(labelPortionTameMeat);

    label_41 = new QLabel(groupBox_2);
    label_41->setObjectName(QString::fromUtf8("label_41"));

    hboxLayout13->addWidget(label_41);


    gridLayout10->addLayout(hboxLayout13, 9, 0, 1, 1);

    hboxLayout14 = new QHBoxLayout();
    hboxLayout14->setObjectName(QString::fromUtf8("hboxLayout14"));
    label_31 = new QLabel(groupBox_2);
    label_31->setObjectName(QString::fromUtf8("label_31"));

    hboxLayout14->addWidget(label_31);

    labelPortionDairy = new QLabel(groupBox_2);
    labelPortionDairy->setObjectName(QString::fromUtf8("labelPortionDairy"));

    hboxLayout14->addWidget(labelPortionDairy);

    label_42 = new QLabel(groupBox_2);
    label_42->setObjectName(QString::fromUtf8("label_42"));

    hboxLayout14->addWidget(label_42);


    gridLayout10->addLayout(hboxLayout14, 10, 0, 1, 1);

    hboxLayout15 = new QHBoxLayout();
    hboxLayout15->setObjectName(QString::fromUtf8("hboxLayout15"));
    label_51 = new QLabel(groupBox_2);
    label_51->setObjectName(QString::fromUtf8("label_51"));

    hboxLayout15->addWidget(label_51);

    labelPortionWildMeat = new QLabel(groupBox_2);
    labelPortionWildMeat->setObjectName(QString::fromUtf8("labelPortionWildMeat"));

    hboxLayout15->addWidget(labelPortionWildMeat);

    label_50 = new QLabel(groupBox_2);
    label_50->setObjectName(QString::fromUtf8("label_50"));

    hboxLayout15->addWidget(label_50);


    gridLayout10->addLayout(hboxLayout15, 12, 0, 1, 1);

    hboxLayout16 = new QHBoxLayout();
    hboxLayout16->setObjectName(QString::fromUtf8("hboxLayout16"));
    label_53 = new QLabel(groupBox_2);
    label_53->setObjectName(QString::fromUtf8("label_53"));

    hboxLayout16->addWidget(label_53);

    labelPortionWildPlants = new QLabel(groupBox_2);
    labelPortionWildPlants->setObjectName(QString::fromUtf8("labelPortionWildPlants"));

    hboxLayout16->addWidget(labelPortionWildPlants);

    label_52 = new QLabel(groupBox_2);
    label_52->setObjectName(QString::fromUtf8("label_52"));

    hboxLayout16->addWidget(label_52);


    gridLayout10->addLayout(hboxLayout16, 13, 0, 1, 1);

    hboxLayout17 = new QHBoxLayout();
    hboxLayout17->setObjectName(QString::fromUtf8("hboxLayout17"));
    label_23 = new QLabel(groupBox_2);
    label_23->setObjectName(QString::fromUtf8("label_23"));

    hboxLayout17->addWidget(label_23);

    labelCaloriesCrops = new QLabel(groupBox_2);
    labelCaloriesCrops->setObjectName(QString::fromUtf8("labelCaloriesCrops"));

    hboxLayout17->addWidget(labelCaloriesCrops);

    label_43 = new QLabel(groupBox_2);
    label_43->setObjectName(QString::fromUtf8("label_43"));

    hboxLayout17->addWidget(label_43);


    gridLayout10->addLayout(hboxLayout17, 15, 0, 1, 1);

    hboxLayout18 = new QHBoxLayout();
    hboxLayout18->setObjectName(QString::fromUtf8("hboxLayout18"));
    label_21 = new QLabel(groupBox_2);
    label_21->setObjectName(QString::fromUtf8("label_21"));

    hboxLayout18->addWidget(label_21);

    labelCaloriesTameMeat = new QLabel(groupBox_2);
    labelCaloriesTameMeat->setObjectName(QString::fromUtf8("labelCaloriesTameMeat"));

    hboxLayout18->addWidget(labelCaloriesTameMeat);

    label_44 = new QLabel(groupBox_2);
    label_44->setObjectName(QString::fromUtf8("label_44"));

    hboxLayout18->addWidget(label_44);


    gridLayout10->addLayout(hboxLayout18, 16, 0, 1, 1);

    hboxLayout19 = new QHBoxLayout();
    hboxLayout19->setObjectName(QString::fromUtf8("hboxLayout19"));
    label_35 = new QLabel(groupBox_2);
    label_35->setObjectName(QString::fromUtf8("label_35"));

    hboxLayout19->addWidget(label_35);

    labelCaloriesDairy = new QLabel(groupBox_2);
    labelCaloriesDairy->setObjectName(QString::fromUtf8("labelCaloriesDairy"));

    hboxLayout19->addWidget(labelCaloriesDairy);

    label_45 = new QLabel(groupBox_2);
    label_45->setObjectName(QString::fromUtf8("label_45"));

    hboxLayout19->addWidget(label_45);


    gridLayout10->addLayout(hboxLayout19, 17, 0, 1, 1);

    hboxLayout20 = new QHBoxLayout();
    hboxLayout20->setObjectName(QString::fromUtf8("hboxLayout20"));
    label_46 = new QLabel(groupBox_2);
    label_46->setObjectName(QString::fromUtf8("label_46"));

    hboxLayout20->addWidget(label_46);

    labelCaloriesWildMeat = new QLabel(groupBox_2);
    labelCaloriesWildMeat->setObjectName(QString::fromUtf8("labelCaloriesWildMeat"));

    hboxLayout20->addWidget(labelCaloriesWildMeat);

    label_47 = new QLabel(groupBox_2);
    label_47->setObjectName(QString::fromUtf8("label_47"));

    hboxLayout20->addWidget(label_47);


    gridLayout10->addLayout(hboxLayout20, 19, 0, 1, 1);

    hboxLayout21 = new QHBoxLayout();
    hboxLayout21->setObjectName(QString::fromUtf8("hboxLayout21"));
    label_48 = new QLabel(groupBox_2);
    label_48->setObjectName(QString::fromUtf8("label_48"));

    hboxLayout21->addWidget(label_48);

    labelCaloriesWildPlants = new QLabel(groupBox_2);
    labelCaloriesWildPlants->setObjectName(QString::fromUtf8("labelCaloriesWildPlants"));

    hboxLayout21->addWidget(labelCaloriesWildPlants);

    label_49 = new QLabel(groupBox_2);
    label_49->setObjectName(QString::fromUtf8("label_49"));

    hboxLayout21->addWidget(label_49);


    gridLayout10->addLayout(hboxLayout21, 20, 0, 1, 1);

    label_4 = new QLabel(groupBox_2);
    label_4->setObjectName(QString::fromUtf8("label_4"));
    label_4->setAlignment(Qt::AlignCenter);

    gridLayout10->addWidget(label_4, 0, 0, 1, 1);

    label_15 = new QLabel(groupBox_2);
    label_15->setObjectName(QString::fromUtf8("label_15"));
    label_15->setAlignment(Qt::AlignCenter);

    gridLayout10->addWidget(label_15, 3, 0, 1, 1);

    line_5 = new QFrame(groupBox_2);
    line_5->setObjectName(QString::fromUtf8("line_5"));
    line_5->setFrameShape(QFrame::HLine);
    line_5->setFrameShadow(QFrame::Sunken);

    gridLayout10->addWidget(line_5, 7, 0, 1, 1);

    label_20 = new QLabel(groupBox_2);
    label_20->setObjectName(QString::fromUtf8("label_20"));
    label_20->setAlignment(Qt::AlignCenter);

    gridLayout10->addWidget(label_20, 14, 0, 1, 1);

    line_4 = new QFrame(groupBox_2);
    line_4->setObjectName(QString::fromUtf8("line_4"));
    line_4->setFrameShape(QFrame::HLine);
    line_4->setFrameShadow(QFrame::Sunken);

    gridLayout10->addWidget(line_4, 18, 0, 1, 1);

    line_7 = new QFrame(groupBox_2);
    line_7->setObjectName(QString::fromUtf8("line_7"));
    line_7->setFrameShape(QFrame::HLine);
    line_7->setFrameShadow(QFrame::Sunken);

    gridLayout10->addWidget(line_7, 11, 0, 1, 1);

    hboxLayout22 = new QHBoxLayout();
    hboxLayout22->setObjectName(QString::fromUtf8("hboxLayout22"));
    label_8 = new QLabel(groupBox_2);
    label_8->setObjectName(QString::fromUtf8("label_8"));

    hboxLayout22->addWidget(label_8);

    labelCaloriesIndividual = new QLabel(groupBox_2);
    labelCaloriesIndividual->setObjectName(QString::fromUtf8("labelCaloriesIndividual"));

    hboxLayout22->addWidget(labelCaloriesIndividual);

    label_36 = new QLabel(groupBox_2);
    label_36->setObjectName(QString::fromUtf8("label_36"));

    hboxLayout22->addWidget(label_36);


    gridLayout10->addLayout(hboxLayout22, 1, 0, 1, 1);


    gridLayout6->addWidget(groupBox_2, 0, 1, 2, 1);

    MainTabs->addTab(diet_tab, QString());
    crops_tab = new QWidget();
    crops_tab->setObjectName(QString::fromUtf8("crops_tab"));
    gridLayout11 = new QGridLayout(crops_tab);
    gridLayout11->setObjectName(QString::fromUtf8("gridLayout11"));
    splitter_7 = new QSplitter(crops_tab);
    splitter_7->setObjectName(QString::fromUtf8("splitter_7"));
    splitter_7->setOrientation(Qt::Vertical);
    layoutWidget = new QWidget(splitter_7);
    layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
    hboxLayout23 = new QHBoxLayout(layoutWidget);
    hboxLayout23->setObjectName(QString::fromUtf8("hboxLayout23"));
    hboxLayout23->setContentsMargins(0, 0, 0, 0);
    tblCrops = new QTableWidget(layoutWidget);
    if (tblCrops->columnCount() < 3)
        tblCrops->setColumnCount(3);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblCrops->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblCrops->setHorizontalHeaderItem(1, __colItem1);
    QTableWidgetItem *__colItem2 = new QTableWidgetItem();
    tblCrops->setHorizontalHeaderItem(2, __colItem2);
    tblCrops->setObjectName(QString::fromUtf8("tblCrops"));
    tblCrops->setAlternatingRowColors(true);
    tblCrops->setSelectionMode(QAbstractItemView::SingleSelection);
    tblCrops->setSelectionBehavior(QAbstractItemView::SelectRows);
    tblCrops->setShowGrid(false);

    hboxLayout23->addWidget(tblCrops);

    lblCropPix = new QLabel(layoutWidget);
    lblCropPix->setObjectName(QString::fromUtf8("lblCropPix"));
    lblCropPix->setMinimumSize(QSize(128, 128));
    lblCropPix->setMaximumSize(QSize(128, 128));
    lblCropPix->setAlignment(Qt::AlignCenter);

    hboxLayout23->addWidget(lblCropPix);

    splitter_7->addWidget(layoutWidget);
    textBrowserCropDefinition = new QTextBrowser(splitter_7);
    textBrowserCropDefinition->setObjectName(QString::fromUtf8("textBrowserCropDefinition"));
    QSizePolicy sizePolicy8(QSizePolicy::Preferred, QSizePolicy::Preferred);
    sizePolicy8.setHorizontalStretch(0);
    sizePolicy8.setVerticalStretch(0);
    sizePolicy8.setHeightForWidth(textBrowserCropDefinition->sizePolicy().hasHeightForWidth());
    textBrowserCropDefinition->setSizePolicy(sizePolicy8);
    splitter_7->addWidget(textBrowserCropDefinition);

    gridLayout11->addWidget(splitter_7, 0, 0, 1, 2);

    gbCustomCropMask = new QGroupBox(crops_tab);
    gbCustomCropMask->setObjectName(QString::fromUtf8("gbCustomCropMask"));
    gbCustomCropMask->setCheckable(true);
    gbCustomCropMask->setChecked(false);
    gridLayout12 = new QGridLayout(gbCustomCropMask);
    gridLayout12->setObjectName(QString::fromUtf8("gridLayout12"));
    label_26 = new QLabel(gbCustomCropMask);
    label_26->setObjectName(QString::fromUtf8("label_26"));
    sizePolicy5.setHeightForWidth(label_26->sizePolicy().hasHeightForWidth());
    label_26->setSizePolicy(sizePolicy5);

    gridLayout12->addWidget(label_26, 0, 0, 1, 1);

    cboCommonCropRaster = new QComboBox(gbCustomCropMask);
    cboCommonCropRaster->setObjectName(QString::fromUtf8("cboCommonCropRaster"));

    gridLayout12->addWidget(cboCommonCropRaster, 0, 1, 1, 1);


    gridLayout11->addWidget(gbCustomCropMask, 1, 0, 1, 2);

    gbSlopeMaskCropLand = new QGroupBox(crops_tab);
    gbSlopeMaskCropLand->setObjectName(QString::fromUtf8("gbSlopeMaskCropLand"));
    gbSlopeMaskCropLand->setCheckable(true);
    gridLayout13 = new QGridLayout(gbSlopeMaskCropLand);
    gridLayout13->setObjectName(QString::fromUtf8("gridLayout13"));
    hboxLayout24 = new QHBoxLayout();
    hboxLayout24->setObjectName(QString::fromUtf8("hboxLayout24"));
    label_30 = new QLabel(gbSlopeMaskCropLand);
    label_30->setObjectName(QString::fromUtf8("label_30"));

    hboxLayout24->addWidget(label_30);

    dsbMinSlopeCropMask = new QDoubleSpinBox(gbSlopeMaskCropLand);
    dsbMinSlopeCropMask->setObjectName(QString::fromUtf8("dsbMinSlopeCropMask"));
    dsbMinSlopeCropMask->setButtonSymbols(QAbstractSpinBox::PlusMinus);

    hboxLayout24->addWidget(dsbMinSlopeCropMask);

    label_32 = new QLabel(gbSlopeMaskCropLand);
    label_32->setObjectName(QString::fromUtf8("label_32"));

    hboxLayout24->addWidget(label_32);


    gridLayout13->addLayout(hboxLayout24, 0, 0, 1, 1);


    gridLayout11->addWidget(gbSlopeMaskCropLand, 2, 0, 1, 1);

    vboxLayout = new QVBoxLayout();
    vboxLayout->setObjectName(QString::fromUtf8("vboxLayout"));
    pbnNewCropParameter = new QPushButton(crops_tab);
    pbnNewCropParameter->setObjectName(QString::fromUtf8("pbnNewCropParameter"));
    sizePolicy8.setHeightForWidth(pbnNewCropParameter->sizePolicy().hasHeightForWidth());
    pbnNewCropParameter->setSizePolicy(sizePolicy8);

    vboxLayout->addWidget(pbnNewCropParameter);

    pbnNewCrop = new QPushButton(crops_tab);
    pbnNewCrop->setObjectName(QString::fromUtf8("pbnNewCrop"));
    sizePolicy8.setHeightForWidth(pbnNewCrop->sizePolicy().hasHeightForWidth());
    pbnNewCrop->setSizePolicy(sizePolicy8);

    vboxLayout->addWidget(pbnNewCrop);


    gridLayout11->addLayout(vboxLayout, 2, 1, 1, 1);

    MainTabs->addTab(crops_tab, QString());
    animals_tab = new QWidget();
    animals_tab->setObjectName(QString::fromUtf8("animals_tab"));
    gridLayout14 = new QGridLayout(animals_tab);
    gridLayout14->setObjectName(QString::fromUtf8("gridLayout14"));
    splitter_3 = new QSplitter(animals_tab);
    splitter_3->setObjectName(QString::fromUtf8("splitter_3"));
    splitter_3->setOrientation(Qt::Vertical);
    layoutWidget1 = new QWidget(splitter_3);
    layoutWidget1->setObjectName(QString::fromUtf8("layoutWidget1"));
    gridLayout15 = new QGridLayout(layoutWidget1);
    gridLayout15->setObjectName(QString::fromUtf8("gridLayout15"));
    gridLayout15->setContentsMargins(0, 0, 0, 0);
    tblAnimals = new QTableWidget(layoutWidget1);
    if (tblAnimals->columnCount() < 4)
        tblAnimals->setColumnCount(4);
    QTableWidgetItem *__colItem3 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(0, __colItem3);
    QTableWidgetItem *__colItem4 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(1, __colItem4);
    QTableWidgetItem *__colItem5 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(2, __colItem5);
    QTableWidgetItem *__colItem6 = new QTableWidgetItem();
    tblAnimals->setHorizontalHeaderItem(3, __colItem6);
    tblAnimals->setObjectName(QString::fromUtf8("tblAnimals"));
    tblAnimals->setAlternatingRowColors(true);
    tblAnimals->setSelectionMode(QAbstractItemView::SingleSelection);
    tblAnimals->setSelectionBehavior(QAbstractItemView::SelectRows);
    tblAnimals->setShowGrid(false);

    gridLayout15->addWidget(tblAnimals, 0, 0, 2, 1);

    spacerItem12 = new QSpacerItem(20, 16, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout15->addItem(spacerItem12, 1, 1, 1, 1);

    lblAnimalPix = new QLabel(layoutWidget1);
    lblAnimalPix->setObjectName(QString::fromUtf8("lblAnimalPix"));
    lblAnimalPix->setMinimumSize(QSize(128, 128));
    lblAnimalPix->setMaximumSize(QSize(128, 128));
    lblAnimalPix->setAlignment(Qt::AlignCenter);

    gridLayout15->addWidget(lblAnimalPix, 0, 1, 1, 1);

    splitter_3->addWidget(layoutWidget1);
    textBrowserAnimalDefinition = new QTextBrowser(splitter_3);
    textBrowserAnimalDefinition->setObjectName(QString::fromUtf8("textBrowserAnimalDefinition"));
    splitter_3->addWidget(textBrowserAnimalDefinition);

    gridLayout14->addWidget(splitter_3, 0, 0, 1, 2);

    gbCustomMaskGrazingLand = new QGroupBox(animals_tab);
    gbCustomMaskGrazingLand->setObjectName(QString::fromUtf8("gbCustomMaskGrazingLand"));
    gbCustomMaskGrazingLand->setCheckable(true);
    gbCustomMaskGrazingLand->setChecked(false);
    gridLayout16 = new QGridLayout(gbCustomMaskGrazingLand);
    gridLayout16->setObjectName(QString::fromUtf8("gridLayout16"));
    label_25 = new QLabel(gbCustomMaskGrazingLand);
    label_25->setObjectName(QString::fromUtf8("label_25"));
    sizePolicy5.setHeightForWidth(label_25->sizePolicy().hasHeightForWidth());
    label_25->setSizePolicy(sizePolicy5);

    gridLayout16->addWidget(label_25, 0, 0, 1, 1);

    cboCommonGrazingRaster = new QComboBox(gbCustomMaskGrazingLand);
    cboCommonGrazingRaster->setObjectName(QString::fromUtf8("cboCommonGrazingRaster"));

    gridLayout16->addWidget(cboCommonGrazingRaster, 0, 1, 1, 1);


    gridLayout14->addWidget(gbCustomMaskGrazingLand, 1, 0, 1, 2);

    gbGenerateMaskGrazingLand = new QGroupBox(animals_tab);
    gbGenerateMaskGrazingLand->setObjectName(QString::fromUtf8("gbGenerateMaskGrazingLand"));
    gbGenerateMaskGrazingLand->setCheckable(true);
    gridLayout17 = new QGridLayout(gbGenerateMaskGrazingLand);
    gridLayout17->setObjectName(QString::fromUtf8("gridLayout17"));
    label_33 = new QLabel(gbGenerateMaskGrazingLand);
    label_33->setObjectName(QString::fromUtf8("label_33"));

    gridLayout17->addWidget(label_33, 0, 0, 1, 1);

    dsbMinimumSlopeGrazingMask = new QDoubleSpinBox(gbGenerateMaskGrazingLand);
    dsbMinimumSlopeGrazingMask->setObjectName(QString::fromUtf8("dsbMinimumSlopeGrazingMask"));
    dsbMinimumSlopeGrazingMask->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    dsbMinimumSlopeGrazingMask->setSingleStep(0.01);
    dsbMinimumSlopeGrazingMask->setValue(8);

    gridLayout17->addWidget(dsbMinimumSlopeGrazingMask, 0, 1, 1, 1);

    label_34 = new QLabel(gbGenerateMaskGrazingLand);
    label_34->setObjectName(QString::fromUtf8("label_34"));

    gridLayout17->addWidget(label_34, 0, 2, 1, 1);

    dsbMaximumSlopeGrazingMask = new QDoubleSpinBox(gbGenerateMaskGrazingLand);
    dsbMaximumSlopeGrazingMask->setObjectName(QString::fromUtf8("dsbMaximumSlopeGrazingMask"));
    dsbMaximumSlopeGrazingMask->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    dsbMaximumSlopeGrazingMask->setValue(13);

    gridLayout17->addWidget(dsbMaximumSlopeGrazingMask, 0, 3, 1, 1);


    gridLayout14->addWidget(gbGenerateMaskGrazingLand, 2, 0, 1, 2);

    gbFoodValue = new QGroupBox(animals_tab);
    gbFoodValue->setObjectName(QString::fromUtf8("gbFoodValue"));
    gridLayout18 = new QGridLayout(gbFoodValue);
    gridLayout18->setObjectName(QString::fromUtf8("gridLayout18"));
    sbCommonRasterValue = new QSpinBox(gbFoodValue);
    sbCommonRasterValue->setObjectName(QString::fromUtf8("sbCommonRasterValue"));
    sbCommonRasterValue->setButtonSymbols(QAbstractSpinBox::PlusMinus);
    sbCommonRasterValue->setMinimum(1);
    sbCommonRasterValue->setMaximum(5000);
    sbCommonRasterValue->setSingleStep(1);
    sbCommonRasterValue->setValue(8);

    gridLayout18->addWidget(sbCommonRasterValue, 0, 0, 1, 1);

    cbCommonLandEnergyType = new QComboBox(gbFoodValue);
    cbCommonLandEnergyType->setObjectName(QString::fromUtf8("cbCommonLandEnergyType"));

    gridLayout18->addWidget(cbCommonLandEnergyType, 0, 1, 1, 1);

    label_28 = new QLabel(gbFoodValue);
    label_28->setObjectName(QString::fromUtf8("label_28"));
    label_28->setAlignment(Qt::AlignCenter);

    gridLayout18->addWidget(label_28, 0, 2, 1, 1);

    cbAreaUnits = new QComboBox(gbFoodValue);
    cbAreaUnits->setObjectName(QString::fromUtf8("cbAreaUnits"));
    sizePolicy2.setHeightForWidth(cbAreaUnits->sizePolicy().hasHeightForWidth());
    cbAreaUnits->setSizePolicy(sizePolicy2);
    cbAreaUnits->setCursor(QCursor(Qt::PointingHandCursor));

    gridLayout18->addWidget(cbAreaUnits, 0, 3, 1, 1);

    label_27 = new QLabel(gbFoodValue);
    label_27->setObjectName(QString::fromUtf8("label_27"));

    gridLayout18->addWidget(label_27, 0, 4, 1, 1);


    gridLayout14->addWidget(gbFoodValue, 3, 0, 1, 1);

    vboxLayout1 = new QVBoxLayout();
    vboxLayout1->setObjectName(QString::fromUtf8("vboxLayout1"));
    pbnNewAnimal = new QPushButton(animals_tab);
    pbnNewAnimal->setObjectName(QString::fromUtf8("pbnNewAnimal"));
    sizePolicy8.setHeightForWidth(pbnNewAnimal->sizePolicy().hasHeightForWidth());
    pbnNewAnimal->setSizePolicy(sizePolicy8);

    vboxLayout1->addWidget(pbnNewAnimal);

    pbnNewAnimalParameter = new QPushButton(animals_tab);
    pbnNewAnimalParameter->setObjectName(QString::fromUtf8("pbnNewAnimalParameter"));
    sizePolicy8.setHeightForWidth(pbnNewAnimalParameter->sizePolicy().hasHeightForWidth());
    pbnNewAnimalParameter->setSizePolicy(sizePolicy8);

    vboxLayout1->addWidget(pbnNewAnimalParameter);


    gridLayout14->addLayout(vboxLayout1, 3, 1, 1, 1);

    MainTabs->addTab(animals_tab, QString());
    results_tab = new QWidget();
    results_tab->setObjectName(QString::fromUtf8("results_tab"));
    gridLayout19 = new QGridLayout(results_tab);
    gridLayout19->setObjectName(QString::fromUtf8("gridLayout19"));
    splitter_5 = new QSplitter(results_tab);
    splitter_5->setObjectName(QString::fromUtf8("splitter_5"));
    splitter_5->setOrientation(Qt::Horizontal);
    splitter_2 = new QSplitter(splitter_5);
    splitter_2->setObjectName(QString::fromUtf8("splitter_2"));
    splitter_2->setOrientation(Qt::Horizontal);
    layoutWidget2 = new QWidget(splitter_2);
    layoutWidget2->setObjectName(QString::fromUtf8("layoutWidget2"));
    vboxLayout2 = new QVBoxLayout(layoutWidget2);
    vboxLayout2->setObjectName(QString::fromUtf8("vboxLayout2"));
    vboxLayout2->setContentsMargins(0, 0, 0, 0);
    lblCropPicCalcs = new QLabel(layoutWidget2);
    lblCropPicCalcs->setObjectName(QString::fromUtf8("lblCropPicCalcs"));
    lblCropPicCalcs->setMinimumSize(QSize(70, 70));
    lblCropPicCalcs->setMaximumSize(QSize(70, 70));
    lblCropPicCalcs->setAlignment(Qt::AlignCenter);

    vboxLayout2->addWidget(lblCropPicCalcs);

    listWidgetCalculationsCrop = new QListWidget(layoutWidget2);
    listWidgetCalculationsCrop->setObjectName(QString::fromUtf8("listWidgetCalculationsCrop"));
    QSizePolicy sizePolicy9(QSizePolicy::Expanding, QSizePolicy::Expanding);
    sizePolicy9.setHorizontalStretch(0);
    sizePolicy9.setVerticalStretch(0);
    sizePolicy9.setHeightForWidth(listWidgetCalculationsCrop->sizePolicy().hasHeightForWidth());
    listWidgetCalculationsCrop->setSizePolicy(sizePolicy9);
    listWidgetCalculationsCrop->setMinimumSize(QSize(70, 0));

    vboxLayout2->addWidget(listWidgetCalculationsCrop);

    splitter_2->addWidget(layoutWidget2);
    textBrowserResultsCrop = new QTextBrowser(splitter_2);
    textBrowserResultsCrop->setObjectName(QString::fromUtf8("textBrowserResultsCrop"));
    sizePolicy9.setHeightForWidth(textBrowserResultsCrop->sizePolicy().hasHeightForWidth());
    textBrowserResultsCrop->setSizePolicy(sizePolicy9);
    splitter_2->addWidget(textBrowserResultsCrop);
    splitter_5->addWidget(splitter_2);
    splitter_4 = new QSplitter(splitter_5);
    splitter_4->setObjectName(QString::fromUtf8("splitter_4"));
    splitter_4->setOrientation(Qt::Horizontal);
    layoutWidget3 = new QWidget(splitter_4);
    layoutWidget3->setObjectName(QString::fromUtf8("layoutWidget3"));
    vboxLayout3 = new QVBoxLayout(layoutWidget3);
    vboxLayout3->setObjectName(QString::fromUtf8("vboxLayout3"));
    vboxLayout3->setContentsMargins(0, 0, 0, 0);
    lblAnimalPicCalcs = new QLabel(layoutWidget3);
    lblAnimalPicCalcs->setObjectName(QString::fromUtf8("lblAnimalPicCalcs"));
    lblAnimalPicCalcs->setMinimumSize(QSize(70, 70));
    lblAnimalPicCalcs->setMaximumSize(QSize(70, 70));
    lblAnimalPicCalcs->setAlignment(Qt::AlignCenter);

    vboxLayout3->addWidget(lblAnimalPicCalcs);

    listWidgetCalculationsAnimal = new QListWidget(layoutWidget3);
    listWidgetCalculationsAnimal->setObjectName(QString::fromUtf8("listWidgetCalculationsAnimal"));
    sizePolicy9.setHeightForWidth(listWidgetCalculationsAnimal->sizePolicy().hasHeightForWidth());
    listWidgetCalculationsAnimal->setSizePolicy(sizePolicy9);
    listWidgetCalculationsAnimal->setMinimumSize(QSize(70, 0));

    vboxLayout3->addWidget(listWidgetCalculationsAnimal);

    splitter_4->addWidget(layoutWidget3);
    textBrowserResultsAnimals = new QTextBrowser(splitter_4);
    textBrowserResultsAnimals->setObjectName(QString::fromUtf8("textBrowserResultsAnimals"));
    sizePolicy6.setHeightForWidth(textBrowserResultsAnimals->sizePolicy().hasHeightForWidth());
    textBrowserResultsAnimals->setSizePolicy(sizePolicy6);
    splitter_4->addWidget(textBrowserResultsAnimals);
    splitter_5->addWidget(splitter_4);

    gridLayout19->addWidget(splitter_5, 0, 0, 1, 6);

    spacerItem13 = new QSpacerItem(341, 27, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout19->addItem(spacerItem13, 1, 0, 1, 1);

    pbnTargets = new QPushButton(results_tab);
    pbnTargets->setObjectName(QString::fromUtf8("pbnTargets"));

    gridLayout19->addWidget(pbnTargets, 1, 1, 1, 1);

    pbnFallow = new QPushButton(results_tab);
    pbnFallow->setObjectName(QString::fromUtf8("pbnFallow"));

    gridLayout19->addWidget(pbnFallow, 1, 2, 1, 1);

    pbnHerds = new QPushButton(results_tab);
    pbnHerds->setObjectName(QString::fromUtf8("pbnHerds"));

    gridLayout19->addWidget(pbnHerds, 1, 3, 1, 1);

    pbnText = new QPushButton(results_tab);
    pbnText->setObjectName(QString::fromUtf8("pbnText"));

    gridLayout19->addWidget(pbnText, 1, 4, 1, 1);

    pbnHtml = new QPushButton(results_tab);
    pbnHtml->setObjectName(QString::fromUtf8("pbnHtml"));

    gridLayout19->addWidget(pbnHtml, 1, 5, 1, 1);

    MainTabs->addTab(results_tab, QString());
    tab = new QWidget();
    tab->setObjectName(QString::fromUtf8("tab"));
    gridLayout20 = new QGridLayout(tab);
    gridLayout20->setObjectName(QString::fromUtf8("gridLayout20"));
    splitter_6 = new QSplitter(tab);
    splitter_6->setObjectName(QString::fromUtf8("splitter_6"));
    splitter_6->setOrientation(Qt::Horizontal);
    tbReport = new QTextBrowser(splitter_6);
    tbReport->setObjectName(QString::fromUtf8("tbReport"));
    sizePolicy.setHeightForWidth(tbReport->sizePolicy().hasHeightForWidth());
    tbReport->setSizePolicy(sizePolicy);
    splitter_6->addWidget(tbReport);

    gridLayout20->addWidget(splitter_6, 0, 0, 1, 1);

    MainTabs->addTab(tab, QString());
    tabLogs = new QWidget();
    tabLogs->setObjectName(QString::fromUtf8("tabLogs"));
    gridLayout21 = new QGridLayout(tabLogs);
    gridLayout21->setObjectName(QString::fromUtf8("gridLayout21"));
    tbLogs = new QTextBrowser(tabLogs);
    tbLogs->setObjectName(QString::fromUtf8("tbLogs"));

    gridLayout21->addWidget(tbLogs, 0, 0, 1, 1);

    MainTabs->addTab(tabLogs, QString());
    help_tab = new QWidget();
    help_tab->setObjectName(QString::fromUtf8("help_tab"));
    gridLayout22 = new QGridLayout(help_tab);
    gridLayout22->setObjectName(QString::fromUtf8("gridLayout22"));
    splitter = new QSplitter(help_tab);
    splitter->setObjectName(QString::fromUtf8("splitter"));
    splitter->setOrientation(Qt::Horizontal);
    layoutWidget4 = new QWidget(splitter);
    layoutWidget4->setObjectName(QString::fromUtf8("layoutWidget4"));
    vboxLayout4 = new QVBoxLayout(layoutWidget4);
    vboxLayout4->setSpacing(1);
    vboxLayout4->setObjectName(QString::fromUtf8("vboxLayout4"));
    vboxLayout4->setContentsMargins(0, 0, 0, 0);
    treeHelp = new QTreeWidget(layoutWidget4);
    QTreeWidgetItem *__treeItem = new QTreeWidgetItem(treeHelp);
    QTreeWidgetItem *__treeItem1 = new QTreeWidgetItem(__treeItem);
    QTreeWidgetItem *__treeItem2 = new QTreeWidgetItem(__treeItem1);
    new QTreeWidgetItem(__treeItem2);
    new QTreeWidgetItem(__treeItem2);
    new QTreeWidgetItem(__treeItem2);

    QTreeWidgetItem *__treeItem3 = new QTreeWidgetItem(__treeItem1);
    new QTreeWidgetItem(__treeItem3);
    new QTreeWidgetItem(__treeItem3);
    new QTreeWidgetItem(__treeItem3);

    QTreeWidgetItem *__treeItem4 = new QTreeWidgetItem(__treeItem1);
    new QTreeWidgetItem(__treeItem4);
    new QTreeWidgetItem(__treeItem4);
    new QTreeWidgetItem(__treeItem4);
    new QTreeWidgetItem(__treeItem4);


    QTreeWidgetItem *__treeItem5 = new QTreeWidgetItem(__treeItem);
    new QTreeWidgetItem(__treeItem5);
    new QTreeWidgetItem(__treeItem5);
    new QTreeWidgetItem(__treeItem5);
    new QTreeWidgetItem(__treeItem5);
    new QTreeWidgetItem(__treeItem5);

    QTreeWidgetItem *__treeItem6 = new QTreeWidgetItem(__treeItem);
    new QTreeWidgetItem(__treeItem6);
    QTreeWidgetItem *__treeItem7 = new QTreeWidgetItem(__treeItem6);
    new QTreeWidgetItem(__treeItem7);
    new QTreeWidgetItem(__treeItem7);
    new QTreeWidgetItem(__treeItem7);
    QTreeWidgetItem *__treeItem8 = new QTreeWidgetItem(__treeItem7);
    new QTreeWidgetItem(__treeItem8);
    new QTreeWidgetItem(__treeItem8);
    QTreeWidgetItem *__treeItem9 = new QTreeWidgetItem(__treeItem8);
    new QTreeWidgetItem(__treeItem9);

    QTreeWidgetItem *__treeItem10 = new QTreeWidgetItem(__treeItem8);
    new QTreeWidgetItem(__treeItem10);

    new QTreeWidgetItem(__treeItem8);


    QTreeWidgetItem *__treeItem11 = new QTreeWidgetItem(__treeItem6);
    QTreeWidgetItem *__treeItem12 = new QTreeWidgetItem(__treeItem11);
    new QTreeWidgetItem(__treeItem12);
    new QTreeWidgetItem(__treeItem12);
    new QTreeWidgetItem(__treeItem12);
    new QTreeWidgetItem(__treeItem12);

    QTreeWidgetItem *__treeItem13 = new QTreeWidgetItem(__treeItem11);
    new QTreeWidgetItem(__treeItem13);
    new QTreeWidgetItem(__treeItem13);

    QTreeWidgetItem *__treeItem14 = new QTreeWidgetItem(__treeItem11);
    new QTreeWidgetItem(__treeItem14);
    new QTreeWidgetItem(__treeItem14);



    QTreeWidgetItem *__treeItem15 = new QTreeWidgetItem(__treeItem);
    new QTreeWidgetItem(__treeItem15);
    QTreeWidgetItem *__treeItem16 = new QTreeWidgetItem(__treeItem15);
    new QTreeWidgetItem(__treeItem16);
    new QTreeWidgetItem(__treeItem16);
    new QTreeWidgetItem(__treeItem16);
    QTreeWidgetItem *__treeItem17 = new QTreeWidgetItem(__treeItem16);
    QTreeWidgetItem *__treeItem18 = new QTreeWidgetItem(__treeItem17);
    new QTreeWidgetItem(__treeItem18);
    new QTreeWidgetItem(__treeItem18);
    new QTreeWidgetItem(__treeItem18);
    new QTreeWidgetItem(__treeItem18);
    new QTreeWidgetItem(__treeItem18);
    new QTreeWidgetItem(__treeItem18);

    QTreeWidgetItem *__treeItem19 = new QTreeWidgetItem(__treeItem17);
    new QTreeWidgetItem(__treeItem19);
    new QTreeWidgetItem(__treeItem19);
    new QTreeWidgetItem(__treeItem19);
    new QTreeWidgetItem(__treeItem19);
    new QTreeWidgetItem(__treeItem19);
    new QTreeWidgetItem(__treeItem19);

    QTreeWidgetItem *__treeItem20 = new QTreeWidgetItem(__treeItem17);
    QTreeWidgetItem *__treeItem21 = new QTreeWidgetItem(__treeItem20);
    new QTreeWidgetItem(__treeItem21);
    new QTreeWidgetItem(__treeItem21);
    new QTreeWidgetItem(__treeItem21);




    QTreeWidgetItem *__treeItem22 = new QTreeWidgetItem(__treeItem15);
    new QTreeWidgetItem(__treeItem22);
    QTreeWidgetItem *__treeItem23 = new QTreeWidgetItem(__treeItem22);
    new QTreeWidgetItem(__treeItem23);
    new QTreeWidgetItem(__treeItem23);
    new QTreeWidgetItem(__treeItem23);
    new QTreeWidgetItem(__treeItem23);

    QTreeWidgetItem *__treeItem24 = new QTreeWidgetItem(__treeItem22);
    QTreeWidgetItem *__treeItem25 = new QTreeWidgetItem(__treeItem24);
    new QTreeWidgetItem(__treeItem25);

    QTreeWidgetItem *__treeItem26 = new QTreeWidgetItem(__treeItem24);
    new QTreeWidgetItem(__treeItem26);

    new QTreeWidgetItem(__treeItem24);

    QTreeWidgetItem *__treeItem27 = new QTreeWidgetItem(__treeItem22);
    QTreeWidgetItem *__treeItem28 = new QTreeWidgetItem(__treeItem27);
    new QTreeWidgetItem(__treeItem28);
    new QTreeWidgetItem(__treeItem28);


    QTreeWidgetItem *__treeItem29 = new QTreeWidgetItem(__treeItem22);
    new QTreeWidgetItem(__treeItem29);
    new QTreeWidgetItem(__treeItem29);



    new QTreeWidgetItem(__treeItem);
    new QTreeWidgetItem(__treeItem);

    QTreeWidgetItem *__treeItem30 = new QTreeWidgetItem(treeHelp);
    QTreeWidgetItem *__treeItem31 = new QTreeWidgetItem(__treeItem30);
    new QTreeWidgetItem(__treeItem31);
    QTreeWidgetItem *__treeItem32 = new QTreeWidgetItem(__treeItem31);
    new QTreeWidgetItem(__treeItem32);
    new QTreeWidgetItem(__treeItem32);


    new QTreeWidgetItem(__treeItem30);


    treeHelp->setObjectName(QString::fromUtf8("treeHelp"));
    QSizePolicy sizePolicy10(QSizePolicy::Fixed, QSizePolicy::Expanding);
    sizePolicy10.setHorizontalStretch(0);
    sizePolicy10.setVerticalStretch(0);
    sizePolicy10.setHeightForWidth(treeHelp->sizePolicy().hasHeightForWidth());
    treeHelp->setSizePolicy(sizePolicy10);
    treeHelp->setMaximumSize(QSize(16777215, 16777215));

    vboxLayout4->addWidget(treeHelp);

    cbDebug = new QCheckBox(layoutWidget4);
    cbDebug->setObjectName(QString::fromUtf8("cbDebug"));

    vboxLayout4->addWidget(cbDebug);

    splitter->addWidget(layoutWidget4);
    textHelp = new QTextBrowser(splitter);
    textHelp->setObjectName(QString::fromUtf8("textHelp"));
    QSizePolicy sizePolicy11(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy11.setHorizontalStretch(255);
    sizePolicy11.setVerticalStretch(0);
    sizePolicy11.setHeightForWidth(textHelp->sizePolicy().hasHeightForWidth());
    textHelp->setSizePolicy(sizePolicy11);
    splitter->addWidget(textHelp);

    gridLayout22->addWidget(splitter, 0, 0, 1, 1);

    MainTabs->addTab(help_tab, QString());

    gridLayout->addWidget(MainTabs, 0, 0, 1, 11);

    QWidget::setTabOrder(lineEditSiteName, lineEditPeriod);
    QWidget::setTabOrder(lineEditPeriod, sbPopulation);
    QWidget::setTabOrder(sbPopulation, lineEditEasting);
    QWidget::setTabOrder(lineEditEasting, lineEditNorthing);
    QWidget::setTabOrder(lineEditNorthing, radioButtonEuclidean);
    QWidget::setTabOrder(radioButtonEuclidean, radioButtonWalkingTime);
    QWidget::setTabOrder(radioButtonWalkingTime, radioButtonPathDistance);
    QWidget::setTabOrder(radioButtonPathDistance, sbModelPrecision);
    QWidget::setTabOrder(sbModelPrecision, cboMapSet);
    QWidget::setTabOrder(cboMapSet, cboDEM);
    QWidget::setTabOrder(cboDEM, pushButtonRun);
    QWidget::setTabOrder(pushButtonRun, pushButtonLoad);
    QWidget::setTabOrder(pushButtonLoad, pushButtonSave);
    QWidget::setTabOrder(pushButtonSave, pushButtonExit);
    QWidget::setTabOrder(pushButtonExit, sliderDiet);
    QWidget::setTabOrder(sliderDiet, sliderCrop);
    QWidget::setTabOrder(sliderCrop, sliderMeat);
    QWidget::setTabOrder(sliderMeat, sbDailyCalories);
    QWidget::setTabOrder(sbDailyCalories, tblCrops);
    QWidget::setTabOrder(tblCrops, textBrowserCropDefinition);
    QWidget::setTabOrder(textBrowserCropDefinition, cboCommonCropRaster);
    QWidget::setTabOrder(cboCommonCropRaster, pbnNewCrop);
    QWidget::setTabOrder(pbnNewCrop, pbnNewCropParameter);
    QWidget::setTabOrder(pbnNewCropParameter, tblAnimals);
    QWidget::setTabOrder(tblAnimals, textBrowserAnimalDefinition);
    QWidget::setTabOrder(textBrowserAnimalDefinition, cboCommonGrazingRaster);
    QWidget::setTabOrder(cboCommonGrazingRaster, sbCommonRasterValue);
    QWidget::setTabOrder(sbCommonRasterValue, cbAreaUnits);
    QWidget::setTabOrder(cbAreaUnits, pbnNewAnimal);
    QWidget::setTabOrder(pbnNewAnimal, pbnNewAnimalParameter);
    QWidget::setTabOrder(pbnNewAnimalParameter, listWidgetCalculationsCrop);
    QWidget::setTabOrder(listWidgetCalculationsCrop, textBrowserResultsCrop);
    QWidget::setTabOrder(textBrowserResultsCrop, listWidgetCalculationsAnimal);
    QWidget::setTabOrder(listWidgetCalculationsAnimal, textBrowserResultsAnimals);
    QWidget::setTabOrder(textBrowserResultsAnimals, pbnTargets);
    QWidget::setTabOrder(pbnTargets, pbnFallow);
    QWidget::setTabOrder(pbnFallow, pbnHerds);
    QWidget::setTabOrder(pbnHerds, pbnText);
    QWidget::setTabOrder(pbnText, pbnHtml);
    QWidget::setTabOrder(pbnHtml, tbReport);
    QWidget::setTabOrder(tbReport, tbLogs);
    QWidget::setTabOrder(tbLogs, treeHelp);
    QWidget::setTabOrder(treeHelp, cbDebug);
    QWidget::setTabOrder(cbDebug, textHelp);

    retranslateUi(LaMainFormBase);

    MainTabs->setCurrentIndex(0);


    QMetaObject::connectSlotsByName(LaMainFormBase);
    } // setupUi

    void retranslateUi(QDialog *LaMainFormBase)
    {
    LaMainFormBase->setWindowTitle(QApplication::translate("LaMainFormBase", "Landuse Analyst", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    label_5->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the animals being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    label_5->setText(QApplication::translate("LaMainFormBase", "Animals:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelAnimalCheck->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the animals being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelAnimalCheck->setText(QApplication::translate("LaMainFormBase", "100%", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    label_3->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the crops being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    label_3->setText(QApplication::translate("LaMainFormBase", "  Crops:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelCropCheck->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the sum of percent of diet figures for all of the crops being used in the model.  <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">This must be 100%</span> to run!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelCropCheck->setText(QApplication::translate("LaMainFormBase", "100%", 0, QApplication::UnicodeUTF8));
    label_7->setText(QApplication::translate("LaMainFormBase", "Copyright 2008 Jason Jorgenson", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pushButtonRun->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Run the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pushButtonRun->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pressing Calculate! will attempt to run the model with the parameters you have chosen.  If there are any errors, this process will fail, and indicate to you what the problem was.  To be on the safe side, always save your model before attempting to Calculate! it.  All results will be saved if the model runs correctly.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pushButtonRun->setText(QApplication::translate("LaMainFormBase", "Run", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pushButtonLoad->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Load previously saved model parameters.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pushButtonLoad->setText(QApplication::translate("LaMainFormBase", "Load", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pushButtonSave->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save all settings of this model to a file</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pushButtonSave->setText(QApplication::translate("LaMainFormBase", "Save", 0, QApplication::UnicodeUTF8));
    pushButtonExit->setText(QApplication::translate("LaMainFormBase", "Exit", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    progressBarCalcs->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shows when program is busy, or progress of tasks.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    progressBarCalcs->setFormat(QApplication::translate("LaMainFormBase", "%p%", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    frame_2->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">To learn more about a feature or field in LandUse Analyst, you can do one of four things.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. <span style=\" font-size:10pt; color:#0000ff;\">Hover over it</span> with your mouse arrow for a brief description (like you are doing now to see this)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Click the <span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">?</span> i"
        "n the top right of the main window and then click on the item you want detailed help for.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. RIght Click on the thing you want help for.  If there is detailed help for it, you will see a <span style=\" font-weight:600; color:#0000ff;\">What is this?</span> option that you can then click on.  Again, you can click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Go to the <span style=\" font-weight:600; color:#0000ff;\">Help</span> <span style=\" font-weight:600; color:#0000ff;\">Tab</span> and click on the item you want help with on the left for an even more detailed description of what things"
        " are and how they work</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    frame_2->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst is a program that attempts to identify how much of the land surrounding an archaeological site would have been needed to sustain its population. <a href=\"http://www.arkygeek.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Land Analyst</span></a>, is Free Open Source Software (FOSS). That means that this program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_17->setText(QString());
    lblVersion->setText(QApplication::translate("LaMainFormBase", "Version: 99.99", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    groupBoxManualSiteEntry->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The information entered here will be inserted as Meta-Data into the resulting maps.  However, Name and Period are optional.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    groupBoxManualSiteEntry->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The name of the site, it's period, and the estimated population.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxManualSiteEntry->setTitle(QApplication::translate("LaMainFormBase", "Settlement Information", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    lineEditSiteName->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the site you are modelling here. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    lineEditSiteName->setText(QApplication::translate("LaMainFormBase", "Shuna", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbPopulation->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Estimated population of the settlement (required)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    textLabel2_4->setText(QApplication::translate("LaMainFormBase", "Name:", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaMainFormBase", "Period", 0, QApplication::UnicodeUTF8));
    label5->setText(QApplication::translate("LaMainFormBase", "Pop'n", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    label_6->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    label_6->setText(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">E</span></p></body></html>", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    lineEditEasting->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easting (required)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    lineEditEasting->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Easting of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    lineEditEasting->setText(QApplication::translate("LaMainFormBase", "744800", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    label_22->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    label_22->setText(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">N</span></p></body></html>", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    lineEditNorthing->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Northing (required)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    lineEditNorthing->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Northing of the site. Be sure you are using the same coordinate system as you do when creating your land suitability mask files!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    lineEditNorthing->setText(QApplication::translate("LaMainFormBase", "3611100", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    model_method_box->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analyst currently offers three types of analysis. Here you select which one you want to use.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Euclidean method starts looking for suitable land at the site and moves outwards from that point 'as the crow flies'. In other words, using Euclidean geometry (or even more simply, it draws circles!)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Walking Time method uses the same basic principle except that it moves outward from t"
        "he site based on walking time instead of distance. This method is probably the most realistic scenario to run, but it is interesting to compare the results of the three different methods.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Path Distance is very similar to Eucidean, except that this method considers topography when calculating distance from the site.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    model_method_box->setTitle(QApplication::translate("LaMainFormBase", "Modelling Method", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    label_2->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    label_2->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_2->setText(QApplication::translate("LaMainFormBase", "Precision: ", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbModelPrecision->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The smaller the value, the longer it will take to calculate the results!</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbModelPrecision->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Landuse Analyst finds suitable land contained with a boundary around the site. This boundary is different for each modelling method, but the process is identical. Once this boundary has been determined, it looks inside and calcualtes the total area of suitable land and compares it to the Area Target. If the area of suitable land contained within this boundary falls within the range set by Model Precision, it has found the solution. If it is under this range, however, the boundary is moved outwards, and the process repeats until enough suitable land has been found.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    radioButtonPathDistance->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate catchment by growing distance based on path distance (considers topography)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    radioButtonPathDistance->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Path Distance is selected, a cost map for the area is created that calculates how far it is  to all areas of the map from the site.  This is very similar to Eucidean, except that path distance considers topography.  The program then calculates area contained within a certain distance of the site.  If the derived area is insufficient to support the population, the distance is increased, and it tries again.  This repeats until the required area is contained.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    radioButtonPathDistance->setText(QApplication::translate("LaMainFormBase", "Path Distance", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    radioButtonWalkingTime->setToolTip(QApplication::translate("LaMainFormBase", "Calculate catchment by growing distance based on walking time", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    radioButtonWalkingTime->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Walking Time is selected, a cost map for the area is created that predicts how long it takes to get to any area on the map from the settlement.  The program then calculates the suitable area contained within the time it takes to walk.  If the derived area is insufficient to support the population, the walking time is increased, and it tries again.  This repeats until the required area is contained.  This method is probably the most realistic scenario to run, but it is interesting to compare the results of the three different methods.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    radioButtonWalkingTime->setText(QApplication::translate("LaMainFormBase", "Walking Time", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    radioButtonEuclidean->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate catchment by growing distance based on distance from the site ('as the crow flies')</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    radioButtonEuclidean->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When Euclidean is selected, a cost map for the area is created that calculates how far it is  to all areas of the map from the site.  This distance does NOT consider topography.  In other words, it is simply as the crow flies.  The program then calculates area contained within a certain distance of the site.  If the derived area is insufficient to support the population, the distance is increased, and it tries again.  This repeats until the required area is contained.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    radioButtonEuclidean->setText(QApplication::translate("LaMainFormBase", "Euclidean", 0, QApplication::UnicodeUTF8));
    gbxGrass->setTitle(QString());
    lblGrass->setText(QString());
    label_29->setText(QApplication::translate("LaMainFormBase", "Mapset:", 0, QApplication::UnicodeUTF8));
    label_24->setText(QApplication::translate("LaMainFormBase", "DEM: ", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(main_tab), QApplication::translate("LaMainFormBase", "Main", 0, QApplication::UnicodeUTF8));
    diet_comp_box->setTitle(QApplication::translate("LaMainFormBase", "Dietary Composition Percentages (Calories!)", 0, QApplication::UnicodeUTF8));
    cboxBaseOnPlants->setText(QApplication::translate("LaMainFormBase", "Base Calcs on Plant Percentage", 0, QApplication::UnicodeUTF8));
    cboxIncludeDairy->setText(QApplication::translate("LaMainFormBase", "Include Calories from Dairy", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelCropPercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from plants.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelCropPercent->setText(QApplication::translate("LaMainFormBase", "50", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sliderDiet->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Plant:Meat plants in the diet (calories)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sliderDiet->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the overall division in the diet as a ratio between calories provided by <span style=\" font-weight:600; color:#0000ff;\">Plants</span> and calories provided by <span style=\" font-weight:600; color:#0000ff;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes food from both wild and tame sources.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-t"
        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Plant to Meat Ratio is the primary distinction you must make when defining the settlements diet. This setting relies on the assumption that all food comes from either plants or animals, regardless of whether or not it is tame or wild. <span style=\" font-weight:600; color:#0000ff;\">Note that this setting is based on calories</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    labelMeatPercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the populations diet that is supplied by food that comes from animals.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelMeatPercent->setText(QApplication::translate("LaMainFormBase", "50", 0, QApplication::UnicodeUTF8));
    groupplantpercent->setTitle(QApplication::translate("LaMainFormBase", "PLANT", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelCropTamePercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by domesticated plants (crops).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelCropTamePercent->setText(QApplication::translate("LaMainFormBase", "90", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sliderCrop->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame plants in the plant portion of the diet (calories)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sliderCrop->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    labelCropWildPercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">plant</span> portion of the diet that is supplied by non-domesticated plants.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelCropWildPercent->setText(QApplication::translate("LaMainFormBase", "10", 0, QApplication::UnicodeUTF8));
    label_9->setText(QApplication::translate("LaMainFormBase", "Wild", 0, QApplication::UnicodeUTF8));
    label_11->setText(QApplication::translate("LaMainFormBase", "Domestic", 0, QApplication::UnicodeUTF8));
    groupmeatpercent->setTitle(QApplication::translate("LaMainFormBase", "MEAT", 0, QApplication::UnicodeUTF8));
    label_14->setText(QApplication::translate("LaMainFormBase", "Domestic", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelMeatWildPercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by non-domesticated animals.  (Hunting, fishing, scavenging, etc.)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelMeatWildPercent->setText(QApplication::translate("LaMainFormBase", "10", 0, QApplication::UnicodeUTF8));
    label_13->setText(QApplication::translate("LaMainFormBase", "Wild", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelMeatTamePercent->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The percentage of calories of the population's <span style=\" font-style:italic; text-decoration: underline;\">meat</span> portion of the diet that is supplied by domesticated animals.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelMeatTamePercent->setText(QApplication::translate("LaMainFormBase", "90", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sliderMeat->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust this slider to set the ratio of Wild:Tame animals in the meat portion of the diet (calories)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sliderMeat->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Wild to Tame Ratio is the distinction you must make when defining the settlements plant or meat portion of the diet. This setting relies on the assumption that all of their food comes from either wild sources or tame sources. To adjust, simply move the slider left or right, or spin your mouse wheel. <span style=\" font-weight:600;\">Note that this setting is based on calories</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    label6->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    label6->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label6->setText(QApplication::translate("LaMainFormBase", "Calories per\n"
"Person per Day", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbDailyCalories->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbDailyCalories->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of LandUse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    label6_2->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Average requirements for each individual</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    label6_2->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This figure is an average only.  In the future, I hope to be able to implement a feature whereby the human population is modelled, and account for different requirements of men, adult women, pregnant women, lactating women, and children.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label6_2->setText(QApplication::translate("LaMainFormBase", "Dairy Use", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbDairyUtilisation->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set the average number of calories per day required per person</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbDairyUtilisation->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In future versions of LandUse Analyst, the demographics of the human population will be modelled, but currently the user has to supply one figure for an average number of calories required by a single person on a daily basis.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbDairyUtilisation->setSuffix(QApplication::translate("LaMainFormBase", " %", 0, QApplication::UnicodeUTF8));
    cboxLimitDairy->setText(QApplication::translate("LaMainFormBase", "Limit to", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbLimitDairyPercent->setToolTip(QApplication::translate("LaMainFormBase", "If selected, dairy products cannot contribute more than this percentage towards the overall diet.  If this level is achieved, surplus will be reported", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    sbLimitDairyPercent->setSuffix(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    labelDairySurplus->setText(QApplication::translate("LaMainFormBase", "Surplus Dairy Produced", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    groupBox_2->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analsyt needs area targets before it can determine landuse for a site. In order to calculate the area requirements for crops and animals, calorie targets must first be determined. The Diet section makes this task very straight forward. It is important to note that all dietary considerations in this program are based on calories (or in some cases KCalories).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With this in mind, the first step is to define their diets as a ratio between calories provided by <span style=\" font-weight:600;\">Plants</span> an"
        "d calories provided by <span style=\" font-weight:600;\">Meat</span> with the top slider. You can either click and drag with the mouse, or use the mouse wheel. As you slide it, you will see that the percentages for both are automatically adjusted. This setting includes all sources of the diet.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The second level of adjustment is to set the proportions between tame and wild sources. This works the same way as the top slider. Things to consider when setting these sliders are fishing, hunting, wild plant foraging, etc.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBox_2->setTitle(QApplication::translate("LaMainFormBase", "Breakdown of Diet", 0, QApplication::UnicodeUTF8));
    label_10->setText(QApplication::translate("LaMainFormBase", "Settlement:", 0, QApplication::UnicodeUTF8));
    labelCaloriesSettlement->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_37->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_12->setText(QApplication::translate("LaMainFormBase", "All Plants:", 0, QApplication::UnicodeUTF8));
    labelPortionPlants->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_38->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_16->setText(QApplication::translate("LaMainFormBase", "All Meat:", 0, QApplication::UnicodeUTF8));
    labelPortionMeat->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_39->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_54->setText(QApplication::translate("LaMainFormBase", "All Dairy", 0, QApplication::UnicodeUTF8));
    labelPortionAllDairy->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_55->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_18->setText(QApplication::translate("LaMainFormBase", "Domestic Crops:", 0, QApplication::UnicodeUTF8));
    labelPortionCrops->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_40->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_19->setText(QApplication::translate("LaMainFormBase", "Domestic Meat:", 0, QApplication::UnicodeUTF8));
    labelPortionTameMeat->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_41->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_31->setText(QApplication::translate("LaMainFormBase", "Dairy Products:", 0, QApplication::UnicodeUTF8));
    labelPortionDairy->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_42->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_51->setText(QApplication::translate("LaMainFormBase", "Wild Meat: ", 0, QApplication::UnicodeUTF8));
    labelPortionWildMeat->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_50->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_53->setText(QApplication::translate("LaMainFormBase", "Wild Plants: ", 0, QApplication::UnicodeUTF8));
    labelPortionWildPlants->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_52->setText(QApplication::translate("LaMainFormBase", "%", 0, QApplication::UnicodeUTF8));
    label_23->setText(QApplication::translate("LaMainFormBase", "Domestic Crops", 0, QApplication::UnicodeUTF8));
    labelCaloriesCrops->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_43->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_21->setText(QApplication::translate("LaMainFormBase", "Domestic Meat", 0, QApplication::UnicodeUTF8));
    labelCaloriesTameMeat->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_44->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_35->setText(QApplication::translate("LaMainFormBase", "Dairy Products", 0, QApplication::UnicodeUTF8));
    labelCaloriesDairy->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_45->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_46->setText(QApplication::translate("LaMainFormBase", "Wild Meat", 0, QApplication::UnicodeUTF8));
    labelCaloriesWildMeat->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_47->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_48->setText(QApplication::translate("LaMainFormBase", "Wild Plants", 0, QApplication::UnicodeUTF8));
    labelCaloriesWildPlants->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_49->setText(QApplication::translate("LaMainFormBase", "MCals", 0, QApplication::UnicodeUTF8));
    label_4->setText(QApplication::translate("LaMainFormBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Calories required Annum</span><span style=\" font-size:11pt; font-weight:600; font-style:italic; vertical-align:super;\">-1</span></p></body></html>", 0, QApplication::UnicodeUTF8));
    label_15->setText(QApplication::translate("LaMainFormBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Contribution to Diet</span></p></body></html>", 0, QApplication::UnicodeUTF8));
    label_20->setText(QApplication::translate("LaMainFormBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Calories Supplied by:</span></p></body></html>", 0, QApplication::UnicodeUTF8));
    label_8->setText(QApplication::translate("LaMainFormBase", "Individual:", 0, QApplication::UnicodeUTF8));
    labelCaloriesIndividual->setText(QApplication::translate("LaMainFormBase", "Adjust Diet Settings", 0, QApplication::UnicodeUTF8));
    label_36->setText(QApplication::translate("LaMainFormBase", "kCals", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(diet_tab), QApplication::translate("LaMainFormBase", "Diet", 0, QApplication::UnicodeUTF8));
    tblCrops->horizontalHeaderItem(0)->setText(QApplication::translate("LaMainFormBase", "Use?", 0, QApplication::UnicodeUTF8));
    tblCrops->horizontalHeaderItem(1)->setText(QApplication::translate("LaMainFormBase", "Crop", 0, QApplication::UnicodeUTF8));
    tblCrops->horizontalHeaderItem(2)->setText(QApplication::translate("LaMainFormBase", "Parameters", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblCrops->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The crop selected here will be displayed below.  If the crop is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each crop being modelled.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblCrops->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Crop Interface has been designed to be very simple and easy to use. The top section lists all of the defined crops, and selecting one will display its settings in the two lower sections. The lower sections are divided into the crop definition details on the left, and the model parameter settings for the currently selected crop on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the crop or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    lblCropPix->setText(QApplication::translate("LaMainFormBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    textBrowserCropDefinition->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a crop above to refresh this window</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    gbCustomCropMask->setTitle(QApplication::translate("LaMainFormBase", "Use Custom Suitability Mask for Common Cropland", 0, QApplication::UnicodeUTF8));
    label_26->setText(QApplication::translate("LaMainFormBase", "Common Crop Land Raster Mask", 0, QApplication::UnicodeUTF8));
    gbSlopeMaskCropLand->setTitle(QApplication::translate("LaMainFormBase", "Generate Suitability Mask for Common Cropland", 0, QApplication::UnicodeUTF8));
    label_30->setText(QApplication::translate("LaMainFormBase", "If the slope is less than", 0, QApplication::UnicodeUTF8));
    dsbMinSlopeCropMask->setSuffix(QApplication::translate("LaMainFormBase", " degrees", 0, QApplication::UnicodeUTF8));
    label_32->setText(QApplication::translate("LaMainFormBase", "consider it ok for crop use", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnNewCropParameter->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Crop Parameter Manager</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnNewCropParameter->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model crops, several details must be supplied. Crop Parameter Manager asks for these specifics. As with Crop Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same crop, follow the same procedure as for defining multiple crops with the same name. Let's say you want to have two parameters set up for Wheat as an example. The Name: field is Wheat for both, but "
        "in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnNewCropParameter->setText(QApplication::translate("LaMainFormBase", "Set Parameters", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnNewCrop->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Crop Manager</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnNewCrop->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pressing this button will open up the Crop Manager.  There, you can create new crops from scratch, or clone previously defined crops to make changes to.  You can also delete crops if you wish.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnNewCrop->setText(QApplication::translate("LaMainFormBase", "Manage Crops", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(crops_tab), QApplication::translate("LaMainFormBase", "Crops", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(0)->setText(QApplication::translate("LaMainFormBase", "Use?", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(1)->setText(QApplication::translate("LaMainFormBase", "Animal", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(2)->setText(QApplication::translate("LaMainFormBase", "Parameters", 0, QApplication::UnicodeUTF8));
    tblAnimals->horizontalHeaderItem(3)->setText(QApplication::translate("LaMainFormBase", "Percentage", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblAnimals->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The animal selected here will be displayed below.  If the animal is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each animal being modelled.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblAnimals->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal Interface has been designed to be very simple and easy to use. The top section lists all of the defined animals, and selecting one will display its settings in the two lower sections. The lower sections are divided into the animal definition details on the left, and the model parameter settings for the currently selected animal on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the animal or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    lblAnimalPix->setText(QApplication::translate("LaMainFormBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    textBrowserAnimalDefinition->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select an animal above to refresh this window</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    gbCustomMaskGrazingLand->setTitle(QApplication::translate("LaMainFormBase", "Use Custom Suitability mask for Common Grazing Land", 0, QApplication::UnicodeUTF8));
    label_25->setText(QApplication::translate("LaMainFormBase", "Select Mask: ", 0, QApplication::UnicodeUTF8));
    gbGenerateMaskGrazingLand->setTitle(QApplication::translate("LaMainFormBase", "Generate Suitability Mask for Common Grazing Land", 0, QApplication::UnicodeUTF8));
    label_33->setText(QApplication::translate("LaMainFormBase", "Slope is greater than ", 0, QApplication::UnicodeUTF8));
    dsbMinimumSlopeGrazingMask->setSuffix(QApplication::translate("LaMainFormBase", " degrees", 0, QApplication::UnicodeUTF8));
    label_34->setText(QApplication::translate("LaMainFormBase", "and less than", 0, QApplication::UnicodeUTF8));
    dsbMaximumSlopeGrazingMask->setSuffix(QApplication::translate("LaMainFormBase", " degrees", 0, QApplication::UnicodeUTF8));
    gbFoodValue->setTitle(QApplication::translate("LaMainFormBase", "Food Value of Common Grazing Land (Required)", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCommonRasterValue->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food Value of grazing land in Kilo Calories</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCommonRasterValue->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0000ff;\">This value </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">MUST</span><span style=\" font-weight:600; color:#0000ff;\"> be the same for all animals grazing common land.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes land is suitable for grazing by more than one type of animal. LandUse Analyst allows you to designate one suitability mask as common grazing land. Note that you can specify an animal to use both common land and specific land at t"
        "he same time. If this is the case, equal preference is given to all animals grazing the common land. This is not always ideal, as it may have been the case that some animals were given preference to the common land if the other suitable land was further away than the other animals using it.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A workaround for this problem is that LandUse Analyst produces classified maps of the land being used, so if it is the case that you find one animal being forced to travel much further than others, you can simply change settings to balance this. This can be accomplished by removing the other animals one at a time from using the common grazing land. It may be the case, however, that there is no ideal solution, and that they simply had to travel the extra distance!</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Not"
        "e that this setting is the number of KCalories per land area unit available for grazing animals <span style=\" font-weight:600;\">per year</span>.  This value applies to all of the land selected in the common raster mask file.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbCommonRasterValue->setSuffix(QString());
    label_28->setText(QApplication::translate("LaMainFormBase", "per", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cbAreaUnits->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cbAreaUnits->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_27->setText(QApplication::translate("LaMainFormBase", "(per annum)", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnNewAnimal->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Animal Manager</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnNewAnimal->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By pressing on the Manage Animals... button you will be brought to the Animal Manager. Here, you can create new animals from scratch, or clone previously defined animals to make changes to. You can also delete animals if you wish. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnNewAnimal->setText(QApplication::translate("LaMainFormBase", "Manage Animals", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnNewAnimalParameter->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open the Animal Parameter Manager</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnNewAnimalParameter->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for the specific information about the animal which tells the program how the animal was fed, and how big a part of the settlements diet it was. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals"
        " with the same name. Let's say you want to have two parameters set up for cows as an example. The Name: field is Cow for both, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will ahve these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnNewAnimalParameter->setText(QApplication::translate("LaMainFormBase", "Set Parameters", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(animals_tab), QApplication::translate("LaMainFormBase", "Animals", 0, QApplication::UnicodeUTF8));
    lblCropPicCalcs->setText(QApplication::translate("LaMainFormBase", "No Image\n"
"Selected", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    listWidgetCalculationsCrop->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select which crop you want to see the calculations for.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    listWidgetCalculationsCrop->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for all of the crops and animals being modelled, simply select them from the list, and the results will be displayed in the area to the right. This information is meant to give the user an opportunity to make sure that the target look feasible before running the model (which can be very time consuming).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_WHATSTHIS
    textBrowserResultsCrop->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for a crop simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    lblAnimalPicCalcs->setText(QApplication::translate("LaMainFormBase", "No Image\n"
"Selected", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    listWidgetCalculationsAnimal->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select which animal you want to see the calculations for.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    listWidgetCalculationsAnimal->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for all of the crops and animals being modelled, simply select them from the list, and the results will be displayed in the area to the right. This information is meant to give the user an opportunity to make sure that the target look feasible before running the model (which can be very time consuming).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_WHATSTHIS
    textBrowserResultsAnimals->setWhatsThis(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To see the Calorie, Production, and Area targets for an animal simply select it from the list on the left, and the results will be displayed in the area to the right.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This information is meant to give you an opportunity to make sure that the targets look feasible before running the model (which can be very time consuming).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnTargets->setText(QApplication::translate("LaMainFormBase", "Targets", 0, QApplication::UnicodeUTF8));
    pbnFallow->setText(QApplication::translate("LaMainFormBase", "Fallow", 0, QApplication::UnicodeUTF8));
    pbnHerds->setText(QApplication::translate("LaMainFormBase", "Herds", 0, QApplication::UnicodeUTF8));
    pbnText->setText(QApplication::translate("LaMainFormBase", "Text Report", 0, QApplication::UnicodeUTF8));
    pbnHtml->setText(QApplication::translate("LaMainFormBase", "HTML", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(results_tab), QApplication::translate("LaMainFormBase", "Calculations", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tbReport->setToolTip(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The results produced by running the model are displayed here.  This feature, however, is not yet implemented in the Alpha version of LandUse Analyst, but is planned for the Initial Release.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    MainTabs->setTabText(MainTabs->indexOf(tab), QApplication::translate("LaMainFormBase", "Results", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(tabLogs), QApplication::translate("LaMainFormBase", "Log", 0, QApplication::UnicodeUTF8));
    treeHelp->headerItem()->setText(0, QApplication::translate("LaMainFormBase", "Help", 0, QApplication::UnicodeUTF8));

    const bool __sortingEnabled = treeHelp->isSortingEnabled();
    treeHelp->setSortingEnabled(false);
    treeHelp->topLevelItem(0)->setText(0, QApplication::translate("LaMainFormBase", "Model", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Main", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Settlement Information", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Site Name", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Population", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Period", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Location", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Easting", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Northing", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "JADIS Database", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Modelling Method", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Euclidean", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Walking Time", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(2)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Path Distance", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(0)->child(2)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Precision", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Diet", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Plant to Meat Ratio", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Wild to Tame Ratio", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Calories per person per day", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Breakdown", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(1)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Clear", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Crops", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Using the Crop Interface", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Managing Crops", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Clone a crop", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Create a new crop", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Saving crops", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Crop Descriptions", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Name", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Crop Notes", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Crop Yield", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Food Value", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Fodder Yield", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(3)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Fodder Food Value", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(1)->child(3)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Crop Area Units", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Crop Parameters", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Parameter Description", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Parameter Name", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Crop Parameter Notes", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Linking to a crop", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(0)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Crop Portion of diet", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Crop Suitability masks", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop Masks Common", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Crop Masks Specific", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Crop Rotation", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Crop to Fallow Ratio", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(2)->child(2)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Crop Fallow Food Value", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Animals", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Using the Animals Interface", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Managing Animals", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Clone an animal", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Create a new animal", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Saving animals", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Defining an animal", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Animal Description", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Animal Name", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Animal Notes", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Usable Meat", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Kill Weight", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Grow Time", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(0)->child(5)->setText(0, QApplication::translate("LaMainFormBase", "Death Rate", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Reproduction", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Sexual Maturity", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Breeding Life", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Young per birth", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Weaning Age", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Gestation Time", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(1)->child(5)->setText(0, QApplication::translate("LaMainFormBase", "Estrous cycle", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Feeding Requirements", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Calories per animal per day", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(2)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "While Gestating", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(2)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "While Lactating", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(1)->child(3)->child(2)->child(0)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Juveniles", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Animal Parameters", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Setting Animal Parameters", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Animal Parameter Details", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Animal Parameter Name", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Animal Parameter Notes", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(1)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Linking to an animal", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(1)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Portion of tame meat diet", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Animal Land Suitability", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Animal Specific Land", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "KCal setting", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Animal Common Land", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "KCal setting", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(2)->child(2)->setText(0, QApplication::translate("LaMainFormBase", "Selecting Area Units", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(3)->setText(0, QApplication::translate("LaMainFormBase", "Fodder as feed", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(3)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Choosing feed", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(3)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Fodder feed", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(3)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Grain feed", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Fallow Use", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(4)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Grazing Fallow", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(3)->child(2)->child(4)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Fallow Priority", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(4)->setText(0, QApplication::translate("LaMainFormBase", "Calculations", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(0)->child(5)->setText(0, QApplication::translate("LaMainFormBase", "Results", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->setText(0, QApplication::translate("LaMainFormBase", "Requirements", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "File Preparation", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(0)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "DEM", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(0)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Masks", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(0)->child(1)->child(0)->setText(0, QApplication::translate("LaMainFormBase", "Digitizing", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(0)->child(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Naming", 0, QApplication::UnicodeUTF8));
    treeHelp->topLevelItem(1)->child(1)->setText(0, QApplication::translate("LaMainFormBase", "Numbers", 0, QApplication::UnicodeUTF8));

    treeHelp->setSortingEnabled(__sortingEnabled);
    cbDebug->setText(QApplication::translate("LaMainFormBase", "Debugging Mode", 0, QApplication::UnicodeUTF8));
    textHelp->setStyleSheet(QApplication::translate("LaMainFormBase", "<CENTER>", 0, QApplication::UnicodeUTF8));
    textHelp->setHtml(QApplication::translate("LaMainFormBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Grande'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><span style=\" font-size:10pt; font-weight:600;\">To learn more about a feature or field in LandUse Analyst, you can do one of four things.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\">1. <span style=\" font-size:10pt; color:#0000ff;\">Hover over it</span> with your mouse arrow for a brief description</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\">2. Click the <span s"
        "tyle=\" font-size:12pt; font-weight:600; color:#0000ff;\">?</span> in the top right of the main window and then click on the item you want detailed help for.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"> Click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\">3. RIght Click on the thing you want help for.  If there is detailed help for it, you will see a <span style=\" font-weight:600; color:#0000ff;\">What is this?</span> option that you can then click on.  Again, you can click anywhere to make the help box go away.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\">4. Go to the <span style=\" font-weight:600; col"
        "or:#0000ff;\">Help</span> <span style=\" font-weight:600; color:#0000ff;\">Tab</span> and click on the item you want help with on the left for an even more detailed description of what things are and how they work</p></body></html>", 0, QApplication::UnicodeUTF8));
    MainTabs->setTabText(MainTabs->indexOf(help_tab), QApplication::translate("LaMainFormBase", "Help", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaMainFormBase);
    } // retranslateUi

};

namespace Ui {
    class LaMainFormBase: public Ui_LaMainFormBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LAMAINFORMBASE_H
