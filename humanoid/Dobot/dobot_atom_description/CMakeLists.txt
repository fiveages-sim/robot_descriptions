cmake_minimum_required(VERSION 3.8)
project(dobot_atom_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY meshes xacro config
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()