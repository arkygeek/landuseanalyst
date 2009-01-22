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
#ifndef LAASSEMBLAGECONVERSION_H
#define LAASSEMBLAGECONVERSION_H

  //QT Includes
#include <QDialog>

  //Local Includes
#include <ui_laassemblageconversionbase.h>
#include <laanimalparameter.h>
#include <lautils.h>
#include <QSpinBox>

class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaAssemblageConversion : public QDialog, private Ui::LaAssemblageConversionBase
{
  Q_OBJECT
  public:
    LaAssemblageConversion(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaAssemblageConversion();

  public slots:
    virtual void on_pbnInsert_clicked();
    virtual void on_pbnCalculate_clicked();
    virtual void on_pbnClearTable_clicked();
    virtual void on_pbnSave_clicked();

  private slots:
      void resizeEvent(QResizeEvent*);

  private:
      void refreshTable();
      void readSettings();
      void writeSettings();

      /** @TODO move this into LaGuiUtils - a gui subclass of LaUtils */
      bool setComboToDefault(QComboBox * thepCombo, QString theDefault);

      LaUtils::AnimalParameterMap mAnimalParameterMap;
      LaUtils::CropMap mCropMap;
      LaAnimalParameter mAnimalParameter;

        //int mRowCount;
};

#endif   //LAASSEMBLAGECONVERSION_H
