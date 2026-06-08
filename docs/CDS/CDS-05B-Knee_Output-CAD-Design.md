# Mini-Atlas V6 Alpha

# CDS-05B Knee Output CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0021

Part Name:

Knee_Output

Parent Assembly:

V6-ASM-0003 Knee Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

* CDS-05A Knee Base CAD Design
* DR-009 Knee Architecture Review
* DR-009A Knee Servo Orientation Review
* CDS-02A Standard Component Library Revision A

---

# 1. Purpose

Knee_Output 为 Knee Joint 运动输出端。

主要职责：

* 承接 Knee Servo 输出扭矩
* 支撑 Lower Leg
* 提供 Carbon Tube Interface
* 提供 Torque Module Interface
* 提供 Mechanical Stop Tab
* 支撑 Knee Joint Shaft

---

Knee_Output 是：

Knee Joint

↓

Lower Leg

之间的主要承力结构。

---

# 2. Design Philosophy

设计原则：

Weight Path

与

Torque Path

分离

---

重量路径：

Robot Weight

↓

Wheel Module

↓

Lower Leg

↓

Knee_Output

↓

Joint Shaft

↓

698 Bearings

↓

Knee_Base

---

扭矩路径：

STS3046

↓

Servo Horn

↓

Torque Module

↓

Knee_Output

---

# 3. Coordinate System

X+

Forward

---

Y+

Left

---

Z+

Up

---

Rotation Axis：

Y Axis

---

Joint Center：

Knee Rotation Center

---

# 4. Overall Dimensions

目标尺寸：

Width

50 mm

---

Height

60 mm

---

Depth

35 mm

---

目标重量：

<35 g

---

允许：

±2 mm

---

# 5. Main Architecture

采用：

Fork Type Output Frame

叉型输出架

---

结构：

```
  Lower Leg

       │

       │

┌──────┴──────┐

│ KneeOutput  │

└──────┬──────┘

       │

  Shaft Boss
```

---

优点：

高刚度

低重量

易打印

易装配

---

# 6. Bearing Interface

对应：

698-2RS ×2

---

轴承安装于：

Knee_Base

---

Output 提供：

Joint Shaft Boss

---

中心孔：

Ø8.10 mm

---

配合：

Slip Fit

---

孔深：

12 mm

---

# 7. Shaft Boss

Knee 比 Hip Pitch 载荷更高。

因此升级：

Hip Pitch

Ø22 mm

↓

Knee

Ø24 mm

---

Boss 外径：

24 mm

---

Boss 长度：

12 mm

---

加强厚度：

5 mm

---

作用：

提高抗弯刚度

降低疲劳风险

---

# 8. Torque Interface

连接：

Torque Module

↓

Knee_Output

---

方式：

4 × M3

---

孔径：

Ø3.2 mm

---

PCD：

18 mm

---

均布：

90°

---

示意：

```
  ●
```

●       ●

```
  ○
```

●       ●

---

中心：

Knee Axis

---

# 9. Lower Leg Interface

冻结：

Leg Adapter Required

---

禁止：

Carbon Tube

直接连接 Output

---

结构：

Knee_Output

↓

Leg Adapter

↓

Carbon Tube

---

优势：

腿长后期可调整

维护方便

兼容升级

---

# 10. Lower Leg Standard

采用：

8 × 10 mm Carbon Tube

---

Visible Length

120 mm

---

Cut Length

150 mm

---

计算：

Insert

15 mm

*

Visible

120 mm

*

Insert

15 mm

=

150 mm

---

# 11. Carbon Tube Clamp

升级方案：

Anti-Slip Clamp

防滑夹紧结构

---

结构：

双M3夹紧

*

防滑齿纹

---

示意：

Cross Section

```
 M3

  ▼
```

┌──────────┐
│/////│
│ Carbon   │
│  Tube    │
│/////\│
└────┬─────┘
│
M3

---

# 12. Clamp Specification

Clamp Gap：

1.5 mm

---

Clamp Screw：

M3 ×16

---

数量：

2

---

Brass Insert：

M3

---

数量：

2

---

# 13. Mechanical Stop Tab

Output侧：

Stop Tab

---

Base侧：

Stop Block

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

Stop Tab 厚度：

4 mm

---

接触长度：

8 mm

---

# 14. Structural Reinforcement

增加：

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

18 mm

---

位置：

Shaft Boss

↓

Leg Adapter

---

目的：

提高疲劳寿命

---

# 15. Wire Routing

预留：

Servo Cable

UART Bus

IMU Extension

---

通孔：

Ø8 mm

---

位置：

Carbon Tube Interface 后方

---

# 16. Printing Specification

材料：

PETG

---

Layer Height：

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

Shaft Boss 朝上

---

示意：

```
  Boss

   ▲

   │
```

┌───────────┐
│ KneeOutput│
└───────────┘

════════════════════

Build Plate

---

目的：

提高孔精度

---

# 18. Weight Estimate

| Component | Weight |
| --------- | -----: |
| PETG Body |   24 g |
| Inserts   |    3 g |
| Screws    |    4 g |

---

Total

≈31 g

---

目标：

<35 g

---

结果：

PASS

---

# 19. Assembly Sequence

Step 1

安装 Brass Insert

---

Step 2

安装 Leg Adapter

---

Step 3

安装 Clamp Screw

---

Step 4

插入 Joint Shaft

---

Step 5

安装 Torque Module

---

Step 6

安装 Carbon Tube

---

Step 7

锁紧 Clamp

---

# 20. Verification Checklist

CAD检查：

□ Shaft Boss正确

□ Torque Interface正确

□ Clamp正确

□ Stop Tab正确

□ 无干涉

---

打印检查：

□ Carbon Tube正常插入

□ Clamp正常锁紧

□ Insert牢固

□ 无裂纹

---

装配检查：

□ Rotation Smooth

□ 无晃动

□ 无偏心

□ 无打滑

---

# 21. Fatigue Verification Target

目标：

100,000 Cycles

---

检查：

□ Clamp 不松动

□ Shaft Boss 无裂纹

□ Rib 无裂纹

□ Carbon Tube 无滑移

---

# 22. Freeze Summary

Part Number

V6-PRT-0021

---

Part Name

Knee_Output

---

Bearing Interface

698-2RS ×2

---

Joint Shaft

Ø8 GCr15

---

Shaft Boss

Ø24 mm

---

Carbon Tube

8 × 10 mm

---

Clamp

Dual M3 Anti-Slip

---

Motion Range

0°~120°

---

Mechanical Limit

-5°~125°

---

Weight

≈31 g

---

Status

APPROVED

READY FOR

CDS-05C-Knee-Torque-Transfer-Module-CAD-Design.md
