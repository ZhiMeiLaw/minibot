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
| DOF | 8 |
| Controller | ESP32 |
| Battery | 3S2P Samsung 30Q |
| Target Weight | < 2.5 kg |
| Estimated Weight | 1.9 ~ 2.3 kg |

---

# 2. Servo System

| Item | Model | Qty | Unit Cost | Total Cost |
|--------|--------|--------:|--------:|--------:|
| Hip Roll | STS3046 | 2 | 150 | 300 |
| Hip Pitch | STS3046 | 2 | 150 | 300 |
| Knee | STS3046 | 2 | 150 | 300 |
| Ankle | STS3215 | 2 | 70 | 140 |

### Servo Cost

```text
1040 RMB
```

### Servo Weight

```text
530 g
```

---

# 3. Wheel System

| Item | Model | Qty | Cost |
|--------|--------|--------:|--------:|
| Wheel Motor | GB37-520 Encoder | 2 | 80 |
| Wheel | 65mm Rubber | 2 | 30 |

### Wheel Cost

```text
110 RMB
```

### Weight

```text
260 g
```

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
| 6803-2RS | 12 | 48 |
| 6802-2RS | 8 | 32 |

### Bearing Cost

```text
80 RMB
```

---

## Carbon Tube

| Spec | Qty | Cost |
|--------|--------:|--------:|
| 8x10 mm | 1 meter | 50 |

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
| Servo System | 1040 |
| Wheel System | 110 |
| Battery System | 200 |
| Electronics | 90 |
| Power System | 106 |
| Mechanical Hardware | 230 |
| Manufacturing | 50 |

---

## Total Prototype Cost

```text
1826 RMB
```

---

## Procurement Buffer (+10%)

```text
183 RMB
```

---

## Recommended Budget

```text
2000 RMB
```

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
| Servo System | 530 g |
| Wheel System | 260 g |
| Battery System | 290 g |
| Electronics | 60 g |
| Power System | 80 g |
| Mechanical Hardware | 240 g |
| Printed Parts | 500 g |

---

## Estimated Weight

```text
1960 g
```

≈

```text
2.0 kg
```

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
2.0 kg
```

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

2 × STS3215

2 × GB37-520 Encoder

ESP32

ICM42688

3S2P Samsung 30Q
```

Prototype Budget

```text
≈ 2000 RMB
```

Prototype Weight

```text
≈ 2.0 kg
```

Status

```text
READY FOR PROCUREMENT

READY FOR CAD

READY FOR SDS-01
```
