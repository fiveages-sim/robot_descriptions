cmake_minimum_required(VERSION 3.8)
project(arx5_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY meshes urdf xacro config
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()