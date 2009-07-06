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

  LaGrassProcess::LaGrassProcess(LaRasterInfo theRasterInfo, QPair<int, int> theCoordinates, QPair<QMap<QString, int>, QMap<QString, int> > & thePairOfAreaTargetMaps, QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
    //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();

    //connect ( buttonBox, SIGNAL(rejected()), this, SLOT(reject()) );

  mAnimalAreaTargetsMap = thePairOfAreaTargetMaps.first;
  mCropAreaTargetsMap = thePairOfAreaTargetMaps.second;
  mDEM = (theRasterInfo.first).first;
  mMapset = (theRasterInfo.first).second;
  mCommonCropRaster = (theRasterInfo.second).first;
  mCommonGrazingRaster = (theRasterInfo.second).second;
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

void LaGrassProcess::accept()
{
    // first, we need to remove the items from the map
    // that use Common Land, and then determine the
    // number of items in the map to set the overall
    // progress bar (number of steps)
  float myMinimumCost = 0.;
  tbGrass->setText("Creating Cost Surface Raster...");
  tbGrass->repaint();
  toggleBusyProgressBar(true);
  int myOverallProgress = 1;
 // qDebug()JASONDIDTHIS<< "\nmCropAreaTargetsMap\n" << mCropAreaTargetsMap;
 // qDebug()JASONDIDTHIS<< "\nmAnimalAreaTargetsMap\n" << mAnimalAreaTargetsMap;
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
       // qDebug()JASONDIDTHIS<< "removing from area map: "  << myCropGuid;
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
       // qDebug()JASONDIDTHIS<< "removing from area map: "  << myAnimalGuid;
        mAnimalAreaTargetsMap.remove(myAnimalGuid);
      }
    }
  }


  int myNumberOfSearches = mCropAreaTargetsMap.size() + mAnimalAreaTargetsMap.size();
  setPbarOverallRange(myNumberOfSearches);
  qDebug() << "Number of Searches: " << myNumberOfSearches;
 // qDebug()JASONDIDTHIS<< "Number of Searches: " << myNumberOfSearches;
    // create cost surface maps

  LaGrass myGrass;
  //int myEasting = mCoordinates.first;
  //int myNorthing = mCoordinates.second;
  //myGrass.makeWalkCost(myEasting, myNorthing, mDEM);

  tbGrass->append("Cost Surface Generation complete.");
  tbGrass->repaint();
 // qDebug()JASONDIDTHIS<< "\nCropAreaTargetsMap is: \n" << mCropAreaTargetsMap;
  
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
     // qDebug()JASONDIDTHIS<< "myAreaTarget: " << myAreaTarget;
     // qDebug()JASONDIDTHIS<< "myName: " << myName;
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
      myMinimumCost = analyseModel("commonCrop", mCommonCropRaster, myCropIterator.value());
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
      myGrass.createInverseMask(myMinimumCost, mCommonCropRaster);   // creates laLeftOver

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

        // go analyse the stuff...
      int myAreaTarget = myAnimalIterator.value();
        // hard coded to add the leftover mask to the common animal mask
      myGrass.mergeMaps(myAnimalRasterFile);

      analyseModel(myName, "laCombinedMasks@" + mMapset, myAreaTarget);
      updateOverallProgress(myOverallProgress);
      myOverallProgress++;
    }
    else
    {
        //do stuff for commonTarget
      myGrass.mergeMaps(mCommonGrazingRaster);   // creates laCombinedMasks
        QString myCommonPixMap = ":/commonTarget.png";
        lblGraphic->setPixmap(myCommonPixMap);
        lblGraphic->repaint();
        lblAreaTarget->setText("Target:\n" + QString::number(myAnimalIterator.value()));
        lblAreaTarget->repaint();
        // hard coded to add the leftover mask to the common animal mask
      analyseModel("commonGrazing", "laCombinedMasks@" + mMapset, myAnimalIterator.value());
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

  //void LaGrassProcess::reject()
  //{
    // abort the grass analysis connect(pushButtonExit, SIGNAL(clicked()), qApp, SLOT(quit()));
  //}

void LaGrassProcess::updateCurrentProgress(int theStep)
{
  pbarTarget->setValue(theStep);
  qDebug() << "Completed Step " << theStep;
  lblCurrentArea->setText(QString::number(theStep));
}

void LaGrassProcess::updateOverallProgress(int theStep)
{
  pbarOverall->setValue(theStep);
  qDebug() << "Completed Search # " << theStep;
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
    case true:    // turn it on
                  // set the progress bar to move (min,max = 0,0)
                  //pbarBusy->setMinimum(0);
                pbarBusy->setMaximum(0);
                pbarBusy->repaint();
                break;
    case false:   // shut it off
                  // set the progress bar to not move (min,max = 0,1)
                  //pbarBusy->setMinimum(0);
                pbarBusy->setMaximum(1);
                break;
  }
}

float LaGrassProcess::analyseModel(QString theItemName, QString theRasterMask, int theAreaTarget)
{
  LaGrass myGrass;
   float myFirst = 0;
   float myLast=100000;
   int myAreaTarget = theAreaTarget;
   float myCurrentlyContainedArea = 0.0;
   int myPrecision = 5;   // change this to real value
   int myStatusCount = 0;
   LandFound mySearchStatus = NotEnough;
   float myMid;
   setPbarTargetRange(17);



   while (myFirst <= myLast)
  {
    updateCurrentProgress(myStatusCount);
    //qDebug() << "On step " << myStatusCount;
    myStatusCount++;
    myMid = (myFirst + myLast) / 2.;    // compute mid point.
      // reclass with 1 to midpoint and null beyond and then check results
      //    echo "0 thru $step = 1" | r.reclass input=$cost output=cost.reclass --o
      //    r.stats -n -a fs=- input=cost.reclass > $TMP1
   // qDebug()JASONDIDTHIS<< "midpoint value: " << myMid;
   // qDebug()JASONDIDTHIS<< "midpoint valueas int: " << static_cast<int>(myMid);

    myGrass.reclass("laWalkCost", static_cast<int>(myMid));   // makes a raster called laCostMapReclassed
    myGrass.createMask("laCostMapReclassed" , theRasterMask);   // creates tmpMask
    myCurrentlyContainedArea = myGrass.getArea("tmpMask");
      // find out if the contained area is within acceptable range

    mySearchStatus = getSearchStatus(static_cast<int>(myCurrentlyContainedArea), myAreaTarget, myPrecision);

    switch (mySearchStatus)
    {
      case NotEnough:
           qDebug() << "     (low) Current is " << myCurrentlyContainedArea << " but I need " << myAreaTarget;
            myFirst = myMid + 1.;    // repeat search in top half.
            break;;
      case TooMuch:
           qDebug() << "     (high) Current is " << myCurrentlyContainedArea << " but I need " << myAreaTarget;
            myLast = myMid - 1.;   // repeat search in bottom half.
            break;
      case FoundTarget:
              // found it. break out of loop   //  ///
              // copy final raster to permanentRaster
           qDebug() << "     ** TARGET FOUND! **  Contained Area is " << myCurrentlyContainedArea;
           // qDebug()JASONDIDTHIS<< "which falls within the precision range";

            QString myRasterName = generateFilename(theItemName, myMid, myAreaTarget);
            myGrass.copyMap("tmpMask", myRasterName);

            updateCurrentProgress(myStatusCount);
            myFirst = myLast+1.;
            break;
    }

  }
  return myMid;
}

QString LaGrassProcess::generateFilename(QString theItemName, float theExtent, int theAreaTarget)
{
  QString myPeriod="";
  QString myPopulation="";
  QString myDietRatio="";
  QString myDairy="";
  QString myAnimalsFed="";

  QString myPeriodSetting = cbPeriod->currentText();
  QString myPopulationSetting = cbPopulation->currentText();
  QString myDietRatioSetting = cbDietRatio->currentText();
  QString myDairySetting = cbDairy->currentText();
  QString myAnimalsFedSetting = cbAnimalsFed->currentText();
  QString myOtherText = leOtherText->text();

  if (myPeriodSetting == "Chalcolithic") {myPeriod = "Chalco";}
  else if (myPeriodSetting == "EEB1") {myPeriod = "EEB1";}
  else if (myPeriodSetting == "LEB1") {myPeriod = "LEB1";}

  if (myPopulationSetting == "Max") {myPopulation = "MaxPop";}
  else if (myPopulationSetting == "Min") {myPopulation = "MinPop";}

  if (myDairySetting == "Dairy 100%") {myDairy = "Dairy100";}
  else if (myDairySetting == "Dairy 50%") {myDairy = "Dairy50";}
  else if (myDairySetting == "No Dairy") {myDairy = "Dairy0";}
  
  if (myDietRatioSetting == "Meat 30%") {myDietRatio = "Meat30";}
  else if (myDietRatioSetting == "Meat 20%") {myDietRatio = "Meat20";}
  else if (myDietRatioSetting == "Meat 10%") {myDietRatio = "Meat10";}
  
  if (myAnimalsFedSetting == "Animals Fed") {myAnimalsFed = "fed";}
  else if (myAnimalsFedSetting == "Animals Not Fed") {myAnimalsFed = "notFed";}
  
  QString myExtent = QString::number(static_cast<int>(theExtent));
  QString myArea = QString::number(theAreaTarget);
  
  QString myDescriptor =  myPeriod + myPopulation + myDietRatio + myDairy + myAnimalsFed + myOtherText;
  QString myRasterName = theItemName + "_" + myDescriptor + "Extent" + myExtent + "Area" + myArea;
  
  return myRasterName;
}

LandFound LaGrassProcess::getSearchStatus(int theCurrentlyContainedArea, int theAreaTarget, int thePrecision)
{
  LandFound myStatus;
  float myPrecision=5.;    //get the real value for precision
  float myAcceptableRange=(theAreaTarget*myPrecision*0.01)/2.0;
  float myMinimumAcceptable = theAreaTarget - myAcceptableRange;
  float myMaximumAcceptable = theAreaTarget + myAcceptableRange;
 // qDebug()JASONDIDTHIS<< "myAcceptableRange:" << myAcceptableRange;
 // qDebug()JASONDIDTHIS<< "myMinimumAcceptable:" << myMinimumAcceptable;
 // qDebug()JASONDIDTHIS<< "myMaximumAcceptable:" << myMaximumAcceptable;
  if (theCurrentlyContainedArea >= myMinimumAcceptable)
    {
     // qDebug()JASONDIDTHIS<< "the currently contained area of " << theCurrentlyContainedArea << "is >= the MIN target of " << theAreaTarget;
      if (theCurrentlyContainedArea <= myMaximumAcceptable)
      {
     // qDebug()JASONDIDTHIS<< "the currently contained area of " << theCurrentlyContainedArea << "is also <= the MAX target of " << theAreaTarget;
        myStatus = FoundTarget;
      }
      else
      {
     // qDebug()JASONDIDTHIS<< "the currently contained area of " << theCurrentlyContainedArea << "is > the MAX target of " << theAreaTarget;
        myStatus = TooMuch;
      }


    }
  else
    {
     // qDebug()JASONDIDTHIS<< "the currently contained area of " << theCurrentlyContainedArea << "is < the MIN target of " << theAreaTarget;
      myStatus = NotEnough;
    }

  return myStatus;
}
