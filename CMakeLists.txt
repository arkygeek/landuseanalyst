project(landuseanalyst) # the name of your project

cmake_minimum_required(VERSION 2.4.0)

IF (WIN32)

  SET (BIN_DIR    ${CMAKE_INSTALL_PREFIX})
  SET (DATA_DIR   ${CMAKE_INSTALL_PREFIX})
  SET (PLUGIN_DIR ${CMAKE_INSTALL_PREFIX}/plugins)

ELSE (WIN32)

  IF (APPLE)
    # for Mac OS X, everything is put inside an application bundle
    SET (CMAKE_INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
    # path for library references
    SET (CMAKE_INSTALL_NAME_DIR @executable_path/lib)
    #set info.plist properties on mac
    SET( PROGNAME landuseanalyst)
    SET( MACOSX_BUNDLE_ICON_FILE landuseanalyst.icns)
    SET( MACOSX_BUNDLE_SHORT_VERSION_STRING 0.0.1 )
    SET( MACOSX_BUNDLE_VERSION 0.0.1 )
    SET( MACOSX_BUNDLE_LONG_VERSION_STRING Version 0.0.1 )
    SET( CMAKE_OSX_ARCHITECTURES ppc;i386 ) #Comment out if not universal binary
  ENDIF (APPLE)

  IF (UNIX AND NOT APPLE)
    SET (BIN_DIR    ${CMAKE_INSTALL_PREFIX}/bin)
    SET (DATA_DIR   ${CMAKE_INSTALL_PREFIX}/share/qgis)
    SET (PLUGIN_DIR ${CMAKE_INSTALL_PREFIX}/lib/qgis)
    ADD_DEFINITIONS(-DPREFIX=\\"${CMAKE_INSTALL_PREFIX}\\")
    ADD_DEFINITIONS(-DPLUGINPATH=\\"${PLUGIN_DIR}\\")
    ADD_DEFINITIONS(-DPKGDATAPATH=\\"${DATA_DIR}\\")
  ENDIF (UNIX AND NOT APPLE)

ENDIF (WIN32)

find_package(Qt4 REQUIRED) # find and setup Qt4 for this project

# tell cmake to process CMakeLists.txt in that subdirectory
add_subdirectory(src)

#############################################################
# Uninstall stuff see: http://www.vtk.org/Wiki/CMake_FAQ
CONFIGURE_FILE(
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake.in"
  "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
  IMMEDIATE @ONLY)

ADD_CUSTOM_TARGET(uninstall
  "${CMAKE_COMMAND}" -P "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake")
