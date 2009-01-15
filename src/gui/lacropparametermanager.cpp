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
#include "lacropparametermanager.h"
#include "lautils.h"
#include "lacrop.h"
#include "lagrass.h"
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
#include <QComboBox>

  LaCropParameterManager::LaCropParameterManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  connect(tblCropParameterProfiles, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
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
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
  lblCropPic->setScaledContents(true);
 //populate the plants combo
  LaUtils::CropMap myCropsMap;
  myCropsMap = LaUtils::getAvailableCrops();
  QMapIterator<QString, LaCrop> myIterator(myCropsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCrop myCrop = myIterator.value();
    QString myGuid = myCrop.guid();
    QString myName = myCrop.name();
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    cboCrop->addItem(myName,myGuid);
  }
  connect(cboCrop, SIGNAL(currentIndexChanged( int)),
      this, SLOT(on_cboCrop_changed( int)));

  // insert all area units into the comboBox
  comboBoxAreaUnits->addItem("Dunum");
  comboBoxAreaUnits->addItem("Hectare");

  refreshCropParameterTable();
}

LaCropParameterManager::~LaCropParameterManager()
{
  writeSettings();
}

void LaCropParameterManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaCropParameterManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaCropParameterManager::refreshCropParameterTable(QString theGuid)
{

  mCropParameterMap.clear();
  tblCropParameterProfiles->clear();
  tblCropParameterProfiles->setRowCount(0);
  tblCropParameterProfiles->setColumnCount(2);


  //we do this in two passes
  //in the first pass we populate a qmap with all the layersets
  //we find....
  mCropParameterMap = LaUtils::getAvailableCropParameters();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaCropParameter> myIterator(mCropParameterMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCropParameter myCropParameter = myIterator.value();
    //qDebug(myCropParameter.toText().toLocal8Bit());
    if (theGuid.isEmpty())
    {
     //qDebug("No default active row was requested.Assigning to myCropParameter.guid()!");;
      theGuid=myCropParameter.guid();
    }
    if (myCropParameter.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblCropParameterProfiles->insertRow(myCurrentRow);
    QString myGuid = myCropParameter.guid();
   //qDebug ("Inserting crop parameter with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblCropParameterProfiles->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myCropParameter.name()  + "  (" + myCropParameter.description() + ")");
    tblCropParameterProfiles->setItem(myCurrentRow, 1, mypNameItem);
    //display an icon indicating if the layerset is local or remote (e.g. terralib)
    //LaCropParameter::Origin myOrigin = myCropParameter.origin();
    //if (myOrigin==LaCropParameter::USERPROFILE)
    //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaCropParameter::ADAPTERPROFILE)
    //{
    //QIcon myIcon;
    //myIcon.addFile(":/remotedata.png");
    //mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaCropParameter::UNDEFINED)
    //{
    //  mypNameItem->setTextColor(Qt::yellow);
    //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblCropParameterProfiles->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblCropParameterProfiles->setHorizontalHeaderLabels(headerLabels);
  tblCropParameterProfiles->setColumnWidth(0,0);
  tblCropParameterProfiles->setColumnWidth(1,tblCropParameterProfiles->width());
  tblCropParameterProfiles->horizontalHeader()->hide();
  tblCropParameterProfiles->verticalHeader()->hide();
  tblCropParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropParameterManager::on_cboCrop_changed(int theIndex)
{
  LaCrop myCrop = LaUtils::getCrop(cboCrop->itemData(cboCrop->currentIndex(),Qt::UserRole).toString());
  QString myCropPic = myCrop.imageFile();


  lblCropPic->setPixmap(myCropPic);
}

void LaCropParameterManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id because user may have customised params
 //qDebug("LaCropParameterManager::cellClicked");
  QString myGuid = tblCropParameterProfiles->item(tblCropParameterProfiles->currentRow(),0)->text();
 //qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectCropParameter(myFileName);
  LaCrop myCrop = LaUtils::getCrop(cboCrop->itemData(cboCrop->currentIndex(),Qt::UserRole).toString());
  QString myAnimalPic = myCrop.imageFile();
  lblCropPic->setPixmap(myAnimalPic);
}
void LaCropParameterManager::selectCropParameter(QString theFileName)
{
 //qDebug("selectCropParameter Called : " + theFileName.toLocal8Bit());
  QString myCropParameterDir = LaUtils::userCropParameterProfilesDirPath();
  LaCropParameter myCropParameter;
  myCropParameter.fromXmlFile(myCropParameterDir + QDir::separator() + theFileName);
  leName->setText(myCropParameter.name());
  mCropParameter=myCropParameter;
  showCropParameter();
}

void LaCropParameterManager::showCropParameter()
{
  leName->setText(mCropParameter.name());
  leDescription->setText(mCropParameter.description());
  setComboToDefault(cboCrop, mCropParameter.cropGuid());
  sbPercentTameCrop->setValue(mCropParameter.percentTameCrop());
  grpCropRotation->setChecked(mCropParameter.cropRotation());
  sbFallowRatio->setValue(mCropParameter.fallowRatio());
  sbFallowValue->setValue(mCropParameter.fallowTDN());
  comboBoxAreaUnits->setCurrentIndex(mCropParameter.areaUnits());
  checkBoxUseCommonLand->setChecked(mCropParameter.useCommonLand());
  checkBoxUseSpecificLand->setChecked(mCropParameter.useSpecificLand());
  //cboRastere->setText(mCropParameter.rasterName());
}

void LaCropParameterManager::on_toolNew_clicked()
{
 //qDebug("New toolbutton clicked");
  LaCropParameter myCropParameter;
  myCropParameter.setGuid();
  mCropParameter = myCropParameter;
  showCropParameter();
}

void LaCropParameterManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblCropParameterProfiles->setColumnWidth(0,0);
  tblCropParameterProfiles->setColumnWidth(1,tblCropParameterProfiles->width());
  tblCropParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropParameterManager::on_toolCopy_clicked()
{
 //qDebug("Copy toolbutton clicked");
  if (tblCropParameterProfiles->currentRow() < 0)
  {
    return;
  }
  //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblCropParameterProfiles->item(tblCropParameterProfiles->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userCropParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaCropParameter myCropParameter;
  myCropParameter.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mCropParameter.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myCropParameter.name();
  }
  */
  //assign this layerset its own guid
  myCropParameter.setGuid();
  QString myNewFileName = LaUtils::userCropParameterProfilesDirPath() + QDir::separator() + myCropParameter.guid() + ".xml";
  myCropParameter.setName(tr("Copy of ") + myCropParameter.name());
  myCropParameter.toXmlFile(myNewFileName);
  refreshCropParameterTable(myCropParameter.guid());
}
void LaCropParameterManager::on_toolDelete_clicked()
{
 //qDebug("Delete toolbutton clicked");
  if (tblCropParameterProfiles->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblCropParameterProfiles->item(tblCropParameterProfiles->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userCropParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshCropParameterTable();
  }
}
void LaCropParameterManager::on_pbnApply_clicked()
{
  mCropParameter.setName(leName->text());
  mCropParameter.setDescription(leDescription->text());
  mCropParameter.setCropGuid(cboCrop->itemData(cboCrop->currentIndex(),Qt::UserRole).toString());
  mCropParameter.setPercentTameCrop(sbPercentTameCrop->value());
  mCropParameter.setCropRotation(grpCropRotation->isChecked());
  mCropParameter.setFallowRatio(sbFallowRatio->value());
  mCropParameter.setFallowValue(sbFallowValue->value());

  QString mySelectedAreaUnit = QString(comboBoxAreaUnits->currentText());
  AreaUnits myAreaUnits;
  if (mySelectedAreaUnit == "Dunum")
  {
    myAreaUnits = Dunum;
    mCropParameter.setAreaUnits(myAreaUnits);
  }
  else if (mySelectedAreaUnit == "Hectare")
  {
    myAreaUnits = Hectare;
    mCropParameter.setAreaUnits(myAreaUnits);
  }

  mCropParameter.setUseCommonLand(checkBoxUseCommonLand->isChecked());
  mCropParameter.setUseSpecificLand(checkBoxUseSpecificLand->isChecked());
  mCropParameter.setRasterName(cboRaster->currentText());
  mCropParameter.toXmlFile( LaUtils::userCropParameterProfilesDirPath() +
      QDir::separator() + mCropParameter.guid() + ".xml");
  refreshCropParameterTable(mCropParameter.guid());
}
bool LaCropParameterManager::setComboToDefault(QComboBox * thepCombo, QString theDefault)
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
