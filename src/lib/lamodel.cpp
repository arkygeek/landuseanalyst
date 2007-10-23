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
#include <QDebug>

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
  mFallowRatio=theModel.fallowRatio();
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
  mFallowRatio=theModel.fallowRatio();
  return *this;
}

QString LaModel::name()           const { return mName;}
QString LaModel::period()         const { return mPeriod;}
int  LaModel::population()        const { return mPopulation;}
int  LaModel::projection()        const { return mProjection;}
int  LaModel::easting()           const { return mEasting;}
int  LaModel::northing()          const { return mNorthing;}
bool LaModel::euclideanDistance() const { return mEuclideanDistance;}
bool LaModel::walkingTime()       const { return mWalkingTime;}
bool LaModel::pathDistance()      const { return mPathDistance;}
int  LaModel::precision()         const { return mPrecision;}
int  LaModel::dietPercent()       const { return mDietPercent;}
int  LaModel::plantPercent()      const
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
int LaModel::meatPercent() const { return mMeatPercent;}
int LaModel::caloriesPerPersonDaily()                      const { return mCaloriesPerPersonDaily;          }
int LaModel::foodValueCommonLand()                         const { return mCommonGrazingTDN;                }

QMap <QString, int> LaModel::animalCalorieTargetsMap()     const { return mCaloriesProvidedByAnimalsMap;    }
QMap <QString, int> LaModel::animalFeedRequirementsMap()   const { return mTDNMap;                          }
QMap <QString, int> LaModel::animalProductionTargetsMap()  const { return mProductionRequiredAnimalsMap;    }
QMap <QString, int> LaModel::animalAreaTargetsMap()        const { return mAreaTargetsAnimalsMap;           }
QMap <QString, int> LaModel::cropCalorieTargetsMap()       const { return mCaloriesProvidedByCropsMap;      }
QMap <QString, int> LaModel::cropProductionTargetsMap()    const { return mProductionRequiredCropsMap;      }
QMap <QString, int> LaModel::cropAreaTargetsMap()          const { return mAreaTargetsCropsMap;             }

QMap <QString, QString> LaModel::calcsAnimalsMap()               { return mCalcsAnimalsMap;}
QMap <QString, QString> LaModel::calcsCropsMap()                 { return mCalcsCropsMap;}

void LaModel::setFallowStatus           (Status theStatus)       { mFallowStatus=theStatus;                 }
void LaModel::setFallowRatio            (float theRatio)         { mFallowRatio=theRatio;                   }
void LaModel::setName                   (QString theName)        { mName=theName;                           }
void LaModel::setPopulation             (int thePopulation)      { mPopulation=thePopulation;               }
void LaModel::setPeriod                 (QString thePeriod)      { mPeriod=thePeriod;                       }
void LaModel::setProjection             (int theIndex)           { mProjection=theIndex;                    }
void LaModel::setEasting                (int theEasting)         { mEasting=theEasting;                     }
void LaModel::setNorthing               (int theNorthing)        { mNorthing=theNorthing;                   }
void LaModel::setEuclideanDistance      (bool theBool)           { mEuclideanDistance=theBool;              }
void LaModel::setWalkingTime            (bool theBool)           { mWalkingTime=theBool;                    }
void LaModel::setPathDistance           (bool theBool)           { mPathDistance=theBool;                   }
void LaModel::setPrecision              (int thePrecision)       { mPrecision=thePrecision;                 }
void LaModel::setDietPercent            (int thePercent)         { mDietPercent=thePercent;                 }
void LaModel::setCropPercent            (int thePercent)         { mPercentOfDietThatIsFromCrops=thePercent;}
void LaModel::setMeatPercent            (int thePercent)         { mMeatPercent=thePercent;                 }
void LaModel::setCaloriesPerPersonDaily (int theCalories)        { mCaloriesPerPersonDaily=theCalories;     }
void LaModel::setCommonLandAreaUnits    (AreaUnits theAreaUnits) { mCommonLandAreaUnits = theAreaUnits;     }
void LaModel::setCommonLandValue        (int theTDN, AreaUnits theAreaUnits)
{
  mCommonGrazingTDN = LaUtils::convertAreaToHectares(theAreaUnits, theTDN);
}
void LaModel::setAnimals(QMap<QString,QString> theAnimals)       { mAnimalsMap = theAnimals;}
void LaModel::setCrops(QMap<QString,QString> theCrops)           { mCropsMap = theCrops;}

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
  myString+="<h1>Model Report</h1>";
  myString+="<h3>" + LaUtils::xmlEncode(mName) + "</h3>";
  //myString+="GUID:" + guid() + "<br />";
  myString+="<br>Population:" + QString::number(mPopulation) + "</br>";
  myString+="<br>Period: " + LaUtils::xmlEncode(mPeriod) + "</br>";
  myString+="<br>Projection: " + QString::number(mProjection) + "</br>";
  myString+="<br>Easting: " + QString::number(mEasting) + "</br>";
  myString+="<br>Northing: " + QString::number(mNorthing) + "</br>";
  myString+="<br>Euclidean Distance: " + QString::number(mEuclideanDistance) + "</br>";
  myString+="<br>Walking Time: " + QString::number(mWalkingTime) + "</br>";
  myString+="<br>Path Distance: " + QString::number(mPathDistance) + "</br>";
  myString+="<br>Precision: " + QString::number(mPrecision) + "</br>";
  myString+="<br>Diet Percent" + QString::number(mDietPercent) + "</br>";
  myString+="<br>Plant Percent: " + QString::number(mPercentOfDietThatIsFromCrops) + "</br>";
  myString+="<br>Meat Percent: " + QString::number(mMeatPercent) + "</br>";
  myString+="<br>Calories Per Person Daily: " + QString::number(mCaloriesPerPersonDaily) + "</br>";
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
    myString += "<br>";
    myString += myAnimal.toHtml();
    myString += "</br>";
    LaAnimalParameter myParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    myString += "<br>";
    myString += myParameter.toHtml();
    myString += "</br>";
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
  //logMessage("method ==> void LaModel::DoCalculations()");
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
  initialiseTDNMap();

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
  initialiseCalcsCropsMap();
}
void LaModel::adjustAnimalTargetsForFodder()
{
  //logMessage("method ==> void LaModel::adjustAnimalTargetsForFodder()");
  // after serious consideration, I have decided to implement fodder later.
  // it is not as important as getting the rest of the project working.
}
int LaModel::caloriesFromCrops()
{
  //logMessage("method ==> int LaModel::caloriesFromCrops()");
  float myDietComposition = 0.01 * ( 100 - mDietPercent );
  float myCropPercent = 0.01 * ( plantPercent() );
  float myCropOverallContributionToDiet = myDietComposition * myCropPercent;
  float myCalorieTarget = population() * (mCaloriesPerPersonDaily/1000.) * 365.; // kcalories
  float myCropCalorieTarget = myCalorieTarget * myCropOverallContributionToDiet;
  int myReturnValue = static_cast<int> (myCropCalorieTarget);
  logMessage("Overall Crop Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

int LaModel::caloriesFromTameMeat()
{
  float myDietComposition=0.01*dietPercent();
  float myMeatPercent=0.01*meatPercent();
  float myAnimalOverallContributionToDiet=myDietComposition * myMeatPercent;
  float myCalorieTarget= population() * (mCaloriesPerPersonDaily/1000.) * 365.; // kcalories
  float myTameMeatCalorieTarget=myCalorieTarget * myAnimalOverallContributionToDiet;
  int myReturnValue = static_cast<int>(myTameMeatCalorieTarget);
  //logMessage("method ==> int LaModel::caloriesFromTameMeat()");
  logMessage("Overall Tame Meat Target: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

int LaModel::countCrops()
{
  //logMessage("method ==> int LaModel::countCrops()");
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
  //logMessage("method ==> int LaModel::countCrops()");
  //logMessage("Crop Count: " + QString::number(myCropCounter).toLocal8Bit());
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
  //logMessage("method ==> int LaModel::countAnimals()");
  //logMessage("Animal Count: " + QString::number(myAnimalCounter).toLocal8Bit());

  return myAnimalCounter;
}

int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)
{
  LaCropParameter myCropParameter = LaUtils::getCropParameter(theCropParameterGuid);
  float myCropPercent = 0.01 * myCropParameter.percentTameCrop();
  float myCropCalorieTarget=caloriesFromCrops()*myCropPercent;
  int myReturnValue = static_cast<int>(myCropCalorieTarget);
  ///@TODO remove this debugging stuff
  //logMessage("method ==> int LaModel::caloriesProvidedByTheCrop(QString theCropParameterGuid)");
  logMessage("Crop Parameter Guid that was passed here: " + theCropParameterGuid.toLocal8Bit());
  logMessage("Crop Parameter Name: " + myCropParameter.name().toLocal8Bit());
  logMessage("myCropParameter.percentTameCrop() is giving a result of:" + QString::number(myCropParameter.percentTameCrop()).toLocal8Bit());
  logMessage("crop percent: " + QString::number(myCropPercent).toLocal8Bit());
  logMessage("Calorie Target float: " + QString::number(myCropCalorieTarget).toLocal8Bit());
  logMessage("Calorie Target int: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)
{
  LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(theAnimalParameterGuid);
  float myAnimalPercent = 0.01 * myAnimalParameter.percentTameMeat();
  float myAnimalCalorieTarget = caloriesFromTameMeat() * myAnimalPercent;
  int myReturnValue = static_cast<int>(myAnimalCalorieTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::caloriesProvidedByTheAnimal(QString theAnimalParameterGuid)");
  logMessage("Animal Parameter Guid: " + myAnimalParameter.guid().toLocal8Bit());
  logMessage("Animal Parameter Name: " + myAnimalParameter.name().toLocal8Bit());
  logMessage("Calorie Target: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}
int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)
{
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  float myCropProductionTarget = theCalorieTarget / (myCrop.cropCalories() / 1000.); //kcalories
  int myReturnValue = static_cast<int>(myCropProductionTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget)");
  logMessage("Crop Guid: " + myCrop.guid().toLocal8Bit());
  logMessage("Crop Name: " + myCrop.name().toLocal8Bit());
  logMessage("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)
{
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = (theCalorieTarget / (myAnimal.meatFoodValue()/1000.)) / (0.01 * myAnimal.usableMeat()); // kcalories
  int myReturnValue = static_cast<int>(myAnimalProductionTarget);
  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget)");
  logMessage("Animal Guid: " + myAnimal.guid().toLocal8Bit());
  logMessage("Animal Name: " + myAnimal.name().toLocal8Bit());
  logMessage("Production Target: " + QString::number(myReturnValue).toLocal8Bit());
  return myReturnValue;
}

int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)
{
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);
  AreaUnits myAreaUnits = myCrop.areaUnits();
  qDebug() << "    LaModel::getAreaTargetsCrops AreaUnits== " << myAreaUnits;
  int myCropYieldHectares = LaUtils::convertAreaToHectares(myAreaUnits, myCrop.cropYield());
  QString myCropParameterGuid = mCropsMap.value(theCropGuid);
  LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
  float myFallowRatio = myCropParameter.fallowRatio();
  float myCropAreaTarget = (theProductionTarget / myCropYieldHectares) * (1.0 + myFallowRatio);
  int myReturnValue = static_cast<int>(myCropAreaTarget);

  ///@TODO remove this debugging stuff
  logMessage("method ==> int LaModel::getAreaTargetsCrops(QString theCropGuid, int theProductionTarget)");
  logMessage("Crop Guid: " + myCrop.guid().toLocal8Bit());
  logMessage("Crop Name: " + myCrop.name().toLocal8Bit());
  logMessage("Area Target is the production target of: " + QString::number(theProductionTarget).toLocal8Bit());
  logMessage(" Divided by the crop yield of " + QString::number(myCropYieldHectares).toLocal8Bit());
  logMessage(" which gives a result of: " + QString::number(myReturnValue).toLocal8Bit());
  logMessage("before adjusting, value yield was: " + QString::number(myCrop.cropYield()).toLocal8Bit());
  logMessage("after adjusting for area units, yield was: " + QString::number(myCropYieldHectares).toLocal8Bit());

return myReturnValue;
}

int LaModel::requiredTDN(QString theAnimalGuid)
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
  float myTotalMothersTDNRequired = myTotalMothers * myAnimal.gestating();
  float myTotalJuvenilesTDNRequired = myTotalJuveniles * myAnimal.juvenile();
  float myTDNNeededToFeedAnimals = myTotalMothersTDNRequired + myTotalJuvenilesTDNRequired;
  int myReturnValue = static_cast<int>(myTDNNeededToFeedAnimals);

  // log report
  logMessage("method ==> int LaModel::requiredTDN(QString theAnimalGuid)");
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
  logMessage("Total Adult Females TDN(Kg) = " + QString::number (myTotalMothersTDNRequired).toLocal8Bit());
  logMessage("Total Juveniles TDN(Kg) = " + QString::number (myTotalJuvenilesTDNRequired).toLocal8Bit());
  logMessage("Total TDN (Kg) Needed To Feed Animals = " + QString::number(myTDNNeededToFeedAnimals).toLocal8Bit());
  logMessage("method ==> int LaModel::requiredTDN(QString theAnimalGuid)");
  logMessage("Animal: " + myAnimal.name().toLocal8Bit());
  logMessage("Breeding Stock: " + QString::number(myTotalMothers).toLocal8Bit());
  logMessage("Juveniles: " + QString::number(myTotalJuveniles).toLocal8Bit());
  logMessage("Kg TDN needed annually to feed the entire herd: " +
      QString::number(myReturnValue).toLocal8Bit());
  logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
  return myReturnValue;
}

QString LaModel::reportForCrop(QString theCropGuid)
{
  LaCrop myCrop = LaUtils::getCrop(theCropGuid);

  QString myReport;
  myReport += "Details for " + myCrop.name();
  myReport += "\n";
  myReport += "Calorie Target: " + QString::number(mCaloriesProvidedByCropsMap.value(theCropGuid));
  myReport += "\n";
  myReport += "Prod'n Target(Kg): " + QString::number(mProductionRequiredCropsMap.value(theCropGuid));
  myReport += "\n";
  myReport += "Area Target: " + QString::number(mAreaTargetsCropsMap.value(theCropGuid));
  myReport += "\n";

  logMessage(myReport.toLocal8Bit());
  return myReport;

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
  float myTotalMothersTDNRequired = myTotalMothers * (myAnimal.gestating()/1000.) * 365.; // kcalories
  float myTotalJuvenilesTDNRequired = myTotalJuveniles * (myAnimal.juvenile()/1000.) * 365.; // kcalories
  float myTDNNeededToFeedAnimals = myTotalMothersTDNRequired + myTotalJuvenilesTDNRequired;

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
  myReport += "TDN (Kg) Req'd Adult: " + QString::number(static_cast <int>(myTotalMothersTDNRequired));
  myReport += "\n";
  myReport += "TDN (Kg) Req'd Juveniles: " + QString::number(static_cast <int>(myTotalJuvenilesTDNRequired));
  myReport += "\n";
  myReport += "Total TDN (Kg) Req'd: " + QString::number(static_cast <int> (myTDNNeededToFeedAnimals));
  myReport += "\n";
  myReport += "Area Target: " + QString::number(mAreaTargetsAnimalsMap.value(theAnimalGuid));
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

void LaModel::initialiseTDNMap()
{
  logMessage("method ==> void LaModel::initialiseTDNMap()");
  mTDNMap.clear();
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    mTDNMap.insert(myAnimalGuid,requiredTDN(myAnimalGuid));
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
  mCommonCropLand = 0;
  mAreaTargetsCropsMap.clear();
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast<int>(mProductionRequiredCropsMap.value(myCropGuid));
    int myAreaTarget = getAreaTargetsCrops(myCropGuid, myProductionTarget);
    mAreaTargetsCropsMap.insert(myCropGuid,myAreaTarget);

    QString myCropParameterGuid = mCropsMap.value(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);

    mCommonCropLand = (myCropParameter.useCommonLand() == true) ? mCommonCropLand + myAreaTarget : mCommonCropLand;
  }
    mAreaTargetsCropsMap.insert("CommonTarget",static_cast<int>(mCommonCropLand));
}

void LaModel::initialiseCalcsCropsMap()
{
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myReport = reportForCrop(myCropGuid);
    logMessage(myReport.toLocal8Bit());
    mCalcsCropsMap.insert(myCropGuid, myReport);
  }
  mCalcsCropsMap.insert("Common Land", QString::number(mCommonCropLand));
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
  mCalcsAnimalsMap.insert("Common Land", QString::number(mCommonGrazingLandAreaTarget));
}

void LaModel::initialiseAreaTargetsAnimalsMap()
{ // this also returns an area target for common land
  logMessage("method ==> void LaModel::initialiseAreaTargetsAnimalsMap()");
  logMessage("Common Grazing Land TDN: " + QString::number(static_cast<int>(mCommonGrazingTDN)).toLocal8Bit());
  mAreaTargetsAnimalsMap.clear();
  mCommonGrazingLandTDNTarget= 0;
  //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    logMessage("Animal: " + myAnimal.name().toLocal8Bit());
    AreaUnits mySpecificAreaUnits = myAnimalParameter.areaUnits();

    float myTDNSpecific = LaUtils::convertAreaToHectares(mySpecificAreaUnits, myAnimalParameter.TDNSpecificGrazingLand());

    float myTDNCommon   = mCommonGrazingTDN;
    qDebug() << "   +++   myTDNSpecific = " << myTDNSpecific;
    qDebug() << "   +++   myTDNCommon   = " << mCommonGrazingTDN;

    // check to see if this animal needs any additional food
    if (mTDNMap[myAnimalGuid] > 0) // yes, the animal needs more food
    {
      logMessage("Animal Needs more Food!");
      // figure out how much grazing land is needed to supply this many calories
      LandBeingGrazed myLandBeingGrazed;
      //int myTDNCommonGrazingLand = myAnimalParameter.TDNCommonGrazingLand();

      myLandBeingGrazed =  (myAnimalParameter.useCommonGrazingLand()==1) ? Common:Unique;

      switch (myLandBeingGrazed)
      {
        case Common:
             {
               logMessage("Animal is grazing Common Land so required TDN is added to common land TDN target");
               mCommonGrazingLandTDNTarget += static_cast<int>(mTDNMap.value(myAnimalGuid));
               logMessage("Cumulative TDN Target for Common Land: " + QString::number(mCommonGrazingLandTDNTarget));
               float myCommonTarget = mTDNMap.value(myAnimalGuid) / myTDNCommon;
               mAreaTargetsAnimalsMap[myAnimalGuid] = static_cast<int>(myCommonTarget);
               break;
             }
        case Unique:
             {
               logMessage("Animal is grazing Unique Land so required TDN is divided by TDN of unique grazing land");
               float myTarget1 = mTDNMap.value(myAnimalGuid) / myTDNSpecific;
               mAreaTargetsAnimalsMap[myAnimalGuid] = static_cast<int>(myTarget1);
               logMessage("The Area Target is: " + QString::number(static_cast<int>(myTarget1)).toLocal8Bit());
               break;
             }
      }
      //int myCaloriesNeeded = static_cast<int>(mTDNMap.value(myAnimalGuid));

      //mProductionRequiredAnimalsMap.insert(myAnimalGuid,getProductionTargetsAnimals(myAnimalGuid, myProductionTarget));
    }
    else // the animal needs no additional food
    {
      logMessage("Animal needs no additional food.");
      mAreaTargetsAnimalsMap[myAnimalGuid] = 0;
    }
    // CHECK FOR AREA UNIT CONVERSION HERE!
    mCommonGrazingLandAreaTarget = mCommonGrazingLandTDNTarget / mCommonGrazingTDN;

  }
    logMessage(" ");
    logMessage("The Final Common Grazing Land Area Target is: " + QString::number(static_cast<int>(mCommonGrazingLandAreaTarget)).toLocal8Bit());
    logMessage(" ");
    mAreaTargetsAnimalsMap.insert("CommonTarget",static_cast<int>(mCommonGrazingLandAreaTarget));
}

Status LaModel::fallowStatus() const
{
  return mFallowStatus;
}

float LaModel::fallowRatio() const
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

  int myHighPriorityCount=0, myMediumPriorityCount=0, myLowPriorityCount=0;
  int   myHighPriorityTDN=0;
  int   myMediumPriorityTDN=0;
  int   myLowPriorityTDN=0;
  // put starting caloric requirements of all used animals into a map
  // for reduction due to grazing of fallow crop land
  // initialiseTDNMap();

  int myTotalFallowTDN=0;

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
            myHighPriorityCount++;
            myHighPriorityTDN += requiredTDN(myAnimalGuid);
            break;
      case  Medium:
            myMediumPriorityCount++;
            myMediumPriorityTDN += requiredTDN(myAnimalGuid);
            break;
      case  Low:
            myLowPriorityCount++;
            myLowPriorityTDN += requiredTDN(myAnimalGuid);
            break;
      case  None:
            break;
      default:
            break;
    } //switch

  } //while animal count
  logMessage("High Priority Animals: " + QString::number(myHighPriorityCount).toLocal8Bit() );
  logMessage("Medium Priority Animals: " + QString::number(myMediumPriorityCount).toLocal8Bit() );
  logMessage("Low Priority Animals: " + QString::number(myLowPriorityCount).toLocal8Bit() );

  logMessage("High Priority Animal Calorie requirements: " + QString::number(myHighPriorityTDN).toLocal8Bit() );
  logMessage("Medium Priority Animal Calorie requirements: " + QString::number(myMediumPriorityTDN).toLocal8Bit() );
  logMessage("Low Priority Animal Calorie requirements: " + QString::number(myLowPriorityTDN).toLocal8Bit() );

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

    AreaUnits myCropAreaUnits = myCrop.areaUnits();
    int myCropYield = LaUtils::convertAreaToHectares(myCropAreaUnits, static_cast<int> (myCrop.cropYield()));
    //QString myCropParameterGuid = mCropsMap.value(theCropGuid);
    //LaCropParameter myCropParameter = LaUtils::getCropParameter(myCropParameterGuid);
    float myFallowRatio = myCropParameter.fallowRatio();
    float myFallowArea = (myCropProductionTarget / myCropYield) * myFallowRatio;

    AreaUnits myFallowAreaUnits = myCropParameter.areaUnits();
    int myFallowTDNBefore = myCropParameter.fallowTDN();
    int myFallowTDN = LaUtils::convertAreaToHectares(myFallowAreaUnits, myFallowTDNBefore);
    float myAvailableFallowTDN = myFallowRatio * myFallowArea * myFallowTDN;

    myTotalFallowTDN += static_cast<int>(myAvailableFallowTDN);
  } // while crop iterator
  logMessage("Total Available Fallow Calories before adjustments: " + QString::number(myTotalFallowTDN).toLocal8Bit());

  // The following three if statements process all of the animals which
  // utilize fallow cropland as grazing land.  It first checks that there
  // is fallow land available, and next allocates the the fallow based on
  // the animals fallow access priority

  // HIGH priority animals get allocated fallow cropland
  if (myTotalFallowTDN > 0)
  {
    Priority myPriority = High;
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowTDN, myHighPriorityTDN);
    logMessage("Remaining Fallow Calories after HIGH adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowTDN = myLeftoverCalories;
  }
  // MEDIUM priority animals get allocated fallow cropland
  if (myTotalFallowTDN > 0)
  {
    Priority myPriority = Medium;
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowTDN, myMediumPriorityTDN);
    logMessage("Remaining Fallow Calories after MED adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowTDN = myLeftoverCalories;
  }
  // LOW priority animals get allocated fallow cropland
  if (myTotalFallowTDN > 0)
  {
    Priority myPriority = Low;
    int myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowTDN, myLowPriorityTDN);
    logMessage("Remaining Fallow Calories after LOW adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowTDN = myLeftoverCalories;
  }
  //int myReturnValue = static_cast<int>(myTotalFallowTDN);
  //return myReturnValue;
}


/* int LaModel::adjustForFodder(LaFoodSource theFoodSources, int theCalsRequired)
{
  // the values given here are percentage of diet, so are easily calculated.
  int myStrawChaffPercentOfDiet = theFoodSources.fodder();
  int myGrainPercentOfDiet = theFoodSources.grain();

} */

int LaModel::doTheFallowAllocation
      (
        Priority thePriority,
        int theAvailableFallowTDN,
        int theTDNNeeded
      )
{
  qDebug() << "TDN Map: " << mTDNMap;
  // when the total number of calories needed by the animals
  // is taken away from the total available calories (from crop fallow),
  // there will be one of two results.
  // 1. the result will be <=0, meaning that additional sources of
  //    food is required for the animals.  (fodder or grazing land)
  // 2. the result will be > 0, meaning that there is enough food value
  //    in the crop fallow to completely feed the animals.
  float myTotalFallowTDN = theAvailableFallowTDN - theTDNNeeded;
  qDebug() << "myTotalFallowTDN: "  << myTotalFallowTDN;
  // set up the conditions for the fallow allocation...
  // there is either enough fallow to feed the animal completely
  // or not enough to feed them completely.  If there is enough,
  // the animal will not be requiring any additional source of
  // calories.  In other words, we won't be needing to graze them
  // on any other land besides the crop fallow.
  Status myFallowStatus;
  myFallowStatus = (myTotalFallowTDN > 0) ? MoreThanEnoughToCompletelySatisfy : NotEnoughToCompletelySatisfy;
  QString myFallowStatusString = (myFallowStatus!=NotEnoughToCompletelySatisfy) ? "More than Enough" : "Not Enough";
  logMessage("Fallow Status: " + myFallowStatusString);
  qDebug () << "FallowStatus: " << myFallowStatus;
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
                mTDNMap[myAnimalGuid] = 0;
              } //endif (fallowUsage(myAnimalGuid)

             } // while animal iterating
             // myTotalFallowTDN += theTDNNeeded;
             break;
          }

    case  NotEnoughToCompletelySatisfy:
          {
            logMessage("CASE: NotEnoughToCompletelySatisfy");
            // because there ARE NO leftover TDN available to feed more critters, this
            // shows that NOT ALL of the animals requirements are met with crop fallow
            // and therefore require more feed so their values in the QMap will be adjusted
            QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
            while (myAnimalIterator.hasNext())
            {
              myAnimalIterator.next();
              logMessage("    Iterating through Animals looking for a match");

              QString myAnimalGuid = myAnimalIterator.key();
              QString myAnimalParameterGuid = myAnimalIterator.value();
              LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
              LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
              int myCurrentAnimalsTDN = mTDNMap.value( myAnimalGuid );
              logMessage("       Current Animal: " + myAnimal.name());
              qDebug() << "        theTDNNeeded: " << theTDNNeeded;
              qDebug() << "        theAvailableFallowTDN: " << theAvailableFallowTDN;
              qDebug() << "        myCurrentAnimalsTDN: " << myCurrentAnimalsTDN;
              if (myAnimalParameter.fallowUsage()==thePriority)
              {
                double myAllottedTDN = ((myCurrentAnimalsTDN / static_cast<float>(theTDNNeeded)) * theAvailableFallowTDN);
                logMessage("Adjusting calories required by: " + myAnimal.name());
                qDebug() << "myAllottedTDN: " << myAllottedTDN;
                logMessage("Allotted TDN from fallow are: " + QString::number(myAllottedTDN));
                logMessage("Original TDN target was: " + QString::number(mTDNMap.value(myAnimalGuid)));
                float myNewTDNTarget = mTDNMap.value(myAnimalGuid) - myAllottedTDN;
                logMessage("New TDN target is: " + QString::number(myNewTDNTarget));
                mTDNMap [myAnimalGuid] = static_cast<int>(myNewTDNTarget);
                myTotalFallowTDN += static_cast<int>(myAllottedTDN);
              } // endif (fallowUsage(myAnimalGuid)==High)

            } // while animal iterating
            logMessage("After allocation, total available TDN from fallow: " + QString::number(myTotalFallowTDN).toLocal8Bit());
            myTotalFallowTDN = 0;
            logMessage("WHICH HAS NOW BEEN SET TO 0");
            break;
          }

    default:
          break;
  } //switch
  return static_cast<int>(myTotalFallowTDN);
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
  myString += QString("<h3> Crop Calorie Targets</h3>\n");
  myString += QString("<table>");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      kCalories\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");

  QMapIterator<QString, int> myCropIterator (mCaloriesProvidedByCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myCalorieTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));

    // add to the QString to create the html file

    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myCalorieTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");


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

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlCalorieAnimalTargets()
{
  // This method returns a QString for an xml file containing the calorie
  // targets for each animal from mCaloriesProvidedByAnimalsMap

  // Loop through the mCaloriesProvidedByAniamlsMap
  QString myString;
  myString += QString("<h3> Animal Calorie Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      kCalories\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, int> myAnimalIterator (mCaloriesProvidedByAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myCalorieTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myCalorieTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");

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
    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlProductionCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mProductionRequiredCropsMap

  // Loop through the mProductionRequiredCropsMap
  QString myString;
  myString += QString("<h3> Crop Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Kg\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, int> myCropIterator (mProductionRequiredCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    int myProductionTarget = static_cast <int>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
    // add to the QString to create the xml file
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myProductionTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");
  } // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlProductionAnimalTargets()
{

  // Sallah, I said *no* camels. That's *five* camels. Can't you count?

  // This method returns a QString for an xml file containing the production
  // targets for each animal from mProductionRequiredAnimalsMap

  // Loop through the mProductionRequiredAnimalsMap
  QString myString;
  myString += QString("<h3> Animal Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Kg\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, int> myAnimalIterator (mProductionRequiredAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    int myProductionTarget = static_cast <int>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    // add to the QString to create the xml file
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myProductionTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");
  } // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlAreaCropTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each crop from mAreaTargetsCropsMap

  // Loop through the mAreaTargetsCropsMap
  QString myString;
  myString += QString("<h3> Crop Area Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Area\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, int> myCropIterator (mAreaTargetsCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    if (myCropGuid != "CommonTarget")
    {
      int myAreaTarget = static_cast <int>(myCropIterator.value());
      LaCrop myCrop = LaUtils::getCrop(myCropGuid);
      LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
      // add to the QString to create the xml file
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + QString::number(myAreaTarget) + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
    else
    {
      QString myAreaTarget = QString::number(mAreaTargetsCropsMap.value("CommonTarget"));
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      CommonTarget\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + myAreaTarget + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
  } // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlAreaAnimalTargets()
{
  // This method returns a QString for an xml file containing the production
  // targets for each animal from mAreaTargetsAnimalsMap

  // Loop through the mAreaTargetsAnimalsMap
  QString myString;
  myString += QString("<h3> Animal Area Targets</h3>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Area\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, int> myAnimalIterator (mAreaTargetsAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    if (myAnimalGuid != "CommonTarget")
    {
      int myAreaTargetUnchanged = static_cast <int>(myAnimalIterator.value());
      LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
      LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
      int myAreaTarget = LaUtils::convertAreaToHectares(myAnimalParameter.areaUnits(), myAreaTargetUnchanged);
      // add to the QString to create the xml file
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + QString::number(myAreaTarget) + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
    else
    {
      QString myAreaTarget = QString::number(mAreaTargetsAnimalsMap.value("CommonTarget"));
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      CommonTarget\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + myAreaTarget + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
  }

    myString += QString("</table>\n");
  return myString;
}

QMap<QString, int> LaModel::getAreaTargetsAnimalsMap()
{
  return mAreaTargetsAnimalsMap;
}

QMap<QString, int> LaModel::getAreaTargetsCropsMap()
{
  return mAreaTargetsCropsMap;
}

//
// Utility functions
//

void LaModel::logMessage(QString theMessage)
{
  emit message(theMessage);
}
