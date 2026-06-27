# Mini-Atlas V6 Alpha

# EDS-05 Communication & Control Architecture

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

- Communication Architecture（通信架构）
- Control Architecture（控制架构）
- Servo Bus（舵机总线）
- IMU Architecture（惯导架构）
- Wheel Control（轮足控制）
- State Machine（状态机）
- Safety System（安全系统）
- OTA Upgrade（在线升级）
- Diagnostic System（诊断系统）

本文件将作为：

```text
SDS-01 Software Architecture Specification
```

的输入文件。

---

# 2. Design Philosophy

V6 Alpha 采用：

```text
Simple
Reliable
Maintainable
```

原则。

避免：

```text
ROS2
DDS
SLAM
Vision
EKF
```

等高复杂度系统。

第一目标：

```text
站立

轮式移动

抬腿

跨障碍

跌倒保护
```

---

# 3. System Architecture

## Overall Architecture

```text

                 ESP32

                    │

      ┌─────────────┼─────────────┐

      │             │             │

    UART           I2C          PWM

      │             │             │

 Servo Bus      ICM42688     Wheel Driver

      │

STS3046

```

---

> **ECO-002 变更**：STS3215 已删除（DR-011 移除踝关节）。

# 4. MCU Selection

## Main Controller

冻结：

```text
ESP32 DevKitC-32E
```

---

## Specification

| Item | Value |
|--------|--------|
| CPU | Dual Core |
| Frequency | 240MHz |
| SRAM | 520KB |
| WiFi | Yes |
| Bluetooth | Yes |

---

## Resource Allocation

### Core 0

负责：

```text
WiFi

OTA

Diagnostics
```

---

### Core 1

负责：

```text
IMU

Control Loop

State Machine
```

---

# 5. Communication Architecture

## Internal Bus

系统采用：

```text
UART

I2C

PWM
```

---

# 6. Servo Bus Architecture

## Bus Type

冻结：

```text
Half Duplex UART
```

---

## Baudrate

冻结：

```text
1000000bps
```

即：

```text
1Mbps
```

---

## Physical Topology

```text

ESP32

 │

 ├───────────────────────────── Servo Bus

 │

Servo1

 │

Servo2

 │

Servo3

 │

Servo4

 │

Servo5

 │

Servo6

 │

Servo7

 │

Servo8

```

---

## Servo Refresh Rate

冻结：

```text
100Hz
```

---

控制周期：

```text
10ms
```

---

# 7. Servo ID Allocation

## Left Leg

| Joint | ID |
|---------|---------:|
| Hip Roll L | 1 |
| Hip Pitch L | 2 |
| Knee L | 3 |

---

## Right Leg

| Joint | ID |
|---------|---------:|
| Hip Roll R | 4 |
| Hip Pitch R | 5 |
| Knee R | 6 |

---

## Reserved

| Function | ID |
|------------|---------:|
| Arms | 7~20 |
| Head | 21~30 |

---

Freeze：

```text
ID 1~6
```

---

# 8. IMU Architecture

## Sensor

冻结：

```text
ICM42688-P
```

---

## Interface

```text
I2C
```

---

## Pin Mapping

| Signal | GPIO |
|------------|------------|
| SDA | GPIO21 |
| SCL | GPIO22 |

---

## Bus Speed

```text
400kHz
```

---

# 9. Attitude Estimation

## Input

IMU 输出：

```text
Gyroscope

Accelerometer
```

---

## Output

生成：

```text
Pitch

Roll
```

---

## Filter

冻结：

```text
Complementary Filter
```

---

算法：

```text

Angle

=

0.98 × Gyro

+

0.02 × Accel

```

---

原因：

```text
简单

稳定

CPU占用低
```

---

暂不采用：

```text
EKF

Madgwick

Mahony
```

---

# 10. Control Architecture

## Layer Structure

```text

Application Layer

        │

Control Layer

        │

HAL Layer

```

---

# HAL Layer

负责：

```text
UART

I2C

PWM

ADC

GPIO
```

---

# Control Layer

负责：

```text
IMU

PID

Servo Control

Wheel Control
```

---

# Application Layer

负责：

```text
Stand

Roll

Step

Obstacle

Recovery
```

---

# 11. Control Loop Frequency

## IMU Loop

冻结：

```text
200Hz
```

---

周期：

```text
5ms
```

---

## Control Loop

冻结：

```text
100Hz
```

---

周期：

```text
10ms
```

---

## State Machine

冻结：

```text
50Hz
```

---

周期：

```text
20ms
```

---

## Telemetry

冻结：

```text
10Hz
```

---

# 12. PID Architecture

## Roll Stabilization

输入：

```text
Roll Error
```

---

输出：

```text
Hip Roll Correction
```

---

结构：

```text

Roll Target

      │

   PID

      │

Hip Roll Servo

```

---

## Pitch Stabilization

输入：

```text
Pitch Error
```

---

输出：

```text
Hip Pitch Correction
```

---

结构：

```text

Pitch Target

      │

   PID

      │

Hip Pitch Servo

```

---

## Freeze

V6 Alpha：

```text
2 PID Loops
```

---

# 13. Wheel Control

## Driver

冻结：

```text
DRV8871
```

---

## Interface

```text
PWM
```

---

## GPIO Mapping

| Function | GPIO |
|------------|------------|
| Left PWM | GPIO25 |
| Right PWM | GPIO26 |
| Left DIR | GPIO27 |
| Right DIR | GPIO14 |

---

## Control Frequency

```text
100Hz
```

---

# 14. Gait State Machine

## Type

冻结：

```text
Finite State Machine (FSM)
```

---

## States

```text

IDLE

STAND

ROLL

STEP

OBSTACLE

RECOVERY

FAULT

```

---

# IDLE

```text
Servo Disabled
```

---

# STAND

```text
Balance Active
```

---

# ROLL

```text
Wheel Motion
```

---

# STEP

```text
Obstacle Crossing
```

---

# OBSTACLE

```text
Wheel Blocked
```

---

# RECOVERY

```text
Fall Recovery
```

---

# FAULT

```text
Emergency Safe State
```

---

# 15. Obstacle Crossing Logic

## Trigger

满足：

```text
Wheel Speed < Threshold

AND

Motor Command > Threshold
```

---

判断：

```text
Obstacle Detected
```

---

动作：

```text

Pause Wheels

↓

Shift Weight

↓

Lift Leg

↓

Forward Step

↓

Resume Rolling

```

---

# 16. Safety Architecture

## Emergency Stop

触发：

```text
Button

UART Command

OTA Command
```

---

动作：

```text
Disable Servo Rail

Stop Wheel Motors
```

---

要求：

```text
Response <100ms
```

---

# 17. Watchdog

## Type

冻结：

```text
ESP32 Task Watchdog
```

---

## Timeout

```text
500ms
```

---

动作：

```text
System Reset
```

---

# 18. Low Battery Protection

## Warning

```text
10.5V
```

---

动作：

```text
限制步态速度
```

---

## Critical

```text
9.9V
```

---

动作：

```text
进入Safe Mode
```

---

# 19. OTA Architecture

## Method

冻结：

```text
WiFi OTA
```

---

## Framework

```text
ESP-IDF Native OTA (Partition A/B)
```

---

未来：

```text
HTTP OTA with Remote Server
```

---

## Requirements

```text
No USB Required
```

---

# 20. Diagnostic System

## Debug UART

冻结：

```text
115200bps
```

---

输出：

```text
Battery Voltage

Pitch

Roll

Servo State

Wheel State

FSM State
```

---

# 21. Fault Management

## Fault 01

```text
Low Battery
```

---

## Fault 02

```text
IMU Failure
```

---

## Fault 03

```text
Servo Timeout
```

---

## Fault 04

```text
Wheel Driver Failure
```

---

## Fault 05

```text
Watchdog Reset
```

---

## Fault 06

```text
Over Temperature
```

---

# 22. Telemetry Data

## Period

```text
10Hz
```

---

## Payload

```text

VBAT

Pitch

Roll

Left Wheel RPM

Right Wheel RPM

Servo Status

FSM State

Fault Code

```

---

# 23. Future Expansion

预留接口：

```text
UART1

SPI

I2C
```

---

用于：

```text
Raspberry Pi

Camera

Lidar

ROS2 Bridge
```

---

# 24. Design Freeze Summary

## MCU

```text
ESP32 DevKitC-32E
```

---

## IMU

```text
ICM42688-P
```

---

## Servo Bus

```text
UART

1Mbps

100Hz
```

---

## Wheel Driver

```text
DRV8871
```

---

## Filter

```text
Complementary Filter
```

---

## Stabilization

```text
Pitch PID

Roll PID
```

---

## State Machine

```text
IDLE

STAND

ROLL

STEP

OBSTACLE

RECOVERY

FAULT
```

---

## Safety

```text
Emergency Stop

Watchdog

Low Battery Protection
```

---

## OTA

```text
WiFi OTA

ESP-IDF A/B
```

---

Status:

```text
APPROVED

READY FOR SDS-01
```
