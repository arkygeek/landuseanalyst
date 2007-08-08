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
#include <QString>
#include <QDomDocument>
#include <QDomElement>
#include "lagrassprocesslib.h"
#include "lautils.h"


LaGrassProcessLib::LaGrassProcessLib() : QObject()
{
  mCurrentArea = 0;
}
LaGrassProcessLib::~LaGrassProcessLib()
{

}

//copy constructor
//LaGrassProcessLib::LaGrassProcessLib(const LaGrassProcessLib& theGrassProcessLib)
//{
//  mCurrentArea=theGrassProcessLib.currentArea();
//}

//LaGrassProcessLib& LaGrassProcessLib::operator=(const LaGrassProcessLib& theGrassProcessLib)
//{
//  if (this == &theGrassProcessLib) return *this;   // Gracefully handle self assignment
//
//  mCurrentArea=theGrassProcessLib.currentArea();
//  return *this;
//}

  ///////////////
 // Accessors //
///////////////

int LaGrassProcessLib::currentArea() const
{
  return mCurrentArea;
}

  //////////////
 // Mutators //
//////////////

void LaGrassProcessLib::setCurrentArea(int theCurrentArea)
{
  mCurrentArea = theCurrentArea;
}


