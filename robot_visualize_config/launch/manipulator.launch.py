import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction

import xacro


def process_xacro(robot, arm_type=None):
    package_description = robot + "_description"
    pkg_path = os.path.join(get_package_share_directory(package_description))
    xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')
    
    # 如果指定了arm_type，则传递给xacro，否则不传递
    if arm_type and arm_type.strip():
        mappings = {'type': arm_type}
        robot_description_config = xacro.process_file(xacro_file, mappings=mappings)
    else:
        robot_description_config = xacro.process_file(xacro_file)
    
    return robot_description_config.toxml()


def generate_launch_description():
    robot = LaunchConfiguration('robot')
    rviz_config_file = os.path.join(get_package_share_directory("robot_visualize_config"), "config", "manipulator.rviz")

    def launch_setup(context, *args, **kwargs):
        robot_value = context.launch_configurations['robot']
        arm_type_value = context.launch_configurations.get('type', '')
        robot_description = process_xacro(robot_value, arm_type_value)
        return [
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz_ocs2',
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
            default_value='piper',
            description='Robot name to visualize'
        ),
        DeclareLaunchArgument(
            'type',
            default_value='',
            description='Type of the manipulator arm (empty means no type parameter passed to xacro)'
        ),
        OpaqueFunction(function=launch_setup)
    ])