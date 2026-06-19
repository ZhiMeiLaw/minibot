# Mini-Atlas V6 Alpha

# CDS-01 CAD Design Specification

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

* CAD工程目录结构
* Part Number规则
* Assembly Number规则
* STEP标准件库
* 公差(Tolerance)规范
* 3D打印设计规范
* 碳纤维管接口规范
* CAD命名规范

本文件为：

```text
Mini-Atlas V6 Alpha

机械CAD设计唯一规范
```

---

# 2. CAD Software Standard

推荐：

```text
Fusion360
```

版本：

```text
Latest Stable
```

---

兼容：

```text
SolidWorks 2022+

FreeCAD 1.0+
```

---

交换格式：

```text
STEP AP214
```

禁止：

```text
STL作为主设计文件
```

STL仅用于打印。

---

# 3. Project Directory Structure

```text
MiniAtlas-V6/

├── CAD/
│
├── Parts/
│   ├── Standard/
│   ├── Servo/
│   ├── Electronics/
│   ├── Mechanical/
│   └── Printed/
│
├── Assemblies/
│   ├── Joint/
│   ├── Leg/
│   ├── Pelvis/
│   └── FullRobot/
│
├── STEP/
│   ├── Vendor/
│   └── Export/
│
├── Drawings/
│
├── STL/
│
└── Release/
```

---

# 4. Part Number Rules

格式：

```text
V6-PPP-XXXX
```

---

PPP

表示分类：

```text
SER
MEC
ELE
PRT
STD
```

---

示例：

```text
V6-SER-0001
STS3046
```

---

```text
V6-STD-0001
688-2RS Bearing

---
> **ECO-001 变更**：原 6803 已取消，改用 688-2RS（8×16×5）作为 Hip Roll 标准轴承示例。
```

---

```text
V6-PRT-0001
Hip Roll Bracket
```

---

# 5. Assembly Number Rules

格式：

```text
V6-ASM-XXXX
```

---

示例：

```text
V6-ASM-0001
Hip Roll Assembly
```

---

```text
V6-ASM-0002
Hip Pitch Assembly
```

---

```text
V6-ASM-0003
Knee Assembly
```

---

```text
V6-ASM-0004
Ankle Assembly
```

---

```text
V6-ASM-0010
Left Leg
```

---

```text
V6-ASM-0011
Right Leg
```

---

```text
V6-ASM-0100
Mini-Atlas Full Assembly
```

---

# 6. STEP Library Standard

---

# Servo Library

必须建立：

```text
STS3046.step

STS3215.step
```

---

要求：

包含：

```text
外壳

安装孔

输出轴

Horn
```

---

允许简化：

```text
内部齿轮
```

---

# Bearing Library

建立：

```text
688-2RS.step

698-2RS.step
```

> **ECO-001 变更**：轴承库由 6803/6802 更新为 688-2RS（Hip Roll）和 698-2RS（Hip Pitch/Knee）。
```

---

要求：

保持真实尺寸

---

# Electronics Library

建立：

```text
ESP32.step

ICM42688.step

DRV8871.step

Buck.step

XT30.step
```

---

# Battery Library

建立：

```text
18650.step
```

---

尺寸：

```text
Ø18.5 x 65 mm
```

---

# 7. Coordinate System Standard

全机统一：

```text
X
Forward
前方
```

---

```text
Y
Left
左侧
```

---

```text
Z
Up
上方
```

---

遵循：

```text
ROS REP-103
```

---

# 8. Unit Standard

统一：

```text
Millimeter
(mm)
```

---

质量：

```text
Gram
(g)
```

---

角度：

```text
Degree
(°)
```

---

禁止：

```text
inch
```

---

# 9. Tolerance Standard

---

# FDM Printed Parts

默认：

```text
±0.20 mm
```

---

# Bearing Pocket

推荐：

```text
+0.05

+0.10
```

---

例如：

688-2RS（Hip Roll 轴承）

外径：

```text
16.0 mm
```

孔：

```text
16.05~16.10 mm
```

> **ECO-001 变更**：示例轴承由 6803 更新为 688-2RS（OD 16mm）。Hip Pitch/Knee 用 698-2RS（OD 19mm），计算方式相同。

---

# Shaft Hole

推荐：

```text
+0.10
```

---

例如：

```text
8.0 shaft

8.10 hole
```

---

# Carbon Tube Interface

推荐：

```text
+0.20
```

---

例如：

```text
10 mm Tube

10.20 Socket
```

---

# Brass Insert Hole

推荐：

```text
-0.10
```

---

例如：

M3铜螺母：

```text
4.6 mm
```

孔：

```text
4.5 mm
```

---

# 10. Printing Material Standard

---

# Structural Parts

统一：

```text
PETG
```

---

层高：

```text
0.20 mm
```

---

填充：

```text
40%
```

---

壁厚：

```text
4 Perimeters
```

---

禁止：

```text
PLA
```

用于：

```text
Hip

Knee

Ankle
```

---

# Prototype Covers

允许：

```text
PLA+
```

---

# High Load Parts

推荐：

```text
PETG-CF

Nylon-CF
```

仅Beta版本。

---

# 11. Minimum Design Rules

---

最小壁厚：

```text
2.5 mm
```

---

承力区域：

```text
4 mm
```

---

轴承座周边：

```text
≥5 mm
```

---

铜螺母周边：

```text
≥3 mm
```

---

孔边距：

```text
≥2D
```

(D=孔径)

---

# 12. Carbon Tube Interface Standard

---

# Thigh Tube

规格：

```text
OD 10mm × ID 8mm
```

长度：

```text
150 mm（裁切后120mm可见）
```

---

插入深度：

```text
15 mm
```

---

固定方式：

```text
M3 Through Bolt
```

---

禁止：

```text
仅胶水固定
```

---

# Calf Tube

规格：

```text
OD 10mm × ID 8mm
```

长度：

```text
150 mm（裁切后120mm可见）
```

---

固定方式：

```text
M3 Through Bolt
```

---

# 13. Wire Routing Standard

所有活动关节：

必须预留：

```text
Servo Bus

Power

Encoder
```

---

线槽宽度：

```text
≥6 mm
```

---

转弯半径：

```text
≥10 mm
```

---

禁止：

```text
锐角折弯
```

---

# 14. Serviceability Requirements

必须满足：

---

舵机可拆卸：

```text
≤5分钟
```

---

电池可更换：

```text
≤2分钟
```

---

ESP32可更换：

```text
≤3分钟
```

---

轮子可更换：

```text
≤3分钟
```

---

# 15. CAD Review Checklist

建模完成后检查：

```text
□ Servo安装空间

□ Bearing安装空间

□ Horn旋转干涉

□ Carbon Tube插入深度

□ 电池安装空间

□ ESP32安装空间

□ Buck安装空间

□ XT30安装空间

□ 线束通道

□ 重心位置

□ 可维护性
```

---

# 16. Release Procedure

设计冻结前必须输出：

```text
STEP

STL

PDF Drawing
```

---

发布目录：

```text
Release/

V6_Alpha_RevA/
```

---

# 17. Freeze Summary

CAD Environment

```text
Fusion360
```

---

Exchange Format

```text
STEP AP214
```

---

Printing Material

```text
PETG
```

---

Carbon Tube

```text
OD 10mm × ID 8mm × L 150mm
```

---

Tolerance

```text
±0.20 mm
```

---

Status

```text
APPROVED

READY FOR PART MODELING

READY FOR ASSEMBLY DESIGN
```
