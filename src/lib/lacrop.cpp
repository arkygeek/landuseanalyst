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
#include "lacrop.h"
#include "lautils.h"

LaCrop::LaCrop() : LaSerialisable(), LaGuid()
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
LaCrop::~LaCrop()
{

}

//copy constructor
LaCrop::LaCrop(const LaCrop& theCrop)
{
  mName=theCrop.name();
  mDescription=theCrop.description();
  setGuid(theCrop.guid());
  mCropYield=theCrop.cropYield();
  mCropCalories=theCrop.cropCalories();
  mCropFodderProduction=theCrop.fodderProduction();
  mCropFodderCalories=theCrop.fodderCalories();
  mYieldUnits=theCrop.yieldUnits();
}

LaCrop& LaCrop::operator=(const LaCrop& theCrop)
{
  if (this == &theCrop) return *this;   // Gracefully handle self assignment

  mName=theCrop.name();
  mDescription=theCrop.description();
  setGuid(theCrop.guid());
  mCropYield=theCrop.cropYield();
  mCropCalories=theCrop.cropCalories();
  mCropFodderProduction=theCrop.fodderProduction();
  mCropFodderCalories=theCrop.fodderCalories();
  mYieldUnits=theCrop.yieldUnits();
  return *this;
}

QString LaCrop::name() const
{
  return mName;
}

QString LaCrop::description() const
{
  return mDescription;
}

int LaCrop::cropYield() const
{
  return mCropYield;
}
int LaCrop::cropCalories() const
{
  return mCropCalories;
}
int LaCrop::fodderProduction() const
{
  return mCropFodderProduction;
}
int LaCrop::fodderCalories() const
{
  return mCropFodderCalories;
}
int LaCrop::yieldUnits() const
{
  return mYieldUnits;
}

void LaCrop::setName(QString theName)
{
  mName=theName;
}

void LaCrop::setDescription(QString theDescription)
{
  mDescription=theDescription;
}

void LaCrop::setCropYield(int theKg)
{
  mCropYield=theKg;
}
void LaCrop::setCropCalories(int theInteger)
{
  mCropCalories=theInteger;
}
void LaCrop::setFodderProduction(int theKg)
{
  mCropFodderProduction=theKg;
}
void LaCrop::setFodderTDN(int theCalories)
{
  mCropFodderCalories=theCalories;
}
void LaCrop::setYieldUnits(int theIndex)
{
  mYieldUnits=theIndex;
}

bool LaCrop::fromXml(QString theXml)
{
  //qDebug("Loading Crop from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("crop");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  //qDebug("Crop::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("Crop::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mCropYield=QString(myTopElement.firstChildElement("cropYield").text()).toInt();
  mCropCalories=QString(myTopElement.firstChildElement("cropCalories").text()).toInt();
  mCropFodderProduction=QString(myTopElement.firstChildElement("fodderProduction").text()).toInt();
  mCropFodderCalories=QString(myTopElement.firstChildElement("fodderCalories").text()).toInt();
  mYieldUnits=QString(myTopElement.firstChildElement("yieldUnits").text()).toInt();
  return true;
}

QString LaCrop::toXml()
{
  QString myString;
  myString+=QString("<crop guid=\"" + guid() + "\">\n");
    myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <cropYield>" + QString::number(mCropYield) + "</cropYield>\n");
  myString+=QString("  <cropCalories>" + QString::number(mCropCalories) + "</cropCalories>\n");
  myString+=QString("  <fodderProduction>" + QString::number(mCropFodderProduction) + "</fodderProduction>\n");
  myString+=QString("  <fodderCalories>" + QString::number(mCropFodderCalories) + "</fodderCalories>\n");
  myString+=QString("  <yieldUnits>" + QString::number(mYieldUnits) + "</yieldUnits>\n");
  myString+=QString("</crop>\n");
  return myString;
}

QString LaCrop::toText()
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
QString LaCrop::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h3 style=\"color:#466aa5; font-size:11pt; font-weight:bold;\">Details for " + LaUtils::xmlEncode(mName) + "</h3></p>";
  //myString+="<p>GUID:" + guid() + "</p>";
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
