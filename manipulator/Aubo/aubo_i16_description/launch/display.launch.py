import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory("aubo_i16_description")
    urdf_path = os.path.join(package_share, "urdf", "aubo_i16.urdf")
    rviz_config_path = os.path.join(package_share, "rviz", "joint_tree.rviz")
    with open(urdf_path, "r", encoding="utf-8") as urdf_file:
        robot_description = urdf_file.read()

    use_joint_state_publisher = LaunchConfiguration("use_joint_state_publisher")
    use_rviz = LaunchConfiguration("use_rviz")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_joint_state_publisher",
                default_value="true",
                description="Start joint_state_publisher_gui for manual joint sliders.",
            ),
            DeclareLaunchArgument(
                "use_rviz",
                default_value="true",
                description="Start RViz with a TF-focused view.",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[{"robot_description": robot_description}],
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                name="joint_state_publisher_gui",
                output="screen",
                arguments=[urdf_path],
                condition=IfCondition(use_joint_state_publisher),
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                arguments=["-d", rviz_config_path],
                condition=IfCondition(use_rviz),
            ),
        ]
    )
