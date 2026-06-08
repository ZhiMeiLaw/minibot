# Mini-Atlas V6 Alpha

# CDS-02A Standard Component Library Revision A

Version: 1.1

Status: APPROVED

Engineering Change Order:

ECO-001

Date:

2026-05

---

# 1. Purpose

本文件用于修订：

CDS-02 Standard Component Library

中关于关节轴承的定义。

---

# 2. Change Summary

原设计：

6803-2RS

17×26×5

6802-2RS

15×24×5

---

修订后：

688-2RS

8×16×5

---

原因：

原轴承尺寸与：

Ø8 Joint Shaft

不匹配。

---

# 3. Engineering Review

---

## Original Design

Bearing

6803

ID

17 mm

---

Shaft

Ø8 mm

---

问题：

```text
轴承内径17mm

转轴8mm

无法直接装配
```

---

需要：

```text
衬套(Bushing)

或

重新设计转轴
```

---

导致：

```text
结构复杂

重量增加

成本增加
```

---

## Revised Design

Bearing

688-2RS

---

Dimensions

ID

8 mm

OD

16 mm

Width

5 mm

---

直接匹配：

```text
Ø8 Shaft
```

---

无需：

```text
衬套

转接套
```

---

# 4. New Joint Bearing Standard

Mini-Atlas V6 Alpha 全关节统一采用：

```text
688-2RS
```

---

规格：

```text
8×16×5 mm
```

---

密封：

```text
2RS
```

橡胶密封

---

材料：

```text
Chrome Steel
```

---

参考型号：

```text
688-2RS
```

---

淘宝关键词：

```text
688轴承

8x16x5

688-2RS
```

---

# 5. Mechanical Benefits

---

## Weight Reduction

原方案

6803

约：

7 g

---

688

约：

2 g

---

单个节省：

5 g

---

全机：

12个轴承

节省：

60 g

---

## Cost Reduction

6803

约：

4 RMB

---

688

约：

1 RMB

---

全机节省：

36 RMB

---

## Volume Reduction

6803

外径：

26 mm

---

688

外径：

16 mm

---

减小：

10 mm

---

有利于：

```text
Hip Roll

Hip Pitch

Knee

Ankle
```

紧凑化设计。

---

# 6. Updated Component Library

---

## V6-STD-0001

688-2RS Bearing

---

File Name

```text
688-2RS.step
```

---

Dimensions

```text
ID = 8 mm

OD = 16 mm

Width = 5 mm
```

---

Mass

```text
≈2 g
```

---

CAD Model

```text
Simple Ring
```

---

Reference Axis

```text
Bearing Center Axis
```

---

# 7. Joint Standardization

以下关节统一采用：

---

## Hip Roll

Bearing

```text
688 ×2
```

---

## Hip Pitch

Bearing

```text
688 ×2
```

---

## Knee

Bearing

```text
688 ×2
```

---

## Ankle

Bearing

```text
688 ×2
```

---

# 8. Shaft Standardization

全机统一：

---

Joint Shaft

```text
Ø8 Hardened Shaft
```

---

Material

```text
GCr15
```

---

Tolerance

```text
h6
```

---

Advantages

```text
统一库存

统一加工

统一维护
```

---

# 9. Carbon Tube Compatibility

保持：

```text
8×10 Carbon Tube
```

---

无需修改：

```text
MDS-02

MDS-03

MDS-04
```

---

# 10. BOM Impact

---

Original

6803 ×12

Cost

≈48 RMB

Weight

≈84 g

---

Revised

688 ×12

Cost

≈12 RMB

Weight

≈24 g

---

Improvement

Weight

```text
-60 g
```

---

Cost

```text
-36 RMB
```

---

# 11. Documents Affected

以下文档需同步更新：

---

CDS-02

---

CDS-03

---

BOM-01

---

BOM-02

---

BOM-03

---

# 12. Freeze Summary

Joint Bearing

```text
688-2RS
```

---

Bearing Size

```text
8×16×5
```

---

Joint Shaft

```text
Ø8
```

---

Carbon Tube

```text
8×10
```

---

Status

```text
APPROVED

ECO-001 CLOSED

READY FOR CDS-03A

HipRoll_Base CAD Design
```
