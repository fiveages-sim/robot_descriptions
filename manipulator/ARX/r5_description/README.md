# ARX R5 Description
This package contains the description files for ARX R5 Manipulator. The origin models could be found at [ARX_Models](https://github.com/ARXroboticsX/ARX_Model)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to r5_description --symlink-install
```

## 2. Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=r5
```

![arx r5](../../.images/arx_r5.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=r5
```