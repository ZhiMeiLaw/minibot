# Mini-Atlas V6 Alpha

# CDS-04D HipPitch Assembly and Digital Mockup

Version: 1.0

Status: INTEGRATION REVIEW

Document Number:

CDS-04D

Subsystem:

Hip Pitch Joint

Assembly Name:

HipPitch_Assembly_RevA

Parent Documents:

* CDS-04A HipPitch Base
* CDS-04B HipPitch Output
* CDS-04C HipPitch Torque Module
* CDS-03D HipRoll Assembly and Digital Mockup
* DR-004 Hip Architecture Review

---

# 1. Purpose

验证 Hip Pitch 子系统可装配性、可维护性、可制造性及运动性能。

通过后：

Hip Pitch Architecture Frozen

---

# 2. Assembly Structure

Assembly

HipPitch_Assembly_RevA

Contains

HipPitch_Base

HipPitch_Output

HipPitch_TorqueModule

SERVO_STS3046

BRG_6803 ×2

SHAFT_8MM_STD

M3 Hardware

---

# 3. Integration Context

Installed On

HipRoll_Output

---

Assembly Chain

Pelvis

↓

HipRoll

↓

HipPitch

↓

Upper Leg

---

Verify Interface Compatibility

PASS REQUIRED

---

# 4. Coordinate Verification

Robot Coordinate

+X Forward

+Y Left

+Z Up

---

All Components

Must Match

Robot Frame

---

Result

PASS REQUIRED

---

# 5. Bearing Installation Review

Components

BRG_6803 ×2

---

Verify

Seat Diameter

26.10 mm

---

Verify

Installation Direction

Accessible

---

Verify

Removal Direction

Accessible

---

Verify

Bearing Gap

10 mm

---

Result

PASS REQUIRED

---

# 6. Shaft Installation Review

Component

SHAFT_8MM_STD

---

Verify

Insertion Possible

Without Servo Removal

---

Verify

No Housing Collision

---

Verify

Clamp Engagement

Full Length

---

Result

PASS REQUIRED

---

# 7. Servo Installation Review

Component

SERVO_STS3046

---

Verify

4 × M3 Accessible

---

Verify

UART Connector Accessible

---

Verify

Cable Exit Clearance

Available

---

Verify

Servo Replacement

Possible

---

Result

PASS REQUIRED

---

# 8. Torque Module Review

Verify

Horn Installation

Possible

---

Verify

Output Shaft Clamp

Accessible

---

Verify

Tool Access

Available

---

Verify

Full Engagement

Confirmed

---

Result

PASS REQUIRED

---

# 9. Carbon Tube Interface Review

Reference

CF_TUBE_12OD_10ID

---

Verify

Insertion Depth ≥25 mm

---

Verify

Dual Clamp Operation

Valid

---

Verify

No Slip Path

Detected

---

Result

PASS REQUIRED

---

# 10. Motion Verification

Required Range

-45°

0°

+90°

---

Verify

No Collision

---

Verify

No Bearing Interference

---

Verify

No Servo Housing Contact

---

Verify

No HipRoll Collision

---

Result

PASS REQUIRED

---

# 11. Mechanical Stop Review

Verify

Stop Engages

Before Servo Hard Stop

---

Verify

Both Directions

Protected

---

Verify

Minimum Clearance

2 mm

---

Result

PASS REQUIRED

---

# 12. Interference Analysis

Required Tools

Section View

Motion Sweep

Collision Detection

---

Acceptable Result

0 Hard Interference

---

Status

MANDATORY

---

# 13. Weight Review

Expected Weight

| Component     |    Weight |
| ------------- | --------: |
| Base          | 100~150 g |
| Output        |  80~120 g |
| Torque Module |   25~45 g |
| Servo         |      80 g |
| Bearings      |      20 g |
| Hardware      |      20 g |

---

Target Assembly Weight

305~435 g

---

Maximum

500 g

---

Result

PASS REQUIRED

---

# 14. Printability Review

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

# 15. Maintenance Review

Must Allow

Servo Replacement

Bearing Replacement

Shaft Replacement

Carbon Tube Replacement

---

Without Destroying Printed Parts

---

Result

PASS REQUIRED

---

# 16. Hip Joint Integration Review

Assembly Chain

HipRoll_Output

↓

HipPitch_Base

↓

HipPitch_Output

---

Verify

Mount Pattern Compatible

---

Verify

Motion Coupling Correct

---

Verify

No Structural Conflict

---

Result

PASS REQUIRED

---

# 17. Digital Mockup Checklist

□ Bearings Install

□ Shaft Install

□ Servo Install

□ Torque Module Install

□ Carbon Tube Install

□ Motion OK

□ No Interference

□ Weight OK

□ Maintenance OK

□ HipRoll Interface OK

---

# 18. Deliverables

Required Files

HipPitch_Assembly_RevA.f3d

HipPitch_Assembly_RevA.step

---

Required Outputs

Exploded View

Section View

Weight Report

Interference Report

Motion Sweep Report

---

# 19. Freeze Decision

If All Checks Pass

Status

FROZEN

---

Hip Pitch Architecture

APPROVED

---

Ready For

Knee Joint Modeling

---

# 20. Exit Criteria

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

HIP PITCH SUBSYSTEM FROZEN
