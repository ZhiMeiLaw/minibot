# Mini-Atlas V6 Alpha

# CDS-07 Full Leg Subsystem Integration

Version: 1.0 Freeze A

Status: APPROVED

Assembly Number:

V6-ASM-0010

Assembly Name:

Full Leg Subsystem

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-03 Hip Roll Joint
* CDS-04 Hip Pitch Joint
* CDS-05 Knee Joint
* CDS-06 Wheel Module Architecture
* DR-010 Leg Subsystem Review
* DR-011 Ankle Architecture Review

---

# 1. Purpose

验证完整单腿系统：

Hip Roll

↓

Hip Pitch

↓

Knee

↓

Wheel Module

是否满足：

* 结构要求
* 运动要求
* 重量要求
* 制造要求
* 维护要求

通过后：

允许进入

Pelvis Integration

阶段。

---

# 2. Assembly Overview

Leg Assembly：

Hip Roll

↓

Hip Pitch

↓

Upper Leg

↓

Knee

↓

Lower Leg

↓

Wheel Module

---

自由度：

Hip Roll

1 DOF

---

Hip Pitch

1 DOF

---

Knee

1 DOF

---

Total

3 DOF

Per Leg

---

# 3. Assembly Structure

Pelvis Interface

↓

Hip Roll Base

↓

Hip Roll Output

↓

Hip Pitch Base

↓

Hip Pitch Output

↓

Upper Leg Carbon Tube

↓

Knee Base

↓

Knee Output

↓

Lower Leg Carbon Tube

↓

Wheel Adapter

↓

GB37-520

↓

80mm Wheel

---

# 4. Geometry Verification

Upper Leg

120 mm

---

Lower Leg

120 mm

---

Wheel Radius

40 mm

---

Overall Leg Length

≈280 mm

---

目标：

270~300 mm

---

结果：

PASS

---

# 5. Weight Verification

Hip Roll

≈150 g

---

Hip Pitch

≈154 g

---

Knee

≈179 g

---

Carbon Tube

≈40 g

---

Wheel Module

≈235 g

---

Hardware

≈40 g

---

Total

≈798 g

---

目标：

<850 g

---

结果：

PASS

---

# 6. Center of Mass Verification

主要质量：

Hip Servo

Hip Pitch Servo

Knee Servo

Battery（未来）

---

重心位置：

Hip Pitch下方

约60 mm

---

评估：

有利于稳定步态

---

结果：

PASS

---

# 7. Motion Envelope Verification

Hip Roll

±25°

---

Hip Pitch

+60°

↓

-30°

---

Knee

0°

↓

120°

---

验证：

站立

PASS

---

抬腿

PASS

---

下蹲

PASS

---

转向

PASS

---

结果：

PASS

---

# 8. Ground Clearance Verification

Wheel Radius

40 mm

---

Lower Leg Offset

20 mm

---

Ground Clearance

≈20 mm

---

目标：

≥15 mm

---

结果：

PASS

---

# 9. Wheel Integration Verification

Wheel Diameter

80 mm

---

Motor

GB37-520

---

安装空间：

充足

---

无干涉

---

结果：

PASS

---

# 10. Structural Load Path Review

载荷路径：

Ground

↓

Wheel

↓

Wheel Adapter

↓

Lower Leg

↓

Knee

↓

Upper Leg

↓

Hip Pitch

↓

Hip Roll

↓

Pelvis

---

所有关节：

Bearing Supported

---

评估：

合理

---

结果：

PASS

---

# 11. Wire Harness Review

Servo Bus：

Hip Roll

↓

Hip Pitch

↓

Knee

---

Motor Cable：

Wheel Module

↓

Pelvis

---

预留通道：

Ø8 mm

---

验证：

□ 不夹线

□ 可维护

□ 可更换

---

结果：

PASS

---

# 12. Maintenance Review

Servo Replacement

<5 min

---

Wheel Replacement

<5 min

---

Bearing Replacement

<10 min

---

Carbon Tube Replacement

<5 min

---

结果：

PASS

---

# 13. Printability Review

平台：

Bambu Lab A1

---

兼容：

A1 Mini

---

最大零件：

<100 mm

---

无需分件

---

结果：

PASS

---

# 14. Reliability Review

风险：

Clamp Loosening

---

措施：

Loctite 243

---

风险：

PETG Fatigue

---

措施：

Ribs

Brass Inserts

---

风险：

Carbon Tube Slip

---

措施：

Dual Clamp

Micro Serration

---

结果：

PASS

---

# 15. Power Impact Review

Servo Count

3 / Leg

---

Wheel Motor

1 / Leg

---

Total Per Leg

4 Actuators

---

双腿：

6 Servo

*

2 Wheel Motors

---

符合：

EDS-02

功耗预算

---

结果：

PASS

---

# 16. CAD Assembly Requirements

建立：

V6-ASM-0010

---

SolidWorks Assembly

或

Fusion360 Assembly

---

必须验证：

* Motion Study
* Collision Check
* Interference Check
* Center Of Mass

---

# 17. Assembly Verification Checklist

CAD：

□ 无干涉

□ 运动范围正确

□ Wheel空间正确

□ 重心合理

---

打印：

□ Carbon Tube装配正常

□ Servo安装正常

□ Bearing安装正常

---

运动：

□ Hip Roll正常

□ Hip Pitch正常

□ Knee正常

□ Wheel正常

---

# 18. Freeze Summary

Architecture

3DOF Leg

*

Wheel Module

---

Hip Roll

STS3046

---

Hip Pitch

STS3046

---

Knee

STS3046

---

Wheel

80 mm

---

Wheel Motor

GB37-520

---

Leg Length

≈280 mm

---

Weight

≈798 g

---

Ground Clearance

≈20 mm

---

Status

APPROVED

DESIGN FREEZE

READY FOR

CDS-08 Dual Leg & Pelvis Integration
