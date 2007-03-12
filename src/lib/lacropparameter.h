/***************************************************************************
                          lacrop.h  -  A crop class
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton  tim@linfiniti.com
                         :     2007 by Jason Jorgenson  arkygeek@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#ifndef LACROPPARAMETER_H
#define LACROPPARAMETER_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/** 
  * A class to represent a crop
  * @author Tim Sutton, Jason Jorgenson
  */

class LaCropParameter : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaCropParameter();
    /** Desctructor . */
    ~LaCropParameter();
    /** copy constructor */
    LaCropParameter(const LaCropParameter& theCropParameter);
    /** Assignement operator */
    LaCropParameter& operator= (const LaCropParameter& theCropParameter);
    
    //
    // Accessors
    //

    /** Get the name for this set of crop model parameters */
    QString name() const;
    /** Set the description for this set of crop model parameters */
    QString description() const;
    /** Portion of the Tame Crop  Diet (Percentage) */
    int percentTameCrop() const;
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

    /** Set the name for this set of crop model parameters */
    void setName(QString theName);
    /** Set the description for this set of crop model parameters */
    void setDescription(QString theDescription);
    /** Portion of the Tame Crop  Diet (Percentage) */
    void setPercentTameCrop(int thePercentage);
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

    /** Return a plain text representation of this layer
     */
    QString toText();
    /** Return a html text representation of this layer
     */
    QString toHtml();
    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml);
  private:
    /** The name for this crop paremeter */
    QString mName;
    /** The description for this crop parameter */
    QString mDescription;
    /** Portion of the Tame Crop Diet (Percentage) */
    int mPercentTameCrop;
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

#endif //LACROPPARAMETER_H

