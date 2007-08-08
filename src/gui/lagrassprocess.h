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

#ifndef LAGRASSPROCESS_H
#define LAGRASSPROCESS_H

//QT Includes
#include <QDialog>
//Local Includes
#include <lautils.h>
#include "ui_lagrassprocessbase.h"

class QTreeWidgetItem;
/**
  This is the grass process gui class
  @author Jason Jorgenson
*/
class LaGrassProcess : public QDialog, private Ui::LaGrassProcessBase
{
  Q_OBJECT
  public:
    LaGrassProcess(QWidget* parent = 0, Qt::WFlags fl = 0 );
    ~LaGrassProcess();

  public slots:
    /** when called starts the grass analysis */
    void on_pbnStart_clicked();
    /** aborts the grass analysis process */
    void on_pbnAbort_clicked();
    void setPbarTargetRange(int theTarget);
    void setPbarOverallRange(int theOverall);
    void updateCurrentProgress(int theArea);
    void updateOverallProgress(int theStep);
    void writeGrassMessage(QString theGrassMessage);
    void updatePreview(QString thePreviewFile);
    void updateGraphic(QString theGraphicFile);
    void toggleBusyProgressBar(bool theStatus);

  private slots:

  private:
      void readSettings();
      void writeSettings();

      int mCurrentAreaTarget;
      int mSearches;
};

#endif //LAGRASSPROCESS_H
