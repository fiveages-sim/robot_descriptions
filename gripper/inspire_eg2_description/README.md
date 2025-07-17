# Inspire EG2 Gripper Description

This package contains the URDF and related files for the Inspire EG2 Gripper.

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to inspire_eg2_description --symlink-install
```

## Visualize the Gripper

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=inspire_eg2
```

![EG2](../.images/inspire_eg2.png)