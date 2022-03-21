/***************************************************************************
                          laanimal.h  -  An animal class
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

#ifndef LAANIMAL_H
#define LAANIMAL_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include "la.h"
#include <QString>
/**
  * An class to represent an animal
  * @author Tim Sutton
  */

class LaAnimal : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaAnimal();
    /** Desctructor . */
    ~LaAnimal();
    /** copy constructor */
    LaAnimal(const LaAnimal& theAnimal);
    /** Assignement operator */
    LaAnimal& operator= (const LaAnimal& theAnimal);

      //
      // Accessors
      //

    /** The name of this animal */
    QString name() const;
    /** The description of this animal */
    QString description() const;
    /** Food value of meat in calories per kh */
    int meatFoodValue() const;
    /** Percentage of animals live weight that can be utilized for meat */
    int usableMeat() const;
    /** The weight in kg at which the animals are slaughtered */
    int killWeight() const;
    /** The weight of an adult */
    int adultWeight() const;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int growTime() const;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int deathRate() const;
    /** The energy type: KCalories or TDN */
    EnergyType feedEnergyType() const;
    /** The number of calories a gestating female requires per day */
    int gestating() const;
    /** The number of calories a lactating female requires per day */
    int lactating() const;
    /** The number of calories adult maintenance requires per day */
    int maintenance() const;
        /** The number of calories a juvenile requires per day */
    int juvenile() const;
    /** The life expectancy in years of the animal */
    int sexualMaturity() const;
    /** The number of years a female will reliably produce offspring */
    int breedingExpectancy() const;
    /** Conception rate or breeding efficiency */
    int conceptionEfficiency() const;
    /** The number of breeding females per breeding male */
    int femalesPerMale() const;
    /** The average number of young produced per pregnancy */
    int youngPerBirth() const;
    /** The age in weeks at which babies stop suckling */
    int weaningAge() const;
    /** The weight when babies stop suckling */
    int weaningWeight() const;
    /** The number of days required for gestation */
    int gestationTime() const;
    /** The number of days in the female estrous cycle */
    int estrousCycle() const;
    /** The number of days the mothers can produce milk */
    int lactationTime() const;
    /** produces milk bool */
    bool milk() const;
    /** weight of milk in grams provided per day after weaning */
    int milkGramsPerDay() const;
    /** value, in kcalories, of milk per Kg */
    int milkFoodValue() const;
    /** provides a fleece bool */
    bool fleece() const;
    /** weight of fleece (average) per year */
    int fleeceWeightKg() const;
    /** The image file associated with the animal */
    QString imageFile() const;

      //
      // Mutators
      //

    /** Set the animalName
     * @see name()
     */
    void setName(QString theName);

    /** Set the animal description
     * @see description()
     */
    void setDescription(QString theDescription);

    /** Set meatFoodValue as calories per kg
     * @see meatFoodValue()
     */
    void setMeatFoodValue(int theFoodValue);

    /** Set useableMeat as a percentage
     * @see usableMeat()
     */
    void setUsableMeat(int thePercentage);

    /** Set killWeight as kg
     * @see killWeight()
     */
    void setKillWeight(int theKg);

    /** Set the growTime in weeks
     * @see growTime()
     */
    void setGrowTime(int theWeeks);
  
  
    /** Set adultWeight as kg
     * @see adultWeight()
     */
    void setAdultWeight(int theKg);
    
    /** Set conceptionEfficiency as a percentage
     * @see conceptionEfficiency()
     */
    void setConceptionEfficiency(int thePercentage);
    
    /** Set femalesToMales as an integer
     * @see femalesToMales()
     */
    void setFemalesToMales(int theInt);
  
  
    /** Set the deathRate as a percentage
     * @see deathRate()
     */
    void setDeathRate(int thePercentage);
    
    /** Set the daily calories required for a gestating female
     * @see feedEnergyType()
     */
    void setFeedEnergyType(EnergyType theFeedEnergyType);

    /** Set the daily calories required for a gestating female
     * @see gestating()
     */
    void setGestating(int theCalories);

    /** Set the daily calories required for a lactating female
     * @see lactating()
     */
    void setLactating(int theCalories);

    /** Set the daily calories required for adult maintenance
     * @see maintenance()
     */
    void setMaintenance(int theCalories);

    /** Set the daily calories required for a juvenile
     * @see juvenile()
     */
    void setJuvenile(int theCalories);

    /** Set the average lifeExpectancy in years
     * @see lifeExpectancy()
     */
    void setSexualMaturity(int theMonths);

    /** Set the average breedingLifeExpectancy in years
     * @see breedingExpectancy()
     */
    void setBreedingExpectancy(int theYears);

    /** Set the average number of youngPerBirth
     * @see youngPerBirth()
     */
    void setYoungPerBirth(int theInteger);

    /** Set the weaningAge in weeks
     * @see weaningAge()
     */
    void setWeaningWeight(int theWeight);
    /** Set the weaning weight
     * @see weaningWeight()
     */
    void setWeaningAge(int theDays);
    /** Set the gestationTime in Days
     * @see gestationTime()
     */
    void setGestationTime(int theDays);

    /** Set the estrousCycle in days
     * @see estrousCycle()
     */
    void setEstrousCycle(int theDays);
    
     /** Set the LactationTime in days
     * @see lactationTime()
      */
    void setLactationTime (int theTime);
    
     /** Set the milk bool flag
     * @see milk()
      */
    void setMilk (bool theBool);
    
    /** Set the Milk Production Per Day in grams
     * @see milkGramsPerDay()
     */
    void setMilkGramsPerDay(int theMilkGrams);
    
    /** Set the food value of milk in KCals
     * @see milkFoodValue()
     */
    void setMilkFoodValue (int theMilkFoodValue);
    
    /** Set the fleece bool flag
     * @see fleece()
     */
    void setFleece (bool theFleeceBool);
    
    /** Set the fleece weight in Kg
     * @see fleeceWeightKg()
     */
    void setFleeceWeightKg (int theFleeceWeight);

    /** Set the image file
     * @see imageFile()
     */
    void setImageFile(QString theImageFileName);
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toXml();
    /** Return a plain text representation of this layer
     */
    QString toText();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtml();

    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml);
  private:
    /** The name for this animal */
    QString mName;
    /** The description for this animal */
    QString mDescription;
    /** Food value of meat in calories per kg */
    int mMeatFoodValue;
    /** Percentage of animals live weight that can be utilized for meat */
    int mUsableMeat;
    /** The weight in kg at which the animals are slaughtered */
    int mKillWeight;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int mGrowTime;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int mDeathRate;
    /** The feed Energy type: KCalories or TDN */
    EnergyType mFeedEnergyType;
    /** The number of calories a gestating female requires per day */
    int mGestating;
    /** The number of calories a lactating female requires per day */
    int mLactating;
    /** The number of calories adult maintenance requires per day */
    int mMaintenance;
    /** The number of calories a juvenile requires per day */
    int mJuvenile;
    /** The life expectancy in years of the animal */
    int mSexualMaturity;
    /** The number of years a female will reliably produce offspring */
    int mBreedingExpectancy;
    /** The average number of young produced per pregnancy */
    int mYoungPerBirth;
    /** the weight of an adult */
    int mAdultWeight;
    /** the conception efficiency or the percent of breeding females that get pregnant per year */
    int mConceptionEfficiency;
    /** females To Males in the breeding herd */
    int mFemalesToMales;  
    /** The age in weeks at which babies stop suckling */
    int mWeaningAge;
    /** The weight when babies stop suckling */
    int mWeaningWeight;
    /** The number of days required for gestation */
    int mGestationTime;
    /** The number of days in the female estrous cycle */
    int mEstrousCycle;
    /** total length of lactation */
    int mLactationTime;
    /** flag for utilisation of milk */
    bool mMilk;
    /** milk production per mother per day in grams */
    int mMilkGramsPerDay;
    /** food value of milk per kg in KCalories */
    int mMilkFoodValue;
    /** flag for provision of a fleece from the animal */
    bool mFleece;
    /** the weight of the fleece, if available, in kg per annum */
    int mFleeceWeightKg;
    /** name of image file */
    QString mImageFile;

  
  
  
  
  
};

#endif   //LAANIMAL_H

