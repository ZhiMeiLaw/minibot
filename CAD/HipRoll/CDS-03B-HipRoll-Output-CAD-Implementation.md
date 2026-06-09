# Mini-Atlas V6 Alpha

# CDS-03B HipRoll Output CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-03B-IMP

Subsystem:

Hip Roll Joint

CAD Part:

HipRoll_Output

Parent Documents:

* CDS-03B HipRoll Output CAD Design
* CDS-03A HipRoll Base CAD Implementation
* CAD-001 CAD Modeling Guideline
* CAD-002 Standard Part Library

---

# 1. Purpose

指导 HipRoll_Output 的实际 CAD 建模。

最终输出：

```text id="jx5tkn"
HipRoll_Output_RevA.f3d

HipRoll_Output_RevA.step

HipRoll_Output_Print_RevA.stl
```

---

# 2. Function

HipRoll_Output 用于：

```text id="d67p8m"
连接输出轴

安装Torque Module

夹持碳管

输出Hip Roll运动
```

---

# 3. Coordinate System

Origin

Hip Roll Rotation Axis

---

Robot Frame

```text id="jlwm7u"
+X Forward

+Y Left

+Z Up
```

---

Status

FROZEN

---

# 4. Skeleton Strategy

First Create

```text id="zhj2uw"
Master Sketch
```

Containing

* Rotation Axis
* Shaft Bore Axis
* Carbon Tube Axis
* Clamp Plane

---

# 5. Global Parameters

```text id="tqf4jt"
Shaft_Dia = 8

Tube_OD = 12

Tube_ID = 10

Clamp_Length = 20

Wall = 5

Clearance = 0.20
```

---

Rule

No Hard-Coded Dimensions

---

# 6. Output Hub

Function

Transmit Torque

---

Bore

```text id="7pvfzw"
8.15 mm
```

---

Hub Diameter

```text id="8whrha"
24 mm
```

---

Hub Thickness

```text id="vjlwmm"
12 mm
```

---

Status

FROZEN

---

# 7. Carbon Tube Clamp

Tube

```text id="z3l6tu"
12 mm OD
```

---

Clamp Type

Split Clamp

---

Fasteners

```text id="z7aqxy"
2 × M3
```

---

Clamp Length

```text id="0mzjlwm"
20 mm
```

---

Status

FROZEN

---

# 8. Torque Module Interface

Connection

```text id="vzwyhh"
Dual Clamp Interface
```

---

Mounting Holes

```text id="1zh7o7"
2 × M3
```

---

Insert Type

```text id="2vtnx6"
INS_M3
```

---

# 9. Mechanical Stop Interface

Required

YES

---

Travel

```text id="gkm7hh"
±30°
```

---

Clearance

```text id="xh7u8w"
2 mm
```

---

Status

FROZEN

---

# 10. Structural Requirements

Minimum Wall

```text id="j8dnrj"
5 mm
```

---

Clamp Wall

```text id="icjlwm"
6 mm
```

---

Hub Wall

```text id="5bbq91"
5 mm
```

---

# 11. Weight Target

Target

```text id="9bmjlwm"
50~80 g
```

---

Maximum

```text id="pbvjlwm"
100 g
```

---

# 12. Print Orientation

Preferred

```text id="jlwmd2"
Hub Down
```

---

Reason

Maximum Strength

Best Bore Accuracy

---

Status

FROZEN

---

# 13. Manufacturing Rules

Material

PETG

---

Perimeters

5

---

Infill

40%

Gyroid

---

Layer Height

0.20 mm

---

# 14. Verification Checklist

□ Shaft Fits

□ Carbon Tube Fits

□ Clamp Operates

□ Torque Module Mount Fits

□ Mechanical Stop Works

□ Weight <100 g

□ A1 Mini Compatible

---

# 15. Deliverables

Required Files

```text id="jlwmk1"
HipRoll_Output_RevA.f3d

HipRoll_Output_RevA.step

HipRoll_Output_Print_RevA.stl
```

---

Required Drawing

```text id="4jlwm4"
HipRoll_Output_DWG_RevA.pdf
```

---

# 16. Exit Criteria

Geometry Complete

PASS

---

Assembly Compatible

PASS

---

Manufacturing Compatible

PASS

---

Status

READY FOR CAD MODELING
