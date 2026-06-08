# Mini-Atlas V6 Alpha

# DR-006 Bearing and Shaft Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-006

Subsystem:

Mechanical Standards

Parent Documents:

* DR-003 Joint Architecture Review
* DR-004 Hip Architecture Review
* DR-005 Servo Capability Review
* CDS-02A Standard Component Library Revision A

Related Documents:

* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* MP-001 Manufacturing Package

---

# 1. Purpose

本评审用于冻结 Mini-Atlas V6 Alpha 的机械标准件体系。

目标：

* 统一轴承规格
* 统一主轴规格
* 统一碳管接口
* 降低BOM复杂度
* 提高可制造性
* 提高维护性

评审通过后：

所有CAD设计必须使用本文档冻结规格。

---

# 2. Design Philosophy

原则：

```text
少规格
少零件
少库存
高复用
```

避免：

```text
Hip 用一种轴承

Knee 用另一种轴承

Wheel 再一种轴承
```

这种设计会显著增加制造和维护成本。

---

# 3. Candidate Bearing Families

## Option A

6803

6802

688

698

---

## Option B

6803

6701

6702

688

698

---

Result

Option A

APPROVED

原因：

* 易采购
* 价格低
* 标准化程度高

---

# 4. Frozen Bearing Library

## 6803

Dimensions

```text
17 × 26 × 5 mm
```

Use

* Hip Roll
* Hip Pitch

Status

FROZEN

---

## 6802

Dimensions

```text
15 × 24 × 5 mm
```

Use

* Knee

Status

FROZEN

---

## 698

Dimensions

```text
8 × 19 × 6 mm
```

Use

* Knee Output
* Auxiliary Supports

Status

FROZEN

---

## 688

Dimensions

```text
8 × 16 × 5 mm
```

Use

* Hip Roll Torque Module
* Hip Pitch Torque Module

Status

FROZEN

---

# 5. Bearing Architecture

Approved Architecture

```text
Bearing

    ||

Bearing

    ||

Output Shaft
```

---

Result

Dual Bearing Support

APPROVED

---

Rejected

```text
Single Bearing
```

Reason

刚性不足

长期磨损大

---

# 6. Output Shaft Review

Candidate

6mm

8mm

10mm

---

## 6mm

Pros

轻

---

Cons

刚度不足

---

Result

REJECTED

---

## 8mm

Pros

刚度足够

重量合理

标准件丰富

---

Result

APPROVED

---

## 10mm

Pros

更强

---

Cons

过重

空间浪费

---

Result

REJECTED

---

# 7. Frozen Shaft Standard

Material

Stainless Steel

---

Diameter

```text
8mm
```

---

Tolerance

```text
h7
```

---

Surface

Polished

---

Status

FROZEN

---

# 8. Carbon Tube Review

Candidate

10mm

12mm

14mm

16mm

---

Evaluation

Weight

Stiffness

Availability

---

Decision

```text
12mm OD

10mm ID
```

Carbon Tube

APPROVED

---

Reason

最佳重量刚度比

---

# 9. Carbon Tube Interface

Architecture

```text
Split Clamp
```

---

Fasteners

2 × M3

---

Clamp Length

20mm

---

Status

FROZEN

---

# 10. Load Path Review

Approved

```text
Leg Load

↓

Carbon Tube

↓

Output Shaft

↓

Bearings

↓

Housing

↓

Pelvis
```

---

Not Through Servo

APPROVED

---

# 11. Tolerance Review

Bearing Seat

```text
+0.05 / +0.10
```

---

Shaft Fit

```text
h7
```

---

Carbon Tube Bore

```text
+0.15
```

---

Status

APPROVED

---

# 12. Manufacturing Review

Manufacturing Method

FDM

---

Printer

Bambu Lab A1 Mini

Bambu Lab A1

---

Layer Height

0.20 mm

---

Nozzle

0.40 mm

---

Material

PETG

---

Status

PASS

---

# 13. Maintenance Review

Bearing Replacement

Tool-less Housing Access

---

Shaft Replacement

Supported

---

Carbon Tube Replacement

Supported

---

Status

PASS

---

# 14. Risk Assessment

Risk

Bearing Seat Wear

Mitigation

Brass Insert

---

Risk

Carbon Tube Slip

Mitigation

Dual Clamp

---

Risk

Shaft Bending

Mitigation

8mm Shaft

---

# 15. Engineering Decision

6803

APPROVED

---

6802

APPROVED

---

698

APPROVED

---

688

APPROVED

---

8mm Shaft

APPROVED

---

12mm Carbon Tube

APPROVED

---

# 16. Freeze Summary

Bearing Family

FROZEN

---

Output Shaft

8mm

FROZEN

---

Carbon Tube

12mm OD

FROZEN

---

Dual Bearing Architecture

FROZEN

---

Status

APPROVED

---

Next Document

DR-007-Manufacturing-Strategy-Review.md
