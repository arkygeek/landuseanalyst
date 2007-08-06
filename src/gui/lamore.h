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
#ifndef LAMORE_H
#define LAMORE_H

//QT Includes
#include <QDialog>

//Local Includes
#include <ui_lamorebase.h>
#include <laanimalparameter.h>
#include <lautils.h>
#include <QSpinBox>

class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaMore : public QDialog, private Ui::LaMoreBase
{
  Q_OBJECT
  public:
    LaMore(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaMore();

  public slots:
    void on_pbnInsert_clicked();

  private slots:
      //void resizeEvent(QResizeEvent*);

  private:
      void refreshTable();
      void readSettings();
      void writeSettings();

      /** @TODO move this into LaGuiUtils - a gui subclass of LaUtils */
      bool setComboToDefault(QComboBox * thepCombo, QString theDefault);

      LaUtils::AnimalParameterMap mAnimalParameterMap;
      LaUtils::CropMap mCropMap;
      LaAnimalParameter mAnimalParameter;
};

#endif //LAMORE_H
