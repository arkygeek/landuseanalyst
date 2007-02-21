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
#include "laplant.h"

LaPlant::LaPlant() : LaSerialisable()
{

}
LaPlant::~LaPlant()
{

}

//copy constructor
LaPlant::LaPlant(const LaPlant& thePlant)
{
  //mName=thePlant.name();
  //mCropYield=thePlant.cropYield();
  //mCropCalories=thePlant.cropCalories();
  //mCropFodderProduction=thePlant.fodderProduction();
  //mCropFodderCalories=thePlant.fodderCalories();
  //mYield=thePlant.yieldUnits();
}

LaPlant& LaPlant::operator=(const LaPlant& thePlant)
{
  if (this == &thePlant) return *this;   // Gracefully handle self assignment

  //mName=thePlant.name();
 // mCropYield=thePlant.cropYield();
 // mCropCalories=thePlant.cropCalories();
 // mCropFodderProduction=thePlant.fodderProduction();
 // mCropFodderCalories=thePlant.fodderCalories();
 // mYield=thePlant.yieldUnits();
  return *this;
}

QString LaPlant::name() const
{
  return mName;
}
int LaPlant::usableMeat() const
{
  return mUsableMeat;
}
int LaPlant::killWeight() const
{
  return mKillWeight;
}
int LaPlant::growTime() const
{
  return mGrowTime;
}
int LaPlant::deathRate() const
{
  return mDeathRate;
}
int LaPlant::gestating() const
{
  return mGestating;
}
int LaPlant::lactating() const
{
  return mLactating;
}
int LaPlant::juvenile() const
{
  return mJuvenile;
}
int LaPlant::lifeExpectancy() const
{
  return mLifeExpectancy;
}
int LaPlant::breedingExpectancy() const
{
  return mBreedingExpectancy;
}
int LaPlant::youngPerBirth() const
{
  return mYoungPerBirth;
}
int LaPlant::weaningAge() const
{
  return mWeaningAge;
}
int LaPlant::gestationTime() const
{
  return mGestationTime;
}
int LaPlant::estrousCycle() const
{
  return mEstrousCycle;
}
void LaPlant::setName(QString theName)
{
  mName=theName;
}
void LaPlant::setUsableMeat(int thePercentage)
{
  if (thePercentage > 100) {thePercentage=100;}
  if (thePercentage < 0) {thePercentage=100;}
  mUsableMeat=thePercentage;
}

void LaPlant::setKillWeight(int theKg)
{
  mKillWeight=theKg;
}
void LaPlant::setGrowTime(int theWeeks)
{
  mGrowTime=theWeeks;
}
void LaPlant::setDeathRate(int thePercentage)
{
  mDeathRate=thePercentage;
}
void LaPlant::setGestating(int theCalories)
{
  mGestating=theCalories;
}
void LaPlant::setLactating(int theCalories)
{
  mLactating=theCalories;
}
void LaPlant::setJuvenile(int theCalories)
{
  mJuvenile=theCalories;
}
void LaPlant::setLifeExpectancy(int theYears)
{
  mLifeExpectancy=theYears;
}
void LaPlant::setBreedingExpectancy(int theYears)
{
  mBreedingExpectancy=theYears;
}
void LaPlant::setYoungPerBirth(int theInteger)
{
  mYoungPerBirth=theInteger;
}
void LaPlant::setWeaningAge(int theWeeks)
{
  mWeaningAge=theWeeks;
}
void LaPlant::setGestationTime(int theDays)
{
  mGestationTime=theDays;
}
void LaPlant::setEstrousCycle(int theDays)
{
  mEstrousCycle=theDays;
}



QString LaPlant::toXml()
{
  QString myString = QString("<Plant Id=\"" + mName + "\"/>\n");
          myString+=QString("<plant>\n");
            myString+=QString("  <name>" + mName + "</name>\n");
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
          myString+=QString("</plant>\n");
  return myString;
}
