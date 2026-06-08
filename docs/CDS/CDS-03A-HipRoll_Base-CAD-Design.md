# Mini-Atlas V6 Alpha

# CDS-03A HipRoll_Base CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Parent Assembly:

V6-ASM-0001 Hip Roll Assembly

Part Number:

V6-PRT-0001

Part Name:

HipRoll_Base

---

# 1. Purpose

HipRoll_Base 是整个 Hip Roll 总成的主基准件（Master Part）。

其作用：

* 固定于 Pelvis（骨盆）
* 安装 STS3046 舵机
* 安装 688 轴承
* 定义 Hip Roll 中心轴
* 提供线束通道
* 提供维护空间

本零件将作为：

```text
Hip Roll
Hip Pitch
Pelvis
```

的统一坐标基准。

---

# 2. Design Requirements

必须满足：

```text
安装 STS3046

安装 688×2

支持 ±25° Roll

支持快速维护

支持 FDM 打印
```

---

设计寿命：

```text
100小时以上
```

Alpha Prototype

---

# 3. Coordinate System

采用机器人全局坐标系：

```text
X+
前方

Y+
左侧

Z+
上方
```

---

原点定义：

```text
Hip Roll Rotation Center
```

即：

```text
Joint Axis Center
```

---

# 4. Overall Dimensions

建议尺寸：

```text
Width
70 mm

Height
60 mm

Depth
42 mm
```

---

允许误差：

```text
±2 mm
```

---

设计目标：

```text
尽量包络STS3046

减少体积
```

---

# 5. Primary Geometry

整体结构：

```text

Front View

┌────────────────────┐
│                    │
│   Servo Pocket     │
│                    │
│      ○ Axis        │
│                    │
└────────────────────┘
```

---

结构形式：

```text
U Shape Frame

(U型框架)
```

---

优点：

```text
打印简单

刚度高

易于安装轴承
```

---

# 6. Hip Roll Axis Location

Joint Center：

```text
X = 0

Y = 0

Z = 0
```

---

作为：

```text
机器人髋关节中心
```

---

轴方向：

```text
X Axis
```

---

即：

```text
Roll Around X
```

---

# 7. Bearing Pocket Design

Bearing：

```text
688-2RS

8×16×5
```

---

数量：

```text
2
```

---

孔径：

```text
16.05 mm
```

---

允许：

```text
16.05~16.10
```

---

孔深：

```text
5.2 mm
```

---

轴承间距：

```text
20 mm
```

---

布局：

```text

Side View

Bearing
    │
    ▼

 ┌─────┐
 │     │
 │     │
 └─────┘

<--20-->

 ┌─────┐
 │     │
 │     │
 └─────┘
```

---

目的：

```text
提高抗弯能力

减少晃动
```

---

# 8. Shaft Support Boss

轴承座外围厚度：

```text
≥4 mm
```

---

推荐：

```text
5 mm
```

---

总外径：

```text
26 mm
```

---

形成：

```text
Bearing Boss
```

---

# 9. STS3046 Mounting Pocket

Servo：

```text
STS3046
```

---

安装位置：

```text
Axis Rear Side
```

---

输出轴中心：

```text
与 Hip Roll Axis 同轴
```

---

允许偏差：

```text
<0.1 mm
```

---

安装孔：

```text
4 × M2.5
```

---

安装板厚度：

```text
4 mm
```

---

铜螺母：

```text
M2.5 Brass Insert
```

---

# 10. Servo Pocket

Pocket尺寸：

```text
48 × 26 × 37 mm
```

---

间隙：

```text
0.5 mm
```

每侧

---

目的：

```text
方便安装

避免打印误差
```

---

# 11. Brass Insert Locations

型号：

```text
M2.5
```

---

孔径：

```text
4.5 mm
```

---

孔深：

```text
5 mm
```

---

数量：

```text
4
```

---

位置：

```text
Servo Mount Pattern
```

---

周边肉厚：

```text
≥3 mm
```

---

# 12. Pelvis Interface

连接面：

```text
Top Face
```

---

安装孔：

```text
M3 × 4
```

---

孔径：

```text
3.2 mm
```

---

孔距：

```text
40 × 30 mm
```

---

用途：

```text
连接 Pelvis Main Frame
```

---

# 13. Wire Routing Channel

预留：

```text
Servo Bus

Servo Power
```

---

线槽宽度：

```text
6 mm
```

---

线槽高度：

```text
5 mm
```

---

转弯半径：

```text
R10
```

---

禁止：

```text
90°锐角
```

---

# 14. Maintenance Access

必须满足：

```text
舵机安装后

仍可接触：

Horn Screw

Mount Screw
```

---

预留：

```text
工具通道
```

---

最小：

```text
Ø8 mm
```

---

# 15. Structural Reinforcement

增加：

```text
Triangular Rib
```

（三角加强筋）

---

厚度：

```text
3 mm
```

---

位置：

```text
Bearing Boss

Servo Pocket
```

交界处

---

# 16. Printing Specification

材料：

```text
PETG
```

---

层高：

```text
0.20 mm
```

---

壁厚：

```text
4 Perimeters
```

---

填充：

```text
40%
```

---

顶部层：

```text
5 Layers
```

---

底部层：

```text
5 Layers
```

---

# 17. Print Orientation

推荐：

```text

Front View

┌──────────┐
│          │
│ Hip Base │
│          │
└──────────┘

打印平台
══════════
```

---

即：

```text
Pelvis Interface
朝下
```

---

优点：

```text
轴承孔圆度最佳

无需内部支撑
```

---

# 18. Support Strategy

允许：

```text
Tree Support
```

---

仅用于：

```text
Servo Pocket
```

---

禁止：

```text
Bearing Pocket 内部支撑
```

---

# 19. Estimated Weight

PETG：

```text
≈35 g
```

---

目标：

```text
<40 g
```

---

# 20. CAD Verification Checklist

建模完成后：

```text
□ Servo可安装

□ Bearing可压入

□ Shaft通过

□ Pelvis连接正常

□ Brass Insert正常

□ 无干涉

□ 线束通过

□ Roll ±25°
```

---

# 21. Manufacturing Checklist

打印完成：

```text
□ Bearing孔检查

□ Servo孔检查

□ 铜螺母安装

□ 去毛刺

□ 试装轴承

□ 试装舵机
```

---

# 22. Freeze Summary

Part Number

```text
V6-PRT-0001
```

---

Part Name

```text
HipRoll_Base
```

---

Bearing

```text
688-2RS ×2
```

---

Servo

```text
STS3046
```

---

Shaft

```text
Ø8
```

---

Material

```text
PETG
```

---

Weight

```text
≈35 g
```

---

Status

```text
APPROVED

READY FOR CAD MODELING

READY FOR CDS-03B HipRoll_Output CAD Design
```
