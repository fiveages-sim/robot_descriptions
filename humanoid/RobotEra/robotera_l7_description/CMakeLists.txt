cmake_minimum_required(VERSION 3.14)
project(robotera_l7_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY xacro config meshes
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
