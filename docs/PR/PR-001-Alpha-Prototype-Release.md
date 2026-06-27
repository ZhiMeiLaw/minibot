# Mini-Atlas V6 Alpha

# PR-001 Alpha Prototype Release

Version: 1.0

Release Status: APPROVED

Release Number:

PR-001

Release Name:

Mini-Atlas V6 Alpha Prototype

Release Type:

Engineering Prototype

Release Date:

TBD

Parent Documents:

* CDS-09 Full Body Integration
* SR-001 System Weight Budget
* BOM-01 Master Bill Of Materials
* EDS-05 Communication & Control Architecture

---

# 1. Purpose

冻结：

Mini-Atlas V6 Alpha

第一台工程样机配置。

用于：

* CAD建模
* 零件打印
* 采购
* 装配
* Bring-Up
* 首次站立测试

---

# 2. Release Scope

本版本目标：

验证：

* 结构正确性
* 装配正确性
* 电气正确性
* 舵机通讯
* IMU数据
* 站立能力
* Wheel Mode

---

本版本不验证：

* 视觉导航
* 机械臂
* 自主定位
* AI功能

---

# 3. Mechanical Configuration

Height

≈560 mm

---

Weight Target

≤4.0 kg

---

Expected Weight

≈3.3 kg

---

Leg

3 DOF

Per Leg

---

Wheel

80 mm

---

Architecture

Wheel Assisted Walker

---

Status

FROZEN

---

# 4. Actuator Configuration

Hip Roll

STS3046

x2

---

Hip Pitch

STS3046

x2

---

Knee

STS3046

x2

---

Wheel Motor

GB37-520

x2

---

Total

8 Actuators

---

# 5. Electronics Configuration

Main Controller

ESP32 DevKitC

x1

---

IMU

ICM42688

x1

---

Servo Bus

UART

---

Wheel Driver

Dual Motor Driver

x1

---

Camera

ESP32-CAM

x1

---

Status

FROZEN

---

# 6. Power Configuration

Battery

3S2P Samsung 30Q

---

Nominal Voltage

11.1V

---

Capacity

≈6000 mAh

---

Main Connector

XT30

---

Servo Rail

7.4V Buck

---

Logic Rail

5V Buck

---

Fuse

25A ATO Slow Blow

---

> **ECO-002 变更**：Fuse 由 15A Automotive Blade 修正为 25A ATO Slow Blow（EDS-03 最新分析，20A 有 18.5A 峰值误动作风险）。

Status

FROZEN

---

# 7. CAD Release

Assembly

V6-ASM-0030

---

Required Assemblies

Pelvis

Left Leg

Right Leg

Torso

Head

Electronics

---

Required Outputs

STEP

STL

Native CAD

---

Status

RELEASED

---

# 8. Print Configuration

Printer

Bambu Lab A1

---

Compatible

A1 Mini

---

Material

PETG

---

Layer Height

0.20 mm

---

Walls

4

---

Top/Bottom

5

---

Infill

40%

Gyroid

---

Status

RELEASED

---

# 9. Procurement Freeze

必须采购：

STS3046 ×6

GB37-520 ×2

Samsung 30Q ×6

ESP32 ×1

ICM42688 ×1

XT30

Buck Modules

Bearings

Carbon Tubes

Fasteners

---

版本：

BOM-01

BOM-02

冻结版本

---

# 10. Assembly Sequence

Stage 1

Print Parts

---

Stage 2

Install Inserts

---

Stage 3

Assemble Joints

---

Stage 4

Assemble Legs

---

Stage 5

Assemble Pelvis

---

Stage 6

Install Electronics

---

Stage 7

Install Battery

---

Stage 8

Cable Routing

---

Stage 9

Power Verification

---

Stage 10

Standing Test

---

# 11. Bring-Up Procedure

Step 1

No Battery

USB Only

---

Step 2

Flash Firmware

---

Step 3

Verify UART

---

Step 4

Verify Servo IDs

---

Step 5

Verify IMU

---

Step 6

Verify Motor Driver

---

Step 7

Verify Wheel Rotation

---

Status

MANDATORY

---

# 12. First Power-On Procedure

Robot Suspended

(No Ground Contact)

---

Connect Battery

---

Measure Current

---

Verify Rails

11.1V

7.4V

5V

---

Verify Temperature

---

Verify No Smoke

---

Status

MANDATORY

---

# 13. Servo Validation

Check:

Hip Roll

---

Hip Pitch

---

Knee

---

Verify:

Direction

Range

Current

Temperature

---

Status

MANDATORY

---

# 14. Wheel Validation

Verify:

Forward

Reverse

Brake

---

Encoder

(Optional)

---

Status

MANDATORY

---

# 15. IMU Validation

Verify:

Roll

Pitch

Yaw

---

Noise

---

Bias

---

Status

MANDATORY

---

# 16. First Standing Test

Environment

Soft Floor

---

Safety Rope

Recommended

---

Procedure

Enable Servo Torque

↓

Move To Stand Pose

↓

Hold 10 s

↓

Observe Current

↓

Observe Temperature

---

Pass Criteria

No Fall

No Overcurrent

No Servo Alarm

---

# 17. Alpha Success Criteria

Mechanical Assembly

PASS

---

Power System

PASS

---

Servo Bus

PASS

---

IMU

PASS

---

Standing

PASS

---

Wheel Drive

PASS

---

Weight

<4 kg

---

Status

ALPHA COMPLETE

---

# 18. Known Risks

Hip Pitch Margin

MEDIUM

---

Wheel Cable Damage

LOW

---

Battery Mount

LOW

---

Servo Clamp Loosening

LOW

---

# 19. Release Deliverables

Required:

* CAD Source
* STL Package
* STEP Package
* BOM
* Firmware
* Wiring Diagram
* Assembly Guide

---

# 20. Release Freeze Summary

Robot Height

≈560 mm

---

Robot Weight

≈3.3 kg

---

Battery

3S2P

Samsung 30Q

---

Controller

ESP32

---

IMU

ICM42688

---

Leg Architecture

3DOF

Wheel Assisted

---

Status

RELEASED

READY FOR

Prototype Manufacturing
