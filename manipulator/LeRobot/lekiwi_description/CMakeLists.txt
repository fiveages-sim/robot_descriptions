cmake_minimum_required(VERSION 3.8)
project(lekiwi_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY meshes xacro urdf config
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()