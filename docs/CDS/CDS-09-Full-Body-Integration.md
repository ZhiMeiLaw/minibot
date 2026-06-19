# Mini-Atlas V6 Alpha

# CDS-09 Full Body Integration

Version: 1.0

Status: SYSTEM INTEGRATION REVIEW

Document Number:

CDS-09

Subsystem:

Full Robot

Assembly Name:

MiniAtlas_V6_Alpha_RevA

Parent Documents:

* CDS-08 Dual Leg and Pelvis Integration
* DR-010 Leg Subsystem Review
* SR-001 System Weight Budget
* DR-012 Leg Kinematics & Torque Validation

---

# 1. Purpose

完成 Mini-Atlas V6 Alpha 全身数字装配。

目标：

* 骨盆与躯干集成
* 双腿与上身集成
* CG验证
* 线束验证
* 维护验证
* 整机重量验证

通过后：

Alpha Architecture Frozen

---

# 2. Full Robot Architecture

Structure

Head

↓

Torso

↓

Pelvis

↓

Hip Roll

↓

Hip Pitch

↓

Knee

↓

Wheel Module

---

Status

COMPLETE

---

# 3. Assembly Structure

Assembly

MiniAtlas_V6_Alpha_RevA

Contains

Pelvis

Torso

Head

Left Leg

Right Leg

Electronics

Battery

Hardware

---

# 4. Coordinate System

Origin

Pelvis Center

---

Robot Coordinate

+X Forward

+Y Left

+Z Up

---

Status

FROZEN

---

# 5. Torso Integration

Verify

Pelvis Interface Compatible

---

Verify

Load Path Continuous

---

Verify

No Structural Conflict

---

Result

PASS REQUIRED

---

# 6. Electronics Layout Review

Components

Raspberry Pi 5

Motor Bus

Power Distribution

IMU

Cooling

---

Verify

Service Access

Possible

---

Verify

Cable Routing

Clean

---

Verify

Cooling Airflow

Available

---

Result

PASS REQUIRED

---

# 7. Battery Layout Review

Preferred Position

Torso Lower Section

---

Reason

Lower CG

---

Verify

Battery Replaceable

---

Verify

Weight Balanced

---

Result

PASS REQUIRED

---

# 8. Center of Gravity Review

Target

CG Above Pelvis

---

Preferred

Slightly Below Hip Pitch Axis

---

Verify

Forward Stability

---

Verify

Backward Stability

---

Verify

Standing Stability

---

Result

PASS REQUIRED

---

# 9. Weight Budget Review

| Subsystem   | Target |
| ----------- | -----: |
| Left Leg    | 1.4 kg |
| Right Leg   | 1.4 kg |
| Pelvis      | 0.4 kg |
| Torso       | 0.8 kg |
| Electronics | 0.3 kg |
| Battery     | 0.5 kg |

---

Expected Total

4.8 kg

---

Maximum

5.5 kg

---

Result

PASS REQUIRED

---

# 10. Wiring Review

Must Route

Servo Bus

Power Bus

IMU

Future Sensors

---

Verify

No Motion Interference

---

Verify

Maintenance Access

Available

---

Result

PASS REQUIRED

---

# 11. Motion Envelope Review

Verify

Full Hip Roll Motion

---

Verify

Full Hip Pitch Motion

---

Verify

Full Knee Motion

---

Verify

No Torso Collision

---

Verify

No Cable Collision

---

Result

PASS REQUIRED

---

# 12. Fall Survival Review

Forward Fall

PASS

---

Backward Fall

PASS

---

Side Fall

PASS

---

Replaceable Damage Parts

YES

---

Result

APPROVED

---

# 13. Manufacturing Review

Printer

Bambu A1 Mini

---

Material

PETG

---

Assembly Feasible

YES

---

Result

PASS

---

# 14. Maintenance Review

Replaceable

Servo

PASS

---

Bearing

PASS

---

Shaft

PASS

---

Battery

PASS

---

Electronics

PASS

---

Result

APPROVED

---

# 15. System Risk Assessment

| Risk         | Level  |
| ------------ | ------ |
| Legs         | Medium |
| Pelvis       | Low    |
| Torso        | Low    |
| Electronics  | Medium |
| Power System | Medium |

---

Overall

MEDIUM

---

# 16. Deliverables

Required Files

MiniAtlas_V6_Alpha_RevA.f3d

MiniAtlas_V6_Alpha_RevA.step

---

Required Outputs

Exploded View

Section View

CG Report

Weight Report

Interference Report

Motion Sweep Report

---

# 17. Freeze Decision

Full Robot Architecture

APPROVED

---

Status

FROZEN

---

Ready For

Alpha Prototype Release

---

# 18. Exit Criteria

Full Integration Complete

PASS

---

Weight Budget Valid

PASS

---

CG Valid

PASS

---

Manufacturing Valid

PASS

---

Maintenance Valid

PASS

---

Status

FULL BODY INTEGRATION APPROVED
