/***************************************************************************
                          LaPlantParameters.h  -  An animal class
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

#ifndef LAPLANTPARAMETERS_H
#define LAPLANTPARAMETERS_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/** 
  * A class to represent animal parameters
  * @author Tim Sutton, Jason Jorgenson
  */

class LaPlantParameters : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaPlantParameters();
    /** Desctructor . */
    ~LaPlantParameters();
    /** copy constructor */
    LaPlantParameters(const LaPlantParameters& thePlantParameters);
    /** Assignement operator */
    LaPlantParameters& operator= (const LaPlantParameters& thePlantParameters);
    
    //
    // Accessors
    //
    /** Get the name for this set of animal model parameters */
    QString name() const;
    /** Portion of the Tame Meat Diet (Percentage) */
    int percentTamePlant() const;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    bool cropRotation() const;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    float fallowRatio() const;
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    int fallowCalories() const;
    /** A flag indicating that the animal grazes land shared with other animals */
    int areaUnits() const;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    bool useCommonLand() const;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    bool useSpecificLand() const;

    //
    // Mutators
    //

    /** Set the name for this set of animal model parameters */
    void setName(QString theName);
    /** Portion of the Tame Meat Diet (Percentage) */
    void setPercentTamePlant(int thePercentage);
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    void setCropRotation(bool theFlag);
    /** The crop to fallow ratio */
    void setFallowRatio(float theRatio);
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    void setFallowCalories(int theCalories);
    /** The index Value for selecting working area units (0==Dunum, 1==Hectare
      */
    void setAreaUnits(int theIndexValue);
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    void setUseSpecificLand(bool theBool);
    /** A flag indicating that the animal grazes land shared with other animals */
    void setUseCommonLand(bool theBool);

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
    int mPercentTamePlant;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    bool mCropRotation;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    float mFallowRatio;
    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    int mFallowCalories;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool mUseCommonLand;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool mUseSpecificLand;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    int mAreaUnits;
};

#endif //LaPlantParameters_H

