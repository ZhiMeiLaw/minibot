# Mini-Atlas V6 Alpha

# FW-008 Bring-Up Software

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-008

Subsystem:

Firmware – Bring-Up Software

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* FW-002 Servo Bus Driver
* FW-003 IMU Driver
* FW-004 Wheel Control
* FW-005 Gait Engine
* FW-006 Safety Manager
* FW-007 OTA Framework
* PR-001 Alpha Prototype Release
* MP-001 Manufacturing Package Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 样机软件完整启动流程（Bring-Up）。

目标：

* 确保所有固件模块正确初始化
* 验证通信总线
* 验证舵机、IMU、轮子
* 执行站立与轮辅助步态闭环测试
* 验证安全管理功能

---

# 2. Bring-Up Architecture

流程：

1. Power-On
2. Board & Peripheral Init
3. Servo Bus Scan
4. IMU Init & Calibration
5. Wheel Controller Init
6. Safety Manager Init
7. Gait Engine Init
8. Motion Layer Start
9. Stand-Up Test
10. Wheel Assisted Gait Test
11. Fault Injection Test

---

# 3. Pre-Bring-Up Checks

* Battery fully charged
* All servos connected (IDs 1~6)
* IMU mounted and oriented
* Wheels installed and free to rotate
* Emergency Stop functional

---

# 4. Bring-Up Task Sequence

| Step | Task                  | Status  |
| ---- | --------------------- | ------- |
| 1    | Board Init            | Pending |
| 2    | UART / I2C Init       | Pending |
| 3    | Servo Scan            | Pending |
| 4    | IMU Calibration       | Pending |
| 5    | Wheel Controller Test | Pending |
| 6    | Safety Manager Test   | Pending |
| 7    | Motion Layer Enable   | Pending |
| 8    | Stand Pose            | Pending |
| 9    | Wheel Assisted Gait   | Pending |
| 10   | Fault Injection       | Pending |

---

# 5. Servo Verification

* Scan all servo IDs
* Verify Range & Direction
* Torque test: ≤80% rated
* Safety overrides functional

---

# 6. IMU Verification

* Raw Data Check
* Attitude Calculation
* Roll / Pitch / Yaw within expected range
* Fall Detection Functional

---

# 7. Wheel Verification

* Forward / Reverse / Stop
* Velocity control loop stable
* Differential drive functioning
* Wheel Assisted Gait stabilization

---

# 8. Safety Manager Verification

* Emergency Stop functional
* Overcurrent detection functional
* Servo timeout detection functional
* IMU failure detection functional
* Battery undervoltage detection functional

---

# 9. First Stand Procedure

Environment:

* Soft Floor
* Safety Rope Recommended

Steps:

1. Enable Servo Torque
2. Move to Stand Pose
3. Hold 10 s
4. Observe IMU Roll/Pitch
5. Observe Servo Currents
6. Observe Wheels Behavior

Pass Criteria:

* No fall
* No overcurrent
* No alarms

---

# 10. Logging & Debug

* UART Console Enabled
* Log Servo Scan, IMU Data, Wheel State
* OTA Status Logged
* Faults Timestamped

---

# 11. Bring-Up Safety Notes

* Use Safety Rope for first standing test
* Verify all cable connections
* Monitor currents
* Limit motion during initial test

---

# 12. Freeze Summary

* Power-On Sequence: FROZEN
* Servo Bus Scan: FROZEN
* IMU Calibration: FROZEN
* Wheel Control Init: FROZEN
* Gait Engine: FROZEN
* Safety Manager: FROZEN
* Stand-Up Test: FROZEN
* Wheel Assisted Gait Test: FROZEN
* Fault Injection Test: FROZEN
* Status: APPROVED
* READY FOR: Alpha Prototype Functional Validation
