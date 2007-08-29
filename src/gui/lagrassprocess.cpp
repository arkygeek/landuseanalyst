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
#include "lagrass.h"

#include <QString>
#include <QMessageBox>
#include <QLabel>
#include <QPixmap>
#include <QSettings>
#include <QtDebug>

  LaGrassProcess::LaGrassProcess(QString theDEM, QPair<int, int> theCoordinates, QPair<QMap<QString, int>, QMap<QString, int> > & thePairOfAreaTargetMaps, QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

  mAnimalAreaTargetsMap = thePairOfAreaTargetMaps.first;
  mCropAreaTargetsMap = thePairOfAreaTargetMaps.second;
  mDEM = theDEM;
  mCoordinates = theCoordinates;
  lblGraphic->setScaledContents(true);
  lblPreview->setScaledContents(true);
  pbarTarget->setRange(0,100);
  pbarTarget->setValue(0);
  pbarOverall->setRange(0,100);
  pbarOverall->setValue(0);
  lblCurrentArea->setText("0");
  lblAreaTarget->setText(0);
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
  toggleBusyProgressBar(true);
  int myOverallProgress = 1;
  // need to change the next line to iterate through both maps and check for common land use
  LaMainForm myMainForm;
  QMapIterator<QString, int > myCropCounter(mCropAreaTargetsMap);
  while (myCropCounter.hasNext())
  {
    myCropCounter.next();
    if (myCropCounter.key() != "CommonTarget")
    {
      // check for use of common targets
      // if it does not use common target then add to count
      QString myCropGuid = myCropCounter.key();
      QString myCropParameterGuid = myMainForm.getMatchingCropParameterGuid(myCropGuid);
      LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
      bool myCommonLandUsed = myCropParameter.useCommonLand();
      if (myCommonLandUsed)
      {
        qDebug() << "removing from area map: "  << myCropGuid;
        mCropAreaTargetsMap.remove(myCropGuid);
      }
    }
  }
  QMapIterator<QString, int > myAnimalCounter(mAnimalAreaTargetsMap);
  while (myAnimalCounter.hasNext())
  {
    myAnimalCounter.next();
    if (myAnimalCounter.key() != "CommonTarget")
    {
      // check for use of common targets
      // if it does not use common target then add to count
      QString myAnimalGuid = myAnimalCounter.key();
      QString myAnimalParameterGuid = myMainForm.getMatchingAnimalParameterGuid(myAnimalGuid);
      LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
      bool myCommonLandUsed = myAnimalParameter.useCommonGrazingLand();
      if (myCommonLandUsed)
      {
        qDebug() << "removing from area map: "  << myAnimalGuid;
        mAnimalAreaTargetsMap.remove(myAnimalGuid);
      }
    }
  }


  int myNumberOfSearches = mCropAreaTargetsMap.size() + mAnimalAreaTargetsMap.size();
  setPbarOverallRange(myNumberOfSearches);

  // create cost surface maps

  LaGrass myGrass;
  //int myEasting = mCoordinates.first;
  //int myNorthing = mCoordinates.second;
  //QString myDEM = mDEM;
  // Make Cost Surface: bool LaGrass::makeWalkCost(int theX, int theY)
  tbGrass->setText("Creating Cost Surface Raster...");
  tbGrass->repaint();
  //myGrass.makeWalkCost(myEasting, myNorthing, mDEM);
  tbGrass->append("Cost Surface Generation complete.");
  tbGrass->repaint();

  QMapIterator<QString, int > myCropIterator(mCropAreaTargetsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    if (myCropIterator.key() != "CommonTarget")
    {
      LaCrop myCrop = LaUtils::getCrop(myCropIterator.key());

      // set the images and area target label
        lblGraphic->setPixmap(myCrop.imageFile());
        lblGraphic->repaint();
        //lblPreview->setPixmap(convertedRasterFile);
        //lblPreview->repaint();
        lblAreaTarget->setText("Target:\n" + QString::number(myCropIterator.value()));
        lblAreaTarget->repaint();

      int myAreaTarget = myCropIterator.value();
      QString myName = myCrop.name();

      LaMainForm myMainForm;
      QString myCropParameterGuid = myMainForm.getMatchingCropParameterGuid(myCropIterator.key());

      LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
      QString myCropRasterFile = myCropParameter.rasterName();

      setPbarTargetRange(17);
      //for (int i=0; i<18; i++)
      //{
      //  pbarTarget->setValue(i);
      //}
      // go analyse the stuff...

      analyseModel(myCropRasterFile, myAreaTarget);
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
    }
    else
    {
      //do stuff for commonTarget
        QString myCommonPixMap = ":/commonTarget.png";
        lblGraphic->setPixmap(myCommonPixMap);
        lblGraphic->repaint();
        lblAreaTarget->setText("Target:\n" + QString::number(myCropIterator.value()));
        lblAreaTarget->repaint();
      analyseModel(":/commonTarget.png", myCropIterator.value());
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
    }
  }

  QMapIterator<QString, int > myAnimalIterator(mAnimalAreaTargetsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    if (myAnimalIterator.key() != "CommonTarget")
    {
      LaAnimal myAnimal = LaUtils::getAnimal(myAnimalIterator.key());

      // set the images and area target label
        lblGraphic->setPixmap(myAnimal.imageFile());
        lblGraphic->repaint();
        //lblPreview->setPixmap(convertedRasterFile);
        //lblPreview->repaint();
        lblAreaTarget->setText("Target:\n" + QString::number(myAnimalIterator.value()));
        lblAreaTarget->repaint();
      QString myName = myAnimal.name();
      LaMainForm myMainForm;
      QString myAnimalParameterGuid = myMainForm.getMatchingAnimalParameterGuid(myAnimalIterator.key());
      LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
      QString myAnimalRasterFile = myAnimalParameter.rasterName();
      setPbarTargetRange(17);
      //for (int i=0; i<18; i++)
      //{
      //  pbarTarget->setValue(i);
      //}
      // go analyse the stuff...
      int myAreaTarget = myAnimalIterator.value();
      analyseModel(myAnimalRasterFile, myAreaTarget);
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
    }
    else
    {
      //do stuff for commonTarget
        QString myCommonPixMap = ":/commonTarget.png";
        lblGraphic->setPixmap(myCommonPixMap);
        lblGraphic->repaint();
        lblAreaTarget->setText("Target:\n" + QString::number(myAnimalIterator.value()));
        lblAreaTarget->repaint();
      analyseModel(":/commonTarget.png", myAnimalIterator.value());
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
    }
  }
  toggleBusyProgressBar(false);
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
                //pbarBusy->setMinimum(0);
                pbarBusy->setMaximum(0);
                pbarBusy->repaint();
                break;
    case false: // shut it off
                // set the progress bar to not move (min,max = 0,1)
                //pbarBusy->setMinimum(0);
                pbarBusy->setMaximum(1);
                break;
  }
}

void LaGrassProcess::analyseModel(QString theRasterMask, int theAreaTarget)
{
  LaGrass myGrass;


  // r.mapcalc "TimeOnlyFrictionMap=if(isnull(DEM), null(), 1)"
  // r.walk max_cost=20000 elevation=dem_patched_filled@PERMANENT friction=theFrictionMap output=rwalkResultsSlopeMax20kFMap coordinate=744800,3611100 percent_memory=100 nseg=4 walk_coeff=0.72,6.0,1.9998,-1.9998 lambda=0 slope_factor=-0.2125 -k

   // find the land!
   int myFirst = 0;
   int myLast=18000;
   int myAreaTarget = theAreaTarget;
   LandFound mySearchStatus = NotEnough;
   int myCurrentlyContainedArea = 0;
   int myPrecision = 5; // change this to real value
   int myStatusCount = 0;
   setPbarTargetRange(17);

   while (myFirst <= myLast)
  {
    updateCurrentProgress(myStatusCount);
    myStatusCount++;
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
            updateCurrentProgress(myStatusCount);
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
