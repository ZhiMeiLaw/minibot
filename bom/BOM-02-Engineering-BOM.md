# Mini-Atlas V6 Alpha

# BOM-02 Engineering BOM

Version: 1.0 Freeze A

Status: ENGINEERING FREEZE

---

# 1. Purpose

本文件用于冻结：

```text
所有标准件

所有轴承

所有转轴

所有铜螺母

所有螺丝

所有挡圈

所有垫片

所有线束

所有连接器

所有舵机附件
```

本文件将作为：

```text
SolidWorks/Fusion360建模依据

装配依据

采购依据
```

---

# 2. Fastener Standard

全机统一标准：

## Screw Standards

```text
M2
M2.5
M3
```

禁止使用：

```text
M2.2
M2.6
M4
```

避免工具混乱。

---

# 3. Screw BOM

## M2×6 Socket Head

用途：

```text
ESP32安装

IMU安装

电子模块安装
```

数量：

```text
30 pcs
```

采购：

```text
304不锈钢
```

---

## M2×8 Socket Head

用途：

```text
线夹

小型支架
```

数量：

```text
30 pcs
```

---

## M2.5×8 Socket Head

用途：

```text
舵机辅助固定
```

数量：

```text
30 pcs
```

---

## M3×8 Socket Head

用途：

```text
关节主体连接
```

数量：

```text
80 pcs
```

---

## M3×12 Socket Head

用途：

```text
轴承座固定
```

数量：

```text
60 pcs
```

---

## M3×16 Socket Head

用途：

```text
骨盆总成
```

数量：

```text
40 pcs
```

---

## M3 Nut

规格：

```text
DIN934
```

数量：

```text
50 pcs
```

---

# 4. Brass Insert BOM

---

## M2 Brass Insert

规格：

```text
OD=3.5mm
L=4mm
```

数量：

```text
50 pcs
```

---

## M2.5 Brass Insert

规格：

```text
OD=4mm
L=5mm
```

数量：

```text
50 pcs
```

---

## M3 Brass Insert

规格：

```text
OD=4.6mm
L=5.7mm
```

数量：

```text
120 pcs
```

---

# 5. Bearing BOM

---

## Main Joint Bearing (Hip Roll)

型号：

```text
688-2RS
```

规格：

```text
8×16×5
```

数量：

```text
4 pcs
```

位置：

```text
Hip Roll（每腿 2 个）
```

> **ECO-001 变更**：由 6803-2RS（Ø17 轴）更新为 688-2RS（Ø8 轴配合）。

---

## Main Joint Bearing (Hip Pitch + Knee)

型号：

```text
698-2RS
```

规格：

```text
8×19×6
```

数量：

```text
8 pcs
```

位置：

```text
Hip Pitch（每腿 2 个）+ Knee（每腿 2 个）
```

> 原 6802-2RS 用于踝关节，已取消（DR-011）。

---

# 6. Shaft BOM

---

## Hip Roll Shaft

规格：

```text
Ø8 GCr15 淬火钢
```

长度：

```text
45 mm
```

数量：

```text
2 pcs
```

> **ECO-001 变更**：由 Ø17 SUS304 更新为 Ø8 GCr15（CDS-02A/MP-001）。

---

## Hip Pitch Shaft

规格：

```text
Ø8 GCr15 淬火钢
```

长度：

```text
40 mm
```

数量：

```text
2 pcs
```

---

## Knee Shaft

规格：

```text
Ø8 GCr15 淬火钢
```

长度：

```text
38 mm
```

数量：

```text
2 pcs
```

> **ECO-001 变更**：踝关节取消，原 Ø6mm 踝轴及相关 E-Clip 取消。

长度：

```text
30 mm
```

数量：

```text
4 pcs
```

---

## Knee Shaft

规格：

```text
8mm Hardened Steel
```

长度：

```text
35 mm
```

数量：

```text
2 pcs
```

---

## Ankle Shaft

规格：

```text
6mm Hardened Steel
```

长度：

```text
25 mm
```

数量：

```text
2 pcs
```

---

采购关键词：

```text
GCr15 光轴
```

---

# 7. E-Clip BOM

---

## 8mm E-Clip

规格：

```text
DIN6799-8
```

数量：

```text
12 pcs
```

用途：

```text
轴向限位（Hip Roll / Hip Pitch / Knee）
```

> **ECO-001 变更**：统一为 Ø8 轴用 E-Clip。原 6mm E-Clip（踝关节用）取消。

---

# 8. Washer BOM

---

## M3 Flat Washer

规格：

```text
DIN125
```

数量：

```text
100 pcs
```

---

## M3 Spring Washer

数量：

```text
100 pcs
```

---

## Shaft Spacer

规格：

```text
8x12x1 mm
```

数量：

```text
20 pcs
```

---

用途：

```text
轴承预紧

消除轴向间隙
```

---

# 9. Servo Accessory BOM

---

# STS3046

## Servo

数量：

```text
6 pcs
```

---

## Original Metal Horn

数量：

```text
6 pcs
```

必须原厂。

---

## Center Screw

数量：

```text
6 pcs
```

---

## Mount Screw Set

数量：

```text
24 pcs
```

---

> **ECO-001 变更**：踝关节取消（DR-011），移除 STS3215 及其附件。

# 10. Carbon Tube BOM

---

## Thigh Tube

规格：

```text
OD 10mm × ID 8mm
```

长度：

```text
150 mm（裁切后 120mm 可见）
```

数量：

```text
2 pcs
```

---

## Calf Tube

规格：

```text
OD 10mm × ID 8mm
```

长度：

```text
150 mm（裁切后 120mm 可见）
```

数量：

```text
2 pcs
```

---

采购：

```text
10mm内径 碳纤维圆管
1米整根
```

> **ECO-001 变更**：碳管规格由 16×14×90 / 14×12×80 更新为 OD10×ID8×150mm（CDS-04B/05B/MP-001）。

---

# 11. Wheel Assembly BOM

---

## Gear Motor

型号：

```text
GB37-520 Encoder
```

数量：

```text
2 pcs
```

---

## Wheel

规格：

```text
65 mm Rubber Wheel
```

数量：

```text
2 pcs
```

---

## Wheel Bearing

型号：

```text
698-2RS
```

数量：

```text
4 pcs
```

> 用于：轮毂轴承支撑（每轮 2 个）

---

## Motor Mount Screw

规格：

```text
M3x8
```

数量：

```text
8 pcs
```

> **ECO-001 变更**：轮组直接刚性安装（DR-011），移除踝关节传动链。

---

# 12. Battery Assembly BOM

---

## Samsung 30Q

数量：

```text
6 pcs
```

---

## Nickel Strip

规格：

```text
0.15mm
```

数量：

```text
1 m
```

---

## Fish Paper

数量：

```text
12 pcs
```

---

## Kapton Tape

数量：

```text
1 Roll
```

---

## Heat Shrink Tube

规格：

```text
80 mm
```

数量：

```text
1 m
```

---

## BMS

型号：

```text
3S 20A BMS
```

数量：

```text
1 pcs
```

---

# 13. Wiring Harness BOM

---

## Servo Bus Cable

规格：

```text
22AWG
```

长度：

```text
3 m
```

---

## Wheel Power Cable

规格：

```text
20AWG
```

长度：

```text
1 m
```

---

## Battery Cable

规格：

```text
16AWG
```

长度：

```text
1 m
```

---

## Logic Cable

规格：

```text
24AWG
```

长度：

```text
2 m
```

---

# 14. Connector BOM

---

## XT30U

数量：

```text
4 sets
```

---

## JST-XH 2P

数量：

```text
10 pcs
```

---

## JST-XH 3P

数量：

```text
10 pcs
```

---

## JST-XH 4P

数量：

```text
10 pcs
```

---

## Dupont Header

数量：

```text
40 pins
```

---

# 15. Cable Management BOM

---

## Spiral Wrap

规格：

```text
6 mm
```

长度：

```text
2 m
```

---

## Cable Tie

规格：

```text
100 mm
```

数量：

```text
100 pcs
```

---

## Adhesive Tie Base

规格：

```text
20x20 mm
```

数量：

```text
20 pcs
```

---

# 16. Service Parts BOM

建议额外采购：

---

## STS3046

```text
1 Spare
```

---

## GB37-520

```text
1 Spare
```

---

## Bearing

```text
4 Spare
```

---

## XT30

```text
2 Spare Sets
```

---

## Fuse

```text
5 Spare
```

---

# 17. Engineering Part Count Summary

| Category | Approx Part Count |
|-----------|-----------:|
| Servo System | 16 |
| Bearings | 20 |
| Shafts | 8 |
| Fasteners | 430+ |
| Wiring | 40 |
| Connectors | 30 |
| Battery Parts | 25 |
| Wheel System | 20 |

---

Total Engineering Parts

```text
≈ 600 Components
```

(包含所有螺丝、垫片、挡圈、连接器)

---

# 18. CAD Freeze Requirements

开始建模前必须冻结：

```text
Bearing Pocket

Brass Insert Hole

Shaft Diameter

Servo Mount Hole

Carbon Tube Interface

Wire Routing Channel

Battery Bay
```

---

# 19. Assembly Readiness

Status：

```text
ENGINEERING BOM COMPLETE

READY FOR CAD MODELING

READY FOR PROTOTYPE BUILD
```
