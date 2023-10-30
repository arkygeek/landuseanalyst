/********************************************************************************
** Form generated from reading ui file 'laanimalparametermanagerbase.ui'
**
** Created: Mon Mar 16 19:50:21 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LAANIMALPARAMETERMANAGERBASE_H
#define UI_LAANIMALPARAMETERMANAGERBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LaAnimalParameterManagerBase
{
public:
    QGridLayout *gridLayout_4;
    QSplitter *splitter;
    QGroupBox *grpProfiles;
    QGridLayout *gridLayout_2;
    QTableWidget *tblAnimalParameterProfiles;
    QGridLayout *gridLayout;
    QToolButton *toolCopy;
    QToolButton *toolDelete;
    QToolButton *toolNew;
    QLabel *lblAnimalPic;
    QSpacerItem *spacerItem;
    QWidget *widget;
    QGridLayout *gridLayout_3;
    QGroupBox *groupBox;
    QGridLayout *gridLayout1;
    QHBoxLayout *hboxLayout;
    QLabel *label;
    QLineEdit *leName;
    QHBoxLayout *hboxLayout1;
    QLabel *label_4;
    QLineEdit *leDescription;
    QHBoxLayout *hboxLayout2;
    QLabel *label_2;
    QComboBox *cboAnimal;
    QLabel *label_3;
    QComboBox *cboRaster;
    QComboBox *cbFallowUsage;
    QGroupBox *grpFodderUse;
    QGridLayout *gridLayout_5;
    QTableWidget *tblFodder;
    QGroupBox *groupBox_3;
    QGridLayout *gridLayout2;
    QHBoxLayout *hboxLayout3;
    QCheckBox *checkBoxCommonRaster;
    QSpinBox *sbCommonRasterValue;
    QFrame *line;
    QCheckBox *checkBoxSpecificRaster;
    QSpinBox *sbSpecificRasterValue;
    QComboBox *cbSpecificLandEnergyType;
    QLabel *label_5;
    QComboBox *cbAreaUnits;
    QGroupBox *groupBox_2;
    QGridLayout *gridLayout3;
    QDoubleSpinBox *sbPercentTameMeat;
    QPushButton *pbnMore;
    QPushButton *pbnImport;
    QPushButton *pbnExport;
    QPushButton *pbnApply;
    QPushButton *pbnClose;

    void setupUi(QWidget *LaAnimalParameterManagerBase)
    {
    if (LaAnimalParameterManagerBase->objectName().isEmpty())
        LaAnimalParameterManagerBase->setObjectName(QString::fromUtf8("LaAnimalParameterManagerBase"));
    LaAnimalParameterManagerBase->resize(587, 686);
    QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(LaAnimalParameterManagerBase->sizePolicy().hasHeightForWidth());
    LaAnimalParameterManagerBase->setSizePolicy(sizePolicy);
    LaAnimalParameterManagerBase->setMinimumSize(QSize(0, 0));
    QIcon icon;
    icon.addPixmap(QPixmap(QString::fromUtf8(":/la_icon.png")), QIcon::Normal, QIcon::Off);
    LaAnimalParameterManagerBase->setWindowIcon(icon);
    gridLayout_4 = new QGridLayout(LaAnimalParameterManagerBase);
    gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
    splitter = new QSplitter(LaAnimalParameterManagerBase);
    splitter->setObjectName(QString::fromUtf8("splitter"));
    splitter->setOrientation(Qt::Vertical);
    grpProfiles = new QGroupBox(splitter);
    grpProfiles->setObjectName(QString::fromUtf8("grpProfiles"));
    gridLayout_2 = new QGridLayout(grpProfiles);
    gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
    tblAnimalParameterProfiles = new QTableWidget(grpProfiles);
    if (tblAnimalParameterProfiles->columnCount() < 2)
        tblAnimalParameterProfiles->setColumnCount(2);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblAnimalParameterProfiles->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblAnimalParameterProfiles->setHorizontalHeaderItem(1, __colItem1);
    tblAnimalParameterProfiles->setObjectName(QString::fromUtf8("tblAnimalParameterProfiles"));
    tblAnimalParameterProfiles->setAlternatingRowColors(true);
    tblAnimalParameterProfiles->setSelectionMode(QAbstractItemView::SingleSelection);
    tblAnimalParameterProfiles->setSelectionBehavior(QAbstractItemView::SelectRows);

    gridLayout_2->addWidget(tblAnimalParameterProfiles, 0, 0, 1, 1);

    gridLayout = new QGridLayout();
#ifndef Q_OS_MAC
    gridLayout->setSpacing(6);
#endif
    gridLayout->setMargin(0);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    toolCopy = new QToolButton(grpProfiles);
    toolCopy->setObjectName(QString::fromUtf8("toolCopy"));
    QIcon icon1;
    icon1.addPixmap(QPixmap(QString::fromUtf8(":/copy.png")), QIcon::Normal, QIcon::Off);
    toolCopy->setIcon(icon1);

    gridLayout->addWidget(toolCopy, 3, 1, 1, 1);

    toolDelete = new QToolButton(grpProfiles);
    toolDelete->setObjectName(QString::fromUtf8("toolDelete"));
    QIcon icon2;
    icon2.addPixmap(QPixmap(QString::fromUtf8(":/delete.png")), QIcon::Normal, QIcon::Off);
    toolDelete->setIcon(icon2);

    gridLayout->addWidget(toolDelete, 3, 2, 1, 1);

    toolNew = new QToolButton(grpProfiles);
    toolNew->setObjectName(QString::fromUtf8("toolNew"));
    QIcon icon3;
    icon3.addPixmap(QPixmap(QString::fromUtf8(":/new.png")), QIcon::Normal, QIcon::Off);
    toolNew->setIcon(icon3);

    gridLayout->addWidget(toolNew, 3, 0, 1, 1);

    lblAnimalPic = new QLabel(grpProfiles);
    lblAnimalPic->setObjectName(QString::fromUtf8("lblAnimalPic"));
    lblAnimalPic->setMinimumSize(QSize(100, 100));
    lblAnimalPic->setMaximumSize(QSize(100, 100));
    lblAnimalPic->setAlignment(Qt::AlignCenter);

    gridLayout->addWidget(lblAnimalPic, 0, 0, 1, 3);

    spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout->addItem(spacerItem, 2, 1, 1, 1);


    gridLayout_2->addLayout(gridLayout, 0, 1, 1, 1);

    splitter->addWidget(grpProfiles);
    widget = new QWidget(splitter);
    widget->setObjectName(QString::fromUtf8("widget"));
    gridLayout_3 = new QGridLayout(widget);
    gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
    gridLayout_3->setContentsMargins(0, 0, 0, 0);
    groupBox = new QGroupBox(widget);
    groupBox->setObjectName(QString::fromUtf8("groupBox"));
    gridLayout1 = new QGridLayout(groupBox);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    hboxLayout = new QHBoxLayout();
#ifndef Q_OS_MAC
    hboxLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
    hboxLayout->setMargin(0);
#endif
    hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
    label = new QLabel(groupBox);
    label->setObjectName(QString::fromUtf8("label"));
    QSizePolicy sizePolicy1(QSizePolicy::Maximum, QSizePolicy::Fixed);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
    label->setSizePolicy(sizePolicy1);

    hboxLayout->addWidget(label);

    leName = new QLineEdit(groupBox);
    leName->setObjectName(QString::fromUtf8("leName"));
    leName->setMinimumSize(QSize(0, 21));

    hboxLayout->addWidget(leName);


    gridLayout1->addLayout(hboxLayout, 0, 0, 1, 2);

    hboxLayout1 = new QHBoxLayout();
#ifndef Q_OS_MAC
    hboxLayout1->setSpacing(6);
#endif
    hboxLayout1->setMargin(0);
    hboxLayout1->setObjectName(QString::fromUtf8("hboxLayout1"));
    label_4 = new QLabel(groupBox);
    label_4->setObjectName(QString::fromUtf8("label_4"));
    sizePolicy1.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
    label_4->setSizePolicy(sizePolicy1);

    hboxLayout1->addWidget(label_4);

    leDescription = new QLineEdit(groupBox);
    leDescription->setObjectName(QString::fromUtf8("leDescription"));
    QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(leDescription->sizePolicy().hasHeightForWidth());
    leDescription->setSizePolicy(sizePolicy2);
    leDescription->setMinimumSize(QSize(0, 21));

    hboxLayout1->addWidget(leDescription);


    gridLayout1->addLayout(hboxLayout1, 1, 0, 1, 2);

    hboxLayout2 = new QHBoxLayout();
#ifndef Q_OS_MAC
    hboxLayout2->setSpacing(6);
#endif
    hboxLayout2->setMargin(0);
    hboxLayout2->setObjectName(QString::fromUtf8("hboxLayout2"));
    label_2 = new QLabel(groupBox);
    label_2->setObjectName(QString::fromUtf8("label_2"));
    QSizePolicy sizePolicy3(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy3.setHorizontalStretch(0);
    sizePolicy3.setVerticalStretch(0);
    sizePolicy3.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
    label_2->setSizePolicy(sizePolicy3);

    hboxLayout2->addWidget(label_2);

    cboAnimal = new QComboBox(groupBox);
    cboAnimal->setObjectName(QString::fromUtf8("cboAnimal"));
    cboAnimal->setMinimumSize(QSize(0, 21));

    hboxLayout2->addWidget(cboAnimal);


    gridLayout1->addLayout(hboxLayout2, 2, 0, 1, 2);

    label_3 = new QLabel(groupBox);
    label_3->setObjectName(QString::fromUtf8("label_3"));
    QSizePolicy sizePolicy4(QSizePolicy::Maximum, QSizePolicy::Preferred);
    sizePolicy4.setHorizontalStretch(0);
    sizePolicy4.setVerticalStretch(0);
    sizePolicy4.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
    label_3->setSizePolicy(sizePolicy4);

    gridLayout1->addWidget(label_3, 3, 0, 1, 1);

    cboRaster = new QComboBox(groupBox);
    cboRaster->setObjectName(QString::fromUtf8("cboRaster"));
    sizePolicy2.setHeightForWidth(cboRaster->sizePolicy().hasHeightForWidth());
    cboRaster->setSizePolicy(sizePolicy2);

    gridLayout1->addWidget(cboRaster, 3, 1, 1, 1);

    cbFallowUsage = new QComboBox(groupBox);
    cbFallowUsage->setObjectName(QString::fromUtf8("cbFallowUsage"));
    sizePolicy2.setHeightForWidth(cbFallowUsage->sizePolicy().hasHeightForWidth());
    cbFallowUsage->setSizePolicy(sizePolicy2);

    gridLayout1->addWidget(cbFallowUsage, 4, 0, 1, 2);


    gridLayout_3->addWidget(groupBox, 0, 0, 1, 1);

    grpFodderUse = new QGroupBox(widget);
    grpFodderUse->setObjectName(QString::fromUtf8("grpFodderUse"));
    grpFodderUse->setMinimumSize(QSize(343, 0));
    grpFodderUse->setCheckable(true);
    grpFodderUse->setChecked(false);
    gridLayout_5 = new QGridLayout(grpFodderUse);
    gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
    tblFodder = new QTableWidget(grpFodderUse);
    if (tblFodder->columnCount() < 4)
        tblFodder->setColumnCount(4);
    QTableWidgetItem *__colItem2 = new QTableWidgetItem();
    tblFodder->setHorizontalHeaderItem(0, __colItem2);
    QTableWidgetItem *__colItem3 = new QTableWidgetItem();
    tblFodder->setHorizontalHeaderItem(1, __colItem3);
    QTableWidgetItem *__colItem4 = new QTableWidgetItem();
    tblFodder->setHorizontalHeaderItem(2, __colItem4);
    QTableWidgetItem *__colItem5 = new QTableWidgetItem();
    tblFodder->setHorizontalHeaderItem(3, __colItem5);
    tblFodder->setObjectName(QString::fromUtf8("tblFodder"));
    tblFodder->setAlternatingRowColors(true);
    tblFodder->setSelectionMode(QAbstractItemView::SingleSelection);
    tblFodder->setSelectionBehavior(QAbstractItemView::SelectRows);
    tblFodder->setShowGrid(false);

    gridLayout_5->addWidget(tblFodder, 0, 0, 1, 1);


    gridLayout_3->addWidget(grpFodderUse, 0, 1, 3, 4);

    groupBox_3 = new QGroupBox(widget);
    groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
    gridLayout2 = new QGridLayout(groupBox_3);
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    hboxLayout3 = new QHBoxLayout();
#ifndef Q_OS_MAC
    hboxLayout3->setSpacing(6);
#endif
#ifndef Q_OS_MAC
    hboxLayout3->setMargin(0);
#endif
    hboxLayout3->setObjectName(QString::fromUtf8("hboxLayout3"));
    checkBoxCommonRaster = new QCheckBox(groupBox_3);
    checkBoxCommonRaster->setObjectName(QString::fromUtf8("checkBoxCommonRaster"));

    hboxLayout3->addWidget(checkBoxCommonRaster);

    sbCommonRasterValue = new QSpinBox(groupBox_3);
    sbCommonRasterValue->setObjectName(QString::fromUtf8("sbCommonRasterValue"));
    sizePolicy2.setHeightForWidth(sbCommonRasterValue->sizePolicy().hasHeightForWidth());
    sbCommonRasterValue->setSizePolicy(sizePolicy2);
    sbCommonRasterValue->setReadOnly(true);
    sbCommonRasterValue->setMaximum(50000);
    sbCommonRasterValue->setSingleStep(1);
    sbCommonRasterValue->setValue(0);

    hboxLayout3->addWidget(sbCommonRasterValue);


    gridLayout2->addLayout(hboxLayout3, 0, 0, 1, 3);

    line = new QFrame(groupBox_3);
    line->setObjectName(QString::fromUtf8("line"));
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    gridLayout2->addWidget(line, 1, 0, 2, 3);

    checkBoxSpecificRaster = new QCheckBox(groupBox_3);
    checkBoxSpecificRaster->setObjectName(QString::fromUtf8("checkBoxSpecificRaster"));
    checkBoxSpecificRaster->setChecked(true);
    checkBoxSpecificRaster->setTristate(false);

    gridLayout2->addWidget(checkBoxSpecificRaster, 3, 0, 1, 2);

    sbSpecificRasterValue = new QSpinBox(groupBox_3);
    sbSpecificRasterValue->setObjectName(QString::fromUtf8("sbSpecificRasterValue"));
    sizePolicy2.setHeightForWidth(sbSpecificRasterValue->sizePolicy().hasHeightForWidth());
    sbSpecificRasterValue->setSizePolicy(sizePolicy2);
    sbSpecificRasterValue->setMinimum(1);
    sbSpecificRasterValue->setMaximum(500000);
    sbSpecificRasterValue->setSingleStep(1);
    sbSpecificRasterValue->setValue(10);

    gridLayout2->addWidget(sbSpecificRasterValue, 2, 2, 2, 1);

    cbSpecificLandEnergyType = new QComboBox(groupBox_3);
    cbSpecificLandEnergyType->setObjectName(QString::fromUtf8("cbSpecificLandEnergyType"));

    gridLayout2->addWidget(cbSpecificLandEnergyType, 4, 0, 1, 1);

    label_5 = new QLabel(groupBox_3);
    label_5->setObjectName(QString::fromUtf8("label_5"));
    label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout2->addWidget(label_5, 4, 1, 1, 1);

    cbAreaUnits = new QComboBox(groupBox_3);
    cbAreaUnits->setObjectName(QString::fromUtf8("cbAreaUnits"));
    sizePolicy2.setHeightForWidth(cbAreaUnits->sizePolicy().hasHeightForWidth());
    cbAreaUnits->setSizePolicy(sizePolicy2);

    gridLayout2->addWidget(cbAreaUnits, 4, 2, 1, 1);


    gridLayout_3->addWidget(groupBox_3, 1, 0, 1, 1);

    groupBox_2 = new QGroupBox(widget);
    groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
    groupBox_2->setMinimumSize(QSize(173, 0));
    gridLayout3 = new QGridLayout(groupBox_2);
    gridLayout3->setMargin(3);
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    sbPercentTameMeat = new QDoubleSpinBox(groupBox_2);
    sbPercentTameMeat->setObjectName(QString::fromUtf8("sbPercentTameMeat"));
    sbPercentTameMeat->setAccelerated(true);
    sbPercentTameMeat->setMaximum(100);
    sbPercentTameMeat->setSingleStep(0.01);

    gridLayout3->addWidget(sbPercentTameMeat, 0, 0, 1, 1);

    pbnMore = new QPushButton(groupBox_2);
    pbnMore->setObjectName(QString::fromUtf8("pbnMore"));
    pbnMore->setEnabled(true);
    sizePolicy3.setHeightForWidth(pbnMore->sizePolicy().hasHeightForWidth());
    pbnMore->setSizePolicy(sizePolicy3);
    pbnMore->setMaximumSize(QSize(41, 22));

    gridLayout3->addWidget(pbnMore, 0, 1, 1, 1);


    gridLayout_3->addWidget(groupBox_2, 2, 0, 2, 1);

    pbnImport = new QPushButton(widget);
    pbnImport->setObjectName(QString::fromUtf8("pbnImport"));
    sizePolicy2.setHeightForWidth(pbnImport->sizePolicy().hasHeightForWidth());
    pbnImport->setSizePolicy(sizePolicy2);
    pbnImport->setMinimumSize(QSize(80, 0));

    gridLayout_3->addWidget(pbnImport, 3, 1, 1, 1);

    pbnExport = new QPushButton(widget);
    pbnExport->setObjectName(QString::fromUtf8("pbnExport"));
    pbnExport->setMinimumSize(QSize(80, 0));

    gridLayout_3->addWidget(pbnExport, 3, 2, 1, 1);

    pbnApply = new QPushButton(widget);
    pbnApply->setObjectName(QString::fromUtf8("pbnApply"));
    sizePolicy2.setHeightForWidth(pbnApply->sizePolicy().hasHeightForWidth());
    pbnApply->setSizePolicy(sizePolicy2);

    gridLayout_3->addWidget(pbnApply, 3, 3, 1, 1);

    pbnClose = new QPushButton(widget);
    pbnClose->setObjectName(QString::fromUtf8("pbnClose"));
    sizePolicy2.setHeightForWidth(pbnClose->sizePolicy().hasHeightForWidth());
    pbnClose->setSizePolicy(sizePolicy2);

    gridLayout_3->addWidget(pbnClose, 3, 4, 1, 1);

    splitter->addWidget(widget);

    gridLayout_4->addWidget(splitter, 0, 0, 1, 1);

    grpProfiles->raise();
    pbnImport->raise();
    pbnApply->raise();
    grpFodderUse->raise();
    groupBox_2->raise();
    groupBox_3->raise();
    groupBox->raise();
    pbnExport->raise();
    QWidget::setTabOrder(tblAnimalParameterProfiles, toolNew);
    QWidget::setTabOrder(toolNew, toolCopy);
    QWidget::setTabOrder(toolCopy, toolDelete);
    QWidget::setTabOrder(toolDelete, leName);
    QWidget::setTabOrder(leName, leDescription);
    QWidget::setTabOrder(leDescription, cboAnimal);
    QWidget::setTabOrder(cboAnimal, checkBoxSpecificRaster);
    QWidget::setTabOrder(checkBoxSpecificRaster, checkBoxCommonRaster);
    QWidget::setTabOrder(checkBoxCommonRaster, sbSpecificRasterValue);
    QWidget::setTabOrder(sbSpecificRasterValue, sbCommonRasterValue);
    QWidget::setTabOrder(sbCommonRasterValue, cbAreaUnits);
    QWidget::setTabOrder(cbAreaUnits, cbFallowUsage);
    QWidget::setTabOrder(cbFallowUsage, pbnClose);

    retranslateUi(LaAnimalParameterManagerBase);
    QObject::connect(pbnClose, SIGNAL(clicked()), LaAnimalParameterManagerBase, SLOT(close()));
    QObject::connect(checkBoxSpecificRaster, SIGNAL(clicked()), checkBoxCommonRaster, SLOT(toggle()));
    QObject::connect(checkBoxCommonRaster, SIGNAL(clicked()), checkBoxSpecificRaster, SLOT(toggle()));

    QMetaObject::connectSlotsByName(LaAnimalParameterManagerBase);
    } // setupUi

    void retranslateUi(QWidget *LaAnimalParameterManagerBase)
    {
    LaAnimalParameterManagerBase->setWindowTitle(QApplication::translate("LaAnimalParameterManagerBase", "Animal Parameter Manager", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    grpProfiles->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for the specific information about the animal which tells the program how the animal was fed, and how big a part of the settlements diet it was. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals"
        " with the same name. Let's say you want to have two parameters set up for cows as an example. The Name: field is Cow for both, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will ahve these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    grpProfiles->setTitle(QApplication::translate("LaAnimalParameterManagerBase", "Available Animal Parameter Settings", 0, QApplication::UnicodeUTF8));
    tblAnimalParameterProfiles->horizontalHeaderItem(0)->setText(QApplication::translate("LaAnimalParameterManagerBase", "FileName", 0, QApplication::UnicodeUTF8));
    tblAnimalParameterProfiles->horizontalHeaderItem(1)->setText(QApplication::translate("LaAnimalParameterManagerBase", "Name", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblAnimalParameterProfiles->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a parameter here to see and/or edit it's properties below.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblAnimalParameterProfiles->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model animals, several details must be supplied. Animal Parameter Manager asks for these specifics. As with Animal Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same animal, follow the same procedure as for defining multiple animals with the same name. Let's say you want to have two parameters set up for Cows as an example. The Name: field is Cow for bot"
        "h, but in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    toolCopy->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolCopy->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new parameter that is similar to one already defined, you can clone this parameter to save time. All of the settings of the parameter you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the parameter you are cloning was).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolCopy->setText(QApplication::translate("LaAnimalParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolDelete->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    toolDelete->setText(QApplication::translate("LaAnimalParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolNew->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolNew->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Animal Parameter Manager, you are just editing the parameter currently selected. To create a new parameter, you <span style=\" font-weight:600;\">must</span> click on the New button.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolNew->setText(QApplication::translate("LaAnimalParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));
    lblAnimalPic->setText(QApplication::translate("LaAnimalParameterManagerBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));
    groupBox->setTitle(QApplication::translate("LaAnimalParameterManagerBase", "Details", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaAnimalParameterManagerBase", "Name:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leName->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the animal parameter you are defining in this field. You do not need a unique name. You can have, for example, 10 different animal parameters defined, all named \"Jericho\". LandUse Analyst uses a special method of saving the animals to eliminate the issue of duplicate filenames. This way, you can have, for example, conservative and optimistic settings for each animal at a site.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_4->setText(QApplication::translate("LaAnimalParameterManagerBase", "Notes:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leDescription->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because LandUse Analyst allows more than one type of parameter to be defined, the Notes: field allows you to give a brief description of the the parameter. For example, you may have two \"Shuna\" parameters defined, and the Notes: fields could contain \"Conservative\" and \"Optimistic\" to distinguish between them.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_2->setText(QApplication::translate("LaAnimalParameterManagerBase", "Animal:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cboAnimal->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal that these parameters are for.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cboAnimal->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is very important to select which animal your parameter settings are for. Once you slect the animal it appies to, simply click Apply, and it will then be properly allocated, and will show up in the dropdown list for that animal in the table on the top.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_3->setText(QApplication::translate("LaAnimalParameterManagerBase", "Raster Mask ", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cbFallowUsage->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your animal is to be allowed to graze fallow land resulting from crop rotation, set the priority of their access to this fallow land here.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cbFallowUsage->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LandUse Analyst allows animals to utilize fallow crop land as grazing land. There are many difficult aspects to including this in a model, but these difficulties are mostly transparent to the user. Essentially, you need to indicate only whether the animal will be allowed to graze fallow, and if so, what is it's access priority in relation to the other animals grazing the same fallow land. Given this, the software handles the rest!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because some animals may have been given preferential access to the fallow land, LandUse Analyst has given three different priority levels to fallow access. The software first looks at the HIGH priority animals, and designates all fallow land to them, until either their needs are satisfied, or the available fallow land is all used. If there is more than enough fallow land for the HIGH priority animals, the remaining amount is then made available to the MED priority animals, and this repeats for the LOW priority ones as well.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    grpFodderUse->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If your settlement fed the animal fodder, check off the Fodder section to enable the Fodder options to be accessible. Straw/Chaff is a percentage of what is available.  Grain is a percentage of the animals diet.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    grpFodderUse->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "Select Fodder if you believe the animals were fed grain to supplement their grazing.  You will then have to select how many kg of the selected grain you believe they fed each animal either every day, week, or month.", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    grpFodderUse->setTitle(QApplication::translate("LaAnimalParameterManagerBase", "Fodder", 0, QApplication::UnicodeUTF8));
    tblFodder->horizontalHeaderItem(0)->setText(QApplication::translate("LaAnimalParameterManagerBase", "Used", 0, QApplication::UnicodeUTF8));
    tblFodder->horizontalHeaderItem(1)->setText(QApplication::translate("LaAnimalParameterManagerBase", "Crop", 0, QApplication::UnicodeUTF8));
    tblFodder->horizontalHeaderItem(2)->setText(QApplication::translate("LaAnimalParameterManagerBase", "Fodder", 0, QApplication::UnicodeUTF8));
    tblFodder->horizontalHeaderItem(3)->setText(QApplication::translate("LaAnimalParameterManagerBase", "Grain", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblFodder->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The animal selected here will be displayed below.  If the animal is to be included in the model, it must be checked off on left.  The model parameters must also be defined and linked to each animal being modelled.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblFodder->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Animal Interface has been designed to be very simple and easy to use. The top section lists all of the defined animals, and selecting one will display its settings in the two lower sections. The lower sections are divided into the animal definition details on the left, and the model parameter settings for the currently selected animal on the right.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you wish to edit either the animal or its parameters, you simply click on the Manage button below the display areas.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_WHATSTHIS
    groupBox_3->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order for LandUse Analyst to create landuse maps, you must first create land suitability files to tell it what land is suitable for use by the crops and the animals. These files can be produced manually or automatically, but at the moment both must be done with external tools like QGis or GRASS. Future versions of Landuse Analyst will have the required features of these programs incorporated into it, but for now this step must be done externally. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBox_3->setTitle(QApplication::translate("LaAnimalParameterManagerBase", "Land Suitability Selection", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    checkBoxCommonRaster->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named common.grazing.mask which more than one animal can graze from</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    checkBoxCommonRaster->setText(QApplication::translate("LaAnimalParameterManagerBase", "Common Land", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCommonRasterValue->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TDN loaded from main form</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCommonRasterValue->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
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
    sbCommonRasterValue->setPrefix(QString());

#ifndef QT_NO_TOOLTIP
    checkBoxSpecificRaster->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">binary raster named: animalName.mask  where animalName is the name of the animal you are setting these parameters for.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    checkBoxSpecificRaster->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes you may want to specify that land is suitable for grazing by only one type of animal. LandUse Analyst allows you to designate a land suitability mask as being unique to that animal. Note that you can specify an animal to use both common land and specific land at the same time. For more detailed information on this, see the help section on Animal Common Land.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    checkBoxSpecificRaster->setText(QApplication::translate("LaAnimalParameterManagerBase", "Specific Land", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbSpecificRasterValue->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TDN (Total Digestive Nutrients) available</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbSpecificRasterValue->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note that this setting is the number of KCalories per land area unit available for grazing animals <span style=\" font-weight:600;\">per year</span>.  This value applies to only the land selected in the unique raster mask file created for this animal.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbSpecificRasterValue->setSuffix(QString());
    sbSpecificRasterValue->setPrefix(QString());
    label_5->setText(QApplication::translate("LaAnimalParameterManagerBase", "per  ", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cbAreaUnits->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cbAreaUnits->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBox_2->setTitle(QApplication::translate("LaAnimalParameterManagerBase", "Portion of Domestic Meat Diet", 0, QApplication::UnicodeUTF8));
    sbPercentTameMeat->setSuffix(QApplication::translate("LaAnimalParameterManagerBase", "%", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnMore->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click here to get help determining this figure</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pbnMore->setText(QApplication::translate("LaAnimalParameterManagerBase", "More", 0, QApplication::UnicodeUTF8));
    pbnImport->setText(QApplication::translate("LaAnimalParameterManagerBase", "Import", 0, QApplication::UnicodeUTF8));
    pbnExport->setText(QApplication::translate("LaAnimalParameterManagerBase", "Export", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnApply->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnApply->setWhatsThis(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a parameter, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as LandUse Analyst has a special way of saving parameters to allow for duplicate parameter names. It is helpful, however, to utilize the Notes field to distinguish between same-named parameter definitions.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnApply->setText(QApplication::translate("LaAnimalParameterManagerBase", "Apply", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnClose->setToolTip(QApplication::translate("LaAnimalParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pbnClose->setText(QApplication::translate("LaAnimalParameterManagerBase", "Close", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaAnimalParameterManagerBase);
    } // retranslateUi

};

namespace Ui {
    class LaAnimalParameterManagerBase: public Ui_LaAnimalParameterManagerBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LAANIMALPARAMETERMANAGERBASE_H
