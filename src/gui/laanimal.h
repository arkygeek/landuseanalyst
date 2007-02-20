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
/** 
  * An class to represent an animal
  * @author Tim Sutton
  */

class LaAnimal : public LaSerialisable 
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
    /** Percentage of animals live weight that can be utilized for meat */
    int usableMeat() const;
    /** The weight in kg at which the animals are slaughtered */
    int killWeight() const;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int growTime() const;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int deathRate() const;
    /** The number of calories a gestating female requires per day */
    int gestating() const;
    /** The number of calories a lactating female requires per day */
    int lactating() const;
    /** The number of calories a juvenile requires per day */
    int juvenile() const;
    /** The life expectancy in years of the animal */
    int lifeExpectancy() const;
    /** The number of years a female will reliably produce offspring */
    int breedingExpectancy() const;
    /** The average number of young produced per pregnancy */
    int youngPerBirth() const;
    /** The age in weeks at which babies stop suckling */
    int weaningAge() const;
    /** The number of days required for gestation */
    int gestationTime() const;
    /** The number of days in the female estrous cycle */
    int estrousCycle() const;

    //
    // Mutators
    //

    /** Set the animalName
     * @see name()
     */
    void setName(QString theName);

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

    /** Set the deathRate as a percentage
     * @see deathRate()
     */
    void setDeathRate(int thePercentage);

    /** Set the daily calories required for a gestating female
     * @see gestating()
     */
    void setGestating(int theCalories);

    /** Set the daily calories required for a lactating female
     * @see UsableMeat()
     */
    void setLactating(int theCalories);

    /** Set the daily calories required for a juvenile
     * @see UsableMeat()
     */
    void setJuvenile(int theCalories);

    /** Set the average lifeExpectancy in years
     * @see lifeExpectancy()
     */
    void setLifeExpectancy(int theYears);

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
    void setWeaningAge(int theWeeks);

    /** Set the gestationTime in Days
     * @see gestationTime()
     */
    void setGestationTime(int theDays);

    /** Set the estrousCycle in days
     * @see estrousCycle()
     */
    void setEstrousCycle(int theDays);

    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toXml();
    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml){ return false; };
  private:
    /** The name for this animal */
    QString mName;
    /** Percentage of animals live weight that can be utilized for meat */
    int mUsableMeat;
    /** The weight in kg at which the animals are slaughtered */
    int mKillWeight;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int mGrowTime;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int mDeathRate;
    /** The number of calories a gestating female requires per day */
    int mGestating;
    /** The number of calories a lactating female requires per day */
    int mLactating;
    /** The number of calories a juvenile requires per day */
    int mJuvenile;
    /** The life expectancy in years of the animal */
    int mLifeExpectancy;
    /** The number of years a female will reliably produce offspring */
    int mBreedingExpectancy;
    /** The average number of young produced per pregnancy */
    int mYoungPerBirth;
    /** The age in weeks at which babies stop suckling */
    int mWeaningAge;
    /** The number of days required for gestation */
    int mGestationTime;
    /** The number of days in the female estrous cycle */
    int mEstrousCycle;
};

#endif //LAANIMAL_H

