/***************************************************************************
                          guid.h  -  description
                             -------------------
    begin                : Oct 2006
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

#ifndef LAGUID_H
#define LAGUID_H

#include <QString>
/** 
  * An abstract base class for any class that has a globally unique
  * identifier (GUID) to represent a unique instance.
  * @author Tim Sutton
  */

class LaGuid 
{
public:
  /** Constructor . */
  LaGuid();
  /** Desctructor . */
  virtual ~LaGuid();
  /** Retrieve the globally unique identifier */
  QString guid() const;
  /** Set the globally unique identifier for this object.
   *  If no Parameter is passed a guid will be self assigned
   *  @param theGuid - a guid for this model
   */
  void setGuid(QString theGuid="");  
private:
  /** A globally unique identifier for this model */
  QString mGuid;
};

#endif   //LAGUID_H

