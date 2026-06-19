# Mini-Atlas V6 Alpha

# CDS-03A HipRoll Base CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-03A-IMP

Subsystem:

Hip Roll Joint

CAD Part:

HipRoll_Base

Parent Documents:

* CDS-03A HipRoll Base CAD Design
* CAD-001 CAD Modeling Guideline
* CAD-002 Standard Part Library

---

# 1. Purpose

指导 HipRoll_Base 的实际 CAD 建模。

最终输出：

```text id="xqz6a9"
HipRoll_Base_RevA.f3d

HipRoll_Base_RevA.step

HipRoll_Base_Print_RevA.stl
```

---

# 2. Coordinate System

Robot Coordinate

```text id="pvtov4"
+X Forward

+Y Left

+Z Up
```

---

Part Origin

Hip Roll Axis Center

---

Status

FROZEN

---

# 3. Main Function

HipRoll_Base 用于：

```text id="mdj8qv"
固定 STS3046

固定双6803轴承

支撑输出轴

连接骨盆
```

---

# 4. Skeleton First Strategy

禁止直接拉实体。

首先建立：

```text id="fzuy4v"
Master Sketch
```

---

包含：

Hip Axis

Bearing Axis

Servo Axis

Pelvis Mount Plane

---

# 5. Global Parameters

Create Parameters

```text id="p8ej2t"
Bearing_OD = 26

Bearing_ID = 17

Bearing_W = 5

Shaft_Dia = 8

Servo_Body_W = 20

Servo_Body_H = 40

Wall = 4

Clearance = 0.25
```

---

Rule

No Hard-Coded Dimensions

---

# 6. Bearing Housing

Library

```text id="g6b3ca"
BRG_6803
```

---

Quantity

2

---

Layout

```text id="6k4n04"
6803

  ||

6803
```

---

Bearing Gap

```text id="dfi1sp"
8 mm
```

---

Seat Diameter

```text id="gv0lzk"
26.10
```

PETG Press Fit

---

# 7. Output Shaft Bore

Nominal

```text id="ghsrb0"
8 mm
```

---

CAD Bore

```text id="5lww2c"
8.15 mm
```

---

Reason

PETG Shrink Compensation

---

# 8. Servo Mount

Reference

```text id="izfjlwm"
SERVO_STS3046
```

---

Mount Style

Rear Mount

---

Fasteners

```text id="fhm9ji"
4 × M3
```

---

Insert Type

```text id="l3j1ya"
INS_M3
```

---

# 9. Pelvis Interface

Mount Pattern

```text id="pcvllg"
4 × M3
```

---

Hole Diameter

```text id="j8xmt7"
3.2 mm
```

---

Boss Thickness

```text id="p2w23s"
6 mm
```

---

# 10. Structural Walls

Minimum

```text id="4sv1a9"
4 mm
```

---

Around Bearing

```text id="72o9zl"
5 mm
```

---

Around Inserts

```text id="3i4cag"
6 mm
```

---

# 11. Print Orientation

Required

```text id="56v4kr"
Bearing Axis

Vertical
```

---

Reason

Maximum Circularity

---

Status

FROZEN

---

# 12. Expected Weight

Target

```text id="jb66qq"
80~120 g
```

---

Maximum

```text id="gdnr39"
150 g
```

---

# 13. Manufacturing Rules

Material

PETG

---

Perimeters

4

---

Infill

35%

Gyroid

---

Layer Height

0.20 mm

---

# 14. Verification Checklist

□ Servo Fits

□ Bearings Fit

□ Shaft Fits

□ Pelvis Mount Fits

□ No Internal Supports

□ A1 Mini Compatible

□ Weight <150 g

---

# 15. Deliverables

Required Files

```text id="3vy4db"
HipRoll_Base_RevA.f3d

HipRoll_Base_RevA.step

HipRoll_Base_Print_RevA.stl
```

---

Required Drawing

```text id="1mtfwl"
HipRoll_Base_DWG_RevA.pdf
```

---

# 16. Exit Criteria

Part Fully Modeled

PASS

---

Manufacturing Review

PASS

---

Assembly Review

PASS

---

Status

READY FOR CAD MODELING
