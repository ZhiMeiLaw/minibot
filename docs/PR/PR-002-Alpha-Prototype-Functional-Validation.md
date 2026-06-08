# Mini-Atlas V6 Alpha

# PR-002 Alpha Prototype Functional Validation

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

PR-002

Release Name:

Mini-Atlas V6 Alpha Functional Validation

Parent Documents:

* PR-001 Alpha Prototype Release
* MP-001 Manufacturing Package Release
* FW-008 Bring-Up Software

Related Documents:

* CDS-09 Full Body Integration
* FW-005 Gait Engine
* FW-006 Safety Manager

---

# 1. Purpose

验证 Mini-Atlas V6 Alpha 样机的功能性能。

目标：

* 验证机械装配正确性
* 验证舵机与总线功能
* 验证 IMU 数据采集与姿态解算
* 验证轮子与差速驱动
* 验证步态闭环
* 验证安全管理功能
* 验证 Bring-Up 流程是否可复现

---

# 2. Validation Environment

* Floor: Soft / Non-slip surface
* Safety Rope: Recommended
* Voltage Supply: Full Battery (3S2P Samsung 30Q)
* Temperature: 20~25°C
* Observation: Continuous Logging via UART

---

# 3. Functional Validation Checklist

## Mechanical Assembly

* [ ] All joints assembled per CAD
* [ ] Bearings properly seated
* [ ] Carbon tubes clamped
* [ ] Heat-set inserts installed

---

## Servo Bus

* [ ] Servo IDs 1~6 detected
* [ ] Torque limits within range
* [ ] Sync Write functional
* [ ] Readback accurate

---

## IMU Functionality

* [ ] Roll / Pitch / Yaw correct
* [ ] Sampling rate 200 Hz
* [ ] Calibration correct
* [ ] Fall detection functional

---

## Wheel Control

* [ ] Forward / Backward / Stop
* [ ] Differential drive correct
* [ ] Velocity PID stable
* [ ] Wheel Assisted Gait operational

---

## Gait Engine

* [ ] Stand Pose correct
* [ ] Step Forward / Backward executed
* [ ] Turning executed
* [ ] COM stabilization functional
* [ ] Safety overrides respected

---

## Safety Manager

* [ ] E-Stop functional
* [ ] Servo timeout detection
* [ ] IMU failure detection
* [ ] Low battery detection
* [ ] Fault propagation verified

---

# 4. Power & Electrical Validation

* Battery voltage stable
* 7.4V Buck for servo rail stable
* 5V logic rail stable
* Peak currents within limits
* No overheat detected

---

# 5. Logging & Telemetry

* All events timestamped
* Servo commands logged
* IMU / Wheel feedback logged
* Fault events logged
* Bring-Up flow logs verified

---

# 6. Test Procedure

1. Pre-Check: Visual inspection
2. Power-On: Verify all rails
3. Servo Scan: Verify IDs & Torque
4. IMU Calibration: Verify orientation
5. Wheel Test: Forward / Reverse / Stop
6. Stand Pose: Hold 10 s
7. Step Forward / Backward: Observe stability
8. Turn Left / Right: Observe COM balance
9. Emergency Stop Test: Trigger E-Stop
10. Fault Injection: Disconnect IMU / Servo
11. Data Logging: Confirm logs correct

---

# 7. Pass Criteria

* All subsystems operational
* No mechanical binding or collision
* Servo bus fully functional
* IMU reporting accurate
* Wheel control stable
* Gait executed with COM balance
* Safety Manager overrides functional
* Robot remains upright during tests
* No overcurrent or thermal fault

---

# 8. Known Issues

* Minor servo torque fluctuation at low speeds
* Wheel assisted gait requires fine-tuning PID
* IMU bias may drift after prolonged operation
* Firmware logging to UART may saturate at high frequency

---

# 9. Validation Summary Table

| Subsystem           | Status | Notes                              |
| ------------------- | ------ | ---------------------------------- |
| Mechanical Assembly | PASS   | All joints verified                |
| Servo Bus           | PASS   | IDs 1~6 detected                   |
| IMU                 | PASS   | Attitude within tolerance          |
| Wheel Control       | PASS   | Velocity control stable            |
| Gait Engine         | PASS   | Forward / Backward / Turn executed |
| Safety Manager      | PASS   | E-Stop and Fault Handling verified |
| Power / Electrical  | PASS   | Voltage and current within spec    |
| Logging             | PASS   | All events captured                |

---

# 10. Freeze Summary

Alpha Prototype

* Mechanical: VERIFIED
* Electrical: VERIFIED
* Software: VERIFIED
* Safety: VERIFIED
* Motion: VERIFIED
* Gait: VERIFIED
* Status: APPROVED
* READY FOR: Beta Prototype / PR-003 Iteration
