import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction

import xacro


def process_xacro(robot):
    package_description = robot + "_description"
    pkg_path = os.path.join(get_package_share_directory(package_description))
    xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    return robot_description_config.toxml()


def generate_launch_description():
    robot = LaunchConfiguration('robot')
    rviz_config_file = os.path.join(get_package_share_directory("robot_visualize_config"), "config", "urdf.rviz")

    def launch_setup(context, *args, **kwargs):
        robot_value = context.launch_configurations['robot']
        robot_description = process_xacro(robot_value)
        return [
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                output='screen',
                arguments=["-d", rviz_config_file]
            ),
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output='screen',
                parameters=[
                    {
                        'publish_frequency': 100.0,
                        'use_tf_static': True,
                        'robot_description': robot_description
                    }
                ],
            ),
            Node(
                package='joint_state_publisher_gui',
                executable='joint_state_publisher_gui',
                name='joint_state_publisher',
                output='screen',
            )
        ]

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot',
            default_value='go2',
            description='Robot name to visualize'
        ),
        OpaqueFunction(function=launch_setup)
    ])