# Cursor skills for robot-descriptions

Project skills live here so agents working on this repo can load them.

```
.cursor/skills/
  README.md
  <skill-name>/
    SKILL.md          # required
    reference.md      # optional
    scripts/          # optional
```

## Add a skill

1. Create `.cursor/skills/<skill-name>/SKILL.md`.
2. `name` must be lowercase letters, numbers, and hyphens only.
3. `description` must say **what** it does and **when** to use it (include Chinese and English trigger terms).
4. Keep `SKILL.md` under 500 lines. Put long examples in `reference.md`.

Do not put skills in `~/.cursor/skills-cursor/` (Cursor internals).

## Pipeline

Typical flow for a new wheeled dual-arm: **extract → package → OCS2**. Skip
stages that are already done. Cross-links live inside each skill.

| Stage | Skill | Use when |
|-------|-------|----------|
| 1. Extract | [web-robot-asset-extraction](web-robot-asset-extraction/SKILL.md) | Company interactive 3D page; probe URDF/meshes/kinematics; decode base64 GLB; infer limits/inertia; label official vs inferred |
| 2. Package | [urdf-to-xacro-package](urdf-to-xacro-package/SKILL.md) | Plain URDF + meshes → peer-style xacro package (`component` macros, ros2_control stubs, sensor_models) |
| 3. Control | [import-humanoid-ocs2](import-humanoid-ocs2/SKILL.md) | Wheeled dual-arm ros2_control / OCS2: Pinocchio order, structured `modeSequence`, `bodyRelative`, `HEAD_GAZE`; Taku/Quanta are worked examples only |
| Chassis | [split-chassis-glb](split-chassis-glb/SKILL.md) | Split chassis GLB into `chassis` / `steer` / `wheel`, write swerve xacro, and add `collider:=simple` boxes from glTF-node AABBs |

Shared habits: prefer local ROS + symlink-install before push; never document
`ROS_DOMAIN_ID` in package READMEs; never force-push; keep Isaac convex/CoACD
out of description PRs unless asked.
