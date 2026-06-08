# Mini-Atlas V6 Alpha

# CDS-05A Knee Base CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0020

Part Name:

Knee_Base

Parent Assembly:

V6-ASM-0003 Knee Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* DR-009 Knee Architecture Review
* DR-009A Knee Servo Orientation Review
* CDS-04D HipPitch Assembly Verification
* CDS-02A Standard Component Library Revision A
* MDS-02 Detailed Joint Design

---

# 1. Purpose

Knee_Base 为 Knee Joint（膝关节）固定端结构。

主要职责：

* 安装 STS3046 Servo
* 支撑 Knee Joint Shaft
* 支撑 698 Bearings
* 提供 Hip Pitch 输出端连接接口
* 提供 Mechanical Stop
* 提供线束通道
* 提供维护拆装空间

---

Knee_Base 不参与运动。

属于：

Fixed Structure（固定结构件）

---

# 2. Design Philosophy

遵循 V6 Alpha 全局原则：

Weight Path

与

Torque Path

分离

---

重量路径：

Robot Weight

↓

Lower Leg

↓

Knee Output

↓

Joint Shaft

↓

698 Bearings

↓

Knee Base

↓

Upper Leg

---

扭矩路径：

STS3046

↓

Servo Horn

↓

Torque Module

↓

Knee Output

---

Servo 不承担结构重量。

---

# 3. Coordinate System

全局坐标：

X+

Forward（前）

Y+

Left（左）

Z+

Up（上）

---

Knee Rotation Axis：

Y Axis

---

Rotation Center：

Knee Joint Center

---

# 4. Overall Dimensions

设计目标：

Width

50 mm

---

Height

60 mm

---

Depth

35 mm

---

允许公差：

±2 mm

---

目标重量：

<45 g

---

# 5. Architecture

采用：

Bearing Supported Knee

---

结构：

Upper Leg

↓

Knee_Base

↓

698 Bearings

↓

Knee_Output

↓

Lower Leg

---

Servo：

Parallel Layout

与腿方向平行

---

# 6. Hip Pitch Interface

连接对象：

HipPitch_Output

---

连接方式：

Leg Adapter Standard

---

接口：

4 × M3

---

孔径：

Ø3.2 mm

---

孔距：

30 × 30 mm

---

Front View

●──────●

│      │

│      │

●──────●

---

兼容：

CDS-04B HipPitch_Output

---

# 7. Bearing Configuration

采用：

698-2RS

数量：

2

---

规格：

8 × 19 × 6 mm

---

安装方式：

双轴承支撑

---

剖面：

[698]

|

| 8mm Shaft |

|

[698]

---

轴承间距：

18 mm

---

目标：

提高抗弯能力

降低摆动

---

# 8. Bearing Seat

轴承外径：

19 mm

---

孔设计：

19.05 mm

---

配合：

轻压入

Press Fit

---

孔深：

6.2 mm

---

两侧对称

---

# 9. Joint Shaft Interface

轴：

Ø8 mm

---

材料：

GCr15

轴承钢

---

长度：

35 mm

---

安装方式：

双轴承支撑

---

目标：

径向间隙

<0.2 mm

---

# 10. Servo Installation

冻结：

STS3046

---

安装方向：

Parallel Layout

---

示意：

Side View

┌─────────┐
│STS3046  │
└─────────┘

```
  │
```

Knee Axis

```
  │
```

Lower Leg

---

安装孔：

4 × M2.5

---

兼容：

标准 STS3046 支架孔位

---

# 11. Servo Maintenance Clearance

要求：

Servo 可独立拆卸

---

拆卸无需：

* 拆轴承
* 拆输出端

---

维护时间：

<5 min

---

# 12. Mechanical Stop

必须配置：

Mechanical Stop

---

工作范围：

0°

↓

120°

---

机械极限：

-5°

↓

125°

---

结构：

Base Stop Block

↓

Output Stop Tab

---

厚度：

4 mm

---

接触长度：

8 mm

---

# 13. Structural Reinforcement

采用：

Triangular Rib

三角加强筋

---

数量：

4

---

厚度：

3 mm

---

长度：

15 mm

---

位置：

Bearing Seat

↓

Servo Mount

---

作用：

提高刚度

降低变形

---

# 14. Wire Harness Routing

预留：

Servo Cable

UART Bus

Future IMU Cable

---

通孔：

Ø8 mm

---

位置：

Servo 后侧

---

要求：

运动过程中不夹线

---

# 15. Brass Insert Layout

采用：

M3 Brass Insert

---

数量：

8

---

位置：

Hip Interface

4

Servo Cover

2

Torque Cover

2

---

孔径：

4.2 mm

---

孔深：

5 mm

---

# 16. Printing Specification

材料：

PETG

---

层高：

0.20 mm

---

Wall：

4

---

Top：

5

---

Bottom：

5

---

Infill：

40%

Gyroid

---

# 17. Printing Orientation

推荐：

Bearing Seat Up

---

示意：

```
  Bearing

     ▲

     │
```

┌────────────────┐
│                │
│   Knee_Base    │
│                │
└────────────────┘

════════════════════

Build Plate

---

目的：

保证：

* 轴承孔精度
* Servo孔精度
* Interface孔精度

---

# 18. Weight Estimate

| Component | Weight |
| --------- | -----: |
| PETG Body |   32 g |
| Inserts   |    4 g |
| Screws    |    5 g |

---

Total

≈41 g

---

目标：

<45 g

---

结果：

PASS

---

# 19. Assembly Sequence

Step 1

安装 Brass Inserts

---

Step 2

安装 698 Bearings

---

Step 3

安装 Servo

---

Step 4

安装 Joint Shaft

---

Step 5

安装 Knee Output

---

Step 6

安装 Torque Module

---

Step 7

安装 Carbon Tube

---

# 20. Verification Checklist

CAD检查：

□ Bearing Seat正确

□ Servo孔位正确

□ Hip Interface正确

□ Wire Routing正确

□ 无干涉

---

打印检查：

□ 轴承压入正常

□ Servo安装正常

□ Insert牢固

□ 无裂纹

---

装配检查：

□ Rotation Smooth

□ 无晃动

□ 无偏心

□ Servo可维护

---

# 21. Freeze Summary

Part Number

V6-PRT-0020

---

Part Name

Knee_Base

---

Bearing

698-2RS ×2

---

Joint Shaft

Ø8 GCr15

---

Servo

STS3046

---

Architecture

Parallel Layout

---

Motion Range

0°~120°

---

Mechanical Limit

-5°~125°

---

Weight

≈41 g

---

Status

APPROVED

READY FOR

CDS-05B-Knee_Output-CAD-Design.md
