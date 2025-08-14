# Robot Descriptions

This repository contains the URDF files for quadruped, humanoid, and manipulator robots, all organized as ROS2 packages. Most of them have been repainted in Blender for better visualization. ☺️

## Quick Start

To clone this repository with only the latest commit (shallow clone):

```bash
git clone --depth 1 https://github.com/fiveages-sim/robot_descriptions
```

This will significantly reduce download time and disk space usage.

## Humanoid Robots

| Brand    | Model                                         | Repaint | Images                                                                                                                                                                                                                   |
|----------|-----------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Booster  | [T1](humanoid/Booster/t1_description/)        | Yes     | <img src="humanoid/.images/booster_t1.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                              |
| EngineAI | [SA01](humanoid/EngineAI/sa01_description/)   | Yes     | <img src="humanoid/.images/engineai_sa01.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                           |
| EngineAI | [PM01](humanoid/EngineAI/pm01_description/)   | Yes     | <img src="humanoid/.images/engineai_pm01.png" width="300" style="object-fit: cover; object-position: center;">                                                                                                           |
| RobotEra | [xbot](humanoid/RobotEra/xbot_description)    | Yes     | <img src="humanoid/.images/robotera_xbot.png" width="200">                                                                                                                                                               |
| Agibot   | [G1](humanoid/Agibot/agibot_g1_description)   | No      | <img src="humanoid/.images/agibot_g1.png" width="200">                                                                                                                                                                   |
| Galaxea  | [R1](humanoid/Galaxea/galaxea_r1_description) | Yes     | <img src="humanoid/.images/galaxea_r1_down.png" width="200">     <img src="humanoid/.images/galaxea_r1.png" width="200">                                                                                                 |
| ARX      | [LIFT](humanoid/ARX/arx_lift_description)         | Yes     | <img src="humanoid/.images/arx_lift.png" width="200" style="object-fit: cover; object-position: center;">     <img src="humanoid/.images/arx_lift2.png" width="200" style="object-fit: cover; object-position: center;"> |
| ARX      | [X7S](humanoid/ARX/x7s_description)           | Yes     | <img src="humanoid/.images/arx_x7s.png" width="200">                                                                                                                                                                     |
| Realman  | [AIDAL](humanoid/Realman/aidal_description)   | Yes     | <img src="humanoid/.images/realman_aidal.png" width="200">                                                                                                                                                               |

## Manipulator Robots

| Brand          | Model                                                       | Repaint | Images                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TheRobotStudio | [SO-ARM](manipulator/LeRobot/so_arm_description)            | Yes     | <img src="manipulator/.images/so100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/so101.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                                         |
| SIGRobotics    | [Lekiwi](manipulator/LeRobot/lekiwi_description)            | Yes     | <img src="manipulator/.images/lekiwi_100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/lekiwi_101.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                               |
| Dobot          | [CR5](manipulator/Dobot/cr5_description)                    | Yes     | <img src="manipulator/.images/dobot_cr5.png" width="200" height="150" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/dobot_cr5_robotiq85.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                   |
| ARX            | [X5/R5](manipulator/ARX/arx5_description)                   | Yes     | <img src="manipulator/.images/arx_x5.png" width="200">    <img src="manipulator/.images/arx_r5.png" width="200">                                                                                                                                                                                                                                                                      |
| AgileX         | [Piper](manipulator/AgileX/piper_description)               | Yes     | <img src="manipulator/.images/agilex_piper.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/agilex_piper_master.png" width="200" height="120" style="object-fit: cover; object-position: center;">                                                                                                                    |
| AgileX         | [AgileX Aloha](manipulator/AgileX/agilex_aloha_description) | Yes     | <img src="manipulator/.images/agilex_split_aloha.png" width="200">   <img src="manipulator/.images/agilex_aloha2.png" width="200">                                                                                                                                                                                                                                                    |
| Galaxea        | [A1/A1X/A1Y](manipulator/Galaxea/galaxea_a1_description)    | Yes     | <img src="manipulator/.images/galaxea_a1.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1x.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1y.png" width="200" height="120" style="object-fit: cover; object-position: center;"> |
| Airbots        | [Play](manipulator/Airbots/airbot_play_description)         | Yes     | <img src="manipulator/.images/airbot_play.png" width="200">                                                                                                                                                                                                                                                                                                                           |
| Realman        | [RM65](manipulator/Realman/rm65_description)                | Yes     | <img src="manipulator/.images/realman_rm65.png" width="200">                                                                                                                                                                                                                                                                                                                          |

### Manipulator Robots with OCS2

I add mobile manipulator OCS2 config for some of the manipulator robots, you can use them with the
`manipulator_ocs2.launch.py` launch file. More details can be found in the [OCS2 documentation](docs/OCS2.md).

<img src="manipulator/.images/dobot_cr5_ocs2.gif" width="300" height="200" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/lekiwi_ocs2.gif" width="300" height="200" style="object-fit: cover; object-position: center;">

## Grippers

| Brand                                          | Models               | Repaint | Images                                                                                                                                                                                                                                              |
|------------------------------------------------|----------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ChangingTek](gripper/changingtek_description) | AG2F90-C<br>AG2F120S | Yes   | <img src="gripper/.images/tek_ag2f90c.png" width="150" height="150" style="object-fit: cover; object-position: center;">  <img src="gripper/.images/tek_ag2f120s.png" width="150" height="150" style="object-fit: cover; object-position: center;"> | |
| [Robotiq](gripper/robotiq_description)         | 2F-85                | Yes   | <img src="gripper/.images/robotiq_85.png" width="150" height="150" style="object-fit: cover; object-position: center;">                                                                                                                             |
| [Inspire](gripper/inspire_description) | EG2-4C2              | Yes   | <img src="gripper/.images/inspire_eg2.png" width="150" height="150" style="object-fit: cover; object-position: center;">                                                                                                                            |                                                                                                                                  |

## Quadruped Robots

| Brand         | Model                                               | Repaint | Images                                                        |
|---------------|-----------------------------------------------------|---------|---------------------------------------------------------------|
| Unitree       | [A1](quadruped/unitree/a1_description)              | No      | <img src="quadruped/.images/unitree_a1.png" width="200">      |
| Unitree       | [Aliengo](quadruped/unitree/aliengo_description)    | No      | <img src="quadruped/.images/unitree_aliengo.png" width="200"> |
| Unitree       | [Go1](quadruped/unitree/go1_description)            | Yes     | <img src="quadruped/.images/unitree_go1.png" width="200">     |
| Unitree       | [Go2](quadruped/unitree/go2_description)            | No      | <img src="quadruped/.images/unitree_go2.png" width="200">     |
| Unitree       | [B2](quadruped/unitree/b2_description)              | No      | <img src="quadruped/.images/unitree_b2.png" width="200">      |
| Deep Robotics | [Lite3](quadruped/deep_robotics/lite3_description)  | Yes     | <img src="quadruped/.images/deep_lite3.png" width="200">      |
| Deep Robotics | [X30](quadruped/deep_robotics/x30_description)      | Yes     | <img src="quadruped/.images/deep_x30.png" width="200">        |
| Xiaomi        | [CyberDog](quadruped/magiclab/cyberdog_description) | Yes     | <img src="quadruped/.images/cyberdog.png" width="200">        |
| MagicLab      | [MagicDog](quadruped/magiclab/magicdog_description) | Yes     | <img src="quadruped/.images/magicdog.png" width="200">        |
| ZsiBot        | [ZSL-1](quadruped/zsibot/zsl1_description)          | Yes     | <img src="quadruped/.images/zsl1.png" width="200">            |