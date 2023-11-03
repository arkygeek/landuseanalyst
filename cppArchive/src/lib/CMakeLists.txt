find_package(Qt5 COMPONENTS Core Gui Widgets Xml REQUIRED) # Add Xml here

cmake_minimum_required(VERSION 3.10)

if(COMMAND cmake_policy)
    cmake_policy(SET CMP0003 NEW)
    cmake_policy(SET CMP0005 NEW)
endif(COMMAND cmake_policy)
cmake_policy(SET CMP0006 NEW)

find_package(Qt5 COMPONENTS Core Gui Xml REQUIRED)

set(CMAKE_AUTOMOC ON)

SET(LA_CORE_SRCS
  laanimal.cpp
  laanimalparameter.cpp
  laguid.cpp
  lacrop.cpp
  lacropparameter.cpp
  lafoodsource.cpp
  laserialisable.cpp
  lautils.cpp
  lamodel.cpp
  lagrass.cpp
  lagrassprocesslib.cpp
  ladietlabels.cpp
)

SET(LA_CORE_OTHER_HDRS
  la.h
  laanimal.h
  laanimalparameter.h
  laguid.h
  lacrop.h
  lamodel.h
  lacropparameter.h
  lafoodsource.h
  laserialisable.h
  version.h
  ladietlabels.h
)

SET(LA_CORE_MOC_HDRS
  lamodel.h
  lagrass.h
  lagrassprocesslib.h
)

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}
  ${QT_INCLUDE_DIR}
)

ADD_LIBRARY(la_core SHARED ${LA_CORE_SRCS})

IF (WIN32)
  SET(PLATFORM_LIBRARIES wsock32)
ENDIF (WIN32)

target_link_libraries(la_core
     Qt5::Core
     Qt5::Gui
     Qt5::QtXml
     ${PLATFORM_LIBRARIES}
)

IF (APPLE)
  INSTALL(TARGETS la_core
    RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}
    LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX})
ELSE (APPLE)
  INSTALL(TARGETS la_core
    RUNTIME DESTINATION ${LIB_DIR}
    LIBRARY DESTINATION ${LIB_DIR})
ENDIF (APPLE)

IF (WIN32)
  IF (MSVC)
    ADD_DEFINITIONS("-DCORE_EXPORT=__declspec(dllexport)")
  ELSE (MSVC)
    ADD_DEFINITIONS("-UCORE_EXPORT \"-DCORE_EXPORT=__declspec(dllexport)\"")
  ENDIF (MSVC)
ENDIF (WIN32)