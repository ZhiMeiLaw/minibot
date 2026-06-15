# Mini-Atlas V6 Alpha

# CAD-021 Prototype Build and Real World Test Protocol

Version: 1.0

Status: PHYSICAL VALIDATION & FIRST WALK GATE

Document Number:

CAD-021

Subsystem:

Prototype Assembly & Real-World Testing

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 首台实体机器人（Prototype v1）的：

* 组装流程
* 上电流程
* 安全测试流程
* 静态站立测试
* 初始步态测试

---

# 2. System Transition

```text
CAD-020 (Manufacturing Plan)
        ↓
CAD-021 (Physical Robot)
        ↓
REAL WORLD BEHAVIOR
```

---

# 3. Prototype Scope

FreeCAD

## Included Systems

* Pelvis
* Left Leg
* Right Leg
* Basic control board
* IMU feedback system

---

# 4. Assembly Protocol

## Step 1: Mechanical Assembly

* Pelvis frame assembly
* Hip module installation
* Knee linkage assembly
* Foot module alignment

---

## Step 2: Actuator Installation

* Hip pitch servo
* Hip roll servo
* knee servo
* torque calibration

---

## Step 3: Wiring Integration

* signal routing
* power distribution
* IMU placement

---

# 5. Pre-Power Safety Checks

## Mechanical Check

* no loose joints
* no binding motion
* full range motion verified

---

## Electrical Check

* no short circuit
* correct polarity
* stable power rail

---

# 6. First Power-On Protocol

Bambu Studio

## Step Sequence

```text
1. Power MCU only
2. Verify IMU response
3. Enable single servo test
4. Enable joint sequential activation
```

---

# 7. Static Standing Test

## Objective

Robot must:

```text
stand without external support
```

---

## Stability Requirements

* no oscillation
* no drift
* no overheating

---

# 8. Weight Shift Test

## Procedure

* shift CoM left/right
* observe hip roll correction
* verify balance response

---

# 9. First Step Test

## Conditions

* slow gait mode only
* high stability margin
* reduced step length

---

## Expected Behavior

* slight forward lean
* controlled swing leg lift
* stable landing

---

# 10. Safety Constraints

## Emergency Stop Conditions

* rapid tilt > threshold
* servo overload
* uncontrolled oscillation

---

# 11. Failure Modes

## Failure 1: Immediate Fall

→ CG misalignment

---

## Failure 2: Joint Lock

→ mechanical misassembly

---

## Failure 3: Oscillation

→ control loop instability

---

# 12. Success Criteria

Prototype is successful if:

* can stand ≥ 30 seconds
* can shift weight left/right
* can perform at least 1 full step
* no structural failure

---

# 13. Data Collection

## Required Logs

* IMU trajectory
* joint angles
* torque usage
* fall events

---

# 14. System Interpretation

```text
If it stands → geometry is correct
If it steps → control system is correct
If it walks → system is complete
```

---

# 15. Key Insight

```text
A robot is no longer a design when it moves in the real world
```

---

# 16. System Status

| Layer              | Status   |
| ------------------ | -------- |
| CAD System         | COMPLETE |
| Control System     | COMPLETE |
| Simulation         | COMPLETE |
| Manufacturing      | COMPLETE |
| Physical Prototype | ACTIVE   |

---

# 17. Next Step

进入：

```text
CAD-022-First-Walking-Event-Analysis.md
```

目标：

👉 分析第一次真实行走数据
👉 修正控制参数
👉 优化稳定性
👉 进入持续迭代阶段

---

# 18. Status

Prototype Execution:

ACTIVE

System State:

```text
FIRST REAL ROBOT TESTING ENABLED
```
