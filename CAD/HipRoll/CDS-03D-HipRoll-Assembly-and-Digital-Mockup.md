# Mini-Atlas V6 Alpha

# CDS-03D HipRoll Assembly and Digital Mockup

Version: 1.0

Status: ASSEMBLY REVIEW

Document Number:

CDS-03D

Subsystem:

Hip Roll Joint

Assembly Name:

HipRoll_Assembly_RevA

Parent Documents:

* CDS-03A HipRoll Base
* CDS-03B HipRoll Output
* CDS-03C HipRoll Torque Module
* DR-004 Hip Architecture Review
* DR-006 Bearing and Shaft Review

---

# 1. Purpose

验证 Hip Roll 总成的可装配性、可制造性和可维护性。

目标：

* 装配验证
* 干涉检查
* 运动检查
* 重量检查
* 维护检查

通过后：

Hip Roll Architecture Frozen

---

# 2. Assembly Structure

Assembly

```text
HipRoll_Assembly_RevA
```

Contains

```text
HipRoll_Base

HipRoll_Output

HipRoll_TorqueModule

SERVO_STS3046

BRG_6803 ×2

SHAFT_8MM

M3 Hardware
```

---

# 3. Coordinate System Verification

Robot Coordinate

```text
+X Forward

+Y Left

+Z Up
```

All Components

Must Match

Robot Frame

---

Status

PASS REQUIRED

---

# 4. Bearing Installation Review

Components

```text
BRG_6803 ×2
```

---

Check

Bearing Seat Diameter

```text
26.10 mm
```

---

Check

Insertion Direction

Accessible

---

Check

Removal Direction

Accessible

---

Result

PASS REQUIRED

---

# 5. Shaft Installation Review

Component

```text
SHAFT_8MM_STD
```

---

Verify

Insertion Possible

Without Servo Removal

---

Verify

No Collision

With Housing

---

Verify

Shaft Locking Method

Valid

---

Result

PASS REQUIRED

---

# 6. Servo Installation Review

Component

```text
SERVO_STS3046
```

---

Check

4 × M3 Mounting Holes

Accessible

---

Check

UART Connector

Accessible

---

Check

Cable Exit

Unobstructed

---

Check

Servo Replacement

Possible

---

Result

PASS REQUIRED

---

# 7. Torque Module Review

Verify

Horn Installation

Possible

---

Verify

Clamp Tightening

Possible

---

Verify

M3 Tool Access

Available

---

Verify

Output Shaft Engagement

Full Length

---

Result

PASS REQUIRED

---

# 8. Carbon Tube Interface Review

Tube

```text
OD = 12 mm
```

---

Verify

Insertion Depth

≥20 mm

---

Verify

Dual Clamp Function

Operational

---

Verify

No Slip Path

Detected

---

Result

PASS REQUIRED

---

# 9. Motion Verification

Hip Roll Range

```text
-30°

0°

+30°
```

---

Verify

No Collision

---

Verify

No Bearing Contact

---

Verify

No Servo Housing Contact

---

Result

PASS REQUIRED

---

# 10. Mechanical Stop Review

Verify

Stop Engagement

Before Servo Hard Stop

---

Verify

Both Directions

Protected

---

Verify

Clearance

```text
2 mm
```

Minimum

---

Result

PASS REQUIRED

---

# 11. Interference Check

Required Analysis

```text
Section View

Motion Sweep

Collision Detection
```

---

Acceptable Result

```text
0 Hard Interference
```

---

Status

MANDATORY

---

# 12. Weight Review

Expected

| Component     |   Weight |
| ------------- | -------: |
| Base          | 80~120 g |
| Output        |  50~80 g |
| Torque Module |  20~40 g |
| Servo         |     80 g |
| Bearings      |     20 g |
| Hardware      |     20 g |

---

Target Assembly Weight

```text
250~350 g
```

---

Maximum

```text
400 g
```

---

Result

PASS REQUIRED

---

# 13. Printability Review

Verify

A1 Mini Compatible

---

Verify

Support Strategy Valid

---

Verify

No Hidden Cavities

---

Verify

Bearing Seats Printable

---

Result

PASS REQUIRED

---

# 14. Maintenance Review

Must Allow

* Servo Replacement
* Bearing Replacement
* Shaft Replacement
* Carbon Tube Replacement

Without Destroying Printed Parts

---

Result

PASS REQUIRED

---

# 15. Digital Mockup Checklist

□ Bearings Install

□ Shaft Install

□ Servo Install

□ Torque Module Install

□ Carbon Tube Install

□ Motion OK

□ No Interference

□ Weight OK

□ Maintenance OK

---

# 16. Assembly Deliverables

Required Files

```text
HipRoll_Assembly_RevA.f3d

HipRoll_Assembly_RevA.step
```

---

Required Outputs

```text
Exploded View

Section View

Weight Report

Interference Report
```

---

# 17. Freeze Decision

If All Checks Pass

Status

FROZEN

---

Hip Roll Architecture

APPROVED

---

Ready For

Hip Pitch Modeling

---

# 18. Exit Criteria

Assembly Complete

PASS

---

Interference Free

PASS

---

Weight Within Budget

PASS

---

Manufacturable

PASS

---

Maintainable

PASS

---

Status

HIP ROLL SUBSYSTEM FROZEN
