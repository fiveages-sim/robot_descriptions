# Realman RS-01 Description

This package contains the description files for Realman RS-01 mobile dual-arm humanoid platform.

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to rs01_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Full Robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rs01
```

![Realman RS01](../../.images/realman_rs01.png)

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rs01 type:=empty
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rs01 type:=eg2-4c2
```

### 2.2 Component

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=rs01 type:=chassis
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=rs01 type:=body
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=rs01 type:=left
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=rs01 type:=right
```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=rs01
```

### 3.2 Mock Component

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=rs01
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=rs01 type:=empty
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=rs01 type:=eg2-4c2
```

### 3.3 Isaac Sim

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=rs01 hardware:=isaac
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=rs01 hardware:=isaac type:=eg2-4c2
```
