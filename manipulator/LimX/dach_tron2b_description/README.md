# DACH_TRON2B description

The geometry comes from LimX Dynamics' TRON2 robot description at
`d81d2a83a3c718bc68deca4e8804fdc984dc34f7`, under `tron2b/DACH_TRON2B`.
The full robot entry point is `xacro/robot.xacro`. It instantiates the body,
head, two arms and two articulated grippers from `xacro/components/`.
The robot has 18 independent movable joints and 16 gripper mimic joints.

For component inspection, expand `xacro/component.xacro` with
`type:=body`, `type:=head`, `type:=arm`, or `type:=gripper`.
Pass `side:=L` or `side:=R` for the arm or gripper. The component entry point
provides an empty attachment link where needed to form a standalone URDF tree.

The mesh directory follows the assembly parts: `body`, `head`, `arm`, and
`gripper`. The arms share one file per visual or collision shape. Shoulder,
elbow, and wrist pitch use the official left-arm meshes as the canonical
geometry. Right-arm occurrences of these shapes mirror the mesh along its
local Y axis (`scale="1 -1 1"`). This is a symmetric model convention.
The original right-arm STL surfaces differ locally. OCS2 uses independently
configured primitive collision shapes for its active collision pairs.

Wrist yaw uses a 180-degree local Z rotation on the right. Wrist roll and its
collision mesh are shared directly. Both grippers share their base,
nut, bar, crank, and jaw meshes, with local Z rotations where needed. For
these wrist yaw, wrist roll, and gripper reuses, the maximum sampled surface
distance was below 0.03 mm. Joint transforms, limits, and inertial data
are carried over from the articulated-gripper source URDF.

## Visual materials

The package uses seven shared materials with lowercase `snake_case` names.
Colors are sRGB hex values; Blender/glTF base colors are stored in linear RGB.

| Material | sRGB color | Metallic | Roughness | Emission strength |
|---|---|---|---|---|
| metal_dark_gray | #50565C | 0.50 | 0.43 | 0 |
| metal_medium_gray | #767D83 | 0.48 | 0.40 | 0 |
| metal_light_gray | #969B9F | 0.48 | 0.38 | 0 |
| polymer_matte_black | #191C20 | 0 | 0.64 | 0 |
| optical_gloss_black | #080C10 | 0 | 0.20 | 0 |
| accent_red | #C62C25 | 0.25 | 0.33 | 0 |
| light_blue | #19CAFF | 0 | 0.26 | 2.2 |

Most arm housings and the head's outer shell use `metal_light_gray`.
The torso front cover, small hardware plates, and gripper carrier use
`metal_medium_gray`. The torso side shells, neck, and face panel around the
camera use `metal_dark_gray`. The face panel is distinct from the narrow
`optical_gloss_black` camera window. Joint inserts, front-cover latches,
and gripper fingers retain `polymer_matte_black`. The torso lamp faces preserve the selected geometry.
Both arms reuse the same colored component meshes.

The color zoning was compared against the
[official product page](https://www.limxdynamics.com/zh/products/tron2),
[dual-arm product image](https://limx-video-oss.limxdynamics.com/limx-website/products/tron2/arm-ball-catch.png),
[load demonstration image](https://limx-video-oss.limxdynamics.com/limx-website/products/tron2/img-1-new.webp),
and the official tabletop operation photos on that page. Reseller photographs
were cross-checked, but images of older housings were not used to redefine
TRON2B's face or torso geometry. These are visual approximations, not factory
paint codes or measured PBR parameters; lighting and exposure vary by image.

GLB is the default visual format and stores the PBR materials.
OCS2 self-collision uses torso and gripper-base boxes and arm cylinders.
Some other links retain STL collision geometry. The `isaac:=true` URDF
export selects STL visuals, while the maintained FaSim asset uses
GLB-derived USD visuals and a separate PhysX contact configuration.

## ROS 2 mock and OCS2

Build in the Ubuntu container from the open workspace. The commands use the
existing FiveAges controller install as the underlay.

```bash
source /opt/ros/jazzy/setup.bash
source ~/fa-deploy-ws/install/setup.bash
cd ~/open-deploy-ws
colcon build --symlink-install \
  --base-paths src/robot-descriptions/manipulator/LimX/dach_tron2b_description \
  --packages-select dach_tron2b_description
source install/setup.bash
ros2 launch dach_tron2b_description demo.launch.py
```

The demo starts the arm controller in HOLD and spawns both gripper controllers.
In another terminal with the same setup, run
`ros2 run controller_manager spawner dach_tron2b_head_controller` to activate
head control. Use `/dach_tron2b_head_controller/commands` with two positions in
radians, yaw followed by pitch. Publish `std_msgs/msg/Float64` to
`/left_gripper_controller/target_percent` or
`/right_gripper_controller/target_percent`, with 0 for closed and 1 for open.
The gripper driver range is -0.09522 to 0.77302 rad.

The dual-arm task plans the 14 arm joints only. The order measured with
Pinocchio is left shoulder-to-wrist then right shoulder-to-wrist. Head and
gripper joints are fixed within the planning model. The runtime model retains
both articulated grippers. The `L_ee_link` and `R_ee_link` TCP origins are
the factory offsets from the matching gripper-base frames
(`-0.0021 0 -0.1313` m), taken from `robot_zeromass_graser.urdf`.
The planning TCPs use the factory flange-relative offset on the corresponding
gripper-base frames in this package. Self-collision is active with 12 link
pairs and a 10 mm configured minimum distance. The HOME targets for the
independent movable grippers are listed under `home_grippers` in
`ros2_controllers.yaml`. The package demo starts the same HOME node for mock and
Isaac. For Isaac, launch with `hardware:=isaac` after starting the FaSim bridge.
The generic OCS2 demo can be used without the package-specific HOME action.

## Validation

Expand and check all supported model variants from a sourced ROS environment:

```bash
python3 src/robot-descriptions/manipulator/LimX/dach_tron2b_description/scripts/validate_description.py \
  ~/upstream/tron2-robot-description/tron2b/DACH_TRON2B/urdf
```

The audit checks xacro expansion, URDF structure, mesh references, and the
factory model's joint and inertial data. See [VALIDATION.md](VALIDATION.md) for
the results and the scope of the simulation checks. Set the ROS package
maintainer before submission.

