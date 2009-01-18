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

#include <lagrass.h>
class LaGrassTest: public QObject
{
  Q_OBJECT;
      private slots:
      void runCommand();
      void getMapsetList();
      void getRasterList();
      void createFrictionMap();
};

void LaGrassTest::runCommand()
{
  LaGrass myGrass;
  QString myCommand = "g.list";
  QStringList myArguments;
  myArguments << "type=rast";
  //first test with no error log param
  QString myResult = myGrass.runCommand(myCommand,myArguments);
  QVERIFY(!myResult.isEmpty());
  //now test with error log
  QString myErrors;
  myResult = myGrass.runCommand(myCommand,myArguments,myErrors);
  QVERIFY(!myResult.isEmpty());
  QVERIFY(myErrors.isEmpty());
}
void LaGrassTest::getMapsetList()
{
  LaGrass myGrass;
  QStringList myList = myGrass.getMapsetList();
  QVERIFY(myList.count() > 0);
}
void LaGrassTest::getRasterList()
{
  QStringList myList;
  LaGrass myGrass;
  QStringList myMapsetList = myGrass.getMapsetList();
  QStringListIterator myIterator(myMapsetList);
  while (myIterator.hasNext())
  {
    //append the raster names in this mapet to our full list
    myList << myGrass.getRasterList(myIterator.next());
  }
  qDebug() << "\n" << myList.join("\n");
  QVERIFY(myList.count() > 0);
}
void LaGrassTest::createFrictionMap()
{
  LaGrass myGrass;
  myGrass.createFrictionMap("tim.dem","laFrictionMap");
}

QTEST_MAIN(LaGrassTest) 
#include "moc_lagrasstest.cxx"
  


