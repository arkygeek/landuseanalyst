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
  tbGrass->setText("Creating Cost Surface Raster...");
  tbGrass->repaint();

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
      qDebug() << "myAreaTarget: " << myAreaTarget;
      qDebug() << "myName: " << myName;
      analyseModel(myName, myCropRasterFile, myAreaTarget);
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
      QString myRasterName = "cerealMask@shuna";
      analyseModel(myRasterName, "cerealMask", myCropIterator.value());
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
      analyseModel(myName, myAnimalRasterFile, myAreaTarget);
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
      analyseModel("treesMask@shuna" ,"treesMask", myAnimalIterator.value());
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

void LaGrassProcess::analyseModel(QString theItem, QString theRasterMask, int theAreaTarget)
{
  LaGrass myGrass;
   float myFirst = 0;
   float myLast=18000;
   int myAreaTarget = theAreaTarget;
   float myCurrentlyContainedArea = 0.0;
   int myPrecision = 5; // change this to real value
   int myStatusCount = 0;
   LandFound mySearchStatus = NotEnough;

   setPbarTargetRange(17);



   while (myFirst <= myLast)
  {
    updateCurrentProgress(myStatusCount);
    myStatusCount++;
    float myMid = (myFirst + myLast) / 2.;  // compute mid point.
    // reclass with 1 to midpoint and null beyond and then check results
    //    echo "0 thru $step = 1" | r.reclass input=$cost output=cost.reclass --o
    //    r.stats -n -a fs=- input=cost.reclass > $TMP1
    qDebug() << "midpoint value: " << myMid;
    qDebug() << "midpoint valueas int: " << static_cast<int>(myMid);

    myGrass.reclass("laWalkCost", static_cast<int>(myMid)); // makes a raster called laCostMapReclassed
    myGrass.createMask("laCostMapReclassed" , theRasterMask); // creates tmpMask
    myCurrentlyContainedArea = myGrass.getArea("tmpMask");
    // find out if the contained area is within acceptable range

    mySearchStatus = getSearchStatus(static_cast<int>(myCurrentlyContainedArea), myAreaTarget, myPrecision);

    switch (mySearchStatus)
    {
      case NotEnough:
            qDebug() << "NotEnough.  Current is " << myCurrentlyContainedArea << "Needed: " << myAreaTarget;
            myFirst = myMid + 1.;  // repeat search in top half.
            break;;
      case TooMuch:
            qDebug() << "NotEnough.  Current is " << myCurrentlyContainedArea << "Needed: " << myAreaTarget;
            myLast = myMid - 1.; // repeat search in bottom half.
            break;
      case FoundTarget:
            // found it. break out of loop /////
            // copy final raster to permanentRaster
            qDebug() << "TARGET FOUND!  Current is " << myCurrentlyContainedArea << "Actual Needed: " << myAreaTarget;
            qDebug() << "which falls within the precision range";
            QString myRasterName = theItem+"RESULTS";
            myGrass.copyMap("tmpMask", myRasterName);
            updateCurrentProgress(myStatusCount);
            myFirst = myLast+1.;
            break;
    }

  }
}

LandFound LaGrassProcess::getSearchStatus(int theCurrentlyContainedArea, int theAreaTarget, int thePrecision)
{
  LandFound myStatus;
  float myPrecision=5.;  //get the real value for precision
  float myAcceptableRange=(theAreaTarget*myPrecision*0.01)/2.0;
  float myMinimumAcceptable = theAreaTarget - myAcceptableRange;
  float myMaximumAcceptable = theAreaTarget + myAcceptableRange;
  qDebug() << "myAcceptableRange:" << myAcceptableRange;
  qDebug() << "myMinimumAcceptable:" << myMinimumAcceptable;
  qDebug() << "myMaximumAcceptable:" << myMaximumAcceptable;
  if (theCurrentlyContainedArea >= myMinimumAcceptable)
    {
      qDebug() << "the currently contained area of " << theCurrentlyContainedArea << "is >= the MIN target of " << theAreaTarget;
      if (theCurrentlyContainedArea <= myMaximumAcceptable)
      {
      qDebug() << "the currently contained area of " << theCurrentlyContainedArea << "is also <= the MAX target of " << theAreaTarget;
        myStatus = FoundTarget;
      }
      else
      {
      qDebug() << "the currently contained area of " << theCurrentlyContainedArea << "is > the MAX target of " << theAreaTarget;
        myStatus = TooMuch;
      }


    }
  else
    {
      qDebug() << "the currently contained area of " << theCurrentlyContainedArea << "is < the MIN target of " << theAreaTarget;
      myStatus = NotEnough;
    }

  return myStatus;
}
