PROJECT(Pluma)
cmake_minimum_required(VERSION 2.8)

file(GLOB HEADERS ${CMAKE_SOURCE_DIR}/Pluma-1.1/include/Pluma/*)
file(GLOB SOURCES ${CMAKE_SOURCE_DIR}/Pluma-1.1/src/Pluma/*)

include_directories(${CMAKE_SOURCE_DIR}/Pluma-1.1/include ${CMAKE_SOURCE_DIR}/Pluma-1.1/src/)
add_library(Pluma STATIC ${SOURCES})
target_link_libraries(Pluma ${CONAN_LIBS})

install(FILES ${HEADERS} DESTINATION include/Pluma)
install(TARGETS Pluma
        ARCHIVE DESTINATION ${PROJECT_NAME}/lib
        LIBRARY DESTINATION ${PROJECT_NAME}/lib
        RUNTIME DESTINATION ${PROJECT_NAME}/bin)
