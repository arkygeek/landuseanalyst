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

}
LaAnimal::~LaAnimal()
{

}

//copy constructor
LaAnimal::LaAnimal(const LaAnimal& theAnimal)
{
  mName=theAnimal.name();
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
  setGuid(myTopElement.attribute("guid"));
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  //etc...Jason complete here


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
