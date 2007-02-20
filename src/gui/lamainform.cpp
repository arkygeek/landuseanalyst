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
#include "laanimalmain.h"
#include "laplantmain.h"
//qt includes
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
  connect(pushButtonExit, SIGNAL(clicked()), qApp, SLOT(quit()));

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

void LaMainForm::on_horizontalSliderMeat_valueChanged(int theValue)
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  labelMeatWildPercent->setText(myMinString);
  labelMeatTamePercent->setText(myMaxString);
}

void LaMainForm::on_horizontalSliderDiet_valueChanged(int theValue)
{
  QString myMinString = QString::number(theValue);
  QString myMaxString = QString::number(100-theValue);
  labelMeatPercent->setText(myMinString);
  labelPlantPercent->setText(myMaxString);
}

void LaMainForm::on_horizontalSliderPlant_valueChanged(int theValue)
{
  QString myMinString = QString::number(100-theValue);
  QString myMaxString = QString::number(theValue);
  labelPlantWildPercent->setText(myMinString);
  labelPlantTamePercent->setText(myMaxString);
}

void LaMainForm::on_pbnNewAnimal_clicked()
{
  LaAnimalMain myAnimalForm;
  myAnimalForm.exec();
}

void LaMainForm::on_pbnNewCrop_clicked()
{
  LaPlantMain myCropForm;
  myCropForm.exec();
}


void LaMainForm::on_pushButtonRun_clicked()
{
  //  implement me!
}

void LaMainForm::on_pushButtonLoad_clicked()
{
  //  implement me!
}

void LaMainForm::on_pushButtonSave_clicked()
{
  //  implement me!
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

void LaMainForm::on_pushButtonDietBreakdown_clicked()
{
  int myOverallPercentage = (100-(horizontalSliderDiet->value()));
  int myTamePlantPercentage = horizontalSliderPlant->value();
  int myDietPercentMeat = horizontalSliderDiet->value();
  int myDietPercentTameMeat = horizontalSliderMeat->value();
  int myCalories = spinBoxDailyCalories->value();
  int myPopulation = spinBoxPopulation->value();

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
  textBrowserResultsLeft->append(theText);
}

void LaMainForm::writeDiet(QString theText) 
{
  breakdownDisplay->append(theText);
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

