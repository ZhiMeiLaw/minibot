# Mini-Atlas V6 Alpha

# EDS-01 System Electrical Architecture

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结 Mini-Atlas V6 Alpha 的整体电气架构（Electrical Architecture）。

本规范定义：

- 电源架构（Power Architecture）
- 控制器架构（Controller Architecture）
- 执行器架构（Actuator Architecture）
- 通信架构（Communication Architecture）
- 安全架构（Safety Architecture）

本文件是：

```text
EDS 系列文档的基础
```

后续：

- EDS-02
- EDS-03
- EDS-04
- EDS-05

均以本文件为依据。

---

# 2. Design Goals

V6 Alpha 的设计目标：

## Goal 1

实现稳定双足站立

(Static Standing)

---

## Goal 2

实现轮足移动

(Wheel-Assisted Locomotion)

---

## Goal 3

实现跨越小障碍

(Obstacle Traversal)

---

## Goal 4

实现基础姿态平衡

(Posture Stabilization)

---

## Goal 5

支持未来升级

- Raspberry Pi
- ROS2
- Camera
- Lidar

---

# 3. Electrical Architecture Overview

## System Block Diagram

```text

                   Battery
                (3S Li-ion)

                       │

                 Main Switch

                       │

                    Fuse

                       │

                     PDB
             (Power Distribution)

     ┌────────────┼────────────┐
     │            │            │

 Servo Rail   Logic Rail   Wheel Rail

   7.4V          5V          11.1V

     │            │            │

STS3046       ESP32       GB37-520

  IMU           Driver
```

> **ECO-001 变更**：踝关节已移除（DR-011），原 STS3215 电气架构取消。

---

# 4. System Domains

系统分为三个电气域（Electrical Domain）。

---

## Servo Domain

负责：

```text
姿态控制

关节运动

抬腿动作
```

---

供电：

```text
7.4V
```

---

执行器：

```text
STS3046
```

> **ECO-001 变更**：踝关节取消，仅保留 6 × STS3046。

---

通信：

```text
UART Bus
```

---

## Logic Domain

负责：

```text
控制运算

状态机

姿态估计

通信
```

---

供电：

```text
5V
```

---

设备：

```text
ESP32

IMU

调试接口
```

---

## Wheel Domain

负责：

```text
轮式移动
```

---

供电：

```text
11.1V
```

---

设备：

```text
GB37-520

Motor Driver
```

---

# 5. Controller Architecture

## Main Controller

冻结：

```text
ESP32 DevKitC-32E
```

---

参数：

| Item | Value |
|--------|--------|
| CPU | Dual Core |
| Frequency | 240MHz |
| SRAM | 520KB |
| Flash | 4MB+ |
| WiFi | Yes |
| Bluetooth | Yes |

---

原因：

```text
性能充足

价格低

开发生态成熟
```

---

# 6. Sensor Architecture

## IMU

冻结：

```text
ICM42688-P
```

---

功能：

```text
Pitch

Roll

Angular Velocity
```

---

接口：

```text
I2C
```

---

速率：

```text
400kHz
```

---

安装位置：

```text
Pelvis Center

骨盆中心
```

---

原因：

最接近机器人重心。

---

# 7. Servo Architecture

## Servo Configuration

| Joint | Servo |
|---------|---------|
| Hip Roll | STS3046 |
| Hip Pitch | STS3046 |
| Knee | STS3046 |

> **ECO-001 变更**：踝关节已移除（DR-011），Ankle 行取消。

---

数量：

| Servo | Qty |
|---------|---------:|
| STS3046 | 6 |

> **ECO-001 变更**：踝关节取消，仅 6 × STS3046。

---

Total:

```text
8 Servos
```

---

# 8. Servo Communication Bus

采用：

```text
Half Duplex UART
```

---

拓扑：

```text

ESP32

  │

  ├──────── Servo Bus ────────┐

  │                           │

Servo1 → Servo2 → Servo3 → Servo4

Servo5 → Servo6 → Servo7 → Servo8

```

---

波特率：

```text
1 Mbps
```

---

原因：

满足：

```text
100Hz Control Loop
```

需求。

---

# 9. Wheel Drive Architecture

## Wheel Motor

冻结：

```text
GB37-520
```

---

数量：

```text
2
```

---

供电：

```text
11.1V Direct
```

---

控制：

```text
PWM
```

---

驱动器：

```text
DRV8871
```

---

# 10. Power Architecture

## Battery

冻结：

```text
3S2P Li-ion
```

---

结构：

```text
18650 × 6
```

---

参数：

```text
11.1V Nominal

12.6V Full
```

---

容量：

```text
6000mAh
```

---

能量：

```text
66Wh
```

---

# 11. Power Rails

## Servo Rail

| Item | Value |
|--------|--------|
| Voltage | 7.4V |
| Continuous | 15A |
| Peak | 20A |

---

## Logic Rail

| Item | Value |
|--------|--------|
| Voltage | 5V |
| Current | 3A |

---

## Wheel Rail

| Item | Value |
|--------|--------|
| Voltage | 11.1V |
| Current | 10A Peak |

---

# 12. Power Distribution

采用：

```text
Star Topology

星型供电
```

---

结构：

```text

Battery

   │

   PDB

 ┌─┼─┐

Servo

Logic

Wheel

```

---

禁止：

```text
Daisy Chain

串联供电
```

---

# 13. Ground Strategy

采用：

```text
Single Point Ground

单点接地
```

---

结构：

```text

Battery -

      │

     PDB

 ┌────┼────┐

Servo Logic Wheel

```

---

目的：

```text
降低噪声

避免地环路
```

---

# 14. Safety Architecture

## Fuse

主保险丝：

```text
20A Slow Blow
```

---

## Emergency Stop

触发：

```text
Button

Software

OTA
```

---

动作：

```text
Disable Servo Rail

Stop Wheel Motors
```

---

## Watchdog

采用：

```text
ESP32 Watchdog
```

---

超时：

```text
500ms
```

---

# 15. Mechanical-Electrical Interface

## Pelvis

安装：

```text
Battery

ESP32

PDB

Buck Converter
```

---

## Thigh

安装：

```text
Servo Wiring
```

---

## Calf

安装：

```text
Servo Wiring

Wheel Wiring
```

---

## Foot

安装：

```text
Wheel Motor
```

---

# 16. Signal Interface Allocation

## UART Bus

| Signal | GPIO |
|----------|----------|
| TX | GPIO17 |
| RX | GPIO16 |

---

## I2C

| Signal | GPIO |
|----------|----------|
| SDA | GPIO21 |
| SCL | GPIO22 |

---

## Wheel PWM

| Signal | GPIO |
|----------|----------|
| Left PWM | GPIO25 |
| Right PWM | GPIO26 |

---

## Battery ADC

| Signal | GPIO |
|----------|----------|
| VBAT Sense | GPIO34 |

---

# 17. Future Expansion Interface

预留：

```text
UART1

SPI

I2C Expansion
```

---

用于：

```text
Camera

Lidar

Raspberry Pi

ROS2 Bridge
```

---

# 18. Electrical BOM Summary

| Item | Model | Qty |
|--------|--------|---------:|
| Controller | ESP32 DevKitC-32E | 1 |
| IMU | ICM42688-P | 1 |
| STS3046 | Servo | 6 |
| Wheel Motor | GB37-520 | 2 |
| Motor Driver | DRV8871 | 1 |
| Battery | Samsung 30Q | 6 |
| XT30 | Amass XT30U | 2 |
| Fuse | 20A ATO | 1 |

> **ECO-001 变更**：踝关节取消，移除 STS3215；轮驱 IC 统一为 DRV8871。
| Battery | Samsung 30Q | 6 |
| XT30 | Amass XT30U | 2 |
| Fuse | 20A ATO | 1 |

---

# 19. Freeze Summary

## Controller

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
```

---

## Wheel Driver

```text
DRV8871
```

---

## Battery

```text
3S2P Samsung 30Q
```

---

## Power Rails

```text
7.4V Servo

5V Logic

11.1V Wheel
```

---

## Safety

```text
Fuse

Emergency Stop

Watchdog
```

---

Status:

```text
APPROVED

READY FOR EDS-02
```
