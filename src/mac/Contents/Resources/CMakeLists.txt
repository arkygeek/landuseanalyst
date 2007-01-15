FILE (GLOB ICONS *.icns)
INSTALL (FILES ${ICONS}
         DESTINATION ${CMAKE_INSTALL_PREFIX}/landuseanalyst.app/Contents/Resources)
