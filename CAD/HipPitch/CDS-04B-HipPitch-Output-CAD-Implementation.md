# Mini-Atlas V6 Alpha

# CDS-04B HipPitch Output CAD Implementation

Version: 1.0

Status: READY FOR MODELING

Document Number:

CDS-04B-IMP

Subsystem:

Hip Pitch Joint

CAD Part:

HipPitch_Output

Parent Documents:

* CDS-04A HipPitch Base CAD Implementation
* DR-004 Hip Architecture Review
* DR-006 Bearing and Shaft Review
* CDS-07 Full Leg Subsystem Integration

---

# 1. Purpose

指导 HipPitch_Output 实际 CAD 建模。

本零件负责：

* 接收 Hip Pitch 输出轴扭矩
* 固定大腿碳管
* 支撑 Knee Joint
* 承载整条腿重量

最终输出：

```text id="h0t7ru"
HipPitch_Output_RevA.f3d

HipPitch_Output_RevA.step

HipPitch_Output_Print_RevA.stl
```

---

# 2. Functional Requirements

HipPitch_Output 必须实现：

```text id="yn4chb"
连接输出轴

安装Torque Module

夹持大腿碳管

连接Knee模块

传递腿部载荷
```

---

# 3. Coordinate System

Origin

Hip Pitch Rotation Axis

---

Robot Frame

```text id="8ocmtr"
+X Forward

+Y Left

+Z Up
```

---

Status

FROZEN

---

# 4. Architecture

Approved Architecture

```text id="hpsuzj"
Output Hub

↓

Tube Clamp

↓

Upper Leg Structure
```

---

Status

FROZEN

---

# 5. Master Sketch

必须首先建立：

```text id="e4tbjp"
Hip Pitch Axis

Output Shaft Axis

Tube Axis

Knee Mount Plane
```

---

禁止直接拉伸实体。

---

# 6. Global Parameters

```text id="c0mvrk"
Shaft_Dia = 8

Tube_OD = 12

Tube_ID = 10

Clamp_Length = 25

Wall = 6

Clearance = 0.20
```

---

No Hard-Coded Dimensions

---

# 7. Output Hub

Reference

```text id="92jlwm"
SHAFT_8MM_STD
```

---

Bore Diameter

```text id="3v8jlwm"
8.15 mm
```

---

Hub Diameter

```text id="wq7jlwm"
28 mm
```

---

Hub Thickness

```text id="1m8jlwm"
15 mm
```

---

Status

FROZEN

---

# 8. Carbon Tube Interface

Reference

```text id="prbjlwm"
CF_TUBE_12OD_10ID
```

---

Clamp Type

```text id="a0ajlwm"
Dual Split Clamp
```

---

Fasteners

```text id="jlwmr7"
2 × M3
```

---

Clamp Length

```text id="jlwmv2"
25 mm
```

---

Insertion Depth

```text id="jlwmm5"
≥25 mm
```

---

Status

FROZEN

---

# 9. Torque Module Interface

Reference

```text id="jlwmn9"
HipPitch_TorqueModule
```

---

Connection Type

```text id="jlwmk4"
Dual Clamp Interface
```

---

Mounting Holes

```text id="jlwmc6"
2 × M3
```

---

Insert Type

```text id="jlwmw3"
INS_M3
```

---

Status

FROZEN

---

# 10. Knee Interface

Connection

```text id="jlwmf8"
Knee_Base
```

---

Mount Pattern

```text id="jlwmd7"
4 × M3
```

---

Hole Diameter

```text id="jlwms2"
3.2 mm
```

---

Mount Boss

```text id="jlwmp9"
6 mm
```

Minimum

---

Status

FROZEN

---

# 11. Structural Requirements

Hub Wall

```text id="jlwmy5"
6 mm
```

Minimum

---

Clamp Wall

```text id="jlwmx1"
6 mm
```

Minimum

---

Knee Mount Region

```text id="jlwmu4"
8 mm
```

Recommended

---

Status

FROZEN

---

# 12. Mechanical Stop Interface

Required

YES

---

Travel

```text id="jlwmb8"
-45°

0°

+90°
```

---

Clearance

```text id="jlwmq6"
2 mm
```

Minimum

---

Status

FROZEN

---

# 13. Weight Target

Target

```text id="jlwmj3"
80~120 g
```

---

Maximum

```text id="jlwmz7"
150 g
```

---

# 14. Print Orientation

Preferred

```text id="jlwmh4"
Hub Down
```

---

Reason

Maximum Strength

Best Bore Accuracy

---

Status

FROZEN

---

# 15. Manufacturing Rules

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

# 16. Verification Checklist

□ Shaft Fits

□ Carbon Tube Fits

□ Torque Module Fits

□ Knee Interface Fits

□ Mechanical Stop Works

□ Weight <150 g

□ A1 Mini Compatible

---

# 17. Deliverables

Required Files

```text id="jlwml2"
HipPitch_Output_RevA.f3d

HipPitch_Output_RevA.step

HipPitch_Output_Print_RevA.stl
```

---

Required Drawing

```text id="jlwmg1"
HipPitch_Output_DWG_RevA.pdf
```

---

# 18. Exit Criteria

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
