"""
通用 launch 工具函数

这个模块提供了用于 launch 文件的通用工具函数，用于消除重复代码。
"""

import os
import re
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_ros.actions import Node
import xacro


def get_default_type_from_xacro(xacro_file):
    """
    从 xacro 文件中读取 type 参数的默认值
    
    Args:
        xacro_file (str): xacro 文件路径
        
    Returns:
        str: 默认的 type 值，如果找不到则返回 None
    """
    try:
        with open(xacro_file, 'r') as f:
            content = f.read()
            # 查找 xacro:arg name="type" default="..." 的模式
            match = re.search(r'xacro:arg\s+name=["\']type["\']\s+default=["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read default type from {xacro_file}: {e}")
    return None


def process_xacro(robot_name, xacro_filename="robot.xacro", **kwargs):
    """
    通用的 xacro 处理函数
    
    Args:
        robot_name (str): 机器人名称
        xacro_filename (str): xacro 文件名 (默认: "robot.xacro")
        **kwargs: 传递给 xacro 的映射参数 (如 type, collider, direction 等)
        
    Returns:
        str: 处理后的 URDF XML 字符串
    """
    package_description = robot_name + "_description"
    pkg_path = get_package_share_directory(package_description)
    xacro_file = os.path.join(pkg_path, 'xacro', xacro_filename)
    
    # 构建 mappings 字典，过滤空值
    mappings = {k: v for k, v in kwargs.items() if v and str(v).strip()}
    
    # 特殊处理：如果 type 参数为空，尝试从 xacro 文件读取默认值
    if 'type' not in mappings:
        default_type = get_default_type_from_xacro(xacro_file)
        if default_type:
            mappings['type'] = default_type
    
    # 根据 mappings 是否为空来决定如何处理 xacro 文件
    if mappings:
        robot_description_config = xacro.process_file(xacro_file, mappings=mappings)
    else:
        robot_description_config = xacro.process_file(xacro_file)
    
    return robot_description_config.toxml()


def create_visualization_nodes(robot_description, rviz_config_file):
    """
    创建通用的可视化节点
    
    Args:
        robot_description (str): 机器人描述 XML
        rviz_config_file (str): RViz 配置文件路径
        
    Returns:
        list: Node 对象列表
    """
    return [
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=["-d", rviz_config_file]
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'publish_frequency': 100.0,
                    'use_tf_static': True,
                    'robot_description': robot_description
                }
            ],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen',
        )
    ]


def create_common_launch_arguments():
    """
    创建通用的 launch 参数
    
    Returns:
        list: DeclareLaunchArgument 对象列表
    """
    return [
        DeclareLaunchArgument(
            'type',
            default_value='',
            description='Type parameter for xacro (empty means no type parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'collider',
            default_value='',
            description='Collider type parameter for xacro (empty means no collider parameter passed to xacro)'
        ),
        DeclareLaunchArgument(
            'direction',
            default_value='',
            description='Direction parameter for xacro (empty means no direction parameter passed to xacro)'
        ),
    ]


def create_visualization_launch_description(
    robot_param_name='robot',
    robot_default_value='go1',
    robot_description_param='robot',
    xacro_filename='robot.xacro',
    rviz_config_name='urdf.rviz',
    additional_args=None
):
    """
    创建通用的可视化 launch 描述
    
    Args:
        robot_param_name (str): 机器人参数名称
        robot_default_value (str): 机器人默认值
        robot_description_param (str): 机器人描述参数名称 (用于显示)
        xacro_filename (str): xacro 文件名
        rviz_config_name (str): RViz 配置文件名
        additional_args (list): 额外的参数列表
        
    Returns:
        LaunchDescription: 配置好的 launch 描述
    """
    def launch_setup(context, *args, **kwargs):
        robot_value = context.launch_configurations[robot_param_name]
        
        # 收集所有可能的 xacro 参数
        xacro_params = {}
        for arg_name in ['type', 'collider', 'direction']:
            if arg_name in context.launch_configurations:
                xacro_params[arg_name] = context.launch_configurations[arg_name]
        
        # 处理 xacro
        robot_description = process_xacro(robot_value, xacro_filename, **xacro_params)
        
        # 获取 RViz 配置文件
        rviz_config_file = os.path.join(
            get_package_share_directory("robot_common_launch"), 
            "config", "rviz", rviz_config_name
        )
        
        # 创建可视化节点
        return create_visualization_nodes(robot_description, rviz_config_file)

    # 构建参数列表
    args = [
        DeclareLaunchArgument(
            robot_param_name,
            default_value=robot_default_value,
            description=f'{robot_description_param} name to visualize'
        )
    ]
    
    # 添加通用参数
    args.extend(create_common_launch_arguments())
    
    # 添加额外参数
    if additional_args:
        args.extend(additional_args)
    
    # 添加 opaque function
    args.append(OpaqueFunction(function=launch_setup))
    
    return LaunchDescription(args)
