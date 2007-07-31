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


QStringList LaGrass::getRasterList(QString theMapset, bool thePrependMapsetFlag /*=true */)
{
  QString myCommand = "g.list";
  QStringList myArguments;
  myArguments << "type=rast";
  myArguments << "mapset=" + theMapset;
  //first test with no error log param
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

void LaGrass::getArea(QString theLayerName, float theArea)
{
  logMessage("method ==> void LaGrass::getArea(float theArea)");

  #ifdef Q_OS_MACX
  QString myProgram = "/Applications/GRASS.app/Contents/Resources/bin/r.stats";
  #else
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  #endif
  QStringList myArgs;
  myArgs << theLayerName;
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);

  if (!myProcess.waitForStarted())
  {
    logMessage("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1))
  {
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

void LaGrass::makeWalkCost(int theX, int theY)
{
  logMessage("method ==> void LaGrass::makeWalkCost(int theX, int theY)");
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

void LaGrass::makeCircle(int theX, int theY)
{
  logMessage("method ==> void LaGrass::makeCircle(int theX, int theY");
  // to verify this worked do
  //    d.rast
  //    and check in the pull downlist (if your eyes dont fall out looking at those fonts)
  //    to remove the file again do:
  //    g.remove rast=circle

  /*
     logMessage("Making crop circle...tweeedee treedee");
     QString myProgram = "/usr/lib/grass/bin/r.circle";
     QStringList myArgs;
     myArgs << "-b"
     << "output=circle"
     <<  "coordinate=744800,3611100"
     << "max=500"
     << "--overwrite";
     */
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "landuse";
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

