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
#include "lacropmanager.h"
#include "lautils.h"
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

  LaCropManager::LaCropManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  connect(tblCrops, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  refreshCropTable();
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
}

LaCropManager::~LaCropManager()
{
  writeSettings();
}

void LaCropManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaCropManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaCropManager::refreshCropTable(QString theGuid)
{

  mCropMap.clear();
  tblCrops->clear();
  tblCrops->setRowCount(0);
  tblCrops->setColumnCount(2);


  //we do this in two passes
  //in the first pass we populate a qmap with all the layersets
  //we find....
  mCropMap = LaUtils::getAvailableCrops();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaCrop> myIterator(mCropMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCrop myCrop = myIterator.value();
    qDebug(myCrop.toText().toLocal8Bit());
    if (theGuid.isEmpty())
    {
      qDebug("No default active row was requested.Assigning to myCrop.guid()!");;
      theGuid=myCrop.guid();
    }
    if (myCrop.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblCrops->insertRow(myCurrentRow);
    QString myGuid = myCrop.guid();
    qDebug ("Inserting crop with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblCrops->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myCrop.name());
    tblCrops->setItem(myCurrentRow, 1, mypNameItem);
    //display an icon indicating if the layerset is local or remote (e.g. terralib)
    //LaCrop::Origin myOrigin = myCrop.origin();
    //if (myOrigin==LaCrop::USERPROFILE)
    //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaCrop::ADAPTERPROFILE)
    //{
    //QIcon myIcon;
    //myIcon.addFile(":/remotedata.png");
    //mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaCrop::UNDEFINED)
    //{
    //  mypNameItem->setTextColor(Qt::yellow);
    //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblCrops->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblCrops->setHorizontalHeaderLabels(headerLabels);
  tblCrops->setColumnWidth(0,0);
  tblCrops->setColumnWidth(1,tblCrops->width());
  tblCrops->horizontalHeader()->hide();
  tblCrops->verticalHeader()->hide();
  tblCrops->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id because user may have customised params
  qDebug("LaCropManager::cellClicked");
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
  qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectCrop(myFileName);
}
void LaCropManager::selectCrop(QString theFileName)
{
  qDebug("selectCrop Called : " + theFileName.toLocal8Bit());
  QString myCropDir = LaUtils::userCropProfilesDirPath();
  LaCrop myCrop;
  myCrop.fromXmlFile(myCropDir + QDir::separator() + theFileName);
  leName->setText(myCrop.name());
  mCrop=myCrop;
  showCrop();
}

void LaCropManager::showCrop()
{
  leName->setText(mCrop.name());
  leDescription->setText(mCrop.description());
  spinBoxCropYield->setValue(mCrop.cropYield());
  spinBoxCropCalories->setValue(mCrop.cropCalories());
  spinBoxCropFodderProduction->setValue(mCrop.fodderProduction());
  spinBoxCropFodderCalories->setValue(mCrop.fodderCalories());
  comboBoxYieldUnits->setCurrentIndex(mCrop.yieldUnits());
}

void LaCropManager::on_pushButtonLoad_clicked()
{
  //
  mCrop.fromXmlFile("/tmp/crop.xml");
  showCrop();
}

void LaCropManager::on_pushButtonSave_clicked()
{

}
void LaCropManager::on_toolNew_clicked()
{
  qDebug("New toolbutton clicked");
  LaCrop myCrop;
  myCrop.setGuid();
  mCrop = myCrop;
  showCrop();
}

void LaCropManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblCrops->setColumnWidth(0,0);
  tblCrops->setColumnWidth(1,tblCrops->width());
  tblCrops->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropManager::on_toolCopy_clicked()
{
  qDebug("Copy toolbutton clicked");
  if (tblCrops->currentRow() < 0)
  {
    return;
  }
  //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userCropProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaCrop myCrop;
  myCrop.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mCrop.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myCrop.name();
  }
  */
  //assign this layerset its own guid
  myCrop.setGuid();
  QString myNewFileName = LaUtils::userCropProfilesDirPath() + QDir::separator() + myCrop.guid() + ".xml";
  myCrop.setName(tr("Copy of ") + myCrop.name());
  myCrop.toXmlFile(myNewFileName);
  refreshCropTable(myCrop.guid());
}
void LaCropManager::on_toolDelete_clicked()
{
  qDebug("Delete toolbutton clicked");
  if (tblCrops->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userCropProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshCropTable();
  }
}
void LaCropManager::on_pbnApply_clicked()
{
  mCrop.setName(leName->text());
  mCrop.setDescription(leDescription->text());
  mCrop.setCropYield(spinBoxCropYield->value());
  mCrop.setCropCalories(spinBoxCropCalories->value());
  mCrop.setFodderProduction(spinBoxCropFodderProduction->value());
  mCrop.setFodderCalories(spinBoxCropFodderCalories->value());
  mCrop.setYieldUnits(comboBoxYieldUnits->currentIndex());
  mCrop.toXmlFile( LaUtils::userCropProfilesDirPath() +
      QDir::separator() + mCrop.guid() + ".xml");
  refreshCropTable(mCrop.guid());
}
