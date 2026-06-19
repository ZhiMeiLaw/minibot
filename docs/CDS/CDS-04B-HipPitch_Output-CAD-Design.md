# Mini-Atlas V6 Alpha

# CDS-04B HipPitch_Output CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0011

Part Name:

HipPitch_Output

Parent Assembly:

V6-ASM-0002 Hip Pitch Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- CDS-04 Hip Pitch Joint CAD Design
- CDS-04A HipPitch_Base CAD Design
- CDS-03C Torque-Transfer-Module CAD Design
- CDS-02A Standard Component Library Revision A
- MDS-02 Detailed Joint Design

---

# 1. Purpose

HipPitch_Output 为 Hip Pitch 关节的运动输出端（Moving Side）。

主要职责：

- 承接 Hip Pitch 关节输出扭矩
- 支撑 Upper Leg（大腿）
- 安装 Joint Shaft
- 连接 Torque Transfer Module
- 提供 Leg Adapter 安装接口
- 提供 Mechanical Stop 接触面

HipPitch_Output 是整个下肢动力链的起点。

---

载荷链：

Wheel Module

↓

Lower Leg

↓

Knee

↓

Upper Leg

↓

HipPitch_Output

↓

Joint Shaft

↓

698 Bearings

↓

HipPitch_Base

---

# 2. Design Philosophy

设计原则：

Servo Generates Torque

Servo Does NOT Carry Weight

---

正确结构：

Weight

↓

HipPitch_Output

↓

Joint Shaft

↓

698 Bearings

↓

HipPitch_Base

---

禁止：

Weight

↓

Horn

↓

Servo

---

# 3. Coordinate System

采用全局坐标系：

X+

Forward

Y+

Left

Z+

Up

---

Hip Pitch Rotation Axis：

Y Axis

---

Rotation Center：

Hip Pitch Joint Center

---

# 4. Overall Dimensions

目标尺寸：

| Parameter | Value |
|------------|--------|
| Width | 50 mm |
| Height | 55 mm |
| Depth | 35 mm |

---

允许：

±3 mm

---

重量目标：

<30 g

---

# 5. Main Structure

结构形式：

Fork Type Output Frame

叉形输出架

---

示意：

Front View

         Leg Adapter

              │

              │

      ┌───────┴───────┐

      │               │

      │ HipPitchOutput│

      │               │

      └───────┬───────┘

              │

          Shaft Boss

---

优势：

- 刚度高
- 打印简单
- 易装配
- 易维护

---

# 6. 698 Bearing Interface

采用：

698-2RS ×2

---

规格：

8 × 19 × 6 mm

---

轴承安装于：

HipPitch_Base

---

Output部分提供：

Shaft Boss

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

Boss外径：

22 mm

---

加强厚度：

5 mm

---

# 7. Joint Shaft Interface

Joint Shaft：

Ø8 GCr15

---

长度：

32 mm

---

结构：

Double Bearing Supported

---

设计目标：

消除晃动

提高抗弯能力

---

# 8. Torque Module Interface

连接：

Torque Transfer Module

↓

HipPitch_Output

---

连接方式：

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

Top View

      ●

  ●       ●

      ○

  ●       ●

---

中心：

Joint Axis

---

# 9. Leg Adapter Interface

冻结：

Leg Adapter Required

---

不允许：

Carbon Tube

直接连接 Output

---

结构：

HipPitch_Output

↓

Leg Adapter

↓

Carbon Tube

---

优势：

后续腿长可快速调整。

---

# 10. Leg Adapter Standard

标准接口：

4 × M3

---

孔径：

Ø3.2 mm

---

孔距：

30 × 30 mm

---

示意：

●──────●

│      │

│      │

●──────●

---

兼容：

未来 Knee Base

---

# 11. Carbon Tube Standard

冻结：

Carbon Tube

8 × 10 mm

---

可见长度：

120 mm

---

切割长度：

150 mm

---

计算：

Hip Pitch Insert

15 mm

+

Visible Length

120 mm

+

Knee Insert

15 mm

=

150 mm

---

# 12. Carbon Tube Clamp

采用：

Dual Bolt Clamp

双螺丝夹紧

---

结构：

Cross Section

      M3

       ▼

 ┌───────────┐
 │           │
 │ Carbon    │
 │ Tube      │
 │           │
 └─────┬─────┘
       │
      M3

---

夹缝：

2.0 mm

> 原 1.5mm 偏紧，放宽至 2.0mm 以保证可靠夹紧（考虑碳管外径 ±0.2mm 公差）。

---

夹紧螺丝：

M3 × 16

---

数量：

2

---

铜螺母：

M3 Brass Insert

---

# 13. Mechanical Stop

必须配置：

Mechanical Stop

---

工作范围：

Forward

+60°

---

Backward

-30°

---

机械极限：

Forward

+65°

---

Backward

-35°

---

安全余量：

5°

---

# 14. Mechanical Stop Geometry

Output侧：

Stop Tab

---

Base侧：

Stop Block

---

示意：

      Stop Tab

          ▼

 ┌────────────┐
 │            │
 │  Output    │
 │            │
 └─────┬──────┘
       │
       │
 Stop Block

---

接触面厚度：

4 mm

---

接触长度：

8 mm

---

# 15. Structural Reinforcement

增加：

Triangular Rib

三角加强筋

---

位置：

Leg Adapter

↓

Shaft Boss

---

厚度：

3 mm

---

长度：

15 mm

---

作用：

提高抗弯能力

---

# 16. Wire Routing

预留：

Knee Servo Cable

---

通孔：

Ø8 mm

---

位置：

Carbon Tube Interface 后方

---

用途：

- Servo Cable
- IMU Cable
- Future Sensor Cable

---

# 17. Printing Specification

材料：

PETG

---

层高：

0.20 mm

---

Wall Count：

4

---

Top Layer：

5

---

Bottom Layer：

5

---

Infill：

40%

Gyroid

---

# 18. Printing Orientation

推荐：

Leg Adapter Interface

朝上

---

示意：

      Clamp

        ▲

        │

 ┌─────────────┐
 │             │
 │ HipPitchOut │
 │             │
 └─────────────┘

════════════════════

Build Plate

---

目的：

保证：

- Shaft Boss精度
- Clamp精度
- Stop精度

---

# 19. Weight Estimate

| Component | Weight |
|------------|--------:|
| PETG Body | 22 g |
| Inserts | 3 g |
| Screws | 4 g |

---

总计：

≈29 g

---

目标：

<30 g

---

结果：

PASS

---

# 20. Assembly Sequence

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

# 21. Verification Checklist

CAD检查：

□ Shaft Boss正确

□ Torque Interface正确

□ Leg Adapter Interface正确

□ Clamp可工作

□ 无干涉

□ ±60°前摆

□ -30°后摆

---

打印检查：

□ Carbon Tube可插入

□ Clamp可锁紧

□ Insert正常

□ 无裂纹

---

装配检查：

□ 无晃动

□ 无打滑

□ Stop正常

□ Torque正常传递

□ Carbon Tube不滑动

---

# 22. Freeze Summary

Part Number

V6-PRT-0011

---

Part Name

HipPitch_Output

---

Bearing Interface

698-2RS ×2

---

Joint Shaft

Ø8 GCr15

---

Leg Adapter

Required

---

Carbon Tube

8 × 10 mm

---

Visible Length

120 mm

---

Cut Length

150 mm

---

Clamp

Dual Bolt Clamp

---

Motion Range

+60°

-30°

---

Weight

≈29 g

---

Status

APPROVED

READY FOR

CDS-04C-HipPitch-Torque-Transfer-Module-CAD-Design.md