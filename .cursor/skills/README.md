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

## Skills

| Skill | Use when |
|-------|----------|
| [split-chassis-glb](split-chassis-glb/SKILL.md) | Split chassis GLB into `chassis` / `steer` / `wheel`, write swerve xacro, and add `collider:=simple` boxes from glTF-node AABBs |
