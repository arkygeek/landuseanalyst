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
#ifndef LAMAINFORMFORM_H
#define LAMAINFORMFORM_H

//QT Includes
#include <QDialog>
#include <QHash>
//Local Includes
#include <ui_lamainformbase.h>
#include <lautils.h>
class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton
*/
class LaMainForm : public QDialog, private Ui::LaMainFormBase
{
  Q_OBJECT
  public:
    LaMainForm(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaMainForm();
  public slots:
  void on_horizontalSliderMeat_valueChanged(int theValue);
  void on_horizontalSliderDiet_valueChanged(int theValue);
  void on_horizontalSliderPlant_valueChanged(int theValue);
  void on_pushButtonDietBreakdown_clicked();
  void on_pushButtonRun_clicked();
  void on_pushButtonLoad_clicked();
  void on_pushButtonSave_clicked();
  void on_pbnNewPlant_clicked();
  void on_pbnNewAnimal_clicked();
  void on_pbnNewPlantParameter_clicked();
  void on_pbnNewAnimalParameter_clicked();
  void on_listWidgetAnimals_itemClicked(QListWidgetItem * theItem);
  void on_listWidgetPlants_itemClicked(QListWidgetItem * theItem);
  void on_listWidgetAnimalParameters_itemClicked(QListWidgetItem * theItem);
  void on_listWidgetPlantParameters_itemClicked(QListWidgetItem * theItem);
  /** Refresh the animals list, remembering which were checked
   * from before */
  void loadAnimals();
  /** Refresh the plants list, remembering which were checked
   * from before */
  void loadPlants();
  /** Refresh the animals list, remembering which were checked
   * from before */
  void loadAnimalParameters();
  /** Refresh the plants list, remembering which were checked
   * from before */
  void loadPlantParameters();

  private slots:
  void helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem);
  void writeMessage(QString theText);
  void writeDiet(QString theText);
  void makeCircle(int theX, int theY);
  void getArea(float theArea);
  void makeWalkCost(int theX, int theY);
  void makeEuclideanCost(int theX, int theY);
  void makePathDistanceCost(int theX, int theY);
  void writeMetaData(QString theValue);
  void doBaseCalculations();

  private:
    void readSettings();
    void writeSettings();
    LaUtils::AnimalMap mAnimalsMap;
    LaUtils::PlantMap mPlantsMap;
    LaUtils::AnimalParameterMap mAnimalParametersMap;
    LaUtils::PlantParameterMap mPlantParametersMap;
};

#endif //LAMAINFORM_H
