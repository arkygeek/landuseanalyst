/***************************************************************************
                          laplantparameter.cpp  -  description
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
#include "laplantparameter.h"
#include "lautils.h"

LaPlantParameter::LaPlantParameter() : LaSerialisable(), LaGuid()
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
LaPlantParameter::~LaPlantParameter()
{

}

//copy constructor
LaPlantParameter::LaPlantParameter(const LaPlantParameter& thePlantParameter)
{
  mName=thePlantParameter.name();
  mDescription=thePlantParameter.description();
  setGuid(thePlantParameter.guid());
  mPercentTamePlant=thePlantParameter.percentTamePlant();
  mCropRotation = thePlantParameter.cropRotation();
  mFallowRatio = thePlantParameter.fallowRatio();
  mFallowCalories = thePlantParameter.fallowCalories();
  mAreaUnits = thePlantParameter.areaUnits();
  mUseCommonLand = thePlantParameter.useCommonLand();
  mUseSpecificLand = thePlantParameter.useSpecificLand();
}

LaPlantParameter& LaPlantParameter::operator=(const LaPlantParameter& thePlantParameter)
{
  if (this == &thePlantParameter) return *this;   // Gracefully handle self assignment

  mName=thePlantParameter.name();
  mDescription=thePlantParameter.description();
  setGuid(thePlantParameter.guid());
  mPercentTamePlant=thePlantParameter.percentTamePlant();
  mCropRotation = thePlantParameter.cropRotation();
  mFallowRatio = thePlantParameter.fallowRatio();
  mFallowCalories = thePlantParameter.fallowCalories();
  mAreaUnits = thePlantParameter.areaUnits();
  mUseCommonLand = thePlantParameter.useCommonLand();
  mUseSpecificLand = thePlantParameter.useSpecificLand();
  return *this;
}

QString LaPlantParameter::name() const
{
  return mName;
}

QString LaPlantParameter::description() const
{
  return mDescription;
}
int LaPlantParameter::percentTamePlant() const
{
  return mPercentTamePlant;
}
bool LaPlantParameter::cropRotation() const
{
  return mCropRotation;
}
float LaPlantParameter::fallowRatio() const
{
  return mFallowRatio;
}
int LaPlantParameter::fallowCalories() const
{
  return mFallowCalories;
}
int LaPlantParameter::areaUnits() const
{
  return mAreaUnits;
}
bool LaPlantParameter::useCommonLand() const
{
  return mUseCommonLand;
}
bool LaPlantParameter::useSpecificLand() const
{
  return mUseSpecificLand;
}

void LaPlantParameter::setName(QString theName)
{
  mName=theName;
}
void LaPlantParameter::setDescription(QString theDescription)
{
  mDescription=theDescription;
}

void LaPlantParameter::setPercentTamePlant(int thePercentage)
{
  mPercentTamePlant=thePercentage;
}
void LaPlantParameter::setCropRotation(bool theFlag)
{
  mCropRotation=theFlag;
}
void LaPlantParameter::setFallowRatio(float theFallowRatio)
{
  mFallowRatio=theFallowRatio;
}
void LaPlantParameter::setFallowCalories(int theCalories)
{
  mFallowCalories=theCalories;
}
void LaPlantParameter::setAreaUnits(int theIndexValue)
{
  mAreaUnits=theIndexValue;
}
void LaPlantParameter::setUseSpecificLand(bool theFlag)
{
  mUseSpecificLand=theFlag;
}
void LaPlantParameter::setUseCommonLand(bool theFlag)
{
  mUseCommonLand=theFlag;
}

bool LaPlantParameter::fromXml(QString theXml)
{
  qDebug("Loading PlantParameter from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("plantParameter");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  qDebug("PlantParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  qDebug("PlantParameter::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=QString(myTopElement.firstChildElement("name").text());
  mDescription=QString(myTopElement.firstChildElement("description").text());
  mPercentTamePlant=QString(myTopElement.firstChildElement("percentTamePlant").text()).toInt();
  mCropRotation=QString(myTopElement.firstChildElement("cropRotation").text()).toInt();
  mFallowRatio=QString(myTopElement.firstChildElement("fallowRatio").text()).toInt();
  mFallowCalories=QString(myTopElement.firstChildElement("fallowCalories").text()).toInt();
  mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mUseCommonLand=QString(myTopElement.firstChildElement("useUniqueLand").text()).toInt();
  mUseSpecificLand=QString(myTopElement.firstChildElement("useSpecificLand").text()).toInt();
  return true;
}

QString LaPlantParameter::toXml()
{
  QString myString;
  myString+=QString("<plantParameter guid=\"" + guid() + "\">\n");
    myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <percentTamePlant>" + QString::number(mPercentTamePlant) + "</percentTamePlant>\n");
  myString+=QString("  <cropRotation>" + QString::number(mCropRotation) + "</cropRotation>\n");
  myString+=QString("  <fallowRatio>" + QString::number(mFallowRatio) + "</fallowRatio>\n");
  myString+=QString("  <fallowCalories>" + QString::number(mFallowCalories) + "</fallowCalories>\n");
  myString+=QString("  <areaUnits>" + QString::number(mAreaUnits) + "</areaUnits>\n");
  myString+=QString("  <useCommonLand>" + QString::number(mUseCommonLand) + "</useCommonLand>\n");
  myString+=QString("  <useSpecificLand>" + QString::number(mUseSpecificLand) + "</useSpecificLand>\n");
  myString+=QString("</plantParameter>\n");
  return myString;
}

QString LaPlantParameter::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("description=>" + LaUtils::xmlEncode(mDescription) + "\n");
  myString+=QString("percentTamePlant=>" + QString::number(mPercentTamePlant) + "\n");
  myString+=QString("cropRotation=>" + QString::number(mCropRotation) + "\n");
  myString+=QString("fallowRatio=>" + QString::number(mFallowRatio) + "\n");
  myString+=QString("fallowCalories=>" + QString::number(mFallowCalories) + "\n");
  myString+=QString("areaUnits=>" + QString::number(mAreaUnits) + "\n");
  myString+=QString("useCommonLand=>" + QString::number(mUseCommonLand) + "\n");
  myString+=QString("useSpecificLand=>" + QString::number(mUseSpecificLand) + "\n");
  return myString;
}
QString LaPlantParameter::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<p>GUID:" + guid() + "</p>";
  myString+="<p>Description:" + mDescription + "</p>";
   myString+="<p>Percent Tame Plant Diet: "
                    + QString::number(mPercentTamePlant)
                    + "</p>";
  myString+="<p>cropRotation: "
                    + QString::number(mCropRotation)
                    + "</p>";
  myString+="<p>fallowRatio: "
                    +QString::number(mFallowRatio)
                    + "</p>";
  myString+="<p>fallowCalories: "
                    + QString::number(mFallowCalories)
                    + "</p>";
  myString+=("<p>AreaUnits(0=Dunum, 1=Hectare): "
                    + QString::number(mAreaUnits)
                    + "</p>");
  myString+=("<p>useCommonLand: "
                    + QString::number(mUseCommonLand)
                    + "</p>");
  myString+=("<p>useSpecificLand: "
                    + QString::number(mUseSpecificLand)
                    + "</p>");
  return myString;
}
