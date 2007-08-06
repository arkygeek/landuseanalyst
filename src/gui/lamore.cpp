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

#include "lamore.h"
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

  LaMore::LaMore(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

  connect(pbnInsert, SIGNAL(clicked()),
      this, SLOT(on_pbnInsert_clicked()));

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
  mRowCount = 0;
}

LaMore::~LaMore()
{
  writeSettings();
}

void LaMore::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaMore::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaMore::resizeEvent ( QResizeEvent * theEvent )
{
  tblAnimals->setColumnWidth(0,0);
  tblAnimals->setColumnWidth(1,tblAnimals->width());
  tblAnimals->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaMore::on_pbnInsert_clicked()
{
  // add an animal to the table
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(QString());
  if (rbManual->isChecked())
  {
    // add item to table from manual inputs
    mRowCount++;
    tblAnimals->insertRow(mRowCount);
    int myCurrentRow = static_cast<int> (mRowCount);
    mypNameItem->setText(leAnimal->text());
    tblAnimals->setItem(myCurrentRow, 0, mypNameItem);
  }
  else if (rbAuto->isChecked())
  {
    // add item to table from pre-defined animals
    mRowCount++;
    tblAnimals->insertRow(mRowCount);
  }
  else return;
  return;
}

void LaMore::refreshTable()
{
  //
}

bool LaMore::setComboToDefault(QComboBox * thepCombo, QString theDefault)
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
