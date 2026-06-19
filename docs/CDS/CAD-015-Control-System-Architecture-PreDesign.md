# Mini-Atlas V6 Alpha

# CAD-015 Control System Architecture PreDesign

Version: 1.0

Status: CONTROL SYSTEM DESIGN GATE

Document Number:

CAD-015

Subsystem:

Balance Control & Servo Control Architecture

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 的控制系统架构，使其能够：

* 执行步态（CAD-014）
* 维持动态平衡
* 控制关节角度
* 实现实时反馈调节

---

# 2. System Transition

```text id="c1"
GEOMETRY (CAD 001–014)
        ↓
MOTION MODEL (Gait)
        ↓
CONTROL SYSTEM (THIS STAGE)
        ↓
REAL ROBOT BEHAVIOR
```

---

# 3. Core Control Philosophy

```text id="p1"
Robot Stability = Continuous Feedback Correction
```

---

# 4. Control System Layers

## Layer 1: High-Level Gait Planner

* Step timing
* Foot placement
* Phase switching

---

## Layer 2: Balance Controller

FreeCAD

* Center of Mass stabilization
* Hip Roll compensation
* Body tilt correction

---

## Layer 3: Joint Controller

* Hip Pitch PID
* Hip Roll PID
* Knee angle PID

---

## Layer 4: Servo Actuation Layer

* PWM / UART command output
* position feedback
* torque limiting

---

# 5. Control Loop Architecture

```text id="a1"
Gait Planner
      ↓
Balance Controller
      ↓
Joint Controller (PID)
      ↓
Servo Driver
      ↓
Actuation
      ↓
Sensor Feedback
      ↑
      └─────────────── loop
```

---

# 6. Balance Control Model

## Core Objective

```text id="b1"
Keep CoM projection inside support polygon
```

---

## Correction Variables

* Hip Roll angle adjustment
* Hip Pitch offset
* Knee micro compensation

---

# 7. PID Control Structure

## Hip Pitch PID

```text id="p2"
error = desired_angle - actual_angle
output = Kp*e + Ki∫e + Kd(de/dt)
```

---

## Hip Roll PID

* Primary stability controller
* Lateral correction

---

## Knee PID

* Load absorption
* posture stabilization

---

# 8. Feedback System

## Input Signals

* IMU (orientation)
* joint encoders
* foot contact sensor (optional)

---

## Output Signals

* servo position command
* torque limit adjustment
* gait phase correction

---

# 9. Stability Feedback Loop

```text id="s1"
IMU → Balance Controller → Joint Adjustment → Motion Correction → IMU
```

---

# 10. Servo Control Layer

## Control Type

* Position control (primary)
* torque limiting (safety)

---

## Communication Layer

* UART recommended
* or PWM fallback

---

# 11. Control Constraints

```text id="c2"
No joint may exceed torque safety envelope
No correction may violate gait timing
```

---

# 12. System Failure Modes

## Failure 1: Oscillation

→ PID gain too high

---

## Failure 2: Drift

→ no integral correction

---

## Failure 3: Fall

→ delayed feedback loop

---

# 13. Stability Requirement

```text id="s2"
Correction latency must be < gait phase transition time
```

---

# 14. Architecture Insight

```text id="i1"
Without control system, gait is only a simulation
With control system, gait becomes reality
```

---

# 15. System Readiness Status

| Layer              | Status      |
| ------------------ | ----------- |
| Geometry           | PASS        |
| Torque Feasibility | CONDITIONAL |
| Gait Model         | PASS        |
| Control System     | IN DESIGN   |

---

# 16. Next Step

进入：

```text id="n1"
CAD-016-Sensor-and-Feedback-System-Design.md
```

目标：

👉 IMU系统设计
👉 joint encoder integration
👉 foot contact sensing
👉 feedback signal完整闭环

---

# 17. Status

Control Architecture:

APPROVED (PRE-IMPLEMENTATION)

System State:

```text id="st1"
CONTROL SYSTEM DEFINED — SENSOR SYSTEM REQUIRED
```
