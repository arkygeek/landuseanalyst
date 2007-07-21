/***************************************************************************
                          LaAnimalParameter.h  -  An animal class
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

#ifndef LAANIMALPARAMETER_H
#define LAANIMALPARAMETER_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include "la.h"
#include "lafoodsource.h"
#include <QString>
/**
  * A class to represent animal parameters
  * @author Tim Sutton, Jason Jorgenson
  */

class LaAnimalParameter : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaAnimalParameter();
    /** Desctructor . */
    ~LaAnimalParameter();
    /** copy constructor */
    LaAnimalParameter(const LaAnimalParameter& theAnimalParameter);
    /** Assignment operator */
    LaAnimalParameter& operator= (const LaAnimalParameter& theAnimalParameter);

    //
    // Accessors
    //
    /** Get the name for this set of animal model parameters */
    QString name() const;
    /** Get the name for this set of animal model parameters */
    QString description() const;
    /** Get the guid of the animal this set of params is associated with */
    QString animalGuid() const;
    /** Portion of the Tame Meat Diet (Percentage) */
    int percentTameMeat() const;

    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    bool useSpecificGrazingLand() const;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool useCommonGrazingLand() const;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    int foodValueOfSpecificGrazingLand() const;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    int foodValueOfCommonGrazingLand() const;    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    int areaUnits() const;
    bool fodderUse() const;

    QString fodderSource1() const;
    int fodder1() const;
    int fodderGrain1() const;

    QString fodderSource2() const;
    int fodder2() const;
    int fodderGrain2() const;

    QString fodderSource3() const;
    int fodder3() const;
    int fodderGrain3() const;

    Priority fallowUsage() const;
    QString rasterName() const;


    //
    // Mutators
    //

    /** Set the name for this set of animal model parameters */
    void setName(QString theName);
    /** Set the name for this set of animal model parameters */
    void setDescription(QString theDescription);
    /** Set the guid of the animal this set of params is associated with */
    void setAnimalGuid(QString theGuid);
    /** Portion of the Tame Meat Diet (Percentage) */
    void setPercentTameMeat(int thePercentage);

    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    void setUseSpecificGrazingLand(bool theBool);
    /** A flag indicating that the animal grazes land shared with other animals */
    void setUseCommonGrazingLand(bool theBool);
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    void setFoodValueOfSpecificGrazingLand(int theCalories);
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    void setFoodValueOfCommonGrazingLand(int theCalories);
    void setFodderUse(bool theBool);

    void setFodderSource1(QString theGuid);
    void setFodder1(int theValue);
    void setFodderGrain1(int theValue);

    void setFodderSource2(QString theGuid);
    void setFodder2(int theValue);
    void setFodderGrain2(int theValue);

    void setFodderSource3(QString theGuid);
    void setFodder3(int theValue);
    void setFodderGrain3(int theValue);

    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    void setFallowUsage(Priority thePriority);
    void setAreaUnits(int theIndexValue);
    void setRasterName(QString theRasterName);
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toXml();
    QString toText();
    QString toHtml();
    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml);
  private:
    /** A name for this set of animal paremeters */
    QString mName;
    /** A name for this set of animal paremeters */
    QString mDescription;
    /** The animal guid these parameters are associated with */
    QString mAnimalGuid;
    /** Portion of the Tame Meat Diet (Percentage) */
    int mPercentTameMeat;

    /** A flag for whether the animal has it's own specific
      * land designated to it for grazing
      */
    bool mUseSpecificGrazingLand;
    /** A flag indicating that the animal grazes land shared with other animals */
    bool mUseCommonGrazingLand;
    /** Food value of specific (or unique) grazing land as calories per dunum/hectare */
    int mFoodValueOfSpecificGrazingLand;
    /** Food value of common (or shared) grazing land as calories per dunum/hectare
      * NOTE that changing this value for any animal changes it for all!
      */
    int mFoodValueOfCommonGrazingLand;
    bool mFodderUse;
    QString mFodderSource1;
    int mFodder1;
    int mFodderGrain1;

    QString mFodderSource2;
    int mFodder2;
    int mFodderGrain2;

    QString mFodderSource3;
    int mFodder3;
    int mFodderGrain3;
    /** If fallow is to be grazed, and if so, at either a
      * HIGH MED or LOW priority to it's access
      */
    Priority mFallowUsage;
    int mAreaUnits;
    QString mRasterName;
};

#endif //LAANIMALPARAMETER_H

