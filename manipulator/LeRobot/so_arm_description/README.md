# SO Arm Description
This package contains the description files for SO100/SO101 Manipulator. The origin models could be found at [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)

* camera support from: [WowRobot](https://wowrobo.com/home)
* camera model from: [3dwhere](https://www.3dwhere.com/models/606v9dvz913o54jn)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to so_arm_description --symlink-install
```

## 2. Visualize the robot

* SO100
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=so_arm type:=so100
  ```
    ![so100](../../.images/so100.png)

* SO101
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=so_arm
  ```
    ![so101](../../.images/so101.png)

## 3. OCS2 Demo

* SO101
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=so_arm
  ```

* SO100
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=so_arm type:=100
  ```