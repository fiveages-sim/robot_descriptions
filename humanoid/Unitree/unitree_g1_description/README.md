# Unitree G1 Description

This package contains the URDF and configuration files for the Unitree G1 humanoid. The origin models could be found at [unitree ros](https://github.com/unitreerobotics/unitree_ros).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to unitree_g1_description --symlink-install
```

## 2. Visualize the robot
### 2.1 Visualize with Joint State Publisher GUI
* G1 with rubber hand
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch humanoid.launch.py
  ```
  ![Unitree G1](../../.images/unitree_g1.png)

* G1 with BrainCo Revo2
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch humanoid.launch.py type:=revo2
  ```
  ![Unitree G1](../../.images/unitree_g1_revo2.png)

### 2.2 Visualize from Unitree SDK2 DDS
* Unitree Mujoco
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch hardware_visualize.launch.py robot:=unitree_g1 hardware:=unitree_sim
  ```
* Real Unitree G1
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch hardware_visualize.launch.py robot:=unitree_g1 hardware:=unitree_real
  ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=unitree_g1
```
[Screencast from 2025-09-02 17-39-02.webm](https://github.com/user-attachments/assets/034081ec-9e49-46a3-9a85-3c422ed5e40c)

### 3.2 OCS2 Arm Controller Demo

* Mock Components
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=unitree_g1
  ```
* Mock Components
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=unitree_g1 type:=revo2
  ```
* Unitree Ros2 Control
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=unitree_g1 hardware:=unitree_sim
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=unitree_g1 type:=revo2 hardware:=unitree_real
  ```