# AgileX Mobile Aloha Description

This package contains the description files for AgileX's Mobile Aloha2 manipulator. The origin models can be found
at [mobile aloha sim](https://github.com/agilexrobotics/mobile_aloha_sim/tree/v2.0.0)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to agilex_aloha_description --symlink-install
```

## 2. Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=agilex_aloha
```

![split](../../.images/agilex_split_aloha.png)

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=agilex_aloha type:="v2"
```

![aloha2](../../.images/agilex_aloha2.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* Split Aloha
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=agilex_aloha dual_arm:=true
  ```

### 3.2 OCS2 Arm Controller Demo

* Split Aloha
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=agilex_aloha
  ```
    ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=agilex_aloha hardware:=gz world:=warehouse
  ```