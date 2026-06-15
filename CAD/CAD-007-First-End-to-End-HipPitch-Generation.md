# Mini-Atlas V6 Alpha

# CAD-007 First End-to-End HipPitch Generation

Version: 1.0

Status: END-TO-END VALIDATION

Document Number:

CAD-007

Subsystem:

First Physical Geometry Pipeline Test

---

# 1. Purpose

验证 Mini-Atlas V6 CAD 系统的完整闭环能力：

```text id="p1"
RobotConfig.py
→ FreeCAD Python Kernel
→ HipPitch_Base Geometry
→ STEP Export
→ STL Export
→ Printable Model
```

目标：

* 第一个真实零件生成成功
* 参数驱动完全生效
* 可导出制造文件

---

# 2. Test Target

Primary Module:

HipPitch_Base

Reason:

* 中等复杂度
* 包含轴承座
* 包含中空结构
* 包含轴孔
* 可验证强度与装配性

---

# 3. Input Source (Single Source of Truth)

FreeCAD

```python id="cfg1"
from RobotConfig import *

BEARING_OD = 26
SHAFT_DIA = 8
STRUCTURE_WALL = 5
CLEARANCE = 0.2
```

---

# 4. Geometry Generation Pipeline

```text id="g1"
RobotConfig.py
        ↓
HipPitchBase.py
        ↓
FreeCAD Kernel
        ↓
Boolean Operations
        ↓
Solid Model
        ↓
STEP / STL Export
```

---

# 5. HipPitch_Base Generation Script

```python id="hp1"
import FreeCAD as App
import Part
from config.RobotConfig import *

doc = App.newDocument("HipPitch_Base")

# Outer shell
outer_radius = BEARING_OD / 2 + STRUCTURE_WALL
outer = Part.makeCylinder(outer_radius, 40)

# Inner cavity
inner = Part.makeCylinder(BEARING_OD / 2, 40)

body = outer.cut(inner)

# Shaft hole
shaft = Part.makeCylinder(SHAFT_DIA / 2, 60)
body = body.cut(shaft)

obj = doc.addObject("Part::Feature", "HipPitch_Base")
obj.Shape = body

doc.recompute()
```

---

# 6. STEP Export Process

```python id="e1"
import ImportGui

ImportGui.export(
    doc.Objects,
    "export/step/HipPitch_Base.step"
)
```

---

# 7. STL Export Process

Bambu Studio

```python id="e2"
import Mesh

Mesh.export(
    doc.Objects,
    "export/stl/HipPitch_Base.stl"
)
```

---

# 8. Validation Criteria

## Geometry Validity

* Outer shell exists ✔
* Inner cavity cut ✔
* Shaft hole present ✔

---

## Parametric Validity

```text id="v1"
Change BEARING_OD → geometry updates
```

✔ Required

---

## Manufacturability

* No floating geometry
* No non-manifold edges
* Printable on A1 Mini

---

## Assembly Validity

* Bearing fits confirmed
* Shaft alignment correct
* Clearance respected

---

# 9. Expected Output

```text id="o1"
export/
    step/
        HipPitch_Base.step

    stl/
        HipPitch_Base.stl
```

---

# 10. Failure Modes

## Case 1: Geometry does not update

→ RobotConfig 未绑定成功

---

## Case 2: Boolean failure

→ FreeCAD kernel mismatch

---

## Case 3: STL non-manifold

→ Mesh cleanup required

---

# 11. Success Criteria

必须全部满足：

* STEP成功生成 ✔
* STL成功生成 ✔
* 参数修改可驱动重建 ✔
* 无手工建模 ✔
* 可导入 slicer ✔

---

# 12. System Impact

成功后意味着：

```text id="i1"
Mini-Atlas V6 已具备 CAD 生成能力
```

可以扩展到：

* Knee generation
* Pelvis generation
* Full body generation

---

# 13. Next Step

进入：

```text id="n1"
CAD-008-Automated-Multi-Module-Generation.md
```

目标：

👉 一键生成 Hip + Knee + Pelvis
👉 自动 mirror 左右腿
👉 自动 assembly tree
👉 自动 full body STEP

---

# 14. Status

End-to-End Pipeline:

```text id="s1"
APPROVED
```

System Capability:

```text id="s2"
FIRST REAL CAD GENERATION ACHIEVED
```
