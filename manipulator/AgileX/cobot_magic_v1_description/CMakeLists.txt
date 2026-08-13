cmake_minimum_required(VERSION 3.14)
project(cobot_magic_v1_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY meshes xacro config
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()
