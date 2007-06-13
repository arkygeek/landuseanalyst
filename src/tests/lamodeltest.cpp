/***************************************************************************
 *   Copyright (C) 2005 by Tim Sutton   *
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
#include <QtTest/QtTest>
#include <QString>

#include <lamodel.h>
#include <lautils.h>
class LaModelTest: public QObject
{
  Q_OBJECT;
      private slots:
      void run();
      void saveAndLoadModel();
};

void LaModelTest::saveAndLoadModel()
{
  LaModel myModel;
  QString myFileName;
  //@TODO make this OS agnostic...
  myFileName = "/tmp/" + myModel.guid() + ".xml";
  LaUtils::createTextFile( myFileName , myModel.toXml());
  LaModel myModel2;
  myModel2.fromXmlFile(myFileName);
  QVERIFY(myModel2.guid()==myModel.guid());
}
void LaModelTest::run()
{
  QString myFileName += "/../../../test_data/modelOutputs/24a192e7-dbb8-4531-b1c5-b9b2718614a2.xml";
  LaModel myModel;
  myModel.fromXmlFile(myFileName);
  //myModel.run();
}

QTEST_MAIN(LaModelTest) 
#include "moc_lamodeltest.cxx"
  

