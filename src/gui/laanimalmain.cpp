/***************************************************************************
 *   Copyright (C) 2007 by: Jason Jorgenson   arkygeek@gmail.com           *
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
#include "laanimalmain.h"
#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QString>

  LaAnimalMain::LaAnimalMain(QWidget* parent, Qt::WFlags fl)
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
}

LaAnimalMain::~LaAnimalMain()
{
  writeSettings();
}

void LaAnimalMain::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaAnimalMain::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaAnimalMain::on_pushButtonLoad_clicked()
{
  //
  mAnimal.fromXmlFile("/tmp/animal.xml");
}

QString LaAnimalMain::on_pushButtonSave_clicked()
{
  mAnimal.setName(lineEditAnimalName->text());
  mAnimal.setUsableMeat(spinBoxUsableMeatPercent->value());
  mAnimal.setKillWeight(spinBoxKillWeight->value());
  mAnimal.setGrowTime(spinBoxGrowTime->value());
  mAnimal.setDeathRate(spinBoxDeathRate->value());
  mAnimal.setGestating(spinBoxCaloriesForGestating->value());
  mAnimal.setLactating(spinBoxCaloriesForLactating->value());
  mAnimal.setJuvenile(spinBoxCaloriesForJuvenile->value());
  mAnimal.setLifeExpectancy(spinBoxLifeExpectancy->value());
  mAnimal.setBreedingExpectancy(spinBoxBreedingLife->value());
  mAnimal.setYoungPerBirth(spinBoxYoungPerBirth->value());
  mAnimal.setWeaningAge(spinBoxWeaningAge->value());
  mAnimal.setGestationTime(spinBoxGestationTime->value());
  mAnimal.setEstrousCycle(spinBoxEstrousCycleTime->value());
  mAnimal.toXmlFile("/tmp/animal" + mAnimal.name() + ".xml");
}

