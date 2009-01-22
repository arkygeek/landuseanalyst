/***************************************************************************
                          laserialisable.h  -  description
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

#ifndef LASERIALISABLE_H
#define LASERIALISABLE_H

class QString;
#include <QFile>
/** 
  * An abstract base class for any class that is serialiseable to xml
  * @author Tim Sutton
  */

class LaSerialisable 
{
public:
    /** Constructor . */
    LaSerialisable();
    /** Desctructor . */
    virtual ~LaSerialisable();
    /** Write this object to xml and return result as qstring (virtual) . */
    virtual QString toXml()=0;
    /** Write this object to xml and return result as qstring (virtual).
     *  We provide a basic default implementation where given a file name,
     *  we will write the serialised xml to that file.
     * Internally it uses toXml() method above so that must be properly implemented.
     */
    virtual bool toXmlFile(const QString theFileName);
    /** Read this object from xml and return result as true for success, false for failure (virtual). */
    virtual bool fromXml(const QString theXml)=0;
    /** Read this object from xml in a file and return result as true for success, false for failure.
     * Internally it uses fromXml(QString) method above so that must be properly implemented.
     */
    virtual bool fromXmlFile(const QString theFileName);
};

#endif   //LASERIALISABLE_H

