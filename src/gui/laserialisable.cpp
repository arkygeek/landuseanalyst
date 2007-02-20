/***************************************************************************
                          laserialisable.cpp  -  description
                             -------------------
    begin                : March 2006
    copyright            : (C) 2003 by Tim Sutton
    email                : tim@linfiniti.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include "laserialisable.h"
#include <QFile>
#include <QString>
#include <QTextStream>

LaSerialisable::LaSerialisable()
{
}
LaSerialisable::~LaSerialisable()
{
}
bool LaSerialisable::toXml(QString theFileName)
{
  bool myResult = false;
  QFile myFile( theFileName );
  if ( myFile.open( QIODevice::WriteOnly ) )
  {
    QTextStream myQTextStream( &myFile );
    myQTextStream << this->toXml();
    myFile.close();
    myResult=true;
  }
  else
  {
    //@TODO Error handler!
    myResult=false;
  }
  return myResult ;

}

bool LaSerialisable::fromXmlFile(QString theFileName)
{
  bool myResult = false;
  QFile myFile( theFileName );
  if ( myFile.open( QIODevice::ReadOnly ) )
  {
    myResult=this->fromXml(myFile.readAll());
    myFile.close();
  }
  else
  {
    qDebug("Failed to open "  + theFileName.toLocal8Bit() + " for deserialisation ");
    //@TODO Error handler!
    myResult=false;
  }
  return myResult ;
}

