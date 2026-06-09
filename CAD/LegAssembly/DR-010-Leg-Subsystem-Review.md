# Mini-Atlas V6 Alpha

# DR-010 Leg Subsystem Review

Version: 1.0

Status: DESIGN REVIEW

Document Number:

DR-010

Subsystem:

Single Leg

Review Type:

System Architecture Review

Parent Documents:

* CDS-03 Hip Roll Series
* CDS-04 Hip Pitch Series
* CDS-05 Knee Series
* DR-009 Knee Architecture Review
* DR-012 Leg Kinematics & Torque Validation

---

# 1. Purpose

验证完整单腿系统：

* 可运动
* 可制造
* 可维护
* 可扩展
* 满足 Alpha Prototype 目标

通过后：

Single Leg Architecture Frozen

---

# 2. Leg Architecture

Mechanical Chain

Pelvis

↓

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

Architecture Status

COMPLETE

---

# 3. Degrees of Freedom

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

---

Status

APPROVED

---

# 4. Kinematic Review

Motion Chain

```text
Hip Roll

↓

Hip Pitch

↓

Knee
```

---

Required Functions

Side Weight Shift

PASS

---

Leg Swing

PASS

---

Ground Clearance

PASS

---

Wheel Mode Compatibility

PASS

---

Result

APPROVED

---

# 5. Motion Range Review

Hip Roll

-30° ~ +30°

---

Hip Pitch

-45° ~ +90°

---

Knee

0° ~ 120°

---

Result

PASS

---

# 6. Torque Review

Hip Roll

STS3046

PASS

---

Hip Pitch

STS3046

PASS

---

Knee

STS3046

PASS

---

Peak Load

Within Budget

---

Result

APPROVED

---

# 7. Structural Review

Load Path

```text
Ground

↓

Wheel

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
```

---

Independent Shaft

YES

---

Dual Bearing

YES

---

Servo Load Isolation

YES

---

Result

APPROVED

---

# 8. Weight Review

Target

Per Leg

1.5 kg

---

Expected

| Item      |  Weight |
| --------- | ------: |
| Hip Roll  | 0.35 kg |
| Hip Pitch | 0.40 kg |
| Knee      | 0.35 kg |
| Tubes     | 0.20 kg |
| Hardware  | 0.10 kg |

---

Total

1.4 kg

---

Result

PASS

---

# 9. Center of Gravity Review

Target

CG Above Hip Axis

---

Expected

Near Pelvis

---

Result

PASS

---

# 10. Manufacturing Review

Printer

Bambu A1 Mini

---

Material

PETG

---

Support Free Preferred

YES

---

Result

PASS

---

# 11. Maintenance Review

Replaceable

Servo

PASS

---

Bearing

PASS

---

Shaft

PASS

---

Carbon Tube

PASS

---

Result

APPROVED

---

# 12. Failure Mode Review

Servo Failure

Recoverable

---

Bearing Failure

Replaceable

---

Shaft Failure

Replaceable

---

Printed Part Failure

Reprintable

---

Result

APPROVED

---

# 13. Risk Assessment

| Risk              | Level  |
| ----------------- | ------ |
| Hip Roll          | Low    |
| Hip Pitch         | Medium |
| Knee              | Medium |
| Leg Structure     | Low    |
| Wheel Integration | Medium |

---

Overall Risk

MEDIUM

---

# 14. Freeze Decision

Single Leg Architecture

APPROVED

---

Status

FROZEN

---

Ready For

Dual Leg Integration

---

# 15. Exit Criteria

Kinematics Valid

PASS

---

Torque Valid

PASS

---

Weight Valid

PASS

---

Manufacturing Valid

PASS

---

Maintenance Valid

PASS

---

Status

LEG SUBSYSTEM APPROVED
