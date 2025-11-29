cmake_minimum_required(VERSION 3.12)
project(vectors_library VERSION 0.1.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python and pybind11
find_package(pybind11 REQUIRED)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src/vectors_cpp)

# Source files
set(SOURCES
    src/vectors_cpp/vector_core.cpp
    src/vectors_cpp/python_bindings.cpp
)

# Create the module
pybind11_add_module(_vectors_core ${SOURCES})

# Set output directory to match Python package structure
set_target_properties(_vectors_core PROPERTIES
    OUTPUT_NAME "_vectors_core"
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src/vectors
)

# Compiler-specific options
if(MSVC)
    target_compile_options(_vectors_core PRIVATE /W4)
else()
    target_compile_options(_vectors_core PRIVATE -Wall -Wextra -pedantic)
endif()

# Optimization options for release builds
set_target_properties(_vectors_core PROPERTIES
    CXX_VISIBILITY_PRESET "hidden"
)

