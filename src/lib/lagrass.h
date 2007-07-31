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

#ifndef LAGRASS_H
#define LAGRASS_H

#include <QString>
#include <QMap>
#include <QObject>
/**
  * A class to wrap various grass functions
  * @author Tim Sutton, Jason Jorgenson
  */

class LaGrass : public QObject
{
  Q_OBJECT;
  public:
    /** Constructor . */
    LaGrass();
    /** Desctructor . */
    ~LaGrass();
    /** This is the main wrapper function - most others
     * will call it to actually invoke the grass engine.
     * @param QString theCommand - a single command name e.g. g.list
     * @param QString theArguments - a stringlist of paramters
     * e.g.
     * QStringList myArgs;
     * myArgs << "type=rast" << "type=vect";
     * @param &QString theErrorLog - a string passed by reference. 
     * On completion, any errors
     * from stderr will have been placed in this string.
     * @return QString - verbatim output of the command as
     * returned by GRASS. The calling function will be responsible
     * for parsing that output.
     */
     QString runCommand(QString theCommand, 
                        QStringList theArguments,
                        QString &theErrorLog);
     /** Overloaded version of above command that needs no
      * log parameter.
     * @param QString theCommand - a single command name e.g. g.list
     * @param QString theArguments - a stringlist of paramters
     * e.g.
     * QStringList myArgs;
     * myArgs << "type=rast" << "type=vect";
     * @return QString - verbatim output of the command as
     * returned by GRASS. The calling function will be responsible
     * for parsing that output.
     */
     QString runCommand(QString theCommand, 
                        QStringList theArguments);
    /** Get a list of grass rasters from the 
     * PERMANENT and users mapset.
     * @param bool thePrependMapsetFlag. Optional paramter which
     * defaults to true. Adds the mapset name in front of each layer
     * e.g.
     * PERMANENT.dem
     * @return QStringList of layer names.
     */
    QStringList getRasterList(QString theMapset, bool thePrependMapsetFlag=true);
    
    void makeCircle(int theX, int theY);
    void getArea(QString theLayerName,float theArea);
    void makeWalkCost(int theX, int theY);
    void makeEuclideanCost(int theX, int theY);
    void makePathDistanceCost(int theX, int theY);
    void writeMetaData(QString theValue);
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
};
#endif //LAGRASS_H


