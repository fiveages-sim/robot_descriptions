cmake_minimum_required(VERSION 3.8)
project(camera_models)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY meshes
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()