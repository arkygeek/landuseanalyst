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
#include "lagrass.h"
#include "la.h"

LaGrassProcessLib::LaGrassProcessLib() : QObject()
{

}
LaGrassProcessLib::~LaGrassProcessLib()
{

}

void LaGrassProcessLib::analyseModel()
{

  // get the area targets


    ///////////////////////
   // Make Cost Surface //
  ///////////////////////

  // r.mapcalc "TimeOnlyFrictionMap=if(isnull(DEM), null(), 1)"
  // r.walk max_cost=20000 elevation=dem_patched_filled@PERMANENT friction=theFrictionMap output=rwalkResultsSlopeMax20kFMap coordinate=744800,3611100 percent_memory=100 nseg=4 walk_coeff=0.72,6.0,1.9998,-1.9998 lambda=0 slope_factor=-0.2125 -k


    ////////////////////
   // find the land! //
  ////////////////////

  // binary search used

   // function:
   //   Searches sortedArray[first]..sortedArray[last] for key.
   // returns: index of the matching element if it finds key,
   //         otherwise  -(index where it could be inserted)-1.
   // parameters:
   //   sortedArray in  array of sorted (ascending) values.
   //   first, last in  lower and upper subscript bounds
   //   key         in  value to search for.
   // returns:
   //   index of key, or -insertion_position -1 if key is not
   //                 in the array. This value can easily be
   //                 transformed into the position to insert it.
   int myFirst = 0;
   int myLast=18000;
   int myAreaTarget = 500; // change this to real value
   LandFound mySearchStatus = NotEnough;
   int myCurrentlyContainedArea = 0;

   while (myFirst <= myLast)
  {
    int myMid = (myFirst + myLast) / 2;  // compute mid point.
    // reclass with 1 to midpoint and null beyond and then check results

    // find out if the contained area is within acceptable range
    mySearchStatus = getSearchStatus(myCurrentlyContainedArea, myAreaTarget);

    switch (mySearchStatus)
    {
      case NotEnough:
            myFirst = myMid + 1;  // repeat search in top half.
            break;;
      case TooMuch:
            myLast = myMid - 1; // repeat search in bottom half.
            break;
      case FoundTarget:
            // found it. break out of loop /////
            myFirst = myLast+1;
            break;
    }

  }
}

LandFound LaGrassProcessLib::getSearchStatus(int theCurrentlyContainedArea, int theAreaTarget)
{
  LandFound myStatus;
  int myPrecision=5;  //get the real value for precision
  float myAcceptableRange=(theAreaTarget*myPrecision*0.01)/2.0;
  float myMinimumAcceptable = theAreaTarget - myAcceptableRange;
  float myMaximumAcceptable = theAreaTarget + myAcceptableRange;

  if (theCurrentlyContainedArea >= myMinimumAcceptable)
    {
      myStatus = (theCurrentlyContainedArea <= myMaximumAcceptable) ? FoundTarget : TooMuch;
    }
  else
    {
      myStatus = NotEnough;
    }

  return myStatus;
}
