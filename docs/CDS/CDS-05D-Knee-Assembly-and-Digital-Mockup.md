# Mini-Atlas V6 Alpha

# CDS-05D Knee Assembly and Digital Mockup

Version: 1.0

Status: INTEGRATION REVIEW

Document Number:

CDS-05D

Subsystem:

Knee Joint

Assembly Name:

Knee_Assembly_RevA

Parent Documents:

* CDS-05A Knee Base
* CDS-05B Knee Output
* CDS-05C Knee Torque Module
* CDS-04D HipPitch Assembly and Digital Mockup
* DR-009 Knee Architecture Review

---

# 1. Purpose

验证 Knee 子系统可装配性、可维护性、可制造性及运动性能。

通过后：

Knee Architecture Frozen，单腿机械链路形成完整 3-DOF。

---

# 2. Assembly Structure

Assembly: Knee_Assembly_RevA

Contains:

* Knee_Base
* Knee_Output
* Knee_TorqueModule
* SERVO_STS3046
* BRG_6802 ×2
* SHAFT_8MM_STD
* M3 Hardware

---

# 3. Integration Context

Installed On:

HipPitch_Output

Assembly Chain:

Pelvis → HipRoll → HipPitch → Knee → Lower Leg → Wheel Module

Verify interface compatibility: PASS REQUIRED

---

# 4. Coordinate Verification

Robot Coordinate:

+X Forward
+Y Left
+Z Up

All Components must match Robot Frame

Result: PASS REQUIRED

---

# 5. Bearing Installation Review

Components: BRG_6802 ×2

Verify:

* Seat Diameter 24.10 mm
* Installation Direction Accessible
* Removal Direction Accessible
* Bearing Gap 10 mm

Result: PASS REQUIRED

---

# 6. Shaft Installation Review

Component: SHAFT_8MM_STD

Verify:

* Insertion possible without removing servo
* No housing collision
* Clamp engagement full length

Result: PASS REQUIRED

---

# 7. Servo Installation Review

Component: SERVO_STS3046

Verify:

* 4 × M3 Accessible
* UART Connector Accessible
* Cable Exit Clearance Available
* Servo Replacement Possible

Result: PASS REQUIRED

---

# 8. Torque Module Review

Verify:

* Horn Installation Possible
* Output Shaft Clamp Accessible
* Tool Access Available
* Full Engagement Confirmed

Result: PASS REQUIRED

---

# 9. Carbon Tube Interface Review

Reference: CF_TUBE_12OD_10ID

Verify:

* Insertion Depth ≥25 mm
* Dual Clamp Operation Valid
* No Slip Path Detected

Result: PASS REQUIRED

---

# 10. Motion Verification

Required Range: 0° ~ 120°

Verify:

* No Collision
* No Bearing Interference
* No Servo Housing Contact
* HipPitch Interface OK

Result: PASS REQUIRED

---

# 11. Mechanical Stop Review

Verify:

* Stop Engages Before Servo Hard Stop
* Both Directions Protected
* Minimum Clearance 2 mm

Result: PASS REQUIRED

---

# 12. Interference Analysis

Required Tools:

* Section View
* Motion Sweep
* Collision Detection

Acceptable Result: 0 Hard Interference

Status: MANDATORY

---

# 13. Weight Review

Expected Weight:

| Component     |    Weight |
| ------------- | --------: |
| Base          | 100~150 g |
| Output        |  80~120 g |
| Torque Module |   25~45 g |
| Servo         |      80 g |
| Bearings      |      20 g |
| Hardware      |      20 g |

Target Assembly Weight: 305~435 g
Maximum: 500 g

Result: PASS REQUIRED

---

# 14. Printability Review

Verify:

* A1 Mini Compatible
* Support Strategy Valid
* No Hidden Cavities
* Bearing Seats Printable

Result: PASS REQUIRED

---

# 15. Maintenance Review

Must allow:

* Servo Replacement
* Bearing Replacement
* Shaft Replacement
* Carbon Tube Replacement

Without Destroying Printed Parts

Result: PASS REQUIRED

---

# 16. Digital Mockup Checklist

□ Bearings Install
□ Shaft Install
□ Servo Install
□ Torque Module Install
□ Carbon Tube Install
□ Motion OK
□ No Interference
□ Weight OK
□ Maintenance OK
□ HipPitch Interface OK

---

# 17. Deliverables

Required Files:

* Knee_Assembly_RevA.f3d
* Knee_Assembly_RevA.step

Required Outputs:

* Exploded View
* Section View
* Weight Report
* Interference Report
* Motion Sweep Report

---

# 18. Freeze Decision

If all checks pass:

* Status: FROZEN
* Knee Architecture: APPROVED
* Ready for Lower Leg / Wheel Module Integration

---

# 19. Exit Criteria

* Assembly Complete: PASS
* Interference Free: PASS
* Weight Within Budget: PASS
* Manufacturable: PASS
* Maintainable: PASS

Status: KNEE SUBSYSTEM FROZEN
