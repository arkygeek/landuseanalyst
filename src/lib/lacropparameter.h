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
#include "la.h"
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
    /** Get the guid of the crop this set of params is associated with */
    QString cropGuid() const;
    /** Portion of the Tame Crop  Diet (Percentage) */
    float percentTameCrop() const;
    /** Flag for determining use of crop rotation */
    bool cropRotation() const;
    /**The ratio of crop to fallow land */
    float fallowRatio() const;
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    int fallowTDN() const;
    /** Selects 0==dunums 1==hectares as units for area */
    AreaUnits areaUnits() const;
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    bool useCommonLand() const;
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    bool useSpecificLand() const;
    QString rasterName() const;

    //
    // Mutators
    //

    /** Set the name for this set of crop model parameters */
    void setName(QString theName);
    /** Set the description for this set of crop model parameters */
    void setDescription(QString theDescription);
    /** Set the guid of the crop this set of params is associated with */
    void setCropGuid(QString theGuid);
    /** Portion of the Tame Crop  Diet (Percentage) */
    void setPercentTameCrop(float thePercentage);
    /** Flag for determining use of crop rotation */
    void setCropRotation(bool theFlag);
    /**The ratio of crop to fallow land */
    void setFallowRatio(float theRatio);
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    void setFallowValue(int theKg);
    /** Selects 0==dunums 1==hectares as units for area */
    void setAreaUnits(AreaUnits theAreaUnit);
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    void setUseCommonLand(bool theBool);
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    void setUseSpecificLand(bool theBool);
    void setRasterName(QString theRasterName);

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
    /** The crop guid these parameters are associated with */
    QString mCropGuid;
    /** Portion of the Tame Crop Diet (Percentage) */
    float mPercentTameCrop;
    /** Food value of specific (or unique) land as calories per dunum/hectare */
    bool mCropRotation;
    /**The ratio of crop to fallow land */
    float mFallowRatio;
    /** The food value, in calories, of a dunum/hectare
      * of fallow land
      */
    int mFallowValue;
    /** Selects 0==dunums 1==hectares as units for area */
    AreaUnits mAreaUnits;
    /** A flag indicating that the crop can be grown on
      * land that is also suitable for other crops
      */
    bool mUseCommonLand;
    /** A flag indicating that the crop requires specific
      * land apart from common agricultural land
      */
    bool mUseSpecificLand;
    QString mRasterName;
};

#endif //LACROPPARAMETER_H

