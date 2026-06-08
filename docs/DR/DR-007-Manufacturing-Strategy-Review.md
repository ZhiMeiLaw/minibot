# Mini-Atlas V6 Alpha

# DR-007 Manufacturing Strategy Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-007

Subsystem:

Manufacturing Strategy

Parent Documents:

* DR-001 System Architecture Review
* DR-006 Bearing and Shaft Review
* MP-001 Manufacturing Package Release

Related Documents:

* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* CDS-06 Wheel Module Architecture
* CDS-08 Dual Leg and Pelvis Integration

---

# 1. Purpose

本评审用于确定 Mini-Atlas V6 Alpha 的制造策略。

目标：

* 最低制造成本
* 最低设备门槛
* 全球可复制
* 开源友好
* 支持个人开发者制造
* 支持快速迭代

本评审通过后：

所有机械设计必须遵守本文档制造约束。

---

# 2. Manufacturing Philosophy

Mini-Atlas V6 Alpha 不追求工业量产。

目标是：

```text
个人开发者
实验室
学校
Maker
```

均可独立制造。

---

# 3. Candidate Manufacturing Methods

## Option A

CNC Aluminum

Advantages

* 强度高
* 精度高

Disadvantages

* 成本高
* 制造周期长
* 不利于开源复制

Result

REJECTED

---

## Option B

Injection Molding

Advantages

* 适合量产

Disadvantages

* 模具成本极高

Result

REJECTED

---

## Option C

FDM 3D Printing

Advantages

* 成本低
* 快速迭代
* 全球可复制

Disadvantages

* 强度较低

Result

APPROVED

---

# 4. Supported Printers

Primary

Bambu Lab A1 Mini

---

Secondary

Bambu Lab A1

---

Validation Printer

A1 Mini

---

Reason

A1 Mini 成本最低。

如果能够在 A1 Mini 上制造：

则意味着绝大多数用户均可复现。

---

# 5. Print Volume Constraints

## A1 Mini

Build Volume

```text
180 × 180 × 180 mm
```

---

Design Rule

任何单个零件不得超过：

```text
170 × 170 × 170 mm
```

预留打印边界。

---

Status

FROZEN

---

# 6. Material Review

## PLA

Advantages

* 易打印

Disadvantages

* 热变形
* 长期蠕变

Result

REJECTED

---

## ABS

Advantages

* 强度较高

Disadvantages

* 翘曲
* 打印难度高

Result

OPTIONAL

---

## PETG

Advantages

* 强度高
* 韧性高
* 易打印

Result

APPROVED

---

## PET-CF

Advantages

* 更高刚度

Result

BETA OPTIONAL

---

# 7. Frozen Materials

Structural Parts

PETG

---

Load Bearing Parts

PETG

---

Covers

PETG

---

Status

FROZEN

---

# 8. Fastener Strategy

Unified Hardware

```text
M3
```

---

Approved

M3×8

M3×10

M3×12

M3×16

M3×20

---

Nuts

M3 Nylon Lock Nut

---

Result

APPROVED

---

# 9. Brass Insert Strategy

Insert Type

Heat Set Brass Insert

---

Thread

M3

---

Application

All Repeated Assembly Locations

---

Examples

* Pelvis
* Hip Roll
* Hip Pitch
* Knee
* Wheel Module

---

Status

FROZEN

---

# 10. Structural Members

## Carbon Tube

Frozen Standard

```text
OD = 12 mm

ID = 10 mm
```

---

Material

Carbon Fiber Tube

---

Application

Upper Leg

Lower Leg

---

Status

FROZEN

---

# 11. Bearing Installation

Method

Press Fit

---

Installation Tool

Hand Press

or

Bench Vise

---

No Adhesive Required

APPROVED

---

# 12. Assembly Philosophy

Rule 1

No Glue

---

Rule 2

No Permanent Assembly

---

Rule 3

Field Repairable

---

Rule 4

All Bearings Replaceable

---

Rule 5

All Servos Replaceable

---

Status

APPROVED

---

# 13. Manufacturing Time Estimate

Hip Roll

4~6 Hours

---

Hip Pitch

4~6 Hours

---

Knee

3~5 Hours

---

Wheel Module

2~4 Hours

---

Pelvis

6~8 Hours

---

Total Robot

Approx.

40~60 Print Hours

---

# 14. Cost Estimate

Printing Material

≈ 1kg PETG

---

Fasteners

≈ $15

---

Bearings

≈ $20

---

Carbon Tubes

≈ $20

---

Total Manufacturing Hardware

≈ $55

Excluding Electronics

---

# 15. Quality Control Requirements

Check:

* Bearing Bore Diameter
* Shaft Alignment
* Carbon Tube Fit
* Servo Mount Fit
* Layer Adhesion
* Brass Insert Retention

---

Status

MANDATORY

---

# 16. Risk Assessment

Risk

Layer Delamination

Mitigation

PETG

4 Perimeters

35% Gyroid

---

Risk

Insert Pull-Out

Mitigation

Long Insert Boss

---

Risk

Warping

Mitigation

A1 Enclosure Optional

---

# 17. Engineering Decision

Manufacturing Method

FDM

APPROVED

---

Primary Material

PETG

APPROVED

---

Primary Printer

A1 Mini

APPROVED

---

Fastener Standard

M3

APPROVED

---

Carbon Tube Standard

12 mm

APPROVED

---

Brass Insert Standard

M3 Heat Set

APPROVED

---

# 18. Freeze Summary

Manufacturing Strategy

FROZEN

---

Printer Platform

FROZEN

---

Material System

FROZEN

---

Fastener System

FROZEN

---

Insert System

FROZEN

---

Status

APPROVED

---

Next Document

DR-008-Printable-Design-Review.md
