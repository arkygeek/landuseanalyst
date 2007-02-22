/***************************************************************************
                          laplant.h  -  A plant class
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

#ifndef LAPLANT_H
#define LAPLANT_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/** 
  * An class to represent an plant
  * @author Tim Sutton, Jason Jorgenson
  */

class LaPlant : public LaSerialisable, public LaGuid 
{
  public:
    /** Constructor . */
    LaPlant();
    /** Desctructor . */
    ~LaPlant();
    /** copy constructor */
    LaPlant(const LaPlant& thePlant); 
    /** Assignement operator */
    LaPlant& operator= (const LaPlant& thePlant);
    
    //
    // Accessors
    //

    /** The name of this plant */
    QString name() const;
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

    /** Set the plantName
     * @see name()
     */
    void setName(QString theName);
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
    void setFodderCalories(int theCalories);
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

    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml);
  private:
    /** The name for this plant */
    QString mName;
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

#endif //LAPLANT_H

