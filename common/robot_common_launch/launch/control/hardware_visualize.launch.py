"""
通用的硬件测试可视化 launch 文件

这个文件用于测试 ros2_control 硬件是否能正常读取数据。
适用于任何机器人，提供基本的可视化功能。

使用方法:
ros2 launch robot_common_launch visualize.launch.py robot:=cr5 type:=x5 hardware:=mock_components
ros2 launch robot_common_launch visualize.launch.py robot:=arx5 type:=x5 hardware:=gz world:=warehouse
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    """Launch setup function using OpaqueFunction"""
    robot_name = context.launch_configurations['robot']
    robot_type = context.launch_configurations.get('type', '')
    hardware = context.launch_configurations.get('hardware', 'mock_components')
    world = context.launch_configurations.get('world', 'empty')

    # 基本参数 - 与demo.launch.py保持一致
    use_sim_time = hardware in ['gz', 'isaac']

    # 使用通用的 controller_manager launch 文件
    controller_manager_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('robot_common_launch'), 'launch','controller_manager.launch.py')
        ]),
        launch_arguments=[
            ('robot', robot_name),
            ('type', robot_type),
            ('use_sim_time', str(use_sim_time)),
            ('world', world),
            ('hardware', hardware),
        ],
    )

    # RViz for visualization
    rviz_base = os.path.join(
        get_package_share_directory("robot_common_launch"), "config", "rviz"
    )
    rviz_full_config = os.path.join(rviz_base, "hardware_test.rviz")
    
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_full_config],
        parameters=[
            {'use_sim_time': use_sim_time}
        ],
    )

    return [
        controller_manager_launch,
        rviz_node,
    ]


def generate_launch_description():
    # Command-line arguments
    robot_name_arg = DeclareLaunchArgument(
        "robot",
        default_value="cr5",
        description="Robot name (arx5, cr5, unitree_g1, etc.)"
    )

    robot_type_arg = DeclareLaunchArgument(
        "type",
        default_value="",
        description="Robot type (x5, r5, robotiq85, etc.). Leave empty to not pass type parameter to xacro."
    )

    hardware_arg = DeclareLaunchArgument(
        "hardware",
        default_value="mock_components",
        description="Hardware type: 'gz' for Gazebo simulation, 'isaac' for Isaac simulation, 'mock_components' for mock components"
    )

    world_arg = DeclareLaunchArgument(
        'world', 
        default_value='empty', 
        description='Gazebo world file name (only used when hardware=gz)'
    )

    return LaunchDescription([
        robot_name_arg,
        robot_type_arg,
        hardware_arg,
        world_arg,
        OpaqueFunction(function=launch_setup),
    ])
