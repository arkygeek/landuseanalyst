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
#ifndef LAANIMALMANAGER_H
#define LAANIMALMANAGER_H

//QT Includes
#include <QDialog>
//Local Includes
#include <ui_laanimalmanagerbase.h>
#include <laanimal.h>
#include <lautils.h>
class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaAnimalManager : public QDialog, private Ui::LaAnimalManagerBase
{
  Q_OBJECT
  public:
    LaAnimalManager(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaAnimalManager();

  public slots:
    void on_pushButtonLoad_clicked();
    void on_pushButtonSave_clicked();

  private slots:
      void cellClicked(int theRow, int theColumn);

  private:
      void refreshAnimalTable(QString theGuid=0);
      void selectAnimal(QString theFileName);

      LaUtils::AnimalMap mAnimalMap;
      LaAnimal mAnimal;
      void readSettings();
      void writeSettings();
};

#endif //LAANIMALFORMMAIN_H