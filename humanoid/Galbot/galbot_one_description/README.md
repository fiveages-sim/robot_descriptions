# Galbot One Description

This package contains the description files for Galbot humanoid. The origin models could be found at [RoboHanger_code](https://github.com/chen01yx/RoboHanger_code)
![galbot_one.png](../../.images/galbot_one.png)
## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galbot_one_description --symlink-install
```

## Visualize the robot

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

## Full-body ROS2 Control Demo



Run with gripper_hitbot:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one 
```

https://github.com/user-attachments/assets/2948099b-ac18-473c-8201-79c42028e2c4


