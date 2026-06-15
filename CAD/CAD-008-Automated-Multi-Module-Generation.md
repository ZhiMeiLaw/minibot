# Mini-Atlas V6 Alpha

# CAD-008 Automated Multi Module Generation

Version: 1.0

Status: SYSTEM SCALING LAYER

Document Number:

CAD-008

Subsystem:

Multi-Module CAD Generator

---

# 1. Purpose

实现 Mini-Atlas V6 的多模块自动生成能力：

* Hip Roll / Hip Pitch / Knee 自动生成
* Pelvis 自动生成
* 左右腿自动镜像生成
* 全下肢 Assembly 自动构建

---

# 2. System Evolution

```text id="e1"
CAD-007 (Single Module)
        ↓
CAD-008 (Multi Module Generator)
```

---

# 3. Generation Target

Primary Output:

```text id="g1"
Left Leg Assembly
Right Leg Assembly
Pelvis Assembly
```

Final Output:

```text id="g2"
Lower Body System
```

---

# 4. Architecture

```text id="a1"
RobotConfig.py
        ↓
Module Generator Engine
        ↓
HipRoll Generator
HipPitch Generator
Knee Generator
Pelvis Generator
        ↓
Assembly Builder
        ↓
Mirror System
        ↓
Export System
```

---

# 5. Core Generator Engine

```python id="c1"
class ModuleFactory:

    def __init__(self, cfg):
        self.cfg = cfg

    def build_hip_roll(self):
        return HipRoll(self.cfg).build()

    def build_hip_pitch(self):
        return HipPitch(self.cfg).build()

    def build_knee(self):
        return Knee(self.cfg).build()
```

---

# 6. Assembly Generator

```python id="a2"
class AssemblyBuilder:

    def build_leg(self, side="L"):

        hip_roll = ModuleFactory(cfg).build_hip_roll()
        hip_pitch = ModuleFactory(cfg).build_hip_pitch()
        knee = ModuleFactory(cfg).build_knee()

        leg = {
            "hip_roll": hip_roll,
            "hip_pitch": hip_pitch,
            "knee": knee
        }

        if side == "R":
            leg = self.mirror(leg)

        return leg
```

---

# 7. Mirror System

FreeCAD

```python id="m1"
def mirror(self, module):
    return module.transform(axis="Y", scale=-1)
```

规则：

* Left = Base model
* Right = Mirror
* 禁止手工复制建模

---

# 8. Pelvis Generator

```python id="p1"
class Pelvis:

    def build(self):

        left_mount = self.create_hip_socket(+1)
        right_mount = self.create_hip_socket(-1)

        battery_slot = self.create_battery_bay()

        cable_channel = self.create_wire_path()

        return self.combine([
            left_mount,
            right_mount,
            battery_slot,
            cable_channel
        ])
```

---

# 9. Full Lower Body Assembly

```text id="f1"
Pelvis
  ↓
Left Hip Roll
  ↓
Left Hip Pitch
  ↓
Left Knee

Pelvis
  ↓
Right Hip Roll
  ↓
Right Hip Pitch
  ↓
Right Knee
```

---

# 10. Build Pipeline

```text id="b1"
build_lower_body()

    ↓

generate_modules()

    ↓

mirror_right_side()

    ↓

assemble_pelvis()

    ↓

validate_geometry()

    ↓

export_step()

    ↓

export_stl()
```

---

# 11. Output Structure

```text id="o1"
export/
    step/
        Pelvis.step
        LeftLeg.step
        RightLeg.step
        LowerBody.step

    stl/
        Pelvis.stl
        LeftLeg.stl
        RightLeg.stl
```

---

# 12. Validation Layer

必须验证：

* Symmetry correctness
* Assembly alignment
* Interference free
* Weight balance
* Printability

---

# 13. Deterministic Rule

```text id="d1"
Same RobotConfig → Same Entire Lower Body
```

禁止：

* 手动调整单个腿结构
* 非镜像右腿设计
* 非参数偏移

---

# 14. System Capability After This Stage

系统能力提升为：

```text id="s1"
✔ Single module generation
✔ Multi-module generation
✔ Symmetry system
✔ Assembly system
```

---

# 15. Next Step

进入：

```text id="n1"
CAD-009-Full-Lower-Body-Assembly-Validation.md
```

目标：

👉 验证完整下肢结构
👉 CG / balance simulation
👉 步态准备前结构验证
👉 为 full body integration 做准备

---

# 16. Status

Multi Module System:

APPROVED

System State:

```text id="st1"
LOWER BODY GENERATION SYSTEM ACTIVE
```
