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
#ifndef LAANIMALPARAMETERMANAGER_H
#define LAANIMALPARAMETERMANAGER_H

//QT Includes
#include <QDialog>
//Local Includes
#include <ui_laanimalparametermanagerbase.h>
#include <laanimalparameter.h>
#include <lautils.h>
#include <QSpinBox>

class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaAnimalParameterManager : public QDialog, private Ui::LaAnimalParameterManagerBase
{
  Q_OBJECT
  public:
    LaAnimalParameterManager(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaAnimalParameterManager();

  public slots:
    //void on_pushButtonLoad_clicked();
    //void on_pushButtonSave_clicked();

  private slots:
      void cellClicked(int theRow, int theColumn);
      void showAnimalParameter();
      void on_toolCopy_clicked();
      void on_toolNew_clicked();
      void on_toolDelete_clicked();
      void on_pbnApply_clicked();
      void resizeEvent(QResizeEvent*);



  private:
      void refreshAnimalParameterTable(QString theGuid=0);
      void selectAnimalParameter(QString theFileName);

      LaUtils::AnimalParameterMap mAnimalParameterMap;
      LaUtils::CropMap mCropMap;
      LaAnimalParameter mAnimalParameter;
      LaFoodSourceMap mFoodSourceMap;
      void readSettings();
      void writeSettings();
      void setFallowComboBox();
      void populateFodder();
      /** @TODO move this into LaGuiUtils - a gui subclass of LaUtils */
      bool setComboToDefault(QComboBox * thepCombo, QString theDefault);
};

#endif //LAANIMALPARAMETERMANAGER_H
