"""
通用的 Controller Manager launch 文件

这个文件负责启动 controller manager 节点和 Gazebo 仿真环境。
具体的控制器激活应该在调用此 launch 文件的应用中处理。

使用方法:
ros2 launch robot_common_launch controller_manager.launch.py robot:=cr5 type:=x5
ros2 launch robot_common_launch controller_manager.launch.py robot:=cr5 type:=x5 use_gazebo:=true world:=warehouse
"""

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory

# Import robot_common_launch utilities
from robot_common_launch import load_robot_config, get_robot_package_path
import xacro


def generate_launch_description():
    # 声明参数
    robot_arg = DeclareLaunchArgument(
        'robot',
        default_value='cr5',
        description='Robot name'
    )
    
    type_arg = DeclareLaunchArgument(
        'type',
        default_value='',
        description='Robot type/variant'
    )
    
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Whether to use simulation time'
    )
    
    
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='dart',
        description='Gazebo world file name (without .sdf extension)'
    )
    
    world_package_arg = DeclareLaunchArgument(
        'world_package',
        default_value='robot_common_launch',
        description='Package containing world files'
    )
    
    
    hardware_arg = DeclareLaunchArgument(
        'hardware',
        default_value='mock_components',
        description='Hardware type: gz for Gazebo, isaac for Isaac, mock_components for mock'
    )

    def launch_setup(context, *args, **kwargs):
        robot_name = context.launch_configurations['robot']
        robot_type = context.launch_configurations['type']
        use_sim_time = context.launch_configurations['use_sim_time'] == 'true'
        world = context.launch_configurations['world']
        world_package = context.launch_configurations['world_package']
        hardware = context.launch_configurations['hardware']
        
        # 根据 hardware 参数自动判断是否使用 Gazebo
        use_gazebo = hardware == 'gz'
        
        # 生成机器人描述
        robot_pkg_path = get_robot_package_path(robot_name)
        if robot_pkg_path is None:
            print(f"[ERROR] Cannot create robot description without package path for robot '{robot_name}'")
            return []
        
        # 构建 xacro mappings
        mappings = {
            'ros2_control_hardware_type': hardware,
        }
        if robot_type and robot_type.strip():
            mappings["type"] = robot_type
        
        # 如果是 Gazebo 模式，添加 gazebo 映射
        if use_gazebo:
            mappings['gazebo'] = 'true'
            print(f"[INFO] Gazebo mode enabled")
        
        # 处理 xacro 文件
        robot_description_file_path = os.path.join(
            robot_pkg_path,
            "xacro",
            "ros2_control",
            "robot.xacro"
        )
        
        robot_description_config = xacro.process_file(
            robot_description_file_path,
            mappings=mappings
        )
        
        robot_description = robot_description_config.toxml()
        
        nodes = []
        
        # Robot State Publisher (总是需要)
        robot_state_publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'publish_frequency': 100.0,
                    'use_tf_static': True,
                    'robot_description': robot_description
                }
            ],
        )
        nodes.append(robot_state_publisher)
        
        if use_gazebo:
            # 世界文件路径
            world_path = os.path.join(get_package_share_directory(world_package), 'worlds', world + '.sdf')
            
            # 启动 Gazebo 仿真
            gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    os.path.join(get_package_share_directory('ros_gz_sim'), 'launch'),
                    '/gz_sim.launch.py',
                ]),
                launch_arguments=[
                    ('gz_args', ['-r -v 4 ', world_path])
                ],
            )
            
            # 在 Gazebo 中生成机器人
            gz_spawn_entity = Node(
                package='ros_gz_sim',
                executable='create',
                output='screen',
                arguments=[
                    '-topic',
                    'robot_description',
                    '-name',
                    robot_name,
                    '-allow_renaming',
                    'true',
                ],
            )

            bridge = Node(
                package='ros_gz_bridge',
                executable='parameter_bridge',
                arguments=[
                    "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
                    "/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan",
                    "/imu@sensor_msgs/msg/Imu@gz.msgs.IMU"
                ],
                output='screen',
            )
            
            nodes.extend([gazebo, gz_spawn_entity, bridge])
        else:
            # ros2_control_node (仅在非Gazebo模式下)
            _, ros2_controllers_path = load_robot_config(robot_name, "ros2_control", robot_type)
            if ros2_controllers_path is not None:
                ros2_control_node = Node(
                    package="controller_manager",
                    executable="ros2_control_node",
                    parameters=[
                        ros2_controllers_path,
                        {'use_sim_time': use_sim_time},
                        # Pass robot_type parameter to the controller if specified
                        {'robot_type': robot_type} if robot_type and robot_type.strip() else {}
                    ],
                    remappings=[
                        ("/controller_manager/robot_description", "/robot_description"),
                    ],
                    output="screen",
                )
                nodes.append(ros2_control_node)
            else:
                print(f"[WARN] No controller config found for robot '{robot_name}', skipping ros2_control_node")
        
        # Joint state broadcaster spawner (在所有模式下都启动)
        joint_state_broadcaster_spawner = Node(
            package='controller_manager',
            executable='spawner',
            arguments=[
                'joint_state_broadcaster',
                '--controller-manager',
                '/controller_manager',
            ],
            parameters=[
                {'use_sim_time': use_sim_time},
            ],
            output='screen',
        )
        nodes.append(joint_state_broadcaster_spawner)
        
        return nodes

    return LaunchDescription([
        robot_arg,
        type_arg,
        use_sim_time_arg,
        world_arg,
        world_package_arg,
        hardware_arg,
        OpaqueFunction(function=launch_setup)
    ])
