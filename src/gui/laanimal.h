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
    int usableMeat() const;
    int killWeight() const;
    int growTime() const;
    int deathRate() const;
    int gestating() const;
    int lactating() const;
    int juvenile() const;
    int lifeExpectancy() const;
    int breedingExpectancy() const;
    int youngPerBirth() const;
    int weaningAge() const;
    int gestationTime() const;
    int estrousCycle() const;

    //
    // Mutators
    //

    /** Set the layerName
     * @see name()
     */
    void setName(QString theName);
    void setUsableMeat(QString theName);
    void setKillWeight(QString theName);
    void setGrowTime(QString theName);
    void setDeathRate(QString theName);
    void setGestating(QString theName);
    void setLactating(QString theName);
    void setJuvenile(QString theName);
    void setLifeExpectancy(QString theName);
    void setBreedingExpectancy(QString theName);
    void setYoungPerBirth(QString theName);
    void setWeaningAge(QString theName);
    void setGestationTime(QString theName);
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
    /** The name for this layer - usually a full path and filename */
    QString mName;
};

#endif //LAANIMAL_H

