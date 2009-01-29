/***************************************************************************
 *   Copyright (C) 2007 by: Jason Jorgenson   arkygeek@gmail.com           *
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
#include "ladietlabels.h"

LaDietLabels::LaDietLabels()
{
}

LaDietLabels::~LaDietLabels()
{
}

  //accessors

float LaDietLabels::dairyMCalories() const
{
  return mDairyMCalories;
}
float LaDietLabels::cropMCalories() const
{
  return mCropMCalories;
}
float LaDietLabels::animalMCalories() const
{
  return mAnimalMCalories;
}
float LaDietLabels::wildAnimalMCalories() const
{
  return mWildAnimalMCalories;
}
float LaDietLabels::wildPlantsMCalories() const
{
  return mWildPlantsMCalories;
}
float LaDietLabels::dairyPortionPct() const
{
  return mDairyPortionPct;
}
float LaDietLabels::tameMeatPortionPct() const
{
  return mTameMeatPortionPct;
}
float LaDietLabels::cropsPortionPct() const
{
  return mCropsPortionPct;
}
float LaDietLabels::wildAnimalPortionPct() const
{
  return mWildAnimalPortionPct;
}
float LaDietLabels::wildPlantsPortionPct() const
{
  return mWildPlantsPortionPct;
}
float LaDietLabels::plantsPortionPct() const
{
  return mPlantsPortionPct;
}
float LaDietLabels::animalPortionPct() const
{
  return mAnimalPortionPct;
}
float LaDietLabels::kiloCaloriesIndividualAnnual() const
{
  return mKiloCaloriesIndividualAnnual;
}
float LaDietLabels::megaCaloriesSettlementAnnual() const
{
  return mMegaCaloriesSettlementAnnual;
}
float LaDietLabels::dairySurplusMCalories() const
{
  return mDairySurplusMCalories;
}

  //mutators

void LaDietLabels::setDairyMCalories(float theDairyMCalories)
{
  mDairyMCalories = theDairyMCalories;
}
void LaDietLabels::setCropMCalories(float theCropMCalories)
{
  mCropMCalories = theCropMCalories;
}
void LaDietLabels::setAnimalMCalories(float theAnimalMCalories)
{
  mAnimalMCalories = theAnimalMCalories;
}
void LaDietLabels::setWildAnimalMCalories(float theWildAnimalMCalorie)
{
  mWildAnimalMCalories = theWildAnimalMCalorie;
}
void LaDietLabels::setWildPlantsMCalories(float theWildPlantsMCalories)
{
  mWildPlantsMCalories = theWildPlantsMCalories;
}
void LaDietLabels::setDairyPortionPct(float theDairyPortionPct)
{
  mDairyPortionPct = theDairyPortionPct;
}
void LaDietLabels::setTameMeatPortionPct(float theTameMeatPortionPct)
{
  mTameMeatPortionPct = theTameMeatPortionPct;
}
void LaDietLabels::setCropsPortionPct(float theCropsPortionPct)
{
  mCropsPortionPct = theCropsPortionPct;
}
void LaDietLabels::setWildAnimalPortionPct(float theWildAnimalPortionPct)
{
  mWildAnimalPortionPct = theWildAnimalPortionPct;
}
void LaDietLabels::setWildPlantsPortionPct(float theWildPlantsPortionPct)
{
  mWildPlantsPortionPct = theWildPlantsPortionPct;
}
void LaDietLabels::setPlantsPortionPct(float thePlantsPortionPct)
{
  mPlantsPortionPct = thePlantsPortionPct;
}
void LaDietLabels::setAnimalPortionPct(float theAnimalPortionPct)
{
  mAnimalPortionPct = theAnimalPortionPct;
}
void LaDietLabels::setKiloCaloriesIndividualAnnual(float theKiloCaloriesIndividualAnnual)
{
  mKiloCaloriesIndividualAnnual = theKiloCaloriesIndividualAnnual;
}
void LaDietLabels::setMegaCaloriesSettlementAnnual(float theMegaCaloriesSettlementAnnua)
{
  mMegaCaloriesSettlementAnnual = theMegaCaloriesSettlementAnnua;
}
void LaDietLabels::setDairySurplusMCalories(float theDairySurplus)
{
  mDairySurplusMCalories = theDairySurplus;
}
