/***************************************************************************
                          laanimal.cpp  -  The animal class
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
#include "laanimal.h"
#include "lautils.h"

LaAnimal::LaAnimal() : LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mUsableMeat=0;
  mKillWeight=0;
  mGrowTime=0;
  mDeathRate=0;
  mGestating=0;
  mLactating=0;
  mJuvenile=0;
  mLifeExpectancy=0;
  mBreedingExpectancy=0;
  mYoungPerBirth=0;
  mWeaningAge=0;
  mGestationTime=0;
  mEstrousCycle=0;
}
LaAnimal::~LaAnimal()
{

}

//copy constructor
LaAnimal::LaAnimal(const LaAnimal& theAnimal)
{
  mName=theAnimal.name();
  setGuid(theAnimal.guid());
  mUsableMeat=theAnimal.usableMeat();
  mKillWeight=theAnimal.killWeight();
  mGrowTime=theAnimal.growTime();
  mDeathRate=theAnimal.deathRate();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mJuvenile=theAnimal.juvenile();
  mLifeExpectancy=theAnimal.lifeExpectancy();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
}

LaAnimal& LaAnimal::operator=(const LaAnimal& theAnimal)
{
  if (this == &theAnimal) return *this;   // Gracefully handle self assignment

  mName=theAnimal.name();
  setGuid(theAnimal.guid());
  mUsableMeat=theAnimal.usableMeat();
  mKillWeight=theAnimal.killWeight();
  mGrowTime=theAnimal.growTime();
  mDeathRate=theAnimal.deathRate();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mJuvenile=theAnimal.juvenile();
  mLifeExpectancy=theAnimal.lifeExpectancy();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
  return *this;
}

QString LaAnimal::name() const
{
  return mName;
}
int LaAnimal::usableMeat() const
{
  return mUsableMeat;
}
int LaAnimal::killWeight() const
{
  return mKillWeight;
}
int LaAnimal::growTime() const
{
  return mGrowTime;
}
int LaAnimal::deathRate() const
{
  return mDeathRate;
}
int LaAnimal::gestating() const
{
  return mGestating;
}
int LaAnimal::lactating() const
{
  return mLactating;
}
int LaAnimal::juvenile() const
{
  return mJuvenile;
}
int LaAnimal::lifeExpectancy() const
{
  return mLifeExpectancy;
}
int LaAnimal::breedingExpectancy() const
{
  return mBreedingExpectancy;
}
int LaAnimal::youngPerBirth() const
{
  return mYoungPerBirth;
}
int LaAnimal::weaningAge() const
{
  return mWeaningAge;
}
int LaAnimal::gestationTime() const
{
  return mGestationTime;
}
int LaAnimal::estrousCycle() const
{
  return mEstrousCycle;
}
void LaAnimal::setName(QString theName)
{
  mName=theName;
}
void LaAnimal::setUsableMeat(int thePercentage)
{
  if (thePercentage > 100) {thePercentage=100;}
  if (thePercentage < 0) {thePercentage=100;}
  mUsableMeat=thePercentage;
}

void LaAnimal::setKillWeight(int theKg)
{
  mKillWeight=theKg;
}
void LaAnimal::setGrowTime(int theWeeks)
{
  mGrowTime=theWeeks;
}
void LaAnimal::setDeathRate(int thePercentage)
{
  mDeathRate=thePercentage;
}
void LaAnimal::setGestating(int theCalories)
{
  mGestating=theCalories;
}
void LaAnimal::setLactating(int theCalories)
{
  mLactating=theCalories;
}
void LaAnimal::setJuvenile(int theCalories)
{
  mJuvenile=theCalories;
}
void LaAnimal::setLifeExpectancy(int theYears)
{
  mLifeExpectancy=theYears;
}
void LaAnimal::setBreedingExpectancy(int theYears)
{
  mBreedingExpectancy=theYears;
}
void LaAnimal::setYoungPerBirth(int theInteger)
{
  mYoungPerBirth=theInteger;
}
void LaAnimal::setWeaningAge(int theWeeks)
{
  mWeaningAge=theWeeks;
}
void LaAnimal::setGestationTime(int theDays)
{
  mGestationTime=theDays;
}
void LaAnimal::setEstrousCycle(int theDays)
{
  mEstrousCycle=theDays;
}

bool LaAnimal::fromXml(QString theXml)
{
  qDebug("Loading animal from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("animal");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
    qDebug("top element could not be found!");
  }
  qDebug("Animal::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  qDebug("Animal::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
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

QString LaAnimal::toXml()
{
  QString myString;
  myString+=QString("<animal guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <usableMeat>" + QString::number(mUsableMeat) + "</usableMeat>\n");
  myString+=QString("  <killWeight>" + QString::number(mKillWeight) + "</killWeight>\n");
  myString+=QString("  <growTime>" + QString::number(mGrowTime) + "</growTime>\n");
  myString+=QString("  <deathRate>" + QString::number(mDeathRate) + "</deathRate>\n");
  myString+=QString("  <gestating>" + QString::number(mGestating) + "</gestating>\n");
  myString+=QString("  <lactating>" + QString::number(mLactating) + "</lactating>\n");
  myString+=QString("  <juvenile>" + QString::number(mJuvenile) + "</juvenile>\n");
  myString+=QString("  <lifeExpectancy>" + QString::number(mLifeExpectancy) + "</lifeExpectancy>\n");
  myString+=QString("  <breedingLife>" + QString::number(mBreedingExpectancy) + "</breedingLife>\n");
  myString+=QString("  <youngPerBirth>" + QString::number(mYoungPerBirth) + "</youngPerBirth>\n");
  myString+=QString("  <weaningAge>" + QString::number(mWeaningAge) + "</weaningAge>\n");
  myString+=QString("  <gestationTime>" + QString::number(mGestationTime) + "</gestationTime>\n");
  myString+=QString("  <estrousCycle>" + QString::number(mEstrousCycle) + "</estrousCycle>\n");
  myString+=QString("</animal>\n");
  return myString;
}

QString LaAnimal::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("usableMeat=>" + QString::number(mUsableMeat) + "\n");
  myString+=QString("killWeight=>" + QString::number(mKillWeight) + "\n");
  myString+=QString("growTime=>" + QString::number(mGrowTime) + "\n");
  myString+=QString("deathRate=>" + QString::number(mDeathRate) + "\n");
  myString+=QString("gestating=>" + QString::number(mGestating) + "\n");
  myString+=QString("lactating=>" + QString::number(mLactating) + "\n");
  myString+=QString("juvenile=>" + QString::number(mJuvenile) + "\n");
  myString+=QString("lifeExpectancy=>" + QString::number(mLifeExpectancy) + "\n");
  myString+=QString("breedingLife=>" + QString::number(mBreedingExpectancy) + "\n");
  myString+=QString("youngPerBirth=>" + QString::number(mYoungPerBirth) + "\n");
  myString+=QString("weaningAge=>" + QString::number(mWeaningAge) + "\n");
  myString+=QString("gestationTime=>" + QString::number(mGestationTime) + "\n");
  myString+=QString("estrousCycle=>" + QString::number(mEstrousCycle) + "\n");
  return myString;
}

QString LaAnimal::toHtml()
{
  QString myString;
  myString+=QString("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">") + "\n";
  myString+=QString("<HTML>") + "\n";
  myString+=QString("<HEAD>") + "\n";
  myString+=QString("<META HTTP-EQUIV=\"CONTENT-TYPE\" CONTENT=\"text/html; charset=utf-8\">") + "\n";
  myString+=QString("<TITLE></TITLE>") + "\n";
  myString+=QString("<META NAME=\"GENERATOR\" CONTENT=\"OpenOffice.org 2.0  (Linux)\">") + "\n";
  myString+=QString("<META NAME=\"CREATED\" CONTENT=\"20070222;14254000\">") + "\n";
  myString+=QString("<META NAME=\"CHANGED\" CONTENT=\"20070222;14332600\">") + "\n";
  myString+=QString("<STYLE TYPE=\"text/css\">") + "\n";
  myString+=QString("<!--") + "\n";
  myString+=QString("@page { margin: 2cm }") + "\n";
  myString+=QString("P { margin-bottom: 0cm }") + "\n";
  myString+=QString("P.western { so-language: en-GB }") + "\n";
  myString+=QString("A:link { color: #000000; text-decoration: none }") + "\n";
  myString+=QString("A:visited { color: #000000; text-decoration: none }") + "\n";
  myString+=QString("-->") + "\n";
  myString+=QString("</STYLE>") + "\n";
  myString+=QString("</HEAD>") + "\n";
  myString+=QString("<BODY LANG=\"en-GB\" LINK=\"#000000\" VLINK=\"#000000\" DIR=\"LTR\">") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=CENTER><FONT SIZE=4 STYLE=\"font-size: 16pt\"><B><U><I>Details for "
                     + LaUtils::xmlEncode(mName)
                     + " </I></U></B></FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=CENTER><FONT COLOR=\"#008000\">"
                    + guid()
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=CENTER><FONT COLOR=\"#008000\">(Global Unique Identifier) </FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Percentage Usable Meat: </B>"
                    +QString::number(mUsableMeat)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Kill Weight: </B>"
                    + QString::number(mKillWeight)
                    + "</FONT>") + "\n";
  myString+=QString("</P>");
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Grow Time: </B>"
                    +QString::number(mGrowTime)
                    + "</FONT>") + "\n";
  myString+=QString("</P>");
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Death Rate: </B>"
                    + QString::number(mDeathRate)
                    + "</FONT>") + "\n";
  myString+=QString("</P>");
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Calories for Gestating female: </B>"
                    + QString::number(mGestating)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Calories for Lactating female: </B>"
                    + QString::number(mLactating)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Calories for Juvenile: </B>"
                    + QString::number(mJuvenile)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Life Expectancy: </B>"
                    + QString::number(mLifeExpectancy)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Breeding Life: </B>"
                    + QString::number(mBreedingExpectancy)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Young Per Birth: </B>"
                    + QString::number(mYoungPerBirth)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Weaning Age: </B>"
                    + QString::number(mWeaningAge)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Gestation Time: </B>"
                    + QString::number(mGestationTime)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("<P CLASS=\"western\" ALIGN=RIGHT><FONT SIZE=3 STYLE=\"font-size: 13pt\"><B>Estrous Cycle: </B>"
                    + QString::number(mEstrousCycle)
                    + "</FONT>") + "\n";
  myString+=QString("</P>") + "\n";
  myString+=QString("</BODY>") + "\n";
  myString+=QString("</HTML>") + "\n";
  return myString;
}
