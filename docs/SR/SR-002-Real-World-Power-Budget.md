# Mini-Atlas V6

# SR-002 Real World Power Budget

Version: 1.0 Freeze A

Status: APPROVED AFTER VALIDATION

Document Number:

SR-002

Subsystem:

System Review

Release Stage:

Alpha → Beta Transition

Parent Documents:

* SR-001 System Weight Budget
* VAL-003 Power System Validation
* VAL-004 Servo System Validation
* VAL-005 Gait Validation
* VAL-007 Endurance Test
* VAL-008 Battery Life Test

---

# 1. Purpose

使用 Alpha 样机实测数据修正系统功耗模型。

目的：

* 修正理论功耗预算
* 建立真实功耗模型
* 修正续航预测
* 修正热设计
* 为 Beta 冻结提供依据

---

# 2. Why This Review Exists

项目初期采用的是理论估算：

```text
Servo Current Estimate
+
Wheel Current Estimate
+
Electronics Estimate
```

实际机器人中通常出现：

```text
理论值 ≠ 实测值
```

误差来源：

* 摩擦
* 装配误差
* 机械振动
* 步态控制
* 电池内阻
* 舵机效率

---

# 3. Original Design Budget

## Electronics

ESP32

200mA

---

IMU

10mA

---

Misc Logic

100mA

---

Subtotal

0.31A

---

## Wheels

GB37-520 ×2

Estimated

1.5A Average

---

Peak

4A

---

## Servos

STS3046 ×6

Estimated

0.7A Average

---

Peak

3A

---

Total Estimated

5.0A Average

---

# 4. Real Measurements

## Standby

Measured

_____ A

Design

0.30A

Difference

_____ %

---

## Standing

Measured

_____ A

Design

3.00A

Difference

_____ %

---

## Walking

Measured

_____ A

Design

5.00A

Difference

_____ %

---

## Peak

Measured

_____ A

Design

12.00A

Difference

_____ %

---

# 5. Power Distribution Analysis

## Logic Rail

Measured

_____ W

---

Percentage

_____ %

---

## Servo Rail

Measured

_____ W

---

Percentage

_____ %

---

## Wheel Rail

Measured

_____ W

---

Percentage

_____ %

---

Observation

Servo Rail expected to dominate.

---

# 6. Servo Energy Analysis

## Hip Roll

Average Current

---

---

Peak Current

---

---

## Hip Pitch

Average Current

---

---

Peak Current

---

---

## Knee

Average Current

---

---

Peak Current

---

---

Finding

Hip Pitch and Knee are expected to consume the majority of energy.

---

# 7. Wheel Energy Analysis

Measure:

Forward

Turn

Correction

---

Average Power

---

---

Peak Power

---

---

Efficiency Impact

---

---

# 8. Battery Utilization

Battery

3S2P Samsung 30Q

---

Nominal Energy

66.6 Wh

---

Measured Runtime

---

---

Measured Consumption

---

---

Utilization

____ %

---

# 9. Thermal Correlation

Compare:

Current

↓

Temperature

---

Servo Temperature

---

---

Buck Temperature

---

---

Battery Temperature

---

---

# 10. Runtime Prediction Model

## Standby

Measured Runtime

---

---

## Standing

Measured Runtime

---

---

## Walking

Measured Runtime

---

---

## Mixed Mission

Measured Runtime

---

---

# 11. Design Margin Analysis

Required Margin

20%

---

Measured Margin

---

---

Result

PASS / FAIL

---

# 12. Beta Recommendations

## Battery

Keep 3S2P

OR

Upgrade to 3S3P

---

Decision

---

---

## Servo

Keep STS3046

OR

Upgrade Select Joints

---

Decision

---

---

## Wheel Motor

Keep GB37-520

OR

Upgrade Gear Ratio

---

Decision

---

---

# 13. Updated System Budget

| Subsystem     | Design | Actual | Delta |
| ------------- | -----: | -----: | ----: |
| Logic         |        |        |       |
| Wheels        |        |        |       |
| Servos        |        |        |       |
| Total Average |        |        |       |
| Total Peak    |        |        |       |

---

# 14. Engineering Actions

Update:

EDS-02 Power Budget

---

Update:

EDS-04 Power Architecture

---

Update:

FW-006 Safety Thresholds

---

Update:

VAL-008 Runtime Targets

---

# 15. Acceptance Criteria

Measured Power Model

VALIDATED

---

Runtime Prediction

VALIDATED

---

Thermal Model

VALIDATED

---

Beta Decisions

APPROVED

---

# 16. Freeze Summary

Real Power Budget

FROZEN

---

Battery Sizing

FROZEN

---

Runtime Model

FROZEN

---

Thermal Model

FROZEN

---

Status

READY FOR

VAL-009-Beta-Release-Review.md
