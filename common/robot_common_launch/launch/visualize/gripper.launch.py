from robot_common_launch import create_visualization_launch_description


def generate_launch_description():
    return create_visualization_launch_description(
        robot_param_name='gripper',
        robot_default_value='robotiq',
        robot_description_param='Gripper',
        xacro_filename='gripper.xacro',
        rviz_config_name='gripper.rviz'
    )