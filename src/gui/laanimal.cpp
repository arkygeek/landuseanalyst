/***************************************************************************
                          omgserialisable.cpp  -  description
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

#include "omglayer.h"

LaAnimal::LaAnimal() : LaSerialisable()
{

}
LaAnimal::~LaAnimal()
{

}

//copy constructor
LaAnimal::LaAnimal(const LaAnimal& theAnimal)
{
  mName=theAnimal.name();
}

LaAnimal& LaAnimal::operator=(const LaAnimal& theAnimal)
{
  if (this == &theAnimal) return *this;   // Gracefully handle self assignment

  mName=theAnimal.name();
  // Put the normal assignment duties here...
  return *this;
}

QString LaAnimal::name() const
{
  return mName;
}

void LaAnimal::setName(QString theName)
{
  mName=theName;
}

QString LaAnimal::toXml()
{
  QString myString = QString("      <Animal Id=\"" 
      + mName.toLocal8Bit() 
      + "\"/>");
  return myString;
}

