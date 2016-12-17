PROJECT(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


#This is needed for the dllexport mechanism
add_definitions(-DCXXPROF_PRELOADER)

#Build the actual component
set(Sources ${CMAKE_CURRENT_SOURCE_DIR}/example/src/interface/Warrior.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/example/src/plugin/Connector.cpp)

message(STATUS "SOURCES " ${Sources})
message(STATUS "CONAN_LIBS " ${CONAN_LIBS})

add_definitions("-std=c++11")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}
                    ${CMAKE_CURRENT_SOURCE_DIR}/example/src/interface
                    ${CONAN_INCLUDE_DIRS})
add_library(${PROJECT_NAME} SHARED ${Sources} ${Headers})
target_link_libraries(${PROJECT_NAME} PUBLIC ${CONAN_LIBS})

add_executable(example ${CMAKE_CURRENT_SOURCE_DIR}/example/src/host/Main.cpp)
target_link_libraries(example ${PROJECT_NAME})
