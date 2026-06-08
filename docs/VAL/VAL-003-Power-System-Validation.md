# Mini-Atlas V6 Alpha

# VAL-003 Power System Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-003

Release Name:

Mini-Atlas V6 Alpha Power System Validation

Parent Documents:

* EDS-02 Power Budget and Current Analysis
* EDS-04 Power Hardware Selection
* BOM-01 Master Bill of Materials
* VAL-002 Electrical Validation

Related Documents:

* FW-006 Safety Manager
* FW-008 Bring-Up Software
* PR-002 Alpha Prototype Functional Validation

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 电源系统在真实工况下的性能与可靠性。

验证内容：

* 电池系统
* PDB配电系统
* Servo Rail
* Logic Rail
* Wheel Rail
* 电流预算
* 热性能
* 续航能力
* 保险丝保护

---

# 2. Validation Objectives

确认：

* 电源架构满足设计要求
* 电压稳定
* 电流容量充足
* 无异常压降
* 无异常发热
* 满足续航目标
* 安全保护有效

---

# 3. Test Equipment

## Required

数字万用表

---

DC钳形表

---

电子负载

---

热成像仪

---

USB串口日志工具

---

电池容量测试仪

---

# 4. Power Architecture Under Test

```text
3S2P Samsung 30Q
        ↓
     15A Fuse
        ↓
   Main Switch
        ↓
        PDB
   ┌────┼────┐
   │    │    │
7.4V  5V  Wheel Rail
Servo Logic Driver
```

---

# 5. Battery Validation

## Battery Pack

Configuration

3S2P

---

Nominal Voltage

11.1V

---

Full Charge

12.6V

---

Cutoff

9.0V

---

Measured Items

* Open Circuit Voltage
* Internal Resistance
* Capacity
* Temperature

---

Acceptance Criteria

Capacity

≥90%

Design Capacity

---

# 6. Idle Current Test

## Condition

Robot Powered

Torque OFF

WiFi OFF

---

Measure

Battery Current

---

Expected

150~300mA

---

Pass Criteria

<500mA

---

# 7. Logic Load Test

## Active

ESP32

IMU

UART

WiFi

---

Measure

5V Rail

---

Expected

<500mA

---

Voltage

4.9~5.1V

---

# 8. Servo Stand Test

## Condition

Stand Pose

Torque ON

---

Duration

60 Seconds

---

Measure

Battery Current

Servo Rail Voltage

Buck Temperature

---

Expected

2~5A

---

Pass Criteria

No Reset

No Voltage Collapse

---

# 9. Walking Current Test

## Mode

Forward Walking

---

Duration

5 Minutes

---

Measure

Average Current

Peak Current

Voltage Sag

---

Expected Average

3~6A

---

Expected Peak

<12A

---

Pass Criteria

No Brownout

---

# 10. Peak Load Test

## Procedure

Command:

Maximum Step

Maximum Acceleration

---

Capture

Current Peak

Voltage Dip

---

Acceptance

Battery Voltage

> 9.5V

---

Servo Rail

> 7.0V

---

Logic Rail

> 4.8V

---

# 11. Buck Converter Thermal Test

## Servo Buck

Load

5A Continuous

---

Duration

30 Minutes

---

Temperature Limit

80°C

---

## Logic Buck

Load

1A Continuous

---

Temperature Limit

70°C

---

# 12. Fuse Validation

## Fuse

15A Automotive Blade

---

Test

Short Duration Overload

---

Expected

Fuse Opens

Before Harness Damage

---

Verification

Harness Intact

---

# 13. Voltage Drop Analysis

Measure

Battery

↓

PDB

↓

Buck Input

↓

Buck Output

↓

Load

---

Acceptance

Total Drop

<0.5V

---

# 14. Runtime Validation

## Scenario A

Standby

---

Expected

> 10 Hours

---

## Scenario B

Standing

---

Expected

> 2 Hours

---

## Scenario C

Walking

---

Expected

> 60 Minutes

---

## Scenario D

Mixed Mission

---

Expected

> 90 Minutes

---

# 15. Brownout Validation

## Simulate

Low Battery

---

Verify

ESP32 Stable

---

Verify

Safety Manager Trigger

---

Threshold

10.0V Warning

9.5V Fault

---

# 16. Recovery Validation

## Battery Replace

↓

Power Cycle

↓

Bring-Up

---

Expected

Normal Startup

---

No Configuration Loss

---

# 17. Data Logging

Record

Battery Voltage

---

Battery Current

---

Servo Rail Voltage

---

Logic Rail Voltage

---

Temperature

---

Runtime

---

Store As

```text
VAL-003-Power-Test-Log.csv
```

---

# 18. Validation Report Template

| Test             | Result | Notes |
| ---------------- | ------ | ----- |
| Battery Capacity |        |       |
| Idle Current     |        |       |
| Logic Current    |        |       |
| Standing Current |        |       |
| Walking Current  |        |       |
| Peak Current     |        |       |
| Buck Thermal     |        |       |
| Fuse Test        |        |       |
| Runtime Test     |        |       |
| Brownout Test    |        |       |

---

# 19. Acceptance Criteria

Battery

PASS

---

Servo Rail

PASS

---

Logic Rail

PASS

---

Thermal

PASS

---

Fuse

PASS

---

Runtime

PASS

---

Safety Response

PASS

---

# 20. Freeze Summary

Battery Pack

VALIDATED

---

Power Budget

VALIDATED

---

Buck Converters

VALIDATED

---

Fuse Protection

VALIDATED

---

Runtime Estimate

VALIDATED

---

Status

READY FOR

VAL-004-Servo-System-Validation.md
