/***************************************************************************
 *   Copyright (C) 2007 by: Tim Sutton        tim@linfiniti.com            *
 *                          Jason Jorgenson   arkygeek@gmail.com           *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/

#include <QString>
#include <QMap>
#include <QPair>
#include <QDomDocument>
#include <QDomElement>
#include "lamodel.h"
#include "lautils.h"
#include "la.h"
#include "ladietlabels.h"

#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QListWidget>
#include <QComboBox>
#include <QHeaderView>
#include <QDebug>

LaModel::LaModel() : QObject(),  LaSerialisable(), LaGuid()
{
  setGuid();
  mName="No Name Set";
  mPopulation=1000;
  mPeriod="No Period Set";
  mProjection=100;
  mPrecision=5;
  mDietPercent=25;
  mPercentOfDietThatIsFromCrops=10;
  mMeatPercent=10;
  mCaloriesPerPersonDaily=2500;
}
LaModel::~LaModel()
{

}

  //copy constructor
LaModel::LaModel(const LaModel& theModel)
{
  mName=theModel.name();
  mPopulation=theModel.population();
  setGuid(theModel.guid());
  mPeriod=theModel.period();
  mProjection=theModel.projection();
  mEasting=theModel.easting();
  mNorthing=theModel.northing();
  mEuclideanDistance=theModel.euclideanDistance();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietPercent=theModel.dietPercent();
  mPercentOfDietThatIsFromCrops=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
  mDairyUtilisation=theModel.dairyUtilisation();
  mBaseOnPlants=theModel.baseOnPlants();
  mIncludeDairy=theModel.includeDairy();
  mLimitDairy=theModel.limitDairy();
  mLimitDairyPercentage=theModel.limitDairyPercent();
  mFallowStatus=theModel.fallowStatus();
  mFallowRatio=theModel.fallowRatio();
}

LaModel& LaModel::operator=(const LaModel& theModel)
{
  if (this == &theModel) return *this; // Gracefully handle self assignment

  mName=theModel.name();
  mPopulation=theModel.population();
  setGuid(theModel.guid());
  mPeriod=theModel.period();
  mProjection=theModel.projection();
  mEasting=theModel.easting();
  mNorthing=theModel.northing();
  mEuclideanDistance=theModel.euclideanDistance();
  mWalkingTime=theModel.walkingTime();
  mPathDistance=theModel.pathDistance();
  mPrecision=theModel.precision();
  mDietPercent=theModel.dietPercent();
  mPercentOfDietThatIsFromCrops=theModel.plantPercent();
  mMeatPercent=theModel.meatPercent();
  mCaloriesPerPersonDaily=theModel.caloriesPerPersonDaily();
  mDairyUtilisation=theModel.dairyUtilisation();
  mBaseOnPlants=theModel.baseOnPlants();
  mIncludeDairy=theModel.includeDairy();
  mLimitDairy=theModel.limitDairy();
  mLimitDairyPercentage=theModel.limitDairyPercent();
  mFallowStatus=theModel.fallowStatus();
  mFallowRatio=theModel.fallowRatio();
  return *this;
}

QString LaModel::name() const { return mName;}
QString LaModel::period() const { return mPeriod;}
float   LaModel::population() const { return mPopulation;}
float   LaModel::projection() const { return mProjection;}
float   LaModel::easting() const { return mEasting;}
float   LaModel::northing() const { return mNorthing;}
bool    LaModel::euclideanDistance() const { return mEuclideanDistance;}
bool    LaModel::walkingTime() const { return mWalkingTime;}
bool    LaModel::pathDistance() const { return mPathDistance;}
float   LaModel::precision() const { return mPrecision;}
float   LaModel::dietPercent() const { return mDietPercent;}
float   LaModel::plantPercent() const
        {
          if (mPercentOfDietThatIsFromCrops < 0) {return 0;}
          else if (mPercentOfDietThatIsFromCrops > 100) {return 100;}
          else {return mPercentOfDietThatIsFromCrops;}
        }
float   LaModel::meatPercent() const { return mMeatPercent; }
float   LaModel::dairyUtilisation() const { return mDairyUtilisation;}
float   LaModel::caloriesPerPersonDaily() const { return mCaloriesPerPersonDaily;}
bool    LaModel::baseOnPlants() const { return mBaseOnPlants;}
bool    LaModel::includeDairy() const { return mIncludeDairy;}
bool    LaModel::limitDairy() const { return mLimitDairy;}
float   LaModel::limitDairyPercent() const { return mLimitDairyPercentage;}
float   LaModel::foodValueCommonLand() const { return mCommonGrazingValue;}
QMap <QString, float> LaModel::animalCalorieTargetsMap() const { return mCaloriesProvidedByMeatMap; }
QMap <QString, float> LaModel::animalFeedRequirementsMap() const { return mValueMap;}
QMap <QString, float> LaModel::animalProductionTargetsMap() const { return mProductionRequiredAnimalsMap;}
QMap <QString, float> LaModel::animalAreaTargetsMap() const
                      { return mAreaTargetsAnimalsMap; }
QMap <QString, float> LaModel::cropCalorieTargetsMap() const
                      { return mCaloriesProvidedByCropsMap;}
QMap <QString, float> LaModel::cropProductionTargetsMap() const
                      { return mProductionRequiredCropsMap;}
QMap <QString, float> LaModel::cropAreaTargetsMap() const
                      { return mAreaTargetsCropsMap; }
QMap <QString, QString> LaModel::calcsAnimalsMap()
                        { return mCalcsAnimalsMap; }
QMap <QString, QString> LaModel::calcsCropsMap()
                        { return mCalcsCropsMap; }
void LaModel::setFallowStatus (Status theStatus) { mFallowStatus=theStatus; }
void LaModel::setFallowRatio (float theRatio) { mFallowRatio=theRatio; }
void LaModel::setName (QString theName) { mName=theName; }
void LaModel::setPopulation (float thePopulation) { mPopulation=thePopulation; }
void LaModel::setPeriod (QString thePeriod) { mPeriod=thePeriod; }
void LaModel::setProjection (float theIndex) { mProjection=theIndex;}
void LaModel::setEasting (float theEasting) { mEasting=theEasting; }
void LaModel::setNorthing (float theNorthing) { mNorthing=theNorthing; }
void LaModel::setEuclideanDistance (bool theBool) { mEuclideanDistance=theBool;}
void LaModel::setWalkingTime (bool theBool) { mWalkingTime=theBool;}
void LaModel::setPathDistance (bool theBool) { mPathDistance=theBool; }
void LaModel::setPrecision (float thePrecision) { mPrecision=thePrecision*.01; }
void LaModel::setDietPercent (float thePercent) { mDietPercent=thePercent*.01; }
void LaModel::setCropPercent (float thePercent)
     { mPercentOfDietThatIsFromCrops = thePercent * .01; }
void LaModel::setMeatPercent (float thePercent) { mMeatPercent=thePercent*.01; }
void LaModel::setCaloriesPerPersonDaily (float theCalories)
     { mCaloriesPerPersonDaily = theCalories; }
void LaModel::setBaseOnPlants (bool theBool) { mBaseOnPlants=theBool; }
void LaModel::setIncludeDairy (bool theBool) { mIncludeDairy=theBool; }
void LaModel::setLimitDairy (bool theBool) { mLimitDairy=theBool; }
void LaModel::setLimitDairyPercent (float thePercent)
     { mLimitDairyPercentage = thePercent * .01; }
void LaModel::setDairyUtilisation (float thePercent)
     { mDairyUtilisation = thePercent * .01; }
void LaModel::setCommonLandAreaUnits(AreaUnits theAreaUnits)
     { mCommonLandAreaUnits = theAreaUnits; }
void LaModel::setCommonLandValue (float theValue, AreaUnits theAreaUnits)
     { mCommonGrazingValue = LaUtils::convertAreaToHectares(theAreaUnits,theValue); }
void LaModel::setAnimals(QMap<QString,QString> theAnimals) { mAnimalsMap = theAnimals; }
void LaModel::setCrops(QMap<QString,QString> theCrops) { mCropsMap = theCrops; }


Status LaModel::fallowStatus() const
{
  return mFallowStatus;
}

float LaModel::fallowRatio() const
{
  return mFallowRatio;
}
float LaModel::requiredValue(QString theAnimalGuid)
{   // this is the generic animal model
  LaAnimal myAnimal = LaUtils::getAnimal(theAnimalGuid);
  float myAnimalProductionTarget = 1;//getProductionTargetsAnimals (theAnimalGuid, static_cast <float> (mCaloriesProvidedByMeatMap.value (theAnimalGuid)));
  float myAnimalsRequired=(myAnimalProductionTarget / myAnimal.killWeight()) / (myAnimal.usableMeat()*.01);
  float myBirthsPerYear = 365.0 / (myAnimal.gestationTime() + myAnimal.estrousCycle() + myAnimal.weaningAge());
  float myOffspringPerMotherYearly = myBirthsPerYear * myAnimal.youngPerBirth() * (1.0-(0.01*myAnimal.deathRate()));
  float myMothersNeededStepOne = myAnimalsRequired/myOffspringPerMotherYearly;
  float myMalesStepOne = (myMothersNeededStepOne * myOffspringPerMotherYearly)/2.;
  float myFemalesStepOne = myMalesStepOne;
  float myMotherReplacementsPerYear = myMothersNeededStepOne/myAnimal.breedingExpectancy();
  float myAdditionalMothers = (myMotherReplacementsPerYear/myOffspringPerMotherYearly)*2.;
  float myMalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2.;
  float myFemalesStepTwo = (myAdditionalMothers*myOffspringPerMotherYearly)/2.;
  float myTotalMothers = myMothersNeededStepOne+myAdditionalMothers;
  float myTotalMales = myMalesStepOne+myMalesStepTwo;
  float myTotalFemales = myFemalesStepOne-myFemalesStepTwo;
  float myTotalJuveniles = myTotalMales+myTotalFemales;
  float myTotalMothersValueRequired = myTotalMothers * myAnimal.gestating();
  float myTotalJuvenilesValueRequired = myTotalJuveniles * myAnimal.juvenile();
  float myValueNeededToFeedAnimals = myTotalMothersValueRequired + myTotalJuvenilesValueRequired;
  float myReturnValue = static_cast<float>(myValueNeededToFeedAnimals);

    // log report
  logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)");
  logMessage("animal prodn target = calorie target of animal / food value");
  logMessage("mCaloriesProvidedByMeatMap.value(theAnimalGuid): " + QString::number(mCaloriesProvidedByMeatMap.value(theAnimalGuid)).toLocal8Bit());
  logMessage("myAnimal.meatFoodValue(): " + QString::number(myAnimal.meatFoodValue()/1000.).toLocal8Bit());
  logMessage("myAnimalProductionTarget = " + QString::number(myAnimalProductionTarget).toLocal8Bit());
  logMessage("slaughter animals reqd: " + QString::number(myAnimalsRequired).toLocal8Bit());
  logMessage("BirthEventsPerYear: " + QString::number(myBirthsPerYear).toLocal8Bit());
  logMessage("OffspringPerMotherYearly = " + QString::number(myOffspringPerMotherYearly).toLocal8Bit());
  logMessage("MothersNeededStepOne = " + QString::number(myMothersNeededStepOne).toLocal8Bit());
  logMessage("MalesStepOne = " + QString::number(myMalesStepOne).toLocal8Bit());
  logMessage("FemalesStepOne = " + QString::number(myFemalesStepOne).toLocal8Bit());
  logMessage("MotherReplacementsPerYear = " + QString::number(myMotherReplacementsPerYear).toLocal8Bit());
  logMessage("AdditionalMothers = " + QString::number(myAdditionalMothers).toLocal8Bit());
  logMessage("MalesStepTwo = " + QString::number(myMalesStepTwo).toLocal8Bit());
  logMessage("FemalesStepTwo = " + QString::number(myFemalesStepTwo).toLocal8Bit());
  logMessage("TotalMothers = " + QString::number(myTotalMothers).toLocal8Bit());
  logMessage("TotalMales = " + QString::number(myTotalMales).toLocal8Bit());
  logMessage("TotalFemales = " + QString::number(myTotalFemales).toLocal8Bit());
  logMessage("TotalJuveniles = " + QString::number(myTotalJuveniles).toLocal8Bit());
  logMessage("Total Adult Females Value(Kg) = " + QString::number (myTotalMothersValueRequired).toLocal8Bit());
  logMessage("Total Juveniles Value(Kg) = " + QString::number (myTotalJuvenilesValueRequired).toLocal8Bit());
  logMessage("Total Value (Kg) Needed To Feed Animals = " + QString::number(myValueNeededToFeedAnimals).toLocal8Bit());
  logMessage("method ==> float LaModel::requiredValue(QString theAnimalGuid)");
  logMessage("Animal: " + myAnimal.name().toLocal8Bit());
  logMessage("Breeding Stock: " + QString::number(myTotalMothers).toLocal8Bit());
  logMessage("Juveniles: " + QString::number(myTotalJuveniles).toLocal8Bit());
  logMessage("Kg Value needed annually to feed the entire herd: " +
      QString::number(myReturnValue).toLocal8Bit());
  logMessage("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
  return myReturnValue;
}








void DoCalculations()
{
  //mCalcsAnimalsMap.clear();
  //mCalcsCropsMap.clear();
  //logMessage("method ==> void LaModel::DoCalculations()");
  // Step 1
  //        Calculate calories needed from crops and tame meat to sustain the settlement
  //        available here -->  caloriesFromCrops();
  //        available here -->  caloriesFromTameMeat();

  // Step 2
  //        Calculate calorie targets for each crop and each animal
  //        (These results will be stored in a QMap)
  //initialiseCaloriesProvidedByMeatMap();
  //initialiseCaloriesProvidedByMilkMap();
  //initialiseCaloriesProvidedByCropsMap();

  // Step 3
  //        Now we need to calculate how many calories the animals
  //          are going to need to stay alive.
  //        (These calculations are going to be stored in a QMap)
  //initialiseValueMap();

  // Step 4
  //        Production targets must now be calculated for each animal and crop
  //        Animals first, because if the animals are fed grain, it will
  //          increase the production targets of the crops
  //initialiseProductionRequiredAnimalsMap();
  //initialiseProductionRequiredCropsMap();

  // Step 5
  //        Area targets for crops are calculated and stored in a QMap
  //        These calculations will produce values for the amount of
  //          fallow land available for grazing, which will in turn
  //          be used to reduce the amount of calories which the animals
  //          who graze the fallow land need from specific grazing land.
  //initialiseAreaTargetsCropsMap();

  // Step 6
  //        If there is available fallow cropland for any animals to
  //          graze, it needs to be allocated to the animals accordingly
  //          to their access priority, and their total calorific
  //          requirements will be reduced to reflect this 'already
  //          counted for' land.
  //allocateFallowGrazingLand();

  // Step 7
  //        If there are additional feed requirements for any animals we
  //          now need to check to see if they receive calories from fodder.
  //        If they do get fed fodder, this is the process that gets followed:
  //          1)  They get fed straw and chaff first, as it is less costly
  //              to the settlement than feeding them the grain.  If there is
  //              enough calories provided by the straw/chaff fodder to satisfy
  //              their remaining calorific needs, there is no need to search
  //              for any additional grazing land, so that animals area target
  //              needs to be set to zero.
  //          2)  If the straw/chaff doesn't satisfy their feeding requirements,
  //              then the same process as above is followed, but considering
  //              of course the grain in this step.  However, at this point, if
  //              grain is being used, the amount of that grain needs to be added
  //              onto the prodction level requirement of the crop. (Step 7)
  //adjustAnimalTargetsForFodder();

  // Step 8
  //        Adjust the production levels of the crops to reflect any increases in
  //          demand resulting from grain being used to feed animals.
  //        adjustCropProductionForFodder();   // implement later
  //
  // Step 8
  //        Calculate area targets for the animals based on their final
  //          calorific requirements after considering fallow grazing
  //          and the use of fodder as feed.
  //initialiseAreaTargetsAnimalsMap();
  //initialiseCalcsAnimalsMap();
  //initialiseCalcsCropsMap();
}
















void LaModel::allocateFallowGrazingLand(float theFallowMCalsAvailable, QMap <QString,float> theAnimalMCalRequirementMap)
{
  logMessage("method ==> void LaModel::allocateFallowGrazingLand()");
    // We need to divide the available fallow land amongst the animals
    // that graze fallow. We split the animal breeds by fallow land
    // access priority (high / medium and low priority).
    // e.g. We have 10 animal breeds, 6 of which graze fallow,
    // caw and horse are high priority, shee and pig medium,
    // chicken and gooxe low.

  float myHighPriorityCount=0, myMediumPriorityCount=0, myLowPriorityCount=0;
  float myHighPriorityValue=0;
  float myMediumPriorityValue=0;
  float myLowPriorityValue=0;
    // put starting caloric requirements of all used animals floato a map
    // for reduction due to grazing of fallow crop land
    // initialiseValueMap();

  float myTotalFallowValue=theFallowMCalsAvailable;

    // Count the Animals in each Priority Level and sum their calorie requirements
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);

    switch (myAnimalParameter.fallowUsage())
    {
      case  High:
            myHighPriorityCount++;
            logMessage("Animal: " + myAnimal.name() );
            logMessage("      : " + QString::number(mValueMap.value(myAnimalGuid)).toLocal8Bit() );
            myHighPriorityValue += mValueMap.value(myAnimalGuid);
            break;
      case  Medium:
            myMediumPriorityCount++;
            myMediumPriorityValue += theAnimalMCalRequirementMap.value(myAnimalGuid);
            break;
      case  Low:
            myLowPriorityCount++;
            myLowPriorityValue += theAnimalMCalRequirementMap.value(myAnimalGuid);
            break;
      case  None:
            break;
      default:
            break;
    }   //switch

  }   //while animal count
  logMessage("High Priority Animals: " + QString::number(myHighPriorityCount).toLocal8Bit() );
  logMessage("Medium Priority Animals: " + QString::number(myMediumPriorityCount).toLocal8Bit() );
  logMessage("Low Priority Animals: " + QString::number(myLowPriorityCount).toLocal8Bit() );

  logMessage("High Priority Animal Calorie requirements: " + QString::number(myHighPriorityValue).toLocal8Bit() );
  logMessage("Medium Priority Animal Calorie requirements: " + QString::number(myMediumPriorityValue).toLocal8Bit() );
  logMessage("Low Priority Animal Calorie requirements: " + QString::number(myLowPriorityValue).toLocal8Bit() );

  logMessage("Total Available Fallow Calories before adjustments: " + QString::number(myTotalFallowValue).toLocal8Bit());

    // The following three if statements process all of the animals which
    // utilize fallow cropland as grazing land.  It first checks that there
    // is fallow land available, and next allocates the the fallow based on
    // the animals fallow access priority

    // HIGH priority animals get allocated fallow cropland
  if (myTotalFallowValue > 0)
  {
    Priority myPriority = High;
    float myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowValue, myHighPriorityValue, myHighPriorityCount);
    logMessage("Remaining Fallow Calories after HIGH adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowValue = myLeftoverCalories;
  }
    // MEDIUM priority animals get allocated fallow cropland
  if (myTotalFallowValue > 0)
  {
    Priority myPriority = Medium;
    float myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowValue, myMediumPriorityValue, myHighPriorityCount);
    logMessage("Remaining Fallow Calories after MED adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowValue = myLeftoverCalories;
  }
    // LOW priority animals get allocated fallow cropland
  if (myTotalFallowValue > 0)
  {
    Priority myPriority = Low;
    float myLeftoverCalories = doTheFallowAllocation(myPriority, myTotalFallowValue, myLowPriorityValue, myHighPriorityCount);
    logMessage("Remaining Fallow Calories after LOW adjustments: " + QString::number(myLeftoverCalories).toLocal8Bit());
    myTotalFallowValue = myLeftoverCalories;
  }
    //float myReturnValue = static_cast<float>(myTotalFallowValue);
    //return myReturnValue;
}


float LaModel::doTheFallowAllocation (Priority thePriority,
                                    float theAvailableFallowValue,
                                    float theValueNeeded, float theNumberOfAnimals)
{
 // qDebug()JASON << "Value Map: " << mValueMap;
    // when the total number of calories needed by the animals
    // is taken away from the total available calories (from crop fallow),
    // there will be one of two results.
    // 1. the result will be <=0, meaning that additional sources of
    //    food is required for the animals.  (fodder or grazing land)
    // 2. the result will be > 0, meaning that there is enough food value
    //    in the crop fallow to completely feed the animals.
  float myTotalFallowValue = theAvailableFallowValue - theValueNeeded;
 // qDebug()JASON << "myTotalFallowValue: "  << myTotalFallowValue;
    // set up the conditions for the fallow allocation...
    // there is either enough fallow to feed the animal completely
    // or not enough to feed them completely.  If there is enough,
    // the animal will not be requiring any additional source of
    // calories.  In other words, we won't be needing to graze them
    // on any other land besides the crop fallow.
  Status myFallowStatus;
  myFallowStatus = (myTotalFallowValue > 0) ? MoreThanEnoughToCompletelySatisfy : NotEnoughToCompletelySatisfy;
  QString myFallowStatusString = (myFallowStatus!=NotEnoughToCompletelySatisfy) ? "More than Enough" : "Not Enough";
  logMessage("Fallow Status: " + myFallowStatusString);
  qDebug () << "FallowStatus: " << myFallowStatus;
  switch (myFallowStatus)
  {
    case  MoreThanEnoughToCompletelySatisfy:
          {
            logMessage("MoreThanEnoughToCompletelySatisfy");
              // because there is leftover calories available to feed more critters, this
              // shows that all of the animals caloric requirements are met with crop fallow
              // and require no more feed so their values in the QMap will be set to 0
            QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
            while (myAnimalIterator.hasNext())
            {
              myAnimalIterator.next();

              QString myAnimalGuid = myAnimalIterator.key();
              QString myAnimalParameterGuid = myAnimalIterator.value();
              LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
              LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);

              if (myAnimalParameter.fallowUsage()==thePriority)
              {
                mValueMap[myAnimalGuid] = 0;
              }   //endif (fallowUsage(myAnimalGuid)

             }   // while animal iterating
               // myTotalFallowValue += theValueNeeded;
             break;
          }

    case  NotEnoughToCompletelySatisfy:
          {
            logMessage("CASE: NotEnoughToCompletelySatisfy");
              // because there ARE NO leftover Value available to feed more critters, this
              // shows that NOT ALL of the animals requirements are met with crop fallow
              // and therefore require more feed so their values in the QMap will be adjusted
            QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
            while (myAnimalIterator.hasNext())
            {
              myAnimalIterator.next();
              logMessage("    Iterating through Animals looking for a match");

              QString myAnimalGuid = myAnimalIterator.key();
              QString myAnimalParameterGuid = myAnimalIterator.value();
              LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
              LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
              float myCurrentAnimalsValue = mValueMap.value( myAnimalGuid );
              logMessage("       Current Animal: " + myAnimal.name());
             // qDebug()JASON << "        theValueNeeded: " << theValueNeeded;
             // qDebug()JASON << "        theAvailableFallowValue: " << theAvailableFallowValue;
             // qDebug()JASON << "        myCurrentAnimalsValue: " << myCurrentAnimalsValue;
              if (myAnimalParameter.fallowUsage()==thePriority)
              {
                double myAllottedValue = (myCurrentAnimalsValue / theValueNeeded) * theAvailableFallowValue;//theNumberOfAnimals;
                logMessage("Adjusting calories required by: " + myAnimal.name());
               // qDebug()JASON << "myAllottedValue: " << myAllottedValue;
                logMessage("Allotted Value from fallow are: " + QString::number(myAllottedValue));
                logMessage("Original Value target was: " + QString::number(mValueMap.value(myAnimalGuid)));
                float myNewValueTarget = mValueMap.value(myAnimalGuid) - myAllottedValue;
                logMessage("New Value target is: " + QString::number(myNewValueTarget));
                mValueMap [myAnimalGuid] = static_cast<float>(myNewValueTarget);
                myTotalFallowValue += static_cast<float>(myAllottedValue);
              }   // endif (fallowUsage(myAnimalGuid)==High)

            }   // while animal iterating
            logMessage("After allocation, total available Value from fallow: " + QString::number(myTotalFallowValue).toLocal8Bit());
            myTotalFallowValue = 0;
            logMessage("WHICH HAS NOW BEEN SET TO 0");
            break;
          }

    default:
          break;
  }   //switch
  return static_cast<float>(myTotalFallowValue);
}






/**
 * Calculates diet portions for setting the diet labels
 * Animals First Includes Diary means that the dairy products
 * from the animal herds will be considered as part of the
 * animals' contribution to the diet, and plant based portion
 * will be derived from these calculations.  This assumes that
 * the model has been 'set'
 * In order to do these calculations, several pieces of informations
 *  are required.  They are:
 *
 *   1. The overall settlement calorie target
 *   2. The Percent of the diet that Animals are responsible forget
 *   3. How many calories the Plants are going to supply
 *   4. The Percent of the Animals that are domestic sources
 *   5. The Percent of the Plants that are domestic sources (crops)
 * @return
 */
LaDietLabels LaModel::doCalcsPlantsFirstIncludeDairy()
{
  LaDietLabels myDietLabels;
  LaAnimal myAnimal;
  float myMCalsIndividualAnnual = mCaloriesPerPersonDaily * 365.0;
  float myMCalsSettlementAnnual = myMCalsIndividualAnnual * mPopulation;
  float myDairyMCalorieCounter = 0.0;
  float myTameMeatMCalorieCounter = 0.0;
  float myWildMeatMCalorieCounter = 0.0;
  QMap <QString,QString> mySelectedAnimalsMap = mAnimalsMap;

  float c1 = 1. - mMeatPercent;
  float c8 = mDairyUtilisation;
  float c10= mPopulation;
  float c11= mCaloriesPerPersonDaily;
  float c14= c10*c11*365.;
  float c15= mDietPercent;
  float c12= mPercentOfDietThatIsFromCrops;
  float e15= c14*c15;

  //float c17=1.-mMeatPercent;
  //float c18=mMeatPercent;

  QMapIterator <QString,QString> myNextAnimalIterator(mySelectedAnimalsMap);
  while (myNextAnimalIterator.hasNext())
  {
    myNextAnimalIterator.next();
    QString myAnimalGuid = myNextAnimalIterator.key();
    QString myAnimalParameterGuid = myNextAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter( myAnimalParameterGuid );

    // adjust the milk calories to correspond to value
    // per kg of each live weight animal
    float c2 = myAnimal.milkGramsPerDay()*.001;
    float c3 = myAnimal.milkFoodValue();
    float c4 = myAnimal.lactationTime();
    float c5 = myAnimal.weaningAge();
    float c6 = myAnimal.killWeight();
    float c7 = myAnimal.usableMeat()*.01;
    float e2 = c2*c3*(c4-c5);
    float e3 = e2*c8;
    float c9 = myAnimal.meatFoodValue();
    float e10= e3+(c9*c7*c6);
    float e7 = (e15*(1.-c1))/e10;
    float c21=e7*e3;
    float c23=e7*c6*c7*c9;
    float c22=e15-c21-c23;

    myDairyMCalorieCounter    += c21;
    myWildMeatMCalorieCounter += c22;
    myTameMeatMCalorieCounter += c23;
     // qDebug()JASON << "c1 = " << c1;
     // qDebug()JASON << "c2 = " << c2;
     // qDebug()JASON << "c3 = " << c3;
     // qDebug()JASON << "c4 = " << c4;
     // qDebug()JASON << "c5 = " << c5;
     // qDebug()JASON << "c6 = " << c6;
     // qDebug()JASON << "c7 = " << c7;

     // qDebug()JASON << "c14 = " << c14;
     // qDebug()JASON << "e2 = " << e2;
     // qDebug()JASON << "e3 = " << e3;
     // qDebug()JASON << "e10 = " << e10;
     // qDebug()JASON << "e15 = " << e15;
     // qDebug()JASON << "e7 = " << e7;
  }

  float c24=(1.-c12)*(c14-e15);
  float c25=(c12)*(c14-e15);
  float c30=c24/c14;
  float c31=c25/c14;

  float c28=(myWildMeatMCalorieCounter)/c14;
  float c29=(myTameMeatMCalorieCounter)/c14;
  float c27=myDairyMCalorieCounter/c14;
   // qDebug()JASON << "c27 = " << c27;
   // qDebug()JASON << "c28 = " << c28;
   // qDebug()JASON << "c29 = " << c29;

  myDietLabels.setDairyMCalories(myDairyMCalorieCounter*.001*.001);
  myDietLabels.setCropMCalories(c25*.001*.001);
  myDietLabels.setWildAnimalMCalories(myWildMeatMCalorieCounter*.001*.001);
  myDietLabels.setWildPlantsMCalories(c24*.001*.001);
  myDietLabels.setDairyPortionPct(c27*100.);
  myDietLabels.setTameMeatPortionPct(c29*100.);
  myDietLabels.setCropsPortionPct(c31*100.);
  myDietLabels.setWildAnimalPortionPct(c28*100.);
  myDietLabels.setWildPlantsPortionPct(c30*100.);
  myDietLabels.setAnimalPortionPct(mDietPercent*100.-c27*100.);
  myDietLabels.setPlantsPortionPct((1.-mDietPercent)*100.);
  myDietLabels.setMCalsIndividualAnnual(myMCalsIndividualAnnual);
  myDietLabels.setMCalsSettlementAnnual(myMCalsSettlementAnnual);
  return myDietLabels;
}

LaDietLabels LaModel::doCalcsPlantsFirstDairySeperate()
{
  LaDietLabels myDietLabels;
  LaAnimal myAnimal;
  QMap <QString,QString> mySelectedAnimalsMap = mAnimalsMap;

  float myDairyCounter=0.;
  float myMeatCounter=0.;

  /** The following loop iterates through the animals and counts the calories
    * provided by the dairy for each as well as the calories each animal
    * contributes via meat.  */
  QMapIterator <QString,QString> myNextAnimalIterator(mySelectedAnimalsMap);
  while (myNextAnimalIterator.hasNext())
  {
    myNextAnimalIterator.next();
    QString myAnimalGuid = myNextAnimalIterator.key();
    QString myAnimalParameterGuid = myNextAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter( myAnimalParameterGuid );
    //
    // Do the dairy and meat calulations for the animals here
    //
    // // // //
    //
    //  VARIABLES REQUIRED
    //


    // Now add the Mcals from the dairy and meat to a counter here
    myDairyCounter ++;
    myMeatCounter ++;
  }




  /*float  myDairyMCalories = myDairyCounter; // sum of all dairy cals from all animals
  float  myCropMCalories; // sum of all crop cals from all crops
  float  myTameMeatMCalories = myMeatCounter;
  float  myWildAnimalMCalories; // calories to come from wild animals
  float  myWildPlantsMCalories; // calories to come from wild plants
  float  myDairyPortionPct; // the portion of the overall diet from dairy
  float  myTameMeatPortionPct; // portion of the diet from tame meat
  float  myCropsPortionPct; // portion of the diet from domestic crops
  float  myWildAnimalPortionPct; // portion of the diet from wild animals
  float  myWildPlantsPortionPct; // portion of the diet from wild plants
  float  myAllMeatPortionPct; // portion of diet from wild and domestic meat
  float  myPlantsPortionPct; // portion of diet from wild plants and domestic crops
  float  myMCalsIndividualAnnual; // how many Mcals an individual requires per annum
  float  myMCalsSettlementAnnual; // how many Mcals the entire settlement requires per annum


  myDietLabels.setDairyMCalories(myDairyMCalories);
  myDietLabels.setCropMCalories(myCropMCalories);
  myDietLabels.setAnimalMCalories(myTameMeatMCalories);
  myDietLabels.setWildAnimalMCalories(myWildAnimalMCalories);
  myDietLabels.setWildPlantsMCalories(myWildPlantsMCalories);
  myDietLabels.setDairyPortionPct(myDairyPortionPct*100.);
  myDietLabels.setTameMeatPortionPct(myTameMeatPortionPct*100.);
  myDietLabels.setCropsPortionPct(myCropsPortionPct*100.);
  myDietLabels.setWildAnimalPortionPct(myWildAnimalPortionPct*100.);
  myDietLabels.setWildPlantsPortionPct(myWildPlantsPortionPct*100.);
  myDietLabels.setAnimalPortionPct(myAllMeatPortionPct*100.);
  myDietLabels.setPlantsPortionPct(myPlantsPortionPct*100.);
  myDietLabels.setMCalsIndividualAnnual(myMCalsIndividualAnnual);
  myDietLabels.setMCalsSettlementAnnual(myMCalsSettlementAnnual);*/
  return myDietLabels;
}

LaDietLabels LaModel::doCalcsAnimalsFirstIncludeDiary() // working :-)
{
  LaDietLabels myDietLabels;
  LaAnimal myAnimal;
  float myMCalsIndividualAnnual = mCaloriesPerPersonDaily * 365.0;
  float myMCalsSettlementAnnual = (myMCalsIndividualAnnual) * mPopulation;
  float myDairyMCalorieCounter = 0.0;
  float myTameMeatMCalorieCounter = 0.0;
  float myWildMeatMCalorieCounter = 0.0;
  QMap <QString,QString> mySelectedAnimalsMap = mAnimalsMap;

  float c1 = 1. - mMeatPercent;
  float c8 = mDairyUtilisation;
  float c10= mPopulation;
  float c11= mCaloriesPerPersonDaily;
  float c14= c10*c11*365.;
  float c15= mDietPercent;
  float c12= mPercentOfDietThatIsFromCrops;
  float e15= c14*c15;

  //float c17=1.-mMeatPercent;
  //float c18=mMeatPercent;

  QMapIterator <QString,QString> myNextAnimalIterator(mySelectedAnimalsMap);
  while (myNextAnimalIterator.hasNext())
  {
    myNextAnimalIterator.next();
    QString myAnimalGuid = myNextAnimalIterator.key();
    QString myAnimalParameterGuid = myNextAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter( myAnimalParameterGuid );

    // adjust the milk calories to correspond to value
    // per kg of each live weight animal
    float c2 = myAnimal.milkGramsPerDay()*.001;
    float c3 = myAnimal.milkFoodValue();
    float c4 = myAnimal.lactationTime();
    float c5 = myAnimal.weaningAge();
    float c6 = myAnimal.killWeight();
    float c7 = myAnimal.usableMeat()*.01;
    float e2 = c2*c3*(c4-c5);
    float e3 = e2*c8;
    float c9 = myAnimal.meatFoodValue();
    float e10= e3+(c9*c7*c6);
    float e7 = (e15*(1.-c1))/e10;
    float c21=e7*e3;
    float c23=e7*c6*c7*c9;
    float c22=e15-c21-c23;

    myDairyMCalorieCounter    += c21;
    myWildMeatMCalorieCounter += c22;
    myTameMeatMCalorieCounter += c23;
     // qDebug()JASON << "c1 = " << c1;
     // qDebug()JASON << "c2 = " << c2;
     // qDebug()JASON << "c3 = " << c3;
     // qDebug()JASON << "c4 = " << c4;
     // qDebug()JASON << "c5 = " << c5;
     // qDebug()JASON << "c6 = " << c6;
     // qDebug()JASON << "c7 = " << c7;

     // qDebug()JASON << "c14 = " << c14;
     // qDebug()JASON << "e2 = " << e2;
     // qDebug()JASON << "e3 = " << e3;
     // qDebug()JASON << "e10 = " << e10;
     // qDebug()JASON << "e15 = " << e15;
     // qDebug()JASON << "e7 = " << e7;
  }

  float c24=(1.-c12)*(c14-e15);
  float c25=(c12)*(c14-e15);
  float c30=c24/c14;
  float c31=c25/c14;

  float c28=(myWildMeatMCalorieCounter)/c14;
  float c29=(myTameMeatMCalorieCounter)/c14;
  float c27=myDairyMCalorieCounter/c14;
   // qDebug()JASON << "c27 = " << c27;
   // qDebug()JASON << "c28 = " << c28;
   // qDebug()JASON << "c29 = " << c29;

  myDietLabels.setDairyMCalories(myDairyMCalorieCounter*.001*.001);
  myDietLabels.setCropMCalories(c25*.001*.001);
  myDietLabels.setAnimalMCalories(myTameMeatMCalorieCounter*.001*.001);
  myDietLabels.setWildAnimalMCalories(myWildMeatMCalorieCounter*.001*.001);
  myDietLabels.setWildPlantsMCalories(c24*.001*.001);
  myDietLabels.setDairyPortionPct(c27*100.);
  myDietLabels.setTameMeatPortionPct(c29*100.);
  myDietLabels.setCropsPortionPct(c31*100.);
  myDietLabels.setWildAnimalPortionPct(c28*100.);
  myDietLabels.setWildPlantsPortionPct(c30*100.);
  myDietLabels.setAnimalPortionPct(mDietPercent*100.-c27*100.);
  myDietLabels.setPlantsPortionPct((1.-mDietPercent)*100.);
  myDietLabels.setMCalsIndividualAnnual(myMCalsIndividualAnnual);
  myDietLabels.setMCalsSettlementAnnual(myMCalsSettlementAnnual*.001);
  return myDietLabels;
}

LaDietLabels LaModel::doCalcsAnimalsFirstDairySeparate()  // working :-)
{
  mCalcsCropsMap.clear();
  mCalcsAnimalsMap.clear();
  mValueMap.clear();
  mAnimalCalcReport.clear();

  LaReportMap myCropCalcsReportMap;
  LaReportMap myAnimalCalcsReportMap;

  QMap <QString, float> myAnimalsMap; // for storing the calculations to send to fallow allocation

  myCropCalcsReportMap.clear();
  myAnimalCalcsReportMap.clear();

  LaDietLabels myDietLabels;
  LaAnimal myAnimal;
  QMap <QString,QString> myCrops = mCropsMap;
  QMap <QString,float> myFoodSourceMapCounter;
  myFoodSourceMapCounter.clear();
  // initialise map to contain all crop varieties and set them to zero
  QMapIterator <QString,QString> myNextCrop(myCrops);
  while (myNextCrop.hasNext())
  {
   // qDebug()JASON << "--------==--------------------------------------------==-------";
   // qDebug()JASON << "--------==        Initializing the fodder Map         ==-------";
   // qDebug()JASON << "--------==--------------------------------------------==-------";

    myNextCrop.next();
    QString myCropGuid = myNextCrop.key();
    myFoodSourceMapCounter.insert(myCropGuid,0);
  }

 // qDebug()JASON << "myFoodSourceMapCounter is:" << myFoodSourceMapCounter;

  float myMCalsIndividualAnnual = mCaloriesPerPersonDaily * 365.0 * .001;
  float myMCalsSettlementAnnual = (myMCalsIndividualAnnual) * mPopulation;
  float myDairyMCalorieCounter = 0.0;
  float myTameMeatMCalorieCounter = 0.0;

  //float myCropMCalorieCounter = 0.0;
  //float myDairySurplusMCalorieCounter = 0.0;
  //float myPercentOfDietFromCrops = mPercentOfDietThatIsFromCrops * .01;
  //float myPercentOfDietFromMeatSources = 1. - myPercentOfDietFromCrops;
  float myWildMeatPortion = (1. - mMeatPercent); // wild meat percent
  //float myDomesticMeatPortion = mMeatPercent; // domestic meat percent
  float myDairyUtilization = mDairyUtilisation;
  float myDairyLimitPercent = mLimitDairyPercentage;
  bool myLimitDairyBool = mLimitDairy;
  //float myPopulation = mPopulation;
  //float myMCaloriesPerPersonDaily = mCaloriesPerPersonDaily * .001;
  float myPlantPercent = 1. - mDietPercent; // @TODO mDietPercent is a bad var name
  float myDomesticCropPortion = mPercentOfDietThatIsFromCrops;

 // qDebug()JASON << "myMCalsIndividualAnnual = " << myMCalsIndividualAnnual;
 // qDebug()JASON << "myMCalsSettlementAnnual = " << myMCalsSettlementAnnual;
 // qDebug()JASON << "myDairyMCalorieCounter = " << myDairyMCalorieCounter;
 // qDebug()JASON << "myTameMeatMCalorieCounter = " << myTameMeatMCalorieCounter;
 // qDebug()JASON << "myWildMeatPortion = " << myWildMeatPortion;
 // qDebug()JASON << "myDomesticMeatPortion = " << myDomesticMeatPortion;
 // qDebug()JASON << "myDairyUtilization = " << myDairyUtilization;
 // qDebug()JASON << "myDairyLimitPercent = " << myDairyLimitPercent;
 // qDebug()JASON << "myLimitDairyBool = " << myLimitDairyBool;
 // qDebug()JASON << "myPlantPercent = " << myPlantPercent;

  QMap <QString,QString> mySelectedAnimalsMap = mAnimalsMap;

  QMapIterator <QString,QString> myNextAnimalIterator(mySelectedAnimalsMap);
  while (myNextAnimalIterator.hasNext())
  {
   // qDebug()JASON << "--------==--------------------------------------------==-------";
   // qDebug()JASON << "--------==        Looping through the animals         ==-------";
   // qDebug()JASON << "--------==--------------------------------------------==-------";

    myNextAnimalIterator.next();
    QString myAnimalGuid = myNextAnimalIterator.key();
    QString myAnimalParameterGuid = myNextAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter( myAnimalParameterGuid );
    float myAdditionalMCalCounter = 0.;
    float myAdditionalMCalCounter1 = 0.;

    float myMilkKgPerDay = myAnimal.milkGramsPerDay() * .001; // entered as Grams so need to convert to kg
    float myMilkFoodValue = myAnimal.milkFoodValue() * .001;
    float myLactationTime = myAnimal.lactationTime();
    float myWeaningAge = myAnimal.weaningAge();
    float myGestatingTime = myAnimal.gestationTime();
    float myEstrousCycle = myAnimal.estrousCycle();
    float myBabiesPerBirth = myAnimal.youngPerBirth();

    float myDeathRate = myAnimal.deathRate() * .01;
    float myBreedingRatio = myAnimal.femalesPerMale();
    float myKillWeight = myAnimal.killWeight();
    float myUsablePortionOfAnimal = myAnimal.usableMeat()*.01;
    float myAdultWeight = myAnimal.adultWeight();
    float myFemalesToMales = myAnimal.femalesPerMale();
    float myConceptionEfficiency = myAnimal.conceptionEfficiency() * .01;
    float myMeatValueMCal = myAnimal.meatFoodValue() * .001;
    float mySexualMaturity = myAnimal.sexualMaturity(); // in months
    float myBreedingYears = myAnimal.breedingExpectancy(); // in years
    float myAnimalContributionToMeatPortion = myAnimalParameter.percentTameMeat() * .01; // B2
    float myAnimalMCalTarget = myAnimalContributionToMeatPortion * myMCalsSettlementAnnual * mDietPercent * mMeatPercent; // B3
    float myPotentialDairyPerOffspring = myMilkKgPerDay * myMilkFoodValue * (myLactationTime - myWeaningAge); // B4
    float myValuePerOffspring = myKillWeight * myUsablePortionOfAnimal * myMeatValueMCal; // B5
    float myActualDairyValueOfOffspring = myPotentialDairyPerOffspring * myDairyUtilization; // B6

    float myBirthingEventsPerYear1 = 365. / (myWeaningAge + myGestatingTime + myEstrousCycle + myLactationTime); // B21
    float myBirthingEventsPerYear = myBirthingEventsPerYear1 < 1. ? 1.:myBirthingEventsPerYear1;
    float myCulledMothersValue1 = (myAdultWeight * myMeatValueMCal * myUsablePortionOfAnimal * (1. / ((mySexualMaturity / 12.) + myBreedingYears)));
    float myCulledMothersValue = myCulledMothersValue1 / (myBabiesPerBirth * myBirthingEventsPerYear); // B7
    float myCulledAdultMalesValue = myCulledMothersValue / myFemalesToMales; // B8
    float myFinalOffspringValue = myValuePerOffspring + myCulledMothersValue + myCulledAdultMalesValue; // B9  + myActualDairyValueOfOffspring  add this to include dairy with meat
    float myOffspringNeededPerYear = myAnimalMCalTarget / myFinalOffspringValue; // B11
    float myMCalsFromTheMeat = myOffspringNeededPerYear * myFinalOffspringValue; // B12
    float myMCalsUtilizedFromDairy = myActualDairyValueOfOffspring * myOffspringNeededPerYear;  // B14

    myTameMeatMCalorieCounter += myMCalsFromTheMeat;
    myDairyMCalorieCounter += myMCalsUtilizedFromDairy;

    LaFoodSourceMap myFoodSourceMap = myAnimalParameter.fodderSourceMap();

    float myMeatPercent = (myMCalsFromTheMeat/myMCalsSettlementAnnual);  // B15
    float myDairyPercent = (myMCalsUtilizedFromDairy/myMCalsSettlementAnnual);  // B16

    //
    // Now to get the herd size so we can calculate MCal requirements
    //
    //   !!! remember that this needs adjustment later for fodder fallow and grain
    //

    float myOffspringPerMotherPerYear = myBirthingEventsPerYear * myBabiesPerBirth * (1. - myDeathRate) * myConceptionEfficiency; // B22
    float myMothersNeededStepOne = myOffspringNeededPerYear / myOffspringPerMotherPerYear; // B23
    float myMalesStepOne = myMothersNeededStepOne * myOffspringPerMotherPerYear * 0.5; // B24
    float myFemalesStepOne = myMalesStepOne; // B25
    float myReplacementMothersPerYear = (myMothersNeededStepOne + (mySexualMaturity/12.)) / myBreedingYears; // B26
    float myBreedingMalesRequired = ((myMothersNeededStepOne / myBreedingRatio) + myMothersNeededStepOne) / myBreedingRatio; // B27
    float myAdditionalMothers = ((myReplacementMothersPerYear/myOffspringPerMotherPerYear)*2.)+(myBreedingMalesRequired * 2.); // B28
    float myMalesStepTwo = myAdditionalMothers * myOffspringPerMotherPerYear * 0.5; // B29
    float myFemalesStepTwo = myMalesStepTwo; // B30
    float myTotalMothers = myMothersNeededStepOne + myReplacementMothersPerYear; // B32
    float myTotalMaleOffspring = myMalesStepOne + myMalesStepTwo; // B33
    float myTotalFemaleOffspring = myFemalesStepOne - myFemalesStepTwo; // B34
    float myTotalOffspring = myTotalMaleOffspring * 2.;//+ myTotalFemaleOffspring; // B35

    float myFeedForGestating = myAnimal.gestating() * .001;
    float myFeedForLactating = myAnimal.lactating() * .001;
    float myFeedForMaintenance = myAnimal.maintenance() * .001;
    float myFeedForOffspringPerKg = myAnimal.juvenile() * .001;

    float myGestatingMCals = myTotalOffspring * myGestatingTime * myFeedForGestating;

    float myLactatingMCals = myTotalOffspring * myLactationTime * myFeedForLactating;
    float myDaysForMaintenance = (365 - (myGestatingTime + myLactationTime) < 0) ? 0 : (365 - (myGestatingTime + myLactationTime));


    float myDryMothers = myTotalMothers - myTotalOffspring < 0 ? 0 : myTotalMothers - myTotalOffspring;
    float myDryMothersMCals = (myDryMothers * 365. * myFeedForMaintenance);
    float myOtherMaintenanceMCals = myDaysForMaintenance * myTotalOffspring * myFeedForMaintenance;
    float myMaintenanceMCals = myDryMothersMCals + myOtherMaintenanceMCals;

    float myAdultMalesMCals = myBreedingMalesRequired * myFeedForMaintenance * 365.;
    float myOffspringMCals = myTotalOffspring * myKillWeight * myFeedForOffspringPerKg * (365. - myWeaningAge);

    QString myAnimalReport = QString("myMilkKgPerDay = " + QString::number(myMilkKgPerDay) + "\n");
    myAnimalReport += QString("myMilkFoodValue = " + QString::number(myMilkFoodValue) + "\n");
    myAnimalReport += QString("myLactationTime = " + QString::number(myLactationTime) + "\n");
    myAnimalReport += QString("myWeaningAge = " + QString::number(myWeaningAge) + "\n");
    myAnimalReport += QString("myKillWeight = " + QString::number(myKillWeight) + "\n");
    myAnimalReport += QString("myUsablePortionOfAnimal = " + QString::number(myUsablePortionOfAnimal) + "\n");
    myAnimalReport += QString("myAdultWeight = " + QString::number(myAdultWeight) + "\n");
    myAnimalReport += QString("myFemalesToMales = " + QString::number(myFemalesToMales) + "\n");
    myAnimalReport += QString("myMeatValueMCal = " + QString::number(myMeatValueMCal) + "\n");
    myAnimalReport += QString("mySexualMaturity = " + QString::number(mySexualMaturity) + "\n");
    myAnimalReport += QString("myBreedingYears = " + QString::number(myBreedingYears) + "\n");
    myAnimalReport += QString("myAnimalContributionToMeatPortion = " + QString::number(myAnimalContributionToMeatPortion) + "\n");
    myAnimalReport += QString("myAnimalMCalTarget = " + QString::number(myAnimalMCalTarget) + "\n");
    myAnimalReport += QString("myPotentialDairyPerOffspring = " + QString::number(myPotentialDairyPerOffspring) + "\n");
    myAnimalReport += QString("myValuePerOffspring = " + QString::number(myValuePerOffspring) + "\n");
    myAnimalReport += QString("myActualDairyValueOfOffspring = " + QString::number(myActualDairyValueOfOffspring) + "\n");
    myAnimalReport += QString("myCulledMothersValue = " + QString::number(myCulledMothersValue) + "\n");
    myAnimalReport += QString("myCulledAdultMalesValue = " + QString::number(myCulledAdultMalesValue) + "\n");
    myAnimalReport += QString("myFinalOffspringValue = " + QString::number(myFinalOffspringValue) + "\n");
    myAnimalReport += QString("myOffspringNeededPerYear = " + QString::number(myOffspringNeededPerYear) + "\n");
    myAnimalReport += QString("myMCalsFromTheMeat = " + QString::number(myMCalsFromTheMeat) + "\n");
    myAnimalReport += QString("myMCalsUtilizedFromDairy = " + QString::number(myMCalsUtilizedFromDairy) + "\n");
    myAnimalReport += QString("myTameMeatMCalorieCounter = " + QString::number(myTameMeatMCalorieCounter) + "\n");
    myAnimalReport += QString("myDairyMCalorieCounter = " + QString::number(myDairyMCalorieCounter) + "\n");
    myAnimalReport += QString("\n");
    myAnimalReport += QString("myBirthingEventsPerYear = " + QString::number(myBirthingEventsPerYear) + "\n");
    myAnimalReport += QString("myOffspringPerMotherPerYear = " + QString::number(myOffspringPerMotherPerYear) + "\n");
    myAnimalReport += QString("myMothersNeededStepOne = " + QString::number(myMothersNeededStepOne) + "\n");
    myAnimalReport += QString("myMalesStepOne = " + QString::number(myMalesStepOne) + "\n");
    myAnimalReport += QString("myFemalesStepOne = " + QString::number(myFemalesStepOne) + "\n");
    myAnimalReport += QString("myReplacementMothersPerYear = " + QString::number(myReplacementMothersPerYear) + "\n");
    myAnimalReport += QString("myBreedingMalesRequired = " + QString::number(myBreedingMalesRequired) + "\n");
    myAnimalReport += QString("myAdditionalMothers = " + QString::number(myAdditionalMothers) + "\n");
    myAnimalReport += QString("myMalesStepTwo = " + QString::number(myMalesStepTwo) + "\n");
    myAnimalReport += QString("myFemalesStepTwo = " + QString::number(myFemalesStepTwo) + "\n");
    myAnimalReport += QString("\n");
    myAnimalReport += QString("myTotalMothers = " + QString::number(myTotalMothers) + "\n");
    myAnimalReport += QString("myTotalMaleOffspring = " + QString::number(myTotalMaleOffspring) + "\n");
    myAnimalReport += QString("myTotalFemaleOffspring = " + QString::number(myTotalFemaleOffspring) + "\n");
    myAnimalReport += QString("myTotalOffspring = " + QString::number(myTotalOffspring) + "\n");
    myAnimalReport += QString("myFeedForGestating = " + QString::number(myFeedForGestating) + "\n");
    myAnimalReport += QString("myFeedForLactating = " + QString::number(myFeedForLactating) + "\n");
    myAnimalReport += QString("myFeedForMaintenance = " + QString::number(myFeedForMaintenance) + "\n");
    myAnimalReport += QString("myFeedForOffspringPerKg = " + QString::number(myFeedForOffspringPerKg) + "\n");
    myAnimalReport += QString("myGestatingMCals = " + QString::number(myGestatingMCals) + "\n");
    myAnimalReport += QString("myLactatingMCals = " + QString::number(myLactatingMCals) + "\n");
    myAnimalReport += QString("myDaysForMaintenance = " + QString::number(myDaysForMaintenance) + "\n");
    myAnimalReport += QString("myGestatingTime = " + QString::number(myGestatingTime) + "\n");
    myAnimalReport += QString("myLactationTime = " + QString::number(myLactationTime) + "\n");
    myAnimalReport += QString("myDryMothers = " + QString::number(myDryMothers) + "\n");
    myAnimalReport += QString("myDryMothersMCals = " + QString::number(myDryMothersMCals) + "\n");
    myAnimalReport += QString("myOtherMaintenanceMCals = " + QString::number(myOtherMaintenanceMCals) + "\n");
    myAnimalReport += QString("myMaintenanceMCals = " + QString::number(myMaintenanceMCals) + "\n");
    myAnimalReport += QString("myAdultMalesMCals = " + QString::number(myAdultMalesMCals) + "\n");
    myAnimalReport += QString("myOffspringMCals = " + QString::number(myOffspringMCals) + "\n");






   // qDebug()JASON << myAnimal.name();
   // qDebug()JASON << "myMilkKgPerDay = " << myMilkKgPerDay;
   // qDebug()JASON << "myMilkFoodValue = " << myMilkFoodValue;
   // qDebug()JASON << "myLactationTime = " << myLactationTime;
   // qDebug()JASON << "myWeaningAge = " << myWeaningAge;
   // qDebug()JASON << "myKillWeight = " << myKillWeight;
   // qDebug()JASON << "myUsablePortionOfAnimal = " << myUsablePortionOfAnimal;
   // qDebug()JASON << "myAdultWeight = " << myAdultWeight;
   // qDebug()JASON << "myFemalesToMales = " << myFemalesToMales;
   // qDebug()JASON << "myMeatValueMCal = " << myMeatValueMCal;
   // qDebug()JASON << "mySexualMaturity = " << mySexualMaturity;
   // qDebug()JASON << "myBreedingYears = " << myBreedingYears;
   // qDebug()JASON << "myAnimalContributionToMeatPortion = " << myAnimalContributionToMeatPortion;
   // qDebug()JASON << "myAnimalMCalTarget = " << myAnimalMCalTarget;
   // qDebug()JASON << "myPotentialDairyPerOffspring = " << myPotentialDairyPerOffspring;
   // qDebug()JASON << "myValuePerOffspring = " << myValuePerOffspring;
   // qDebug()JASON << "myActualDairyValueOfOffspring = " << myActualDairyValueOfOffspring;
   // qDebug()JASON << "myCulledMothersValue = " << myCulledMothersValue;
   // qDebug()JASON << "myCulledAdultMalesValue = " << myCulledAdultMalesValue;
   // qDebug()JASON << "myFinalOffspringValue = " << myFinalOffspringValue;
   // qDebug()JASON << "myOffspringNeededPerYear = " << myOffspringNeededPerYear;
   // qDebug()JASON << "myMCalsFromTheMeat = " << myMCalsFromTheMeat;
   // qDebug()JASON << "myMCalsUtilizedFromDairy = " << myMCalsUtilizedFromDairy;
   // qDebug()JASON << "myTameMeatMCalorieCounter = " << myTameMeatMCalorieCounter;
   // qDebug()JASON << "myDairyMCalorieCounter = " << myDairyMCalorieCounter;


   // qDebug()JASON << "myBirthingEventsPerYear = " << myBirthingEventsPerYear;
   // qDebug()JASON << "myOffspringPerMotherPerYear = " << myOffspringPerMotherPerYear;
   // qDebug()JASON << "myMothersNeededStepOne = " << myMothersNeededStepOne;
   // qDebug()JASON << "myMalesStepOne = " << myMalesStepOne;
   // qDebug()JASON << "myFemalesStepOne = " << myFemalesStepOne;
   // qDebug()JASON << "myReplacementMothersPerYear = " << myReplacementMothersPerYear;
   // qDebug()JASON << "myBreedingMalesRequired = " << myBreedingMalesRequired;
   // qDebug()JASON << "myAdditionalMothers = " << myAdditionalMothers;
   // qDebug()JASON << "myMalesStepTwo = " << myMalesStepTwo;
   // qDebug()JASON << "myFemalesStepTwo = " << myFemalesStepTwo;
   // qDebug()JASON << "         ++         ++         ";
   // qDebug()JASON << "+++++++++++++++++++++++++++++++";
   // qDebug()JASON << "           ++  +  ++           ";
   // qDebug()JASON << "+++++++++++++++++++++++++++++++";
   // qDebug()JASON << "         ++         ++         ";

   // qDebug()JASON << "myTotalMothers = " << myTotalMothers;
   // qDebug()JASON << "myTotalMaleOffspring = " << myTotalMaleOffspring;
   // qDebug()JASON << "myTotalFemaleOffspring = " << myTotalFemaleOffspring;
   // qDebug()JASON << "myTotalOffspring = " << myTotalOffspring;

   // qDebug()JASON << "myFeedForGestating = " << myFeedForGestating;
   // qDebug()JASON << "myFeedForLactating = " << myFeedForLactating;
   // qDebug()JASON << "myFeedForMaintenance = " << myFeedForMaintenance;
   // qDebug()JASON << "myFeedForOffspringPerKg = " << myFeedForOffspringPerKg;

   // qDebug()JASON << "myGestatingMCals = " << myGestatingMCals;
   // qDebug()JASON << "myLactatingMCals = " << myLactatingMCals;
   // qDebug()JASON << "myDaysForMaintenance = " << myDaysForMaintenance;
   // qDebug()JASON << "________------~~~~ Number of days gestating: " << myGestatingTime;
   // qDebug()JASON << "________------~~~~ Number of days lactating: " << myLactationTime;
   // qDebug()JASON << "myDryMothers = " << myDryMothers;
   // qDebug()JASON << "myDryMothersMCals = " << myDryMothersMCals;
   // qDebug()JASON << "myOtherMaintenanceMCals = " << myOtherMaintenanceMCals;
   // qDebug()JASON << "myMaintenanceMCals = " << myMaintenanceMCals;
   // qDebug()JASON << "myAdultMalesMCals = " << myAdultMalesMCals;
   // qDebug()JASON << "myOffspringMCals = "   << myOffspringMCals;

    // still looping through the animals here....

    QMapIterator <QString,LaFoodSource> myNextCrop(myFoodSourceMap);
    while (myNextCrop.hasNext())
    {
     // qDebug()JASON << "    ----==--------------------------------------------==----";
     // qDebug()JASON << "    ----==          Adding to the fodder Map          ==----";
     // qDebug()JASON << "    ----==--------------------------------------------==----";
      myNextCrop.next();
      QString myCropGuid = myNextCrop.key();

      LaFoodSource myFoodSource = myFoodSourceMap.value(myCropGuid);
      float myGrain = myFoodSource.grain() * .001;
      float myFodder = myFoodSource.fodder() * .001;
      float myDays = myFoodSource.days();
      float myGrainToAdd = myGrain * myDays * myTotalOffspring;
      float myGrainTotal = myFoodSourceMapCounter.value(myCropGuid) + myGrainToAdd;
     // qDebug()JASON << "        myGrain = " << myGrain;
     // qDebug()JASON << "        myFodder = " << myFodder;
     // qDebug()JASON << "        myDays = " << myDays;

     // qDebug()JASON << "  previous value of the fodder counter: " << myFoodSourceMapCounter.value(myCropGuid);

      myFoodSourceMapCounter.insert(myCropGuid,myGrainTotal);
     // qDebug()JASON << "  -------> next value of the fodder counter: " << myFoodSourceMapCounter.value(myCropGuid);

     // qDebug()JASON << "Additional MCal counter original Value: " << myAdditionalMCalCounter;
      LaCrop myCrop = LaUtils::getCrop(myCropGuid);
      float myFoodValueOfCrop = myCrop.cropCalories() * .001;
      float myFoodValueofFodder = myCrop.fodderValue() * .001;
     // qDebug()JASON << "Food Value of the Crop: " << myFoodValueOfCrop;
     // qDebug()JASON << "Food Value of the Fodder: " << myFoodValueofFodder;

      float myGrainMCal = myGrainToAdd * myFoodValueOfCrop;
      float myFodderMCal = myFodder * myDays * myFoodValueofFodder * myTotalOffspring;
      myAdditionalMCalCounter1 += myFodderMCal;
      myAdditionalMCalCounter += myGrainMCal + myFodderMCal; // ok, I wimped out here...
      // myFodderMCal really should be checked to make sure that there is actually enough
      // straw and chaff produced from the crop to cover the requested amount.
     // qDebug()JASON << " myGrainMCal = " << myGrainMCal;
     // qDebug()JASON << " myFodderMCal = " << myFodderMCal;
     // qDebug()JASON << " Crop Name: " << myCrop.name();
     // qDebug()JASON << " value to add grain: " << myGrainToAdd;
     // qDebug()JASON << " Value now of the fodder counter: " << myFoodSourceMapCounter.value(myCropGuid);
     // qDebug()JASON << " myFoodSourceMapCounter = " << myFoodSourceMapCounter;
     // qDebug()JASON << "Total MCals counted so far for grain feeding this animal: " << myAdditionalMCalCounter;
    }

    // .^.^.^.^.^.^.^.^.^     Insert data into myAnimalCalcsMap    .^.^.^.^.^.^.^.^.^
    // .^.^.^.^.^.^.^.^.^      GUID , (theReportString , Area)     .^.^.^.^.^.^.^.^.^

    float myAnimalHerdMCalsRequired1 = myGestatingMCals + myLactatingMCals + myMaintenanceMCals + myAdultMalesMCals + myOffspringMCals;
   // qDebug()JASON << "  ---- AnimalHerd MCals Required before accounting for grain feeding: " << myAnimalHerdMCalsRequired1;
    // the next line adjusts for the grain contribution
    float myAnimalHerdMCalsRequired = myAnimalHerdMCalsRequired1 - myAdditionalMCalCounter;
   // qDebug()JASON << "  ---- AnimalHerd MCals Required *AFTER* accounting for grain feeding: " << myAnimalHerdMCalsRequired;
    myAnimalReport += QString("myAnimalHerdMCalsRequired1 = " + QString::number(myAnimalHerdMCalsRequired1) + "\n");
    myAnimalReport += QString("myAnimalHerdMCalsRequired = " + QString::number(myAnimalHerdMCalsRequired) + "\n");
    myAnimalReport += QString(".........................\n");
    myAnimalReport += QString(".        Summary        .\n");
    myAnimalReport += QString(".........................\n");

    myAnimalReport += QString("MCal Target = " + QString::number(myMCalsFromTheMeat) + "\n");
    myAnimalReport += QString("Dairy Contribution = " + QString::number(myMCalsUtilizedFromDairy) + "\n");
    myAnimalReport += QString("Meat Percent = " + QString::number(myMeatPercent*100.) + "\% \n");
    myAnimalReport += QString("Dairy Percent = " + QString::number(myDairyPercent*100.) + "\% \n");
    myAnimalReport += QString("Number of Offspring = " + QString::number(myTotalMaleOffspring * 2.) + "\n");
    myAnimalReport += QString("Number of Mothers = " + QString::number(myTotalMothers) + "\n");
    myAnimalReport += QString("Number of Breeding Males = " + QString::number(myBreedingMalesRequired) + "\n");

    //float myLandValue = myAnimalParameter.ValueCommonGrazingLand();
   // qDebug()JASON << "the common land grazing value I have is: " << myLandValue;
   // qDebug()JASON << "the Herd MCals are .originally. :" << myAnimalHerdMCalsRequired;
   // qDebug()JASON << "and they are being temporarily stored in the report map slot for area target for further adjustment";
    //float myAnimalAreaTarget = myAnimalHerdMCalsRequired / myLandValue;
   // qDebug()JASON << "but at this point we would need " << myAnimalAreaTarget << " Ha of Land";

    QPair <QString,float> myReportAndAreaTarget;
    myReportAndAreaTarget.first = myAnimalReport;
    myReportAndAreaTarget.second = myAnimalHerdMCalsRequired;
    myAnimalCalcsReportMap.insert(myAnimalGuid,myReportAndAreaTarget);
    myAnimalsMap.insert(myAnimalGuid,myAnimalHerdMCalsRequired);
    mValueMap.insert(myAnimalGuid,myAnimalHerdMCalsRequired);
  } // done looping through the animals here

  // ----------- Dairy Portion to be calculated ------------
  // ------ the check should be: SUM(B11..B15) == 1.0 ------

  // limit the dairy.  if no limit the limit is 100 percent
  float myDairyLimit = myLimitDairyBool ? myDairyLimitPercent : 1.; // B22
  float myDomesticMeatPercent = myTameMeatMCalorieCounter / myMCalsSettlementAnnual;  // B11
  float myWildMeatPercent = myWildMeatPortion * mDietPercent; // B13
  bool myLimitSatisfies = ( myDomesticMeatPercent + myWildMeatPercent + myDairyLimit) > 1. ? TRUE:FALSE; // B21 -- BOOL --
  float myNewLimit = myLimitSatisfies ? (1. - myDomesticMeatPercent - myWildMeatPercent) : myDairyLimit; // B20
  bool myPotentialDairyLessThanLimitBool = (myDairyMCalorieCounter / myMCalsSettlementAnnual) < myDairyLimit ? TRUE:FALSE; // B19 -- BOOL --
  float myNewDairy = myPotentialDairyLessThanLimitBool ? myDairyMCalorieCounter : myNewLimit * myMCalsSettlementAnnual; // B18
  float myOverallDairyPercent = myNewDairy / myMCalsSettlementAnnual; // B12 and B8

  // --- To get the final Crops and Wild Plants percent, we need to get the overall Meat and Dairy First ---
  float myOverallMeatPercent = myWildMeatPercent + myDomesticMeatPercent; // B7
  float myOverallPlantPercent = 1. - myOverallMeatPercent - myOverallDairyPercent; // B6
  float myOverallCropPercent = myOverallPlantPercent * myDomesticCropPortion; // B14
  float myOverallWildPlantPercent = myOverallPlantPercent * ( 1. - myPlantPercent); // B15
  float myOverallDomesticMeatMCals = myTameMeatMCalorieCounter; // B25
  float myOverallDairyMCals = myOverallDairyPercent * myMCalsSettlementAnnual; // B26
  float myOverallWildMeatMCals = myWildMeatPercent * myMCalsSettlementAnnual; // B27
  float myOverallCropsMCals = myOverallCropPercent * myMCalsSettlementAnnual; // B28
  float myOverallWildPlantsMCals = myOverallWildPlantPercent * myMCalsSettlementAnnual; // B29
  float myOverallMeatMCals = myOverallWildMeatMCals + myOverallDomesticMeatMCals;
  float myFirstDairySurplusBool = myDairyMCalorieCounter - myOverallDairyMCals;
  float myOVerallDairySurplusMCals = myFirstDairySurplusBool > 0 ? myFirstDairySurplusBool : 0;
  float myMCalsFromFallowCounter = 0.;
  //QString myCropReport = QString("myOverallPlantPercent = " + QString::number(myOverallPlantPercent) + "\n");
  //myCropReport += QString("myDomesticCropPortion = " + QString::number(myDomesticCropPortion) + "\n");
  //myCropReport += QString("myOverallCropPercent = " + QString::number(myOverallCropPercent) + "\n");
  //myCropReport += QString("myOverallMeatPercent = " + QString::number(myOverallMeatPercent) + "\n");
  //myCropReport += QString("myOverallDairyPercent = " + QString::number(myOverallDairyPercent) + "\n");
  //myCropReport += QString("----- = " );//+ QString::number(HOLDER) + "\n");

  // now that we have dairy contributions calculated we can calculate targets for crops
  QMap <QString,QString> mySelectedCropsMap = mCropsMap;

  QMapIterator <QString,QString> myNextCropIterator(mySelectedCropsMap);
  while (myNextCropIterator.hasNext())
  {
   // qDebug()JASON << "        **--------------------------------------------**        ";
   // qDebug()JASON << "**********         Looping through the crops          **********";
   // qDebug()JASON << "        **--------------------------------------------**        ";

    myNextCropIterator.next();
    QString myCropGuid = myNextCropIterator.key();
    QString myCropParameterGuid = myNextCropIterator.value();
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter( myCropParameterGuid );

    float myCropPortion = myCropParameter.percentTameCrop() * .01;
   // qDebug()JASON << "          myCropPortion = " << myCropPortion;
    float myCropFoodValue = myCrop.cropCalories() * .001;
   // qDebug()JASON << "          myCropFoodValue = " <<  myCropFoodValue;
    float myCropPercent = myCropPortion /* * myOverallPlantPercent */ * myOverallCropPercent;
   // qDebug()JASON << "          myOverallCropPercent = " << myOverallCropPercent;
   // qDebug()JASON << "          myCropPercent = " << myCropPercent;
    float myMCalsFromTheCrop = myCropPercent * myMCalsSettlementAnnual;

    float myKgForPeople1 = myMCalsFromTheCrop / (myCropFoodValue);
    float myAnimalKgAdd1 = myFoodSourceMapCounter.value(myCropGuid);

    // adjust for spoilage and reseeding here
    float mySpoilagePercent = myCropParameter.spoilage() * .01;
    float myReseedPercent = myCropParameter.reseed() * .01;

    float myKgForPeopleReseed = (myKgForPeople1 * myReseedPercent);
    float myKgForPeopleSpoilage = (myKgForPeople1 * mySpoilagePercent);
    float myKgForPeople = myKgForPeopleReseed + myKgForPeopleSpoilage + myKgForPeople1;

    float myAnimalKgAddReseed = (myAnimalKgAdd1 * myReseedPercent);
    float myAnimalKgAddSpoilage = (myAnimalKgAdd1 * mySpoilagePercent);
    float myAnimalKgAdd = myAnimalKgAddReseed + myAnimalKgAddSpoilage + myAnimalKgAdd1;

    float myAdjustedTarget = myKgForPeople + myAnimalKgAdd;

    float myCropYield = myCrop.areaUnits() == Dunum ? myCrop.cropYield()*10. : myCrop.cropYield();
    float myCropAreaTargetPeople = myKgForPeople / myCropYield;
    float myCropAreaTargetAnimals = myAnimalKgAdd / myCropYield;

    float myRatio = myCropParameter.fallowRatio();
    float myFallowValue = myCropParameter.fallowValue();
    float myCropAreaTarget1 = myAdjustedTarget / myCropYield;
    float myCropAreaTarget = myCropAreaTarget1 * (myRatio + 1.);

    float myFallowArea = myRatio * myCropAreaTarget1;
    float myFallowMCals = myFallowArea * myFallowValue;


    myMCalsFromFallowCounter += myFallowMCals;

    QString myCropReport = QString("MCals People = " + QString::number(myMCalsFromTheCrop) + "\n");
    myCropReport += QString("myCropPortion = " + QString::number(myCropPortion) + "\n");
    myCropReport += QString("myCropFoodValue = " + QString::number(myCropFoodValue) + "\n");
    myCropReport += QString("myOverallCropPercent = " + QString::number(myOverallCropPercent) + "\n");
    myCropReport += QString("myCropPercent = " + QString::number(myCropPercent) + "\n");
    myCropReport += QString("myMCalsFromTheCrop = " + QString::number(myMCalsFromTheCrop) + "\n");

    myCropReport += QString("myAnimalKgAdd = " + QString::number(myAnimalKgAdd) + "\n");
    myCropReport += QString("myAdjustedTarget = " + QString::number(myAdjustedTarget) + "\n");
    myCropReport += QString("myCrop.cropYield() = " + QString::number(myCrop.cropYield()) + "\n");
    myCropReport += QString("myCropYield = " + QString::number(myCropYield) + "\n");

    myCropReport += QString("Crop Production People before adjusting= " + QString::number(myKgForPeople1) + "\n");
    myCropReport += QString("Extra Kg to account for spoilage= " + QString::number(myKgForPeopleSpoilage) + "\n");
    myCropReport += QString("Extra Kg to account for reseeding= " + QString::number(myKgForPeopleReseed) + "\n");
    myCropReport += QString("Crop Production People after adjusting= " + QString::number(myKgForPeople) + "\n");
    myCropReport += QString("Crop Production Animal before adjusting= " + QString::number(myAnimalKgAdd1) + "\n");
    myCropReport += QString("Extra Kg to account for spoilage= " + QString::number(myAnimalKgAddSpoilage) + "\n");
    myCropReport += QString("Extra Kg to account for reseeding= " + QString::number(myAnimalKgAddReseed) + "\n");
    myCropReport += QString("Crop Production Animal after adjusting= " + QString::number(myAnimalKgAdd) + "\n");

    myCropReport += QString("myCropAreaTarget People = " + QString::number(myCropAreaTargetPeople) + "\n");
    myCropReport += QString("myCropAreaTarget Animals= " + QString::number(myCropAreaTargetAnimals) + "\n");

    myCropReport += QString("myCropAreaTarget = " + QString::number(myCropAreaTarget) + "\n");
    myCropReport += QString("\n");




    myCropReport += QString("Kg for People = " + QString::number(myKgForPeople) + "\n");
    myCropReport += QString("KG for Animals = " + QString::number(myAnimalKgAdd) + "\n");
    myCropReport += QString("Percent of Diet = " + QString::number(myCropPercent * 100.) + "\% \n");
    myCropReport += QString("Area Target People: " + QString::number(myCropAreaTargetPeople) + "\n");
    myCropReport += QString("Area Target Animal: " + QString::number(myCropAreaTargetAnimals) + "\n");
    myCropReport += QString("Area Target is " + QString::number(myCropAreaTarget) + "\n");
    myCropReport += QString("myFallowValue =  " + QString::number(myFallowValue) + "\n");

    myCropReport += QString("MCals from Fallow: " + QString::number(myFallowMCals) + "\n");

   // qDebug()JASON << "______ myCropPortion= " << myCropPortion;
   // qDebug()JASON << "______ myCropFoodValue= " << myCropFoodValue;
   // qDebug()JASON << "______ myCropPercent= " << myCropPercent;
   // qDebug()JASON << "______ myMCalsFromTheCrop= " << myMCalsFromTheCrop;
   // qDebug()JASON << "______ myKgForPeople= " << myKgForPeople;
   // qDebug()JASON << "______ myAnimalsKgAdd= " << myAnimalKgAdd;
   // qDebug()JASON << "______ my Area Target: " << myCropAreaTarget;
   // qDebug()JASON << "______ MCals from Fallow = " << myFallowMCals;
   // qDebug()JASON << "______ MCals total from Fallow Counter= " << myMCalsFromFallowCounter;

    QPair <QString,float> myReportAndAreaTarget;

    myReportAndAreaTarget.first = myCropReport;
    myReportAndAreaTarget.second = myCropAreaTarget;
    myCropCalcsReportMap.insert(myCropGuid,myReportAndAreaTarget);

  }

  allocateFallowGrazingLand(myMCalsFromFallowCounter, myAnimalsMap);

  // finally, we have the mcal target for the animal herd, stored in mValueMap !!!!!!!
  // So at this stage all we have to do is polish up the data contained in myAnimalCalcsMap
  //    so that it contains the final area target along with the rest of the calculations to
  //    be sent in the QString portion of the QPair
  // To do this, I will iterate through the report, and transfer the targets from mValueMap
  //    as well as add on to the report

  QMapIterator <QString,QPair<QString,float> > myReportIterator(myAnimalCalcsReportMap);
  while (myReportIterator.hasNext())
  {
   // qDebug()JASON << "--------==---------------------------------------------==-------";
   // qDebug()JASON << "--------==        Looping to Update Animal Map         ==-------";
   // qDebug()JASON << "--------==---------------------------------------------==-------";

    myReportIterator.next();
    QString myAnimalGuid = myReportIterator.key();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);

    // and now we do the magic B-D
    QPair <QString,float> myPair;
    myPair = myReportIterator.value();
   // qDebug()JASON << "     ****** dump of myPair" << myPair;

    QString myReport = myPair.first;
    float myMCalTarget = mValueMap.value(myAnimalGuid);

   // qDebug()JASON << "        *** contents of myMCalTarget: " << myMCalTarget;
    float myLandValue = mCommonGrazingValue;
   // qDebug()JASON << "  mCommonGrazingValue= " << mCommonGrazingValue;
    float myAreaTarget = myMCalTarget / myLandValue;
   // qDebug()JASON << " myAreaTarget = " << myAreaTarget;
    myPair.second = myAreaTarget;

    myReport += QString("Final MCal Target = " + QString::number(static_cast <int>(myMCalTarget)) + "\n");
    myReport += QString("Final Area Target = " + QString::number(static_cast <int>(myAreaTarget)) + "\n");

    myPair.first = myReport;
   // qDebug()JASON << "my Report should look like: " << myReport;
    myAnimalCalcsReportMap[myAnimalGuid] = myPair;
    mAnimalCalcReport.insert(myAnimalGuid,myPair);
  }

 // qDebug()JASON << "myFinal Calculations for animals map: \n" << mAnimalCalcReport;

 // qDebug()JASON << "myDairyLimit = " << myDairyLimit;
 // qDebug()JASON << "myDomesticMeatPercent = " << myDomesticMeatPercent;
 // qDebug()JASON << "myWildMeatPercent = " << myWildMeatPercent;
 // qDebug()JASON << "myLimitSatisfies = " << myLimitSatisfies;
 // qDebug()JASON << "myNewLimit = " << myNewLimit;
 // qDebug()JASON << "myPotentialDairyLessThanLimitBool = " << myPotentialDairyLessThanLimitBool;
 // qDebug()JASON << "myNewDairy = " << myNewDairy;
 // qDebug()JASON << "myOverallDairyPercent = " << myOverallDairyPercent;
 // qDebug()JASON << "myOverallMeatPercent = " << myOverallMeatPercent;
 // qDebug()JASON << "myOverallPlantPercent = " << myOverallPlantPercent;
 // qDebug()JASON << "myOverallCropPercent = " << myOverallCropPercent;
 // qDebug()JASON << "myOverallWildPlantPercent = " << myOverallWildPlantPercent;
 // qDebug()JASON << "myOverallDomesticMeatMCals = " << myOverallDomesticMeatMCals;
 // qDebug()JASON << "myOverallDairyMCals = " << myOverallDairyMCals;
 // qDebug()JASON << "myOverallWildMeatMCals = " << myOverallWildMeatMCals;
 // qDebug()JASON << "myOverallCropsMCals = " << myOverallCropsMCals;
 // qDebug()JASON << "myOverallWildPlantsMCals = " << myOverallWildPlantsMCals;
 // qDebug()JASON << "myOverallMeatMCals = " << myOverallMeatMCals;
 // qDebug()JASON << "myFirstDairySurplusBool = " << myFirstDairySurplusBool;
 // qDebug()JASON << "myOverallDairySurplusMCals = " << myOVerallDairySurplusMCals;
 // qDebug()JASON << "***********************************************************************";
 // qDebug()JASON << "**                                                                   **";
 // qDebug()JASON << "**                        Calculating Again                          **";
 // qDebug()JASON << "**                                                                   **";
 // qDebug()JASON << "***********************************************************************";



  // ----------- Set the Diet Labels in preparation for return -------------
  myDietLabels.setDairyMCalories(myOverallDairyMCals);
  myDietLabels.setCropMCalories(myOverallCropsMCals);
  myDietLabels.setAnimalMCalories(myOverallMeatMCals);
  myDietLabels.setWildAnimalMCalories(myOverallWildMeatMCals);
  myDietLabels.setWildPlantsMCalories(myOverallWildPlantsMCals);
  myDietLabels.setDairyPortionPct(myOverallDairyPercent*100.);
  myDietLabels.setTameMeatPortionPct(myDomesticMeatPercent*100.);
  myDietLabels.setCropsPortionPct(myOverallCropPercent*100.);
  myDietLabels.setWildAnimalPortionPct(myWildMeatPercent*100.);
  myDietLabels.setWildPlantsPortionPct(myOverallWildPlantPercent*100.);
  myDietLabels.setAnimalPortionPct(myOverallMeatPercent*100.);
  myDietLabels.setPlantsPortionPct(myOverallPlantPercent*100.);
  myDietLabels.setMCalsIndividualAnnual(myMCalsIndividualAnnual);
  myDietLabels.setMCalsSettlementAnnual(myMCalsSettlementAnnual);
  myDietLabels.setDairySurplusMCalories(myOVerallDairySurplusMCals);

  // -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  // -=-=-=-=-=- Setting the report info with area targets -=-=-=-=-=-
  // -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 // qDebug()JASON << "££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "   ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "      ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "   ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "£££";
 // qDebug()JASON << " £££    mValueMap = " << mValueMap;;
 // qDebug()JASON << "£££";
 // qDebug()JASON << "££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "   ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "      ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "   ££££££££££££££££££££££££££££££££££££";
 // qDebug()JASON << "££££££££££££££££££££££££££££££££££££";
  myDietLabels.setCropCalcsReportMap(myCropCalcsReportMap);
  myDietLabels.setAnimalCalcsReportMap(mAnimalCalcReport);




  return myDietLabels;

}

QMap<QString, float> LaModel::getAreaTargetsAnimalsMapPFID ()
{
  QMap<QString, float> myAreaTargetsAnimalsMap;
  return myAreaTargetsAnimalsMap;
}

QMap<QString, float> LaModel::getAreaTargetsAnimalsMapPFDS ()
{
  QMap<QString, float> myAreaTargetsAnimalsMap;
  return myAreaTargetsAnimalsMap;
}

QMap<QString, float> LaModel::getAreaTargetsAnimalsMapAFID ()
{
  LaDietLabels myDietLabels;
  float myMCalsIndividualAnnual = mCaloriesPerPersonDaily * 365.0;
  float myMCalsSettlementAnnual =  (myMCalsIndividualAnnual) * mPopulation;
  float myDairyUtilisation = mDairyUtilisation;

  float myDairyMCalorieCounter = 0.0;
  QMap <QString,QString> mySelectedAnimalsMap = mAnimalsMap;
  QMapIterator <QString,QString> myNextAnimalIterator(mySelectedAnimalsMap);
  while (myNextAnimalIterator.hasNext())
  {
    myNextAnimalIterator.next();
    QString myAnimalGuid = myNextAnimalIterator.key();
    QString myAnimalParameterGuid = myNextAnimalIterator.value();
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    float c2 = myAnimal.milkGramsPerDay() * 1000.;
    float c3 = myAnimal.milkFoodValue();
    float myDaysOfMilking = myAnimal.lactationTime() - myAnimal.weaningAge();
    float myKCaloriesFromMilk = ( myDaysOfMilking
                              * c3
                              * c2 ) / 1000.;
    float myMCaloriesFromMilk = myKCaloriesFromMilk / 1000.;
    myDairyMCalorieCounter += myMCaloriesFromMilk;

   // qDebug()JASON << "Adding " << myKCaloriesFromMilk << " KCalories to total KCalories from milk which is now at: "        << myDairyMCalorieCounter << "MCalories";
  }



  float myDairyMCalories = myDairyUtilisation * myDairyMCalorieCounter;
  float myDairyPortionPct = (myDairyMCalories) / myMCalsSettlementAnnual;
  float myAnimalsCalorieTarget = myMCalsSettlementAnnual * mDietPercent;
  float myAnimalCalsMinusDairyBit = myAnimalsCalorieTarget - myDairyMCalories;

  float myWildAnimalMCalories = myAnimalCalsMinusDairyBit * (1. - mMeatPercent);
  float myTameAnimalMCalories = myAnimalCalsMinusDairyBit * (mMeatPercent);

  float myWildAnimalPortionPct = myWildAnimalMCalories / myMCalsSettlementAnnual;
  float myTameMeatPortionPct = myTameAnimalMCalories / (myMCalsSettlementAnnual - myDairyMCalories);
  float myPlantsPortionPct = 1. - myWildAnimalPortionPct - myTameMeatPortionPct - myDairyPortionPct;
  float myCropsPortionPct = myPlantsPortionPct * (mPercentOfDietThatIsFromCrops);
  float myWildPlantsPortionPct = myPlantsPortionPct * (1. - mPercentOfDietThatIsFromCrops);

  float myCropMCalories = myMCalsSettlementAnnual * myCropsPortionPct;
  float myWildPlantsMCalories = myMCalsSettlementAnnual * myWildPlantsPortionPct;


  float myAnimalPortionPct = mDietPercent;

  myDietLabels.setDairyMCalories(myDairyMCalories);
  myDietLabels.setCropMCalories(myCropMCalories);
  myDietLabels.setAnimalMCalories(myTameAnimalMCalories);
  myDietLabels.setWildAnimalMCalories(myWildAnimalMCalories);
  myDietLabels.setWildPlantsMCalories(myWildPlantsMCalories);
  myDietLabels.setDairyPortionPct(myDairyPortionPct*100.);
  myDietLabels.setTameMeatPortionPct(myTameMeatPortionPct*100.);
  myDietLabels.setCropsPortionPct(myCropsPortionPct*100.);
  myDietLabels.setWildAnimalPortionPct(myWildAnimalPortionPct*100.);
  myDietLabels.setWildPlantsPortionPct(myWildPlantsPortionPct*100.);
  myDietLabels.setPlantsPortionPct(myPlantsPortionPct*100.);
  myDietLabels.setAnimalPortionPct(myAnimalPortionPct*100.);
  myDietLabels.setMCalsIndividualAnnual(myMCalsIndividualAnnual);
  myDietLabels.setMCalsSettlementAnnual(myMCalsSettlementAnnual);
{
  QMap<QString, float> myAreaTargetsAnimalsMap;
  return myAreaTargetsAnimalsMap;
}
}

QMap<QString, float> LaModel::getAreaTargetsAnimalsMapAFDS ()
{
  QMap<QString, float> myAreaTargetsAnimalsMap;
  return myAreaTargetsAnimalsMap;
}


QMap<QString, float> LaModel::getAreaTargetsCropsMapPFID ()
{
  QMap<QString, float> myAreaTargetsCropsMap;
  return myAreaTargetsCropsMap;
}

QMap<QString, float> LaModel::getAreaTargetsCropsMapPFDS ()
{
  QMap<QString, float> myAreaTargetsCropsMap;
  return myAreaTargetsCropsMap;
}

QMap<QString, float> LaModel::getAreaTargetsCropsMapAFID ()
{
  QMap<QString, float> myAreaTargetsCropsMap;
  return myAreaTargetsCropsMap;
}

QMap<QString, float> LaModel::getAreaTargetsCropsMapAFDS ()
{
  QMap<QString, float> myAreaTargetsCropsMap;
  return myAreaTargetsCropsMap;
}

// REPORTS

bool LaModel::fromXml(QString theXml)
{
  logMessage("method ==> bool LaModel::fromXml(QString theXml)");
  QString myFlag;
  logMessage("Loading model from xml");
  QDomDocument myDocument("mydocument");
  myDocument.setContent(theXml);
  QDomElement myTopElement = myDocument.firstChildElement("model");
  if (myTopElement.isNull())
  {
      //TODO - just make this a warning
    logMessage("top element could not be found!");
  }
  logMessage("Model::fromXml - guid found : " + myTopElement.attribute("guid").toLocal8Bit());
  setGuid(myTopElement.attribute("guid"));
  logMessage("Model::fromXml - guid set to : " + guid().toLocal8Bit());
  mName=LaUtils::xmlDecode(myTopElement.firstChildElement("name").text());
  mPopulation=QString(myTopElement.firstChildElement("population").text()).toInt();
  mPeriod=LaUtils::xmlDecode(myTopElement.firstChildElement("period").text());
  mProjection=QString(myTopElement.firstChildElement("projection").text()).toInt();
  mEasting=QString(myTopElement.firstChildElement("easting").text()).toInt();
  mNorthing=QString(myTopElement.firstChildElement("northing").text()).toInt();
  myFlag = myTopElement.firstChildElement("euclideanDistance").text();
  if (myFlag=="1")
  {
    mEuclideanDistance=true;
  }
  else
  {
    mEuclideanDistance=false;
  }
  myFlag = myTopElement.firstChildElement("walkingTime").text();
  if (myFlag=="1")
  {
    mWalkingTime=true;
  }
  else
  {
    mWalkingTime=false;
  }
  myFlag = myTopElement.firstChildElement("pathDistance").text();
  if (myFlag=="1")
  {
    mPathDistance=true;
  }
  else
  {
    mPathDistance=false;
  }
  mPrecision=QString(myTopElement.firstChildElement("precision").text()).toInt();
  mDietPercent=QString(myTopElement.firstChildElement("dietPercent").text()).toInt();
  mPercentOfDietThatIsFromCrops=QString(myTopElement.firstChildElement("plantPercent").text()).toInt();
  mMeatPercent=QString(myTopElement.firstChildElement("meatPercent").text()).toInt();
  mCaloriesPerPersonDaily=QString(myTopElement.firstChildElement("caloriesPerPersonDaily").text()).toInt();

  mBaseOnPlants=QString(myTopElement.firstChildElement("baseOnPlants").text()).toInt();
  mIncludeDairy=QString(myTopElement.firstChildElement("includeDairy").text()).toInt();
  mLimitDairy=QString(myTopElement.firstChildElement("limitDairy").text()).toInt();
  mLimitDairyPercentage=QString(myTopElement.firstChildElement("limitDairyPercent").text()).toInt();

  mDairyUtilisation=QString(myTopElement.firstChildElement("dairyUtilisation").text()).toInt();
  return true;
}

QString LaModel::toXml()
{
  logMessage("method ==> QString LaModel::toXml()");
  QString myString;
  myString+=QString("<model guid=\"" + guid() + "\">\n");
  myString+=QString("  <name>" + LaUtils::xmlEncode(mName) + "</name>\n");
  myString+=QString("  <population>" + QString::number(mPopulation) + "</population>\n");
  myString+=QString("  <period>" + LaUtils::xmlEncode(mPeriod) + "</period>\n");
  myString+=QString("  <projection>" + QString::number(mProjection) + "</projection>\n");
  myString+=QString("  <easting>" + QString::number(mEasting) + "</easting>\n");
  myString+=QString("  <northing>" + QString::number(mNorthing) + "</northing>\n");
  myString+=QString("  <euclideanDistance>" + QString::number(mEuclideanDistance) + "</euclideanDistance>\n");
  myString+=QString("  <walkingTime>" + QString::number(mWalkingTime) + "</walkingTime>\n");
  myString+=QString("  <pathDistance>" + QString::number(mPathDistance) + "</pathDistance>\n");
  myString+=QString("  <precision>" + QString::number(mPrecision) + "</precision>\n");
  myString+=QString("  <dietPercent>" + QString::number(mDietPercent) + "</dietPercent>\n");
  myString+=QString("  <plantPercent>" + QString::number(mPercentOfDietThatIsFromCrops) + "</plantPercent>\n");
  myString+=QString("  <meatPercent>" + QString::number(mMeatPercent) + "</meatPercent>\n");
  myString+=QString("  <caloriesPerPersonDaily>" + QString::number(mCaloriesPerPersonDaily) + "</caloriesPerPersonDaily>\n");

  myString+=QString("  <baseOnPlants>" + QString::number(mBaseOnPlants) + "</baseOnPlants>\n");
  myString+=QString("  <includeDairy>" + QString::number(mIncludeDairy) + "</includeDairy>\n");
  myString+=QString("  <limitDairy>" + QString::number(mLimitDairy) + "</limitDairy>\n");
  myString+=QString("  <limitDairyPercent>" + QString::number(mLimitDairyPercentage) + "</limitDairyPercent>\n");

  myString+=QString("  <dairyUtilisation>" + QString::number(mDairyUtilisation) + "</dairyUtilisation>\n");
  myString+=QString("</model>\n");
  return myString;
}

QString LaModel::toText()
{
  logMessage("method ==> QString LaModel::toText()");
  QString myString;
  myString+=QString("guid=>" + guid() + "\n");
  myString+=QString("name=>" + LaUtils::xmlEncode(mName) + "\n");
  myString+=QString("population=>" + QString::number(mPopulation) + "\n");
  myString+=QString("period=>" + LaUtils::xmlEncode(mPeriod) + "\n");
  myString+=QString("projection=>" + QString::number(mProjection) + "\n");
  myString+=QString("easting=>" + QString::number(mEasting) + "\n");
  myString+=QString("northing=>" + QString::number(mNorthing) + "\n");
  myString+=QString("euclideanDistance=>" + QString::number(mEuclideanDistance) + "\n");
  myString+=QString("walkingTime=>" + QString::number(mWalkingTime) + "\n");
  myString+=QString("pathDistance=>" + QString::number(mPathDistance) + "\n");
  myString+=QString("precision=>" + QString::number(mPrecision) + "\n");
  myString+=QString("dietPercent=>" + QString::number(mDietPercent) + "\n");
  myString+=QString("plantPercent=>" + QString::number(mPercentOfDietThatIsFromCrops) + "\n");
  myString+=QString("meatPercent=>" + QString::number(mMeatPercent) + "\n");
  myString+=QString("caloriesPerPersonDaily=>" + QString::number(mCaloriesPerPersonDaily) + "\n");

  myString+=QString("baseOnPlants=>" + QString::number(mBaseOnPlants) + "\n");
  myString+=QString("includeDairy=>" + QString::number(mIncludeDairy) + "\n");
  myString+=QString("limitDairy=>" + QString::number(mLimitDairy) + "\n");
  myString+=QString("limitDairyPercent=>" + QString::number(mLimitDairyPercentage) + "\n");

  myString+=QString("dairyUtilisation=>" + QString::number(mDairyUtilisation) + "\n");
  return myString;
}

QString LaModel::toHtml()
{
  logMessage("method ==> QString LaModel::toHtml()");
  QString myString;
  myString+="<h1>Model Report</h1>";
  myString+="<h3>" + LaUtils::xmlEncode(mName) + "</h3>";
    //myString+="GUID:" + guid() + "<br />";
  myString+="<br>Population:" + QString::number(mPopulation) + "</br>";
  myString+="<br>Period: " + LaUtils::xmlEncode(mPeriod) + "</br>";
  myString+="<br>Projection: " + QString::number(mProjection) + "</br>";
  myString+="<br>Easting: " + QString::number(mEasting) + "</br>";
  myString+="<br>Northing: " + QString::number(mNorthing) + "</br>";
  myString+="<br>Euclidean Distance: " + QString::number(mEuclideanDistance) + "</br>";
  myString+="<br>Walking Time: " + QString::number(mWalkingTime) + "</br>";
  myString+="<br>Path Distance: " + QString::number(mPathDistance) + "</br>";
  myString+="<br>Precision: " + QString::number(mPrecision) + "</br>";
  myString+="<br>Diet Percent" + QString::number(mDietPercent) + "</br>";
  myString+="<br>Plant Percent: " + QString::number(mPercentOfDietThatIsFromCrops) + "</br>";
  myString+="<br>Meat Percent: " + QString::number(mMeatPercent) + "</br>";
  myString+="<br>Calories Per Person Daily: " + QString::number(mCaloriesPerPersonDaily) + "</br>";

  myString+="<br>BaseOnPlants=>" + QString::number(mBaseOnPlants) + "</br>";
  myString+="<br>IncludeDairy=>" + QString::number(mIncludeDairy) + "</br>";
  myString+="<br>LimitDairy=>" + QString::number(mLimitDairy) + "</br>";
  myString+="<br>LimitDairyPercent=>" + QString::number(mLimitDairyPercentage) + "</br>";

  myString+="<br>Dairy Use: " + QString::number(mDairyUtilisation) + "</br>";
    //iterate through animals
  QMapIterator<QString, QString > myAnimalIterator(mAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    QString myAnimalParameterGuid = myAnimalIterator.value();
      //QString myText = "Animal " + myAnimalGuid.toLocal8Bit() +
      //  " , ";
      //myText +=  myAnimalParameterGuid.toLocal8Bit() ;
      //myText += " ";
      //myString += myText + "<br />";
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    myString += "<br>";
    myString += myAnimal.toHtml();
    myString += "</br>";
    LaAnimalParameter myParameter = LaUtils::getAnimalParameter(myAnimalParameterGuid);
    myString += "<br>";
    myString += myParameter.toHtml();
    myString += "</br>";
  }

    //iterate through crops
  QMapIterator<QString, QString > myCropIterator(mCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    QString myCropParameterGuid = myCropIterator.value();
      //QString myText = "Crop " + myCropGuid.toLocal8Bit() +
      //  " , ";
      //myText += myCropParameterGuid.toLocal8Bit() ;
      //myText += " ";
      //myString += myText + "<br />";
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    myString += myCrop.toHtml();
    myString += "<br />";
    LaCropParameter myParameter = LaUtils::getCropParameter(myCropParameterGuid);
    myString += myParameter.toHtml();
    myString += "<br />";
  }
  return myString;
}

void LaModel::logMessage(QString theMessage)
{
  emit message(theMessage);
}

QString LaModel::toHtmlCalorieCropTargets()
{
    // This method returns a QString for an xml file containing the calorie
    // targets for each crop from mCaloriesProvidedByCropsMap

    // Loop through the mCaloriesProvidedByCropsMap
  QString myString;
  myString += QString("<h3> Crop Calorie Targets</h3>\n");
  myString += QString("<table>");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      kCalories\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");

  QMapIterator<QString, float> myCropIterator (mCaloriesProvidedByCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    float myCalorieTarget = static_cast <float>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));

      // add to the QString to create the html file

    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myCalorieTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");


      // add to the QString to create the xml file
      //myString += QString("  <crop>\n");
      //myString += QString("    <guid=\"" + myCropIterator.key() + "\">\n");
      //myString += QString("    <name>" + LaUtils::xmlEncode(myCrop.name()) + "</name>\n");
      //myString += QString("    <description>" + LaUtils::xmlEncode(myCrop.description()) + "</description>\n");
      //myString += QString("    <parameterGuid=\"" + myCropParameter.guid() + "\">\n");
      //myString += QString("    <name>" + LaUtils::xmlEncode(myCropParameter.name()) + "</name>\n");
      //myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
      //myString += QString("  </crop>\n");
  }   // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlCalorieAnimalTargets()
{
    // This method returns a QString for an xml file containing the calorie
    // targets for each animal from mCaloriesProvidedByMeatMap

    // Loop through the mCaloriesProvidedByAniamlsMap
  QString myString;
  myString += QString("<h3> Animal Calorie Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      kCalories\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, float> myAnimalIterator (mCaloriesProvidedByMeatMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    float myCalorieTarget = static_cast <float>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myCalorieTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");

      // add to the QString to create the xml file
      //myString += QString("  <animal>\n");
      //myString += QString("    <guid=\"" + myAnimalIterator.key() + "\">\n");
      //myString += QString("    <name>" + LaUtils::xmlEncode(myAnimal.name()) + "</name>\n");
      //myString += QString("    <description>" + LaUtils::xmlEncode(myAnimal.description()) + "</description>\n");
      //myString += QString("    <parameterGuid=\"" + myAnimalParameter.guid() + "\">\n");
      //myString += QString("    <name>" + LaUtils::xmlEncode(myAnimalParameter.name()) + "</name>\n");
      //myString += QString("    <calorieTarget>" + QString::number(myCalorieTarget) + "</calorieTarget>\n");
      //myString += QString("  </animal>\n");

  }   // while animal iterator
    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlProductionCropTargets()
{
    // This method returns a QString for an xml file containing the production
    // targets for each crop from mProductionRequiredCropsMap

    // Loop through the mProductionRequiredCropsMap
  QString myString;
  myString += QString("<h3> Crop Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Kg\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, float> myCropIterator (mProductionRequiredCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    float myProductionTarget = static_cast <float>(myCropIterator.value());
    LaCrop myCrop = LaUtils::getCrop(myCropGuid);
    LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
      // add to the QString to create the xml file
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myProductionTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");
  }   // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlProductionAnimalTargets()
{

    // Sallah, I said *no* camels. That's *five* camels. Can't you count?

    // This method returns a QString for an xml file containing the production
    // targets for each animal from mProductionRequiredAnimalsMap

    // Loop through the mProductionRequiredAnimalsMap
  QString myString;
  myString += QString("<h3> Animal Production Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Kg\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, float> myAnimalIterator (mProductionRequiredAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    float myProductionTarget = static_cast <float>(myAnimalIterator.value());
    LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
    LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
      // add to the QString to create the xml file
    myString += QString("  <tr>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
    myString += QString("    </td>\n");
    myString += QString("    <td>\n");
    myString += QString("      " + QString::number(myProductionTarget) + "\n");
    myString += QString("    </td>\n");
    myString += QString("  </tr>\n");
  }   // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlAreaCropTargets()
{
    // This method returns a QString for an xml file containing the production
    // targets for each crop from mAreaTargetsCropsMap

    // Loop through the mAreaTargetsCropsMap
  QString myString;
  myString += QString("<h3> Crop Area Targets</h3>\n");
  myString += QString("<P STYLE=\"margin-bottom: 0in\"><BR>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <COL WIDTH=64*>\n");
  myString += QString("  <COL WIDTH=16*>\n");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Crop\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Area\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, float> myCropIterator (mAreaTargetsCropsMap);
  while (myCropIterator.hasNext())
  {
    myCropIterator.next();
    QString myCropGuid = myCropIterator.key();
    if (myCropGuid != "CommonTarget")
    {
      float myAreaTarget = static_cast <float>(myCropIterator.value());
      LaCrop myCrop = LaUtils::getCrop(myCropGuid);
      LaCropParameter myCropParameter = LaUtils::getCropParameter(mCropsMap.value(myCropGuid));
        // add to the QString to create the xml file
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + LaUtils::xmlEncode(myCrop.name()) + "\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + QString::number(myAreaTarget) + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
    else
    {
      QString myAreaTarget = QString::number(mAreaTargetsCropsMap.value("CommonTarget"));
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      CommonTarget\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + myAreaTarget + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
  }   // while crop iterator

    myString += QString("</table>\n");
  return myString;
}

QString LaModel::toHtmlAreaAnimalTargets()
{
    // This method returns a QString for an xml file containing the production
    // targets for each animal from mAreaTargetsAnimalsMap

    // Loop through the mAreaTargetsAnimalsMap
  QString myString;
  myString += QString("<h3> Animal Area Targets</h3>\n");
  myString += QString("\n");
  myString += QString("<table>");
  myString += QString("  <tr>\n");
  myString += QString("    <th>\n");
  myString += QString("      Animal\n");
  myString += QString("    </th>\n");
  myString += QString("    <th>\n");
  myString += QString("      Area\n");
  myString += QString("    </th>\n");
  myString += QString("  </tr>\n");
  QMapIterator<QString, float> myAnimalIterator (mAreaTargetsAnimalsMap);
  while (myAnimalIterator.hasNext())
  {
    myAnimalIterator.next();
    QString myAnimalGuid = myAnimalIterator.key();
    if (myAnimalGuid != "CommonTarget")
    {
      float myAreaTargetUnchanged = static_cast <float>(myAnimalIterator.value());
      LaAnimal myAnimal = LaUtils::getAnimal(myAnimalGuid);
      LaAnimalParameter myAnimalParameter = LaUtils::getAnimalParameter(mAnimalsMap.value(myAnimalGuid));
      float myAreaTarget = LaUtils::convertAreaToHectares(myAnimalParameter.areaUnits(), myAreaTargetUnchanged);
        // add to the QString to create the xml file
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + LaUtils::xmlEncode(myAnimal.name()) + "\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + QString::number(myAreaTarget) + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
    else
    {
      QString myAreaTarget = QString::number(mAreaTargetsAnimalsMap.value("CommonTarget"));
      myString += QString("  <tr>\n");
      myString += QString("    <td>\n");
      myString += QString("      CommonTarget\n");
      myString += QString("    </td>\n");
      myString += QString("    <td>\n");
      myString += QString("      " + myAreaTarget + "\n");
      myString += QString("    </td>\n");
      myString += QString("  </tr>\n");
    }
  }

    myString += QString("</table>\n");
  return myString;
}

QMap<QString, float> LaModel::getAreaTargetsAnimalsMap()
{
  return mAreaTargetsAnimalsMap;
}

QMap<QString, float> LaModel::getAreaTargetsCropsMap()
{
  return mAreaTargetsCropsMap;
}
