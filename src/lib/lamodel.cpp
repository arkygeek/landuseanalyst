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
  return mPlantPercent;
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
  // mainform data
  int myPopulation, myDietComposition, myCropPercent, myAnimalPercent, myCaloriesPerPersonPerDay;

  // Manage Crops (Description)
  int myCropYield, myCropFoodValue, myFodderYield, myFodderFoodValue;
  // Manage Crop Parameters
  int myPortionOfDietTamePlant;
  bool myCropRotation, myCropCommonLand, myCropSpecificLand;
  float myCropFallowRatio;
  int myFoodValueFallowLand;

  // Manage Animal (Description)
  int myAnimalFoodValue, myUsableMeat, myKillWeight, myGrowTime, myDeathRate;
  // Reproduction figures
  int mySexualMaturity, myBreedingLife, myYoungPerBirth, myWeaningAge, myGestation, myEstrousCycle;
  // Feed Requirements
  int myCaloriesPerDayGestating, myCaloriesPerDayLactating, myCaloriesPerDayJuvenile;
  // Manage Animal Parameters
  int myPortionOfDietTameAnimals;
  // land suitability
  bool myAnimalCommonLand, myAnimalSpecificLand, myFodderGrazed;
  int myKcalPerYearSpecificLand, myKcalPerYearCommonLand;
  // fodder
  int myCrop1FodderPercentAnimalsDiet, myCrop1GrainPercentAnimalsDiet;
  int myCrop2FodderPercentAnimalsDiet, myCrop2GrainPercentAnimalsDiet;
  int myCrop3FodderPercentAnimalsDiet, myCrop3GrainPercentAnimalsDiet;
  int myFallowPriority;

  ///////////////////////////
  // Assign initial values //
  ///////////////////////////

  // mainform data
  myPopulation=500;
  myDietComposition=50;
  myCropPercent=90;
  myAnimalPercent=90;
  myCaloriesPerPersonPerDay=2500;

  // Manage Crops (Description)
  myCropYield=60;
  myCropFoodValue=3000;
  myFodderYield=50;
  myFodderFoodValue=1000;
  // Manage Crop Parameters
  myPortionOfDietTamePlant=100;
  myCropRotation=1;
  myCropCommonLand=1;
  myCropSpecificLand=1;
  myCropFallowRatio=1.0;
  myFoodValueFallowLand=10000;

  // Manage Animal (Description)
  myUsableMeat=50;
  myKillWeight=100;
  myGrowTime=10;
  myDeathRate=10;
  // Reproduction figures
  mySexualMaturity=18;
  myBreedingLife=6;
  myYoungPerBirth=8;
  myWeaningAge=12;
  myGestation=120;
  myEstrousCycle=21;
  // Feed Requirements
  myCaloriesPerDayGestating=5000;
  myCaloriesPerDayLactating=5000;
  myCaloriesPerDayJuvenile=3500;
  // Manage Animal Parameters
  myPortionOfDietTameAnimals=100;
  // land suitability
  myAnimalCommonLand=1;
  myAnimalSpecificLand=1;
  myFodderGrazed=1;
  myKcalPerYearSpecificLand=1500;
  myKcalPerYearCommonLand=1500;
  // fodder
  myCrop1FodderPercentAnimalsDiet=0;
  myCrop1GrainPercentAnimalsDiet=0;
  myCrop2FodderPercentAnimalsDiet=0;
  myCrop2GrainPercentAnimalsDiet=0;
  myCrop3FodderPercentAnimalsDiet=0;
  myCrop3GrainPercentAnimalsDiet=0;
  myFallowPriority=1;

  ///////////////////////////////
  // Generic Crop Calculations //
  /////////////////////////////////////////
  // We need to calculate three values:  //
  //  1. Calorie target                  //
  //  2. Production target               //
  //  3. Area target                     //
  /////////////////////////////////////////

  // 1. Crop Calorie Target Calculations
  float myCropOverallContributionToDiet;
  float myCalorieTarget;
  float myCropCalorieTarget;
  // we must multiply by 0.01 to turn the following into percentages
  myCropOverallContributionToDiet=((100-myDietComposition)*0.01)*(myCropPercent*.01);
  myCalorieTarget=myPopulation*myCaloriesPerPersonPerDay*365;
  myCropCalorieTarget=myCalorieTarget*myCropOverallContributionToDiet;

  // 2. Crop Production Target Calculations
  float myCropProductionTarget;
  // kg of crop = required calories from this crop DIVIDEDBY calories in one kg (edible part) of the  crop
  myCropProductionTarget=(myCropCalorieTarget/myCropFoodValue);

  // 3. Crop Area Target Calculations
  float myCropAreaTarget; // this will be in dunums!!!
  // the following does not allow for units other than dunums.
  ///* @TODO allow for units other than just dunums */
  myCropAreaTarget=myCropProductionTarget/myCropYield;

  /////////////////////////////////
  // Generic Animal Calculations //
  /////////////////////////////////////////
  // We need to calculate three values:  //
  //  1. Calorie target                  //
  //  2. Production target               //
  //  3. Area target                     //
  /////////////////////////////////////////

  // 1. Animal Calorie Target Calculations
  float myAnimalOverallContributionToDiet;
  float myAnimalCalorieTarget;
  // we must multiply by 0.01 to turn the following into percentages
  myAnimalOverallContributionToDiet=(myDietComposition*0.01)*(myAnimalPercent*.01);
  myCropCalorieTarget=myCalorieTarget*myAnimalOverallContributionToDiet;

  // 2. Animal Production Target Calculations
  float  myAnimalProductionTarget;
  myAnimalProductionTarget=(myAnimalCalorieTarget/myAnimalFoodValue);

  // 3. Animal Area Target Calculations


}
