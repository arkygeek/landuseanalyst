#include "lautils.h"
#include "laanimal.h"
#include "lacrop.h"
#include "laanimalparameter.h"
#include "lacropparameter.h"
#include "la.h"

#include <QApplication>
#include <QDir>
#include <QFile>
#include <QPluginLoader>
#include <QSettings>
#include <QString>
#include <QStringList>
#include <QVector>
#include <QtXml>

#include <QFileDialog>
#ifdef Q_OS_MACX
//for getting app bundle path
#include <ApplicationServices/ApplicationServices.h>
#endif


/**
 * Returns the path to the settings directory in user's home dir
 */
const QString LaUtils::userSettingsDirPath()
{
  QSettings mySettings;
  QString myPath=
      mySettings.value("dataDirs/dataDir", QDir::homePath() + QString("/.landuseAnalyst/") ).toString();
  //  Make sure the users settings dir actually exists
  //qDebug("LaUtils::userSettingsDirPath() = " + myPath.toLocal8Bit());
  QDir().mkpath(myPath);
  return myPath;
}
const QString LaUtils::getModelOutputDir()
{
  QString myPath = userSettingsDirPath()+QDir::separator()+"modelOutputs"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}
const QString LaUtils::userAnimalProfilesDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"animalProfiles"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}


const QString LaUtils::userCropProfilesDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"cropProfiles"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}


LaUtils::AnimalMap LaUtils::getAvailableAnimals()
{
  LaUtils::AnimalMap myMap;
  QDir myDirectory(userAnimalProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading animal: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaAnimal myAnimal;
      myAnimal.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myAnimal.name().isEmpty())
      {
        qDebug("Animal name was empty!");
        continue;
      }
      //qDebug("Adding " + myAnimal.name());
      //qDebug(myAnimal.toText().toLocal8Bit());
      myMap[myAnimal.guid()]=myAnimal;
    }
  }
  return myMap;
}
LaAnimal LaUtils::getAnimal(QString theGuid)
{
  QDir myDirectory(userAnimalProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading animal: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaAnimal myAnimal;
      myAnimal.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myAnimal.name().isEmpty())
      {
        qDebug("Animal name was empty!");
        continue;
      }
      //qDebug("Adding " + myAnimal.name());
      //qDebug(myAnimal.toText().toLocal8Bit());
      if (myAnimal.guid()==theGuid)
      {
        return myAnimal;
      }
    }
  }
  LaAnimal myAnimal; //blank animal
  return myAnimal;
}

LaUtils::CropMap LaUtils::getAvailableCrops()
{
  LaUtils::CropMap myMap;
  QDir myDirectory(userCropProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading crop: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaCrop myCrop;
      myCrop.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myCrop.name().isEmpty())
      {
        qDebug("Crop name was empty!");
        continue;
      }
      //qDebug("Adding " + myCrop.name());
      myMap[myCrop.guid()]=myCrop;
      //qDebug(myCrop.toText().toLocal8Bit());
    }
  }
  return myMap;
}

LaCrop LaUtils::getCrop(QString theGuid)
{
  QDir myDirectory(userCropProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading crop: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaCrop myCrop;
      myCrop.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myCrop.name().isEmpty())
      {
        qDebug("Crop name was empty!");
        continue;
      }
      //qDebug("Adding " + myCrop.name());
      //qDebug(myCrop.toText().toLocal8Bit());
      if (myCrop.guid()==theGuid)
      {
        return myCrop;
      }
    }
  }
  LaCrop myCrop; //blank crop
  return myCrop;
}
const QString LaUtils::userConversionTablesDirPath()
{
  // always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"conversionTables"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

const QString LaUtils::userAnimalParameterProfilesDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"animalParameterProfiles"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

const QString LaUtils::userImagesDirPath()
{
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst") +
    QDir::separator()+"images"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

const QString LaUtils::userCropParameterProfilesDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator() + "cropParameterProfiles" + QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

int LaUtils::convertAreaToHectares(AreaUnits theAreaUnit, int theArea)
{
  // this may seem ridiculous to do it this way, but
  // i plan to include other area units and this way
  // it will make it very easy to work with in the future
  // all need be done is add new units to la.h enum and enter
  // into the following switch...

  float myHectares = 0.;

  switch (theAreaUnit)  // Dunum, Hectare
  {
    case  Dunum:
      myHectares = theArea * 10.;
      break;
    case  Hectare:
      myHectares = theArea;
      break;   /*    add new units here after updating la.h enum ex:
    case  Acre:
      HyHectares = theArea / 2.47105381;
      break;     */
  }
  return static_cast<int>(myHectares);
}

LaUtils::AnimalParameterMap LaUtils::getAvailableAnimalParameters()
{
  LaUtils::AnimalParameterMap myMap;
  QDir myDirectory(userAnimalParameterProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading animalParameter: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaAnimalParameter myAnimalParameter;
      myAnimalParameter.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myAnimalParameter.name().isEmpty())
      {
        qDebug("AnimalParameter name was empty!");
        continue;
      }
      //qDebug("Adding " + myAnimalParameter.name());
      //qDebug(myAnimalParameter.toText().toLocal8Bit());
      myMap[myAnimalParameter.guid()]=myAnimalParameter;


      //for debug only...
      ;
      qDebug(" ++ lautil  Restoring " +
          QString::number(myAnimalParameter.fodderSourceMap().count()).toLocal8Bit()
          + " food sources into animal parameter.");
    }
  }
  return myMap;
}

LaAnimalParameter LaUtils::getAnimalParameter(QString theGuid)
{
  QDir myDirectory(userAnimalParameterProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading animalParameter: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaAnimalParameter myAnimalParameter;
      myAnimalParameter.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myAnimalParameter.name().isEmpty())
      {
        qDebug("AnimalParameter name was empty!");
        continue;
      }
      //qDebug("Adding " + myAnimalParameter.name());
      //qDebug(myAnimalParameter.toText().toLocal8Bit());
      if (myAnimalParameter.guid()==theGuid)
      {
        return myAnimalParameter;
      }
    }
  }
  LaAnimalParameter myAnimalParameter;
  return myAnimalParameter; //retrun a blank one since no match found

}

LaUtils::CropParameterMap LaUtils::getAvailableCropParameters()
{
  LaUtils::CropParameterMap myMap;
  QDir myDirectory(userCropParameterProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading cropParameter: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaCropParameter myCropParameter;
      myCropParameter.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myCropParameter.name().isEmpty())
      {
        //qDebug("CropParameter name was empty!");
        continue;
      }
      //qDebug("Adding " + myCropParameter.name());
      myMap[myCropParameter.guid()]=myCropParameter;
      //qDebug(myCropParameter.toText().toLocal8Bit());
    }
  }
  return myMap;
}

LaCropParameter LaUtils::getCropParameter(QString theGuid)
{
  QDir myDirectory(userCropParameterProfilesDirPath());
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //Ignore directories
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if the filename ends in .xml try to load it into our layerSets listing
    if(myFileInfo.completeSuffix()=="xml")
    {
      //qDebug("Loading animalParameter: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaCropParameter myCropParameter;
      myCropParameter.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myCropParameter.name().isEmpty())
      {
        qDebug("CropParameter name was empty!");
        continue;
      }
      //qDebug("Adding " + myCropParameter.name());
      //qDebug(myCropParameter.toText().toLocal8Bit());
      if (myCropParameter.guid()==theGuid)
      {
        return myCropParameter;
      }
    }
  }
  LaCropParameter myCropParameter;
  return myCropParameter; //retrun a blank one since no match found

}


QStringList LaUtils::sortList(QStringList theList)
{
    //sort the taxon list alpabetically descending order
    theList.sort(); //this sorts ascending!
    //flip the sort order
    QStringList mySortedList;
    QStringList::Iterator myIterator= theList.end();
    while( myIterator!=theList.begin() )
    {
      myIterator--;
      mySortedList << *myIterator;
    }
    return mySortedList;
}

QStringList LaUtils::uniqueList(QStringList theList)
{
    //remove any duplicates from a sorted list
    QStringList myUniqueList;
    QString myLast = "";
    QStringListIterator myIterator( theList );
    while( myIterator.hasNext() )
    {
      QString myCurrent = myIterator.next();
      if (myCurrent!=myLast)
      {
        myUniqueList << myCurrent;
      }
      myLast=myCurrent;
    }
    return myUniqueList;
}

//return a string list of all the experiment files
QStringList LaUtils::getExperimentsList()
{
  QStringList myExperimentList;
  QSettings mySettings;
  QString myWorkDir = mySettings.value("dataDirs/dataDir",QDir::homePath()+QDir::separator()+".landuseAnalyst").toString()+
                      QString("/modelOutputs/");
  QDir myDirectory(myWorkDir);
  myDirectory.setFilter(QDir::Dirs | QDir::Files | QDir::NoSymLinks );
  //qDebug ("Current directory is: " +  myWorkDir.toAscii());
  QFileInfoList myList = myDirectory.entryInfoList();
  for (unsigned int i = 0; i < static_cast<unsigned int>(myList.size()); ++i)
  {
    QFileInfo myFileInfo = myList.at(i);
    //qDebug("Get ExperimentsList Scanning : " + myFileInfo.fileName().toLocal8Bit());
    if(myFileInfo.fileName() == "." ||myFileInfo.fileName() == ".." )
    {
      continue;
    }
    //if this is an empty dir, just skip it...
    if (myFileInfo.absoluteDir().count() < 1)
    {
      continue;
    }
    //todo - check that the file is a directory (it should be)

    //Now look in each dir under the workdir for the xml experiment file
    //the experiment file should be named <dir name>.xml
    QString myFile = myFileInfo.absolutePath() + QDir::separator()
                                 + myFileInfo.fileName() + QDir::separator()
                                 + myFileInfo.fileName() + ".xml";
    //qDebug("Get ExperimentsList Checking: " + myFile.toLocal8Bit());
    if (QFile::exists(myFile))
    {
      myExperimentList << myFile;
      //qDebug("Get ExperimentsList Adding: " + myFile.toLocal8Bit());
    }
  }
  return myExperimentList;
}

bool LaUtils::createTextFile(QString theFileName, QString theData)
{
  //create the txt file
  QFile myFile( theFileName );
  if ( myFile.open( QIODevice::WriteOnly ) )
  {
    QTextStream myQTextStream( &myFile );
    myQTextStream << theData;
  }
  else
  {
    return false;
  }
  myFile.close();
  return true ;
}

QString LaUtils::xmlEncode(QString theString)
{
  theString = theString.replace("<","&lt;");
  theString = theString.replace(">","&gt;");
  theString = theString.replace("&","&amp;");
  return theString;
}

QString LaUtils::xmlDecode(QString theString)
{
  theString = theString.replace("&lt;","<");
  theString = theString.replace("&gt;",">");
  theString = theString.replace("&amp;","&");
  return theString;
}

QString LaUtils::getStandardCss()
{
  QString myStyle = ".glossy{ background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565); color: white; padding-left: 4px; border: 1px solid #6c6c6c; }";
  myStyle += "body {background: white;}";
  myStyle += "h1 {font-size : 22pt; color: #0063F7; }";
  myStyle += "h2 {font-size : 18pt; color: #0063F7; }";
  myStyle += "h3 {font-size : 14pt; color: #0063F7; }";
  myStyle += ".cellHeader {color:#466aa5; font-size : 12pt;}";
  myStyle += ".parameterHeader {font-weight: bold;}";
  myStyle += ".largeCell {color:#000000; font-size : 12pt;}";
  myStyle += ".table {"
                    "  border-width: 1px 1px 1px 1px;"
                    "  border-spacing: 2px;"
                    "  border-style: solid solid solid solid;"
                    "  border-color: black black black black;"
                    "  border-collapse: separate;"
                    "  background-color: white;"
                    "}";
  return myStyle;
}

QString LaUtils::openGraphicFile()
{
  QString myHomePath = QDir::homePath();
  QString myFileName = QFileDialog::getOpenFileName(0, "Choose an image", myHomePath, "Images (*.png *.xpm *.jpg)");
  QFileInfo fi(myFileName);
  QString myName = fi.fileName();
  QString myDestinationFilePathName = userImagesDirPath() + myName;
  QFile::copy(myFileName, myDestinationFilePathName);
  return myDestinationFilePathName;
}

QString LaUtils::saveFile()
{
  QString myHomePath = QDir::homePath();
  QString myFileName = QFileDialog::getSaveFileName(0, "Choose a file name", userConversionTablesDirPath(), "*.csv");
  QFileInfo fi(myFileName);
  QString myName = fi.fileName();
  QString myDestinationFilePathName = userConversionTablesDirPath() + myName;
  return myDestinationFilePathName;
}
