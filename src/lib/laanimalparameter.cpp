/***************************************************************************
                          laanimalParameter.cpp  -  The animalParameter class
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
#include "laanimalparameter.h"
#include "lautils.h"

LaAnimalParameter::LaAnimalParameter() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mDescription="Not Set";
  //mPercentTameMeat=20;
  //mFoodValueOfSpecificGrazingLand = 5000;
  //mFoodValueOfCommonGrazingLand = 5000;
}
LaAnimalParameter::~LaAnimalParameter()
{

}

//copy constructor
LaAnimalParameter::LaAnimalParameter(const LaAnimalParameter& theAnimalParameter)
{
  mName=theAnimalParameter.name();
  mDescription=theAnimalParameter.description();
  setGuid(theAnimalParameter.guid());
  setAnimalGuid(theAnimalParameter.animalGuid());
  mPercentTameMeat=theAnimalParameter.percentTameMeat();
  mFoodValueOfSpecificGrazingLand = theAnimalParameter.foodValueOfSpecificGrazingLand();
  mFoodValueOfCommonGrazingLand = theAnimalParameter.foodValueOfCommonGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mFodderUse = theAnimalParameter.fodderUse();
  mFodderWheat = theAnimalParameter.fodderWheat();
  mFodderWheatGrain = theAnimalParameter.fodderWheatGrain();
  mFodderBarley = theAnimalParameter.fodderBarley();
  mFodderBarleyGrain = theAnimalParameter.fodderBarleyGrain();
  mFodderLentils = theAnimalParameter.fodderLentils();
  mFodderLentilsGrain = theAnimalParameter.fodderLentilsGrain();
  mUseSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameter.useCommonGrazingLand();
  mFallowUsage = theAnimalParameter.fallowUsage();
}

LaAnimalParameter& LaAnimalParameter::operator=(const LaAnimalParameter& theAnimalParameter)
{
  if (this == &theAnimalParameter) return *this;   // Gracefully handle self assignment

  mName=theAnimalParameter.name();
  mDescription=theAnimalParameter.description();
  setGuid(theAnimalParameter.guid());
  setAnimalGuid(theAnimalParameter.animalGuid());
  mPercentTameMeat = theAnimalParameter.percentTameMeat();
  mFoodValueOfSpecificGrazingLand = theAnimalParameter.foodValueOfSpecificGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mFoodValueOfCommonGrazingLand = theAnimalParameter.foodValueOfCommonGrazingLand();
  mUseSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameter.useCommonGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mFodderUse = theAnimalParameter.fodderUse();
  mFodderWheat = theAnimalParameter.fodderWheat();
  mFodderWheatGrain = theAnimalParameter.fodderWheatGrain();
  mFodderBarley = theAnimalParameter.fodderBarley();
  mFodderBarleyGrain = theAnimalParameter.fodderBarleyGrain();
  mFodderLentils = theAnimalParameter.fodderLentils();
  mFodderLentilsGrain = theAnimalParameter.fodderLentilsGrain();
  mFallowUsage = theAnimalParameter.fallowUsage();
  return *this;
}

QString LaAnimalParameter::name() const
{
  return mName;
}
QString LaAnimalParameter::description() const
{
  return mDescription;
}
QString LaAnimalParameter::animalGuid() const
{
  return mAnimalGuid;
}
int LaAnimalParameter::percentTameMeat() const
{
  return mPercentTameMeat;
}
int LaAnimalParameter::foodValueOfSpecificGrazingLand() const
{
  return mFoodValueOfSpecificGrazingLand;
}
int LaAnimalParameter::foodValueOfCommonGrazingLand() const
{
  return mFoodValueOfCommonGrazingLand;
}
bool LaAnimalParameter::useSpecificGrazingLand() const
{
  return mUseSpecificGrazingLand;
}
bool LaAnimalParameter::useCommonGrazingLand() const
{
  return mUseCommonGrazingLand;
}
int LaAnimalParameter::areaUnits() const
{
  return mAreaUnits;
}

bool LaAnimalParameter::fodderUse() const
{
  return mFodderUse;
}
int LaAnimalParameter::fodderWheat() const
{
  return mFodderWheat;
}
int LaAnimalParameter::fodderWheatGrain() const
{
  return mFodderWheatGrain;
}
int LaAnimalParameter::fodderBarley() const
{
  return mFodderBarley;
}
int LaAnimalParameter::fodderBarleyGrain() const
{
  return mFodderBarleyGrain;
}
int LaAnimalParameter::fodderLentils() const
{
  return mFodderLentils;
}
int LaAnimalParameter::fodderLentilsGrain() const
{
  return mFodderLentilsGrain;
}
int LaAnimalParameter::fallowUsage() const
{
  return mFallowUsage;
}

/////////////////////////////////////////////////////////

void LaAnimalParameter::setName(QString theName)
{
  mName=theName;
}
void LaAnimalParameter::setDescription(QString theDescription)
{
  mDescription=theDescription;
}
void LaAnimalParameter::setAnimalGuid(QString theGuid) 
{
  mAnimalGuid = theGuid;
}
void LaAnimalParameter::setPercentTameMeat(int thePercentage)
{
  mPercentTameMeat=thePercentage;
}
void LaAnimalParameter::setFoodValueOfSpecificGrazingLand(int theCalories)
{
  mFoodValueOfSpecificGrazingLand=theCalories;
}
void LaAnimalParameter::setFoodValueOfCommonGrazingLand(int theCalories)
{
  mFoodValueOfCommonGrazingLand=theCalories;
}
void LaAnimalParameter::setUseSpecificGrazingLand(bool theFlag)
{
  mUseSpecificGrazingLand=theFlag;
}
void LaAnimalParameter::setUseCommonGrazingLand(bool theFlag)
{
  mUseCommonGrazingLand=theFlag;
}
void LaAnimalParameter::setAreaUnits(int theIndexValue)
{
  mAreaUnits=theIndexValue;
}

void LaAnimalParameter::setFodderUse(bool theBool)
{
  mFodderUse=theBool;
}
void LaAnimalParameter::setFodderWheat(int theValue)
{
  mFodderWheat=theValue;
}
void LaAnimalParameter::setFodderWheatGrain(int theValue)
{
  mFodderWheatGrain=theValue;
}
void LaAnimalParameter::setFodderBarley(int theValue)
{
  mFodderBarley=theValue;
}
void LaAnimalParameter::setFodderBarleyGrain(int theValue)
{
  mFodderBarleyGrain=theValue;
}
void LaAnimalParameter::setFodderLentils(int theValue)
{
  mFodderLentils=theValue;
}
void LaAnimalParameter::setFodderLentilsGrain(int theValue)
{
  mFodderLentilsGrain=theValue;
}

void LaAnimalParameter::setFallowUsage(int theIndexValue)
{
  mFallowUsage=theIndexValue;
}

bool LaAnimalParameter::fromXml(QString theXml)
{
  qDebug("Loading animal parameter from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("animalParameter");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  qDebug("AnimalParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  qDebug("AnimalParameter::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mAnimalGuid=LaUtils::xmlDecode(myTopElement.firstChildElement("animal").text());
  mPercentTameMeat=QString(myTopElement.firstChildElement("percentTameMeat").text()).toInt();
  mUseCommonGrazingLand=QString(myTopElement.firstChildElement("useCommonGrazingLand").text()).toInt();
  mUseSpecificGrazingLand=QString(myTopElement.firstChildElement("useSpecificGrazingLand").text()).toInt();
  mFoodValueOfCommonGrazingLand=QString(myTopElement.firstChildElement("foodValueOfCommonGrazingLand").text()).toInt();
mFoodValueOfSpecificGrazingLand=QString(myTopElement.firstChildElement("foodValueOfSpecificGrazingLand").text()).toInt();
///////////
  mAreaUnits=QString(myTopElement.firstChildElement("areaUnits").text()).toInt();
  mFodderUse=QString(myTopElement.firstChildElement("fodderUse").text()).toInt();;
  mFodderWheat=QString(myTopElement.firstChildElement("fodderWheat").text()).toInt();;
  mFodderWheatGrain=QString(myTopElement.firstChildElement("fodderWheatGrain").text()).toInt();;
  mFodderBarley=QString(myTopElement.firstChildElement("fodderBarley").text()).toInt();;
  mFodderBarleyGrain=QString(myTopElement.firstChildElement("fodderBarleyGrain").text()).toInt();;
  mFodderLentils=QString(myTopElement.firstChildElement("fodderLentils").text()).toInt();;
  mFodderLentilsGrain=QString(myTopElement.firstChildElement("fodderLentilsGrain").text()).toInt();;

///////////
  mFallowUsage=QString(myTopElement.firstChildElement("fallowUsage").text()).toInt();
  return true;
}

QString LaAnimalParameter::toXml()
{
  QString myString;
  myString+=QString("<animalParameter guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <animal>" + LaUtils::xmlEncode(mAnimalGuid) + "</animal>\n");
  myString+=QString("  <percentTameMeat>" + QString::number(mPercentTameMeat) + "</percentTameMeat>\n");
  myString+=QString("  <useCommonGrazingLand>" + QString::number(mUseCommonGrazingLand) + "</useCommonGrazingLand>\n");
  myString+=QString("  <useSpecificGrazingLand>" + QString::number(mUseSpecificGrazingLand) + "</useSpecificGrazingLand>\n");  myString+=QString("  <foodValueOfCommonGrazingLand>" + QString::number(mFoodValueOfCommonGrazingLand) + "</foodValueOfCommonGrazingLand>\n");
  myString+=QString("  <foodValueOfSpecificGrazingLand>" + QString::number(mFoodValueOfSpecificGrazingLand) + "</foodValueOfSpecificGrazingLand>\n");
  myString+=QString("  <areaUnits>" + QString::number(mAreaUnits) + "</areaUnits>\n");
  myString+=QString("  <fodderUse>"+ QString::number(mFodderUse) +"</fodderUse>\n");
  myString+=QString("  <fodderWheat>"+ QString::number(mFodderWheat) +"</fodderWheat>\n");
  myString+=QString("  <fodderWheatGrain>"+ QString::number(mFodderWheatGrain) +"</fodderWheatGrain>\n");
  myString+=QString("  <fodderBarley>"+ QString::number(mFodderBarley) +"</fodderBarley>\n");
  myString+=QString("  <fodderBarleyGrain>"+ QString::number(mFodderBarleyGrain) +"</fodderBarleyGrain>\n");
  myString+=QString("  <fodderLentils>"+ QString::number(mFodderLentils) +"</fodderLentils>\n");
  myString+=QString("  <fodderLentilsGrain>"+ QString::number(mFodderLentilsGrain) +"</fodderLentilsGrain>\n");
  myString+=QString("  <fallowUsage>" + QString::number(mFallowUsage) + "</fallowUsage>\n");
  myString+=QString("</animalParameter>\n");
  return myString;
}

QString LaAnimalParameter::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("description=>" + LaUtils::xmlEncode(mDescription) + "\n");
  myString+=QString("animal=>" + mAnimalGuid + "\n");
  myString+=QString("percentTameMeat=>" + QString::number(mPercentTameMeat) + "\n");
  myString+=QString("useCommonGrazingLand=>" + QString::number(mUseCommonGrazingLand) + "\n");
  myString+=QString("useSpecificGrazingLand=>" + QString::number(mUseSpecificGrazingLand) + "\n");
  myString+=QString("foodValueOfCommonGrazingLand=>" + QString::number(mFoodValueOfCommonGrazingLand) + "\n");
  myString+=QString("foodValueOfSpecificGrazingLand=>" + QString::number(mFoodValueOfSpecificGrazingLand) + "\n");
  myString+=QString("areaUnits=>" + QString::number(mAreaUnits) + "\n");
  myString+=QString("fodderUse=>"+ QString::number(mFodderUse) + "\n");
  myString+=QString("fodderWheat=>"+ QString::number(mFodderWheat) + "\n");
  myString+=QString("fodderWheatGrain=>"+ QString::number(mFodderWheatGrain) + "\n");
  myString+=QString("fodderBarley=>"+ QString::number(mFodderBarley) + "\n");
  myString+=QString("fodderBarleyGrain=>"+ QString::number(mFodderBarleyGrain) + "\n");
  myString+=QString("fodderLentils=>"+ QString::number(mFodderLentils) + "\n");
  myString+=QString("fodderWheatLentils=>"+ QString::number(mFodderLentilsGrain) + "\n");
  myString+=QString("fallowUsage=>" + QString::number(mFallowUsage) + "\n");
  return myString;
}

QString LaAnimalParameter::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h1>Details for " + LaUtils::xmlEncode(mName) + "</h1></p>";
  myString+="<p>GUID:" + guid() + "</p>";
  myString+="<p>Description:" + mDescription + "</p>";
  myString+="<p>Animal:" + mAnimalGuid + "</p>";
  myString+="<p>Percentage of Tame Meat: " + QString::number(mPercentTameMeat) + "</p>";
  myString+="<p>Use Common Grazing Land: " + QString::number(mUseCommonGrazingLand) + "</p>";
  myString+="<p>Use Specific Grazing Land: " + QString::number(mUseSpecificGrazingLand) + "</p>";
  myString+="<p>Food Value Of Common Grazing Land: " + QString::number(mFoodValueOfCommonGrazingLand) + "</p>";
  myString+="<p>Food Value Of Specific Grazing Land: " + QString::number(mFoodValueOfSpecificGrazingLand) + "</p>";
  myString+="<p>Area Units: "+ QString::number(mAreaUnits) + "</p>";
  myString+="<p>fodderWheat:"+ QString::number(mFodderWheat) + "</p>";
  myString+="<p>fodderWheatGrain:"+ QString::number(mFodderWheatGrain) + "</p>";
  myString+="<p>fodderBarley:"+ QString::number(mFodderBarley) + "</p>";
  myString+="<p>fodderBarleyGrain:"+ QString::number(mFodderBarleyGrain) + "</p>";
  myString+="<p>fodderLentils:"+ QString::number(mFodderLentils) + "</p>";
  myString+="<p>fodderWheatLentils:"+ QString::number(mFodderLentilsGrain) + "</p>";
  myString+="<p>Fallow Usage: " + QString::number(mFallowUsage) + "</p>";
  return myString;
}
