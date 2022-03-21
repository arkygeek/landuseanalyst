#################################################################
#
#         QMAKE Project File for Landuse Analyst 
# 
#                      Tim Sutton 2006
#
#################################################################
message(******************** settings.pro ***********************)

#################################################################
#
#    all platforms - change these settings as you need them
#
#################################################################

unix:WORKDIR=$$system(pwd)
#a hack to get the current working dir under windows
win32:WORKDIR=$$system(cd)
message(Building in $${WORKDIR})
APP_NAME=LanduseAnalyst
#whether to build unit tests
TESTS=false
#whether to build console only applications
CONSOLE=false
#whether to build the qt designer plugins
DESIGNER=false
#whether to show experimental features to the user (set to true to hide 
#experimental features when making a release
ALLOW_EXPERIMENTAL=true
#whether to use to qgis mapping component
#at the moment it only builds on linux & windows :-(
USE_QGIS=true
#linux-g++:USE_QGIS=true

##################################################################
#  How Should We Build? Debug and release or release only???
##################################################################

#
# Building both debug and release versions (turned off by default)
#

#create both debug and relase makefiles
#CONFIG += debug_and_release
#build both release and debug targets when make is run
#CONFIG += build_all 

#
# Building release only version
#

CONFIG += release

#################################################################
#         Should not need to change below this point!!!!        #
#################################################################


#################################################################
##
## General compilation settings and defines
##
#################################################################
CONFIG += warn_off 
LANGUAGE  = C++
CONFIG += exceptions
# Require that there are no undefined symbols in any libs!
QMAKE_LFLAGS_SHLIB *= --no-undefined
#clear all qt modules - each pro should specify exactly which qt modules it wants
QT =

#################################################################
##
## Destination dir
##
#################################################################

# Where binary exes and libs should be placed when built
CONFIG(debug, debug|release){
  message(DEBUG?       : yes)
  # for ifdefs in code that should run only 
  # when debug support is enabled
  DEBUGMODE=true 
  DEFINES += $${APP_NAME}DEBUG=1
  APP_NAME=$${APP_NAME}-debug
  win32:CONFIG+=console
}else{
  message(DEBUG?       : no )
  APP_NAME=$${APP_NAME}-release
}
DESTDIR=$${WORKDIR}/$${APP_NAME}

#################################################################
#
# INSTALL PATHS
#
#################################################################

linux-g++:BINDIR=$${DESTDIR}/bin
win32:BINDIR=$${DESTDIR}
macx:BINDIR=$${DESTDIR}/$${APP_NAME}.app/Contents/MacOS/

linux-g++:LIBDIR=$${DESTDIR}/lib
macx:LIBDIR=$${BINDIR}
win32:LIBDIR=$${DESTDIR}

PLUGINDIR=$${DESTDIR}/lib/qgis
macx:PLUGINDIR=$${DESTDIR}/$${APP_NAME}.app/Contents/lib/qgis

PROVIDERDIR=$${BINDIR}/lib/qgis
macx:PROVIDERDIR=$${DESTDIR}/$${APP_NAME}.app/Contents/lib/qgis

win32:DOCDIR=$${DESTDIR}/share/qgis/doc
win32:DEVELOPERSIMAGEDIR=$${DESTDIR}/share/qgis/images/developers

message(WORKDIR      : $${WORKDIR})
message(DESTDIR      : $${DESTDIR})
message(BINDIR    : $${BINDIR})
message(LIBDIR    : $${LIBDIR})
message(PLUGINDIR : $${PLUGINDIR})

#################################################################
##
## Libraries to link to (used on a case by case basis as needed)
##
#################################################################

#QGISCORELIBADD=-lqgis_core
#CONFIG(debug, debug|release){
#  QGISCORELIBADD=$$member(QGISCORELIBADD, 0)-debug
#}

#not currently used since I had to incorporate composer into gui lib due to 
#cyclical dependency issues
#QGISCOMPOSERLIBADD=-lqgis_composer
#CONFIG(debug, debug|release){
#  QGISCOMPOSERLIBADD=$$member(QGISCOMPOSERLIBADD, 0)-debug
#}

#QGISGUILIBADD=-lqgis_gui
#CONFIG(debug, debug|release){
#  QGISGUILIBADD=$$member(QGISGUILIBADD, 0)-debug
#}

#win32:GDALLIBADD=-lgdal
#unix:GDALLIBADD=-lgdal
#macx:GDALLIBADD=-framework gdal

#SQLITELIBADD=-lsqlite3
#PROJLIBADD=-lproj
#GEOSLIBADD=-lgeos
#EXPATLIBADD=-lexpat

win32:LIBS += -lWs2_32

#################################################################
#
# Lib search paths (globally set for all pro files)
#
#################################################################

win32:LIBS+=-LC:\msys\local\lib
win32:LIBS+=-L$${DESTDIR}
#win32:LIBS+=-L$${DESTDIR}/lib/qgis
linux-g++:LIBS+=-L$${DESTDIR}/lib
macx:LIBS+=-L$${QGISLIBDIR}
macx:LIBS+=-F/Library/Frameworks/
macx:LIBS+=-L/usr/local/lib


#################################################################
#
# Include paths (globally set for all pro files)
#
#################################################################

contains(USE_QGIS,true){
  macx:QGISSRCDIR=/Users/timsutton/dev/cpp/qgis/src
  linux-g++:QGISSRCDIR=/home/timlinux/dev/cpp/qgis/src
  win32:QGISSRCDIR=c:/dev/cpp/qgis/src
  
  unix:INCLUDEPATH += $${QGISDIR}/include/qgis
  win32:INCLUDEPATH += $${QGISSRCDIR}
  win32:INCLUDEPATH += c:/mingw/include
  INCLUDEPATH +=$${QGISSRCDIR}/core \
                $${QGISSRCDIR}/gui \
                $${QGISSRCDIR}/plugins \
                $${QGISSRCDIR}/providers \
                $${QGISSRCDIR}/raster \
                $${QGISSRCDIR}/ui 
}

#
#   windows platform (MinGW) 
#

win32{
  message(Installing for windows!)
  INCLUDEPATH += . 
  INCLUDEPATH += C:/msys/local/include
}
INCLUDEPATH += $${OBJDIR}/ui 

#################################################################
#
#   windows platform (MinGW) 
#
#################################################################

win32{
  message(Installing for windows!)
  #add any win specific rules here 
  INCLUDEPATH += c:/msys/local/include
  GEOSINCADD = c:/msys/local/include/geos
  #PYTHONINCLUDE =  c:/Python25/include
  #PYTHONLIBADD = -Lc:/Python25/libs -lpython25
}


#################################################################
#
# MacOSX platform specific directives
#
#################################################################

macx{
  #fixme should not need the next line
  #INCLUDEPATH += /Users/timsutton/dev/cpp/om/src
  FRAMEWORKSDIR=$${DESTDIR}/$${APP_NAME}.app/Contents/Frameworks
  message (Checking if $${FRAMEWORKSDIR}/gdal.framework/gdal exists)
  exists( $${FRAMEWORKSDIR}/gdal.framework/gdal )
  {
    message(Gdal framework already in the bundle...skipping copy)
  }else{
    system(mkdir -p $${FRAMEWORKSDIR})
    system(cp -RP /Library/Frameworks/gdal.framework $${FRAMEWORKSDIR}/)
    message(Gdal framework copied into the bundle)
  }
  system(cp mac/Info.plist $${DESTDIR}/bin/$${APP_NAME}.app/Contents)
}


#################################################################
#
# Where intermediate build files should go
#
#################################################################

OBJDIR                =  $${WORKDIR}/obj
MOC_DIR               =  $${OBJDIR}/moc
UI_DIR                =  $${OBJDIR}/ui
macx:OBJECTS_DIR       =  $${OBJDIR}/o/mac
linux-g++:OBJECTS_DIR =  $${OBJDIR}/o/linux
win32:OBJECTS_DIR     =  $${OBJDIR}/o/win32
#These next two are not currently needed for this simple project
#RCC_DIR               =  $${OBJDIR}/rcc
