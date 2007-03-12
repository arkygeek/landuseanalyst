# the next line sets up include and link directories and defines some variables that we will use.
# you can modify the behavior by setting some variables, e.g.
#   set(QT_USE_OPENGL TRUE)
# -> this will cause cmake to include and link against the OpenGL module
set(QT_USE_CORE TRUE)
set(QT_USE_GUI TRUE)
include(${QT_USE_FILE})

# the variable "landuseanalyst_SRCS" contains all .cpp files of this project
set(landuseanalyst_SRCS
    main.cpp
    lamainform.cpp
    lacropmanager.cpp
    lacropparametermanager.cpp
    laanimalmanager.cpp
    laanimalparametermanager.cpp
   )
SET(landuseanalyst_UIS
    ../ui/lamainformbase.ui
    ../ui/lacropmanagerbase.ui
    ../ui/lacropparametermanagerbase.ui
    ../ui/laanimalmanagerbase.ui
    ../ui/laanimalparametermanagerbase.ui
    )
SET(landuseanalyst_MOC_HDRS
    lamainform.h
    lacropmanager.h
    lacropparametermanager.h
    laanimalmanager.h
    laanimalparametermanager.h
    )
SET(landuseanalyst_RCCS
    ../resources/resources.qrc
    )

# tell cmake to create .moc files for all files in the variable landuseanalyst_SRCS that require such a file.
# note: this assumes that you use #include "header.moc" in your files
qt4_automoc(${landuseanalyst_SRCS})

# tell cmake to create ui_ files for everything specified in landuseanalyst_UIS
QT4_WRAP_UI(landuseanalyst_UIS_H ${landuseanalyst_UIS})

#tell cmake to generate moc_ files for everything specified in landuseanalyst_MOCS
QT4_WRAP_CPP(landuseanalyst_MOC_SRCS ${landuseanalyst_MOC_HDRS})

# tell cmake to generate resources
QT4_ADD_RESOURCES(landuseanalyst_RCC_SRCS ${landuseanalyst_RCCS})

# Don't forget to include output directory, otherwise
# the UI file won't be wrapped!
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/../lib
    )

# application icon
IF (WIN32)
  IF( MINGW )
    # resource compilation for MinGW
    ADD_CUSTOM_COMMAND( OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/icon.o
      COMMAND windres.exe -I${CMAKE_CURRENT_SOURCE_DIR} -i${CMAKE_CURRENT_SOURCE_DIR}/landuseanalyst.rc
      -o ${CMAKE_CURRENT_BINARY_DIR}/icon.o )
    SET(landuseanalyst_SRCS ${landuseanalyst_SRCS} ${CMAKE_CURRENT_BINARY_DIR}/icon.o)
  ELSE( MINGW )
    SET(landuseanalyst_SRCS ${landuseanalyst_SRCS} landuseanalyst.rc)
  ENDIF( MINGW )
ENDIF (WIN32)


#Now add these generated files to the ADD_EXECUTABLE step
# If this is NOT done, then the ui_*.h files will not be generated
# ditto for moc, rc etc files
# create an executable file named "landuseanalyst" from the source
# files in the variable "landuseanalyst_SRCS".
IF( APPLE )
  add_executable(landuseanalyst
               MACOSX_BUNDLE
               ${landuseanalyst_SRCS}
               ${landuseanalyst_UIS_H}
               ${landuseanalyst_MOC_SRCS}
               ${landuseanalyst_RCC_SRCS}
               )
  # For Mac OS X, the executable must be at the root of the bundle's executable folder
  INSTALL(TARGETS landuseanalyst RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX})
ELSE( NOT APPLE )
  # Remove console if on WIN32 and not Debug.
  IF (WIN32)
    IF (CMAKE_BUILD_TYPE MATCHES Debug)
      add_executable(landuseanalyst
        ${landuseanalyst_SRCS}
        ${landuseanalyst_UIS_H}
        ${landuseanalyst_MOC_SRCS}
        ${landuseanalyst_RCC_SRCS}
        )
    ELSE (CMAKE_BUILD_TYPE MATCHES Debug)
      #adding win32 below indicates no console display should be done
      add_executable(landuseanalyst WIN32
        ${landuseanalyst_SRCS}
        ${landuseanalyst_UIS_H}
        ${landuseanalyst_MOC_SRCS}
        ${landuseanalyst_RCC_SRCS}
        )
      ADD_EXECUTABLE(landuseanalyst WIN32 ${landuseanalyst_SRCS})
    ENDIF (CMAKE_BUILD_TYPE MATCHES Debug)
  ELSE (WIN32)
    add_executable(landuseanalyst
      ${landuseanalyst_SRCS}
      ${landuseanalyst_UIS_H}
      ${landuseanalyst_MOC_SRCS}
      ${landuseanalyst_RCC_SRCS}
      )
  ENDIF (WIN32)
  INSTALL(TARGETS landuseanalyst RUNTIME DESTINATION ${BIN_DIR})
ENDIF( APPLE )


# link the "landuseanalyst" target against the Qt libraries. which libraries
# exactly, is defined by the "include(${QT_USE_FILE})" line above, which sets up this variable.
target_link_libraries(landuseanalyst 
     ${QT_LIBRARIES}
     la_core
     )
