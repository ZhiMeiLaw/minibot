# Mini-Atlas V6 Alpha

# CDS-03C HipRoll Torque Transfer Module CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-03C-IMP

Subsystem:

Hip Roll Joint

CAD Part:

HipRoll_TorqueModule

Parent Documents:

* CDS-03C HipRoll Torque Transfer Module CAD Design
* CDS-03A HipRoll Base CAD Implementation
* CDS-03B HipRoll Output CAD Implementation
* DR-003 Joint Architecture Review

---

# 1. Purpose

指导 HipRoll Torque Transfer Module 实际建模。

本零件负责：

* STS3046输出轴扭矩传递
* 输出轴夹紧
* 舵机与关节解耦
* 防止弯矩进入舵机

最终输出：

```text id="6vbpk8"
HipRoll_TorqueModule_RevA.f3d

HipRoll_TorqueModule_RevA.step

HipRoll_TorqueModule_Print_RevA.stl
```

---

# 2. Functional Principle

Load Path

```text id="6ygxsh"
Servo Torque

↓

Torque Module

↓

Output Shaft

↓

Output Arm

↓

Carbon Tube
```

禁止：

```text id="r49z0v"
Leg Load

↓

Servo Output Shaft
```

---

# 3. Coordinate System

Origin

Servo Output Axis

---

Robot Frame

```text id="d6z2hj"
+X Forward

+Y Left

+Z Up
```

---

Status

FROZEN

---

# 4. Architecture

Approved

```text id="2m2qyr"
Dual Clamp
```

Layout

```text id="qh56g6"
Servo Horn

 ||

Clamp Body

 ||

Output Shaft Clamp
```

---

Status

FROZEN

---

# 5. Global Parameters

```text id="qv9zpr"
Shaft_Dia = 8

Clamp_Bolt = M3

Wall = 5

Clearance = 0.20

Insert_Dia = 4.6
```

---

No Hard-Coded Dimensions

---

# 6. Servo Interface

Reference

```text id="c1n7qq"
SERVO_STS3046
```

---

Mount Style

Horn Clamp

---

Fasteners

```text id="klx7r6"
2 × M3
```

---

Status

FROZEN

---

# 7. Output Shaft Interface

Reference

```text id="p3djsi"
SHAFT_8MM_STD
```

---

Clamp Bore

```text id="mfw36o"
8.15 mm
```

---

Clamp Length

```text id="x2ydwz"
12 mm
```

---

Fasteners

```text id="bpn7y9"
2 × M3
```

---

Status

FROZEN

---

# 8. Clamp Design Rules

Split Clamp

Required

YES

---

Gap Width

```text id="6w6i70"
2 mm
```

---

Minimum Wall

```text id="f78s9x"
5 mm
```

---

Status

FROZEN

---

# 9. Insert Design

Insert Type

```text id="x4y2mi"
INS_M3
```

---

Hole Diameter

```text id="6a7kzz"
4.6 mm
```

---

Boss Diameter

```text id="2d4fmi"
6 mm
```

---

Boss Height

```text id="xkpb7m"
8 mm
```

---

Status

FROZEN

---

# 10. Mechanical Safety

Must Withstand

```text id="3g9wlt"
4.5 Nm
```

Continuous Torque

---

Factor of Safety

```text id="fj0s1o"
2.0
```

Target

---

Design Torque

```text id="qsk7mq"
9 Nm
```

---

Status

FROZEN

---

# 11. Structural Requirements

Minimum Wall

```text id="4i6nq0"
5 mm
```

---

Around Inserts

```text id="8v9h3j"
6 mm
```

---

Around Clamp

```text id="j7r4d2"
6 mm
```

---

# 12. Weight Target

Target

```text id="p9v9ho"
20~40 g
```

---

Maximum

```text id="8gx4zz"
50 g
```

---

# 13. Print Orientation

Preferred

```text id="w4f7qp"
Clamp Split Vertical
```

---

Reason

Maximum Clamp Strength

Best Layer Direction

---

Status

FROZEN

---

# 14. Manufacturing Rules

Material

PETG

---

Perimeters

5

---

Infill

50%

Gyroid

---

Layer Height

0.20 mm

---

Support

NONE

Preferred

---

# 15. Verification Checklist

□ Servo Horn Fits

□ Shaft Fits

□ Clamp Operates

□ Inserts Install

□ No Cracks

□ Weight <50 g

□ A1 Mini Compatible

---

# 16. Deliverables

Required Files

```text id="cki4nr"
HipRoll_TorqueModule_RevA.f3d

HipRoll_TorqueModule_RevA.step

HipRoll_TorqueModule_Print_RevA.stl
```

---

Required Drawing

```text id="4fwhps"
HipRoll_TorqueModule_DWG_RevA.pdf
```

---

# 17. Exit Criteria

Geometry Complete

PASS

---

Assembly Compatible

PASS

---

Torque Verification Complete

PASS

---

Manufacturing Compatible

PASS

---

Status

READY FOR CAD MODELING
