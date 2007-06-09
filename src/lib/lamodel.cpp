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

#include <QString>
#include <QDomDocument>
#include <QDomElement>
#include "lamodel.h"
#include "lautils.h"
#include "la.h"

LaModel::LaModel() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mPopulation=500;
  mPeriod="No Period Set";
  mProjection=100;
  mPrecision=5;
  mDietPercent=25;
  mPlantPercent=10;
  mMeatPercent=10;
  mCaloriesPerPersonDaily=2500;
}
LaModel::~LaModel()
{

}

//copy constructor
LaModel::LaModel(const LaModel& theModel)
{
  mName=theModel.name();
  mPopulation=theModel.population();
  setGuid(theModel.guid());
  mPeriod=theModel.period();
  mProjection=theModel.projection();
  mEasting=theModel.easting();
  mNorthing=theModel.northing();
  mEuclideanDistance=theModel.euclideanDistance();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietPercent=theModel.dietPercent();
  mPlantPercent=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
  mSpare=theModel.spare();
  mFallowStatus=theModel.fallowStatus();
}

LaModel& LaModel::operator=(const LaModel& theModel)
{
  if (this == &theModel) return *this;   // Gracefully handle self assignment

  mName=theModel.name();
  mPopulation=theModel.population();
  setGuid(theModel.guid());
  mPeriod=theModel.period();
  mProjection=theModel.projection();
  mEasting=theModel.easting();
  mNorthing=theModel.northing();
  mEuclideanDistance=theModel.euclideanDistance();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietPercent=theModel.dietPercent();
  mPlantPercent=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
  mSpare=theModel.spare();
  mFallowStatus=theModel.fallowStatus();
  return *this;
}

QString LaModel::name() const
{
  return mName;
}
int LaModel::population() const
{
  return mPopulation;
}
QString LaModel::period() const
{
  return mPeriod;
}
int LaModel::projection() const
{
  return mProjection;
}
int LaModel::easting() const
{
  return mEasting;
}
int LaModel::northing() const
{
  return mNorthing;
}
bool LaModel::euclideanDistance() const
{
  return mEuclideanDistance;
}
bool LaModel::walkingTime() const
{
  return mWalkingTime;
}
bool LaModel::pathDistance() const
{
  return mPathDistance;
}
int LaModel::precision() const
{
  return mPrecision;
}
int LaModel::dietPercent() const
{
  return mDietPercent;
}
int LaModel::plantPercent() const
{
  if (mPlantPercent < 0)
  {
    return 0;
  }
  else if (mPlantPercent > 100)
  {
    return 100;
  }
  else
  {
    return mPlantPercent;
  }
}
int LaModel::meatPercent() const
{
  return mMeatPercent;
}
int LaModel::caloriesPerPersonDaily() const
{
  return mCaloriesPerPersonDaily;
}
int LaModel::spare() const
{
  return mSpare;
}

void LaModel::setFallowStatus(Status theStatus)
{
  mFallowStatus=theStatus;
}

void LaModel::setName(QString theName)
{
  mName=theName;
}
void LaModel::setPopulation(int thePopulation)
{
  mPopulation=thePopulation;
}
void LaModel::setPeriod(QString thePeriod)
{
  mPeriod=thePeriod;
}

void LaModel::setProjection(int theIndex)
{
  mProjection=theIndex;
}
void LaModel::setEasting(int theEasting)
{
  mEasting=theEasting;
}
void LaModel::setNorthing(int theNorthing)
{
  mNorthing=theNorthing;
}
void LaModel::setEuclideanDistance(bool theBool)
{
  mEuclideanDistance=theBool;
}
void LaModel::setWalkingTime(bool theBool)
{
  mWalkingTime=theBool;
}
void LaModel::setPathDistance(bool theBool)
{
  mPathDistance=theBool;
}
void LaModel::setPrecision(int thePrecision)
{
  mPrecision=thePrecision;
}
void LaModel::setDietPercent(int thePercent)
{
  mDietPercent=thePercent;
}
void LaModel::setPlantPercent(int thePercent)
{
  mPlantPercent=thePercent;
}
void LaModel::setMeatPercent(int thePercent)
{
  mMeatPercent=thePercent;
}
void LaModel::setCaloriesPerPersonDaily(int theCalories)
{
  mCaloriesPerPersonDaily=theCalories;
}
void LaModel::setAnimals(QMap<QString,QString> theAnimals)
{
  mAnimalsMap = theAnimals;
}
void LaModel::setCrops(QMap<QString,QString> theCrops)
{
  mCropsMap = theCrops;
}

void LaModel::setSpare(int theSpare)
{
  mSpare=theSpare;
}

bool LaModel::fromXml(QString theXml)
{
  QString myFlag;
  qDebug("Loading model from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("model");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  qDebug("Model::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  qDebug("Model::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mPopulation=QString(myTopElement.firstChildElement("population").text()).toInt();
  mPeriod=LaUtils::xmlDecode(myTopElement.firstChildElement("period").text());
  mProjection=QString(myTopElement.firstChildElement("projection").text()).toInt();
  mEasting=QString(myTopElement.firstChildElement("easting").text()).toInt();
  mNorthing=QString(myTopElement.firstChildElement("northing").text()).toInt();
  myFlag = myTopElement.firstChildElement("euclideanDistance").text();
  if (myFlag=="1")
  {
    mEuclideanDistance=true;
  }
  else
  {
    mEuclideanDistance=false;
  }
  myFlag = myTopElement.firstChildElement("walkingTime").text();
  if (myFlag=="1")
  {
    mWalkingTime=true;
  }
  else
  {
    mWalkingTime=false;
  }
  myFlag = myTopElement.firstChildElement("pathDistance").text();
  if (myFlag=="1")
  {
    mPathDistance=true;
  }
  else
  {
    mPathDistance=false;
  }
  mPrecision=QString(myTopElement.firstChildElement("precision").text()).toInt();
  mDietPercent=QString(myTopElement.firstChildElement("dietPercent").text()).toInt();
  mPlantPercent=QString(myTopElement.firstChildElement("plantPercent").text()).toInt();
  mMeatPercent=QString(myTopElement.firstChildElement("meatPercent").text()).toInt();
  mCaloriesPerPersonDaily=QString(myTopElement.firstChildElement("caloriesPerPersonDaily").text()).toInt();
  mSpare=QString(myTopElement.firstChildElement("spare").text()).toInt();
  return true;
}

QString LaModel::toXml()
{
  QString myString;
  myString+=QString("<model guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <population>" + QString::number(mPopulation) + "</population>\n");
  myString+=QString("  <period>" + LaUtils::xmlEncode(mPeriod) + "</period>\n");
  myString+=QString("  <projection>" + QString::number(mProjection) + "</projection>\n");
  myString+=QString("  <easting>" + QString::number(mEasting) + "</easting>\n");
  myString+=QString("  <northing>" + QString::number(mNorthing) + "</northing>\n");
  myString+=QString("  <euclideanDistance>" + QString::number(mEuclideanDistance) + "</euclideanDistance>\n");
  myString+=QString("  <walkingTime>" + QString::number(mWalkingTime) + "</walkingTime>\n");
  myString+=QString("  <pathDistance>" + QString::number(mPathDistance) + "</pathDistance>\n");
  myString+=QString("  <precision>" + QString::number(mPrecision) + "</precision>\n");
  myString+=QString("  <dietPercent>" + QString::number(mDietPercent) + "</dietPercent>\n");
  myString+=QString("  <plantPercent>" + QString::number(mPlantPercent) + "</plantPercent>\n");
  myString+=QString("  <meatPercent>" + QString::number(mMeatPercent) + "</meatPercent>\n");
  myString+=QString("  <caloriesPerPersonDaily>" + QString::number(mCaloriesPerPersonDaily) + "</caloriesPerPersonDaily>\n");
  myString+=QString("  <spare>" + QString::number(mSpare) + "</spare>\n");
  myString+=QString("</model>\n");
  return myString;
}

QString LaModel::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("population=>" + QString::number(mPopulation) + "\n");
  myString+=QString("period=>" + LaUtils::xmlEncode(mPeriod) + "\n");
  myString+=QString("projection=>" + QString::number(mProjection) + "\n");
  myString+=QString("easting=>" + QString::number(mEasting) + "\n");
  myString+=QString("northing=>" + QString::number(mNorthing) + "\n");
  myString+=QString("euclideanDistance=>" + QString::number(mEuclideanDistance) + "\n");
  myString+=QString("walkingTime=>" + QString::number(mWalkingTime) + "\n");
  myString+=QString("pathDistance=>" + QString::number(mPathDistance) + "\n");
  myString+=QString("precision=>" + QString::number(mPrecision) + "\n");
  myString+=QString("dietPercent=>" + QString::number(mDietPercent) + "\n");
  myString+=QString("plantPercent=>" + QString::number(mPlantPercent) + "\n");
  myString+=QString("meatPercent=>" + QString::number(mMeatPercent) + "\n");
  myString+=QString("caloriesPerPersonDaily=>" + QString::number(mCaloriesPerPersonDaily) + "\n");
  myString+=QString("spare=>" + QString::number(mSpare) + "\n");
  return myString;
}

QString LaModel::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1><br />";
  myString+="GUID:" + guid() + "<br />";
  myString+="Population:" + QString::number(mPopulation) + "<br />";
  myString+="Period: " + LaUtils::xmlEncode(mPeriod) + "<br />";
  myString+="Projection: " + QString::number(mProjection) + "<br />";
  myString+="Easting: " + QString::number(mEasting) + "<br />";
  myString+="Northing: " + QString::number(mNorthing) + "<br />";
  myString+="Euclidean Distance: " + QString::number(mEuclideanDistance) + "<br />";
  myString+="Walking Time: " + QString::number(mWalkingTime) + "<br />";
  myString+="Path Distance: " + QString::number(mPathDistance) + "<br />";
  myString+="Precision: " + QString::number(mPrecision) + "<br />";
  myString+="Diet Percent" + QString::number(mDietPercent) + "<br />";
  myString+="Plant Percent: " + QString::number(mPlantPercent) + "<br />";
  myString+="Meat Percent: " + QString::number(mMeatPercent) + "<br />";
  myString+="Calories Per PersonDaily: " + QString::number(mCaloriesPerPersonDaily) + "<br />";
  myString+="Spare: " + QString::number(mSpare) + "</p>";
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    //QString myText = "Animal " + myAnimalGuid.toLocal8Bit() +
    //  " , ";
    //myText +=  myAnimalParameterGuid.toLocal8Bit() ;
    //myText += " ";
    //myString += myText + "<br />";
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    myString += myAnimal.toHtml();
    myString += "<br />";
    LaAnimalParameter myParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    myString += myParameter.toHtml();
    myString += "<br />";
  }

  //iterate through crops
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = myCropIterator.value();
    //QString myText = "Crop " + myCropGuid.toLocal8Bit() +
    //  " , ";
    //myText += myCropParameterGuid.toLocal8Bit() ;
    //myText += " ";
    //myString += myText + "<br />";
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    myString += myCrop.toHtml();
    myString += "<br />";
    LaCropParameter myParameter = LaUtils::getCropParameter(myCropParameterGuid);
    myString += myParameter.toHtml();
    myString += "<br />";
  }
  return myString;
}

void LaModel::run()
{
  LaModel myModel;

  /* Basic Steps are:

    X breakdownDiet               ---> int LaModel::breakdownDiet()
    X countCrops                  ---> int LaModel::countCrops()
    X countAnimals                ---> int LaModel::countAnimals()
    X getCalorieTargetCrops       ---> float LaModel::caloriesFromPlants()
    X getCalorieTargetAnimals     ---> float LaModel::caloriesFromTameMeat()
    X getProductionTargetsCrops   ---> float LaModel::getProductionTargetsCrops
                                        (QString theCropGuid, int theCalorieTarget)
    X getProductionTargetsAnimals ---> float LaModel::getProductionTargetsAnimals
                                          (QString theAnimalGuid, int theCalorieTarget)
    X getAreaTargetsCrops         ---> float LaModel::getAreaTargetsCrops
                                          (QString theCropGuid, float theProductionTarget)
      allocateFallowGrazingLand   ---> float LaModel::allocateFallowGrazingLand()
      getAreaTargetsAnimals       ---> float LaModel::caloriesNeededByAnimal
                                          (QString theAnimalGuid)
      adjustAreaTargetsCrops      --->

  */

  float myCaloriesFromCrops;
  myCaloriesFromCrops = caloriesFromPlants();


}

float LaModel::caloriesFromPlants()
{

  float myDietComposition=0.01*(100-mDietPercent);
  float myCropPercent=0.01*(plantPercent());
  float myCropOverallContributionToDiet=((100-myDietComposition))*myCropPercent;
  float myCalorieTarget=population()*caloriesPerPersonDaily()*365;
  float myCropCalorieTarget=myCalorieTarget*myCropOverallContributionToDiet;
  return myCropCalorieTarget;
}

float LaModel::caloriesFromTameMeat()
{
  float myDietComposition=0.01*dietPercent();
  float myMeatPercent=0.01*meatPercent();
  float myAnimalOverallContributionToDiet=myDietComposition*myMeatPercent;
  float myCalorieTarget=population()*mCaloriesPerPersonDaily*365;
  float myTameMeatCalorieTarget=myCalorieTarget*myAnimalOverallContributionToDiet;
  return myTameMeatCalorieTarget;
}

int LaModel::countCrops()
{
  int myCropCounter=0;
  //iterate through crops
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = myCropIterator.value();
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
    myCropCounter++;
  }
  return myCropCounter;
}

int LaModel::countAnimals()
{
  int myAnimalCounter=0;
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    myAnimalCounter++;
  }
  return myAnimalCounter;
}

float LaModel::getCalorieTargetCrops(QString theCropParameterGuid)
{
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myCropPercent=0.01*myCropParameter.percentTameCrop();
  float myCropCalorieTarget=caloriesFromPlants()*myCropPercent;
  return myCropCalorieTarget;
}

float LaModel::getCalorieTargetAnimals(QString theAnimalParameterGuid)
{
  LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(theAnimalParameterGuid);
  float myAnimalPercent=0.01*myAnimalParameter.percentTameMeat();
  float myAnimalCalorieTarget=caloriesFromTameMeat()*myAnimalPercent;
  return myAnimalCalorieTarget;
}
float LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)
{
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropProductionTarget = theCalorieTarget / myCrop.cropCalories();
  return myCropProductionTarget;
}

float LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)
{
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = (theCalorieTarget / myAnimal.meatFoodValue()) / (0.01 * myAnimal.usableMeat());
  return myAnimalProductionTarget;
}

float LaModel::getAreaTargetsCrops(QString theCropGuid, float theProductionTarget)
{
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropAreaTarget = theProductionTarget/myCrop.cropYield();
  return myCropAreaTarget;
}

float LaModel::caloriesNeededByAnimal(QString theAnimalGuid)
{ // this is essentially the generic animal model
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);

  float myAnimalOverallContributionToDiet=(dietPercent() * 0.01) * (meatPercent() * 0.01);
  float myCalorieTarget = population() * mCaloriesPerPersonDaily * 365;
  float myAnimalCalorieTarget=myCalorieTarget*myAnimalOverallContributionToDiet;
  float myAnimalProductionTarget=(myAnimalCalorieTarget/myAnimal.meatFoodValue());
  float myAnimalsRequired=myAnimalProductionTarget/(myAnimal.usableMeat()*.01);

  float myBirthsPerYear = 365 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + (myAnimal.weaningAge() * 7));
  float myOffspringPerMotherYearly = myBirthsPerYear*myAnimal.youngPerBirth()*(1-myAnimal.deathRate());
  float myMothersNeededStepOne = myAnimalsRequired/myOffspringPerMotherYearly;
  float myMalesStepOne = myMothersNeededStepOne/2;
  float myFemalesStepOne = myMothersNeededStepOne/2;
  float myMotherReplacementsPerYear = myMothersNeededStepOne/myAnimal.deathRate();
  float myAdditionalMothers = (myMotherReplacementsPerYear/myOffspringPerMotherYearly)*2;
  float myMalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
  float myFemalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;

  float myTotalMothers = myMothersNeededStepOne+myAdditionalMothers;
  float myTotalMales = myMalesStepOne+myMalesStepTwo;
  float myTotalFemales = myFemalesStepOne+myFemalesStepTwo;
  float myTotalJuveniles = myTotalMales+myTotalFemales;

  float myTotalMothersCaloriesRequired = myTotalMothers * myAnimal.gestating() * 365.;
  float myTotalJuvenilesCaloriesRequired = myTotalJuveniles * myAnimal.juvenile() * 365.;

  float myTotalCaloriesNeededToFeedAnimals = myTotalMothersCaloriesRequired + myTotalJuvenilesCaloriesRequired;
  return myTotalCaloriesNeededToFeedAnimals;
}

float LaModel::getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget)
{
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myAvailableFallow = myCropParameter.fallowRatio() * theAreaTarget;
  return myAvailableFallow;
}

void LaModel::initialiseAnimalCaloriesMap()
{
  mAnimalCaloriesMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    mAnimalCaloriesMap.insert(myAnimalGuid,caloriesNeededByAnimal(myAnimalGuid));
  }
}

Status LaModel::fallowStatus() const
{
  return mFallowStatus;
}

float LaModel::allocateFallowGrazingLand()
{
  // We need to divide the available fallow land amongst the animals
  // that graze fallow. We split the animal breeds by fallow land
  // access priority (high / medium and low priority).
  // e.g. We have 10 animal breeds, 6 of which graze fallow,
  // caw and horse are high priority, shee and pig medium,
  // chicken and gooxe low.

  int myAnimalsHighPriorityCount, myAnimalsMediumPriorityCount, myAnimalsLowPriorityCount;
  float   myAnimalsHighPriorityCalorieRequirements;
  float   myAnimalsMediumPriorityCalorieRequirements;
  float   myAnimalsLowPriorityCalorieRequirements;
  // put starting caloric requirements of all used animals into a map
  // for reduction due to grazing of fallow crop land
  initialiseAnimalCaloriesMap();

  float myTotalFallowCalories=0;

  myAnimalsHighPriorityCount=0;
  myAnimalsMediumPriorityCount=0;
  myAnimalsLowPriorityCount=0;

  myAnimalsHighPriorityCalorieRequirements=0;
  myAnimalsMediumPriorityCalorieRequirements=0;
  myAnimalsLowPriorityCalorieRequirements=0;

  // Count the Animals in each Priority Level and sum their calorie requirements
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);

    switch (myAnimalParameter.fallowUsage())
    {
      case  High:
            myAnimalsHighPriorityCount++;
            myAnimalsHighPriorityCalorieRequirements += caloriesNeededByAnimal(myAnimalGuid);
            break;
      case  Medium:
            myAnimalsMediumPriorityCount++;
            myAnimalsMediumPriorityCalorieRequirements += caloriesNeededByAnimal(myAnimalGuid);
            break;
      case  Low:
            myAnimalsLowPriorityCount++;
            myAnimalsLowPriorityCalorieRequirements += caloriesNeededByAnimal(myAnimalGuid);
            break;
      case  None:
            break;
      default:
            break;
    } //switch

  } //while animal count

  //  iterate through crops to determine the total calories available to animals
  //  by grazing fallow crop land

  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = myCropIterator.value();
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);

    float myCropPercent = 0.01 * myCropParameter.percentTameCrop();
    float myCropCalorieTarget = caloriesFromPlants() * myCropPercent;
    float myCropProductionTarget = myCropCalorieTarget / myCrop.cropCalories();
    float myCropAreaTarget = myCropProductionTarget / myCrop.cropYield();
    float myAvailableFallowCalories = myCropParameter.fallowRatio() * myCropAreaTarget * myCropParameter.fallowCalories();

    myTotalFallowCalories += myAvailableFallowCalories;
  } // while crop iterator

  ////////////////////////////////////////
  // The following three if statements  //
  // process all of the animals which   //
  // utilize fallow cropland as grazing //
  // land.  It first checks that there  //
  // is fallow land available, and next //
  // allocates the the fallow based on  //
  // the animals fallow access priority //
  ////////////////////////////////////////

  // HIGH priority animals get allocated fallow cropland
  if (myTotalFallowCalories > 0)
  {
    Priority myPriority = High;
    myTotalFallowCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsHighPriorityCalorieRequirements);
  }
  // MEDIUM priority animals get allocated fallow cropland
  if (myTotalFallowCalories > 0)
  {
    Priority myPriority = Medium;
    myTotalFallowCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsMediumPriorityCalorieRequirements);
  }
  // LOW priority animals get allocated fallow cropland
  if (myTotalFallowCalories > 0)
  {
    Priority myPriority = Low;
    myTotalFallowCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsLowPriorityCalorieRequirements);
  }
  return myTotalFallowCalories;
}

float LaModel::doTheFallowAllocation (Priority thePriority,
                                      float theAvailableFallowCalories,
                                      float theTotalCalorificRequirements)
{
  float myTotalFallowCalories=theAvailableFallowCalories - theTotalCalorificRequirements;
  Status myFallowStatus;

  if (myTotalFallowCalories > 0) {myFallowStatus=MoreThanEnoughToCompletelySatisfy;}
  else {myFallowStatus=NotEnoughToCompletelySatisfy;}

  switch (myFallowStatus)
  {
    case  MoreThanEnoughToCompletelySatisfy:
          {
            // because there is leftover calories available to feed more critters, this
            // shows that all of the animals caloric requirements are met with crop fallow
            // and require no more feed so their values in the QMap will be set to 0
            QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
            while (myAnimalIterator.hasNext())
            {
              myAnimalIterator.next();

              QString myAnimalGuid = myAnimalIterator.key();
              QString myAnimalParameterGuid = myAnimalIterator.value();
              LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
              LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);

              if (myAnimalParameter.fallowUsage()==thePriority)
              {
                mAnimalCaloriesMap[myAnimalGuid] = 0;
              } //endif (fallowUsage(myAnimalGuid)

            } // while animal iterating
            break;
          }

    case  NotEnoughToCompletelySatisfy:
          {
            // because there ARE NO leftover calories available to feed more critters, this
            // shows that NOT ALL of the animals caloric requirements are met with crop fallow
            // and therefore require more feed so their values in the QMap will be adjusted accordingly
            QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
            while (myAnimalIterator.hasNext())
            {
              myAnimalIterator.next();

              QString myAnimalGuid = myAnimalIterator.key();
              QString myAnimalParameterGuid = myAnimalIterator.value();
              LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
              LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);

              if (myAnimalParameter.fallowUsage()==thePriority)
              {
                float myAdjustedCaloricRequirements = (mAnimalCaloriesMap.value(myAnimalGuid) / theTotalCalorificRequirements) * myTotalFallowCalories;
                mAnimalCaloriesMap[myAnimalGuid] = myAdjustedCaloricRequirements;
              } //endif (fallowUsage(myAnimalGuid)==High)

            } // while animal iterating
            break;
          }

    default:
          break;
  } //switch
  return myTotalFallowCalories;
}

float LaModel::adjustAreaTargetsCrops()
{
  int a;
  return a;
}
