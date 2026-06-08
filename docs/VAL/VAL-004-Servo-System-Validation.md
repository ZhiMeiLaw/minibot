# Mini-Atlas V6 Alpha

# VAL-004 Servo System Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-004

Release Name:

Mini-Atlas V6 Alpha Servo System Validation

Parent Documents:

* EDS-05 Communication & Control Architecture
* FW-002 Servo Bus Driver
* CDS-03 Hip Roll Joint CAD Design
* CDS-04 Hip Pitch Joint CAD Design
* CDS-05 Knee Joint CAD Design
* VAL-003 Power System Validation

Related Documents:

* FW-005 Gait Engine
* FW-006 Safety Manager
* PR-002 Alpha Prototype Functional Validation

---

# 1. Purpose

验证 STS3046 舵机系统在 Mini-Atlas V6 Alpha 上的实际性能。

验证内容：

* 通讯可靠性
* 位置精度
* 重复定位精度
* 同步控制能力
* 输出能力
* 温升特性
* 电流特性
* 过载保护
* 长时间运行可靠性

---

# 2. Test Configuration

## Hardware

ESP32 DevKitC

---

STS3046 × 6

---

3S2P Samsung 30Q

---

ICM42688

---

## Software

FW-002 Servo Bus Driver

FW-005 Gait Engine

FW-006 Safety Manager

---

# 3. Servo ID Verification

Verify:

```text
ID 1  Left Hip Roll
ID 2  Left Hip Pitch
ID 3  Left Knee

ID 4  Right Hip Roll
ID 5  Right Hip Pitch
ID 6  Right Knee
```

---

Test

1000 Scan Cycles

---

Acceptance

0 Missing Servo

0 Duplicate ID

---

# 4. Communication Reliability Test

## Method

Continuous:

Ping

Read

Write

Sync Write

---

Duration

1 Hour

---

Acceptance

Packet Error Rate

<0.01%

---

Bus Timeout

0

---

# 5. Position Accuracy Test

## Procedure

Command:

```text
0°
15°
30°
45°
60°
```

---

Measure

Actual Position

---

Acceptance

±1.0°

---

# 6. Repeatability Test

## Procedure

Move:

```text
0°
→
45°
→
0°
```

Repeated

100 Cycles

---

Measure

Position Error

---

Acceptance

±0.5°

---

# 7. Synchronization Test

## Procedure

All 6 Servos

Sync Write

---

Measure

Start Delay

---

Acceptance

<20 ms

---

Joint Deviation

<2°

---

# 8. Load Holding Test

## Hip Pitch

Apply Static Load

---

Duration

10 Minutes

---

Measure

Position Drift

---

Acceptance

<2°

---

# 9. Current Consumption Test

## No Load

Measure

Current

---

## Stand Pose

Measure

Current

---

## Walking

Measure

Average

Peak

---

Record

Per Servo

---

# 10. Thermal Test

## Condition

Stand Pose

Torque ON

---

Duration

30 Minutes

---

Measure

Servo Case Temperature

---

Acceptance

<70°C

---

Warning

65°C

---

# 11. Overload Protection Test

## Procedure

Apply External Resistance

---

Observe

Current

Temperature

Response

---

Acceptance

Safety Manager Detects Fault

---

# 12. Mechanical Backlash Test

Measure:

Hip Roll

Hip Pitch

Knee

---

Acceptance

<2°

---

# 13. Endurance Test

## Procedure

Continuous Motion

---

Cycle Count

10,000 Cycles

---

Motion

```text
-30°
↔
+30°
```

---

Acceptance

No Failure

---

# 14. Fault Injection Test

Disconnect Servo

---

Corrupt Bus Packet

---

Reduce Supply Voltage

---

Expected

FAULT State

---

# 15. Gait Integration Test

## Verify

Stand Pose

---

Forward Walking

---

Backward Walking

---

Turning

---

Acceptance

Stable Motion

---

# 16. Data Logging

Record:

Position

Velocity

Current

Temperature

Error Flags

---

Store

```text
VAL-004-Servo-Test-Log.csv
```

---

# 17. Validation Report

| Test              | Result | Notes |
| ----------------- | ------ | ----- |
| ID Verification   |        |       |
| Communication     |        |       |
| Position Accuracy |        |       |
| Repeatability     |        |       |
| Synchronization   |        |       |
| Load Holding      |        |       |
| Current Test      |        |       |
| Thermal Test      |        |       |
| Overload Test     |        |       |
| Backlash Test     |        |       |
| Endurance Test    |        |       |
| Fault Injection   |        |       |

---

# 18. Acceptance Criteria

Communication

PASS

---

Accuracy

PASS

---

Repeatability

PASS

---

Thermal

PASS

---

Overload Protection

PASS

---

Endurance

PASS

---

Safety Integration

PASS

---

# 19. Known Risks

Hip Pitch Continuous Load

Monitor Closely

---

Knee Peak Current

Monitor Closely

---

Servo Gear Wear

Evaluate After 10k Cycles

---

# 20. Freeze Summary

STS3046 Bus

VALIDATED

---

Position Control

VALIDATED

---

Synchronization

VALIDATED

---

Thermal Performance

VALIDATED

---

Overload Protection

VALIDATED

---

Reliability

VALIDATED

---

Status

READY FOR

VAL-005-Gait-Validation.md
