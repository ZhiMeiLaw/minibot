# Mini-Atlas V6 Alpha

# MDS-04 Pelvis & Electronics Assembly Specification

## 骨盆与电子系统装配规范

Version: v0.1 Freeze A

Status: APPROVED

---

# 1. Introduction（简介）

本文档定义：

* Pelvis Assembly（骨盆总成）
* Battery Bay（电池仓）
* Electronics Bay（电子舱）
* Wire Routing（线束系统）
* Power Distribution（电源分配）
* Thermal Design（散热设计）
* Serviceability（维护设计）

目标：

```text
Compact

Lightweight

Service Friendly

Low Center Of Mass
```

---

# 2. Pelvis Assembly（骨盆总成）

---

## 2.1 Function（功能）

骨盆是整机核心承力结构。

负责连接：

```text
Left Hip Roll

Right Hip Roll

Battery

Electronics

Power System
```

---

## 2.2 Design Freeze

外形尺寸：

```text
Width  = 120 mm

Depth  = 80 mm

Height = 60 mm
```

---

## 2.3 Structure

采用：

```text
Box Frame

箱式结构
```

---

结构示意：

```text
Front

┌─────────────────┐

│ Electronics Bay │

├─────────────────┤

│  Battery Bay    │

└─────────────────┘

Rear
```

---

设计原则：

```text
Battery Below

Electronics Above
```

---

# 3. Battery Bay（电池仓）

---

## 3.1 Battery Freeze

冻结：

```text
3S Li-ion

11.1V
```

---

推荐规格：

```text
18650 × 3

or

18650 × 6
```

---

推荐容量：

```text
2500~3500mAh
```

---

## 3.2 Location

必须位于：

```text
Pelvis Bottom
骨盆下层
```

---

原因：

```text
Lower Center Of Mass
降低重心
```

---

## 3.3 Battery Tray

采用：

```text
Slide-In Tray

抽拉式电池托盘
```

---

结构：

```text
Rear Hatch

     │

Battery Tray

     │

Lock Tab
```

---

目标：

```text
Battery Replacement

<30 Seconds
```

---

# 4. Electronics Bay（电子舱）

---

位于：

```text
Battery Bay Upper Side
```

---

结构：

```text
Top Cover

   │

Electronics Plate

   │

Battery Bay
```

---

# 5. ESP32 Mounting Plate

---

## Controller Freeze

```text
ESP32 DevKitC-32E
```

---

安装方式：

```text
4-Point Mount
```

---

固定件：

```text
M3 Nylon Standoff

M3 Spacer
```

---

高度：

```text
10 mm
```

---

原因：

```text
Improve Air Flow

避免短路
```

---

# 6. Power Distribution Board（PDB）

---

## Function

负责：

```text
Battery Input

Power Distribution

Fuse

Voltage Monitoring
```

---

## Location

位于：

```text
ESP32 Rear Side
```

---

布局：

```text
ESP32

  │

 PDB

  │

Battery
```

---

# 7. Buck Converter Assembly

---

## Servo Rail

转换：

```text
11.1V

↓

7.4V
```

---

输出能力：

```text
15A Continuous
```

---

## Logic Rail

转换：

```text
11.1V

↓

5V
```

---

输出能力：

```text
3A Continuous
```

---

## Location

位于：

```text
Left Side

Right Side
```

分离安装。

---

避免：

```text
Thermal Concentration
热量集中
```

---

# 8. IMU Installation

---

## Sensor Freeze

推荐：

```text
ICM42688
```

---

## Location

必须：

```text
Robot Centerline

机器人中心线
```

---

推荐：

```text
Pelvis Geometric Center
```

---

原因：

```text
Reduce Rotational Error
```

---

## Orientation

规定：

```text
+X Forward

+Y Left

+Z Up
```

---

# 9. Main Power Switch

---

采用：

```text
Physical Switch

实体电源开关
```

---

位置：

```text
Rear Panel
```

---

要求：

```text
Accessible Without Disassembly
```

---

# 10. XT30 / XT60 Standard

---

## Battery Connector

V6 Freeze：

```text
XT30
```

---

原因：

```text
Smaller

Lighter

Enough Current
```

---

禁止：

```text
Dupont Power Connector
```

---

# 11. Wire Harness Routing

## 线束系统

---

原则：

```text
No External Cable
```

---

目标：

```text
All Internal Routing
```

---

# Main Routing

```text
Pelvis

  │

Thigh Tube

  │

Calf Tube

  │

Ankle
```

---

## Tube Entry Hole

孔径：

```text
6 mm
```

---

孔边：

```text
Chamfer Required
```

---

# 12. Center Of Mass Design

## 重心设计

---

目标：

```text
COM Inside Pelvis
```

---

位置：

```text
Near Hip Axis
```

---

推荐：

```text
10~20 mm Below Hip Pitch Axis
```

---

结构示意：

```text
Hip Axis

──────────────

     COM

      ●

Battery

███████
```

---

## Weight Priority

```text
Battery

↓

Wheel Motor

↓

Servo

↓

Electronics
```

---

最重部件必须最低。

---

# 13. Thermal Design（散热设计）

---

## Ventilation

骨盆两侧：

```text
Vent Slots
```

---

建议：

```text
3 × 20 mm
```

通风槽。

---

## Buck Cooling

降压模块：

```text
Natural Convection
```

---

禁止：

```text
Closed Box Design
```

---

# 14. Service Hatch（维护开口）

---

## Rear Hatch

骨盆后部：

```text
Removable Cover
```

---

固定：

```text
4 × M3
```

---

打开后可访问：

```text
Battery

XT30

Power Switch

Fuse
```

---

## Top Hatch

顶部盖板：

```text
4 × M3
```

---

打开后可访问：

```text
ESP32

PDB

Buck Converter

IMU
```

---

# 15. Wiring BOM

---

## Power

| Item        | Qty |
| ----------- | --: |
| XT30 Male   |   1 |
| XT30 Female |   1 |
| Main Switch |   1 |
| Fuse Holder |   1 |

---

## Signal

| Item            | Qty |
| --------------- | --: |
| Servo Extension |   8 |
| IMU Cable       |   1 |

---

## Power Conversion

| Item      | Qty |
| --------- | --: |
| 7.4V Buck |   1 |
| 5V Buck   |   1 |

---

# 16. Serviceability Requirements

---

## Battery Swap

目标：

```text
<30 Seconds
```

---

## ESP32 Replacement

目标：

```text
<10 Minutes
```

---

## Buck Replacement

目标：

```text
<10 Minutes
```

---

## IMU Replacement

目标：

```text
<15 Minutes
```

---

# 17. Final Freeze Summary

## Pelvis

```text
120 × 80 × 60 mm
```

---

## Battery

```text
3S Li-ion

XT30
```

---

## Controller

```text
ESP32 DevKitC-32E
```

---

## IMU

```text
ICM42688
```

---

## Power

```text
11.1V Battery

7.4V Servo Rail

5V Logic Rail
```

---

## Wiring

```text
Internal Routing

Carbon Tube
```

---

## COM

```text
10~20 mm Below Hip Axis
```

---

# Engineering Approval

Status:

```text
APPROVED
```

Revision:

```text
Freeze A
```

This document is authorized for:

* Pelvis CAD Design
* Electronics Layout
* Prototype Manufacturing
* System Integration

---

# End Of Document
