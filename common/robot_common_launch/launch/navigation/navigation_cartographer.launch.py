import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_rviz = LaunchConfiguration('use_rviz')
    nav2_params_file = LaunchConfiguration('nav2_params_file')
    cartographer_config_dir = LaunchConfiguration('cartographer_config_dir')
    configuration_basename = LaunchConfiguration('configuration_basename')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')
    declare_use_rviz_argument = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Launch rviz if true')
    declare_nav2_params_file_cmd = DeclareLaunchArgument(
        'nav2_params_file',
        default_value=os.path.join(get_package_share_directory("robot_common_launch"),
                                   'config', 'nav2', 'nav2_params.yaml'),
        description='Full path to the ROS2 parameters file to use for Nav2')
    declare_cartographer_config_dir_cmd = DeclareLaunchArgument(
        'cartographer_config_dir',
        default_value=os.path.join(get_package_share_directory('robot_common_launch'),
                                   'config', 'cartographer'),
        description='Full path to config file to load')
    declare_configuration_basename_cmd = DeclareLaunchArgument(
        'configuration_basename',
        default_value='cartographer.lua',
        description='Name of lua file for cartographer')

    # 引用 cartographer 的 launch 文件
    cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('robot_common_launch'),
                        'launch', 'cartographer.launch.py')
        ]),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'use_rviz': use_rviz,
            'cartographer_config_dir': cartographer_config_dir,
            'configuration_basename': configuration_basename,
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

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_use_rviz_argument)
    ld.add_action(declare_nav2_params_file_cmd)
    ld.add_action(declare_cartographer_config_dir_cmd)
    ld.add_action(declare_configuration_basename_cmd)
    ld.add_action(cartographer_launch)
    ld.add_action(nav2_launch)

    return ld
