/***************************************************************************
                          laguid.cpp  -  description
                             -------------------
    begin                : Sept 2006
    copyright            : (C) 2006 by Tim Sutton
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

#include "laguid.h"
#include <QUuid>

LaGuid::LaGuid()
{
}
LaGuid::~LaGuid()
{
}
const QString LaGuid::guid()
{
  return mGuid;
}

void LaGuid::setGuid(QString theGuid)
{
  if (theGuid.isEmpty())
  {
    mGuid=QUuid::createUuid().toString().replace("{","").replace("}","");
  }
  else
  {
    mGuid=theGuid;
  }
}
