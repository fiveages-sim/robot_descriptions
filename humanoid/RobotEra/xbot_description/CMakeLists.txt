cmake_minimum_required(VERSION 3.14)
project(xbot_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY meshes urdf xacro
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()