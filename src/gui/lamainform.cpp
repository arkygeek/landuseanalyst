/***************************************************************************
 *   Copyright (C) 2007 by: Tim Sutton        tim@linfiniti.com            *
 *                          Jason Jorgenson   arkygeek@gmail.com           *
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

//app includes
#include "lamainform.h"
#include "version.h"
#include "laanimalmanager.h"
#include "lacropmanager.h"
#include "lacropparametermanager.h"
#include "laanimalparametermanager.h"
#include "lamodel.h"
#include "lamodelreports.h"

//qt includes
#include <QComboBox>
#include <QDir>
#include <QFile>
#include <QHeaderView>
#include <QListWidget>
#include <QProcess>
#include <QSettings>
#include <QStringList>
#include <QTableWidgetItem>
#include <QTextStream>
#include <QTreeWidget>
#include <QTreeWidgetItem>

LaMainForm::LaMainForm(QWidget* parent, Qt::WFlags fl)
  : QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

  lblVersion->setText(QString("Version: %1").arg(VERSION) + " " + QString("$Revision$").replace("$",""));
  tblAnimals->horizontalHeader()->hide();
  tblAnimals->verticalHeader()->hide();
  tblAnimals->horizontalHeader()->setResizeMode(2,QHeaderView::Stretch);
  tblCrops->horizontalHeader()->hide();
  tblCrops->verticalHeader()->hide();
  tblCrops->horizontalHeader()->setResizeMode(2,QHeaderView::Stretch);
  loadAnimals();
  loadCrops();
  setDietLabels();
  /** See the qtdocs on signals and slots to understand below.
   * we connect the currentItemChanged signal that a tree view emits when you
   * click on an item to a little method that sets the help viewer contents
   * appropriately. TS
   *
   * Make sure this is the last stuff we do in the ctor! TS
   */
  connect(treeHelp, SIGNAL(currentItemChanged(QTreeWidgetItem * ,QTreeWidgetItem *)),
      this, SLOT(helpItemClicked(QTreeWidgetItem * ,QTreeWidgetItem *)));
  connect(pushButtonExit, SIGNAL(clicked()), qApp, SLOT(quit()));
  connect(tblAnimals, SIGNAL(cellClicked( int,int)),
      this, SLOT(animalCellClicked( int,int)));
  connect(tblAnimals, SIGNAL(cellChanged( int,int)),
      this, SLOT(animalCellChanged( int,int)));
  connect(tblCrops, SIGNAL(cellClicked( int,int)),
      this, SLOT(cropCellClicked( int,int)));
  connect(tblCrops, SIGNAL(cellChanged( int,int)),
      this, SLOT(cropCellChanged( int,int)));
}

LaMainForm::~LaMainForm()
{
  writeSettings();
}

void LaMainForm::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaMainForm::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaMainForm::on_spinBoxDailyCalories_valueChanged(int theValue)
{
  setDietLabels();
}

void LaMainForm::on_horizontalSliderMeat_valueChanged(int theValue)
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  labelMeatWildPercent->setText(myMinString);
  labelMeatTamePercent->setText(myMaxString);
  setDietLabels();
}

void LaMainForm::on_horizontalSliderDiet_valueChanged(int theValue)
{
  QString myMinString = QString::number(theValue);
  QString myMaxString = QString::number(100-theValue);
  labelMeatPercent->setText(myMinString);
  labelCropPercent->setText(myMaxString);
  setDietLabels();
}

void LaMainForm::on_horizontalSliderCrop_valueChanged(int theValue)
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  labelCropWildPercent->setText(myMinString);
  labelCropTamePercent->setText(myMaxString);
  setDietLabels();
}

/**
  * The stuff above is related to form function, like the
  * sychronization of the sliders and display numbers,
  * clearing of the listWidgets, and so forth.
  */

void LaMainForm::on_pbnNewAnimal_clicked()
{
  LaAnimalManager myAnimalManager;
  myAnimalManager.exec();
  loadAnimals();
}
void LaMainForm::on_pbnNewCrop_clicked()
{
  LaCropManager myCropManager;
  myCropManager.exec();
  loadCrops();
}
void LaMainForm::on_pbnNewCropParameter_clicked()
{
    LaCropParameterManager myCropParameterManager;
    myCropParameterManager.exec();
    loadCrops();
}
void LaMainForm::on_pbnNewAnimalParameter_clicked()
{
    LaAnimalParameterManager myAnimalParameterManager;
    myAnimalParameterManager.exec();
    loadAnimals();
}

void LaMainForm::on_pbnFallow_clicked()
{
    //LaModelReports myModelReports;
    //myModelReports.fallowTable();
}

void LaMainForm::loadAnimals()
{
  listWidgetCalculationsAnimal->clear();
  tblAnimals->clear();
  tblAnimals->setRowCount(0);
  tblAnimals->setColumnCount(4);
  //compute percentages each animal parameter adds to the total and
  //print the total perc. Its up to the user at this stage to ensure
  //that everything tots up to 100%
  int myCurrentRow=0;
  int myRunningPercentage=0;
  QMap<QString,LaAnimal> myAnimalsMap = LaUtils::getAvailableAnimals();
  //debug statement to print all animal keys
  //qDebug((static_cast<QStringList>(myAnimalsMap.keys())).join("\n").toLocal8Bit());
  LaUtils::AnimalParameterMap myAnimalParametersMap;
  myAnimalParametersMap = LaUtils::getAvailableAnimalParameters();
  QMapIterator<QString, LaAnimal> myIterator(myAnimalsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaAnimal myAnimal = myIterator.value();
    QString myGuid = myAnimal.guid();
    QString myName = myAnimal.name();
    QPair<bool,QString> myValue;
    //check if this animal is in mAnimalsMap and if not add it
    //with a blank pair for now
    if (!mAnimalsMap.contains(myGuid))
    {
      myValue.first = false;
      myValue.second = "";
      mAnimalsMap.insert(myGuid,myValue);
      qDebug("Added new blank pair to mAnimals map for keeping track of percentages: " +
          myGuid.toLocal8Bit());
    }
    else
    {
      myValue=mAnimalsMap[myGuid];
    }
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    tblAnimals->insertRow(myCurrentRow);
    // Add details to the new row
    //QTableWidgetItem *mypUsedItem= new QTableWidgetItem(tr("Used?"));
    QTableWidgetItem *mypUsedItem= new QTableWidgetItem(tr(""));
    if (myValue.first)
    {
      mypUsedItem->setCheckState(Qt::Checked);
    }
    else
    {
      mypUsedItem->setCheckState(Qt::Unchecked);
    }
    tblAnimals->setItem(myCurrentRow, 0, mypUsedItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myAnimal.name());
    mypNameItem->setData(Qt::UserRole,myGuid);
    tblAnimals->setItem(myCurrentRow, 1, mypNameItem);
    mypNameItem->setIcon(myIcon);
    //create a var to hold the percentage for each selected parameter
    //add the animal parameters combo to the form
    QComboBox * mypCombo = new QComboBox(this);
    QMapIterator<QString, LaAnimalParameter> myIterator(myAnimalParametersMap);
    while (myIterator.hasNext())
    {
      myIterator.next();
      LaAnimalParameter myAnimalParameter = myIterator.value();
      QString myParameterGuid = myAnimalParameter.guid();
      QString myParameterName = myAnimalParameter.name();
      //only add this entry if it is for the current animal
      if (myGuid != myAnimalParameter.animalGuid())
      {
        continue;
      }
      //if the animal paraameter id has not yet been set in mAnimalsMap
      //set it now...
      if (myValue.second.isEmpty())
      {
        myValue.second = myParameterGuid;
      }
      //see if this animal parameter percentage can be added to our running tot
      qDebug("Comparing " + myValue.second.toLocal8Bit() + " <-> " +
          myAnimalParameter.guid().toLocal8Bit());
      if (myValue.second == myAnimalParameter.guid())
      {
        if (myValue.first)
          {
            myRunningPercentage += myAnimalParameter.percentTameMeat();
            QListWidgetItem *item = new QListWidgetItem(myAnimal.name());
            item->setData(Qt::UserRole,myAnimal.guid());
            listWidgetCalculationsAnimal->addItem(item);
          }
        QTableWidgetItem *mypPercentItem =
          new QTableWidgetItem(QString::number(myAnimalParameter.percentTameMeat()));
        qDebug("Percentage this animal contributes to diet: " +
            QString::number(myAnimalParameter.percentTameMeat()).toLocal8Bit());
        tblAnimals->setItem(myCurrentRow, 3, mypPercentItem);
      }
      //                icon, disp name, userdata
      mypCombo->addItem(myIcon,myParameterName,myParameterGuid);
    }
    setComboToDefault(mypCombo, myValue.second);
    mAnimalsMap[myGuid]=myValue;
    tblAnimals->setCellWidget ( myCurrentRow, 2, mypCombo);
    myCurrentRow++;
  }
  //finally show the total percentage all the selected animals contribute to the diet
  QIcon myIcon;
  if (myRunningPercentage==100)
  {
    myIcon.addFile(":/status_ok.png");
  }
  else
  {
    myIcon.addFile(":/status_error.png");
  }
  QString myPercentItem = QString::number(myRunningPercentage);
  labelAnimalCheck->setText(myPercentItem + "\%");
  //QLabel::setPixmap(labelAnimalCheck->(myIcon));
  //tblAnimals->insertRow(myCurrentRow);
  //QTableWidgetItem *mypLabelItem = new QTableWidgetItem(QString(tr("Total Diet %")));
  //tblAnimals->setItem(myCurrentRow, 1, mypLabelItem);
  //QTableWidgetItem *mypPercentItem =
  //        new QTableWidgetItem(QString::number(myRunningPercentage));
  //mypPercentItem->setIcon(myIcon);
  //tblAnimals->setItem(myCurrentRow, 3, mypPercentItem);
}

void LaMainForm::loadCrops()
{
  listWidgetCalculationsCrop->clear();
  tblCrops->clear();
  tblCrops->setRowCount(0);
  tblCrops->setColumnCount(4);
  //compute percentages each crop parameter adds to the total and
  //print the total perc. Its up to the user at this stage to ensure
  //that everything tots up to 100%
  int myCurrentRow=0;
  int myRunningPercentage=0;
  QMap<QString,LaCrop> myCropsMap;
  myCropsMap = LaUtils::getAvailableCrops();
  //debug statemetn to print all crop keys
  //qDebug((static_cast<QStringList>(myCropsMap.keys())).join("\n").toLocal8Bit());
  LaUtils::CropParameterMap myCropParametersMap;
  myCropParametersMap = LaUtils::getAvailableCropParameters();
  QMapIterator<QString, LaCrop> myIterator(myCropsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCrop myCrop = myIterator.value();
    QString myGuid = myCrop.guid();
    QString myName = myCrop.name();
    QPair<bool,QString> myValue;
    //check if this crop is in mCropsMap and if not add it
    //with a blank pair for now
    if (!mCropsMap.contains(myGuid))
    {
      myValue.first = false;
      myValue.second = "";
      mCropsMap.insert(myGuid,myValue);
      qDebug("Added new blank pair to mCrops map for keeping track of percentages: " +
          myGuid.toLocal8Bit());
    }
    else
    {
      myValue=mCropsMap[myGuid];
    }

    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    tblCrops->insertRow(myCurrentRow);
    // Add details to the new row
    QTableWidgetItem *mypUsedItem= new QTableWidgetItem(tr("Used?"));

    (myValue.first) ? mypUsedItem->setCheckState(Qt::Checked) : mypUsedItem->setCheckState(Qt::Unchecked);

    tblCrops->setItem(myCurrentRow, 0, mypUsedItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myCrop.name());
    mypNameItem->setData(Qt::UserRole,myGuid);
    tblCrops->setItem(myCurrentRow, 1, mypNameItem);
    mypNameItem->setIcon(myIcon);
    //create a var to hold the percentage for each selected parameter
    //add the crop parameters combo to the form
    QComboBox * mypCombo = new QComboBox(this);
    QMapIterator<QString, LaCropParameter> myIterator(myCropParametersMap);
    while (myIterator.hasNext())
    {
      myIterator.next();
      LaCropParameter myCropParameter = myIterator.value();
      QString myParameterGuid = myCropParameter.guid();
      QString myParameterName = myCropParameter.name();
      //only add this entry if it is for the current crop
      if (myGuid != myCropParameter.cropGuid())
      {
        continue;
      }
      //if the crop paraameter id has not yet been set in mCropsMap
      //set it now...
      if (myValue.second.isEmpty())
      {
        myValue.second = myParameterGuid;
      }
      //see if this crop parameter percentage can be added to our running tot
      qDebug("Comparing " + myValue.second.toLocal8Bit() + " <-> " +
          myCropParameter.guid().toLocal8Bit());
      if (myValue.second == myCropParameter.guid())
      {
        if (myValue.first)
          {
            myRunningPercentage += myCropParameter.percentTameCrop();
            QListWidgetItem *item = new QListWidgetItem(myCrop.name());
            item->setData(Qt::UserRole,myCrop.guid());
            listWidgetCalculationsCrop->addItem(item);
            //QListWidgetItem *itemWidget->setData( Qt::UserRole + 0, myCrop.guid());
            //QListWidgetItem *itemWidget->setData( Qt::DisplayRole, myCrop.name());
            //listWidgetCalculationsCrop->addItem(itemWidget);
          }
        QTableWidgetItem *mypPercentItem =
          new QTableWidgetItem(QString::number(myCropParameter.percentTameCrop()));
        qDebug("Percentage this crop contributes to diet: " +
            QString::number(myCropParameter.percentTameCrop()).toLocal8Bit());
        tblCrops->setItem(myCurrentRow, 3, mypPercentItem);
      }
      //                icon, disp name, userdata
      mypCombo->addItem(myIcon,myParameterName,myParameterGuid);
    }
    setComboToDefault(mypCombo, myValue.second);
    mCropsMap[myGuid]=myValue;
    tblCrops->setCellWidget ( myCurrentRow, 2, mypCombo);
    myCurrentRow++;
  }
  //finally show the total percentage all the selected crops contribute to the diet
  QIcon myIcon;
  (myRunningPercentage==100) ? myIcon.addFile(":/status_ok.png") : myIcon.addFile(":/status_error.png");

  QString myPercentItem = QString::number(myRunningPercentage);
  labelCropCheck->setText(myPercentItem + "\%");

  //tblCrops->insertRow(myCurrentRow);
  //QTableWidgetItem *mypLabelItem = new QTableWidgetItem(QString(tr("Total Diet %")));
  //tblCrops->setItem(myCurrentRow, 1, mypLabelItem);
  //QTableWidgetItem *mypPercentItem =
  //        new QTableWidgetItem(QString::number(myRunningPercentage));
  //mypPercentItem->setIcon(myIcon);
  //tblCrops->setItem(myCurrentRow, 3, mypPercentItem);
}

void LaMainForm::setDietLabels()
{
  int myDietPercentMeat = horizontalSliderDiet->value();
  int myDietPercentPlant = (100-(horizontalSliderDiet->value()));
  float myTameCropPercentage = horizontalSliderCrop->value()*(myDietPercentPlant/100.);
  float myTameMeatPercentage = horizontalSliderMeat->value()*(myDietPercentMeat/100.);
  int myCaloriesIndividual = spinBoxDailyCalories->value();
  int myPopulation = spinBoxPopulation->value();

  float mykCaloriesIndividualAnnual = (myCaloriesIndividual*365.)/1000.;
  float mykCaloriesSettlementAnnual = mykCaloriesIndividualAnnual*myPopulation;

  float myTameCropkCalories = (myTameCropPercentage/100.)*mykCaloriesSettlementAnnual;
  float myTameAnimalkCalories = (myTameMeatPercentage/100.)*mykCaloriesSettlementAnnual;

  labelCaloriesIndividual->setText(QString::number(mykCaloriesIndividualAnnual));
  labelCaloriesSettlement->setText(QString::number(mykCaloriesSettlementAnnual));
  labelPortionPlants->setText(QString::number(myDietPercentPlant));
  labelPortionMeat->setText(QString::number(myDietPercentMeat));
  labelPortionCrops->setText(QString::number(myTameCropPercentage));
  labelPortionTameMeat->setText(QString::number(myTameMeatPercentage));
  labelCaloriesCrops->setText(QString::number(myTameCropkCalories));
  labelCaloriesTameMeat->setText(QString::number(myTameAnimalkCalories));
}

void LaMainForm::animalCellClicked(int theRow, int theColumn)
{
  qDebug("LaMainForm::animalCellClicked");
  QTableWidgetItem* mypItem = tblAnimals->item(tblAnimals->currentRow(),1);
  if (mypItem)
  {
    QString myGuid = mypItem->data(Qt::UserRole).toString();
    //QString myGuid = tblAnimals->item(tblAnimals->currentRow(),1)->data(Qt::UserRole).toString();
    //get all animals, then get the animal for this cell if it exists
    QMap<QString,LaAnimal> myAnimalsMap = LaUtils::getAvailableAnimals();
    LaAnimal myAnimal = myAnimalsMap[myGuid];
    textBrowserAnimalDefinition->setHtml(myAnimal.toHtml());
    QComboBox * mypCombo=dynamic_cast<QComboBox *>(tblAnimals->cellWidget(tblAnimals->currentRow(),2));
    myGuid = mypCombo->itemData(mypCombo->currentIndex(),Qt::UserRole).toString();
    //get all animal parameters, then get the animal parameter for this cell if it exists
    LaUtils::AnimalParameterMap myAnimalParametersMap;
    myAnimalParametersMap = LaUtils::getAvailableAnimalParameters();
    LaAnimalParameter myAnimalParameter = myAnimalParametersMap[myGuid];
    textBrowserAnimalParameterDefinition->setHtml(myAnimalParameter.toHtml());
  }
  loadAnimals();
}

void LaMainForm::animalCellChanged(int theRow, int theColumn)
{
  QTableWidgetItem* mypItem = tblAnimals->item(tblAnimals->currentRow(),1);
  if (mypItem)
  {
    QString myGuid = mypItem->data(Qt::UserRole).toString();
    // QString myGuid = tblAnimals->item(tblAnimals->currentRow(),1)->data(Qt::UserRole).toString();
    bool myStateFlag = tblAnimals->item(tblAnimals->currentRow(),0)->checkState();
    QPair<bool,QString> myPair = mAnimalsMap[myGuid];
    myPair.first = myStateFlag;
    QComboBox * mypCombo=dynamic_cast<QComboBox *>(tblAnimals->cellWidget(tblAnimals->currentRow(),2));
    myPair.second = mypCombo->itemData(mypCombo->currentIndex(),Qt::UserRole).toString();
    mAnimalsMap[myGuid] = myPair;
    //debug only - comment out later
    printCropsAndAnimals();
  }
}

void LaMainForm::cropCellClicked(int theRow, int theColumn)
{
  qDebug("LaMainForm::cropCellClicked");
    QTableWidgetItem* mypItem = tblCrops->item(tblCrops->currentRow(),1);
  if (mypItem)
  {
    QString myGuid = mypItem->data(Qt::UserRole).toString();
    //QString myGuid = tblCrops->item(tblCrops->currentRow(),1)->data(Qt::UserRole).toString();
    //get all crops, then get the crop for this cell if it exists
    QMap<QString,LaCrop> myCropsMap = LaUtils::getAvailableCrops();
    LaCrop myCrop = myCropsMap[myGuid];
    textBrowserCropDefinition->setHtml(myCrop.toHtml());
    QComboBox * mypCombo=dynamic_cast<QComboBox *>(tblCrops->cellWidget(tblCrops->currentRow(),2));
    myGuid = mypCombo->itemData(mypCombo->currentIndex(),Qt::UserRole).toString();
    //get all crops parameters, then get the crop parameter for this cell if it exists
    LaUtils::CropParameterMap myCropParametersMap;
    myCropParametersMap = LaUtils::getAvailableCropParameters();
    LaCropParameter myCropParameter = myCropParametersMap[myGuid];
    textBrowserCropParameterDefinition->setHtml(myCropParameter.toHtml());
  }
  loadCrops();
}

void LaMainForm::cropCellChanged(int theRow, int theColumn)
{
  QTableWidgetItem* mypItem = tblCrops->item(tblCrops->currentRow(),1);
  if (mypItem)
  {
    QString myGuid = mypItem->data(Qt::UserRole).toString();
    //QString myGuid = tblCrops->item(tblCrops->currentRow(),1)->data(Qt::UserRole).toString();
    bool myStateFlag = tblCrops->item(tblCrops->currentRow(),0)->checkState();
    QPair<bool,QString> myPair = mCropsMap[myGuid];
    myPair.first = myStateFlag;
    QComboBox * mypCombo=dynamic_cast<QComboBox *>(tblCrops->cellWidget(tblCrops->currentRow(),2));
    myPair.second = mypCombo->itemData(mypCombo->currentIndex(),Qt::UserRole).toString();
    mCropsMap[myGuid] = myPair;
    //debug only - comment out later
    printCropsAndAnimals();
  }
}

void LaMainForm::on_pushButtonRun_clicked()
{
  if (labelCropCheck->text() != "100\%" or labelAnimalCheck->text() != "100\%")
    {
      textBrowserResultsRight->setText("Check that Animals and Crops are both at 100%\n");
      textBrowserResultsRight->append("I am NOT going to do anything until you do!");
      return;
    }

  mCommonGrazingLandFoodValue = sbCommonRasterCalories->value();
  LaModel myModel;
  connect(&myModel, SIGNAL(message( QString )), 
             this, SLOT(logMessage( QString )));
  // Get a list of the selected animals
  QMap<QString,QString> mySelectedAnimalsMap;
  //          <animal guid <enabled, animalparamters guid>>
  QMapIterator<QString, QPair<bool, QString> > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QPair<bool,QString> myPair = myAnimalIterator.value();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myPair.second;
    bool mySelectedFlag = myPair.first;
    if (mySelectedFlag)
    {
      mySelectedAnimalsMap.insert(myAnimalGuid,myAnimalParameterGuid);
      qDebug("Added <" + myAnimalGuid.toLocal8Bit() + " , " + myAnimalParameterGuid.toLocal8Bit() + " >");
    }
  }
  myModel.setAnimals(mySelectedAnimalsMap);

  // Get a list of the selected crops
  QMap<QString,QString> mySelectedCropsMap;
  //          <crop guid <enabled, cropparamters guid>>
  QMapIterator<QString, QPair<bool, QString> > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QPair<bool,QString> myPair = myCropIterator.value();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = myPair.second;
    bool mySelectedFlag = myPair.first;
    if (mySelectedFlag)
    {
      mySelectedCropsMap.insert(myCropGuid,myCropParameterGuid);
      qDebug("Added <" + myCropGuid.toLocal8Bit() + " , " + myCropParameterGuid.toLocal8Bit() + " >");
    }
  }
  myModel.setCrops(mySelectedCropsMap);

  // Populate the model with all the form data
  myModel.setName(lineEditSiteName->text());
  myModel.setPopulation(spinBoxPopulation->value());
  myModel.setPeriod(lineEditPeriod->text());
  myModel.setProjection(comboBoxProjection->currentIndex());
  myModel.setEasting(lineEditEasting->text().toInt());
  myModel.setNorthing(lineEditNorthing->text().toInt());
  myModel.setEuclideanDistance(radioButtonEuclidean->isChecked());
  myModel.setWalkingTime(radioButtonWalkingTime->isChecked());
  myModel.setPathDistance(radioButtonPathDistance->isChecked());
  myModel.setPrecision(spinBoxModelPrecision->value());
  myModel.setDietPercent(horizontalSliderDiet->value());
  myModel.setCropPercent(horizontalSliderCrop->value());
  myModel.setMeatPercent(horizontalSliderMeat->value());
  myModel.setCaloriesPerPersonDaily(spinBoxDailyCalories->value());
  myModel.setCommonLandValue(sbCommonRasterCalories->value());
  textBrowserResultsLeft->setText(myModel.toHtml());

  // for debugging only...
  qDebug("LAMAINFORM!!!!");
  qDebug("Number of Crops: " + QString::number(myModel.countCrops()).toLocal8Bit());
  qDebug("Number of Animals: " + QString::number(myModel.countAnimals()).toLocal8Bit());
  qDebug("Calories from Crops: " + QString::number(myModel.caloriesFromCrops()).toLocal8Bit());
  qDebug("Calories from Animals: " + QString::number(myModel.caloriesFromTameMeat()).toLocal8Bit());
  qDebug("end LAMAINFORM!!!!");
  // iterate through crops and animals and display the calorie, production and area targets
  myModel.DoCalculations();
  myModel.toXmlFile( LaUtils::getModelOutputDir() +
      QDir::separator() + myModel.guid() + ".xml");

  //textBrowserResultsRight->append("Crop Calorie Targets");
  textBrowserResultsRight->append(myModel.toHtmlCalorieCropTargets());
  //textBrowserResultsRight->append("Animal Calorie Targets");
  textBrowserResultsRight->append(myModel.toHtmlCalorieAnimalTargets());

  //textBrowserResultsRight->append("Crop Production Targets");
  textBrowserResultsRight->append(myModel.toHtmlProductionCropTargets());
  //textBrowserResultsRight->append("Animal Production Targets");
  textBrowserResultsRight->append(myModel.toHtmlProductionAnimalTargets());

  //textBrowserResultsRight->append("Crop Area Targets");
  textBrowserResultsRight->append(myModel.toHtmlAreaCropTargets());
  //textBrowserResultsRight->append("Animal Area Targets");
  textBrowserResultsRight->append(myModel.toHtmlAreaAnimalTargets());
}


void LaMainForm::debugChecks()
{
  // iterate through crops and display the calorie, production and area targets

  // iterate through animals and display the calorie, production and area targets
}

void LaMainForm::on_pushButtonLoad_clicked()
{
  //  implement me!
  //  seriously... please implement me!
}

void LaMainForm::on_pushButtonSave_clicked()
{
  //  implement me!
  //  go on... get on with it!
}

void LaMainForm::writeResultsLeft(QString theText)
{
  textBrowserResultsLeft->append(theText);
}

void LaMainForm::writeResultsRight(QString theText)
{
  textBrowserResultsRight->append(theText);
}



bool LaMainForm::setComboToDefault(QComboBox * thepCombo, QString theDefault)
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

void LaMainForm::helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem)
{
  writeResultsLeft("Item clicked in help browser: " + thepCurrentItem->text(0).toLocal8Bit());
  QFile myQFile( ":/helpDocs/" + thepCurrentItem->text(0)  + ".html" );
  if ( myQFile.open( QIODevice::ReadOnly ) ) {
    //now we parse the loc file, checking each line for its taxon
    QTextStream myStream( &myQFile );
    textHelp->setHtml(myStream.readAll());
    myQFile.close();
  }
  else
  {
    writeResultsLeft("Help resource for : " + thepCurrentItem->text(0).toLocal8Bit() + " not found!");
  }
}


void LaMainForm::printCropsAndAnimals()
{
  textBrowserResultsLeft->clear();
  textBrowserResultsRight->clear();
  QMapIterator<QString, QPair<bool, QString> > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QPair<bool,QString> myPair = myAnimalIterator.value();
    QString myAnimalGuid = myAnimalIterator.key();
    bool mySelectedFlag = myPair.first;
    QString myAnimalParameterGuid = myPair.second;
    QString myText = "Animal <" + myAnimalGuid.toLocal8Bit() +
      " , <";
    mySelectedFlag ? myText += "true," : myText += "false,";
    myText +=  myAnimalParameterGuid.toLocal8Bit() ;
    myText += "> >";
    tbLogs->append(myText);
  }

  QMapIterator<QString, QPair<bool, QString> > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QPair<bool,QString> myPair = myCropIterator.value();
    QString myCropGuid = myCropIterator.key();
    bool mySelectedFlag = myPair.first;
    QString myCropParameterGuid = myPair.second;
    QString myText = "Crop <" + myCropGuid.toLocal8Bit() +
      " , <";
    mySelectedFlag ? myText += "true," : myText += "false,";
    myText +=  myCropParameterGuid.toLocal8Bit() ;
    myText += "> >";
    tbLogs->append(myText);
  }
}

void LaMainForm::logMessage(QString theMessage)
{
  tbLogs->append(theMessage);
  tbLogs->ensureCursorVisible();
}
