/********************************************************************************
** Form generated from reading ui file 'lacropparametermanagerbase.ui'
**
** Created: Tue Apr 7 19:36:12 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LACROPPARAMETERMANAGERBASE_H
#define UI_LACROPPARAMETERMANAGERBASE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QDoubleSpinBox>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QTableWidget>
#include <QtGui/QToolButton>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_LaCropParameterManagerBase
{
public:
    QGridLayout *gridLayout;
    QGroupBox *grpProfiles;
    QGridLayout *gridLayout1;
    QGridLayout *gridLayout2;
    QToolButton *toolDelete;
    QToolButton *toolCopy;
    QSpacerItem *spacerItem;
    QLabel *lblCropPic;
    QToolButton *toolNew;
    QPushButton *pbnImport;
    QPushButton *pbnExport;
    QSpacerItem *spacerItem1;
    QTableWidget *tblCropParameterProfiles;
    QLabel *label;
    QLineEdit *leName;
    QGroupBox *grpCropRotation;
    QGridLayout *gridLayout3;
    QLabel *labelFallow1;
    QLabel *labelFallow3;
    QDoubleSpinBox *sbFallowRatio;
    QLabel *labelFallow5;
    QLabel *labelFallow2;
    QSpinBox *sbFallowValue;
    QComboBox *cbFallowEnergyType;
    QComboBox *cbAreaUnits;
    QLabel *label_4;
    QLineEdit *leDescription;
    QHBoxLayout *hboxLayout;
    QLabel *label_2;
    QComboBox *cboCrop;
    QGroupBox *groupBoxSuitableLand;
    QGridLayout *gridLayout4;
    QCheckBox *checkBoxUseCommonLand;
    QCheckBox *checkBoxUseSpecificLand;
    QLabel *label_3;
    QComboBox *cboRaster;
    QLabel *labelPortionDiet;
    QDoubleSpinBox *sbPercentTameCrop;
    QLabel *labelPortionDiet_2;
    QSpinBox *sbReseed;
    QLabel *labelPortionDiet_3;
    QSpinBox *sbSpoilage;
    QSpacerItem *spacerItem2;
    QPushButton *pbnApply;
    QPushButton *pbnClose;

    void setupUi(QWidget *LaCropParameterManagerBase)
    {
    if (LaCropParameterManagerBase->objectName().isEmpty())
        LaCropParameterManagerBase->setObjectName(QString::fromUtf8("LaCropParameterManagerBase"));
    LaCropParameterManagerBase->resize(520, 583);
    LaCropParameterManagerBase->setMinimumSize(QSize(0, 0));
    const QIcon icon = QIcon(QString::fromUtf8(":/la_icon_small.png"));
    LaCropParameterManagerBase->setWindowIcon(icon);
    gridLayout = new QGridLayout(LaCropParameterManagerBase);
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    grpProfiles = new QGroupBox(LaCropParameterManagerBase);
    grpProfiles->setObjectName(QString::fromUtf8("grpProfiles"));
    gridLayout1 = new QGridLayout(grpProfiles);
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    gridLayout2 = new QGridLayout();
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    toolDelete = new QToolButton(grpProfiles);
    toolDelete->setObjectName(QString::fromUtf8("toolDelete"));
    const QIcon icon1 = QIcon(QString::fromUtf8(":/delete.png"));
    toolDelete->setIcon(icon1);

    gridLayout2->addWidget(toolDelete, 2, 2, 1, 1);

    toolCopy = new QToolButton(grpProfiles);
    toolCopy->setObjectName(QString::fromUtf8("toolCopy"));
    const QIcon icon2 = QIcon(QString::fromUtf8(":/copy.png"));
    toolCopy->setIcon(icon2);

    gridLayout2->addWidget(toolCopy, 2, 1, 1, 1);

    spacerItem = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout2->addItem(spacerItem, 1, 1, 1, 1);

    lblCropPic = new QLabel(grpProfiles);
    lblCropPic->setObjectName(QString::fromUtf8("lblCropPic"));
    lblCropPic->setMinimumSize(QSize(100, 100));
    lblCropPic->setMaximumSize(QSize(100, 100));
    lblCropPic->setAlignment(Qt::AlignCenter);

    gridLayout2->addWidget(lblCropPic, 0, 0, 1, 3);

    toolNew = new QToolButton(grpProfiles);
    toolNew->setObjectName(QString::fromUtf8("toolNew"));
    const QIcon icon3 = QIcon(QString::fromUtf8(":/new.png"));
    toolNew->setIcon(icon3);

    gridLayout2->addWidget(toolNew, 2, 0, 1, 1);


    gridLayout1->addLayout(gridLayout2, 0, 3, 2, 1);

    pbnImport = new QPushButton(grpProfiles);
    pbnImport->setObjectName(QString::fromUtf8("pbnImport"));
    pbnImport->setMinimumSize(QSize(80, 0));

    gridLayout1->addWidget(pbnImport, 1, 0, 1, 1);

    pbnExport = new QPushButton(grpProfiles);
    pbnExport->setObjectName(QString::fromUtf8("pbnExport"));
    pbnExport->setMinimumSize(QSize(80, 0));

    gridLayout1->addWidget(pbnExport, 1, 1, 1, 1);

    spacerItem1 = new QSpacerItem(71, 27, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout1->addItem(spacerItem1, 1, 2, 1, 1);

    tblCropParameterProfiles = new QTableWidget(grpProfiles);
    if (tblCropParameterProfiles->columnCount() < 2)
        tblCropParameterProfiles->setColumnCount(2);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblCropParameterProfiles->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblCropParameterProfiles->setHorizontalHeaderItem(1, __colItem1);
    tblCropParameterProfiles->setObjectName(QString::fromUtf8("tblCropParameterProfiles"));
    tblCropParameterProfiles->setAlternatingRowColors(true);
    tblCropParameterProfiles->setSelectionMode(QAbstractItemView::SingleSelection);
    tblCropParameterProfiles->setSelectionBehavior(QAbstractItemView::SelectRows);

    gridLayout1->addWidget(tblCropParameterProfiles, 0, 0, 1, 3);


    gridLayout->addWidget(grpProfiles, 0, 0, 1, 6);

    label = new QLabel(LaCropParameterManagerBase);
    label->setObjectName(QString::fromUtf8("label"));

    gridLayout->addWidget(label, 1, 0, 1, 1);

    leName = new QLineEdit(LaCropParameterManagerBase);
    leName->setObjectName(QString::fromUtf8("leName"));

    gridLayout->addWidget(leName, 1, 1, 1, 1);

    grpCropRotation = new QGroupBox(LaCropParameterManagerBase);
    grpCropRotation->setObjectName(QString::fromUtf8("grpCropRotation"));
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(grpCropRotation->sizePolicy().hasHeightForWidth());
    grpCropRotation->setSizePolicy(sizePolicy);
    grpCropRotation->setMinimumSize(QSize(227, 100));
    grpCropRotation->setCheckable(true);
    grpCropRotation->setChecked(false);
    gridLayout3 = new QGridLayout(grpCropRotation);
    gridLayout3->setObjectName(QString::fromUtf8("gridLayout3"));
    labelFallow1 = new QLabel(grpCropRotation);
    labelFallow1->setObjectName(QString::fromUtf8("labelFallow1"));
    sizePolicy.setHeightForWidth(labelFallow1->sizePolicy().hasHeightForWidth());
    labelFallow1->setSizePolicy(sizePolicy);
    labelFallow1->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(labelFallow1, 0, 0, 1, 1);

    labelFallow3 = new QLabel(grpCropRotation);
    labelFallow3->setObjectName(QString::fromUtf8("labelFallow3"));
    labelFallow3->setLayoutDirection(Qt::LeftToRight);
    labelFallow3->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

    gridLayout3->addWidget(labelFallow3, 0, 1, 1, 1);

    sbFallowRatio = new QDoubleSpinBox(grpCropRotation);
    sbFallowRatio->setObjectName(QString::fromUtf8("sbFallowRatio"));
    sbFallowRatio->setMinimumSize(QSize(0, 22));
    sbFallowRatio->setMaximum(5);
    sbFallowRatio->setSingleStep(0.25);
    sbFallowRatio->setValue(1);

    gridLayout3->addWidget(sbFallowRatio, 0, 2, 1, 1);

    labelFallow5 = new QLabel(grpCropRotation);
    labelFallow5->setObjectName(QString::fromUtf8("labelFallow5"));
    sizePolicy.setHeightForWidth(labelFallow5->sizePolicy().hasHeightForWidth());
    labelFallow5->setSizePolicy(sizePolicy);
    labelFallow5->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(labelFallow5, 0, 3, 1, 2);

    labelFallow2 = new QLabel(grpCropRotation);
    labelFallow2->setObjectName(QString::fromUtf8("labelFallow2"));
    labelFallow2->setAlignment(Qt::AlignCenter);

    gridLayout3->addWidget(labelFallow2, 1, 0, 1, 5);

    sbFallowValue = new QSpinBox(grpCropRotation);
    sbFallowValue->setObjectName(QString::fromUtf8("sbFallowValue"));
    QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Minimum);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(sbFallowValue->sizePolicy().hasHeightForWidth());
    sbFallowValue->setSizePolicy(sizePolicy1);
    sbFallowValue->setMinimumSize(QSize(0, 22));
    sbFallowValue->setMinimum(1);
    sbFallowValue->setMaximum(5000);
    sbFallowValue->setSingleStep(10);
    sbFallowValue->setValue(500);

    gridLayout3->addWidget(sbFallowValue, 2, 0, 1, 2);

    cbFallowEnergyType = new QComboBox(grpCropRotation);
    cbFallowEnergyType->setObjectName(QString::fromUtf8("cbFallowEnergyType"));
    cbFallowEnergyType->setMinimumSize(QSize(0, 22));

    gridLayout3->addWidget(cbFallowEnergyType, 2, 2, 1, 2);

    cbAreaUnits = new QComboBox(grpCropRotation);
    cbAreaUnits->setObjectName(QString::fromUtf8("cbAreaUnits"));
    sizePolicy.setHeightForWidth(cbAreaUnits->sizePolicy().hasHeightForWidth());
    cbAreaUnits->setSizePolicy(sizePolicy);
    cbAreaUnits->setMinimumSize(QSize(0, 22));

    gridLayout3->addWidget(cbAreaUnits, 2, 4, 1, 1);


    gridLayout->addWidget(grpCropRotation, 1, 2, 4, 4);

    label_4 = new QLabel(LaCropParameterManagerBase);
    label_4->setObjectName(QString::fromUtf8("label_4"));
    sizePolicy.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
    label_4->setSizePolicy(sizePolicy);

    gridLayout->addWidget(label_4, 2, 0, 1, 1);

    leDescription = new QLineEdit(LaCropParameterManagerBase);
    leDescription->setObjectName(QString::fromUtf8("leDescription"));
    sizePolicy.setHeightForWidth(leDescription->sizePolicy().hasHeightForWidth());
    leDescription->setSizePolicy(sizePolicy);

    gridLayout->addWidget(leDescription, 2, 1, 1, 1);

    hboxLayout = new QHBoxLayout();
    hboxLayout->setObjectName(QString::fromUtf8("hboxLayout"));
    label_2 = new QLabel(LaCropParameterManagerBase);
    label_2->setObjectName(QString::fromUtf8("label_2"));
    sizePolicy.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
    label_2->setSizePolicy(sizePolicy);

    hboxLayout->addWidget(label_2);

    cboCrop = new QComboBox(LaCropParameterManagerBase);
    cboCrop->setObjectName(QString::fromUtf8("cboCrop"));
    cboCrop->setMinimumSize(QSize(0, 26));

    hboxLayout->addWidget(cboCrop);


    gridLayout->addLayout(hboxLayout, 3, 0, 1, 2);

    groupBoxSuitableLand = new QGroupBox(LaCropParameterManagerBase);
    groupBoxSuitableLand->setObjectName(QString::fromUtf8("groupBoxSuitableLand"));
    sizePolicy.setHeightForWidth(groupBoxSuitableLand->sizePolicy().hasHeightForWidth());
    groupBoxSuitableLand->setSizePolicy(sizePolicy);
    groupBoxSuitableLand->setMinimumSize(QSize(115, 0));
    gridLayout4 = new QGridLayout(groupBoxSuitableLand);
    gridLayout4->setObjectName(QString::fromUtf8("gridLayout4"));
    checkBoxUseCommonLand = new QCheckBox(groupBoxSuitableLand);
    checkBoxUseCommonLand->setObjectName(QString::fromUtf8("checkBoxUseCommonLand"));
    sizePolicy.setHeightForWidth(checkBoxUseCommonLand->sizePolicy().hasHeightForWidth());
    checkBoxUseCommonLand->setSizePolicy(sizePolicy);
    checkBoxUseCommonLand->setChecked(true);

    gridLayout4->addWidget(checkBoxUseCommonLand, 0, 0, 1, 2);

    checkBoxUseSpecificLand = new QCheckBox(groupBoxSuitableLand);
    checkBoxUseSpecificLand->setObjectName(QString::fromUtf8("checkBoxUseSpecificLand"));
    sizePolicy.setHeightForWidth(checkBoxUseSpecificLand->sizePolicy().hasHeightForWidth());
    checkBoxUseSpecificLand->setSizePolicy(sizePolicy);

    gridLayout4->addWidget(checkBoxUseSpecificLand, 1, 0, 1, 2);

    label_3 = new QLabel(groupBoxSuitableLand);
    label_3->setObjectName(QString::fromUtf8("label_3"));
    label_3->setAlignment(Qt::AlignCenter);
    label_3->setMargin(0);
    label_3->setTextInteractionFlags(Qt::NoTextInteraction);

    gridLayout4->addWidget(label_3, 2, 0, 1, 1);

    cboRaster = new QComboBox(groupBoxSuitableLand);
    cboRaster->setObjectName(QString::fromUtf8("cboRaster"));

    gridLayout4->addWidget(cboRaster, 2, 1, 1, 1);


    gridLayout->addWidget(groupBoxSuitableLand, 4, 0, 4, 2);

    labelPortionDiet = new QLabel(LaCropParameterManagerBase);
    labelPortionDiet->setObjectName(QString::fromUtf8("labelPortionDiet"));
    sizePolicy.setHeightForWidth(labelPortionDiet->sizePolicy().hasHeightForWidth());
    labelPortionDiet->setSizePolicy(sizePolicy);
    labelPortionDiet->setFrameShape(QFrame::NoFrame);
    labelPortionDiet->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

    gridLayout->addWidget(labelPortionDiet, 5, 2, 1, 2);

    sbPercentTameCrop = new QDoubleSpinBox(LaCropParameterManagerBase);
    sbPercentTameCrop->setObjectName(QString::fromUtf8("sbPercentTameCrop"));
    sbPercentTameCrop->setButtonSymbols(QAbstractSpinBox::UpDownArrows);
    sbPercentTameCrop->setAccelerated(true);
    sbPercentTameCrop->setMaximum(100);
    sbPercentTameCrop->setSingleStep(0.01);

    gridLayout->addWidget(sbPercentTameCrop, 5, 4, 1, 2);

    labelPortionDiet_2 = new QLabel(LaCropParameterManagerBase);
    labelPortionDiet_2->setObjectName(QString::fromUtf8("labelPortionDiet_2"));
    sizePolicy.setHeightForWidth(labelPortionDiet_2->sizePolicy().hasHeightForWidth());
    labelPortionDiet_2->setSizePolicy(sizePolicy);
    labelPortionDiet_2->setFrameShape(QFrame::NoFrame);
    labelPortionDiet_2->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

    gridLayout->addWidget(labelPortionDiet_2, 6, 2, 1, 3);

    sbReseed = new QSpinBox(LaCropParameterManagerBase);
    sbReseed->setObjectName(QString::fromUtf8("sbReseed"));
    sbReseed->setMaximum(100);

    gridLayout->addWidget(sbReseed, 6, 5, 1, 1);

    labelPortionDiet_3 = new QLabel(LaCropParameterManagerBase);
    labelPortionDiet_3->setObjectName(QString::fromUtf8("labelPortionDiet_3"));
    sizePolicy.setHeightForWidth(labelPortionDiet_3->sizePolicy().hasHeightForWidth());
    labelPortionDiet_3->setSizePolicy(sizePolicy);
    labelPortionDiet_3->setFrameShape(QFrame::NoFrame);
    labelPortionDiet_3->setAlignment(Qt::AlignBottom|Qt::AlignLeading|Qt::AlignLeft);

    gridLayout->addWidget(labelPortionDiet_3, 7, 2, 1, 3);

    sbSpoilage = new QSpinBox(LaCropParameterManagerBase);
    sbSpoilage->setObjectName(QString::fromUtf8("sbSpoilage"));
    sbSpoilage->setMaximum(100);

    gridLayout->addWidget(sbSpoilage, 7, 5, 1, 1);

    spacerItem2 = new QSpacerItem(181, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout->addItem(spacerItem2, 8, 0, 1, 2);

    pbnApply = new QPushButton(LaCropParameterManagerBase);
    pbnApply->setObjectName(QString::fromUtf8("pbnApply"));
    QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Fixed);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(pbnApply->sizePolicy().hasHeightForWidth());
    pbnApply->setSizePolicy(sizePolicy2);

    gridLayout->addWidget(pbnApply, 8, 2, 1, 1);

    pbnClose = new QPushButton(LaCropParameterManagerBase);
    pbnClose->setObjectName(QString::fromUtf8("pbnClose"));
    sizePolicy2.setHeightForWidth(pbnClose->sizePolicy().hasHeightForWidth());
    pbnClose->setSizePolicy(sizePolicy2);

    gridLayout->addWidget(pbnClose, 8, 3, 1, 3);

    QWidget::setTabOrder(tblCropParameterProfiles, pbnImport);
    QWidget::setTabOrder(pbnImport, pbnExport);
    QWidget::setTabOrder(pbnExport, toolNew);
    QWidget::setTabOrder(toolNew, toolCopy);
    QWidget::setTabOrder(toolCopy, toolDelete);
    QWidget::setTabOrder(toolDelete, leName);
    QWidget::setTabOrder(leName, leDescription);
    QWidget::setTabOrder(leDescription, cboCrop);
    QWidget::setTabOrder(cboCrop, checkBoxUseCommonLand);
    QWidget::setTabOrder(checkBoxUseCommonLand, checkBoxUseSpecificLand);
    QWidget::setTabOrder(checkBoxUseSpecificLand, sbFallowRatio);
    QWidget::setTabOrder(sbFallowRatio, sbFallowValue);
    QWidget::setTabOrder(sbFallowValue, cbAreaUnits);
    QWidget::setTabOrder(cbAreaUnits, pbnApply);
    QWidget::setTabOrder(pbnApply, pbnClose);

    retranslateUi(LaCropParameterManagerBase);
    QObject::connect(pbnClose, SIGNAL(pressed()), LaCropParameterManagerBase, SLOT(close()));
    QObject::connect(checkBoxUseSpecificLand, SIGNAL(clicked()), checkBoxUseCommonLand, SLOT(toggle()));
    QObject::connect(checkBoxUseCommonLand, SIGNAL(clicked()), checkBoxUseSpecificLand, SLOT(toggle()));

    QMetaObject::connectSlotsByName(LaCropParameterManagerBase);
    } // setupUi

    void retranslateUi(QWidget *LaCropParameterManagerBase)
    {
    LaCropParameterManagerBase->setWindowTitle(QApplication::translate("LaCropParameterManagerBase", "Crop Parameter Manager", 0, QApplication::UnicodeUTF8));
    grpProfiles->setTitle(QApplication::translate("LaCropParameterManagerBase", "Available Crop Parameter Settings", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolDelete->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    toolDelete->setText(QApplication::translate("LaCropParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolCopy->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolCopy->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new parameter that is similar to one already defined, you can clone this parameter to save time. All of the settings of the parameter you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the parameter you are cloning was).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolCopy->setText(QApplication::translate("LaCropParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));
    lblCropPic->setText(QApplication::translate("LaCropParameterManagerBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolNew->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new parameter</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolNew->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Crop Parameter Manager, you are just editing the parameter currently selected. To create a new parameter, you <span style=\" font-weight:600;\">must</span> click on the New button.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolNew->setText(QApplication::translate("LaCropParameterManagerBase", "...", 0, QApplication::UnicodeUTF8));
    pbnImport->setText(QApplication::translate("LaCropParameterManagerBase", "Import", 0, QApplication::UnicodeUTF8));
    pbnExport->setText(QApplication::translate("LaCropParameterManagerBase", "Export", 0, QApplication::UnicodeUTF8));
    tblCropParameterProfiles->horizontalHeaderItem(0)->setText(QApplication::translate("LaCropParameterManagerBase", "FileName", 0, QApplication::UnicodeUTF8));
    tblCropParameterProfiles->horizontalHeaderItem(1)->setText(QApplication::translate("LaCropParameterManagerBase", "Name", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblCropParameterProfiles->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a parameter here to see and/or edit it's properties below.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblCropParameterProfiles->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model crops, several details must be supplied. Crop Parameter Manager asks for these specifics. As with Crop Manager, it is possible to have more than one parameter named the same thing. Again, just enter a descriptor in the Notes: field.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different parameters for the same crop, follow the same procedure as for defining multiple crops with the same name. Let's say you want to have two parameters set up for Wheat as an example. The Name: field is Wheat for both, but "
        "in Notes: field, enter Optimistic for one, and Conservative for the other. Then adjust the parameters as you wish for each. Even though the name is the same, the parameters are saved uniquely. Having multiple parameters can be useful for setting up different scenarios, such as drought years, diease, catastrophic events, etc. Eventually, LandUse Analyst will have the ability to model over time, and will have these types of scenarios incorporated into the model.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label->setText(QApplication::translate("LaCropParameterManagerBase", "Name:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leName->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the crop parameter you are defining in this field. You do not need a unique name. You can have, for example, 10 different crop parameters defined, all named \"Jericho\". LandUse Analyst uses a special method of saving the crop to eliminate the issue of duplicate filenames. This way, you can have, for example, conservative and optimistic settings for each crop at a site. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_WHATSTHIS
    grpCropRotation->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If crops were rotated, the checkbox needs to be checked. The variables for crop rotation are unavailable until this has been done.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Keep in mind that animals can graze the fallow land. Because of this, you will need to estimate what the food value from the fallow land would have been, similar to what needs to be done when defining grazing land.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    grpCropRotation->setTitle(QApplication::translate("LaCropParameterManagerBase", "Crop Rotation", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelFallow1->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelFallow1->setText(QApplication::translate("LaCropParameterManagerBase", "Ratio", 0, QApplication::UnicodeUTF8));
    labelFallow3->setText(QApplication::translate("LaCropParameterManagerBase", " 1: ", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbFallowRatio->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fallow Ratio</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbFallowRatio->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When crop rotation is used, this field must be set. If the land grows a crop one year, and is left fallow the next, then the crop to fallow ratio is 1:1 so you would set the value to 1. For more complicated rotations, such as a cereal-legume-fallow rotation, it gets slightly more complicated. That situation would be one year out of three fallow and two years out of three crop. In this case, the setting would be 0.50 which might seem confusing.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Just remember that you need to <span style=\" font-weight:600;\">divi"
        "de the </span><span style=\" font-weight:600; font-style:italic;\">number of years of fallow</span><span style=\" font-weight:600;\"> by the </span><span style=\" font-weight:600; font-style:italic;\">number of years of crop</span> to set this properly.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_TOOLTIP
    labelFallow5->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A value of 1:1 is default, and means that half the land is fallow, half is crop.  If there is a crop rotation so that it is only fallow every 3rd year, you could use a ratio of 2:1.  If they cropped continuously, the ratio would be 1:0.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    labelFallow5->setText(QApplication::translate("LaCropParameterManagerBase", "Crop:Fallow ", 0, QApplication::UnicodeUTF8));
    labelFallow2->setText(QApplication::translate("LaCropParameterManagerBase", "Fallow's Food Value", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbFallowValue->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food Value of Fallow Land</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbFallowValue->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the selected crop is being grown in a rotation, producing fallow land, that land can be grazed. LandUse Analyst needs to know how many calories this land can give grazing animals per year. These numbers are in KCalories per dunum/hectare. (you can select the area units)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbFallowValue->setSuffix(QString());

#ifndef QT_NO_TOOLTIP
    cbAreaUnits->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    label_4->setText(QApplication::translate("LaCropParameterManagerBase", "Notes:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leDescription->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because LandUse Analyst allows more than one type of parameter to be defined, the Notes: field allows you to give a brief description of the the parameter. For example, you may have two \"Shuna\" parameters defined, and the Notes: fields could contain \"Conservative\" and \"Optimistic\" to distinguish between them.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_2->setText(QApplication::translate("LaCropParameterManagerBase", "Crop:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cboCrop->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Crop that these parameters are for.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cboCrop->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is very important to select which crop your parameter settings are for. Once you slect the crop it appies to, simply click Apply, and it will then be properly allocated, and will show up in the dropdown list for that crop in the table on the top.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS


#ifndef QT_NO_WHATSTHIS
    groupBoxSuitableLand->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order for LandUse Analyst to create landuse maps, you must first create land suitability files to tell it what land is suitable for use by the crops and the crops. These files can be produced manually or automatically, but at the moment both must be done with external tools like QGis or GRASS. Future versions of Landuse Analyst will have the required features of these programs incorporated into it, but for now this step must be done externally. </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxSuitableLand->setTitle(QApplication::translate("LaCropParameterManagerBase", "Suitability Masks", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    checkBoxUseCommonLand->setToolTip(QApplication::translate("LaCropParameterManagerBase", "binary raster named: pigmask", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    checkBoxUseCommonLand->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes land is suitable for growing more than one type of crop. LandUse Analyst allows you to designate one suitability mask as common. Note that you can specify a crop to use both common land and specific land at the same time. If this is the case, equal preference is given to all crops using the common land.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    checkBoxUseCommonLand->setText(QApplication::translate("LaCropParameterManagerBase", "Common Land", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    checkBoxUseSpecificLand->setToolTip(QApplication::translate("LaCropParameterManagerBase", "binary raster named: pigmask", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    checkBoxUseSpecificLand->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sometimes you may want to specify that land is suitable for growing only one type of crop. LandUse Analyst allows you to designate a land suitability mask as being unique to a certain crop. Note that you can specify a crop to use both common land and specific land at the same time. For more detailed information on this, see the help section on Crop Masks Common.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    checkBoxUseSpecificLand->setText(QApplication::translate("LaCropParameterManagerBase", "Specific Land", 0, QApplication::UnicodeUTF8));
    label_3->setText(QApplication::translate("LaCropParameterManagerBase", "Raster\n"
"Mask", 0, QApplication::UnicodeUTF8));
    labelPortionDiet->setText(QApplication::translate("LaCropParameterManagerBase", "Portion of Tame Plant Diet", 0, QApplication::UnicodeUTF8));
    sbPercentTameCrop->setSuffix(QApplication::translate("LaCropParameterManagerBase", "%", 0, QApplication::UnicodeUTF8));
    labelPortionDiet_2->setText(QApplication::translate("LaCropParameterManagerBase", "Percent of harvest to re-seed", 0, QApplication::UnicodeUTF8));
    sbReseed->setSuffix(QApplication::translate("LaCropParameterManagerBase", "%", 0, QApplication::UnicodeUTF8));
    labelPortionDiet_3->setText(QApplication::translate("LaCropParameterManagerBase", "Percent of harvest to spoilage", 0, QApplication::UnicodeUTF8));
    sbSpoilage->setSuffix(QApplication::translate("LaCropParameterManagerBase", "%", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnApply->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnApply->setWhatsThis(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a parameter, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as LandUse Analyst has a special way of saving parameters to allow for duplicate parameter names. It is helpful, however, to utilize the Notes field to distinguish between same-named parameter definitions.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnApply->setText(QApplication::translate("LaCropParameterManagerBase", "Apply", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnClose->setToolTip(QApplication::translate("LaCropParameterManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pbnClose->setText(QApplication::translate("LaCropParameterManagerBase", "Close", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaCropParameterManagerBase);
    } // retranslateUi

};

namespace Ui {
    class LaCropParameterManagerBase: public Ui_LaCropParameterManagerBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LACROPPARAMETERMANAGERBASE_H
