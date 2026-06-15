# Mini-Atlas V6 Alpha

# CAD-002 Standard Part Library

Version: 1.0

Status: CORE INFRASTRUCTURE

Document Number:

CAD-002

Subsystem:

Standard Components System

---

# 1. Purpose

建立 Mini-Atlas V6 的标准零件库（Standard Part Library），用于：

* 统一所有机械尺寸基准
* 消除跨模块尺寸冲突
* 支持参数化CAD生成
* 确保可维护性与可替换性

---

# 2. Library Philosophy

所有结构必须基于：

```text id="libp1"
Standard Part = Single Source Geometry Definition
```

禁止：

* 每个模块自定义轴承尺寸
* 每个模块自定义螺丝孔位
* 非标准碳管规格

---

# 3. Bearing Library

## BRG_6803

6803 bearing

Dimensions:

```text id="brg01"
OD = 26 mm
ID = 17 mm
Width = 5 mm
```

Usage:

* Hip Roll
* Hip Pitch

---

## BRG_6802

6802 bearing

Dimensions:

```text id="brg02"
OD = 24 mm
ID = 15 mm
Width = 5 mm
```

Usage:

* Knee Joint

---

# 4. Servo Library

## SERVO_STS3046

STS3046 servo

Key Dimensions:

```text id="srv01"
Width = 32 mm
Height = 30 mm
Thickness = 12 mm
Shaft = 8 mm spline
```

Mount Pattern:

* 4 × M3

Usage:

* Hip Roll
* Hip Pitch
* Knee

---

# 5. Shaft Library

## SHAFT_8MM_STD

8mm steel shaft

Dimensions:

```text id="shf01"
Diameter = 8 mm
Tolerance = h7
Material = SS304
```

Usage:

* All joints unified shaft system

---

# 6. Carbon Tube Library

## CF_TUBE_12OD_10ID

carbon fiber tube 12mm

Dimensions:

```text id="tub01"
OD = 12 mm
ID = 10 mm
Wall = 1 mm
```

Usage:

* Upper / Lower Leg Structure

---

# 7. Fastener Library

## M3 Standard

M3 screw

Specification:

```text id="fas01"
Diameter = 3 mm
Pitch = 0.5 mm
Head = Socket Cap
```

Insert Type:

* M3 Heat-set Insert (INS_M3)

---

# 8. Insert Library

## INS_M3

Specification:

```text id="ins01"
Outer Diameter = 4.6 mm
Length = 5 mm
Boss Diameter = 6 mm
```

Usage:

* All structural joints

---

# 9. Clearance Standards

Global Rules:

```text id="clr01"
Sliding Fit Clearance = 0.20 mm
Press Fit Clearance = 0.00 ~ -0.05 mm
Bearing Seat Clearance = +0.05 mm
```

---

# 10. Wall Thickness Standards

Minimums:

```text id="wall01"
Structural Wall = 5 mm
Bearing Housing = 6 mm
Load Bearing Zone = 8 mm
```

---

# 11. Material Standards

Primary Material:

PETG

Properties:

* Toughness > PLA
* Flexibility moderate
* Good layer adhesion

---

# 12. Compatibility Rules

All modules must:

* Use only library-defined parts
* Never redefine bearing dimensions
* Never modify servo mounting pattern
* Always use global clearance rules

---

# 13. Version Control Rule

If any standard part changes:

```text id="vc01"
ALL modules must be regenerated
```

Including:

* Hip Roll
* Hip Pitch
* Knee
* Pelvis

---

# 14. Next Step

进入：

```text id="next02"
CAD-003-Robot-Parameter-System.md
```

建立：

* RobotConfig.py
* 全局参数源
* 自动驱动CAD生成

---

# 15. Status

Standard Part Library:

APPROVED

Ready for Parametric System Build
