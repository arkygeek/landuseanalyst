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
#include "laplantmanager.h"
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

  LaPlantManager::LaPlantManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl) 
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  connect(tblPlants, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  refreshPlantTable();
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
}

LaPlantManager::~LaPlantManager()
{
  writeSettings();
}

void LaPlantManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaPlantManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaPlantManager::refreshPlantTable(QString theGuid)
{

  mPlantMap.clear();
  tblPlants->clear();
  tblPlants->setRowCount(0);
  tblPlants->setColumnCount(2);


  //we do this in two passes
  //in the first pass we populate a qmap with all the layersets
  //we find....
  mPlantMap = LaUtils::getAvailablePlants();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaPlant> myIterator(mPlantMap);
  while (myIterator.hasNext()) 
  {
    myIterator.next();
    LaPlant myPlant = myIterator.value();
    qDebug(myPlant.toText().toLocal8Bit());
    if (theGuid.isEmpty())
    {
      qDebug("No default active row was requested.Assigning to myPlant.guid()!");;
      theGuid=myPlant.guid();
    }
    if (myPlant.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblPlants->insertRow(myCurrentRow);
    QString myGuid = myPlant.guid();
    qDebug ("Inserting plant with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblPlants->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myPlant.name());
    tblPlants->setItem(myCurrentRow, 1, mypNameItem);
    //display an icon indicating if the layerset is local or remote (e.g. terralib)
    //LaPlant::Origin myOrigin = myPlant.origin();
    //if (myOrigin==LaPlant::USERPROFILE)
    //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaPlant::ADAPTERPROFILE)
    //{
    //QIcon myIcon;
    //myIcon.addFile(":/remotedata.png");
    //mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaPlant::UNDEFINED)
    //{
    //  mypNameItem->setTextColor(Qt::yellow);
    //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblPlants->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblPlants->setHorizontalHeaderLabels(headerLabels);
  tblPlants->setColumnWidth(0,0);
  tblPlants->setColumnWidth(1,tblPlants->width());
  tblPlants->horizontalHeader()->hide();
  tblPlants->verticalHeader()->hide();
  tblPlants->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaPlantManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id because user may have customised params
  qDebug("LaPlantManager::cellClicked");
  QString myGuid = tblPlants->item(tblPlants->currentRow(),0)->text();
  qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectPlant(myFileName);
}
void LaPlantManager::selectPlant(QString theFileName)
{
  qDebug("selectPlant Called : " + theFileName);
  QString myPlantDir = LaUtils::userPlantProfilesDirPath();
  LaPlant myPlant;
  myPlant.fromXmlFile(myPlantDir + QDir::separator() + theFileName);
  leName->setText(myPlant.name());
  mPlant=myPlant;
  showPlant();
}

void LaPlantManager::showPlant()
{
  leName->setText(mPlant.name());
  leDescription->setText(mPlant.description());
  spinBoxCropYield->setValue(mPlant.cropYield());
  spinBoxCropCalories->setValue(mPlant.cropCalories());
  spinBoxCropFodderProduction->setValue(mPlant.fodderProduction());
  spinBoxCropFodderCalories->setValue(mPlant.fodderCalories());
  comboBoxYieldUnits->setCurrentIndex(mPlant.yieldUnits());
}

void LaPlantManager::on_pushButtonLoad_clicked()
{
  //
  mPlant.fromXmlFile("/tmp/plant.xml");
  showPlant();
}

void LaPlantManager::on_pushButtonSave_clicked()
{

}
void LaPlantManager::on_toolNew_clicked()
{
  qDebug("New toolbutton clicked");
  LaPlant myPlant;
  myPlant.setGuid();
  mPlant = myPlant;
  showPlant();
}

void LaPlantManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblPlants->setColumnWidth(0,0);
  tblPlants->setColumnWidth(1,tblPlants->width());
  tblPlants->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaPlantManager::on_toolCopy_clicked()
{
  qDebug("Copy toolbutton clicked");
  if (tblPlants->currentRow() < 0)
  {
    return;
  }
  //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblPlants->item(tblPlants->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userPlantProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaPlant myPlant;
  myPlant.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mPlant.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myPlant.name();
  }
  */
  //assign this layerset its own guid
  myPlant.setGuid();
  QString myNewFileName = LaUtils::userPlantProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  myPlant.setName(tr("Copy of ") + myPlant.name());
  myPlant.toXmlFile(myNewFileName);
  refreshPlantTable(myPlant.guid());
}
void LaPlantManager::on_toolDelete_clicked()
{
  qDebug("Delete toolbutton clicked");
  if (tblPlants->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblPlants->item(tblPlants->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userPlantProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshPlantTable();
  }
}
void LaPlantManager::on_pbnApply_clicked()
{
  mPlant.setName(leName->text());
  mPlant.setCropYield(spinBoxCropYield->value());
  mPlant.setCropCalories(spinBoxCropCalories->value());
  mPlant.setFodderProduction(spinBoxCropFodderProduction->value());
  mPlant.setFodderCalories(spinBoxCropFodderCalories->value());
  mPlant.setYieldUnits(comboBoxYieldUnits->currentIndex());
  mPlant.toXmlFile( LaUtils::userPlantProfilesDirPath() +
      QDir::separator() + mPlant.guid() + ".xml");
  refreshPlantTable(mPlant.guid());
}
