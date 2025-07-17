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

    dual_arm = launch.actions.DeclareLaunchArgument(
        name='dual_arm',
        default_value='false',
        description='Whether to enable dual arm mode'
    )

    def launch_setup(context, *args, **kwargs):
        robot_name_value = context.launch_configurations['robot_name']
        type_value = context.launch_configurations['type']
        debug_value = context.launch_configurations['debug']
        dual_arm_value = context.launch_configurations['dual_arm']
        
        # 生成带类型的机器人标识符
        robot_identifier = robot_name_value
        if type_value and type_value.strip():
            robot_identifier = f"{robot_name_value}_{type_value}"
            print(f"🚀 Launching OCS2 for robot: {robot_name_value} (type: {type_value})")
        else:
            print(f"🚀 Launching OCS2 for robot: {robot_name_value} (default type)")
        
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
            task_file_value = os.path.join(
                get_package_share_directory(f'{robot_name_value}_description'),
                'config', 'ocs2', 'task.info'
            )
            print(f"📁 Task file: {task_file_value}")
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
                    'taskFile': task_file_value,
                    'libFolder': lib_folder_value,
                    'dual_arm_mode': dual_arm_value,
                }.items()
            )
            print("✅ Mobile manipulator configured successfully (RViz will auto-start)")
            return [mobile_manipulator]
        except Exception as e:
            print(f"❌ Error launching mobile_manipulator: {e}")
            return []

    return LaunchDescription([
        robot_name,
        robot_type,
        debug,
        dual_arm,
        OpaqueFunction(function=launch_setup)
    ]) 