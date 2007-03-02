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
#include "laplantparametermanager.h"
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

  LaPlantParameterManager::LaPlantParameterManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  connect(tblPlantParameterProfiles, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  refreshPlantParameterTable();
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
}

LaPlantParameterManager::~LaPlantParameterManager()
{
  writeSettings();
}

void LaPlantParameterManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaPlantParameterManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaPlantParameterManager::refreshPlantParameterTable(QString theGuid)
{

  mPlantParameterMap.clear();
  tblPlantParameterProfiles->clear();
  tblPlantParameterProfiles->setRowCount(0);
  tblPlantParameterProfiles->setColumnCount(2);


  //we do this in two passes
  //in the first pass we populate a qmap with all the layersets
  //we find....
  mPlantParameterMap = LaUtils::getAvailablePlantParameters();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaPlantParameter> myIterator(mPlantParameterMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaPlantParameter myPlantParameter = myIterator.value();
    qDebug(myPlantParameter.toText().toLocal8Bit());
    if (theGuid.isEmpty())
    {
      qDebug("No default active row was requested.Assigning to myPlantParameter.guid()!");;
      theGuid=myPlantParameter.guid();
    }
    if (myPlantParameter.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblPlantParameterProfiles->insertRow(myCurrentRow);
    QString myGuid = myPlantParameter.guid();
    qDebug ("Inserting plant parameter with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblPlantParameterProfiles->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myPlantParameter.name());
    tblPlantParameterProfiles->setItem(myCurrentRow, 1, mypNameItem);
    //display an icon indicating if the layerset is local or remote (e.g. terralib)
    //LaPlantParameter::Origin myOrigin = myPlantParameter.origin();
    //if (myOrigin==LaPlantParameter::USERPROFILE)
    //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaPlantParameter::ADAPTERPROFILE)
    //{
    //QIcon myIcon;
    //myIcon.addFile(":/remotedata.png");
    //mypNameItem->setIcon(myIcon);
    //}
    //else if (myOrigin==LaPlantParameter::UNDEFINED)
    //{
    //  mypNameItem->setTextColor(Qt::yellow);
    //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblPlantParameterProfiles->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblPlantParameterProfiles->setHorizontalHeaderLabels(headerLabels);
  tblPlantParameterProfiles->setColumnWidth(0,0);
  tblPlantParameterProfiles->setColumnWidth(1,tblPlantParameterProfiles->width());
  tblPlantParameterProfiles->horizontalHeader()->hide();
  tblPlantParameterProfiles->verticalHeader()->hide();
  tblPlantParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaPlantParameterManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id because user may have customised params
  qDebug("LaPlantParameterManager::cellClicked");
  QString myGuid = tblPlantParameterProfiles->item(tblPlantParameterProfiles->currentRow(),0)->text();
  qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectPlantParameter(myFileName);
}
void LaPlantParameterManager::selectPlantParameter(QString theFileName)
{
  qDebug("selectPlantParameter Called : " + theFileName);
  QString myPlantParameterDir = LaUtils::userPlantParameterProfilesDirPath();
  LaPlantParameter myPlantParameter;
  myPlantParameter.fromXmlFile(myPlantParameterDir + QDir::separator() + theFileName);
  leName->setText(myPlantParameter.name());
  mPlantParameter=myPlantParameter;
  showPlantParameter();
}

void LaPlantParameterManager::showPlantParameter()
{
  leName->setText(mPlantParameter.name());
  leDescription->setText(mPlantParameter.description());
  sbPercentTamePlant->setValue(mPlantParameter.percentTamePlant());
  grpCropRotation->setChecked(mPlantParameter.cropRotation());
  sbFallowRatio->setValue(mPlantParameter.fallowRatio());
  sbFallowCalories->setValue(mPlantParameter.fallowCalories());
  comboBoxAreaUnits->setCurrentIndex(mPlantParameter.areaUnits());
  checkBoxUseCommonLand->setChecked(mPlantParameter.useCommonLand());
  checkBoxUseSpecificLand->setChecked(mPlantParameter.useSpecificLand());
}

void LaPlantParameterManager::on_toolNew_clicked()
{
  qDebug("New toolbutton clicked");
  LaPlantParameter myPlantParameter;
  myPlantParameter.setGuid();
  mPlantParameter = myPlantParameter;
  showPlantParameter();
}

void LaPlantParameterManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblPlantParameterProfiles->setColumnWidth(0,0);
  tblPlantParameterProfiles->setColumnWidth(1,tblPlantParameterProfiles->width());
  tblPlantParameterProfiles->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaPlantParameterManager::on_toolCopy_clicked()
{
  qDebug("Copy toolbutton clicked");
  if (tblPlantParameterProfiles->currentRow() < 0)
  {
    return;
  }
  //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblPlantParameterProfiles->item(tblPlantParameterProfiles->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userPlantParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaPlantParameter myPlantParameter;
  myPlantParameter.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mPlantParameter.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myPlantParameter.name();
  }
  */
  //assign this layerset its own guid
  myPlantParameter.setGuid();
  QString myNewFileName = LaUtils::userPlantParameterProfilesDirPath() + QDir::separator() + myPlantParameter.guid() + ".xml";
  myPlantParameter.setName(tr("Copy of ") + myPlantParameter.name());
  myPlantParameter.toXmlFile(myNewFileName);
  refreshPlantParameterTable(myPlantParameter.guid());
}
void LaPlantParameterManager::on_toolDelete_clicked()
{
  qDebug("Delete toolbutton clicked");
  if (tblPlantParameterProfiles->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblPlantParameterProfiles->item(tblPlantParameterProfiles->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userPlantParameterProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshPlantParameterTable();
  }
}
void LaPlantParameterManager::on_pbnApply_clicked()
{
  mPlantParameter.setName(leName->text());
  mPlantParameter.setDescription(leDescription->text());
  mPlantParameter.setPercentTamePlant(sbPercentTamePlant->value());
  mPlantParameter.setCropRotation(grpCropRotation->isChecked());
  mPlantParameter.setFallowRatio(sbFallowRatio->value());
  mPlantParameter.setFallowCalories(sbFallowCalories->value());
  mPlantParameter.setAreaUnits(comboBoxAreaUnits->currentIndex());
  mPlantParameter.setUseCommonLand(checkBoxUseCommonLand->isChecked());
  mPlantParameter.setUseSpecificLand(checkBoxUseSpecificLand->isChecked());
  mPlantParameter.toXmlFile( LaUtils::userPlantParameterProfilesDirPath() +
      QDir::separator() + mPlantParameter.guid() + ".xml");
  refreshPlantParameterTable(mPlantParameter.guid());
}
