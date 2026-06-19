# Mini-Atlas V6 Alpha

# CAD-016 Sensor and Feedback System Design

Version: 1.0

Status: SENSOR INTEGRATION LAYER

Document Number:

CAD-016

Subsystem:

Perception & Feedback System

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的传感器系统，使其能够：

* 感知姿态变化
* 检测关节状态
* 识别地面接触
* 提供实时反馈给控制系统（CAD-015）

---

# 2. System Role

```text id="r1"
Sensors → Feedback → Control System → Actuation
```

---

# 3. Sensor Architecture

FreeCAD

```text id="a1"
IMU (Body Orientation)
Joint Encoders (Angle Feedback)
Foot Contact Sensors (Ground State)
Optional: Current Sensors (Torque Estimate)
```

---

# 4. IMU System

## Function

```text id="i1"
Measure global orientation of robot
```

---

## Placement

* Torso center (primary)
* Optional secondary IMU on pelvis

---

## Outputs

* Roll
* Pitch
* Yaw
* Angular velocity

---

# 5. Joint Encoder System

## Function

```text id="j1"
Measure real joint angle vs commanded angle
```

---

## Location

* Hip Roll
* Hip Pitch
* Knee joint

---

## Requirement

* High resolution (<0.5°)
* Low latency

---

# 6. Foot Contact Detection

## Function

```text id="f1"
Detect ground contact state
```

---

## Methods

* Force sensitive resistor (FSR)
* Micro-switch (binary)
* Load cell (advanced)

---

## States

```text id="f2"
CONTACT / NO CONTACT
```

---

# 7. Feedback Loop Integration

## Signal Flow

```text id="s1"
IMU + Encoders + Foot Sensors
        ↓
State Estimator
        ↓
Balance Controller (CAD-015)
        ↓
Servo Commands
```

---

# 8. State Estimation Model

## Core Idea

```text id="e1"
Robot State = Fusion(Sensor Inputs)
```

---

## Estimated States

* Center of Mass projection
* Body tilt angle
* Support phase (single/double)
* Joint load estimation

---

# 9. Feedback Latency Requirement

```text id="l1"
Total latency must be < gait phase duration
```

---

# 10. Sensor Placement Strategy

## Torso IMU

* Global orientation reference

---

## Pelvis IMU (optional)

* Local stability reference

---

## Foot Sensors

* Contact timing trigger

---

# 11. Failure Modes

## Failure 1: IMU Drift

→ long-term orientation error

---

## Failure 2: Encoder Noise

→ unstable joint control

---

## Failure 3: Foot Sensor Delay

→ incorrect gait phase detection

---

# 12. System Constraints

```text id="c1"
Sensor data must be real-time and synchronized
```

---

# 13. Feedback Control Dependency

Sensors directly enable:

* CAD-015 Control System
* CAD-014 Gait Cycle execution
* Stability correction loop

---

# 14. Design Insight

```text id="i1"
Without sensors, robot is blind; without feedback, robot is unstable
```

---

# 15. System Integration Status

| Layer          | Status    |
| -------------- | --------- |
| Geometry       | PASS      |
| Gait Model     | PASS      |
| Control System | PASS      |
| Sensor System  | IN DESIGN |

---

# 16. Next Step

进入：

```text id="n1"
CAD-017-Real-Time-Control-Loop-Integration.md
```

目标：

👉 将 Sensor + Control + Gait 全部闭环
👉 实现实时稳定控制架构
👉 构建“可运行机器人控制循环”

---

# 17. Status

Sensor System:

APPROVED (ARCHITECTURE LEVEL)

System State:

```text id="st1"
PERCEPTION LAYER DEFINED — REAL-TIME LOOP REQUIRED
```
