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
#ifndef LAFOODSOURCE_H
#define LAFOODSOURCE_H
#include <QString>

/**
	@author Jason Jorgenson
*/
class LaFoodSource{
public:
  LaFoodSource();

  ~LaFoodSource();

    // accessors
  int grain() const;
  int fodder() const;
  int days() const;
  bool used() const;
  QString cropGuid() const;
    // mutators
  void setGrain(int theValue);
  void setFodder(int theValue);
  void setDays(int theValue);
  void setUsed(bool theBool);
  void setCropGuid(QString theCropGuid);
  private:
  int mGrain;
  int mFodder;
  int mDays;
  bool mUsed;
  QString mCropGuid;
};

#endif
