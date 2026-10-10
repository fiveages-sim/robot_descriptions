---
name: web-robot-asset-extraction
description: >-
  Probe a company interactive 3D product/blog page for robot simulation assets
  (URDF/MJCF/USD, GLB/glTF meshes, kinematic JSON), decode base64 meshes, infer
  joint limits and inertias, and label official vs inferred. Use when extracting
  from a web viewer, 官网 3D, 产品页模型, urdf from website, base64 GLB,
  model-viewer, three.js robot, or rebuilding a best-effort URDF from public
  page assets.
---

# Extract robot simulation assets from a web 3D viewer

Next stage after a usable URDF: [urdf-to-xacro-package](../urdf-to-xacro-package/SKILL.md).
Then control: [import-humanoid-ocs2](../import-humanoid-ocs2/SKILL.md).

Goal: find out what the page actually serves (kinematic tree, visual meshes,
trajectories), say plainly whether a complete sim asset exists, and if not,
rebuild a best-effort URDF with clearly labeled inferred values.

## 1. Probe the page (curl, no browser)

- Save the HTML and every JS chunk it loads, including lazily loaded viewer
  chunks. Search with
  `rg -i 'urdf|mjcf|usd|glb|gltf|\.json|three|model-viewer|spline|sketchfab|babylon|draco|meshopt'`.
- Follow asset URLs and record HTTP status, content type, size and SHA-256.
  Check `robots.txt` and the sitemap. Keep requests low volume: guess only a
  handful of obvious names such as `<robot>.urdf`, and never brute-force a
  wordlist.
- Note any license, download button, "request access" text, or acceptable-use
  policy on the page.
- Watch for disguised assets: GLB served as base64 text (`*.glb.txt`), Draco or
  meshopt compression, and several copies of the model for different figures.

## 2. Classify what you found

- **Kinematic JSON:** joints with name, type, parent, child, xyz, rpy and axis.
  Check whether limits, effort, velocity, mass, inertia, visual or collision are
  present (usually they are not).
- **Visual meshes:** decode the base64, decompress to a plain GLB with
  gltf-transform, then inspect node names, hierarchy, animations, skins,
  triangle counts and bounds. A name like `<link>__<i>`, or materials called
  `urdf_*`, means it was exported from an unpublished URDF. Leftover OBJ names
  in `extras` hint at the original per-link files.
- **Trajectories:** joint-angle or link-pose replays. These are data, not a
  model description.
- **Comparing copies:** compare per-link triangle counts, bounds and
  nearest-vertex distance to tell whether the copies are the same mesh with
  different compression or a separate lower-poly export. Use the densest
  complete copy as the main source and fill missing links from the others.
- Report the result as yes, no or partial, with the exact public URLs and which
  files are visual-only and which are kinematic.

## 3. Joint-limit clues

Keep three kinds of evidence separate, and never present one as another:

- (a) values the site states explicitly,
- (b) values hardcoded in viewer code, such as gripper travel or clamp ranges,
- (c) ranges observed in trajectories. Compute per-joint min, max and peak
  speed into a CSV. These are lower bounds only.

To infer limits from geometry:

- Run forward kinematics with the meshes and sample points on their surfaces,
  weighted by area.
- Sweep each joint in about 5° steps. Check the minimum distance to the parent
  link (excluding a small sphere around the hinge) and separately to non-parent
  links.
- Snap the collision-free range to integer degrees. It must still contain the
  observed trajectory range.
- A joint with no stop, such as a wheel or a steering joint that clears a full
  turn, becomes `continuous`.
- Document the collision or feature that set each limit.

## 4. Mass and inertia by reference

- Pick public robots with similar structure, for example an arm with planetary
  actuators, a waist with a folding lift, or a swerve or skid base. Fetch their
  real URDF or xacro and record the source path and commit.
- Map each link to its closest reference link. Let k be the ratio of joint
  spacings. Scale mass by k³ and inertia by k⁵, and take the center of mass from
  the mesh centroid.
- If a link has no credible reference, or the scaled mass would exceed a
  solid-aluminum fill of its bounding box, leave it unknown. Do not make up a
  number.
- Effort and velocity limits come from the same reference robot and are labeled
  as borrowed.

## 5. Build the URDF

- Split the visual GLB into one file per link: bake each node to world
  coordinates, move it under the scene root, delete the other nodes, then
  `prune()`, keeping materials. At the zero pose, world coordinates equal link
  coordinates, so the visual needs no origin offset.
- Keep meshes as GLB unless the target toolchain needs STL.
- Assemble the URDF from the kinematic tree, per-link meshes, inferred limits
  and borrowed inertials.
- Sensor frames such as lidars, cameras and IMUs are usually meshless fixed
  links. Identify them from their names and cross-check their poses against
  domes or cutouts on the body mesh.

## 6. Report

- Plainly say what is official, what was inferred, and what is unknown.
- Save a parameter doc listing each joint's limit with its evidence, and each
  link's mass with its reference and scale factor.
- If the asset is going into this repo, continue with
  [urdf-to-xacro-package](../urdf-to-xacro-package/SKILL.md).
