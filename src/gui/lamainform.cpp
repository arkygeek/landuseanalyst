/***************************************************************************
 *   Copyright (C) 2007 by Tim Sutton   *
 *   tim@linfiniti.com   *
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
#include <QSettings>
  LaMainForm::LaMainForm(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
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

void LaMainForm::on_calculate_button_clicked()
{
	qDebug("QGIS Rocks");
}

void LaMainForm::on_pigview_clicked()
{
	qDebug("Jason Rocks");
/*
	int myPigSnoutLength = spinSnoutLength->value();
pigpercent
piglittersize
pigweight
pigfodderuse
pigfodderamount
pigfoddercrop
pigfoddertime
piggrazefallow
pigraster
dietslider   for overall MEAT value
meatslider   for tame percentage
dailycalories
*/

//float myPigSnoutLength = spinSnoutLength->value();


}

void LaMainForm::on_meatslider_valueChanged(int theValue)
{
qDebug("Some plonker moved the meat slider! New value:" + QString::number(theValue).toLocal8Bit());
	QString myMinString = QString::number(100-theValue);
	QString myMaxString = QString::number(theValue);
	meatwildpercent->setText(myMinString);
	meattamepercent->setText(myMaxString);
}

void LaMainForm::on_dietslider_valueChanged(int theValue)
{
qDebug("Some plonker moved the diet slider! New value:" + QString::number(theValue).toLocal8Bit());
	QString myMinString = QString::number(theValue);
	QString myMaxString = QString::number(100-theValue);
	meatpercent->setText(myMinString);
	plantpercent->setText(myMaxString);
}

void LaMainForm::on_plantslider_valueChanged(int theValue)
{
qDebug("Some plonker moved the plant slider! New value:" + QString::number(theValue).toLocal8Bit());
	QString myMinString = QString::number(100-theValue);
	QString myMaxString = QString::number(theValue);
	plantwildpercent->setText(myMinString);
	planttamepercent->setText(myMaxString);
}
