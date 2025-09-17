# Airbot Play Description

This package contains the description files for Discover Robotics's Airbot Play manipulator. The origin models could be cound at [DISCOVERSE](https://github.com/TATP-233/DISCOVERSE).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to airbot_play_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=airbot_play
```

![airbot play](../../.images/airbot_play.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=airbot_play
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=airbot_play hardware:=gz
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=airbot_play hardware:=isaac
```