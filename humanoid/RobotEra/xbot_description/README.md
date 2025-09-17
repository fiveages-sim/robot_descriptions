# RobotEra Xbot-L Description
This repository contains the urdf model of RobotEra Xbot L. The origin models could be found at [humanoid_gym](https://github.com/roboterax/humanoid-gym).

![xbot](../../.images/robotera_xbot.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to xbot_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=xbot
```