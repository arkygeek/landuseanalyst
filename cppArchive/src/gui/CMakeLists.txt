cmake_minimum_required(VERSION 3.10)

if(COMMAND cmake_policy)
    cmake_policy(SET CMP0003 NEW)
    cmake_policy(SET CMP0005 NEW)
endif(COMMAND cmake_policy)
cmake_policy(SET CMP0006 NEW)

find_package(Qt5 COMPONENTS Core Gui Widgets REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(landuseanalyst_SRCS
    main.cpp
    lamainform.cpp
    lacropmanager.cpp
    lacropparametermanager.cpp
    laanimalmanager.cpp
    laanimalparametermanager.cpp
    laassemblageconversion.cpp
    lagrassprocess.cpp
)

add_executable(landuseanalyst
    ${landuseanalyst_SRCS}
)

target_link_libraries(landuseanalyst
     Qt5::Core
     Qt5::Gui
     Qt5::Widgets
     la_core
)

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
               )
  # For Mac OS X, the executable must be at the root of the bundle's executable folder
  INSTALL(TARGETS landuseanalyst RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX})
ELSE( NOT APPLE )
  # Remove console if on WIN32 and not Debug.
  IF (WIN32)
    IF (CMAKE_BUILD_TYPE MATCHES Debug)
      add_executable(landuseanalyst
        ${landuseanalyst_SRCS}
        )
    ELSE (CMAKE_BUILD_TYPE MATCHES Debug)
      #adding win32 below indicates no console display should be done
      add_executable(landuseanalyst WIN32
        ${landuseanalyst_SRCS}
        )
    ENDIF (CMAKE_BUILD_TYPE MATCHES Debug)
  ENDIF (WIN32)
  INSTALL(TARGETS landuseanalyst RUNTIME DESTINATION ${BIN_DIR})
ENDIF( APPLE )


# link the "landuseanalyst" target against the Qt libraries. which libraries
# exactly, is defined by the "include(${QT_USE_FILE})" line above, which sets up this variable.
target_link_libraries(landuseanalyst
     ${QT_LIBRARIES}
     la_core
     )
