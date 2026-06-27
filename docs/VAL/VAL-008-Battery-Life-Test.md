# Mini-Atlas V6 Alpha

# VAL-008 Battery Life Test

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-008

Release Name:

Mini-Atlas V6 Alpha Battery Life Test

Parent Documents:

* SR-001 System Weight Budget
* VAL-003 Power System Validation
* VAL-007 Endurance Test
* FW-006 Safety Manager

Related Documents:

* BOM-01 Master Bill of Materials
* PR-003 Beta Prototype Iteration

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 实际续航能力。

目标：

* 测量真实续航时间
* 测量平均功耗
* 测量峰值功耗
* 验证电池温升
* 验证低电压保护
* 验证剩余电量估算模型

---

# 2. Battery Configuration

Battery Pack

Samsung 30Q

---

Configuration

3S2P

---

Nominal Voltage

11.1V

---

Full Charge

12.6V

---

Cutoff Voltage

9.0V

---

Nominal Capacity

3000mAh

---

Nominal Energy

33.3Wh

---

> **ECO-002 变更**：电池容量由 6000mAh/66.6Wh 修正为 3000mAh/33.3Wh。

Status

FROZEN

---

# 3. Test Equipment

Required

* DC Power Analyzer
* Battery Capacity Meter
* Thermal Camera
* USB Logger
* Digital Multimeter

---

Optional

* Electronic Load
* Data Acquisition System

---

# 4. Test Scenarios

## Scenario A

Sleep Mode

---

Robot ON

Torque OFF

WiFi OFF

---

Purpose

Measure standby consumption

---

## Scenario B

Idle Mode

---

Torque OFF

Sensors Active

WiFi Active

---

Purpose

Measure electronics consumption

---

## Scenario C

Standing Mode

---

Stand Pose

Torque ON

---

Purpose

Measure static holding consumption

---

## Scenario D

Walking Mode

---

Continuous Walking

---

Purpose

Measure locomotion consumption

---

## Scenario E

Mixed Mission

---

Stand

Walk

Turn

Stop

Repeat

---

Purpose

Simulate real usage

---

# 5. Data Collection

Record:

Battery Voltage

---

Battery Current

---

Battery Temperature

---

Servo Current

---

Wheel Current

---

Runtime

---

Sampling Interval

1 Second

---

# 6. Standby Runtime Test

Expected Current

100~300mA

---

Expected Runtime

20+ Hours

---

Acceptance

> 15 Hours

---

# 7. Idle Runtime Test

Expected Current

300~500mA

---

Expected Runtime

10+ Hours

---

Acceptance

> 8 Hours

---

# 8. Standing Runtime Test

Expected Current

2~4A

---

Expected Runtime

90~180 Minutes

---

Acceptance

> 60 Minutes

---

# 9. Walking Runtime Test

Expected Average Current

4~7A

---

Expected Runtime

45~90 Minutes

---

Acceptance

> 45 Minutes

---

# 10. Mixed Mission Test

Mission Profile

30% Standing

50% Walking

20% Turning

---

Target Runtime

60~120 Minutes

---

Acceptance

> 60 Minutes

---

# 11. Peak Current Analysis

Measure:

Maximum Current

---

Voltage Sag

---

Acceptance

Battery Voltage

> 9.5V

---

No ESP32 Reset

---

No Servo Dropout

---

# 12. Thermal Validation

Battery Surface

---

Maximum

60°C

---

Preferred

<50°C

---

Acceptance

No Thermal Runaway

---

# 13. State-of-Charge Model

Record:

Voltage

↓

Capacity

↓

Runtime

---

Build:

SOC Lookup Table

---

Purpose

Future Battery Gauge

---

# 14. Low Battery Validation

Trigger

10.0V Warning

---

Verify

User Alert

---

Trigger

9.5V Fault

---

Verify

Safety Manager Stop Motion

---

Trigger

9.0V Cutoff

---

Verify

Controlled Shutdown

---

# 15. Aging Projection

Calculate:

100 Cycles

---

300 Cycles

---

500 Cycles

---

Estimate:

Runtime Degradation

---

# 16. Data Files

Store:

```text
VAL-008-Battery-Life-Test.csv
```

---

Store:

```text
VAL-008-SOC-Model.xlsx
```

---

# 17. Validation Report

| Test          | Runtime | Result |
| ------------- | ------: | ------ |
| Sleep         |         |        |
| Idle          |         |        |
| Standing      |         |        |
| Walking       |         |        |
| Mixed Mission |         |        |
| Thermal       |         |        |
| Low Battery   |         |        |

---

# 18. Acceptance Criteria

Battery Runtime

PASS

---

Thermal

PASS

---

Voltage Stability

PASS

---

SOC Model

PASS

---

Safety Manager

PASS

---

# 19. Engineering Outputs

Update:

SR-002 Real World Power Budget

---

Update:

FW-006 Battery Thresholds

---

Update:

EDS-04 Power Architecture

---

# 20. Freeze Summary

Battery Runtime

VALIDATED

---

Power Budget

VALIDATED

---

SOC Model

VALIDATED

---

Low Voltage Protection

VALIDATED

---

Status

READY FOR

VAL-009-Beta-Release-Review.md
