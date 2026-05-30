cmake_minimum_required(VERSION 3.8)
project(rs01_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY xacro config urdf
  DESTINATION share/${PROJECT_NAME}/
)

install(
  DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
