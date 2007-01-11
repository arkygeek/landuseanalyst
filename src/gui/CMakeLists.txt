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
   )
SET(landuseanalyst_UIS
    ../ui/lamainformbase.ui
    )
SET(landuseanalyst_MOC_HDRS
    lamainform.h
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
include_directories(${CMAKE_CURRENT_BINARY_DIR})

#Now add these generated files to the ADD_EXECUTABLE step
# If this is NOT done, then the ui_*.h files will not be generated
# ditto for moc, rc etc files
# create an executable file named "landuseanalyst" from the source 
# files in the variable "landuseanalyst_SRCS".
add_executable(landuseanalyst 
               ${landuseanalyst_SRCS} 
               ${landuseanalyst_UIS_H} 
               ${landuseanalyst_MOC_SRCS}
               ${landuseanalyst_RCC_SRCS}
               )

# link the "landuseanalyst" target against the Qt libraries. which libraries 
# exactly, is defined by the "include(${QT_USE_FILE})" line above, which sets up this variable.
target_link_libraries(landuseanalyst ${QT_LIBRARIES})

# install destination for the built binary
install(TARGETS landuseanalyst DESTINATION bin)
