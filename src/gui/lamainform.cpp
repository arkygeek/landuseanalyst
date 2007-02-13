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
#include "lamainform.h"
#include "version.h"
#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>


LaMainForm::LaMainForm(QWidget* parent, Qt::WFlags fl)
  : QDialog(parent,fl) 
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  /** See the qtdocs on signals and slots to understand below.
   * we connect the currentItemChanged signal that a tree view emits when you 
   * click on an item to a little method that sets the help viewer contents
   * appropriately. TS
   */
  connect(treeHelp, SIGNAL(currentItemChanged(QTreeWidgetItem * ,QTreeWidgetItem *)), 
      this, SLOT(helpItemClicked(QTreeWidgetItem * ,QTreeWidgetItem *)));
  // makeCircle(0,0);
  lblVersion->setText(QString("Version: %1").arg(VERSION) + " " + QString("$Revision$").replace("$",""));
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

void LaMainForm::on_buttonWheatView_clicked()
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myWheatPercentage = wheatPercent->value();     // PERCENTAGE OF WHEAT in plant portion of diet
  int myWheatYield = wheatYield->value();      // expected average WHEAT YIELD
  int myWheatCalories = wheatCalories->value();      // FALLOW RATIO for WHEAT
  float myWheatFallowRatio = wheatFallowRatio->value();  // 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  // calculate area required for wheat
  float myWheatArea;  // wheat area 
  float myWheatFallowArea;  // wheat fallow area
  float myWheatTotalArea;  // wheat total area
  myWheatArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myWheatPercentage/100.))*myCalories*365.)/myWheatCalories)*myPopulation)/myWheatYield)*1000.);
  myWheatFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myWheatPercentage/100.))*myCalories*365.)/myWheatCalories)*myPopulation)/myWheatYield)*1000.)*(myWheatFallowRatio);
  myWheatTotalArea = myWheatArea + myWheatFallowArea;
  writeMessage("Wheat area: " + QString::number(myWheatArea).toLocal8Bit());
  writeMessage("Wheat fallow area: " + QString::number(myWheatFallowArea).toLocal8Bit());
  writeMessage("Wheat total area: " + QString::number(myWheatTotalArea).toLocal8Bit());
}

void LaMainForm::on_buttonBarleyView_clicked() 
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myBarleyPercent = barleyPercent->value();     // PERCENTAGE OF BARLEY in plant portion of diet
  int myBarleyYield = barleyYield->value();      // expected average BARLEY YIELD
  int myBarleyCalories = barleyCalories->value();      // FALLOW RATIO for BARLEY
  float myBarleyFallowRatio = barleyFallowRatio->value();  // 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  // calculate area required for barley
  float myBarleyArea;  // barley area 
  float myBarleyFallowArea;  // barley fallow area
  float myBarleyTotalArea;  // barley total area
  myBarleyArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myBarleyPercent/100.))*myCalories*365.)/myBarleyCalories)*myPopulation)/myBarleyYield)*1000.);
  myBarleyFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myBarleyPercent/100.))*myCalories*365.)/myBarleyCalories)*myPopulation)/myBarleyYield)*1000.)*(myBarleyFallowRatio);
  myBarleyTotalArea = myBarleyArea + myBarleyFallowArea;
  writeMessage("Barley area: " + QString::number(myBarleyArea).toLocal8Bit());
  writeMessage("Barley fallow area: " + QString::number(myBarleyFallowArea).toLocal8Bit());
  writeMessage("Barley total area: " + QString::number(myBarleyTotalArea).toLocal8Bit());
}

void LaMainForm::on_buttonLentilView_clicked() 
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myLentilPercent = lentilPercent->value();     // PERCENTAGE OF LENTIL in plant portion of diet
  int myLentilYield = lentilYield->value();      // expected average LENTIL YIELD
  int myLentilCalories = lentilCalories->value();      // FALLOW RATIO for LENTIL
  float myLentilFallowRatio = lentilFallowRatio->value();  // 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  // calculate area required for LENTIL
  float myLentilArea;  // wheat area 
  float myLentilFallowArea;  // wheat fallow area
  float myLentilTotalArea;  // wheat total area
  myLentilArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myLentilPercent/100.))*myCalories*365.)/myLentilCalories)*myPopulation)/myLentilYield)*1000.);
  myLentilFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myLentilPercent/100.))*myCalories*365.)/myLentilCalories)*myPopulation)/myLentilYield)*1000.)*(myLentilFallowRatio);
  myLentilTotalArea = myLentilArea + myLentilFallowArea;
  writeMessage("Lentil area: " + QString::number(myLentilArea).toLocal8Bit());
  writeMessage("Lentil fallow area: " + QString::number(myLentilFallowArea).toLocal8Bit());
  writeMessage("Lentil total area: " + QString::number(myLentilTotalArea).toLocal8Bit());
}

void LaMainForm::on_buttonOliveView_clicked() 
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myOlivePercent = olivePercent->value();     // PERCENTAGE OF OLIVE in plant portion of diet
  int myOliveYield = oliveYield->value();      // expected average OLIVE YIELD
  int myOliveCalories = oliveCalories->value();      // FALLOW RATIO for OLIVE
  float  myOliveFallowRatio = oliveFallowRatio->value();  // 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  // calculate area required for OLIVE
  float myOliveArea;  // olive area 
  float myOliveFallowArea;  // olive fallow area
  float myOliveTotalArea;  // olive total area
  myOliveArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myOlivePercent/100.))*myCalories*365.)/myOliveCalories)*myPopulation)/myOliveYield)*1000.);
  myOliveFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myOlivePercent/100.))*myCalories*365.)/myOliveCalories)*myPopulation)/myOliveYield)*1000.)*(myOliveFallowRatio);
  myOliveTotalArea = myOliveArea + myOliveFallowArea;
  writeMessage("olive area: " + QString::number(myOliveArea).toLocal8Bit());
  writeMessage("olive fallow area: " + QString::number(myOliveFallowArea).toLocal8Bit());
  writeMessage("olive total area: " + QString::number(myOliveTotalArea).toLocal8Bit());
}

void LaMainForm::on_buttonGrapeView_clicked() 
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myGrapePercent = grapePercent->value();     // PERCENTAGE OF GRAPE in plant portion of diet
  int myGrapeYield = grapeYield->value();      // expected average GRAPE YIELD
  int myGrapeCalories = grapeCalories->value();      // FALLOW RATIO for GRAPE
  float myGrapeFallowRatio = grapeFallowRatio->value();  // 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  // calculate area required for grape
  float myGrapeArea;  // grape area 
  float myGrapeFallowArea;  // grape fallow area
  float myGrapeTotalArea;  // grape total area
  myGrapeArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myGrapePercent/100.))*myCalories*365.)/myGrapeCalories)*myPopulation)/myGrapeYield)*1000.);
  myGrapeFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myGrapePercent/100.))*myCalories*365.)/myGrapeCalories)*myPopulation)/myGrapeYield)*1000.)*(myGrapeFallowRatio);
  myGrapeTotalArea = myGrapeArea + myGrapeFallowArea;
  writeMessage("grape area: " + QString::number(myGrapeArea).toLocal8Bit());
  writeMessage("grape fallow area: " + QString::number(myGrapeFallowArea).toLocal8Bit());
  writeMessage("grape total area: " + QString::number(myGrapeTotalArea).toLocal8Bit());
}

void LaMainForm::on_buttonPigView_clicked() 
{
  int myMeatDietPercent = dietSlider->value(); 
  int myMeatTamePercent = meatSlider->value(); 
  int myPigPercent = pigPercent->value(); 
  int myPigLitterSize = pigLitterSize->value(); 
  int myPigKillWeight = pigWeight->value(); 
  int myPigGrowTime = pigGrowTime->value(); 
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();
  bool myPigUseFodder = pigFodderUse->isChecked(); 
  float myPigProdnTgt = 
    (
      (
        (
          (
            (myMeatDietPercent/100.)*
            (myMeatTamePercent/100.)*
            (myPigPercent/100.)
          )
          *myCalories
          *myPopulation
        )
        /3000.
      )
      *365.*2.
    ); 
  float myPigButcherNumbersRqd = (myPigProdnTgt/100.);
  float mySows = ((10.*myPigProdnTgt)/(1760.53*myPigLitterSize));
  float myDrySows = ((mySows*30.80)/249.70);
  float myGestSows = ((mySows*41.6)/249.70);
  float myLactatingSows = ((mySows*177.20)/249.70);
  float mySucklingPigs = (((355.10/41.60)/10.)*myPigLitterSize*myLactatingSows);
  float myNursingPigs = ((((mySows*420.10)/249.70)/10.)*myPigLitterSize);
  float myGrowingPigs = ((((mySows*1414.70)/249.70)/10.)*myPigLitterSize);
  float total = (mySows+mySucklingPigs+myNursingPigs+myGrowingPigs);
  writeMessage("fodder flag value: " + QString::number(myPigUseFodder).toLocal8Bit());
  writeMessage("You supplied me with this information:");
  writeMessage("Population of Settlement: " + QString::number(myPopulation).toLocal8Bit());
  writeMessage("Calories/person per day: " + QString::number(myCalories).toLocal8Bit());
  writeMessage("Percentage of Calories in the diet from MEAT: " + QString::number(myMeatDietPercent).toLocal8Bit());
  writeMessage("Percentage of MEAT that is from domesticated animals: " + QString::number(myMeatTamePercent).toLocal8Bit());
  writeMessage("Percentage of DOMESTICATED MEAT that is from PIGS: " + QString::number(myPigPercent).toLocal8Bit());
  writeMessage("Calories per kg in PIG MEAT: 3000 assumed");
  writeMessage("Average Litter Size: " + QString::number(myPigLitterSize).toLocal8Bit());
  writeMessage("kg of meat per year: " + QString::number(myPigProdnTgt/2.).toLocal8Bit());
  writeMessage("Number of 100kg pigs: " + QString::number(myPigButcherNumbersRqd).toLocal8Bit());
  writeMessage("mySows required to produce this much meat: " + QString::number(mySows).toLocal8Bit());
  writeMessage("Non-Pregnant sows and gilts: " + QString::number(myDrySows).toLocal8Bit());
  writeMessage("Gestating sows: " + QString::number(myGestSows).toLocal8Bit());
  writeMessage("Lactating sows: " + QString::number(myLactatingSows).toLocal8Bit());
  writeMessage("Total Adult Females: " + QString::number(mySows).toLocal8Bit());
  writeMessage("Suckling Pigs: " + QString::number(mySucklingPigs).toLocal8Bit());
  writeMessage("Nursery Pigs: " + QString::number(myNursingPigs).toLocal8Bit());
  writeMessage("Growing and finishing pigs: " + QString::number(myGrowingPigs).toLocal8Bit());
  writeMessage("Total pigs: " + QString::number(total).toLocal8Bit());
}


void LaMainForm::on_meatSlider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  meatWildPercent->setText(myMinString);
  meatTamePercent->setText(myMaxString);
}

void LaMainForm::on_dietSlider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(theValue);
  QString myMaxString = QString::number(100-theValue);
  meatPercent->setText(myMinString);
  plantPercent->setText(myMaxString);
}

void LaMainForm::on_plantSlider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  plantWildPercent->setText(myMinString);
  plantTamePercent->setText(myMaxString);
}

void LaMainForm::helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem) 
{
  writeMessage("Item clicked in help browser: " + thepCurrentItem->text(0).toLocal8Bit());
  QFile myQFile( ":/" + thepCurrentItem->text(0)  + ".html" );
  if ( myQFile.open( QIODevice::ReadOnly ) ) {
    //now we parse the loc file, checking each line for its taxon
    QTextStream myStream( &myQFile );
    textHelp->setHtml(myStream.readAll());
    myQFile.close();
  }
  else {
    writeMessage("Help resource for : " + thepCurrentItem->text(0).toLocal8Bit() + " not found!");
  }
}

void LaMainForm::on_buttonDietBreakdown_clicked() 
{
  int myOverallPercentage = (100-(dietSlider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantSlider->value();       // TAME PLANT percentage
  int myDietPercentMeat = dietSlider->value();
  int myDietPercentTameMeat = meatSlider->value();
  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  float myTotalCalories = myPopulation*myCalories*365.;
  float myPlantCalories = (myOverallPercentage/100.)*myTotalCalories;
  float myTamePlantCalories = ((myOverallPercentage/100.)*(myTamePlantPercentage/100.))*myTotalCalories;
  float myAnimalCalories = (myDietPercentMeat/100.)*myTotalCalories;
  float myTameAnimalCalories = ((myDietPercentMeat/100.)*(myDietPercentTameMeat/100.))*myTotalCalories;

  writeDiet("Calories per person per year: " + QString::number((myCalories*365.)/1000.).toLocal8Bit() + "kcal");
  writeDiet("Calories required for population are: " + QString::number(myTotalCalories/1000.).toLocal8Bit() + "kcal");
  writeDiet(" ");
  writeDiet("Plants contribute " + QString::number(myOverallPercentage).toLocal8Bit() + "% to diet, or " + QString::number(myPlantCalories/1000.).toLocal8Bit() + " kcal");
  writeDiet("Meat contributes " + QString::number(myDietPercentMeat).toLocal8Bit() + "% to diet, or  " + QString::number(myAnimalCalories/1000.).toLocal8Bit() + " kcal");
  writeDiet(" ");
  writeDiet("Tame Plants account for " + QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(myPlantCalories/1000.).toLocal8Bit() + " kcal");
  writeDiet("Tame Animals account for " + QString::number((myDietPercentMeat/100.)*(myDietPercentTameMeat/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(myAnimalCalories/1000.).toLocal8Bit() + " kcal");
}

void LaMainForm::writeMessage(QString theText) 
{
  textBrowserResults->append(theText);
}

void LaMainForm::writeDiet(QString theText) 
{
  breakdownDisplay->append(theText);
}

void LaMainForm::writeResultsCellValue(int theRow, int theCol, QString theValue) 
{
  QTableWidgetItem *mypItem = new QTableWidgetItem(theValue);
  tableResults->setItem(theRow, theCol, mypItem);
}

void LaMainForm::getArea(float theArea) 
{
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "tempraster";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);

  if (!myProcess.waitForStarted()) 
  {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1))
  {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

void LaMainForm::makeWalkCost(int theX, int theY) 
{
}

void LaMainForm::makeEuclideanCost(int theX, int theY) 
{
}

void LaMainForm::makePathDistanceCost(int theX, int theY) 
{
}

void LaMainForm::writeMetaData(QString theValue) 
{
}

void LaMainForm::makeCircle(int theX, int theY) 
{
  // to verify this worked do
  //    d.rast
  //    and check in the pull downlist (if your eyes dont fall out looking at those fonts)
  //    to remove teh file again do:
  //    g.remove rast=circle

  /*
     qDebug("Making crop circle...tweeedee treedee");
     QString myProgram = "/usr/lib/grass/bin/r.circle";
     QStringList myArgs;
     myArgs << "-b" 
     << "output=circle" 
     <<  "coordinate=744800,3611100" 
     << "max=500" 
     << "--overwrite";
     */
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "landuse";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);
  if (!myProcess.waitForStarted()) {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1)) {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

void LaMainForm::doBaseCalculations()
{

}

void LaMainForm::on_buttonRun_clicked() 
{
  // OVERALL PLANT PERCENTAGE
  int myOverallPercentage = (100-(dietSlider->value()));
  // TAME PLANT percentage
  int myTamePlantPercentage = plantSlider->value();

  int myCalories = dailyCalories->value();
  int myPopulation = population->value();

  int myWheatPercent = wheatPercent->value();
  int myBarleyPercent = barleyPercent->value();
  int myLentilPercent = lentilPercent->value(); 
  int myOlivePercent = olivePercent->value();
  int myGrapePercent = grapePercent->value();

  if (!wheat->isChecked()) myWheatPercent = 0;
  if (!barley->isChecked()) myBarleyPercent = 0;
  if (!lentils->isChecked()) myLentilPercent = 0;
  if (!olives->isChecked()) myOlivePercent = 0;
  if (!grapes->isChecked()) myGrapePercent = 0;

  int myCropCheck = myBarleyPercent+myWheatPercent+myLentilPercent+myOlivePercent+myGrapePercent;
  writeMessage("crop total: " + QString::number(myCropCheck).toLocal8Bit());
  int mySheepPercent = sheepPercent->value();
  int myGoatPercent = goatPercent->value();
  int myPigPercent = pigPercent->value();
  int myCowPercent = cowPercent->value();
  int myDonkeyPercent = donkeyPercent->value();
  
  if (!sheep->isChecked()) mySheepPercent = 0;
  if (!goat->isChecked()) myGoatPercent = 0;
  if (!pig->isChecked()) myPigPercent = 0;
  if (!cow->isChecked()) myCowPercent = 0;
  if (!donkey->isChecked()) myDonkeyPercent = 0;
  int myAnimalCheck = mySheepPercent+myGoatPercent+myPigPercent+myCowPercent+myDonkeyPercent;
  writeMessage("animal total: " + QString::number(myAnimalCheck).toLocal8Bit());

  if (myCropCheck==(100)) 
  {
    if (myAnimalCheck==(100))
    {
      float myWheatFallowArea = 0.;
      float myWheatTotalArea = 0.;
      float myBarleyFallowArea = 0.;
      float myBarleyTotalArea = 0.;
      float myLentilFallowArea = 0.;
      float myLentilTotalArea = 0.;
      float myOliveFallowArea = 0.;
      float myOliveTotalArea = 0.;
      float myGrapeFallowArea = 0.;
      float myGrapeTotalArea = 0.;
      float myTotalCropArea = 0.;
      float myAvailableFallow = 0.;
      float myWheatKilograms = 0.;
      float myBarleyKilograms = 0.;
      float myLentilKilograms = 0.;
      float myOliveKilograms = 0.;
      float myGrapeKilograms = 0.;
      float myTotalWheatCalories = 0.;
      float myTotalBarleyCalories = 0.;
      float myTotalLentilCalories = 0.;
      float myTotalOliveCalories = 0.;
      float myTotalGrapeCalories = 0.;
    
      float myTotalCalories = myPopulation*myCalories*365.;
      float myPlantCalories = (myOverallPercentage/100.)*myPopulation*myCalories*365.;
      float myTamePlantCalories = ((myOverallPercentage/100.)*(myTamePlantPercentage/100.))*myPopulation*myCalories*365.;
      if (wheat->isChecked() ) 
      {
        int myWheatYield = wheatYield->value();
        int myWheatCalories = wheatCalories->value();      // calories in 1 kg of WHEAT
        float myWheatFallowRatio = wheatFallowRatio->value(); 
        float myWheatArea;
        myTotalWheatCalories = myTamePlantCalories*(myWheatPercent/100.);
        myWheatKilograms = myTotalWheatCalories/myWheatCalories;
        myWheatArea = (((myWheatKilograms)/myWheatYield)*1000.)/10000.;
        myWheatFallowArea = myWheatArea * myWheatFallowRatio;
        myWheatTotalArea = myWheatArea + myWheatFallowArea;
        writeMessage("Wheat area: " + QString::number(myWheatArea).toLocal8Bit());
        writeMessage("Wheat fallow area: " + QString::number(myWheatFallowArea).toLocal8Bit());
        writeMessage("Wheat total area: " + QString::number(myWheatTotalArea).toLocal8Bit());
    
        writeResultsCellValue(1,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myWheatPercent/100.)*100.));
        writeResultsCellValue(1,1,QString::number(myWheatKilograms));
        writeResultsCellValue(1,2,QString::number(myTotalWheatCalories/1000.));
        writeResultsCellValue(1,3,QString::number(myWheatArea));
        writeResultsCellValue(1,4,QString::number(myWheatFallowArea));
        writeResultsCellValue(1,5,QString::number(myWheatTotalArea));
      }
      else
      {
        myWheatTotalArea = 0;
        myWheatFallowArea = 0;
        myWheatKilograms = 0;
      }
    
      if (barley->isChecked() )
      {
        int myBarleyYield = barleyYield->value(); 
        int myBarleyCalories = barleyCalories->value();      // calories in 1 kg of BARLEY
        float myBarleyFallowRatio = barleyFallowRatio->value();
        float myBarleyArea;
        myTotalBarleyCalories = myTamePlantCalories*(myBarleyPercent/100.);
        myBarleyKilograms = myTotalBarleyCalories/myBarleyCalories;
        myBarleyArea = (((myBarleyKilograms)/myBarleyYield)*1000.)/10000.;
        myBarleyFallowArea = myBarleyArea * myBarleyFallowRatio;
        myBarleyTotalArea = myBarleyArea + myBarleyFallowArea;
        writeMessage("Barley area: " + QString::number(myBarleyArea).toLocal8Bit());
        writeMessage("Barley fallow area: " + QString::number(myBarleyFallowArea).toLocal8Bit());
        writeMessage("Barley total area: " + QString::number(myBarleyTotalArea).toLocal8Bit());
    
        writeResultsCellValue(2,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myBarleyPercent/100.)*100.));
        writeResultsCellValue(2,1,QString::number(myBarleyKilograms));
        writeResultsCellValue(2,2,QString::number(myTotalBarleyCalories/1000.));
        writeResultsCellValue(2,3,QString::number(myBarleyArea));
        writeResultsCellValue(2,4,QString::number(myBarleyFallowArea));
        writeResultsCellValue(2,5,QString::number(myBarleyTotalArea));
      }
      else
      {
        myBarleyTotalArea=0;
        myBarleyFallowArea=0;
        myBarleyKilograms=0;
      }
    
      if (lentils->isChecked() )
      {
        int myLentilYield = lentilYield->value();
        int myLentilCalories = lentilCalories->value();      // calories in 1 kg of LENTILS
        float myLentilFallowRatio = lentilFallowRatio->value();
        float myLentilArea; 
        myTotalLentilCalories = myTamePlantCalories*(myLentilPercent/100.);
        myLentilKilograms = myTotalLentilCalories/myLentilCalories;
        myLentilArea = (((myLentilKilograms)/myLentilYield)*1000.)/10000.;
        myLentilFallowArea = myLentilArea * myLentilFallowRatio;
        myLentilTotalArea = myLentilArea + myLentilFallowArea;
        writeMessage("Lentil area: " + QString::number(myLentilArea).toLocal8Bit());
        writeMessage("Lentil fallow area: " + QString::number(myLentilFallowArea).toLocal8Bit());
        writeMessage("Lentil total area: " + QString::number(myLentilTotalArea).toLocal8Bit());
    
        writeResultsCellValue(3,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myLentilPercent/100.)*100.));
        writeResultsCellValue(3,1,QString::number(myLentilKilograms));
        writeResultsCellValue(3,2,QString::number(myTotalLentilCalories/1000.));
        writeResultsCellValue(3,3,QString::number(myLentilArea));
        writeResultsCellValue(3,4,QString::number(myLentilFallowArea));
        writeResultsCellValue(3,5,QString::number(myLentilTotalArea));
      }
      else
      {
        myLentilTotalArea = 0;
        myLentilFallowArea = 0;
        myLentilKilograms = 0;
      }
    
      if (olives->isChecked() )
      {
        int myOliveYield = oliveYield->value();
        int myOliveCalories = oliveCalories->value();      // calories in 1 kg of OLIVES
        float  myOliveFallowRatio = oliveFallowRatio->value();
        float myOliveArea;
        myTotalOliveCalories = myTamePlantCalories*(myOlivePercent/100.);
        myOliveKilograms = myTotalOliveCalories/myOliveCalories;
        myOliveArea = (((myOliveKilograms)/myOliveYield)*1000.)/10000.;
        myOliveFallowArea = myOliveArea *  myOliveFallowRatio;
        myOliveTotalArea = myOliveArea + myOliveFallowArea;
        writeMessage("olive area: " + QString::number(myOliveArea).toLocal8Bit());
        writeMessage("olive fallow area: " + QString::number(myOliveFallowArea).toLocal8Bit());
        writeMessage("olive total area: " + QString::number(myOliveTotalArea).toLocal8Bit());
    
        writeResultsCellValue(4,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myOlivePercent/100.)*100.));
        writeResultsCellValue(4,1,QString::number(myOliveKilograms));
        writeResultsCellValue(4,2,QString::number(myTotalOliveCalories/1000.));
        writeResultsCellValue(4,3,QString::number(myOliveArea));
        writeResultsCellValue(4,4,QString::number(myOliveFallowArea));
        writeResultsCellValue(4,5,QString::number(myOliveTotalArea));
      }
      else
      {
        myOliveTotalArea = 0;
        myOliveFallowArea = 0;
        myOliveKilograms=0;
      }

      if (grapes->isChecked() )
      {
        int myGrapeYield = grapeYield->value();
        int myGrapeCalories = grapeCalories->value();
        float myGrapeFallowRatio = grapeFallowRatio->value();  // calories in 1 kg of GRAPES
        float myGrapeArea;
        myTotalGrapeCalories = myTamePlantCalories*(myGrapePercent/100.);
        myGrapeKilograms = myTotalGrapeCalories/myGrapeCalories;
        myGrapeArea = (((myGrapeKilograms)/myGrapeYield)*1000.)/10000.;
        myGrapeFallowArea = myGrapeArea * myGrapeFallowRatio;
        myGrapeTotalArea = myGrapeArea + myGrapeFallowArea;
        writeMessage("grape area: " + QString::number(myGrapeArea).toLocal8Bit());
        writeMessage("grape fallow area: " + QString::number(myGrapeFallowArea).toLocal8Bit());
        writeMessage("grape total area: " + QString::number(myGrapeTotalArea).toLocal8Bit());
    
        writeResultsCellValue(5,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myGrapePercent/100.)*100.));
        writeResultsCellValue(5,1,QString::number(myGrapeKilograms));
        writeResultsCellValue(5,2,QString::number(myTotalGrapeCalories/1000.));
        writeResultsCellValue(5,3,QString::number(myGrapeArea));
        writeResultsCellValue(5,4,QString::number(myGrapeFallowArea));
        writeResultsCellValue(5,5,QString::number(myGrapeTotalArea));
      }
      else
      {
        myGrapeTotalArea = 0;
        myGrapeFallowArea = 0;
        myGrapeKilograms = 0;
      }
    
      myAvailableFallow = (myWheatFallowArea+myBarleyFallowArea+myLentilFallowArea+myOliveFallowArea+myGrapeFallowArea);
      myTotalCropArea = (myWheatTotalArea+myBarleyTotalArea+myLentilTotalArea+myOliveTotalArea+myGrapeTotalArea)-myAvailableFallow;
      myTotalCropArea = myAvailableFallow + myTotalCropArea;
      myTotalCalories = myTotalWheatCalories+myTotalBarleyCalories+myTotalLentilCalories+myTotalOliveCalories+myTotalGrapeCalories;
    
      if ( calculations->isChecked() )
      {
        // this can just stay empty now, I guess.
        // I guess it could do the filling of
        // the table, or pop up a report window
        // as an alternative
      }
      else if (euclidean->isChecked() )
      {
        writeMessage("Euclidean is checked.");
        // create animalcost raster (cost surface)
        // for euclidean, distance from point (the coordinates of the site)
        // for walk time, r.walk with 18000 seconds as max cost
        // for path dist, use _______ with 15km as max cost
        // (this is done with grass.)
    
        //  determine how many animals use fallow,
        //  how many use unique rasters, and
        //  set targets to 0 if not using unique raster after
        //  adding to common target.
        int myHIGH = 0;
        int myMED = 0;
        int myLOW = 0;
        int myAnimalCount = 0;
        float myCommonAnimalTarget = 0;
        int myFallowGrazingAnimalsCount = 0;
        float mySheepFallow = 0;
        float myGoatFallow = 0;
        float myPigFallow = 0;
        float myCowFallow = 0;
        float myDonkeyFallow = 0;
        float myAvailableFallow = 0;
    
        float mySheepTarget = 0;
        float myGoatTarget = 0;
        float myPigTarget = 0;
        float myCowTarget = 0;
        float myDonkeyTarget = 0;
        float myAnimalTarget = 0;
        float myCropTarget = 0;
        float myWheatTarget = 0;
        float myBarleyTarget = 0;
        float myLentilTarget = 0;
        float myOliveTarget = 0;
        float myGrapeTarget = 0;
        float myEqualFallow = 0;
        float mySheepLeftover = 0;
        float myGoatLeftover = 0;
        float myPigLeftover = 0;
        float myCowLeftover = 0;
        float myDonkeyLeftover = 0;
    /********************************************************************
    Animal Modelling to determine target areas
    *********************************************************************/
      int myMeatDietPercent = dietSlider->value(); 
      int myMeatTamePercent = meatSlider->value(); 
    
        if (pig->isChecked() )
        {
          int myPigLitterSize = pigLitterSize->value(); 
          int myPigKillWeight = pigWeight->value(); 
          int myPigGrowTime = pigGrowTime->value(); 
          int myCalories = dailyCalories->value();
          int myPopulation = population->value();
          bool myPigUseFodder = pigFodderUse->isChecked(); 
          float myPigProdnTgt = 
            (
              (
                (
                  (
                    (myMeatDietPercent/100.)*
                    (myMeatTamePercent/100.)*
                    (myPigPercent/100.)
                  )
                  *myCalories
                  *myPopulation
                )
                /3000.
              )
              *365.*2.
            ); 
          float myPigButcherNumbersRqd = (myPigProdnTgt/100.);
          float mySows = ((10.*myPigProdnTgt)/(1760.53*myPigLitterSize));
          float myDrySows = ((mySows*30.80)/249.70);
          float myGestSows = ((mySows*41.6)/249.70);
          float myLactatingSows = ((mySows*177.20)/249.70);
          float mySucklingPigs = (((355.10/41.60)/10.)*myPigLitterSize*myLactatingSows);
          float myNursingPigs = ((((mySows*420.10)/249.70)/10.)*myPigLitterSize);
          float myGrowingPigs = ((((mySows*1414.70)/249.70)/10.)*myPigLitterSize);
          float total = (mySows+mySucklingPigs+myNursingPigs+myGrowingPigs);
          writeMessage("fodder flag value: " + QString::number(myPigUseFodder).toLocal8Bit());
          writeMessage("You supplied me with this information:");
          writeMessage("Population of Settlement: " + QString::number(myPopulation).toLocal8Bit());
          writeMessage("Calories/person per day: " + QString::number(myCalories).toLocal8Bit());
          writeMessage("Percentage of Calories in the diet from MEAT: " + QString::number(myMeatDietPercent).toLocal8Bit());
          writeMessage("Percentage of MEAT that is from domesticated animals: " + QString::number(myMeatTamePercent).toLocal8Bit());
          writeMessage("Percentage of DOMESTICATED MEAT that is from PIGS: " + QString::number(myPigPercent).toLocal8Bit());
          writeMessage("Calories per kg in PIG MEAT: 3000 assumed");
          writeMessage("Average Litter Size: " + QString::number(myPigLitterSize).toLocal8Bit());
          writeMessage("kg of meat per year: " + QString::number(myPigProdnTgt/2.).toLocal8Bit());
          writeMessage("Number of 100kg pigs: " + QString::number(myPigButcherNumbersRqd).toLocal8Bit());
          writeMessage("mySows required to produce this much meat: " + QString::number(mySows).toLocal8Bit());
          writeMessage("Non-Pregnant sows and gilts: " + QString::number(myDrySows).toLocal8Bit());
          writeMessage("Gestating sows: " + QString::number(myGestSows).toLocal8Bit());
          writeMessage("Lactating sows: " + QString::number(myLactatingSows).toLocal8Bit());
          writeMessage("Total Adult Females: " + QString::number(mySows).toLocal8Bit());
          writeMessage("Suckling Pigs: " + QString::number(mySucklingPigs).toLocal8Bit());
          writeMessage("Nursery Pigs: " + QString::number(myNursingPigs).toLocal8Bit());
          writeMessage("Growing and finishing pigs: " + QString::number(myGrowingPigs).toLocal8Bit());
          writeMessage("Total pigs: " + QString::number(total).toLocal8Bit());
        }
    
    /********************************************************************
    Adjusting Animal Targets to account for grazing of fallow crop land
    *********************************************************************/
        if (sheep->isChecked())
        {
          if (sheepGrazeFallow->isChecked())
          {
            myAnimalCount++;
            if (fallowSheepPriority->currentIndex()==0)  // 0 == HIGH
            {
              int mySheepFallow=1; // item 1, or HIGH
              myHIGH++;
            }
            else if (fallowSheepPriority->currentIndex()==1)  // 1 == MED
              {
                int mySheepFallow=2; // item 2, or MED
                myMED++;
              }
            else if (fallowSheepPriority->currentIndex()==2)  // 2 == LOW
              {
                int mySheepFallow=3; // item 3, or LOW
                myLOW++;
              }
          }
        }
    
        if (goat->isChecked())
        {
          if (goatGrazeFallow->isChecked())
          {
            myAnimalCount++;
            if (fallowGoatPriority->currentIndex()==0)  // 0 == HIGH
            {
              int myGoatFallow=1; // item 1, or HIGH
            }
            else if (fallowGoatPriority->currentIndex()==1)  // 1 == MED
              {
                int myGoatFallow=2; // item 2, or MED
              }
            else if (fallowGoatPriority->currentIndex()==2)  // 2 == LOW
              {
                int myGoatFallow=3; // item 3, or LOW
              }
          }
        }
    
        if (pig->isChecked())
        {
          if (pigGrazeFallow->isChecked())
          {
            myAnimalCount++;
            if (fallowPigPriority->currentIndex()==0)  // 0 == HIGH
            {
              int myPigFallow=1; // item 1, or HIGH
              writeMessage("Pig Priority: " + QString::number(myPigFallow).toLocal8Bit());
            }
            else if (fallowPigPriority->currentIndex()==1)  // 1 == MED
              {
                int myPigFallow=2; // item 2, or MED
                writeMessage("Pig Priority: " + QString::number(myPigFallow).toLocal8Bit());
              }
            else if (fallowPigPriority->currentIndex()==2)  // 2 == LOW
              {
                int myPigFallow=3; // item 3, or LOW
                writeMessage("Pig Priority: " + QString::number(myPigFallow).toLocal8Bit());
              }
          }
        }
    
        if (cow->isChecked())
        {
          if (cowGrazeFallow->isChecked())
          {
            myAnimalCount++;
            if (fallowCowPriority->currentIndex()==0)  // 0 == HIGH
            {
              int myCowFallow=1; // item 1, or HIGH
            }
            else if (fallowCowPriority->currentIndex()==1)  // 1 == MED
              {
                int myCowFallow=2; // item 2, or MED
              }
            else if (fallowCowPriority->currentIndex()==1)  // 2 == LOW
              {
                int myCowFallow=3; // item 3, or LOW
              }
          }
        }
    
        if (donkey->isChecked())
        {
          if (donkeyGrazeFallow->isChecked())
          {
            myAnimalCount++;
            if (fallowDonkeyPriority->currentIndex()==0)  // 0 == HIGH
            {
              int myDonkeyFallow=1; // item 1, or HIGH
            }
            else if (fallowDonkeyPriority->currentIndex()==1)  // 1 == MED
              {
                int myDonkeyFallow=2; // item 2, or MED
              }
            else if (fallowDonkeyPriority->currentIndex()==1)  // 2 == LOW
              {
                int myDonkeyFallow=3; // item 3, or LOW
              }
          }
        }
    
    
      while (!myHIGH==0)
      {
    
        myEqualFallow = myAvailableFallow/myHIGH;
    
        if (sheep->isChecked())
        {
          if (sheepGrazeFallow->isChecked())
          {
            if (mySheepFallow==1)  // if it is useHIGH
            {
              if (mySheepTarget < myEqualFallow)
              {
                mySheepLeftover = myEqualFallow - mySheepTarget;
                mySheepFallow = 0.;
                mySheepTarget = 0.;
                myHIGH--;
              }
              else 
              {
                mySheepTarget = mySheepTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (goat->isChecked())
        {
          if (goatGrazeFallow->isChecked())
          {
            if (myGoatFallow==1)
            {
              if (myGoatTarget < myEqualFallow)
              {
                myGoatLeftover = myEqualFallow - mySheepTarget;
                myGoatFallow = 0.;
                myGoatTarget = 0.;
                myHIGH--;
              }
              else 
              {
                myGoatTarget = myGoatTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (pig->isChecked())
        {
          if (pigGrazeFallow->isChecked())
          {
            if (myPigFallow==1)
            {
              if (myPigTarget < myEqualFallow)
              {
                myPigLeftover = myEqualFallow - mySheepTarget;
                myPigFallow = 0.;
                myPigTarget = 0.;
                myHIGH--;
              }
              else 
              {
                myPigTarget = myPigTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (cow->isChecked())
        {
          if (cowGrazeFallow->isChecked())
          {
            if (myCowFallow==1)
            {
              if (myCowTarget < myEqualFallow)
              {
                myCowLeftover = myEqualFallow - mySheepTarget;
                myCowFallow = 0.;
                myCowTarget = 0.;
                myHIGH--;
              }
              else 
              {
                myCowTarget = myCowTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (donkey->isChecked())
        {
          if (donkeyGrazeFallow->isChecked())
          {
            if (myDonkeyFallow==1)
            {
              if (myDonkeyTarget < myEqualFallow)
              {
                myDonkeyLeftover = myEqualFallow - mySheepTarget;
                myDonkeyFallow = 0.;
                myDonkeyTarget = 0.;
                myHIGH--;
              }
              else 
              {
                myDonkeyTarget = myDonkeyTarget - myEqualFallow;
              }
            }
          }
        }
      myAvailableFallow = mySheepLeftover+myGoatLeftover+myPigLeftover+myCowLeftover+myDonkeyLeftover;
      } // end of do while
    
      
      while (!myMED==0)
      {
        myEqualFallow = myAvailableFallow/myMED;
    
        if (sheep->isChecked())
        {
          if (sheepGrazeFallow->isChecked())
          {
            if (mySheepFallow==2)  // if it is useMED
            {
              if (mySheepTarget < myEqualFallow)
              {
                mySheepLeftover = myEqualFallow - mySheepTarget;
                mySheepFallow = 0.;
                mySheepTarget = 0.;
                myMED--;
              }
              else 
              {
                mySheepTarget = mySheepTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (goat->isChecked())
        {
          if (goatGrazeFallow->isChecked())
          {
            if (myGoatFallow==2)  // if it is useMED
            {
              if (myGoatTarget < myEqualFallow)
              {
                myGoatLeftover = myEqualFallow - mySheepTarget;
                myGoatFallow = 0.;
                myGoatTarget = 0.;
                myMED--;
              }
              else 
              {
                myGoatTarget = myGoatTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (pig->isChecked())
        {
          if (pigGrazeFallow->isChecked())
          {
            if (myPigFallow==2)  // if it is useMED
            {
              if (myPigTarget < myEqualFallow)
              {
                myPigLeftover = myEqualFallow - mySheepTarget;
                myPigFallow = 0.;
                myPigTarget = 0.;
                myMED--;
              }
              else 
              {
                myPigTarget = myPigTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (cow->isChecked())
        {
          if (cowGrazeFallow->isChecked())
          {
            if (myCowFallow==2)  // if it is useMED
            {
              if (myCowTarget < myEqualFallow)
              {
                myCowLeftover = myEqualFallow - mySheepTarget;
                myCowFallow = 0.;
                myCowTarget = 0.;
                myMED--;
              }
              else 
              {
                myCowTarget = myCowTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (donkey->isChecked())
        {
          if (donkeyGrazeFallow->isChecked())
          {
            if (myDonkeyFallow==2)  // if it is useMED
            {
              if (myDonkeyTarget < myEqualFallow)
              {
                myDonkeyLeftover = myEqualFallow - mySheepTarget;
                myDonkeyFallow = 0.;
                myDonkeyTarget = 0.;
                myMED--;
              }
              else 
              {
                myDonkeyTarget = myDonkeyTarget - myEqualFallow;
              }
            }
          }
        }
      myAvailableFallow = mySheepLeftover+myGoatLeftover+myPigLeftover+myCowLeftover+myDonkeyLeftover;
      } // end of do while
    
      while (!myLOW==0)
      {
    
        myEqualFallow = myAvailableFallow/myLOW;
    
        if (sheep->isChecked())
        {
          if (sheepGrazeFallow->isChecked())
          {
            if (mySheepFallow==3)  // if it is useLOW
            {
              if (mySheepTarget < myEqualFallow)
              {
                mySheepLeftover = myEqualFallow - mySheepTarget;
                mySheepFallow = 0;
                mySheepTarget = 0;
                myLOW--;
              }
              else 
              {
                mySheepTarget = mySheepTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (goat->isChecked())
        {
          if (goatGrazeFallow->isChecked())
          {
            if (myGoatFallow==3)  // if it is useLOW
            {
              if (myGoatTarget < myEqualFallow)
              {
                myGoatLeftover = myEqualFallow - mySheepTarget;
                myGoatFallow = 0;
                myGoatTarget = 0;
                myLOW--;
              }
              else 
              {
                myGoatTarget = myGoatTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (pig->isChecked())
        {
          if (pigGrazeFallow->isChecked())
          {
            if (myPigFallow==3)  // if it is useLOW
            {
              if (myPigTarget < myEqualFallow)
              {
                myPigLeftover = myEqualFallow - mySheepTarget;
                myPigFallow = 0;
                myPigTarget = 0;
                myLOW--;
              }
              else 
              {
                myPigTarget = myPigTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (cow->isChecked())
        {
          if (cowGrazeFallow->isChecked())
          {
            if (myCowFallow==3)  // if it is useLOW
            {
              if (myCowTarget < myEqualFallow)
              {
                myCowLeftover = myEqualFallow - mySheepTarget;
                myCowFallow = 0;
                myCowTarget = 0;
                myLOW--;
              }
              else 
              {
                myCowTarget = myCowTarget - myEqualFallow;
              }
            }
          }
        }
    
        if (donkey->isChecked())
        {
          if (donkeyGrazeFallow->isChecked())
          {
            if (myDonkeyFallow==3)  // if it is useLOW
            {
              if (myDonkeyTarget < myEqualFallow)
              {
                myDonkeyLeftover = myEqualFallow - mySheepTarget;
                myDonkeyFallow = 0;
                myDonkeyTarget = 0;
                myLOW--;
              }
              else 
              {
                myDonkeyTarget = myDonkeyTarget - myEqualFallow;
              }
            }
          }
        }
     
      myAvailableFallow = mySheepLeftover+myGoatLeftover+myPigLeftover+myCowLeftover+myDonkeyLeftover;
    
      } // end of do while
    
        if (!sheepRaster->isChecked())
        {
          myCommonAnimalTarget=myCommonAnimalTarget+mySheepTarget;
          mySheepTarget=0;
          myFallowGrazingAnimalsCount++;
        }
        if (!goatraster->isChecked())
        {
          myCommonAnimalTarget=myCommonAnimalTarget+myGoatTarget;
          myGoatTarget=0;
          myFallowGrazingAnimalsCount++;
        }
        if (!pigRaster->isChecked())
        {
          myCommonAnimalTarget=myCommonAnimalTarget+myPigTarget;
          myPigTarget=0;
          myFallowGrazingAnimalsCount++;
        }
        if (!cowRaster->isChecked())
        {
          myCommonAnimalTarget=myCommonAnimalTarget+myCowTarget;
          myCowTarget=0;
          myFallowGrazingAnimalsCount++;
        }
        if (!donkeyRaster->isChecked())
        {
          myCommonAnimalTarget=myCommonAnimalTarget+myDonkeyTarget;
          myDonkeyTarget=0;
          myFallowGrazingAnimalsCount++;
        }
    
        writeMessage("Sheep Priority: " + QString::number(mySheepFallow).toLocal8Bit());
        writeMessage("Goat Priority: " + QString::number(myGoatFallow).toLocal8Bit());
    
        writeMessage("Pig Priority: " + QString::number(myPigFallow).toLocal8Bit());
    
        writeMessage("Cow Priority: " + QString::number(myCowFallow).toLocal8Bit());
    
        writeMessage("Donkey Priority: " + QString::number(myDonkeyFallow).toLocal8Bit());
    
    
    
        float myTotalAreaRequired = myCropTarget + myAnimalTarget + myWheatTarget + myBarleyTarget
          + myLentilTarget + myOliveTarget + myGrapeTarget + mySheepTarget + myGoatTarget
          + myPigTarget + myCowTarget;
        int myIncrement = precision->value();
        bool mySolutionFlag=false;
        int myRadius; // =sqrt(myTotalAreaRequired/3.14); // minimum size possible
    
        /*
          while (mySolutionFlag==false)
          {
        // create the temp_cost_surface raster, with all values > radius set to void
        //  make all temp rasters originalraster_temp maybe?
        // multiply each suitability layer by the temp_cost_surface
        // check each resumyLentilTotalAreant new raster to see if target has been met. if so, mySolutionFlag=true
        myRadius = myRadius + myIncrement;
        //query each
        }
        */
    
      }
    
      else if (walking->isChecked() )
      {
        writeMessage("Walking Distance is checked");
        //
        // the only difference for this routine is in how we make the cost surface map,
        //  and the value we start the loop at.  I think the best solution is to make
        //  r.walk calculate the cost surface for 5 hours, or 300 minutes.  Anything
        //  further away than that is going to be dubious anyway.  And, instead of starting
        //  on the 'inside' we start on the outside, and work in.  Binary search again, I
        //  think, would be fastest.
      }
      else if (pathdistance->isChecked() )
      {
        writeMessage("Path Distance is checked.");
        //
        // the difference for this routine is, again, in how we make the cost surface map,
        //  and the value we start the loop at.  I think the best solution is to make
        //  r.path calculate the cost surface for like 15km.  Anything
        //  further away than that is going to be dubious anyway.  And, instead of starting
        //  on the 'inside' we start on the outside, and work in.  Binary search again, I
        //  think, would be fastest.
      }
    }
    else writeMessage("You wanker!  make sure that everything adds up to 100! ");
  }
  else writeMessage("You wanker!  make sure that everything adds up to 100! ");
}
/*   NOTES and bash stuff
     if the wheat button is checked then
     if NOT a unique raster then
     get the area required for wheat and add it to total area 
     else run a seperate loop for wheat
     else add nothing to total area

     repeat for all crops

     bash code for the loop looks like this:

     euclidean () {   # =-FUNCTION-= to create raster using EUCLIDEAN DISTANCE
     area=0
     while [ ${area} -le ${land_reqrd_total} ]
     do #the magic loop
       (( myRadius = ${myRadius} + 30)) # <---- model precision value used HERE!
       r.circle -b output=circle coordinate=744800,3611100 max=${myRadius} --overwrite 
       g.remove rast=catchment
       r.mapcalc catchment="${src}"*circle
       echo a catchment area with a myRadius of ${myRadius} meters contains
       area=`r.stats -an input=catchment | awk '{printf("%d\n", $2);}'`
       echo ${area} square meters of land and our target is 
       echo ${land_reqrd_total} square meters of land
     done


*/
