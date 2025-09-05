# Common Visualize config for robots

* Compile
```bash
cd ~/ros2_ws
colcon build --packages-up-to robot_visualize_config --symlink-install
```

# Quadruped & Humanoid
* Visualize the robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config visualize.launch.py
```

* Specify the robot model
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config visualize.launch.py robot:=x30
```

# Manipulator
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py
```

# Gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config gripper.launch.py
```

# DexHand
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config hand.launch.py
```