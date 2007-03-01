/***************************************************************************
                          LaAnimalParameters.h  -  An animal class
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

#ifndef LAANIMALPARAMETERS_H
#define LAANIMALPARAMETERS_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/**
  * A class to represent animal parameters
  * @author Tim Sutton, Jason Jorgenson
  */

class LaAnimalParameters : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaAnimalParameters();
    /** Desctructor . */
    ~LaAnimalParameters();
    /** copy constructor */
    LaAnimalParameters(const LaAnimalParameters& theAnimalParameters);
    /** Assignment operator */
    LaAnimalParameters& operator= (const LaAnimalParameters& theAnimalParameters);

    //
    // Accessors
    //
    /** Get the name for this set of animal model parameters */
    QString name() const;
    /** Portion of the Tame Meat Diet (Percentage) */
    int percentTameMeat() const;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    int foodValueOfSpecificGrazingLand() const;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    int foodValueOfCommonGrazingLand() const;
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    bool useSpecificGrazingLand() const;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool useCommonGrazingLand() const;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    int fallowUsage() const;

    //
    // Mutators
    //

    /** Set the name for this set of animal model parameters */
    void setName(QString theName);
    /** Portion of the Tame Meat Diet (Percentage) */
    void setPercentTameMeat(int thePercentage);
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    void setFoodValueOfSpecificGrazingLand(int theCalories);
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    void setFoodValueOfCommonGrazingLand(int theCalories);
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    void setUseSpecificGrazingLand(bool theBool);
    /** A flag indicating that the animal grazes land shared with other animals */
    void setUseCommonGrazingLand(bool theBool);
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    void setFallowUsage(int theIndex);

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
    bool fromXml(const QString theXml);
  private:
    /** A name for this set of animal paremeters */
    QString mName;
    /** Portion of the Tame Meat Diet (Percentage) */
    int mPercentTameMeat;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    int mFoodValueOfSpecificGrazingLand;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    int mFoodValueOfCommonGrazingLand;
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    bool mUseSpecificGrazingLand;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool mUseCommonGrazingLand;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    int mFallowUsage;
};

#endif //LAANIMALPARAMETERS_H

