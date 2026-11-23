# Third-Party Notices

`robot-description` (TRON2 robot description) is distributed under the
Apache License 2.0 (see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE)).

This file lists third-party components, referenced hardware, and
per-asset provenance so downstream users can comply with all applicable
licenses and re-distribution terms.

> **Status:** items marked `⚠ TO CONFIRM` are pending sign-off from the
> hardware / product / legal owners. Do not cut a public release while
> any `⚠ TO CONFIRM` entry remains.

---

## 1. First-party assets (LimX Dynamics)

| Path | Kind | License | Notes |
|------|------|---------|-------|
| `tron2/*/urdf/*.urdf` | URDF | Apache-2.0 | Generated from `xacro/` sources. |
| `tron2/*/xacro/*.xacro` | xacro | Apache-2.0 | Hand-maintained. |
| `tron2/*/xml/*.xml` | MuJoCo model | Apache-2.0 | Hand-maintained. |
| `tron2/*/meshes/*.STL` | STL mesh | Apache-2.0 ⚠ TO CONFIRM | Exported from LimX-owned CAD. Confirm no third-party CAD is embedded (see §3). |
| `tron2/*/usd/*.usd` | USD asset | Apache-2.0 ⚠ TO CONFIRM | Same provenance question as STL. |

Generation pipeline (documented in [`ASSETS.md`](ASSETS.md)):
`SolidWorks / OnShape CAD  →  STL / USD export  →  URDF via xacro`.

---

## 2. External hardware referenced in the YG variants

The `WFYG_TRON2A` and `SFYG_TRON2A` variants **reference** the following
third-party hardware. This repository ships **geometry / collision meshes
only** for integration purposes; it does **not** ship vendor firmware,
SDKs, drivers, or precision CAD.

| Hardware | Referenced as | Vendor | Provenance of geometry | License / permission |
|----------|---------------|--------|------------------------|----------------------|
| RoboSense Fairy96 LiDAR | mesh on `transition_Link`, `radar_Link` | RoboSense | ⚠ TO CONFIRM (LimX-authored placeholder vs. vendor CAD) | ⚠ TO CONFIRM |
| AgileX Piper X arm | arm chain meshes on `WFYG` / `SFYG` / `DA` / `DACH` | AgileX Robotics | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| Huace M722 RTK | antenna / RTK box meshes on `antenna_*_Link` | Huace Navigation | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| NVIDIA Jetson Orin NX (compute) | compute box mesh on `transition_Link` | NVIDIA | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| Intel RealSense D435 | chest camera link `d435_Link` + optical frame | Intel | ⚠ TO CONFIRM | ⚠ TO CONFIRM |

**Owner action required:** For each row above, confirm one of the
following and update this file:

- **(A)** The mesh is a LimX-authored simplified placeholder, contains
  no vendor-derived CAD, and may be re-distributed under Apache-2.0.
  → Change `⚠ TO CONFIRM` to `Apache-2.0 (LimX placeholder)`.
- **(B)** The mesh is derived from a vendor CAD file that permits
  re-distribution. → Record the source URL, the vendor's re-distribution
  terms, and any attribution requirement.
- **(C)** Neither. → Replace the mesh with an approved placeholder before
  release and update this row.

---

## 3. Documentation media

| Path | Kind | Provenance | License |
|------|------|------------|---------|
| `docs/images/DA.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| `docs/images/DACH.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| `docs/images/WF.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| `docs/images/WFYG.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| `docs/images/SF_0.jpg`, `docs/images/SF_1.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |
| `docs/images/SFYG_0.jpg`, `docs/images/SFYG_1.jpg` | Photo / render | ⚠ TO CONFIRM | ⚠ TO CONFIRM |

Before release, run:
```bash
exiftool docs/images/*.jpg | grep -iE '(gps|serial|make|model|software|author|artist|copyright)'
```
and strip anything that discloses office locations, camera serials, or
individual contributors' names, unless intentionally kept:
```bash
exiftool -all= docs/images/*.jpg
```

---

## 4. Build / runtime toolchain (not redistributed)

The following are **runtime dependencies only** — they are neither
vendored nor packaged in this repository, but downstream users need
them to consume the assets.

| Tool | Purpose | License | Where obtained |
|------|---------|---------|----------------|
| xacro | Expand `.xacro` → `.urdf` | BSD-3-Clause | ROS distribution |
| urdfdom / `check_urdf` | URDF validation | BSD-2-Clause | ROS / package manager |
| MuJoCo | Load `xml/robot.xml` | Apache-2.0 (≥ 2.1.2) | https://mujoco.org |
| Isaac Sim | Load `usd/*.usd` | NVIDIA proprietary EULA | https://developer.nvidia.com/isaac-sim |
| RoboSense driver, RealSense SDK, Piper SDK, RTK driver | Runtime on physical hardware | Various | Vendor documentation |

None of the above are bundled here; users must obtain and license them
independently.

---

## 5. What this repository does **not** include

- No control policies (`.onnx`, `.pt`, `.pth`).
- No SDK binaries (`.so`, `.dll`, `.dylib`, `.lib`, wheels).
- No factory calibration values or per-serial calibration files.
- No motion / bag / trajectory data.
- No firmware.
- No customer- or site-specific configuration.

For those, see the sibling repositories in the `limxdynamics` org.

---

## 6. Update procedure

Whenever a mesh, USD, image, or upstream reference is added or changed:

1. Update the corresponding row in this file.
2. Re-run the EXIF strip (§3) and CAD-metadata scan (`strings` on the
   first 80 bytes of every STL).
3. If the change touches an `⚠ TO CONFIRM` row, block the merge on
   written sign-off from the responsible owner.
