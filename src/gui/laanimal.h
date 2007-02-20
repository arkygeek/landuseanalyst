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
    int mUsableMeat() const;
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

    /** Set the layerName
     * @see name()
     */
    void setName(QString theName);

    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setUsableMeat(int thePercentage);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setKillWeight(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setGrowTime(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setDeathRate(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setGestating(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setLactating(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setJuvenile(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setLifeExpectancy(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setBreedingExpectancy(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setYoungPerBirth(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setWeaningAge(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setGestationTime(QString theName);
    /** Set the useable meat as a percentage
     * @see UsableMeat()
     */
    void setEstrousCycle(QString theName);

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
    int killWeight;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int growTime;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int deathRate;
    /** The number of calories a gestating female requires per day */
    int gestating;
    /** The number of calories a lactating female requires per day */
    int lactating;
    /** The number of calories a juvenile requires per day */
    int juvenile;
    /** The life expectancy in years of the animal */
    int lifeExpectancy;
    /** The number of years a female will reliably produce offspring */
    int breedingExpectancy;
    /** The average number of young produced per pregnancy */
    int youngPerBirth;
    /** The age in weeks at which babies stop suckling */
    int weaningAge;
    /** The number of days required for gestation */
    int gestationTime;
    /** The number of days in the female estrous cycle */
    int estrousCycle;
};

#endif //LAANIMAL_H

