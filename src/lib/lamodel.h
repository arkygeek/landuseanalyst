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

#include <QDialog>
#include <QHash>
#include <QPair>
class QString;
#include "laserialisable.h"
#include "laguid.h"
#include "la.h"
#include "ladietlabels.h"

#include <QString>
#include <QMap>
/**
  * A class to represent a model
  * @author Tim Sutton, Jason Jorgenson
  */

class LaModel : public QObject, public LaSerialisable, public LaGuid
{
  Q_OBJECT;
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
    /** euclidean Distance selected */
    bool euclideanDistance() const;
    /** swalkingTime elected */
    bool walkingTime() const;
    /** pathDistance selected */
    bool pathDistance() const;
    /** The precision of the land area calculations */
    int precision() const;
    /** what percent of the diet comes from Meat */
    int dietPercent() const;
    /** what percent of the diet comes from crops */
    int plantPercent() const;
    /** what percent of the diet comes from meat */
    int meatPercent() const;
    /** TCalories per person per day */
    int caloriesPerPersonDaily() const;
    /** */
    /** Food Value of the common grazing land */
    int foodValueCommonLand() const;
    /** Dairy Utilisation */
    int dairyUtilisation() const;
    /** a bool to indicate whether the diet ratios
      * will be based on plants or animals.
      * If te bool is TRUE it is based on plants
      */
    bool baseOnPlants() const;
    /** this bool, if true, will consider dairy as
      * part of meat when doing the diet calculations
      */
    bool includeDairy() const;
    /** this bool will impose an overall limit on
      * the portion of the diet that can be based
      * on dairy products
      */
    bool limitDairy() const;
    /** this is the maximum percent of the diet that
      * dairy products can be
      * @SEE includeDairy()
      */
    int limitDairyPercent() const;
    /** animals can be assigned an access to fallow
     * grazing land from 0 to 3,, 0 being not allowed to graze,
     * and then a three levels of preference
     */
    Status fallowStatus() const;
    /** the ratio of sown land to fallow land
      */
    float fallowRatio() const;
    /** this will calculate how many calories crops will provide */
    int caloriesFromCrops();
    /** this calculates how many calories will come from tame meat */
    int caloriesFromTameMeat();
    /** this calculates how many calories will come from mailk products */
    int caloriesFromMilk(QString theAnimalGuid);
    /** this returns the number of different crops being modeled */
    int countCrops();
    /** this returns the number of different animals being modelled */
    int countAnimals();
    /** this returns the calories from dairy produced by the herd of an animal */
    int caloriesFromDairyProducts();
    /** holder */
    int caloriesProvidedByTheCrop(QString theCropParameterGuid);
    /** holder */
    int caloriesProvidedByTheMeatOfTheAnimal(QString theAnimalParameterGuid);
    /** holder */
    int caloriesProvidedByTheMilkOfTheAnimal (QString theAnimalParameterGuid , QString theAnimalGuid);
    /** holder */
    int getProductionTargetsCrops(QString theCropGuid, int theCalorieTarget);
    /** holder */
    int getProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget);
    /** holder */
    //int getAdjustedProductionTargetsAnimals(QString theAnimalGuid, int theCalorieTarget);
    int getAreaTargetsCrops(QString theCropGuid, int theProductionTarget);
    /** holder */
    int getFallowLandForACrop(QString theCropParameterGuid, int theAreaTarget);
    /** holder */
    void allocateFallowGrazingLand();
    /** holder */
    void adjustAnimalTargetsForFodder();
    /** holder */
    int requiredValue(QString theAnimalGuid);
    /** holder */
    int adjustAreaTargetsCrops();
    /** holder */
    int doTheFallowAllocation(Priority, int, int);
    /** holder */
    HerdSize calculateHerdSize (QString theAnimalGuid);
    /** holder */
    
    QMap <QString, int> animalCalorieTargetsMap() const;
    /** holder */
    QMap <QString, int> animalFeedRequirementsMap() const;
    /** holder */
    QMap <QString, int> animalProductionTargetsMap() const;
    /** holder */
    QMap <QString, int> animalAreaTargetsMap() const;
    /** holder */
    QMap <QString, int> cropCalorieTargetsMap() const;
    /** holder */
    QMap <QString, int> cropProductionTargetsMap() const;
    /** holder */
    QMap <QString, int> cropAreaTargetsMap() const;
    /** holder */
    QMap <QString, QString> calcsCropsMap();
    /** holder */
    QMap <QString, QString> calcsAnimalsMap();
    /** holder */

    QString reportForAnimal(QString theAnimalGuid);
    /** holder */
    QString reportForCrop(QString theCropGuid);
    /** holder */
    QMap<QString, int> getAreaTargetsAnimalsMap();
    /** holder */
    QMap<QString, int> getAreaTargetsCropsMap();
    /** holder */

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

    /** Set the percent of dairy utilisation
     * @see dairyUtilisation()
     */
    void setDairyUtilisation(int thePercent);
    /** Set the holder
     * @see holder()
     */
    void setBaseOnPlants(bool theBool);
    /** Set the holder
     * @see holder()
     */
    void setIncludeDairy(bool theBool);
    /** Set the holder
     * @see holder()
     */
    void setLimitDairy(bool theBool);
    /** Set the holder
     * @see holder()
     */
    void setLimitDairyPercent(int thePercent);
    /** Set food value of the common land
     * @see commonLandValue()
     */
    void setCommonLandValue(int theValue, AreaUnits theAreaUnits);

    /** Set the holder
     * @see holder()
     */
    void setCommonLandAreaUnits(AreaUnits theAreaUnits);
    
    /** Set the holder
     * @see holder()
     */
    void setHerdSize(QString theAnimalGuid);

    /** Set the animals for this model
     * @param QMap<QString,QString> a list of animal guid and animal parameter guids
     */
    void setAnimals(QMap<QString,QString>);

    /** Set the crop for this model
     * @param QMap<QString,QString> a list of crop guid and animal parameter guids
     */
    void setCrops(QMap<QString,QString>);

    LaDietLabels doCalcsPlantsFirstIncludeDairy ();
    LaDietLabels doCalcsPlantsFirstDairySeperate ();
    LaDietLabels doCalcsAnimalsFirstIncludeDiary ();
    LaDietLabels doCalcsAnimalsFirstDairySeparate ();
    
    /** Perform calculations
     */
    void DoCalculations();

    float countTotalCaloriesFromDairy();
    /** Clear all mpas holding results of calculations
     * @see clearCalcMaps()
     */
    void clearCalcMaps();
    /** Set the holder
     * @see holder()
     */
    void setFallowStatus(Status theStatus);
    /** Set the holder
     * @see holder()
     */
    void setFallowRatio(float theRatio);
      //void setDoTheFallowAllocation(Priority, float, float);
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toXml();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlCalorieAnimalTargets();
    /** Return an html representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlCalorieCropTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlProductionAnimalTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlAreaCropTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlAreaAnimalTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable interface so
     * it MUST implement this
     */
    QString toHtmlProductionCropTargets();
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

    /** Broadcast to any listeners status messages.
     *  This is a convenience function. Internally it will
     *  do emit message(QString theMessage) each time it
     *  is called.
     *  @param QString theMessage to be logged. */
    void logMessage(QString theMessage);


  signals:
    /** Send log info to any listeners.
     * @param QString the message to be logged.
     */
    void message(QString theMessage);

  private:
    /** A map of calorie targets for animals.
     */
    QMap <QString,int> mCaloriesProvidedByMeatMap;
    /** Initialise the map of calories needing to be provided
     * by each individual animal.
     */
    void initialiseCaloriesProvidedByMeatMap();

    /** A map of calorie targets for animals.
     */
    QMap <QString,int> mCaloriesProvidedByMilkMap;
    /** Initialise the map of calories  provided
     * by milk.
     */
    void initialiseCaloriesProvidedByMilkMap();
    
    /** A map of calorie targets for crops.
     */
    QMap <QString,int> mCaloriesProvidedByCropsMap;
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
    QMap <QString,int> mProductionRequiredCropsMap;
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

    /** Initialise thecalculations map for Animals
     */
    void initialiseCalcsAnimalsMap();

    /** Initialise thecalculations map for Crops
     */
    void initialiseCalcsCropsMap();
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
    QMap <QString,int> mValueMap;
    /** Initialise the cumulative calories map to the calories
     * required for each animal.
     */
    void initialiseValueMap();
    
    QMap <QString, LaFoodSourceMap> mFodderMap;   // QPair < StrawAndChaff , Grain >
    /** Initialise the cumulative calories map to the calories
     * required for each animal.
     */
    void initialiseFodderMap();
    
    /** A map of all of the calculations for Animals
     */
    QMap <QString,QString> mCalcsAnimalsMap;

    /** A map of all of the calculations for Crops
     */
    QMap <QString,QString> mCalcsCropsMap;


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
    /** The percent of dairy utilisation by the settlement */
    int mDairyUtilisation;

    /** The percent of dairy utilisation by the settlement */
    int mBaseOnPlants;
    /** The percent of dairy utilisation by the settlement */
    bool mIncludeDairy;
    /** The percent of dairy utilisation by the settlement */
    int mLimitDairy;
    /** The percent of dairy utilisation by the settlement */
    int mLimitDairyPercentage;

    /** A map to hold the associated animals and their parameters */
    QMap <QString,QString> mAnimalsMap;
    /** A map to hold the associated crops and their parameters */
    QMap <QString,QString> mCropsMap;
    /** holder */
    AreaUnits mCommonLandAreaUnits;
    /** holder */
    Status mFallowStatus;
    /** holder */
    float mFallowRatio;
    /** holder */
    int mCommonGrazingLandValueTarget;
    /** holder */
      //int mCommonGrazingLandValue;
    int mCommonGrazingValue;
    /** holder */
    int mCommonGrazingLandAreaTarget;
    /** holder */
    int mCommonCropLand;
    /** holder */
    HerdSize mHerdSize;

};
#endif   //LAMODEL_H

