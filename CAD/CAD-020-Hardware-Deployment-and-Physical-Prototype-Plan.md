# Mini-Atlas V6 Alpha

# CAD-020 Hardware Deployment and Physical Prototype Plan

Version: 1.0

Status: MANUFACTURING TRANSITION LAYER

Document Number:

CAD-020

Subsystem:

Physical Prototype & Manufacturing Deployment

---

# 1. Purpose

将 Mini-Atlas V6 Alpha 从“仿真优化系统”推进到：

* 可制造结构设计
* 可采购BOM定义
* 可3D打印/加工方案
* 可装配原型机器人

---

# 2. System Transition

```text id="t1"
CAD-019 (Optimized Simulation)
        ↓
CAD-020 (Physical Deployment)
        ↓
REAL ROBOT PROTOTYPE
```

---

# 3. Manufacturing Strategy

FreeCAD

## Approach

* 3D打印（主结构）
* 标准件（轴承/螺丝）
* 模块化装配
* 可快速迭代设计

---

# 4. Manufacturing Stack

## 4.1 结构制造

* FDM 3D打印（主结构）
* 局部加强件（高应力区域）

---

## 4.2 标准件

* 轴承（6802 / 6803 系列）
* M3 / M4 螺丝
* 金属轴

---

## 4.3 执行器

* 高扭矩舵机（Hip / Knee）
* 中扭矩舵机（Hip Roll）

---

# 5. BOM (Bill of Materials)

## 5.1 Mechanical

```text id="b1"
Pelvis Frame ×1
Hip Modules ×2
Knee Modules ×2
Leg Links ×2
Foot Modules ×2
```

---

## 5.2 Actuation

```text id="b2"
Hip Pitch Servo ×2
Hip Roll Servo ×2
Knee Servo ×2
```

---

## 5.3 Electronics

```text id="b3"
MCU / SBC (Raspberry Pi or STM32)
IMU Sensor
Power Distribution Board
Battery Pack
```

---

# 6. Manufacturing Process

## Step 1: CAD Export

FreeCAD

```text id="s1"
STEP → STL
```

---

## Step 2: Slicing

Bambu Studio

* layer height: 0.2mm
* infill: 30–60%
* wall thickness optimized

---

## Step 3: Printing

* FDM printer (A1 Mini compatible)
* PLA / PETG material

---

## Step 4: Post Processing

* sanding
* insert bearing
* assembly alignment

---

# 7. Assembly Strategy

## Modular Assembly

```text id="a1"
Hip Module → Knee Module → Leg Module → Pelvis Integration
```

---

## Assembly Rules

* Left/Right mirrored parts
* No manual drilling allowed
* All tolerance predefined in CAD

---

# 8. Tolerance System

## Mechanical Clearance

```text id="t2"
0.2mm – 0.5mm clearance range
```

---

## Bearing Fit

* press-fit or light interference fit

---

# 9. Electrical Integration

## Wiring Architecture

```text id="e1"
MCU → Servo Bus → Joint Actuators
MCU → IMU
MCU → Power System
```

---

# 10. Risk Analysis

## Manufacturing Risks

* warping during print
* misalignment of joints
* servo torque underestimation
* wiring failure in moving joints

---

## Mitigation

* print orientation optimization
* reinforcement ribs
* modular wiring channels

---

# 11. Prototype Definition

## Prototype v1 Scope

* Lower body only
* Static walking test
* Basic balance control

---

# 12. Success Criteria

Prototype is valid if:

* can stand without support
* can perform weight shift
* can execute slow step cycle
* no structural failure

---

# 13. Key Insight

```text id="k1"
A robot is not finished when it is designed — it is finished when it stands without falling
```

---

# 14. System Status

| Layer              | Status   |
| ------------------ | -------- |
| CAD Design         | COMPLETE |
| Simulation         | COMPLETE |
| Optimization       | COMPLETE |
| Manufacturing Plan | ACTIVE   |

---

# 15. Next Step

进入：

```text id="n1"
CAD-021-Prototype-Build-and-Real-World-Test-Protocol.md
```

目标：

👉 第一台真实机器人组装
👉 上电测试
👉 站立测试
👉 初始步态测试

---

# 16. Status

Manufacturing Readiness:

APPROVED

System State:

```text id="st1"
READY FOR PHYSICAL PROTOTYPE BUILD
```
