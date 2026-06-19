# Mini-Atlas V6 Alpha

# DR-009 Knee Architecture Review

Version: 2.0

Status: FROZEN

Document Number:

DR-009

Subsystem:

Knee Joint

Review Type:

Architecture Freeze

Parent Documents:

* DR-003 Joint Architecture Review
* DR-006 Bearing and Shaft Review
* CDS-07 Full Leg Subsystem Integration
* DR-012 Leg Kinematics & Torque Validation

---

# 1. Purpose

冻结 Knee Joint 机械架构。

目标：

* 承载单腿支撑载荷
* 支持动态步行
* 支持轮式运动
* 支持跌倒恢复
* 兼容 Alpha Prototype

---

# 2. Functional Requirements

Knee 必须实现：

```text
膝关节弯曲

支撑腿部重量

承受动态冲击

连接上腿

连接下腿

支持维护
```

---

# 3. Architecture Candidates

Candidate A

Servo Direct Drive

Result

REJECTED

Reason

Servo承担弯矩

---

Candidate B

Servo + Bearing

Result

REJECTED

Reason

结构刚度不足

---

Candidate C

Independent Shaft

Dual Bearing

Torque Module

Result

APPROVED

````

结构：

```text
Servo

↓

Torque Module

↓

Output Shaft

↓

Dual Bearing

↓

Knee Structure
````

---

# 4. Servo Selection Review

Candidate

STS3046

---

Rated Torque

≈4.5 Nm

---

Alpha Requirement

≈2.5~3.0 Nm

---

Result

PASS

---

Status

APPROVED

---

# 5. Bearing Review

Approved Bearing

6802

Dimensions

15 × 24 × 5

---

Quantity

2

---

Layout

```text
6802

 ||

6802
```

---

Bearing Gap

10 mm

---

Status

APPROVED

---

# 6. Shaft Review

Approved Shaft

SHAFT_8MM_STD

---

Material

SS304

---

Diameter

8 mm

---

Reason

与 Hip Roll / Hip Pitch 共用

---

Status

APPROVED

---

# 7. Upper Leg Interface

Reference

HipPitch_Output

---

Connection

4 × M3

---

Boss Thickness

6 mm

---

Status

APPROVED

---

# 8. Lower Leg Interface

Reference

Lower Leg Tube

---

Tube

CF_TUBE_12OD_10ID

---

Insertion Depth

≥25 mm

---

Clamp Type

Dual Split Clamp

---

Status

APPROVED

---

# 9. Motion Range Review

Required

```text
Extension     0°

Walk Range   60°

Max Flexion 120°
```

---

Approved Range

```text
0° ~ 120°
```

---

Status

APPROVED

---

# 10. Mechanical Stop Review

Required

YES

---

Reason

Protect Servo

Protect Bearings

Protect Printed Parts

---

Stop Margin

5°

Before Servo Limit

---

Status

APPROVED

---

# 11. Maintenance Review

Must Allow

* Servo Replacement
* Bearing Replacement
* Shaft Replacement
* Carbon Tube Replacement

Without Destroying Parts

---

Status

APPROVED

---

# 12. Weight Budget

| Component     |   Target |
| ------------- | -------: |
| Base          | 80~120 g |
| Output        | 80~120 g |
| Torque Module |  25~45 g |
| Hardware      |     20 g |

---

Target Assembly Weight

205~305 g

---

Maximum

350 g

---

Status

APPROVED

---

# 13. Manufacturing Review

Material

PETG

---

Printer

Bambu A1 Mini

---

Support Free Preferred

YES

---

Status

APPROVED

---

# 14. Freeze Decision

Approved Architecture

```text
STS3046

↓

Torque Module

↓

8mm Shaft

↓

Dual 6802

↓

Knee Output
```

---

Status

FROZEN

---

# 15. Exit Criteria

Architecture Stable

PASS

---

Weight Budget Valid

PASS

---

Servo Capability Valid

PASS

---

Manufacturing Valid

PASS

---

Status

READY FOR CAD IMPLEMENTATION
