import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():
    # 1. 手动声明你想用的参数（现在你想加什么词都可以，比如 side, stand, apple）
    # 这些就是你在 --show-args 里想看到的
    declared_arguments = [
        DeclareLaunchArgument('robot', default_value='nero'),
        DeclareLaunchArgument('type', default_value='v1'),
        DeclareLaunchArgument('side', default_value='left'),
        DeclareLaunchArgument('stand', default_value='v1'),
    ]

    # 2. 获取参数的值
    # 获取用户在命令行输入的内容，比如 side:=right
    launch_type = LaunchConfiguration('type')
    launch_side = LaunchConfiguration('side')
    launch_stand = LaunchConfiguration('stand')

    # 3. 找到你的 xacro 文件路径
    # 假设你的包名是 nero_description
    pkg_path = get_package_share_directory('nero_description')
    xacro_file = os.path.join(pkg_path, 'xacro', 'robot.xacro')

    # 4. 重点：亲手把参数塞给 xacro 命令
    # 这一步绕过了那个死板的黑盒函数，直接把参数传到底
    robot_description_content = Command([
        'xacro ', xacro_file,
        ' type:=', launch_type,
        ' side:=', launch_side,
        ' stand:=', launch_stand
    ])

    # 5. 启动标准节点
    return LaunchDescription(declared_arguments + [
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description_content}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2'
            # 如果你有配置文件，可以在这里 arguments=['-d', rviz_config]
        )
    ])