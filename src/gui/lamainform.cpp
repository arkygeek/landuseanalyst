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
#include "lamainform.h"
#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QFile>
#include <QTextStream>
  LaMainForm::LaMainForm(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
  //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  /** See the qtdocs on signals and slots to understand below.
   * we connect the currentItemChanged signal that a tree view emits when you 
   * click on an item to a little method that sets the help viewer contents
   * appropriately. TS
   */
  connect(treeHelp, SIGNAL(currentItemChanged(QTreeWidgetItem * ,QTreeWidgetItem *)), 
               this, SLOT(helpItemClicked(QTreeWidgetItem * ,QTreeWidgetItem *)));
}

LaMainForm::~LaMainForm()
{
  writeSettings();
}

void LaMainForm::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaMainForm::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaMainForm::on_calculate_button_clicked()
{
	qDebug("QGIS Rocks");
}

void LaMainForm::on_wheatview_clicked()
{
	int pdp = (100-(dietslider->value())); //grab value from slider for overall meat percentage
	int ptp = meatslider->value(); //grab value from slider for tame plant percentage
	int wp = wheat_percent->value(); //grab value from form for percentage of wheat in plant portion of diet
	int wy = wheat_yield->value();
	double wfr = wheat_fallow_ratio->value();
	//double wcr = wheat_crop_ratio->value();
	int cal = dailycalories->value();
	int popn = population->value();

/*
cropcalc () {			# =-FUNCTION-= to determine land required for CROPS

	if [ $GIS_FLAG_A -eq 1 ] 		# Calculate area required for Crop 1
		then		# Flag was Selected
			crop1area=`echo "scale=3; (((${GIS_OPT_POPN} * ${GIS_OPT_CROP1REQ}) / ${GIS_OPT_CROP1YIELD}) * 1000)" | bc`
			crop1fallow=`echo "scale=3; ${crop1area} * ${GIS_OPT_CROP1RATIO})" | bc`
		else		#Flag NOT Selected
			crop1area=0
			crop1fallow=0
	fi

	if [ $GIS_FLAG_B -eq 1 ] 		# Calculate area required for Crop 2
		then
			crop2area=`echo "scale=3; (((${GIS_OPT_POPN} * ${GIS_OPT_CROP2REQ}) / ${GIS_OPT_CROP2YIELD}) * 1000)" | bc`
			crop2fallow=`echo "scale=3; ${crop2area} * ${GIS_OPT_CROP2RATIO})" | bc`
		else
			crop2area=0
			crop2fallow=0
	fi

	if [ $GIS_FLAG_C -eq 1 ] 		# Calculate area required for Crop 3
		then
			crop3area=`echo "scale=3; (((${GIS_OPT_POPN} * ${GIS_OPT_CROP3REQ}) / ${GIS_OPT_CROP3YIELD}) * 1000)" | bc`
			crop3fallow=`echo "scale=3; ${crop3area} * ${GIS_OPT_CROP3RATIO})" | bc`
		else
			crop3area=0
			crop3fallow=0
	fi

	if [ $GIS_FLAG_D -eq 1 ] 		# Calculate area required for Crop 4
		then
			crop4area=`echo "scale=3; (((${GIS_OPT_POPN} * ${GIS_OPT_CROP4REQ}) / ${GIS_OPT_CROP4YIELD}) * 1000)" | bc`
			crop4fallow=`echo "scale=3; ${crop4area} * ${GIS_OPT_CROP4RATIO})" | bc`
		else
			crop4area=0
			crop4fallow=0
	fi

	if [ $GIS_FLAG_E -eq 1 ] 		# Calculate area required for Crop 5
		then
			crop5area=`echo "scale=3; (((${GIS_OPT_POPN} * ${GIS_OPT_CROP5REQ}) / ${GIS_OPT_CROP5YIELD}) * 1000)" | bc`
			crop5fallow=`echo "scale=3; ${crop5area} * ${GIS_OPT_CROP5RATIO})" | bc`
		else
			crop5area=0
			crop5fallow=0
	fi
}


*/

}


void LaMainForm::on_pigview_clicked()
{
	int mdp = dietslider->value(); //grab value from slider for overall meat percentage
	int mtp = meatslider->value(); //grab value from slider for tame meat percentage
	int pp = pigpercent->value(); //grab value from form for percentage of pigmeat of meat portion of diet
	int pls = piglittersize->value(); //grab value from form for pig litter size
	int pw = pigweight->value(); //grab value from form for for pig kill weight
	int pgt = piggrowtime->value(); //grab value from form for pig grow time
	int cal = dailycalories->value();
	int popn = population->value();
	bool pfflag = pigfodderuse->isCheckable(); //grab value from form for fodder use flag
	int pfa = pigfodderamount->value(); //grab value from form for amount of fodder
	//int pfc = pigfoddercrop->currentindex(); //grab value from form for type of fodder
	//int pft = pigfoddertime->currentindex(); //grab value from form for time measurement of fodder rate
	//int pgrflag = piggrazefallow->checked(); //grab value from form for fallow grazing flag
	float meat = (((((mdp/100.)*(mtp/100.)*(pp/100.))*cal*popn)/3000.)*365.*2.); // 3000 is calories/kg of pork
	float animals = (meat/100.);
	float sows = ((10.*meat)/(1760.53*pls));
	float drysows = ((sows*30.80)/249.70);
	float gsows = ((sows*41.6)/249.70);
	float lsows = ((sows*177.20)/249.70);
	float spigs = (((355.10/41.60)/10.)*pls*lsows);
	float npigs = ((((sows*420.10)/249.70)/10.)*pls);
	float gpigs = ((((sows*1414.70)/249.70)/10.)*pls);
	float total = (sows+spigs+npigs+gpigs);
	qDebug("fodder flag value: " + QString::number(pfflag).toLocal8Bit());
	qDebug("You supplied me with this information:");
	qDebug("Population of Settlement: " + QString::number(popn).toLocal8Bit());
	qDebug("Calories/person per day: " + QString::number(cal).toLocal8Bit());
	qDebug("Percentage of Calories in the diet from MEAT: " + QString::number(mdp).toLocal8Bit());
	qDebug("Percentage of MEAT that is from domesticated animals: " + QString::number(mtp).toLocal8Bit());
	qDebug("Percentage of DOMESTICATED MEAT that is from PIGS: " + QString::number(pp).toLocal8Bit());
	qDebug("Calories per kg in PIG MEAT: 3000 assumed");
	qDebug("Average Litter Size: " + QString::number(pls).toLocal8Bit());
	qDebug("kg of meat per year: " + QString::number(meat).toLocal8Bit());
	qDebug("Number of 100kg pigs: " + QString::number(animals).toLocal8Bit());
	qDebug("Sows required to produce this much meat: " + QString::number(sows).toLocal8Bit());
	qDebug("Non-Pregnant sows and gilts: " + QString::number(drysows).toLocal8Bit());
	qDebug("Gestating Sows: " + QString::number(gsows).toLocal8Bit());
	qDebug("Lactating Sows: " + QString::number(lsows).toLocal8Bit());
	qDebug("Total Adult Females: " + QString::number(sows).toLocal8Bit());
	qDebug("Suckling Pigs: " + QString::number(spigs).toLocal8Bit());
	qDebug("Nursery Pigs: " + QString::number(npigs).toLocal8Bit());
	qDebug("Growing and finishing pigs: " + QString::number(gpigs).toLocal8Bit());
	qDebug("Total pigs: " + QString::number(total).toLocal8Bit());
}

void LaMainForm::on_meatslider_valueChanged(int theValue)
{
	QString myMinString = QString::number(100-theValue);
	QString myMaxString = QString::number(theValue);
	meatwildpercent->setText(myMinString);
	meattamepercent->setText(myMaxString);
}

void LaMainForm::on_dietslider_valueChanged(int theValue)
{
	QString myMinString = QString::number(theValue);
	QString myMaxString = QString::number(100-theValue);
	meatpercent->setText(myMinString);
	plantpercent->setText(myMaxString);
}

void LaMainForm::on_plantslider_valueChanged(int theValue)
{
	QString myMinString = QString::number(100-theValue);
	QString myMaxString = QString::number(theValue);
	plantwildpercent->setText(myMinString);
	planttamepercent->setText(myMaxString);
}

void LaMainForm::helpItemClicked(QTreeWidgetItem * thepCurrentItem, QTreeWidgetItem * thepOldItem)
{
  qDebug("Item clicked in help browser: " + thepCurrentItem->text(0).toLocal8Bit());
  QFile myQFile( ":/" + thepCurrentItem->text(0)  + ".html" );
  if ( myQFile.open( QIODevice::ReadOnly ) ) 
  {
    //now we parse the loc file, checking each line for its taxon
    QTextStream myStream( &myQFile );
    textHelp->setHtml(myStream.readAll());
    myQFile.close();
  }
  else
  {
    qDebug("Help resource for : " + thepCurrentItem->text(0).toLocal8Bit() + " not found!");
  }
}

