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
  QSize size = mySettings.value("mainwindow/size", QSize(200, 400)).toSize();
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
  int myOverallProgress = 1;
  int myNumberOfSearches = mCropAreaTargetsMap.size() + mAnimalAreaTargetsMap.size();
  setPbarOverallRange(myNumberOfSearches);

  QMapIterator<QString, int > myCropIterator(mCropAreaTargetsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    LaCrop myCrop = LaUtils::getCrop(myCropIterator.key());
    lblGraphic->setPixmap(myCrop.imageFile());
    lblGraphic->repaint();
    lblAreaTarget->setText("Target:\n" + QString::number(myCropIterator.value()));
    lblAreaTarget->repaint();
    QString myName = myCrop.name();
    LaMainForm myMainForm;
    QString myCropParameterGuid = myMainForm.getMatchingCropParameterGuid(myCropIterator.key());
    LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
    QString myCropRasterFile = myCropParameter.rasterName();
    qDebug() << "MyName" << myName << "needs area of: " << myCropIterator.value();
    qDebug() << "The Raster is: " << myCropRasterFile;

    // go analyse the stuff...
    updateOverallProgress(myOverallProgress);
    myOverallProgress++;
  }

  QMapIterator<QString, int > myAnimalIterator(mAnimalAreaTargetsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalIterator.key());
    lblGraphic->setPixmap(myAnimal.imageFile());
    lblGraphic->repaint();
    lblAreaTarget->setText("Target:\n" + QString::number(myAnimalIterator.value()));
    lblAreaTarget->repaint();
    QString myName = myAnimal.name();
    LaMainForm myMainForm;
    QString myAnimalParameterGuid = myMainForm.getMatchingAnimalParameterGuid(myAnimalIterator.key());
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    QString myAnimalRasterFile = myAnimalParameter.rasterName();
    qDebug() << myName <<" needs area of: " << myAnimalIterator.value();
    qDebug() << "The Raster is: " << myAnimalRasterFile;


    // go analyse the stuff...
    updateOverallProgress(myOverallProgress);
    myOverallProgress++;
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

void LaGrassProcess::analyseModel(QString theRasterMask, int theAreaTarget)
{

  // get the area targets


    ///////////////////////
   // Make Cost Surface //
  ///////////////////////

  // r.mapcalc "TimeOnlyFrictionMap=if(isnull(DEM), null(), 1)"
  // r.walk max_cost=20000 elevation=dem_patched_filled@PERMANENT friction=theFrictionMap output=rwalkResultsSlopeMax20kFMap coordinate=744800,3611100 percent_memory=100 nseg=4 walk_coeff=0.72,6.0,1.9998,-1.9998 lambda=0 slope_factor=-0.2125 -k



   // find the land!
   int myFirst = 0;
   int myLast=18000;
   int myAreaTarget = 500; // change this to real value
   LandFound mySearchStatus = NotEnough;
   int myCurrentlyContainedArea = 0;
   int myPrecision = 5; // change this to real value

   while (myFirst <= myLast)
  {
    int myMid = (myFirst + myLast) / 2;  // compute mid point.
    // reclass with 1 to midpoint and null beyond and then check results
    //    echo "0 thru $step = 1" | r.reclass input=$cost output=cost.reclass --o
    //    r.stats -n -a fs=- input=cost.reclass > $TMP1

    // find out if the contained area is within acceptable range
    mySearchStatus = getSearchStatus(myCurrentlyContainedArea, myAreaTarget, myPrecision);

    switch (mySearchStatus)
    {
      case NotEnough:
            myFirst = myMid + 1;  // repeat search in top half.
            break;;
      case TooMuch:
            myLast = myMid - 1; // repeat search in bottom half.
            break;
      case FoundTarget:
            // found it. break out of loop /////
            myFirst = myLast+1;
            break;
    }

  }
}

LandFound LaGrassProcess::getSearchStatus(int theCurrentlyContainedArea, int theAreaTarget, int thePrecision)
{
  LandFound myStatus;
  int myPrecision=5;  //get the real value for precision
  float myAcceptableRange=(theAreaTarget*myPrecision*0.01)/2.0;
  float myMinimumAcceptable = theAreaTarget - myAcceptableRange;
  float myMaximumAcceptable = theAreaTarget + myAcceptableRange;

  if (theCurrentlyContainedArea >= myMinimumAcceptable)
    {      myStatus = (theCurrentlyContainedArea <= myMaximumAcceptable) ? FoundTarget : TooMuch;    }
  else
    {
      myStatus = NotEnough;
    }

  return myStatus;
}
