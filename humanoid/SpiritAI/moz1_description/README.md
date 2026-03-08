# SpiritAI MOZ1 Description

This package contains the description files for Spirit AI Moz1.

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to moz1_description --symlink-install
```

## 2. Visualize the robot

## 2.1 Full Robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=moz1
```

## 2.2 Components
* Wheel
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=moz1 type:=wheel
  ```
* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=moz1 type:=chassis
  ```

---
# 关节名称与限位
|关节|连杆名称|关节名称|关节限位(Degree)|关节限位(Rad)|
|-----|-----|-----|-----|-----|
|底盘|base_link||||
|左后轮|wheel01|Base-0|||
|右后轮|wheel02|Base-1|||
|右前轮|wheel03|Base-2|||
|左前轮|wheel04|Base-3|||
|腰腿(靠近底盘)|leg01|LegWaist-0|-30~30||
|腰腿|leg02|LegWaist-1|-90~90||
|腰腿|leg03|LegWaist-2|-145~1||
|腰腿|waist01|LegWaist-3|-10~80||
|腰腿|waist02|LegWaist-4|-30~30||
|腰腿|waist03|LegWaist-5|-180~180||
|左臂1(靠近躯干)|left01|LeftArm-0|-180~120||
|左臂2|left02|LeftArm-1|-170~9||
|左臂3|left03|LeftArm-2|-175~175||
|左臂4|left04|LeftArm-3|-129~10||
|左臂5|left05|LeftArm-4|-175~175||
|左臂6|left06|LeftArm-5|-95~95||
|左臂7|left07|LeftArm-6|-90~90||
|右臂1(靠近躯干)|right01|RightArm-0|-120~180||
|右臂2|right02|RightArm-1|-170~9||
|右臂3|right03|RightArm-2|-175~175||
|右臂4|right04|RightArm-3|-90~129||
|右臂5|right05|RightArm-4|-175~175||
|右臂6|right06|RightArm-5|-95~95||
|右臂7|right07|RightArm-6|-90~90||

# Launch
```bash
colcon build
source install/setup.bash
ros2 launch moz1_description robot_display.launch.py