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
#include "laanimalmanager.h"
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
#include <QLabel>
#include <QPixmap>
#include <QDebug> 
  LaAnimalManager::LaAnimalManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
    //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  lblAnimalPix->setScaledContents(true);
  connect(tblAnimals, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
    //connect(pbnAnimalPic, SIGNAL(clicked()), this, SLOT(on_pbnAnimalPic_clicked()));

  refreshAnimalTable();
    //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
}
//
LaAnimalManager::~LaAnimalManager()
{
  writeSettings();
}

void LaAnimalManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaAnimalManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaAnimalManager::refreshAnimalTable(QString theGuid)
{

  mAnimalMap.clear();
  tblAnimals->clear();
  tblAnimals->setRowCount(0);
  tblAnimals->setColumnCount(2);


    //we do this in two passes
    //in the first pass we populate a qmap with all the layersets
    //we find....
  mAnimalMap = LaUtils::getAvailableAnimals();

    //the second pass populates the table
    //doing it from the map ensures that the rows
    //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaAnimal> myIterator(mAnimalMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaAnimal myAnimal = myIterator.value();
   // qDebug()JASONDIDTHIS<< myAnimal.toText();
    if (theGuid.isEmpty())
    {
        //qDebug("No default active row was requested.Assigning to myAnimal.guid()!");;
      theGuid=myAnimal.guid();
    }
    if (myAnimal.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
      // Insert new row ready to fill with details
    tblAnimals->insertRow(myCurrentRow);
    QString myGuid = myAnimal.guid();
    qDebug() << "Inserting animal with guid: " << myGuid;
      // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblAnimals->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myAnimal.name());
    tblAnimals->setItem(myCurrentRow, 1, mypNameItem);
      //display an icon indicating if the layerset is local or remote (e.g. terralib)
      //LaAnimal::Origin myOrigin = myAnimal.origin();
      //if (myOrigin==LaAnimal::USERPROFILE)
      //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
      //}
      //else if (myOrigin==LaAnimal::ADAPTERPROFILE)
      //{
      //QIcon myIcon;
      //myIcon.addFile(":/remotedata.png");
      //mypNameItem->setIcon(myIcon);
      //}
      //else if (myOrigin==LaAnimal::UNDEFINED)
      //{
      //  mypNameItem->setTextColor(Qt::yellow);
      //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblAnimals->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblAnimals->setHorizontalHeaderLabels(headerLabels);
  tblAnimals->setColumnWidth(0,0);
  tblAnimals->setColumnWidth(1,tblAnimals->width());
  tblAnimals->horizontalHeader()->hide();
  tblAnimals->verticalHeader()->hide();
  tblAnimals->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaAnimalManager::cellClicked(int theRow, int theColumn)
{
    //note we use the alg name not the id becuase user may have customised params
 // qDebug()JASONDIDTHIS<< "LaAnimalManager::cellClicked";
  QString myGuid = tblAnimals->item(tblAnimals->currentRow(),0)->text();
 // qDebug()JASONDIDTHIS<< "Guid is: " << myGuid;
  QString myFileName = myGuid + ".xml";
  selectAnimal(myFileName);
}
void LaAnimalManager::selectAnimal(QString theFileName)
{
 // qDebug()JASONDIDTHIS<< "selectAnimal Called : " << theFileName;
  QString myAnimalDir = LaUtils::userAnimalProfilesDirPath();
  LaAnimal myAnimal;
  myAnimal.fromXmlFile(myAnimalDir + QDir::separator() + theFileName);
  mAnimal=myAnimal;
  showAnimal();
}

void LaAnimalManager::showAnimal()
{
  leName->setText(mAnimal.name());
  leDescription->setText(mAnimal.description());
  sbMeatFoodValue->setValue(mAnimal.meatFoodValue());
  sbUsableMeatPercent->setValue(mAnimal.usableMeat());
  sbKillWeight->setValue(mAnimal.killWeight());
  sbAdultWeight->setValue(mAnimal.adultWeight());
  sbConceptionEfficiency->setValue(mAnimal.conceptionEfficiency());
  sbFemalesToMales->setValue(mAnimal.femalesPerMale());
  sbGrowTime->setValue(mAnimal.growTime());
  sbDeathRate->setValue(mAnimal.deathRate());
  cbFeedEnergyType->setCurrentIndex(mAnimal.feedEnergyType());
  sbEnergyForPregnant->setValue(mAnimal.gestating());
  sbEnergyForLactating->setValue(mAnimal.lactating());
  sbEnergyForMaintenance->setValue(mAnimal.maintenance());
  sbEnergyForJuvenilePerKg->setValue(mAnimal.juvenile());
  sbSexualMaturity->setValue(mAnimal.sexualMaturity());
  sbBreedingLife->setValue(mAnimal.breedingExpectancy());
  sbYoungPerBirth->setValue(mAnimal.youngPerBirth());
  sbWeaningAge->setValue(mAnimal.weaningAge());
  sbWeaningWeight->setValue(mAnimal.weaningWeight());
  sbGestationTime->setValue(mAnimal.gestationTime());
  sbEstrousCycleTime->setValue(mAnimal.estrousCycle());
  sbLactationTime->setValue(mAnimal.lactationTime());
  checkBoxMilk->setChecked(mAnimal.milk());
  sbMilk->setValue(mAnimal.milkGramsPerDay());
  sbMilkFoodValue->setValue(mAnimal.milkFoodValue());
  checkBoxFleece->setChecked(mAnimal.fleece());
  sbFleeceWeight->setValue(mAnimal.fleeceWeightKg());
  lblAnimalPix->setPixmap(mAnimal.imageFile());
}

void LaAnimalManager::on_pbnAnimalPic_clicked()
{
  LaUtils myUtils;
  QString myFile = myUtils.openGraphicFile();
  lblAnimalPix->setPixmap(myFile);
  mImageFile = myFile;
}

void LaAnimalManager::on_pushButtonLoad_clicked()
{
    //
  mAnimal.fromXmlFile("/tmp/animal.xml");
  showAnimal();
}

void LaAnimalManager::on_pushButtonSave_clicked()
{
    // not yet implemented
}

void LaAnimalManager::on_toolNew_clicked()
{
  qDebug("New toolbutton clicked");
  LaAnimal myAnimal;
  myAnimal.setGuid();
  mAnimal = myAnimal;
  showAnimal();
}

void LaAnimalManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblAnimals->setColumnWidth(0,0);
  tblAnimals->setColumnWidth(1,tblAnimals->width());
  tblAnimals->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaAnimalManager::on_toolCopy_clicked()
{
  qDebug("Copy toolbutton clicked");
  if (tblAnimals->currentRow() < 0)
  {
    return;
  }
    //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblAnimals->item(tblAnimals->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userAnimalProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaAnimal myAnimal;
  myAnimal.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mAnimal.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myAnimal.name();
  }
  */
    //assign this layerset its own guid
  myAnimal.setGuid();
  QString myNewFileName = LaUtils::userAnimalProfilesDirPath() + QDir::separator() + myAnimal.guid() + ".xml";
  myAnimal.setName(tr("Copy of ") + myAnimal.name());
  myAnimal.toXmlFile(myNewFileName);
  refreshAnimalTable(myAnimal.guid());
}
void LaAnimalManager::on_toolDelete_clicked()
{
  qDebug("Delete toolbutton clicked");
  if (tblAnimals->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblAnimals->item(tblAnimals->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userAnimalProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshAnimalTable();
  }
}
void LaAnimalManager::on_pbnApply_clicked()
{
  mAnimal.setName(leName->text());
  mAnimal.setDescription(leDescription->text());
  mAnimal.setMeatFoodValue(sbMeatFoodValue->value());
  mAnimal.setUsableMeat(sbUsableMeatPercent->value());
  mAnimal.setKillWeight(sbKillWeight->value());
  mAnimal.setAdultWeight(sbAdultWeight->value());
  mAnimal.setConceptionEfficiency(sbConceptionEfficiency->value());
  mAnimal.setFemalesToMales(sbFemalesToMales->value());
  mAnimal.setGrowTime(sbGrowTime->value());
  mAnimal.setDeathRate(sbDeathRate->value());
  
  QString mySelectedFeedEnergyType = QString(cbFeedEnergyType->currentText());
  EnergyType myFeedEnergyType;

  if (mySelectedFeedEnergyType == "KCalories")
  {
    myFeedEnergyType = KCalories;
    mAnimal.setFeedEnergyType(myFeedEnergyType);
  }
  else if (mySelectedFeedEnergyType == "TDN")
  {
    myFeedEnergyType = TDN;
    mAnimal.setFeedEnergyType(myFeedEnergyType);
  }
  
  mAnimal.setGestating(sbEnergyForPregnant->value());
  mAnimal.setLactating(sbEnergyForLactating->value());
  mAnimal.setMaintenance(sbEnergyForMaintenance->value());
  mAnimal.setJuvenile(sbEnergyForJuvenilePerKg->value());
  mAnimal.setSexualMaturity(sbSexualMaturity->value());
  mAnimal.setBreedingExpectancy(sbBreedingLife->value());
  mAnimal.setYoungPerBirth(sbYoungPerBirth->value());
  mAnimal.setWeaningAge(sbWeaningAge->value());
  mAnimal.setWeaningWeight(sbWeaningWeight->value());
  mAnimal.setGestationTime(sbGestationTime->value());
  mAnimal.setEstrousCycle(sbEstrousCycleTime->value());
  mAnimal.setLactationTime(sbLactationTime->value());
  mAnimal.setMilk(checkBoxMilk->checkState());
  mAnimal.setMilkGramsPerDay(sbMilk->value());
  mAnimal.setMilkFoodValue(sbMilkFoodValue->value());
  mAnimal.setFleece(checkBoxFleece->checkState());
  mAnimal.setFleeceWeightKg(sbFleeceWeight->value());
  mAnimal.setImageFile(mImageFile);
  mAnimal.toXmlFile( LaUtils::userAnimalProfilesDirPath() +
      QDir::separator() + mAnimal.guid() + ".xml");
  refreshAnimalTable(mAnimal.guid());
}
