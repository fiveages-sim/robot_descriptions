"""
通用的 Controller Manager launch 文件

这个文件负责启动 controller manager 节点和 Gazebo 仿真环境。
具体的控制器激活应该在调用此 launch 文件的应用中处理。

使用方法:
ros2 launch robot_common_launch controller_manager.launch.py robot:=cr5 type:=x5
ros2 launch robot_common_launch controller_manager.launch.py robot:=cr5 hardware:=gz
ros2 launch robot_common_launch controller_manager.launch.py robot:=cr5 hardware:=gz world:=warehouse

# Gazebo GUI可以随时连接（在另一个终端运行）:
gz sim -g
"""

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
from ros_gz_bridge.actions import RosGzBridge
from ros_gz_sim.actions import GzServer

# Import robot_common_launch utilities
from robot_common_launch import load_robot_config, get_robot_package_path, get_gz_bridge_config_path, get_gz_image_bridge_topics
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
            
            # 启动 Gazebo Server (创建组合容器)
            gz_server = GzServer(
                world_sdf_file=world_path,
                world_sdf_string='',
                container_name='ros_gz_container',
                create_own_container=True,
                use_composition=True,
            )
            
            # 获取 Gazebo bridge 配置 (优先使用机器人特定配置，否则使用默认配置)
            gz_bridge_config_path = get_gz_bridge_config_path(robot_name)
            
            # 启动 ROS-Gazebo Bridge (复用已创建的容器)
            ros_gz_bridge = RosGzBridge(
                bridge_name='ros_gz_bridge',
                config_file=gz_bridge_config_path,
                container_name='ros_gz_container',
                create_own_container=False,
                use_composition=True,
            )
            
            nodes.extend([gz_server, ros_gz_bridge])
            
            # 检查是否需要启动 Image Bridge (可选)
            gz_image_topics = get_gz_image_bridge_topics(robot_name)
            if gz_image_topics is not None and len(gz_image_topics) > 0:
                # 为每个图像话题创建独立的 image_bridge 节点
                for topic in gz_image_topics:
                    # 从话题名生成节点名称 (例如: /camera/image -> bridge_gz_ros_camera_image)
                    node_name = f'bridge_gz_ros{topic.replace("/", "_")}'
                    
                    image_bridge_node = Node(
                        package='ros_gz_image',
                        executable='image_bridge',
                        name=node_name,
                        output='screen',
                        parameters=[
                            {'use_sim_time': use_sim_time},
                        ],
                        arguments=[topic],
                    )
                    nodes.append(image_bridge_node)
            
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
            
            nodes.append(gz_spawn_entity)
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
