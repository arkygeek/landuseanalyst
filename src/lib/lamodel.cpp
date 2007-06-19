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

#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QListWidget>
#include <QComboBox>
#include <QHeaderView>

LaModel::LaModel() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mPopulation=500;
  mPeriod="No Period Set";
  mProjection=100;
  mPrecision=5;
  mDietPercent=25;
  mPercentOfDietThatIsFromCrops=10;
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
  mPercentOfDietThatIsFromCrops=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
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
  mPercentOfDietThatIsFromCrops=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
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
  if (mPercentOfDietThatIsFromCrops < 0)
  {
    return 0;
  }
  else if (mPercentOfDietThatIsFromCrops > 100)
  {
    return 100;
  }
  else
  {
    return mPercentOfDietThatIsFromCrops;
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
void LaModel::setCropPercent(int thePercent)
{
  mPercentOfDietThatIsFromCrops=thePercent;
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

bool LaModel::fromXml(QString theXml)
{
  qDebug("method ==> bool LaModel::fromXml(QString theXml)");
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
  mPercentOfDietThatIsFromCrops=QString(myTopElement.firstChildElement("plantPercent").text()).toInt();
  mMeatPercent=QString(myTopElement.firstChildElement("meatPercent").text()).toInt();
  mCaloriesPerPersonDaily=QString(myTopElement.firstChildElement("caloriesPerPersonDaily").text()).toInt();
  return true;
}

QString LaModel::toXml()
{
  qDebug("method ==> QString LaModel::toXml()");
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
  myString+=QString("  <plantPercent>" + QString::number(mPercentOfDietThatIsFromCrops) + "</plantPercent>\n");
  myString+=QString("  <meatPercent>" + QString::number(mMeatPercent) + "</meatPercent>\n");
  myString+=QString("  <caloriesPerPersonDaily>" + QString::number(mCaloriesPerPersonDaily) + "</caloriesPerPersonDaily>\n");
  myString+=QString("</model>\n");
  return myString;
}

QString LaModel::toText()
{
  qDebug("method ==> QString LaModel::toText()");
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
  myString+=QString("plantPercent=>" + QString::number(mPercentOfDietThatIsFromCrops) + "\n");
  myString+=QString("meatPercent=>" + QString::number(mMeatPercent) + "\n");
  myString+=QString("caloriesPerPersonDaily=>" + QString::number(mCaloriesPerPersonDaily) + "\n");
  return myString;
}

QString LaModel::toHtml()
{
  qDebug("method ==> QString LaModel::toHtml()");
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
  myString+="Plant Percent: " + QString::number(mPercentOfDietThatIsFromCrops) + "<br />";
  myString+="Meat Percent: " + QString::number(mMeatPercent) + "<br />";
  myString+="Calories Per PersonDaily: " + QString::number(mCaloriesPerPersonDaily) + "<br />";
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

    /////////////////////////////////////////////
   //                                         //
  //  The 'GUTS' of this class follow below  //
 //                                         //
/////////////////////////////////////////////

void LaModel::DoCalculations()
{
  qDebug("method ==> void LaModel::DoCalculations()");
  // Step 1
  //        Calculate calories needed from crops and tame meat to sustain the settlement
  //        available here -->  caloriesFromCrops();
  //        available here -->  caloriesFromTameMeat();

  // Step 2
  //        Calculate calorie targets for each crop and each animals
  //        (These results will be stored in a QMap)
  initialiseCaloriesProvidedByCropsMap();
  initialiseCaloriesProvidedByAnimalsMap();

  // Step 3
  //        Now we need to calculate how many calories the animals
  //          are going to need to stay alive.
  //        (These calculations are going to be stored in a QMap)
  initialiseCaloriesRequiredByAnimalsMap();

  // Step 4
  //        Production targets must now be calculated for each animal and crop
  //        Animals first, because if the animals are fed grain, it will
  //          increase the production targets of the crops
  initialiseProductionRequiredAnimalsMap();
  initialiseProductionRequiredCropsMap();

  // Step 5
  //        Area targets for crops are calculated and stored in a QMap
  //        These calculations will produce values for the amount of
  //          fallow land available for grazing, which will in turn
  //          be used to reduce the amount of calories which the animals
  //          who graze the fallow land need from specific grazing land.
  initialiseAreaTargetsCropsMap();

  // Step 6
  //        If there is available fallow cropland for any animals to
  //          graze, it needs to be allocated to the animals accordingly
  //          to their access priority, and their total calorific
  //          requirements will be reduced to reflect this 'already
  //          counted for' land.
  allocateFallowGrazingLand();

  // Step 7
  //        If there are additional feed requirements for any animals we
  //          now need to check to see if they receive calories from fodder.
  //        If they do get fed fodder, this is the process that gets followed:
  //          1)  They get fed straw and chaff first, as it is less costly
  //              to the settlement than feeding them the grain.  If there is
  //              enough calories provided by the straw/chaff fodder to satisfy
  //              their remaining calorific needs, there is no need to search
  //              for any additional grazing land, so that animals area target
  //              needs to be set to zero.
  //          2)  If the straw/chaff doesn't satisfy their feeding requirements,
  //              then the same process as above is followed, but considering
  //              of course the grain in this step.  However, at this point, if
  //              grain is being used, the amount of that grain needs to be added
  //              onto the prodction level requirement of the crop. (Step 7)
  adjustAnimalTargetsForFodder();

  // Step 8
  //        Adjust the production levels of the crops to reflect any increases in
  //          demand resulting from grain being used to feed animals.
  //        adjustCropProductionForFodder(); // implement later
  //
  // Step 8
  //        Calculate area targets for the animals based on their final
  //          calorific requirements after considering fallow grazing
  //          and the use of fodder as feed.
  initialiseAreaTargetsAnimalsMap();
}
void LaModel::adjustAnimalTargetsForFodder()
{
  qDebug("method ==> void LaModel::adjustAnimalTargetsForFodder()");
  // after serious consideration, I have decided to implement fodder later.
  // it is not as important as getting the rest of the project working.
}
int LaModel::caloriesFromCrops()
{
  qDebug("method ==> int LaModel::caloriesFromCrops()");
  float myDietComposition = 0.01 * ( 100 - mDietPercent );
  float myCropPercent = 0.01 * ( plantPercent() );
  float myCropOverallContributionToDiet = myDietComposition * myCropPercent;
  float myCalorieTarget = population() * caloriesPerPersonDaily() * 365;
  float myCropCalorieTarget = myCalorieTarget * myCropOverallContributionToDiet;
  int myReturnValue = static_cast<int> (myCropCalorieTarget);
  qDebug("method ==> int LaModel::caloriesFromCrops()");
  qDebug("Overall Crop Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesFromTameMeat()
{
  qDebug("method ==> int LaModel::caloriesFromTameMeat()");
  float myDietComposition=0.01*dietPercent();
  float myMeatPercent=0.01*meatPercent();
  float myAnimalOverallContributionToDiet=myDietComposition*myMeatPercent;
  float myCalorieTarget=population()*mCaloriesPerPersonDaily*365;
  float myTameMeatCalorieTarget=myCalorieTarget*myAnimalOverallContributionToDiet;
  int myReturnValue = static_cast<int>(myTameMeatCalorieTarget);
  qDebug("method ==> int LaModel::caloriesFromTameMeat()");
  qDebug("Overall Crop Tame Meat Target: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::countCrops()
{
  qDebug("method ==> int LaModel::countCrops()");
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
  qDebug("method ==> int LaModel::countCrops()");
  qDebug("Crop Count: " + QString::number(myCropCounter).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myCropCounter;
}

int LaModel::countAnimals()
{
  qDebug("method ==> int LaModel::countAnimals()");
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
  qDebug("method ==> int LaModel::countAnimals()");
  qDebug("Animal Count: " + QString::number(myAnimalCounter).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myAnimalCounter;
}

int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)
{
  qDebug("method ==> int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)");
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myCropPercent = 0.01 * myCropParameter.percentTameCrop();
  float myCropCalorieTarget=caloriesFromCrops()*myCropPercent;
  int myReturnValue = static_cast<int>(myCropCalorieTarget);
  ///@TODO remove this debugging stuff
  qDebug("method ==> int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)");
  qDebug("Crop Parameter Guid that was passed here: " + theCropParameterGuid.toLocal8Bit());
  qDebug("Crop Parameter Name: " + myCropParameter.name().toLocal8Bit());
  qDebug("myCropParameter.percentTameCrop() is giving a result of:" + QString::number(myCropParameter.percentTameCrop()).toLocal8Bit());
  qDebug("crop percent: " + QString::number(myCropPercent).toLocal8Bit());
  qDebug("Calorie Target float: " + QString::number(myCropCalorieTarget).toLocal8Bit());
  qDebug("Calorie Target int: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)
{
  qDebug("method ==> int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)");
  LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(theAnimalParameterGuid);
  float myAnimalPercent=0.01*myAnimalParameter.percentTameMeat();
  float myAnimalCalorieTarget=caloriesFromTameMeat()*myAnimalPercent;
  int myReturnValue = static_cast<int>(myAnimalCalorieTarget);
  ///@TODO remove this debugging stuff
  qDebug("method ==> int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)");
  qDebug("Animal Parameter Guid: " + myAnimalParameter.guid().toLocal8Bit());
  qDebug("Animal Parameter Name: " + myAnimalParameter.name().toLocal8Bit());
  qDebug("Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}
int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)
{
  qDebug("method ==> int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)");
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropProductionTarget = theCalorieTarget / myCrop.cropCalories();
  int myReturnValue = static_cast<int>(myCropProductionTarget);
  ///@TODO remove this debugging stuff
  qDebug("method ==> int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)");
  qDebug("Crop Guid: " + myCrop.guid().toLocal8Bit());
  qDebug("Crop Name: " + myCrop.name().toLocal8Bit());
  qDebug("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)
{
  qDebug("method ==> int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)");
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = (theCalorieTarget / myAnimal.meatFoodValue()) / (0.01 * myAnimal.usableMeat());
  int myReturnValue = static_cast<int>(myAnimalProductionTarget);
  ///@TODO remove this debugging stuff
  qDebug("method ==> int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)");
  qDebug("Animal Guid: " + myAnimal.guid().toLocal8Bit());
  qDebug("Animal Name: " + myAnimal.name().toLocal8Bit());
  qDebug("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)
{
  qDebug("method ==> int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)");
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropAreaTarget = theProductionTarget/myCrop.cropYield();
  int myReturnValue = static_cast<int>(myCropAreaTarget);
  ///@TODO remove this debugging stuff
  qDebug("method ==> int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)");
  qDebug("Crop Guid: " + myCrop.guid().toLocal8Bit());
  qDebug("Crop Name: " + myCrop.name().toLocal8Bit());
  qDebug("Area Target is the production target of: " + theProductionTarget);
  qDebug(" Divided by the crop yield of " + myCrop.cropYield());
  qDebug(" which gives a result of: " + QString::number(myReturnValue).toLocal8Bit());
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)
{ // this is essentially the generic animal model
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  qDebug("||||||||||||||||||||||||||||||||||||||||||||||||");
  qDebug("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv");
  qDebug("method ==> int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)");
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  // LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(theAnimalGuid));
  // float myAnimalOverallContributionToDiet=(dietPercent() * 0.01) * (meatPercent() * 0.01);
  // float myCalorieTarget = population() * mCaloriesPerPersonDaily * 365;
  // float myAnimalCalorieTarget=myCalorieTarget*myAnimalOverallContributionToDiet;

  float myAnimalProductionTarget=(mCaloriesProvidedByAnimalsMap.value(theAnimalGuid) / myAnimal.meatFoodValue());
    qDebug("animal prodn target = calorie target of animal / food value");
    qDebug("mCaloriesProvidedByAnimalsMap.value(theAnimalGuid): " + QString::number(mCaloriesProvidedByAnimalsMap.value(theAnimalGuid)).toLocal8Bit());
    qDebug("myAnimal.meatFoodValue(): " + QString::number(myAnimal.meatFoodValue()).toLocal8Bit());
    qDebug("myAnimalProductionTarget = " + QString::number(myAnimalProductionTarget).toLocal8Bit());
  float myAnimalsRequired=(myAnimalProductionTarget / myAnimal.killWeight()) / (myAnimal.usableMeat()*.01);
    qDebug("slaughter animals reqd: " + QString::number(myAnimalsRequired).toLocal8Bit());
  float myBirthsPerYear = 365.0 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + (myAnimal.weaningAge() * 7.0));
    qDebug("BirthEventsPerYear: " + QString::number(myBirthsPerYear).toLocal8Bit());
  float myOffspringPerMotherYearly = myBirthsPerYear * myAnimal.youngPerBirth() * (1.0-(0.01*myAnimal.deathRate()));
    qDebug("OffspringPerMotherYearly = " + QString::number(myOffspringPerMotherYearly).toLocal8Bit());
  float myMothersNeededStepOne = myAnimalsRequired/myOffspringPerMotherYearly;
    qDebug("MothersNeededStepOne = " + QString::number(myMothersNeededStepOne).toLocal8Bit());
  float myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly)/2;
    qDebug("MalesStepOne = " + QString::number(myMalesStepOne).toLocal8Bit());
  float myFemalesStepOne = myMalesStepOne;
    qDebug("FemalesStepOne = " + QString::number(myFemalesStepOne).toLocal8Bit());
  float myMotherReplacementsPerYear = myMothersNeededStepOne/myAnimal.breedingExpectancy();
    qDebug("MotherReplacementsPerYear = " + QString::number(myMotherReplacementsPerYear).toLocal8Bit());
  float myAdditionalMothers = (myMotherReplacementsPerYear/myOffspringPerMotherYearly)*2;
    qDebug("AdditionalMothers = " + QString::number(myAdditionalMothers).toLocal8Bit());
  float myMalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
    qDebug("MalesStepTwo = " + QString::number(myMalesStepTwo).toLocal8Bit());
  float myFemalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
    qDebug("FemalesStepTwo = " + QString::number(myFemalesStepTwo).toLocal8Bit());
  float myTotalMothers = myMothersNeededStepOne+myAdditionalMothers;
    qDebug("TotalMothers = " + QString::number(myTotalMothers).toLocal8Bit());
  float myTotalMales = myMalesStepOne+myMalesStepTwo;
    qDebug("TotalMales = " + QString::number(myTotalMales).toLocal8Bit());
  float myTotalFemales = myFemalesStepOne-myFemalesStepTwo;
    qDebug("TotalFemales = " + QString::number(myTotalFemales).toLocal8Bit());
  float myTotalJuveniles = myTotalMales+myTotalFemales;
    qDebug("TotalJuveniles = " + QString::number(myTotalJuveniles).toLocal8Bit());
  float myTotalMothersCaloriesRequired = myTotalMothers * myAnimal.gestating() * 365.;
    qDebug("TotalMothersCaloriesRequired = " + QString::number(myTotalMothersCaloriesRequired).toLocal8Bit());
  float myTotalJuvenilesCaloriesRequired = myTotalJuveniles * myAnimal.juvenile() * 365.;
    qDebug("TotalJuvenilesCaloriesRequired = " + QString::number(myTotalJuvenilesCaloriesRequired).toLocal8Bit());
  float myTotalCaloriesNeededToFeedAnimals = myTotalMothersCaloriesRequired + myTotalJuvenilesCaloriesRequired;
    qDebug("TotalCaloriesNeededToFeedAnimals = " + QString::number(myTotalCaloriesNeededToFeedAnimals).toLocal8Bit());

  qDebug("method ==> int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)");
  qDebug("Animal: " + myAnimal.name().toLocal8Bit());
  qDebug("Breeding Stock: " + QString::number(myTotalMothers).toLocal8Bit());
  qDebug("Juveniles: " + QString::number(myTotalJuveniles).toLocal8Bit());
  qDebug("Calories needed annually to feed the entire herd: " +
      QString::number(myTotalCaloriesNeededToFeedAnimals).toLocal8Bit());
  qDebug("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
  qDebug("||||||||||||||||||||||||||||||||||||||||||||||||");
  qDebug("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

  int myReturnValue = static_cast<int>(myTotalCaloriesNeededToFeedAnimals);
  return myReturnValue;
}

int LaModel::getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget)
{
  qDebug("method ==> int LaModel::getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget)");
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myAvailableFallow = myCropParameter.fallowRatio() * theAreaTarget;
  int myReturnValue = static_cast<int>(myAvailableFallow);
  return myReturnValue;
}

void LaModel::initialiseCaloriesProvidedByAnimalsMap()
{
  qDebug("method ==> void LaModel::initialiseCaloriesProvidedByAnimalsMap()");
  mCaloriesProvidedByAnimalsMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = mAnimalsMap.value(myAnimalGuid);
    mCaloriesProvidedByAnimalsMap.insert(myAnimalGuid,caloriesProvidedByTheAnimal(myAnimalParameterGuid));
  }
}

void LaModel::initialiseCaloriesProvidedByCropsMap()
{
  qDebug("method ==> void LaModel::initialiseCaloriesProvidedByCropsMap()");
  mCaloriesProvidedByCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = mCropsMap.value(myCropGuid);
    mCaloriesProvidedByCropsMap.insert(myCropGuid,caloriesProvidedByTheCrop(myCropParameterGuid));
  }
}

void LaModel::initialiseCaloriesRequiredByAnimalsMap()
{
  qDebug("method ==> void LaModel::initialiseCaloriesRequiredByAnimalsMap()");
  mCaloriesRequiredByAnimalsMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    mCaloriesRequiredByAnimalsMap.insert(myAnimalGuid,caloriesNeededByAnimal(myAnimalGuid));
  }
}

void LaModel::initialiseProductionRequiredCropsMap()
{
  qDebug("method ==> void LaModel::initialiseProductionRequiredCropsMap()");
  mProductionRequiredCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast<int>(mCaloriesProvidedByCropsMap.value(myCropGuid));
    mProductionRequiredCropsMap.insert(myCropGuid,getProductionTargetsCrops(myCropGuid, myProductionTarget));
    qDebug("cropGuid: " + QString::number(mProductionRequiredCropsMap.value(myCropGuid)).toLocal8Bit());
    qDebug("ProductionTarget: " + QString::number(mProductionRequiredCropsMap.value(myCropGuid)).toLocal8Bit());
    qDebug("cropGuid: " + myCropGuid.toLocal8Bit());

  }
}

void LaModel::initialiseProductionRequiredAnimalsMap()
{
  qDebug("method ==> void LaModel::initialiseProductionRequiredAnimalsMap()");
  mProductionRequiredAnimalsMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myProductionTarget = static_cast<int>(mCaloriesProvidedByAnimalsMap.value(myAnimalGuid));
    mProductionRequiredAnimalsMap.insert(myAnimalGuid,getProductionTargetsAnimals(myAnimalGuid, myProductionTarget));
  }
}

void LaModel::initialiseAreaTargetsCropsMap()
{
  qDebug("method ==> void LaModel::initialiseAreaTargetsCropsMap()");
  mAreaTargetsCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast<int>(mProductionRequiredCropsMap.value(myCropGuid));
    mProductionRequiredCropsMap.insert(myCropGuid,getAreaTargetsCrops(myCropGuid, myProductionTarget));
  }
}

void LaModel::initialiseAreaTargetsAnimalsMap()
{ // this also returns an area target for common land
  qDebug("method ==> void LaModel::initialiseAreaTargetsAnimalsMap()");
  mAreaTargetsAnimalsMap.clear();
  mCommonGrazingLandAreaTarget = 0;
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    // check to see if this animal needs any additional food
    if (mCaloriesRequiredByAnimalsMap[myAnimalGuid] > 0) // yes, the animal needs more food
    {
      // figure out how much grazing land is needed to supply this many calories
      LandBeingGrazed myLandBeingGrazed;
      if (myAnimalParameter.useCommonGrazingLand()==1){myLandBeingGrazed=Common;}
      else {myLandBeingGrazed=Unique;}

      switch (myLandBeingGrazed)
      {
        case Common:
             {
               mCommonGrazingLandAreaTarget++;
               mAreaTargetsAnimalsMap[myAnimalGuid]=0;
             }
        case Unique:
             {
               float myTarget = mCaloriesRequiredByAnimalsMap.value(myAnimalGuid) / myAnimalParameter.foodValueOfSpecificGrazingLand();
               mAreaTargetsAnimalsMap[myAnimalGuid]=static_cast<int>(myTarget);
             }
      }
      //int myCaloriesNeeded = static_cast<int>(mCaloriesRequiredByAnimalsMap.value(myAnimalGuid));

      //mProductionRequiredAnimalsMap.insert(myAnimalGuid,getProductionTargetsAnimals(myAnimalGuid, myProductionTarget));
    }
    else // the animal needs no additional food
    {
      mAreaTargetsAnimalsMap[myAnimalGuid] = 0;
    }
  }
}

Status LaModel::fallowStatus() const
{
  return mFallowStatus;
}

void LaModel::allocateFallowGrazingLand()
{
  qDebug("method ==> void LaModel::allocateFallowGrazingLand()");
  // We need to divide the available fallow land amongst the animals
  // that graze fallow. We split the animal breeds by fallow land
  // access priority (high / medium and low priority).
  // e.g. We have 10 animal breeds, 6 of which graze fallow,
  // caw and horse are high priority, shee and pig medium,
  // chicken and gooxe low.

  int myAnimalsHighPriorityCount=0, myAnimalsMediumPriorityCount=0, myAnimalsLowPriorityCount=0;
  int   myAnimalsHighPriorityCalorieRequirements=0;
  int   myAnimalsMediumPriorityCalorieRequirements=0;
  int   myAnimalsLowPriorityCalorieRequirements=0;
  // put starting caloric requirements of all used animals into a map
  // for reduction due to grazing of fallow crop land
  // initialiseCaloriesRequiredByAnimalsMap();

  int myTotalFallowCalories=0;

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
  qDebug("High Priority Animals: " + QString::number(myAnimalsHighPriorityCount).toLocal8Bit() );
  qDebug("Medium Priority Animals: " + QString::number(myAnimalsMediumPriorityCount).toLocal8Bit() );
  qDebug("Low Priority Animals: " + QString::number(myAnimalsLowPriorityCount).toLocal8Bit() );
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
    float myCropCalorieTarget = caloriesFromCrops() * myCropPercent;
    float myCropProductionTarget = myCropCalorieTarget / myCrop.cropCalories();
    float myCropAreaTarget = myCropProductionTarget / myCrop.cropYield();
    float myAvailableFallowCalories = myCropParameter.fallowRatio() * myCropAreaTarget * myCropParameter.fallowCalories();

    myTotalFallowCalories += static_cast<int>(myAvailableFallowCalories);
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
  //int myReturnValue = static_cast<int>(myTotalFallowCalories);
  //return myReturnValue;
}

int LaModel::doTheFallowAllocation
      (
        Priority thePriority,
        int theAvailableFallowCalories,
        int theTotalCalorificRequirements
      )
{

  // when the total number of calories needed by the animals
  // is taken away from the total available calories (from crop fallow),
  // there will be one of two results.
  // 1. the result will be <=0, meaning that additional sources of
  //    food is required for the animals.  (fodder or grazing land)
  // 2. the result will be > 0, meaning that there is enough food value
  //    in the crop fallow to completely feed the animals.
  int myTotalFallowCalories = theAvailableFallowCalories - theTotalCalorificRequirements;

  // set up the conditions for the fallow allocation...
  // there is either enough fallow to feed the animal completely
  // or not enough to feed them completely.  If there is enough,
  // the animal will not be requiring any additional source of
  // calories.  In other words, we won't be needing to graze them
  // on any other land besides the crop fallow.
  Status myFallowStatus;
  if (myTotalFallowCalories > 0) {myFallowStatus = MoreThanEnoughToCompletelySatisfy;}
  else {myFallowStatus = NotEnoughToCompletelySatisfy;}

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
                mCaloriesRequiredByAnimalsMap[myAnimalGuid] = 0;
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
                int myAdjustedCaloricRequirements =
                    static_cast<int>(
                                     (
                                      mCaloriesRequiredByAnimalsMap.value( myAnimalGuid )
                                      / theTotalCalorificRequirements
                                     )
                                     * myTotalFallowCalories
                                    );
                mCaloriesRequiredByAnimalsMap [myAnimalGuid] = myAdjustedCaloricRequirements;
              } //endif (fallowUsage(myAnimalGuid)==High)

            } // while animal iterating
            break;
          }

    default:
          break;
  } //switch
  return myTotalFallowCalories;
}

////////// All of the following functions are GRASS related functions ////////

int LaModel::adjustAreaTargetsCrops()
{
  qDebug("method ==> int LaModel::adjustAreaTargetsCrops()");
  int a;
  return a;
}

void LaModel::getArea(float theArea)
{
  qDebug("method ==> void LaModel::getArea(float theArea)");
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "tempraster";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);

  if (!myProcess.waitForStarted())
  {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1))
  {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

void LaModel::makeWalkCost(int theX, int theY)
{
  qDebug("method ==> void LaModel::makeWalkCost(int theX, int theY)");
}

void LaModel::makeEuclideanCost(int theX, int theY)
{
  qDebug("method ==> void LaModel::makeEuclideanCost(int theX, int theY)");
}

void LaModel::makePathDistanceCost(int theX, int theY)
{
  qDebug("method ==> void LaModel::makePathDistanceCost(int theX, int theY)");
}

void LaModel::writeMetaData(QString theValue)
{
  qDebug("method ==> void LaModel::writeMetaData(QString theValue)");
}

void LaModel::makeCircle(int theX, int theY)
{
  qDebug("method ==> void LaModel::makeCircle(int theX, int theY");
  // to verify this worked do
  //    d.rast
  //    and check in the pull downlist (if your eyes dont fall out looking at those fonts)
  //    to remove teh file again do:
  //    g.remove rast=circle

  /*
     qDebug("Making crop circle...tweeedee treedee");
     QString myProgram = "/usr/lib/grass/bin/r.circle";
     QStringList myArgs;
     myArgs << "-b"
     << "output=circle"
     <<  "coordinate=744800,3611100"
     << "max=500"
     << "--overwrite";
     */
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "landuse";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);
  if (!myProcess.waitForStarted()) {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1)) {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

  ////////////////////////////////////////////////////////////////////////
 // The following is all for generating reports on calculation results //
////////////////////////////////////////////////////////////////////////

QString LaModel::toXmlCalorieCropTargets()
{
  // This method returns a QString for an xml file containing the calorie
  // targets for each crop from mCaloriesProvidedByCropsMap

  // Loop through the mCaloriesProvidedByCropsMap
  QString myString;
  myString += QString("<cropCalorieTargetReport>\n");
  QMapIterator<QString, float> myCropIterator (mCaloriesProvidedByCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myCalorieTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <crop>\n");
    myString += QString("    <guid=\"" + myCropIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCrop.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myCrop.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myCropParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCropParameter.name()) + "</name>\n");
    myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
    myString += QString("  </crop>\n");
  } // while crop iterator

  myString += QString("</cropCalorieTargetReport>\n");
  return myString;
}

QString LaModel::toXmlCalorieAnimalTargets()
{
  // This method returns a QString for an xml file containing the calorie
  // targets for each animal from mCaloriesProvidedByAnimalsMap

  // Loop through the mCaloriesProvidedByAniamlsMap
  QString myString;
  myString += QString("<animalCalorieTargetReport>\n");
  QMapIterator<QString, float> myAnimalIterator (mCaloriesProvidedByAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myCalorieTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <animal>\n");
    myString += QString("    <guid=\"" + myAnimalIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimal.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myAnimal.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myAnimalParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimalParameter.name()) + "</name>\n");
    myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
    myString += QString("  </animal>\n");

  } // while crop iterator

  myString += QString("</animalCalorieTargetReport>\n");
  return myString;
}

QString LaModel::toXmlProductionCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mProductionRequiredCropsMap

  // Loop through the mProductionRequiredCropsMap
  QString myString;
  myString += QString("<cropProductionTargetReport>\n");
  QMapIterator<QString, float> myCropIterator (mProductionRequiredCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <crop>\n");
    myString += QString("    <guid=\"" + myCropIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCrop.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myCrop.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myCropParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCropParameter.name()) + "</name>\n");
    myString += QString("    <productionTarget>" + QString::number(myProductionTarget) + "</productionTarget>\n");
    myString += QString("  </crop>\n");
  } // while crop iterator

  myString+=QString("</cropProductionTargetReport>\n");
  return myString;
}

QString LaModel::toXmlProductionAnimalTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each animal from mProductionRequiredAnimalsMap

  // Loop through the mProductionRequiredAnimalsMap
  QString myString;
  myString += QString("<animalProductionTargetReport>\n");
  QMapIterator<QString, int> myAnimalIterator (mProductionRequiredAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myProductionTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <animal>\n");
    myString += QString("    <guid=\"" + myAnimalIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimal.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myAnimal.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myAnimalParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimalParameter.name()) + "</name>\n");
    myString += QString("    <productionTarget>" + QString::number(myProductionTarget) + "</productionTarget>\n");
    myString += QString("  </animal>\n");
  } // while crop iterator

  myString += QString("</animalProductionTargetReport>\n");
  return myString;
}

QString LaModel::toXmlAreaCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mAreaTargetsCropsMap

  // Loop through the mAreaTargetsCropsMap
  QString myString;
  myString += QString("<cropAreaTargetReport>\n");
  QMapIterator<QString, int> myCropIterator (mAreaTargetsCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myAreaTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <crop>\n");
    myString += QString("    <guid=\"" + myCropIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCrop.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myCrop.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myCropParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myCropParameter.name()) + "</name>\n");
    myString += QString("    <productionTarget>" + QString::number(myAreaTarget) + "</productionTarget>\n");
    myString += QString("  </crop>\n");
  } // while crop iterator

  myString+=QString("</cropAreaTargetReport>\n");
  return myString;
}

QString LaModel::toXmlAreaAnimalTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each animal from mAreaTargetsAnimalsMap

  // Loop through the mAreaTargetsAnimalsMap
  QString myString;
  myString += QString("<animalAreaTargetReport>\n");
  QMapIterator<QString, int> myAnimalIterator (mAreaTargetsAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myAreaTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <animal>\n");
    myString += QString("    <guid=\"" + myAnimalIterator.key() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimal.name()) + "</name>\n");
    myString += QString("    <description>" + LaUtils::xmlEncode(myAnimal.description()) + "</description>\n");
    myString += QString("    <parameterGuid=\"" + myAnimalParameter.guid() + "\">\n");
    myString += QString("    <name>" + LaUtils::xmlEncode(myAnimalParameter.name()) + "</name>\n");
    myString += QString("    <productionTarget>" + QString::number(myAreaTarget) + "</productionTarget>\n");
    myString += QString("  </animal>\n");
  } // while crop iterator

  myString += QString("</animalAreaTargetReport>\n");
  return myString;
}
