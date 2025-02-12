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

#include "lafoodsource.h"

LaFoodSource::LaFoodSource()
{
}
LaFoodSource::~LaFoodSource()
{
}

  //accessors

int LaFoodSource::grain() const
{
  return mGrain;
}
int LaFoodSource::fodder() const
{
  return mFodder;
}
int LaFoodSource::days() const
{
  return mDays;
}
bool LaFoodSource::used() const
{
 return mUsed; 
}
QString LaFoodSource::cropGuid() const
{
 return mCropGuid; 
}
  //mutators

void LaFoodSource::setGrain(int theValue)
{
  mGrain = theValue;
}
void LaFoodSource::setFodder(int theValue)
{
  mFodder = theValue;
}
void LaFoodSource::setDays(int theValue)
{
  mDays = theValue;
}
void LaFoodSource::setUsed(bool theBool)
{
  mUsed = theBool;
}
void LaFoodSource::setCropGuid(QString theCropGuid)
{
  mCropGuid = theCropGuid;
}
