# Mini-Atlas V6 Alpha

# VAL-001 Mechanical Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER ALPHA

Document Number:

VAL-001

Release Name:

Mini-Atlas V6 Alpha Mechanical Validation

Parent Documents:

* MP-001 Manufacturing Package Release
* CDS-03 ~ CDS-09 Full Body Integration
* PR-002 Alpha Prototype Functional Validation
* PR-003 Beta Prototype Iteration

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 样机机械结构的可靠性、精度与运动性能。

目标：

* 验证所有关节间隙与装配精度
* 验证轴承与舵机安装质量
* 验证碳管接口与夹紧
* 验证结构承载能力
* 验证跌落与冲击耐受
* 验证重量和重心符合设计要求

---

# 2. Mechanical Validation Checklist

| Subsystem    | Test            | Criteria                               | Status  |
| ------------ | --------------- | -------------------------------------- | ------- |
| Hip Roll     | Range of Motion | ±0.1 mm clearance                      | Pending |
| Hip Pitch    | Range of Motion | Smooth, no binding                     | Pending |
| Knee         | Range of Motion | Smooth, no binding                     | Pending |
| Bearings     | Press-Fit       | Correct depth, no play                 | Pending |
| Carbon Tubes | Clamp Torque    | Hold without slippage                  | Pending |
| Pelvis       | Mounting        | Correct alignment                      | Pending |
| Leg Assembly | Weight          | ≤ 0.65 kg per leg                      | Pending |
| Full Robot   | Center of Mass  | Within ±5 mm X/Y/Z                     | Pending |
| Frame        | Static Load     | No permanent deformation at max torque | Pending |
| Robot        | Drop Test       | From 10 cm, no damage                  | Pending |

---

# 3. Test Procedures

## 3.1 Joint Motion Test

1. Move each joint through full range manually
2. Measure angular displacement & clearances
3. Confirm smooth operation

## 3.2 Bearing Fit Test

1. Verify axial / radial seating
2. Apply small torque, ensure no slippage

## 3.3 Carbon Tube Test

1. Clamp each tube
2. Apply bending load, measure deflection
3. Verify torque is maintained

## 3.4 Leg Weight & COM

1. Weigh individual leg assembly
2. Measure COM relative to Pelvis reference
3. Verify against design values

## 3.5 Structural Load Test

1. Apply max expected torque at Hip / Knee
2. Measure deflection
3. Inspect for cracks

## 3.6 Drop Test

1. Place robot on soft floor
2. Drop from 10 cm, multiple orientations
3. Inspect for mechanical damage

---

# 4. Reporting

* Document measured clearances
* Document torque applied & deflection
* Document mass & COM
* Capture photos of each test
* Record any anomalies

---

# 5. Freeze Summary

* Mechanical Validation Completed: Pending / APPROVED
* Issues Identified: List in VAL-001-Actions
* Status: READY FOR Electrical Validation (VAL-002)

---

# 6. Next Steps

* VAL-002 Electrical Validation
* VAL-003 Power System Validation
* VAL-004 Servo System Validation
* VAL-005 Gait Validation
* VAL-006 Safety System Validation
* VAL-007 Endurance Test
* VAL-008 Battery Life Test
* VAL-009 Beta Release Review
