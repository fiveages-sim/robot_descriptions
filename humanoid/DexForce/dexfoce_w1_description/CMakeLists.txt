cmake_minimum_required(VERSION 3.14)
project(dexforce_w1_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY xacro meshes config
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()
