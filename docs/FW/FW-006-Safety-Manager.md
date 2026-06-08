# Mini-Atlas V6 Alpha

# FW-006 Safety Manager

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-006

Subsystem:

Firmware – Safety Manager

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* FW-002 Servo Bus Driver
* FW-003 IMU Driver
* FW-004 Wheel Control
* FW-005 Gait Engine
* PR-001 Alpha Prototype Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的安全管理层（Safety Manager）架构。

目标：

* 监控舵机、IMU、轮子、电池
* 处理 E-Stop
* 防止过流 / 过热 / 姿态异常
* 与 Motion / Gait / Wheel Engine 集成
* 确保 Alpha 样机运行安全

---

# 2. Safety Architecture

## Layers

* Hardware Monitoring
* Sensor Monitoring (IMU, Voltage)
* Servo & Motor Monitoring
* Motion / Gait Overrides
* Emergency Stop Handling

---

# 3. Safety Task Architecture

| Task                            | Priority | Period |
| ------------------------------- | -------: | -----: |
| Servo Timeout Check             |       10 |  10 ms |
| IMU Data Check                  |        9 |  10 ms |
| Battery Voltage / Current Check |        8 |  20 ms |
| Wheel / Motor Health            |        8 |  10 ms |
| Safety Decision                 |       10 |  10 ms |

---

# 4. Emergency Stop

Trigger Conditions:

* Physical E-Stop Button Pressed
* Servo Bus Lost / Timeout
* Battery Critical (V < 9.5V)
* IMU Failure
* Watchdog Timeout

Action:

* Disable All Servo Torque
* Stop Wheels
* Motion Layer → FAULT
* Report Status via UART

Status

FROZEN

---

# 5. Servo Monitoring

* Monitor Bus Heartbeat
* Detect Lost or Stalled Servos
* Current Threshold: 2A / Servo Continuous, 5A Peak
* Overcurrent → Disable Servo → FAULT

---

# 6. IMU Monitoring

* Check Data Freshness (Timeout 50 ms)
* Check Roll / Pitch Thresholds (>45° sustained 500 ms → FAULT)
* IMU Fail → Freeze Motion, Stabilize via Wheel

---

# 7. Battery Monitoring

* Voltage Check: Vmin=9.5V
* Voltage Warning: 10.5V
* Current Check: ≤ Max Rated
* Low Battery → FAULT / Shutdown

---

# 8. Wheel / Motor Monitoring

* Monitor Current Draw
* Monitor Temperature (Motor / Driver)
* Fault → Stop PWM, notify Motion Layer

---

# 9. Fault Handling

* FAULT Mode → All Motion Stops
* Maintain Power to Electronics
* Log Fault Event
* Require Reset or E-Stop Release

---

# 10. Safety Overrides

* Gait Engine / Motion Layer always query Safety Manager
* Safety Manager can override any motion
* Real-time priority: Safety > Motion

---

# 11. Watchdog Integration

* Hardware Watchdog Enabled
* Software Watchdog Monitors Safety Task
* Timeout → System Reset → Re-initialize Safety

---

# 12. Bring-Up Procedure

1. Initialize Safety Manager
2. Verify Servo Bus Alive
3. Verify IMU Data
4. Verify Battery Voltage / Current
5. Enable Motion Layer
6. Verify E-Stop Function
7. Verify Fault Propagation

Pass Criteria:

* All Safety Conditions Active
* Emergency Stop Functional
* Fault Propagation Verified

---

# 13. Freeze Summary

Safety Manager

* Monitored Systems: Servo, IMU, Wheel, Battery
* E-Stop Handling: Enabled
* Fault Detection: Enabled
* Watchdog: Hardware + Software
* Safety Override: Motion Layer
* Status: APPROVED
* READY FOR: FW-007-OTA-Framework.md
