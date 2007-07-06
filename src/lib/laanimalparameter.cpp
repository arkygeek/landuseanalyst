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
  mFodderSource1 = theAnimalParameter.fodderSource1();
  mFodderSource1Grain = theAnimalParameter.fodderSource1Grain();
  mFodderSource2 = theAnimalParameter.fodderSource2();
  mFodderSource2Grain = theAnimalParameter.fodderSource2Grain();
  mFodderSource3 = theAnimalParameter.fodderSource3();
  mFodderSource3Grain = theAnimalParameter.fodderSource3Grain();
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
  mFodderSource1 = theAnimalParameter.fodderSource1();
  mFodderSource1Grain = theAnimalParameter.fodderSource1Grain();
  mFodderSource2 = theAnimalParameter.fodderSource2();
  mFodderSource2Grain = theAnimalParameter.fodderSource2Grain();
  mFodderSource3 = theAnimalParameter.fodderSource3();
  mFodderSource3Grain = theAnimalParameter.fodderSource3Grain();
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
int LaAnimalParameter::fodderSource1() const
{
  return mFodderSource1;
}
int LaAnimalParameter::fodderSource1Grain() const
{
  return mFodderSource1Grain;
}
int LaAnimalParameter::fodderSource2() const
{
  return mFodderSource2;
}
int LaAnimalParameter::fodderSource2Grain() const
{
  return mFodderSource2Grain;
}
int LaAnimalParameter::fodderSource3() const
{
  return mFodderSource3;
}
int LaAnimalParameter::fodderSource3Grain() const
{
  return mFodderSource3Grain;
}
Priority LaAnimalParameter::fallowUsage() const
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
void LaAnimalParameter::setFodderSource1(int theValue)
{
  mFodderSource1=theValue;
}
void LaAnimalParameter::setFodderSource1Grain(int theValue)
{
  mFodderSource1Grain=theValue;
}
void LaAnimalParameter::setFodderSource2(int theValue)
{
  mFodderSource2=theValue;
}
void LaAnimalParameter::setFodderSource2Grain(int theValue)
{
  mFodderSource2Grain=theValue;
}
void LaAnimalParameter::setFodderSource3(int theValue)
{
  mFodderSource3=theValue;
}
void LaAnimalParameter::setFodderSource3Grain(int theValue)
{
  mFodderSource3Grain=theValue;
}

void LaAnimalParameter::setFallowUsage(Priority thePriority)
{
  mFallowUsage=thePriority;
}

bool LaAnimalParameter::fromXml(QString theXml)
{
  //qDebug("Loading animal parameter from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("animalParameter");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  //qDebug("AnimalParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("AnimalParameter::fromXml - guid set to : " + guid().toLocal8Bit());
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
  mFodderSource1=QString(myTopElement.firstChildElement("fodderSource1").text()).toInt();;
  mFodderSource1Grain=QString(myTopElement.firstChildElement("fodderSource1Grain").text()).toInt();;
  mFodderSource2=QString(myTopElement.firstChildElement("fodderSource2").text()).toInt();;
  mFodderSource2Grain=QString(myTopElement.firstChildElement("fodderSource2Grain").text()).toInt();;
  mFodderSource3=QString(myTopElement.firstChildElement("fodderSource3").text()).toInt();;
  mFodderSource3Grain=QString(myTopElement.firstChildElement("fodderSource3Grain").text()).toInt();;

  QString myFallowUsage = QString(myTopElement.firstChildElement("fallowUsage").text());
  if (myFallowUsage == "High")
  {
      mFallowUsage=High;
  }
  else if (myFallowUsage == "Medium")
  {
      mFallowUsage=Medium;
  }    
  else if (myFallowUsage == "Low")
  {
      mFallowUsage=Low;
  }
  else
  {
    mFallowUsage=None;
  } 
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
  myString+=QString("  <fodderSource1>"+ QString::number(mFodderSource1) +"</fodderSource1>\n");
  myString+=QString("  <fodderSource1Grain>"+ QString::number(mFodderSource1Grain) +"</fodderSource1Grain>\n");
  myString+=QString("  <fodderSource2>"+ QString::number(mFodderSource2) +"</fodderSource2>\n");
  myString+=QString("  <fodderSource2Grain>"+ QString::number(mFodderSource2Grain) +"</fodderSource2Grain>\n");
  myString+=QString("  <fodderSource3>"+ QString::number(mFodderSource3) +"</fodderSource3>\n");
  myString+=QString("  <fodderSource3Grain>"+ QString::number(mFodderSource3Grain) +"</fodderSource3Grain>\n");
  switch (mFallowUsage)
  {
    case  High:
      myString+=QString("  <fallowUsage>High</fallowUsage>\n");
      break;
    case  Medium:
      myString+=QString("  <fallowUsage>Medium</fallowUsage>\n");
      break;
    case  Low:
      myString+=QString("  <fallowUsage>Low</fallowUsage>\n");
      break;
    default:
      myString+=QString("  <fallowUsage></fallowUsage>\n");
      break;
  } //switch
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
  myString+=QString("fodderSource1=>"+ QString::number(mFodderSource1) + "\n");
  myString+=QString("fodderSource1Grain=>"+ QString::number(mFodderSource1Grain) + "\n");
  myString+=QString("fodderSource2=>"+ QString::number(mFodderSource2) + "\n");
  myString+=QString("fodderSource2Grain=>"+ QString::number(mFodderSource2Grain) + "\n");
  myString+=QString("fodderSource3=>"+ QString::number(mFodderSource3) + "\n");
  myString+=QString("fodderSource1Lentils=>"+ QString::number(mFodderSource3Grain) + "\n");
  myString+=QString("fallowUsage=>" + QString::number(mFallowUsage) + "\n");
  return myString;
}

QString LaAnimalParameter::toHtml()
{
  QString myString;
  myString+="<p align=\"center\"><h3 >Details for " + LaUtils::xmlEncode(mName) + "</h3></p>";
  myString+="<table>";
  //myString+="<tr><td><b>GUID:</th><td>" + guid() + "</td></tr>";
  myString+="<tr><td><b>Description:</b></td><td>" + mDescription + "</td></tr>";
  //myString+="<tr><td><b>Animal:</b></td><td>" + mAnimalGuid + "</td></tr>";
  myString+="<tr><td><b>Percentage of Tame Meat:</b></td><td> " + QString::number(mPercentTameMeat) + "</td></tr>";
  myString+="<tr><td><b>Use Common Grazing Land:</b></td><td> " + QString::number(mUseCommonGrazingLand) + "</td></tr>";
  myString+="<tr><td><b>Use Specific Grazing Land:</b></td><td> " + QString::number(mUseSpecificGrazingLand) + "</td></tr>";
  myString+="<tr><td><b>Food Value Of Common Grazing Land:</b></td><td> " + QString::number(mFoodValueOfCommonGrazingLand) + "</td></tr>";
  myString+="<tr><td><b>Food Value Of Specific Grazing Land:</b></td><td> " + QString::number(mFoodValueOfSpecificGrazingLand) + "</td></tr>";
  myString+="<tr><td><b>Area Units:</b></td><td> "+ QString::number(mAreaUnits) + "</td></tr>";
  myString+="<tr><td><b>Fodder Wheat:</b></td><td>"+ QString::number(mFodderSource1) + "</td></tr>";
  myString+="<tr><td><b>Fodder Wheat Grain:</b></td><td>"+ QString::number(mFodderSource1Grain) + "</td></tr>";
  myString+="<tr><td><b>Fodder Barley:</b></td><td>"+ QString::number(mFodderSource2) + "</td></tr>";
  myString+="<tr><td><b>Fodder Barley Grain:</b></td><td>"+ QString::number(mFodderSource2Grain) + "</td></tr>";
  myString+="<tr><td><b>Fodder Lentils:</b></td><td>"+ QString::number(mFodderSource3) + "</td></tr>";
  myString+="<tr><td><b>Fodder Wheat Lentils:</b></td><td>"+ QString::number(mFodderSource3Grain) + "</td></tr>";
  myString+="<tr><td><b>Fallow Usage:</b></td><td> " + QString::number(mFallowUsage) + "</td></tr>";
  myString+="</table>";
  return myString;
}
