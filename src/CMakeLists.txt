
# tell cmake to process CMakeLists.txt in that subdirectory
#add_subdirectory(resources)
#add_subdirectory(ui)
add_subdirectory(lib)
add_subdirectory(gui)
IF (ENABLE_TESTS)
  add_subdirectory(tests)
ENDIF (ENABLE_TESTS)

IF (APPLE)
  add_subdirectory(mac)
ENDIF(APPLE)

