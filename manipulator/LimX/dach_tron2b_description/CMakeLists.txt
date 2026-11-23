cmake_minimum_required(VERSION 3.14)
project(dach_tron2b_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch meshes xacro DESTINATION share/${PROJECT_NAME})
install(FILES LICENSE NOTICE THIRD_PARTY_NOTICES.md DESTINATION share/${PROJECT_NAME})

install(PROGRAMS scripts/home_grippers DESTINATION lib/${PROJECT_NAME})

ament_package()
