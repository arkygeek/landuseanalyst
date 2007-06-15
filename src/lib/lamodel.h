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

#ifndef Percent
#define Percent

#include <QDialog>
#include <QHash>
#include <QPair>
class QString;
#include "laserialisable.h"
#include "laguid.h"
#include "la.h"
#include <QString>
#include <QMap>
/**
  * A class to represent an model
  * @author Tim Sutton, Jason Jorgenson
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
    int population() const;
    /** Term for the period or time of the analysis e.g. Chalcolithic */
    QString period() const;
    /** What coordinate system being used */
    int projection() const;
    /** East coordinates */
    int easting() const;
    /** North coordinates */
    int northing() const;
    /** Do we use the Euclidean Distance modelling method */
    bool euclideanDistance() const;
    /** The number of calories a walkingTime female requires per day */
    bool walkingTime() const;
    /** The number of calories a pathDistance requires per day */
    bool pathDistance() const;
    /** The life expectancy in years of the model */
    int precision() const;
    /** The number of years a female will reliably produce offspring */
    int dietPercent() const;
    /** The average number of young produced per pregnancy */
    int plantPercent() const;
    /** The age in weeks at which babies stop suckling */
    int meatPercent() const;
    /** The number of days required for gestation */
    int caloriesPerPersonDaily() const;
    /** The number of days in the female estrous cycle */

    Status fallowStatus() const;

    int caloriesFromCrops();
    int caloriesFromTameMeat();
    int countCrops();
    int countAnimals();
    int caloriesProvidedByTheCrop(QString theCropParameterGuid);
    int caloriesProvidedByTheAnimal(QString theAnimalParameterGuid);
    int getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget);
    int getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget);
    int getAreaTargetsCrops(QString theCropGuid, int theProductionTarget);
    int getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget);
    void allocateFallowGrazingLand();
    void adjustAnimalTargetsForFodder();
    int caloriesNeededByAnimal(QString theAnimalGuid);
    int adjustAreaTargetsCrops();
    int doTheFallowAllocation(Priority, int, int);

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
    void setPopulation(int thePopulation);

    /** Set period of site being studied
     * @see period()
     */
    void setPeriod(QString thePeriod);

    /** Set projection
     * @see projection()
     */
    void setProjection(int theIndex);

    /** Set the easting
     * @see easting()
     */
    void setEasting(int theEasting);

    /** Set the northing
     * @see northing()
     */
    void setNorthing(int theNorthing);

    /** Set method of analysis to euclideanDistance
     * @see euclideanDistance()
     */
    void setEuclideanDistance(bool theBool);

    /** Set method of analysis to  walkingTime
     * @see Period()
     */
    void setWalkingTime(bool theBool);

    /** Set method of analysis to pathDistance
     * @see pathDistance()
     */
    void setPathDistance(bool theBool);

    /** Set mmodel's precision
     * @see precision()
     */
    void setPrecision(int thePrecision);

    /** Set the overall percent that Plants form, for the entire population's diet
     * @see dietPercent()
     */
    void setDietPercent(int theDietPercent);

    /** Set the percent of TAME Plants, of the Plant based portion of the diet
     * @see plantPercent()
     */
    void setCropPercent(int theDietPercent);

    /** Set the meatPercent in weeks
     * @see meatPercent()
     */
    void setMeatPercent(int theMeatPercent);

    /** Set the caloriesPerPersonDaily in Days
     * @see caloriesPerPersonDaily()
     */
    void setCaloriesPerPersonDaily(int theCaloriesPerPersonDaily);

    /** Set the animals for this model
     * @param QMap<QString,QString> a list of animal guid and animal parameter guids
     */
    void setAnimals(QMap<QString,QString>);

    /** Set the crop for this model
     * @param QMap<QString,QString> a list of crop guid and animal parameter guids
     */
    void setCrops(QMap<QString,QString>);

    /** Perform calcs
     */
    void DoCalculations();

    void setFallowStatus(Status theStatus);
    //void setDoTheFallowAllocation(Priority, float, float);
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
    /** A map of calorie targets for animals.
     */
    QMap <QString,float> mCaloriesProvidedByAnimalsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual animal.
     */
    void initialiseCaloriesProvidedByAnimalsMap();

    /** A map of calorie targets for crops.
     */
    QMap <QString,float> mCaloriesProvidedByCropsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual crop.
     */
    void initialiseCaloriesProvidedByCropsMap();

    /** A map of production targets for animals.
     */
    QMap <QString,int> mProductionRequiredAnimalsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual animal.
     */
    void initialiseProductionRequiredAnimalsMap();

    /** A map of calorie targets for crops.
     */
    QMap <QString,float> mProductionRequiredCropsMap;
    /** Initialise the map of production levels needing
     * to meet the calorie requirements
     */
    void initialiseProductionRequiredCropsMap();
///////////////////////////////////////////////////////////////////////////////////
    /** A map of are targets for animals.
     */
    QMap <QString,int> mAreaTargetsAnimalsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual animal.
     */
    void initialiseAreaTargetsAnimalsMap();

    /** A map of are targets for crops.
     */
    QMap <QString,int> mAreaTargetsCropsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual crop.
     */
    void initialiseAreaTargetsCropsMap();


///////////////////////////////////////////////////////////////////////////////////

    /** A map of running totals for calorie requirements for animals.
     * As we account for each resource (fallow, crop x, crop y etc)
     * we can remove it from the cumulative total.
     */
    QMap <QString,float> mCaloriesRequiredByAnimalsMap;
    /** Initialise the cumulative calories map to the calories
     * required for each animal.
     */
    void initialiseCaloriesRequiredByAnimalsMap();



    /** The name for this model */
    QString mName;
    /** The population for this model */
    int mPopulation;
    /** Period of the site */
    QString mPeriod;
    /** The projection of the data used in the model */
    int mProjection;
    /** East coordinate of the site being analysed */
    int mEasting;
    /** North coordinate of the site being analysed */
    int mNorthing;
    /** Euclidean method of analysis */
    bool mEuclideanDistance;
    /** Walking time method of analysis */
    bool mWalkingTime;
    /** Path distance method of analysis */
    bool mPathDistance;
    /** Precision or degree of accuracy used to determine results */
    int mPrecision;
    /** Percentage of overall diet fulfilled by plant derived food */
    int mDietPercent;
    /** Percentage of Plant derived food fulfilled by domesticated crops */
    int mPercentOfDietThatIsFromCrops;
    /** Percentage of Animal (meat) derived food fulfilled by domesticated animals */
    int mMeatPercent;
    /** The number of calories required per person per day (average) */
    int mCaloriesPerPersonDaily;
    /** A map to hold the associated animals and their parameters */
    QMap<QString,QString> mAnimalsMap;
    /** A map to hold the associated crops and their parameters */
    QMap<QString,QString> mCropsMap;

    Status mFallowStatus;
    void makeCircle(int theX, int theY);
    void getArea(float theArea);
    void makeWalkCost(int theX, int theY);
    void makeEuclideanCost(int theX, int theY);
    void makePathDistanceCost(int theX, int theY);
    void writeMetaData(QString theValue);
    int mCommonGrazingLandAreaTarget;
};
#endif //Percent

