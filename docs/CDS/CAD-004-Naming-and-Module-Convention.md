# Mini-Atlas V6 Alpha

# CAD-004 Naming and Module Convention

Version: 1.0

Status: SYSTEM STANDARDIZATION

Document Number:

CAD-004

Subsystem:

CAD Naming & Structure Rules

---

# 1. Purpose

统一 Mini-Atlas V6 Alpha 所有 CAD 模块命名规则与结构规范，确保：

* 自动生成可预测
* 文件可追踪
* 模块可替换
* 支持批量 build

---

# 2. Core Naming Philosophy

```text id="p1"
Name = Function + Subsystem + Variant + Revision
```

---

# 3. Module Naming Standard

## Standard Format

```text id="naming01"
[Subsystem]_[Part]_[Variant]_Rev[Version]
```

---

## Examples

```text id="ex01"
HipRoll_Base_RevA
HipRoll_Output_RevA
HipRoll_TorqueModule_RevA

HipPitch_Base_RevA
HipPitch_Output_RevA
HipPitch_TorqueModule_RevA

Knee_Base_RevA
Knee_Output_RevA
Knee_TorqueModule_RevA
```

---

# 4. Assembly Naming Standard

```text id="asm01"
[System]_[AssemblyType]_Rev[Version]
```

Examples:

```text id="ex02"
SingleLeg_Assembly_RevA
DualLeg_Pelvis_Assembly_RevA
MiniAtlas_FullBody_RevA
```

---

# 5. File Naming Standard

## CAD Source File

```text id="file01"
*.FCStd
```

Example:

```text id="file02"
Knee_Base_RevA.FCStd
```

---

## STEP Export

```text id="step01"
Knee_Base_RevA.step
```

---

## STL Export

```text id="stl01"
Knee_Base_Print_RevA.stl
```

---

## Drawing

```text id="dwg01"
Knee_Base_DWG_RevA.pdf
```

---

# 6. Module Directory Structure

```text id="dir01"
modules/
    hip_roll/
        HipRoll_Base_RevA.py
        HipRoll_Output_RevA.py

    hip_pitch/
        HipPitch_Base_RevA.py
        HipPitch_Output_RevA.py

    knee/
        Knee_Base_RevA.py
        Knee_Output_RevA.py
```

---

# 7. Assembly Structure Rule

```text id="asm02"
assemblies/
    leg_left/
    leg_right/
    full_body/
```

规则：

* 左右腿必须 mirror生成
* 禁止手动复制文件
* 所有 assembly 必须可重建

---

# 8. Revision Rule

```text id="rev01"
RevA → RevB → RevC
```

规则：

* 禁止跳版本号
* 每次修改必须递增
* RevA 永远是第一冻结版本

---

# 9. Symmetry Rule

```text id="sym01"
Left = Mirror(Right)
```

规则：

* 不允许独立设计左右腿
* 必须通过 script mirror(axis="Y")

---

# 10. Module Dependency Rule

```text id="dep01"
RobotConfig.py
    ↓
Module (Hip/Knee/Pelvis)
    ↓
Assembly
    ↓
Full Robot
```

---

# 11. Build System Compatibility

所有命名必须支持：

```bash id="build01"
python build_all.py
```

输出：

* STEP
* STL
* Assembly Tree
* Report

---

# 12. Forbidden Rules

❌ 禁止：

* HipPitchFinal_v2_NEW_NEW.FCStd
* knee_final_fix2_real.fcstd
* copy_of_hip_pitch.fcstd

---

# 13. Git-Like Discipline (Recommended)

建议未来结构：

```text id="git01"
commit = Rev change

branch = experimental module

tag = frozen release (PR-001)
```

---

# 14. Next Step

进入：

```text id="next04"
CAD-005-Assembly-and-Build-System.md
```

建立：

* build_all.py
* 自动生成CAD
* 自动导出STEP/STL
* 一键生成整机模型

---

# 15. Status

Naming System:

APPROVED

System now compatible with:

```text id="status01"
FULL PARAMETRIC CAD GENERATION PIPELINE
```
