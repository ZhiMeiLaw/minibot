# Mini-Atlas V6 Alpha

# MDS-03 Assembly Specification

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Design Purpose

本规范用于冻结：

- Bearing（轴承）
- Shaft（转轴）
- Carbon Tube（碳纤维管）
- Fastener（紧固件）
- Brass Insert（热熔铜螺母）
- E-Clip（轴挡圈）
- Assembly Sequence（装配顺序）

目标：

任何拥有基础机械装配能力的人均可依据本规范完成 Mini-Atlas V6 Alpha 下半身总成装配。

---

# 2. Standard Hardware Freeze

## 2.1 Hip Roll Bearing

### Function

承担：

- 髋关节 Roll 方向侧向载荷
- 骨盆重量
- 动态行走冲击

### Specification

| Parameter | Value |
|------------|------------|
| Type | 6803-2RS |
| ID | 17 mm |
| OD | 26 mm |
| Width | 5 mm |
| Quantity | 2 |

---

## 2.2 Hip Pitch Bearing

### Specification

| Parameter | Value |
|------------|------------|
| Type | 6803-2RS |
| Quantity | 2 |

---

## 2.3 Knee Bearing

### Specification

| Parameter | Value |
|------------|------------|
| Type | 6802-2RS |
| ID | 15 mm |
| OD | 24 mm |
| Width | 5 mm |
| Quantity | 2 |

---

## 2.4 Ankle Bearing

### Specification

| Parameter | Value |
|------------|------------|
| Type | 6801-2RS |
| ID | 12 mm |
| OD | 21 mm |
| Width | 5 mm |
| Quantity | 2 |

---

# 3. Shaft Specification

## 3.1 Hip Roll Shaft

### Function

承担：

- Hip Roll 主载荷
- Roll轴旋转中心

### Specification

| Parameter | Value |
|------------|------------|
| Material | SUS304 Stainless Steel |
| Diameter | 17 mm |
| Length | 45 mm |

---

## 3.2 Hip Pitch Shaft

| Parameter | Value |
|------------|------------|
| Material | SUS304 |
| Diameter | 17 mm |
| Length | 40 mm |

---

## 3.3 Knee Shaft

| Parameter | Value |
|------------|------------|
| Material | SUS304 |
| Diameter | 15 mm |
| Length | 35 mm |

---

## 3.4 Ankle Shaft

| Parameter | Value |
|------------|------------|
| Material | SUS304 |
| Diameter | 12 mm |
| Length | 30 mm |

---

# 4. Carbon Fiber Tube Freeze

采用现货标准碳纤维圆管。

禁止定制。

原因：

- 降低成本
- 易采购
- 易更换

---

## 4.1 Thigh Tube（大腿）

| Parameter | Value |
|------------|------------|
| Material | Carbon Fiber |
| OD | 16 mm |
| ID | 14 mm |
| Length | 90 mm |

Quantity:

2

---

## 4.2 Calf Tube（小腿）

| Parameter | Value |
|------------|------------|
| Material | Carbon Fiber |
| OD | 14 mm |
| ID | 12 mm |
| Length | 80 mm |

Quantity:

2

---

# 5. Fastener Freeze

## 5.1 M2 Screw

### Application

- IMU安装
- 小型PCB固定

### Specification

M2 × 6

---

## 5.2 M2.5 Screw

### Application

- ESP32安装

### Specification

M2.5 × 8

---

## 5.3 M3 Screw

### Application

- 结构件连接
- 舵机固定

### Specification

M3 × 8

M3 × 10

M3 × 12

---

## 5.4 M4 Screw

### Application

- 主承力连接

### Specification

M4 × 16

---

# 6. Brass Insert Specification

## Function

热熔嵌入塑料件内部。

用于：

- 重复拆装
- 增强螺纹强度

---

## Specification

| Parameter | Value |
|------------|------------|
| Type | M3 Brass Insert |
| OD | 4.6 mm |
| Length | 5 mm |

---

## Recommended Hole

4.4 mm

---

# 7. E-Clip Specification

## Function

防止转轴轴向窜动。

---

## Hip Roll

| Item | Value |
|------------|------------|
| Shaft Diameter | 17 mm |
| E-Clip | DIN6799-17 |

---

## Hip Pitch

| Item | Value |
|------------|------------|
| Shaft Diameter | 17 mm |
| E-Clip | DIN6799-17 |

---

## Knee

| Item | Value |
|------------|------------|
| Shaft Diameter | 15 mm |
| E-Clip | DIN6799-15 |

---

## Ankle

| Item | Value |
|------------|------------|
| Shaft Diameter | 12 mm |
| E-Clip | DIN6799-12 |

---

# 8. Hip Roll Assembly

## Cross Section

                 Pelvis Bracket

        ┌─────────────────────┐
        │                     │
        │     6803 Bearing    │
        │         │           │
        │         │           │
        │      17mm Shaft     │
        │         │           │
        │     6803 Bearing    │
        │                     │
        └─────────────────────┘

                 │

             Servo Horn

                 │

             Hip Frame

---

## Assembly Sequence

1. 压入左侧6803轴承
2. 压入右侧6803轴承
3. 插入17mm主轴
4. 安装E-Clip
5. 安装STS3046舵机
6. 安装舵盘Horn
7. 固定Hip Roll支架

---

# 9. Hip Pitch Assembly

## Cross Section

            Hip Roll Frame

                   │

              6803 Bearing

                   │

               17mm Shaft

                   │

              6803 Bearing

                   │

             Thigh Assembly

---

## Assembly Sequence

1. 安装轴承
2. 插入主轴
3. 安装舵机
4. 固定Horn
5. 固定大腿连接座

---

# 10. Knee Assembly

## Cross Section

          Thigh Tube

               │

          6802 Bearing

               │

            15mm Shaft

               │

          6802 Bearing

               │

           Calf Tube

---

## Assembly Sequence

1. 安装轴承
2. 插入15mm主轴
3. 安装STS3046
4. 安装Horn
5. 固定小腿组件

---

# 11. Ankle Assembly

## Cross Section

            Calf Tube

                │

           6801 Bearing

                │

            12mm Shaft

                │

           6801 Bearing

                │

           Wheel Module

---

## Assembly Sequence

1. 安装6801轴承
2. 插入12mm主轴
3. 安装STS3215
4. 安装Horn
5. 固定轮足模块

---

# 12. Joint Load Path

## Hip Roll

Ground

↓

Wheel

↓

Ankle

↓

Calf

↓

Knee

↓

Thigh

↓

Hip Roll

↓

Pelvis

---

## Hip Pitch

Ground

↓

Wheel

↓

Ankle

↓

Calf

↓

Knee

↓

Hip Pitch

↓

Hip Roll

↓

Pelvis

---

# 13. Assembly Verification Checklist

装配完成后检查：

- Bearing转动顺畅
- 无明显间隙
- E-Clip安装正确
- Horn无松动
- 碳管无裂纹
- 舵机输出轴无卡滞
- 所有M3螺丝已锁紧

---

# 14. Freeze Summary

## Bearings

6803-2RS
6802-2RS
6801-2RS

## Shafts

17 mm
15 mm
12 mm

## Carbon Tubes

16×14×90 mm
14×12×80 mm

## Fasteners

M2
M2.5
M3
M4

## Brass Insert

M3 × 5 mm

## E-Clips

DIN6799 Series

Status:

APPROVED FOR CAD MODELING