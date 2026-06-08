# Mini-Atlas V6 Alpha

# DR-005 Servo Capability Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-005

Subsystem:

Actuator Capability Assessment

Parent Documents:

* DR-002 Actuator Selection Review
* DR-004 Hip Architecture Review
* SR-001 System Weight Budget

Related Documents:

* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* VAL-004 Servo System Validation

---

# 1. Purpose

评审 STS3046 是否能够满足 Mini-Atlas V6 Alpha 全部关节需求。

目标：

* 验证静态扭矩能力
* 验证动态扭矩能力
* 验证速度能力
* 验证热能力
* 验证寿命风险

---

# 2. Selected Servo

Model

STS3046

---

Supply Voltage

7.4V

---

Communication

UART Bus

---

Weight

≈80g

---

Rated Torque

≈4.5Nm

---

Status

FROZEN

---

# 3. Robot Assumptions

Robot Height

55cm

---

Target Weight

4.0kg

---

Maximum Weight

5.0kg

---

Leg Count

2

---

DOF

6

---

# 4. Hip Roll Analysis

Function

COM Shift

Lateral Balance

---

Estimated Load

Low

---

Required Torque

≈3.0Nm

---

Available Torque

4.5Nm

---

Margin

50%

---

Result

PASS

---

# 5. Hip Pitch Analysis

Function

Forward Motion

Weight Support

---

Required Torque

≈4.0Nm

---

Available Torque

4.5Nm

---

Margin

12.5%

---

Result

PASS

---

# 6. Knee Analysis

Function

Leg Support

Shock Absorption

---

Required Torque

≈4.0Nm

---

Available Torque

4.5Nm

---

Margin

12.5%

---

Result

PASS

---

# 7. Dynamic Walking Analysis

Walking introduces:

* Inertia
* Acceleration
* Impact

---

Estimated Dynamic Multiplier

1.2~1.5

---

Mitigation

Wheel Assisted Gait

---

Result

ACCEPTABLE

---

# 8. Thermal Analysis

Expected Temperature

40~60°C

---

Maximum Allowed

70°C

---

Thermal Validation

VAL-004

---

Result

PASS

---

# 9. Gear Wear Analysis

Potential Failure Modes

* Gear Wear
* Output Shaft Play
* Bearing Fatigue

---

Mitigation

* Dual Bearing Architecture
* Torque Transfer Module
* Mechanical Stops

---

Result

ACCEPTABLE

---

# 10. Power Consumption Analysis

Average Current

0.5~0.8A

---

Peak Current

1.0~1.5A

---

6 Servo Peak

6~9A

---

Supported By

3S2P Battery

---

Result

PASS

---

# 11. Upgrade Path Evaluation

Option A

Keep STS3046

---

Option B

Hip Pitch → STS3215

---

Option C

Hip Pitch + Knee → STS3250

---

Evaluation

Alpha:

Not Required

---

Beta:

Re-evaluate After Testing

---

# 12. Manufacturing Impact

Using One Servo Type:

Advantages

* Single Spare Part
* Single Firmware Driver
* Single BOM Item
* Lower Cost

---

Result

STRONGLY RECOMMENDED

---

# 13. Cost Analysis

STS3046 × 6

---

Estimated Cost

Lowest Among Candidates

---

Replacement Cost

Acceptable

---

Result

PASS

---

# 14. Validation Requirements

Must Pass:

* VAL-004 Servo Validation
* VAL-005 Gait Validation
* VAL-007 Endurance Test

---

If Failed:

Re-open DR-005

---

# 15. Engineering Decision

Hip Roll

STS3046

APPROVED

---

Hip Pitch

STS3046

APPROVED

---

Knee

STS3046

APPROVED

---

# 16. Freeze Summary

Actuator Type

STS3046

---

Quantity

6

---

Bus

UART

---

Voltage

7.4V

---

Upgrade Required

NO

---

Status

APPROVED

---

Next Document

DR-006-Bearing-and-Shaft-Review.md
