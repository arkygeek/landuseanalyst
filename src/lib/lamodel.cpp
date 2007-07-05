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

LaModel::LaModel() : QObject(),  LaSerialisable(), LaGuid()
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
int LaModel::foodValueCommonLand() const
{
  return mCommonGrazingLandFoodValue;
}
QMap <QString, int> LaModel::animalCalorieTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mCaloriesProvidedByAnimalsMap;
}
QMap <QString, int> LaModel::animalFeedRequirementsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mCaloriesRequiredByAnimalsMap;
}
QMap <QString, int> LaModel::animalProductionTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mProductionRequiredAnimalsMap;
}
QMap <QString, int> LaModel::animalAreaTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mAreaTargetsAnimalsMap;
}
QMap <QString, int> LaModel::cropCalorieTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mCaloriesProvidedByCropsMap;
}
QMap <QString, int> LaModel::cropProductionTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mProductionRequiredCropsMap;
}
QMap <QString, int> LaModel::cropAreaTargetsMap() const
{
  // need to implement logic to ensure that the calculations have been performed!
  return mAreaTargetsCropsMap;
}

QMap <QString, QString> LaModel::calcsAnimalsMap()
{
  initialiseCaloriesProvidedByCropsMap();
  initialiseCaloriesProvidedByAnimalsMap();
  initialiseCaloriesRequiredByAnimalsMap();
  initialiseProductionRequiredAnimalsMap();
  initialiseProductionRequiredCropsMap();
  initialiseAreaTargetsCropsMap();
  allocateFallowGrazingLand();
  adjustAnimalTargetsForFodder();
  initialiseAreaTargetsAnimalsMap();
  initialiseCalcsAnimalsMap();
  return mCalcsAnimalsMap;
}

QMap <QString, QString> LaModel::calcsCropsMap() const
{
  return mCalcsCropsMap;
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

void LaModel::setCommonLandValue(int theValue)
{
  mCommonGrazingLandFoodValue=theValue;
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
  logMessage("method ==> bool LaModel::fromXml(QString theXml)");
  QString myFlag;
  logMessage("Loading model from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("model");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    logMessage("top element could not be found!");
  }
  logMessage("Model::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  logMessage("Model::fromXml - guid set to : " + guid().toLocal8Bit());
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
  logMessage("method ==> QString LaModel::toXml()");
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
  logMessage("method ==> QString LaModel::toText()");
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
  logMessage("method ==> QString LaModel::toHtml()");
  QString myString;
  myString+="<p align=\"center\"><h1 style=\"color:#466aa5; font-size:14pt; font-weight:bold;\">Model Report</h1><p/>";
  myString+="<p align=\"center\"><h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\">" + LaUtils::xmlEncode(mName) + "</h3><p/>";
  //myString+="GUID:" + guid() + "<br />";
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

void LaModel::clearCalcMaps()
{
  mCalcsAnimalsMap.clear();
  mCalcsCropsMap.clear();
}

void LaModel::DoCalculations()
{
  mCalcsAnimalsMap.clear();
  mCalcsCropsMap.clear();
  logMessage("method ==> void LaModel::DoCalculations()");
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
  initialiseCalcsAnimalsMap();
}
void LaModel::adjustAnimalTargetsForFodder()
{
  logMessage("method ==> void LaModel::adjustAnimalTargetsForFodder()");
  // after serious consideration, I have decided to implement fodder later.
  // it is not as important as getting the rest of the project working.
}
int LaModel::caloriesFromCrops()
{
  logMessage("method ==> int LaModel::caloriesFromCrops()");
  float myDietComposition = 0.01 * ( 100 - mDietPercent );
  float myCropPercent = 0.01 * ( plantPercent() );
  float myCropOverallContributionToDiet = myDietComposition * myCropPercent;
  float myCalorieTarget = population() * (mCaloriesPerPersonDaily/1000.) * 365.; // kcalories
  float myCropCalorieTarget = myCalorieTarget * myCropOverallContributionToDiet;
  int myReturnValue = static_cast<int> (myCropCalorieTarget);
  logMessage("Overall Crop Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesFromTameMeat()
{
  logMessage("method ==> int LaModel::caloriesFromTameMeat()");
  float myDietComposition=0.01*dietPercent();
  float myMeatPercent=0.01*meatPercent();
  float myAnimalOverallContributionToDiet=myDietComposition * myMeatPercent;
  float myCalorieTarget= population() * (mCaloriesPerPersonDaily/1000.) * 365.; // kcalories
  float myTameMeatCalorieTarget=myCalorieTarget * myAnimalOverallContributionToDiet;
  int myReturnValue = static_cast<int>(myTameMeatCalorieTarget);
  logMessage("method ==> int LaModel::caloriesFromTameMeat()");
  logMessage("Overall Tame Meat Target: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::countCrops()
{
  logMessage("method ==> int LaModel::countCrops()");
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
  logMessage("method ==> int LaModel::countCrops()");
  logMessage("Crop Count: " + QString::number(myCropCounter).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myCropCounter;
}

int LaModel::countAnimals()
{
  logMessage("method ==> int LaModel::countAnimals()");
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
  logMessage("method ==> int LaModel::countAnimals()");
  logMessage("Animal Count: " + QString::number(myAnimalCounter).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myAnimalCounter;
}

int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)
{
  logMessage("method ==> int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)");
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myCropPercent = 0.01 * myCropParameter.percentTameCrop();
  float myCropCalorieTarget=caloriesFromCrops()*myCropPercent;
  int myReturnValue = static_cast<int>(myCropCalorieTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)");
  logMessage("Crop Parameter Guid that was passed here: " + theCropParameterGuid.toLocal8Bit());
  logMessage("Crop Parameter Name: " + myCropParameter.name().toLocal8Bit());
  logMessage("myCropParameter.percentTameCrop() is giving a result of:" + QString::number(myCropParameter.percentTameCrop()).toLocal8Bit());
  logMessage("crop percent: " + QString::number(myCropPercent).toLocal8Bit());
  logMessage("Calorie Target float: " + QString::number(myCropCalorieTarget).toLocal8Bit());
  logMessage("Calorie Target int: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)
{
  logMessage("method ==> int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)");
  LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(theAnimalParameterGuid);
  float myAnimalPercent = 0.01 * myAnimalParameter.percentTameMeat();
  float myAnimalCalorieTarget = caloriesFromTameMeat() * myAnimalPercent;
  int myReturnValue = static_cast<int>(myAnimalCalorieTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)");
  logMessage("Animal Parameter Guid: " + myAnimalParameter.guid().toLocal8Bit());
  logMessage("Animal Parameter Name: " + myAnimalParameter.name().toLocal8Bit());
  logMessage("Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}
int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)
{
  logMessage("method ==> int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)");
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropProductionTarget = theCalorieTarget / (myCrop.cropCalories() / 1000.); //kcalories
  int myReturnValue = static_cast<int>(myCropProductionTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)");
  logMessage("Crop Guid: " + myCrop.guid().toLocal8Bit());
  logMessage("Crop Name: " + myCrop.name().toLocal8Bit());
  logMessage("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)
{
  logMessage("method ==> int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)");
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = (theCalorieTarget / (myAnimal.meatFoodValue()/1000.)) / (0.01 * myAnimal.usableMeat()); // kcalories
  int myReturnValue = static_cast<int>(myAnimalProductionTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)");
  logMessage("Animal Guid: " + myAnimal.guid().toLocal8Bit());
  logMessage("Animal Name: " + myAnimal.name().toLocal8Bit());
  logMessage("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)
{
  logMessage("method ==> int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)");
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropAreaTarget = theProductionTarget / myCrop.cropYield();
  int myReturnValue = static_cast<int>(myCropAreaTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)");
  logMessage("Crop Guid: " + myCrop.guid().toLocal8Bit());
  logMessage("Crop Name: " + myCrop.name().toLocal8Bit());
  logMessage("Area Target is the production target of: " + QString::number(theProductionTarget).toLocal8Bit());
  logMessage(" Divided by the crop yield of " + QString::number(myCrop.cropYield()).toLocal8Bit());
  logMessage(" which gives a result of: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
  return myReturnValue;
}

int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)
{ // this is the generic animal model
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = getProductionTargetsAnimals (theAnimalGuid, static_cast <int> (mCaloriesProvidedByAnimalsMap.value (theAnimalGuid)));


  float myAnimalsRequired=(myAnimalProductionTarget / myAnimal.killWeight()) / (myAnimal.usableMeat()*.01);
  float myBirthsPerYear = 365.0 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + (myAnimal.weaningAge() * 7.0));
  float myOffspringPerMotherYearly = myBirthsPerYear * myAnimal.youngPerBirth() * (1.0-(0.01*myAnimal.deathRate()));
  float myMothersNeededStepOne = myAnimalsRequired/myOffspringPerMotherYearly;
  float myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly)/2;
  float myFemalesStepOne = myMalesStepOne;
  float myMotherReplacementsPerYear = myMothersNeededStepOne/myAnimal.breedingExpectancy();
  float myAdditionalMothers = (myMotherReplacementsPerYear/myOffspringPerMotherYearly)*2;
  float myMalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
  float myFemalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
  float myTotalMothers = myMothersNeededStepOne+myAdditionalMothers;
  float myTotalMales = myMalesStepOne+myMalesStepTwo;
  float myTotalFemales = myFemalesStepOne-myFemalesStepTwo;
  float myTotalJuveniles = myTotalMales+myTotalFemales;
  float myTotalMothersCaloriesRequired = myTotalMothers * (myAnimal.gestating()/1000.) * 365.; // kcalories
  float myTotalJuvenilesCaloriesRequired = myTotalJuveniles * (myAnimal.juvenile()/1000.) * 365.; // kcalories
  float myTotalCaloriesNeededToFeedAnimals = myTotalMothersCaloriesRequired + myTotalJuvenilesCaloriesRequired;
  int myReturnValue = static_cast<int>(myTotalCaloriesNeededToFeedAnimals);

  // log report
  logMessage("method ==> int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)");
  logMessage("animal prodn target = calorie target of animal / food value");
  logMessage("mCaloriesProvidedByAnimalsMap.value(theAnimalGuid): " + QString::number(mCaloriesProvidedByAnimalsMap.value(theAnimalGuid)).toLocal8Bit());
  logMessage("myAnimal.meatFoodValue(): " + QString::number(myAnimal.meatFoodValue()/1000.).toLocal8Bit());
  logMessage("myAnimalProductionTarget = " + QString::number(myAnimalProductionTarget).toLocal8Bit());
  logMessage("slaughter animals reqd: " + QString::number(myAnimalsRequired).toLocal8Bit());
  logMessage("BirthEventsPerYear: " + QString::number(myBirthsPerYear).toLocal8Bit());
  logMessage("OffspringPerMotherYearly = " + QString::number(myOffspringPerMotherYearly).toLocal8Bit());
  logMessage("MothersNeededStepOne = " + QString::number(myMothersNeededStepOne).toLocal8Bit());
  logMessage("MalesStepOne = " + QString::number(myMalesStepOne).toLocal8Bit());
  logMessage("FemalesStepOne = " + QString::number(myFemalesStepOne).toLocal8Bit());
  logMessage("MotherReplacementsPerYear = " + QString::number(myMotherReplacementsPerYear).toLocal8Bit());
  logMessage("AdditionalMothers = " + QString::number(myAdditionalMothers).toLocal8Bit());
  logMessage("MalesStepTwo = " + QString::number(myMalesStepTwo).toLocal8Bit());
  logMessage("FemalesStepTwo = " + QString::number(myFemalesStepTwo).toLocal8Bit());
  logMessage("TotalMothers = " + QString::number(myTotalMothers).toLocal8Bit());
  logMessage("TotalMales = " + QString::number(myTotalMales).toLocal8Bit());
  logMessage("TotalFemales = " + QString::number(myTotalFemales).toLocal8Bit());
  logMessage("TotalJuveniles = " + QString::number(myTotalJuveniles).toLocal8Bit());
  logMessage("TotalMothersCaloriesRequired = " + QString::number (myTotalMothersCaloriesRequired).toLocal8Bit());
  logMessage("TotalJuvenilesCaloriesRequired = " + QString::number (myTotalJuvenilesCaloriesRequired).toLocal8Bit());
  logMessage("Total kiloCalories Needed To Feed Animals = " + QString::number(myTotalCaloriesNeededToFeedAnimals).toLocal8Bit());
  logMessage("method ==> int LaModel::caloriesNeededByAnimal(QString theAnimalGuid)");
  logMessage("Animal: " + myAnimal.name().toLocal8Bit());
  logMessage("Breeding Stock: " + QString::number(myTotalMothers).toLocal8Bit());
  logMessage("Juveniles: " + QString::number(myTotalJuveniles).toLocal8Bit());
  logMessage("Calories needed annually to feed the entire herd: " +
      QString::number(myReturnValue).toLocal8Bit());
  logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
  return myReturnValue;
}


QString LaModel::reportForAnimal(QString theAnimalGuid)
{ // this is the animal model calculation results
  QString myReport;
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget=getProductionTargetsAnimals( theAnimalGuid, static_cast <int>(mCaloriesProvidedByAnimalsMap.value(theAnimalGuid)));
  float myAnimalsRequired=(myAnimalProductionTarget / myAnimal.killWeight()) / (myAnimal.usableMeat()*.01);
  float myBirthsPerYear = 365.0 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + (myAnimal.weaningAge() * 7.0));
  float myOffspringPerMotherYearly = myBirthsPerYear * myAnimal.youngPerBirth() * (1.0-(0.01*myAnimal.deathRate()));
  float myMothersNeededStepOne = myAnimalsRequired/myOffspringPerMotherYearly;
  float myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly)/2;
  float myFemalesStepOne = myMalesStepOne;
  float myMotherReplacementsPerYear = myMothersNeededStepOne/myAnimal.breedingExpectancy();
  float myAdditionalMothers = (myMotherReplacementsPerYear/myOffspringPerMotherYearly)*2;
  float myMalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
  float myFemalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2;
  float myTotalMothers = myMothersNeededStepOne+myAdditionalMothers;
  float myTotalMales = myMalesStepOne+myMalesStepTwo;
  float myTotalFemales = myFemalesStepOne-myFemalesStepTwo;
  float myTotalJuveniles = myTotalMales+myTotalFemales;
  float myTotalMothersCaloriesRequired = myTotalMothers * (myAnimal.gestating()/1000.) * 365.; // kcalories
  float myTotalJuvenilesCaloriesRequired = myTotalJuveniles * (myAnimal.juvenile()/1000.) * 365.; // kcalories
  float myTotalCaloriesNeededToFeedAnimals = myTotalMothersCaloriesRequired + myTotalJuvenilesCaloriesRequired;

  myReport += "Details for " + myAnimal.name();
  myReport += "\n";
  myReport += "Calorie Target: " + QString::number(mCaloriesProvidedByAnimalsMap.value(theAnimalGuid));
  myReport += "\n";
  myReport += "Prod'n Target(Kg): " + QString::number(myAnimalProductionTarget);
  myReport += "\n";
  myReport += "slaughter animals: " + QString::number(myAnimalsRequired);
  myReport += "\n";
  myReport += "Births/Year: " + QString::number(myBirthsPerYear);
  myReport += "\n";
  myReport += "Offspring/Mother: " + QString::number(myOffspringPerMotherYearly);
  myReport += "\n";
  myReport += "Adult Females: " + QString::number(myTotalMothers);
  myReport += "\n";
  myReport += "Juveniles: " + QString::number(myTotalJuveniles);
  myReport += "\n";
  myReport += "Cals Req'd Adult: " + QString::number(myTotalMothersCaloriesRequired);
  myReport += "\n";
  myReport += "Cals Req'd Juveniles: " + QString::number(myTotalJuvenilesCaloriesRequired);
  myReport += "\n";
  myReport += "Total kiloCalories: " + QString::number(myTotalCaloriesNeededToFeedAnimals);
  myReport += "\n";
  logMessage(myReport.toLocal8Bit());
  return myReport;
}


int LaModel::getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget)
{
  logMessage("method ==> int LaModel::getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget)");
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myAvailableFallow = myCropParameter.fallowRatio() * theAreaTarget;
  int myReturnValue = static_cast<int>(myAvailableFallow);
  logMessage("crop parameter: " + myCropParameter.name().toLocal8Bit());
  logMessage("fallow land for the crop: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

void LaModel::initialiseCaloriesProvidedByAnimalsMap()
{
  logMessage("method ==> void LaModel::initialiseCaloriesProvidedByAnimalsMap()");
  mCaloriesProvidedByAnimalsMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = mAnimalsMap.value(myAnimalGuid);
    mCaloriesProvidedByAnimalsMap.insert(myAnimalGuid,caloriesProvidedByTheAnimal(myAnimalParameterGuid));
    logMessage("Animal Guid: " + myAnimalGuid.toLocal8Bit());
    logMessage("Calories Provided: " + QString::number(caloriesProvidedByTheAnimal(myAnimalParameterGuid)).toLocal8Bit());
  }
}

void LaModel::initialiseCaloriesProvidedByCropsMap()
{
  logMessage("method ==> void LaModel::initialiseCaloriesProvidedByCropsMap()");
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
  logMessage("method ==> void LaModel::initialiseCaloriesRequiredByAnimalsMap()");
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
  logMessage("method ==> void LaModel::initialiseProductionRequiredCropsMap()");
  mProductionRequiredCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast<int>(mCaloriesProvidedByCropsMap.value(myCropGuid));
    mProductionRequiredCropsMap.insert(myCropGuid,getProductionTargetsCrops(myCropGuid, myProductionTarget));
    logMessage("cropGuid: " + QString::number(mProductionRequiredCropsMap.value(myCropGuid)).toLocal8Bit());
    logMessage("ProductionTarget: " + QString::number(mProductionRequiredCropsMap.value(myCropGuid)).toLocal8Bit());
    logMessage("cropGuid: " + myCropGuid.toLocal8Bit());

  }
}

void LaModel::initialiseProductionRequiredAnimalsMap()
{
  logMessage("method ==> void LaModel::initialiseProductionRequiredAnimalsMap()");
  mProductionRequiredAnimalsMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myCalorieTarget = static_cast<int>(mCaloriesProvidedByAnimalsMap.value(myAnimalGuid));
    mProductionRequiredAnimalsMap.insert(myAnimalGuid,getProductionTargetsAnimals(myAnimalGuid, myCalorieTarget));
  }
}

void LaModel::initialiseAreaTargetsCropsMap()
{
  logMessage("method ==> void LaModel::initialiseAreaTargetsCropsMap()");
  mAreaTargetsCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast<int>(mProductionRequiredCropsMap.value(myCropGuid));
    mAreaTargetsCropsMap.insert(myCropGuid,getAreaTargetsCrops(myCropGuid, myProductionTarget));
  }
}

void LaModel::initialiseCalcsAnimalsMap()
{ // this also returns an area target for common land
  //mCalcsAnimalsMap.clear();
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myReport = reportForAnimal(myAnimalGuid);
    logMessage(myReport.toLocal8Bit());
    mCalcsAnimalsMap.insert(myAnimalGuid, myReport);
  }
}

void LaModel::initialiseAreaTargetsAnimalsMap()
{ // this also returns an area target for common land
  logMessage("method ==> void LaModel::initialiseAreaTargetsAnimalsMap()");
  logMessage("Common Grazing LAnd Food Value: " + QString::number(static_cast<int>(mCommonGrazingLandFoodValue)).toLocal8Bit());
  mAreaTargetsAnimalsMap.clear();
  mCommonGrazingLandCalorieTarget= 0;
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    logMessage("XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx");
    logMessage("Animal: " + myAnimal.name().toLocal8Bit());
    // check to see if this animal needs any additional food
    if (mCaloriesRequiredByAnimalsMap[myAnimalGuid] > 0) // yes, the animal needs more food
    {
      logMessage("Animal Needs more Food!");
      // figure out how much grazing land is needed to supply this many calories
      LandBeingGrazed myLandBeingGrazed;
      myLandBeingGrazed =  (myAnimalParameter.useCommonGrazingLand()==1) ? Common:Unique;

      switch (myLandBeingGrazed)
      {
        case Common:
               logMessage("Animal is grazing Common Land so required calories are added to common land target");
               mCommonGrazingLandCalorieTarget += static_cast<int>(mCaloriesRequiredByAnimalsMap.value(myAnimalGuid));
               mAreaTargetsAnimalsMap[myAnimalGuid]=0;
               break;
        case Unique:
               logMessage("Animal is grazing Unique Land so required calories are divided by food value of unique grazing land");
               float myTarget = mCaloriesRequiredByAnimalsMap.value(myAnimalGuid) / myAnimalParameter.foodValueOfSpecificGrazingLand();
               mAreaTargetsAnimalsMap[myAnimalGuid] = static_cast<int>(myTarget);
               logMessage("The Area Target is: " + QString::number(static_cast<int>(myTarget)).toLocal8Bit());
               break;
      }
      //int myCaloriesNeeded = static_cast<int>(mCaloriesRequiredByAnimalsMap.value(myAnimalGuid));

      //mProductionRequiredAnimalsMap.insert(myAnimalGuid,getProductionTargetsAnimals(myAnimalGuid, myProductionTarget));
    }
    else // the animal needs no additional food
    {
      logMessage("Animal needs no additional food.");
      mAreaTargetsAnimalsMap[myAnimalGuid] = 0;
    }
    mCommonGrazingLandAreaTarget = mCommonGrazingLandCalorieTarget / mCommonGrazingLandFoodValue;

    logMessage("XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx");
  }
    logMessage("The Common Grazing Land Area Target is: " + QString::number(static_cast<int>(mCommonGrazingLandAreaTarget)).toLocal8Bit());
}

Status LaModel::fallowStatus() const
{
  return mFallowStatus;
}

void LaModel::allocateFallowGrazingLand()
{
  logMessage("method ==> void LaModel::allocateFallowGrazingLand()");
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
  logMessage("High Priority Animals: " + QString::number(myAnimalsHighPriorityCount).toLocal8Bit() );
  logMessage("Medium Priority Animals: " + QString::number(myAnimalsMediumPriorityCount).toLocal8Bit() );
  logMessage("Low Priority Animals: " + QString::number(myAnimalsLowPriorityCount).toLocal8Bit() );

  logMessage("High Priority Animal Calorie requirements: " + QString::number(myAnimalsHighPriorityCalorieRequirements).toLocal8Bit() );
  logMessage("Medium Priority Animal Calorie requirements: " + QString::number(myAnimalsMediumPriorityCalorieRequirements).toLocal8Bit() );
  logMessage("Low Priority Animal Calorie requirements: " + QString::number(myAnimalsLowPriorityCalorieRequirements).toLocal8Bit() );

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
    float myCropCalorieTarget = caloriesFromCrops() * myCropPercent; // already kcalories
    float myCropProductionTarget = myCropCalorieTarget / (myCrop.cropCalories()/1000.);
    float myCropAreaTarget = myCropProductionTarget / myCrop.cropYield();
    float myAvailableFallowCalories = myCropParameter.fallowRatio() * myCropAreaTarget * myCropParameter.fallowCalories();

    myTotalFallowCalories += static_cast<int>(myAvailableFallowCalories);
  } // while crop iterator
  logMessage("Total Available Fallow Calories before adjustments: " + QString::number(myTotalFallowCalories).toLocal8Bit());
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
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsHighPriorityCalorieRequirements);
    logMessage("Remaining Fallow Calories after HIGH adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowCalories = myLeftoverCalories;
  }
  // MEDIUM priority animals get allocated fallow cropland
  if (myTotalFallowCalories > 0)
  {
    Priority myPriority = Medium;
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsMediumPriorityCalorieRequirements);
    logMessage("Remaining Fallow Calories after MED adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowCalories = myLeftoverCalories;
  }
  // LOW priority animals get allocated fallow cropland
  if (myTotalFallowCalories > 0)
  {
    Priority myPriority = Low;
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowCalories, myAnimalsLowPriorityCalorieRequirements);
    logMessage("Remaining Fallow Calories after LOW adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowCalories = myLeftoverCalories;
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
  myFallowStatus = (myTotalFallowCalories > 0) ? MoreThanEnoughToCompletelySatisfy : NotEnoughToCompletelySatisfy;
  logMessage("Fallow Status: " + QString(myFallowStatus).toLocal8Bit());
  switch (myFallowStatus)
  {
    case  MoreThanEnoughToCompletelySatisfy:
          {
            logMessage("MoreThanEnoughToCompletelySatisfy");
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
             // myTotalFallowCalories += theTotalCalorificRequirements;
             break;
          }

    case  NotEnoughToCompletelySatisfy:
          {
            logMessage("NotEnoughToCompletelySatisfy");
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
                int myAllottedCalories =
                    static_cast<int>(
                                     (
                                      mCaloriesRequiredByAnimalsMap.value( myAnimalGuid )
                                      / theTotalCalorificRequirements
                                     )
                                     * theAvailableFallowCalories //myTotalFallowCalories
                                    );
                logMessage("Adjusting calories required by: " + myAnimal.name().toLocal8Bit());
                logMessage("Allotted Calories from fallow are: " + QString::number(myAllottedCalories).toLocal8Bit());
                logMessage("Original calorie target was: " + QString::number(mCaloriesRequiredByAnimalsMap.value(myAnimalGuid)).toLocal8Bit());
                float myNewCalorieTarget = mCaloriesRequiredByAnimalsMap.value(myAnimalGuid) - myAllottedCalories;
                logMessage("New calorie target is: " + QString::number(myNewCalorieTarget).toLocal8Bit());
                mCaloriesRequiredByAnimalsMap [myAnimalGuid] = static_cast<int>(myNewCalorieTarget);
                myTotalFallowCalories += myAllottedCalories;
              } //endif (fallowUsage(myAnimalGuid)==High)

            } // while animal iterating
            logMessage("After allocation, total available calories from fallow: " + QString::number(myTotalFallowCalories).toLocal8Bit());
            myTotalFallowCalories = 0;
            logMessage("WHICH HAS NOW BEEN SET TO 0");
            break;
          }

    default:
          break;
  } //switch
  return myTotalFallowCalories;
}



  ////////////////////////////////////////////////////////////////////////
 // The following is all for generating reports on calculation results //
////////////////////////////////////////////////////////////////////////

QString LaModel::toHtmlCalorieCropTargets()
{
  // This method returns a QString for an xml file containing the calorie
  // targets for each crop from mCaloriesProvidedByCropsMap

  // Loop through the mCaloriesProvidedByCropsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Crop Calorie Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Crop</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>kCalories</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");

  QMapIterator<QString, int> myCropIterator (mCaloriesProvidedByCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myCalorieTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));

    // add to the QString to create the html file

    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myCrop.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myCalorieTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");


    // add to the QString to create the xml file
    //myString += QString("  <crop>\n");
    //myString += QString("    <guid=\"" + myCropIterator.key() + "\">\n");
    //myString += QString("    <name>" + LaUtils::xmlEncode(myCrop.name()) + "</name>\n");
    //myString += QString("    <description>" + LaUtils::xmlEncode(myCrop.description()) + "</description>\n");
    //myString += QString("    <parameterGuid=\"" + myCropParameter.guid() + "\">\n");
    //myString += QString("    <name>" + LaUtils::xmlEncode(myCropParameter.name()) + "</name>\n");
    //myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
    //myString += QString("  </crop>\n");
  } // while crop iterator

    myString += QString("</TABLE>\n");
  return myString;
}

QString LaModel::toHtmlCalorieAnimalTargets()
{
  // This method returns a QString for an xml file containing the calorie
  // targets for each animal from mCaloriesProvidedByAnimalsMap

  // Loop through the mCaloriesProvidedByAniamlsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Animal Calorie Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Animal</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>kCalories</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");
  QMapIterator<QString, int> myAnimalIterator (mCaloriesProvidedByAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myCalorieTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myAnimal.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myCalorieTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");

    // add to the QString to create the xml file
    //myString += QString("  <animal>\n");
    //myString += QString("    <guid=\"" + myAnimalIterator.key() + "\">\n");
    //myString += QString("    <name>" + LaUtils::xmlEncode(myAnimal.name()) + "</name>\n");
    //myString += QString("    <description>" + LaUtils::xmlEncode(myAnimal.description()) + "</description>\n");
    //myString += QString("    <parameterGuid=\"" + myAnimalParameter.guid() + "\">\n");
    //myString += QString("    <name>" + LaUtils::xmlEncode(myAnimalParameter.name()) + "</name>\n");
    //myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
    //myString += QString("  </animal>\n");

  } // while animal iterator
    myString += QString("</TABLE>\n");
  return myString;
}

QString LaModel::toHtmlProductionCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mProductionRequiredCropsMap

  // Loop through the mProductionRequiredCropsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Crop Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Crop</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Kg</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");
  QMapIterator<QString, int> myCropIterator (mProductionRequiredCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myCrop.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myProductionTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");
  } // while crop iterator

    myString += QString("</TABLE>\n");
  return myString;
}

QString LaModel::toHtmlProductionAnimalTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each animal from mProductionRequiredAnimalsMap

  // Loop through the mProductionRequiredAnimalsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Animal Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Animal</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Kg</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");
  QMapIterator<QString, int> myAnimalIterator (mProductionRequiredAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myProductionTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myAnimal.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myProductionTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");
  } // while crop iterator

    myString += QString("</TABLE>\n");
  return myString;
}

QString LaModel::toHtmlAreaCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mAreaTargetsCropsMap

  // Loop through the mAreaTargetsCropsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Crop Area Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Crop</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Area</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");
  QMapIterator<QString, int> myCropIterator (mAreaTargetsCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myAreaTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myCrop.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myAreaTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");
  } // while crop iterator

    myString += QString("</TABLE>\n");
  return myString;
}

QString LaModel::toHtmlAreaAnimalTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each animal from mAreaTargetsAnimalsMap

  // Loop through the mAreaTargetsAnimalsMap
  QString myString;
  myString += QString("<h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\"> Animal Area Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("</P>\n");
  myString += QString("<TABLE WIDTH=100% BORDER=1 BORDERCOLOR=\"#000000\" CELLPADDING=4 CELLSPACING=0>\n");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <TR VALIGN=TOP>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Animal</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("    <TH WIDTH=50%>\n");
  myString += QString("      <P>Area</P>\n");
  myString += QString("    </TH>\n");
  myString += QString("  </TR>\n");
  QMapIterator<QString, int> myAnimalIterator (mAreaTargetsAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myAreaTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <TR VALIGN=TOP>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + LaUtils::xmlEncode(myAnimal.name()) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("    <TD WIDTH=50%>\n");
    myString += QString("      <P>" + QString::number(myAreaTarget) + "</P>\n");
    myString += QString("    </TD>\n");
    myString += QString("  </TR>\n");
  } // while crop iterator

    myString += QString("</TABLE>\n");
  return myString;
}

//
// Grass related functions follow ...
//

int LaModel::adjustAreaTargetsCrops()
{
  logMessage("method ==> int LaModel::adjustAreaTargetsCrops()");
  int a;
  return a;
}

void LaModel::getArea(float theArea)
{
  logMessage("method ==> void LaModel::getArea(float theArea)");
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "tempraster";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);

  if (!myProcess.waitForStarted())
  {
    logMessage("The process never started.....aaargh");
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

  logMessage(myString.toLocal8Bit());

  logMessage("The process completed");
}

void LaModel::makeWalkCost(int theX, int theY)
{
  logMessage("method ==> void LaModel::makeWalkCost(int theX, int theY)");
}

void LaModel::makeEuclideanCost(int theX, int theY)
{
  logMessage("method ==> void LaModel::makeEuclideanCost(int theX, int theY)");
}

void LaModel::makePathDistanceCost(int theX, int theY)
{
  logMessage("method ==> void LaModel::makePathDistanceCost(int theX, int theY)");
}

void LaModel::writeMetaData(QString theValue)
{
  logMessage("method ==> void LaModel::writeMetaData(QString theValue)");
}

void LaModel::makeCircle(int theX, int theY)
{
  logMessage("method ==> void LaModel::makeCircle(int theX, int theY");
  // to verify this worked do
  //    d.rast
  //    and check in the pull downlist (if your eyes dont fall out looking at those fonts)
  //    to remove teh file again do:
  //    g.remove rast=circle

  /*
     logMessage("Making crop circle...tweeedee treedee");
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
    logMessage("The process never started.....aaargh");
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

  logMessage(myString.toLocal8Bit());

  logMessage("The process completed");
}

//
// Utility functions
//

void LaModel::logMessage(QString theMessage)
{
  emit message(theMessage);
}
