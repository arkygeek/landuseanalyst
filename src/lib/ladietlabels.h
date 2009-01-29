/***************************************************************************
 *   Copyright  (C) 2007 by: Jason Jorgenson   arkygeek@gmail.com           *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *    (at your option) any later version.                                   *
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
#ifndef LADIETLABELS_H
#define LADIETLABELS_H
#include <QString>
/**
 * This class represents all of the required data for setting labels in the diet tab.
 *
 * @author Jason Jorgenson
 */
class LaDietLabels{
public:
  LaDietLabels();

  ~LaDietLabels();

  // accessors
  float dairyMCalories() const;
  float cropMCalories() const;
  float animalMCalories() const;
  float wildAnimalMCalories() const;
  float wildPlantsMCalories() const;
  float dairyPortionPct() const;
  float tameMeatPortionPct() const;
  float cropsPortionPct() const;
  float wildAnimalPortionPct() const;
  float wildPlantsPortionPct() const;
  float plantsPortionPct() const;
  float animalPortionPct() const;
  float kiloCaloriesIndividualAnnual() const;
  float megaCaloriesSettlementAnnual() const;
  float dairySurplusMCalories() const;
  // mutators
  void setDairyMCalories (float theDairyMCalories);
  void setCropMCalories (float theCropMCalories);
  void setAnimalMCalories (float theAnimalMCalories);
  void setWildAnimalMCalories (float theWildAnimalMCalorie);
  void setWildPlantsMCalories (float theWildPlantsMCalories);
  void setDairyPortionPct (float theDairyPortionPct);
  void setTameMeatPortionPct (float theTameMeatPortionPct);
  void setCropsPortionPct (float theCropsPortionPct);
  void setWildAnimalPortionPct (float theWildAnimalPortionPct);
  void setWildPlantsPortionPct (float theWildPlantsPortionPct);
  void setPlantsPortionPct (float thePlantsPortionPct);
  void setAnimalPortionPct (float theAnimalPortionPct);
  void setKiloCaloriesIndividualAnnual (float theKCaloriesIndividualAnnual);
  void setMegaCaloriesSettlementAnnual (float theMCaloriesSettlementAnnua);
  void setDairySurplusMCalories (float theDairySurplusMCalories);
  private:
  float mDairyMCalories;
  float mCropMCalories;
  float mAnimalMCalories;
  float mWildAnimalMCalories;
  float mWildPlantsMCalories;
  float mDairyPortionPct;
  float mTameMeatPortionPct;
  float mCropsPortionPct;
  float mWildAnimalPortionPct;
  float mWildPlantsPortionPct;
  float mPlantsPortionPct;
  float mAnimalPortionPct;
  float mKiloCaloriesIndividualAnnual;
  float mMegaCaloriesSettlementAnnual;
  float mDairySurplusMCalories;
};

#endif
