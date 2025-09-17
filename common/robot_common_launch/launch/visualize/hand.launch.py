from launch.actions import DeclareLaunchArgument
from robot_common_launch import create_visualization_launch_description


def generate_launch_description():
    # 添加额外的 direction 参数
    additional_args = [
        DeclareLaunchArgument(
            'direction',
            default_value='',
            description='Direction of the hand (empty means no direction parameter passed to xacro)'
        )
    ]
    
    return create_visualization_launch_description(
        robot_param_name='hand',
        robot_default_value='brainco',
        robot_description_param='Hand',
        xacro_filename='hand.xacro',
        rviz_config_name='hand.rviz',
        additional_args=additional_args
    )