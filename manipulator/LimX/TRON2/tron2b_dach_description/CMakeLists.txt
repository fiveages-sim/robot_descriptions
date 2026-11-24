cmake_minimum_required(VERSION 3.14)
project(tron2b_dach_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config meshes xacro DESTINATION share/${PROJECT_NAME})
install(FILES LICENSE DESTINATION share/${PROJECT_NAME})

ament_package()
