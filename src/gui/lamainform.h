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
class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton
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
    void on_pushButtonDietBreakdown_clicked();
    void on_pushButtonRun_clicked();
    void on_pushButtonLoad_clicked();
    void on_pushButtonSave_clicked();
    void on_pbnNewCrop_clicked();
    void on_pbnNewAnimal_clicked();
    void on_pbnNewCropParameter_clicked();
    void on_pbnNewAnimalParameter_clicked();

    /** Refresh the animals list, remembering which were checked
     * from before */
    void loadAnimals();
    /** Refresh the crops list, remembering which were checked
     * from before */
    void loadCrops();

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
    void animalCellClicked(int theRow, int theColumn);
    void cropCellClicked(int theRow, int theColumn);
  private:
    void readSettings();
    void writeSettings();
    bool setComboToDefault(QComboBox * thepCombo, QString theDefault);
    LaUtils::AnimalParameterMap mAnimalParametersMap;
    LaUtils::CropParameterMap mCropParametersMap;
    //    <animal guid <enabled, animalparamters guid>>
    QMap <QString,QPair<bool,QString> > mAnimalsMap;
    QMap <QString,QPair<bool,QString> > mCropsMap;
};

#endif //LAMAINFORM_H
