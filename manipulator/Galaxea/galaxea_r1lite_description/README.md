# Galaxea R1 Lite Description

This package contains the description files for Galaxea R1 Humanoid Robot. The origin models could be found
at [GalaxeaManipSim](https://github.com/OpenGalaxea/GalaxeaManipSim).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galaxea_r1lite_description --symlink-install
```

## 2. Visualize the robot

* R1 Lite with A1X Arm
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_r1lite
```

![A1X](../../.images/galaxea_r1lite_x.png)
* R1 Lite with A1Y Arm
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_r1lite type:=y
```

![A1Y](../../.images/galaxea_r1lite_y.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=galaxea_r1
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1 hardware:=gz
```