cmake_minimum_required(VERSION 3.10)

# if(COMMAND cmake_policy) 
#         cmake_policy(SET CMP0003 OLD) 
#         cmake_policy(SET CMP0005 OLD) 
# endif(COMMAND cmake_policy)  
# cmake_policy(SET CMP0006 OLD)

if(COMMAND cmake_policy)
  cmake_policy(SET CMP0003 NEW)
  cmake_policy(SET CMP0005 NEW)
endif(COMMAND cmake_policy)
cmake_policy(SET CMP0006 NEW)

# set(QT_USE_CORE TRUE)
# set(QT_USE_GUI TRUE)
# set(QT_USE_QTTEST TRUE)
# include(${QT_USE_FILE})

find_package(Qt5 COMPONENTS Core Gui Test REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)


#####################################################
# Don't forget to include output directory, otherwise
# the UI file won't be wrapped!
INCLUDE_DIRECTORIES(
  ${Qt5Core_INCLUDE_DIRS}
  ${Qt5Gui_INCLUDE_DIRS}
  ${Qt5Widgets_INCLUDE_DIRS}
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}/..
  ${CMAKE_CURRENT_BINARY_DIR}/../ui
  ${CMAKE_CURRENT_SOURCE_DIR} 
  ${CMAKE_CURRENT_SOURCE_DIR}/..
  ${CMAKE_CURRENT_SOURCE_DIR}/../lib
  ${CMAKE_CURRENT_SOURCE_DIR}/../widgets
  ${CMAKE_CURRENT_SOURCE_DIR}/../gui
  #${GDAL_INCLUDE_DIR}
  #${OM_INCLUDE_DIR}
  #${QGIS_INCLUDE_DIR}
  #${PROJ_INCLUDE_DIR}
  #${GEOS_INCLUDE_DIR}
)

# expect that classes are being IMPORTED for the exe
IF (WIN32)
  # expect that classes are being imported
  # Note: MSVC doesn't like when the macros are quotes
  # and MSYS doesn't like them unqouted (bacause of braces)
  IF (MSVC)
    ADD_DEFINITIONS("-DCORE_EXPORT=__declspec(dllimport)")
    ADD_DEFINITIONS("-DGUI_EXPORT=__declspec(dllexport)")
  ELSE (MSVC)
    ADD_DEFINITIONS("\"-DCORE_EXPORT=__declspec(dllimport)\"")
    ADD_DEFINITIONS("\"-DGUI_EXPORT=__declspec(dllexport)\"")
  ENDIF (MSVC)
ENDIF (WIN32)

#############################################################
# libraries

# because of htonl
IF (WIN32)
  SET(PLATFORM_LIBRARIES wsock32)
ENDIF (WIN32)

# Since the tests are not actually installed, but rather
# run directly from the build/src/tests dir we need to
# ensure the omg libs can be found.
IF (APPLE)
  # For Mac OS X, the executable must be at the root of the bundle's executable folder
  SET (CMAKE_INSTALL_NAME_DIR @executable_path/../lib)
ENDIF (APPLE)

MESSAGE("Test Data Dir: ${TEST_DATA_DIR}")
ADD_DEFINITIONS(-DTEST_DATA_DIR="\\"${TEST_DATA_DIR}\\"")
#note for tests we should not include the moc of our
#qtests in the executable file list as the moc is
#directly included in the sources
#and should not be compiled twice. Trying to include
#them in will cause an error at build time 

#############################################################
# Tests
# Add a block like the one below for each test that you
# create. You can run the tests using make test
#############################################################

# model test
MESSAGE ("Test Install Dir: ${LA_TEST_DIR}")
SET(modeltest_SRCS lamodeltest.cpp)
SET(modeltest_MOC_CPPS lamodeltest.cpp)
# QT4_WRAP_CPP(modeltest_MOC_SRCS ${modeltest_MOC_CPPS})
SET(CMAKE_AUTOMOC ON)
ADD_CUSTOM_TARGET(modeltestmoc ALL DEPENDS ${modeltest_MOC_SRCS})
ADD_EXECUTABLE(modeltest ${modeltest_SRCS})
ADD_DEPENDENCIES(modeltest modeltestmoc)
TARGET_LINK_LIBRARIES(modeltest ${QT_LIBRARIES} la_core)
INSTALL(TARGETS modeltest RUNTIME DESTINATION ${LA_TEST_DIR})
ADD_TEST(model ${LA_TEST_DIR}/modeltest)

# grass test
SET(grasstest_SRCS lagrasstest.cpp)
SET(grasstest_MOC_CPPS lagrasstest.cpp)
# QT4_WR.P_CPP(grasstest_MOC_SRCS ${grasstest_MOC_CPPS})
set(CMAKE_AUTOMOC ON)
ADD_CUSTOM_TARGET(grasstestmoc ALL DEPENDS ${grasstest_MOC_SRCS})
ADD_EXECUTABLE(grasstest ${grasstest_SRCS})
ADD_DEPENDENCIES(grasstest grasstestmoc)
TARGET_LINK_LIBRARIES(grasstest ${QT_LIBRARIES} la_core)
INSTALL(TARGETS grasstest RUNTIME DESTINATION ${LA_TEST_DIR})
ADD_TEST(grass ${LA_TEST_DIR}/grasstest)








# Put the libs needed into the test dir
MESSAGE ("Current Binary Dir: ${CMAKE_CURRENT_BINARY_DIR}")
IF (WIN32)
INSTALL (FILES ${CMAKE_BINARY_DIR}/src/lib/libla_core.dll DESTINATION ${LA_TEST_DIR})
ENDIF (WIN32)

IF (APPLE)
INSTALL (FILES ${CMAKE_BINARY_DIR}/src/lib/libla_core.dylib DESTINATION ${LA_TEST_DIR}/lib/)
#experiment tests need modeller plugins here
ENDIF (APPLE)
