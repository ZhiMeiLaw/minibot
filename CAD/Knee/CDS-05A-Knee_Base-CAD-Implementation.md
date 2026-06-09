# Mini-Atlas V6 Alpha

# CDS-05A Knee Base CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-05A-IMP

Subsystem:

Knee Joint

CAD Part:

Knee_Base

Parent Documents:

* DR-009 Knee Architecture Review
* CDS-04D HipPitch Assembly and Digital Mockup
* CAD-001 CAD Modeling Guideline
* CAD-002 Standard Part Library

---

# 1. Purpose

指导 Knee_Base 实际 CAD 建模。

Knee_Base 负责：

* 固定 STS3046 输出轴
* 支撑双 6802 轴承
* 连接 Upper Leg Tube
* 连接 Knee Output

最终输出：

```text id="knee-files"
Knee_Base_RevA.f3d
Knee_Base_RevA.step
Knee_Base_Print_RevA.stl
```

---

# 2. Functional Requirements

* 承受整条腿重量和步态动态载荷
* 安装 STS3046 舵机
* 安装 6802 双轴承
* 连接 HipPitch_Output
* 维护可拆卸性

---

# 3. Coordinate System

Origin

Knee Rotation Axis

Robot Frame

+X Forward

+Y Left

+Z Up

Status

FROZEN

---

# 4. Master Sketch

必须先建立：

* Knee Axis
* Bearing Axis
* Servo Axis
* Upper Leg Tube Mount Plane
* HipPitch Interface Plane

禁止直接拉伸实体。

---

# 5. Global Parameters

```text
Shaft_Dia = 8 mm
Bearing_OD = 24 mm
Bearing_ID = 15 mm
Bearing_W = 5 mm
Wall = 5 mm
Clearance = 0.25 mm
Tube_OD = 12 mm
Tube_ID = 10 mm
Clamp_Length = 25 mm
```

---

# 6. Bearing Housing

Reference: BRG_6802 ×2

Layout: Parallel

Gap: 10 mm

Seat Diameter: 24.10 mm

Status: FROZEN

---

# 7. Output Shaft Bore

Reference: SHAFT_8MM_STD

Bore Diameter: 8.15 mm (PETG Compensation)

Clamp Length: 15 mm

Status: FROZEN

---

# 8. Servo Mount

Reference: SERVO_STS3046

Mount Style: Side Mount

Fasteners: 4 × M3

Insert Type: INS_M3

Status: FROZEN

---

# 9. Upper Leg Interface

Reference: HipPitch_Output

Mount Pattern: 4 × M3

Hole Diameter: 3.2 mm

Boss Thickness: 6 mm

Status: FROZEN

---

# 10. Lower Leg Interface

Reference: Knee_Output (future)

Tube: CF_TUBE_12OD_10ID

Insertion Depth: ≥25 mm

Clamp Type: Dual Split Clamp

Status: FROZEN

---

# 11. Structural Requirements

Minimum Wall: 5 mm

Bearing Area: 6 mm

Clamp Area: 6 mm

Main Load Path: ≥8 mm

Status: FROZEN

---

# 12. Motion Range

Flexion: 0° ~ 120°

Extension: 0° ~ 0°

Status: FROZEN

---

# 13. Mechanical Stop

Required: YES

Stop Margin: 5° before servo limit

Status: FROZEN

---

# 14. Weight Target

Target: 100~150 g

Maximum: 180 g

Status: FROZEN

---

# 15. Print Orientation

Preferred: Bearing Axis Vertical

Reason: Maximum Bearing Accuracy

Status: FROZEN

---

# 16. Manufacturing Rules

Material: PETG

Perimeters: 4

Infill: 35% Gyroid

Layer Height: 0.20 mm

Support: None Preferred

Status: FROZEN

---

# 17. Verification Checklist

□ Servo Fits

□ Bearings Fit

□ Shaft Fits

□ Upper Leg Interface Fits

□ No Internal Supports

□ Weight <180 g

□ A1 Mini Compatible

---

# 18. Deliverables

Required Files:

Knee_Base_RevA.f3d

Knee_Base_RevA.step

Knee_Base_Print_RevA.stl

Required Drawing:

Knee_Base_DWG_RevA.pdf

---

# 19. Exit Criteria

Geometry Complete: PASS

Assembly Compatible: PASS

Manufacturing Compatible: PASS

Status: READY FOR CAD MODELING
