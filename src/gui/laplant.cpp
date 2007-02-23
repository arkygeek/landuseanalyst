/***************************************************************************
                          omgserialisable.cpp  -  description
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
#include "laplant.h"
#include "lautils.h"

LaPlant::LaPlant() : LaSerialisable(), LaGuid()
{
  setGuid();
}
LaPlant::~LaPlant()
{

}

//copy constructor
LaPlant::LaPlant(const LaPlant& thePlant)
{
  mName=thePlant.name();
  mCropYield=thePlant.cropYield();
  mCropCalories=thePlant.cropCalories();
  mCropFodderProduction=thePlant.fodderProduction();
  mCropFodderCalories=thePlant.fodderCalories();
  mCropYield=thePlant.yieldUnits();
}

LaPlant& LaPlant::operator=(const LaPlant& thePlant)
{
  if (this == &thePlant) return *this;   // Gracefully handle self assignment

  mName=thePlant.name();
  mCropYield=thePlant.cropYield();
  mCropCalories=thePlant.cropCalories();
  mCropFodderProduction=thePlant.fodderProduction();
  mCropFodderCalories=thePlant.fodderCalories();
  mCropYield=thePlant.yieldUnits();
  return *this;
}

QString LaPlant::name() const
{
  return mName;
}
int LaPlant::cropYield() const
{
  return mCropYield;
}
int LaPlant::cropCalories() const
{
  return mCropCalories;
}
int LaPlant::fodderProduction() const
{
  return mCropFodderProduction;
}
int LaPlant::fodderCalories() const
{
  return mCropFodderCalories;
}
int LaPlant::yieldUnits() const
{
  return mYieldUnits;
}

void LaPlant::setName(QString theName)
{
  mName=theName;
}
void LaPlant::setCropYield(int theKg)
{
  mCropYield=theKg;
}
void LaPlant::setCropCalories(int theInteger)
{
  mCropCalories=theInteger;
}
void LaPlant::setFodderProduction(int theKg)
{
  mCropFodderProduction=theKg;
}
void LaPlant::setFodderCalories(int theCalories)
{
  mCropFodderCalories=theCalories;
}
void LaPlant::setYieldUnits(int theIndex)
{
  mYieldUnits=theIndex;
}

bool LaPlant::fromXml(QString theXml)
{
  qDebug("Loading Plant from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("Plant");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  setGuid(myTopElement.attribute("guid"));
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mCropYield=QString(myTopElement.firstChildElement("cropYield").text()).toInt();
  mCropCalories=QString(myTopElement.firstChildElement("cropCalories").text()).toInt();
  mCropFodderProduction=QString(myTopElement.firstChildElement("fodderProduction").text()).toInt();
  mCropFodderCalories=QString(myTopElement.firstChildElement("fodderCalories").text()).toInt();
  mYieldUnits=QString(myTopElement.firstChildElement("yieldUnits").text()).toInt();

    
  return true;
}

QString LaPlant::toXml()
{
  QString myString = QString("<Plant Id=\"" + mName + "\"/>\n");
          myString+=QString("<plant>\n");
            myString+=QString("  <name>" + mName + "</name>\n");
            myString+=QString("  <yield>" + QString::number(mCropYield) + "</yield>\n");
            myString+=QString("  <cropCalories>" + QString::number(mCropCalories) + "</cropCalories>\n");
            myString+=QString("  <fodderProduction>" + QString::number(mCropFodderProduction) + "</fodderProduction>\n");
            myString+=QString("  <fodderCalories>" + QString::number(mCropFodderCalories) + "</fodderCalories>\n");
            myString+=QString("  <yieldUnits>" + QString::number(mYieldUnits) + "</yieldUnits>\n");
          myString+=QString("</plant>\n");
  return myString;
}

QString LaPlant::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("cropYield=>" + QString::number(mCropYield) + "\n");
  myString+=QString("cropCalories=>" + QString::number(mCropCalories) + "\n");
  myString+=QString("fodderProduction=>" + QString::number(mCropFodderProduction) + "\n");
  myString+=QString("fodderCalories=>" + QString::number(mCropFodderCalories) + "\n");
  myString+=QString("yieldUnits=>" + QString::number(mYieldUnits) + "\n");
  return myString;
}
QString LaPlant::toHtml()
{
  QString myString;
  myString+=QString("<BODY>") + "\n";
  myString+=QString("<P><B><U><I>Details for "
                     + LaUtils::xmlEncode(mName)
                     + " </I></U></B>" + "\n");
  myString+=QString("</P>") + "\n";
  myString+=QString("<P>" + guid() + "\n");
  myString+=QString("</P>") + "\n";
  myString+=QString("<P>(Global Unique Identifier)") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P><B>Average Crop Yield: </B>"
                    +QString::number(mCropYield)
                    + "\n");
  myString+=QString("</P>") + "\n";
  myString+=QString("<P><B>Calories per Kg: </B>"
                    + QString::number(mCropCalories)
                    + "\n");
  myString+=QString("</P>");
  myString+=QString("<P><B>Kg of Fodder produced: </B>"
                    +QString::number(mCropFodderProduction)
                    + "\n");
  myString+=QString("</P>");
  myString+=QString("<P><B>Calories per Kg in fodder: </B>"
                    + QString::number(mCropFodderCalories)
                    + "\n");
  myString+=QString("</P>");
  myString+=QString("<P><B>AreaUnits(0=Dunum, 2=Hectare): </B>"
                    + QString::number(mYieldUnits)
                    + "\n");
  myString+=QString("</P>") + "\n";
  myString+=QString("</BODY>") + "\n";
  return myString;
}
