cmake_minimum_required(VERSION 3.14)
project(ur5e_description)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY xacro config
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()
