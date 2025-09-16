import launch
from ament_index_python.packages import get_package_share_directory
import os
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction
from launch import LaunchDescription


def generate_launch_description():
    """
    通用的机器人OCS2 launch文件
    
    使用方法:
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=franka
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5 type:=red
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=piper type:=long_arm
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5 task_file:=task_custom
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5 type:=red task_file:=task_red
    """
    
    # 机器人名称参数
    robot_name = launch.actions.DeclareLaunchArgument(
        name='robot_name',
        default_value='cr5',
        description='Name of the robot (e.g., cr5, piper, x5, etc.)'
    )

    # 机器人类型参数
    robot_type = launch.actions.DeclareLaunchArgument(
        name='type',
        default_value='',
        description='Robot type/variant (e.g., red, blue, long_arm, short_arm, etc.). If empty, uses default configuration.'
    )

    debug = launch.actions.DeclareLaunchArgument(
        name='debug',
        default_value='false',
        description='Whether to enable debug mode'
    )

    # 手柄控制参数
    enable_joystick = launch.actions.DeclareLaunchArgument(
        name='enable_joystick',
        default_value='false',
        description='Whether to enable joystick control for single arm mode'
    )

    joystick_device = launch.actions.DeclareLaunchArgument(
        name='joystick_device',
        default_value='/dev/input/js0',
        description='Joystick device path (e.g., /dev/input/js0)'
    )

    # OCS2任务文件参数
    task_file = launch.actions.DeclareLaunchArgument(
        name='task_file',
        default_value='task',
        description='OCS2 task file name (without .info extension, e.g., task, task_custom, etc.)'
    )

    def launch_setup(context, *args, **kwargs):
        robot_name_value = context.launch_configurations['robot_name']
        type_value = context.launch_configurations['type']
        debug_value = context.launch_configurations['debug']
        enable_joystick_value = context.launch_configurations['enable_joystick']
        joystick_device_value = context.launch_configurations['joystick_device']
        task_file_value = context.launch_configurations['task_file']
        
        # 生成带类型的机器人标识符
        robot_identifier = robot_name_value
        if type_value and type_value.strip():
            robot_identifier = f"{robot_name_value}_{type_value}"
            print(f"🚀 Launching OCS2 for robot: {robot_name_value} (type: {type_value})")
        else:
            print(f"🚀 Launching OCS2 for robot: {robot_name_value} (default type)")
        
        # 手柄配置信息
        if enable_joystick_value == 'true':
            print(f"🎮 Joystick control enabled:")
            print(f"   - Device: {joystick_device_value}")
        else:
            print(f"🎮 Joystick control disabled")
        
        # 自动生成所有路径
        try:
            # URDF文件路径 - 如果有类型则使用类型版本，否则使用默认版本
            if type_value and type_value.strip():
                urdf_filename = f'{robot_identifier}.urdf'
            else:
                urdf_filename = f'{robot_name_value}.urdf'
                
            urdf_file_value = os.path.join(
                get_package_share_directory(f'{robot_name_value}_description'),
                'urdf', urdf_filename
            )
            print(f"📁 URDF: {urdf_file_value}")
        except Exception as e:
            print(f"❌ Error: Could not find {robot_name_value}_description package: {e}")
            return []
        
        try:
            task_file_path = os.path.join(
                get_package_share_directory(f'{robot_name_value}_description'),
                'config', 'ocs2', f'{task_file_value}.info'
            )
            print(f"📁 Task file: {task_file_path}")
        except Exception as e:
            print(f"❌ Error: Could not find task config for {robot_name_value}: {e}")
            return []
        
        try:
            # lib folder路径 - 包含类型信息
            lib_folder_value = os.path.join(
                get_package_share_directory('ocs2_mobile_manipulator'),
                'auto_generated', robot_identifier
            )
            print(f"📁 Lib folder: {lib_folder_value}")
        except Exception as e:
            print(f"❌ Error: Could not find ocs2_mobile_manipulator package: {e}")
            return []

        # 启动mobile_manipulator，RViz自动启动
        try:
            mobile_manipulator = launch.actions.IncludeLaunchDescription(
                launch.launch_description_sources.PythonLaunchDescriptionSource(
                    os.path.join(get_package_share_directory(
                        'ocs2_mobile_manipulator_ros'), 'launch/include/mobile_manipulator.launch.py')
                ),
                launch_arguments={
                    'rviz': 'true',  # 自动启动RViz
                    'debug': debug_value,
                    'urdfFile': urdf_file_value,
                    'taskFile': task_file_path,
                    'libFolder': lib_folder_value,
                    'enableJoystick': enable_joystick_value,
                }.items()
            )
            print("✅ Mobile manipulator configured successfully (RViz will auto-start)")
            
            # 如果启用手柄，添加joy_node
            nodes_to_return = [mobile_manipulator]
            if enable_joystick_value == 'true':
                from launch_ros.actions import Node
                joy_node = Node(
                    package='joy',
                    executable='joy_node',
                    name='joy_node',
                    parameters=[{
                        'dev': joystick_device_value,
                        'deadzone': 0.05,
                        'autorepeat_rate': 20.0
                    }],
                    output='screen'
                )
                nodes_to_return.append(joy_node)
                print("✅ Joy node added for joystick control")
            
            return nodes_to_return
        except Exception as e:
            print(f"❌ Error launching mobile_manipulator: {e}")
            return []

    return LaunchDescription([
        robot_name,
        robot_type,
        debug,
        enable_joystick,
        joystick_device,
        task_file,
        OpaqueFunction(function=launch_setup)
    ]) 