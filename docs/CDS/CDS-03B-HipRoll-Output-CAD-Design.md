# Mini-Atlas V6 Alpha

# CDS-03B HipRoll_Output CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Parent Assembly:

V6-ASM-0001 Hip Roll Assembly

Part Number:

V6-PRT-0002

Part Name:

HipRoll_Output

---

# 1. Purpose

HipRoll_Output 是 Hip Roll 关节的运动输出端（Moving Side）。

其作用：

- 与 HipRoll_Base 形成旋转关节
- 连接 Ø8 Joint Shaft
- 接收 STS3046 输出转矩
- 提供 Carbon Tube 安装接口
- 将 Hip Roll 动作传递到大腿（Upper Leg）

本零件是：

Hip Roll

↓

Hip Pitch

↓

Knee

整个腿部载荷链的起点。

---

# 2. Functional Requirements

必须满足：

- 承受整条腿重量
- 支持 ±25° Roll
- 与 Base 无干涉
- 安装 Carbon Tube
- 安装 Horn Hub
- 安装 Joint Shaft

---

设计寿命：

100 小时以上

Alpha Prototype

---

# 3. Coordinate System

采用 CDS-03A 坐标系：

X+

Forward（前）

Y+

Left（左）

Z+

Up（上）

---

原点：

Hip Roll Rotation Center

Joint Axis Center

---

# 4. Design Philosophy

Output Side 不允许：

Servo Direct Load

舵机直接承重

---

必须采用：

Bearing Supported Structure

轴承支撑结构

---

载荷路径：

Upper Leg
↓
Carbon Tube
↓
HipRoll_Output
↓
Ø8 Shaft
↓
688 Bearings
↓
HipRoll_Base

---

STS3046仅负责：

Torque

转矩输出

---

# 5. Overall Dimensions

建议尺寸：

Width

50 mm

Height

50 mm

Depth

35 mm

---

目标：

尽量轻量化

---

重量目标：

<25 g

---

# 6. Main Structure

采用：

Fork Type Structure

叉形结构

---

示意图：

Front View

      Carbon Tube
            │
            │
     ┌──────┴──────┐
     │             │
     │ Hip Output  │
     │             │
     └──────┬──────┘
            │
            │
         Shaft

---

优点：

- 刚度高
- 易打印
- 易安装

---

# 7. Shaft Boss Design

核心结构：

Shaft Boss

转轴座

---

孔径：

Ø8.10 mm

---

配合：

滑动配合

Slip Fit

---

孔深：

12 mm

---

轴中心：

Joint Center

---

外围加强厚度：

≥4 mm

推荐：

5 mm

---

Boss 外径：

20 mm

---

# 8. Horn Hub Interface

连接：

HipRoll_Output

↓

Horn Hub

↓

STS3046

---

接口形式：

4 Bolt Pattern

---

螺丝：

M3 × 4

---

分布：

90° 等分

---

PCD：

18 mm

---

结构：

Top View

     M3

      ●

●           ●

      ○

●           ●

      ●

中心：

Servo Axis

---

# 9. Torque Transfer Design

禁止：

仅靠摩擦传递

---

必须：

Mechanical Lock

机械锁紧

---

采用：

M3 Clamp

夹紧结构

---

安全转矩：

>5 N·m

---

远高于：

STS3046 峰值输出

---

# 10. Carbon Tube Interface

规格：

Carbon Tube

OD 10mm × ID 8mm

---

插入深度：

15 mm

---

安装方式：

Split Clamp

开口夹持

---

结构：

Cross Section

      M3 Bolt

         ▼

 ┌─────────────┐
 │             │
 │ Carbon Tube │
 │             │
 └──────┬──────┘
        │
     Clamp Gap

---

夹缝：

2.0 mm

---

锁紧螺丝：

M3 × 16

---

铜螺母：

M3 Brass Insert

---

# 11. Clamp Design

材料：

PETG

---

壁厚：

4 mm

---

夹持区域长度：

18 mm

---

禁止：

胶水固定

扎带固定

---

必须：

机械夹持

---

# 12. Structural Reinforcement

增加：

Triangular Rib

三角加强筋

---

位置：

Carbon Clamp

↓

Shaft Boss

---

厚度：

3 mm

---

长度：

15 mm

---

目的：

减少弯曲变形

---

# 13. Clearance Requirement

与 HipRoll_Base 间隙：

≥0.5 mm

---

推荐：

1.0 mm

---

避免：

打印误差干涉

---

# 14. Maintenance Access

必须满足：

Carbon Tube 可拆卸

---

拆装时间：

<3分钟

---

工具：

2.0mm Hex

---

# 15. Wire Routing

预留：

未来 Hip Pitch Servo

---

线束孔：

Ø8 mm

---

位置：

Carbon Clamp 后方

---

目的：

内部走线

---

# 16. Printing Specification

材料：

PETG

---

层高：

0.20 mm

---

壁数：

4

---

填充：

40%

Gyroid

---

顶部：

5层

---

底部：

5层

---

# 17. Printing Orientation

推荐：

Carbon Tube Interface

朝上

---

示意：

      Clamp

        ▲

        │

 ┌───────────┐
 │           │
 │ HipOutput │
 │           │
 └───────────┘

═══════════════════

Build Plate

---

优点：

- Shaft Boss 精度高
- Clamp 精度高
- 支撑最少

---

# 18. Support Strategy

允许：

Tree Support

---

仅用于：

Clamp Overhang

---

禁止：

Shaft Hole Support

---

# 19. Weight Estimate

PETG Body

≈18 g

---

Brass Inserts

≈2 g

---

Fasteners

≈3 g

---

Total

≈23 g

---

目标：

<25 g

---

# 20. Assembly Sequence

Step 1

安装 Brass Insert

---

Step 2

安装 Carbon Clamp 螺丝

---

Step 3

插入 Ø8 Shaft

---

Step 4

连接 Horn Hub

---

Step 5

安装 Carbon Tube

---

Step 6

锁紧 M3 Clamp

---

# 21. Verification Checklist

打印后：

□ Shaft 可通过

□ Carbon Tube 可插入

□ Clamp 正常锁紧

□ Brass Insert 正常

□ 无裂纹

---

装配后：

□ Roll ±25°

□ 无干涉

□ 无明显晃动

□ Torque 正常传递

□ Carbon Tube 无滑动

---

# 22. Future Compatibility

预留升级：

STS3250

STS3255

---

无需修改：

Carbon Tube Interface

---

仅修改：

Horn Hub

---

# 23. Freeze Summary

Part Number

V6-PRT-0002

---

Part Name

HipRoll_Output

---

Material

PETG

---

Weight

≈23 g

---

Shaft

Ø8

---

Bearing

688 ×2

(Installed In Base)

---

Carbon Tube

OD 10mm × ID 8mm

---

Insert Depth

15 mm

---

Clamp

Split Clamp

---

Status

APPROVED

READY FOR

CDS-03C-Horn_Hub-CAD-Design.md