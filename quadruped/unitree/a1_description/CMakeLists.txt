cmake_minimum_required(VERSION 3.8)
project(a1_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY meshes xacro config urdf
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()