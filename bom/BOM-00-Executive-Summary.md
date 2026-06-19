# Mini-Atlas V6 Alpha

# BOM-00 Executive Summary

Version: 1.0 Freeze A

Status: PROJECT FREEZE

---

# 1. Project Overview

| Item | Value |
|--------|--------|
| Project | Mini-Atlas V6 Alpha |
| Architecture | Wheel-Assisted Humanoid |
| Height | 550 mm |
| DOF | 6 servo + 2 wheel |
| Controller | ESP32 |
| Battery | 3S2P Samsung 30Q |
| Target Weight | < 4.0 kg |
| Estimated Weight | 3.0 ~ 3.8 kg |

> **ECO-001 变更**：重量目标由 <2.5kg 修正为 <4.0kg，与 SR-001/PR-001 保持一致。

---

# 2. Servo System

| Item | Model | Qty | Unit Cost | Total Cost |
|--------|--------|--------:|--------:|--------:|
| Hip Roll | STS3046 | 2 | 150 | 300 |
| Hip Pitch | STS3046 | 2 | 150 | 300 |
| Knee | STS3046 | 2 | 150 | 300 |

> **ECO-001 变更**：踝关节已移除（DR-011）。原 STS3215 × 2（140 RMB）方案取消。

### Servo Cost

```text
900 RMB
```

### Servo Weight

```text
420 g
```

---

# 3. Wheel System

| Item | Model | Qty | Cost |
|--------|--------|--------:|--------:|
| Wheel Motor | GB37-520 Encoder | 2 | 80 |
| Wheel | 80mm Rubber | 2 | 40 |

> **ECO-001 变更**：轮径由 65mm 更新为 80mm（DR-011 决定）。

### Wheel Cost

```text
160 RMB
```

### Weight

```text
350 g
```

> 注：80mm 轮毂 + 轮胎，重量略高于 65mm 配置。

---

# 4. Battery System

| Item | Model | Qty | Cost |
|--------|--------|--------:|--------:|
| Cell | Samsung 30Q | 6 | 150 |
| BMS | 3S 20A | 1 | 20 |
| Nickel Strip | 0.15mm | 1 | 10 |
| Fish Paper | - | 12 | 5 |
| Kapton Tape | - | 1 | 10 |
| Heat Shrink | - | 1 | 5 |

### Battery Cost

```text
200 RMB
```

### Weight

```text
290 g
```

---

# 5. Electronics

| Item | Model | Qty | Cost |
|--------|--------|--------:|--------:|
| MCU | ESP32 DevKitC-32E | 1 | 25 |
| IMU | ICM42688-P | 1 | 35 |
| Driver | DRV8871 | 2 | 30 |

### Electronics Cost

```text
90 RMB
```

### Weight

```text
60 g
```

---

# 6. Power System

| Item | Model | Cost |
|--------|--------|--------:|
| Servo Buck | 20A Buck | 40 |
| Logic Buck | MP1584EN | 10 |
| XT30 | Amass XT30U | 20 |
| Fuse | ATO 25A | 10 |
| MOSFET | IRLZ44N | 8 |
| Reverse MOSFET | IRF4905 | 8 |
| Main Switch | MTS102 | 10 |

### Power Cost

```text
106 RMB
```

### Weight

```text
80 g
```

---

# 7. Mechanical Hardware

## Bearings

| Model | Qty | Cost |
|--------|--------:|--------:|
| 688-2RS | 4 | 20 |
| 698-2RS | 6 | 30 |

> **ECO-001 变更**：轴承系统全面更新为 688/698 微型轴承（Ø8 轴配合）。原 6803-2RS（Ø17轴）系统取消。

### Bearing Cost

```text
50 RMB
```

---

## Carbon Tube

| Spec | Qty | Cost |
|--------|--------:|--------:|
| OD 10mm × ID 8mm | 1 meter | 50 |

---

## Fasteners

包含：

```text
M2

M2.5

M3

Nut

Washer

Spacer

E-Clip

Brass Insert
```

### Cost

```text
80 RMB
```

---

## Cable Management

包含：

```text
Tie Wrap

Spiral Wrap

Adhesive Base
```

### Cost

```text
20 RMB
```

---

### Mechanical Hardware Cost

```text
230 RMB
```

### Weight

```text
240 g
```

---

# 8. Manufacturing

## 3D Printing

| Material | Qty | Cost |
|--------|--------:|--------:|
| PETG | 500g | 50 |

---

### Manufacturing Cost

```text
50 RMB
```

### Weight

```text
500 g
```

---

# 9. Prototype Cost Summary

| Category | Cost |
|------------|-----------:|
| Servo System | 900 |
| Wheel System | 160 |
| Battery System | 200 |
| Electronics | 90 |
| Power System | 106 |
| Mechanical Hardware | 230 |
| Manufacturing | 50 |

---

## Total Prototype Cost

```text
1736 RMB
```

---

## Procurement Buffer (+10%)

```text
174 RMB
```

---

## Recommended Budget

```text
2000 RMB
```

> **ECO-001 变更**：轴承系统更新降低轴承成本；踝关节取消减少舵机成本。轮组升级增加少量成本。

---

# 10. Spare Parts Budget

| Item | Cost |
|--------|--------:|
| Spare Servos | 370 |
| Spare Motor | 40 |
| Spare Bearings | 40 |
| Spare Electronics | 70 |
| Spare XT30/Fuse | 30 |
| Spare Fasteners | 30 |

---

## Spare Parts Total

```text
580 RMB
```

---

# 11. Weight Budget

| Category | Weight |
|------------|-----------:|
| Servo System | 420 g |
| Wheel System | 350 g |
| Battery System | 290 g |
| Electronics | 60 g |
| Power System | 80 g |
| Mechanical Hardware | 200 g |
| Printed Parts | 500 g |

---

## Estimated Weight

```text
1900 g
```

≈

```text
1.9 kg
```

> **注意**：此预算基于 <2.5kg 目标制定。实际 V6 Alpha 预期重量 3.0~3.8kg（PR-001），需以 SR-001 为准进行更新。

---

# 12. Project Budget Summary

## Minimum Build

```text
1826 RMB
```

---

## Recommended Build Budget

```text
2000 RMB
```

---

## Build + Spare Parts

```text
2400 RMB
```

---

## Expected Weight

```text
3.0 ~ 3.8 kg
```

> **ECO-001 变更**：与 SR-001/PR-001 保持一致。原 <2.5kg 目标取消。

---

# 13. Upgrade Impact

## STS3046 → STS3250

Additional Cost

```text
+900 RMB
```

---

Additional Weight

```text
+120 g
```

---

Battery Runtime

```text
-10% ~ -15%
```

---

# FINAL FREEZE

Architecture

```text
6 × STS3046

2 × GB37-520 Encoder

ESP32

ICM42688

3S2P Samsung 30Q
```

> **ECO-001 变更**：踝关节取消（DR-011），移除 STS3215 × 2。

Prototype Budget

```text
≈ 2000 RMB
```

Prototype Weight

```text
≈ 3.3 kg
```

Status

```text
READY FOR PROCUREMENT

READY FOR CAD

READY FOR SDS-01
```
