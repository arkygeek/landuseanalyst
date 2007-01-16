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

void LaMainForm::on_wheatview_clicked()
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myWheatPercentage = wheat_percent->value();     // PERCENTAGE OF WHEAT in plant portion of diet
  int myWheatYield = wheat_yield->value();      // expected average WHEAT YIELD
  int myWheatCalories = wheatcals->value();      // FALLOW RATIO for WHEAT
  float myWheatFallowRatio = wheat_fallow_ratio->value();  // 
  int myCalories = dailycalories->value();
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

void LaMainForm::on_barleyview_clicked() 
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myBarleyPercentage = barley_percent->value();     // PERCENTAGE OF BARLEY in plant portion of diet
  int myBarleyYield = barley_yield->value();      // expected average BARLEY YIELD
  int myBarleyCaloriese = barleycals->value();      // FALLOW RATIO for BARLEY
  float myBarleyFallowRatio = barley_fallow_ratio->value();  // 
  int myCalories = dailycalories->value();
  int myPopulation = population->value();

  // calculate area required for barley
  float myBarleyArea;  // barley area 
  float myBarleyFallowArea;  // barley fallow area
  float myBarleyTotalArea;  // barley total area
  myBarleyArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myBarleyPercentage/100.))*myCalories*365.)/myBarleyCaloriese)*myPopulation)/myBarleyYield)*1000.);
  myBarleyFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myBarleyPercentage/100.))*myCalories*365.)/myBarleyCaloriese)*myPopulation)/myBarleyYield)*1000.)*(myBarleyFallowRatio);
  myBarleyTotalArea = myBarleyArea + myBarleyFallowArea;
  writeMessage("Barley area: " + QString::number(myBarleyArea).toLocal8Bit());
  writeMessage("Barley fallow area: " + QString::number(myBarleyFallowArea).toLocal8Bit());
  writeMessage("Barley total area: " + QString::number(myBarleyTotalArea).toLocal8Bit());
}

void LaMainForm::on_lentilview_clicked() 
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myLentilPercentage = lentil_percent->value();     // PERCENTAGE OF LENTIL in plant portion of diet
  int myLentilYield = lentil_yield->value();      // expected average LENTIL YIELD
  int myLentilCalories = lentilcals->value();      // FALLOW RATIO for LENTIL
  float myLentilFallowRatio = lentil_fallow_ratio->value();  // 
  int myCalories = dailycalories->value();
  int myPopulation = population->value();

  // calculate area required for LENTIL
  float myLentilArea;  // wheat area 
  float myLentilFallowArea;  // wheat fallow area
  float myLentilTotalArea;  // wheat total area
  myLentilArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myLentilPercentage/100.))*myCalories*365.)/myLentilCalories)*myPopulation)/myLentilYield)*1000.);
  myLentilFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myLentilPercentage/100.))*myCalories*365.)/myLentilCalories)*myPopulation)/myLentilYield)*1000.)*(myLentilFallowRatio);
  myLentilTotalArea = myLentilArea + myLentilFallowArea;
  writeMessage("Lentil area: " + QString::number(myLentilArea).toLocal8Bit());
  writeMessage("Lentil fallow area: " + QString::number(myLentilFallowArea).toLocal8Bit());
  writeMessage("Lentil total area: " + QString::number(myLentilTotalArea).toLocal8Bit());
}

void LaMainForm::on_oliveview_clicked() 
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myOlivePercentage = olive_percent->value();     // PERCENTAGE OF OLIVE in plant portion of diet
  int oy = olive_yield->value();      // expected average OLIVE YIELD
  int ocal = olivecals->value();      // FALLOW RATIO for OLIVE
  float ofr = olive_fallow_ratio->value();  // 
  int myCalories = dailycalories->value();
  int myPopulation = population->value();

  // calculate area required for OLIVE
  float oa;  // olive area 
  float myOliveFallowArea;  // olive fallow area
  float myOliveTotalArea;  // olive total area
  oa = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myOlivePercentage/100.))*myCalories*365.)/ocal)*myPopulation)/oy)*1000.);
  myOliveFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myOlivePercentage/100.))*myCalories*365.)/ocal)*myPopulation)/oy)*1000.)*(ofr);
  myOliveTotalArea = oa + myOliveFallowArea;
  writeMessage("olive area: " + QString::number(oa).toLocal8Bit());
  writeMessage("olive fallow area: " + QString::number(myOliveFallowArea).toLocal8Bit());
  writeMessage("olive total area: " + QString::number(myOliveTotalArea).toLocal8Bit());
}

void LaMainForm::on_grapeview_clicked() 
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myGrapePercent = grape_percent->value();     // PERCENTAGE OF GRAPE in plant portion of diet
  int gy = grape_yield->value();      // expected average GRAPE YIELD
  int gcal = grapecals->value();      // FALLOW RATIO for GRAPE
  float gfr = grape_fallow_ratio->value();  // 
  int myCalories = dailycalories->value();
  int myPopulation = population->value();

  // calculate area required for grape
  float ga;  // grape area 
  float myGrapeFallowArea;  // grape fallow area
  float myGrapeTotalArea;  // grape total area
  ga = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myGrapePercent/100.))*myCalories*365.)/gcal)*myPopulation)/gy)*1000.);
  myGrapeFallowArea = ((((((((myOverallPercentage*myTamePlantPercentage)/100.)*(myGrapePercent/100.))*myCalories*365.)/gcal)*myPopulation)/gy)*1000.)*(gfr);
  myGrapeTotalArea = ga + myGrapeFallowArea;
  writeMessage("grape area: " + QString::number(ga).toLocal8Bit());
  writeMessage("grape fallow area: " + QString::number(myGrapeFallowArea).toLocal8Bit());
  writeMessage("grape total area: " + QString::number(myGrapeTotalArea).toLocal8Bit());
}

void LaMainForm::on_pigview_clicked() 
{
  int mdp = dietslider->value(); //grab value from slider for overall meat percentage
  int mtp = (100 - (meatslider->value())); //grab value from slider for tame meat percentage
  int pp = pigpercent->value(); //grab value from form for percentage of pigmeat of meat portion of diet
  int pls = piglittersize->value(); //grab value from form for pig litter size
  int pw = pigweight->value(); //grab value from form for for pig kill weight
  int pgt = piggrowtime->value(); //grab value from form for pig grow time
  int myCalories = dailycalories->value();
  int myPopulation = population->value();
  bool pfflag = pigfodderuse->isCheckable(); //grab value from form for fodder use flag
  int pfa = pigfodderamount->value(); //grab value from form for amount of fodder
  //int pfc = pigfoddercrop->currentindex(); //grab value from form for type of fodder
  //int pft = pigfoddertime->currentindex(); //grab value from form for time measurement of fodder rate
  //int pgrflag = piggrazefallow->checked(); //grab value from form for fallow grazing flag
  float meat = (((((mdp/100.)*(mtp/100.)*(pp/100.))*myCalories*myPopulation)/3000.)*365.*2.); // 3000 is calories/kg of pork
  float animals = (meat/100.);
  float mySows = ((10.*meat)/(1760.53*pls));
  float myDrySows = ((mySows*30.80)/249.70);
  float gmySows = ((mySows*41.6)/249.70);
  float myLactatingSows = ((mySows*177.20)/249.70);
  float mySucklingPigs = (((355.10/41.60)/10.)*pls*myLactatingSows);
  float myNursingPigs = ((((mySows*420.10)/249.70)/10.)*pls);
  float myGrapePercentigs = ((((mySows*1414.70)/249.70)/10.)*pls);
  float total = (mySows+mySucklingPigs+myNursingPigs+myGrapePercentigs);
  writeMessage("fodder flag value: " + QString::number(pfflag).toLocal8Bit());
  writeMessage("You supplied me with this information:");
  writeMessage("Population of Settlement: " + QString::number(myPopulation).toLocal8Bit());
  writeMessage("Calories/person per day: " + QString::number(myCalories).toLocal8Bit());
  writeMessage("Percentage of Calories in the diet from MEAT: " + QString::number(mdp).toLocal8Bit());
  writeMessage("Percentage of MEAT that is from domesticated animals: " + QString::number(mtp).toLocal8Bit());
  writeMessage("Percentage of DOMESTICATED MEAT that is from PIGS: " + QString::number(pp).toLocal8Bit());
  writeMessage("Calories per kg in PIG MEAT: 3000 assumed");
  writeMessage("Average Litter Size: " + QString::number(pls).toLocal8Bit());
  writeMessage("kg of meat per year: " + QString::number(meat).toLocal8Bit());
  writeMessage("Number of 100kg pigs: " + QString::number(animals).toLocal8Bit());
  writeMessage("mySows required to produce this much meat: " + QString::number(mySows).toLocal8Bit());
  writeMessage("Non-Pregnant sows and gilts: " + QString::number(myDrySows).toLocal8Bit());
  writeMessage("Gestating sows: " + QString::number(gmySows).toLocal8Bit());
  writeMessage("Lactating sows: " + QString::number(myLactatingSows).toLocal8Bit());
  writeMessage("Total Adult Females: " + QString::number(mySows).toLocal8Bit());
  writeMessage("Suckling Pigs: " + QString::number(mySucklingPigs).toLocal8Bit());
  writeMessage("Nursery Pigs: " + QString::number(myNursingPigs).toLocal8Bit());
  writeMessage("Growing and finishing pigs: " + QString::number(myGrapePercentigs).toLocal8Bit());
  writeMessage("Total pigs: " + QString::number(total).toLocal8Bit());
}


void LaMainForm::on_meatslider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  meatwildpercent->setText(myMinString);
  meattamepercent->setText(myMaxString);
}

void LaMainForm::on_dietslider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(theValue);
  QString myMaxString = QString::number(100-theValue);
  meatpercent->setText(myMinString);
  plantpercent->setText(myMaxString);
}

void LaMainForm::on_plantslider_valueChanged(int theValue) 
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  plantwildpercent->setText(myMinString);
  planttamepercent->setText(myMaxString);
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

void LaMainForm::on_diet_breakdown_button_clicked() 
{
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int pdm = dietslider->value();
  int ptm = meatslider->value();
  int myCalories = dailycalories->value();
  int myPopulation = population->value();

  float myTotalCalories = myPopulation*myCalories*365.;
  float myPlantCalories = (myOverallPercentage/100.)*myTotalCalories;
  float tamemyPlantCalories = ((myOverallPercentage/100.)*(myTamePlantPercentage/100.))*myTotalCalories;
  float animalcals = (pdm/100.)*myTotalCalories;
  float tameanimalcals = ((pdm/100.)*(ptm/100.))*myTotalCalories;

  writeDiet("Calories per person per year: " + QString::number((myCalories*365.)/1000.).toLocal8Bit() + "kcal");
  writeDiet("Calories required for population are: " + QString::number(myTotalCalories/1000.).toLocal8Bit() + "kcal");
  writeDiet(" ");
  writeDiet("Plants contribute " + QString::number(myOverallPercentage).toLocal8Bit() + "% to diet, or " + QString::number(myPlantCalories/1000.).toLocal8Bit() + " kcal");
  writeDiet("Meat contributes " + QString::number(pdm).toLocal8Bit() + "% to diet, or  " + QString::number(animalcals/1000.).toLocal8Bit() + " kcal");
  writeDiet(" ");
  writeDiet("Tame Plants account for " + QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(myPlantCalories/1000.).toLocal8Bit() + " kcal");
  writeDiet("Tame Animals account for " + QString::number((pdm/100.)*(ptm/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(animalcals/1000.).toLocal8Bit() + " kcal");
}

void LaMainForm::writeMessage(QString theText) 
{
  textBrowserResults->append(theText);
}

void LaMainForm::writeDiet(QString theText) 
{
  breakdown_display->append(theText);
}

void LaMainForm::writePlantCellValue(int theRow, int theCol, QString theValue) 
{
  QTableWidgetItem *mypItem = new QTableWidgetItem(theValue);
  plant_table->setItem(theRow, theCol, mypItem);
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
  int myOverallPercentage = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int myTamePlantPercentage = plantslider->value();       // TAME PLANT percentage
  int myCalories = dailycalories->value();
  int myPopulation = population->value();
  float myWheatFallowArea = 0;    // WHEAT fallow area
  float myWheatTotalArea = 0;    // WHEAT total area
  float myBarleyFallowArea = 0;    // BARLEY fallow area
  float myBarleyTotalArea = 0;    // BARLEY total area
  float myLentilFallowArea = 0;    // LENTIL fallow area
  float myLentilTotalArea = 0;    // LENTIL total area
  float myOliveFallowArea = 0;    // OLIVE fallow area
  float myOliveTotalArea = 0;    // OLIVE total area
  float myGrapeFallowArea = 0;    // grape fallow area
  float myGrapeTotalArea = 0;    // grape total area
  float myStandardTotalArea = 0;    // total area required for crops using the standard mask
  float myStandardCropTotalArea = 0;    // total area of sown land
  float myStandardFallowAreaTotal = 0;  // total area of fallow
  float myWheatKilograms = 0;
  float myBarleyKilograms = 0;
  float myLentilKilograms = 0;
  float myOliveKilograms = 0;
  float myGrapeKilograms = 0;
  float myTotalWheatCalories = 0;
  float myTotalBarleyCalories = 0;
  float myTotalLentilCalories = 0;
  float myTotalOliveCalories = 0;
  float myTotalGrapeCalories = 0;

  float myTotalCalories = myPopulation*myCalories*365.;
  float myPlantCalories = (myOverallPercentage/100.)*myPopulation*myCalories*365.;
  float tamemyPlantCalories = ((myOverallPercentage/100.)*(myTamePlantPercentage/100.))*myPopulation*myCalories*365.;
  if (wheat->isChecked() ) 
  {
    int myWheatPercent = wheat_percent->value();     // PERCENTAGE OF WHEAT in plant portion of diet
    int myWheatYield = wheat_yield->value();      // expected average WHEAT YIELD
    int myWheatCalories = wheatcals->value();      // calories in 1 kg of WHEAT
    float myWheatFallowRatio = wheat_fallow_ratio->value();  // FALLOW RATIO for WHEAT
    float myWheatArea;          // WHEAT area 
    myTotalWheatCalories = tamemyPlantCalories*(myWheatPercent/100.);
    myWheatKilograms = myTotalWheatCalories/myWheatCalories;
    myWheatArea = (((myWheatKilograms)/myWheatYield)*1000.)/10000.;
    myWheatFallowArea = myWheatArea * myWheatFallowRatio;
    myWheatTotalArea = myWheatArea + myWheatFallowArea;
    writeMessage("Wheat area: " + QString::number(myWheatArea).toLocal8Bit());
    writeMessage("Wheat fallow area: " + QString::number(myWheatFallowArea).toLocal8Bit());
    writeMessage("Wheat total area: " + QString::number(myWheatTotalArea).toLocal8Bit());

    writePlantCellValue(1,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myWheatPercent/100.)*100.));
    writePlantCellValue(1,1,QString::number(myWheatKilograms));
    writePlantCellValue(1,2,QString::number(myTotalWheatCalories/1000.));
    writePlantCellValue(1,3,QString::number(myWheatArea));
    writePlantCellValue(1,4,QString::number(myWheatFallowArea));
    writePlantCellValue(1,5,QString::number(myWheatTotalArea));
  }
  else
  {
    myWheatTotalArea = 0;
    myWheatFallowArea = 0;
    myWheatKilograms = 0;
  }

  if (barley->isChecked() )
  {
    int myBarleyPercentage = barley_percent->value();     // PERCENTAGE OF BARLEY in plant portion of diet
    int myBarleyYield = barley_yield->value();      // expected average BARLEY YIELD
    int myBarleyCaloriese = barleycals->value();      // calories in 1 kg of BARLEY
    float myBarleyFallowRatio = barley_fallow_ratio->value();  // FALLOW RATIO for BARLEY
    float myBarleyArea;  // barley area 
    myTotalBarleyCalories = tamemyPlantCalories*(myBarleyPercentage/100.);
    myBarleyKilograms = myTotalBarleyCalories/myBarleyCaloriese;
    myBarleyArea = (((myBarleyKilograms)/myBarleyYield)*1000.)/10000.;
    myBarleyFallowArea = myBarleyArea * myBarleyFallowRatio;
    myBarleyTotalArea = myBarleyArea + myBarleyFallowArea;
    writeMessage("Barley area: " + QString::number(myBarleyArea).toLocal8Bit());
    writeMessage("Barley fallow area: " + QString::number(myBarleyFallowArea).toLocal8Bit());
    writeMessage("Barley total area: " + QString::number(myBarleyTotalArea).toLocal8Bit());

    writePlantCellValue(2,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myBarleyPercentage/100.)*100.));
    writePlantCellValue(2,1,QString::number(myBarleyKilograms));
    writePlantCellValue(2,2,QString::number(myTotalBarleyCalories/1000.));
    writePlantCellValue(2,3,QString::number(myBarleyArea));
    writePlantCellValue(2,4,QString::number(myBarleyFallowArea));
    writePlantCellValue(2,5,QString::number(myBarleyTotalArea));
  }
  else
  {
    myBarleyTotalArea=0;
    myBarleyFallowArea=0;
    myBarleyKilograms=0;
  }

  if (lentils->isChecked() )
  {
    int myLentilPercentage = lentil_percent->value();     // PERCENTAGE OF LENTIL in plant portion of diet
    int myLentilYield = lentil_yield->value();      // expected average LENTIL YIELD
    int myLentilCalories = lentilcals->value();      // calories in 1 kg of LENTILS
    float myLentilFallowRatio = lentil_fallow_ratio->value();  // FALLOW RATIO for LENTIL
    float myLentilArea;  // wheat area 
    myTotalLentilCalories = tamemyPlantCalories*(myLentilPercentage/100.);
    myLentilKilograms = myTotalLentilCalories/myLentilCalories;
    myLentilArea = (((myLentilKilograms)/myLentilYield)*1000.)/10000.;
    myLentilFallowArea = myLentilArea * myLentilFallowRatio;
    myLentilTotalArea = myLentilArea + myLentilFallowArea;
    writeMessage("Lentil area: " + QString::number(myLentilArea).toLocal8Bit());
    writeMessage("Lentil fallow area: " + QString::number(myLentilFallowArea).toLocal8Bit());
    writeMessage("Lentil total area: " + QString::number(myLentilTotalArea).toLocal8Bit());

    writePlantCellValue(3,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myLentilPercentage/100.)*100.));
    writePlantCellValue(3,1,QString::number(myLentilKilograms));
    writePlantCellValue(3,2,QString::number(myTotalLentilCalories/1000.));
    writePlantCellValue(3,3,QString::number(myLentilArea));
    writePlantCellValue(3,4,QString::number(myLentilFallowArea));
    writePlantCellValue(3,5,QString::number(myLentilTotalArea));
  }
  else
  {
    myLentilTotalArea = 0;
    myLentilFallowArea = 0;
    myLentilKilograms = 0;
  }

  if (olives->isChecked() )
  {
    int myOlivePercentage = olive_percent->value();     // PERCENTAGE OF OLIVE in plant portion of diet
    int oy = olive_yield->value();      // expected average OLIVE YIELD
    int ocal = olivecals->value();      // calories in 1 kg of OLIVES
    float ofr = olive_fallow_ratio->value();  // FALLOW RATIO for OLIVE
    float oa;          // olive area 
    myTotalOliveCalories = tamemyPlantCalories*(myOlivePercentage/100.);
    myOliveKilograms = myTotalOliveCalories/ocal;
    oa = (((myOliveKilograms)/oy)*1000.)/10000.;
    myOliveFallowArea = oa * ofr;
    myOliveTotalArea = oa + myOliveFallowArea;
    writeMessage("olive area: " + QString::number(oa).toLocal8Bit());
    writeMessage("olive fallow area: " + QString::number(myOliveFallowArea).toLocal8Bit());
    writeMessage("olive total area: " + QString::number(myOliveTotalArea).toLocal8Bit());

    writePlantCellValue(4,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myOlivePercentage/100.)*100.));
    writePlantCellValue(4,1,QString::number(myOliveKilograms));
    writePlantCellValue(4,2,QString::number(myTotalOliveCalories/1000.));
    writePlantCellValue(4,3,QString::number(oa));
    writePlantCellValue(4,4,QString::number(myOliveFallowArea));
    writePlantCellValue(4,5,QString::number(myOliveTotalArea));
  }
  else
  {
    myOliveTotalArea = 0;
    myOliveFallowArea = 0;
    myOliveKilograms=0;
  }

  if (grapes->isChecked() )
  {
    int myGrapePercent = grape_percent->value();     // PERCENTAGE OF GRAPE in plant portion of diet
    int gy = grape_yield->value();      // expected average GRAPE YIELD
    int gcal = grapecals->value();      // FALLOW RATIO for GRAPE
    float gfr = grape_fallow_ratio->value();  // calories in 1 kg of GRAPES
    float ga;          // grape area 
    myTotalGrapeCalories = tamemyPlantCalories*(myGrapePercent/100.);
    myGrapeKilograms = myTotalGrapeCalories/gcal;
    ga = (((myGrapeKilograms)/gy)*1000.)/10000.;
    myGrapeFallowArea = ga * gfr;
    myGrapeTotalArea = ga + myGrapeFallowArea;
    writeMessage("grape area: " + QString::number(ga).toLocal8Bit());
    writeMessage("grape fallow area: " + QString::number(myGrapeFallowArea).toLocal8Bit());
    writeMessage("grape total area: " + QString::number(myGrapeTotalArea).toLocal8Bit());

    writePlantCellValue(5,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myGrapePercent/100.)*100.));
    writePlantCellValue(5,1,QString::number(myGrapeKilograms));
    writePlantCellValue(5,2,QString::number(myTotalGrapeCalories/1000.));
    writePlantCellValue(5,3,QString::number(ga));
    writePlantCellValue(5,4,QString::number(myGrapeFallowArea));
    writePlantCellValue(5,5,QString::number(myGrapeTotalArea));
  }
  else
  {
    myGrapeTotalArea = 0;
    myGrapeFallowArea = 0;
    myGrapeKilograms = 0;
  }

  if (sheep->isChecked() )
  {
    writeMessage("sheep is checked.");
    /* fill table
       writePlantCellValue(7,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(wp/100.)*100.));
       writePlantCellValue(7,1,QString::number(myWheatKilograms));
       writePlantCellValue(7,2,QString::number(myTotalWheatCalories/1000.));
       writePlantCellValue(7,4,QString::number(myWheatArea));
       writePlantCellValue(7,5,QString::number(myWheatFallowArea));
       writePlantCellValue(7,6,QString::number(myWheatTotalArea));
       writePlantCellValue(7,7,QString::number(myWheatTotalArea));
       */
  }
  else
  {
  }

  if (goat->isChecked() )
  {
    writeMessage("goat is checked.");
    /* fill table
       writePlantCellValue(8,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myBarleyPercentage/100.)*100.));
       writePlantCellValue(8,1,QString::number(myBarleyKilograms));
       writePlantCellValue(8,2,QString::number(myTotalBarleyCalories/1000.));
       writePlantCellValue(8,4,QString::number(myBarleyArea));
       writePlantCellValue(8,5,QString::number(myBarleyFallowArea));
       writePlantCellValue(8,6,QString::number(myBarleyTotalArea));
       writePlantCellValue(8,7,QString::number(myBarleyTotalArea));
       */
  }
  else
  {
  }

  if (pig->isChecked() )
  {
    writeMessage("pig is checked.");
    /* fill table
       writePlantCellValue(9,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myLentilPercentage/100.)*100.));
       writePlantCellValue(9,1,QString::number(myLentilKilograms));
       writePlantCellValue(9,2,QString::number(myTotalLentilCalories/1000.));
       writePlantCellValue(9,4,QString::number(myLentilArea));
       writePlantCellValue(9,5,QString::number(myLentilFallowArea));
       writePlantCellValue(9,6,QString::number(myLentilTotalArea));
       writePlantCellValue(9,7,QString::number(myLentilTotalArea));
       */
  }
  else
  {
  }

  if (cow->isChecked() )
  {
    writeMessage("cow is checked.");
    /* fill table
       writePlantCellValue(10,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myOlivePercentage/100.)*100.));
       writePlantCellValue(10,1,QString::number(myOliveKilograms));
       writePlantCellValue(10,2,QString::number(myTotalOliveCalories/1000.));
       writePlantCellValue(10,4,QString::number(oa));
       writePlantCellValue(10,5,QString::number(myOliveFallowArea));
       writePlantCellValue(10,6,QString::number(myOliveTotalArea));
       writePlantCellValue(10,7,QString::number(myLentilTotalArea));
       */
  }
  else
  {
    //do nothing
  }

  if (chicken->isChecked() )
  {
    writeMessage("chicken is checked.");
    /* fill table
       writePlantCellValue(11,0,QString::number((myOverallPercentage/100.)*(myTamePlantPercentage/100.)*(myGrapePercent/100.)*100.));
       writePlantCellValue(11,1,QString::number(myGrapeKilograms));
       writePlantCellValue(11,2,QString::number(myTotalGrapeCalories/1000.));
       writePlantCellValue(11,4,QString::number(ga));
       writePlantCellValue(11,5,QString::number(myGrapeFallowArea));
       writePlantCellValue(11,6,QString::number(myGrapeTotalArea));
       writePlantCellValue(11,7,QString::number(myLentilTotalArea));
       */
  }
  else
  {
    //do nothing
  }

  myStandardFallowAreaTotal = (myWheatFallowArea+myBarleyFallowArea+myLentilFallowArea+myOliveFallowArea+myGrapeFallowArea);
  myStandardCropTotalArea = (myWheatTotalArea+myBarleyTotalArea+myLentilTotalArea+myOliveTotalArea+myGrapeTotalArea)-myStandardFallowAreaTotal;
  myStandardTotalArea = myStandardFallowAreaTotal + myStandardCropTotalArea;
  myTotalCalories = myTotalWheatCalories+myTotalBarleyCalories+myTotalLentilCalories+myTotalOliveCalories+myTotalGrapeCalories;

  /* Animals
     writeMessage("----------==========   RESULTS   ==========----------");
     writeMessage(" * * *   WHEAT   * * *");
     writeMessage("Total calories supplied by wheat (kcal) : " + QString::number(myTotalWheatCalories/1000.).toLocal8Bit());
     writeMessage("kg of wheat to produce this many calories is: " + QString::number(myWheatKilograms).toLocal8Bit());

     writeMessage(" * * *   BARLEY   * * *");
     writeMessage("Total calories supplied by barley (kcal): " + QString::number(myTotalBarleyCalories/1000.).toLocal8Bit());
     writeMessage("kg of barley to produce this many calories is: " + QString::number(myBarleyKilograms).toLocal8Bit());

     writeMessage(" * * *   LENTILS   * * *");
     writeMessage("Total calories supplied by lentils (kcal): " + QString::number(myTotalLentilCalories/1000.).toLocal8Bit());
     writeMessage("kg of lentil to produce this many calories is: " + QString::number(myLentilKilograms).toLocal8Bit());

     writeMessage(" * * *   OLIVES   * * *");
     writeMessage("Total calories supplied by olives m(kcal): " + QString::number(myTotalOliveCalories/1000.).toLocal8Bit());
     writeMessage("kg of olive to produce this many calories is: " + QString::number(myOliveKilograms).toLocal8Bit());

     writeMessage(" * * *   GRAPES   * * *");
     writeMessage("Total calories supplied by grapes (kcal): " + QString::number(myTotalGrapeCalories/1000.).toLocal8Bit());
     writeMessage("kg of grape to produce this many calories is: " + QString::number(myGrapeKilograms).toLocal8Bit());

     writeMessage(" * * *   LAND REQUIREMENTS   * * *");
     writeMessage("Total Sown Land required (ha): " + QString::number(myStandardCropTotalArea).toLocal8Bit());
     writeMessage("Total area of fallow land (ha): " + QString::number(myStandardFallowAreaTotal).toLocal8Bit());
     writeMessage("Total area required for crops (ha): " + QString::number(myStandardTotalArea).toLocal8Bit());
     */

}

void LaMainForm::on_run_button_clicked() 
{
  writeMessage("running...");

  doBaseCalculations();
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

    int myAnimalCount = 0;
    int myCommonAnimalTarget = 0;
    int myFallowGrazingAnimalsCount = 0;
    // these will be passed here from base calculations
    float mySheepTarget = 0;
    float myGoatTarget = 0;
    float myPigTarget = 0;
    float myCowTargetArea = 0;
    float myChickenTarget = 0;
    float myAnimalTarget = 0;
    float myCropTarget = 0;
    float myWheatTarget = 0;
    float myBarleyTarget = 0;
    float myLentilTarget = 0;
    float myOliveTarget = 0;
    float myGrapeTarget = 0;
    float myStandardFallowAreaTotal = 0;

    if (sheep->isChecked())
    {
      if (sheepgrazefallow->isChecked())
      {
        myAnimalCount++;
      }
      if (!sheepraster->isChecked())
      {
        myCommonAnimalTarget=myCommonAnimalTarget+mySheepTarget;
        mySheepTarget=0;
        myFallowGrazingAnimalsCount++;
      }
    }

    if (goat->isChecked())
    {
      if (goatgrazefallow->isChecked())     myAnimalCount++;
      if (!goatraster->isChecked())
      {
        myCommonAnimalTarget=myCommonAnimalTarget+myGoatTarget;
        myGoatTarget=0;
        myFallowGrazingAnimalsCount++;
      }
    }

    if (pig->isChecked())
    {
      if (piggrazefallow->isChecked())      myAnimalCount++;
      if (!pigraster->isChecked())
      {
        myCommonAnimalTarget=myCommonAnimalTarget+myPigTarget;
        myPigTarget=0;
        myFallowGrazingAnimalsCount++;
      }
    }

    if (cow->isChecked())
    {
      if (cowgrazefallow->isChecked())      myAnimalCount++;
      if (!cowraster->isChecked())
      {
        myCommonAnimalTarget=myCommonAnimalTarget+myCowTargetArea;
        myCowTargetArea=0;
        myFallowGrazingAnimalsCount++;
      }
    }
    /*
       if (chicken->isChecked())
       {
       if (chickengrazefallow->isChecked())  myAnimalCount++;
       if (!chickenraster->isChecked())
       {
       myCommonAnimalTarget=myCommonAnimalTarget+myChickenTarget;
       myChickenTarget=0;
       myFallowGrazingAnimalsCount++;
       }
       }
       */

    float myAnimalFallowQuota = (myStandardFallowAreaTotal) / (myFallowGrazingAnimalsCount);
    float extra_fallow = 0;

    // in the following, we determine the target areas for each animal
    // as well as create the cost surfaces for each as required

    if (myFallowGrazingAnimalsCount > 0)
    {
      myCommonAnimalTarget = myCommonAnimalTarget - (myFallowGrazingAnimalsCount *  myAnimalFallowQuota);
      if (myCommonAnimalTarget < 0)
      {
        extra_fallow = (myCommonAnimalTarget * (-1.));
        myCommonAnimalTarget = 0;
      }
      //create animalcost raster (cost surface)
      // for euclidean, distance from point (the coordinates of the site)
      // for walk time, r.walk with 18000 seconds as max cost
      // for path dist, use _______ with 15km as max cost
    }
    else
    {
      myCommonAnimalTarget=0;
    }

    // note.  this can all be replaced with if (foo_target > 0) foo_target=foo_target - myAnimalFallowQuota;
    //        I did like this to show logic more clearly (???)

    if (sheep->isChecked())
    {
      if (sheepraster->isChecked())
      {
        if (sheepgrazefallow->isChecked())
        {
          mySheepTarget = mySheepTarget - (myAnimalFallowQuota + extra_fallow);
          if (mySheepTarget < 0)
          {
            extra_fallow = (mySheepTarget * (-1.));
            mySheepTarget = 0;
          }
        }
      }
    }

    if (goat->isChecked())
    {
      if (goatraster->isChecked())
      {
        if (goatgrazefallow->isChecked())
        {
          myGoatTarget = myGoatTarget - (myAnimalFallowQuota + extra_fallow);
          if (myGoatTarget < 0)
          {
            extra_fallow = (myGoatTarget * (-1.));
            myGoatTarget = 0;
          }
        }
      }
    }

    if (pig->isChecked())
    {
      if (pigraster->isChecked())
      {
        if (piggrazefallow->isChecked())
        {
          myPigTarget = myPigTarget - (myAnimalFallowQuota + extra_fallow);
          if (myPigTarget < 0)
          {
            extra_fallow = (myPigTarget * (-1.));
            myPigTarget = 0;
          }
        }
      }
    }

    if (cow->isChecked())
    {
      if (cowraster->isChecked())
      {
        if (cowgrazefallow->isChecked())
        {
          myCowTargetArea = myCowTargetArea - (myAnimalFallowQuota + extra_fallow);
          if (myCowTargetArea < 0)
          {
            extra_fallow = (myCowTargetArea * (-1.));
            myCowTargetArea = 0;
          }
        }
      }
    }

    /*
       if (chicken->isChecked())
       {
       if (chickenraster->isChecked())
       {
       if (chickengrazefallow->isChecked())
       {
       myChickenTarget = myChickenTarget - (myAnimalFallowQuota + extra_fallow);
       if (myChickenTarget < 0)
       {
       extra_fallow = (myChickenTarget * (-1.));
       myChickenTarget = 0;
       }
       }
       }
       }
       */

    float myTotalAreaRequired = myCropTarget + myAnimalTarget + myWheatTarget + myBarleyTarget
      + myLentilTarget + myOliveTarget + myGrapeTarget + mySheepTarget + myGoatTarget
      + myPigTarget + myCowTargetArea;
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
