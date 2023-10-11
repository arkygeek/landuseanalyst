/********************************************************************************
** Form generated from reading ui file 'lacropmanagerbase.ui'
**
** Created: Mon Mar 16 19:50:20 2009
**      by: Qt User Interface Compiler version 4.4.3
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_LACROPMANAGERBASE_H
#define UI_LACROPMANAGERBASE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QFrame>
#include <QtGui/QGridLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QSpinBox>
#include <QtGui/QTableWidget>
#include <QtGui/QToolButton>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_LaCropManagerBase
{
public:
    QGridLayout *gridLayout_2;
    QGroupBox *grpProfiles;
    QGridLayout *gridLayout;
    QGridLayout *gridLayout1;
    QToolButton *toolNew;
    QToolButton *toolDelete;
    QToolButton *toolCopy;
    QSpacerItem *spacerItem;
    QLabel *lblCropPix;
    QTableWidget *tblCrops;
    QPushButton *pbnImport;
    QPushButton *pbnExport;
    QSpacerItem *spacerItem1;
    QGroupBox *groupBoxPlantDescription;
    QGridLayout *gridLayout2;
    QLabel *label;
    QLineEdit *leName;
    QLabel *label_4;
    QLineEdit *leDescription;
    QPushButton *pbnCropPic;
    QFrame *line_2;
    QVBoxLayout *vboxLayout;
    QLabel *labelPlantDescription4;
    QLabel *labelPlantDescription6;
    QLabel *label_3;
    QVBoxLayout *vboxLayout1;
    QSpinBox *sbCropYield;
    QSpinBox *sbCropFodderProduction;
    QComboBox *cbAreaUnits;
    QLabel *label_2;
    QSpinBox *sbCropCalories;
    QFrame *line;
    QLabel *label_5;
    QSpinBox *sbCropFodderValue;
    QComboBox *cbFodderEnergyType;
    QSpacerItem *spacerItem2;
    QPushButton *pbnApply;
    QPushButton *pbnClose;

    void setupUi(QDialog *LaCropManagerBase)
    {
    if (LaCropManagerBase->objectName().isEmpty())
        LaCropManagerBase->setObjectName(QString::fromUtf8("LaCropManagerBase"));
    LaCropManagerBase->resize(454, 456);
    QIcon icon;
    icon.addPixmap(QPixmap(QString::fromUtf8(":/la_icon_small.png")), QIcon::Normal, QIcon::Off);
    LaCropManagerBase->setWindowIcon(icon);
    gridLayout_2 = new QGridLayout(LaCropManagerBase);
    gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
    grpProfiles = new QGroupBox(LaCropManagerBase);
    grpProfiles->setObjectName(QString::fromUtf8("grpProfiles"));
    gridLayout = new QGridLayout(grpProfiles);
#ifndef Q_OS_MAC
    gridLayout->setSpacing(6);
#endif
#ifndef Q_OS_MAC
    gridLayout->setMargin(9);
#endif
    gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
    gridLayout1 = new QGridLayout();
#ifndef Q_OS_MAC
    gridLayout1->setSpacing(6);
#endif
#ifndef Q_OS_MAC
    gridLayout1->setMargin(0);
#endif
    gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
    toolNew = new QToolButton(grpProfiles);
    toolNew->setObjectName(QString::fromUtf8("toolNew"));
    QIcon icon1;
    icon1.addPixmap(QPixmap(QString::fromUtf8(":/new.png")), QIcon::Normal, QIcon::Off);
    toolNew->setIcon(icon1);

    gridLayout1->addWidget(toolNew, 2, 0, 1, 1);

    toolDelete = new QToolButton(grpProfiles);
    toolDelete->setObjectName(QString::fromUtf8("toolDelete"));
    QIcon icon2;
    icon2.addPixmap(QPixmap(QString::fromUtf8(":/delete.png")), QIcon::Normal, QIcon::Off);
    toolDelete->setIcon(icon2);

    gridLayout1->addWidget(toolDelete, 2, 2, 1, 1);

    toolCopy = new QToolButton(grpProfiles);
    toolCopy->setObjectName(QString::fromUtf8("toolCopy"));
    QIcon icon3;
    icon3.addPixmap(QPixmap(QString::fromUtf8(":/copy.png")), QIcon::Normal, QIcon::Off);
    toolCopy->setIcon(icon3);

    gridLayout1->addWidget(toolCopy, 2, 1, 1, 1);

    spacerItem = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

    gridLayout1->addItem(spacerItem, 1, 1, 1, 1);

    lblCropPix = new QLabel(grpProfiles);
    lblCropPix->setObjectName(QString::fromUtf8("lblCropPix"));
    QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    sizePolicy.setHorizontalStretch(0);
    sizePolicy.setVerticalStretch(0);
    sizePolicy.setHeightForWidth(lblCropPix->sizePolicy().hasHeightForWidth());
    lblCropPix->setSizePolicy(sizePolicy);
    lblCropPix->setMinimumSize(QSize(100, 100));
    lblCropPix->setMaximumSize(QSize(100, 100));
    lblCropPix->setAlignment(Qt::AlignCenter);

    gridLayout1->addWidget(lblCropPix, 0, 0, 1, 3);


    gridLayout->addLayout(gridLayout1, 0, 3, 2, 1);

    tblCrops = new QTableWidget(grpProfiles);
    if (tblCrops->columnCount() < 2)
        tblCrops->setColumnCount(2);
    QTableWidgetItem *__colItem = new QTableWidgetItem();
    tblCrops->setHorizontalHeaderItem(0, __colItem);
    QTableWidgetItem *__colItem1 = new QTableWidgetItem();
    tblCrops->setHorizontalHeaderItem(1, __colItem1);
    tblCrops->setObjectName(QString::fromUtf8("tblCrops"));
    QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
    sizePolicy1.setHorizontalStretch(0);
    sizePolicy1.setVerticalStretch(0);
    sizePolicy1.setHeightForWidth(tblCrops->sizePolicy().hasHeightForWidth());
    tblCrops->setSizePolicy(sizePolicy1);
    tblCrops->setMinimumSize(QSize(0, 0));
    tblCrops->setAlternatingRowColors(true);
    tblCrops->setSelectionMode(QAbstractItemView::SingleSelection);
    tblCrops->setSelectionBehavior(QAbstractItemView::SelectRows);

    gridLayout->addWidget(tblCrops, 0, 0, 1, 3);

    pbnImport = new QPushButton(grpProfiles);
    pbnImport->setObjectName(QString::fromUtf8("pbnImport"));
    pbnImport->setMinimumSize(QSize(80, 0));

    gridLayout->addWidget(pbnImport, 1, 0, 1, 1);

    pbnExport = new QPushButton(grpProfiles);
    pbnExport->setObjectName(QString::fromUtf8("pbnExport"));
    pbnExport->setMinimumSize(QSize(80, 0));

    gridLayout->addWidget(pbnExport, 1, 1, 1, 1);

    spacerItem1 = new QSpacerItem(111, 27, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout->addItem(spacerItem1, 1, 2, 1, 1);


    gridLayout_2->addWidget(grpProfiles, 0, 0, 1, 3);

    groupBoxPlantDescription = new QGroupBox(LaCropManagerBase);
    groupBoxPlantDescription->setObjectName(QString::fromUtf8("groupBoxPlantDescription"));
    gridLayout2 = new QGridLayout(groupBoxPlantDescription);
    gridLayout2->setObjectName(QString::fromUtf8("gridLayout2"));
    label = new QLabel(groupBoxPlantDescription);
    label->setObjectName(QString::fromUtf8("label"));

    gridLayout2->addWidget(label, 0, 0, 1, 2);

    leName = new QLineEdit(groupBoxPlantDescription);
    leName->setObjectName(QString::fromUtf8("leName"));

    gridLayout2->addWidget(leName, 0, 2, 1, 4);

    label_4 = new QLabel(groupBoxPlantDescription);
    label_4->setObjectName(QString::fromUtf8("label_4"));

    gridLayout2->addWidget(label_4, 1, 0, 2, 2);

    leDescription = new QLineEdit(groupBoxPlantDescription);
    leDescription->setObjectName(QString::fromUtf8("leDescription"));

    gridLayout2->addWidget(leDescription, 1, 2, 1, 3);

    pbnCropPic = new QPushButton(groupBoxPlantDescription);
    pbnCropPic->setObjectName(QString::fromUtf8("pbnCropPic"));
    sizePolicy.setHeightForWidth(pbnCropPic->sizePolicy().hasHeightForWidth());
    pbnCropPic->setSizePolicy(sizePolicy);

    gridLayout2->addWidget(pbnCropPic, 1, 5, 1, 1);

    line_2 = new QFrame(groupBoxPlantDescription);
    line_2->setObjectName(QString::fromUtf8("line_2"));
    line_2->setFrameShape(QFrame::HLine);
    line_2->setFrameShadow(QFrame::Sunken);

    gridLayout2->addWidget(line_2, 2, 1, 1, 5);

    vboxLayout = new QVBoxLayout();
    vboxLayout->setObjectName(QString::fromUtf8("vboxLayout"));
    labelPlantDescription4 = new QLabel(groupBoxPlantDescription);
    labelPlantDescription4->setObjectName(QString::fromUtf8("labelPlantDescription4"));
    QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Preferred);
    sizePolicy2.setHorizontalStretch(0);
    sizePolicy2.setVerticalStretch(0);
    sizePolicy2.setHeightForWidth(labelPlantDescription4->sizePolicy().hasHeightForWidth());
    labelPlantDescription4->setSizePolicy(sizePolicy2);
    labelPlantDescription4->setTextFormat(Qt::AutoText);
    labelPlantDescription4->setWordWrap(false);

    vboxLayout->addWidget(labelPlantDescription4);

    labelPlantDescription6 = new QLabel(groupBoxPlantDescription);
    labelPlantDescription6->setObjectName(QString::fromUtf8("labelPlantDescription6"));
    QSizePolicy sizePolicy3(QSizePolicy::Minimum, QSizePolicy::Preferred);
    sizePolicy3.setHorizontalStretch(0);
    sizePolicy3.setVerticalStretch(0);
    sizePolicy3.setHeightForWidth(labelPlantDescription6->sizePolicy().hasHeightForWidth());
    labelPlantDescription6->setSizePolicy(sizePolicy3);
    labelPlantDescription6->setTextFormat(Qt::AutoText);
    labelPlantDescription6->setWordWrap(false);

    vboxLayout->addWidget(labelPlantDescription6);

    label_3 = new QLabel(groupBoxPlantDescription);
    label_3->setObjectName(QString::fromUtf8("label_3"));

    vboxLayout->addWidget(label_3);


    gridLayout2->addLayout(vboxLayout, 3, 0, 5, 2);

    vboxLayout1 = new QVBoxLayout();
    vboxLayout1->setObjectName(QString::fromUtf8("vboxLayout1"));
    sbCropYield = new QSpinBox(groupBoxPlantDescription);
    sbCropYield->setObjectName(QString::fromUtf8("sbCropYield"));
    QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Fixed);
    sizePolicy4.setHorizontalStretch(0);
    sizePolicy4.setVerticalStretch(0);
    sizePolicy4.setHeightForWidth(sbCropYield->sizePolicy().hasHeightForWidth());
    sbCropYield->setSizePolicy(sizePolicy4);
    sbCropYield->setMaximum(400);
    sbCropYield->setValue(60);

    vboxLayout1->addWidget(sbCropYield);

    sbCropFodderProduction = new QSpinBox(groupBoxPlantDescription);
    sbCropFodderProduction->setObjectName(QString::fromUtf8("sbCropFodderProduction"));
    sizePolicy4.setHeightForWidth(sbCropFodderProduction->sizePolicy().hasHeightForWidth());
    sbCropFodderProduction->setSizePolicy(sizePolicy4);
    sbCropFodderProduction->setMaximum(400);
    sbCropFodderProduction->setValue(60);

    vboxLayout1->addWidget(sbCropFodderProduction);

    cbAreaUnits = new QComboBox(groupBoxPlantDescription);
    cbAreaUnits->setObjectName(QString::fromUtf8("cbAreaUnits"));
    QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Fixed);
    sizePolicy5.setHorizontalStretch(0);
    sizePolicy5.setVerticalStretch(0);
    sizePolicy5.setHeightForWidth(cbAreaUnits->sizePolicy().hasHeightForWidth());
    cbAreaUnits->setSizePolicy(sizePolicy5);

    vboxLayout1->addWidget(cbAreaUnits);


    gridLayout2->addLayout(vboxLayout1, 3, 2, 5, 1);

    label_2 = new QLabel(groupBoxPlantDescription);
    label_2->setObjectName(QString::fromUtf8("label_2"));

    gridLayout2->addWidget(label_2, 4, 3, 1, 1);

    sbCropCalories = new QSpinBox(groupBoxPlantDescription);
    sbCropCalories->setObjectName(QString::fromUtf8("sbCropCalories"));
    sizePolicy.setHeightForWidth(sbCropCalories->sizePolicy().hasHeightForWidth());
    sbCropCalories->setSizePolicy(sizePolicy);
    sbCropCalories->setMinimum(1);
    sbCropCalories->setMaximum(5000);
    sbCropCalories->setValue(3000);

    gridLayout2->addWidget(sbCropCalories, 4, 4, 1, 2);

    line = new QFrame(groupBoxPlantDescription);
    line->setObjectName(QString::fromUtf8("line"));
    line->setFrameShape(QFrame::HLine);
    line->setFrameShadow(QFrame::Sunken);

    gridLayout2->addWidget(line, 5, 3, 1, 3);

    label_5 = new QLabel(groupBoxPlantDescription);
    label_5->setObjectName(QString::fromUtf8("label_5"));
    label_5->setAlignment(Qt::AlignCenter);

    gridLayout2->addWidget(label_5, 6, 3, 1, 3);

    sbCropFodderValue = new QSpinBox(groupBoxPlantDescription);
    sbCropFodderValue->setObjectName(QString::fromUtf8("sbCropFodderValue"));
    sizePolicy.setHeightForWidth(sbCropFodderValue->sizePolicy().hasHeightForWidth());
    sbCropFodderValue->setSizePolicy(sizePolicy);
    sbCropFodderValue->setMinimum(1);
    sbCropFodderValue->setMaximum(500000);
    sbCropFodderValue->setSingleStep(1);
    sbCropFodderValue->setValue(1123);

    gridLayout2->addWidget(sbCropFodderValue, 7, 3, 1, 2);

    cbFodderEnergyType = new QComboBox(groupBoxPlantDescription);
    cbFodderEnergyType->setObjectName(QString::fromUtf8("cbFodderEnergyType"));

    gridLayout2->addWidget(cbFodderEnergyType, 7, 5, 1, 1);

    label->raise();
    leName->raise();
    label_4->raise();
    leDescription->raise();
    pbnCropPic->raise();
    line_2->raise();
    line->raise();
    sbCropFodderValue->raise();
    cbFodderEnergyType->raise();

    gridLayout_2->addWidget(groupBoxPlantDescription, 1, 0, 1, 3);

    spacerItem2 = new QSpacerItem(31, 31, QSizePolicy::Expanding, QSizePolicy::Minimum);

    gridLayout_2->addItem(spacerItem2, 2, 0, 1, 1);

    pbnApply = new QPushButton(LaCropManagerBase);
    pbnApply->setObjectName(QString::fromUtf8("pbnApply"));
    pbnApply->setCheckable(false);
    pbnApply->setFlat(false);

    gridLayout_2->addWidget(pbnApply, 2, 1, 1, 1);

    pbnClose = new QPushButton(LaCropManagerBase);
    pbnClose->setObjectName(QString::fromUtf8("pbnClose"));
    QSizePolicy sizePolicy6(QSizePolicy::Minimum, QSizePolicy::Fixed);
    sizePolicy6.setHorizontalStretch(0);
    sizePolicy6.setVerticalStretch(0);
    sizePolicy6.setHeightForWidth(pbnClose->sizePolicy().hasHeightForWidth());
    pbnClose->setSizePolicy(sizePolicy6);

    gridLayout_2->addWidget(pbnClose, 2, 2, 1, 1);

    QWidget::setTabOrder(tblCrops, pbnImport);
    QWidget::setTabOrder(pbnImport, pbnExport);
    QWidget::setTabOrder(pbnExport, toolNew);
    QWidget::setTabOrder(toolNew, toolCopy);
    QWidget::setTabOrder(toolCopy, toolDelete);
    QWidget::setTabOrder(toolDelete, leName);
    QWidget::setTabOrder(leName, leDescription);
    QWidget::setTabOrder(leDescription, sbCropYield);
    QWidget::setTabOrder(sbCropYield, sbCropCalories);
    QWidget::setTabOrder(sbCropCalories, sbCropFodderProduction);
    QWidget::setTabOrder(sbCropFodderProduction, sbCropFodderValue);
    QWidget::setTabOrder(sbCropFodderValue, cbAreaUnits);
    QWidget::setTabOrder(cbAreaUnits, pbnApply);
    QWidget::setTabOrder(pbnApply, pbnClose);

    retranslateUi(LaCropManagerBase);
    QObject::connect(pbnClose, SIGNAL(clicked()), LaCropManagerBase, SLOT(reject()));

    QMetaObject::connectSlotsByName(LaCropManagerBase);
    } // setupUi

    void retranslateUi(QDialog *LaCropManagerBase)
    {
    LaCropManagerBase->setWindowTitle(QApplication::translate("LaCropManagerBase", "Crop Profile Manager", 0, QApplication::UnicodeUTF8));
    grpProfiles->setTitle(QApplication::translate("LaCropManagerBase", "Available Crop Profiles", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolNew->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Define a new crop</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolNew->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you simply change the name or settings and click apply in the Crop Manager, you are just editing the Crop currently selected. To create a new Crop, you must click on the New button.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolNew->setText(QApplication::translate("LaCropManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolDelete->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete the currently selected crop</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    toolDelete->setText(QApplication::translate("LaCropManagerBase", "...", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    toolCopy->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clone the currently selected crop</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    toolCopy->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to create a new crop that is similar to one already defined, you can clone this crop to save time. All of the settings of the crop you are cloning are transferred to the new clone, but the name is changed to Clone of ... (whatever the name of the crop you are cloning was).</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    toolCopy->setText(QApplication::translate("LaCropManagerBase", "...", 0, QApplication::UnicodeUTF8));
    lblCropPix->setText(QApplication::translate("LaCropManagerBase", "No Graphic\n"
"Selected", 0, QApplication::UnicodeUTF8));
    tblCrops->horizontalHeaderItem(0)->setText(QApplication::translate("LaCropManagerBase", "FileName", 0, QApplication::UnicodeUTF8));
    tblCrops->horizontalHeaderItem(1)->setText(QApplication::translate("LaCropManagerBase", "Name", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    tblCrops->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a crop here to see and/or edit it's properties below.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    tblCrops->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model any crop, several details must be entered to define specific varieties. Crop Manager asks for general information about the crop in this section. You might want to have more than one strain of the same variety, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different strains of the same variety is quite easy. Let's say you want to have two kinds of wheat for example. The Name: field is Wheat for both, but in Notes: field, enter Hard Red for one, and Soft White for the other. The"
        "n adjust the other parameters as you wish. Even though the name is the same, the crop is saved uniquely.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnImport->setText(QApplication::translate("LaCropManagerBase", "Import", 0, QApplication::UnicodeUTF8));
    pbnExport->setText(QApplication::translate("LaCropManagerBase", "Export", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    groupBoxPlantDescription->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to enable LandUse Analyst to model any crop, several details must be entered to define specific varieties. Crop Manager asks for general information about the crop in this section. You might want to have more than one strain of the same variety, however, which is allowed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To define different strains of the same variety is quite easy. Let's say you want to have two kinds of wheat for example. The Name: field is Wheat for both, but in Notes: field, enter Hard Red for one, and Soft White for the other. The"
        "n adjust the other parameters as you wish. Even though the name is the same, the crop is saved uniquely.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    groupBoxPlantDescription->setTitle(QApplication::translate("LaCropManagerBase", "Crop Description", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("LaCropManagerBase", "Name:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leName->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the name of the crop you are defining in this field. You do not need a unique name. You can have, for example, 10 crops defined, all named \"Wheat\". LandUse Analyst uses a special method of saving the crops to eliminate the issue of duplicate filenames.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_4->setText(QApplication::translate("LaCropManagerBase", "Notes:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_WHATSTHIS
    leDescription->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Because LandUse Analyst allows more than one type of crop to be defined, the Notes: field allows you to give a brief description of the the crop. For example, you may have two \"Wheat\" crops defined, and the Notes: fields could contain \"Hard Red\" and \"Soft White\" to distinguish between them.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnCropPic->setText(QApplication::translate("LaCropManagerBase", "Set Graphic", 0, QApplication::UnicodeUTF8));
    labelPlantDescription4->setText(QApplication::translate("LaCropManagerBase", "Crop Yield", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    labelPlantDescription6->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder produced from Wheat</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    labelPlantDescription6->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder is the straw and chaff left after harvesting the grain.  Enter the number of Kilograms expected for this crop per (either) dunum or hectare</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    labelPlantDescription6->setText(QApplication::translate("LaCropManagerBase", "Fodder", 0, QApplication::UnicodeUTF8));
    label_3->setText(QApplication::translate("LaCropManagerBase", "Area Units *", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCropYield->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yield of Crop</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCropYield->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here you must enter what you think the average yield for the crop would have been. This is a measure of Kg produced per the given area of sown land.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbCropYield->setSuffix(QApplication::translate("LaCropManagerBase", " Kg/*", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCropFodderProduction->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder produced from Wheat</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCropFodderProduction->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Fodder Yield is how many Kg of Straw and Chaff (per area unit) that is <span style=\" font-weight:600;\">made available to animals for feed</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fodder is the straw and chaff left after harvesting the grain.  Enter the number of Kilograms expected to be produced from this crop per (either) dunum or hectare.  <span style=\" font-weight:600; color:#0000ff;\""
        ">Note that this fodder amount is solely for consumption by animals.</span>  If straw or chaff is being used for other purposes, it must be taken out of the total expected fodder level.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbCropFodderProduction->setSuffix(QApplication::translate("LaCropManagerBase", " Kg/*", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    cbAreaUnits->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 dunum = 1000 square meters</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 hectare = 10,000 square meters</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    cbAreaUnits->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select either Dunums or Hectares. This option is merely for convenience, to accomodate data that is available based on the two different units. (Basically I just got sick of having to convert between the two all the time! :P)</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    label_2->setText(QApplication::translate("LaCropManagerBase", "Crop Value:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCropCalories->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The number of calories in 1 Kg of that part of the crop which is eaten (ie. the grain or fruit). </p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCropCalories->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbCropCalories->setSuffix(QApplication::translate("LaCropManagerBase", " Cal/Kg", 0, QApplication::UnicodeUTF8));
    label_5->setText(QApplication::translate("LaCropManagerBase", "Food Value of Fodder:", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    sbCropFodderValue->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calories per kilogram of fodder</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    sbCropFodderValue->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food value of fodder when used as feed for domestic animals.  This is measured in calories per kilogram.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    sbCropFodderValue->setSuffix(QString());

#ifndef QT_NO_TOOLTIP
    pbnApply->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Saves all settings</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP


#ifndef QT_NO_WHATSTHIS
    pbnApply->setWhatsThis(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After completing all fields to define a crop, you <span style=\" font-weight:600;\">MUST</span> click the Apply button to save it. The name does not have to be unique, as LandUse Analyst has a special way of saving crops to allow for duplicate crop names. It is helpful, however, to utilize the Notes field to distinguish between same-named crop definitions.</p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_WHATSTHIS

    pbnApply->setText(QApplication::translate("LaCropManagerBase", "Apply", 0, QApplication::UnicodeUTF8));

#ifndef QT_NO_TOOLTIP
    pbnClose->setToolTip(QApplication::translate("LaCropManagerBase", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#0000ff;\">Have you applied your changes?</span></p></body></html>", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_TOOLTIP

    pbnClose->setText(QApplication::translate("LaCropManagerBase", "Close", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(LaCropManagerBase);
    } // retranslateUi

};

namespace Ui {
    class LaCropManagerBase: public Ui_LaCropManagerBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LACROPMANAGERBASE_H
