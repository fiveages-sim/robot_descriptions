# Common Launch files for robots

* Compile
```bash
cd ~/ros2_ws
colcon build --packages-up-to robot_common_launch --symlink-install
```

# Quadruped & Humanoid
* Visualize the robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py
```

* Specify the robot model
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=x30
```

# Manipulator
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py
```

# Gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch gripper.launch.py
```

# DexHand
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch hand.launch.py
```