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

#include "lagrassprocess.h"
#include "lautils.h"
#include "lacropparameter.h"
#include "laanimalparameter.h"
#include "lamainform.h"
#include "lacrop.h"
#include "laanimal.h"

#include <QString>
#include <QMessageBox>
#include <QLabel>
#include <QPixmap>
#include <QSettings>
#include <QtDebug>

  LaGrassProcess::LaGrassProcess(QPair<QMap<QString, int>, QMap<QString, int> > & thePair, QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

  mAnimalAreaTargetsMap = thePair.first;
  mCropAreaTargetsMap = thePair.second;

  lblGraphic->setScaledContents(true);
  lblPreview->setScaledContents(true);
  pbarTarget->setRange(0,100);
  pbarTarget->setValue(0);
  pbarOverall->setRange(0,100);
  pbarOverall->setValue(0);
  lblCurrentArea->setText(0);
  lblAreaTarget->setText(0);
  qDebug() << "thePair" << thePair;
}

LaGrassProcess::~LaGrassProcess()
{
  writeSettings();
}

void LaGrassProcess::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaGrassProcess::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaGrassProcess::on_pbnStart_clicked()
{
  // so here we go.  I have the maps and their targets, so i
  // think all i need to do is iterate through them one at a time!

  QMapIterator<QString, int > myCropIterator(mCropAreaTargetsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    LaCrop myCrop = LaUtils::getCrop(myCropIterator.key());
    QString myName = myCrop.name();
    LaMainForm myMainForm;
    QString myCropParameterGuid = myMainForm.getMatchingCropParameterGuid(myCropIterator.key());
    LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
    QString myCropRasterFile = myCropParameter.rasterName();
    qDebug() << "MyName" << myName << "needs area of: " << myCropIterator.value();
    qDebug() << "The Raster is: " << myCropRasterFile;
    lblAreaTarget->setText("Target:\n" + QString::number(myCropIterator.value()));
    lblGraphic->setPixmap(myCrop.imageFile());
    // go analyse the stuff...
  }

  QMapIterator<QString, int > myAnimalIterator(mAnimalAreaTargetsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalIterator.key());
    QString myName = myAnimal.name();
    LaMainForm myMainForm;
    QString myAnimalParameterGuid = myMainForm.getMatchingAnimalParameterGuid(myAnimalIterator.key());
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    QString myAnimalRasterFile = myAnimalParameter.rasterName();
    qDebug() << "MyName" << myName <<"needs area of: " << myAnimalIterator.value();
    qDebug() << "The Raster is: " << myAnimalRasterFile;
    lblAreaTarget->setText("Target:\n" + QString::number(myAnimalIterator.value()));
    lblGraphic->setPixmap(myAnimal.imageFile());
    // go analyse the stuff...
    //
  }
}

void LaGrassProcess::setPbarTargetRange(int theTarget)
{
  pbarTarget->reset();
  pbarTarget->setRange(0,theTarget);
  pbarTarget->setValue(0);
  lblAreaTarget->setText("Target:\n" + QString::number(theTarget));
}

void LaGrassProcess::setPbarOverallRange(int theOverall)
{
  pbarOverall->reset();
  pbarOverall->setRange(0,theOverall);
  pbarOverall->setValue(0);
}

void LaGrassProcess::on_pbnAbort_clicked()
{
  // abort the grass analysis
}

void LaGrassProcess::updateCurrentProgress(int theArea)
{
  pbarTarget->setValue(theArea);
  lblCurrentArea->setText(QString::number(theArea));
}

void LaGrassProcess::updateOverallProgress(int theStep)
{
  pbarOverall->setValue(theStep);
}

void LaGrassProcess::writeGrassMessage(QString theGrassMessage)
{
  tbGrass->append(theGrassMessage);
}

void LaGrassProcess::updatePreview(QString thePreviewFile)
{
  lblPreview->setPixmap(thePreviewFile);
}

void LaGrassProcess::updateGraphic(QString theGraphicFile)
{
  lblGraphic->setPixmap(theGraphicFile);
}

void LaGrassProcess::toggleBusyProgressBar(bool theStatus)
{
  switch (theStatus)
  {
    case true:  // turn it on
                // set the progress bar to move (min,max = 0,0)
                pbarBusy->setRange(0,0);
                break;
    case false: // shut it off
                // set the progress bar to not move (min,max = 0,1)
                pbarBusy->setRange(0,1);
                break;
  }
}
