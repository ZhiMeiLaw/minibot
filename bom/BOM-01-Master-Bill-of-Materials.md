# Mini-Atlas V6 Alpha

# BOM-01 Master Bill of Materials

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

* 采购型号（Part Number）
* 数量（Quantity）
* 单价（Unit Cost）
* 总价（Total Cost）
* 重量（Weight）
* 替代型号（Alternative Parts）
* 淘宝采购关键词（Taobao Search Keywords）

本文件作为：

```text
V6 Alpha Prototype Build
```

唯一采购依据。

---

# 2. Project Summary

## Robot Configuration

```text
Mini-Atlas V6 Alpha

Height:
550 mm

Weight Target:
< 4.0 kg

Architecture:
Wheel-Assisted Humanoid

Controller:
ESP32

Battery:
3S2P Li-ion

DOF:
6 Servo + 2 Wheel
```

> **ECO-001 变更**：重量目标修正为 <4.0kg（DOF 由 8 修正为 6 舵机 + 2 轮毂电机）。

---

# 3. Mechanical BOM

## 3.1 Servo System

### Hip Roll Servo

| Item        | Value        |
| ----------- | ------------ |
| Model       | STS3046      |
| Qty         | 2            |
| Weight      | 70g          |
| Unit Cost   | 150 RMB      |
| Total       | 300 RMB      |
| Keyword     | STS3046 串口舵机 |
| Alternative | STS3250      |

---

### Hip Pitch Servo

| Item        | Value   |
| ----------- | ------- |
| Model       | STS3046 |
| Qty         | 2       |
| Weight      | 70g     |
| Unit Cost   | 150 RMB |
| Total       | 300 RMB |
| Alternative | STS3250 |

---

### Knee Servo

| Item        | Value   |
| ----------- | ------- |
| Model       | STS3046 |
| Qty         | 2       |
| Weight      | 70g     |
| Unit Cost   | 150 RMB |
| Total       | 300 RMB |
| Alternative | STS3250 |

---

## Servo Summary

| Model   | Qty |
| ------- | --: |
| STS3046 |   6 |

> **ECO-001 变更**：踝关节已移除（DR-011）。原 STS3215 × 2 方案取消。

---

Total Weight

```text
420 g
```

---

Total Cost

```text
900 RMB
```

---

# 3.2 Bearings

## Joint Bearing

| Item      | Value    |
| --------- | -------- |
| Model     | 688-2RS  |
| ID        | 8 mm     |
| OD        | 16 mm    |
| Width     | 5 mm     |
| Qty       | 4        |
| Unit Cost | 5 RMB    |
| Total     | 20 RMB   |

> 用于：Hip Roll（每关节 2 个）

---

## Auxiliary Bearing

| Item      | Value    |
| --------- | -------- |
| Model     | 698-2RS  |
| ID        | 8 mm     |
| OD        | 19 mm    |
| Width     | 6 mm     |
| Qty       | 8        |
| Unit Cost | 5 RMB    |
| Total     | 40 RMB   |

> 用于：Hip Pitch（每关节 2 个）+ Knee（每关节 2 个）。**ECO-001 变更**：轴承系统由 6803/6802（Ø17/Ø15 轴）更新为 688/698（Ø8 轴配合）。

---

Bearing Cost

```text
60 RMB
```

---

# 3.3 Carbon Fiber Tubes

## Thigh

| Item   | Value   |
| ------ | ------- |
| Spec   | OD 10mm × ID 8mm |
| Length | 120 mm visible / 150 mm cut |
| Qty    | 2       |

---

## Calf

| Item   | Value   |
| ------ | ------- |
| Spec   | OD 10mm × ID 8mm |
| Length | 120 mm visible / 150 mm cut |
| Qty    | 2       |

---

采购：

```text
10mm内径 碳纤维圆管
1米
```

> **ECO-001 变更**：碳管规格由 16×14×90 / 14×12×80 更新为 OD10×ID8×150mm（CDS-04B/05B/MP-001）。

---

Cost

```text
50 RMB
```

---

Weight

```text
40 g
```

---

# 3.4 Wheel Assembly

## Wheel Motor

| Item      | Value            |
| --------- | ---------------- |
| Model     | GB37-520 Encoder |
| Qty       | 2                |
| Weight    | 110 g            |
| Unit Cost | 40 RMB           |
| Total     | 80 RMB           |

---

## Wheel

| Item     | Value  |
| -------- | ------ |
| Diameter | 80 mm  |
| Qty      | 2      |
| Cost     | 40 RMB |

> **ECO-001 变更**：轮径由 65mm 更新为 80mm（DR-011 决定）。

---

## Wheel Adapter Plate

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 2            |
| Weight    | 40 g         |
| Cost      | 5 RMB        |

---

## Wheel Hub

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 2            |
| Weight    | 25 g         |
| Cost      | 3 RMB        |

> **ECO-002 变更**：新增 Wheel Hub 独立零件（CDS-06 §7），用于压配合电机轴 + M3 顶丝固定轮子。

---

Wheel Cost

```text
160 RMB
```

---

Weight

```text
350 g
```

---

# 3.5 Fasteners

## Screws

| Type   | Qty |
| ------ | --: |
| M2×6   |  30 |
| M2×8   |  30 |
| M2.5×8 |  30 |
| M3×8   |  50 |
| M3×12  |  50 |

---

## Brass Inserts

| Model | Qty |
| ----- | --: |
| M2    |  50 |
| M2.5  |  50 |
| M3    | 100 |

---

## E-Clips

| Size | Qty |
| ---- | --: |
| 3 mm |  20 |
| 4 mm |  20 |

---

Cost

```text
50 RMB
```

---

Weight

```text
80 g
```

---

# 3.6 Pelvis Assembly

## Pelvis Main Frame

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 1            |
| Weight    | 180 g        |
| Cost      | 15 RMB       |

---

## Pelvis Battery Bay

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 1            |
| Weight    | 60 g         |
| Cost      | 5 RMB        |

> **ECO-002 变更**：新增独立 Battery Bay 零件（MDS-04 §3），滑入式设计，支持 <30秒电池更换。

---

## Pelvis Electronics Deck

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 1            |
| Weight    | 40 g         |
| Cost      | 5 RMB        |

> **ECO-002 变更**：新增独立 Electronics Deck（MDS-04 §4-6），ESP32 4点安装 + Buck 固定槽。

---

## Pelvis Service Hatch

| Item      | Value        |
| --------- | ------------ |
| Model     | PETG Printed |
| Qty       | 1            |
| Weight    | 25 g         |
| Cost      | 3 RMB        |

> **ECO-002 变更**：新增 Service Hatch（MDS-04 §14），后部可拆卸盖板，4×M3 固定，支持电池/XT30/开关维护。

---

Pelvis Cost

```text
28 RMB
```

---

Weight

```text
305 g
```

---

# 4. Electrical BOM

## 4.1 Controller

### Main MCU

| Item   | Value             |
| ------ | ----------------- |
| Model  | ESP32 DevKitC-32E |
| Qty    | 1                 |
| Cost   | 25 RMB            |
| Weight | 12 g              |

---

## 4.2 IMU

### Motion Sensor

| Item  | Value      |
| ----- | ---------- |
| Model | ICM42688-P |
| Qty   | 1          |
| Cost  | 35 RMB     |

---

# 4.3 Motor Driver

### Wheel Driver

| Item  | Value   |
| ----- | ------- |
| Model | DRV8871 |
| Qty   | 2       |
| Cost  | 15 RMB  |
| Total | 30 RMB  |

---

# 4.4 Battery Pack

## Cell

| Item  | Value       |
| ----- | ----------- |
| Model | Samsung 30Q |
| Qty   | 6           |
| Cost  | 25 RMB      |
| Total | 150 RMB     |

---

## Configuration

```text
3S2P
```

---

Weight

```text
290 g
```

---

# 4.5 Power System

## Servo Buck

| Item  | Value    |
| ----- | -------- |
| Model | 20A Buck |
| Qty   | 1        |
| Cost  | 40 RMB   |

---

## Logic Buck

| Item  | Value    |
| ----- | -------- |
| Model | MP1584EN |
| Qty   | 1        |
| Cost  | 10 RMB   |

---

## Fuse

| Item  | Value       |
| ----- | ----------- |
| Model | ATO 25A     |
| Qty   | 1           |
| Cost  | 5 RMB       |

---

> **ECO-002 变更**：Fuse 数量由 2 修正为 1（主回路单点保护），规格统一为 25A Slow Blow（EDS-03 最新分析）。

---

## MOSFET

| Item  | Value   |
| ----- | ------- |
| Model | IRLZ44N |
| Qty   | 1       |
| Cost  | 8 RMB   |

---

## Reverse Protection

| Item  | Value   |
| ----- | ------- |
| Model | IRF4905 |
| Qty   | 1       |
| Cost  | 8 RMB   |

---

# 4.6 Connectors

## XT30

| Item    | Qty |
| ------- | --: |
| XT30U-M |   2 |
| XT30U-F |   2 |

---

Cost

```text
20 RMB
```

---

# 4.7 Wiring

| Type  | Length |
| ----- | ------ |
| AWG16 | 1m     |
| AWG18 | 1m     |
| AWG20 | 1m     |
| AWG24 | 2m     |

---

Cost

```text
30 RMB
```

---

# 5. Manufacturing BOM

## 3D Printing

| Material | Qty   |
| -------- | ----- |
| PETG     | 500 g |

---

Cost

```text
50 RMB
```

---

Weight

```text
500 g
```

---

# 6. Cost Summary

| Category           |     Cost |
| ------------------ | -------: |
| Servo System       |  900 RMB |
| Bearings           |   60 RMB |
| Carbon Tube        |   50 RMB |
| Wheels             |  160 RMB |
| Wheel Hardware     |   13 RMB |
| Fasteners          |   50 RMB |
| Pelvis Assembly    |   28 RMB |
| Controller         |   25 RMB |
| IMU                |   35 RMB |
| Drivers            |   30 RMB |
| Battery            |  150 RMB |
| Power System       |   70 RMB |
| Connectors         |   20 RMB |
| Wiring             |   30 RMB |
| Printing           |   50 RMB |

---

> **ECO-002 变更**：新增 Wheel Hardware（Adapter + Hub）28 RMB，Pelvis Assembly 28 RMB。

---

Total

```text
1666 RMB
```

---

Expected Range

```text
1500~1900 RMB
```

> **ECO-001 变更**：轴承更新 + 踝关节取消 + 轮组升级，成本结构变化。

---

# 7. Weight Budget

| Category           | Weight |
| ------------------ | -----: |
| Servos             |  420 g |
| Battery            |  290 g |
| Wheel System       |  400 g |
| Electronics        |   60 g |
| Bearings           |   60 g |
| Fasteners          |   80 g |
| Carbon Tube        |   40 g |
| Pelvis Assembly    |  305 g |
| Printed Parts      |  500 g |

---

Estimated Total

```text
2215 g
```

---

Expected Final Weight

```text
3.0~3.8 kg
```

> **ECO-001 变更**：与 SR-001/PR-001 一致。原 <2.5kg 目标取消。
> **ECO-002 变更**：新增 Pelvis Assembly 305g，Wheel System 增加 Hub/Adapter 约 50g。

---

# 8. Upgrade Impact Analysis

## Upgrade Path

```text
STS3046
→
STS3250
```

---

Cost Increase

```text
+900 RMB
```

---

Weight Increase

```text
+120 g
```

---

Battery Runtime Impact

```text
-10~15%
```

---

# 9. Freeze Summary

## Prototype Budget

```text
1580 RMB
```

---

## Prototype Weight

```text
≈ 3.3 kg
```

---

## Architecture

```text
6×STS3046

2×GB37-520 Encoder

ESP32

3S2P Samsung 30Q
```

> **ECO-001 变更**：踝关节取消（DR-011），移除 STS3215 × 2。

---

Status

```text
APPROVED

READY FOR CAD MODELING

READY FOR PROCUREMENT

READY FOR SDS-01
```
