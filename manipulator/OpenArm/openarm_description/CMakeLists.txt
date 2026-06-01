cmake_minimum_required(VERSION 3.14)
project(openarm_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY meshes urdf xacro config
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()