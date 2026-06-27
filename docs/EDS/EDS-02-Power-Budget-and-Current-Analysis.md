# Mini-Atlas V6 Alpha

# EDS-02 Power Budget & Current Analysis

Version: 1.0 Freeze A

Status: APPROVED

---

# 1. Purpose

本文件用于冻结：

- Power Budget（功耗预算）
- Current Budget（电流预算）
- Battery Runtime（续航估算）
- Peak Current Analysis（峰值电流分析）
- Wire Gauge Selection（线径选择）
- Thermal Budget（热预算）
- Battery Sag Analysis（电压跌落分析）

本文件是：

```text
Servo Rail
Battery Pack
Buck Converter
Fuse
Wire Harness
```

设计依据。

---

# 2. Design Philosophy

V6 Alpha 采用：

```text
Typical Current Design

典型工况设计
```

而非：

```text
Worst Case Stall Current Design

堵转极限设计
```

原因：

机器人正常工作时：

- 舵机不会长期堵转
- 轮电机不会持续堵转
- 峰值持续时间通常小于 500ms

因此：

```text
典型电流
+
合理峰值余量
```

比纯堵转设计更合理。

---

# 3. Electrical Domains

系统划分为：

## Servo Domain

负责：

```text
Hip Roll
Hip Pitch
Knee
```

供电：

```text
7.4V
```

---

> **ECO-002 变更**：Ankle 已移除（DR-011），舵机域仅包含 Hip Roll / Hip Pitch / Knee。

---

## Logic Domain

负责：

```text
ESP32

IMU

Status LED
```

供电：

```text
5V
```

---

## Wheel Domain

负责：

```text
Left Wheel

Right Wheel
```

供电：

```text
11.1V
```

---

# 4. Servo Configuration

## STS3046

数量：

```text
6
```

用于：

```text
Hip Roll L/R

Hip Pitch L/R

Knee L/R
```

---

> **ECO-002 变更**：Ankle/STS3215 章节已删除（DR-011 移除踝关节）。

# 5. STS3046 Current Model

## Datasheet Reference

工作电压：

```text
6V~12V
```

---

额定：

```text
7.4V
```

---

经验数据：

| State | Current |
|---------|---------:|
| Idle | 80mA |
| Holding | 400mA |
| Walking | 1.0A |
| Aggressive Motion | 1.5A |
| Stall | 4.5A |

---

## Design Current

冻结：

```text
1.0A Typical
```

---

总计：

```text
6 × 1.0A

= 6A
```

---

> **ECO-002 变更**：STS3215 Current Model 章节已删除（DR-011 移除踝关节）。

# 7. Servo Rail Analysis

## Typical Current

```text
STS3046

6A
```

---

> **ECO-002 变更**：STS3215 已删除（DR-011 移除踝关节），Servo Rail Typical 从 7.4A 降为 6.0A。

## Dynamic Peak

假设：

```text
6个关节同时大负载
```

---

估算：

```text
10A
```

---

## Extreme Peak

短时：

```text
12A
```

---

冻结：

| Parameter | Value |
|------------|------------|
| Typical | 6.5A |
| Peak | 12A |
| Design Margin | 20A |

---

# 8. Wheel Motor Current Model

## GB37-520

假设：

```text
12V 150RPM
```

型号。

---

经验数据：

| State | Current |
|---------|---------:|
| No Load | 150mA |
| Cruise | 800mA |
| Acceleration | 1.5A |
| Stall | 4A |

---

数量：

```text
2
```

---

## Typical Current

```text
0.8A × 2

= 1.6A
```

---

## Peak Current

```text
1.5A × 2

= 3A
```

---

冻结：

| Parameter | Value |
|------------|------------|
| Typical | 1.6A |
| Peak | 3A |

---

# 9. Logic Domain Current

## ESP32

| State | Current |
|---------|---------:|
| Idle | 80mA |
| WiFi Active | 240mA |

---

冻结：

```text
250mA
```

---

## ICM42688

```text
3mA
```

---

## LED + Misc

```text
50mA
```

---

## Total

```text
303mA
```

---

冻结：

```text
500mA Budget
```

---

# 10. Total System Current

## Typical

Servo:

```text
6.0A
```

Wheel:

```text
1.6A
```

Logic:

```text
0.5A
```

---

总计：

```text
8.1A
```

---

## Peak

Servo:

```text
12A
```

Wheel:

```text
3A
```

Logic:

```text
0.5A
```

---

总计：

```text
15.5A
```

---

冻结：

| Parameter | Value |
|------------|------------|
| Typical | 8.1A |
| Peak | 15.5A |

---

# 11. Power Budget

## Battery Voltage

标称：

```text
11.1V
```

---

## Typical Power

```text
11.1V × 8.1A

= 90W
```

---

## Peak Power

```text
11.1V × 15.5A

= 172W
```

---

冻结：

| Parameter | Value |
|------------|------------|
| Typical | 90W |
| Peak | 172W |

---

# 12. Battery Pack

## Configuration

冻结：

```text
3S2P
```

---

电芯：

```text
Samsung 30Q
```

---

参数：

```text
3000mAh
```

---

总容量：

```text
3000mAh
```

---

总能量：

```text
33.3Wh
```

---

> **ECO-002 变更**：电池容量由 6000mAh/66Wh 修正为 3000mAh/33.3Wh（3S2P 串联不倍增容量）。

---

# 13. Runtime Analysis

## Walking Mode

功耗：

```text
90W
```

---

续航：

```text
33.3Wh / 90W

≈ 0.37h
```

---

即：

```text
22分钟
```

---

## Mixed Usage

假设：

- 50% 移动
- 50% 站立

平均功耗：

```text
52W
```

---

续航：

```text
33.3Wh / 52W

≈ 0.64h
```

---

即：

```text
38分钟
```

---

冻结：

| Mode | Runtime |
|---------|---------|
| Walking | 20~25 min |
| Mixed | 35~40 min |

---

# 14. Battery Sag Analysis

## 30Q Internal Resistance

约：

```text
15mΩ
```

---

3S2P：

```text
22mΩ
```

---

典型电流：

```text
8A
```

---

压降：


::contentReference[oaicite:0]{index=0}


```text
0.18V
```

---

峰值：

```text
15A
```

---

压降：

```text
0.33V
```

---

结论：

```text
完全可接受
```

---

# 15. Wire Gauge Selection

## Battery

冻结：

```text
AWG18 Silicone
```

---

持续能力：

```text
16A+
```

---

## Servo Rail

冻结：

```text
AWG16 Silicone
```

---

持续能力：

```text
22A+
```

---

## Wheel Rail

冻结：

```text
AWG20 Silicone
```

---

## Logic Rail

冻结：

```text
AWG24 Silicone
```

---

# 16. Thermal Budget

## Servo Buck

输出：

```text
7.4V
```

---

输入：

```text
11.1V
```

---

效率：

```text
90%
```

---

负载：

```text
44W
```

---

损耗：

```text
5W
```

---

要求：

```text
必须安装散热片
```

---

## ESP32

发热：

```text
<2W
```

---

无需额外散热。

---

# 17. Safety Margin Analysis

## Servo Rail Margin

设计：

```text
20A
```

---

实际：

```text
12A Peak
```

---

余量：

```text
40%
```

---

符合要求。

---

## Battery Margin

设计：

```text
30A+
```

---

实际：

```text
15.5A Peak
```

---

余量：

```text
~50%
```

---

符合要求。

---

# 18. Freeze Summary

## Servo Rail

```text
7.4V

6.5A Typical

12A Peak
```

---

## Wheel Rail

```text
11.1V

1.6A Typical

3A Peak
```

---

## Logic Rail

```text
5V

0.5A Budget
```

---

## Total System

```text
8.1A Typical

15.5A Peak
```

---

## Battery

```text
3S2P Samsung 30Q

33.3Wh
```

---

## Runtime

```text
Walking

20~25 Minutes

Mixed Use

35~40 Minutes
```

---

Status:

```text
APPROVED

READY FOR EDS-03
```