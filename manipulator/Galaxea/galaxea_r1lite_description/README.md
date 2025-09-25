# Galaxea R1 Lite Description

This package contains the description files for Galaxea R1 Humanoid Robot. The origin models could be found
at [GalaxeaManipSim](https://github.com/OpenGalaxea/GalaxeaManipSim).

## 1. Build

```bash
cd ~/XZN/integrate_latest/
colcon build --packages-up-to galaxea_r1lite_description --symlink-install
```

## 2. Visualize the robot

* R1 Lite with A1X Arm
```bash
source ~/XZN/integrate_latest/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=galaxea_r1lite
```

![A1X](../../.images/galaxea_r1lite_x.png)
* R1 Lite with A1Y Arm
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=galaxea_r1lite type:=y
```

![A1Y](../../.images/galaxea_r1lite_y.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/XZN/integrate_latest/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=galaxea_r1lite
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/XZN/integrate_latest/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1lite
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1 hardware:=gz
```