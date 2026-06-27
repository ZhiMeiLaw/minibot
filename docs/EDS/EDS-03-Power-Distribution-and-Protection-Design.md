# Mini-Atlas V6 Alpha

# EDS-03 Power Distribution & Protection Design

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

- Power Distribution（电源分配）
- Protection Design（保护设计）
- Fuse Selection（保险丝选型）
- Connector Selection（连接器选型）
- Grounding Strategy（接地策略）
- Soft Start（软启动）
- Power Sequencing（上电时序）
- Fault Protection（故障保护）

本文件目标：

```text
确保机器人在大电流动态负载下
仍然能够安全可靠运行
```

---

# 2. Design Philosophy

采用：

```text
Fail Safe Design

故障安全设计
```

原则：

1. 单个器件故障不应导致起火
2. 电池短路必须被保护
3. 舵机异常不得损坏主控
4. 主控异常不得导致机器人失控
5. 故障必须可诊断

---

# 3. Power Topology

## System Overview

```text

          3S2P Battery
          (11.1V)

               │

          Main Fuse

               │

        Main Power Switch

               │

              PDB

     ┌─────────┼─────────┐

     │         │         │

 Servo Buck  Logic    Wheel

    7.4V      5V      11.1V

     │         │         │

 Servo Bus   ESP32   DRV8871

```

---

# 4. Power Distribution Board (PDB)

## Function

PDB（Power Distribution Board）

负责：

```text
电源输入

保险丝安装

电源分配

电压监测

接地汇流
```

---

## Input

```text
Battery 11.1V
```

---

## Outputs

### Servo Rail

```text
7.4V
```

---

### Logic Rail

```text
5V
```

---

### Wheel Rail

```text
11.1V
```

---

# 5. Ground Strategy

采用：

```text
Single Point Ground

单点接地
```

---

## Layout

```text

Battery -

     │

    PDB

 ┌───┼───┐

Servo Logic Wheel

```

---

禁止：

```text
Ground Daisy Chain

地线串联
```

---

原因：

避免：

```text
Ground Bounce

Ground Loop

IMU Noise
```

---

# 6. Main Fuse Analysis

## Previous Design Review

EDS-02 中：

```text
20A Fuse
```

---

重新分析：

系统峰值：

```text
18.5A
```

---

保险丝工作原则：

```text
持续工作电流

≤

额定值 80%
```

---

20A Fuse：

```text
16A Continuous
```

---

存在误动作风险。

---

# Freeze Update

主保险丝升级：

```text
25A Slow Blow
```

---

推荐型号：

```text
ATO Blade Fuse
```

---

# 7. XT30 Evaluation

## Current Requirement

系统峰值：

```text
18~20A
```

---

XT30额定：

```text
30A Continuous
```

---

结论：

```text
完全满足需求
```

---

# Freeze

保持：

```text
XT30
```

---

无需升级 XT60。

---

原因：

### XT60

优点：

```text
更大余量
```

缺点：

```text
更重

更大

更贵
```

---

对于 V6 Alpha：

```text
XT30 最优
```

---

# 8. Servo Power Architecture

## Option A

单 Buck

```text

Battery

   │

20A Buck

   │

All Servos

```

---

优点：

```text
简单

成本低
```

---

缺点：

```text
单点故障
```

---

## Option B

双 Buck

```text

Battery

   │

 ┌─┴─┐

BuckA BuckB

 │      │

Left   Right

Leg    Leg

```

---

优点：

```text
冗余

故障隔离
```

---

缺点：

```text
成本增加
```

---

# Freeze

V6 Alpha：

```text
Single Buck
```

---

V6 Beta：

```text
Dual Buck
```

---

# 9. Servo Soft Start

## Problem

STS3046 上电瞬间：

```text
同时初始化
```

可能产生：

```text
10A+

Inrush Current
```

---

导致：

```text
Buck Reset

Voltage Dip
```

---

# Solution

采用：

```text
Servo Rail Soft Start
```

---

方法：

MOSFET控制上电

```text

ESP32

  │

MOSFET

  │

Servo Rail

```

---

上电顺序：

```text
Power On

↓

ESP32 Boot

↓

Buck Stable

↓

Enable Servo Rail

```

---

延时：

```text
500ms
```

---

# Freeze

```text
Required
```

---

# 10. Reverse Polarity Protection

## Requirement

防止：

```text
电池接反
```

---

方案

### Schottky

淘汰

原因：

```text
损耗大
```

---

### MOSFET Reverse Protection

采用

---

结构：

```text

Battery

  │

P-MOS

  │

PDB

```

---

优点：

```text
损耗极低
```

---

# Freeze

```text
MOSFET Reverse Protection
```

---

# 11. Voltage Monitoring

## Purpose

监测：

```text
电池电压
```

---

结构：

```text

Battery

   │

Divider

   │

ESP32 ADC

```

---

分压：

```text
100k

33k
```

---

量程：

```text
0~15V
```

---

# Low Battery Threshold

## Warning

```text
10.5V
```

---

## Critical

```text
9.9V
```

---

动作：

```text
禁止步态

仅允许停车
```

---

# 12. Over Current Protection

## Servo Rail

保护目标：

```text
Buck

Wiring

Battery
```

---

方法：

```text
Fuse
```

+

```text
Software Monitor
```

---

# Wheel Rail

保护：

```text
Driver Current Limit
```

---

DRV8871：

内部保护。

---

# 13. Wire Harness Protection

## Requirement

所有线束：

```text
不可直接接触碳管边缘
```

---

采用：

```text
PET Braided Sleeve

编织网管
```

---

固定：

```text
Zip Tie

Cable Clamp
```

---

# 14. Power Sequencing

## Power ON

```text

Battery

↓

Switch ON

↓

ESP32 Start

↓

Buck Stable

↓

IMU Init

↓

Servo Enable

↓

Stand Mode

```

---

## Power OFF

```text

Standby

↓

Disable Servo

↓

Stop Wheel

↓

Power Off

```

---

# 15. Emergency Stop

## Trigger

### Hardware Button

---

### UART Command

---

### OTA Command

---

# Action

```text
Disable Servo Rail

Stop Wheel Motor

Enter Safe State
```

---

响应时间：

```text
<100ms
```

---

# 16. Thermal Protection

## Servo Buck

温度：

```text
>80°C
```

报警。

---

```text
>100°C
```

关闭Servo Rail。

---

## Battery

```text
>60°C
```

禁止运动。

---

# 17. Reliability Review

## XT30

PASS

---

## 25A Fuse

PASS

---

## AWG16 Servo Rail

PASS

---

## Single Buck

PASS

Alpha可接受

---

## Soft Start

MANDATORY

---

## Reverse Protection

MANDATORY

---

# 18. Design Freeze Summary

## Main Fuse

```text
25A Slow Blow
```

---

## Connector

```text
Amass XT30
```

---

## Ground

```text
Single Point Ground
```

---

## Servo Power

```text
Single 20A Buck
```

---

## Soft Start

```text
Required
```

---

## Reverse Protection

```text
MOSFET Based
```

---

## Voltage Monitoring

```text
Required
```

---

## Low Battery

```text
Warning = 10.5V

Critical = 9.9V
```

---

## Emergency Stop

```text
Required
```

---

Status:

```text
APPROVED

READY FOR EDS-04
```
