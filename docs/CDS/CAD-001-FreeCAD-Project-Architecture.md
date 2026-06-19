# Mini-Atlas V6 Alpha

# CAD-001 FreeCAD Project Architecture

Version: 1.0

Status: SYSTEM FOUNDATION

Document Number:

CAD-001

Subsystem:

CAD Infrastructure

---

# 1. Purpose

建立 Mini-Atlas V6 的参数化CAD工程结构，使所有机械结构可通过代码自动生成。

目标：

* 消除手工建模依赖
* 所有零件参数化
* 支持批量重建
* 支持结构级修改传播
* 支持自动导出 STEP / STL

---

# 2. CAD Philosophy

本项目CAD系统遵循：

```text id="cadsys01"
Single Source of Truth = RobotConfig.py
```

所有几何必须来自：

* 参数
* 约束
* 函数

而不是手工几何编辑。

---

# 3. Toolchain

Primary CAD Engine:

FreeCAD

Automation Layer:

Python API (FreeCAD scripting)

Export Pipeline:

* STEP (Assembly)
* STL (Printing)
* SVG (2D drawings)

Slicing:

Bambu Studio

---

# 4. Project Directory Structure

```text id="proj001"
MiniAtlas_V6_CAD/

├── config/
│   ├── RobotConfig.py
│   ├── MaterialConfig.py
│   └── ServoConfig.py
│
├── core/
│   ├── primitives/
│   ├── bearings/
│   ├── tubes/
│   └── fasteners/
│
├── modules/
│   ├── hip_roll/
│   ├── hip_pitch/
│   ├── knee/
│   └── pelvis/
│
├── assemblies/
│   ├── leg_left/
│   ├── leg_right/
│   └── full_body/
│
├── export/
│   ├── step/
│   ├── stl/
│   └── drawings/
│
└── scripts/
    ├── build_all.py
    ├── export_step.py
    └── export_stl.py
```

---

# 5. Parametric Core Principle

所有几何必须依赖：

```python id="param001"
RobotConfig.py
```

示例：

```python id="cfg001"
Shaft_Dia = 8
Bearing_6803_OD = 26
Bearing_6803_ID = 17

Servo_STS3046_Width = 32
Servo_STS3046_Height = 30

Tube_OD = 12
Tube_ID = 10

Wall = 5
Clearance = 0.2
```

---

# 6. Module Generation Rule

每个机械模块必须包含：

## 必须结构

* create_geometry()
* apply_constraints()
* assemble_interfaces()
* validate_fit()

---

示例结构：

```python id="mod001"
class KneeBase:

    def __init__(self, cfg):
        self.cfg = cfg

    def create_geometry(self):
        pass

    def add_bearing_seat(self):
        pass

    def add_servo_mount(self):
        pass

    def export(self):
        pass
```

---

# 7. Assembly Rule

装配必须通过：

```text id="asm001"
Coordinate System Alignment
```

统一使用：

* Pelvis Center as origin
* Z-up convention
* Left-right symmetry mirror system

---

# 8. Symmetry System

Left / Right 模块必须通过：

```python id="sym001"
mirror(axis="Y")
```

自动生成。

禁止手工复制。

---

# 9. Build Pipeline

标准流程：

```text id="pipe001"
RobotConfig.py
    ↓
Python CAD Generator
    ↓
FreeCAD Geometry
    ↓
STEP Export
    ↓
STL Export
    ↓
Bambu Studio
    ↓
A1 Mini Print
```

---

# 10. Validation Rules

每个模块必须通过：

* Dimensional Check
* Interference Check
* Assembly Check
* Printability Check

---

# 11. Output Definition

每次 build 必须生成：

```text id="out001"
STEP
STL
Assembly Tree
Validation Report
```

---

# 12. System Constraint

禁止：

* 手工CAD最终版本
* 非参数化尺寸
* 固定几何依赖

必须：

* 全参数驱动
* 可重建
* 可版本化

---

# 13. Next Step

进入：

```text id="next001"
CAD-002-Standard-Part-Library.md
```

建立：

* 轴承库
* 舵机库
* 紧固件库
* 碳管库

为 HipPitch / Knee / Pelvis 提供统一零件系统。

---

# 14. Status

CAD System Architecture:

APPROVED

Ready for implementation phase
