/***************************************************************************
 *   Copyright (C) 2006 by Tim Sutton   *
 *   tim@linfiniti.com   *
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
#ifndef LAUTILS_H
#define LAUTILS_H
class QString;
class QStringList;
#include <QHash>
#include <QMap>
#include "laanimal.h"
#include "lacrop.h"
#include "laanimalparameter.h"
#include "lacropparameter.h"

/** This is a helper class with mainly static methods for easily
 * obtaining the directories and paths relating to the application
 * for example the users settings dir.
 */
class LaUtils
{
  public:
    /**
     * Find the place on the filesystem where user data
     * are stored.
     *
     * Typically this will be ~/.landuseAnalyst
     *
     * @return QString containing the relevant directory name
     */
    static const QString userSettingsDirPath();
    /**
     * Find the place on the filesystem where user defined animal
     * profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/animalProfiles
     *
     * @return QString containing the relevant directory name
     */
    static const QString userAnimalProfilesDirPath();
    /**
     * Find the place on the filesystem where user defined animal
     * model parameter profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/animalParameters
     *
     * @return QString containing the relevant directory name
     */
    static const QString userAnimalParametersDirPath();
    /**
     * Find the place on the filesystem where user defined crop
     * model parameter profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/cropParameters
     *
     * @return QString containing the relevant directory name
     */
    static const QString userCropParametersDirPath();
    /** Get the place where model outputs are to be stored.
     * By default this is in ~/.landuseAnalyst/modelOutputs
     * But if modelOutputsDir is specified in QSettings, it will override
     * the default.
     */
    static const QString getModelOutputDir();
    /**
     * Find the place on the filesystem where user defined crop
     * profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/crops
     *
     * @return QString containing the relevant directory name
     */
    static const QString userCropProfilesDirPath();

    /** This typedef is used to refer to a collection of layersets.
     * the key is the layerset name
     * the value is the layerset itself
     */
    typedef QMap<QString,LaCrop> CropMap;

    /** Get a QMap of the avaliable layersets in the users layersets directory
     * @return a QMap<QString,OmgLayerSet> where the QString key is the layerset name
     **/
    static LaUtils::CropMap getAvailableCrops();

    /** Get a LaCrop given its GUID.
     * If no matching crop is found, a blank one is
     * returned.
     */
    static LaCrop getCrop(QString theGuid);
    
    /** This typedef is used to refer to a collection of layersets.
     * the key is the layerset name
     * the value is the layerset itself
     */
    typedef QMap<QString,LaAnimal> AnimalMap;
    
    /** Get a LaAnimal given its GUID.
     * If no matching animal is found, a blank one is
     * returned.
     */
    static LaAnimal getAnimal(QString theGuid);

   /**
     * Find the place on the filesystem where user defined cropParameter
     * profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/cropParameters
     *
     * @return QString containing the relevant directory name
     */
    static const QString userCropParameterProfilesDirPath();

    /** This typedef is used to refer to a collection of layersets.
     * the key is the layerset name
     * the value is the layerset itself
     */
    typedef QMap<QString,LaCropParameter> CropParameterMap;

    /** Get a QMap of the avaliable layersets in the users layersets directory
     * @return a QMap<QString,OmgLayerSet> where the QString key is the layerset name
     **/
    static LaUtils::CropParameterMap getAvailableCropParameters();

    /** Get a LaCropParameter given its GUID.
     * If no matching animalparameter is found, a blank one is
     * returned.
     */
    static LaCropParameter getCropParameter(QString theGuid);
    
    /** This typedef is used to refer to a collection of layersets.
     * the key is the layerset name
     * the value is the layerset itself
     */
    typedef QMap<QString,LaAnimalParameter> AnimalParameterMap;
    /** Get a QMap of the avaliable layersets in the users layersets directory
     * @return a QMap<QString,OmgLayerSet> where the QString key is the layerset name
     **/
    static LaUtils::AnimalParameterMap getAvailableAnimalParameters();
    
    /** Get a LaAnimalParameter given its GUID.
     * If no matching animalparameter is found, a blank one is
     * returned.
     */
    static LaAnimalParameter getAnimalParameter(QString theGuid);
    
    /**
     * Find the place on the filesystem where user defined animalParameter
     * profiles are stored.
     *
     * Typically this will be ~/.landuseAnalyst/animalParameterProfiles
     *
     * @return QString containing the relevant directory name
     */
    static const QString userAnimalParameterProfilesDirPath();
    

    /** Get a QMap of the avaliable animals from the users animals directory
     * @return a QMap<QString,OmgLayerSet> where the QString key is 
     * the animal name.
     **/
    static LaUtils::AnimalMap getAvailableAnimals();

    /** Sort a string list into descending alphabetic order
     *  and return the result.
     *  @param theList - the QStringList to be sorted
     *  @return QStringList - sorted in descending alphabetical order
     */
    static QStringList sortList(QStringList theList);

    /** Remove any duplucate entries from a sorted list
     *  @param theList - the QStringList to be sorted
     *  @return QStringList - a list with no sequential duplicates
     */
    static QStringList uniqueList(QStringList theList);

    /** Scan the users work directory looking for experiment files
     * and return the list of files found.
     * @return A QStringList of files found
     */
    static QStringList getExperimentsList();

    /** A helper method to easily write a file to disk.
     * @param theFileName - the filename to be created or overwritten
     * @param theData - the data that will be written into the file
     * @return bool - false if the file could not be written
     */
    static bool createTextFile(QString theFileName, QString theData);

    /** A helper method to xml encode any special chars in a string
     * (< > & etc) will become (&lt; &gt; &amp; etc)
     * @param QString - the string to be properly encoded
     * @return A QString with the special chars properly encoded
     */
    static QString xmlEncode(QString theString);

    /** A helper method to xml deencode any special chars in a string
     * (&lt; &gt; &amp; etc) will become (< > & etc)
     * @param QString - the string to be properly decoded
     * @return A QString with the encoded chars properly decoded
     */
    static QString xmlDecode(QString theString);

    /** Get the standard style sheet for reports. Typically this will be 
      * used like this:
      * QString myStyle = getStandardCss();
      * textBrowserFoo->document()->setDefaultStylesheet(myStyle);
      */
    static QString getStandardCss();
  private:

};


#endif
