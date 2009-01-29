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
    float population() const;
    /** Term for the period or time of the analysis e.g. Chalcolithic */
    QString period() const;
    /** What coordinate system being used */
    float projection() const;
    /** East coordinates */
    float easting() const;
    /** North coordinates */
    float northing() const;
    /** euclidean Distance selected */
    bool euclideanDistance() const;
    /** swalkingTime elected */
    bool walkingTime() const;
    /** pathDistance selected */
    bool pathDistance() const;
    /** The precision of the land area calculations */
    float precision() const;
    /** what percent of the diet comes from Meat */
    float dietPercent() const;
    /** what percent of the diet comes from crops */
    float plantPercent() const;
    /** what percent of the diet comes from meat */
    float meatPercent() const;
    /** TCalories per person per day */
    float caloriesPerPersonDaily() const;
    /** */
    /** Food Value of the common grazing land */
    float foodValueCommonLand() const;
    /** Dairy Utilisation */
    float dairyUtilisation() const;
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
    float limitDairyPercent() const;
    /** animals can be assigned an access to fallow
     * grazing land from 0 to 3,, 0 being not allowed to graze,
     * and then a three levels of preference
     */
    Status fallowStatus() const;
    /** the ratio of sown land to fallow land
      */
    float fallowRatio() const;

    /** this calculates how many calories will come from tame meat */
    float caloriesFromTameMeat();
    /** this calculates how many calories will come from mailk products */
    float caloriesFromMilk(QString theAnimalGuid);
    /** this returns the number of different crops being modeled */
    float countCrops();
    /** this returns the number of different animals being modelled */
    float countAnimals();
    /** this returns the calories from dairy produced by the herd of an animal */
    float caloriesFromDairyProducts();
    /** holder */
    float caloriesProvidedByTheCrop(QString theCropParameterGuid);
    /** holder */
    float caloriesProvidedByTheMeatOfTheAnimal(QString theAnimalParameterGuid);
    /** holder */
    float caloriesProvidedByTheMilkOfTheAnimal (QString theAnimalParameterGuid , QString theAnimalGuid);
    /** holder */
    //float getProductionTargetsCrops(QString theCropGuid, float theCalorieTarget);
    /** holder */
    //float getProductionTargetsAnimals(QString theAnimalGuid, float theCalorieTarget);
    /** holder */
    //float getAdjustedProductionTargetsAnimals(QString theAnimalGuid, float theCalorieTarget);
    float getAreaTargetsCrops(QString theCropGuid, float theProductionTarget);
    /** holder */
    float getFallowLandForACrop(QString theCropParameterGuid, float theAreaTarget);
    /** holder */
    void allocateFallowGrazingLand();
    /** holder */
    void adjustAnimalTargetsForFodder();
    /** holder */
    float requiredValue(QString theAnimalGuid);
    /** holder */
    float adjustAreaTargetsCrops();
    /** holder */
    float doTheFallowAllocation(Priority, float, float);
    /** holder */
    //HerdSize calculateHerdSize (QString theAnimalGuid);
    /** holder */
    
    QMap <QString, float> animalCalorieTargetsMap() const;
    /** holder */
    QMap <QString, float> animalFeedRequirementsMap() const;
    /** holder */
    QMap <QString, float> animalProductionTargetsMap() const;
    /** holder */
    QMap <QString, float> animalAreaTargetsMap() const;
    /** holder */
    QMap <QString, float> cropCalorieTargetsMap() const;
    /** holder */
    QMap <QString, float> cropProductionTargetsMap() const;
    /** holder */
    QMap <QString, float> cropAreaTargetsMap() const;
    /** holder */
    QMap <QString, QString> calcsCropsMap();
    /** holder */
    QMap <QString, QString> calcsAnimalsMap();
    /** holder */

    QString reportForAnimal(QString theAnimalGuid);
    /** holder */
    QString reportForCrop(QString theCropGuid);
    /** holder */
    QMap<QString, float> getAreaTargetsAnimalsMap();
    /** holder */
    QMap<QString, float> getAreaTargetsCropsMap();
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
    void setPopulation(float thePopulation);

    /** Set period of site being studied
     * @see period()
     */
    void setPeriod(QString thePeriod);

    /** Set projection
     * @see projection()
     */
    void setProjection(float theIndex);

    /** Set the easting
     * @see easting()
     */
    void setEasting(float theEasting);

    /** Set the northing
     * @see northing()
     */
    void setNorthing(float theNorthing);

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
    void setPrecision(float thePrecision);

    /** Set the overall percent that Plants form, for the entire population's diet
     * @see dietPercent()
     */
    void setDietPercent(float theDietPercent);

    /** Set the percent of TAME Plants, of the Plant based portion of the diet
     * @see plantPercent()
     */
    void setCropPercent(float theDietPercent);

    /** Set the meatPercent in weeks
     * @see meatPercent()
     */
    void setMeatPercent(float theMeatPercent);

    /** Set the caloriesPerPersonDaily in Days
     * @see caloriesPerPersonDaily()
     */
    void setCaloriesPerPersonDaily(float theCaloriesPerPersonDaily);

    /** Set the percent of dairy utilisation
     * @see dairyUtilisation()
     */
    void setDairyUtilisation(float thePercent);
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
    void setLimitDairyPercent(float thePercent);
    /** Set food value of the common land
     * @see commonLandValue()
     */
    void setCommonLandValue(float theValue, AreaUnits theAreaUnits);

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

    QMap<QString, float> getAreaTargetsAnimalsMapAFID ();
    QMap<QString, float> getAreaTargetsAnimalsMapAFDS ();
    QMap<QString, float> getAreaTargetsAnimalsMapPFDS ();
    QMap<QString, float> getAreaTargetsAnimalsMapPFID ();

    QMap<QString, float> getAreaTargetsCropsMapAFID ();
    QMap<QString, float> getAreaTargetsCropsMapAFDS ();
    QMap<QString, float> getAreaTargetsCropsMapPFDS ();
    QMap<QString, float> getAreaTargetsCropsMapPFID ();




    float countCaloriesForAnimals();

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
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toXml();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlCalorieAnimalTargets();
    /** Return an html representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlCalorieCropTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlProductionAnimalTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlAreaCropTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlAreaAnimalTargets();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtmlProductionCropTargets();
    /** Return a plain text representation of this layer
     */
    QString toText();
    /** Return an xml representation of this layer
     * @NOTE this class inherits the serialisable floaterface so
     * it MUST implement this
     */
    QString toHtml();

    /** Read this object from xml and return result as true for success, false for failure.
     * @see LaSerialisable
     * @NOTE this class inherits the serialisable floaterface so
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
    QMap <QString,float> mCaloriesProvidedByMeatMap;
    /** Initialise the map of calories needing to be provided
     * by each individual animal.
     */
    void initialiseCaloriesProvidedByMeatMap();

    /** A map of calorie targets for animals.
     */
    QMap <QString,float> mCaloriesProvidedByMilkMap;
    /** Initialise the map of calories  provided
     * by milk.
     */
    void initialiseCaloriesProvidedByMilkMap();
    
    /** A map of calorie targets for crops.
     */
    QMap <QString,float> mCaloriesProvidedByCropsMap;
    /** Initialise the map of calories needing to be provided
     * by each individual crop.
     */
    void initialiseCaloriesProvidedByCropsMap();

    /** A map of production targets for animals.
     */
    QMap <QString,float> mProductionRequiredAnimalsMap;
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
    QMap <QString,float> mAreaTargetsAnimalsMap;
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
    QMap <QString,float> mAreaTargetsCropsMap;

    /** Initialise the map of calories needing to be provided
     * by each individual crop.
     */
    void initialiseAreaTargetsCropsMap();


///////////////////////////////////////////////////////////////////////////////////

    /** A map of running totals for calorie requirements for animals.
     * As we account for each resource (fallow, crop x, crop y etc)
     * we can remove it from the cumulative total.
     */
    QMap <QString,float> mValueMap;
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
    float mPopulation;
    /** Period of the site */
    QString mPeriod;
    /** The projection of the data used in the model */
    float mProjection;
    /** East coordinate of the site being analysed */
    float mEasting;
    /** North coordinate of the site being analysed */
    float mNorthing;
    /** Euclidean method of analysis */
    bool mEuclideanDistance;
    /** Walking time method of analysis */
    bool mWalkingTime;
    /** Path distance method of analysis */
    bool mPathDistance;
    /** Precision or degree of accuracy used to determine results */
    float mPrecision;
    /** Percentage of overall diet fulfilled by plant derived food */
    float mDietPercent;
    /** Percentage of Plant derived food fulfilled by domesticated crops */
    float mPercentOfDietThatIsFromCrops;
    /** Percentage of Animal (meat) derived food fulfilled by domesticated animals */
    float mMeatPercent;
    /** The number of calories required per person per day (average) */
    float mCaloriesPerPersonDaily;
    /** The percent of dairy utilisation by the settlement */
    float mDairyUtilisation;

    /** The percent of dairy utilisation by the settlement */
    float mBaseOnPlants;
    /** The percent of dairy utilisation by the settlement */
    bool mIncludeDairy;
    /** The percent of dairy utilisation by the settlement */
    float mLimitDairy;
    /** The percent of dairy utilisation by the settlement */
    float mLimitDairyPercentage;

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
    float mCommonGrazingLandValueTarget;
    /** holder */
      //float mCommonGrazingLandValue;
    float mCommonGrazingValue;
    /** holder */
    float mCommonGrazingLandAreaTarget;
    /** holder */
    float mCommonCropLand;
    /** holder */
    HerdSize mHerdSize;

};
#endif   //LAMODEL_H

