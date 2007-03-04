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

  LaAnimalParameterManager::LaAnimalParameterManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  connect(tblAnimalParameterProfiles, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  refreshAnimalParameterTable();
  //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
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
  //in the first pass we populate a qmap with all the layersets
  //we find....
  mAnimalParameterMap = LaUtils::getAvailableAnimalParameters();

  //the second pass populates the table
  //doing it from the map ensures that the rows
  //are sorted by layerset name

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
      qDebug("No default active row was requested.Assigning to myAnimalParameter.guid()!");;
      theGuid=myAnimalParameter.guid();
    }
    if (myAnimalParameter.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
    // Insert new row ready to fill with details
    tblAnimalParameterProfiles->insertRow(myCurrentRow);
    QString myGuid = myAnimalParameter.guid();
    qDebug ("Inserting animalParameter with guid: " + myGuid.toLocal8Bit());
    // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblAnimalParameterProfiles->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myAnimalParameter.name());
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

void LaAnimalParameterManager::cellClicked(int theRow, int theColumn)
{
  //note we use the alg name not the id becuase user may have customised params
  qDebug("LaAnimalParameterManager::cellClicked");
  QString myGuid = tblAnimalParameterProfiles->item(tblAnimalParameterProfiles->currentRow(),0)->text();
  qDebug("Guid is: " + myGuid.toLocal8Bit());
  QString myFileName = myGuid + ".xml";
  selectAnimalParameter(myFileName);
}
void LaAnimalParameterManager::selectAnimalParameter(QString theFileName)
{
  qDebug("selectAnimalParameter Called : " + theFileName);
  QString myAnimalParameterDir = LaUtils::userAnimalParameterProfilesDirPath();
  LaAnimalParameter myAnimalParameter;
  myAnimalParameter.fromXmlFile(myAnimalParameterDir + QDir::separator() + theFileName);
  mAnimalParameter=myAnimalParameter;
  showAnimalParameter();
}

void LaAnimalParameterManager::showAnimalParameter()
{
  leName->setText(mAnimalParameter.name());
  leDescription->setText(mAnimalParameter.description());
  sbPercentTameMeat->setValue(mAnimalParameter.percentTameMeat());
  checkBoxCommonRaster->setChecked(mAnimalParameter.useCommonGrazingLand());
  checkBoxSpecificRaster->setChecked(mAnimalParameter.useSpecificGrazingLand());
  sbSpecificRasterCalories->setValue(mAnimalParameter.foodValueOfSpecificGrazingLand());
  sbCommonRasterCalories->setValue(mAnimalParameter.foodValueOfCommonGrazingLand());
  comboBoxAreaUnits->setCurrentIndex(mAnimalParameter.areaUnits());
  grpFodderUse->setChecked(mAnimalParameter.fodderUse());
  sbFodderWheat->setValue(mAnimalParameter.fodderWheat());
  sbFodderWheatGrain->setValue(mAnimalParameter.fodderWheatGrain());
  sbFodderBarley->setValue(mAnimalParameter.fodderBarley());
  sbFodderBarleyGrain->setValue(mAnimalParameter.fodderBarleyGrain());
  sbFodderLentils->setValue(mAnimalParameter.fodderLentils());
  sbFodderLentilsGrain->setValue(mAnimalParameter.fodderLentilsGrain());

  comboBoxFallowUsage->setCurrentIndex(mAnimalParameter.fallowUsage());
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
  }
}
void LaAnimalParameterManager::on_pbnApply_clicked()
{
  mAnimalParameter.setName(leName->text());
  mAnimalParameter.setDescription(leDescription->text());
  mAnimalParameter.setPercentTameMeat(sbPercentTameMeat->value());
  mAnimalParameter.setUseCommonGrazingLand(checkBoxCommonRaster->isChecked());
  mAnimalParameter.setUseSpecificGrazingLand(checkBoxSpecificRaster->isChecked());
  mAnimalParameter.setFoodValueOfCommonGrazingLand(sbCommonRasterCalories->value());
  mAnimalParameter.setFoodValueOfSpecificGrazingLand(sbSpecificRasterCalories->value());
  mAnimalParameter.setFodderUse(grpFodderUse->isChecked());
  mAnimalParameter.setFodderWheat(sbFodderWheat->value());
  mAnimalParameter.setFodderWheatGrain(sbFodderWheatGrain->value());
  mAnimalParameter.setFodderBarley(sbFodderBarley->value());
  mAnimalParameter.setFodderBarleyGrain(sbFodderBarleyGrain->value());
  mAnimalParameter.setFodderLentils(sbFodderLentils->value());
  mAnimalParameter.setFodderLentilsGrain(sbFodderLentilsGrain->value());

  mAnimalParameter.setAreaUnits(comboBoxAreaUnits->currentIndex());
  mAnimalParameter.setFallowUsage(comboBoxFallowUsage->currentIndex());
  mAnimalParameter.toXmlFile( LaUtils::userAnimalParameterProfilesDirPath() +
      QDir::separator() + mAnimalParameter.guid() + ".xml");
  refreshAnimalParameterTable(mAnimalParameter.guid());
}
