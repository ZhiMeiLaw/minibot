# Mini-Atlas V6 Alpha

# CAD-005 Assembly and Build System

Version: 1.0

Status: SYSTEM EXECUTION CORE

Document Number:

CAD-005

Subsystem:

Build & Automation System

---

# 1. Purpose

建立 Mini-Atlas V6 Alpha 的完整自动构建系统（Build System），实现：

* 一键生成 CAD 模型
* 自动装配单腿 / 双腿 / 全身
* 自动导出 STEP / STL
* 自动生成验证报告
* 支持完整重建（Full Regeneration）

---

# 2. Core Concept

```text id="c1"
RobotConfig.py
        ↓
Python CAD Generator
        ↓
FreeCAD Geometry Engine
        ↓
Assembly Builder
        ↓
Exporter (STEP / STL)
        ↓
Validation System
```

---

# 3. Build System Architecture

```text id="a1"
scripts/
    build_all.py
    build_leg.py
    build_knee.py
    build_hip.py
    build_full_body.py
    export_step.py
    export_stl.py
    validate.py
```

---

# 4. Main Build Script

## build_all.py

```python id="b1"
from modules.hip_roll import HipRoll
from modules.hip_pitch import HipPitch
from modules.knee import Knee
from assemblies.full_body import FullBody
from config.RobotConfig import *

def build_all():
    print("Starting Mini-Atlas V6 Build...")

    hip_roll = HipRoll(RobotConfig)
    hip_pitch = HipPitch(RobotConfig)
    knee = Knee(RobotConfig)

    full_body = FullBody(
        hip_roll,
        hip_pitch,
        knee
    )

    full_body.build()

    full_body.export_step("export/step/")
    full_body.export_stl("export/stl/")

    print("Build Complete")

if __name__ == "__main__":
    build_all()
```

---

# 5. Module Build Interface

所有模块必须实现：

```python id="m1"
class Module:

    def __init__(self, cfg):
        self.cfg = cfg

    def build(self):
        pass

    def export_step(self, path):
        pass

    def export_stl(self, path):
        pass
```

---

# 6. Assembly System

## Full Body Assembly

```text id="ab1"
Pelvis
    ↓
Hip Roll (L/R)
    ↓
Hip Pitch (L/R)
    ↓
Knee (L/R)
    ↓
Lower Leg
```

---

## Assembly Rule

* Left / Right 自动 mirror
* 所有模块必须来自 config
* 禁止手工修改 assembly

---

# 7. Export System

## STEP Export

```text id="e1"
export/step/
    MiniAtlas_FullBody.step
```

用途：

* 装配检查
* 外部软件分析
* 工程存档

---

## STL Export

```text id="e2"
export/stl/
    Knee_Base_Print.stl
```

用途：

* 3D打印
* Bambu Studio 导入
* A1 Mini制造

---

# 8. Validation System

## validate.py

检查：

* 尺寸一致性
* 干涉检查
* 对称性
* 重量预算
* 可制造性

---

输出：

```text id="v1"
Validation_Report.pdf
```

---

# 9. Regeneration System

```text id="r1"
任何参数变更 → 全系统重建
```

触发条件：

* RobotConfig.py 修改
* 结构参数变化
* 新版本 Servo / Bearing

---

# 10. Symmetry Engine

```text id="s1"
mirror(axis="Y")
```

规则：

* Left = Generated
* Right = Mirror
* 禁止手动复制

---

# 11. Build Modes

## Mode 1: Full Build

```text id="bm1"
build_all()
```

---

## Mode 2: Partial Build

```text id="bm2"
build_leg()
build_knee()
```

---

## Mode 3: Debug Build

```text id="bm3"
single module generation
```

---

# 12. System Constraints

必须保证：

* 可重复构建（Deterministic Build）
* 无人工CAD依赖
* 所有模型来源参数系统
* 输出一致性100%

---

# 13. Output Definition

每次 build 必须生成：

* STEP files
* STL files
* Assembly tree
* Validation report
* Weight report

---

# 14. Next Step

进入：

```text id="n1"
CAD-006-FreeCAD-Python-Kernel-Implementation.md
```

实现：

* FreeCAD Python API 对接
* 自动生成 Hip / Knee / Pelvis 几何体
* 第一个真实“可运行CAD生成器”

---

# 15. Status

Build System:

APPROVED

System State:

```text id="st1"
READY FOR REAL CAD GENERATION ENGINE
```
