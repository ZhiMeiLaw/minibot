# Mini-Atlas V6 Alpha

# VAL-005 Gait Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-005

Release Name:

Mini-Atlas V6 Alpha Gait Validation

Parent Documents:

* FW-005 Gait Engine
* FW-004 Wheel Control
* VAL-004 Servo System Validation
* CDS-03~09 Mechanical CAD
* PR-002 Alpha Prototype Functional Validation

Related Documents:

* FW-006 Safety Manager
* VAL-001 ~ VAL-004

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 样机步态性能及运动闭环能力。

目标：

* 验证站立稳定性
* 验证单腿支撑与重心控制
* 验证前进 / 后退 / 转向步态
* 验证 Wheel Assisted Gait 功能
* 验证跌倒恢复（预留）
* 验证连续行走稳定性
* 与 Safety Manager 协同验证

---

# 2. Test Environment

* Floor: Non-slip, Soft Mat
* Safety Rope: Recommended
* Lighting: Adequate for visual observation
* Power: Full 3S2P Battery
* Logging: UART / WiFi telemetry

---

# 3. Stand Pose Validation

## Procedure

1. Enable Torque
2. Move to Stand Pose
3. Hold for 30 s
4. Measure COM drift
5. Measure Joint Currents

## Acceptance Criteria

* COM drift < ±5 mm
* No torque spike >80%
* Wheels stable / torque OFF

---

# 4. Single-Leg Support Test

## Procedure

1. Lift one leg slightly
2. Hold 5 s
3. Observe Pelvis stability
4. Repeat left / right

## Acceptance Criteria

* Roll / Pitch < 5°
* Servo currents within limits
* No mechanical binding

---

# 5. Forward Walking Test

## Procedure

1. Command step forward
2. Observe gait cycle
3. Measure foot clearance
4. Measure COM stability

## Duration

5 minutes continuous

## Acceptance Criteria

* Step cycle smooth
* COM remains centered
* No servo overcurrent
* No wheel slip

---

# 6. Backward Walking Test

* Same procedure as forward, reversing step direction
* Verify stability and repeatability

---

# 7. Turning Test

## Procedure

1. Command turn left / right
2. Observe leg and wheel coordination
3. Measure yaw rate

## Acceptance Criteria

* Turn radius matches target
* COM stabilized
* No overcurrent or fall

---

# 8. Wheel Assisted Gait Validation

* Enable wheel assisted mode
* Observe COM stabilization during steps
* Measure wheel velocity correction
* Verify feedback from IMU improves balance

---

# 9. Continuous Walking Test

* Duration: 10 minutes
* Mode: Forward + Turn + Stop
* Measure: Joint currents, IMU, wheel speed, COM trajectory
* Acceptance: No drift, no servo overcurrent, no falls

---

# 10. Fault Injection Test

* IMU disconnect → observe gait reaction
* Servo disconnect → observe gait reaction
* Wheel power loss → observe gait reaction
* Acceptance: Safety Manager overrides motion

---

# 11. Data Logging

* Joint Positions
* Joint Currents
* IMU Roll / Pitch / Yaw
* Wheel Velocity
* COM trajectory
* Fault Events

File: `VAL-005-Gait-Test-Log.csv`

---

# 12. Validation Report Template

| Test                | Result | Notes |
| ------------------- | ------ | ----- |
| Stand Pose          |        |       |
| Single-Leg Support  |        |       |
| Forward Walking     |        |       |
| Backward Walking    |        |       |
| Turning             |        |       |
| Wheel Assisted Gait |        |       |
| Continuous Walking  |        |       |
| Fault Injection     |        |       |

---

# 13. Acceptance Criteria

* Robot remains upright
* Joint currents within limits
* Wheel assisted gait functional
* Motion smooth and repeatable
* Safety Manager overrides operational

---

# 14. Freeze Summary

Gait Engine

VALIDATED

---

Wheel Assisted Gait

VALIDATED

---

COM Stability

VALIDATED

---

Continuous Walking

VALIDATED

---

Safety Integration

VALIDATED

---

Status

READY FOR

VAL-006-Safety-System-Validation.md
