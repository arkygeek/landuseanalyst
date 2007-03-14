/***************************************************************************
 *   Copyright (C) 2007 by: Tim Sutton        tim@linfiniti.com            *
 *                          Jason Jorgenson   arkygeek@gmail.com           *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/

#ifndef LAMODEL_H
#define LAMODEL_H

class QString;
#include "laserialisable.h"
#include "laguid.h"
#include <QString>
/**
  * An class to represent an model
  * @author Tim Sutton
  */

class LaModel : public LaSerialisable, public LaGuid
{
  public:
    /** Constructor . */
    LaModel();
    /** Desctructor . */
    ~LaModel();
    /** copy constructor */
    LaModel(const LaModel& theModel);
    /** Assignement operator */
    LaModel& operator= (const LaModel& theModel);

    //
    // Accessors
    //

    /** The name of this model */
    QString name() const;
    /** The population of this model */
    QString population() const;
    /** Percentage of models live weight that can be utilized for meat */
    int period() const;
    /** The weight in kg at which the models are slaughtered */
    int projection() const;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int easting() const;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int northing() const;
    /** The number of calories a euclidean female requires per day */
    int euclidean() const;
    /** The number of calories a walkingTime female requires per day */
    int walkingTime() const;
    /** The number of calories a pathDistance requires per day */
    int pathDistance() const;
    /** The life expectancy in years of the model */
    int precision() const;
    /** The number of years a female will reliably produce offspring */
    int dietSlider() const;
    /** The average number of young produced per pregnancy */
    int plantSlider() const;
    /** The age in weeks at which babies stop suckling */
    int meatSlider() const;
    /** The number of days required for gestation */
    int caloriesPerPersonDaily() const;
    /** The number of days in the female estrous cycle */
    int spare() const;

    //
    // Mutators
    //

    /** Set the modelName
     * @see name()
     */
    void setName(QString theName);

    /** Set the model population
     * @see population()
     */
    void setPopulation(QString thePopulation);

    /** Set useableMeat as a percentage
     * @see period()
     */
    void setPeriod(int thePercentage);

    /** Set projection as kg
     * @see projection()
     */
    void setProjection(int theKg);

    /** Set the easting in weeks
     * @see easting()
     */
    void setEasting(int theWeeks);

    /** Set the northing as a percentage
     * @see northing()
     */
    void setNorthing(int thePercentage);

    /** Set the daily calories required for a euclidean female
     * @see euclidean()
     */
    void setEuclidean(int theCalories);

    /** Set the daily calories required for a walkingTime female
     * @see Period()
     */
    void setWalkingTime(int theCalories);

    /** Set the daily calories required for a pathDistance
     * @see Period()
     */
    void setPathDistance(int theCalories);

    /** Set the average lifeExpectancy in years
     * @see lifeExpectancy()
     */
    void setPrecision(int theMonths);

    /** Set the average dietSliderExpectancy in years
     * @see dietSlider()
     */
    void setDietSlider(int theYears);

    /** Set the average number of plantSlider
     * @see plantSlider()
     */
    void setPlantSlider(int theInteger);

    /** Set the meatSlider in weeks
     * @see meatSlider()
     */
    void setMeatSlider(int theWeeks);

    /** Set the caloriesPerPersonDaily in Days
     * @see caloriesPerPersonDaily()
     */
    void setCaloriesPerPersonDaily(int theDays);

    /** Set the spare in days
     * @see spare()
     */
    void setSpare(int theDays);

    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toXml();
    /** Return a plain text representation of this layer
     */
    QString toText();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtml();

    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    bool fromXml(const QString theXml);
  private:
    /** The name for this model */
    QString mName;
    /** The population for this model */
    QString mPopulation;
    /** Percentage of models live weight that can be utilized for meat */
    int mPeriod;
    /** The weight in kg at which the models are slaughtered */
    int mProjection;
    /** The number of weeks from birth it takes to attain slaughtering weight */
    int mEasting;
    /** The percentage of babies that die before being usable as either meat or breeding */
    int mNorthing;
    /** The number of calories a euclidean female requires per day */
    int mEuclidean;
    /** The number of calories a walkingTime female requires per day */
    int mWalkingTime;
    /** The number of calories a pathDistance requires per day */
    int mPathDistance;
    /** The life expectancy in years of the model */
    int mPrecision;
    /** The number of years a female will reliably produce offspring */
    int mDietSlider;
    /** The average number of young produced per pregnancy */
    int mPlantSlider;
    /** The age in weeks at which babies stop suckling */
    int mMeatSlider;
    /** The number of days required for gestation */
    int mCaloriesPerPersonDaily;
    /** The number of days in the female estrous cycle */
    int mSpare;
};

#endif //LAMODEL_H

