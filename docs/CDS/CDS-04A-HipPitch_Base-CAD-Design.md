# Mini-Atlas V6 Alpha

# CDS-04A HipPitch_Base CAD Design

Version: 1.0 Freeze A

Status: APPROVED

Part Number:

V6-PRT-0010

Part Name:

HipPitch_Base

Parent Assembly:

V6-ASM-0002 Hip Pitch Joint

Parent System:

Mini-Atlas V6 Alpha

Related Documents:

- CDS-03D Hip Roll Assembly Verification
- CDS-04 Hip Pitch Joint CAD Design
- CDS-02A Standard Component Library Revision A
- MDS-02 Detailed Joint Design
- MDS-04 Pelvis & Electronics Assembly Specification

---

# 1. Purpose

HipPitch_Base 是 Hip Pitch 关节的固定端（Fixed Side）。

其作用：

- 固定 Hip Pitch Servo
- 安装 698 Bearings
- 支撑 Hip Pitch Joint Shaft
- 提供 Hip Roll Interface
- 提供 Mechanical Stop
- 提供 Servo Maintenance Access

---

HipPitch_Base 不参与运动。

其属于：

```text
Pelvis
 ↓
Hip Roll
 ↓
HipPitch_Base
```

固定结构链。

---

# 2. Design Philosophy

设计原则：

```text
Servo Never Carries Structure Load
```

（舵机不承受结构载荷）

---

所有重量：

```text
Upper Leg
 ↓
HipPitch_Output
 ↓
Joint Shaft
 ↓
698 Bearings
 ↓
HipPitch_Base
```

---

禁止：

```text
Upper Leg
 ↓
Servo Horn
 ↓
Servo
```

---

# 3. Coordinate System

沿用全局坐标系：

```text
X+  Forward
Y+  Left
Z+  Up
```

---

Hip Pitch Rotation Axis：

```text
Y Axis
```

---

Rotation Center：

```text
Hip Pitch Joint Center
```

---

# 4. Overall Envelope

目标尺寸：

| Parameter | Value |
|------------|--------|
| Width | 50 mm |
| Height | 60 mm |
| Depth | 35 mm |

---

允许调整：

±3 mm

---

设计目标：

```text
尽可能紧凑
```

---

# 5. Hip Roll Interface

HipPitch_Base 上端连接：

```text
HipRoll_Output
```

---

接口形式：

```text
4 × M3
```

---

孔径：

```text
Ø3.2 mm
```

---

孔距：

```text
30 × 30 mm
```

---

结构：

```text

Top View

●──────●
│      │
│      │
●──────●

```

---

# 6. Hip Pitch Axis Location

冻结：

```text
Hip Pitch Axis
```

位于：

```text
Hip Roll Axis
```
外侧 35mm
> 与 DR-012 Section 2 保持一致（"Hip Pitch Offset: 35mm"）。

示意：

```text

Hip Roll Axis

   O─────────────────── 35mm ─────────────────── O

   Hip Pitch Axis

```

> **注意**：本参数与 DR-012 冻结值一致。原来 v1.0 中的"下方15mm"描述有误，已修正为 DR-012 的 35mm 偏移值。

---

# 7. Bearing Selection

冻结：

```text
698-2RS
```

规格：

```text
8 × 19 × 6 mm
```

---

数量：

```text
2
```

---

安装方式：

```text
Press Fit Pocket
```

---

Pocket Diameter：

```text
19.05 mm
```

---

Pocket Depth：

```text
6.2 mm
```

---

# 8. Bearing Layout

采用：

```text
Dual Bearing Support
```

---

布局：

```text

Side View

698
│
│ 20 mm
│
698

```

---

轴承中心间距：

```text
20 mm
```

---

目的：

提高抗弯刚度。

---

# 9. Joint Shaft Specification

冻结：

```text
Ø8 GCr15 Shaft
```

---

长度：

```text
32 mm
```

---

配合：

```text
Bearing
Slip Fit
```

---

# 10. Servo Installation

Servo：

```text
STS3046
```

---

安装方式：

```text
Side Mount
```

---

示意：

```text

Front View

┌─────────┐
│ STS3046 │
└─────────┘

     │

HipPitchBase

```

---

安装螺丝：

```text
M2.5 × 8
```

---

数量：

```text
4
```

---

# 11. Servo Maintenance Window

必须提供：

```text
Maintenance Access
```

---

要求：

无需拆解整个骨盆。

---

能够：

```text
拆4颗M2.5
```

直接取出舵机。

---

维护时间：

```text
<5 min
```

---

# 12. Mechanical Stop

采用：

```text
Stop Block
```

---

工作范围：

```text
+60°
-30°
```

---

机械极限：

```text
+65°
-35°
```

---

结构：

```text

Output Tab

    ▼

 ┌───────┐
 │       │
 └───┬───┘
     │
 Stop Block

```

---

厚度：

```text
4 mm
```

---

# 13. Pelvis Clearance

必须保证：

```text
Hip Roll Motion
```

不与：

```text
Hip Pitch Servo
```

发生干涉。

---

最小间隙：

```text
1.0 mm
```

---

推荐：

```text
2.0 mm
```

---

# 14. Wire Routing

预留：

```text
Servo Cable
```

通道。

---

孔径：

```text
Ø8 mm
```

---

位置：

```text
Servo Rear Side
```

---

允许：

- Servo Cable
- IMU Cable
- Future Sensor Cable

---

# 15. Brass Insert Locations

标准：

```text
M3 Brass Insert
```

---

数量：

```text
8
```

---

用途：

- Hip Roll Interface
- Bearing Cover
- Servo Protection Cover

---

# 16. Structural Reinforcement

增加：

```text
Triangular Rib
```

---

位置：

```text
Bearing Pocket
↓
Hip Roll Interface
```

---

厚度：

```text
3 mm
```

---

长度：

```text
15 mm
```

---

# 17. Printing Specification

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

Wall Count：

```text
4
```

---

Infill：

```text
40%
Gyroid
```

---

# 18. Printing Orientation

推荐：

```text

Bearing Axis

Horizontal

```

---

示意：

```text

      Bearing

         O

         O

 ┌──────────┐
 │ Base     │
 └──────────┘

═══════════════════

Build Plate

```

---

目的：

保证轴承孔圆度。

---

# 19. Weight Estimate

| Component | Weight |
|------------|--------:|
| PETG Body | 32 g |
| Inserts | 4 g |
| Screws | 5 g |

---

总重：

```text
≈41 g
```

---

目标：

```text
<45 g
```

---

# 20. Verification Checklist

CAD检查：

```text
□ 698可安装

□ STS3046可安装

□ Servo可拆卸

□ 无干涉

□ Wire Routing正常

□ Mechanical Stop正常

□ Hip Roll Interface正确
```

---

打印检查：

```text
□ Bearing Press Fit正常

□ Brass Insert正常

□ 无明显翘曲

□ 无裂纹
```

---

装配检查：

```text
□ Joint Rotation顺畅

□ Servo安装正常

□ Servo可维护

□ ±60°前摆

□ -30°后摆
```

---

# 21. Freeze Summary

Part Number:

```text
V6-PRT-0010
```

---

Part Name:

```text
HipPitch_Base
```

---

Bearing:

```text
698-2RS ×2
```

---

Servo:

```text
STS3046
```

---

Joint Shaft:

```text
Ø8 GCr15
```

---

Axis Offset:

```text
35 mm
```

> 与 DR-012 Section 2 一致。v1.0 中的 15mm 已修正。

Weight:

```text
≈41 g
```

---

Status:

```text
APPROVED

READY FOR

CDS-04B-HipPitch_Output-CAD-Design.md
```
