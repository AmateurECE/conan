cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++17")

message("CONAN_LIBS=${CONAN_LIBS}")
add_executable(fsadaptortest fsadaptortest.cpp)
target_link_libraries(fsadaptortest ${CONAN_LIBS})
target_include_directories(fsadaptortest PRIVATE
    ${CONAN_INCLUDE_DIRS}
)
