cmake_minimum_required(VERSION 3.8)
project(agibot_g1_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY meshes urdf xacro
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()