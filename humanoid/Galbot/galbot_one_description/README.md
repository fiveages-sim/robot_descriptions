# Galbot One Description

This package contains URDF/Xacro/config files for Galbot One, aligned with the workspace conventions used by `robot_common_launch` and `ocs2_arm_controller`.

![galbot_one.png](../../.images/galbot_one.png)![galbot_one.png](../galbot_one.png)
## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galbot_one_description --symlink-install
```

## Visualize!

### Full Robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one
```

Hide grippers (type:=none):

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one type:=none
```

### Component




* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=chassis
  ```

* Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=body
  ```

* Arms module
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=arm
  ```

* Gripper module
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=gripper
  ```

## Full-body OCS2 Demo



Run with gripper_hitbot:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one 
```
