#include "lautils.h"
#include "laanimal.h"
#include "laplant.h"
//#include "laanimalparameter.h"
//#include "laplantparameter.h"

#include <QApplication>
#include <QDir>
#include <QFile>
#include <QPluginLoader>
#include <QSettings>
#include <QString>
#include <QStringList>
#include <QVector>
#include <QtXml>
#ifdef Q_OS_MACX
//for getting app bundle path
#include <ApplicationServices/ApplicationServices.h>
#endif


/*
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

const QString LaUtils::userAnimalParametersDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"animalParameters"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

const QString LaUtils::userPlantProfilesDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"plantProfiles"+QDir::separator();
  QDir().mkpath(myPath);
  return myPath;
}

const QString LaUtils::userPlantParametersDirPath()
{
  //alg profiles are always saved in the users home dir under .landuseAnalyst/
  QString myPath = QDir::homePath() + QString("/.landuseAnalyst/") +
    QDir::separator()+"plantParameters"+QDir::separator();
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
      qDebug("Loading animal: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaAnimal myAnimal;
      myAnimal.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myAnimal.name().isEmpty())
      {
        qDebug("Animal name was empty!");
        continue;
      }
      qDebug("Adding " + myAnimal.name());
      //qDebug(myAnimal.toText().toLocal8Bit());
      myMap[myAnimal.guid()]=myAnimal;
    }
  }
  return myMap;
}

LaUtils::PlantMap LaUtils::getAvailablePlants()
{
  LaUtils::PlantMap myMap;
  QDir myDirectory(userPlantProfilesDirPath());
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
      qDebug("Loading plant: " + myList.at(i).absoluteFilePath().toLocal8Bit());
      LaPlant myPlant;
      myPlant.fromXmlFile(myFileInfo.absoluteFilePath());
      if (myPlant.name().isEmpty())
      {
        qDebug("Plant name was empty!");
        continue;
      }
      qDebug("Adding " + myPlant.name());
      myMap[myPlant.guid()]=myPlant;
      //qDebug(myPlant.toText().toLocal8Bit());
    }
  }
  return myMap;
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
