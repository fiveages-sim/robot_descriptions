---
name: obj-to-glb
description: >-
  Batch-convert description-package OBJ/MTL visuals to GLB with Blender,
  splitting each mesh by loose parts. Use when converting meshes to GLB,
  OBJ 转 GLB, 批量替换 mesh, Blender API, 按松散零部件拆分, separate loose,
  flat normals, v//vn, 破面, or export_yup.
---

# OBJ to GLB for description visuals

Canonical example: [unitree_g1_description](../../../humanoid/Unitree/unitree_g1_description/).
Chassis split / simple colliders: [split-chassis-glb](../split-chassis-glb/SKILL.md).

Use **Blender's Python API** (`blender --background --python`), not trimesh.
trimesh keeps face positions and then writes averaged vertex normals. These
OBJ shells are flat (`f v//vn`, one normal shared by the three corners), so
that average cracks every sharp edge in RViz (破面).

## Import

Start from an empty file (`bpy.ops.wm.read_factory_settings(use_empty=True)`).
The default Cube must not be exported.

These OBJ files are already ROS Z-up (X forward, Y left, Z up). Blender's
default OBJ import is Y-up / −Z forward and will rotate them. Import with:

```python
bpy.ops.wm.obj_import(
    filepath=obj_path,
    up_axis="Z",
    forward_axis="Y",
    use_split_objects=True,
    validate_meshes=False,
)
```

`validate_meshes=False` so Blender does not rewrite the shell. The importer
keeps custom split normals (`mesh.has_custom_normals`). Do not Shade Smooth
and do not clear custom normals.

MTL must sit next to the OBJ. `baseColorFactor` comes from `Kd`.

## Separate by loose parts

One OBJ is often several shells that only share the file. Before export, split
them the way Blender's Mesh → Separate → By Loose Parts does. They stay in
**one** GLB (one node per island). Do not emit one file per part; the xacro
still points at a single mesh per link.

```python
bpy.ops.object.select_all(action="DESELECT")
for obj in mesh_objects:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.separate(type="LOOSE")
bpy.ops.object.mode_set(mode="OBJECT")
```

RViz walks the whole node tree, so 22 torso islands in one file are fine.
Origins stay put; do not apply a location that recenters a part.

## Export

```python
bpy.ops.export_scene.gltf(
    filepath=glb_path,
    export_format="GLB",
    export_yup=False,
    export_normals=True,
    export_materials="EXPORT",
    export_texcoords=False,
    export_animations=False,
    export_skins=False,
    export_lights=False,
    export_cameras=False,
)
```

`export_yup=False` is required on Blender 5.2. `export_yup=True` bakes
`(x, y, z) -> (x, z, -y)` into the buffers and leaves the node at **identity**.
RViz does not add its own Y-up fix, so the link lies on its side. Older
Blender left a +90° X node rotation under that flag (`head.glb`, `logo.glb`);
do not reconvert those.

Keep one left-side GLB. Mirror the other side in xacro with
`scale="1 ${direction} 1"` (`direction` is `1` on the left and `-1` on the
right). Do not export a second `*_right` GLB from the right USD.

## Validate before deleting OBJ/MTL

Load the GLB the way RViz does (node transforms applied) and compare to the OBJ:

- Face count equal.
- World AABB and signed volume match (float32 noise only).
- Inward-normal face count matches the OBJ. A difference of one or two faces
  is the importer; a large jump means normals were smoothed.
- Node translations are identity. A loose part must not have moved.

Retarget xacro `.obj` → `.glb` and delete `.obj`/`.mtl` only after that.

Ogre caches a mesh by its path. Restart RViz after an in-place replace.
`symlink-install` sees the new file; a copied install needs a rebuild.

## Do not

- Use trimesh (or any path that recomputes smooth vertex normals) for these shells.
- Import with Blender's default Y-up OBJ axes.
- Use `export_yup=True` on Blender 5.2 for an already Z-up mesh.
- Trust accessor `min`/`max` when a node rotation is present.
- Put visual GLB on collision / `selfCollision` (see split-chassis-glb §8).
