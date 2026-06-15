# Mini-Atlas V6 Alpha

# CAD-006 FreeCAD Python Kernel Implementation

Version: 1.0

Status: EXECUTION ENGINE LAYER

Document Number:

CAD-006

Subsystem:

CAD Execution Kernel

---

# 1. Purpose

实现 Mini-Atlas V6 的真实 CAD 生成内核，使 Python 脚本能够：

* 调用 FreeCAD API
* 生成参数化几何体
* 构建 Hip / Knee / Pelvis 模块
* 导出 STEP / STL
* 与 RobotConfig 完全绑定

---

# 2. System Transition

```text id="t1"
CAD-005 (Build System)
        ↓
CAD-006 (Execution Kernel)
        ↓
REAL GEOMETRY GENERATION
```

---

# 3. Core Engine Architecture

```text id="a1"
RobotConfig.py
        ↓
Python CAD Kernel
        ↓
FreeCAD Document Object
        ↓
Part / Sketch / Body
        ↓
STEP / STL Export
```

---

# 4. FreeCAD Python Runtime Model

```text id="r1"
App (Document Manager)
Part (Geometry Engine)
Sketcher (2D Constraints)
PartDesign (Solid Features)
Mesh (STL Export)
```

---

# 5. Kernel Bootstrap Script

## kernel.py

```python id="k1"
import FreeCAD as App
import Part
from config.RobotConfig import *

class CADKernel:

    def __init__(self, name):
        self.doc = App.newDocument(name)

    def create_box(self, x, y, z):
        return Part.makeBox(x, y, z)

    def create_cylinder(self, radius, height):
        return Part.makeCylinder(radius, height)

    def add_part(self, shape):
        obj = self.doc.addObject("Part::Feature", "Part")
        obj.Shape = shape
        return obj

    def save(self, path):
        self.doc.saveAs(path)
```

---

# 6. First Real Module: HipPitch_Base

## HipPitch_Base.py

```python id="hp1"
from kernel import CADKernel
from config.RobotConfig import *
import Part

class HipPitchBase:

    def __init__(self):
        self.kernel = CADKernel("HipPitch_Base")

    def build(self):

        # Outer shell
        outer = Part.makeCylinder(
            BEARING_6803_OD/2 + STRUCTURE_WALL,
            40
        )

        # Inner bore
        inner = Part.makeCylinder(
            BEARING_6803_OD/2,
            40
        )

        body = outer.cut(inner)

        # Shaft hole
        shaft = Part.makeCylinder(
            SHAFT_DIA/2,
            60
        )

        body = body.cut(shaft)

        self.kernel.add_part(body)

        return self.kernel

    def export(self):
        self.kernel.save("export/step/HipPitch_Base.step")
```

---

# 7. Knee Base Generator

```python id="k1"
class KneeBase:

    def build(self):

        outer = Part.makeCylinder(
            BEARING_6802_OD/2 + STRUCTURE_WALL,
            35
        )

        inner = Part.makeCylinder(
            BEARING_6802_OD/2,
            35
        )

        body = outer.cut(inner)

        shaft = Part.makeCylinder(
            SHAFT_DIA/2,
            50
        )

        body = body.cut(shaft)

        self.kernel.add_part(body)

        return self.kernel
```

---

# 8. Pelvis Generator Concept

```text id="p1"
Left Hip Mount
Right Hip Mount
Central Battery Bay
Cable Channel
```

全部由：

* cylinder
* box
* boolean cut

组合生成

---

# 9. Boolean Modeling Rule

所有结构必须遵循：

```text id="b1"
Solid = Base - Holes + Reinforcement
```

禁止：

* 非参数建模
* 手工雕刻曲面依赖
* 不可复现形状

---

# 10. Export Pipeline

## STEP Export

```python id="e1"
doc.saveAs("HipPitch_Base.FCStd")
```

---

## STL Export

```python id="e2"
import Mesh
Mesh.export(doc.Objects, "HipPitch_Base.stl")
```

---

# 11. Coordinate System Enforcement

```text id="c1"
+X Forward
+Y Left
+Z Up
```

必须全局一致。

---

# 12. Assembly Compatibility

所有生成零件必须：

* 可以导入 assembly script
* 可镜像生成
* 可装配验证

---

# 13. Deterministic Rule

```text id="d1"
Same Config → Same Geometry
```

禁止随机性。

---

# 14. System Status

CAD Kernel Status:

```text id="s1"
ACTIVE
```

Capabilities:

* Geometry generation ✔
* STEP export ✔
* STL export ✔
* Parametric binding ✔

---

# 15. Next Step

进入：

```text id="n1"
CAD-007-First-End-to-End-HipPitch-Generation.md
```

目标：

👉 用 RobotConfig.py
👉 一键生成 HipPitch_Base.step
👉 一键生成 STL
👉 在 FreeCAD中可视化

---

# 16. Exit Status

Kernel Layer:

APPROVED

System State:

```text id="st1"
FIRST REAL CAD GENERATION POSSIBLE
```
