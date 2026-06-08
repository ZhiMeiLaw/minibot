# Mini-Atlas V6 Alpha

# EDS-04 Power Hardware Selection

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结 Mini-Atlas V6 Alpha 的具体电源硬件选型。

冻结内容包括：

- Battery Cell（电池电芯）
- Battery Pack（电池包）
- Servo Buck Converter（舵机电源）
- Logic Buck Converter（逻辑电源）
- MOSFET（功率开关）
- Fuse（保险丝）
- XT30 Connector（电池连接器）
- Main Switch（主电源开关）
- PDB（电源分配板）
- Wire Harness（线束）
- Connector BOM（连接器BOM）

本文件冻结后：

```text
允许直接采购

允许开始PCB设计

允许开始线束设计
```

---

# 2. Design Requirements

## Electrical Requirements

### Battery

```text
11.1V Nominal

12.6V Full

6Ah Capacity
```

---

### Servo Rail

```text
7.4V

15A Continuous

20A Peak
```

---

### Logic Rail

```text
5V

1A Typical

3A Peak
```

---

### Wheel Rail

```text
11.1V Direct

3A Peak
```

---

# 3. Battery Cell Selection

---

## Candidate A

Samsung 30Q

### Specification

| Item | Value |
|--------|--------|
| Capacity | 3000mAh |
| Continuous Current | 15A |
| Chemistry | INR |
| Weight | 48g |

---

### Pros

```text
价格低

容易买到

社区验证广泛
```

---

### Cons

```text
倍率一般
```

---

## Candidate B

Molicel P28A

### Specification

| Item | Value |
|--------|--------|
| Capacity | 2800mAh |
| Continuous Current | 25A |
| Weight | 46g |

---

### Pros

```text
高倍率

机器人领域广泛使用
```

---

### Cons

```text
价格较高
```

---

## Candidate C

Molicel P30B

### Specification

| Item | Value |
|--------|--------|
| Capacity | 3000mAh |
| Continuous Current | 30A |
| Weight | 47g |

---

### Pros

```text
性能最佳
```

---

### Cons

```text
价格最高
```

---

# Freeze

V6 Alpha

采用：

```text
Samsung 30Q
```

---

原因：

```text
当前峰值电流

<20A

3S2P完全满足
```

---

# 4. Battery Pack Freeze

## Configuration

```text
3S2P
```

---

## Cell Count

```text
6
```

---

## Capacity

```text
6000mAh
```

---

## Energy

```text
66Wh
```

---

## Weight

约：

```text
290g
```

---

# 5. Servo Buck Converter

---

# Requirements

输入：

```text
9V~13V
```

---

输出：

```text
7.4V
```

---

能力：

```text
15A Continuous

20A Peak
```

---

# Candidate Analysis

---

## LM2596

淘汰

原因：

```text
3A
```

---

## XL4015

淘汰

原因：

```text
5A
```

---

## MP2307

淘汰

原因：

```text
电流不足
```

---

## DROK 20A Buck

### Specification

| Item | Value |
|--------|--------|
| Input | 6~40V |
| Output | Adjustable |
| Current | 20A Peak |
| Efficiency | 90~95% |

---

### Pros

```text
成熟

现货

大量验证
```

---

### Cons

```text
体积偏大
```

---

# Freeze

Servo Rail

采用：

```text
DROK 20A Buck
```

---

输出：

```text
7.4V
```

---

要求：

```text
必须安装散热片
```

---

# 6. Logic Buck Converter

---

# Requirements

```text
5V

<1A Typical
```

---

# Freeze

采用：

```text
MP1584EN Module
```

---

### Specification

| Item | Value |
|--------|--------|
| Input | 4.5~28V |
| Output | Adjustable |
| Current | 3A |

---

输出：

```text
5.0V
```

---

# 7. Servo Power MOSFET

---

# Requirements

```text
20A Peak

Logic Level
```

---

# Candidate

IRLZ44N

---

### Specification

| Item | Value |
|--------|--------|
| Vds | 55V |
| Id | 47A |
| Rds(on) | 22mΩ |

---

# Usage

用于：

```text
Servo Rail Soft Start

Servo Rail Enable
```

---

# Freeze

```text
IRLZ44N
```

---

# Future Upgrade

V6 Beta：

```text
AO4407

AO3400 Array
```

---

# 8. Reverse Polarity MOSFET

---

用途：

```text
防止电池接反
```

---

Freeze：

```text
IRF4905

P-Channel MOSFET
```

---

原因：

```text
低压降

成熟方案
```

---

# 9. Main Fuse Selection

---

需求：

```text
20A Peak

机器人负载
```

---

# Freeze

采用：

```text
ATO Automotive Fuse
```

---

规格：

```text
25A

Slow Blow
```

---

推荐：

```text
Littelfuse

Bussmann
```

---

# 10. XT30 Selection

---

不要购买杂牌。

---

# Freeze

采用：

```text
Amass XT30U
```

---

型号：

```text
XT30U-M

XT30U-F
```

---

额定：

```text
30A Continuous
```

---

完全满足 V6 Alpha。

---

# 11. Main Power Switch

---

需求：

```text
20A Peak
```

---

# Freeze

采用：

```text
MTS-102 Toggle Switch
```

---

参数：

```text
SPDT

金属拨杆
```

---

安装：

```text
Pelvis Side Panel
```

---

# 12. Voltage Divider

---

用途：

```text
Battery Voltage Monitoring
```

---

结构：

```text
100k

33k
```

---

输出：

```text
ESP32 ADC
```

---

量程：

```text
0~15V
```

---

# 13. PDB Schematic Freeze

---

## Functional Block Diagram

```text

Battery XT30

      │

  25A Fuse

      │

 Main Switch

      │

 Reverse MOSFET

      │

      PDB

 ┌────┼────┐

 │    │    │

Servo Logic Wheel

Buck  Buck Rail

```

---

# PDB Functions

## Power Input

```text
XT30
```

---

## Main Fuse

```text
25A
```

---

## Voltage Monitor

```text
ADC Divider
```

---

## Ground Plane

```text
Single Point Ground
```

---

## Servo Rail Connector

```text
XT30
```

---

## Logic Rail Connector

```text
JST-XH
```

---

# 14. Wire Selection

---

## Battery Harness

Freeze：

```text
AWG18 Silicone
```

---

长度：

```text
≤150mm
```

---

## Servo Rail

Freeze：

```text
AWG16 Silicone
```

---

原因：

```text
20A Peak
```

---

## Wheel Rail

Freeze：

```text
AWG20 Silicone
```

---

## Logic Rail

Freeze：

```text
AWG24 Silicone
```

---

# 15. Connector BOM

## Battery

| Item | Model |
|--------|--------|
| Battery Connector | XT30U |
| PDB Connector | XT30U |

---

## Servo Rail

| Item | Model |
|--------|--------|
| Power Input | XT30 |
| Distribution | JST-XH |

---

## Logic Rail

| Item | Model |
|--------|--------|
| ESP32 | JST-XH |
| IMU | JST-SH |

---

## Wheel Rail

| Item | Model |
|--------|--------|
| Motor | JST-VH |

---

# 16. Procurement BOM

| Item | Model | Qty |
|--------|--------|--------:|
| Samsung 30Q | 3000mAh | 6 |
| XT30U-M | Amass | 2 |
| XT30U-F | Amass | 2 |
| 25A Fuse | ATO | 2 |
| Fuse Holder | Automotive | 1 |
| DROK 20A Buck | Servo Rail | 1 |
| MP1584EN | Logic Rail | 1 |
| IRLZ44N | Soft Start | 1 |
| IRF4905 | Reverse Protection | 1 |
| MTS-102 | Switch | 1 |
| AWG16 Silicone Wire | Red/Black | 1m |
| AWG18 Silicone Wire | Red/Black | 1m |
| AWG20 Silicone Wire | Red/Black | 1m |
| AWG24 Silicone Wire | Red/Black | 2m |

---

# 17. Design Review Findings

## XT30

Status:

```text
PASS
```

---

## 25A Fuse

Status:

```text
PASS
```

---

## AWG16 Servo Rail

Status:

```text
PASS
```

---

## Samsung 30Q

Status:

```text
PASS
```

---

## Single Buck

Status:

```text
ACCEPTABLE FOR ALPHA
```

---

建议：

```text
V6 Beta

升级双Buck结构
```

---

# 18. Freeze Summary

## Battery

```text
Samsung 30Q

3S2P

6000mAh
```

---

## Servo Rail

```text
DROK 20A Buck

7.4V
```

---

## Logic Rail

```text
MP1584EN

5V
```

---

## Soft Start MOSFET

```text
IRLZ44N
```

---

## Reverse Protection

```text
IRF4905
```

---

## Fuse

```text
ATO 25A Slow Blow
```

---

## Connector

```text
Amass XT30U
```

---

## Switch

```text
MTS-102
```

---

## Wiring

```text
AWG16
AWG18
AWG20
AWG24
```

---

Status:

```text
APPROVED

READY FOR EDS-05
```
