/***************************************************************************
                          laanimalParameter.cpp  -  The animalParameter class
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton
    email                : tim@linfiniti.com
                         : (C) 2007 by Jason Jorgenson
    email                : arkygeek@gmail.com
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
#include "lacrop.h"
#include "lafoodsource.h"

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
  mFodder1 = theAnimalParameter.fodder1();
  mFodderGrain1 = theAnimalParameter.fodderGrain1();

  mFodderSource2 = theAnimalParameter.fodderSource2();
  mFodder2 = theAnimalParameter.fodder2();
  mFodderGrain2 = theAnimalParameter.fodderGrain2();

  mFodderSource3 = theAnimalParameter.fodderSource3();
  mFodder3 = theAnimalParameter.fodder3();
  mFodderGrain3 = theAnimalParameter.fodderGrain3();

  mUseSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameter.useCommonGrazingLand();
  mFallowUsage = theAnimalParameter.fallowUsage();
  mRasterName = theAnimalParameter.rasterName();
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
  mFodder1 = theAnimalParameter.fodder1();
  mFodderGrain1 = theAnimalParameter.fodderGrain1();

  mFodderSource2 = theAnimalParameter.fodderSource2();
  mFodder2 = theAnimalParameter.fodder2();
  mFodderGrain2 = theAnimalParameter.fodderGrain2();

  mFodderSource3 = theAnimalParameter.fodderSource3();
  mFodder3 = theAnimalParameter.fodder3();
  mFodderGrain3 = theAnimalParameter.fodderGrain3();

  mFallowUsage = theAnimalParameter.fallowUsage();
  mRasterName = theAnimalParameter.rasterName();
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
QString LaAnimalParameter::fodderSource1() const
{
  return mFodderSource1;
}
int LaAnimalParameter::fodder1() const
{
  return mFodder1;
}
int LaAnimalParameter::fodderGrain1() const
{
  return mFodderGrain1;
}
QString LaAnimalParameter::fodderSource2() const
{
  return mFodderSource2;
}
int LaAnimalParameter::fodder2() const
{
  return mFodder2;
}
int LaAnimalParameter::fodderGrain2() const
{
  return mFodderGrain2;
}
QString LaAnimalParameter::fodderSource3() const
{
  return mFodderSource3;
}
int LaAnimalParameter::fodder3() const
{
  return mFodder3;
}
int LaAnimalParameter::fodderGrain3() const
{
  return mFodderGrain3;
}
Priority LaAnimalParameter::fallowUsage() const
{
  return mFallowUsage;
}

QString LaAnimalParameter::rasterName() const
{
  return mRasterName;
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

void LaAnimalParameter::setFodderSource1(QString theGuid)
{
  mFodderSource1=theGuid;
}
void LaAnimalParameter::setFodder1(int theValue)
{
  mFodder1=theValue;
}
void LaAnimalParameter::setFodderGrain1(int theValue)
{
  mFodderGrain1=theValue;
}

void LaAnimalParameter::setFodderSource2(QString theGuid)
{
  mFodderSource2=theGuid;
}
void LaAnimalParameter::setFodder2(int theValue)
{
  mFodder2=theValue;
}
void LaAnimalParameter::setFodderGrain2(int theValue)
{
  mFodderGrain2=theValue;
}

void LaAnimalParameter::setFodderSource3(QString theGuid)
{
  mFodderSource3=theGuid;
}
void LaAnimalParameter::setFodder3(int theValue)
{
  mFodder3=theValue;
}
void LaAnimalParameter::setFodderGrain3(int theValue)
{
  mFodderGrain3=theValue;
}

void LaAnimalParameter::setFallowUsage(Priority thePriority)
{
  mFallowUsage=thePriority;
}

void LaAnimalParameter::setRasterName(QString theRasterName)
{
  mRasterName=theRasterName;
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
  mFodderUse=QString(myTopElement.firstChildElement("fodderUse").text()).toInt();
  mFodderSource1=QString(myTopElement.firstChildElement("fodderSource1").text()).toInt();
  mFodder1=QString(myTopElement.firstChildElement("fodder1").text()).toInt();
  mFodderGrain1=QString(myTopElement.firstChildElement("fodderGrain1").text()).toInt();

  mFodderSource2=QString(myTopElement.firstChildElement("fodderSource2").text()).toInt();
  mFodder2=QString(myTopElement.firstChildElement("fodder2").text()).toInt();
  mFodderGrain2=QString(myTopElement.firstChildElement("fodderGrain2").text()).toInt();

  mFodderSource3=QString(myTopElement.firstChildElement("fodderSource3").text()).toInt();
  mFodder3=QString(myTopElement.firstChildElement("fodder3").text()).toInt();
  mFodderGrain3=QString(myTopElement.firstChildElement("fodderGrain3").text()).toInt();

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
  mRasterName=LaUtils::xmlDecode(myTopElement.firstChildElement("rasterName").text());
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


  myString+=QString("  <fodderSource1>"+ mFodderSource1 +"</fodderSource1>\n");
  myString+=QString("  <fodder1>"+ QString::number(mFodder1) + "</fodder1>\n");
  myString+=QString("  <fodderGrain1>"+ QString::number(mFodderGrain1) +"</fodderGrain1>\n");

  myString+=QString("  <fodderSource2>"+ mFodderSource2 +"</fodderSource2>\n");
  myString+=QString("  <fodder2>"+ QString::number(mFodder2) +"</fodder2>\n");
  myString+=QString("  <fodderGrain2>"+ QString::number(mFodderGrain2) +"</fodderGrain2>\n");

  myString+=QString("  <fodderSource3>"+ mFodderSource3 +"</fodderSource3>\n");
  myString+=QString("  <fodder3>"+ QString::number(mFodder3) +"</fodder3>\n");
  myString+=QString("  <fodderGrain3>"+ QString::number(mFodderGrain3) +"</fodderGrain3>\n");
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
  myString+=QString("  <rasterName>" + LaUtils::xmlEncode(mRasterName) + "</RasterName>\n");
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
  myString+=QString("fodderUse=>" + QString::number(mFodderUse) + "\n");

  myString+=QString("fodderSource1=>" + mFodderSource1 + "\n");
  myString+=QString("fodder1=>" + QString::number(mFodder1) + "\n");
  myString+=QString("fodderGrain1=>" + QString::number(mFodderGrain1) + "\n");

  myString+=QString("fodderSource2=>" + mFodderSource2 + "\n");
  myString+=QString("fodder2=>" + QString::number(mFodder2) + "\n");
  myString+=QString("fodderGrain2=>" + QString::number(mFodderGrain2) + "\n");

  myString+=QString("fodderSource3=>" + mFodderSource3 + "\n");
  myString+=QString("fodder3=>" + QString::number(mFodder3) + "\n");
  myString+=QString("fodderGrain3=>" + QString::number(mFodderGrain3) + "\n");

  myString+=QString("fallowUsage=>" + QString::number(mFallowUsage) + "\n");
  myString+=QString("rasterName=>" + LaUtils::xmlEncode(mRasterName) + "\n");
  return myString;
}

QString LaAnimalParameter::toHtml()
{
  QString myString;
  QString myFodderUse = (mFodderUse==0) ? "Not Used" : "Used";
  QString myFallowUsage;
  switch (mFallowUsage)
  {
    case  High:
      myFallowUsage=QString("High Priority");
      break;
    case  Medium:
      myFallowUsage=QString("Medium Priority");
      break;
    case  Low:
      myFallowUsage=QString("Low Priority");
      break;
    default:
      myFallowUsage=QString("None");
      break;
  }

  myString+="<h3 >Details for " + LaUtils::xmlEncode(mName) + "</h3>";
  myString+="<table>";
  //myString+="<tr><td>GUID:</th><td>" + guid() + "</td></tr>";
  myString+="<tr><td>Description:</td><td>" + mDescription + "</td></tr>";
  //myString+="<tr><td>Animal:</td><td>" + mAnimalGuid + "</td></tr>";
  myString+="<tr><td>Raster Mask:</td><td>" + LaUtils::xmlEncode(mRasterName) + "</td></tr>";
  myString+="<tr><td>Percentage of Tame Meat:</td><td> " + QString::number(mPercentTameMeat) + "</td></tr>";
  myString+="<tr><td>Use Common Grazing Land:</td><td> " + QString::number(mUseCommonGrazingLand) + "</td></tr>";
  myString+="<tr><td>Use Specific Grazing Land:</td><td> " + QString::number(mUseSpecificGrazingLand) + "</td></tr>";
  myString+="<tr><td>Food Value Of Common Grazing Land:</td><td> " + QString::number(mFoodValueOfCommonGrazingLand) + "</td></tr>";
  myString+="<tr><td>Food Value Of Specific Grazing Land:</td><td> " + QString::number(mFoodValueOfSpecificGrazingLand) + "</td></tr>";
  myString+="<tr><td>Area Units:</td><td> "+ QString::number(mAreaUnits) + "</td></tr>";


  if (myFallowUsage=="None")
  {
    myString+="<tr><td>No Fallow Grazing</td></tr>";
  }
  else
  {
    myString+="<tr><td>Fallow Grazing:</td><td>" + myFallowUsage + "</td></tr>";
  }
  if (myFodderUse=="Used")
  {
    myString+="<tr><td>Fodder Source 1:</td><td>"+ mFodderSource1 + "</td></tr>";
    myString+="<tr><td>Fodder 1:</td><td>"+ QString::number(mFodder1) + "</td></tr>";
    myString+="<tr><td>Fodder Grain 1:</td><td>"+ QString::number(mFodderGrain1) + "</td></tr>";

    myString+="<tr><td>Fodder Source 2:</td><td>"+ mFodderSource2 + "</td></tr>";
    myString+="<tr><td>Fodder 2:</td><td>"+ QString::number(mFodder2) + "</td></tr>";
    myString+="<tr><td>Fodder Grain 2:</td><td>"+ QString::number(mFodderGrain2) + "</td></tr>";

    myString+="<tr><td>Fodder Lentils:</td><td>"+ mFodderSource3 + "</td></tr>";
    myString+="<tr><td>Fodder 3:</td><td>"+ QString::number(mFodder3) + "</td></tr>";
    myString+="<tr><td>Fodder Grain 3:</td><td>"+ QString::number(mFodderGrain3) + "</td></tr>";
  }
  else
  {
    myString+="<tr><td>Fodder not used</td><td>";
  }

  myString+="</table>";
  return myString;
}
