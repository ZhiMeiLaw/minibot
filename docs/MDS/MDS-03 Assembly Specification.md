# Mini-Atlas V6 Alpha

# MDS-03 Assembly Specification

Version: 1.1 Freeze B

Status: APPROVED

> **ECO-001 变更记录**
> - 2026-06: 轴承系统由 6803/6802/6801 更新为 688-2RS/698-2RS；主轴 Ø8 GCr15；碳管 OD10×ID8×L150mm。本版本取代 MDS-03 v1.0 Freeze A。

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
| Type | 688-2RS |
| ID | 8 mm |
| OD | 16 mm |
| Width | 5 mm |
| Quantity | 4 |

---

## 2.2 Hip Pitch Bearing

### Specification

| Parameter | Value |
|------------|------------|
| Type | 698-2RS |
| Quantity | 4 |

规格：8 × 19 × 6 mm

---

## 2.3 Knee Bearing

### Specification

| Parameter | Value |
|------------|------------|
| Type | 698-2RS |
| Quantity | 2 |

规格：8 × 19 × 6 mm

---

## 2.4 Ankle

**已移除。** DR-011 决定采用 Rigid Wheel Mount（刚性轮足融合），踝关节取消。详见 DR-011-Ankle-Architecture-Review.md。

---

# 3. Shaft Specification

## 3.1 Hip Roll Shaft

### Function

承担：

- Hip Roll 主载荷
- Roll 轴旋转中心

### Specification

| Parameter | Value |
|------------|------------|
| Material | GCr15 轴承钢（淬火） |
| Diameter | 8 mm |
| Length | 45 mm |
| Tolerance | h7 |
| Surface | 抛光 |

---

## 3.2 Hip Pitch Shaft

| Parameter | Value |
|------------|------------|
| Material | GCr15 |
| Diameter | 8 mm |
| Length | 40 mm |

---

## 3.3 Knee Shaft

| Parameter | Value |
|------------|------------|
| Material | GCr15 |
| Diameter | 8 mm |
| Length | 38 mm |

---

# 4. Carbon Fiber Tube Freeze

采用现货标准碳纤维圆管。

禁止定制。

原因：

- 降低成本
- 易采购
- 易更换

规格标注：`OD × ID × L`（外径 × 内径 × 长度）

---

## 4.1 Thigh Tube（大腿）

| Parameter | Value |
|------------|------------|
| Material | Carbon Fiber |
| OD | 10 mm |
| ID | 8 mm |
| Length | 120 mm visible / 150 mm raw |
| Quantity | 2 |

---

## 4.2 Calf Tube（小腿）

| Parameter | Value |
|------------|------------|
| Material | Carbon Fiber |
| OD | 10 mm |
| ID | 8 mm |
| Length | 120 mm visible / 150 mm raw |
| Quantity | 2 |

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

## Hip Roll / Hip Pitch / Knee

| Item | Value |
|------------|------------|
| Shaft Diameter | 8 mm |
| E-Clip | DIN6799-8 |

---

# 8. Hip Roll Assembly

## Cross Section

                  Pelvis Bracket

        ┌─────────────────────┐
        │                     │
        │     688 Bearing     │
        │         │           │
        │         │           │
        │      Ø8 Shaft      │
        │         │           │
        │     688 Bearing    │
        │                     │
        └─────────────────────┘

                  │

              Servo Horn

                  │

              Hip Frame

---

## Assembly Sequence

1. 压入左侧 688 轴承
2. 压入右侧 688 轴承
3. 插入 Ø8 主轴
4. 安装 E-Clip
5. 安装 STS3046 舵机
6. 安装舵盘 Horn
7. 固定 Hip Roll 支架

---

# 9. Hip Pitch Assembly

## Cross Section

            Hip Roll Frame

                   │

              698 Bearing

                   │

               Ø8 Shaft

                   │

              698 Bearing

                   │

             Thigh Assembly

---

## Assembly Sequence

1. 安装 698 轴承
2. 插入 Ø8 主轴
3. 安装 STS3046
4. 安装 Horn
5. 固定大腿连接座

---

# 10. Knee Assembly

## Cross Section

          Thigh Tube

               │

          698 Bearing

               │

            Ø8 Shaft

               │

          698 Bearing

               │

           Calf Tube

---

## Assembly Sequence

1. 安装 698 轴承
2. 插入 Ø8 主轴
3. 安装 STS3046
4. 安装 Horn
5. 固定小腿组件

---

# 11. Ankle Assembly

**已移除。** DR-011 选择 Rigid Wheel Mount 方案，详见 DR-011-Ankle-Architecture-Review.md。

轮组直接通过刚性安装座连接在小腿末端，无独立踝关节。

---

# 12. Joint Load Path

## Hip Roll

Ground

↓

Wheel

↓

（Calf）

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

（Calf）

↓

Knee

↓

Thigh

↓

Hip Pitch

↓

Hip Roll

↓

Pelvis

---

# 13. Assembly Verification Checklist

装配完成后检查：

- Bearing 转动顺畅
- 无明显间隙
- E-Clip 安装正确
- Horn 无松动
- 碳管无裂纹
- 舵机输出轴无卡滞
- 所有 M3 螺丝已锁紧

---

# 14. Bearing Quantities Summary

| Bearing | ID×OD×W | 应用 | 数量 |
|---------|---------|------|------|
| 688-2RS | 8×16×5 | Hip Roll | 4 |
| 698-2RS | 8×19×6 | Hip Pitch + Knee | 6 |
| **合计** | | | **10** |

> 注：踝关节已移除（DR-011），原 6801/6802 轴承系统不再使用。

---

# 15. Shaft Quantities Summary

| Shaft | 位置 | 数量 |
|-------|------|------|
| Ø8×45 | Hip Roll | 2 |
| Ø8×40 | Hip Pitch | 2 |
| Ø8×38 | Knee | 2 |

---

# 16. Freeze Summary

## Bearings

688-2RS（8×16×5）

698-2RS（8×19×6）

## Shafts

Ø8 GCr15 h7

## Carbon Tubes

OD 10mm × ID 8mm × L 150mm

## Fasteners

M2 / M2.5 / M3 / M4

## Brass Insert

M3 × 5 mm

## E-Clips

DIN6799-8

Status:

APPROVED FOR CAD MODELING

(End of file - total 487 lines)