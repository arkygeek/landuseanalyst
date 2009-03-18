# Install script for directory: /Users/arkygeek/devel/landuseanalyst/src/gui

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/Users/arkygeek/apps")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  IF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    FILE(INSTALL DESTINATION "/Users/arkygeek/apps" TYPE DIRECTORY FILES "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Debug/landuseanalyst.app" USE_SOURCE_PERMISSIONS)
    IF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
      EXECUTE_PROCESS(COMMAND "/usr/bin/install_name_tool"
        -change "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Debug/libla_core.dylib" "@executable_path/lib/libla_core.dylib"
        "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
    ENDIF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
  ENDIF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
  IF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    FILE(INSTALL DESTINATION "/Users/arkygeek/apps" TYPE DIRECTORY FILES "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/Release/landuseanalyst.app" USE_SOURCE_PERMISSIONS)
    IF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
      EXECUTE_PROCESS(COMMAND "/usr/bin/install_name_tool"
        -change "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/Release/libla_core.dylib" "@executable_path/lib/libla_core.dylib"
        "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
    ENDIF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
  ENDIF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
  IF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
    FILE(INSTALL DESTINATION "/Users/arkygeek/apps" TYPE DIRECTORY FILES "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/MinSizeRel/landuseanalyst.app" USE_SOURCE_PERMISSIONS)
    IF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
      EXECUTE_PROCESS(COMMAND "/usr/bin/install_name_tool"
        -change "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/MinSizeRel/libla_core.dylib" "@executable_path/lib/libla_core.dylib"
        "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
    ENDIF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
  ENDIF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Mm][Ii][Nn][Ss][Ii][Zz][Ee][Rr][Ee][Ll])$")
  IF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    FILE(INSTALL DESTINATION "/Users/arkygeek/apps" TYPE DIRECTORY FILES "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/gui/RelWithDebInfo/landuseanalyst.app" USE_SOURCE_PERMISSIONS)
    IF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
      EXECUTE_PROCESS(COMMAND "/usr/bin/install_name_tool"
        -change "/Users/arkygeek/devel/landuseanalyst/buildXCODE/src/lib/RelWithDebInfo/libla_core.dylib" "@executable_path/lib/libla_core.dylib"
        "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
    ENDIF(EXISTS "$ENV{DESTDIR}/Users/arkygeek/apps/landuseanalyst.app/Contents/MacOS/landuseanalyst")
  ENDIF("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

