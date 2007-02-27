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
  * A class to represent plant parameters
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
    /** Assignment operator */
    LaPlantParameters& operator= (const LaPlantParameters& thePlantParameters);

    //
    // Accessors
    //
    /** Get the name for this set of plant model parameters */
    QString name() const;
    /** Portion of the Tame Plant  Diet (Percentage) */
    int percentTamePlant() const;
    /** Flag for determining use of crop rotation */
    bool cropRotation() const;
    /**The ratio of crop to fallow land */
    float fallowRatio() const;
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    int fallowCalories() const;
    /** Selects 0==dunums 1==hectares as units for area */
    int areaUnits() const;
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    bool useCommonLand() const;
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    bool useSpecificLand() const;

    //
    // Mutators
    //

    /** Set the name for this set of animal model parameters */
    void setName(QString theName);
    /** Portion of the Tame Plant  Diet (Percentage) */
    void setPercentTamePlant(int thePercentage);
    /** Flag for determining use of crop rotation */
    void setCropRotation(bool theFlag);
    /**The ratio of crop to fallow land */
    void setFallowRatio(float theRatio);
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    void setFallowCalories(int theCalories);
    /** Selects 0==dunums 1==hectares as units for area */
    void setAreaUnits(int theIndexValue);
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    void setUseCommonLand(bool theBool);
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    void setUseSpecificLand(bool theBool);

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
    /** A name for this set of plant paremeters */
    QString mName;
    /** Portion of the Tame Plant Diet (Percentage) */
    int mPercentTamePlant;
    /** Food value of specific (or unique) land as calories per dunum/hectare */
    bool mCropRotation;
    /**The ratio of crop to fallow land */
    float mFallowRatio;
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    int mFallowCalories;
    /** Selects 0==dunums 1==hectares as units for area */
    int mAreaUnits;
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    bool mUseCommonLand;
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    bool mUseSpecificLand;

};

#endif //LaPlantParameters_H

