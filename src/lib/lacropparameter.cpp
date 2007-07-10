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
  mFallowTDN = theCropParameter.fallowTDN();
  mAreaUnits = theCropParameter.areaUnits();
  mUseCommonLand = theCropParameter.useCommonLand();
  mUseSpecificLand = theCropParameter.useSpecificLand();
  mRasterName = theCropParameter.rasterName();
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
  mFallowTDN = theCropParameter.fallowTDN();
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
int LaCropParameter::fallowTDN() const
{
  return mFallowTDN;
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
void LaCropParameter::setFallowTDN(int theKg)
{
  mFallowTDN=theKg;
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
  mFallowTDN=QString(myTopElement.firstChildElement("fallowTDN").text()).toInt();
  mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mUseCommonLand=QString(myTopElement.firstChildElement("useCommonLand").text()).toInt();
  mUseSpecificLand=QString(myTopElement.firstChildElement("useSpecificLand").text()).toInt();
  mRasterName=LaUtils::xmlDecode(myTopElement.firstChildElement("rasterName").text());
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
  myString+=QString("  <fallowTDN>" + QString::number(mFallowTDN) + "</fallowTDN>\n");
  myString+=QString("  <areaUnits>" + QString::number(mAreaUnits) + "</areaUnits>\n");
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
  QString myCropRotation = (mCropRotation==0) ? "None" : "Used";
  myString+=QString("cropRotation=>" + myCropRotation + "\n");
  myString+=QString("fallowRatio=>" + QString::number(mFallowRatio) + "\n");

  QString myUnits = (mAreaUnits==0) ? "Dunum" : "Hectare";
  myString+=QString("fallowTDN kg/" + myUnits + "=>" + QString::number(mFallowTDN) + "\n");
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
  myString+="<table>";  //  myString+="<tr><td><b>GUID:</th><td>" + guid() + "</td></tr>";
  myString+="<tr><td><b>Description: </td><td>" + mDescription + "</td></tr>";
  myString+="<tr><td><b>Raster Mask: </td><td>" + mRasterName + "</td></tr>";
  myString+="<tr><td><b>Percent Tame Crop Diet: </td><td>" + QString::number(mPercentTameCrop) + "</td></tr>";
  myString+="<tr><td><b>cropRotation: </td><td>" + myCropRotation + "</td></tr>";
  myString+="<tr><td><b>fallowRatio: </th><td>" + QString::number(mFallowRatio) + "</td></tr>";
  myString+="<tr><td><b>Fallow TDN kg/" + myUnits + ": </td><td>" + QString::number(mFallowTDN) + "</td></tr>";

  myString+=("<tr><td><b>" + myLandUsed + " Land Raster: </td><td>" + myRasterName + "</td></tr>");
  myString+="</table>";
  return myString;
}
