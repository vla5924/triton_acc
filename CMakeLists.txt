option(TRITON_ACC_BUILD_BACKEND "Build triton-shared Acc backend" ON)

set(TRITON_ACC_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
set(TRITON_ACC_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_BINARY_DIR}/include) # Tablegen'd files
add_subdirectory(include)
add_subdirectory(lib)

if (TRITON_ACC_BUILD_BACKEND)
  add_subdirectory(python)
endif()
