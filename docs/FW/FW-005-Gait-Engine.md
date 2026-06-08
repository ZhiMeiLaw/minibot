# Mini-Atlas V6 Alpha

# FW-005 Gait Engine

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-005

Subsystem:

Firmware – Gait Engine

Target Platform:

ESP32 DevKitC

Related Documents:

* FW-001 Firmware Architecture
* FW-002 Servo Bus Driver
* FW-003 IMU Driver
* FW-004 Wheel Control
* CDS-03~09 Mechanical CAD
* PR-001 Alpha Prototype Release

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 步态引擎（Gait Engine）架构与实现策略。

目标：

* 控制 3 DOF / Leg（Hip Roll / Hip Pitch / Knee）
* 配合轮子辅助（Wheel Assisted Gait）
* 保证站立稳定性与步态平衡
* 提供 Motion Layer 接口
* 可与 Safety Manager 完全集成

---

# 2. Gait Philosophy

Alpha 版本特点：

* Quasi-Static Gait
* 不依赖 ZMP / MPC
* 不依赖力传感器
* 静态重心修正通过 Wheel Module
* 步态周期 1~2 秒 / 步
* 支持 Forward / Backward / Turn

---

# 3. Software Architecture

Application Layer

↓

Motion Layer

↓

Gait Engine

↓

Leg Controller Interface

↓

Servo Bus Driver

↓

STS3046

↓

ICM42688 (Feedback)

↓

Wheel Controller

↓

GB37-520

---

# 4. Gait State Machine

| State         | Description                    |
| ------------- | ------------------------------ |
| STANDBY       | Robot Idle                     |
| STANDING      | Legs Torque Enabled, Feet Flat |
| STEP_FORWARD  | Left / Right Alternating Step  |
| STEP_BACKWARD | Reverse Step                   |
| TURN_LEFT     | Hip Roll / Wheel Differential  |
| TURN_RIGHT    | Hip Roll / Wheel Differential  |
| WHEEL_ASSIST  | Wheels Active, Legs Passive    |
| FAULT         | Any Safety Fault Detected      |

---

# 5. Step Cycle Definition

Alpha Gait Cycle:

* Duration: 1.5 s / step
* Phase Split:

  * 0~25% Lift Left / Right Foot
  * 25~75% Swing / Transfer
  * 75~100% Contact / Stabilization

---

# 6. Leg Trajectory Planning

Inputs:

* Step Length (mm)
* Step Height (mm)
* Step Speed (mm/s)
* Direction (Forward / Backward / Turn)

Outputs:

* Joint Targets: Hip Roll / Hip Pitch / Knee

Trajectory Type:

* Cubic Polynomial
* Smooth Acceleration / Deceleration

---

# 7. Wheel Assisted Gait

Purpose:

* 修正重心偏移
* 支持低速稳定
* 支持微小姿态调整

Inputs:

* IMU Roll / Pitch
* Desired COM Offset
* Current Wheel Position

Outputs:

* Wheel Velocity PWM

Loop Rate: 200 Hz

---

# 8. Gait Engine API

```cpp id="u8x0tz"
void gait_set_step_parameters(float step_length_mm,
                              float step_height_mm,
                              float step_duration_s);

void gait_start();
void gait_stop();
void gait_update();
bool gait_is_running();
```

---

# 9. Motion Layer Interface

* Gait Engine 提供 Joint Targets → Servo Bus Driver
* IMU Feedback → Gait Engine
* Wheel Feedback → Wheel Controller → Gait Engine

Loop Rate:

* Motion Loop: 100 Hz
* Gait Engine Update: 100 Hz
* Wheel Assisted Correction: 200 Hz

---

# 10. Safety Integration

* Safety Manager overrides Gait Engine
* Any Servo Fault → Stop Step
* Emergency Stop → Stop immediately
* IMU Fault → Stop Step / Stabilize using Wheels

---

# 11. Bring-Up Procedure

1. Verify Servo Bus Driver functional
2. Verify IMU driver operational
3. Verify Wheel Controller operational
4. Initialize Gait Engine parameters
5. Enable STANDING
6. Execute STEP_FORWARD / STEP_BACKWARD
7. Monitor Joint Currents
8. Monitor IMU / Wheel Feedback
9. Verify Safety Interlocks

Pass Criteria:

* Robot remains upright
* Servos do not exceed 80% torque
* Wheels provide smooth stabilization

---

# 12. Verification Checklist

□ Gait Engine initializes correctly
□ Step parameters accepted
□ Trajectory outputs within Joint Limits
□ Safety Manager overrides functional
□ Wheel Assisted Gait stabilizes COM
□ Forward / Backward / Turn validated
□ Emergency Stop functional
□ Motion Loop 100 Hz stable

---

# 13. Freeze Summary

Gait Engine

* Step Cycle: 1.5 s
* Leg DOF: 3 / Leg
* Wheel Assisted: Enabled
* Trajectory: Cubic Polynomial
* Feedback: IMU + Wheel
* Safety Overrides: Enabled
* Update Rate: Motion 100 Hz / Wheel 200 Hz
* Status: APPROVED
* READY FOR: FW-006-Safety-Manager.md
