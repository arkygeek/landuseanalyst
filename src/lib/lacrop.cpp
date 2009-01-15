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
  mCropFodderValue=1000;

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
  mCropFodderValue=theCrop.fodderValue();
  mCropFodderEnergyType=theCrop.cropFodderEnergyType();
  mAreaUnits=theCrop.areaUnits();
  mImageFile=theCrop.imageFile();
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
  mCropFodderValue=theCrop.fodderValue();
  mCropFodderEnergyType=theCrop.cropFodderEnergyType();
  mAreaUnits=theCrop.areaUnits();
  mImageFile=theCrop.imageFile();
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
int LaCrop::fodderValue() const
{
  return mCropFodderValue;
}
EnergyType LaCrop::cropFodderEnergyType() const
{
 return mCropFodderEnergyType; 
}
AreaUnits LaCrop::areaUnits() const
{
  return mAreaUnits;
}
QString LaCrop::imageFile() const
{
  return mImageFile;
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
void LaCrop::setCropFodderValue(int theValue)
{
  mCropFodderValue=theValue;
}
void LaCrop::setCropFodderEnergyType(EnergyType theEnergyType)
{
  mCropFodderEnergyType=theEnergyType;
}
void LaCrop::setAreaUnits(AreaUnits theAreaUnit)
{
  mAreaUnits=theAreaUnit;
}
void LaCrop::setImageFile(QString theImageFileName)
{
  mImageFile=theImageFileName;
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
   //qDebug("top element could not be found!");
  }
  //qDebug("Crop::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("Crop::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mCropYield=QString(myTopElement.firstChildElement("cropYield").text()).toInt();
  mCropCalories=QString(myTopElement.firstChildElement("cropCalories").text()).toInt();
  mCropFodderProduction=QString(myTopElement.firstChildElement("fodderProduction").text()).toInt();
  mCropFodderValue=QString(myTopElement.firstChildElement("fodderCalories").text()).toInt();
  QString myCropFodderEnergyType = QString(myTopElement.firstChildElement("cropFodderEnergyType").text());
  if (myCropFodderEnergyType == "KCalories")
  {
    mCropFodderEnergyType=KCalories;
  }
  else if (myCropFodderEnergyType == "TDN")
  {
    mCropFodderEnergyType=TDN;
  }
  
    QString myAreaUnits = QString(myTopElement.firstChildElement("areaUnits").text());
  if (myAreaUnits == "Dunum")
  {
    mAreaUnits=Dunum;
  }
  else if (myAreaUnits == "Hectare")
  {
    mAreaUnits=Hectare;
  }
  mImageFile=QString(myTopElement.firstChildElement("imageFile").text());
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
  myString+=QString("  <fodderCalories>" + QString::number(mCropFodderValue) + "</fodderCalories>\n");
  
  switch (mCropFodderEnergyType)
  {
    case KCalories:
      myString+=QString("  <cropFodderEnergyType>KCalories</cropFodderEnergyType>\n");
      break;
    case TDN:
      myString+=QString("  <cropFodderEnergyType>TDN</cropFodderEnergyType>\n");
      break;
  }
  
  switch (mAreaUnits)
  {
    case Dunum:
      myString+=QString("  <areaUnits>Dunum</areaUnits>\n");
      break;
    case Hectare:
      myString+=QString("  <areaUnits>Hectare</areaUnits>\n");
      break;
  }
  myString+=QString("  <imageFile>" + LaUtils::xmlEncode(mImageFile) + "</imageFile>\n");
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
  myString+=QString("fodderCalories=>" + QString::number(mCropFodderValue) + "\n");
  QString myCropFodderEnergyType = (mCropFodderEnergyType==0) ? "KCalories" : "TDN";
  myString+=QString("cropFodderEnergyType=>" + myCropFodderEnergyType + "\n");
  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  myString+=QString("yieldUnits=>" + myUnits + "\n");
  return myString;
}

QString LaCrop::toHtml()
{
  QString myString;
  myString+="<h3>Details for " + LaUtils::xmlEncode(mName) + "</h3>";
  //myString+="<p>GUID:" + guid() + "</p>";
  myString+="<table>";
  myString+="<tr><td><b>Description: </b></td><td>" + mDescription + "</td></tr>";
  myString+="<tr><td><b>Avg Yield: </b></td><td>" + QString::number(mCropYield) + "</td></tr>";
  myString+="<tr><td><b>Cals/Kg: </b></td><td>" + QString::number(mCropCalories) + "</td></tr>";
  QString myCropFodderEnergyType = (mCropFodderEnergyType==0) ? "KCalories" : "TDN";
  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  myString+="<tr><td><b>Fodder (kg/" + myUnits + "): </b></td><td>" + QString::number(mCropFodderProduction) + "</td></tr>";
  myString+="<tr><td><b>Fodder Value/Kg: </b></td><td>" + QString::number(mCropFodderValue) + "</td></tr>";
  myString+="<tr><td><b>FodderEnergyType: </b></td><td>" + myCropFodderEnergyType + "</td></tr>";
  myString+="<tr><td><b>AreaUnits: </b></td><td>" + myUnits + "</td></tr>";
  myString+="</table>";
  return myString;
}
