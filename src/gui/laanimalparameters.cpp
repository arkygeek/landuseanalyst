/***************************************************************************
                          LaAnimalParametersparameters.cpp  -  The animal class
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
#include "laanimalparameters.h"
#include "lautils.h"

LaAnimalParameters::LaAnimalParameters() : LaSerialisable(), LaGuid()
{
  setGuid();
}
LaAnimalParameters::~LaAnimalParameters()
{

}

//copy constructor
LaAnimalParameters::LaAnimalParameters(const LaAnimalParameters& theAnimalParameters)
{
  mPercentTameMeat=theAnimalParameters.percentTameMeat();
  mFoodValueOfSpecificGrazingLand = theAnimalParameters.foodValueOfSpecificGrazingLand();
  mFoodValueOfCommonGrazingLand = theAnimalParameters.foodValueOfCommonGrazingLand();
  mUseSpecificGrazingLand = theAnimalParameters.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameters.useCommonGrazingLand();
  mFallowUsage = theAnimalParameters.fallowUsage();
}

LaAnimalParameters& LaAnimalParameters::operator=(const LaAnimalParameters& theAnimalParameters)
{
  if (this == &theAnimalParameters) return *this;   // Gracefully handle self assignment

  mPercentTameMeat=theAnimalParameters.percentTameMeat();
  mFoodValueOfSpecificGrazingLand = theAnimalParameters.foodValueOfSpecificGrazingLand();
  mFoodValueOfCommonGrazingLand = theAnimalParameters.foodValueOfCommonGrazingLand();
  mUseSpecificGrazingLand = theAnimalParameters.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameters.useCommonGrazingLand();
  mFallowUsage = theAnimalParameters.fallowUsage();
  return *this;
}

QString LaAnimalParameters::name() const
{
  return mName;
}

int LaAnimalParameters::percentTameMeat() const
{
  return mPercentTameMeat;
}
int LaAnimalParameters::foodValueOfSpecificGrazingLand() const
{
  return mFoodValueOfSpecificGrazingLand;
}
int LaAnimalParameters::foodValueOfCommonGrazingLand() const
{
  return mFoodValueOfCommonGrazingLand;
}
bool LaAnimalParameters::useSpecificGrazingLand() const
{
  return mUseSpecificGrazingLand;
}
bool LaAnimalParameters::useCommonGrazingLand() const
{
  return mUseCommonGrazingLand;
}
int LaAnimalParameters::fallowUsage() const
{
  return mFallowUsage;
}

void LaAnimalParameters::setPercentTameMeat(int thePercent)
{
  mPercentTameMeat=thePercent;
}
void LaAnimalParameters::setFoodValueOfSpecificGrazingLand(int theCalories)
{
  mFoodValueOfSpecificGrazingLand=theCalories;
}
void LaAnimalParameters::setFoodValueOfCommonGrazingLand(int theCalories)
{
  mFoodValueOfCommonGrazingLand=theCalories;
}
void LaAnimalParameters::setUseSpecificGrazingLand(bool theFlag)
{
  mUseSpecificGrazingLand=theFlag;
}
void LaAnimalParameters::setUseCommonGrazingLand(bool theFlag)
{
  mUseCommonGrazingLand=theFlag;
}
void LaAnimalParameters::setFallowUsage(int theIndexValue)
{
  mFallowUsage=theIndexValue;
}


void LaAnimalParameters::setName(QString theName)
{
  mName = theName;
}

bool LaAnimalParameters::fromXml(QString theXml)
{
  qDebug("Loading animal Parameters from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("animalParameters");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  setGuid(myTopElement.attribute("guid"));
  mPercentTameMeat=QString(myTopElement.firstChildElement("percentTameMeat").text()).toInt();
  mFoodValueOfSpecificGrazingLand=QString(myTopElement.firstChildElement("foodValueOfSpecificGrazingLand").text()).toInt();
  mFoodValueOfCommonGrazingLand=QString(myTopElement.firstChildElement("foodValueOfCommonGrazingLand").text()).toInt();
  mUseSpecificGrazingLand=QString(myTopElement.firstChildElement("useSpecificGrazingLand").text()).toInt();
  mUseCommonGrazingLand=QString(myTopElement.firstChildElement("useCommonGrazingLand").text()).toInt();
  mFallowUsage=QString(myTopElement.firstChildElement("fallowUsage").text()).toInt();


  return true;
}

QString LaAnimalParameters::toXml()
{
  QString myString;
  myString+=QString("<animalParameters guid=\"" + guid() + "\">\n");
  myString+=QString("  <percentTameMeat>" + QString::number(mPercentTameMeat) + "</percentTameMeat>\n");
  myString+=QString("  <foodValueOfSpecificGrazingLand>" + QString::number(mFoodValueOfSpecificGrazingLand) + "</foodValueOfSpecificGrazingLand>\n");
  myString+=QString("  <foodValueOfCommonGrazingLand>" + QString::number(mFoodValueOfCommonGrazingLand) + "</foodValueOfCommonGrazingLand>\n");
  myString+=QString("  <useSpecificGrazingLand>" + QString::number(mUseSpecificGrazingLand) + "</useSpecificGrazingLand>\n");
  myString+=QString("  <useCommonGrazingLand>" + QString::number(mUseCommonGrazingLand) + "</useCommonGrazingLand>\n");
  myString+=QString("  <fallowUsage>" + QString::number(mFallowUsage) + "</fallowUsage>\n");
  myString+=QString("</animalParamaters>\n");
  return myString;
}
