import os
import re

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction

import xacro


def get_default_type_from_xacro(xacro_file):
    """Read default type parameter value from xacro file"""
    try:
        with open(xacro_file, 'r') as f:
            content = f.read()
            # Find pattern xacro:arg name="type" default="..."
            match = re.search(r'xacro:arg\s+name=["\']type["\']\s+default=["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read default type from {xacro_file}: {e}")
    return None


def process_xacro(hand, hand_type=None, collider=None, direction=None):
    package_description = hand + "_description"
    pkg_path = os.path.join(get_package_share_directory(package_description))
    xacro_file = os.path.join(pkg_path, 'xacro', 'hand.xacro')
    
    # Build mappings dictionary
    mappings = {}
    
    # If type is specified, pass it to xacro
    if hand_type and hand_type.strip():
        mappings['type'] = hand_type
    else:
        # If no type specified, try to read default value from xacro file
        default_type = get_default_type_from_xacro(xacro_file)
        if default_type:
            mappings['type'] = default_type
        # If cannot read default value, don't pass type parameter, let xacro use its default
    
    # If collider is specified, pass it to xacro
    if collider and collider.strip():
        mappings['collider'] = collider
    
    # If direction is specified, pass it to xacro
    if direction and direction.strip():
        mappings['direction'] = direction
    
    # Process xacro file based on whether mappings is empty or not
    if mappings:
        robot_description_config = xacro.process_file(xacro_file, mappings=mappings)
    else:
        robot_description_config = xacro.process_file(xacro_file)
    
    return robot_description_config.toxml()


def generate_launch_description():
    rviz_config_file = os.path.join(get_package_share_directory("robot_visualize_config"), "config", "hand.rviz")

    def launch_setup(context, *args, **kwargs):
        hand_value = context.launch_configurations['hand']
        hand_type_value = context.launch_configurations.get('type', '')
        collider_value = context.launch_configurations.get('collider', '')
        direction_value = context.launch_configurations.get('direction', '')
        robot_description = process_xacro(hand_value, hand_type_value, collider_value, direction_value)
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
            'hand',
            default_value='brainco',
            description='hand name to visualize'
        ),
        DeclareLaunchArgument(
            'type',
            default_value='',
            description='Type of the hand (empty means no type parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'collider',
            default_value='',
            description='Collider type of the hand(empty means no collider parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'direction',
            default_value='',
            description='Direction of the hand(empty means no direction parameter passed to xacro)'
        ),
        OpaqueFunction(function=launch_setup)
    ])