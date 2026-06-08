# Mini-Atlas V6 Alpha

# DR-008 Printable Design Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-008

Subsystem:

DFM (Design For Manufacturing)

Parent Documents:

* DR-006 Bearing and Shaft Review
* DR-007 Manufacturing Strategy Review
* MP-001 Manufacturing Package Release

Related Documents:

* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* CDS-06 Wheel Module Architecture
* CDS-08 Dual Leg and Pelvis Integration

---

# 1. Purpose

本评审用于验证 Mini-Atlas V6 Alpha 全部结构件是否满足：

* Bambu Lab A1 Mini 打印能力
* Bambu Lab A1 打印能力
* PETG材料约束
* 无特殊工业设备制造要求

目标：

确保项目能够被个人开发者完整复现。

---

# 2. Manufacturing Baseline

Primary Printer

Bambu Lab A1 Mini

---

Secondary Printer

Bambu Lab A1

---

Nozzle

0.4 mm

---

Layer Height

0.20 mm

---

Material

PETG

---

Status

FROZEN

---

# 3. Printable Envelope Review

A1 Mini Build Volume

```text
180 × 180 × 180 mm
```

Design Envelope

```text
170 × 170 × 170 mm
```

Rule

任何单个零件必须放入设计包络。

---

Result

PASS

---

# 4. Part Classification

## Class A

Structural Load Bearing

Examples

* Hip Roll Base
* Hip Pitch Base
* Knee Base
* Pelvis

Requirements

* 4 Perimeters
* 35% Gyroid Infill
* PETG

---

## Class B

Motion Components

Examples

* Hip Roll Output
* Hip Pitch Output
* Knee Output

Requirements

* 5 Perimeters
* 40% Gyroid

---

## Class C

Covers

Examples

* Electronics Cover
* Cable Cover

Requirements

* 2 Perimeters
* 15% Gyroid

---

# 5. Overhang Review

Maximum Allowed Unsupported Overhang

```text
45°
```

Preferred

```text
≤ 40°
```

---

Result

PASS

---

# 6. Bridging Review

Maximum Recommended Bridge

```text
20 mm
```

Preferred

```text
< 15 mm
```

---

All Designs

Must Avoid Long Bridges

---

Status

APPROVED

---

# 7. Bearing Seat Review

Affected Parts

* Hip Roll Base
* Hip Pitch Base
* Knee Base

Requirements

* Vertical Print Orientation
* Circularity Preservation

Tolerance

```text
+0.05 ~ +0.10 mm
```

---

Status

APPROVED

---

# 8. Shaft Bore Review

Affected Parts

* Output Arms
* Torque Modules

Requirements

* Printed Vertical
* Reamed if Necessary

Tolerance

```text
+0.10 mm
```

---

Status

APPROVED

---

# 9. Brass Insert Review

Standard

M3 Heat Set Insert

---

Boss Diameter

```text
≥ 6 mm
```

---

Boss Height

```text
≥ 8 mm
```

---

Edge Clearance

```text
≥ 2 mm
```

---

Status

APPROVED

---

# 10. Carbon Tube Interface Review

Tube Standard

```text
12 mm OD
10 mm ID
```

---

Clamp Type

Split Clamp

---

Fasteners

2 × M3

---

Minimum Clamp Length

```text
20 mm
```

---

Status

APPROVED

---

# 11. Support Strategy

Goal

Support-Free First

---

Allowed Supports

* Bearing Pocket Roof
* Cable Tunnel Roof
* Internal Service Channels

---

Avoid

* Deep Internal Supports
* Non-removable Supports

---

Status

APPROVED

---

# 12. Hip Roll Manufacturability Review

Components

* CDS-03A Base
* CDS-03B Output
* CDS-03C Torque Module

Result

PASS

---

No Critical Support Required

PASS

---

A1 Mini Compatible

PASS

---

# 13. Hip Pitch Manufacturability Review

Components

* CDS-04A Base
* CDS-04B Output
* CDS-04C Torque Module

Result

PASS

---

No Critical Support Required

PASS

---

A1 Mini Compatible

PASS

---

# 14. Knee Manufacturability Review

Components

* CDS-05A Base
* CDS-05B Output
* CDS-05C Torque Module

Result

PASS

---

A1 Mini Compatible

PASS

---

# 15. Pelvis Manufacturability Review

Components

* CDS-08 Pelvis

Result

PASS

---

Split Design

Required

---

A1 Mini Compatible

PASS

---

# 16. Print Time Analysis

| Subsystem    | Estimated Print Time |
| ------------ | -------------------: |
| Hip Roll     |                4~6 h |
| Hip Pitch    |                4~6 h |
| Knee         |                3~5 h |
| Wheel Module |                2~4 h |
| Pelvis       |                6~8 h |
| Covers       |                2~3 h |

---

Total Robot

```text
40~60 Hours
```

---

# 17. Common Failure Modes

Failure

Bearing Pocket Too Tight

Mitigation

Tolerance Rule DR-006

---

Failure

Insert Pull-Out

Mitigation

Boss Geometry Standard

---

Failure

Carbon Tube Slip

Mitigation

Dual Clamp

---

Failure

Layer Separation

Mitigation

PETG
4+ Perimeters

---

# 18. Verification Checklist

□ Fits A1 Mini Volume

□ PETG Compatible

□ M3 Hardware Compatible

□ Bearing Seats Printable

□ Inserts Accessible

□ No Non-removable Supports

□ Serviceable After Assembly

□ Weight Within Budget

---

# 19. Engineering Decision

Printable on A1 Mini

APPROVED

---

Printable on A1

APPROVED

---

PETG Compatible

APPROVED

---

Support Strategy

APPROVED

---

Manufacturing Package

READY

---

# 20. Freeze Summary

Print Envelope

FROZEN

---

PETG Rules

FROZEN

---

Support Rules

FROZEN

---

Insert Rules

FROZEN

---

Bearing Seat Rules

FROZEN

---

Status

APPROVED

---

DR Series Completion

DR-001 → DR-008

COMPLETE
