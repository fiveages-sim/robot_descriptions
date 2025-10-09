import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    slam_params_file = LaunchConfiguration('slam_params_file')
    nav2_params_file = LaunchConfiguration('nav2_params_file')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        'slam_params_file',
        default_value=os.path.join(get_package_share_directory("robot_common_launch"),
                                   'config', 'slam_toolbox', 'mapper_params_online_async.yaml'),
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')
    declare_nav2_params_file_cmd = DeclareLaunchArgument(
        'nav2_params_file',
        default_value=os.path.join(get_package_share_directory("robot_common_launch"),
                                   'config', 'nav2', 'nav2_params.yaml'),
        description='Full path to the ROS2 parameters file to use for Nav2')

    # 引用 slam_toolbox 的官方 launch 文件
    slam_toolbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('slam_toolbox'),
                        'launch', 'online_async_launch.py')
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'slam_params_file': slam_params_file,
        }.items()
    )

    # 引用 nav2_bringup 的 navigation launch 文件
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('nav2_bringup'),
                        'launch', 'navigation_launch.py')
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'params_file': nav2_params_file,
        }.items()
    )

    # 引用 nav2_bringup 的 rviz launch 文件
    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('nav2_bringup'),
                        'launch', 'rviz_launch.py')
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
        }.items()
    )

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_slam_params_file_cmd)
    ld.add_action(declare_nav2_params_file_cmd)
    ld.add_action(slam_toolbox_launch)
    ld.add_action(nav2_launch)
    ld.add_action(rviz_launch)

    return ld
