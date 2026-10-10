---
name: urdf-to-xacro-package
description: >-
  Turn a plain URDF plus per-link meshes into a peer-style xacro description
  package in this repo (component macros, ros2_control stubs, sensor_models),
  validated against the original URDF. Use when packaging URDF, 转 xacro,
  对齐邻居包, component.xacro, robot_descriptions layout, or adding a new
  <robot>_description from an existing URDF.
---

# Plain URDF and meshes to a structured xacro package

Prior stage: [web-robot-asset-extraction](../web-robot-asset-extraction/SKILL.md).
Next (wheeled dual-arm control): [import-humanoid-ocs2](../import-humanoid-ocs2/SKILL.md).
Chassis GLB split / simple colliders: [split-chassis-glb](../split-chassis-glb/SKILL.md).

Goal: rewrite a working URDF as a xacro package that looks like its neighbors in
this repo, without changing any kinematics, limits, inertials or meshes.

## 1. Learn the repo's conventions first

Read 3 to 6 neighboring description packages of the same kind: humanoids, mobile
manipulators, wheeled bases. Note the following, and follow whatever most of
them do:

- Package path pattern, such as `<category>/<Brand>/<robot>_description`, and
  the brand folder's casing.
- Layout: `xacro/robot.xacro`, `xacro/component.xacro` with a `type` argument,
  `xacro/components/*.xacro`, `xacro/ros2_control/{robot,interfaces}.xacro`, and
  `config/ros2_control/ros2_controllers.yaml`. Note whether `config/ocs2`,
  launch or rviz files exist.
- Macro naming, such as PascalCase with a robot prefix, and how left and right
  are handled (often a `direction:=1/-1` parameter on one shared arm macro).
- Arguments such as `enable_wheel_joints` (wheeled robots often default to fixed
  in `robot.xacro` and true in `component.xacro`) and `isaac` (hides sensor
  meshes).
- Angle style, such as `${deg/180*PI}`, and mesh path style, such as
  `file://$(find pkg)/meshes/x.glb` versus `package://`.
- `package.xml` format and `exec_depend` entries (for example
  `robot_common_launch`, `sensor_models`), the CMake install directories, and
  README style.
- Whether packages ship a generated URDF. Usually they do not.

Check how sensors are included. A `sensor_models` package may provide only
meshes and no macros, in which case neighbors write a link with a visual mesh
plus a fixed joint, often wrapped in `<xacro:unless value="${isaac}">`. Copy
that pattern and do not invent macros. If a needed sensor mesh is missing, say
so.

## 2. Generate, don't hand-copy

- Write a small script that parses the source URDF and emits the component xacro
  files, so every number comes from the original.
- Split by component: chassis or wheels, body (lift, fold, waist), head, arm
  (one macro for both sides), gripper. Express left/right asymmetry as
  `${a if direction == 1 else b}`.
- Add a ros2_control xacro for the hardware types the neighbors support (mock,
  gz, isaac) and a controllers yaml with the same controller groups.
- Replace bare sensor frames with sensor-model visuals at the source poses. If
  the sensor mesh origin differs from the source frame, for example a frame on
  the mounting face, keep the frame pose and put the offset on the visual
  origin. Fit that offset against the body mesh and report it.
- Leave out configuration that cannot be derived from available data, such as
  MPC weights, and say so rather than filling it with guesses.
- Do **not** put `ROS_DOMAIN_ID` in the package README.

## 3. Validate

- Expand every variant with xacro: the full robot with default arguments, with
  each flag toggled, each ros2_control hardware type, and every component `type`
  and side. If ROS is not installed, use the pip `xacro` package with a small
  `ament_index_python` stub so `$(find)` resolves.
- Run `check_urdf` (from `liburdfdom-tools`) on each output, and record the
  joint and link counts.
- Semantically diff the source URDF against the expanded full robot (with flags
  matching the original, such as wheel joints enabled). Compare joint types,
  parents and children, origins, axes, limits, inertials and mesh files within a
  tolerance. The only differences should be the intended ones.
- Confirm that every referenced mesh path exists.
- A component that produces two root links (such as both grippers at once) will
  fail `check_urdf`, so generate one side per call.

## 4. Ship

- Update `package.xml`, `CMakeLists.txt`, the README and the parameter doc to
  match the neighbors.
- Prefer iterate on the local ROS machine with symlink-install when the user
  needs to relaunch. Make a normal commit on the requested branch and push it.
  Never force-push.
- If the push fails for authentication on a box, run `gh auth login` and then
  `gh auth setup-git`.
- Report which packages you followed, the new layout, the validation table, the
  intended differences, the commit hash and the push result.

## 5. Next: control stack

Visualization-only packages still need ros2_control and OCS2. After the xacro
package exists, continue with
[import-humanoid-ocs2](../import-humanoid-ocs2/SKILL.md) when the robot is a
wheeled dual-arm (or the closest peer control recipe for other morphologies).
