cmake_minimum_required(VERSION 3.8)
project(robot_visualize_config)

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY config launch
        DESTINATION share/${PROJECT_NAME}/
)

ament_package()