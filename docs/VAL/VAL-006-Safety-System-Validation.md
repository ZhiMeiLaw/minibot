# Mini-Atlas V6 Alpha

# VAL-006 Safety System Validation

Version: 1.0 Freeze A

Status: DRAFT / APPROVED AFTER TEST

Document Number:

VAL-006

Release Name:

Mini-Atlas V6 Alpha Safety System Validation

Parent Documents:

* FW-006 Safety Manager
* VAL-004 Servo System Validation
* VAL-005 Gait Validation
* PR-002 Alpha Prototype Functional Validation

Related Documents:

* VAL-001 ~ VAL-005
* FW-008 Bring-Up Software

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 样机安全系统功能是否完整可靠。

目标：

* E-Stop 功能验证
* Servo / Motor Fault检测
* IMU异常检测
* Battery低电压 / 过流保护
* Wheel故障检测
* 整体安全策略闭环验证

---

# 2. Safety Validation Checklist

| Subsystem         | Test                       | Acceptance Criteria                | Status  |
| ----------------- | -------------------------- | ---------------------------------- | ------- |
| E-Stop            | Physical button press      | Immediate torque OFF, PWM=0, FAULT | Pending |
| Servo Bus         | Disconnect / stall         | Motion override, FAULT reported    | Pending |
| IMU               | Disconnect / fail          | Motion stop, FAULT triggered       | Pending |
| Battery           | Undervoltage / overcurrent | Motion stop, alarm                 | Pending |
| Wheel             | Disconnect / overload      | Motion stop, FAULT reported        | Pending |
| Watchdog          | Task stall                 | System reset, proper recovery      | Pending |
| Fault Propagation | Inject multiple faults     | All overrides effective            | Pending |

---

# 3. Test Procedures

## 3.1 Emergency Stop

1. Press E-Stop button
2. Verify servo torque OFF
3. Verify wheel PWM=0
4. Check FAULT state
5. Release button, verify controlled restart

---

## 3.2 Servo Fault Test

1. Simulate STS3046 disconnect
2. Verify Safety Manager stops motion
3. Verify FAULT logged
4. Verify recovery after reconnect

---

## 3.3 IMU Fault Test

1. Simulate I2C failure / power down
2. Verify motion stop
3. Verify FAULT reported
4. Confirm wheel stabilization if possible

---

## 3.4 Battery Fault Test

1. Reduce voltage to <9.5V
2. Observe Safety Manager reaction
3. Confirm torque OFF
4. Verify system logs event

---

## 3.5 Wheel Fault Test

1. Disconnect GB37-520
2. Command walking motion
3. Confirm motion stopped / FAULT logged

---

## 3.6 Watchdog Validation

1. Stall critical task
2. Confirm hardware + software watchdog triggers
3. System reset occurs
4. Controlled recovery

---

# 4. Integration Verification

* Safety Manager overrides Gait Engine
* Motion Layer cannot move robot when FAULT active
* Logs capture all events
* COM stability maintained when faults simulated during walking

---

# 5. Duration / Load

* Continuous operation: 60 minutes
* Randomly inject faults
* Measure reaction time <100ms
* Verify no damage to mechanical or electrical components

---

# 6. Data Logging

* Event Type
* Timestamp
* Subsystem
* Action Taken
* Recovery Status

---

# 7. Validation Report Template

| Test              | Result | Notes |
| ----------------- | ------ | ----- |
| E-Stop            |        |       |
| Servo Fault       |        |       |
| IMU Fault         |        |       |
| Battery Fault     |        |       |
| Wheel Fault       |        |       |
| Watchdog          |        |       |
| Fault Propagation |        |       |

---

# 8. Acceptance Criteria

* All faults trigger immediate safe stop
* FAULT states correctly logged
* Recovery procedures functional
* No mechanical damage
* No servo / wheel overheating

---

# 9. Freeze Summary

Safety Manager

VALIDATED

---

Fault Detection

VALIDATED

---

E-Stop

VALIDATED

---

Battery Protection

VALIDATED

---

System Recovery

VALIDATED

---

Status

READY FOR

VAL-007-Endurance-Test.md
