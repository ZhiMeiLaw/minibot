# Mini-Atlas V6 Alpha

# VAL-002 Electrical Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER ALPHA

Document Number:

VAL-002

Release Name:

Mini-Atlas V6 Alpha Electrical Validation

Parent Documents:

* EDS-04 Power Hardware Selection
* EDS-05 Communication & Control Architecture
* MP-001 Manufacturing Package Release
* FW-001 Firmware Architecture
* VAL-001 Mechanical Validation

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 电气系统设计是否满足要求。

验证范围：

* 电池系统
* PDB配电板
* Buck电源模块
* ESP32主控
* STS3046总线
* ICM42688
* Wheel Driver
* 线束系统
* E-Stop系统

---

# 2. Validation Objectives

确认：

* 电源连接正确
* 无短路
* 电压稳定
* 电流正常
* 通讯可靠
* EMI可接受
* 安全机制正常

---

# 3. Electrical Architecture Under Test

```text
Battery
   ↓
Main Fuse
   ↓
Power Switch
   ↓
PDB
   ├── 7.4V Servo Rail
   ├── 5V Logic Rail
   └── Wheel Driver Rail

ESP32
   ├── Servo Bus
   ├── IMU
   └── OTA/WiFi
```

---

# 4. Pre-Power Inspection

## Visual Inspection

检查：

* 极性正确
* 焊点完整
* 无虚焊
* 无裸露导体
* 无压伤线束

---

## Continuity Test

使用万用表验证：

* VBAT → GND 无短路
* 7.4V → GND 无短路
* 5V → GND 无短路

---

Pass Criteria

> 任何电源轨均不得短路

---

# 5. Power Rail Verification

## Battery Rail

Nominal

11.1V

---

Expected

10.5~12.6V

---

## Servo Rail

7.4V Buck

---

Expected

7.3~7.5V

---

Load Test

3A

---

## Logic Rail

5V Buck

---

Expected

4.9~5.1V

---

Load Test

1A

---

# 6. Power-On Current Validation

## Idle Current

Robot Standing

Torque OFF

---

Target

<300mA

---

## Logic Only

ESP32

IMU

WiFi

---

Target

<200mA

---

## Full System

Torque ON

---

Target

<2A

---

# 7. Servo Bus Validation

Verify:

* UART RX
* UART TX
* Direction Control

---

Servo IDs

1~6

---

Tests

Ping

Read

Write

Sync Write

---

Pass Criteria

1000 Cycles

0 Errors

---

# 8. IMU Validation

Verify:

ICM42688

WHO_AM_I

---

Verify

200Hz Sampling

---

Verify

No I2C Errors

---

Pass Criteria

1 Hour Continuous

0 Errors

---

# 9. Wheel Driver Validation

Verify

PWM Output

---

Verify

Forward

Reverse

Brake

---

Verify

No Driver Overheat

---

Pass Criteria

30 Minutes Continuous

---

# 10. E-Stop Validation

Trigger Methods

* Physical Switch
* Software Command

---

Expected Result

Servo Torque OFF

Wheel PWM = 0

FAULT State

---

Reaction Time

<100ms

---

# 11. Watchdog Validation

Inject:

Task Stall

---

Expected

Watchdog Reset

---

Boot Recovery

Successful

---

# 12. Noise & EMI Validation

Monitor:

Servo Rail Ripple

---

Monitor:

5V Rail Ripple

---

Monitor:

UART Error Count

---

Pass Criteria

No Communication Loss

---

# 13. Thermal Validation

Components

* Buck Converter
* Wheel Driver
* PDB
* Main Switch

---

Test Duration

30 Minutes

---

Max Temperature

70°C

---

# 14. Wiring Harness Validation

Verify:

* Connector Retention
* Wire Strain Relief
* Flex Routing

---

Test

100 Motion Cycles

---

Pass Criteria

No Wire Damage

---

# 15. Fault Injection Tests

Inject:

Servo Disconnect

---

Inject:

IMU Disconnect

---

Inject:

Battery Undervoltage

---

Inject:

Wheel Driver Failure

---

Expected

Safety Manager FAULT

---

# 16. Electrical Validation Report

记录：

* 电压
* 电流
* 温度
* 通讯错误数
* Fault日志

---

保存：

```text
VAL-002-Test-Report.xlsx
```

---

# 17. Acceptance Criteria

Battery System

PASS

---

Power Rails

PASS

---

Servo Bus

PASS

---

IMU

PASS

---

Wheel Driver

PASS

---

E-Stop

PASS

---

Watchdog

PASS

---

Harness

PASS

---

# 18. Freeze Summary

Electrical Architecture

VALIDATED

---

Power Distribution

VALIDATED

---

Communication

VALIDATED

---

Safety Functions

VALIDATED

---

Status

READY FOR

VAL-003-Power-System-Validation.md
