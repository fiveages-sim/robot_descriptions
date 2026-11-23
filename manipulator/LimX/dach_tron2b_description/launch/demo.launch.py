from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    upstream = get_package_share_path("ocs2_arm_controller") / "launch/demo.launch.py"
    enable_gripper = LaunchConfiguration("enable_gripper")
    launch_mode = LaunchConfiguration("launch_mode")
    return LaunchDescription([
        DeclareLaunchArgument("hardware", default_value="mock_components"),
        DeclareLaunchArgument("launch_mode", default_value="full"),
        DeclareLaunchArgument("enable_gripper", default_value="true"),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(upstream)),
            launch_arguments={
                "robot": "dach_tron2b",
                "hardware": LaunchConfiguration("hardware"),
                "launch_mode": launch_mode,
                "enable_gripper": enable_gripper,
            }.items(),
        ),
        Node(package="dach_tron2b_description", executable="home_grippers",
             condition=IfCondition(PythonExpression([
                 "'", enable_gripper, "'.lower() == 'true' and '", launch_mode, "' != 'rviz_only'",
             ])), output="screen"),
    ])
