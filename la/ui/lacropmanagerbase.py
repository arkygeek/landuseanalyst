# -*- coding: utf-8 -*-
"""****************************************************************
 LanduseAnalyst - A QGIS plugin for determining the extent of the catchment area
 of a settlement (with respect to required land needed for food production).
 Land area targets for each food source supplied to the model are calculated based
 on a multitude of demographic and dietary inputs.
******************************************************************
    begin                : 2022-03-22
    copyright            : (C) 2022 by Dr. Jason S. Jorgenson
    email                : jjorgenson@gmail.com
    git sha              : $Format:%H$
******************************************************************
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
***************************************************************"""

import os
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUiType

# from qgis.PyQt import Qt
from qgis.PyQt.QtCore import QSettings, QPoint, QSize, Qt
from la.lib.lacrop import LaCrop
from la.lib.lautils import LaUtils
from la.gui.lacropmanager import LaCropManager
# from qgis.PyQt.QtWidgets import 

Ui_LaCropProfileManagerBase, _ = loadUiType(
    os.path.join(os.path.dirname(__file__), "../ui/lacropprofilemanagerbase.ui")
)

class LaCropProfileManagerBase(QDialog, Ui_LaCropProfileManagerBase):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(LaCropProfileManagerBase, self).__init__(parent, flags)
        self.setupUi(self)
        self.readSettings()
        self.lblCropPix.setScaledContents(True)
        self.tblCrops.cellClicked.connect(self.cellClicked)
        self.cbAreaUnits.addItem("Dunum")
        self.cbAreaUnits.addItem("Hectare")
        self.cbFodderEnergyType.addItem("KCalories")
        self.cbFodderEnergyType.addItem("TDN")
        self.refreshCropTable()

        # disable these buttons unless experimental is allowed
        self.pbnImport.setVisible(False)
        self.pbnExport.setVisible(False)

    def readSettings(self):
        mySettings = QSettings()
        pos = mySettings.value("mainwindow/pos", QPoint(200, 200))
        size = mySettings.value("mainwindow/size", QSize(400, 400))
        self.resize(size)
        self.move(pos)
		

    def writeSettings(self):
        # TODO: Implement this method
        pass
    
    def on_pbnCropPic_clicked(self):
        # TODO: Implement this method
        pass

    def refreshCropTable(self, theGuid=None):
        # TODO: Implement this method
        pass

    def cellClicked(self, theRow, theColumn):
        # TODO: Implement this method
        pass

    def selectCrop(self, theFileName):
        # TODO: Implement this method
        pass

    def showCrop(self):
        # TODO: Implement this method
        pass

    def on_pushButtonLoad_clicked(self):
        # TODO: Implement this method
        pass

    def on_pushButtonSave_clicked(self):
        # TODO: Implement this method
        pass

    def on_toolNew_clicked(self):
        # TODO: Implement this method
        pass

    def resizeEvent(self, theEvent):
        # TODO: Implement this method
        pass

    def on_toolCopy_clicked(self):
        # TODO: Implement this method
        pass

    def on_toolDelete_clicked(self):
        # TODO: Implement this method
        pass

    def on_pbnApply_clicked(self):
        # TODO: Implement this method
        pass




























""" # lacropmanagerbase.py from lacropmanagerbase.ui

import sys
from datetime import datetime, timezone, timedelta
import numpy as np
from enum import Enum

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtWidgets import QMessageBox, QToolTip, QStackedWidget, QHBoxLayout, QVBoxLayout, QSplitter, QFormLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem
from qgis.PyQt.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QHeaderView, QDialog
from qgis.PyQt.QtGui import QPainter, QBrush, QPen, QColor, QFont, QIcon
from qgis.PyQt.QtCore import Qt, QPoint, QRect, QObject, QEvent, pyqtSignal, pyqtSlot, QSize, QDir

## IMPORTS:
# from la.ui import lacropmanagerbase


class LaCropManagerBase(QDialog):
	def __init__(self, parent=None):
		super(LaCropManagerBase, self).__init__(parent)
		self.setupUi(self)
		self.initUI()
		self.show() # Show the GUI

	def initUI(self):
			pass

	def __str__(self):
 		return """

""" 

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
#ifndef LACROPMANAGER_H
#define LACROPMANAGER_H

  //QT Includes
#include <QDialog>
  //Local Includes
#include <ui_lacropmanagerbase.h>
#include <lacrop.h>
#include <lautils.h>
class QTreeWidgetItem;
/**
  This is the main gui class
  @author Tim Sutton, Jason Jorgenson
*/
class LaCropManager : public QDialog, private Ui::LaCropManagerBase
{
  Q_OBJECT
  public:
      LaCropManager(QWidget* parent = 0, Qt::WFlags fl = 0 );
      ~LaCropManager();

  public slots:
      void on_pushButtonLoad_clicked();
      void on_pushButtonSave_clicked();
      void on_pbnCropPic_clicked();

  private slots:
      void cellClicked(int theRow, int theColumn);
      void showCrop();
      void on_toolCopy_clicked();
      void on_toolNew_clicked();
      void on_toolDelete_clicked();
      void on_pbnApply_clicked();
      void resizeEvent(QResizeEvent*);

  private:
      void refreshCropTable(QString theGuid=0);
      void selectCrop(QString theFileName);

      LaUtils::CropMap mCropMap;
      LaCrop mCrop;
      void readSettings();
      void writeSettings();
      QString mImageFile;
};

#endif   //LACROPFORMMAIN_H


/***************************************************************************
 *   Copyright (C) 2007 by: Jason Jorgenson   arkygeek@gmail.com           *
 *             (c) 2007 by: Tim Sutton tim@linfiniti.com
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
#include "lacropmanager.h"
#include "lautils.h"
#include <QSettings>
#include <QTreeWidget>
#include <QTreeWidgetItem>
#include <QTableWidgetItem>
#include <QDir>
#include <QFile>
#include <QTextStream>
#include <QProcess>
#include <QStringList>
#include <QString>
#include <QMessageBox>
#include <QHeaderView>
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QFileDialog>
#include <QListWidgetItem>
#include <QDebug>

  LaCropManager::LaCropManager(QWidget* parent, Qt::WFlags fl)
: QDialog(parent,fl)
{
    //required by Qt4 to initialise the ui
  setupUi(this);
  readSettings();
  lblCropPix->setScaledContents(true);
  connect(tblCrops, SIGNAL(cellClicked( int,int)),
      this, SLOT(cellClicked( int,int)));
  cbAreaUnits->addItem("Dunum");
  cbAreaUnits->addItem("Hectare");
  cbFodderEnergyType->addItem("KCalories");
  cbFodderEnergyType->addItem("TDN");
  refreshCropTable();
    //disable these buttons unless experimental is allowed
  pbnImport->setVisible(false);
  pbnExport->setVisible(false);
}

LaCropManager::~LaCropManager()
{
  writeSettings();
}

void LaCropManager::readSettings()
{
  QSettings mySettings;
  QPoint pos = mySettings.value("mainwindow/pos", QPoint(200, 200)).toPoint();
  QSize size = mySettings.value("mainwindow/size", QSize(400, 400)).toSize();
  resize(size);
  move(pos);
}

void LaCropManager::writeSettings()
{
  QSettings mySettings;
  mySettings.setValue("mainwindow/pos", pos());
  mySettings.setValue("mainwindow/size", size());
}

void LaCropManager::on_pbnCropPic_clicked()
{
  LaUtils myUtils;
  QString myFile = myUtils.openGraphicFile();
  lblCropPix->setPixmap(myFile);
  mImageFile = myFile;
}

void LaCropManager::refreshCropTable(QString theGuid)
{

  mCropMap.clear();
  tblCrops->clear();
  tblCrops->setRowCount(0);
  tblCrops->setColumnCount(2);


    //we do this in two passes
    //in the first pass we populate a qmap with all the layersets
    //we find....
  mCropMap = LaUtils::getAvailableCrops();

    //the second pass populates the table
    //doing it from the map ensures that the rows
    //are sorted by layerset name

  int mySelectedRow=0;
  int myCurrentRow=0;
  QMapIterator<QString, LaCrop> myIterator(mCropMap);
  while (myIterator.hasNext())
  {
    myIterator.next();
    LaCrop myCrop = myIterator.value();
   // qDebug()JASONDIDTHIS<< myCrop.toText();
    if (theGuid.isEmpty())
    {
     // qDebug()JASONDIDTHIS<< "No default active row was requested.Assigning to myCrop.guid()!";
      theGuid=myCrop.guid();
    }
    if (myCrop.guid()==theGuid)
    {
      mySelectedRow=myCurrentRow;
    }
      // Insert new row ready to fill with details
    tblCrops->insertRow(myCurrentRow);
    QString myGuid = myCrop.guid();
   // qDebug()JASONDIDTHIS<< "Inserting crop with guid: " << myGuid;
      // Add details to the new row
    QTableWidgetItem *mypFileNameItem= new QTableWidgetItem(myGuid);
    tblCrops->setItem(myCurrentRow, 0, mypFileNameItem);
    QTableWidgetItem *mypNameItem = new QTableWidgetItem(myCrop.name());
    tblCrops->setItem(myCurrentRow, 1, mypNameItem);
      //display an icon indicating if the layerset is local or remote (e.g. terralib)
      //LaCrop::Origin myOrigin = myCrop.origin();
      //if (myOrigin==LaCrop::USERPROFILE)
      //{
    QIcon myIcon;
    myIcon.addFile(":/localdata.png");
    mypNameItem->setIcon(myIcon);
      //}
      //else if (myOrigin==LaCrop::ADAPTERPROFILE)
      //{
      //QIcon myIcon;
      //myIcon.addFile(":/remotedata.png");
      //mypNameItem->setIcon(myIcon);
      //}
      //else if (myOrigin==LaCrop::UNDEFINED)
      //{
      //  mypNameItem->setTextColor(Qt::yellow);
      //}
    myCurrentRow++;
  }

  if (myCurrentRow>0)
  {
    tblCrops->setCurrentCell(mySelectedRow,1);
    cellClicked(mySelectedRow,1);
  }
  else
  {
    on_toolNew_clicked();
  }
  QStringList headerLabels;
  headerLabels << "File Name" << "Name";
  tblCrops->setHorizontalHeaderLabels(headerLabels);
  tblCrops->setColumnWidth(0,0);
  tblCrops->setColumnWidth(1,tblCrops->width());
  tblCrops->horizontalHeader()->hide();
  tblCrops->verticalHeader()->hide();
  tblCrops->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropManager::cellClicked(int theRow, int theColumn)
{
    //note we use the alg name not the id because user may have customised params
 // qDebug()JASONDIDTHIS<< "LaCropManager::cellClicked";
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
 // qDebug()JASONDIDTHIS<< "Guid is: " << myGuid;
  QString myFileName = myGuid + ".xml";
  selectCrop(myFileName);
}
void LaCropManager::selectCrop(QString theFileName)
{
 // qDebug()JASONDIDTHIS<< "selectCrop Called : " << theFileName;
  QString myCropDir = LaUtils::userCropProfilesDirPath();
  LaCrop myCrop;
  myCrop.fromXmlFile(myCropDir + QDir::separator() + theFileName);
  leName->setText(myCrop.name());
  mCrop=myCrop;
  showCrop();
}

void LaCropManager::showCrop()
{
  leName->setText(mCrop.name());
  leDescription->setText(mCrop.description());
  sbCropYield->setValue(mCrop.cropYield());
  sbCropCalories->setValue(mCrop.cropCalories());
  sbCropFodderProduction->setValue(mCrop.fodderProduction());
  sbCropFodderValue->setValue(mCrop.fodderValue());
  cbAreaUnits->setCurrentIndex(mCrop.areaUnits());
  cbFodderEnergyType->setCurrentIndex(mCrop.cropFodderEnergyType());
  lblCropPix->setPixmap(mCrop.imageFile());
}

void LaCropManager::on_pushButtonLoad_clicked()
{
    //
  mCrop.fromXmlFile("/tmp/crop.xml");
  showCrop();
}

void LaCropManager::on_pushButtonSave_clicked()
{

}
void LaCropManager::on_toolNew_clicked()
{
 // qDebug()JASONDIDTHIS<< "New toolbutton clicked";
  LaCrop myCrop;
  myCrop.setGuid();
  mCrop = myCrop;
  showCrop();
}

void LaCropManager::resizeEvent ( QResizeEvent * theEvent )
{
  tblCrops->setColumnWidth(0,0);
  tblCrops->setColumnWidth(1,tblCrops->width());
  tblCrops->horizontalHeader()->setResizeMode(1,QHeaderView::Stretch);
}

void LaCropManager::on_toolCopy_clicked()
{
 // qDebug()JASONDIDTHIS<< "Copy toolbutton clicked";
  if (tblCrops->currentRow() < 0)
  {
    return;
  }
    //to clone, we get the algorithm guid that is currently selected
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
  if (myGuid.isEmpty())
  {
    return;
  }
  QString myOriginalFileName = LaUtils::userCropProfilesDirPath() + QDir::separator() + myGuid + ".xml";
  LaCrop myCrop;
  myCrop.fromXmlFile(myOriginalFileName);
  /*
  int myCount = 1;
  while (mCrop.contains(myProfileName))
  {
    myProfileName = tr("Copy ") + QString::number(myCount++) + " of " + myCrop.name();
  }
  */
    //assign this layerset its own guid
  myCrop.setGuid();
  QString myNewFileName = LaUtils::userCropProfilesDirPath() + QDir::separator() + myCrop.guid() + ".xml";
  myCrop.setName(tr("Copy of ") + myCrop.name());
  myCrop.toXmlFile(myNewFileName);
  refreshCropTable(myCrop.guid());
}
void LaCropManager::on_toolDelete_clicked()
{
 // qDebug()JASONDIDTHIS<< "Delete toolbutton clicked";
  if (tblCrops->currentRow() < 0)
  {
    return;
  }
  QString myGuid = tblCrops->item(tblCrops->currentRow(),0)->text();
  if (!myGuid.isEmpty())
  {
    QFile myFile(LaUtils::userCropProfilesDirPath() + QDir::separator() + myGuid + ".xml");
    if (!myFile.remove())
    {
      QMessageBox::warning(this, tr("Landuse Analyst"),
      tr("Unable to delete file \n") + myFile.fileName());
    }
    refreshCropTable();
  }
}
void LaCropManager::on_pbnApply_clicked()
{
  mCrop.setName(leName->text());
  mCrop.setDescription(leDescription->text());
  mCrop.setCropYield(sbCropYield->value());
  mCrop.setCropCalories(sbCropCalories->value());
  mCrop.setFodderProduction(sbCropFodderProduction->value());
  mCrop.setCropFodderValue(sbCropFodderValue->value());
  QString mySelectedAreaUnit = QString(cbAreaUnits->currentText());
  AreaUnits myAreaUnits;
  if (mySelectedAreaUnit == "Dunum")
  {
    myAreaUnits = Dunum;
    mCrop.setAreaUnits(myAreaUnits);
  }
  else if (mySelectedAreaUnit == "Hectare")
  {
    myAreaUnits = Hectare;
    mCrop.setAreaUnits(myAreaUnits);
  }

  mCrop.setImageFile(mImageFile);
  mCrop.toXmlFile( LaUtils::userCropProfilesDirPath() +
      QDir::separator() + mCrop.guid() + ".xml");
  refreshCropTable(mCrop.guid());
}



 """