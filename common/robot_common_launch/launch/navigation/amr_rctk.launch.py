from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import os
home_dir = os.path.expanduser("~")
foldername = os.path.join(home_dir, "maps")
if not os.path.exists(foldername):
    os.makedirs(foldername)
def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='amr_rctk',
            parameters=[{'use_sim_time': use_sim_time}],
            executable='pose_publisher',
            name='pose_publisher',
            namespace='amr_rctk'
        ),

        Node(
            package='amr_rctk',
            executable='mapping_node.py',
            name='mapping_node',
            output='screen',
            parameters=[
                {'foldername': foldername},
                {'navigation_command': 'robot_common_launch nav2.launch.py use_sim_time:=false'},
                {'start_mapping_command': 'ros2 launch robot_common_launch cartographer.launch.py'},
                {'save_map_command': 'ros2 run nav2_map_server map_saver_cli -f'}
            ]
        )
    ])
