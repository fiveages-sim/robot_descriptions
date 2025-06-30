# SO Arm Description

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to so_arm_description --symlink-install
```

## 2. Visualize the robot

  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=so_arm
  ```

![so101](../../.images/so101.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=so_arm
```