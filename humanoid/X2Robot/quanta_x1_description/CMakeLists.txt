cmake_minimum_required(VERSION 3.8)
project(quanta_x1_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY xacro urdf meshes
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()