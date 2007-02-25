/***************************************************************************
                          LaPlantParametersparameters.cpp  -  The plant class
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton  tim@linfiniti.com
                         :     2007 by Jason Jorgenson  arkygeek@gmail.com
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
#include "laplantparameters.h"
#include "lautils.h"

LaPlantParameters::LaPlantParameters() : LaSerialisable(), LaGuid()
{
  setGuid();
}
LaPlantParameters::~LaPlantParameters()
{

}

//copy constructor
LaPlantParameters::LaPlantParameters(const LaPlantParameters& thePlantParameters)
{
  mPercentTamePlant=thePlantParameters.percentTamePlant();
  mCropRotation = thePlantParameters.cropRotation();
  mFallowRatio = thePlantParameters.fallowRatio();
  mFallowCalories = thePlantParameters.fallowCalories();
  mAreaUnits = thePlantParameters.areaUnits();
  mUseCommonLand = thePlantParameters.useCommonLand();
  mUseSpecificLand = thePlantParameters.useSpecificLand();
}

LaPlantParameters& LaPlantParameters::operator=(const LaPlantParameters& thePlantParameters)
{
  if (this == &thePlantParameters) return *this;   // Gracefully handle self assignment
  mPercentTamePlant=thePlantParameters.percentTamePlant();
  mCropRotation = thePlantParameters.cropRotation();
  mFallowRatio = thePlantParameters.fallowRatio();
  mFallowCalories = thePlantParameters.fallowCalories();
  mAreaUnits = thePlantParameters.areaUnits();
  mUseCommonLand = thePlantParameters.useCommonLand();
  mUseSpecificLand = thePlantParameters.useSpecificLand();
  return *this;
}

QString LaPlantParameters::name() const
{
  return mName;
}

int LaPlantParameters::percentTamePlant() const
{
  return mPercentTamePlant;
}
bool LaPlantParameters::cropRotation() const
{
  return mCropRotation;
}
float LaPlantParameters::fallowRatio() const
{
  return mFallowRatio;
}
int LaPlantParameters::fallowCalories() const
{
  return mFallowCalories;
}
int LaPlantParameters::areaUnits() const
{
  return mAreaUnits;
}
bool LaPlantParameters::useCommonLand() const
{
  return mUseCommonLand;
}
bool LaPlantParameters::useSpecificLand() const
{
  return mUseSpecificLand;
}

void LaPlantParameters::setPercentTamePlant(int thePercentage)
{
  mPercentTamePlant=thePercentage;
}
void LaPlantParameters::setCropRotation(bool theFlag)
{
  mCropRotation=theFlag;
}
void LaPlantParameters::setFallowRatio(float theFallowRatio)
{
  mFallowRatio=theFallowRatio;
}
void LaPlantParameters::setFallowCalories(int theCalories)
{
  mFallowCalories=theCalories;
}
void LaPlantParameters::setAreaUnits(int theIndexValue)
{
  mAreaUnits=theIndexValue;
}
void LaPlantParameters::setUseSpecificLand(bool theFlag)
{
  mUseSpecificLand=theFlag;
}
void LaPlantParameters::setUseCommonLand(bool theFlag)
{
  mUseCommonLand=theFlag;
}

void LaPlantParameters::setName(QString theName)
{
  mName = theName;
}

bool LaPlantParameters::fromXml(QString theXml)
{
  qDebug("Loading plant Parameters from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("plantParameters");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  setGuid(myTopElement.attribute("guid"));
  mPercentTamePlant=QString(myTopElement.firstChildElement("percentTamePlant").text()).toInt();
  mCropRotation=QString(myTopElement.firstChildElement("cropRotation").text()).toInt();
  mFallowRatio=QString(myTopElement.firstChildElement("fallowRatio").text()).toInt();
  mFallowCalories=QString(myTopElement.firstChildElement("fallowCalories").text()).toInt();
  mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mUseCommonLand=QString(myTopElement.firstChildElement("useUniqueLand").text()).toInt();
  mUseSpecificLand=QString(myTopElement.firstChildElement("useSpecificLand").text()).toInt();
  return true;
}

QString LaPlantParameters::toXml()
{
  QString myString;
  myString+=QString("<plantParameters guid=\"" + guid() + "\">\n");
  myString+=QString("  <percentTamePlant>" + QString::number(mPercentTamePlant) + "</percentTamePlant>\n");
  myString+=QString("  <cropRotation>" + QString::number(mCropRotation) + "</cropRotation>\n");
  myString+=QString("  <fallowRatio>" + QString::number(mFallowRatio) + "</fallowRatio>\n");
  myString+=QString("  <fallowCalories>" + QString::number(mFallowCalories) + "</fallowCalories>\n");
  myString+=QString("  <areaUnits>" + QString::number(mAreaUnits) + "</areaUnits>\n");
  myString+=QString("  <useCommonLand>" + QString::number(mUseCommonLand) + "</useCommonLand>\n");
  myString+=QString("  <useSpecificLand>" + QString::number(mUseSpecificLand) + "</useSpecificLand>\n");
  myString+=QString("</plantParameters>\n");
  return myString;
}
