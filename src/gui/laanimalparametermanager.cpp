/***************************************************************************
 *   Copyright (C) 2007 by: Jason Jorgenson   arkygeek@gmail.com           *
 *             (c) 2007 by: Tim Sutton tim@linfiniti.com
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
#include "laanimalparametermanager.h"
#include "la.h"
#include "lautils.h"
#include "laanimal.h"
#include "lafoodsource.h"
#include "lamainform.h"
#include "lagrass.h"
#include "laassemblageconversion.h"
#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QString>
#include <QMessageBox>
#include <QHeaderView>
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QFileDialog>
#include <QListWidgetItem>
#include <QIcon>
#include <QtDebug>
#include <QPair>

  LaAnimalParameterManager::LaAnimalParameterManager(QPair<LaTripleMap, int> & thePair, AreaUnits & theAreaUnits, EnergyType & theEnergyType, QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  lblAnimalPic->setScaledContents(true);
  QStringList myList;
  LaGrass myGrass;
  QStringList myMapsetList = myGrass.getMapsetList();
  QStringListIterator myIterator1(myMapsetList);
  while (myIterator1.hasNext())
  {
    //append the raster names in this mapet to our full list
    myList << myGrass.getRasterList(myIterator1.next());
  }
  //myGrass.getRasterList(myMapsetList);
  cboRaster->addItems(myList);
  mSelectedCropsMap = thePair.first;
  mCommonGrazedLandTDN = thePair.second;
  mCommonGrazingLandAreaUnits = theAreaUnits;
  sbCommonRasterValue->setReadOnly(false);
  sbCommonRasterValue->setValue(mCommonGrazedLandTDN);
  sbCommonRasterValue->setReadOnly(true);
  connect(tblAnimalParameterProfiles, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  connect(cboAnimal, SIGNAL(currentIndexChanged( int)),
      this, SLOT(on_cboAnimal_changed( int)));
  //connect(pbnMore, SIGNAL(clicked()),
      //this, SLOT(on_pbnMore_clicked()));
  refreshAnimalParameterTable();
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
  //populate the animals combo
  LaUtils::AnimalMap myAnimalsMap;
  myAnimalsMap = LaUtils::getAvailableAnimals();
  QMapIterator<QString, LaAnimal> myIterator(myAnimalsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaAnimal myAnimal = myIterator.value();
    QString myGuid = myAnimal.guid();
    QString myName = myAnimal.name();
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    cboAnimal->addItem(myName,myGuid);
  }
  comboBoxAreaUnits->addItem("Dunum");
  comboBoxAreaUnits->addItem("Hectare");
  //comboBoxSpecificLandEnergyType->addItem("KCalories");
  //comboBoxSpecificLandEnergyType->addItem("TDN");
  setSpecificLandEnergyType();
  setFallowComboBox();
  populateFodder();
  refreshAnimalParameterTable();
}

LaAnimalParameterManager::~LaAnimalParameterManager()
{
  writeSettings();
}

void LaAnimalParameterManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaAnimalParameterManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaAnimalParameterManager::refreshAnimalParameterTable(QString theGuid)
{

  mAnimalParameterMap.clear();
  tblAnimalParameterProfiles->clear();
  tblAnimalParameterProfiles->setRowCount(0);
  tblAnimalParameterProfiles->setColumnCount(2);


  //we do this in two passes
  //in the first pass we populate a qmap with all the animal parameters
  //we find....
  mAnimalParameterMap = LaUtils::getAvailableAnimalParameters();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by animalparameter name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaAnimalParameter> myIterator(mAnimalParameterMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaAnimalParameter myAnimalParameter = myIterator.value();
    //qDebug(myAnimalParameter.toText().toLocal8Bit());
    if (theGuid.isEmpty())
    {
      qDebug("No default active row was requested.Assigning to myAnimalParameter.guid()!");
      theGuid=myAnimalParameter.guid();
    }
    if (myAnimalParameter.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblAnimalParameterProfiles->insertRow(myCurrentRow);
    QString myGuid = myAnimalParameter.guid();
    qDebug ("Inserting animalParameter into table with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblAnimalParameterProfiles->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myAnimalParameter.name()  + "  (" + myAnimalParameter.description() + ")");
    tblAnimalParameterProfiles->setItem(myCurrentRow, 1, mypNameItem);
    //display an icon indicating if the layerset is local or remote (e.g. terralib)
    //LaAnimalParameter::Origin myOrigin = myAnimalParameter.origin();
    //if (myOrigin==LaAnimalParameter::USERPROFILE)
    //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaAnimalParameter::ADAPTERPROFILE)
    //{
    //QIcon myIcon;
    //myIcon.addFile(":/remotedata.png");
    //mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaAnimalParameter::UNDEFINED)
    //{
    //  mypNameItem->setTextColor(Qt::yellow);
    //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblAnimalParameterProfiles->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblAnimalParameterProfiles->setHorizontalHeaderLabels(headerLabels);
  tblAnimalParameterProfiles->setColumnWidth(0,0);
  tblAnimalParameterProfiles->setColumnWidth(1,tblAnimalParameterProfiles->width());
  tblAnimalParameterProfiles->horizontalHeader()->hide();
  tblAnimalParameterProfiles->verticalHeader()->hide();
  tblAnimalParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaAnimalParameterManager::populateFodder()
{

  qDebug() << "++==++ mCropsMap line 185" << mSelectedCropsMap;

  tblFodder->clear();
  tblFodder->setRowCount(0);
  tblFodder->setColumnCount(3);

  int myCurrentRow=0;
  QMap<QString,LaCrop> myCropsMap;
  myCropsMap = LaUtils::getAvailableCrops();

  QMapIterator<QString, LaCrop> myIterator(myCropsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCrop myCrop = myIterator.value();
    QString myGuid = myCrop.guid();
    QString myName = myCrop.name();

    tblFodder->insertRow(myCurrentRow);
    // Add details to the new row
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myCrop.name());

    if (mSelectedCropsMap.contains(myGuid) == true)
    {
      QPair <bool, QString> myPair = mSelectedCropsMap.value(myGuid);
      if (myPair.first)
      {
        QIcon myIcon;
        myIcon.addFile(":/status_ok.png");
        mypNameItem->setIcon(myIcon);
      }
      else
      {
        QIcon myIcon;
        myIcon.addFile(":/status_error.png");
        mypNameItem->setIcon(myIcon);
      }
    }
    else
    {
      QIcon myIcon;
      myIcon.addFile(":/status_error.png");
      mypNameItem->setIcon(myIcon);
    }

    mypNameItem->setCheckState(Qt::Unchecked);
    mypNameItem->setData(Qt::UserRole,myGuid);
    tblFodder->setItem(myCurrentRow, 0, mypNameItem);
    //mypNameItem->setIcon(myIcon);
    //create a var to hold the percentage for each selected parameter
    //add the crop parameters combo to the form
    QSpinBox * mypSpinFodder = new QSpinBox(this);
    //mypSpinFodder->addItem(myParameterName,myParameterGuid);
    QSpinBox * mypSpinGrain = new QSpinBox(this);

    const int myDefaultFodderValue=0;
    const int myDefaultGrainValue=0;

    mypSpinFodder->setValue(myDefaultFodderValue);
    mypSpinGrain->setValue(myDefaultGrainValue);

    //myCropsMap[myGuid]=myValue;
    tblFodder->setCellWidget ( myCurrentRow, 1, mypSpinFodder);
    tblFodder->setCellWidget ( myCurrentRow, 2, mypSpinGrain);

    myCurrentRow++;
  }
}

void LaAnimalParameterManager::refreshFodderTable(QString theGuid)
{
  LaFoodSourceMap myFoodSourceMap = mAnimalParameter.fodderSourceMap();
  qDebug("Restoring " + QString::number(myFoodSourceMap.count()).toLocal8Bit()
    + " food sources into animal parameter.");
  for (int myCurrentRow=0; myCurrentRow < tblFodder->rowCount(); myCurrentRow++)
  {
    QTableWidgetItem * mypItem = tblFodder->item(myCurrentRow,0);
    QString myGuid = mypItem->data(Qt::UserRole).toString();
    qDebug("tblFodderGuid: " + myGuid.toLocal8Bit());
    QSpinBox * mypFodderSpinBox = qobject_cast <QSpinBox *> (tblFodder->cellWidget(myCurrentRow,1));
    QSpinBox * mypGrainSpinBox = qobject_cast <QSpinBox *> (tblFodder->cellWidget(myCurrentRow,2));
    if (myFoodSourceMap.contains(myGuid))
    {
      LaFoodSource myFoodSource = myFoodSourceMap.value(myGuid);
      int myFodderValue = myFoodSource.fodder();
      int myGrainValue = myFoodSource.grain();
      ///@TODO remove this debug stuff
      qDebug("value from map for myFodderValue: " + QString::number(myFodderValue).toLocal8Bit());
      qDebug("value from map for myGrainValue: " + QString::number(myGrainValue).toLocal8Bit());
      mypFodderSpinBox->setValue(myFodderValue);
      mypGrainSpinBox->setValue(myGrainValue);
      mypItem->setCheckState(Qt::Checked);
      qDebug("++++ Crop Guid in fodder Table: " + myGuid.toLocal8Bit());
      //Q_ASSERT(mySelectedCropsMap.contains(myGuid));
      //QString myGuidFromSelectedMap = mySelectedCropsMap.value(myGuid);
      //qDebug("++-- Crop Guid from selected map: " + myGuidFromSelectedMap.toLocal8Bit());
      //qDebug() << "++-- Crop Guid from selected map:" << myGuidFromSelectedMap;
    }
    else
    {
      mypFodderSpinBox->setValue(0);
      mypGrainSpinBox->setValue(0);
      mypItem->setCheckState(Qt::Unchecked);
    }

  }
}

void LaAnimalParameterManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id becuase user may have customised params
  //qDebug("LaAnimalParameterManager::cellClicked");
  QString myGuid = tblAnimalParameterProfiles->item(tblAnimalParameterProfiles->currentRow(),0)->text();
  //qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectAnimalParameter(myFileName);
}
void LaAnimalParameterManager::selectAnimalParameter(QString theFileName)
{
  //qDebug("selectAnimalParameter Called : " + theFileName.toLocal8Bit());
  QString myAnimalParameterDir = LaUtils::userAnimalParameterProfilesDirPath();
  mAnimalParameter.fromXmlFile(myAnimalParameterDir + QDir::separator() + theFileName);
  //
  //for debuggin only:
  //
  qDebug("-- Restoring " + QString::number(mAnimalParameter.fodderSourceMap().count()).toLocal8Bit()
    + " food sources into animal parameter.");
  // end of deub section
  showAnimalParameter();
}

void LaAnimalParameterManager::showAnimalParameter()
{
  leName->setText(mAnimalParameter.name());
  leDescription->setText(mAnimalParameter.description());
  setComboToDefault(cboAnimal, mAnimalParameter.animalGuid());
  sbPercentTameMeat->setValue(mAnimalParameter.percentTameMeat());
  checkBoxCommonRaster->setChecked(mAnimalParameter.useCommonGrazingLand());
  checkBoxSpecificRaster->setChecked(mAnimalParameter.useSpecificGrazingLand());
  sbSpecificRasterValue->setValue(mAnimalParameter.ValueSpecificGrazingLand());
  sbCommonRasterValue->setValue(mCommonGrazedLandTDN);
  comboBoxAreaUnits->setCurrentIndex(mAnimalParameter.areaUnits());
  comboBoxSpecificLandEnergyType->setCurrentIndex(mAnimalParameter.energyType());
  grpFodderUse->setChecked(mAnimalParameter.fodderUse());

  refreshFodderTable();

  if (mAnimalParameter.fallowUsage()==High)
  {
    setComboToDefault(comboBoxFallowUsage,tr("High"));
  }
  else if (mAnimalParameter.fallowUsage()==Medium)
  {
    setComboToDefault(comboBoxFallowUsage,tr("Medium"));
  }
  else if (mAnimalParameter.fallowUsage()==Low)
  {
    setComboToDefault(comboBoxFallowUsage,tr("Low"));
  }
  else
  {
    setComboToDefault(comboBoxFallowUsage,tr("None"));
  }

  //leRasterName->setText(mAnimalParameter.rasterName());
}

void LaAnimalParameterManager::on_toolNew_clicked()
{
  qDebug("New toolbutton clicked");
  LaAnimalParameter myAnimalParameter;
  myAnimalParameter.setGuid();
  mAnimalParameter = myAnimalParameter;
  showAnimalParameter();
}

void LaAnimalParameterManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblAnimalParameterProfiles->setColumnWidth(0,0);
  tblAnimalParameterProfiles->setColumnWidth(1,tblAnimalParameterProfiles->width());
  tblAnimalParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaAnimalParameterManager::on_toolCopy_clicked()
{
  qDebug("Copy toolbutton clicked");
  if (tblAnimalParameterProfiles->currentRow() < 0)
  {
    return;
  }
  //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblAnimalParameterProfiles->item(tblAnimalParameterProfiles->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userAnimalParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaAnimalParameter myAnimalParameter;
  myAnimalParameter.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mAnimalParameter.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myAnimalParameter.name();
  }
  */
  //assign this layerset its own guid
  myAnimalParameter.setGuid();
  QString myNewFileName = LaUtils::userAnimalParameterProfilesDirPath() + QDir::separator() + myAnimalParameter.guid() + ".xml";
  myAnimalParameter.setName(tr("Copy of ") + myAnimalParameter.name());
  myAnimalParameter.toXmlFile(myNewFileName);
  refreshAnimalParameterTable(myAnimalParameter.guid());
  refreshFodderTable();
}
void LaAnimalParameterManager::on_toolDelete_clicked()
{
  qDebug("Delete toolbutton clicked");
  if (tblAnimalParameterProfiles->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblAnimalParameterProfiles->item(tblAnimalParameterProfiles->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userAnimalParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshAnimalParameterTable();
    refreshFodderTable();
  }
}

void LaAnimalParameterManager::on_cboAnimal_changed(int theIndex)
{
  LaAnimal myAnimal = LaUtils::getAnimal(cboAnimal->itemData(cboAnimal->currentIndex(),Qt::UserRole).toString());
  QString myAnimalPic = myAnimal.imageFile();
  lblAnimalPic->setPixmap(myAnimalPic);
}

void LaAnimalParameterManager::on_pbnMore_clicked()
{
  LaAssemblageConversion myAssemblageConversion;
  myAssemblageConversion.exec();
}

void LaAnimalParameterManager::on_pbnApply_clicked()
{
  mAnimalParameter.setName(leName->text());
  mAnimalParameter.setDescription(leDescription->text());
  mAnimalParameter.setAnimalGuid(cboAnimal->itemData(cboAnimal->currentIndex(),Qt::UserRole).toString());
  mAnimalParameter.setPercentTameMeat(sbPercentTameMeat->value());
  mAnimalParameter.setUseCommonGrazingLand(checkBoxCommonRaster->isChecked());
  mAnimalParameter.setUseSpecificGrazingLand(checkBoxSpecificRaster->isChecked());

  QString mySelectedAreaUnit = QString(comboBoxAreaUnits->currentText());
  QString mySelectedEnergyType = QString(comboBoxSpecificLandEnergyType->currentText());
  AreaUnits myAreaUnits;
  EnergyType myEnergyType;

  if (mySelectedEnergyType == "KCalories")
  {
    myEnergyType = KCalories;
    mAnimalParameter.setEnergyType(myEnergyType);
  }
  else if (mySelectedEnergyType == "TDN")
  {
    myEnergyType = TDN;
    mAnimalParameter.setEnergyType(myEnergyType);
  }

  if (mySelectedAreaUnit == "Dunum")
  {
    myAreaUnits = Dunum;
    mAnimalParameter.setAreaUnits(myAreaUnits);
  }
  else if (mySelectedAreaUnit == "Hectare")
  {
    myAreaUnits = Hectare;
    mAnimalParameter.setAreaUnits(myAreaUnits);
  }

  mAnimalParameter.setValueCommonGrazingLand(sbCommonRasterValue->value());
  mAnimalParameter.setValueSpecificGrazingLand(sbSpecificRasterValue->value());
  mAnimalParameter.setFodderUse(grpFodderUse->isChecked());

  // populate the fodder map from the table.
  LaFoodSourceMap myFoodSourceMap;
  int myRowCount = tblFodder->rowCount();
  for (int myCurrentRow=0; myCurrentRow < myRowCount; ++myCurrentRow)
  {

    QTableWidgetItem * mypNameWidget =
      tblFodder->item(myCurrentRow,0);
    QSpinBox * mypFodderSpinBox =
      qobject_cast<QSpinBox *>
      (tblFodder->cellWidget(myCurrentRow,1));
    QSpinBox * mypGrainSpinBox =
      qobject_cast<QSpinBox *>
      (tblFodder->cellWidget(myCurrentRow,2));

    //dont bother doing anything further if the
    //first widget in the row is not checked
    if (!mypNameWidget->checkState())
    {
      continue;
    }
    LaFoodSource myFoodSource;
    myFoodSource.setFodder(mypFodderSpinBox->value());
    myFoodSource.setGrain(mypGrainSpinBox->value());
    QString myGuid = mypNameWidget->data(Qt::UserRole).toString();

    myFoodSourceMap.insert(myGuid, myFoodSource);

  }

  qDebug("Inserting " + QString::number(myFoodSourceMap.count()).toLocal8Bit()
    + " food sources into animal parameter.");
  mAnimalParameter.setFodderData(myFoodSourceMap);



  QString myFallowUsage = QString(comboBoxFallowUsage->currentText());
  //setFallowComboBox();
  Priority myPriority;
  if (myFallowUsage == "HIGH Fallow Priority")
  {
      myPriority = High;
      mAnimalParameter.setFallowUsage(myPriority);
  }
  else if (myFallowUsage == "MED Fallow Priority")
  {
      myPriority = Medium;
      mAnimalParameter.setFallowUsage(myPriority);
  }
  else if (myFallowUsage == "LOW Fallow Priority")
  {
      myPriority = Low;
      mAnimalParameter.setFallowUsage(myPriority);
  }
  else
  {
      myPriority = None;
      mAnimalParameter.setFallowUsage(myPriority);
  }
  mAnimalParameter.setRasterName(cboRaster->currentText());
  mAnimalParameter.toXmlFile( LaUtils::userAnimalParameterProfilesDirPath() +
      QDir::separator() + mAnimalParameter.guid() + ".xml");
  refreshAnimalParameterTable(mAnimalParameter.guid());
  refreshFodderTable();
}

void LaAnimalParameterManager::setSelectedCropsMap(LaTripleMap theSelectedCropsMap)
{
  mSelectedCropsMap = theSelectedCropsMap;
}

bool LaAnimalParameterManager::setComboToDefault(QComboBox * thepCombo, QString theDefault)
{
  if (!theDefault.isEmpty())
  {
    //loop through list looking for a match
    for ( int myCounter = 0; myCounter < thepCombo->count(); myCounter++ )
    {
      thepCombo->setCurrentIndex(myCounter);

      if (thepCombo->itemData(myCounter,Qt::UserRole)==theDefault)
      {
        break;
      }
    }
  }
  else
  {
    return false;
  }
  return true;
}

void LaAnimalParameterManager::setFallowComboBox()
{
  comboBoxFallowUsage->addItem("Do Not Graze Fallow", "None");
  comboBoxFallowUsage->addItem("HIGH Fallow Priority", "High");
  comboBoxFallowUsage->addItem("MED Fallow Priority", "Medium");
  comboBoxFallowUsage->addItem("LOW Fallow Priority", "Low");
}

void LaAnimalParameterManager::setSpecificLandEnergyType()
{
  comboBoxSpecificLandEnergyType->addItem(/*"Use KCalories", */"KCalories");
  comboBoxSpecificLandEnergyType->addItem(/*"Use TDN", */"TDN");
}

