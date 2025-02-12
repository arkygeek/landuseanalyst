/***************************************************************************
                          laanimal.cpp  -  The animal class
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton
                         : (C) 2009 by Jason Jorgenson
    email                : tim@linfiniti.com
                         : jjorgenson@gmail.com
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
    //mGestating=5000;//
    //mLactating=5000;
    //mJuvenile=3500;
  mSexualMaturity=18;
  mBreedingExpectancy=5;
  mYoungPerBirth=1;
  mWeaningAge=12;
  mWeaningWeight=30;
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
  mFeedEnergyType=theAnimal.feedEnergyType();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mMaintenance=theAnimal.maintenance();
  mJuvenile=theAnimal.juvenile();
  mSexualMaturity=theAnimal.sexualMaturity();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mConceptionEfficiency=theAnimal.conceptionEfficiency();
  mFemalesToMales=theAnimal.femalesPerMale();
  mAdultWeight=theAnimal.adultWeight();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mWeaningWeight=theAnimal.weaningWeight();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
  mLactationTime=theAnimal.lactationTime();
  mMilk=theAnimal.milk();
  mMilkGramsPerDay=theAnimal.milkGramsPerDay();
  mMilkFoodValue=theAnimal.milkFoodValue();
  mFleece=theAnimal.fleece();
  mFleeceWeightKg=theAnimal.fleeceWeightKg();
  mImageFile=theAnimal.imageFile();
}

LaAnimal& LaAnimal::operator=(const LaAnimal& theAnimal)
{
  if (this == &theAnimal) return *this;     // Gracefully handle self assignment

  mName=theAnimal.name();
  mDescription=theAnimal.description();
  setGuid(theAnimal.guid());
  mMeatFoodValue=theAnimal.meatFoodValue();
  mUsableMeat=theAnimal.usableMeat();
  mKillWeight=theAnimal.killWeight();
  mGrowTime=theAnimal.growTime();
  mDeathRate=theAnimal.deathRate();
  mFeedEnergyType=theAnimal.feedEnergyType();
  mGestating=theAnimal.gestating();
  mLactating=theAnimal.lactating();
  mMaintenance=theAnimal.maintenance();
  mJuvenile=theAnimal.juvenile();
  mSexualMaturity=theAnimal.sexualMaturity();
  mBreedingExpectancy=theAnimal.breedingExpectancy();
  mYoungPerBirth=theAnimal.youngPerBirth();
  mWeaningAge=theAnimal.weaningAge();
  mWeaningWeight=theAnimal.weaningWeight();
  mConceptionEfficiency=theAnimal.conceptionEfficiency();
  mFemalesToMales=theAnimal.femalesPerMale();
  mAdultWeight=theAnimal.adultWeight();
  mGestationTime=theAnimal.gestationTime();
  mEstrousCycle=theAnimal.estrousCycle();
  mLactationTime=theAnimal.lactationTime();
  mMilk=theAnimal.milk();
  mMilkGramsPerDay=theAnimal.milkGramsPerDay();
  mMilkFoodValue=theAnimal.milkFoodValue();
  mFleece=theAnimal.fleece();
  mFleeceWeightKg=theAnimal.fleeceWeightKg();
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
EnergyType LaAnimal::feedEnergyType() const
{
 return mFeedEnergyType; 
}
int LaAnimal::gestating() const
{
  return mGestating;
}
int LaAnimal::lactating() const
{
  return mLactating;
}
int LaAnimal::maintenance() const
{
  return mMaintenance;
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
int LaAnimal::conceptionEfficiency() const
{
  return mConceptionEfficiency;
}

int LaAnimal::femalesPerMale() const
{
  return mFemalesToMales;
}

int LaAnimal::adultWeight() const
{
  return mAdultWeight;
}
int LaAnimal::youngPerBirth() const
{
  return mYoungPerBirth;
}
int LaAnimal::weaningAge() const
{
  return mWeaningAge;
}
int LaAnimal::weaningWeight() const
{
  return mWeaningWeight;
}
int LaAnimal::gestationTime() const
{
  return mGestationTime;
}
int LaAnimal::estrousCycle() const
{
  return mEstrousCycle;
}
int LaAnimal::lactationTime() const
{
 return mLactationTime; 
}

bool LaAnimal::milk() const
{
  return mMilk;
}
int  LaAnimal::milkGramsPerDay() const
{
  return mMilkGramsPerDay;
}
int  LaAnimal::milkFoodValue() const
{
  return mMilkFoodValue;
}
bool LaAnimal::fleece() const
{
  return mFleece;
}
int  LaAnimal::fleeceWeightKg() const
{
  return mFleeceWeightKg;
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
void LaAnimal::setFeedEnergyType(EnergyType theEnergyType)
{
  mFeedEnergyType=theEnergyType; 
}
void LaAnimal::setGestating(int theCalories)
{
  mGestating=theCalories;
}
void LaAnimal::setLactating(int theCalories)
{
  mLactating=theCalories;
}
void LaAnimal::setMaintenance(int theCalories)
{
  mMaintenance=theCalories;
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
void LaAnimal::setConceptionEfficiency(int thePercentage)
{
  mConceptionEfficiency=thePercentage;
}
void LaAnimal::setFemalesToMales(int theInt)
{
  mFemalesToMales=theInt;
}
void LaAnimal::setAdultWeight(int theKg)
{
  mAdultWeight=theKg;
}
void LaAnimal::setYoungPerBirth(int theInteger)
{
  mYoungPerBirth=theInteger;
}
void LaAnimal::setWeaningAge(int theWeeks)
{
  mWeaningAge=theWeeks;
}
void LaAnimal::setWeaningWeight(int theWeight)
{
  mWeaningWeight=theWeight;
}
void LaAnimal::setGestationTime(int theDays)
{
  mGestationTime=theDays;
}
void LaAnimal::setEstrousCycle(int theDays)
{
  mEstrousCycle=theDays;
}

void LaAnimal::setLactationTime (int theTime)
{
  mLactationTime = theTime; 
}

void LaAnimal::setMilk (bool theBool)
{
  mMilk = theBool;
}
void LaAnimal::setMilkGramsPerDay(int theMilkGrams)
{
  mMilkGramsPerDay = theMilkGrams;
}
void LaAnimal::setMilkFoodValue (int theMilkFoodValue)
{
  mMilkFoodValue = theMilkFoodValue;
}
void LaAnimal::setFleece (bool theFleeceBool)
{
  mFleece = theFleeceBool;
}
void LaAnimal::setFleeceWeightKg (int theFleeceWeight)
{
  mFleeceWeightKg = theFleeceWeight;
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
  mAdultWeight=QString(myTopElement.firstChildElement("adultWeight").text()).toInt();
  mConceptionEfficiency=QString(myTopElement.firstChildElement("conceptionEfficiency").text()).toInt();
  mFemalesToMales=QString(myTopElement.firstChildElement("femalesToMales").text()).toInt();
  mGrowTime=QString(myTopElement.firstChildElement("growTime").text()).toInt();
  mDeathRate=QString(myTopElement.firstChildElement("deathRate").text()).toInt();
  
  QString myFeedEnergyType = QString(myTopElement.firstChildElement("feedEnergyType").text());
  if (myFeedEnergyType == "KCalories")
  {
    mFeedEnergyType=KCalories;
  }
  else if (myFeedEnergyType == "TDN")
  {
    mFeedEnergyType=TDN;
  }
  mGestating=QString(myTopElement.firstChildElement("gestating").text()).toInt();
  mLactating=QString(myTopElement.firstChildElement("lactating").text()).toInt();
  mMaintenance=QString(myTopElement.firstChildElement("maintenance").text()).toInt();
  mJuvenile=QString(myTopElement.firstChildElement("juvenile").text()).toInt();
  mSexualMaturity=QString(myTopElement.firstChildElement("sexualMaturity").text()).toInt();
  mBreedingExpectancy=QString(myTopElement.firstChildElement("breedingExpectancy").text()).toInt();
  mYoungPerBirth=QString(myTopElement.firstChildElement("youngPerBirth").text()).toInt();
  mWeaningAge=QString(myTopElement.firstChildElement("weaningAge").text()).toInt();
  mWeaningWeight=QString(myTopElement.firstChildElement("weaningWeight").text()).toInt();
  mGestationTime=QString(myTopElement.firstChildElement("gestationTime").text()).toInt();
  mEstrousCycle=QString(myTopElement.firstChildElement("estrousCycle").text()).toInt();
  mLactationTime=QString(myTopElement.firstChildElement("lactationTime").text()).toInt();
  mMilk=QString(myTopElement.firstChildElement("milk").text()).toInt();
  mMilkGramsPerDay=QString(myTopElement.firstChildElement("milkGramsPerDay").text()).toInt();
  mMilkFoodValue=QString(myTopElement.firstChildElement("milkFoodValue").text()).toInt();
  mFleece=QString(myTopElement.firstChildElement("fleece").text()).toInt();
  mFleeceWeightKg=QString(myTopElement.firstChildElement("fleeceWeightKg").text()).toInt();
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
  myString+=QString("  <adultWeight>" + QString::number(mAdultWeight) + "</adultWeight>\n");
  myString+=QString("  <conceptionEfficiency>" + QString::number(mConceptionEfficiency) + "</conceptionEfficiency>\n");
  myString+=QString("  <femalesToMales>" + QString::number(mFemalesToMales) + "</femalesToMales>\n");
  myString+=QString("  <growTime>" + QString::number(mGrowTime) + "</growTime>\n");
  myString+=QString("  <deathRate>" + QString::number(mDeathRate) + "</deathRate>\n");
  
  switch (mFeedEnergyType)
  {
    case KCalories:
      myString+=QString("  <feedEnergyType>KCalories</feedEnergyType>\n");
      break;
    case TDN:
      myString+=QString("  <feedEnergyType>TDN</feedEnergyType>\n");
      break;
  }
  
  myString+=QString("  <gestating>" + QString::number(mGestating) + "</gestating>\n");
  myString+=QString("  <lactating>" + QString::number(mLactating) + "</lactating>\n");
  myString+=QString("  <maintenance>" + QString::number(mMaintenance) + "</maintenance>\n");
  myString+=QString("  <juvenile>" + QString::number(mJuvenile) + "</juvenile>\n");
  myString+=QString("  <sexualMaturity>" + QString::number(mSexualMaturity) + "</sexualMaturity>\n");
  myString+=QString("  <breedingExpectancy>" + QString::number(mBreedingExpectancy) + "</breedingExpectancy>\n");
  myString+=QString("  <youngPerBirth>" + QString::number(mYoungPerBirth) + "</youngPerBirth>\n");
  myString+=QString("  <weaningAge>" + QString::number(mWeaningAge) + "</weaningAge>\n");
  myString+=QString("  <weaningWeight>" + QString::number(mWeaningWeight) + "</weaningWeight>\n");
  myString+=QString("  <gestationTime>" + QString::number(mGestationTime) + "</gestationTime>\n");
  myString+=QString("  <estrousCycle>" + QString::number(mEstrousCycle) + "</estrousCycle>\n");
  myString+=QString("  <lactationTime>" + QString::number(mLactationTime) + "</lactationTime>\n");
  myString+=QString("  <milk>" + QString::number(mMilk) + "</milk>\n");
  myString+=QString("  <milkGramsPerDay>" + QString::number(mMilkGramsPerDay) + "</milkGramsPerDay>\n");
  myString+=QString("  <milkFoodValue>" + QString::number(mMilkFoodValue) + "</milkFoodValue>\n");
  myString+=QString("  <fleece>" + QString::number(mFleece) + "</fleece>\n");
  myString+=QString("  <fleeceWeightKg>" + QString::number(mFleeceWeightKg) + "</fleeceWeightKg>\n");
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
  myString+=QString("adultWeight=>" + QString::number(mAdultWeight) + "\n");
  myString+=QString("conceptionEfficiency=>" + QString::number(mConceptionEfficiency) + "\n");
  myString+=QString("femalesToMales=>" + QString::number(mFemalesToMales) + "\n");
  myString+=QString("growTime=>" + QString::number(mGrowTime) + "\n");
  myString+=QString("deathRate=>" + QString::number(mDeathRate) + "\n");
  
  switch (mFeedEnergyType)
  {
    case KCalories:
      myString+=QString("feedEnergyType=>KCalories\n");
      break;
    case TDN:
      myString+=QString("feedEnergyType=>TDN\n");
      break;
  }
  
  myString+=QString("gestating=>" + QString::number(mGestating) + "\n");
  myString+=QString("lactating=>" + QString::number(mLactating) + "\n");
  myString+=QString("maintenance=>" + QString::number(mMaintenance) + "\n");
  myString+=QString("juvenile=>" + QString::number(mJuvenile) + "\n");
  myString+=QString("sexualMaturity=>" + QString::number(mSexualMaturity) + "\n");
  myString+=QString("breedingExpectancy=>" + QString::number(mBreedingExpectancy) + "\n");
  myString+=QString("youngPerBirth=>" + QString::number(mYoungPerBirth) + "\n");
  myString+=QString("weaningAge=>" + QString::number(mWeaningAge) + "\n");
  myString+=QString("weaningWeight=>" + QString::number(mWeaningWeight) + "\n");
  myString+=QString("gestationTime=>" + QString::number(mGestationTime) + "\n");
  myString+=QString("estrousCycle=>" + QString::number(mEstrousCycle) + "\n");
  myString+=QString("lactationTime=>" + QString::number(mLactationTime) + "\n");
  myString+=QString("milk=>" + QString::number(mMilk) + "\n");
  myString+=QString("milkGramsPerDay=>" + QString::number(mMilkGramsPerDay) + "\n");
  myString+=QString("milkFoodValue=>" + QString::number(mMilkFoodValue) + "\n");
  myString+=QString("fleece=>" + QString::number(mFleece) + "\n");
  myString+=QString("fleeceWeightKg=>" + QString::number(mFleeceWeightKg) + "\n");
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
  myString+="<tr><td><b>Weaning Weight:</b></td><td>" + QString::number(mWeaningWeight) + "</td></tr>";
  myString+="<tr><td><b>Kill Weight (Kg):</b></td><td>" + QString::number(mKillWeight) + "</td></tr>";
  
  myString+="<tr><td><b>Adult Weight (Kg):</b></td><td>" + QString::number(mAdultWeight) + "</td></tr>";
  myString+="<tr><td><b>Conception Efficiency(Percent):</b></td><td>" + QString::number(mConceptionEfficiency) + "</td></tr>";
  myString+="<tr><td><b>Females to Males (Breeding):</b></td><td>" + QString::number(mFemalesToMales) + "</td></tr>";
  myString+="<tr><td><b>Grow Time:</b></td><td>" + QString::number(mGrowTime) + "</td></tr>";
  myString+="<tr><td><b>Death Rate (%):</b></td><td>" + QString::number(mDeathRate) + "</td></tr>";

  myString+="<tr><td><b>Gestation Time:</b></td><td>" + QString::number(mGestationTime) + "</td></tr>";
  myString+="<tr><td><b>Estrous Cycle:</b></td><td>" + QString::number(mEstrousCycle) + "</td></tr>";
  myString+="<tr><td><b>lactationTime:</b></td><td>" + QString::number(mLactationTime) + "</td></tr>";
  myString+="<tr><td><b>milk:</b></td><td>" + QString::number(mMilk) + "</td></tr>";
  myString+="<tr><td><b>milkGramsPerDay:</b></td><td>" + QString::number(mMilkGramsPerDay) + "</td></tr>";
  myString+="<tr><td><b>milkFoodValue:</b></td><td>" + QString::number(mMilkFoodValue) + "</td></tr>";
  myString+="<tr><td><b>fleece:</b></td><td>" + QString::number(mFleece) + "</td></tr>";
  myString+="<tr><td><b>fleeceWeightKg:</b></td><td>" + QString::number(mFleeceWeightKg) + "</td></tr>";
  myString+="<tr><td></td><td>";
  myString+="<tr><td><FONT COLOR=\"#0063F7\">Feed Requirements (pa)</FONT></td><td>";
  
  switch (mFeedEnergyType)
  {
    case KCalories:
      myString+="<tr><td><b>EnergyType:</b></td><td>KCalories</td></tr>";
      break;
    case TDN:
      myString+="<tr><td><b>EnergyType:</b></td><td>TDN</td></tr>";
      break;
  }
  
  myString+="<tr><td><b>Gestating Female:</b></td><td>" + QString::number(mGestating) + "</td></tr>";
  myString+="<tr><td><b>Lactating Female:</b></td><td>" + QString::number(mLactating) + "</td></tr>";
  myString+="<tr><td><b>Adult Maintenance:</b></td><td>" + QString::number(mMaintenance) + "</td></tr>";
  myString+="<tr><td><b>Juveniles:</b></td><td>" + QString::number(mJuvenile) + "</td></tr>";
  myString+="</table>";
  return myString;
}
