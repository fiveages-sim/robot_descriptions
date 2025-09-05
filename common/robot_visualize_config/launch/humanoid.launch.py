import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction

import xacro


def process_xacro(robot, arm_end_effector=None, collider=None):
    package_description = robot + "_description"
    pkg_path = os.path.join(get_package_share_directory(package_description))
    xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')
    
    # 构建mappings字典
    mappings = {}
    
    # 如果指定了arm_end_effector，则传递给xacro
    if arm_end_effector and arm_end_effector.strip():
        mappings['end_effector'] = arm_end_effector
    
    # 如果指定了collider，则传递给xacro
    if collider and collider.strip():
        mappings['collider'] = collider
    
    # 根据mappings是否为空来决定如何处理xacro文件
    if mappings:
        robot_description_config = xacro.process_file(xacro_file, mappings=mappings)
    else:
        robot_description_config = xacro.process_file(xacro_file)
    
    return robot_description_config.toxml()


def generate_launch_description():
    robot = LaunchConfiguration('robot')
    rviz_config_file = os.path.join(get_package_share_directory("robot_visualize_config"), "config", "humanoid.rviz")

    def launch_setup(context, *args, **kwargs):
        robot_value = context.launch_configurations['robot']
        arm_end_effector_value = context.launch_configurations.get('end_effector', '')
        collider_value = context.launch_configurations.get('collider', '')
        robot_description = process_xacro(robot_value, arm_end_effector_value, collider_value)
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
            default_value='unitree_g1',
            description='Robot name to visualize'
        ),
        DeclareLaunchArgument(
            'end_effector',
            default_value='',
            description='end_effector of the manipulator arm (empty means no end_effector parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'collider',
            default_value='',
            description='Collider type of the manipulator arm (empty means no collider parameter passed to xacro)'
        ),
        OpaqueFunction(function=launch_setup)
    ])