cmake_minimum_required(VERSION 3.8)
project(BruteForce)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp Operation.cpp Operation.h StringMatching.cpp StringMatching.h)
add_executable(BruteForce ${SOURCE_FILES})