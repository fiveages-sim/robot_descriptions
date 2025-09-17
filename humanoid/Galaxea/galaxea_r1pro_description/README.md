# Galaxea R1 Pro Description

This package contains the description files for Galaxea R1 Pro Humanoid Robot. The origin models could be found
at [GMR](https://github.com/YanjieZe/GMR).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galaxea_r1pro_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=galaxea_r1pro
```
![Galaxea R1 Pro](../../.images/galaxea_r1_pro.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=galaxea_r1pro
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1pro
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1pro hardware:=gz world:=warehouse
```