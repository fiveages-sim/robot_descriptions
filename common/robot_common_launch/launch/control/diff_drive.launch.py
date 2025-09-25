"""
通用的差分驱动控制器 launch 文件

这个文件用于启动差分驱动控制器，适用于移动机器人。
包含controller_manager、差分驱动控制器、rosbridge和twist_stamper。

使用方法:
ros2 launch robot_common_launch diff_drive.launch.py robot:=go1 type:=x5 hardware:=gz world:=warehouse
ros2 launch robot_common_launch diff_drive.launch.py robot:=go1 type:=x5 hardware:=mock_components
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
    hardware = context.launch_configurations.get('hardware', 'gz')
    world = context.launch_configurations.get('world', 'default')

    # 基本参数 - 与demo.launch.py保持一致
    use_sim_time = hardware in ['gz', 'isaac']

    # 使用通用的 controller_manager launch 文件
    controller_manager_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('robot_common_launch'), 'launch', 'controller_manager.launch.py'),
        ]),
        launch_arguments=[
            ('robot', robot_name),
            ('type', robot_type),
            ('use_sim_time', str(use_sim_time)),
            ('world', world),
            ('hardware', hardware),
        ],
    )

    # Diff drive controller spawner
    diff_drive_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller'],
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time},
        ],
        remappings=[
            ('/diff_drive_controller/cmd_vel', '/cmd_vel')
        ]
    )

    # Rosbridge for web interface
    ros_bridge = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_websocket',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # Rosapi for web interface
    rosapi = Node(
        package='rosapi',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'params_glob': "[*]"}
        ],
        executable='rosapi_node',
        name='rosapi',
    )

    # Twist stamper for coordinate frame transformation
    twist_stamper = Node(
        package='twist_stamper',
        executable='twist_stamper',
        name='twist_stamper',
        output='screen',
        remappings=[
            ('cmd_vel_in', '/cmd_vel'),
            ('cmd_vel_out', '/diff_drive_controller/cmd_vel')
        ],
        parameters=[
            {'frame_id': 'base_link'},
            {'use_sim_time': use_sim_time}
        ]
    )

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node',
        output='screen',
        parameters=[os.path.join(get_package_share_directory('robot_common_launch'), 'config/nav2/ekf.yaml'),
                    {'use_sim_time': use_sim_time}]
    )

    return [
        controller_manager_launch,
        diff_drive_controller_spawner,
        ros_bridge,
        rosapi,
        twist_stamper,
        robot_localization_node
    ]


def generate_launch_description():
    # Command-line arguments
    robot_name_arg = DeclareLaunchArgument(
        "robot",
        default_value="go1",
        description="Robot name (go1, unitree_g1, etc.)"
    )

    robot_type_arg = DeclareLaunchArgument(
        "type",
        default_value="",
        description="Robot type (x5, r5, etc.). Leave empty to not pass type parameter to xacro."
    )

    hardware_arg = DeclareLaunchArgument(
        "hardware",
        default_value="gz",
        description="Hardware type: 'gz' for Gazebo simulation, 'isaac' for Isaac simulation, 'mock_components' for mock components"
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value='default',
        description='Gazebo world file name (only used when hardware=gz)'
    )

    return LaunchDescription([
        robot_name_arg,
        robot_type_arg,
        hardware_arg,
        world_arg,
        OpaqueFunction(function=launch_setup),
    ])
