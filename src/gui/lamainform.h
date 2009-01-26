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
#ifndef mCommonGrazingLandValue
#define mCommonGrazingLandValue

  //QT Includes
#include <QDialog>
#include <QHash>
#include <QPair>
#include <QDebug>
  //Local Includes
#include <ui_lamainformbase.h>
#include <lautils.h>
#include <la.h>
#include <laanimal.h>
#include <laanimalparameter.h>
#include "ladietlabels.h"

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
  /**
    * The Main form gui of LA.  Sets up the required clot connections
    * as well as initializing the GUI.
    * @param parent
    * @param fl
    */
    LaMainForm(QWidget* parent = 0, Qt::WFlags fl = 0 );
    /**
     * No idea what to put here
     */
    ~LaMainForm();
  public slots:
    double totalWeightFromLinearGrowth(float theDaysToGain, float theGainPerDay);
    void on_sliderMeat_valueChanged(int theValue);
    void on_cboxIncludeDairy_clicked(bool theBool);
    void on_cboxBaseOnPlants_clicked(bool theBool);
    void on_cboxLimitDairy_clicked(bool theBool);
    void on_sliderDiet_valueChanged(int theValue);
    void on_sbDairyUtilisation_valueChanged(int theValue);
    void on_sliderCrop_valueChanged(int theValue);
    QMap <QString, QString> getSelectedCrops();
    QPair <int, int> getSiteCoordinates();
    LaTripleMap getAvailableCrops();
    QString getMatchingCropParameterGuid(QString theCropGuid);
    QString getMatchingAnimalParameterGuid(QString theAnimalGuid);
    QString getDEM();
    void on_pushButtonRun_clicked();
    void on_pushButtonLoad_clicked();
    void on_pushButtonSave_clicked();
    void on_pbnNewCrop_clicked();
    void on_pbnNewAnimal_clicked();
    void on_pbnNewCropParameter_clicked();
    void on_pbnNewAnimalParameter_clicked();
    void on_sbDailyCalories_valueChanged(int theValue);
    void on_pbnFallow_clicked();
    void on_cbDebug_clicked();
    void on_cboMapSet_currentIndexChanged();
    /** Refresh the animals list, remembering which were checked
     * from before */
    void loadAnimals();
    /** Refresh the crops list, remembering which were checked
     * from before */
    void loadCrops();
    /**
     * Set's the model.  All data comes from the mainForm except for the map
     * of crops and animals which are being used. 
     */
    void setModel();
    void setDietLabels();
    /** Slot to log any messages from classes we are listening
     * to.
     * @param QString containing the message.
     */
    void logMessage(QString theString);
  private slots:

      //Rene Belloq: You and I are very much alike. Archeology is our religion,
      // yet we have both fallen from the pure faith. Our methods have not differed
      // as much as you pretend. I am but a shadowy reflection of you. It would take
      // only a nudge to make you like me. To push you out of the light.
      //Indiana Jones: Now you're getting nasty.

    void helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem);
    void writeResults(QString theText);
    void cropCalcClicked(QListWidgetItem * thepCurrentItem, QListWidgetItem * thepOldItem);
    void animalCalcClicked(QListWidgetItem * thepCurrentItem, QListWidgetItem * thepOldItem);
    void animalCellClicked(int theRow, int theColumn);
    void animalCellChanged(int theRow, int theColumn);
    void cropCellClicked(int theRow, int theColumn);
    void cropCellChanged(int theRow, int theColumn);
    private:

    /**
     * Restore controls to their last used values
     */
    void readSettings();
    void writeSettings();
      // A simple helper / debug function to print the state of
      // animals and crops maps
    void debugChecks();
    void printCropsAndAnimals();
    /* Show html report in the animal tab for the animal and its associated param */
    void showAnimalDefinitionReport(LaAnimal &theAnimal, LaAnimalParameter &theAnimalParamter);
    void showCropDefinitionReport(LaCrop &theCrop, LaCropParameter &theCropParamter);
    bool setComboToDefault(QComboBox * thepCombo, QString theDefault);
      //    <animal guid <enabled, animalparamters guid>>
    LaTripleMap mAnimalsMap;
    LaTripleMap mCropsMap;
    double mWeightCounter;
    QMap <QString,QString> mSelectedAnimalsMap;
    QMap <QString,QString> mSelectedCropsMap;
};

#endif   //LAMAINFORM_H
