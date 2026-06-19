# Mini-Atlas V6 Alpha

# CDS-08 Dual Leg and Pelvis Integration

Version: 1.0

Status: INTEGRATION REVIEW

Document Number:

CDS-08

Subsystem:

Lower Body

Assembly Name:

DualLeg_Pelvis_Assembly_RevA

Parent Documents:

* CDS-03D HipRoll Assembly
* CDS-04D HipPitch Assembly
* CDS-05D Knee Assembly
* DR-010 Leg Subsystem Review

---

# 1. Purpose

完成双腿与骨盆的第一次数字装配（Digital Mockup）。

目标：

* 骨盆与左右腿对齐
* 双腿长度一致
* 下肢重量分布均衡
* 髋关节同步
* 确认线缆/通道布置
* 骨盆、腿部打印件可装配
* 骨盆维护可行

---

# 2. Assembly Structure

Assembly: DualLeg_Pelvis_Assembly_RevA

Contains:

* Pelvis_RevA
* Left Leg Assembly (Hip Roll → Hip Pitch → Knee)
* Right Leg Assembly (Hip Roll → Hip Pitch → Knee)
* SERVO_STS3046 ×6
* Bearings ×12
* SHAFT_8MM ×6
* M3 Hardware

---

# 3. Coordinate System

Origin: Pelvis Center

+X Forward

+Y Left

+Z Up

Status: FROZEN

---

# 4. Pelvis Interface

* Hip Roll Mounting Holes symmetric
* Hip Pitch Output Plane aligned
* Cable / Tube Passages confirmed

Status: FROZEN

---

# 5. Leg Alignment

* Left / Right Legs equal length
* Hip Roll / Hip Pitch / Knee axes parallel
* Ground Clearance verified
* Foot / Wheel interface aligned

Result: PASS REQUIRED

---

# 6. Motion Range Verification

* Hip Roll ±30°
* Hip Pitch -45°~+90°
* Knee 0°~120°

Check for collision during full motion sweep:

* Left leg vs Right leg
* Left leg vs Pelvis
* Right leg vs Pelvis

Result: PASS REQUIRED

---

# 7. Weight and Balance Review

* Total Lower Body Weight ~2.8~3.0 kg
* Pelvis Center of Gravity near center
* Leg distribution symmetrical

Result: PASS REQUIRED

---

# 8. Maintenance Review

* Servo replacement possible without拆解骨盆
* Bearings accessible
* Shaft可拆卸
* Tube可更换

Result: PASS REQUIRED

---

# 9. Interference Analysis

* Digital Mockup sweep
* Section View
* Collision Detection

Result: 0 Hard Interference

Status: MANDATORY

---

# 10. Printability Review

* Bambu A1 Mini compatible
* No hidden cavities
* Support strategy valid
* Bearing / Tube seats printable

Result: PASS REQUIRED

---

# 11. Deliverables

Required Files:

DualLeg_Pelvis_Assembly_RevA.f3d

DualLeg_Pelvis_Assembly_RevA.step

Required Outputs:

* Exploded View
* Section View
* Motion Sweep Report
* Weight Report
* Interference Report

---

# 12. Freeze Decision

* Dual Leg Assembly: FROZEN
* Pelvis: FROZEN
* Ready for Full Body Integration

---

# 13. Exit Criteria

* Assembly Complete: PASS
* Interference Free: PASS
* Weight Distribution Valid: PASS
* Manufacturable: PASS
* Maintainable: PASS

Status: DUAL LEG & PELVIS SUBSYSTEM FROZEN
