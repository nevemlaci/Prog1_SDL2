cmake_minimum_required(VERSION 3.31)
project(prog1_sdl2 C)

set(CMAKE_C_STANDARD 11)

list(APPEND CMAKE_PREFIX_PATH external_dependencies)

find_package(SDL2 REQUIRED)
find_package(SDL2_image REQUIRED)
find_package(SDL2_ttf REQUIRED)

add_subdirectory(external_dependencies/SDL2_GFX)

add_executable(prog1_sdl2 main.c)

target_link_libraries(
        prog1_sdl2
        PRIVATE SDL2::SDL2main
        PRIVATE SDL2::SDL2
        PRIVATE SDL2_image::SDL2_image
        PRIVATE SDL2_ttf::SDL2_ttf
        PRIVATE sdl2_gfx_static
)

include(cmake/copy_dlls.cmake)

copy_depend_dlls(prog1_sdl2)