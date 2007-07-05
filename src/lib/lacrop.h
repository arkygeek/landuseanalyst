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

#ifndef LACROP_H
#define LACROP_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/** 
  * An class to represent an crop
  * @author Tim Sutton, Jason Jorgenson
  */

class LaCrop : public LaSerialisable, public LaGuid 
{
  public:
    /** Constructor . */
    LaCrop();
    /** Desctructor . */
    ~LaCrop();
    /** copy constructor */
    LaCrop(const LaCrop& theCrop); 
    /** Assignement operator */
    LaCrop& operator= (const LaCrop& theCrop);
    
    //
    // Accessors
    //

    /** The name of this crop */
    QString name() const;
    /** The description of this crop */
    QString description() const;
    /** Average amount in Kg of production per hectare or dunum */
    int cropYield() const;
    /** The food value in calories of 1 kg of crop product (ie/ grain/fruit) */
    int cropCalories() const;
    /** How many Kg of fodder is left for animal feed after harvesting */
    int fodderProduction() const;
    /** The food value in calories of 1 Kg of fodder */
    int fodderCalories() const;
    /** All production levels based on either Kg/Dunum or Kg/Hectare
     *  0==Dunum 1==Hectare
     */
    int yieldUnits() const;

    //
    // Mutators
    //

    /** Set the cropName
     * @see name()
     */
    void setName(QString theName);

    /** Set the animal description
     * @see description()
     */
    void setDescription(QString theDescription);

    /** Set cropYield as Kg/area
     * @see cropYield()
     */
    void setCropYield(int theKg);
    /** Set cropCalories as kg 
     * @see cropCalories()
     */
    void setCropCalories(int theCalories);
    /** Set the fodderProduction as Kg/area
     * @see fodderProduction()
     */
    void setFodderProduction(int theKg);
    /** Set the fodderCalories with an integer
     * @see fodderCalories()
     */
    void setFodderTDN(int theCalories);
    /** Set the yieldUnits for area from index
     * @see yieldUnits()
     */
    void setYieldUnits(int theIndex);

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
    /** The name for this crop */
    QString mName;
    /** The description for this animal */
    QString mDescription;
    /** Set cropYield as Kg/area
     * @see cropYield()
     */
    int mCropYield;
    /** Set cropCalories as kg 
     * @see cropCalories()
     */
    int mCropCalories;
    /** Set the fodderProduction as Kg/area
     * @see fodderProduction()
     */
    int mCropFodderProduction;
    /** Set the fodderCalories with an integer
     * @see fodderCalories()
     */
    int mCropFodderCalories;
    /** Set the yieldUnits for area from index
     * @see yieldUnits()
     */
    int mYieldUnits;

};

#endif //LACROP_H

