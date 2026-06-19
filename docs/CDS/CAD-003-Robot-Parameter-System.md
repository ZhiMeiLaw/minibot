# Mini-Atlas V6 Alpha

# CAD-003 Robot Parameter System

Version: 1.0

Status: CORE SYSTEM FOUNDATION

Document Number:

CAD-003

Subsystem:

Parametric Control System

---

# 1. Purpose

建立 Mini-Atlas V6 Alpha 的唯一参数源系统（Single Source of Truth）。

所有 CAD 模型必须完全由该参数驱动生成。

---

# 2. Core Principle

```text id="core01"
RobotConfig.py = SINGLE SOURCE OF TRUTH
```

禁止：

* CAD内部手工修改关键尺寸
* 模块内定义独立轴承尺寸
* 非参数化建模

---

# 3. System Architecture

```text id="arch01"
RobotConfig.py
        ↓
Module Parameters
        ↓
CAD Generator (FreeCAD Python)
        ↓
Geometry
        ↓
STEP / STL Export
```

---

# 4. RobotConfig.py (Core Definition)

```python id="cfgcore01"
# Mini-Atlas V6 Alpha - Global Parameters

# ========== Structural ==========
STRUCTURE_WALL = 5.0
LOAD_BEARING_WALL = 8.0

# ========== Clearance ==========
CLEARANCE_SLIDE = 0.20
CLEARANCE_BEARING = 0.05

# ========== Shaft System ==========
SHAFT_DIA = 8.0
SHAFT_MATERIAL = "SS304"

# ========== Bearings ==========
BEARING_6803_OD = 26.0
BEARING_6803_ID = 17.0
BEARING_6803_W  = 5.0

BEARING_6802_OD = 24.0
BEARING_6802_ID = 15.0
BEARING_6802_W  = 5.0

# ========== Servo ==========
SERVO_STS3046_WIDTH  = 32.0
SERVO_STS3046_HEIGHT = 30.0
SERVO_STS3046_THICK  = 12.0
SERVO_MOUNT_M3_SPACING = 4

# ========== Carbon Tube ==========
TUBE_OD = 12.0
TUBE_ID = 10.0

# ========== Inserts ==========
INSERT_M3_OD = 4.6
INSERT_M3_LEN = 5.0

# ========== Mechanical Limits ==========
HIP_ROLL_RANGE  = 30
HIP_PITCH_RANGE = 90
KNEE_RANGE      = 120

# ========== Global Scaling ==========
LEG_SYMMETRY = True
MIRROR_AXIS = "Y"
```

---

# 5. Parameter Hierarchy

```text id="hier01"
Global (RobotConfig)
    ↓
Module Override (only geometry offsets)
    ↓
Local Sketch Constraints
```

---

# 6. Forbidden Rules

❌ 禁止：

* 在CAD中写死尺寸
* 在模块中重复定义轴承参数
* 使用非RobotConfig来源数据

---

# 7. Module Parameter Injection

所有模块必须使用：

```python id="inj01"
from RobotConfig import *
```

示例：

```python id="inj02"
bearing_od = BEARING_6803_OD
shaft_dia = SHAFT_DIA
wall = STRUCTURE_WALL
```

---

# 8. Symmetry System

```text id="sym01"
Left Leg = Right Leg (mirror Y axis)
```

规则：

* 不允许单独设计左右腿
* 必须通过 mirror() 自动生成

---

# 9. Module Dependency Rule

所有CAD模块依赖关系：

```text id="dep01"
RobotConfig.py
    ↓
HipRoll / HipPitch / Knee
    ↓
Pelvis / Leg Assembly
    ↓
Full Body
```

---

# 10. Regeneration Rule

任何参数修改：

```text id="regen01"
必须触发全系统重建
```

影响范围：

* Hip Roll
* Hip Pitch
* Knee
* Pelvis
* Full Assembly

---

# 11. Build System Definition

未来标准构建方式：

```bash id="build01"
python build_all.py
```

输出：

* STEP files
* STL files
* Assembly tree
* Validation report

---

# 12. Validation Layer

每次生成必须验证：

* Dimension consistency
* Bearing fit
* Servo fit
* Tube fit
* Symmetry correctness

---

# 13. Next Step

进入：

```text id="next03"
CAD-004-Naming-and-Module-Convention.md
```

建立：

* HipPitch_Base 命名规则
* Knee_Module 标准
* 自动生成文件结构规范

---

# 14. Status

Robot Parameter System:

APPROVED

System is now:

```text id="status01"
READY FOR CAD GENERATION ENGINE
```
