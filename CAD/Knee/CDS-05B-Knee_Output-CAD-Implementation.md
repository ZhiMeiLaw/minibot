# Mini-Atlas V6 Alpha

# CDS-05B Knee Output CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-05B-IMP

Subsystem:

Knee Joint

CAD Part:

Knee_Output

Parent Documents:

* CDS-05A Knee Base CAD Implementation
* DR-009 Knee Architecture Review
* CDS-07 Full Leg Subsystem Integration
* DR-012 Leg Kinematics & Torque Validation

---

# 1. Purpose

指导 Knee_Output 实际 CAD 建模。

本零件负责：

* 接收 Knee 输出轴扭矩
* 固定 Lower Leg Carbon Tube
* 支撑 Wheel Module
* 传递腿部动态载荷

最终输出：

Knee_Output_RevA.f3d

Knee_Output_RevA.step

Knee_Output_Print_RevA.stl

---

# 2. Functional Requirements

Knee_Output 必须实现：

连接输出轴

安装 Torque Module

夹持 Lower Leg Tube

连接 Wheel Module

传递动态载荷

---

# 3. Coordinate System

Origin

Knee Rotation Axis

---

Robot Coordinate

+X Forward

+Y Left

+Z Up

---

Status

FROZEN

---

# 4. Architecture

Approved Architecture

Output Hub

↓

Tube Clamp

↓

Lower Leg Structure

↓

Wheel Module

---

Status

FROZEN

---

# 5. Master Sketch

必须首先建立：

Knee Axis

Output Shaft Axis

Tube Axis

Wheel Mount Plane

---

禁止直接实体建模

---

# 6. Global Parameters

Shaft_Dia = 8

Tube_OD = 12

Tube_ID = 10

Clamp_Length = 25

Wall = 6

Clearance = 0.20

---

No Hard-Coded Dimensions

---

# 7. Output Hub

Reference

SHAFT_8MM_STD

---

Bore Diameter

8.15 mm

---

Hub Diameter

28 mm

---

Hub Thickness

15 mm

---

Status

FROZEN

---

# 8. Carbon Tube Interface

Reference

CF_TUBE_12OD_10ID

---

Clamp Type

Dual Split Clamp

---

Fasteners

2 × M3

---

Clamp Length

25 mm

---

Insertion Depth

≥25 mm

---

Status

FROZEN

---

# 9. Torque Module Interface

Reference

Knee_TorqueModule

---

Connection Type

Dual Clamp Interface

---

Mounting Holes

2 × M3

---

Insert Type

INS_M3

---

Status

FROZEN

---

# 10. Wheel Module Interface

Reference

Wheel_Module_RevA

---

Mount Pattern

4 × M3

---

Hole Diameter

3.2 mm

---

Boss Thickness

6 mm

---

Status

FROZEN

---

# 11. Structural Requirements

Hub Region

6 mm Wall

Minimum

---

Clamp Region

6 mm Wall

Minimum

---

Wheel Mount Region

8 mm Wall

Recommended

---

Fillet Radius

≥2 mm

Required

---

Status

FROZEN

---

# 12. Motion Range

Extension

0°

---

Walk Range

60°

---

Max Flexion

120°

---

Approved Range

0° ~ 120°

---

Status

FROZEN

---

# 13. Mechanical Stop Interface

Required

YES

---

Stop Margin

5°

Before Servo Limit

---

Status

FROZEN

---

# 14. Weight Target

Target

80~120 g

---

Maximum

150 g

---

Status

FROZEN

---

# 15. Print Orientation

Preferred

Hub Down

---

Reason

Maximum Strength

Best Bore Accuracy

---

Status

FROZEN

---

# 16. Manufacturing Rules

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

Support

None Preferred

---

# 17. Verification Checklist

□ Shaft Fits

□ Carbon Tube Fits

□ Torque Module Fits

□ Wheel Interface Fits

□ Mechanical Stop Works

□ Weight <150 g

□ A1 Mini Compatible

---

# 18. Deliverables

Required Files

Knee_Output_RevA.f3d

Knee_Output_RevA.step

Knee_Output_Print_RevA.stl

---

Required Drawing

Knee_Output_DWG_RevA.pdf

---

# 19. Exit Criteria

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
