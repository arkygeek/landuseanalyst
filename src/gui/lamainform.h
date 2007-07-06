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
#include <QPair>
//Local Includes
#include <ui_lamainformbase.h>
#include <lautils.h>
#include <la.h>
#include <laanimal.h>
#include <laanimalparameter.h>


//forward declarations
class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaMainForm : public QDialog, private Ui::LaMainFormBase
{
  Q_OBJECT;
  public:
    LaMainForm(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaMainForm();
  public slots:
    void on_horizontalSliderMeat_valueChanged(int theValue);
    void on_horizontalSliderDiet_valueChanged(int theValue);
    void on_horizontalSliderCrop_valueChanged(int theValue);
    void on_pushButtonRun_clicked();
    void on_pushButtonLoad_clicked();
    void on_pushButtonSave_clicked();
    void on_pbnNewCrop_clicked();
    void on_pbnNewAnimal_clicked();
    void on_pbnNewCropParameter_clicked();
    void on_pbnNewAnimalParameter_clicked();
    void on_spinBoxDailyCalories_valueChanged(int theValue);
    void on_pbnFallow_clicked();
    void on_cbDebug_clicked();
    /** Refresh the animals list, remembering which were checked
     * from before */
    void loadAnimals();
    /** Refresh the crops list, remembering which were checked
     * from before */
    void loadCrops();
    void setDietLabels();
    /** Slot to log any messages from classes we are listening
     * to.
     * @param QString containing the message.
     */
    void logMessage(QString theString);
  private slots:
    void helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem);
    void writeResults(QString theText);
    void cropCalcClicked(QListWidgetItem * thepCurrentItem, QListWidgetItem * thepOldItem);
    void animalCalcClicked(QListWidgetItem * thepCurrentItem, QListWidgetItem * thepOldItem);
    void animalCellClicked(int theRow, int theColumn);
    void animalCellChanged(int theRow, int theColumn);
    void cropCellClicked(int theRow, int theColumn);
    void cropCellChanged(int theRow, int theColumn);
  private:
    void readSettings();
    void writeSettings();
    // A simple helper / debug function to print the state of
    // animals and crops maps
    void debugChecks();
    void printCropsAndAnimals();
    /* Show html report in the animal tab for the animal and its associated param */
    void showAnimalDefinitionReport(LaAnimal &theAnimal, LaAnimalParameter &theAnimalParamter);
    bool setComboToDefault(QComboBox * thepCombo, QString theDefault);
    //    <animal guid <enabled, animalparamters guid>>
    LaTripleMap mAnimalsMap;
    LaTripleMap mCropsMap;
    int mCommonGrazingLandFoodValue;
};

#endif //LAMAINFORM_H
