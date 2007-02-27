/***************************************************************************
                          omgserialisable.cpp  -  description
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton
    email                : tim@linfiniti.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
#include <QString>
#include <QDomDocument>
#include <QDomElement>
#include "laplant.h"
#include "lautils.h"

LaPlant::LaPlant() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mDescription="Not Set";
  mCropYield=60;
  mCropCalories=3000;
  mCropFodderProduction=50;
  mCropFodderCalories=1000;
  mYieldUnits=0;
}
LaPlant::~LaPlant()
{

}

//copy constructor
LaPlant::LaPlant(const LaPlant& thePlant)
{
  mName=thePlant.name();
  mDescription=thePlant.description();
  setGuid(thePlant.guid());
  mCropYield=thePlant.cropYield();
  mCropCalories=thePlant.cropCalories();
  mCropFodderProduction=thePlant.fodderProduction();
  mCropFodderCalories=thePlant.fodderCalories();
  mYieldUnits=thePlant.yieldUnits();
}

LaPlant& LaPlant::operator=(const LaPlant& thePlant)
{
  if (this == &thePlant) return *this;   // Gracefully handle self assignment

  mName=thePlant.name();
  mDescription=thePlant.description();
  setGuid(thePlant.guid());
  mCropYield=thePlant.cropYield();
  mCropCalories=thePlant.cropCalories();
  mCropFodderProduction=thePlant.fodderProduction();
  mCropFodderCalories=thePlant.fodderCalories();
  mYieldUnits=thePlant.yieldUnits();
  return *this;
}

QString LaPlant::name() const
{
  return mName;
}

QString LaPlant::description() const
{
  return mDescription;
}

int LaPlant::cropYield() const
{
  return mCropYield;
}
int LaPlant::cropCalories() const
{
  return mCropCalories;
}
int LaPlant::fodderProduction() const
{
  return mCropFodderProduction;
}
int LaPlant::fodderCalories() const
{
  return mCropFodderCalories;
}
int LaPlant::yieldUnits() const
{
  return mYieldUnits;
}

void LaPlant::setName(QString theName)
{
  mName=theName;
}

void LaPlant::setDescription(QString theDescription)
{
  mDescription=theDescription;
}

void LaPlant::setCropYield(int theKg)
{
  mCropYield=theKg;
}
void LaPlant::setCropCalories(int theInteger)
{
  mCropCalories=theInteger;
}
void LaPlant::setFodderProduction(int theKg)
{
  mCropFodderProduction=theKg;
}
void LaPlant::setFodderCalories(int theCalories)
{
  mCropFodderCalories=theCalories;
}
void LaPlant::setYieldUnits(int theIndex)
{
  mYieldUnits=theIndex;
}

bool LaPlant::fromXml(QString theXml)
{
  qDebug("Loading Plant from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("plant");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  qDebug("Plant::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  qDebug("Plant::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mCropYield=QString(myTopElement.firstChildElement("cropYield").text()).toInt();
  mCropCalories=QString(myTopElement.firstChildElement("cropCalories").text()).toInt();
  mCropFodderProduction=QString(myTopElement.firstChildElement("fodderProduction").text()).toInt();
  mCropFodderCalories=QString(myTopElement.firstChildElement("fodderCalories").text()).toInt();
  mYieldUnits=QString(myTopElement.firstChildElement("yieldUnits").text()).toInt();
  return true;
}

QString LaPlant::toXml()
{
  QString myString;
  myString+=QString("<plant guid=\"" + guid() + "\">\n");
    myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <cropYield>" + QString::number(mCropYield) + "</cropYield>\n");
  myString+=QString("  <cropCalories>" + QString::number(mCropCalories) + "</cropCalories>\n");
  myString+=QString("  <fodderProduction>" + QString::number(mCropFodderProduction) + "</fodderProduction>\n");
  myString+=QString("  <fodderCalories>" + QString::number(mCropFodderCalories) + "</fodderCalories>\n");
  myString+=QString("  <yieldUnits>" + QString::number(mYieldUnits) + "</yieldUnits>\n");
  myString+=QString("</plant>\n");
  return myString;
}

QString LaPlant::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("description=>" + LaUtils::xmlEncode(mDescription) + "\n");
  myString+=QString("cropYield=>" + QString::number(mCropYield) + "\n");
  myString+=QString("cropCalories=>" + QString::number(mCropCalories) + "\n");
  myString+=QString("fodderProduction=>" + QString::number(mCropFodderProduction) + "\n");
  myString+=QString("fodderCalories=>" + QString::number(mCropFodderCalories) + "\n");
  myString+=QString("yieldUnits=>" + QString::number(mYieldUnits) + "\n");
  return myString;
}
QString LaPlant::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<p>GUID:" + guid() + "</p>";
  myString+="<p>Description:" + mDescription + "</p>";
   myString+="<p>Average Crop Yield: "
                    + QString::number(mCropYield)
                    + "</p>";
  myString+="<p>Calories per Kg: "
                    + QString::number(mCropCalories)
                    + "</p>";
  myString+="<p>Kg of Fodder produced: "
                    +QString::number(mCropFodderProduction)
                    + "</p>";
  myString+="<p>Calories per Kg in fodder: "
                    + QString::number(mCropFodderCalories)
                    + "</p>";
  myString+=("<p>AreaUnits(0=Dunum, 1=Hectare): "
                    + QString::number(mYieldUnits)
                    + "</p>");
  return myString;
}
