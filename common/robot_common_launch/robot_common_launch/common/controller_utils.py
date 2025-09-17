"""
Common controller utilities for launch files.

This module provides utility functions for controller detection and management.
"""

from launch_ros.actions import Node


def detect_controllers(robot_name, robot_type="", patterns=None):
    """
    Detect controllers from ROS2 controller configuration.
    
    Args:
        robot_name (str): Name of the robot
        robot_type (str): Robot type/variant
        patterns (list): List of patterns to match controller names
        
    Returns:
        list: List of detected controllers
        
    Example:
        >>> controllers = detect_controllers('cr5', 'x5', ['hand', 'gripper'])
        >>> print(controllers)
        [{'name': 'hand_controller', 'type': 'joint_trajectory_controller', ...}]
    """
    # Import here to avoid circular imports
    from .robot_utils import load_robot_config
    
    if patterns is None:
        patterns = ['hand', 'gripper']
    
    config, _ = load_robot_config(robot_name, "ros2_control", robot_type)
    
    if config is None:
        print(f"[WARN] No controllers will be detected for robot '{robot_name}'")
        return []
    
    controllers = []
    
    # Check controller_manager section for matching controllers
    controller_manager = config.get('controller_manager', {}).get('ros__parameters', {})
    
    for controller_name, controller_config in controller_manager.items():
        # Check if controller name matches any pattern
        if any(pattern.lower() in controller_name.lower() for pattern in patterns):
            # Extract controller type and parameters
            controller_type = controller_config.get('type', '')
            controllers.append({
                'name': controller_name,
                'type': controller_type,
                'config': controller_config
            })
            print(f"[INFO] Detected controller: {controller_name} ({controller_type})")
    
    # Also check for controller parameter sections
    for section_name, section_config in config.items():
        if any(pattern.lower() in section_name.lower() for pattern in patterns):
            if section_name not in [c['name'] for c in controllers]:
                controllers.append({
                    'name': section_name,
                    'type': 'unknown',
                    'config': section_config
                })
                print(f"[INFO] Detected controller section: {section_name}")
    
    print(f"[INFO] Total controllers detected: {len(controllers)}")
    return controllers


def create_controller_spawners(controllers, use_sim_time=False):
    """
    Create spawner nodes for controllers.
    
    Args:
        controllers (list): List of controller configurations
        use_sim_time (bool): Whether to use simulation time
        
    Returns:
        list: List of Node objects for controller spawners
        
    Example:
        >>> controllers = detect_controllers('cr5', 'x5', ['hand'])
        >>> spawners = create_controller_spawners(controllers, use_sim_time=True)
        >>> print(len(spawners))
        1
    """
    spawners = []
    
    for controller in controllers:
        controller_name = controller['name']
        
        print(f"[INFO] Creating spawner for controller: {controller_name}")
        
        spawner = Node(
            package='controller_manager',
            executable='spawner',
            arguments=[controller_name],
            output='screen',
            parameters=[
                {'use_sim_time': use_sim_time},
            ],
        )
        
        spawners.append(spawner)
    
    return spawners
