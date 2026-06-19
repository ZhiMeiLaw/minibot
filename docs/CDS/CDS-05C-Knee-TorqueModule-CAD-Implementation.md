# Mini-Atlas V6 Alpha

# CDS-05C Knee Torque Module CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-05C-IMP

Subsystem:

Knee Joint

CAD Part:

Knee_TorqueModule

Parent Documents:

* CDS-05A Knee Base CAD Implementation
* CDS-05B Knee Output CAD Implementation
* DR-009 Knee Architecture Review
* DR-012 Leg Kinematics & Torque Validation

---

# 1. Purpose

指导 Knee_TorqueModule 实际 CAD 建模。

本零件负责：

* STS3046 输出扭矩传递
* 夹紧输出轴
* 舵机与结构解耦
* 确保承载能力

最终输出：

Knee_TorqueModule_RevA.f3d

Knee_TorqueModule_RevA.step

Knee_TorqueModule_Print_RevA.stl

---

# 2. Functional Principle

Load Path

Servo Torque

↓

Torque Module

↓

Output Shaft

↓

Knee Output

↓

Lower Leg

---

禁止：

Leg Load

↓

Servo Output Shaft

---

# 3. Coordinate System

Origin

Servo Output Axis

---

Robot Frame

+X Forward

+Y Left

+Z Up

Status

FROZEN

---

# 4. Architecture

Approved Architecture

Dual Clamp Torque Module

---

Layout

Servo Horn

||

Clamp Body

||

Output Shaft Clamp

---

Status

FROZEN

---

# 5. Global Parameters

Shaft_Dia = 8 mm

Clamp_Bolt = M3

Wall = 6 mm

Clearance = 0.20 mm

Insert_Dia = 4.6 mm

---

No Hard-Coded Dimensions

---

# 6. Servo Interface

Reference: SERVO_STS3046

Mount Style: Horn Clamp

Fasteners: 2 × M3

Status: FROZEN

---

# 7. Output Shaft Interface

Reference: SHAFT_8MM_STD

Clamp Bore: 8.15 mm

Clamp Length: 15 mm

Fasteners: 2 × M3

Status: FROZEN

---

# 8. Split Clamp Geometry

Required: YES

Gap Width: 2 mm

Minimum Clamp Thickness: 6 mm

Minimum Outer Wall: 6 mm

Status: FROZEN

---

# 9. Insert Design

Reference: INS_M3

Insert Hole: 4.6 mm

Boss Diameter: 6 mm

Boss Height: 8 mm

Status: FROZEN

---

# 10. Design Torque Requirement

Servo Rated Torque ≈ 4.5 Nm

Required Safety Factor 2.0

Design Torque 9 Nm

Permanent Deformation NOT ALLOWED

Crack Initiation NOT ALLOWED

Status: FROZEN

---

# 11. Structural Requirements

Clamp Region: 6 mm Wall

Insert Region: 6 mm Wall

Hub Region: 6 mm Wall

Fillet Radius ≥2 mm

Status: FROZEN

---

# 12. Weight Target

Target: 25~45 g

Maximum: 60 g

Status: FROZEN

---

# 13. Print Orientation

Preferred: Clamp Split Vertical

Reason: Maximum Clamp Strength & Best Layer Direction

Status: FROZEN

---

# 14. Manufacturing Rules

Material: PETG

Perimeters: 5

Infill: 50% Gyroid

Layer Height: 0.20 mm

Support: NONE Preferred

Status: FROZEN

---

# 15. Verification Checklist

□ Servo Horn Fits

□ Shaft Fits

□ Clamp Operates

□ Inserts Installed

□ No Cracks

□ Weight <60 g

□ A1 Mini Compatible

---

# 16. Deliverables

Required Files:

Knee_TorqueModule_RevA.f3d

Knee_TorqueModule_RevA.step

Knee_TorqueModule_Print_RevA.stl

Required Drawing:

Knee_TorqueModule_DWG_RevA.pdf

---

# 17. Exit Criteria

Geometry Complete: PASS

Assembly Compatible: PASS

Torque Verification Complete: PASS

Manufacturing Compatible: PASS

Status: READY FOR CAD MODELING
