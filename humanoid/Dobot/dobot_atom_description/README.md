# Dobot Atom Description

This package contains the URDF and configuration files for the Dobot Atom humanoid. The origin models could be found at [dobot_atom_ros2](https://github.com/Dobot-Arm/dobot_atom_ros2).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to dobot_atom_description --symlink-install
```

## 2. Visualize the robot
### 2.1 Full Robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=dobot_atom type:=full
```
  ![Atom](.images/dobot_atom.png)

### 2.2 Full Upper Robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=dobot_atom type:=upper
```

### 2.3 Component
* Upper Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=dobot_atom
  ```
* Left Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=dobot_atom type:=left_arm
  ```
* Right Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=dobot_atom type:=right_arm
  ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=dobot_atom type:=upper
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=dobot_atom hardware:=isaac 
```