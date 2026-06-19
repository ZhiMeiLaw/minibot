# Mini-Atlas V6

# CAD-001 CAD Modeling Guideline

Version: 1.0

Status: FROZEN

Document Number:

CAD-001

Subsystem:

CAD Standards

Applies To:

All CAD Models

All Assemblies

All STEP Files

All STL Files

---

# 1. Purpose

定义 Mini-Atlas V6 全项目 CAD 规范。

目标：

* 保持一致性
* 便于协作
* 便于版本管理
* 便于制造
* 便于维护

---

# 2. CAD Platform

Primary CAD

Fusion 360

---

Supported

FreeCAD

Onshape

---

Exchange Format

STEP AP214

---

Status

FROZEN

---

# 3. Project Folder Structure

```text
CAD/

├── Library
│
├── HipRoll
│
├── HipPitch
│
├── Knee
│
├── Wheel
│
├── Pelvis
│
├── LegAssembly
│
└── FullBody
```

---

# 4. File Naming Rules

Part

```text
Subsystem_PartName_RevA.f3d
```

Example

```text
HipRoll_Base_RevA.f3d

HipRoll_Output_RevA.f3d
```

---

Assembly

```text
Subsystem_Assembly_RevA.f3d
```

Example

```text
HipRoll_Assembly_RevA.f3d
```

---

# 5. Revision Rules

Major

```text
RevA
RevB
RevC
```

Geometry Change

---

Minor

```text
A01
A02
A03
```

Non-Geometry Change

---

Rule

Never Use

```text
final
final2
latest
new
```

---

# 6. Coordinate System Standard

Robot Coordinate System

```text
+X Forward

+Y Left

+Z Up
```

---

All Assemblies

Must Follow

Same Coordinate System

---

Status

FROZEN

---

# 7. Origin Placement

Rule

Place Origin At

Joint Center

---

Hip Roll

Origin = Hip Roll Axis

---

Hip Pitch

Origin = Hip Pitch Axis

---

Knee

Origin = Knee Axis

---

Reason

Simplifies Kinematics

---

# 8. Units

Unit

Millimeter

---

Angle

Degree

---

Mass

Gram

---

Status

FROZEN

---

# 9. Parameter Naming

Examples

```text
Bearing_OD

Bearing_ID

Shaft_Dia

Tube_OD

Tube_ID

Wall_Thickness
```

---

Avoid

```text
d1

d2

test

value1
```

---

# 10. Standard Parameters

```text
Shaft_Dia = 8

Tube_OD = 12

Tube_ID = 10

M3_Clearance = 3.2

M3_Insert = 4.6
```

---

Status

FROZEN

---

# 11. Material Naming

PETG

```text
MAT_PETG
```

---

Carbon Tube

```text
MAT_CF_TUBE
```

---

Steel Shaft

```text
MAT_SS304
```

---

# 12. Bearing Naming

6803

```text
BRG_6803
```

---

6802

```text
BRG_6802
```

---

698

```text
BRG_698
```

---

688

```text
BRG_688
```

---

# 13. Hardware Naming

M3x8

```text
SCR_M3x8
```

---

M3x12

```text
SCR_M3x12
```

---

Insert

```text
INS_M3
```

---

# 14. Assembly Rules

Rule 1

One File = One Part

---

Rule 2

No Derived Geometry

Without Documentation

---

Rule 3

All Bearings

Reference Library Model

---

Rule 4

No Duplicate Components

---

# 15. STEP Export Rules

Export Format

STEP AP214

---

Naming

```text
HipRoll_Base_RevA.step
```

---

Status

FROZEN

---

# 16. STL Export Rules

Naming

```text
HipRoll_Base_Print_RevA.stl
```

---

Unit

Millimeter

---

Binary STL

---

# 17. Print Orientation Rule

Every Printable Part Must Have

```text
Preferred_Print_Orientation
```

Documented

---

# 18. Manufacturing Metadata

Each Part Must Record

* Weight
* Print Time
* Material
* Infill
* Support Requirement

---

# 19. Release Package

Each Frozen Part Must Include

```text
F3D

STEP

STL

Drawing PDF
```

---

# 20. Freeze Summary

Naming Convention

FROZEN

---

Coordinate System

FROZEN

---

Revision System

FROZEN

---

Export Rules

FROZEN

---

Status

APPROVED

---

Next Document

CAD-002-Standard-Part-Library.md
