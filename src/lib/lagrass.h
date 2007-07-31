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
    //
    // Grass functions
    //
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


