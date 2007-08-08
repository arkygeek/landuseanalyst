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


#ifndef LAGRASSPROCESSLIB_H
#define LAGRASSPROCESSLIB_H

#include <QString>
#include <QMap>
#include <QObject>
/**
  * A class for grass analysis
  * @author Jason Jorgenson, Tim Sutton
  */

class LaGrassProcessLib : public QObject
{
  Q_OBJECT
  public:
    /** Constructor . */
    LaGrassProcessLib();
    /** Desctructor . */
    ~LaGrassProcessLib();

  ///////////////
 // Accessors //
///////////////
    /** Return the Current Area */
    int currentArea() const;

  //////////////
 // Mutators //
//////////////
    /** Set the Current Area
     * @see currentArea()
     */
    void setCurrentArea(int theCurrentArea);

  signals:
    /** Send log info to any listeners.
     * @param QString the message to be logged.
     */

  private:
    int mCurrentArea;
};

#endif //LAGRASSPROCESSLIB_H
