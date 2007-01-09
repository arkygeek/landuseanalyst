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
	int pdp = (100-(dietslider->value())); 		// OVERALL PLANT PERCENTAGE
	int ptp = meatslider->value(); 			// TAME PLANT percentage
	int wp = wheat_percent->value(); 		// PERCENTAGE OF WHEAT in plant portion of diet
	int wy = wheat_yield->value();			// expected average WHEAT YIELD
	int wcal = wheatcals->value();			// FALLOW RATIO for WHEAT
	float wfr = wheat_fallow_ratio->value();	// 
	int cal = dailycalories->value();
	int popn = population->value();

// calculate area required for wheat
	float wa;	// wheat area 
	float wfa;	// wheat fallow area
	float wta;	// wheat total area
	wa = ((((((((pdp*ptp)/100.)*(wp/100.))*cal*365.)/wcal)*popn)/wy)*1000.);
	wfa = ((((((((pdp*ptp)/100.)*(wp/100.))*cal*365.)/wcal)*popn)/wy)*1000.)*(wfr);
	wta = wa + wfa;
	qDebug("Wheat area: " + QString::number(wa).toLocal8Bit());
	qDebug("Wheat fallow area: " + QString::number(wfa).toLocal8Bit());
	qDebug("Wheat total area: " + QString::number(wta).toLocal8Bit());



}

void LaMainForm::on_barleyview_clicked()
{
	int pdp = (100-(dietslider->value())); 		// OVERALL PLANT PERCENTAGE
	int ptp = meatslider->value(); 			// TAME PLANT percentage
	int bp = barley_percent->value(); 		// PERCENTAGE OF BARLEY in plant portion of diet
	int by = barley_yield->value();			// expected average BARLEY YIELD
	int bcal = barleycals->value();			// FALLOW RATIO for BARLEY
	float bfr = barley_fallow_ratio->value();	// 
	int cal = dailycalories->value();
	int popn = population->value();

// calculate area required for wheat
	float ba;	// wheat area 
	float bfa;	// wheat fallow area
	float bta;	// wheat total area
	ba = ((((((((pdp*ptp)/100.)*(bp/100.))*cal*365.)/bcal)*popn)/by)*1000.);
	bfa = ((((((((pdp*ptp)/100.)*(bp/100.))*cal*365.)/bcal)*popn)/by)*1000.)*(bfr);
	bta = ba + bfa;
	qDebug("Barley area: " + QString::number(ba).toLocal8Bit());
	qDebug("Barley fallow area: " + QString::number(bfa).toLocal8Bit());
	qDebug("Barley total area: " + QString::number(bta).toLocal8Bit());



}

void LaMainForm::on_lentilview_clicked()
{
	int pdp = (100-(dietslider->value())); 		// OVERALL PLANT PERCENTAGE
	int ptp = meatslider->value(); 			// TAME PLANT percentage
	int lp = lentil_percent->value(); 		// PERCENTAGE OF LENTIL in plant portion of diet
	int ly = lentil_yield->value();			// expected average LENTIL YIELD
	int lcal = lentilcals->value();			// FALLOW RATIO for LENTIL
	float lfr = lentil_fallow_ratio->value();	// 
	int cal = dailycalories->value();
	int popn = population->value();

// calculate area required for LENTIL
	float la;	// wheat area 
	float lfa;	// wheat fallow area
	float lta;	// wheat total area
	la = ((((((((pdp*ptp)/100.)*(lp/100.))*cal*365.)/lcal)*popn)/ly)*1000.);
	lfa = ((((((((pdp*ptp)/100.)*(lp/100.))*cal*365.)/lcal)*popn)/ly)*1000.)*(lfr);
	lta = la + lfa;
	qDebug("Lentil area: " + QString::number(la).toLocal8Bit());
	qDebug("Lentil fallow area: " + QString::number(lfa).toLocal8Bit());
	qDebug("Lentil total area: " + QString::number(lta).toLocal8Bit());



}

void LaMainForm::on_oliveview_clicked()
{
	int pdp = (100-(dietslider->value())); 		// OVERALL PLANT PERCENTAGE
	int ptp = meatslider->value(); 			// TAME PLANT percentage
	int op = olive_percent->value(); 		// PERCENTAGE OF OLIVE in plant portion of diet
	int oy = olive_yield->value();			// expected average OLIVE YIELD
	int ocal = olivecals->value();			// FALLOW RATIO for OLIVE
	float ofr = olive_fallow_ratio->value();	// 
	int cal = dailycalories->value();
	int popn = population->value();

// calculate area required for OLIVE
	float oa;	// olive area 
	float ofa;	// olive fallow area
	float ota;	// olive total area
	oa = ((((((((pdp*ptp)/100.)*(op/100.))*cal*365.)/ocal)*popn)/oy)*1000.);
	ofa = ((((((((pdp*ptp)/100.)*(op/100.))*cal*365.)/ocal)*popn)/oy)*1000.)*(ofr);
	ota = oa + ofa;
	qDebug("olive area: " + QString::number(oa).toLocal8Bit());
	qDebug("olive fallow area: " + QString::number(ofa).toLocal8Bit());
	qDebug("olive total area: " + QString::number(ota).toLocal8Bit());



}

void LaMainForm::on_grapeview_clicked()
{
	int pdp = (100-(dietslider->value())); 		// OVERALL PLANT PERCENTAGE
	int ptp = meatslider->value(); 			// TAME PLANT percentage
	int gp = grape_percent->value(); 		// PERCENTAGE OF GRAPE in plant portion of diet
	int gy = grape_yield->value();			// expected average GRAPE YIELD
	int gcal = grapecals->value();			// FALLOW RATIO for GRAPE
	float gfr = grape_fallow_ratio->value();	// 
	int cal = dailycalories->value();
	int popn = population->value();

// calculate area required for grape
	float ga;	// grape area 
	float gfa;	// grape fallow area
	float gta;	// grape total area
	ga = ((((((((pdp*ptp)/100.)*(gp/100.))*cal*365.)/gcal)*popn)/gy)*1000.);
	gfa = ((((((((pdp*ptp)/100.)*(gp/100.))*cal*365.)/gcal)*popn)/gy)*1000.)*(gfr);
	gta = ga + gfa;
	qDebug("grape area: " + QString::number(ga).toLocal8Bit());
	qDebug("grape fallow area: " + QString::number(gfa).toLocal8Bit());
	qDebug("grape total area: " + QString::number(gta).toLocal8Bit());



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

