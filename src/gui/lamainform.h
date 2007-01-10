/***************************************************************************
 *   Copyright (C) 2007 by Tim Sutton   *
 *   tim@linfiniti.com   *
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
//Local Includes
#include <ui_lamainformbase.h>
class QTreeWidgetItem;
/**
@author Tim Sutton
*/
class LaMainForm : public QDialog, private Ui::LaMainFormBase
{
	Q_OBJECT
	public:
		LaMainForm(QWidget* parent = 0, Qt::WFlags fl = 0 );
		~LaMainForm();
  public slots:
	void on_meatslider_valueChanged(int theValue);
	void on_dietslider_valueChanged(int theValue);
	void on_plantslider_valueChanged(int theValue);
	void on_pigview_clicked();
	void on_wheatview_clicked();
	void on_barleyview_clicked();
	void on_lentilview_clicked();
	void on_oliveview_clicked();
	void on_grapeview_clicked();
	void on_run_button_clicked();

  private slots:
  void helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem);
  void writeMessage(QString theText);
  void writePlantCellValue(int theRow, int theCol, QString theValue);
	private:
		void readSettings();
		void writeSettings();
};

#endif //LAMAINFORM_H
