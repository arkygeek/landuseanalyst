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
#include <QStringList>
#include <QDomDocument>
#include <QDomElement>
#include <QComboBox>

#include "laanimalparameter.h"
#include "lautils.h"
#include "lacrop.h"
#include "lafoodsource.h"
#include "la.h"
#include "lagrass.h"

LaAnimalParameter::LaAnimalParameter() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mDescription="Not Set";
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
  mValueSpecificGrazingLand = theAnimalParameter.ValueSpecificGrazingLand();
  mValueCommonGrazingLand = theAnimalParameter.ValueCommonGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mEnergyType = theAnimalParameter.energyType();
  mFodderUse = theAnimalParameter.fodderUse();
  mFoodSourceMap = theAnimalParameter.fodderSourceMap();

  // fodder stuff here

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
  mValueSpecificGrazingLand = theAnimalParameter.ValueSpecificGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mValueCommonGrazingLand = theAnimalParameter.ValueCommonGrazingLand();
  mUseSpecificGrazingLand = theAnimalParameter.useSpecificGrazingLand();
  mUseCommonGrazingLand = theAnimalParameter.useCommonGrazingLand();
  mAreaUnits = theAnimalParameter.areaUnits();
  mEnergyType = theAnimalParameter.energyType();
  mFodderUse = theAnimalParameter.fodderUse();

  // fodder stuff here

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
float LaAnimalParameter::percentTameMeat() const
{
  return mPercentTameMeat;
}
int LaAnimalParameter::ValueSpecificGrazingLand() const
{
  //int myAreaInHectares = LaUtils::convertAreaToHectares (mAreaUnits, mValueSpecificGrazingLand);
  //return myAreaInHectares;
  return mValueSpecificGrazingLand;
}
int LaAnimalParameter::ValueCommonGrazingLand() const
{
  //int myAreaInHectares = LaUtils::convertAreaToHectares (mAreaUnits, mValueCommonGrazingLand);
  //return myAreaInHectares;
  return mValueCommonGrazingLand;
}
bool LaAnimalParameter::useSpecificGrazingLand() const
{
  return mUseSpecificGrazingLand;
}
bool LaAnimalParameter::useCommonGrazingLand() const
{
  return mUseCommonGrazingLand;
}
AreaUnits LaAnimalParameter::areaUnits() const
{
  return mAreaUnits;
}

EnergyType LaAnimalParameter::energyType() const
{
  return mEnergyType;
}

bool LaAnimalParameter::fodderUse() const
{
  return mFodderUse;
}

LaFoodSourceMap LaAnimalParameter::fodderSourceMap() const
{
  return mFoodSourceMap;
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
void LaAnimalParameter::setPercentTameMeat(float thePercentage)
{
  mPercentTameMeat=thePercentage;
}
void LaAnimalParameter::setValueSpecificGrazingLand(int theCalories)
{
  mValueSpecificGrazingLand=theCalories;
}
void LaAnimalParameter::setValueCommonGrazingLand(int theCalories)
{
  mValueCommonGrazingLand=theCalories;
}
void LaAnimalParameter::setUseSpecificGrazingLand(bool theFlag)
{
  mUseSpecificGrazingLand=theFlag;
}
void LaAnimalParameter::setUseCommonGrazingLand(bool theFlag)
{
  mUseCommonGrazingLand=theFlag;
}
void LaAnimalParameter::setAreaUnits(AreaUnits theAreaUnits)
{
  mAreaUnits=theAreaUnits;
}

void LaAnimalParameter::setEnergyType(EnergyType theEnergyType)
{
  mEnergyType=theEnergyType;
}

void LaAnimalParameter::setFodderUse(bool theBool)
{
  mFodderUse=theBool;
}

// fodder stuff here
void LaAnimalParameter::setFodderData(LaFoodSourceMap theFoodSourceMap)
{
  mFoodSourceMap = theFoodSourceMap;
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
   //qDebug("top element could not be found!");
  }
  //qDebug("AnimalParameter::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("AnimalParameter::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mAnimalGuid=LaUtils::xmlDecode(myTopElement.firstChildElement("animal").text());
  mPercentTameMeat=QString(myTopElement.firstChildElement("percentTameMeat").text()).toFloat();
  mUseCommonGrazingLand=QString(myTopElement.firstChildElement("useCommonGrazingLand").text()).toInt();
  mUseSpecificGrazingLand=QString(myTopElement.firstChildElement("useSpecificGrazingLand").text()).toInt();
  mValueCommonGrazingLand=QString(myTopElement.firstChildElement("foodValueOfCommonGrazingLand").text()).toInt();
  mValueSpecificGrazingLand=QString(myTopElement.firstChildElement("foodValueOfSpecificGrazingLand").text()).toInt();
  ///////////
  //mAreaUnits=LaUtils::xmlDecode(myTopElement.firstChildElement("areaUnits").text());
  QString myAreaUnits = QString(myTopElement.firstChildElement("areaUnits").text());
  if (myAreaUnits == "Dunum")
  {
    mAreaUnits=Dunum;
  }
  else if (myAreaUnits == "Hectare")
  {
    mAreaUnits=Hectare;
  }
QString myEnergyType = QString(myTopElement.firstChildElement("energyType").text());
  if (myEnergyType == "KCalories")
  {
    mEnergyType=KCalories;
  }
  else if (myEnergyType == "TDN")
  {
    mEnergyType=TDN;
  }
  mFodderUse=QString(myTopElement.firstChildElement("fodderUse").text()).toInt();
  // populate the fodder map
  mFoodSourceMap.clear();
  QDomNodeList myFodderCropsList = myDocument.elementsByTagName("fodderCrop");
  for (int myCounter=0; myCounter < myFodderCropsList.size(); myCounter++)
  {
    QDomNode myFoodSourceNode = myFodderCropsList.item(myCounter);
    QDomElement myFoodSourceElement = myFoodSourceNode.toElement();

    // load the data from the xml into local variables
    QString myGuid = myFoodSourceElement.firstChildElement("fodderCropGuid").text();
    int myFodderStrawChaff = myFoodSourceElement.firstChildElement("fodderStrawChaff").text().toInt();
    int myGrain = myFoodSourceElement.firstChildElement("fodderGrain").text().toInt();
    LaFoodSource myFoodSource;

    // setup the data to insert into the map
    myFoodSource.setFodder(myFodderStrawChaff);
    myFoodSource.setGrain(myGrain);
    // insert data into map
    mFoodSourceMap.insert(myGuid,myFoodSource);
  } // end of for loop
 //qDebug("Number of food sources restored from xml: " + QString::number(mFoodSourceMap.count()).toLocal8Bit());

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
  myString+=QString("  <useSpecificGrazingLand>" + QString::number(mUseSpecificGrazingLand) + "</useSpecificGrazingLand>\n");  myString+=QString("  <foodValueOfCommonGrazingLand>" + QString::number(mValueCommonGrazingLand) + "</foodValueOfCommonGrazingLand>\n");
  myString+=QString("  <foodValueOfSpecificGrazingLand>" + QString::number(mValueSpecificGrazingLand) + "</foodValueOfSpecificGrazingLand>\n");

  switch (mAreaUnits)
  {
    case Dunum:
      myString+=QString("  <areaUnits>Dunum</areaUnits>\n");
      break;
    case Hectare:
      myString+=QString("  <areaUnits>Hectare</areaUnits>\n");
      break;
  }

  switch (mEnergyType)
  {
    case KCalories:
      myString+=QString("  <energyType>KCalories</energyType>\n");
      break;
    case TDN:
      myString+=QString("  <energyType>TDN</energyType\n");
      break;
  }

  myString+=QString("  <fodderUse>"+ QString::number(mFodderUse) +"</fodderUse>\n");

  if (mFodderUse)
  {

   //qDebug("Fodder is used");
    myString+=QString("   <fodderCrops>\n");
    // write out the map for fodder info to xml
    QMapIterator<QString, LaFoodSource> myIterator(mFoodSourceMap);
    while (myIterator.hasNext())
    {
      myIterator.next();
      LaFoodSource myFoodSource = myIterator.value();

      QString myGuid = myIterator.key();
      QString myFodderStrawChaff = QString::number(myFoodSource.fodder());
      QString myFodderGrain = QString::number(myFoodSource.grain());
      myString+=QString("    <fodderCrop>\n");
      myString+=QString("      <fodderCropGuid>" + myGuid + "</fodderCropGuid>\n");
      myString+=QString("      <fodderStrawChaff>" + myFodderStrawChaff + "</fodderStrawChaff>\n");
      myString+=QString("      <fodderGrain>"+ myFodderGrain + "</fodderGrain>\n");
      myString+=QString("    </fodderCrop>\n");
    }
    myString+=QString("   </fodderCrops>\n");
  }
  else
  {
   //qDebug("Fodder is not used");
  }

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
  myString+=QString("foodValueOfCommonGrazingLand=>" + QString::number(mValueCommonGrazingLand) + "\n");
  myString+=QString("foodValueOfSpecificGrazingLand=>" + QString::number(mValueSpecificGrazingLand) + "\n");
  myString+=QString("areaUnits=>" + QString::number(mAreaUnits) + "\n");
  myString+=QString("energyType=>" + QString::number(mEnergyType) + "\n");
  myString+=QString("fodderUse=>" + QString::number(mFodderUse) + "\n");

  if (mFodderUse)
  {
    // write out the map for fodder info to text
  }
  else
  {
    myString+="Fodder not used";
  }

  myString+=QString("fallowUsage=>" + QString::number(mFallowUsage) + "\n");
  myString+=QString("rasterName=>" + LaUtils::xmlEncode(mRasterName) + "\n");
  return myString;
}

QString LaAnimalParameter::toHtml()
{
  QString myString;
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
  myString+="<tr><td>Food Value Of Common Grazing Land:</td><td> " + QString::number(mValueCommonGrazingLand) + "</td></tr>";
  myString+="<tr><td>Food Value Of Specific Grazing Land:</td><td> " + QString::number(mValueSpecificGrazingLand) + "</td></tr>";
  myString+="<tr><td>Energy Type:</td><td> "+ QString::number(mEnergyType) + "</td></tr>";
  myString+="<tr><td>Area Units:</td><td> "+ QString::number(mAreaUnits) + "</td></tr>";


  if (myFallowUsage=="None")
  {
    myString+="<tr><td>No Fallow Grazing</td></tr>";
  }
  else
  {
    myString+="<tr><td>Fallow Grazing:</td><td>" + myFallowUsage + "</td></tr>";
  }
  if (mFodderUse)
  {
    myString+=QString("   <fodderCrops>\n");
    // write out the map for fodder info to xml
    int myCounter = 0;
    QMapIterator<QString, LaFoodSource> myIterator(mFoodSourceMap);
    while (myIterator.hasNext())
    {
      myIterator.next();
      myCounter++;
      LaFoodSource myFoodSource = myIterator.value();

      QString myGuid = myIterator.key();
      QString myFodderStrawChaff = QString::number(myFoodSource.fodder());
      QString myFodderGrain = QString::number(myFoodSource.grain());

      myString+="<tr><td>Fodder Source #:</td><td> " + QString::number(myCounter) + "</td></tr>";
      myString+="<tr><td>Crop Guid: "+ myGuid + "</td></tr>";
      myString+="<tr><td>Straw and Chaff: "+ myFodderStrawChaff + "</td></tr>";
      myString+="<tr><td>Grain: "+ myFodderGrain + "</td></tr>";
    }
  }
  else
  {
    myString+="<tr><td>Fodder not used</td><td>";
  }

  myString+="</table>";
  return myString;
}
