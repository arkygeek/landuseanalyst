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

#include "lagrass.h"
#include "lautils.h"
#include "la.h"
//#include "lagrassprocess.h"

#include <QString>
#include <QStringList>
#include <QSettings>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QDebug>


LaGrass::LaGrass() : QObject()
{
}
LaGrass::~LaGrass()
{

}

QStringList LaGrass::getMapsetList()
{
  QString myCommand = "g.mapsets";
  QStringList myArguments;
  myArguments << "-l";
  //run the command ignoring error logs
  QString myResult = runCommand(myCommand,myArguments);
  myResult = myResult.simplified();
  QStringList myList = myResult.split(QRegExp("\\s+")); // splits on white space
  return myList;
}

QStringList LaGrass::getRasterList(QString theMapset, bool thePrependMapsetFlag /*=true */)
{
  QString myCommand = "g.list";
  QStringList myArguments;
  myArguments << "type=rast";
  myArguments << "mapset=" + theMapset;
  //run the command ignoring error logs
  QString myResult = runCommand(myCommand,myArguments);
  //check for no files
  if (myResult.contains("no raster files available"))
  {
    //return an empty list
    return QStringList();
  }
  //strip off grass decoration crap...
  myResult.replace("raster files available in mapset " + theMapset + ":","");
  myResult = myResult.simplified();
  QStringList myList = myResult.split(QRegExp("\\s+")); // splits on white space
  QStringList myFinalList;
  //prepend the mapset name to each raster name
  if (thePrependMapsetFlag)
  {
    QStringListIterator myIterator(myList);
    while (myIterator.hasNext())
    {
      QString myString = myIterator.next();
      myFinalList << myString + "@" + theMapset;
    }
  }
  return myFinalList;
}

bool LaGrass::copyMap(QString theOriginalRaster, QString theCopy)
{
  QString myCommand = "g.copy";
  QStringList myArguments;
  myArguments << "rast=" + theOriginalRaster + "," + theCopy;
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());
  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  qDebug(myResult.toLocal8Bit());
  if (myErrorLog.isEmpty())
  {
    return true;
  }
  else
  {
    return false;
  }
}

bool LaGrass::createFrictionMap(QString theBaseRaster,QString theOutputRaster)
{
  //r.mapcalc "laFrictionMap = if(isnull(laDEM), null(), 1)"
  QString myCommand = "r.mapcalc";
  QStringList myArguments;
  myArguments << " \"" + theOutputRaster + " = if(isnull(" + theBaseRaster + "), null(), 1)\"";
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());
  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  qDebug(myResult.toLocal8Bit());
  if (myErrorLog.isEmpty())
  {
    return true;
  }
  else
  {
    return false;
  }
}

bool LaGrass::createMask(QString theCostSurface, QString theMaskRaster)
{
  //r.mapcalc "laFrictionMap = if(isnull(laDEM), null(), 1)"
  QString myCommand = "r.mapcalc";
  QStringList myArguments;
  myArguments << " tmpMask=" + theCostSurface + "*" + theMaskRaster;
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());
  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  qDebug(myResult.toLocal8Bit());
  if (myErrorLog.isEmpty())
  {
    return true;
  }
  else
  {
    return false;
  }
}

float LaGrass::getArea(QString theLayerName)
{
  logMessage("method ==> void LaGrass::getArea(float theArea)");
  //r.stats -a -n fs=,
  QString myCommand = "r.stats";
  QStringList myArguments;
  myArguments << "-a" << "-n" << "fs=," << "input="+theLayerName;
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());
  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  qDebug(myResult.toLocal8Bit());
  if (myErrorLog.isEmpty())
  {
    return 0;
  }
  else
  {
    qDebug() << "myResult: " << myResult;
    myResult = myResult.simplified();
    qDebug() << "myResult.simplified(): " << myResult;
    //put each line of output into a list entry
    QStringList myList = myResult.split(QRegExp("\\s+"));
    qDebug() << "myList: " << myList;
   // if (myList.count() < 1)
    //{
      //row should be like 3,32323 (class,area)
      QStringList myList2 = myList.at(1).split((","));
      qDebug() << "myList2: " << myList2;
      //if (myList2.count() < 1)
      //{
        //get only area
        float myArea = myList2.at(1).toFloat() * 0.0001; // adjust for hectares
        qDebug() << "Area (returnValue): " << myArea;
        return myArea;
      //}
    //}
  }
  return 0;
}

bool LaGrass::makeWalkCost(int theX, int theY, QString theDEM)
{
  //logMessage("method ==> void LaGrass::makeWalkCost(int theX, int theY)");
  //r.walk max_cost=20000 elevation=dem_patched_filled@PERMANENT friction=theFrictionMap output=rwalkResultsSlopeMax20kFMap coordinate=744800,3611100 percent_memory=100 nseg=4 walk_coeff=0.72,6.0,1.9998,-1.9998 lambda=0 slope_factor=-0.2125 -k
  //qDebug() << "Coordinates: " << theX << "," << theY;
  QString myElevationMap=theDEM;
  QString myFrictionMap=theDEM;

  QString myCommand = "r.walk";
  QStringList myArguments;
  myArguments << "max_cost=18000"
              << "elevation=" + myElevationMap
              << "friction=" + myFrictionMap
              << "output=laWalkCost"
              << "coordinate=" + QString::number(theX) + "," + QString::number(theY)
              << "percent_memory=100"
              << "nseg=4"
              << "walk_coeff=0.72,6.0,1.9998,-1.999"
              << "lambda=0"
              << "slope_factor=-0.2125"
              << "-k"
              << "--overwrite";
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());

  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  //qDebug(myResult.toLocal8Bit());
  //LaGrassProcess myLaGrassProcess;
  if (myErrorLog.isEmpty())
  {
    return true;
  }
  else
  {
    return false;
  }
}

void LaGrass::makeEuclideanCost(int theX, int theY)
{
  logMessage("method ==> void LaGrass::makeEuclideanCost(int theX, int theY)");
}

void LaGrass::makePathDistanceCost(int theX, int theY)
{
  logMessage("method ==> void LaGrass::makePathDistanceCost(int theX, int theY)");
}

void LaGrass::writeMetaData(QString theValue)
{
  logMessage("method ==> void LaGrass::writeMetaData(QString theValue)");
}

bool LaGrass::reclass(QString theRaster, int theMax)
{
  qDebug() << "reclass invoked";
  //r.mapcalc "laFrictionMap = if(isnull(laDEM), null(), 1)"
  QString myCommand = "r.mapcalc";
  QStringList myArguments;
  myArguments << " laCostMapReclassed=if(" + theRaster + "<" + QString::number(theMax) + ", 1, 0)";
  qDebug(myCommand.toLocal8Bit() + myArguments.join(" ").toLocal8Bit());
  QString myErrorLog;
  QString myResult = runCommand(myCommand,myArguments,myErrorLog);
  qDebug(myResult.toLocal8Bit());
  if (myErrorLog.isEmpty())
  {
    return true;
  }
  else
  {
    return false;
  }
  /*#ifdef Q_OS_MACX
  QString myProgram = "/Applications/GRASS.app/Contents/Resources/bin/r.reclass";
  #else
  QString myProgram = "/usr/lib/grass/bin/r.reclass";
  #endif
  //windows users can wallow in self pity for now...

  QStringList myArguments;
  myArguments << " input=" + theRaster << "output=laCostMapReclassed";

  QProcess myProcess;
     myProcess.start(myProgram, myArguments);
     if (!myProcess.waitForStarted())
      {
      qDebug() << "Process Didn't Start";
        return false;
      }

     QString myPipedText = "0 thru " + QString::number(theMax) + " = 1";
     qDebug() << "myPipedText: " << myPipedText;
     myProcess.write(myPipedText.toUtf8());
     myProcess.closeWriteChannel();

    if (!myProcess.waitForFinished())
    {
      qDebug() << "something not working so good in wait for finished";
      return false;
    }
     QByteArray result = myProcess.readAll();
      qDebug() << " working good";

     return true;*/
/*   QProcess gzip;
     gzip.start("gzip", QStringList() << "-c");
     if (!gzip.waitForStarted())
         return false;

     gzip.write("Qt rocks!");
     gzip.closeWriteChannel();

     if (!gzip.waitForFinished())
         return false;

     QByteArray result = gzip.readAll();
*/


}

//
// Utility functions
//

void LaGrass::logMessage(QString theMessage)
{
  emit message(theMessage);
}

QString LaGrass::runCommand(QString theCommand,
    QStringList theArguments,
    QString &theErrorLog /*=""*/)
{
  #ifdef Q_OS_MACX
  QString myProgram = "/Applications/GRASS.app/Contents/Resources/bin/" + theCommand;
  #else
  QString myProgram = "/usr/lib/grass/bin/" + theCommand;
  #endif
  //windows users can wallow in self pity for now...

  QProcess myProcess;
  myProcess.start(myProgram, theArguments);

  if (!myProcess.waitForStarted())
  {
    logMessage("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1))
  {
  }

  QString myLog;
  //log
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myLog.append(myArray);
  //errors
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  theErrorLog.append(myArray);
  // get rid of some grass decorations...
  qDebug() <<"GRASS> " << theCommand << theArguments;
  qDebug() <<"Results: " << myLog;
  myLog.replace("----------------------------------------------","");

  return myLog;
}
QString LaGrass::runCommand(QString theCommand,
    QStringList theArguments)
{
  QString myErrors;
  QString myLog = runCommand(theCommand, theArguments, myErrors);
  return myLog;
}

// reclass
