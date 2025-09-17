# ARX Lift Description

This package contains the description files for ARX Lift. The origin models could be found
at [ARX_Models](https://github.com/ARXroboticsX/ARX_Model)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to arx_lift_description --symlink-install
```
  
## 2. Visualize the robot

* Lift with X5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=arx_lift
    ```
  ![arx lift x5](../../.images/arx_lift2.png)

* Lift with R5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=arx_lift type:="r5"
    ```

  ![arx lift](../../.images/arx_lift.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo
* Lift with X5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=arx_lift
    ```
* Lift with R5 Arm
   ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=arx_lift type:=r5
    ```

### 3.2 OCS2 Arm Controller Demo

* Lift with X5 Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=arx_lift
  ```

* Lift with R5 Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=arx_lift type:=r5 hardware:=gz world:=warehouse
  ```