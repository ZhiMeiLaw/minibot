# Mini-Atlas V6 Alpha

# CDS-04A HipPitch Base CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-04A-IMP

Subsystem:

Hip Pitch Joint

CAD Part:

HipPitch_Base

Parent Documents:

* CDS-04A HipPitch Base CAD Design
* CDS-03D HipRoll Assembly and Digital Mockup
* DR-004 Hip Architecture Review
* DR-006 Bearing and Shaft Review

---

# 1. Purpose

指导 HipPitch_Base 实际 CAD 建模。

HipPitch_Base 是：

* Hip Pitch 舵机安装主体
* 双6803轴承安装主体
* Hip Roll 输出端连接主体
* 整个腿部主要受力结构

最终输出：

```text
HipPitch_Base_RevA.f3d

HipPitch_Base_RevA.step

HipPitch_Base_Print_RevA.stl
```

---

# 2. Functional Requirements

HipPitch_Base 必须实现：

```text
安装STS3046

安装双6803

安装8mm输出轴

连接HipRoll_Output

支撑整个腿部
```

---

# 3. Coordinate System

Origin

Hip Pitch Rotation Axis

---

Robot Coordinate

```text
+X Forward

+Y Left

+Z Up
```

---

Status

FROZEN

---

# 4. Design Strategy

采用：

```text
Independent Output Shaft
+
Dual Bearing Support
+
Torque Module Decoupling
```

---

禁止：

```text
Direct Servo Load Bearing
```

---

Status

FROZEN

---

# 5. Master Sketch

首先建立：

```text
HipPitch Axis

Bearing Axis

Servo Axis

HipRoll Interface Plane
```

---

禁止直接实体建模。

---

# 6. Global Parameters

```text
Bearing_OD = 26

Bearing_ID = 17

Bearing_W = 5

Shaft_Dia = 8

Wall = 5

Clearance = 0.25
```

---

No Hard-Coded Dimensions

---

# 7. Bearing Housing

Reference

```text
BRG_6803
```

---

Quantity

```text
2
```

---

Layout

```text
6803

 ||

6803
```

---

Bearing Gap

```text
10 mm
```

---

Seat Diameter

```text
26.10 mm
```

---

Status

FROZEN

---

# 8. Output Shaft Support

Reference

```text
SHAFT_8MM_STD
```

---

Bore Diameter

```text
8.15 mm
```

---

Support Length

```text
≥20 mm
```

---

Status

FROZEN

---

# 9. Servo Mount

Reference

```text
SERVO_STS3046
```

---

Mount Style

Side Mount

---

Fasteners

```text
4 × M3
```

---

Insert Type

```text
INS_M3
```

---

Status

FROZEN

---

# 10. Hip Roll Interface

Connection

```text
HipRoll_Output
```

---

Mount Pattern

```text
4 × M3
```

---

Hole Diameter

```text
3.2 mm
```

---

Boss Thickness

```text
6 mm
```

---

Status

FROZEN

---

# 11. Structural Requirements

Bearing Area

```text
5 mm Wall
```

Minimum

---

Insert Area

```text
6 mm Wall
```

Minimum

---

Main Load Path

```text
≥8 mm
```

Recommended

---

Status

FROZEN

---

# 12. Weight Target

Target

```text
100~150 g
```

---

Maximum

```text
180 g
```

---

# 13. Print Orientation

Required

```text
Bearing Axis Vertical
```

---

Reason

Maximum Bearing Accuracy

---

Status

FROZEN

---

# 14. Manufacturing Rules

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

# 15. Verification Checklist

□ Servo Fits

□ Bearings Fit

□ Shaft Fits

□ HipRoll Interface Fits

□ No Internal Supports

□ Weight <180 g

□ A1 Mini Compatible

---

# 16. Deliverables

Required Files

```text
HipPitch_Base_RevA.f3d

HipPitch_Base_RevA.step

HipPitch_Base_Print_RevA.stl
```

---

Required Drawing

```text
HipPitch_Base_DWG_RevA.pdf
```

---

# 17. Exit Criteria

Geometry Complete

PASS

---

Manufacturing Compatible

PASS

---

Assembly Compatible

PASS

---

Status

READY FOR CAD MODELING
