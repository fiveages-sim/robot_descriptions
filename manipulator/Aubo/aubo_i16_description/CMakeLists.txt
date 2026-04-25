cmake_minimum_required(VERSION 3.8)
project(aubo_i16_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY meshes xacro urdf config launch rviz
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
