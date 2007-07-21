/***************************************************************************
 *             Globally useful typedefs and defines
 *
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

#ifndef LA
#define LA

#include <QMap>
#include <QPair>
#include <QString>

//    <animal guid <enabled, animalparamters guid>>
//    or
//    <plant guid <enabled, animalparamters guid>>
typedef QMap <QString,QPair<bool,QString> > LaTripleMap;

//    LaFoodSource is a map < <Guid,enabled> , <Fodder,Grain> >
//    or
//    LaFoodSource is a map < <Guid,disabled> , <Fodder,Grain> >
typedef QMap < QPair<QString,bool> , QPair<int,int> > LaFoodSourceMap;

enum Priority {None, High, Medium, Low};
enum Status {MoreThanEnoughToCompletelySatisfy, NotEnoughToCompletelySatisfy};
enum LandBeingGrazed {Common, Unique};
#endif //LA
