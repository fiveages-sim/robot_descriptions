import os
import re

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction

import xacro


def get_default_type_from_xacro(xacro_file):
    """从xacro文件中读取type参数的默认值"""
    try:
        with open(xacro_file, 'r') as f:
            content = f.read()
            # 查找 xacro:arg name="type" default="..." 的模式
            match = re.search(r'xacro:arg\s+name=["\']type["\']\s+default=["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read default type from {xacro_file}: {e}")
    return None


def process_xacro(gripper, gripper_type=None, collider=None):
    package_description = gripper + "_description"
    pkg_path = os.path.join(get_package_share_directory(package_description))
    xacro_file = os.path.join(pkg_path, 'xacro', 'gripper.xacro')
    
    # 构建mappings字典
    mappings = {}
    
    # 如果指定了type，则传递给xacro
    if gripper_type and gripper_type.strip():
        mappings['type'] = gripper_type
    else:
        # 如果没有指定type，尝试从xacro文件读取默认值
        default_type = get_default_type_from_xacro(xacro_file)
        if default_type:
            mappings['type'] = default_type
        # 如果无法读取默认值，则不传递type参数，让xacro使用其默认值
    
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
    rviz_config_file = os.path.join(get_package_share_directory("robot_visualize_config"), "config", "gripper.rviz")

    def launch_setup(context, *args, **kwargs):
        gripper_value = context.launch_configurations['gripper']
        gripper_type_value = context.launch_configurations.get('type', '')
        collider_value = context.launch_configurations.get('collider', '')
        robot_description = process_xacro(gripper_value, gripper_type_value, collider_value)
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
            'gripper',
            default_value='robotiq',
            description='gripper name to visualize'
        ),
        DeclareLaunchArgument(
            'type',
            default_value='',
            description='Type of the manipulator arm (empty means no type parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'collider',
            default_value='',
            description='Collider type of the manipulator arm (empty means no collider parameter passed to xacro)'
        ),
        OpaqueFunction(function=launch_setup)
    ])