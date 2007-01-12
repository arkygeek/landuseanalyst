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
#include <QTableWidgetItem>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>

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
  makeCircle(0,0);
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

/*void LaMainForm::on_calculate_button_clicked()
  {
  writeMessage("QGIS Rocks");
  }
  */

void LaMainForm::on_wheatview_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int wp = wheat_percent->value();     // PERCENTAGE OF WHEAT in plant portion of diet
  int wy = wheat_yield->value();      // expected average WHEAT YIELD
  int wcal = wheatcals->value();      // FALLOW RATIO for WHEAT
  float wfr = wheat_fallow_ratio->value();  // 
  int cal = dailycalories->value();
  int popn = population->value();

  // calculate area required for wheat
  float wa;  // wheat area 
  float wfa;  // wheat fallow area
  float wta;  // wheat total area
  wa = ((((((((pdp*ptp)/100.)*(wp/100.))*cal*365.)/wcal)*popn)/wy)*1000.);
  wfa = ((((((((pdp*ptp)/100.)*(wp/100.))*cal*365.)/wcal)*popn)/wy)*1000.)*(wfr);
  wta = wa + wfa;
  writeMessage("Wheat area: " + QString::number(wa).toLocal8Bit());
  writeMessage("Wheat fallow area: " + QString::number(wfa).toLocal8Bit());
  writeMessage("Wheat total area: " + QString::number(wta).toLocal8Bit());
}

void LaMainForm::on_barleyview_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int bp = barley_percent->value();     // PERCENTAGE OF BARLEY in plant portion of diet
  int by = barley_yield->value();      // expected average BARLEY YIELD
  int bcal = barleycals->value();      // FALLOW RATIO for BARLEY
  float bfr = barley_fallow_ratio->value();  // 
  int cal = dailycalories->value();
  int popn = population->value();

  // calculate area required for barley
  float ba;  // barley area 
  float bfa;  // barley fallow area
  float bta;  // barley total area
  ba = ((((((((pdp*ptp)/100.)*(bp/100.))*cal*365.)/bcal)*popn)/by)*1000.);
  bfa = ((((((((pdp*ptp)/100.)*(bp/100.))*cal*365.)/bcal)*popn)/by)*1000.)*(bfr);
  bta = ba + bfa;
  writeMessage("Barley area: " + QString::number(ba).toLocal8Bit());
  writeMessage("Barley fallow area: " + QString::number(bfa).toLocal8Bit());
  writeMessage("Barley total area: " + QString::number(bta).toLocal8Bit());
}

void LaMainForm::on_lentilview_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int lp = lentil_percent->value();     // PERCENTAGE OF LENTIL in plant portion of diet
  int ly = lentil_yield->value();      // expected average LENTIL YIELD
  int lcal = lentilcals->value();      // FALLOW RATIO for LENTIL
  float lfr = lentil_fallow_ratio->value();  // 
  int cal = dailycalories->value();
  int popn = population->value();

  // calculate area required for LENTIL
  float la;  // wheat area 
  float lfa;  // wheat fallow area
  float lta;  // wheat total area
  la = ((((((((pdp*ptp)/100.)*(lp/100.))*cal*365.)/lcal)*popn)/ly)*1000.);
  lfa = ((((((((pdp*ptp)/100.)*(lp/100.))*cal*365.)/lcal)*popn)/ly)*1000.)*(lfr);
  lta = la + lfa;
  writeMessage("Lentil area: " + QString::number(la).toLocal8Bit());
  writeMessage("Lentil fallow area: " + QString::number(lfa).toLocal8Bit());
  writeMessage("Lentil total area: " + QString::number(lta).toLocal8Bit());
}

void LaMainForm::on_oliveview_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int op = olive_percent->value();     // PERCENTAGE OF OLIVE in plant portion of diet
  int oy = olive_yield->value();      // expected average OLIVE YIELD
  int ocal = olivecals->value();      // FALLOW RATIO for OLIVE
  float ofr = olive_fallow_ratio->value();  // 
  int cal = dailycalories->value();
  int popn = population->value();

  // calculate area required for OLIVE
  float oa;  // olive area 
  float ofa;  // olive fallow area
  float ota;  // olive total area
  oa = ((((((((pdp*ptp)/100.)*(op/100.))*cal*365.)/ocal)*popn)/oy)*1000.);
  ofa = ((((((((pdp*ptp)/100.)*(op/100.))*cal*365.)/ocal)*popn)/oy)*1000.)*(ofr);
  ota = oa + ofa;
  writeMessage("olive area: " + QString::number(oa).toLocal8Bit());
  writeMessage("olive fallow area: " + QString::number(ofa).toLocal8Bit());
  writeMessage("olive total area: " + QString::number(ota).toLocal8Bit());
}

void LaMainForm::on_grapeview_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int gp = grape_percent->value();     // PERCENTAGE OF GRAPE in plant portion of diet
  int gy = grape_yield->value();      // expected average GRAPE YIELD
  int gcal = grapecals->value();      // FALLOW RATIO for GRAPE
  float gfr = grape_fallow_ratio->value();  // 
  int cal = dailycalories->value();
  int popn = population->value();

  // calculate area required for grape
  float ga;  // grape area 
  float gfa;  // grape fallow area
  float gta;  // grape total area
  ga = ((((((((pdp*ptp)/100.)*(gp/100.))*cal*365.)/gcal)*popn)/gy)*1000.);
  gfa = ((((((((pdp*ptp)/100.)*(gp/100.))*cal*365.)/gcal)*popn)/gy)*1000.)*(gfr);
  gta = ga + gfa;
  writeMessage("grape area: " + QString::number(ga).toLocal8Bit());
  writeMessage("grape fallow area: " + QString::number(gfa).toLocal8Bit());
  writeMessage("grape total area: " + QString::number(gta).toLocal8Bit());
}

void LaMainForm::on_pigview_clicked() 
{
  int mdp = dietslider->value(); //grab value from slider for overall meat percentage
  int mtp = (100 - (meatslider->value())); //grab value from slider for tame meat percentage
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
  writeMessage("fodder flag value: " + QString::number(pfflag).toLocal8Bit());
  writeMessage("You supplied me with this information:");
  writeMessage("Population of Settlement: " + QString::number(popn).toLocal8Bit());
  writeMessage("Calories/person per day: " + QString::number(cal).toLocal8Bit());
  writeMessage("Percentage of Calories in the diet from MEAT: " + QString::number(mdp).toLocal8Bit());
  writeMessage("Percentage of MEAT that is from domesticated animals: " + QString::number(mtp).toLocal8Bit());
  writeMessage("Percentage of DOMESTICATED MEAT that is from PIGS: " + QString::number(pp).toLocal8Bit());
  writeMessage("Calories per kg in PIG MEAT: 3000 assumed");
  writeMessage("Average Litter Size: " + QString::number(pls).toLocal8Bit());
  writeMessage("kg of meat per year: " + QString::number(meat).toLocal8Bit());
  writeMessage("Number of 100kg pigs: " + QString::number(animals).toLocal8Bit());
  writeMessage("Sows required to produce this much meat: " + QString::number(sows).toLocal8Bit());
  writeMessage("Non-Pregnant sows and gilts: " + QString::number(drysows).toLocal8Bit());
  writeMessage("Gestating Sows: " + QString::number(gsows).toLocal8Bit());
  writeMessage("Lactating Sows: " + QString::number(lsows).toLocal8Bit());
  writeMessage("Total Adult Females: " + QString::number(sows).toLocal8Bit());
  writeMessage("Suckling Pigs: " + QString::number(spigs).toLocal8Bit());
  writeMessage("Nursery Pigs: " + QString::number(npigs).toLocal8Bit());
  writeMessage("Growing and finishing pigs: " + QString::number(gpigs).toLocal8Bit());
  writeMessage("Total pigs: " + QString::number(total).toLocal8Bit());
}

void LaMainForm::on_run_button_clicked() 
{
  writeMessage("running...");
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int cal = dailycalories->value();
  int popn = population->value();
  float wfa;    // WHEAT fallow area
  float wta;    // WHEAT total area
  float bfa;    // BARLEY fallow area
  float bta;    // BARLEY total area
  float lfa;    // LENTIL fallow area
  float lta;    // LENTIL total area
  float ofa;    // OLIVE fallow area
  float ota;    // OLIVE total area
  float gfa;    // grape fallow area
  float gta;    // grape total area
  float stdtotalarea;    // total area required for crops using the standard mask
  float stdcroptotalarea;    // total area of sown land
  float stdfallowtotalarea;  // total area of fallow
  float wheatkg, barleykg, lentilkg, olivekg, grapekg;
  float wheatcaltot, barleycaltot, lentilcaltot, olivecaltot, grapecaltot;

  float totalcals = popn*cal*365.;
  float plantcals = (pdp/100.)*popn*cal*365.;
  float tameplantcals = ((pdp/100.)*(ptp/100.))*popn*cal*365.;


  if ( calculations->isChecked() )
  {

    if (wheat->isChecked() ) 
    {
      int wp = wheat_percent->value();     // PERCENTAGE OF WHEAT in plant portion of diet
      int wy = wheat_yield->value();      // expected average WHEAT YIELD
      int wcal = wheatcals->value();      // calories in 1 kg of WHEAT
      float wfr = wheat_fallow_ratio->value();  // FALLOW RATIO for WHEAT
      float wa;          // WHEAT area 
      wheatcaltot = tameplantcals*(wp/100.);
      wheatkg = wheatcaltot/wcal;
      wa = (((wheatkg)/wy)*1000.)/10000.;
      wfa = wa * wfr;
      wta = wa + wfa;
      writeMessage("Wheat area: " + QString::number(wa).toLocal8Bit());
      writeMessage("Wheat fallow area: " + QString::number(wfa).toLocal8Bit());
      writeMessage("Wheat total area: " + QString::number(wta).toLocal8Bit());

      writePlantCellValue(1,0,QString::number((pdp/100.)*(ptp/100.)*(wp/100.)*100.));
      writePlantCellValue(1,1,QString::number(wheatkg));
      writePlantCellValue(1,2,QString::number(wheatcaltot/1000.));
      writePlantCellValue(1,3,QString::number(wa));
      writePlantCellValue(1,4,QString::number(wfa));
      writePlantCellValue(1,5,QString::number(wta));
    }
    else
    {
      wta = 0;
      wfa = 0;
      wheatkg = 0;
    }

    if (barley->isChecked() )
    {
      int bp = barley_percent->value();     // PERCENTAGE OF BARLEY in plant portion of diet
      int by = barley_yield->value();      // expected average BARLEY YIELD
      int bcal = barleycals->value();      // calories in 1 kg of BARLEY
      float bfr = barley_fallow_ratio->value();  // FALLOW RATIO for BARLEY
      float ba;  // barley area 
      barleycaltot = tameplantcals*(bp/100.);
      barleykg = barleycaltot/bcal;
      ba = (((barleykg)/by)*1000.)/10000.;
      bfa = ba * bfr;
      bta = ba + bfa;
      writeMessage("Barley area: " + QString::number(ba).toLocal8Bit());
      writeMessage("Barley fallow area: " + QString::number(bfa).toLocal8Bit());
      writeMessage("Barley total area: " + QString::number(bta).toLocal8Bit());

      writePlantCellValue(2,0,QString::number((pdp/100.)*(ptp/100.)*(bp/100.)*100.));
      writePlantCellValue(2,1,QString::number(barleykg));
      writePlantCellValue(2,2,QString::number(barleycaltot/1000.));
      writePlantCellValue(2,3,QString::number(ba));
      writePlantCellValue(2,4,QString::number(bfa));
      writePlantCellValue(2,5,QString::number(bta));
    }
    else
    {
      bta=0;
      bfa=0;
      barleykg=0;
    }

    if (lentils->isChecked() )
    {
      int lp = lentil_percent->value();     // PERCENTAGE OF LENTIL in plant portion of diet
      int ly = lentil_yield->value();      // expected average LENTIL YIELD
      int lcal = lentilcals->value();      // calories in 1 kg of LENTILS
      float lfr = lentil_fallow_ratio->value();  // FALLOW RATIO for LENTIL
      float la;  // wheat area 
      lentilcaltot = tameplantcals*(lp/100.);
      lentilkg = lentilcaltot/lcal;
      la = (((lentilkg)/ly)*1000.)/10000.;
      lfa = la * lfr;
      lta = la + lfa;
      writeMessage("Lentil area: " + QString::number(la).toLocal8Bit());
      writeMessage("Lentil fallow area: " + QString::number(lfa).toLocal8Bit());
      writeMessage("Lentil total area: " + QString::number(lta).toLocal8Bit());

      writePlantCellValue(3,0,QString::number((pdp/100.)*(ptp/100.)*(lp/100.)*100.));
      writePlantCellValue(3,1,QString::number(lentilkg));
      writePlantCellValue(3,2,QString::number(lentilcaltot/1000.));
      writePlantCellValue(3,3,QString::number(la));
      writePlantCellValue(3,4,QString::number(lfa));
      writePlantCellValue(3,5,QString::number(lta));
    }
    else
    {
      lta = 0;
      lfa = 0;
      lentilkg=0;
    }

    if (olives->isChecked() )
    {
      int op = olive_percent->value();     // PERCENTAGE OF OLIVE in plant portion of diet
      int oy = olive_yield->value();      // expected average OLIVE YIELD
      int ocal = olivecals->value();      // calories in 1 kg of OLIVES
      float ofr = olive_fallow_ratio->value();  // FALLOW RATIO for OLIVE
      float oa;          // olive area 
      olivecaltot = tameplantcals*(op/100.);
      olivekg = olivecaltot/ocal;
      oa = (((olivekg)/oy)*1000.)/10000.;
      ofa = oa * ofr;
      ota = oa + ofa;
      writeMessage("olive area: " + QString::number(oa).toLocal8Bit());
      writeMessage("olive fallow area: " + QString::number(ofa).toLocal8Bit());
      writeMessage("olive total area: " + QString::number(ota).toLocal8Bit());

      writePlantCellValue(4,0,QString::number((pdp/100.)*(ptp/100.)*(op/100.)*100.));
      writePlantCellValue(4,1,QString::number(olivekg));
      writePlantCellValue(4,2,QString::number(olivecaltot/1000.));
      writePlantCellValue(4,3,QString::number(oa));
      writePlantCellValue(4,4,QString::number(ofa));
      writePlantCellValue(4,5,QString::number(ota));
    }
    else
    {
      ota = 0;
      ofa = 0;
      olivekg=0;
    }

    if (grapes->isChecked() )
    {
      int gp = grape_percent->value();     // PERCENTAGE OF GRAPE in plant portion of diet
      int gy = grape_yield->value();      // expected average GRAPE YIELD
      int gcal = grapecals->value();      // FALLOW RATIO for GRAPE
      float gfr = grape_fallow_ratio->value();  // calories in 1 kg of GRAPES
      float ga;          // grape area 
      grapecaltot = tameplantcals*(gp/100.);
      grapekg = grapecaltot/gcal;
      ga = (((grapekg)/gy)*1000.)/10000.;
      gfa = ga * gfr;
      gta = ga + gfa;
      writeMessage("grape area: " + QString::number(ga).toLocal8Bit());
      writeMessage("grape fallow area: " + QString::number(gfa).toLocal8Bit());
      writeMessage("grape total area: " + QString::number(gta).toLocal8Bit());

      writePlantCellValue(5,0,QString::number((pdp/100.)*(ptp/100.)*(gp/100.)*100.));
      writePlantCellValue(5,1,QString::number(grapekg));
      writePlantCellValue(5,2,QString::number(grapecaltot/1000.));
      writePlantCellValue(5,3,QString::number(ga));
      writePlantCellValue(5,4,QString::number(gfa));
      writePlantCellValue(5,5,QString::number(gta));
    }
    else
    {
      gta = 0;
      gfa = 0;
      grapekg = 0;
    }

    if (sheep->isChecked() )
    {
      writeMessage("sheep is checked.");
      /* fill table
         writePlantCellValue(7,0,QString::number((pdp/100.)*(ptp/100.)*(wp/100.)*100.));
         writePlantCellValue(7,1,QString::number(wheatkg));
         writePlantCellValue(7,2,QString::number(wheatcaltot/1000.));
         writePlantCellValue(7,4,QString::number(wa));
         writePlantCellValue(7,5,QString::number(wfa));
         writePlantCellValue(7,6,QString::number(wta));
         writePlantCellValue(7,7,QString::number(wta));
         */
    }
    else
    {
    }

    if (goat->isChecked() )
    {
      writeMessage("goat is checked.");
      /* fill table
         writePlantCellValue(8,0,QString::number((pdp/100.)*(ptp/100.)*(bp/100.)*100.));
         writePlantCellValue(8,1,QString::number(barleykg));
         writePlantCellValue(8,2,QString::number(barleycaltot/1000.));
         writePlantCellValue(8,4,QString::number(ba));
         writePlantCellValue(8,5,QString::number(bfa));
         writePlantCellValue(8,6,QString::number(bta));
         writePlantCellValue(8,7,QString::number(bta));
         */
    }
    else
    {
    }

    if (pig->isChecked() )
    {
      writeMessage("pig is checked.");
      /* fill table
         writePlantCellValue(9,0,QString::number((pdp/100.)*(ptp/100.)*(lp/100.)*100.));
         writePlantCellValue(9,1,QString::number(lentilkg));
         writePlantCellValue(9,2,QString::number(lentilcaltot/1000.));
         writePlantCellValue(9,4,QString::number(la));
         writePlantCellValue(9,5,QString::number(lfa));
         writePlantCellValue(9,6,QString::number(lta));
         writePlantCellValue(9,7,QString::number(lta));
         */
    }
    else
    {
    }

    if (cow->isChecked() )
    {
      writeMessage("cow is checked.");
      /* fill table
         writePlantCellValue(10,0,QString::number((pdp/100.)*(ptp/100.)*(op/100.)*100.));
         writePlantCellValue(10,1,QString::number(olivekg));
         writePlantCellValue(10,2,QString::number(olivecaltot/1000.));
         writePlantCellValue(10,4,QString::number(oa));
         writePlantCellValue(10,5,QString::number(ofa));
         writePlantCellValue(10,6,QString::number(ota));
         writePlantCellValue(10,7,QString::number(lta));
         */
    }
    else
    {
    }

    if (chicken->isChecked() )
    {
      writeMessage("chicken is checked.");
      /* fill table
         writePlantCellValue(11,0,QString::number((pdp/100.)*(ptp/100.)*(gp/100.)*100.));
         writePlantCellValue(11,1,QString::number(grapekg));
         writePlantCellValue(11,2,QString::number(grapecaltot/1000.));
         writePlantCellValue(11,4,QString::number(ga));
         writePlantCellValue(11,5,QString::number(gfa));
         writePlantCellValue(11,6,QString::number(gta));
         writePlantCellValue(11,7,QString::number(lta));
         */
    }
    else
    {
    }

    stdfallowtotalarea = (wfa+bfa+lfa+ofa+gfa);
    stdcroptotalarea = (wta+bta+lta+ota+gta)-stdfallowtotalarea;
    stdtotalarea = stdfallowtotalarea + stdcroptotalarea;
    totalcals = wheatcaltot+barleycaltot+lentilcaltot+olivecaltot+grapecaltot;

    /* Animals











       writeMessage("----------==========   RESULTS   ==========----------");



       writeMessage(" * * *   WHEAT   * * *");
       writeMessage("Total calories supplied by wheat (kcal) : " + QString::number(wheatcaltot/1000.).toLocal8Bit());
       writeMessage("kg of wheat to produce this many calories is: " + QString::number(wheatkg).toLocal8Bit());

       writeMessage(" * * *   BARLEY   * * *");
       writeMessage("Total calories supplied by barley (kcal): " + QString::number(barleycaltot/1000.).toLocal8Bit());
       writeMessage("kg of barley to produce this many calories is: " + QString::number(barleykg).toLocal8Bit());

       writeMessage(" * * *   LENTILS   * * *");
       writeMessage("Total calories supplied by lentils (kcal): " + QString::number(lentilcaltot/1000.).toLocal8Bit());
       writeMessage("kg of lentil to produce this many calories is: " + QString::number(lentilkg).toLocal8Bit());

       writeMessage(" * * *   OLIVES   * * *");
       writeMessage("Total calories supplied by olives m(kcal): " + QString::number(olivecaltot/1000.).toLocal8Bit());
       writeMessage("kg of olive to produce this many calories is: " + QString::number(olivekg).toLocal8Bit());

       writeMessage(" * * *   GRAPES   * * *");
       writeMessage("Total calories supplied by grapes (kcal): " + QString::number(grapecaltot/1000.).toLocal8Bit());
       writeMessage("kg of grape to produce this many calories is: " + QString::number(grapekg).toLocal8Bit());

       writeMessage(" * * *   LAND REQUIREMENTS   * * *");
       writeMessage("Total Sown Land required (ha): " + QString::number(stdcroptotalarea).toLocal8Bit());
       writeMessage("Total area of fallow land (ha): " + QString::number(stdfallowtotalarea).toLocal8Bit());
       writeMessage("Total area required for crops (ha): " + QString::number(stdtotalarea).toLocal8Bit());
       */
  }
  if (euclidean->isChecked() )
  {
    writeMessage("Euclidean is checked.");
  }
  if (walking->isChecked() )
  {
    writeMessage("Walking Distance is checked");
  }
  if (pathdistance->isChecked() )
  {
    writeMessage("Path Distance is checked.");
  }
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
  writeMessage("Item clicked in help browser: " + thepCurrentItem->text(0).toLocal8Bit());
  QFile myQFile( ":/" + thepCurrentItem->text(0)  + ".html" );
  if ( myQFile.open( QIODevice::ReadOnly ) ) {
    //now we parse the loc file, checking each line for its taxon
    QTextStream myStream( &myQFile );
    textHelp->setHtml(myStream.readAll());
    myQFile.close();
  }
  else {
    writeMessage("Help resource for : " + thepCurrentItem->text(0).toLocal8Bit() + " not found!");
  }
}

void LaMainForm::on_diet_breakdown_button_clicked() 
{
  int pdp = (100-(dietslider->value()));     // OVERALL PLANT PERCENTAGE
  int ptp = plantslider->value();       // TAME PLANT percentage
  int pdm = dietslider->value();
  int ptm = meatslider->value();
  int cal = dailycalories->value();
  int popn = population->value();

  float totalcals = popn*cal*365.;
  float plantcals = (pdp/100.)*totalcals;
  float tameplantcals = ((pdp/100.)*(ptp/100.))*totalcals;
  float animalcals = (pdm/100.)*totalcals;
  float tameanimalcals = ((pdm/100.)*(ptm/100.))*totalcals;

  writeDiet("Calories per person per year: " + QString::number((cal*365.)/1000.).toLocal8Bit() + "kcal");
  writeDiet("Calories required for population are: " + QString::number(totalcals/1000.).toLocal8Bit() + "kcal");
  writeDiet(" ");
  writeDiet("Plants contribute " + QString::number(pdp).toLocal8Bit() + "% to diet, or " + QString::number(plantcals/1000.).toLocal8Bit() + " kcal");
  writeDiet("Meat contributes " + QString::number(pdm).toLocal8Bit() + "% to diet, or  " + QString::number(animalcals/1000.).toLocal8Bit() + " kcal");
  writeDiet(" ");
  writeDiet("Tame Plants account for " + QString::number((pdp/100.)*(ptp/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(plantcals/1000.).toLocal8Bit() + " kcal");
  writeDiet("Tame Animals account for " + QString::number((pdm/100.)*(ptm/100.)*100.).toLocal8Bit() + "% of the diet, or " + QString::number(animalcals/1000.).toLocal8Bit() + " kcal");
}

void LaMainForm::writeMessage(QString theText) 
{
  textBrowserResults->append(theText);
}

void LaMainForm::writeDiet(QString theText) 
{
  breakdown_display->append(theText);
}

void LaMainForm::writePlantCellValue(int theRow, int theCol, QString theValue) 
{
  QTableWidgetItem *mypItem = new QTableWidgetItem(theValue);
  plant_table->setItem(theRow, theCol, mypItem);
}

void LaMainForm::getArea(float theArea) 
{
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "tempraster";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);

  if (!myProcess.waitForStarted()) 
  {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1))
  {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

void LaMainForm::makeWalkCost(int theX, int theY) 
{
}

void LaMainForm::makeEuclideanCost(int theX, int theY) 
{
}

void LaMainForm::makePathDistanceCost(int theX, int theY) 
{
}

void LaMainForm::writeMetaData(QString theValue) 
{
}

void LaMainForm::makeCircle(int theX, int theY) 
{
  // to verify this worked do
  //    d.rast
  //    and check in the pull downlist (if your eyes dont fall out looking at those fonts)
  //    to remove teh file again do:
  //    g.remove rast=circle

  /*
     qDebug("Making crop circle...tweeedee treedee");
     QString myProgram = "/usr/lib/grass/bin/r.circle";
     QStringList myArgs;
     myArgs << "-b" 
     << "output=circle" 
     <<  "coordinate=744800,3611100" 
     << "max=500" 
     << "--overwrite";
     */
  QString myProgram = "/usr/lib/grass/bin/r.stats";
  QStringList myArgs;
  myArgs << "landuse";
  QProcess myProcess;
  myProcess.start(myProgram, myArgs);
  if (!myProcess.waitForStarted()) {
    qDebug("The process never started.....aaargh");
  }

  while (myProcess.waitForReadyRead(-1)) {
  }

  QString myString;
  myString+=("--------- Output ----------\n");
  myProcess.setReadChannel(QProcess::StandardOutput);
  QByteArray myArray = myProcess.readAll();
  myString.append(myArray);
  myString+=("--------- Errors ----------\n");
  myProcess.setReadChannel(QProcess::StandardError);
  myArray = myProcess.readAll();
  myString.append(myArray);

  qDebug(myString.toLocal8Bit());

  qDebug("The process completed");
}

/*   NOTES and bash stuff
     if the wheat button is checked then
     if NOT a unique raster then
     get the area required for wheat and add it to total area 
     else run a seperate loop for wheat
     else add nothing to total area

     repeat for all crops

     bash code for the loop looks like this:

     euclidean () {   # =-FUNCTION-= to create raster using EUCLIDEAN DISTANCE
     area=0
     while [ ${area} -le ${land_reqrd_total} ]
     do #the magic loop
     (( radius = ${radius} + 30)) # <---- model precision value used HERE!
     r.circle -b output=circle coordinate=744800,3611100 max=${radius} --overwrite 
     g.remove rast=catchment
     r.mapcalc catchment="${src}"*circle
     echo a catchment area with a radius of ${radius} meters contains
     area=`r.stats -an input=catchment | awk '{printf("%d\n", $2);}'`
     echo ${area} square meters of land and our target is 
     echo ${land_reqrd_total} square meters of land
     done

# write info to history section of raster map
r.support map=catchment history="Radius was ${radius}"
r.support map=catchment history="This results in ${area} sq meters and the target was ${land_reqrd_total}"
r.support map=catchment history="Population was: ${popn}"
r.support map=catchment history="Expected avg BARLEY yield: ${barley_yield}"
r.support map=catchment history="Expected avg WHEAT yield: ${wheat_yield}"
r.support map=catchment history="Expected avg LENTIL yield: ${lentil_yield}"
r.support map=catchment history="BARLEY required per year per person (kg): ${barley_reqrd}"
r.support map=catchment history="WHEAT required per year per person (kg): ${wheat_reqrd}"
r.support map=catchment history="LENTILS required per year per person (kg): ${lentil_reqrd}"
# open a display and show results
d.mon x0
d.rast aster_band01@PERMANENT
d.rast -o catchment
}

*/

/*  binary serach algorythm
// function:
//   Searches sortedArray[first]..sortedArray[last] for key.  
// returns: index of the matching element if it finds key, 
//         otherwise  -(index where it could be inserted)-1.
// parameters:
//   sortedArray in  array of sorted (ascending) values.
//   first, last in  lower and upper subscript bounds
//   key         in  value to search for.
// returns:
//   index of key, or -insertion_position -1 if key is not 
//                 in the array. This value can easily be
//                 transformed into the position to insert it.

while (first <= last)
{
  int mid = (first + last) / 2;  // compute mid point.
  if (key > sortedArray[mid]) 
    first = mid + 1;  // repeat search in top half.
  else if (key < sortedArray[mid]) 
    last = mid - 1; // repeat search in bottom half.
  else
    return mid;     // found it. return position /////
}
return -(first + 1);    // failed to find key
}

*/
