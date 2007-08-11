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
  mDescription="Not Set";
  mMeatFoodValue=3000;
  mUsableMeat=50;
  mKillWeight=100;
  mGrowTime=10;
  mDeathRate=10;
  mGestating=5000;
  mLactating=5000;
  mJuvenile=3500;
  mSexualMaturity=18;
  mBreedingExpectancy=5;
  mYoungPerBirth=1;
  mWeaningAge=12;
  mGestationTime=120;
  mEstrousCycle=21;
}
LaAnimal::~LaAnimal()
{

}

//copy constructor
LaAnimal::LaAnimal(const LaAnimal& theAnimal)
{
  mName=theAnimal.name();
  mDescription=theAnimal.description();
  mMeatFoodValue=theAnimal.meatFoodValue();
  setGuid(theAnimal.guid());
  mUsableMeat=theAnimal.usableMeat();
  mKillWeight=theAnimal.killWeight();
  mGrowTime=theAnimal.growTime();
  mDeathRate=theAnimal.deathRate();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mJuvenile=theAnimal.juvenile();
  mSexualMaturity=theAnimal.sexualMaturity();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
  mImageFile=theAnimal.imageFile();
}

LaAnimal& LaAnimal::operator=(const LaAnimal& theAnimal)
{
  if (this == &theAnimal) return *this;   // Gracefully handle self assignment

  mName=theAnimal.name();
  mDescription=theAnimal.description();
  setGuid(theAnimal.guid());
  mMeatFoodValue=theAnimal.meatFoodValue();
  mUsableMeat=theAnimal.usableMeat();
  mKillWeight=theAnimal.killWeight();
  mGrowTime=theAnimal.growTime();
  mDeathRate=theAnimal.deathRate();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mJuvenile=theAnimal.juvenile();
  mSexualMaturity=theAnimal.sexualMaturity();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
  mImageFile=theAnimal.imageFile();
  return *this;
}

QString LaAnimal::name() const
{
  return mName;
}
QString LaAnimal::description() const
{
  return mDescription;
}
int LaAnimal::meatFoodValue() const
{
  return mMeatFoodValue;
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
int LaAnimal::sexualMaturity() const
{
  return mSexualMaturity;
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
QString LaAnimal::imageFile() const
{
  return mImageFile;
}
void LaAnimal::setName(QString theName)
{
  mName=theName;
}
void LaAnimal::setDescription(QString theDescription)
{
  mDescription=theDescription;
}
void LaAnimal::setMeatFoodValue(int theMeatFoodValue)
{
  mMeatFoodValue=theMeatFoodValue;
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
void LaAnimal::setSexualMaturity(int theMonths)
{
  mSexualMaturity=theMonths;
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
void LaAnimal::setImageFile(QString theImageFileName)
{
  mImageFile=theImageFileName;
}
bool LaAnimal::fromXml(QString theXml)
{
  //qDebug("Loading animal from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("animal");
  if (myTopElement.isNull())
  {
    //TODO - just make this a warning
   //qDebug("top element could not be found!");
  }
  //qDebug("Animal::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  //qDebug("Animal::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mDescription=LaUtils::xmlDecode(myTopElement.firstChildElement("description").text());
  mMeatFoodValue=QString(myTopElement.firstChildElement("meatFoodValue").text()).toInt();
  mUsableMeat=QString(myTopElement.firstChildElement("usableMeat").text()).toInt();
  mKillWeight=QString(myTopElement.firstChildElement("killWeight").text()).toInt();
  mGrowTime=QString(myTopElement.firstChildElement("growTime").text()).toInt();
  mDeathRate=QString(myTopElement.firstChildElement("deathRate").text()).toInt();
  mGestating=QString(myTopElement.firstChildElement("gestating").text()).toInt();
  mLactating=QString(myTopElement.firstChildElement("lactating").text()).toInt();
  mJuvenile=QString(myTopElement.firstChildElement("juvenile").text()).toInt();
  mSexualMaturity=QString(myTopElement.firstChildElement("sexualMaturity").text()).toInt();
  mBreedingExpectancy=QString(myTopElement.firstChildElement("breedingExpectancy").text()).toInt();
  mYoungPerBirth=QString(myTopElement.firstChildElement("youngPerBirth").text()).toInt();
  mWeaningAge=QString(myTopElement.firstChildElement("weaningAge").text()).toInt();
  mGestationTime=QString(myTopElement.firstChildElement("gestationTime").text()).toInt();
  mEstrousCycle=QString(myTopElement.firstChildElement("estrousCycle").text()).toInt();
  mImageFile=QString(myTopElement.firstChildElement("imageFile").text());
  return true;
}

QString LaAnimal::toXml()
{
  QString myString;
  myString+=QString("<animal guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <description>" + LaUtils::xmlEncode(mDescription) + "</description>\n");
  myString+=QString("  <meatFoodValue>" + QString::number(mMeatFoodValue) + "</meatFoodValue>\n");
  myString+=QString("  <usableMeat>" + QString::number(mUsableMeat) + "</usableMeat>\n");
  myString+=QString("  <killWeight>" + QString::number(mKillWeight) + "</killWeight>\n");
  myString+=QString("  <growTime>" + QString::number(mGrowTime) + "</growTime>\n");
  myString+=QString("  <deathRate>" + QString::number(mDeathRate) + "</deathRate>\n");
  myString+=QString("  <gestating>" + QString::number(mGestating) + "</gestating>\n");
  myString+=QString("  <lactating>" + QString::number(mLactating) + "</lactating>\n");
  myString+=QString("  <juvenile>" + QString::number(mJuvenile) + "</juvenile>\n");
  myString+=QString("  <sexualMaturity>" + QString::number(mSexualMaturity) + "</sexualMaturity>\n");
  myString+=QString("  <breedingExpectancy>" + QString::number(mBreedingExpectancy) + "</breedingExpectancy>\n");
  myString+=QString("  <youngPerBirth>" + QString::number(mYoungPerBirth) + "</youngPerBirth>\n");
  myString+=QString("  <weaningAge>" + QString::number(mWeaningAge) + "</weaningAge>\n");
  myString+=QString("  <gestationTime>" + QString::number(mGestationTime) + "</gestationTime>\n");
  myString+=QString("  <estrousCycle>" + QString::number(mEstrousCycle) + "</estrousCycle>\n");
  myString+=QString("  <imageFile>" + LaUtils::xmlEncode(mImageFile) + "</imageFile>\n");
  myString+=QString("</animal>\n");
  return myString;
}

QString LaAnimal::toText()
{
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("description=>" + LaUtils::xmlEncode(mDescription) + "\n");
  myString+=QString("meatFoodValue=>" + QString::number(mMeatFoodValue) + "\n");
  myString+=QString("usableMeat=>" + QString::number(mUsableMeat) + "\n");
  myString+=QString("killWeight=>" + QString::number(mKillWeight) + "\n");
  myString+=QString("growTime=>" + QString::number(mGrowTime) + "\n");
  myString+=QString("deathRate=>" + QString::number(mDeathRate) + "\n");
  myString+=QString("gestating=>" + QString::number(mGestating) + "\n");
  myString+=QString("lactating=>" + QString::number(mLactating) + "\n");
  myString+=QString("juvenile=>" + QString::number(mJuvenile) + "\n");
  myString+=QString("sexualMaturity=>" + QString::number(mSexualMaturity) + "\n");
  myString+=QString("breedingExpectancy=>" + QString::number(mBreedingExpectancy) + "\n");
  myString+=QString("youngPerBirth=>" + QString::number(mYoungPerBirth) + "\n");
  myString+=QString("weaningAge=>" + QString::number(mWeaningAge) + "\n");
  myString+=QString("gestationTime=>" + QString::number(mGestationTime) + "\n");
  myString+=QString("estrousCycle=>" + QString::number(mEstrousCycle) + "\n");
  return myString;
}

QString LaAnimal::toHtml()
{
  QString myString;
  myString+="<h2>Details for " + LaUtils::xmlEncode(mName) + "</h2>";
  myString+="<table>";
  myString+="<tr><td><b>Description:</b></td><td>" + mDescription + "</td></tr>";
  myString+="<tr><td><b>Meat Food Value:</b></td><td>" + QString::number(mMeatFoodValue) + "</td></tr>";
  myString+="<tr><td><b>Usable Meat (%):</b></td><td>" + QString::number(mUsableMeat) + "</td></tr>";

  myString+="<tr><td><b>Sexual Maturity:</b></td><td>" + QString::number(mSexualMaturity) + "</td></tr>";
  myString+="<tr><td><b>Years Breedable:</b></td><td>" + QString::number(mBreedingExpectancy) + "</td></tr>";
  myString+="<tr><td><b>Young Per Birth:</b></td><td>" + QString::number(mYoungPerBirth) + "</td></tr>";
  myString+="<tr><td><b>Weaning Age:</b></td><td>" + QString::number(mWeaningAge) + "</td></tr>";
  myString+="<tr><td><b>Kill Weight (Kg):</b></td><td>" + QString::number(mKillWeight) + "</td></tr>";
  myString+="<tr><td><b>Grow Time:</b></td><td>" + QString::number(mGrowTime) + "</td></tr>";
  myString+="<tr><td><b>Death Rate (%):</b></td><td>" + QString::number(mDeathRate) + "</td></tr>";

  myString+="<tr><td><b>Gestation Time:</b></td><td>" + QString::number(mGestationTime) + "</td></tr>";
  myString+="<tr><td><b>Estrous Cycle:</b></td><td>" + QString::number(mEstrousCycle) + "</td></tr>";
  myString+="<tr><td></td><td>";
  myString+="<tr><td><FONT COLOR=\"#0063F7\">TDN Requirements (Kg/yr)</FONT></td><td>";
  myString+="<tr><td><b>Gestating Female:</b></td><td>" + QString::number(mGestating) + "</td></tr>";
  myString+="<tr><td><b>Lactating Female:</b></td><td>" + QString::number(mLactating) + "</td></tr>";
  myString+="<tr><td><b>Juveniles:</b></td><td>" + QString::number(mJuvenile) + "</td></tr>";
  myString+="</table>";
  return myString;
}
