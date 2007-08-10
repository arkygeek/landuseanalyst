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


#include <QString>
#include <QStringList>
#include <QSettings>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>

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
  QStringList myList = myResult.split(QRegExp("\\s+"));
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
  QStringList myList = myResult.split(QRegExp("\\s+"));
  QStringList myFinalList;
  //prepend the mapset name to each raster name
  if (thePrependMapsetFlag)
  {
    QStringListIterator myIterator(myList);
    while (myIterator.hasNext())
    {
      QString myString = myIterator.next();
      myFinalList << theMapset + "." + myString;
    }
  }
  return myFinalList;
}
bool LaGrass::createFrictionMap(QString theBaseRaster,QString theOutputRaster)
{
  //r.mapcalc "laFrictionMap = if(isnull(laDEM), null(), 1)"
  QString myCommand = "r.mapcalc";
  QStringList myArguments;
  myArguments << "\"" + theOutputRaster + " = if(isnull(" + theBaseRaster + "), null(), 1)\"";
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
  QString myCommand = "r.stats -a -n fs=,";
  QStringList myArguments;
  myArguments << "-a" << "-n" << "fs=," << theLayerName;
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
    myResult = myResult.simplified();
    //put each line of output into a list entry
    QStringList myList = myResult.split(QRegExp("\\s+"));
    if (myList.count() < 1)
    {
      //row should be like 3,32323 (class,area)
      QStringList myList2 = myList.at(0).split((","));
      if (myList2.count() < 1)
      {
        //get only area
        return myList.at(1).toFloat();
      }
    }
  }
  return 0;
}

bool LaGrass::makeWalkCost(int theX, int theY)
{
  logMessage("method ==> void LaGrass::makeWalkCost(int theX, int theY)");
  //r.walk max_cost=20000 elevation=dem_patched_filled@PERMANENT friction=theFrictionMap output=rwalkResultsSlopeMax20kFMap coordinate=744800,3611100 percent_memory=100 nseg=4 walk_coeff=0.72,6.0,1.9998,-1.9998 lambda=0 slope_factor=-0.2125 -k
  QString myElevationMap="", myFrictionMap="";

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
              << "-k";
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

void LaGrass::reclass(QString theRaster, int theMax)
{
  QString myProgram = "/usr/lib/grass/bin/r.reclass";
  QStringList myArgs;
  myArgs << "input=" + theRaster
         << "output=laCostMapReclassed"
         << "\"0 thru " + QString::number(theMax) + " = 1\"";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);
  if (!myProcess.waitForStarted()) {
    logMessage("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1)) {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  logMessage(myString.toLocal8Bit());

  logMessage("The process completed");
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

