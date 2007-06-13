set(QT_USE_CORE TRUE)
set(QT_USE_GUI TRUE)
set(QT_USE_QTTEST TRUE)
include(${QT_USE_FILE})
#####################################################
# Don't forget to include output directory, otherwise
# the UI file won't be wrapped!
INCLUDE_DIRECTORIES(
  ${QT_INCLUDE_DIR}
# binary make output dirs for uics and mocs
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}/..
  ${CMAKE_CURRENT_BINARY_DIR}/../ui
# source dirs
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

IF (WIN32)
  SET (DEST ${CMAKE_INSTALL_PREFIX})
ELSE (WIN32)
  SET (DEST ${CMAKE_CURRENT_BINARY_DIR})
ENDIF (WIN32)

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
SET(modeltest_SRCS lamodeltest.cpp)
SET(modeltest_MOC_CPPS lamodeltest.cpp)
QT4_WRAP_CPP(modeltest_MOC_SRCS ${modeltest_MOC_CPPS})
ADD_CUSTOM_TARGET(modeltestmoc ALL DEPENDS ${modeltest_MOC_SRCS})
ADD_EXECUTABLE(modeltest ${modeltest_SRCS})
ADD_DEPENDENCIES(modeltest modeltestmoc)
TARGET_LINK_LIBRARIES(modeltest ${QT_LIBRARIES} la_core)
INSTALL(TARGETS modeltest RUNTIME DESTINATION ${DEST})
ADD_TEST(model ${DEST}/modeltest)

