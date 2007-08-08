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

#include "laassemblageconversion.h"
#include "la.h"
#include "lautils.h"
#include "laanimal.h"
#include "lafoodsource.h"
#include "lamainform.h"

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
#include <QIcon>
#include <QtDebug>
#include <QPair>

  LaAssemblageConversion::LaAssemblageConversion(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

//  connect(pbnInsert, SIGNAL(clicked()),
 //     this, SLOT(on_pbnInsert_clicked()));

  tblAnimals->setColumnCount(5);
  //populate the animals combo
  LaUtils::AnimalMap myAnimalsMap;
  myAnimalsMap = LaUtils::getAvailableAnimals();
  QMapIterator<QString, LaAnimal> myIterator(myAnimalsMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaAnimal myAnimal = myIterator.value();
    QString myGuid = myAnimal.guid();
    QString myName = myAnimal.name();
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    cboAnimal->addItem(myName,myGuid);
  }
}

LaAssemblageConversion::~LaAssemblageConversion()
{
  writeSettings();
}

void LaAssemblageConversion::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaAssemblageConversion::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaAssemblageConversion::resizeEvent ( QResizeEvent * theEvent )
{
  //tblAnimals->setColumnWidth(0,0);
  //tblAnimals->setColumnWidth(1,tblAnimals->width());
  tblAnimals->horizontalHeader()->setResizeMode(0,QHeaderView::Stretch);
}

void LaAssemblageConversion::on_pbnInsert_clicked()
{
  // add an animal to the table
  qDebug() << "pbnInsert";
  int myRowCount = tblAnimals->rowCount();

  qDebug() << "rowCount: " << myRowCount;
  if (rbManual->isChecked() == true)
  {
    qDebug() << "manual is checked";
    // add item to table from manual inputs
    tblAnimals->insertRow(myRowCount);

    QString myName = leAnimal->text();
    int myUsableMeat = sbUsableMeat->value();
    int myCalsPerKg = sbCalsPerKg->value();
    float myNumber = dsbNumber->value();

    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myName);
    tblAnimals->setItem(myRowCount, 0, mypNameItem);
    qDebug() << "myName = " << myName;

    QTableWidgetItem *mypUsableMeatItem= new QTableWidgetItem(QString::number(myUsableMeat));
    tblAnimals->setItem(myRowCount, 2, mypUsableMeatItem);

    QTableWidgetItem *mypCalsPerKgItem= new QTableWidgetItem(QString::number(myCalsPerKg));
    tblAnimals->setItem(myRowCount, 3, mypCalsPerKgItem);

    QTableWidgetItem *mypNumber= new QTableWidgetItem(QString::number(myNumber));
    tblAnimals->setItem(myRowCount, 1, mypNumber);
    //tblAnimals->insertRow(myRowCount);
  }
  else if (rbAuto->isChecked() == true)
  {
    // add item to table from pre-defined animals
    qDebug() << "auto is checked";
    LaAnimal myAnimal = LaUtils::getAnimal( cboAnimal->itemData( cboAnimal->currentIndex(), Qt::UserRole).toString());
    tblAnimals->insertRow(myRowCount);

    QString myName = myAnimal.name();
    int myUsableMeatPercent = myAnimal.usableMeat();
    int myKillWeight = myAnimal.killWeight();
    int myCalsPerKg = myAnimal.meatFoodValue();
    float myUsableMeat = (0.01*myUsableMeatPercent) * myKillWeight;
    float myNumber = dsbNumber->value();

    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myName);
    tblAnimals->setItem(myRowCount, 0, mypNameItem);
    qDebug() << "myName = " << myName;

    QTableWidgetItem *mypUsableMeatItem= new QTableWidgetItem(QString::number(myUsableMeat));
    tblAnimals->setItem(myRowCount, 2, mypUsableMeatItem);

    QTableWidgetItem *mypCalsPerKgItem= new QTableWidgetItem(QString::number(myCalsPerKg));
    tblAnimals->setItem(myRowCount, 3, mypCalsPerKgItem);


    QTableWidgetItem *mypNumber= new QTableWidgetItem(QString::number(myNumber));
    tblAnimals->setItem(myRowCount, 1, mypNumber);
  }
  else
    {
      qDebug() << "nothing selected, just returning";
      return;
    }
  return;
}

void LaAssemblageConversion::on_pbnCalculate_clicked()
{
  // calculate the percent of diet based on entries in tblAnimals

  // iterate through the table and get a sum of the adjusted meat value
  // which is the NISP * weight of usable meat * calories per kg
  float myAdjustmentSum = 0.0;
  float myContributionToDiet = 0.0;
  // iterate through table
  for (int myCurrentRow=0; myCurrentRow < tblAnimals->rowCount(); myCurrentRow++)
  {
    //QTableWidgetItem * mypNameWidget        = tblAnimals->item(myCurrentRow,0);
    QTableWidgetItem * mypNumberWidget      = tblAnimals->item(myCurrentRow,1);
    QTableWidgetItem * mypUsableMeatWidget  = tblAnimals->item(myCurrentRow,2);
    QTableWidgetItem * mypCalsPerKgWidget   = tblAnimals->item(myCurrentRow,3);

    myAdjustmentSum += (mypNumberWidget->text().toFloat())
                     * (mypUsableMeatWidget->text().toInt())
                     * (mypCalsPerKgWidget->text().toInt())
                     * 0.001; // to keep figures within limits
    qDebug() << "row: " << myCurrentRow <<" Adjustment sum: " << myAdjustmentSum;
  }
  // iterate table again, adding percentage contribution to diet
  float myDebugSumCheck = 0.0;
  for (int myCurrentRow1=0; myCurrentRow1 < tblAnimals->rowCount(); myCurrentRow1++)
  {
    QTableWidgetItem * mypNumberWidget      = tblAnimals->item(myCurrentRow1,1);
    QTableWidgetItem * mypUsableMeatWidget  = tblAnimals->item(myCurrentRow1,2);
    QTableWidgetItem * mypCalsPerKgWidget   = tblAnimals->item(myCurrentRow1,3);

    myContributionToDiet = (((mypNumberWidget->text().toFloat())
                     * (mypUsableMeatWidget->text().toInt())
                     * (mypCalsPerKgWidget->text().toInt())
                     * 0.001)
                     / myAdjustmentSum)
                     * 100.0; // to make it percent (ie. 10.56% instead of 0.1056)
   myDebugSumCheck += myContributionToDiet;
    QTableWidgetItem *mypContributionToDiet= new QTableWidgetItem(QString::number(myContributionToDiet));
    tblAnimals->setItem(myCurrentRow1, 4, mypContributionToDiet);
    qDebug() << "debug sum check: " << myDebugSumCheck;
  }
  qDebug() << "Final debug sum (should be 100) : " << myDebugSumCheck;


}

void LaAssemblageConversion::on_pbnClearTable_clicked()
{
  tblAnimals->clear();
}

void LaAssemblageConversion::refreshTable()
{
  //
}

bool LaAssemblageConversion::setComboToDefault(QComboBox * thepCombo, QString theDefault)
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
