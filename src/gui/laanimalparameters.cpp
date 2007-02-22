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

void setLaAnimalParameters::setPercentTameMeat(int thePercent)
{
  mPercentTameMeat=thePercent;
}
void setLaAnimalParameters::setFoodValueOfSpecificGrazingLand(int theCalories)
{
  mFoodValueOfSpecificGrazingLand=theCalories;
}
void setLaAnimalParameters::setFoodValueOfCommonGrazingLand(int theCalories)
{
  mFoodValueOfCommonGrazingLand=theCalories;
}
void setLaAnimalParameters::setUseSpecificGrazingLand(bool theFlag)
{
  mUseSpecificGrazingLand=theFlag;
}
void setLaAnimalParameters::setUseCommonGrazingLand(bool theFlag)
{
  mUseCommonGrazingLand=theFlag;
}
void setLaAnimalParameters::setFallowUsage(int theIndexValue)
{
  mFallowUsage=theIndexValue;
}


void LaAnimalParameters::setName(QString theName) const
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
  mUsableMeat=QString(myTopElement.firstChildElement("usableMeat").text()).toInt();
  mKillWeight=QString(myTopElement.firstChildElement("killWeight").text()).toInt();
  mGrowTime=QString(myTopElement.firstChildElement("growTime").text()).toInt();
  mDeathRate=QString(myTopElement.firstChildElement("deathRate").text()).toInt();
  mGestating=QString(myTopElement.firstChildElement("gestating").text()).toInt();
  mLactating=QString(myTopElement.firstChildElement("lactating").text()).toInt();
  mJuvenile=QString(myTopElement.firstChildElement("juvenile").text()).toInt();
  mLifeExpectancy=QString(myTopElement.firstChildElement("lifeExpectancy").text()).toInt();
  mBreedingExpectancy=QString(myTopElement.firstChildElement("breedingExpectancy").text()).toInt();
  mYoungPerBirth=QString(myTopElement.firstChildElement("youngPerBirth").text()).toInt();
  mWeaningAge=QString(myTopElement.firstChildElement("weaningAge").text()).toInt();
  mGestationTime=QString(myTopElement.firstChildElement("gestationTime").text()).toInt();
  mEstrousCycle=QString(myTopElement.firstChildElement("estrousCycle").text()).toInt();
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
