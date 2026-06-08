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
< 2.5 kg

Architecture:
Wheel-Assisted Humanoid

Controller:
ESP32

Battery:
3S2P Li-ion

DOF:
8
```

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

### Ankle Servo

| Item        | Value   |
| ----------- | ------- |
| Model       | STS3215 |
| Qty         | 2       |
| Weight      | 55g     |
| Unit Cost   | 70 RMB  |
| Total       | 140 RMB |
| Alternative | STS3046 |

---

## Servo Summary

| Model   | Qty |
| ------- | --: |
| STS3046 |   6 |
| STS3215 |   2 |

---

Total Weight

```text
530 g
```

---

Total Cost

```text
1040 RMB
```

---

# 3.2 Bearings

## Joint Bearing

| Item      | Value    |
| --------- | -------- |
| Model     | 6803-2RS |
| ID        | 17 mm    |
| OD        | 26 mm    |
| Width     | 5 mm     |
| Qty       | 12       |
| Unit Cost | 4 RMB    |
| Total     | 48 RMB   |

---

## Auxiliary Bearing

| Item      | Value    |
| --------- | -------- |
| Model     | 6802-2RS |
| Qty       | 8        |
| Unit Cost | 4 RMB    |
| Total     | 32 RMB   |

---

Bearing Cost

```text
80 RMB
```

---

# 3.3 Carbon Fiber Tubes

## Thigh

| Item   | Value   |
| ------ | ------- |
| Spec   | 8×10 mm |
| Length | 90 mm   |
| Qty    | 2       |

---

## Calf

| Item   | Value   |
| ------ | ------- |
| Spec   | 8×10 mm |
| Length | 80 mm   |
| Qty    | 2       |

---

采购：

```text
8x10 碳纤维圆管
1米
```

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
| Diameter | 65 mm  |
| Qty      | 2      |
| Cost     | 30 RMB |

---

Wheel Cost

```text
110 RMB
```

---

Weight

```text
260 g
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

| Item  | Value   |
| ----- | ------- |
| Model | ATO 25A |
| Qty   | 2       |
| Cost  | 5 RMB   |

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

| Category     |     Cost |
| ------------ | -------: |
| Servo System | 1040 RMB |
| Bearings     |   80 RMB |
| Carbon Tube  |   50 RMB |
| Wheels       |  110 RMB |
| Fasteners    |   50 RMB |
| Controller   |   25 RMB |
| IMU          |   35 RMB |
| Drivers      |   30 RMB |
| Battery      |  150 RMB |
| Power System |   70 RMB |
| Connectors   |   20 RMB |
| Wiring       |   30 RMB |
| Printing     |   50 RMB |

---

Total

```text
1740 RMB
```

---

Expected Range

```text
1700~2000 RMB
```

---

# 7. Weight Budget

| Category      | Weight |
| ------------- | -----: |
| Servos        |  530 g |
| Battery       |  290 g |
| Wheel System  |  260 g |
| Electronics   |   60 g |
| Bearings      |  120 g |
| Fasteners     |   80 g |
| Carbon Tube   |   40 g |
| Printed Parts |  500 g |

---

Estimated Total

```text
1880 g
```

---

Expected Final Weight

```text
1.9~2.3 kg
```

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
1740 RMB
```

---

## Prototype Weight

```text
≈1.9 kg
```

---

## Architecture

```text
6×STS3046

2×STS3215

2×GB37-520 Encoder

ESP32

3S2P Samsung 30Q
```

---

Status

```text
APPROVED

READY FOR CAD MODELING

READY FOR PROCUREMENT

READY FOR SDS-01
```
