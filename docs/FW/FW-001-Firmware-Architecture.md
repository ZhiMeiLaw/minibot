# Mini-Atlas V6 Alpha

# FW-001 Firmware Architecture

Version: 1.0 Freeze A

Status: APPROVED

Document Number:

FW-001

Subsystem:

Firmware

Target Platform:

ESP32 DevKitC

Related Documents:

* EDS-05 Communication & Control Architecture
* PR-001 Alpha Prototype Release
* MP-001 Manufacturing Package Release
* FW-002 Servo Bus Driver
* FW-003 IMU Driver
* FW-004 Wheel Control
* FW-005 Gait Engine

---

# 1. Purpose

定义 Mini-Atlas V6 Alpha 固件总体架构。

冻结：

* Repository Structure
* Software Layers
* RTOS Architecture
* Task Model
* Control Loop
* Safety Framework
* OTA Framework
* Bring-Up Architecture

本文件作为全部固件开发的顶层规范。

---

# 2. Firmware Goals

V6 Alpha 固件目标：

* 稳定
* 易调试
* 易维护
* 易扩展

优先级：

Reliability

↓

Safety

↓

Maintainability

↓

Performance

---

# 3. Software Stack

Application Layer

↓

Motion Layer

↓

Hardware Abstraction Layer

↓

ESP-IDF

↓

ESP32

---

采用：

ESP-IDF

FreeRTOS

---

Arduino Framework

NOT ALLOWED

---

# 4. Repository Structure

```text
firmware/

├── app/
│
├── motion/
│
├── gait/
│
├── servo/
│
├── wheel/
│
├── imu/
│
├── safety/
│
├── ota/
│
├── comm/
│
├── board/
│
├── drivers/
│
├── tests/
│
└── tools/
```

---

# 5. Layer Architecture

## Application Layer

负责：

* Robot State
* Mode Manager
* User Commands

---

## Motion Layer

负责：

* Joint Targets
* IK/FK
* Pose Generation

---

## Device Layer

负责：

* Servo Driver
* IMU Driver
* Wheel Driver

---

## HAL Layer

负责：

* UART
* I2C
* GPIO
* Timer

---

# 6. RTOS Architecture

采用：

FreeRTOS

---

Core0

Communication

Safety

OTA

---

Core1

Motion

Control Loop

Sensor Fusion

---

# 7. Task Architecture

| Task        | Priority |       Period |
| ----------- | -------: | -----------: |
| Safety Task |       10 |        10 ms |
| Motion Task |        9 |        10 ms |
| Servo Task  |        8 |        10 ms |
| IMU Task    |        8 |         5 ms |
| Wheel Task  |        7 |        10 ms |
| Comm Task   |        6 |        20 ms |
| OTA Task    |        2 | Event Driven |

---

# 8. Main Control Frequency

System Tick

1 kHz

---

Motion Loop

100 Hz

---

Servo Update

100 Hz

---

Wheel Update

100 Hz

---

IMU Sampling

200 Hz

---

Status

FROZEN

---

# 9. Robot State Machine

BOOT

↓

INIT

↓

STANDBY

↓

READY

↓

STANDING

↓

WALKING

↓

WHEEL_MODE

↓

FAULT

---

状态切换必须经过 Safety Manager。

---

# 10. Communication Architecture

UART1

Servo Bus

---

I2C

IMU

---

UART0

Debug Console

---

WiFi

OTA

---

Status

FROZEN

---

# 11. Motion Architecture

Pose Generator

↓

IK Solver

↓

Joint Targets

↓

Servo Driver

---

控制模式：

Position Control

Only

---

Torque Control

Not Implemented

---

# 12. Sensor Architecture

Primary Sensor

ICM42688

---

Data Rate

200 Hz

---

Outputs

Roll

Pitch

Yaw

Angular Velocity

Acceleration

---

# 13. Safety Manager

Safety Manager 独立运行。

监控：

Servo Timeout

---

IMU Failure

---

Low Battery

---

Over Current

---

Watchdog

---

# 14. Emergency Stop

触发条件：

E-Stop Button

---

Servo Bus Lost

---

Battery Critical

---

Watchdog Trigger

---

动作：

Disable Torque

Stop Wheels

Enter FAULT

---

Status

FROZEN

---

# 15. Watchdog Framework

Software Watchdog

100 ms

---

Hardware Watchdog

Enabled

---

Recovery

System Restart

---

Status

FROZEN

---

# 16. OTA Framework

WiFi OTA

---

Partition Layout

A/B

---

Rollback

Supported

---

Safe Update

Required

---

Status

FROZEN

---

# 17. Logging Framework

Levels

ERROR

WARN

INFO

DEBUG

---

Output

UART Console

---

Future

WiFi Log Streaming

---

# 18. Bring-Up Software Flow

Power On

↓

Board Init

↓

UART Init

↓

I2C Init

↓

IMU Detect

↓

Servo Scan

↓

Wheel Driver Init

↓

Safety Init

↓

READY

---

任何步骤失败：

↓

FAULT

---

# 19. Coding Standards

Language

C++17

---

Compiler

ESP-IDF Toolchain

---

禁止：

Dynamic Allocation

Inside Control Loop

---

禁止：

Blocking Delay

Inside Real-Time Tasks

---

必须：

Static Memory Preferred

---

# 20. Freeze Summary

Platform

ESP32 DevKitC

---

Framework

ESP-IDF

---

RTOS

FreeRTOS

---

Control Rate

100 Hz

---

IMU Rate

200 Hz

---

Servo Bus

UART

---

Safety Manager

Enabled

---

Watchdog

Enabled

---

OTA

Enabled

---

Status

APPROVED

READY FOR

FW-002-Servo-Bus-Driver.md
