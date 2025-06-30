# Robot Descriptions

This Repository contains the URDF and SRDF files for the quadruped, humanoid and manipulator robot. All sorted as ros2 packages.

I collect them from internet and repaint some of them, better visualization can make me coding happier. ☺️

## Humanoid Robots

| Brand    | Model                                      | Repaint | Images                                                     |
|----------|--------------------------------------------|---------|------------------------------------------------------------|
| Booster  | [T1](humanoid/Booster/t1_description/)     | Yes     | <img src="humanoid/.images/booster_t1.png" width="200" style="object-fit: cover; object-position: center;">    |
| RobotEra | [xbot](humanoid/RobotEra/xbot_description) | Yes     | <img src="humanoid/.images/robotera_xbot.png" width="200"> |


## Manipulator Robots

| Brand          | Model                                                         | Repaint | Images                                                                                                                                                                                                                                                              |
|----------------|---------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TheRobotStudio | [SO-ARM](manipulator/Dobot/so_arm_description)                | No      | <img src="manipulator/.images/so101.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                                              |
| Dobot          | [CR5](manipulator/Dobot/cr5_description)                      | Yes     | <img src="manipulator/.images/dobot_cr5.png" width="200" height="150" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/dobot_cr5_robotiq85.png" width="200" height="150" style="object-fit: cover; object-position: center;"> |
| ARX            | [R5](manipulator/ARX/r5_description)                          | Yes     | <img src="manipulator/.images/arx_r5.png" width="200">                                                                                                                                                                                                              |
| ARX            | [X5](manipulator/ARX/x5_description)                          | Yes     | <img src="manipulator/.images/arx_x5.png" width="200">                                                                                                                                                                                                              |
| ARX            | [LIFT](manipulator/ARX/lift_description)                      | Yes     | <img src="manipulator/.images/arx_lift.png" width="200" height="150" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/arx_lift2.png" width="200" height="150" style="object-fit: cover; object-position: center;">            |
| ARX            | [X7S](manipulator/ARX/x7s_description)                        | Yes     | <img src="manipulator/.images/arx_x7s.png" width="200">                                                                                                                                                                                                             |
| AgileX         | [Piper](manipulator/AgileX/piper_description)                 | Yes     | <img src="manipulator/.images/agilex_piper.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/agilex_piper_master.png" width="200" height="120" style="object-fit: cover; object-position: center;">  |
| AgileX         | [Mobile ALoha2](manipulator/AgileX/mobile_aloha2_description) | Yes     | <img src="manipulator/.images/agilex_aloha2.png" width="200">                                                                                                                                                                                                       |
| Galaxea        | [A1X / A1Y](manipulator/Galaxea/a1xy_description)             | Yes     | <img src="manipulator/.images/galaxea_a1x.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1y.png" width="200" height="120" style="object-fit: cover; object-position: center;">           |
| Airbots        | [Play](manipulator/Airbots/airbot_play_description)           | Yes     | <img src="manipulator/.images/airbot_play.png" width="200">                                                                                                                                                                                                         |

### Manipulator Robots with OCS2
I add mobile manipulator OCS2 config for some of the manipulator robots, you can use them with the `manipulator_ocs2.launch.py` launch file. More details can be found in the [OCS2 documentation](docs/OCS2.md).

![cr5 ocs2](manipulator/.images/dobot_cr5_ocs2.gif)

## Grippers
| Brand                                  | Model | Mimic | Images                                                                                                                 | Collision                                                                                                                        |
|----------------------------------------|-------|-------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Robotiq](gripper/robotiq_description) | 85    | Yes   | <img src="gripper/.images/robotiq85.png" width="200" height="150" style="object-fit: cover; object-position: center;"> | <img src="gripper/.images/robotiq85_collision.png" width="200" height="150" style="object-fit: cover; object-position: center;"> |

## Quadruped Robots

| Brand         | Model                                              | Repaint | Images                                                        |
|---------------|----------------------------------------------------|---------|---------------------------------------------------------------|
| Unitree       | [A1](quadruped/unitree/a1_description)             | No      | <img src="quadruped/.images/unitree_a1.png" width="200">      |
| Unitree       | [Aliengo](quadruped/unitree/aliengo_description)   | No      | <img src="quadruped/.images/unitree_aliengo.png" width="200"> |
| Unitree       | [Go1](quadruped/unitree/go1_description)           | Yes     | <img src="quadruped/.images/unitree_go1.png" width="200">     |
| Unitree       | [Go2](quadruped/unitree/go2_description)           | No      | <img src="quadruped/.images/unitree_go2.png" width="200">     |
| Unitree       | [B2](quadruped/unitree/b2_description)             | No      | <img src="quadruped/.images/unitree_b2.png" width="200">      |
| Deep Robotics | [Lite3](quadruped/deep_robotics/lite3_description) | Yes     | <img src="quadruped/.images/deep_lite3.png" width="200">      |
| Deep Robotics | [X30](quadruped/deep_robotics/x30_description)     | Yes     | <img src="quadruped/.images/deep_x30.png" width="200">        |