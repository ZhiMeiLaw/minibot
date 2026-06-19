# Mini-Atlas V6 Alpha

# MDS-02 Detailed Joint Design Specification

## 关节详细设计规范

Version: v0.2 Freeze A

Status: APPROVED

---

# 1. Design Philosophy（设计理念）

## 核心原则

机器人关节必须遵循：

```text
Servo Provides Torque

Bearing Provides Support

Structure Provides Strength
```

即：

```text
舵机负责输出扭矩

轴承负责承重

结构负责传递载荷
```

---

# 2. Standard Mechanical Components（标准机械件）

---

## 2.1 Bearing（轴承）

### Purpose（用途）

Bearing（轴承）用于：

* 支撑转轴
* 降低摩擦
* 承受径向载荷
* 承受部分轴向载荷

---

### Hip Joint Bearing

冻结型号：

```text
MR128-2RS
```

尺寸：

```text
8 × 12 × 3.5 mm
```

参数：

| Item                | Value  |
| ------------------- | ------ |
| Inner Diameter (内径) | 8 mm   |
| Outer Diameter (外径) | 12 mm  |
| Width (厚度)          | 3.5 mm |

---

### Knee Joint Bearing

冻结型号：

```text
MR106-2RS
```

尺寸：

```text
6 × 10 × 3 mm
```

---

### Ankle Joint Bearing

冻结型号：

```text
MR105-2RS
```

尺寸：

```text
5 × 10 × 4 mm
```

---

## 2.2 Shaft（转轴）

### Hip Shaft

材料：

```text
7075 Aluminum

7075航空铝
```

直径：

```text
8 mm
```

---

### Knee Shaft

材料：

```text
SUS304 Stainless Steel

304不锈钢
```

直径：

```text
6 mm
```

---

### Ankle Shaft

材料：

```text
SUS304 Stainless Steel
```

直径：

```text
5 mm
```

---

## 2.3 Servo Horn（舵盘）

### Definition（定义）

Servo Horn（舵盘）是：

```text
Servo Output Interface
舵机输出接口
```

作用：

```text
Transmit Torque
传递扭矩
```

---

禁止：

```text
Servo Horn Load Bearing
舵盘直接承重
```

---

## 2.4 Coupler（联轴器）

采用：

```text
Split Clamp Coupler

开口夹紧联轴器
```

作用：

```text
Horn
 ↓
Coupler
 ↓
Joint Shaft
```

优点：

* 易维护
* 无需胶水
* 不损伤转轴

---

# 3. Hip Roll Joint（髋关节侧摆）

---

## Function（功能）

负责：

```text
Center Of Mass Shift

重心转移
```

---

## Importance（重要性）

这是：

```text
Highest Loaded Joint

整机受力最大的关节
```

---

## Architecture（结构）

```text
Pelvis Side Plate

    │

 MR128 Bearing

    │

   8mm Shaft

    │

 MR128 Bearing

    │

 Hip Roll Bracket

    ▲

 Split Coupler

    ▲

 STS3046 Servo
```

---

## Bearing Layout（轴承布局）

必须：

```text
Dual Bearing Support

双轴承支撑
```

---

轴承间距：

```text
25~30 mm
```

---

禁止：

```text
Single Bearing Design
```

---

## Design Freeze

| Item    | Value        |
| ------- | ------------ |
| Servo   | STS3046      |
| Shaft   | 8 mm         |
| Bearing | MR128 × 2    |
| Support | Dual Bearing |

---

# 4. Hip Pitch Joint（髋关节前后摆）

---

## Function

负责：

```text
Leg Swing

摆腿运动
```

---

## Structure

采用：

```text
Fork Structure

叉架结构
```

---

## Cross Section

```text
Side Plate

 Bearing

   │

  Shaft

   │

 Bearing

Side Plate
```

---

## Load Path（载荷路径）

```text
Thigh

 ↓

Bearing

 ↓

Shaft

 ↓

Bearing

 ↓

Pelvis
```

---

## Design Freeze

| Item      | Value     |
| --------- | --------- |
| Servo     | STS3046   |
| Shaft     | 8 mm      |
| Bearing   | MR128 × 2 |
| Structure | Fork      |

---

# 5. Knee Joint（膝关节）

---

## Function

负责：

```text
Leg Extension

腿部伸展

Leg Retraction

腿部收缩
```

---

## Design Philosophy

采用：

```text
Direct Drive

直驱
```

---

原因：

* 简化结构
* 降低成本
* 降低重量

---

## Cross Section

```text
Left Plate

  │

Bearing

  │

6mm Shaft

  │

Bearing

  │

Right Plate
```

---

## Structural Requirement

必须：

```text
Double Shear

双剪切结构
```

---

禁止：

```text
Single Side Support
单边支撑
```

---

## Future Upgrade

预留：

```text
GT2 Timing Belt

同步带
```

安装空间。

未来可升级：

```text
1.5 : 1 Reduction
```

---

## Design Freeze

| Item    | Value        |
| ------- | ------------ |
| Servo   | STS3046      |
| Shaft   | 6 mm         |
| Bearing | MR106 × 2    |
| Drive   | Direct Drive |

---

# 6. Ankle Joint（踝关节）

---

## Function

负责：

```text
Wheel Attitude Control

轮组姿态控制
```

---

## DOF Freeze

冻结：

```text
1 DOF
Pitch Only
```

---

暂不采用：

```text
Pitch + Roll
```

双自由度方案。

---

## Structure

```text
Calf

 │

Bearing

 │

5mm Shaft

 │

Bearing

 │

Wheel Fork
```

---

## Design Freeze

| Item    | Value     |
| ------- | --------- |
| Servo   | STS3215   |
| Shaft   | 5 mm      |
| Bearing | MR105 × 2 |
| DOF     | 1         |

---

# 7. Carbon Tube Structure（碳管结构）

---

## Design Freeze Revision A

经过 Design Review：

```text
16×14

↓

14×12
```

统一规格。

---

## Thigh Tube（大腿）

尺寸：

```text
OD = 14 mm

ID = 12 mm

Length = 120 mm
```

---

## Calf Tube（小腿）

尺寸：

```text
OD = 14 mm

ID = 12 mm

Length = 120 mm
```

---

## Advantages（优点）

```text
采购简单

重量更轻

库存统一

打印接口统一
```

---

# 8. Internal Wiring（内部布线）

---

所有线束：

```text
Servo Cable

Motor Cable

IMU Cable
```

优先走：

```text
Carbon Tube Internal Routing

碳管内部走线
```

---

预留孔径：

```text
6 mm
```

---

# 9. Standard BOM（标准件BOM）

## Per Leg

### Hip Roll

| Item          | Qty |
| ------------- | --: |
| STS3046       |   1 |
| MR128 Bearing |   2 |
| 8mm Shaft     |   1 |
| Split Coupler |   1 |

---

### Hip Pitch

| Item          | Qty |
| ------------- | --: |
| STS3046       |   1 |
| MR128 Bearing |   2 |
| 8mm Shaft     |   1 |

---

### Knee

| Item          | Qty |
| ------------- | --: |
| STS3046       |   1 |
| MR106 Bearing |   2 |
| 6mm Shaft     |   1 |

---

### Ankle

| Item          | Qty |
| ------------- | --: |
| STS3215       |   1 |
| MR105 Bearing |   2 |
| 5mm Shaft     |   1 |

---

# 10. Design Freeze Summary

## Hip Roll

```text
STS3046

8mm Shaft

MR128 ×2
```

---

## Hip Pitch

```text
STS3046

8mm Shaft

MR128 ×2
```

---

## Knee

```text
STS3046

6mm Shaft

MR106 ×2

Direct Drive
```

---

## Ankle

```text
STS3215

5mm Shaft

MR105 ×2

1 DOF
```

---

## Carbon Tube

```text
OD 14 mm

ID 12 mm

Length 120 mm
```

---

## Wheel

```text
GB37-520

80 mm Wheel
```

> **ECO-001 变更**：轮径由 100mm 更新为 80mm（DR-011 决定）。

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

This document is now authorized for:

* CAD Design
* Mechanical BOM Creation
* Prototype Manufacturing

---

# End Of Document
