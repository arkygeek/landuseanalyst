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


#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include "zintatuform.h"
//qt includes
#include <QApplication>
#include <QSplashScreen>
#include <QSettings>
#include <QString>
#include <QPixmap>
#include <QBitmap>
#include <QFile>
//std includes
#ifdef Q_OS_MACX
#include <ApplicationServices/ApplicationServices.h>
#endif

int main(int argc, char *argv[])
{
  QApplication  myApp(argc,argv);

  //NOTE: make sure these lines stay after myApp init above
  QCoreApplication::setOrganizationName("linfiniti.com");
  QCoreApplication::setOrganizationDomain("zintatu.linfiniti.com");
  QCoreApplication::setApplicationName("zintatu");
	
#ifdef Q_OS_MACX
  // Install OpenDocuments AppleEvent handler after application object is initialized
  // but before any other event handling (including dialogs or splash screens) occurs.
  // If an OpenDocuments event has been created before the application was launched,
  // it must be handled before some other event handler runs and dismisses it as unknown.
  // If run at startup, the handler will set either or both of myProjectFileName and myFileList.
  //AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments, openDocumentsAEHandler, 0, false);

  // If the QtCore framework is bundled with the application, clear the library search path
  // and look for Qt plugins only within the application bundle.
  QString bundledQtCore(QCoreApplication::applicationDirPath().append("/lib/QtCore.framework"));
  if (QFile::exists(bundledQtCore))
  {
    QCoreApplication::setLibraryPaths(QStringList(QCoreApplication::applicationDirPath()));
  }
#endif

	//dont display the splash on first run...
	QSettings mySettings;
	if (mySettings.value("firstRun/firstRun",true).toBool()==false)
	{
		QPixmap myPixmap(":/zintatu_logo.png");
		QSplashScreen *mypSplash = new QSplashScreen(myPixmap);
		QPixmap myMaskPixmap(":/zintatu_logo_mask.png", 0, Qt::ThresholdDither |   Qt::ThresholdAlphaDither | Qt::AvoidDither );
		mypSplash->setMask( myMaskPixmap.createHeuristicMask() );
		mypSplash->show();

		ZintatuForm * mypZintatu = new ZintatuForm();
		mypZintatu->show();
		mypSplash->finish(mypZintatu);
		delete mypSplash;
		// note if the widget does not inherit qdialog
		// (as in the case of our main window)
		// you must call app exec!
	}
	else
	{
		ZintatuForm * mypZintatu = new ZintatuForm();
		mypZintatu->show();
	}
  return myApp.exec();
}
/* Test to determine if this program was started on Mac OS X by double-clicking
 * the application bundle rather then from a command line. If clicked, argv[1]
 * contains a process serial number in the form -psn_0_1234567. Don't process
 * the command line arguments in this case because argv[1] confuses the processing.
 */
bool bundleclicked(int argc, char *argv[])
{
  return ( argc > 1 && memcmp(argv[1], "-psn_", 5) == 0 );
}

