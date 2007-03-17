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
  mPopulation="Not Set";
  mPeriod=50;
  mProjection=100;
  mEasting=10;
  mNorthing=10;
  mEuclidean=5000;
  mWalkingTime=5000;
  mPathDistance=3500;
  mPrecision=18;
  mDietSlider=5;
  mPlantSlider=1;
  mMeatSlider=12;
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
  mEuclidean=theModel.euclidean();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietSlider=theModel.dietSlider();
  mPlantSlider=theModel.plantSlider();
  mMeatSlider=theModel.meatSlider();
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
  mEuclidean=theModel.euclidean();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietSlider=theModel.dietSlider();
  mPlantSlider=theModel.plantSlider();
  mMeatSlider=theModel.meatSlider();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
  mSpare=theModel.spare();
  return *this;
}

QString LaModel::name() const
{
  return mName;
}
QString LaModel::population() const
{
  return mPopulation;
}
int LaModel::period() const
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
int LaModel::euclidean() const
{
  return mEuclidean;
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
int LaModel::dietSlider() const
{
  return mDietSlider;
}
int LaModel::plantSlider() const
{
  return mPlantSlider;
}
int LaModel::meatSlider() const
{
  return mMeatSlider;
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
void LaModel::setPopulation(QString thePopulation)
{
  mPopulation=thePopulation;
}
void LaModel::setPeriod(int thePercentage)
{
  if (thePercentage > 100) {thePercentage=100;}
  if (thePercentage < 0) {thePercentage=100;}
  mPeriod=thePercentage;
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
void LaModel::setEuclidean(int theCalories)
{
  mEuclidean=theCalories;
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
void LaModel::setDietSlider(int theYears)
{
  mDietSlider=theYears;
}
void LaModel::setPlantSlider(int theInteger)
{
  mPlantSlider=theInteger;
}
void LaModel::setMeatSlider(int theWeeks)
{
  mMeatSlider=theWeeks;
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
  mPopulation=LaUtils::xmlDecode(myTopElement.firstChildElement("population").text());
  mPeriod=QString(myTopElement.firstChildElement("period").text()).toInt();
  mProjection=QString(myTopElement.firstChildElement("projection").text()).toInt();
  mEasting=QString(myTopElement.firstChildElement("easting").text()).toInt();
  mNorthing=QString(myTopElement.firstChildElement("northing").text()).toInt();
  mEuclidean=QString(myTopElement.firstChildElement("euclidean").text()).toInt();
  mWalkingTime=QString(myTopElement.firstChildElement("walkingTime").text()).toInt();
  mPathDistance=QString(myTopElement.firstChildElement("pathDistance").text()).toInt();
  mPrecision=QString(myTopElement.firstChildElement("precision").text()).toInt();
  mDietSlider=QString(myTopElement.firstChildElement("dietSlider").text()).toInt();
  mPlantSlider=QString(myTopElement.firstChildElement("plantSlider").text()).toInt();
  mMeatSlider=QString(myTopElement.firstChildElement("meatSlider").text()).toInt();
  mCaloriesPerPersonDaily=QString(myTopElement.firstChildElement("caloriesPerPersonDaily").text()).toInt();
  mSpare=QString(myTopElement.firstChildElement("spare").text()).toInt();
  return true;
}

QString LaModel::toXml()
{
  QString myString;
  myString+=QString("<model guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <population>" + LaUtils::xmlEncode(mPopulation) + "</population>\n");
  myString+=QString("  <period>" + QString::number(mPeriod) + "</period>\n");
  myString+=QString("  <projection>" + QString::number(mProjection) + "</projection>\n");
  myString+=QString("  <easting>" + QString::number(mEasting) + "</easting>\n");
  myString+=QString("  <northing>" + QString::number(mNorthing) + "</northing>\n");
  myString+=QString("  <euclidean>" + QString::number(mEuclidean) + "</euclidean>\n");
  myString+=QString("  <walkingTime>" + QString::number(mWalkingTime) + "</walkingTime>\n");
  myString+=QString("  <pathDistance>" + QString::number(mPathDistance) + "</pathDistance>\n");
  myString+=QString("  <precision>" + QString::number(mPrecision) + "</precision>\n");
  myString+=QString("  <dietSlider>" + QString::number(mDietSlider) + "</dietSlider>\n");
  myString+=QString("  <plantSlider>" + QString::number(mPlantSlider) + "</plantSlider>\n");
  myString+=QString("  <meatSlider>" + QString::number(mMeatSlider) + "</meatSlider>\n");
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
  myString+=QString("population=>" + LaUtils::xmlEncode(mPopulation) + "\n");
  myString+=QString("period=>" + QString::number(mPeriod) + "\n");
  myString+=QString("projection=>" + QString::number(mProjection) + "\n");
  myString+=QString("easting=>" + QString::number(mEasting) + "\n");
  myString+=QString("northing=>" + QString::number(mNorthing) + "\n");
  myString+=QString("euclidean=>" + QString::number(mEuclidean) + "\n");
  myString+=QString("walkingTime=>" + QString::number(mWalkingTime) + "\n");
  myString+=QString("pathDistance=>" + QString::number(mPathDistance) + "\n");
  myString+=QString("precision=>" + QString::number(mPrecision) + "\n");
  myString+=QString("dietSlider=>" + QString::number(mDietSlider) + "\n");
  myString+=QString("plantSlider=>" + QString::number(mPlantSlider) + "\n");
  myString+=QString("meatSlider=>" + QString::number(mMeatSlider) + "\n");
  myString+=QString("caloriesPerPersonDaily=>" + QString::number(mCaloriesPerPersonDaily) + "\n");
  myString+=QString("spare=>" + QString::number(mSpare) + "\n");
  return myString;
}

QString LaModel::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<p>GUID:" + guid() + "</p>";
  myString+="<p>Population:" + mPopulation + "</p>";
  myString+="<p>Percentage Usable Meat: " + QString::number(mPeriod) + "</p>";
  myString+="<p>Kill Weight: " + QString::number(mProjection) + "</p>";
  myString+="<p>Grow Time: " + QString::number(mEasting) + "</p>";
  myString+="<p>Death Rate: " + QString::number(mNorthing) + "</p>";
  myString+="<p>Calories fostating female: " + QString::number(mEuclidean) + "</p>";
  myString+="<p>Calories foctating female: " + QString::number(mWalkingTime) + "</p>";
  myString+="<p>Calories fovenile: " + QString::number(mPathDistance) + "</p>";
  myString+="<p>Sexual Maturity: " + QString::number(mPrecision) + "</p>";
  myString+="<p>Breeding Expectancy" + QString::number(mDietSlider) + "</p>";
  myString+="<p>Young Per Birth: " + QString::number(mPlantSlider) + "</p>";
  myString+="<p>Weaning Age: " + QString::number(mMeatSlider) + "</p>";
  myString+="<p>Gestation Time: " + QString::number(mCaloriesPerPersonDaily) + "</p>";
  myString+="<p>Estrous Cycle: " + QString::number(mSpare) + "</p>";
  return myString;
}