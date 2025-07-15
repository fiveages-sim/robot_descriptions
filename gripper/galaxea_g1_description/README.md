# Galaxea G1 Description

This package contains the description files for Galaxea G1 Gripper. I got the origin URDF files from the [Galaxea URDF](https://github.com/userguide-galaxea/URDF).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to galaxea_g1_description --symlink-install
```

## 2. Visualize the gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_g1
```

![G1](../.images/galaxea_g1.png)