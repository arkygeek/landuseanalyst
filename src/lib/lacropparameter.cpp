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
    //mCropFodderValue=1000;
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
  mSpoilage=theCropParameter.spoilage();
  mReseed=theCropParameter.reseed();
  mCropRotation = theCropParameter.cropRotation();
  mFallowRatio = theCropParameter.fallowRatio();
  mFallowValue = theCropParameter.fallowValue();
  mAreaUnits = theCropParameter.areaUnits();
  mUseCommonLand = theCropParameter.useCommonLand();
  mUseSpecificLand = theCropParameter.useSpecificLand();
  mRasterName = theCropParameter.rasterName();
}

LaCropParameter& LaCropParameter::operator=(const LaCropParameter& theCropParameter)
{
  if (this == &theCropParameter) return *this;     // Gracefully handle self assignment

  mName=theCropParameter.name();
  mDescription=theCropParameter.description();
  setGuid(theCropParameter.guid());
  setCropGuid(theCropParameter.cropGuid());
  mPercentTameCrop=theCropParameter.percentTameCrop();
  mSpoilage=theCropParameter.spoilage();
  mReseed=theCropParameter.reseed();
  mCropRotation = theCropParameter.cropRotation();
  mFallowRatio = theCropParameter.fallowRatio();
  mFallowValue = theCropParameter.fallowValue();
  mAreaUnits = theCropParameter.areaUnits();
  mUseCommonLand = theCropParameter.useCommonLand();
  mUseSpecificLand = theCropParameter.useSpecificLand();
  mRasterName = theCropParameter.rasterName();
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

float LaCropParameter::percentTameCrop() const
{
  return mPercentTameCrop;
}
float LaCropParameter::spoilage() const
{
  return mSpoilage;
}
float LaCropParameter::reseed() const
{
  return mReseed;
}
bool LaCropParameter::cropRotation() const
{
  return mCropRotation;
}
float LaCropParameter::fallowRatio() const
{
  return mFallowRatio;
}
int LaCropParameter::fallowValue() const
{
  return mFallowValue;
}
AreaUnits LaCropParameter::areaUnits() const
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
QString LaCropParameter::rasterName() const
{
  return mRasterName;
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

void LaCropParameter::setPercentTameCrop(float thePercentage)
{
  mPercentTameCrop=thePercentage;
}
void LaCropParameter::setSpoilage(float thePercentage)
{
  mSpoilage=thePercentage;
}
void LaCropParameter::setReseed(float thePercentage)
{
  mReseed=thePercentage;
}
void LaCropParameter::setCropRotation(bool theFlag)
{
  mCropRotation=theFlag;
}
void LaCropParameter::setFallowRatio(float theFallowRatio)
{
  mFallowRatio=theFallowRatio;
}
void LaCropParameter::setFallowValue(int theKg)
{
  mFallowValue=theKg;
}
void LaCropParameter::setAreaUnits(AreaUnits theAreaUnit)
{
  mAreaUnits=theAreaUnit;
}
void LaCropParameter::setUseSpecificLand(bool theFlag)
{
  mUseSpecificLand=theFlag;
}
void LaCropParameter::setUseCommonLand(bool theFlag)
{
  mUseCommonLand=theFlag;
}

void LaCropParameter::setRasterName(QString theRasterName)
{
  mRasterName=theRasterName;
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
     //qDebug("top element could not be found!");
  }
    //qDebug("CropParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
    //qDebug("CropParameter::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mCropGuid=LaUtils::xmlDecode(myTopElement.firstChildElement("crop").text());
  mPercentTameCrop=QString(myTopElement.firstChildElement("percentTameCrop").text()).toFloat();
  mSpoilage=QString(myTopElement.firstChildElement("spoilage").text()).toFloat();
  mReseed=QString(myTopElement.firstChildElement("reseed").text()).toFloat();
  mCropRotation=QString(myTopElement.firstChildElement("cropRotation").text()).toInt();
  mFallowRatio=QString(myTopElement.firstChildElement("fallowRatio").text()).toFloat();
  mFallowValue=QString(myTopElement.firstChildElement("fallowValue").text()).toInt();

  QString myAreaUnits = QString(myTopElement.firstChildElement("areaUnits").text());
  if (myAreaUnits == "Dunum")
  {
    mAreaUnits=Dunum;
  }
  else if (myAreaUnits == "Hectare")
  {
    mAreaUnits=Hectare;
  }
    //mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mUseCommonLand=QString(myTopElement.firstChildElement("useCommonLand").text()).toInt();
  mUseSpecificLand=QString(myTopElement.firstChildElement("useSpecificLand").text()).toInt();
  mRasterName=LaUtils::xmlDecode(myTopElement.firstChildElement("rasterName").text());
  return true;
}

QString LaCropParameter::toXml()
{
  QString myString;
  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  myString+=QString("<cropParameter guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <crop>" + LaUtils::xmlEncode(mCropGuid) + "</crop>\n");
  myString+=QString("  <percentTameCrop>" + QString::number(mPercentTameCrop) + "</percentTameCrop>\n");
  myString+=QString("  <spoilage>" + QString::number(mSpoilage) + "</spoilage>\n");
  myString+=QString("  <reseed>" + QString::number(mReseed) + "</reseed>\n");
  myString+=QString("  <cropRotation>" + QString::number(mCropRotation) + "</cropRotation>\n");
  myString+=QString("  <fallowRatio>" + QString::number(mFallowRatio) + "</fallowRatio>\n");
  myString+=QString("  <fallowValue>" + QString::number(mFallowValue) + "</fallowValue>\n");
  myString+=QString("  <areaUnits>" + myUnits + "</areaUnits>\n");
  myString+=QString("  <useCommonLand>" + QString::number(mUseCommonLand) + "</useCommonLand>\n");
  myString+=QString("  <useSpecificLand>" + QString::number(mUseSpecificLand) + "</useSpecificLand>\n");
  myString+=QString("  <rasterName>" + LaUtils::xmlEncode(mRasterName) + "</rasterName>\n");
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
  myString+=QString("spoilage=>" + QString::number(mSpoilage) + "\n");
  myString+=QString("reseed=>" + QString::number(mReseed) + "\n");
  QString myCropRotation = (mCropRotation==0) ? "None" : "Used";
  myString+=QString("cropRotation=>" + myCropRotation + "\n");
  myString+=QString("fallowRatio=>" + QString::number(mFallowRatio) + "\n");

  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  myString+=QString("fallowValue kg/" + myUnits + "=>" + QString::number(mFallowValue) + "\n");
    //myString+=QString("areaUnits=>" + QString::number(mAreaUnits) + "\n");

  QString myLandUsed = (mUseCommonLand==1) ? "Common" : "Specific";
  myString+=QString("Landused=>" + myLandUsed + "\n");
    //myString+=QString("useSpecificLand=>" + QString::number(mUseSpecificLand) + "\n");
  myString+=QString("rasterName=>" + LaUtils::xmlEncode(mRasterName) + "\n");
  return myString;
}
QString LaCropParameter::toHtml()
{
  QString myString;
  QString myCropRotation = (mCropRotation==0) ? "None" : "Used";
  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  QString myLandUsed = (mUseCommonLand==1) ? "Common" : "Specific";
  QString myRasterName = (mUseCommonLand==1) ? "LaCropCommonMask" : mRasterName;

  myString+="<h3 >Details for " + LaUtils::xmlEncode(mName) + "</h3>";
  myString+="<table>";    //  myString+="<tr><td><b>GUID:</th><td>" + guid() + "</td></tr>";
  myString+="<tr><td><b>Description: </b></td><td>" + mDescription + "</td></tr>";
  myString+="<tr><td><b>Raster Mask: </b></td><td>" + mRasterName + "</td></tr>";
  myString+="<tr><td><b>Percent Tame Crop Diet: </b></td><td>" + QString::number(mPercentTameCrop) + "</td></tr>";
  myString+="<tr><td><b>Percent of Spoilage: </b></td><td>" + QString::number(mSpoilage) + "</td></tr>";
  myString+="<tr><td><b>Percent for reseeding: </b></td><td>" + QString::number(mReseed) + "</td></tr>";
  myString+="<tr><td><b>cropRotation: </b></td><td>" + myCropRotation + "</td></tr>";
  myString+="<tr><td><b>fallowRatio: </b></th><td>" + QString::number(mFallowRatio) + "</td></tr>";
  myString+="<tr><td><b>Fallow Value kg/" + myUnits + ": </b></td><td>" + QString::number(mFallowValue) + "</td></tr>";

  myString+=("<tr><td><b>" + myLandUsed + " Land Raster: </b></td><td>" + myRasterName + "</td></tr>");
  myString+="</table>";
  return myString;
}
