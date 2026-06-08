# Mini-Atlas V6 Alpha

# DR-001 System Architecture Review

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

DR-001

Subsystem:

System Architecture

Related Documents:

* MDS-001 System Requirements
* SR-001 System Weight Budget
* EDS-001 System Electrical Architecture
* FW-001 Firmware Architecture

---

# 1. Purpose

本评审用于确定 Mini-Atlas V6 Alpha 的总体系统架构。

本次评审将冻结：

* 整机形态
* 自由度配置
* 驱动方式
* 控制架构
* 电源架构
* 软件架构边界

评审通过后：

不得改变总体机器人架构。

---

# 2. Design Goals

Mini-Atlas V6 Alpha 目标：

* 高度约55cm
* 重量小于5kg
* 低成本
* 可完全开源
* 支持室内移动
* 支持轮辅助步态
* 支持未来视觉系统升级

---

# 3. Candidate Architectures

## Option A

Pure Humanoid

```text
Leg
Leg
```

Advantages

* 最仿人

Disadvantages

* 控制复杂
* 能耗高
* 开发周期长

Result

REJECTED

---

## Option B

Wheel Robot

```text
Wheel
Wheel
```

Advantages

* 简单

Disadvantages

* 无双足能力

Result

REJECTED

---

## Option C

Hybrid Wheel-Leg

```text
Leg
Leg

+
Wheel
Wheel
```

Advantages

* 控制简单
* 能耗低
* 可保持双足结构
* 容易实现稳定运动

Result

APPROVED

---

# 4. Selected Architecture

Configuration

```text
          Torso

            │

         Pelvis

      ┌─────┴─────┐

 Left Leg     Right Leg

      │             │

     Wheel       Wheel
```

Status

FROZEN

---

# 5. Degrees of Freedom

## Hip Roll

1 DOF

---

## Hip Pitch

1 DOF

---

## Knee Pitch

1 DOF

---

Per Leg

3 DOF

---

Total

6 DOF

---

Reason

最低可行双足自由度配置

---

# 6. Actuation Architecture

Selected

STS3046

UART Bus Servo

---

Reasons

* 低成本
* 可级联
* 总线简单
* 重量可接受

---

Servo Count

6

---

Status

FROZEN

---

# 7. Mobility Architecture

Walking Mode

```text
Hip Roll
Hip Pitch
Knee
```

---

Stability Mode

```text
Wheel Assisted Gait
```

---

Purpose

利用轮组补偿重心变化。

---

Status

FROZEN

---

# 8. Controller Architecture

Main Controller

ESP32 DevKitC

---

Functions

* Gait Engine
* Wheel Control
* Servo Control
* Safety Manager
* OTA

---

Status

FROZEN

---

# 9. Sensor Architecture

IMU

ICM42688-P

---

Functions

* Roll
* Pitch
* Yaw
* Fall Detection

---

Status

FROZEN

---

# 10. Power Architecture

Battery

3S2P Samsung 30Q

---

Servo Rail

7.4V

---

Logic Rail

5V

---

Status

FROZEN

---

# 11. Communication Architecture

Servo Bus

UART

---

IMU

I2C

---

Debug

USB UART

---

OTA

WiFi

---

Status

FROZEN

---

# 12. Software Architecture

Layers

```text
Application

Motion Layer

Gait Engine

Servo Driver

Hardware Layer
```

Status

FROZEN

---

# 13. Weight Budget

Target

≤ 5kg

---

Expected

3.5~4.5kg

---

Status

FROZEN

---

# 14. Manufacturing Strategy

Primary

FDM 3D Printing

---

Material

PETG

---

Optional

ABS

---

Carbon Tube

Structural Members

---

Status

FROZEN

---

# 15. Future Expansion

Reserved

* Camera
* Depth Sensor
* ROS2 Companion Computer
* AI Module

---

Not Included In Alpha

* Arms
* Hands
* Vision System
* Autonomous Navigation

---

# 16. Risks

Risk 1

Hip Pitch Torque Margin

Mitigation

Torque Transfer Module

---

Risk 2

Battery Runtime

Mitigation

Wheel Assisted Gait

---

Risk 3

COM Stability

Mitigation

IMU Closed Loop

---

# 17. Review Decision

Mechanical

PASS

Electrical

PASS

Firmware

PASS

Manufacturing

PASS

---

Overall Decision

APPROVED

---

# 18. Freeze Summary

Robot Height

55cm

---

Architecture

Hybrid Wheel-Leg

---

DOF

6

---

Servo

STS3046 × 6

---

Controller

ESP32

---

Battery

3S2P Samsung 30Q

---

Mobility

Wheel Assisted Gait

---

Status

APPROVED

---

Next Document

DR-002-Actuator-Selection-Review.md
