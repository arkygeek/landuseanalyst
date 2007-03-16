/***************************************************************************
                          lacropparameter.cpp  -  description
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
#include "lacropparameter.h"
#include "lautils.h"

LaCropParameter::LaCropParameter() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mDescription="Not Set";
  //mCropYield=60;
  //mCropCalories=3000;
  //mCropFodderProduction=50;
  //mCropFodderCalories=1000;
  //mYieldUnits=0;
}
LaCropParameter::~LaCropParameter()
{

}

//copy constructor
LaCropParameter::LaCropParameter(const LaCropParameter& theCropParameter)
{
  mName=theCropParameter.name();
  mDescription=theCropParameter.description();
  setGuid(theCropParameter.guid());
  setCropGuid(theCropParameter.cropGuid());
  mPercentTameCrop=theCropParameter.percentTameCrop();
  mCropRotation = theCropParameter.cropRotation();
  mFallowRatio = theCropParameter.fallowRatio();
  mFallowCalories = theCropParameter.fallowCalories();
  mAreaUnits = theCropParameter.areaUnits();
  mUseCommonLand = theCropParameter.useCommonLand();
  mUseSpecificLand = theCropParameter.useSpecificLand();
}

LaCropParameter& LaCropParameter::operator=(const LaCropParameter& theCropParameter)
{
  if (this == &theCropParameter) return *this;   // Gracefully handle self assignment

  mName=theCropParameter.name();
  mDescription=theCropParameter.description();
  setGuid(theCropParameter.guid());
  setCropGuid(theCropParameter.cropGuid());
  mPercentTameCrop=theCropParameter.percentTameCrop();
  mCropRotation = theCropParameter.cropRotation();
  mFallowRatio = theCropParameter.fallowRatio();
  mFallowCalories = theCropParameter.fallowCalories();
  mAreaUnits = theCropParameter.areaUnits();
  mUseCommonLand = theCropParameter.useCommonLand();
  mUseSpecificLand = theCropParameter.useSpecificLand();
  return *this;
}

QString LaCropParameter::name() const
{
  return mName;
}

QString LaCropParameter::description() const
{
  return mDescription;
}

QString LaCropParameter::cropGuid() const
{
  return mCropGuid;
}

int LaCropParameter::percentTameCrop() const
{
  return mPercentTameCrop;
}
bool LaCropParameter::cropRotation() const
{
  return mCropRotation;
}
float LaCropParameter::fallowRatio() const
{
  return mFallowRatio;
}
int LaCropParameter::fallowCalories() const
{
  return mFallowCalories;
}
int LaCropParameter::areaUnits() const
{
  return mAreaUnits;
}
bool LaCropParameter::useCommonLand() const
{
  return mUseCommonLand;
}
bool LaCropParameter::useSpecificLand() const
{
  return mUseSpecificLand;
}

void LaCropParameter::setName(QString theName)
{
  mName=theName;
}
void LaCropParameter::setDescription(QString theDescription)
{
  mDescription=theDescription;
}

void LaCropParameter::setCropGuid(QString theGuid)
{
  mCropGuid = theGuid;
}

void LaCropParameter::setPercentTameCrop(int thePercentage)
{
  mPercentTameCrop=thePercentage;
}
void LaCropParameter::setCropRotation(bool theFlag)
{
  mCropRotation=theFlag;
}
void LaCropParameter::setFallowRatio(float theFallowRatio)
{
  mFallowRatio=theFallowRatio;
}
void LaCropParameter::setFallowCalories(int theCalories)
{
  mFallowCalories=theCalories;
}
void LaCropParameter::setAreaUnits(int theIndexValue)
{
  mAreaUnits=theIndexValue;
}
void LaCropParameter::setUseSpecificLand(bool theFlag)
{
  mUseSpecificLand=theFlag;
}
void LaCropParameter::setUseCommonLand(bool theFlag)
{
  mUseCommonLand=theFlag;
}

bool LaCropParameter::fromXml(QString theXml)
{
  //qDebug("Loading CropParameter from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("cropParameter");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  //qDebug("CropParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("CropParameter::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mCropGuid=LaUtils::xmlDecode(myTopElement.firstChildElement("crop").text());
  mPercentTameCrop=QString(myTopElement.firstChildElement("percentTameCrop").text()).toInt();
  mCropRotation=QString(myTopElement.firstChildElement("cropRotation").text()).toInt();
  mFallowRatio=QString(myTopElement.firstChildElement("fallowRatio").text()).toFloat();
  mFallowCalories=QString(myTopElement.firstChildElement("fallowCalories").text()).toInt();
  mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mUseCommonLand=QString(myTopElement.firstChildElement("useCommonLand").text()).toInt();
  mUseSpecificLand=QString(myTopElement.firstChildElement("useSpecificLand").text()).toInt();
  return true;
}

QString LaCropParameter::toXml()
{
  QString myString;
  myString+=QString("<cropParameter guid=\"" + guid() + "\">\n");
    myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <crop>" + LaUtils::xmlEncode(mCropGuid) + "</crop>\n");
  myString+=QString("  <percentTameCrop>" + QString::number(mPercentTameCrop) + "</percentTameCrop>\n");
  myString+=QString("  <cropRotation>" + QString::number(mCropRotation) + "</cropRotation>\n");
  myString+=QString("  <fallowRatio>" + QString::number(mFallowRatio) + "</fallowRatio>\n");
  myString+=QString("  <fallowCalories>" + QString::number(mFallowCalories) + "</fallowCalories>\n");
  myString+=QString("  <areaUnits>" + QString::number(mAreaUnits) + "</areaUnits>\n");
  myString+=QString("  <useCommonLand>" + QString::number(mUseCommonLand) + "</useCommonLand>\n");
  myString+=QString("  <useSpecificLand>" + QString::number(mUseSpecificLand) + "</useSpecificLand>\n");
  myString+=QString("</cropParameter>\n");
  return myString;
}

QString LaCropParameter::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("description=>" + LaUtils::xmlEncode(mDescription) + "\n");
  myString+=QString("crop=>" + mCropGuid + "\n");
  myString+=QString("percentTameCrop=>" + QString::number(mPercentTameCrop) + "\n");
  myString+=QString("cropRotation=>" + QString::number(mCropRotation) + "\n");
  myString+=QString("fallowRatio=>" + QString::number(mFallowRatio) + "\n");
  myString+=QString("fallowCalories=>" + QString::number(mFallowCalories) + "\n");
  myString+=QString("areaUnits=>" + QString::number(mAreaUnits) + "\n");
  myString+=QString("useCommonLand=>" + QString::number(mUseCommonLand) + "\n");
  myString+=QString("useSpecificLand=>" + QString::number(mUseSpecificLand) + "\n");
  return myString;
}
QString LaCropParameter::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<table>";
  //  myString+="<tr><td><b>GUID:</th><td>" + guid() + "</td></tr>";
  myString+="<tr><td><b>Description: </th><td>" + mDescription + "</p>";
  myString+="<tr><td><b>Percent Tame Crop Diet: </th><td>" + QString::number(mPercentTameCrop) + "</td></tr>";
  myString+="<tr><td><b>cropRotation: </th><td>" + QString::number(mCropRotation) + "</td></tr>";
  myString+="<tr><td><b>fallowRatio: </th><td>" + QString::number(mFallowRatio) + "</td></tr>";
  myString+="<tr><td><b>fallowCalories: </th><td>" + QString::number(mFallowCalories) + "</td></tr>";
  myString+=("<tr><td><b>AreaUnits(0=Dunum, 1=Hectare): </th><td>" + QString::number(mAreaUnits) + "</td></tr>");
  myString+=("<tr><td><b>useCommonLand: </th><td>" + QString::number(mUseCommonLand) + "</td></tr>");
  myString+=("<tr><td><b>useSpecificLand: </th><td>" + QString::number(mUseSpecificLand) + "</td></tr>");
  myString+="</table>";
  return myString;
}
