# Mini-Atlas V6

# CAD-002 Standard Part Library

Version: 1.0

Status: FROZEN

Document Number:

CAD-002

Subsystem:

CAD Standard Library

Parent Documents:

* CAD-001 CAD Modeling Guideline
* DR-006 Bearing and Shaft Review
* DR-007 Manufacturing Strategy Review

Applies To:

All CAD Models

All Assemblies

All Drawings

All Manufacturing Packages

---

# 1. Purpose

建立 Mini-Atlas V6 统一标准件库。

目标：

* 消除重复建模
* 保证尺寸一致
* 保证装配一致
* 保证BOM一致
* 提高CAD效率

所有装配必须引用本标准件库。

禁止自行创建重复标准件。

---

# 2. Library Directory Structure

```text
CAD/

└── Library

    ├── Bearings
    ├── Servo
    ├── Shafts
    ├── CarbonTube
    ├── Fasteners
    ├── Inserts
    ├── Electronics
    └── Reference
```

---

# 3. Bearing Library

Directory

```text
Library/Bearings
```

---

## BRG_6803

Dimensions

```text
17 × 26 × 5 mm
```

CAD File

```text
BRG_6803_RevA.step
```

Application

* Hip Roll
* Hip Pitch

Status

FROZEN

---

## BRG_6802

Dimensions

```text
15 × 24 × 5 mm
```

CAD File

```text
BRG_6802_RevA.step
```

Application

* Knee

Status

FROZEN

---

## BRG_698

Dimensions

```text
8 × 19 × 6 mm
```

CAD File

```text
BRG_698_RevA.step
```

Application

* Knee Output
* Support Bearings

Status

FROZEN

---

## BRG_688

Dimensions

```text
8 × 16 × 5 mm
```

CAD File

```text
BRG_688_RevA.step
```

Application

* Torque Modules

Status

FROZEN

---

# 4. Servo Library

Directory

```text
Library/Servo
```

---

## SERVO_STS3046

CAD File

```text
SERVO_STS3046_RevA.step
```

Properties

* Reference Geometry Included
* Output Horn Included
* Mounting Holes Included

Coordinate System

Origin

Output Shaft Center

Status

FROZEN

---

# 5. Shaft Library

Directory

```text
Library/Shafts
```

---

## SHAFT_8MM_STD

Material

SS304

Diameter

```text
8 mm
```

Tolerance

```text
h7
```

Length

Parametric

CAD File

```text
SHAFT_8MM_STD_RevA.f3d
```

Status

FROZEN

---

# 6. Carbon Tube Library

Directory

```text
Library/CarbonTube
```

---

## CF_TUBE_12OD_10ID

Dimensions

```text
OD = 12 mm

ID = 10 mm
```

Length

Parametric

CAD File

```text
CF_TUBE_12OD_10ID_RevA.f3d
```

Applications

* Upper Leg
* Lower Leg

Status

FROZEN

---

# 7. Fastener Library

Directory

```text
Library/Fasteners
```

---

## M3 Hardware Set

Approved Lengths

```text
8
10
12
16
20
mm
```

Files

```text
SCR_M3x8.step
SCR_M3x10.step
SCR_M3x12.step
SCR_M3x16.step
SCR_M3x20.step
```

Status

FROZEN

---

## M3 Nut

File

```text
NUT_M3_RevA.step
```

Status

FROZEN

---

## M3 Nylon Lock Nut

File

```text
NUT_M3_LOCK_RevA.step
```

Status

FROZEN

---

# 8. Heat Insert Library

Directory

```text
Library/Inserts
```

---

## INS_M3

Type

Heat Set Brass Insert

Hole Diameter

```text
4.6 mm
```

CAD File

```text
INS_M3_RevA.step
```

Status

FROZEN

---

# 9. Electronics Library

Directory

```text
Library/Electronics
```

---

## ESP32 DevKitC

File

```text
ESP32_DEVKITC_RevA.step
```

Purpose

Envelope Check

Status

REFERENCE ONLY

---

## ICM42688

File

```text
ICM42688_RevA.step
```

Purpose

PCB Layout

Status

REFERENCE ONLY

---

# 10. Reference Geometry Library

Directory

```text
Library/Reference
```

---

## Joint Axis Marker

File

```text
REF_JOINT_AXIS.f3d
```

Purpose

Assembly Alignment

---

## Robot Coordinate Frame

File

```text
REF_ROBOT_FRAME.f3d
```

Coordinate

```text
+X Forward

+Y Left

+Z Up
```

---

# 11. Library Quality Requirements

Every Library Part Must Include

* Origin
* Named Parameters
* Material
* Revision

---

Required

PASS

---

# 12. Revision Control

Library Parts

Only Updated By

Major Review

---

Revision Naming

```text
RevA

RevB

RevC
```

---

Status

FROZEN

---

# 13. BOM Mapping

Each Library Part Must Map To BOM

Example

```text
BRG_6803

→

BOM-01 Item #034
```

Required

YES

---

# 14. Validation Checklist

□ Correct Dimensions

□ Correct Origin

□ Correct Material

□ Correct Naming

□ STEP Export Valid

□ Assembly Compatible

□ BOM Linked

---

# 15. Freeze Summary

Bearing Library

FROZEN

---

Servo Library

FROZEN

---

Shaft Library

FROZEN

---

Carbon Tube Library

FROZEN

---

Fastener Library

FROZEN

---

Insert Library

FROZEN

---

Electronics Library

FROZEN

---

Status

APPROVED

---

Next Document

CDS-03A-HipRoll_Base-CAD-Design.md
