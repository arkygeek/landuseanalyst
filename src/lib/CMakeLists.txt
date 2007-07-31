#############################################################
# sources

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
  )
#headers that dont need to be MOCs but that may be distributed etc later
SET(LA_CORE_OTHER_HDRS
  laanimal.h
  laanimalparameter.h
  laguid.h
  lacrop.h
  lamodel.h
  lacropparameter.h
  lafoodsource.h
  laserialisable.h
  version.h
  )
#headers that need to be mocd
SET(LA_CORE_MOC_HDRS
  lamodel.h
  lagrass.h
  )

set(QT_USE_CORE TRUE)
set(QT_USE_GUI TRUE)
include(${QT_USE_FILE})

QT4_WRAP_CPP(LA_CORE_MOC_SRCS ${LA_CORE_MOC_HDRS})

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}
  ${QT_INCLUDE_DIR}
)

#############################################################
# library


ADD_LIBRARY(la_core SHARED ${LA_CORE_SRCS} ${LA_CORE_MOC_SRCS} )

# because of htonl
IF (WIN32)
  SET(PLATFORM_LIBRARIES wsock32)
ENDIF (WIN32)

TARGET_LINK_LIBRARIES(la_core
  ${QT_LIBRARIES}
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

# expect that classes are being EXPORTED for the lib
IF (WIN32)
  IF (MSVC)
    ADD_DEFINITIONS("-DCORE_EXPORT=__declspec(dllexport)")
  ELSE (MSVC)
    ADD_DEFINITIONS("-UCORE_EXPORT \"-DCORE_EXPORT=__declspec(dllexport)\"")
  ENDIF (MSVC)
ENDIF (WIN32)

