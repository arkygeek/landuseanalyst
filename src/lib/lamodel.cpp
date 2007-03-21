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
  mEasting=10;
  mNorthing=10;
  mEuclideanDistance=5000;
  mWalkingTime=5000;
  mPathDistance=3500;
  mPrecision=18;
  mDietPercent=5;
  mPlantPercent=1;
  mMeatPercent=12;
  mCaloriesPerPersonDaily=120;
  mSpare=21;
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
int LaModel::euclideanDistance() const
{
  return mEuclideanDistance;
}
int LaModel::walkingTime() const
{
  return mWalkingTime;
}
int LaModel::pathDistance() const
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

void LaModel::setProjection(int theKg)
{
  mProjection=theKg;
}
void LaModel::setEasting(int theWeeks)
{
  mEasting=theWeeks;
}
void LaModel::setNorthing(int thePercentage)
{
  mNorthing=thePercentage;
}
void LaModel::setEuclideanDistance(int theCalories)
{
  mEuclideanDistance=theCalories;
}
void LaModel::setWalkingTime(int theCalories)
{
  mWalkingTime=theCalories;
}
void LaModel::setPathDistance(int theCalories)
{
  mPathDistance=theCalories;
}
void LaModel::setPrecision(int theMonths)
{
  mPrecision=theMonths;
}
void LaModel::setDietPercent(int theYears)
{
  mDietPercent=theYears;
}
void LaModel::setPlantPercent(int theInteger)
{
  mPlantPercent=theInteger;
}
void LaModel::setMeatPercent(int theWeeks)
{
  mMeatPercent=theWeeks;
}
void LaModel::setCaloriesPerPersonDaily(int theDays)
{
  mCaloriesPerPersonDaily=theDays;
}
void LaModel::setSpare(int theDays)
{
  mSpare=theDays;
}

bool LaModel::fromXml(QString theXml)
{
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
  mEuclideanDistance=QString(myTopElement.firstChildElement("euclideanDistance").text()).toInt();
  mWalkingTime=QString(myTopElement.firstChildElement("walkingTime").text()).toInt();
  mPathDistance=QString(myTopElement.firstChildElement("pathDistance").text()).toInt();
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
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<p>GUID:" + guid() + "</p>";
  myString+="<p>Population:" + QString::number(mPopulation) + "</p>";
  myString+="<p>Percentage Usable Meat: " + LaUtils::xmlEncode(mPeriod) + "</p>";
  myString+="<p>Kill Weight: " + QString::number(mProjection) + "</p>";
  myString+="<p>Grow Time: " + QString::number(mEasting) + "</p>";
  myString+="<p>Death Rate: " + QString::number(mNorthing) + "</p>";
  myString+="<p>Calories fostating female: " + QString::number(mEuclideanDistance) + "</p>";
  myString+="<p>Calories foctating female: " + QString::number(mWalkingTime) + "</p>";
  myString+="<p>Calories fovenile: " + QString::number(mPathDistance) + "</p>";
  myString+="<p>Sexual Maturity: " + QString::number(mPrecision) + "</p>";
  myString+="<p>Breeding Expectancy" + QString::number(mDietPercent) + "</p>";
  myString+="<p>Young Per Birth: " + QString::number(mPlantPercent) + "</p>";
  myString+="<p>Weaning Age: " + QString::number(mMeatPercent) + "</p>";
  myString+="<p>Gestation Time: " + QString::number(mCaloriesPerPersonDaily) + "</p>";
  myString+="<p>Estrous Cycle: " + QString::number(mSpare) + "</p>";
  return myString;
}
