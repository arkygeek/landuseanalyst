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

#include "laanimal.h"

LaAnimal::LaAnimal() : LaSerialisable()
{

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
QString LaAnimal::usableMeat() const
{
  return mUsableMeat;
}
QString LaAnimal::killWeight() const
{
  return mKillWeight;
}
QString LaAnimal::growTime() const
{
  return mGrowTime;
}
QString LaAnimal::deathRate() const
{
  return mDeathRate;
}
QString LaAnimal::gestating() const
{
  return mGestating;
}
QString LaAnimal::lactating() const
{
  return mLactating;
}
QString LaAnimal::juvenile() const
{
  return mJuvenile;
}
QString LaAnimal::lifeExpectancy() const
{
  return mLifeExpectancy;
}
QString LaAnimal::breedingExpectancy() const
{
  return mBreedingExpectancy;
}
QString LaAnimal::youngPerBirth() const
{
  return mYoungperBirth;
}
QString LaAnimal::weaningAge() const
{
  return mWeaningAge;
}
QString LaAnimal::gestationTime() const
{
  return mGestationTime;
}
QString LaAnimal::estrousCycle() const
{
  return mEstrousCycle;
}

void LaAnimal::setName(QString theName)
{
  mName=theName;
}
void LaAnimal::setUsableMeat(QString theName)
{
  mUsableMeat=theName;
}
void LaAnimal::setKillWeight(QString theName)
{
  mKillWeight=theName;
}
void LaAnimal::setGrowTime(QString theName)
{
  mGrowTime=theName;
}
void LaAnimal::setDeathRate(QString theName)
{
  mDeathRate=theName;
}
void LaAnimal::setGestating(QString theName)
{
  mGestating=theName;
}
void LaAnimal::setLactating(QString theName)
{
  mLactating=theName;
}
void LaAnimal::setJuvenile(QString theName)
{
  mJuvenile=theName;
}
void LaAnimal::setLifeExpectancy(QString theName)
{
  mLifeExpectancy=theName;
}
void LaAnimal::setBreedingExpectancy(QString theName)
{
  mBreedingExpectancy=theName;
}
void LaAnimal::setYoungPerBirth(QString theName)
{
  mYoungPerBirth=theName;
}
void LaAnimal::setWeaningAge(QString theName)
{
  mWeaningAge=theName;
}
void LaAnimal::setGestationTime(QString theName)
{
  mGestationTime=theName;
}
void LaAnimal::setEstrousCycle(QString theName)
{
  mEstrousCycle=theName;
}



QString LaAnimal::toXml()
{
  QString myString = QString("<Animal Id=\"" + mName.toLocal8Bit() + "\"/>\n");
          myString+=QString("<animal>\n");
            myString+=QString("  <name>" + mName.toLocal8Bit() + "</name>\n");
            myString+=QString("  <usableMeat>" + mUsableMeat.toLocal8Bit() + "</usableMeat>\n");
            myString+=QString("  <killWeight>" + mKillWeight.toLocal8Bit() + "</killWeight>\n");
            myString+=QString("  <growTime>" + mGrowTime.toLocal8Bit() + "</growTime>\n");
            myString+=QString("  <deathRate>" + mDeathRate.toLocal8Bit() + "</deathRate>\n");
            myString+=QString("  <gestating>" + mGestating.toLocal8Bit() + "</gestating>\n");
            myString+=QString("  <lactating>" + mLactating.toLocal8Bit() + "</lactating>\n");
            myString+=QString("  <juvenile>" + mJuvenile.toLocal8Bit() + "</juvenile>\n");
            myString+=QString("  <lifeExpectancy>" + mLifeExpectancy.toLocal8Bit() + "</lifeExpectancy>\n");
            myString+=QString("  <breedingLife>" + mBreedingExpectancy.toLocal8Bit() + "</breedingLife>\n");
            myString+=QString("  <youngPerBirth>" + mYoungPerBirth.toLocal8Bit() + "</youngPerBirth>\n");
            myString+=QString("  <weaningAge>" + mWeaningAge.toLocal8Bit() + "</weaningAge>\n");
            myString+=QString("  <gestationTime>" + mGestationTime.toLocal8Bit() + "</gestationTime>\n");
            myString+=QString("  <estrousCycle>" + mEstrousCycle.toLocal8Bit() + "</estrousCycle>\n");
          myString+=QString("</animal>\n");
  return myString;
}
