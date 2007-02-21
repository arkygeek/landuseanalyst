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
#include "laplantmain.h"
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

LaPlantMain::LaPlantMain(QWidget* parent, Qt::WFlags fl)
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

LaPlantMain::~LaPlantMain()
{
  writeSettings();
}

void LaPlantMain::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaPlantMain::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaPlantMain::on_pushButtonLoad_clicked()
{
  mPlant.fromXmlFile("/tmp/plant.xml");
}

//void LaPlantMain::on_pushButtonSave_clicked()
//{
  // if all fields have been completed,
  // save contents of all fields to disk,
  // and return info to lamainform.
  // If the name field is missing,
  // prompt user for name.  File might
  // get stored as cropname.lac
//}
void LaPlantMain::on_pushButtonSave_clicked()
{
  mPlant.setName(lineEditPlantName->text());
  mPlant.setCropYield(spinBoxPlantYield->value());
  mPlant.setCropCalories(spinBoxPlantCalories->value());
  mPlant.setFodderProduction(spinBoxFodderProduction->value());
  mPlant.setFodderCalories(spinBoxFodderCalories->value());
  mPlant.setYieldUnits(comboBoxYieldUnits->currentIndex());
  mPlant.toXmlFile( LaUtils::userPlantProfilesDirPath() + 
      QDir::separator() + mPlant.name() + ".xml");

}
