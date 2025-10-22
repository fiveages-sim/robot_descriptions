"""
Common robot utilities for launch files.

This module provides utility functions for robot path management and configuration loading.
"""

import os
import yaml
from ament_index_python.packages import get_package_share_directory

# 全局缓存字典，避免重复读取配置文件
_config_cache = {}


def clear_config_cache():
    """
    清除配置缓存
    
    在开发或测试时，如果配置文件被修改，可以调用此函数清除缓存
    """
    global _config_cache
    _config_cache.clear()
    print("[INFO] Config cache cleared")


def get_robot_package_path(robot_name):
    """
    Get common robot-related paths.
    
    Args:
        robot_name (str): Name of the robot (e.g., 'cr5', 'arx5', etc.)
        
    Returns:
        str: Path to the robot description package, or None if not found
        
    Example:
        >>> robot_path = get_robot_package_path('cr5')
        >>> print(robot_path)
        '/opt/ros/humble/share/cr5_description'
    """
    robot_pkg = robot_name + "_description"
    try:
        robot_pkg_path = get_package_share_directory(robot_pkg)
        return robot_pkg_path
    except Exception as e:
        print(f"[ERROR] Failed to get package path for '{robot_pkg}': {e}")
        return None


def load_robot_config(robot_name, config_type="ros2_control", robot_type=""):
    """
    Get robot configuration from ROS2 controller configuration file.
    
    Args:
        robot_name (str): Name of the robot (e.g., 'cr5', 'arx5', etc.)
        config_type (str): Type of configuration file (default: 'ros2_control')
        robot_type (str): Robot type/variant (e.g., 'x5', 'r5', 'robotiq85', etc.)
        
    Returns:
        tuple: (config_dict, config_path) or (None, None) if failed
        
    Example:
        >>> config, path = load_robot_config('cr5', 'ros2_control', 'x5')
        >>> if config:
        ...     print(f"Loaded config from: {path}")
    """
    # 创建缓存键
    cache_key = f"{robot_name}_{config_type}_{robot_type}"
    
    # 检查缓存
    if cache_key in _config_cache:
        return _config_cache[cache_key]
    
    robot_pkg_path = get_robot_package_path(robot_name)
    if robot_pkg_path is None:
        return None, None
        
    try:
        # Try type-specific config file first, fallback to default
        if config_type == "ros2_control":
            config_file = f"{robot_type}.yaml" if robot_type and robot_type.strip() else "ros2_controllers.yaml"
            config_path = os.path.join(robot_pkg_path, "config", "ros2_control", config_file)
            
            if not os.path.exists(config_path):
                config_file = "ros2_controllers.yaml"
                config_path = os.path.join(robot_pkg_path, "config", "ros2_control", config_file)
                print(f"[INFO] Type-specific ros2 control config not found, using default: {config_file}")
            else:
                print(f"[INFO] Using ros2 control config file: {config_file}")
        else:
            # For other config types, use the specified type
            config_file = f"{robot_type}.yaml" if robot_type and robot_type.strip() else f"{config_type}.yaml"
            config_path = os.path.join(robot_pkg_path, "config", config_type, config_file)
            
        print(f"[INFO] Reading {config_type} config from: {config_path}")
        
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # 缓存结果
        result = (config, config_path)
        _config_cache[cache_key] = result
            
        return result
        
    except FileNotFoundError:
        print(f"[WARN] {config_type} config file not found for robot '{robot_name}'")
        return None, None
    except yaml.YAMLError as e:
        print(f"[ERROR] Failed to parse YAML config for robot '{robot_name}': {e}")
        return None, None
    except Exception as e:
        print(f"[ERROR] Unexpected error reading config for robot '{robot_name}': {e}")
        return None, None


def get_planning_urdf_path(robot_name, robot_type=""):
    """
    Get planning URDF file path based on robot type.
    
    Args:
        robot_name (str): Name of the robot
        robot_type (str): Robot type/variant
        
    Returns:
        str: Path to planning URDF file, or None if not found
        
    Example:
        >>> urdf_path = get_planning_urdf_path('cr5', 'x5')
        >>> print(urdf_path)
        '/opt/ros/humble/share/cr5_description/urdf/cr5_x5.urdf'
    """
    robot_pkg_path = get_robot_package_path(robot_name)
    if robot_pkg_path is None:
        return None
    
    if robot_type and robot_type.strip():
        # Try type-specific URDF first
        robot_identifier = robot_name + "_" + robot_type
        type_specific_urdf = os.path.join(robot_pkg_path, "urdf", robot_identifier + ".urdf")
        
        # Check if type-specific URDF exists
        if os.path.exists(type_specific_urdf):
            return type_specific_urdf
        else:
            # Fallback to default URDF if type-specific doesn't exist
            default_urdf = os.path.join(robot_pkg_path, "urdf", robot_name + ".urdf")
            return default_urdf
    else:
        # Use default URDF
        default_urdf = os.path.join(robot_pkg_path, "urdf", robot_name + ".urdf")
        return default_urdf


def get_info_file_name(robot_name, robot_type="", config_type="ros2_control"):
    """
    Get info_file_name from ROS2 controller configuration, fallback to 'task'.
    
    Args:
        robot_name (str): Name of the robot
        robot_type (str): Robot type/variant
        config_type (str): Type of configuration file
        
    Returns:
        str: Info file name (default: 'task')
        
    Example:
        >>> info_file = get_info_file_name('cr5', 'x5')
        >>> print(info_file)
        'task'
    """
    config, _ = load_robot_config(robot_name, config_type, robot_type)
    
    if config is None:
        return 'task'
    
    try:
        # Extract info_file_name from ocs2_arm_controller parameters
        info_file_name = config.get('ocs2_arm_controller', {}).get('ros__parameters', {}).get('info_file_name', 'task')
        return info_file_name
    except KeyError as e:
        print(f"[WARN] Key error in config for robot '{robot_name}': {e}, using default 'task'")
        return 'task'


def get_gz_bridge_config_path(robot_name):
    """
    Get Gazebo bridge configuration file path for a robot.
    
    首先尝试加载机器人特定的配置，如果不存在则返回默认配置。
    
    Args:
        robot_name (str): Name of the robot (e.g., 'cr5', 'agibot_g1', etc.)
        
    Returns:
        str: Path to gz_bridge.yaml file (robot-specific or default)
        
    Example:
        >>> bridge_config = get_gz_bridge_config_path('agibot_g1')
        >>> print(f"Using bridge config: {bridge_config}")
    """
    robot_pkg_path = get_robot_package_path(robot_name)
    
    # 首先尝试机器人特定的配置
    if robot_pkg_path is not None:
        gz_bridge_config_path = os.path.join(robot_pkg_path, "config", "gazebo", "gz_bridge.yaml")
        
        if os.path.exists(gz_bridge_config_path):
            print(f"[INFO] Using robot-specific Gazebo bridge config: {gz_bridge_config_path}")
            return gz_bridge_config_path
    
    # 如果没有找到机器人特定的配置，使用默认配置
    try:
        robot_common_launch_path = get_package_share_directory('robot_common_launch')
        default_gz_bridge_config_path = os.path.join(robot_common_launch_path, "config", "gazebo", "gz_bridge.yaml")
        
        if os.path.exists(default_gz_bridge_config_path):
            print(f"[INFO] Using default Gazebo bridge config for robot '{robot_name}': {default_gz_bridge_config_path}")
            return default_gz_bridge_config_path
        else:
            print(f"[WARN] Default Gazebo bridge config not found: {default_gz_bridge_config_path}")
            return None
    except Exception as e:
        print(f"[ERROR] Failed to get default Gazebo bridge config: {e}")
        return None


def get_gz_image_bridge_topics(robot_name):
    """
    Get Gazebo image bridge topic list for a robot.
    
    仅查找机器人特定的配置，如果不存在则返回None（不启动image bridge）。
    Image bridge是可选的，只有需要相机图像传输的机器人才需要配置。
    
    配置文件格式应该是一个YAML文件，包含一个话题列表：
    ---
    topics:
      - /camera/image
      - /camera/depth_image
    
    Args:
        robot_name (str): Name of the robot (e.g., 'cr5', 'agibot_g1', etc.)
        
    Returns:
        list or None: List of image topics if config exists, otherwise None
        
    Example:
        >>> topics = get_gz_image_bridge_topics('agibot_g1')
        >>> if topics:
        ...     print(f"Image topics: {topics}")
        ... else:
        ...     print("No image bridge needed for this robot")
    """
    robot_pkg_path = get_robot_package_path(robot_name)
    
    if robot_pkg_path is None:
        return None
    
    gz_image_bridge_config_path = os.path.join(robot_pkg_path, "config", "gazebo", "gz_image_bridge.yaml")
    
    if os.path.exists(gz_image_bridge_config_path):
        try:
            with open(gz_image_bridge_config_path, 'r') as file:
                config = yaml.safe_load(file)
                
            if config and 'topics' in config:
                topics = config['topics']
                print(f"[INFO] Found Gazebo image bridge config for robot '{robot_name}' with {len(topics)} topics")
                return topics
            else:
                print(f"[WARN] Image bridge config exists but 'topics' key not found for robot '{robot_name}'")
                return None
        except Exception as e:
            print(f"[ERROR] Failed to read image bridge config for robot '{robot_name}': {e}")
            return None
    else:
        print(f"[INFO] No image bridge config found for robot '{robot_name}', skipping image bridge")
        return None
